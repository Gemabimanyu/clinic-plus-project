# XMAX 344cc — Build Spec Final

**Dokumen kerja.** Semua angka di sini diturunkan dari spesifikasi dan pengukuran mesin ini sendiri, memakai metode di *Advanced Engine Tuning* Tahap 3 (Aliran), Tahap 4 (Camshaft), Tahap 7 (Saluran), Tahap 8 (Mekanik), Tahap 9 (CVT), dan Tahap 11 (Kalibrasi).

Terakhir diperbarui: 26 September 2026 — revisi setelah pengukuran seat klep dan flange port, penetapan batas peak 9.000 rpm, dan spesifikasi porting kepala.

---

## 1. Kondisi mesin saat ini

### 1.1 Dasar

| | |
|---|---|
| Basis | Yamaha XMAX 300 (292,1cc — bore 70,0 × stroke 75,9) |
| Bore sekarang | **76,0 mm** |
| Stroke | **76,0 mm** |
| **Kapasitas** | **344,8 cc** |
| Kenaikan dari standar | +18,0% |
| Konfigurasi | 1 silinder, 4 klep, SOHC |
| Penyaluran | CVT |

### 1.2 Kepala silinder — terukur

| | |
|---|---|
| Klep isap | 28,0 mm × 2 |
| Klep buang | 22,5 mm × 2 |
| Diameter seat isap (throat) | **Ø25,5 mm** → rasio throat/klep **0,911** |
| **Luas throat isap total** | **1.021 mm²** |
| Batang klep | Ø5 mm (3,8% luas throat) |
| Port isap di flange | **oval 30 × 34 mm**, siamese (satu lubang untuk dua klep) — **801 mm² kalau elips murni; 887–938 mm² kalau oval bersudut** (lihat peringatan di bawah) |
| Rasio port/throat | **0,78–0,92** tergantung bentuk flange — port tetap penampang tersempit |
| Luas klep isap / bore | 0,271 (2 × (28/76)²) |
| Luas klep buang / isap | 0,646 |
| Porting | standar — rencana di §5 |

> **⚠ Peringatan — bentuk flange belum diukur.** Dua sumbu 30 × 34 tidak cukup untuk menentukan luas. Semua angka di dokumen ini memakai **elips murni** (`π/4 × 30 × 34 = 801 mm²`). Buku ini sendiri (Kamus, CSA) memakai faktor **0,92 × lebar × tinggi** untuk port oval hasil porting yang bersudut. Kalau flange XMAX berbentuk seperti itu, luasnya **~938 mm²** — dan hampir semua angka porting di §5 bergeser (lihat §5.2). **Ukur luas flange dari scan/CAD sebelum menggerinda atau mencetak manifold.**

> **Koreksi:** versi sebelumnya menulis rasio throat/klep 0,935 dan luas throat 1.077 mm². Itu asumsi, bukan ukuran; seat terukur Ø25,5 memberi 1.021 mm² (−5,1%). Baris "rasio klep/bore 0,368" sebelumnya adalah rasio diameter satu klep (28/76), bukan rasio luas.

### 1.3 Camshaft

| | |
|---|---|
| Durasi | **260°** (konvensi lift tidak diketahui — K dikalibrasi dari mesin ini sendiri, jadi tetap konsisten selama cam yang sama) |
| Status | sudah dimodifikasi |
| K time-area mesin ini | 1.021 × 260 / (344,8 × 8.400) = **0,092** |
| MGV throat di peak | **95 m/s** |

### 1.4 Saluran isap — geometri terkoreksi CAD

| | |
|---|---|
| Panjang klep → ujung TB | **206 mm** (CAD; asumsi awal 250mm ternyata meleset) |
| Throttle body | **36 mm** (standar, tidak diubah) |
| Pipa TB → boks plenum | **227 mm** (CAD, sudah dibuat/prototipe) |
| Bentuk pipa | **sudah tirus** — mulut Ø65,8mm di plenum, mengerucut menerus ke ujung TB |
| Ujung pipa di TB | rencana direvisi **42,5 → 40mm** untuk menghapus step menuju spigot TB |
| **Panjang total tract** | **433 mm fisik** (≈460mm efektif dengan koreksi ujung) |
| Volume plenum | **4,5 L terukur** (tutup aftermarket) |
| Filter mesh | 265 × 85 mm (22.525 mm²) |
| Lubang inlet | 2 slot kotak 87 × 17 mm (2.958 mm² total) |

