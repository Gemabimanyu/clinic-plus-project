# TAHAP 11 — KALIBRASI: MEMBACA MESIN NYATA

*Semua tahap sebelumnya mengajarkan cara MENGHITUNG. Tahap ini mengajarkan cara MEMBACA — mengubah data lapangan yang berantakan (cam card tidak lengkap, dyno chassis, spek "standar" yang tidak jelas) jadi angka yang bisa dipercaya.*

---

## 1. Kenapa tahap ini ada

Rumus-rumus di buku ini butuh input yang bersih: durasi cam, throat, Vd, rpm. Di dunia nyata, input itu jarang datang bersih. Yang datang biasanya:

- Cam card cuma nyebut durasi dan "overlap sekian derajat" — tanpa jelas overlap itu diukur dari mana
- Dyno chassis kasih angka HP di rpm tertentu — tapi tidak bilang itu di roda atau di crank
- "Klep standar" — tanpa ukuran pasti
- Dua sumber data yang saling bertentangan

Tahap ini adalah kumpulan teknik buat menangani situasi itu — semuanya diuji lewat kasus nyata, bukan teori.

---

## 2. Membaca cam card dari data yang tidak lengkap

### 2.1 Masalahnya

Cam card sering cuma kasih sebagian info: durasi, mungkin "overlap", mungkin IVC/EVO kira-kira. Kalau angka-angka itu tidak konsisten satu sama lain, harus ada cara memilah mana yang salah.

### 2.2 Tiga cara mengukur overlap — dan cuma satu yang benar-benar overlap

**Kesalahan paling umum:** mengira "overlap" itu satu angka yang bisa didapat dengan berbagai cara pengukuran, padahal ada tiga hal berbeda yang sering tertukar namanya:

| Yang diukur | Sebenarnya apa |
|---|---|
| Sudut crank dari IVO ke TDC + EVC dari TDC | **Overlap sesungguhnya** (derajat) |
| Lift valve isap dan buang saat piston di TDC | **Bukan overlap** — ini lift di titik overlap, satuan mm bukan derajat |
| Estimasi kasar dari ingatan/feeling | Rentan salah, jangan dipakai untuk hitungan presisi |

**Kasus nyata:** sebuah cam disebut "durasi 259°, overlap 2,3" (dikira 23°). Belakangan diketahui "2,3" itu sebenarnya lift di TDC (2,4mm masing-masing sisi), bukan sudut sama sekali. Dua angka ini **tidak bisa dipertukarkan** — satu dalam derajat, satu dalam milimeter.

### 2.3 Menguak IVO/EVC dari lift di TDC

Kalau yang diketahui adalah **lift di TDC** (bukan sudut), baliknya rumus profil harmonik (Tahap 4):

```
lift(θ) = lift_maks × sin²(π × θ / durasi)

θ = (durasi / π) × arcsin(√(lift_TDC / lift_maks))
```

dengan `θ` = IVO (untuk valve isap) atau EVC (untuk valve buang).

**Validasi metode ini ke data yang sudah diketahui benar** (Mesin Contoh A, IVO 38° BTDC, lift maks 10,8mm, durasi 281°):
```
lift_TDC = 10,8 × sin²(π × 38/281) = 1,837 mm
```
Buku menyebut nilai ini **1,83 mm** — cocok. Metode ini bisa dipercaya.

### 2.4 Kalau dua metode kasih hasil beda jauh — curigai profil non-harmonik

Pada satu kasus nyata, lift-TDC 2,4mm/2,4mm memberi LSA hasil hitung **86°** — jauh di luar rentang wajar buku (paling ketat 98–104°). Sementara sumber lain untuk cam yang sama menyebut **LSA 104°**, dan itu konsisten dengan IVC/EVO yang disebut terpisah (~54°).

**Kesimpulannya:** rumus harmonik `sin²` adalah **pendekatan**, bukan potret cam sesungguhnya. Cam performa sering punya ramp yang lebih agresif di awal buka/tutup dibanding kurva harmonik murni — sehingga lift di TDC bisa lebih tinggi dari yang diprediksi harmonik pada sudut yang sama.

