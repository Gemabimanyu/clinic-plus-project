# LAMPIRAN

---

## A. Rumus ringkas

### A.1 Geometri

```
Kapasitas       Vd = π/4 × bore² × stroke
Ruang bakar     Vc = Vd / (CR − 1)
Luas piston     A_p = π/4 × bore²
Luas klep       A_klep = n × π/4 × D_klep²
Luas throat     A_throat = n × π/4 × D_throat²
Luas tirai      A_tirai = n × π × D_klep × lift
Lift kritis     = A_throat / (n × π × D_klep)
Lebar seat      = (D_klep − D_throat) / 2
CSA oval        ≈ 0,92 × lebar × tinggi
Rasio rod       = panjang_rod / stroke
```

### A.2 Kinematika

```
MPS             = 2 × stroke[m] × rpm / 60
Posisi piston   s(θ) = r(1 − cos θ) + L − √(L² − (r sin θ)²)
Percepatan TDC  a = ω² × r × (1 + r/L),   ω = 2π × rpm/60
Gaya inersia    F = massa × a
```

### A.3 Aliran

```
MGV             = (A_piston / CSA) × MPS
Q_rata2         = Vd × (rpm/60) / 2 × VE
duty            = durasi_isap / 720
Q_puncak        = Q_rata2 / duty × (π/2)
Cf              = Q_nyata / (A_throat × √(2Δp/ρ))
K               = (v_teoretis / v_nyata)² − 1
Δp_rugi         = K × ½ × ρ × v²
v_teoretis      = √(2Δp/ρ)      [28"H₂O → 107,6 m/s; 10" → 64,3 m/s]
CFM             = m³/s × 2118,88
CFM_28          = CFM_10 × √2,8
```

### A.4 Kompresi

```
CR              = (Vd + Vc) / Vc
DCR             = 1 + (V_sapu_IVC / Vd) × (CR − 1)
CR untuk DCR    = 1 + (DCR − 1) × Vd / V_sapu_IVC
Efisiensi ideal η = 1 − 1/CR^0,4
Vc total        = pentroof + gasket + deck + kantong − dome
```

### A.5 Camshaft

```
durasi_in       = IVO_BTDC + 180 + IVC_ABDC
durasi_ex       = EVO_BBDC + 180 + EVC_ATDC
overlap         = IVO_BTDC + EVC_ATDC
ICL             = durasi_in/2 − IVO_BTDC        (ATDC)
ECL             = durasi_ex/2 − EVC_ATDC        (BTDC)
LSA             = (ICL + ECL) / 2
lift(θ)         = lift_maks × sin²(π θ / durasi)      [pendekatan harmonik]

durasi_baru     = durasi_acuan × (A_thr_acuan / A_thr_baru)
                                × (Vd_baru / Vd_acuan)
                                × (rpm_baru / rpm_acuan)

luas overlap/cc = n_klep × π × D_klep × lift_TDC / kapasitas
```

### A.6 Valvetrain

```
Percepatan nose a = (lift/2) × (2π/Φ_cam)² × ω_cam²
                    Φ_cam dalam radian cam = durasi_crank/2
                    ω_cam = 2π × (rpm/2) / 60
Gaya inersia    F = massa_rakitan × a
Per dibutuhkan  = F × faktor_aman / 9,81      [kgf], faktor 1,3–1,5
```

### A.7 Gelombang

```
Kecepatan suara c = 20,05 × √(T[K])
                    [45 °C → 357 m/s; gas buang ~1100 K → 650 m/s]
Runner isap     L = c × durasi / (12 × n × rpm)
Header buang    L = c_gas × (180 + EVO_BBDC) / (12 × n × rpm)
Koreksi ujung   L_efektif = L_fisik + k × jari-jari
                    k = 0,61 pipa polos, 0,85 bellmouth
Helmholtz       f_H = (c/2π) × √(A / (V_eff × L_eff))
                V_eff = V_cyl × (CR+1) / (2(CR−1))
```

### A.8 Bahan bakar dan pengapian

```
Lambda          λ = AFR / AFR_stoikiometri
Energi/kg udara = LHV / AFR
Pendinginan     ΔT = panas_laten / AFR / 1,005      [K]
```

### A.9 CVT dan penyaluran

