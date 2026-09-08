# XMAX 344cc — Build Spec Final

**Dokumen kerja.** Semua angka di sini diturunkan dari spesifikasi dan pengukuran mesin ini sendiri, memakai metode di *Advanced Engine Tuning* Tahap 4 (Camshaft), Tahap 7 (Saluran), Tahap 9 (CVT), dan Tahap 11 (Kalibrasi).

Terakhir diperbarui: 7 September 2026 — revisi setelah pengukuran CAD/3D-scan menggantikan asumsi geometri awal.

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

### 1.2 Kepala silinder

| | |
|---|---|
| Klep isap | 28,0 mm × 2 |
| Klep buang | 22,5 mm × 2 |
| Rasio throat/klep | 0,935 |
| **Luas throat isap total** | **1.077 mm²** |
| Rasio klep isap / bore | 0,368 (2 klep × 28 / 76) |
| Porting | standar, dirapikan (tidak diperbesar) |

### 1.3 Camshaft

| | |
|---|---|
| Durasi | **260°** |
| Status | sudah dimodifikasi |

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

Diturunkan dari uji BMEP (rentang 11,5–13,0 bar terhadap 40,6 hp). Cek silang kecepatan port/piston di rentang itu semua di bawah batas mesin tertala (Tahap 3/8). **Lolos.**

### 2.5 Validasi lapangan — cocok dengan pipa 227mm yang sudah dibuat

Setelah pipa 227mm terpasang dan diuji **tanpa boks**, laporan pengendara: tendangan tenaga masuk **7.000–8.500 rpm**, jauh berbeda dari sebelum pipa dipasang.

Prediksi gelombang untuk kondisi tanpa boks (ujung bebas, k=0,61):

```
L efektif = 433 + 0,61 × 32,9 = 453 mm
h2        = 7.781 rpm
```

**Terukur: pusat pita 7.750 rpm. Selisih 0,4%.** Lebar pita prediksi (±10% dari titik tertala) = 7.003–8.559 rpm, terukur 7.000–8.500 — kedua metrik cocok.

Dengan boks terpasang (ujung ter-flange, k=0,82): **h2 = 7.674–8.408 rpm**, tergantung koreksi ujung persis — tetap di dalam rentang kerja 7.800–8.800 dari uji BMEP. **Dua metode independen (BMEP dan gelombang) saling menumpuk.**

> **Pelajaran yang menonaktifkan rekomendasi lama:** perbedaan rasa berkendara yang besar antara "sebelum" dan "sesudah" pipa terpasang adalah efek berpindah dari harmonik **h4 ke h2** — bukan efek boks. Rpm-nya nyaris sama; yang berubah kekuatan denyutnya. Jangan salah atribusi efek boks vs efek pipa saat mengevaluasi hasil.

---

## 3. Tumpukan rugi — dengan geometri terukur, bukan diasumsikan

**@8.400 rpm, aliran puncak** (`ρ` = 1,184 kg/m³, VE 0,85). Ini revisi total dari versi pertama dokumen ini, yang salah mengasumsikan pipa lurus Ø42,5mm dengan step tajam ke TB.

| Titik | v | Δp | Bisa diubah? |
|---|---|---|---|
| TB butterfly 36 mm | 87,7 m/s | **1.138 Pa** | ❌ TB tetap standar |
| Mulut pipa Ø65,8, menonjol ke plenum | 26,2 m/s | 367 Pa | ✅ radius |
| Kerucut TB 40→36 (spigot 32mm) | 71,0 m/s | 182 Pa | ✅ dihaluskan |
| Step sambungan 42,5→40 | 71,0 m/s | 170 Pa | ✅ dihapus (revisi ujung pipa) |
| Gesek sepanjang pipa tirus | — | 100 Pa | tetap |
| Slot inlet (aliran teredam boks) | 13,9 m/s | 57 Pa | ✅ radius tepi |

```
Total dapat diperbaiki  : ~520 Pa  ≈ 0,5% tekanan atmosfer
Rugi TB (tidak diubah)  : 1.138 Pa — tetap yang terbesar
```

**TB tetap penyempitan terbesar.** Klaim versi awal dokumen ini ("mulut pipa mengalahkan TB") gugur begitu geometri sebenarnya diukur — kecepatan di mulut Ø65,8mm cuma 26,2 m/s, bukan 62,9 m/s yang dihitung dari asumsi Ø42,5mm lurus. Lihat Tahap 11 §10.3 untuk pelajaran lengkapnya.

---

## 4. Yang dikerjakan — urut nilai, dan hasilnya kecil

### 4.1 Revisi ujung pipa ke TB: 42,5 → 40mm langsung

Menghapus step 42,5→40 (170 Pa) dengan memperpanjang tirus pipa langsung ke Ø40, menyatu dengan spigot TB. **Nilai: ~170 Pa.**

### 4.2 Bellmouth di mulut pipa

| | |
|---|---|
| Radius | **R8** pada mulut Ø65,8mm |
| Nilai | ~250 Pa (dari K=0,9 menonjol ke K=0,05) |
| Kendala | tinggi bagian depan boks cuma **100mm** — OD mulut+bellmouth (Ø86mm) nyaris mentok |
| Opsi A | **penampang oval** CSA-setara (50×86,6mm), radius R8 penuh keliling, celah vertikal naik 7,1→15mm, ongkos gesek +6 Pa |
| Opsi B | **bellmouth menyatu ke dinding boks** (flanged inlet) — tidak ada bibir untuk diputari, rugi masuk turun lagi ke ~16 Pa, dan ukurannya justru lebih kecil dari opsi berdiri bebas (mulut dalam 66×102,6mm, bukan OD 86mm) |

