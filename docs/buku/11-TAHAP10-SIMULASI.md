# TAHAP 10 — SIMULASI DAN VALIDASI

*Tahap ini OPSIONAL. Berguna kalau dipakai benar, membuang waktu kalau dipakai salah.*

---

## 1. Kapan simulasi berguna dan kapan tidak

### 1.1 Alat yang tepat untuk pertanyaan yang tepat

| Pertanyaan | Alat |
|---|---|
| Panjang runner, panjang header, volume plenum | **simulasi 1D** atau perhitungan gelombang (Tahap 7) |
| Diameter throttle body, CSA port | **perhitungan** (Tahap 3) |
| Radius short-turn mana yang lebih baik | **CFD 3D** |
| Bentuk penampang bundar vs oval | **CFD 3D** |
| Di mana aliran lepas di dalam port | **CFD 3D** |
| Berapa HP yang dihasilkan | **dyno** — bukan simulasi |

**Alur kerja yang benar:**
```
perhitungan 1D → dimensi utama
CFD 3D         → menghaluskan bentuk
flowbench      → validasi head
dyno           → validasi mesin
lintasan       → validasi keseluruhan
```

### 1.2 Aturan emasnya

> **CFD kuat untuk MEMBANDINGKAN, lemah untuk memprediksi angka mutlak tanpa kalibrasi.**

Kalau CFD bilang bellmouth R8 lebih baik 4% daripada R5 — percaya arahnya.
Kalau CFD bilang "tenaga 18,3 HP" — jangan percaya.

### 1.3 Akurasi yang realistis

| Kasus | Akurasi absolut |
|---|---|
| Flow port head (steady, vs flowbench) | ±3–8% |
| Koefisien flow throttle body / stack | ±5% |
| Pressure drop plenum & airbox | ±5–10% |
| Tumble / swirl ratio | ±10–15% |
| Panjang runner optimal | **buruk** — salah alat |
| Prediksi HP absolut | **buruk** |

---

## 2. Cara kerja CFD

### 2.1 Alurnya

**1. Geometri** — ambil volume **fluida**, bukan bendanya. Untuk port, artinya rongga dari mulut manifold sampai keluar throat.

**2. Meshing** — potong volume jadi jutaan sel. Di dinding wajib ada lapisan prisma (8–15 lapis) karena di situlah rugi gesekan dan separasi terjadi.

**3. Solver** — tiap sel menyelesaikan persamaan Navier-Stokes secara iteratif sampai residual turun.

**4. Model turbulensi** — aliran nyata turbulen dan mustahil dihitung penuh, jadi dimodelkan. k-ω SST paling umum untuk saluran.

**5. Boundary condition** — ini yang paling sering bikin hasil ngaco.

**6. Post-processing** — mass flow, koefisien flow, peta kecepatan, zona separasi.

---

## 3. Menyiapkan flowbench virtual

### 3.1 Susunan yang benar

```
plenum setengah bola  →  mulut port di bidang datar  →  port  →  keluar throat
   (tekanan total)            (dinding/flange)                (tekanan statik 0)
```

**Plenum harus setengah bola berpusat di mulut port**, dipotong tepat di bidang mulut. Bidang datar di sekelilingnya jadi muka flange (dinding). Dengan begini batas masuk berjarak sama ke segala arah dan aliran masuk dari reservoir yang benar-benar tenang.

Radius plenum minimal **3× diameter port**.

### 3.2 Depresi yang dipakai

Jalankan di **10"H₂O**, bukan 28".

**Alasannya dua-duanya nyata:**
- Di 28" kecepatan throat ~107 m/s = Mach 0,31 — terlalu tinggi untuk solver *incompressible*
- Di 10" jadi ~64 m/s = Mach 0,19, jauh lebih sah
- Start dingin dengan beda tekanan besar sering bikin solver diverge

**Konversi ke depresi acuan** pakai akar rasio tekanan — ini praktik baku flowbench:
```
CFM_28 = CFM_10 × √(28/10)
```

Sah karena pada Re > 10⁵ koefisien flow praktis tidak tergantung Re.

### 3.3 Model satu cabang

Port 4 valve bercabang simetris terhadap sekat pemisah. Modelkan **satu cabang saja** dengan bidang simetri di sekat: satu cabang membawa separuh aliran dan separuh CSA.