### 1.5 Manajemen mesin

| | |
|---|---|
| ECU | MiniXX (versi Mini, bukan Super) |
| Sensor | MAP terpasang |
| Tabel RPM vs MAP | **terkunci** — tidak bisa diedit |
| Tabel RPM vs TPS | terbuka, saat ini **100 di semua sel** (netral) |
| Konsekuensi | seluruh penentuan bahan bakar berjalan lewat sinyal MAP |

---

## 2. Data dyno — koreksi dan validasi lapangan

### 2.1 Yang tertulis di sheet awal

Leads dyno inersia, 3,3 kg·m², roller Ø267 mm, **tanpa locked ratio pulley**.

```
Peak power :  40,6 hp @ 6.563 rpm
Peak torsi :  68,18 Nm @ 2.103 rpm
Kolom Ratio:  3,95 (tetap)
```

### 2.2 Uji BMEP — sheet ini tidak lolos

| Titik | Torsi | BMEP | vs KTM 690 SMC R di titik setara |
|---|---|---|---|
| 40,6 hp @ 6.563 rpm | 44,1 Nm | **16,05 bar** | 1,34× |
| 68,18 Nm @ 2.103 rpm | 68,2 Nm | **24,85 bar** | 1,86× |

Faktor kelebihannya **tidak konstan** (1,34× vs 1,86×, membesar ke rpm rendah) — tanda tangan **rasio CVT yang bergeser** sementara software memakai `Ratio 3,95` yang tetap, bukan kesalahan kalibrasi (lihat Tahap 11 §9).

### 2.3 Apa yang bisa dipakai

| Besaran | Status |
|---|---|
| **Tenaga 40,6 hp** | ✅ dipakai — dihitung dari percepatan roller, tidak menyentuh rpm mesin |
| Sumbu Engine RPM, torsi, posisi peak | ❌ dibuang — turunan dari rasio yang rusak |

### 2.4 Peak power sebenarnya: **7.800 – 8.800 rpm**

Diturunkan dari uji BMEP (rentang 11,5–13,0 bar terhadap 40,6 hp). Cek silang kecepatan port/piston di rentang itu semua di bawah batas mesin tertala (Tahap 3/8). **Lolos.** Titik kerja yang dipakai untuk semua perhitungan di bawah: **8.400 rpm**.

### 2.5 Validasi lapangan — cocok dengan pipa 227mm yang sudah dibuat

Setelah pipa 227mm terpasang dan diuji **tanpa boks**, laporan pengendara: tendangan tenaga masuk **7.000–8.500 rpm**, jauh berbeda dari sebelum pipa dipasang.

Prediksi gelombang untuk kondisi tanpa boks (ujung bebas, k=0,61):

```
L efektif = 433 + 0,61 × 32,9 = 453 mm
h2        = 7.781 rpm
```

**Terukur: pusat pita 7.750 rpm. Selisih 0,4%.** Lebar pita prediksi (±10% dari titik tertala) = 7.003–8.559 rpm, terukur 7.000–8.500 — kedua metrik cocok.

Dengan boks terpasang (ujung ter-flange, k=0,82): **h2 = 7.674–8.408 rpm**, tetap di dalam rentang kerja 7.800–8.800 dari uji BMEP.

> **Pelajaran:** perbedaan rasa berkendara yang besar antara "sebelum" dan "sesudah" pipa terpasang adalah efek berpindah dari harmonik **h4 ke h2** — bukan efek boks. Rpm-nya nyaris sama; yang berubah kekuatan denyutnya.

### 2.6 Angka dyno kemungkinan membaca tinggi

Dibanding mesin pabrikan dengan spesifikasi terbuka (Honda CRF450R, Tahap 11 §11.4): 40,6 hp di roller lewat CVT pada 8.400 rpm setara **14,3–14,8 bar BMEP di engkol** — lebih tinggi dari mesin motocross 13,5:1 (~13,3 bar), padahal cam-nya 260° jalanan. Bacaan paling masuk akal: dyno ini membaca **~8–12% tinggi**.

Perhitungan proporsional di dokumen ini (anggaran porting, pergeseran peak) tidak terpengaruh. Angka hp absolut hanya berlaku **di dyno yang sama**.