> **Aturan praktis:** kalau ada dua sumber data yang saling bertentangan, dan salah satunya (LSA/ICL/IVC) konsisten secara internal dengan durasi yang diketahui sementara yang lain (lift-TDC via harmonik) menghasilkan angka di luar rentang wajar buku manapun — percayai yang konsisten secara internal. Model harmonik berguna untuk validasi kasar, bukan sebagai sumber kebenaran mutlak.

### 2.5 Cara cepat mengunci cam card dari LSA + durasi

Kalau LSA sudah diketahui pasti (dari pembuat cam, paling bisa dipercaya karena itu properti fisik cam yang tidak berubah), dan cam simetris (durasi in = durasi ex):

```
IVO = EVC = durasi/2 − LSA
IVC = EVO = durasi − 180 − IVO
overlap = IVO + EVC
```

Ini cara **paling sedikit asumsi** — LSA adalah properti tergerinda di cam (tidak berubah pemasangan), jadi kalau sumbernya kredibel, pakai ini sebagai jangkar utama.

---

## 3. Memprediksi rpm peak power dari spesifikasi

### 3.1 Membalik rumus time-area

Rumus durasi dari Tahap 4:
```
durasi_baru = durasi_acuan × (A_thr_acuan/A_thr_baru) × (Vd_baru/Vd_acuan) × (rpm_baru/rpm_acuan)
```

Kalau yang ingin dicari adalah **rpm** (bukan durasi) — karena durasi, valve, dan Vd sudah diketahui dari spek mesin yang mau dianalisis — tinggal dibalik:

```
rpm_baru = rpm_acuan × (durasi_baru/durasi_acuan) × (A_thr_baru/A_thr_acuan) × (Vd_acuan/Vd_baru)
```

**Ini alat paling berguna di tahap ini**: dari spek cam + valve + kapasitas suatu mesin, bisa diperkirakan di rpm berapa mesin itu "match" — titik di mana durasi cam dan luas throat bekerja sama secara optimal.

### 3.2 Kasus tervalidasi

Mesin dengan bore 66mm, valve isap 2×23mm (3 valve), durasi 259°, dihitung dengan metode ini terhadap acuan Mesin Contoh A:

```
rpm prediksi = 10.087 rpm
rpm real di dyno = 10.200 rpm
selisih = 1,1%
```

**Selisih 1,1% ini bagus sekali** untuk metode yang cuma butuh data geometri, tanpa CFD atau flowbench. Ini bukan jaminan akurasi segini selalu terjadi — tapi menunjukkan metodenya valid kalau asumsi rasio throat/valve-nya masuk akal (di kasus ini dipakai 0,935, seagresif Mesin Contoh A).

### 3.3 Throat tidak selalu diketahui — pakai rentang, bukan angka tunggal

Kalau cuma diameter valve yang diketahui (bukan throat aktual), jangan paksa satu angka. Hitung rentang dari beberapa asumsi rasio throat/valve (0,86 konservatif sampai 0,935 agresif) dan laporkan **rentang rpm**, bukan angka tunggal palsu presisi.

| Rasio throat/valve | Karakter |
|---|---|
| 0,86–0,90 | konservatif, OEM/harian |
| 0,90–0,92 | balap lazim |
| 0,935 | agresif, terbukti Mesin Contoh A |

---

## 4. Jangan pinjam acuan dari mesin yang terlalu beda — pakai data mesin itu sendiri kalau ada

### 4.1 Kesalahan yang terjadi

Untuk mesin besar (bore 76mm, stroke 76mm, 345cc, arsitektur touring/matic harian), rpm ideal awalnya dihitung dengan meminjam acuan dari Mesin Contoh A (drag kecil, 199,5cc, sangat berbeda karakter penggunaan). Hasilnya: **8.408 rpm**.