Yang hilang cuma rugi di ujung sekat — dan itu sama untuk semua varian, jadi tidak menggeser peringkat.

### 3.4 Setelan numerik

| Parameter | Nilai |
|---|---|
| Solver | steady, incompressible |
| Turbulensi | k-ω SST |
| Skema konveksi U | bounded linearUpwind |
| Algoritma | SIMPLE baku (bukan SIMPLEC) |
| Relaksasi | p 0,3 / U 0,7 |
| Iterasi | 3000 |
| Lapisan prisma | 6 lapis, ekspansi 1,2 |

SIMPLEC dengan relaksasi 0,9 diverge dari start dingin. Jangan dinaikkan tanpa alasan.

### 3.5 Refinement volume, bukan cuma permukaan

Ini krusial dan mudah terlewat.

Pengaturan refinement permukaan hanya menghaluskan **permukaan**. Dinding port dapat sel halus dan lapisan prisma rapi, tapi **inti port** — tempat aliran utama lewat — bisa tertinggal di sel background yang kasar.

**Solusinya:** buat STL kedua berisi volume port saja, pakai sebagai refinement region mode *inside*.

---

## 4. Jebakan yang mahal

Bagian ini adalah yang paling berharga dari seluruh bab. Semua yang tertulis di sini ditemukan dengan cara mahal.

### 4.1 Aturan yang paling penting

> **Jalankan kasus berjawaban pasti LEBIH DULU, bukan terakhir.**

Pipa bundar lurus dengan boundary condition yang sama **harus** memberi Cf 0,85–0,95. Kalau tidak, setup-mu yang salah — bukan geometri yang sedang kamu pelajari.

Dalam pengembangan metode ini, **sebelas kasus port dijalankan dan dianalisis** sebelum pemeriksaan itu dilakukan. Semuanya tidak berlaku. Saat pipa lurus akhirnya dijalankan, hasilnya Cf 0,387 — langsung menunjuk ke setup, bukan ke geometri port yang sudah dituduh empat hipotesis berturut-turut.

### 4.2 Diagnostik numerik tidak menangkap apa pun

Selama sebelas kasus yang salah itu, **semua indikator hijau**:

| Diagnostik | Status |
|---|---|
| Pemeriksaan mesh | "Mesh OK" |
| Ketimpangan massa | 0,000–0,004% |
| Residual | turun 4 dekade |
| Rasio viskositas turbulen | normal |

Yang akhirnya menangkap bug:

1. **Nilai Cf yang tidak masuk akal secara fisika**
2. **Melihat medan dengan TANDA kecepatan aksial**, bukan besarnya

Poin kedua layak digarisbawahi. Selama hanya besar kecepatan yang dilihat, **aliran balik −15,7 m/s di tengah port terbaca sebagai "aliran lambat"**. Begitu tandanya dibuka, penyumbatnya langsung terlihat.

> **Keseimbangan massa 0,000% bukan bukti hasilnya benar. Itu cuma bukti mesh-nya tidak bocor.**

### 4.3 Daftar bug dan penjaganya

**Bug 1 — Pusat tutup tidak sebidang dengan cincinnya**

Saat bellmouth ditambahkan ke model, cincin penampang pertama pindah ke hulu tapi pusat tutupnya tidak ikut. Tutup mulut port jadi **kerucut yang menyumbat**.

Ini yang paling merusak: ia membuat **setiap perbaikan yang benar tampak memperburuk keadaan**. Memperbaiki plenum justru menurunkan Cf dari 0,566 ke 0,217, karena plenum lama kebetulan menelan kerucut itu.

*Penjaga:* pusat tutup wajib sebidang dengan cincin yang ditutupnya, toleransi 0,001 mm.

**Bug 2 — Klasifikasi patch outlet dengan uji jarak sederhana**

Cakram keluar throat tegak lurus **sumbu valve** yang miring 13°, jadi uji terhadap sumbu vertikal hanya menangkap pita tipis; sisa cakram jadi dinding yang menyumbat throat.

*Penjaga:* klasifikasi pakai arah normal segitiga, dan luas patch outlet wajib ±10% luas throat.

**Bug 3 — Plenum berupa bola yang digeser ke depan mulut**