---

## 3. Tumpukan rugi — dengan geometri terukur, bukan diasumsikan

**@8.400 rpm, aliran puncak** (`ρ` = 1,184 kg/m³, VE 0,85).

| Titik | v | Δp | Bisa diubah? |
|---|---|---|---|
| TB butterfly 36 mm | 87,7 m/s | **1.138 Pa** | ❌ TB tetap standar |
| Mulut pipa Ø65,8, menonjol ke plenum | 26,2 m/s | 367 Pa | ✅ radius |
| Pemuaian port 801 → throat 1.021 di dalam kepala (bila mendadak; port dianggap elips) | 111,5 m/s | ~342 Pa | ✅ blending bowl (§5) |
| Kerucut TB 40→36 (spigot 32mm) | 71,0 m/s | 182 Pa | ✅ dihaluskan |
| Step sambungan 42,5→40 | 71,0 m/s | 170 Pa | ✅ dihapus (revisi ujung pipa) |
| Gesek sepanjang pipa tirus | — | 100 Pa | tetap |
| Slot inlet (aliran teredam boks) | 13,9 m/s | 57 Pa | ✅ radius tepi |

**TB tetap penyempitan dengan rugi terbesar,** tapi hadiah dari memperbesarnya dibatasi rugi itu sendiri (§6). Port kepala adalah **penampang tersempit** saluran, dan menentukan rpm peak — itu yang digarap di §5.

---

## 4. Saluran di luar kepala — yang dikerjakan

### 4.1 Revisi ujung pipa ke TB: 42,5 → 40mm langsung

Menghapus step 42,5→40 (170 Pa) dengan memperpanjang tirus pipa langsung ke Ø40, menyatu dengan spigot TB. **Nilai: ~170 Pa.**

### 4.2 Bellmouth di mulut pipa

| | |
|---|---|
| Radius | **R8** pada mulut Ø65,8mm |
| Nilai | ~250 Pa (dari K=0,9 menonjol ke K=0,05) |
| Kendala | tinggi bagian depan boks cuma **100mm** — OD mulut+bellmouth (Ø86mm) nyaris mentok |
| Opsi A | **penampang oval** CSA-setara (50×86,6mm), radius R8 penuh keliling, celah vertikal naik 7,1→15mm, ongkos gesek +6 Pa |
| Opsi B | **bellmouth menyatu ke dinding boks** (flanged inlet) — tidak ada bibir untuk diputari, rugi masuk turun lagi ke ~16 Pa, dan ukurannya justru lebih kecil dari opsi berdiri bebas |

**Opsi B direkomendasikan** kalau ruang depan boks memang mentok rangka.

### 4.3 Material manifold: PPS-CF (bukan aluminium)

| | Efek |
|---|---|
| Jalur panas dari head (efek sirip) | aluminium menyalurkan panas ~100mm ke hilir; PPS-CF berhenti di ~6mm |
| Estimasi penurunan IAT | **~1,3 K** |
| Estimasi gain | **+0,17 hp** |

PPS-CF material yang benar untuk part yang menempel head. **Pipa juga sebaiknya PPS-CF untuk versi permanen** (PETG melunak ~80°C; ABS diserang uap bensin dari reversion). PETG cukup untuk prototipe bentuk.

### 4.4 Boks: **selalu terpasang, tidak dibongkar untuk volume**

Volume terukur **4,5 L** sudah lolos kedua kriteria (Tahap 11 §10.2):

| Kriteria | Hasil di 4,5 L |
|---|---|
| Dekopling (≥5× volume kolom runner ~785cc) | 5,7× ✅ |
| Riak MAP (target <7%) | 6,5% ✅ |

### 4.5 Nipel MAP diberi peredam

Orifis **Ø0,8–1,0 mm** di jalur selang — 1 silinder speed-density adalah kasus riak terburuk, dan tabel dasarnya terkunci.

### 4.6 Piping: **panjang 227mm dipertahankan**

Total ~460 mm efektif menala **h2 di ~8.400 rpm** dan **h3 di ~5.600 rpm**. Setelah porting peak bergeser ke ~8.800–9.000, sehingga h2 tiba sedikit di bawah peak — itu justru melebarkan dataran tenaga (§8). **Jangan dipendekkan ke ~430 mm**: h2 akan bertumpuk tepat di peak, puncak sedikit naik tapi band menyempit.