Setelah ada data dyno asli untuk mesin itu sendiri (40,5 HP @ 6.500 rpm dengan durasi 260°), perhitungan yang sama diulang — tapi sekarang **mesin itu sendiri** dipakai sebagai acuan (bukan Mesin Contoh A):

```
rpm_baru = rpm_sekarang × (durasi_baru/durasi_sekarang)
         = 6.500 × (280/260) = 7.000 rpm
```

**Selisihnya 1.400 rpm** (8.408 vs 7.000) — cukup besar untuk mengubah keputusan desain valve spring, rasio CVT, dan target kompresi.

### 4.2 Kenapa ini terjadi

Meminjam acuan dari mesin lain membawa serta **semua karakter mesin itu** — rod ratio, kualitas porting, budaya tuning (drag murni vs harian), bahkan asumsi implisit yang tidak terlihat di angka. Semakin jauh karakter mesin acuan dari mesin yang dianalisis, semakin besar potensi melesetnya.

> **Aturan urutan kepercayaan acuan, dari terbaik ke terlemah:**
> 1. **Data mesin itu sendiri** (measured langsung) — paling kuat, tidak ada asumsi lintas-mesin
> 2. **Mesin dengan arsitektur & displacement mirip** (bore/stroke/valve count serupa)
> 3. **Mesin manapun yang tersedia datanya** — dipakai kalau tidak ada pilihan lain, tapi kasih rentang lebar dan tandai eksplisit sebagai asumsi lemah

Begitu ada satu titik data real untuk suatu mesin — **buang acuan lama, pakai data sendiri**. Ini variasi dari prinsip Tahap 10: "kalibrasi ulang perhitunganmu dengan hasil nyata."

---

## 5. Mengecek kecukupan throttle body dari spesifikasi

### 5.1 Rumus

```
Q_rata2  = Vd × (rpm/60) / 2 × VE
duty     = durasi_isap / 720
Q_puncak = Q_rata2 / duty × (π/2)
v_di_TB  = Q_puncak / (A_TB × (1 − blokade_poros))
```

### 5.2 Contoh: TB 36mm pada mesin 345cc

Di 6.500 rpm dengan VE diasumsikan 0,90: kecepatan di TB 36mm dihitung **~77 m/s**. Dibandingkan Mesin Contoh A yang terbukti nyaman di 61 m/s, ini sudah masuk zona "sangat agresif" — indikasi TB mulai membatasi.

**Peringatan penting:** cek ini HARUS dilakukan sebelum menyalahkan cam atau valve kalau tenaga mentok. TB yang terlalu kecil menghasilkan gejala yang mirip dengan cam salah durasi (tenaga mendatar sebelum rpm sasaran) — tapi solusinya beda total.

---

## 6. Crank HP vs Wheel HP — kesalahan yang paling mudah terjadi dan paling merusak kesimpulan

### 6.1 Masalahnya

Semua rumus tenaga di buku ini (`Tenaga ≈ CFM × 0,43–0,50`) menghitung **tenaga di crankshaft**. Tapi dyno yang paling umum dipakai untuk motor matic adalah **dyno chassis** (dyno roda) — dan angka yang keluar dari situ adalah **WHP (Wheel Horsepower)**, sudah dipotong rugi CVT, final drive, dan ban.

> **Kalau angka dyno langsung dimasukkan ke rumus yang mengasumsikan crank power, semua kesimpulan turunan darinya akan meleset — termasuk Cf efektif yang tampak jauh lebih buruk dari kenyataan.**

### 6.2 Cara mengenali jenis dyno dari spesifikasinya

| Ciri | Jenis dyno | Yang terukur |
|---|---|---|
| Ada **roller** dengan diameter tertentu, motor naik di atasnya | **Dyno chassis (inersia atau brake)** | **WHP** |
| Motor terhubung langsung ke dyno lewat crankshaft/kopling, tanpa roda | **Dyno mesin** | **Crank HP** |
| Disebut "dyno inersia [merek]" dengan angka inersia roller (kg·m²) | **Dyno chassis inersia** | **WHP** |

