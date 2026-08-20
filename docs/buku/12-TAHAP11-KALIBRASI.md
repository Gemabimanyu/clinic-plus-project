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

#### Koreksi: Borda-Carnot hanya untuk PELEBARAN

Analisis di atas punya cacat yang baru ketahuan belakangan, dan cacatnya instruktif.

Urutan aliran di kasus ini adalah **plenum → pipa Ø42,5 → TB Ø36 → klep**. Jadi step 42,5 ke 36 itu **penyempitan**, bukan pelebaran. Borda-Carnot dipakai ke arah yang salah.

Rumus yang benar berbeda untuk tiap arah:

```
pelebaran mendadak   K = (1 − A_kecil/A_besar)²        [pakai v di sisi KECIL]
penyempitan mendadak K = 0,5 × (1 − A_kecil/A_besar)   [pakai v di sisi KECIL]
```

Perhatikan bedanya: pelebaran dikuadratkan, penyempitan tidak dan dikali 0,5. Untuk rasio luas yang sama, **pelebaran jauh lebih mahal daripada penyempitan** — itu sebabnya Tahap 7 §3.3 melarang pelebaran di tengah jalan tapi tidak melarang penyempitan bertahap.

Dihitung ulang dengan rumus yang benar, @8.400 rpm:

| | K | v (di TB) | Δp |
|---|---|---|---|
| Step tepi tajam | 0,141 | 87,7 m/s | **643 Pa** |
| Diberi radius/kerucut | 0,05 | 87,7 m/s | 228 Pa |
| **Selisih** | | | **415 Pa** |

**Kesimpulan prioritasnya tidak berubah** — step ini tetap item menengah, bukan yang terbesar. Tapi angkanya naik beberapa kali lipat dari hitungan pertama, dan itu cukup untuk memindahkannya dari "kerjakan kalau sempat" ke "kerjakan kalau boks memang dibuka".

> **Pelajarannya:** sebelum memilih rumus rugi aliran, **gambar dulu arah alirannya.** Rumus penyempitan dan pelebaran terlihat mirip dan sama-sama memberi angka yang "masuk akal" — tidak ada yang akan meneriakkan kesalahan ke kamu. Satu-satunya pengaman adalah menelusuri jalur udara dari mulut filter sampai klep sebelum menghitung apapun.

### 7.5 Bentuk lubang sama pentingnya dengan luasnya

Lanjutan kasus yang sama: tutup plenum aftermarket punya lubang inlet 2× slot kotak (masing-masing 87×17mm) menuju filter mesh 265×85mm. Pertanyaan awalnya "apakah lubang ini cukup besar" — tapi luas cuma separuh cerita.

**Cek luas dulu:**

| Bagian | Luas | Setara Ø |
|---|---|---|
| Slot inlet (2×) | 2.958 mm² | Ø61,4mm |
| Muka filter | 22.525 mm² | Ø169mm |

Keduanya **sudah lebih dari cukup** dibanding rekomendasi minimal (Ø55–60mm, bagian 5). Tapi slotnya berbentuk **kotak bertepi tajam** — pola yang sama dengan "mulut rata bertepi tajam" di tabel K (Kamus Istilah), K=0,5, jauh dari mulut yang dibulatkan (K=0,05).

**Bandingkan rugi tiga titik pembatas dalam satu sistem** (@8.400 rpm):

| Titik | K | Rugi tekanan |
|---|---|---|
| Slot inlet (tepi tajam, sekarang) | 0,5 | 320 Pa |
| Step TB→pipa (36→42,5mm) | 0,08 | 432 Pa |
| **Throttle body (butterfly, WOT)** | **0,25** | **1.351 Pa** |

TB tetap pembatas terbesar (~4× rugi slot inlet), meski slotnya sendiri belum ideal.

**Efek membulatkan tepi slot, tanpa mengubah luas:**

| Bentuk tepi | K | Rugi @8.400rpm |
|---|---|---|
| Tajam (sekarang) | 0,5 | 320 Pa |
| Radius kecil / chamfer | 0,2 | 128 Pa |
| Bellmouth penuh | 0,05 | 32 Pa |