```
Kecepatan       v[km/h] = 0,06 × π × D_roda[m] × rpm / i_total
Rasio dari data i_total = 0,06 × π × D_roda × rpm / v_terukur
Tenaga          HP = (Nm × rpm) / 7127
                PS = (Nm × rpm) / 7024
                kW = (Nm × rpm) / 9549
Percepatan      a = (P_roda − rugi) / (massa × v)
```

### A.10 Pemuaian termal

```
Δpanjang        = panjang × α × ΔT
α aluminium     = 23 × 10⁻⁶ /K
α baja          = 12 × 10⁻⁶ /K
α titanium      = 8,6 × 10⁻⁶ /K
α besi cor      = 11 × 10⁻⁶ /K
```

---

## B. Perkakas hitung

Semua ada di direktori `tools/`, ditulis dengan Python. Tiap berkas punya `_selfcheck()` yang harus lolos sebelum hasilnya dipakai.

| Berkas | Fungsi | Tahap |
|---|---|---|
| `konfigurasi.py` | bandingkan square/overbore/overstroke | 2 |
| `port_design.py` | sizing klep, throat, port, kalibrasi | 3 |
| `exhaust_check.py` | proporsi ex/in, keputusan durasi ex | 3 |
| `cam_design.py` | DCR, durasi, overlap, kantong klep, anggaran ruang bakar | 4 |
| `cam_dari_acuan.py` | urai timing acuan, skalakan ke mesin baru | 4 |
| `kompresi_terkalibrasi.py` | batas DCR dari mesin terbukti | 5 |
| `bahan_bakar.py` | energi per kg udara, lambda, pendinginan muatan | 5 |
| `intake_tune.py` | panjang runner, Helmholtz, wave tuning | 7 |
| `tract_profile.py` | profil luas sepanjang saluran, perbandingan TB | 7 |
| `exhaust_system.py` | port buang, header, harmonik panjang | 7 |
| `valvetrain.py` | percepatan klep, gaya inersia, kebutuhan per | 8 |
| `cvt_gearing.py` | rasio, kecepatan, pemilihan gear | 9 |
| `spek_final.py` | rangkuman spek + beban mekanis | — |
| `hp_per_liter.py` | tenaga spesifik, perkiraan HP dari lintasan | — |
| `bandingkan_mesin.py` | perbandingan mesin balap dunia | — |
| `port_geom.py` | generator volume fluida port untuk CFD | 10 |
| `cfd_case.py` | pembangun case CFD | 10 |
| `report_case.py` | tarik hasil CFD, periksa kelayakan | 10 |
| `slice_fig.py` | irisan medan CFD | 10 |
| `diag_profil.py` | profil kecepatan melintang bertanda | 10 |

---

## C. Daftar periksa build

### C.1 Sebelum merancang

**Data mesin acuan** (yang sudah terbukti jalan)
- [ ] Bore, stroke, panjang rod
- [ ] Diameter klep isap dan buang
- [ ] **Diameter dalam seat (throat)** isap dan buang
- [ ] **CSA port di titik tersempit** — isap dan buang
- [ ] Timing cam lengkap **dan pada lift berapa diukur**
- [ ] Lift maksimum
- [ ] Kompresi statis **terukur dengan buret**
- [ ] Jenis bahan bakar
- [ ] Diameter throttle body
- [ ] **Panjang runner isap**
- [ ] Diameter dalam header
- [ ] **Panjang header** — dari klep sampai titik pelebaran
- [ ] RPM tenaga puncak
- [ ] Hasil terukur (dyno atau lintasan + berat)

**Yang paling sering hilang dan paling merugikan:**

| Data hilang | Akibat |
|---|---|
| Throat (bukan diameter klep) | perhitungan port meleset sampai 40% |
| Lift acuan timing cam | durasi salah baca sampai 20° |
| Panjang header | harmonik knalpot tidak bisa ditentukan |
| Vc terukur | kompresi meleset 1–2 angka penuh |

### C.2 Saat merancang

- [ ] Hitung DCR terbukti dari mesin acuan → itu batas bahan bakarmu
- [ ] Tentukan rpm sasaran dari **beban g** yang sudah terbukti, bukan dari rpm mutlak
- [ ] Hitung durasi dari time-area, bukan aturan jempol
- [ ] **Periksa silang ICL** dengan cam acuan
- [ ] Hitung CSA port dengan **dua jangkar** — kalau berbeda jauh, cari asumsi busuk
- [ ] Periksa rasio port/throat — jangan sampai port lebih kecil dari throat
- [ ] Periksa rasio throat ex/in → tentukan apakah cam simetris
- [ ] Hitung kantong klep **sebelum** menghitung dome piston
- [ ] Hitung anggaran volume ruang bakar lengkap
- [ ] Hitung kebutuhan per klep dari massa rakitan dan rpm sasaran
- [ ] Tentukan panjang runner dan header dari harmonik yang terbukti