**Opsi B direkomendasikan** kalau ruang depan boks memang mentok rangka — bukan kompromi, tapi konfigurasi yang secara aerodinamis lebih baik untuk kasus ruang sempit ini.

### 4.3 Material manifold: PPS-CF (bukan aluminium)

| | Efek |
|---|---|
| Jalur panas dari head (efek sirip) | aluminium menyalurkan panas ~100mm ke hilir; PPS-CF berhenti di ~6mm |
| Estimasi penurunan IAT | **~1,3 K** |
| Estimasi gain | **+0,17 hp** |

Kecil, tapi PPS-CF tetap material yang benar untuk part yang menempel head — suhu kerja tinggi, stabil dimensi, dan sekalian menghapus efek sirip. **Pipa juga sebaiknya PPS-CF untuk versi permanen** (bukan PETG/ABS — PETG melunak ~80°C, terlalu dekat suhu ruang mesin; ABS diserang uap bensin dari reversion). PETG cukup untuk prototipe pengujian bentuk saja.

### 4.4 Boks: **dipertahankan, tidak dibongkar untuk volume**

Volume terukur **4,5 L** sudah lolos kedua kriteria (Tahap 11 §10.2):

| Kriteria | Hasil di 4,5 L |
|---|---|
| Dekopling (≥5× volume kolom runner ~785cc) | 5,7× ✅ |
| Riak MAP (target <7%) | 6,5% ✅ |

Tidak ada alasan membongkar boks demi volume. Yang layak dikerjakan kalau boks toh dibuka: radius bibir mulut pipa (§4.2) dan orifis peredam MAP (§4.5).

### 4.5 Nipel MAP diberi peredam

| | |
|---|---|
| Orifis | Ø0,8 – 1,0 mm di jalur selang |
| Alasan | 1 silinder speed-density = kasus riak terburuk, tabel dasar terkunci |

### 4.6 Piping: **panjang 227mm dipertahankan**

227mm bukan angka sembarang — ia menala h2 ke ~8.100 rpm, tengah rentang kerja 7.800–8.800 yang divalidasi dua metode independen (§2.4–2.5). **Jangan diubah** kecuali data baru (tacho jalan atau dyno locked-pulley) menggeser rentang kerja.

---

## 5. Yang TIDAK dikerjakan, dan alasannya

| Tidak dikerjakan | Alasan |
|---|---|
| Memperbesar throttle body ke 44mm | hanya +0,13 hp; TB tetap penyempitan terbesar tapi bukan prioritas dibanding item lain |
| Downdraft tanpa pipa | neraca rugi tikungan vs rugi masuk tipis (~140–420 Pa), membayar turun satu orde harmonik (h2→h3) — tidak sepadan |
| Melepas boks secara permanen | kehilangan udara dingin (tiap +10°C ≈ −1,3 hp) jauh lebih besar dari untung rugi saluran (~130 Pa ≈ 0,03 hp) |
| Membesarkan volume plenum | sudah lolos kedua kriteria di 4,5 L; menambah volume cuma menggeser resonansi airbox ke arah yang tidak pasti (dua model berselisih 65%) |
| Mengejar cam durasi lebih panjang tanpa alasan lain | plafon HP dikunci oleh luas throat (Tahap 4 §3.5) — durasi tanpa upgrade valve cuma memindahkan rpm, bukan menaikkan plafon |

---

## 6. Perkiraan gain — jujur soal skalanya

| Sumber | Perkiraan |
|---|---|
| Manifold PPS-CF (efek sirip mati) | +0,17 hp |
| Bellmouth + hapus step + bore halus | +0,15 hp |
| **Total dari seluruh pekerjaan saluran isap** | **~+0,3 hp (≈0,8%)** — di dalam derau dyno |
| **Boks dipasang kembali (kalau sedang dilepas)** | **+1,3 – 3,7 hp** — bergantung suhu ruang mesin |

**Saluran isap sudah mendekati selesai.** Nilai terbesar yang tersisa di area ini bukan di detail pipa — itu di memastikan boks selalu terpasang. Untuk tenaga lebih lanjut, tuasnya pindah ke luar saluran isap: rasio kompresi, cam, porting throat, sistem buang, dan penyetelan CVT ke rentang kerja 7.800–8.800 rpm yang baru diketahui (roller/per CVT kemungkinan masih disetel untuk asumsi peak lama di ~6.500 rpm).

---

## 7. Yang masih perlu diukur

| # | Yang diukur | Cara | Mengunci apa |
|---|---|---|---|
| 1 | **Rpm tahan CVT** saat akselerasi penuh | tacho yang bisa dibaca saat jalan (Tahap 9 §3.1) | apakah roller/per CVT perlu disetel ulang ke 7.800–8.800 rpm |
| 2 | **Run dyno dengan locked ratio pulley** | atau umpankan rpm asli dari pickup pengapian | seluruh sumbu rpm dan kurva torsi terkonfirmasi permanen |
| 3 | Ruang bebas riil di depan boks (untuk opsi bellmouth §4.2) | ukur dari CAD/scan | Opsi A (oval) vs Opsi B (menyatu dinding) |

---

*Metode: Advanced Engine Tuning — Tahap 3 §1 (plafon CFM & batas domainnya), Tahap 4 §3.4–3.5 (konstanta time-area, invarian bore-up), Tahap 7 (saluran & bellmouth), Tahap 9 §2–3 (rpm kerja CVT), Tahap 11 §7–10 (studi kasus plenum, uji BMEP, diagnosis rasio, rancang plenum dari sasaran).*