Chamfer sederhana **memangkas rugi 60%** tanpa menambah luas sama sekali.

> **Pelajaran tambahan:** ketika luas sudah cukup, **bentuk tepi jadi tuas yang lebih murah daripada memperbesar lubang lagi**. Ini kebalikan dari asumsi umum "kalau kurang tenaga, perbesar lubangnya" — kadang yang kurang bukan luasnya, tapi kehalusan bentuknya.

### 7.6 Ringkasan studi kasus

1. **Panjang efektif saluran isap = jarak ke ujung terbuka**, bukan cuma "ada part atau tidak". Melepas satu komponen bisa memindahkan titik ujung terbuka, bukan cuma menghilangkan restriksi.
2. **Cocokkan rentang rpm yang dirasakan pengendara ke tabel harmonik** — ini cara memvalidasi teori tanpa perlu dyno run baru.
3. **Plenum meredam pulsa, bukan cuma menjadi reservoir volume.** Hilangnya peredaman ini terdengar sebagai suara sebelum terlihat di angka dyno.
4. **Hitung skala sebelum memprioritaskan perbaikan.** Step diameter yang "kelihatan salah" bisa ternyata menyumbang < 0,5% — valid diperbaiki, tapi bukan prioritas.
5. **Bentuk tepi lubang bisa jadi tuas lebih murah daripada memperbesar luasnya** — cek keduanya, jangan cuma luas.

---

## 8. Menguji kewarasan angka dyno dengan inversi BMEP

### 8.1 Kenapa angka dyno butuh diuji

Sheet dyno terlihat otoritatif. Ada grafik, ada angka desimal, ada nama software. Tapi dyno adalah instrumen dengan banyak parameter yang dimasukkan manusia — konstanta inersia, diameter roller, rasio gigi, faktor koreksi atmosfer — dan **tidak satupun dari parameter itu diverifikasi oleh alatnya sendiri.**

Ada satu uji yang bisa dilakukan siapa saja, tanpa alat tambahan, dari dua angka yang selalu tertulis di sheet: **tenaga dan rpm.**

### 8.2 BMEP — besaran yang tidak bisa dibohongi

BMEP (*brake mean effective pressure*) adalah tekanan rata-rata efektif yang bekerja di atas piston sepanjang langkah usaha. Dia hanya bergantung pada torsi dan kapasitas:

```
BMEP = 4π × T / Vd                    [4 langkah; T dalam Nm, Vd dalam m³, hasil Pa]
T    = P / ω = P / (rpm × 2π/60)      [P dalam Watt]
```

Kenapa ini kuat sebagai alat uji: BMEP punya **plafon fisik yang keras**. Dia dibatasi oleh berapa banyak udara yang bisa masuk silinder dan berapa banyak energi yang bisa dilepas bahan bakar dari udara itu. Mesin aspirasi alami tidak bisa melampauinya, seberapapun bagus porting-nya.

### 8.3 Jangkar: pakai mesin produksi nyata, bukan angka hafalan

Jangan pakai "plafon 15 bar" sebagai angka keramat. Pakai mesin yang bisa kamu cek spesifikasinya sendiri, dan bandingkan **di titik yang setara**.

| Mesin acuan | Kapasitas | Titik | BMEP |
|---|---|---|---|
| Yamaha XMAX 300 standar | 292cc | 27,6 PS @ 7.250 (peak power) | **11,5 bar** |
| Honda CBR250RR | 249,7cc | 38 PS @ 12.500 (peak power) | **10,7 bar** |
| KTM 690 SMC R | 693cc | 73,5 Nm @ 6.500 (peak torsi) | **13,3 bar** |
| KTM 690 SMC R | 693cc | 74 hp @ 8.000 (peak power) | **11,9 bar** |

**Perhatikan pola penting:** BMEP di peak power selalu **lebih rendah** daripada di peak torsi, karena VE sudah menurun di rpm yang lebih tinggi. KTM 690 — single NA yang dikembangkan penuh oleh pabrikan — turun dari 13,3 ke 11,9 bar. Jadi kalau menguji angka di peak power, **bandingkan ke angka peak power**, jangan ke peak torsi.