### C.3 Sebelum merakit

- [ ] Bore diukur di 3 ketinggian × 2 arah
- [ ] Piston diukur di gauge point yang benar
- [ ] Clearance piston sesuai anjuran pabrik piston
- [ ] Ring gap diukur di bore, ring tegak lurus
- [ ] **Ring kedua gap-nya lebih besar dari ring atas**
- [ ] Rakitan klep ditimbang
- [ ] Per klep diukur dengan tester (seat dan open)
- [ ] Coil bind clearance ≥ 0,5 mm pada lift maksimum
- [ ] Kruk as diseimbangkan sesuai massa piston yang dipakai

### C.4 Saat merakit

- [ ] **Ujung expander ring oli bertemu, tidak tumpang tindih**
- [ ] Ring dipasang dengan alat, bukan tangan
- [ ] Tanda "TOP" pada ring menghadap atas
- [ ] Gap ring disebar, tidak di atas pin, tidak di sisi thrust
- [ ] Torsi baut sesuai spesifikasi dan urutan

### C.5 Sebelum diputar

- [ ] **Cek clay kelegaan klep-piston** — wajib, tanpa pengecualian
- [ ] Kalau rod aluminium, tambah margin 0,25 mm
- [ ] Verifikasi volume ruang bakar dengan buret
- [ ] Periksa lebar seat, terutama sisi buang
- [ ] Mesin diputar tangan dua putaran penuh tanpa hambatan
- [ ] Tekanan oli terbaca sebelum dinyalakan

### C.6 Saat tuning

- [ ] Mekanis sehat dulu — kompresi, kebocoran, celah klep
- [ ] Bahan bakar kasar ke λ aman (0,82–0,85)
- [ ] Cari MBT pengapian, **2° per run**
- [ ] Haluskan bahan bakar di sekitar rpm puncak
- [ ] Ulangi pengapian dan bahan bakar sekali lagi
- [ ] Setel sudut injeksi kalau ECU mendukung
- [ ] **Mundurkan pengapian 2°** sebagai margin akhir
- [ ] **Satu perubahan per run**

### C.7 Setelah jalan

- [ ] Baca busi setelah run beban penuh (bukan setelah idle)
- [ ] Periksa kondisi piston setelah beberapa run
- [ ] Setel CVT ke rpm tenaga puncak
- [ ] Uji variasi panjang header ±50 mm
- [ ] Verifikasi rpm di garis finish — mendekati puncak, tidak mentok limiter
- [ ] **Kalibrasi ulang perhitungan** dengan hasil nyata

---

## D. Data mesin contoh

### D.1 Mesin Contoh A — 199cc, 2 klep, drag matic

| Parameter | Nilai | Tanda |
|---|---|---|
| Bore × stroke | 63 × 64 mm = 199,5 cc | [UKUR] |
| Klep isap / buang | 31 / 27 mm | [UKUR] |
| Throat isap | 29 mm (rasio 0,935) | [UKUR] |
| Port isap | bundar Ø29,5 mm (683 mm²) | [UKUR] |
| Port buang | Ø29 mm (660 mm²) | [UKUR] |
| Lift | 10,8 mm | [UKUR] |
| Cam | IN 38 BTDC / 63 ABDC, EX 63 BBDC / 38 ATDC | [UKUR] |
| Durasi | 281° / 281° | [HITUNG] |
| Overlap | 76° | [HITUNG] |
| ICL / LSA | 102,5° ATDC / 102,5° | [HITUNG] |
| Lift di TDC | 1,83 mm per klep (3,67 gabungan) | [HITUNG] |
| Kompresi statis | 16:1 | [UKUR] |
| **DCR** | **12,83** | [HITUNG] |
| Bahan bakar | bensol / avgas 100LL | [UKUR] |
| Throttle body | 38 mm | [UKUR] |
| Header dalam / muffler | 30 / 50 mm | [UKUR] |
| Hasil | 500 m 15,4 s, trap 158 km/h | [UKUR] |

**Besaran turunan yang dipakai sebagai jangkar kalibrasi:**