Untuk motor matic, dyno chassis jauh lebih umum (lebih murah, tidak perlu lepas mesin) — jadi **asumsikan WHP kecuali dinyatakan sebaliknya**.

### 6.3 Konversi WHP ke crank HP

```
HP_crank = WHP / (1 − rugi_drivetrain)
```

Rugi drivetrain pada CVT (Tahap 9, bagian 6): **10–30%**, tergantung kondisi belt, pulley, dan final gear.

| Rugi diasumsikan | Kondisi |
|---|---|
| 10% | CVT terawat sangat baik |
| 20% | tengah, umum |
| 30% | CVT kurang terawat / belt aus |

### 6.4 Kasus nyata — kesalahan yang terjadi dan bagaimana ditemukan

Dyno chassis (roller 267mm, inersia 3,3 kg·m² — ciri dyno chassis inersia) mencatat **40,5 HP @ 6.500 rpm** untuk suatu mesin 345cc. Angka ini langsung dipakai dalam rumus `Tenaga ≈ CFM × 0,43–0,50` seolah-olah itu crank power.

Hasilnya: **Cf efektif sistem dihitung cuma 0,37–0,43** — jauh di bawah bahkan "standar pabrikan" (0,55). Kesimpulan yang ditarik: throttle body pasti sangat mencekik.

**Setelah dikoreksi** (WHP 40,5 dianggap sudah dipotong rugi drivetrain 20%):
```
HP_crank = 40,5 / (1 − 0,20) = 50,6 HP
```
Cf efektif dihitung ulang: **0,47–0,54** — mendekati "standar pabrikan", masuk akal.

**Pelajarannya:** kesimpulan "TB sangat mencekik" ternyata sebagian besar cuma salah unit, bukan murni masalah mekanis. TB tetap layak diperiksa (kecepatan 77 m/s tetap tinggi), tapi tingkat keparahannya jauh lebih ringan dari kesimpulan awal yang salah unit.

### 6.5 Yang TIDAK terpengaruh oleh kesalahan unit ini

Prediksi **rpm** peak power (bagian 3) tidak memakai HP sama sekali dalam rumusnya — cuma durasi, throat, Vd, dan rpm acuan. Jadi validasi rpm (bagian 3.2) tetap sah walau ada kesalahan unit HP di analisis lain. **Selalu periksa rumus mana yang benar-benar dipakai** sebelum menyimpulkan satu kesalahan merusak seluruh analisis.

---

## 7. Studi kasus: mendiagnosis efek plenum dan piping dari rasa berkendara

*Rasa di jok — bukan cuma angka dyno — adalah data. Bagian ini menunjukkan cara menerjemahkan laporan kualitatif jadi angka yang bisa dihitung, memakai rumus gelombang dari Tahap 7.*

### 7.1 Laporan yang jadi bahan kasus

Mesin 345cc (bore 76, stroke 76), panjang valve→TB 250mm, piping TB→plenum 240mm, TB 36mm, pipa dari TB ke plenum 42,5mm. Laporan pengendara:

- **Dengan box+piping terpasang:** tenaga terasa "flat" — narik terus dari bawah tanpa lubang.
- **Box+piping dilepas:** low-to-mid turun dan TB "ngorok"; mid sedikit turun tanpa ngorok; mid-high sangat enak dan rpm naik lebih cepat; tapi "jambakan" (sentakan torsi) kurang terasa.

### 7.2 Panjang efektif menentukan titik tertala, bukan cuma "ada box atau tidak"

Titik pantul gelombang tekanan (Tahap 7 §2.1) ada di **ujung terbuka** saluran isap. Melepas box+piping tidak cuma "menghilangkan komponen" — itu **memindahkan ujung terbuka** dari mulut plenum ke mulut TB, memendekkan panjang efektif dari 490mm menjadi 250mm.

```
rpm_tertala = c × durasi / (12 × n × L)
```