Rentang praktis yang bisa dipakai:

| | BMEP di peak power |
|---|---|
| Mesin OEM biasa | 10–12 bar |
| Tertala baik | 12–13 bar |
| Balap serius | 13–14 bar |
| Di atas 15 bar | bukan NA |

### 8.4 Kasus nyata: sheet yang tidak lolos

Data yang diuji — XMAX bore-up, Vd 344,8cc, cam 260°, porting standar dirapikan, dyno inersia Leads:

```
tertulis di sheet:  40,6 hp @ 6.563 rpm  (peak power)
                    68,18 Nm @ 2.103 rpm (peak torsi)
```

Inversi:

| Titik | Torsi | BMEP | vs KTM 690 di titik setara |
|---|---|---|---|
| 40,6 hp @ 6.563 rpm | 44,1 Nm | **16,05 bar** | **1,34×** |
| 68,18 Nm @ 2.103 rpm | 68,2 Nm | **24,85 bar** | **1,86×** |

Keduanya di atas apa yang dicapai single NA terbaik buatan pabrik. Sheet ini tidak lolos uji — dan sekarang pertanyaannya bukan lagi "apakah ada yang salah", melainkan **"yang mana yang salah"**.

### 8.5 Dua bacaan, dan cara memilih

Ketika BMEP kelewat tinggi, hanya ada dua kemungkinan dasar:

| | Konsekuensi |
|---|---|
| **(a) Tenaganya benar, rpm-nya meleset** | peak sebenarnya ada di rpm lebih tinggi |
| **(b) Rpm-nya benar, tenaganya digelembungkan** | tenaga sebenarnya lebih kecil |

Untuk kasus di atas:

| Kalau BMEP-nya | 40,6 hp terjadi di | atau, di 6.563 rpm tenaganya |
|---|---|---|
| 11,5 bar | 9.162 rpm | 29,1 hp |
| 12,0 bar | 8.781 rpm | 30,3 hp |
| 12,5 bar | 8.429 rpm | 31,6 hp |
| 13,0 bar | 8.105 rpm | 32,9 hp |

Cara memilih di antara keduanya ada di bagian berikutnya.

---

## 9. Membedakan salah kalibrasi dari salah rasio — khusus dyno matic

### 9.1 Uji pembedanya: apakah faktor errornya konstan?

Ini inti bab ini, dan setahu penulis belum ditulis di tempat lain.

**Hitung faktor kelebihan BMEP di minimal dua titik** yang berjauhan di grafik — biasanya di peak power dan di peak torsi.

```
faktor = BMEP_terbaca / BMEP_wajar_di_titik_setara
```

Lalu baca polanya:

| Pola | Artinya |
|---|---|
| **Faktor sama di semua titik** | kesalahan **kalibrasi** — konstanta inersia, faktor koreksi atmosfer, atau salah satuan. Menggeser seluruh grafik dengan pengali yang sama |
| **Faktor membesar ke arah rpm rendah** | kesalahan **rasio** — rpm mesin diturunkan dari rpm roller lewat rasio tetap, padahal rasionya bergeser |
| Faktor acak, tidak berpola | data mentahnya sendiri berantakan — ulangi run |

**Kenapa uji ini bekerja:** kesalahan kalibrasi bersifat perkalian terhadap seluruh dataset. Kesalahan rasio pada CVT bersifat *progresif*, karena besarnya penyimpangan rasio berubah sepanjang run.

### 9.2 Kasus yang sama, diuji

| Titik | Faktor kelebihan |
|---|---|
| Peak power | **1,34×** |
| Peak torsi | **1,86×** |

Tidak konstan, dan membesar ke arah rpm rendah. **Vonisnya: kesalahan rasio.**

Konfirmasinya ada di header sheet itu sendiri: kolom `Ratio 3.95`. Software menurunkan rpm mesin dari rpm roller dikali angka tetap 3,95. Pada matic tanpa *locked ratio pulley*, rasio itu bergeser terus-menerus sepanjang akselerasi:

- **Di kecepatan tinggi** CVT sudah shift-out penuh, rasio aktual mendekati angka tetap yang diasumsikan → error kecil (1,34×)
- **Di kecepatan rendah** CVT masih di rasio berat, mesin berputar jauh lebih cepat daripada yang dihitung → error membengkak (1,86×)

Bentuk errornya persis sesuai mekanismenya.

### 9.3 Kenapa tenaganya selamat tapi torsi dan rpm tidak

Pada dyno inersia:

```
P = I × ω_roller × (dω_roller/dt)
```

**Tenaga dihitung murni dari percepatan roller.** Rpm mesin tidak muncul sama sekali di rumus itu. Jadi tenaga lolos dari kesalahan rasio.

Torsi lain ceritanya — software menghitungnya sebagai `T = P / ω_mesin`, memakai rpm mesin yang rusak. Jadi torsi ikut rusak.

| Besaran | Nasib pada kesalahan rasio |
|---|---|
| Tenaga (hp/kW) | ✅ selamat — dari percepatan roller |
| Sumbu rpm mesin | ❌ rusak, makin parah ke rpm rendah |
| Torsi (Nm) | ❌ rusak — turunan dari rpm yang rusak |
| Posisi peak di sumbu rpm | ❌ tidak bermakna |

**Konsekuensi praktisnya besar:** angka tenaga yang dibanggakan orang biasanya benar. Yang salah adalah *di mana* tenaga itu terjadi — dan justru itulah yang dibutuhkan untuk menala cam, saluran isap, dan setelan CVT.

### 9.4 Cara memperbaikinya

Salah satu dari dua ini menyelesaikannya permanen:

1. **Run dengan locked ratio pulley** — rasio jadi benar-benar tetap, angka di kolom `Ratio` jadi sah. Ini yang paling bersih.
2. **Umpankan sinyal rpm asli dari pickup pengapian** ke software, jangan biarkan dia menurunkan dari rasio.

Kalau keduanya tidak tersedia, jalan murahnya ada di Tahap 9 §3.1: **tacho yang bisa dibaca saat jalan.** Catat rpm yang ditahan CVT saat akselerasi penuh. Pada matic, angka itu justru lebih berguna daripada seluruh sumbu rpm di sheet dyno — karena di situlah mesin benar-benar bekerja.

### 9.5 Cek silang: apakah rpm hasil koreksi masuk akal?

Jangan berhenti setelah mengoreksi. Uji apakah rpm baru itu wajar untuk mesinnya, pakai besaran yang tidak terlibat di perhitungan tadi:

| rpm | v throat isap | v TB | MPS |
|---|---|---|---|
| 7.800 | 77 m/s | 81 m/s | 19,8 m/s |
| 8.100 | 80 m/s | 85 m/s | 20,5 m/s |
| 8.500 | 84 m/s | 89 m/s | 21,5 m/s |
| 8.800 | 87 m/s | 92 m/s | 22,3 m/s |

Semuanya di bawah batas: throat masih di bawah rentang kerja mesin tertala (97–115 m/s, Tahap 7 §1.4), MPS masih di bawah Mesin Contoh A (21,3 m/s). **Rpm hasil koreksi lolos cek silang** — kalau tidak lolos, koreksinya sendiri yang perlu dicurigai.

---

## 10. Merancang plenum dari sasaran, bukan dari acuan pabrikan

### 10.1 Kenapa angka pabrikan tidak boleh jadi sasaran

Aturan plenum di Tahap 7 §3.4 berbunyi `V_plenum ≈ 1,0–1,5 × kapasitas mesin`. Airbox skutik standar berada di **8–15× kapasitas mesin**. Selisihnya sepuluh kali lipat, dan keduanya benar — untuk tujuan yang berbeda.

Aturan Tahap 7 ditulis untuk **plenum balap**: ruang kecil yang langsung menyuapi runner pendek. Airbox OEM adalah **kelas komponen lain**, dan ukurannya adalah harga dari enam kendala yang sebagian besar tidak berlaku bagi pembangun mesin:

| Kendala pabrikan | Mendorong volume besar karena | Berlaku untuk mesin tune? |
|---|---|---|
| **Regulasi kebisingan** | boks = filter low-pass akustik; makin besar makin senyap deru induksi. Sering ini kendala yang mengikat, bukan tenaga | Tidak |
| **Margin filter kotor** | *face velocity* dibuat < 1 m/s padahal media dirancang 1–3 m/s — margin 3–4× agar motor tetap normal dengan filter dekil di 20.000 km | Sebagian |
| **Sinyal MAP stabil** | riak tekanan = error perhitungan massa udara = error AFR | **Ya — lihat §10.5** |
| **Karakter rata untuk semua orang** | reservoir-dominant = tidak ada tanjakan/lubang tenaga | Tidak |
| **Satu kalibrasi untuk semua kondisi** | perilaku reservoir kurang sensitif terhadap ketinggian dan suhu daripada penalaan gelombang | Sebagian |
| **Volume gratis di skutik** | ruang bawah jok toh menganggur | Ya |

> **Aturan yang bisa ditarik:** sebelum meniru angka pabrikan, tanyakan **kendala apa yang sedang dibayar oleh angka itu.** Kalau kendalanya bukan kendalamu, angkanya bukan sasaranmu.

### 10.2 Dua kriteria volume yang diturunkan dari mesinnya sendiri

Ganti acuan pinjaman dengan dua kriteria yang keduanya memakai data mesin itu sendiri.

**Kriteria 1 — dekopling.** Agar plenum berperan sebagai ujung terbuka yang memantulkan gelombang dengan bersih, volumenya harus jauh lebih besar daripada kolom udara di saluran yang menempel padanya:

```
V_plenum ≈ 5–10 × volume kolom runner
volume kolom runner = Σ (luas penampang × panjang) sepanjang saluran ke klep
```

**Kriteria 2 — responsivitas inlet.** Boks harus sanggup mengisi ulang dirinya lebih cepat daripada mesin mengosongkannya. Kalau tidak, boks itu sendiri jadi hambatan. Syaratnya, Helmholtz sisi inlet harus jauh di atas frekuensi isap:

```
f_inlet = (c/2π) × √(A_inlet / (V_plenum × L_inlet_efektif))
f_isap  = rpm / 120                                    [1 silinder, 4 langkah]

syarat:  f_inlet ≥ 3 × f_isap_maksimum
```

Perhatikan bahwa kriteria 2 **mengikat volume dan luas inlet bersama-sama**: memperbesar boks tanpa memperbesar inlet menurunkan f_inlet dan bisa membuat boks jadi lambat. Ini hubungan yang hilang kalau volume dipilih sebagai angka tunggal.

**Diterapkan ke kasus XMAX 344,8cc** (pipa 240mm Ø42,5 + tract 250mm Ø36 ≈ 595cc kolom runner):

| Kriteria | Hasil |
|---|---|
| Dekopling 5–10× | 2,97 – 5,95 L |
| Responsivitas inlet (inlet 2.958mm², plafon 8.500 rpm) | lolos sampai > 6 L |
| **Rentang sah** | **3,0 – 6,0 L** |

Hasilnya **rentang, bukan titik.** Itu jawaban yang jujur: di dalam rentang itu volume bukan lagi tuas yang menentukan, dan usaha lebih baik dialihkan ke geometri.

### 10.3 Tumpukan rugi sebagai alat prioritas

Sebelum memutuskan apa yang dikerjakan, susun semua rugi tekanan di satu tabel, di rpm yang sama, dengan kecepatan aliran di titik masing-masing. Ini mengubah perdebatan selera jadi urutan angka.

Kasus XMAX, **@8.400 rpm, aliran puncak**:

| Titik | K | v | Δp |
|---|---|---|---|
| **Mulut pipa menonjol ke plenum** | 0,9 | 62,9 m/s | **2.108 Pa** |
| TB butterfly 36mm — tidak diubah | 0,25 | 87,7 m/s | 1.138 Pa |
| Mulut pipa rata bertepi tajam | 0,5 | 62,9 m/s | 1.171 Pa |
| Penyempitan 42,5→36 tepi tajam | 0,141 | 87,7 m/s | 643 Pa |
| Slot inlet (aliran sudah diredam boks) | 0,5 | 13,9 m/s | 57 Pa |
| — setelah diperbaiki — | | | |
| Mulut pipa **dengan bellmouth** | 0,05 | 62,9 m/s | **117 Pa** |
| Penyempitan **dikerucutkan** | 0,05 | 87,7 m/s | 228 Pa |