| | Nilai |
|---|---|
| Luas klep isap / bore | 0,242 |
| Throat per cc | 3,31 mm²/cc |
| Kecepatan gas port isap | 97 m/s |
| Kecepatan gas port buang | 101 m/s |
| Rasio port/throat isap | 1,035 |
| Rasio port/throat buang | 1,49 |
| Rasio throat ex/in | 0,671 |
| Kecepatan puncak di TB | 61 m/s |
| MPS @10.000 rpm | 21,3 m/s |
| Perkiraan tenaga | ~28 HP crank, ~140 HP/L |

### D.2 Mesin Contoh B — 150cc, 4 klep, rancangan

| Parameter | Nilai |
|---|---|
| Bore × stroke × rod | 57,3 × 58 × 95 mm = 149,6 cc |
| Klep isap / buang | 22 / 19 mm |
| Throat isap / buang | 20,2 / 16,7 mm |
| Luas klep isap / bore | 0,295 |
| Throat per cc | 4,28 mm²/cc |
| CSA port isap | 615–665 mm², oval 22,7 × 29,5 |
| CSA port buang | 594–653 mm², Ø setara ~28 mm |
| Short-turn radius min | 11,8 mm |
| Bowl maksimum | 669 mm² |
| Cam in / ex | 261° / 261° @1mm |
| IN buka / tutup | 28° BTDC / 53° ABDC |
| EX buka / tutup | 53° BBDC / 28° ATDC |
| ICL / LSA | 102,5° / 102,5° |
| Overlap | 55° |
| Lift in / ex | 9,0 / 7,6–9,0 mm |
| Lift di TDC | 0,97 mm per klep isap |
| Kantong klep | 2,71 mm |
| CR statis | 14:1 (DCR 12,07, margin +0,76) |
| Dome piston | usir 2,45 cc |
| Throttle body | 36 mm |
| Runner isap | 155 mm |
| Header dalam | 29,1 mm |
| RPM sasaran | 12.000 (6.093 g di TDC) |
| Potensi flow | 90,7 CFM @28" |
| Potensi tenaga | ~41 HP (~274 HP/L) |

### D.3 Mesin Contoh C — 155cc, 3 klep, standar

| Parameter | Nilai |
|---|---|
| Bore × stroke | 58 × 58,6 mm = 154,8 cc |
| Katup | 3 klep (2 isap + 1 buang) |
| Pendingin | udara |
| CR standar | 10,5:1 |
| Tenaga standar | 12,7 HP @ 7.750 rpm (82 HP/L) |
| Luas klep isap / bore | 0,262 |
| Rasio throat ex/in | 0,679 |
| Lift kritis in / ex | 4,59 / 5,03 mm |
| Klep maksimum yang muat | isap 21,5 mm ×2, buang 26,7 mm ×1 |
| Potensi flow (klep maks) | 89 CFM @28" |
| Potensi tenaga | ~40 HP |
| CR disarankan | 12,5–13:1 (bukan 14, karena busi menepi) |

---

## E. Perbandingan mesin balap dunia

Semua dihitung dengan definisi yang sama dari spesifikasi bore/stroke/rpm publik. **Diameter klep dan CSA port tidak dipublikasikan pabrikan** — dipakai proporsi lazim di kelasnya. Ini perkiraan beralasan, bukan data pabrik.

| Mesin | MPS | Klep/bore | v throat | v port | HP/L |
|---|---|---|---|---|---|
| F1 V10 3.0L (19.000 rpm) | 25,2 | 0,296 | 105 | 95 | 317 |
| F1 V8 2.4L (18.000 rpm) | 23,9 | 0,296 | 99 | 90 | 312 |
| F1 V6 turbo 1.6L | 23,0 | 0,289 | 98 | 89 | 562* |
| MotoGP 1000 I4 (18.000 rpm) | 29,1 | 0,296 | 121 | 112 | 290 |
| Drag V8 8,2L NA 2 klep (10.500 rpm) | 32,0 | 0,297 | 133 | 106 | 165 |
| Mesin Contoh A | 21,3 | 0,242 | 109 | 105 | ~140 |
| Mesin Contoh B | 23,2 | 0,295 | 97 | 94 | ~274 |

*\*turbo — tidak sebanding dengan yang NA*

**Pengamatan pokok:** kecepatan port semua mesin jatuh di **89–112 m/s**, dan rasio klep/bore semua mesin 4 klep jatuh di **0,289–0,297**.