---

## 5. Porting kepala — spesifikasi final

### 5.1 Kendala dan anggaran

| | |
|---|---|
| Batas peak power | **≤ 9.000 rpm** (MPS 22,8 m/s — stroke 76 adalah batas struktural mesin ini) |
| Yang tetap | klep 28 / 22,5, throat Ø25,5, TB 36, cam 260°, panjang tract |
| Anggaran aliran | **+7,1%** aliran efektif (kalibrasi mandiri: rpm peak berbanding lurus dengan aliran efektif pada K yang sama) |

Kerja kualitas (short turn, bowl, boss) juga menaikkan koefisien alir dan **ikut memakan anggaran yang sama**. Porting yang rapi di kepala OEM lazim memberi 5–15% — merapikan saja bisa menghabiskan anggaran.

### 5.2 Rantai penampang sasaran

**Semua angka di bagian ini bergantung pada luas flange yang sebenarnya (A₀).** Pinch sasaran dihitung dari A₀ yang terukur, bukan dari dua sumbu:

```
A_eff0      = 1 / √(1/A₀² + 1/1.021²)
A_eff_sasar = A_eff0 × rpm_sasaran / 8.400
pinch       = 1 / √(1/A_eff_sasar² − 1/1.021²)
```

| Bentuk flange 30 × 34 | A₀ | MGV port @8.400 | Pinch untuk peak 8.800 | Pinch untuk peak 9.000 |
|---|---|---|---|---|
| elips murni (0,785) | 801 mm² | 121 m/s | 865 | 900 |
| oval agak bersudut (0,87) | 887 | 109 | 966 | 1.009 |
| oval bersudut (0,92) | 938 | 103 | 1.026 | 1.075 |

Kalau flange ternyata oval bersudut, port-nya hampir sebesar throat, MGV-nya sudah di rentang sehat, dan **pinch 860–882 di bawah ini justru akan mengecilkan saluran** — peak turun di bawah 8.400. Tabel di bawah ini dan di §5.3 dihitung untuk kasus **elips murni**; untuk kasus lain, geser semua ukuran mengikuti tabel di atas.

| Stasiun | Luas | MGV @9.000 |
|---|---|---|
| TB Ø36 | 1.018 mm² | 102 m/s |
| **Ujung manifold cetak = pinch (bisa diganti)** | **860 / 870 / 882** | 120 / 119 / 117 |
| Flange port kepala (dibuka sekali) | **930 mm² = oval 32,0 × 37,0** | 111 |
| Dua cabang, **bersih** dari boss/batang | ≥ 475 per cabang | 109 |
| Bowl → throat (tetap) | 1.021 | 101 |

Setelah pinch, luas mekar sangat landai sampai throat (setengah-sudut bowl ~2,2°, jauh di bawah batas difuser 7°).

### 5.3 Pinch di manifold cetak — kenop rpm peak

| Ujung manifold | Oval | Step per sisi ke flange 930 | Peak (sebelum gain Cd) |
|---|---|---|---|
| 860 | 30,78 × 35,58 | 0,61 / 0,71 mm | ~8.770 rpm |
| **870** | **30,96 × 35,78** | 0,52 / 0,61 mm | **~8.830 rpm** |
| 882 | 31,17 × 36,03 | 0,42 / 0,48 mm | ~8.900 rpm |

Kepala dikerjakan **sekali** ke ukuran tetap; rpm peak disetel dengan mencetak manifold dengan ujung berbeda — murah dan bisa dibatalkan. Step 0,4–0,7 mm per sisi berfungsi sebagai anti-reversion dan tetap di atas toleransi cetak; rugi step-nya ~22 Pa (diabaikan).

Batas atas susunan ini: dengan flange 930 dan step 0,5 mm, ujung manifold paling besar ~882. Pinch di atas 900 butuh flange ~960.

### 5.4 Di dalam kepala