```
total dapat diperbaiki : ~2.400 Pa  = 2,4% tekanan atmosfer
rugi TB (tidak diubah) :  1.138 Pa
```

**Temuan yang mengejutkan: mulut pipa di dalam plenum lebih mahal daripada throttle body-nya sendiri.** Komponen yang tidak punya nama, tidak dijual sebagai part, dan tidak pernah disebut di forum — mengalahkan komponen yang paling sering diganti orang.

Ini terjadi karena tabel K sangat menghukum mulut yang menonjol ke dalam ruang (K = 0,8–1,0) dibanding mulut beradius (K = 0,05) — beda **20 kali lipat**, jauh lebih besar daripada selisih K antar ukuran TB.

### 10.4 Ruang bebas mengalahkan volume

Bellmouth hanya bekerja kalau udara bisa mengalir masuk **dari segala arah** ke mulutnya. Bellmouth yang mulutnya rapat ke dinding boks cuma tepi tajam yang mahal.

```
jarak mulut ke dinding di depannya : ≥ 1,0 × D saluran   (ideal 1,5 × D)
jarak radial mulut ke dinding      : ≥ 0,5 × D saluran
radius bellmouth                   : 0,15–0,20 × D       [Tahap 7 §3.2]
```

> **Aturan prioritas:** kalau harus memilih, **boks lebih kecil dengan ruang bebas yang benar mengalahkan boks lebih besar yang mulut pipanya terjepit.** Ini kebalikan dari naluri kebanyakan orang, yang mengejar liter.

Konsekuensi rancangan: **masukkan pipa lewat muka ujung yang kecil dan arahkan menyusuri sisi terpanjang boks**, bukan menembus muka lebar. Dengan cara itu ruang bebas di depan mulut hampir selalu terpenuhi tanpa memperbesar boks.

Susunan itu juga memberi bonus: filter jadi berada tegak lurus terhadap sumbu bellmouth, sehingga **tidak ada jet udara yang menghantam mulut** — masalah yang muncul kalau filter dipasang persis berhadapan dengan pipa.

### 10.5 Sinyal MAP sebagai kendala rancang — jebakan ECU aftermarket

Ini kendala yang tidak ada di buku manapun, dan akan mengenai siapapun memakai ECU aftermarket pada mesin 1 silinder.

Banyak ECU aftermarket kelas menengah mengunci **tabel dasar RPM vs MAP** dan hanya membuka **tabel koreksi RPM vs TPS**. Artinya seluruh penentuan bahan bakar berjalan lewat sinyal MAP, dan tuner **tidak bisa menulis ulang tabel utamanya.**

Pada mesin 1 silinder ini jadi serius, karena tidak ada silinder lain yang mengisi jeda antar langkah isap — riak tekanan di saluran isap adalah kasus terburuk.

```
riak per langkah isap = (Vd × VE) / V_plenum
```

| V plenum | untuk Vd 344,8cc, VE 0,85 | |
|---|---|---|
| 3,0 L | 9,8% | |
| 4,5 L | 6,5% | |
| 5,0 L | 5,9% | |

**Konsekuensi rancangan:**

- Volume plenum berpindah dari "urusan karakter" jadi **kendala akurasi bahan bakar**
- Dinding boks harus **kaku dan berusuk** — dinding tipis yang melentur menambah *compliance* yang tidak terhitung dan mengaburkan sinyal
- Nipel MAP diberi **orifis kecil (Ø0,8–1,0mm) plus volume redam kecil**, agar sensor membaca rata-rata dan bukan denyut sesaat. Nyaris gratis, dan sering jadi perbaikan tuning terbesar per rupiah pada 1 silinder speed-density
- Kebocoran **antara TB dan klep** = udara yang tidak terbaca MAP = campuran miskin yang tidak bisa dilihat tabel terkunci. Bagian itu wajib kedap. Kebocoran di hulu TB "hanya" memasukkan debu