Batas geometri dan batas mekanisnya universal. Yang membedakan F1 bukan kecepatan gasnya, tapi **stroke pendek** yang memungkinkan rpm tinggi pada kecepatan piston yang sama.

---

## F. Data terukur versus asumsi

Jangan memperlakukan semua angka di buku ini sama.

### F.1 Terukur — dipercaya

Semua data di Lampiran D yang bertanda [UKUR], plus:

| Data | Nilai |
|---|---|
| Manifold standar 150cc | port 30,2 → TB 38 mm, panjang 43 mm, belok 34° |

### F.2 Asumsi — verifikasi sebelum dipakai

| Data | Nilai dipakai | Catatan |
|---|---|---|
| Rod Mesin Contoh A | 105 mm | pengaruh ke DCR kecil (±0,07) |
| Throat buang Mesin A | 0,88 × klep | tidak diukur langsung |
| **Panjang header Mesin A** | tidak diketahui | **paling penting untuk diukur** |
| Massa motor + rider | 150 kg | menggeser perkiraan HP ±10% |
| CdA | 0,35 | menggeser perkiraan HP |
| Tinggi pent-roof | 3,5 mm | menggeser anggaran ruang bakar |
| Tebal gasket | 0,8 mm | ukur |
| Deck clearance | 0,5 mm | ukur |
| Klep & port mesin balap dunia | proporsi lazim | **bukan data pabrik** |
| Klep Mesin Contoh C | 21 / 26 mm | **bukan data pabrik** |
| Kecepatan suara gas buang | 650 m/s | ±8% ketidakpastian |
| Koefisien rugi butterfly | K = 0,25 | perkiraan |
| Cf untuk perkiraan flow | 0,62 | bisa berbeda ±15% |

### F.3 Dari simulasi — kuat untuk membandingkan

| Data | Nilai |
|---|---|
| Cf pipa lurus (kontrol) | 0,879 |
| Cf port 615/aspect 1,30/ST 0,40 | 0,849 |
| Koefisien rugi port | K = 0,387 |
| Ongkos tikungan 37° | 3,4% |

---

## G. Penutup

Ada satu benang yang menyatukan seluruh buku ini:

> **Ukur mesinmu sendiri. Itu sumber data terbaik yang kamu punya.**

Setiap kali buku ini bisa memilih antara tabel umum dan pengukuran dari mesin yang sudah terbukti jalan, pengukuran yang menang — dan setiap kali, tabel umum meleset dengan cara yang merugikan:

| Yang dikatakan tabel umum | Yang dikatakan mesin nyata | Kerugian kalau ikut tabel |
|---|---|---|
| Throat maksimum 0,90 × klep | jalan di 0,935 | **7,4% flow hilang** |
| Kecepatan TB 105 m/s | jalan di 61 m/s | **TB 8 mm terlalu kecil** |
| DCR maksimum 12,5 untuk bensin | jalan di 12,83 dengan avgas | kompresi diturunkan tanpa perlu |
| Lift berguna maksimum 0,25 × klep | jalan di 1,6–2,5× lift kritis | cam terlalu jinak |

Empat dari empat. Bukan karena bukunya salah, tapi karena buku itu ditulis untuk populasi mesin lain.

**Dan pelajaran kedua, dari bagian simulasi:**

> **Diagnostik yang hijau bukan bukti hasilnya benar.** Periksa kewarasan fisikanya, dan lihat datanya sendiri — bukan cuma ringkasannya.

Sebelas simulasi berturut-turut memberi hasil salah sementara setiap indikator numerik menyatakan sehat. Yang membongkarnya cuma dua hal: satu angka yang tidak masuk akal, dan keberanian untuk melihat medan alirannya langsung.

**Terakhir, dan yang paling penting:**

> **Buku ini memberi baseline, bukan jaminan.**

Selisih 10–25% antara perhitungan dan kenyataan itu normal. Perhitungan menyingkirkan pilihan yang jelas salah dan menghemat waktu serta uang. Ia tidak menggantikan pengukuran, dan tidak pernah bisa.

Bangun. Ukur. Kalibrasi ulang. Bangun lagi.

---

*Dokumen ini disusun tanpa gambar. Diagram, grafik dyno contoh, dan visualisasi medan aliran dapat ditambahkan pada revisi berikutnya.*