| Konfigurasi | L | h2 | h3 | h4 | h5 |
|---|---|---|---|---|---|
| Dengan box+piping | 490mm | 7.893 | 5.262 | 3.946 | 3.157 |
| Tanpa box+piping | 250mm | 15.470 | 10.313 | 7.735 | 6.188 |

(durasi 260°, c = 357 m/s @45°C dalam saluran)

**Mencocokkan ke laporan:** dengan box, h3 (**~5.260 rpm**) jatuh di low-mid — cocok dengan "flat, narik dari bawah". Tanpa box, dukungan bergeser ke h4–h5 (**~6.200–7.700 rpm**) — cocok dengan "low-mid turun, mid-high sangat enak". **Ini bukan kebetulan** — panjang efektif yang berubah adalah penyebab langsung pergeseran karakter yang dirasakan.

### 7.3 Kenapa "ngorok" cuma muncul di satu sisi, dan kenapa "jambakan" berkurang

**Ngorok tanpa box:** plenum bukan cuma titik pantul gelombang — dia juga peredam pulsa tekanan mentah (termasuk balik dari overlap) sebelum keluar ke udara terbuka. Tanpa itu, pulsa keluar mentah lewat mulut TB yang sempit (36mm, lihat bagian 5) — itu sumber suaranya.

**Jambakan berkurang meski mid-high enak:** harmonik lebih tinggi (h4/h5) secara konsisten memberi penguatan lebih lemah dan lebih halus daripada harmonik rendah (h2/h3) pada sistem nyata (tidak ideal/lossy). RPM naik dan tenaga di sana baik, tapi kenaikannya lebih landai — bukan lonjakan tajam.

> **Pelajaran umum:** modifikasi yang "menghilangkan pembatas" tidak selalu berarti "menghilangkan sesuatu yang buruk". Kadang yang dihilangkan justru komponen yang sedang bekerja sebagai alat tuning aktif — dan hasilnya adalah pertukaran karakter, bukan perbaikan murni.

### 7.4 Mengukur rugi dari step diameter dengan Borda-Carnot

Sambungan TB (36mm) ke pipa plenum (42,5mm) adalah **pelebaran mendadak** — pola yang Tahap 7 §3.3 larang secara kualitatif ("JANGAN ada pelebaran di tengah jalan"). Untuk mengukur seberapa besar, buku ini menambahkan satu rumus di luar tabel K yang sudah ada (Kamus Istilah, Kelompok K):

```
K_pelebaran_mendadak = (1 − A_kecil/A_besar)²
```

Rumus ini (Borda-Carnot) melengkapi tabel K yang sudah ada — dipakai khusus untuk **step diameter di tengah saluran**, beda dari kasus mulut/ujung terbuka yang sudah ditabelkan.

**Diterapkan ke kasus ini:**
```
A_TB/A_pipa = (36/42,5)² = 0,718
K = (1 − 0,718)² = 0,080
```

Setelah dihaluskan (taper landai): **K turun ke ~0,012–0,024**.

**Tapi periksa skalanya sebelum menyimpulkan ini penting:**

| | Rugi tekanan @5.260 rpm |
|---|---|
| Step sekarang | 162 Pa |
| Setelah dihaluskan | 24–49 Pa |
| **Selisih** | **~113–138 Pa** |

113–138 Pa itu **~0,12% dari tekanan atmosfer** — diterjemahkan ke tenaga, sekitar **0,1–0,15% gain**. Jauh di bawah ambang yang bisa dirasakan (2–5%, Tahap 1). Sebagai pembanding, rugi TB itu sendiri (butterfly WOT, K=0,25) di kecepatan yang sama adalah **~3× lebih besar** dari rugi step ini.

> **Aturan yang bisa ditarik:** benar secara teknis (menghilangkan pola pelebaran mendadak) tidak otomatis berarti signifikan. **Hitung dulu skalanya** — kalau perbaikan yang "kelihatan jelas salah" ternyata cuma menyumbang < 0,5% terhadap tenaga, itu bukan prioritas, walau tetap sah dikerjakan kalau sedang bongkar untuk alasan lain.