### 10.6 Jangan pakai aliran puncak di titik yang sudah diredam boks

Kesalahan yang mudah terjadi saat menyusun tumpukan rugi: memakai **aliran puncak** di semua titik.

Aliran puncak (`Q_rata2 / duty × π/2`) berlaku di saluran yang tersambung langsung ke klep. Tapi **plenum ada justru untuk meredam pulsa itu** — di hulu boks, aliran mendekati rata-rata, bukan puncak.

Bedanya besar. Untuk slot inlet XMAX @6.500 rpm:

| Asumsi aliran | v | Δp (K=0,5) |
|---|---|---|
| Rata-rata | 5,4 m/s | 8,5 Pa |
| 2× rata-rata (realistis) | 10,7 m/s | 34 Pa |
| Puncak — asumsi yang salah | 23,4 m/s | 161 Pa |

Salah asumsi di sini menggelembungkan rugi inlet **5–20×**, dan itu cukup untuk memindahkan pekerjaan yang sepele ke urutan atas daftar prioritas.

> **Aturan:** pakai aliran puncak di **hilir** plenum, aliran mendekati rata-rata di **hulu** plenum. Titik pemisahnya adalah plenum itu sendiri.

### 10.7 Ringkasan urutan merancang plenum

1. Telusuri jalur udara dari mulut filter sampai klep, **gambar arahnya** — ini menentukan rumus rugi mana yang dipakai di tiap step
2. Susun **tumpukan rugi** di satu rpm, urutkan dari terbesar
3. Kerjakan **bentuk mulut dan tepi** dulu — hampir selalu paling murah per Pa
4. Tentukan **rentang volume** dari kriteria dekopling dan responsivitas inlet, bukan dari angka pabrikan
5. Di dalam rentang itu, **utamakan ruang bebas bellmouth di atas mengejar liter**
6. Kalau ECU-nya speed-density dengan tabel terkunci, **naikkan volume ke sisi atas rentang** dan redam nipel MAP
7. Tentukan **panjang saluran** dari rpm kerja sebenarnya — dan pastikan rpm itu sudah lolos uji BMEP di §8

---

## 11. Daftar periksa kalibrasi

Sebelum menerima kesimpulan dari data lapangan:

- [ ] **Cam card**: apakah overlap yang disebut itu SUDUT (derajat) atau LIFT (mm)? Jangan campur.
- [ ] Kalau ada beberapa sumber data cam yang bertentangan, cek **konsistensi internal** (LSA+durasi → IVC/EVO harus cocok satu sama lain)
- [ ] **RPM prediksi**: pakai data mesin itu sendiri sebagai acuan kalau tersedia, jangan pinjam dari mesin yang jauh beda karakter
- [ ] **Throttle body**: dicek kecukupannya SEBELUM menyalahkan cam/valve kalau tenaga mendatar
- [ ] **Dyno**: pastikan dulu ini dyno chassis (WHP) atau dyno mesin (crank HP) — cek dari ada/tidaknya roller
- [ ] Kalau WHP, **konversi ke crank HP** sebelum dimasukkan ke rumus `Tenaga ≈ CFM × 0,43–0,50`
- [ ] Rugi drivetrain diasumsikan eksplisit (10/20/30%) dan **ditulis** — jangan diam-diam
- [ ] **Sebelum melepas atau mengganti komponen saluran** (box, piping, filter), hitung dulu apakah itu mengubah panjang efektif ke ujung terbuka — jangan asumsikan "dilepas = pasti lebih baik"
- [ ] Kalau ada step diameter di saluran, **hitung K dan bandingkan skalanya** ke komponen lain (TB, tikungan) sebelum memprioritaskan perbaikan
- [ ] **Gambar arah aliran** sebelum memilih rumus rugi — penyempitan dan pelebaran punya rumus berbeda dan sama-sama memberi angka yang "masuk akal"
- [ ] **Uji BMEP** setiap angka dyno sebelum dipakai sebagai jangkar: `BMEP = 4π × T / Vd`, bandingkan ke mesin produksi nyata **di titik yang setara** (peak power ke peak power)
- [ ] Kalau BMEP kelewat tinggi, **hitung faktor kelebihannya di ≥2 titik**: konstan = salah kalibrasi, membesar ke rpm rendah = salah rasio
- [ ] Pada dyno matic, cek apakah ada kolom **`Ratio` tetap** — kalau run tidak memakai *locked ratio pulley*, sumbu rpm dan seluruh kurva torsi tidak bisa dipakai
- [ ] **Aliran puncak di hilir plenum, aliran mendekati rata-rata di hulu plenum** — jangan pakai puncak di titik yang justru sudah diredam boks
- [ ] Sebelum meniru angka pabrikan, tanyakan **kendala apa yang sedang dibayar angka itu** — kalau bukan kendalamu, itu bukan sasaranmu