- **Tidak boleh ada penampang lebih kecil dari ujung manifold** di titik mana pun. Ukur via **cetakan silikon port + 3D scan**, hitung CSA sepanjang jalur. Titik yang kurang (biasanya di boss guide atau short turn) dikerjakan sampai ≥930, tidak lebih.
- **Cabang dihitung bersih.** Boss yang melintang miring memotong penampang: batang saja ~24 mm², boss OD 9–10 mm ~78–96 mm². Luas kotor cabang yang dibutuhkan 499–571 mm² (Ø25,2–27,0 setara) tergantung boss.
- **Boss guide dipendekkan keluar dari bowl**, ujungnya dibentuk tetesan air; guide tidak dipotong, sisakan dinding 1,5–2 mm (Tahap 3 §6.6).
- **Short turn** melengkung menerus, lantai port **tidak diturunkan**.
- **Bowl** di-blend ke seat tanpa step; potongan 60° menyatu mulus.
- **Bifurkasi** tajam, di tengah, dua cabang simetris.
- **Finishing isap 60–80 grit, arah silang — jangan dipoles.**
- Tebal dinding ke water jacket minimal **3 mm**.

### 5.5 Sisi buang — boleh agresif

`rpm_peak` ditentukan oleh sisi isap; sisi buang tidak menggeser peak selama bukan pembatas. Perbaikan port buang menaikkan BMEP (rugi pemompaan dan gas sisa turun) **tanpa memakan anggaran rpm**. Boss dibersihkan lebih agresif, short turn dan bowl di-blend, **dipoles**, flange disamakan dengan header.

Klep buang **tetap 22,5** — rasio buang/isap 0,646 hampir sama dengan Honda CRF450R (0,666).

### 5.6 Urutan kerja

1. Cetakan silikon port → 3D scan → **luas flange A₀ yang sebenarnya** dan peta CSA sepanjang jalur. Hitung ulang pinch dari A₀ (§5.2) sebelum langkah berikutnya — ini yang menentukan apakah flange perlu dibuka sama sekali
2. Buka flange ke luas pinch + step (untuk kasus elips: 32,0 × 37,0); kerjakan interior sampai tidak ada titik < ujung manifold
3. Semua item kualitas (§5.4) + sisi buang (§5.5)
4. Cetak manifold dengan ujung **860 dan 870**
5. Flow bench per klep kalau ada; dyno — catat di rpm berapa peak mendarat
6. Peak < 8.700 → cetak 882. Peak 8.700–9.000 → selesai. Peak > 9.000 → cetak ujung lebih kecil
7. Setel ulang CVT ke peak yang baru

### 5.7 Kalau suatu saat mengincar 9.500 rpm

Butuh massa bolak-balik ≤ **387 g** (dari ~495 g) supaya beban big end sama dengan hari ini (Tahap 8 §1.4). Profil porting tinggal diteruskan: pinch ~995, flange ~1.030 (kasus flange elips; hitung ulang dari A₀ terukur) — semua potongan di atas searah dengan tahap itu.

---

## 6. Yang TIDAK dikerjakan, dan alasannya

| Tidak dikerjakan | Alasan |
|---|---|
| TB 43–44 mm | +0,15–0,30 hp (dibatasi total rugi TB), ongkos di bukaan kecil. Kalau suatu saat naik, **Ø40** adalah ukuran setara proporsi Honda (Tahap 11 §5.3, §11) |
| Downdraft | tanpa boks −2 s/d −5 hp: udara panas + tract maksimal ~280 mm cuma bisa menangkap h3. Downdraft sendiri tidak salah — CRF450R memakainya **dengan** airbox |
| Melepas boks | kehilangan udara dingin −1,3 s/d −3,7 hp, jauh melebihi untung rugi saluran |
| Membesarkan volume plenum | sudah lolos kedua kriteria di 4,5 L |
| Cam durasi lebih panjang | menggeser peak melewati batas 9.000; plafon HP dikunci luas throat (Tahap 4 §3.5) |
| Memperbesar throat / TR 0,935 | throat sudah lebih besar dari port; dikunci pemilik |
| Klep buang Ø24–25 | tidak dibutuhkan: throat buang 22,5 dilewati ~1,24× kecepatan titik tersempit isap, jauh di bawah jangkar Mesin Contoh A (~1,5×) — sisi buang sudah lega, juga setelah porting (Tahap 3 §5.5). Sasaran 1,15–1,20 yang sempat dipakai dalam konsultasi tidak didukung data |
| Memendekkan tract ke 430 mm | h2 bertumpuk di peak, band menyempit |

---

## 7. Perkiraan gain — jujur soal skalanya

Semua angka hp di bawah **pada dyno yang sama** (§2.6).