### 7.5 Ringkasan studi kasus

1. **Panjang efektif saluran isap = jarak ke ujung terbuka**, bukan cuma "ada part atau tidak". Melepas satu komponen bisa memindahkan titik ujung terbuka, bukan cuma menghilangkan restriksi.
2. **Cocokkan rentang rpm yang dirasakan pengendara ke tabel harmonik** — ini cara memvalidasi teori tanpa perlu dyno run baru.
3. **Plenum meredam pulsa, bukan cuma menjadi reservoir volume.** Hilangnya peredaman ini terdengar sebagai suara sebelum terlihat di angka dyno.
4. **Hitung skala sebelum memprioritaskan perbaikan.** Step diameter yang "kelihatan salah" bisa ternyata menyumbang < 0,5% — valid diperbaiki, tapi bukan prioritas.

---

## 8. Daftar periksa kalibrasi

Sebelum menerima kesimpulan dari data lapangan:

- [ ] **Cam card**: apakah overlap yang disebut itu SUDUT (derajat) atau LIFT (mm)? Jangan campur.
- [ ] Kalau ada beberapa sumber data cam yang bertentangan, cek **konsistensi internal** (LSA+durasi → IVC/EVO harus cocok satu sama lain)
- [ ] **RPM prediksi**: pakai data mesin itu sendiri sebagai acuan kalau tersedia, jangan pinjam dari mesin yang jauh beda karakter
- [ ] **Throttle body**: dicek kecukupannya SEBELUM menyalahkan cam/valve kalau tenaga mendatar
- [ ] **Dyno**: pastikan dulu ini dyno chassis (WHP) atau dyno mesin (crank HP) — cek dari ada/tidaknya roller
- [ ] Kalau WHP, **konversi ke crank HP** sebelum dimasukkan ke rumus `Tenaga ≈ CFM × 0,43–0,50`
- [ ] Rugi drivetrain diasumsikan eksplisit (10/20/30%) dan **ditulis** — jangan diam-diam
- [ ] **Sebelum melepas atau mengganti komponen saluran** (box, piping, filter), hitung dulu apakah itu mengubah panjang efektif ke ujung terbuka — jangan asumsikan "dilepas = pasti lebih baik"
- [ ] Kalau ada step diameter di saluran, **hitung K via Borda-Carnot dan bandingkan skalanya** ke komponen lain (TB, tikungan) sebelum memprioritaskan perbaikan

---

## 9. Ringkasan Tahap 11

1. **Overlap dalam derajat dan lift-di-TDC dalam mm adalah dua hal berbeda** — jangan tertukar.
2. **Model harmonik untuk memvalidasi cam, bukan sumber kebenaran mutlak** — cam nyata bisa punya ramp lebih agresif dari `sin²`.
3. **Rumus time-area bisa dibalik untuk memprediksi rpm** dari spek cam+valve+Vd yang diketahui — tervalidasi 1,1% selisih pada satu kasus nyata.
4. **Data mesin itu sendiri selalu mengalahkan acuan dari mesin lain**, sekali tersedia.
5. **Cek kecukupan TB sebelum menyalahkan cam** kalau tenaga mendatar.
6. **Dyno chassis mengukur WHP, bukan crank HP.** Kenali dari ada/tidaknya roller. Konversi sebelum dipakai di rumus tenaga.
7. **Satu kesalahan unit tidak selalu merusak semua kesimpulan** — periksa rumus mana yang benar-benar terpengaruh.
8. **Panjang efektif saluran = jarak ke ujung terbuka**, bukan cuma "ada part atau tidak" — melepas komponen bisa memindahkan titik itu, bukan cuma menghilangkan restriksi.
9. **Hitung skala sebelum memprioritaskan perbaikan.** Sesuatu yang "kelihatan jelas salah" secara teknis bisa ternyata menyumbang < 0,5% terhadap tenaga.

**Berikutnya:** Lampiran — rumus ringkas, daftar periksa build, dan data mesin contoh.