---

## 12. Ringkasan Tahap 11

1. **Overlap dalam derajat dan lift-di-TDC dalam mm adalah dua hal berbeda** — jangan tertukar.
2. **Model harmonik untuk memvalidasi cam, bukan sumber kebenaran mutlak** — cam nyata bisa punya ramp lebih agresif dari `sin²`.
3. **Rumus time-area bisa dibalik untuk memprediksi rpm** dari spek cam+valve+Vd yang diketahui — tervalidasi 1,1% selisih pada satu kasus nyata.
4. **Data mesin itu sendiri selalu mengalahkan acuan dari mesin lain**, sekali tersedia.
5. **Cek kecukupan TB sebelum menyalahkan cam** kalau tenaga mendatar.
6. **Dyno chassis mengukur WHP, bukan crank HP.** Kenali dari ada/tidaknya roller. Konversi sebelum dipakai di rumus tenaga.
7. **Satu kesalahan unit tidak selalu merusak semua kesimpulan** — periksa rumus mana yang benar-benar terpengaruh.
8. **Panjang efektif saluran = jarak ke ujung terbuka**, bukan cuma "ada part atau tidak" — melepas komponen bisa memindahkan titik itu, bukan cuma menghilangkan restriksi.
9. **Hitung skala sebelum memprioritaskan perbaikan.** Sesuatu yang "kelihatan jelas salah" secara teknis bisa ternyata menyumbang < 0,5% terhadap tenaga.
10. **Gambar arah aliran sebelum memilih rumus rugi.** Penyempitan dan pelebaran punya rumus berbeda, dan keduanya memberi angka yang terlihat masuk akal — tidak ada yang akan meneriakkan kesalahan ke kamu.
11. **Angka dyno adalah data yang harus diuji, bukan kebenaran yang diterima.** Inversi BMEP menguji sheet manapun dari dua angka yang selalu ada di situ: tenaga dan rpm.
12. **Bandingkan ke mesin produksi nyata di titik yang setara** — BMEP di peak power selalu lebih rendah daripada di peak torsi.
13. **Pola faktor error memberi tahu jenis kesalahannya.** Konstan = kalibrasi. Membesar ke rpm rendah = rasio. Ini uji yang bisa dilakukan dari dua titik di sheet.
14. **Pada dyno inersia matic, tenaga selamat tapi rpm dan torsi bisa rusak** — tenaga dihitung dari percepatan roller dan tidak menyentuh rpm mesin. Yang hilang justru *di mana* tenaga itu terjadi, dan itulah yang dibutuhkan untuk menala.
15. **Angka pabrikan membayar kendala pabrikan** — kebisingan, margin servis, kalibrasi tunggal untuk semua kondisi. Kalau kendalanya bukan kendalamu, angkanya bukan sasaranmu.
16. **Volume plenum diturunkan dari dekopling dan responsivitas inlet**, dan hasilnya rentang, bukan titik. Di dalam rentang itu, ruang bebas bellmouth lebih menentukan daripada liter.
17. **Komponen tanpa nama bisa mengalahkan komponen yang paling sering diganti.** Mulut pipa di dalam plenum ternyata lebih mahal daripada throttle body-nya sendiri.

**Berikutnya:** Lampiran — rumus ringkas, daftar periksa build, dan data mesin contoh.