Permukaannya cuma 5 mm dari mulut port. **62% aliran masuk lewat 0,42% luas patch pada 72 m/s** — itu jet, bukan plenum.

*Penjaga:* luas patch inlet wajib ±20% dari luas setengah bola.

**Bug 4 — Bidang flange mewarisi refinement dinding**

Mesh membengkak 123 ribu → 615 ribu sel, waktu jalan 82 menit per kasus.

*Penjaga:* beri bidang flange region sendiri di level rendah.

**Bug 5 — Mask plot yang terlalu ketat**

Membuang segitiga bersisi > 3 mm padahal sel background 5 mm punya diagonal 8,7 mm — menciptakan "lubang" palsu yang mudah disalahartikan sebagai cacat mesh.

*Penjaga:* ambang mask harus di atas diagonal sel terkasar.

### 4.4 Hasil setelah semua diperbaiki

| Kasus | Cf | K |
|---|---|---|
| Pipa lurus (acuan berjawaban pasti) | **0,879** | 0,295 |
| Port bengkok 37° | **0,849** | 0,387 |

**Ongkos tikungan cuma 3,4%.**

Ini temuan desain yang penting: dengan short-turn radius yang wajar, **port bukan pembatasnya**. Cf 0,849 adalah plafon port telanjang; head lengkap dengan valve di lift 9 mm akan turun ke 0,55–0,65.

Artinya usaha menggerus bentuk port memberi hasil kecil dibandingkan **membesarkan throat**.

---

## 5. Validasi

### 5.1 Rantai validasi

Tiap tahap memvalidasi tahap sebelumnya:

| Tahap | Memvalidasi | Toleransi wajar |
|---|---|---|
| Perhitungan | — | — |
| CFD | perbandingan bentuk | ±5% relatif |
| Flowbench | Cf head | ±5% |
| Dyno | tenaga mesin | ±3% antar run |
| Lintasan | keseluruhan sistem | ±0,2 detik |

### 5.2 Kalibrasi ulang

Setelah punya hasil nyata, **kembalikan ke perhitungan**:

1. Bandingkan CFM terukur di flowbench dengan CFM terhitung → dapat Cf sebenarnya
2. Bandingkan HP dyno dengan CFM terukur → dapat faktor HP/CFM sebenarnya
3. Bandingkan waktu lintasan dengan HP dyno → dapat rugi drivetrain sebenarnya

Setelah tiga angka itu diketahui, perhitunganmu untuk build berikutnya jauh lebih dipercaya.

**Ini yang membuat pembuat mesin berpengalaman lebih akurat** — bukan karena mereka tahu rumus yang berbeda, tapi karena rumus mereka sudah dikalibrasi ke pekerjaan mereka sendiri.

### 5.3 Yang harus dicatat tiap build

- [ ] Semua dimensi terukur (bukan yang direncanakan)
- [ ] Cf flowbench kalau ada
- [ ] Grafik dyno lengkap dengan kondisi cuaca
- [ ] Setelan CVT final
- [ ] Waktu dan trap lintasan
- [ ] Kondisi part setelah beberapa run (spark plug, piston, ring)

Catatan ini adalah **aset paling berharga** yang kamu bangun. Nilainya melebihi mesin itu sendiri.

---

## 6. Ringkasan Tahap 10

1. **CFD untuk bentuk, 1D untuk panjang, dyno untuk tenaga.** Jangan tertukar.
2. **CFD kuat membandingkan, lemah memprediksi angka mutlak.**
3. **Jalankan kasus berjawaban pasti lebih dulu.** Ini aturan yang paling mahal kalau dilanggar.
4. **Diagnostik numerik yang hijau bukan bukti hasilnya benar.**
5. **Lihat tanda kecepatan, bukan cuma besarnya.** Aliran balik terbaca sebagai "lambat".
6. **Periksa kewarasan fisika** — nilai di luar rentang wajar berarti ada yang salah secara struktural.
7. **Kalibrasi ulang perhitunganmu** dengan hasil nyata setelah tiap build.
8. **Catatan build adalah aset paling berharga.**

---

*Ini tahap terakhir. Lanjut ke Lampiran untuk rumus ringkas, daftar perkakas, dan daftar periksa.*