| Sumber | Perkiraan |
|---|---|
| Manifold PPS-CF (efek sirip mati) | +0,17 hp |
| Bellmouth + hapus step + bore halus | +0,15 hp |
| **Porting kepala ke anggaran +7,1%** | **peak ~8.800–9.000 rpm, ~43,5 hp** (BMEP dipertahankan) |
| Sisi buang digarap | kenaikan BMEP tanpa menggeser peak — besarnya ditunggu dyno |
| **Boks selalu terpasang** | **+1,3 – 3,7 hp** dibanding tanpa boks |

Di bawah batas 9.000 rpm, tenaga cuma punya satu tuas yang tersisa: **BMEP** (`HP ∝ BMEP × Vd × rpm`, Vd dan rpm terkunci). Plafon realistis NA RON98 ~13,0–13,5 bar → **~43–45 hp**.

---

## 8. Powerband lebar untuk CVT

Di CVT, "lebar" berarti: dataran rata ±500 rpm di rpm tahan CVT, torsi cukup di rpm kopling mencengkeram, dan part-throttle yang bersih.

1. **Penalaan berlapis** — h3 (~5.600) menopang start, h2 (~8.400) menopang sisi bawah peak, porting menopang sisi atas. Tract tidak diubah.
2. **Boks selalu terpasang** — juga menstabilkan tekanan di mulut pipa di bukaan kecil (gejala tanpa boks: "ngorok" di TPS 10–25%).
3. **Pinch 860–870** untuk tengah yang lebih berisi; 882 untuk karakter lebih ke atas.
4. **Knalpot ditala ke ~7.000 rpm** — mengisi celah antara h3 dan h2. Jangan ditala ke rpm yang sama dengan isap.
5. **Mapping timing & AFR di 5.500–7.500 rpm** — sering tertinggal karena peta disetel untuk peak.
6. **Sprocket cam adjustable** untuk menggeser karakter (SOHC: isap dan buang bergeser bersama; 1° sprocket = 2° engkol). Durasi tidak diubah.
7. **Rasio kompresi** — menaikkan BMEP di semua rpm, paling terasa bawah-tengah.
8. **CVT disetel terakhir**, di atas kurva hasil dyno: kopling masuk ~5.500, rpm tahan 8.400–8.700 (tengah dataran, bukan tepat di peak), per CVT untuk respons kickdown.

---

## 9. Yang masih perlu diukur

| # | Yang diukur | Cara | Mengunci apa |
|---|---|---|---|
| 1 | **Luas flange isap (A₀) dan CSA sepanjang port** — WAJIB sebelum porting | cetakan silikon + 3D scan | seluruh ukuran porting §5 (801 vs 938 mm² menggeser pinch dari 900 ke 1.075) |
| 2 | **Rpm tahan CVT** saat akselerasi penuh | tacho yang bisa dibaca saat jalan (Tahap 9 §3.1) | setelan roller/per |
| 3 | **Run dyno dengan locked ratio pulley** | atau umpankan rpm asli dari pickup pengapian | sumbu rpm dan kurva torsi |
| 4 | **Motor acuan di dyno yang sama** | satu motor yang tenaganya diketahui | seberapa tinggi dyno membaca (§2.6) |
| 5 | Rasio kompresi | cc-ing ruang bakar | ruang untuk menaikkan BMEP |
| 6 | Ukuran knalpot + durasi buang | ukur | penalaan knalpot ke ~7.000 |
| 7 | Panjang rod, jenis bantalan crank, berat paket piston | ukur/timbang | batas rpm mekanis yang sebenarnya |
| 8 | Ruang bebas riil di depan boks | CAD/scan | opsi bellmouth A vs B |

---

*Metode: Advanced Engine Tuning — Tahap 3 §5.4, §6.5–6.6 (rasio port/throat, step anti-reversion, boss guide), Tahap 4 §3.4–3.5, §3.7 (kalibrasi time-area per mesin, invarian bore-up, kepenuhan lobe), Tahap 7 (saluran & bellmouth), Tahap 8 §1.4, §1.6 (massa bolak-balik, plain bearing), Tahap 9 §2–3 (rpm kerja CVT), Tahap 11 §3.4, §5.3, §7–11 (basis kalibrasi, TB, studi kasus plenum, uji BMEP, diagnosis rasio, pembanding CRF450R).*
