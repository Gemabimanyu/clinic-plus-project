# ADVANCED ENGINE TUNING
## Panduan Membangun Mesin 1 Silinder Matic

**Dokumen Lengkap — 30.763 kata, 13 bab + Lampiran**

---

## DAFTAR ISI

1. **00-PENGANTAR** — Ruang lingkup, peringatan, peta belajar (1.942 kata)
2. **01-KAMUS-ISTILAH** — 21 istilah dalam 6 kelompok (3.014 kata)
3. **02-TAHAP1-MENGUKUR** — Torsi vs tenaga, dyno, pengumpulan data (2.101 kata)
4. **03-TAHAP2-KONFIGURASI** — Bore/stroke, jumlah klep, rasio rod (2.505 kata)
5. **04-TAHAP3-ALIRAN** — Head, klep, throat, port, porting (2.028 kata)
6. **05-TAHAP4-CAMSHAFT** — Timing, durasi, overlap, kelegaan klep (1.939 kata)
7. **06-TAHAP5-KOMPRESI-BBM** — Kompresi dinamis, bahan bakar, detonasi (2.433 kata)
8. **07-TAHAP6-PENGAPIAN-AFR** — Spark, AFR, busi, koil, ECU (2.956 kata)
9. **08-TAHAP7-SALURAN** — TB, runner, stack, knalpot (2.115 kata)
10. **09-TAHAP8-MEKANIK** — Material, ring, per klep, keandalan (3.359 kata)
11. **10-TAHAP9-CVT** — Transmisi, penyetelan, gear selection (1.772 kata)
12. **11-TAHAP10-SIMULASI** — CFD, validasi, jebakan simulasi (1.562 kata)
13. **12-LAMPIRAN** — Rumus, perkakas, daftar periksa, data mesin (3.037 kata)

---

# PENGANTAR

## Ruang lingkup

Buku ini khusus untuk **mesin 1 silinder, 4 langkah, transmisi CVT (matic)**, dengan konfigurasi katup 2, 3, atau 4 klep. Kapasitas acuan: **125–250 cc**.

**Yang TIDAK dibahas:** mesin multi-silinder, 2 langkah, transmisi manual bergigi, turbo/supercharger, diesel.

**Kenapa CVT dipisahkan:** CVT mengubah cara mesin harus ditala. Pada motor bergigi, lebar pita tenaga sangat penting karena putaran jatuh saat pindah gigi. Pada CVT, mesin bisa ditahan di satu titik putaran sepanjang akselerasi — sehingga **tenaga puncak jauh lebih penting daripada lebar pita**.

## PERINGATAN — baca ini sebelum melanjutkan

> **Buku ini memberi BASELINE, bukan jaminan.**

Setiap angka adalah titik awal yang beralasan, bukan hasil akhir yang pasti. Selisih 10–25% antara hitungan dan kenyataan itu normal.

**Cara memakai buku ini dengan benar:**
1. Pakai perhitungan untuk menentukan titik awal
2. Bangun mesinnya
3. **Ukur di dyno** — ini tidak bisa dilewati
4. Sesuaikan berdasarkan hasil ukur
5. Kalibrasi ulang perhitunganmu dengan hasil nyata

## Peta belajar — urutan yang benar

```
1. Mengukur          → tanpa ini semua cuma tebakan
2. Konfigurasi       → keputusan permanen
3. Head              → plafon tenaga
4. Cam               → di rpm berapa plafon tercapai
5. Kompresi + BBM    → seberapa efisien
6. Pengapian + AFR   → murah, cepat, berisiko
7. Saluran           → gelombang tekanan
8. Mekanik           → supaya tidak jebol
9. CVT               → supaya sampai ke roda
10. Simulasi         → opsional
```

---

# KAMUS ISTILAH

## KELOMPOK 1 — UKURAN DAN GEOMETRI

### CSA — Cross-Sectional Area
**Luas penampang saluran**

Untuk port 4 klep bercabang, CSA adalah **runner bersama** sebelum pecah dua — bukan CSA tiap cabang.

**Kesalahpahaman umum:**
- Menyebut port dalam diameter, bukan luas (pembedaan luas berskala dengan kuadrat diameter)
- Mengukur di tempat salah (seharusnya di titik tersempit, bukan di mulut flange)

### Throat
**Diameter dalam seat klep**

Pada lift tinggi, **throat adalah pembatas sesungguhnya**. Membesarkan throat adalah satu-satunya perubahan yang menaikkan plafon flow.

**Rentang rasio throat/klep:**
| Rasio | Keterangan |
|---|---|
| 0,85–0,88 | konservatif |
| 0,88–0,92 | balap lazim |
| 0,92–0,94 | agresif |
| > 0,94 | berisiko |

### Bore, Stroke, Rod

**Bore** menentukan klep maksimum yang muat.
**Stroke** menentukan kecepatan piston pada rpm tertentu.
**Rod** mempengaruhi percepatan piston dan side thrust.

**Rasio rod khas:**
| Rasio | Keterangan |
|---|---|
| < 1,6 | sangat pendek |
| 1,6–1,75 | pendek |
| 1,75–1,9 | umum |
| > 1,9 | panjang |

## KELOMPOK 2 — KECEPATAN DAN ALIRAN

### MPS — Mean Piston Speed
```
MPS = 2 × stroke[m] × rpm / 60
```

| MPS | Keterangan |
|---|---|
| < 20 m/s | aman |
| 20–22 | tinggi tapi wajar drag |
| 22–24 | sangat tinggi, perlu part serius |
| > 24 | ekstrem |

### MGV — Mean Gas Velocity
```
MGV = (luas piston / CSA) × MPS
```

**Dua konvensi berbeda:**
| Konvensi | CSA | Nilai khas |
|---|---|---|
| Di port | CSA port | 90–115 m/s |
| Di throat | luas throat | 95–135 m/s |

**Kesalahpahaman umum:** Mengecilkan TB TIDAK menaikkan MGV di port (MGV ditentukan oleh CSA port, bukan TB).

### Cf — Koefisien Flow

| Cf (acuan throat) | Keterangan |
|---|---|
| < 0,50 | jelek |
| 0,55 | standar pabrikan |
| 0,62 | porting bagus |
| 0,70 | porting sangat bagus |
| 0,85–0,95 | saluran tanpa klep |

### VE — Volumetric Efficiency

| VE | Keterangan |
|---|---|
| 0,75–0,85 | mesin standar |
| 0,85–0,95 | diporting |
| 0,95–1,05 | balap tertala baik |
| > 1,05 | tuning gelombang bekerja sangat baik |

## KELOMPOK 3 — KOMPRESI

### CR — Compression Ratio
```
CR = (Vd + Vc) / Vc
Vc = pent-roof + gasket + deck clearance + kantong klep − dome piston
```

| CR | Keterangan |
|---|---|
| 9–11 | standar bensin |
| 11–13 | tune-up, bensin oktan tinggi |
| 13–16 | balap, bensin balap / avgas |
| 16+ | metanol, atau IVC sangat telat |

### DCR — Dynamic Compression Ratio

```
DCR = 1 + (V_sapu_saat_IVC / Vd) × (CR − 1)
```

**DCR yang menentukan detonasi, bukan CR.**

**Kesalahpahaman umum:**
- DCR berubah dengan rpm (tidak, DCR murni geometri)
- CR tinggi selalu berarti DCR tinggi (tidak, IVC telat menurunkan DCR)

---

# TAHAP 1 — MEMAHAMI APA YANG DIUKUR

## 1. Torsi versus tenaga

### Hubungan keduanya

```
Tenaga = torsi × kecepatan sudut
HP = (Nm × rpm) / 7127
```

Torsi dan tenaga bukan dua hal yang bersaing — **tenaga adalah torsi dikali putaran**.

### Mana yang penting untuk akselerasi

**Tenaga.** Bukan torsi.

```
a = (Tenaga_di_roda − rugi) / (massa × kecepatan)
```

Torsi di **roda** yang penting, dan torsi roda = torsi mesin × rasio. Rasio bisa diubah, tapi tenaga tidak bisa dikalikan.

### Mitos "stroke panjang lebih bertorsi"

Untuk **kapasitas sama**, torsi teoretisnya sama — tidak peduli square, overbore, atau overstroke.

Yang berbeda adalah **di putaran berapa torsi puncak terjadi**. Overstroke punya bore kecil → luas klep terbatas → napasnya habis di rpm lebih rendah → torsi puncak turun ke rpm rendah.

**Itu yang terasa "bertorsi", padahal sebenarnya "kehabisan napas lebih awal".**

## 2. Powerband

**Powerband** = rentang di mana tenaga berada di atas ~90% dari puncaknya.

### Pertukaran: lebar pita vs tinggi puncak

| | Pita lebar | Pita sempit |
|---|---|---|
| Durasi cam | pendek | panjang |
| Overlap | kecil | besar |
| Puncak tenaga | lebih rendah | lebih tinggi |
| Cocok untuk | motor bergigi | CVT, drag |

### Kenapa CVT mengubah aturannya

Motor bergigi: setiap pindah gigi menjatuhkan putaran. Butuh pita lebar.

**CVT tidak punya masalah itu.** Rasio berubah kontinu, mesin bisa ditahan di satu titik.

> **Pada CVT, yang perlu dioptimalkan adalah tenaga di SATU titik putaran, bukan lebar pita.**

## 3. Dyno

### Kenapa dyno wajib

Perubahan 2–5% tidak bisa dirasakan tapi menumpuk jadi signifikan. Tanpa dyno, akan sulit mengetahui apakah perubahan berhasil atau merugikan.

### Jenis dyno

**Inertia dyno** — mesin memutar drum bermassa diketahui. Cepat, murah, tapi tidak bisa menahan putaran tetap.

**Brake dyno** — punya rem yang bisa diatur. Bisa tuning steady-state per titik, tapi lebih mahal dan butuh pendinginan.

**Dyno mesin vs chassis** — untuk matic, dyno chassis yang relevan (termasuk rugi CVT).

### Prosedur yang benar

1. **Panaskan sampai suhu kerja stabil**
2. **Run pertama sebagai pemanasan** (jangan dicatat)
3. **Minimal tiga run** yang dicatat, ambil rata-rata
4. **Dinginkan antar run**
5. **Satu perubahan per sesi**
6. **Catat semuanya:** suhu, kelembaban, bahan bakar, setelan CVT, jam

**Poin 5 adalah yang paling sering dilanggar dan paling merugikan.**

---

# TAHAP 2 — MEMILIH KONFIGURASI DASAR

## 1. Square, overbore, overstroke

| Istilah | Rasio bore/stroke |
|---|---|
| Overstroke | < 1,0 |
| Square | = 1,0 |
| Overbore | > 1,0 |

### Perbandingan pada kapasitas sama (150 cc, 4 klep)

| Konfigurasi | Bore | Stroke | B/S | RPM maks | Potensi |
|---|---|---|---|---|---|
| Overstroke | 52,0 | 70,6 | 0,74 | 9.344 | **66%** |
| Square | 57,6 | 57,6 | 1,00 | 11.465 | **100%** |
| Overbore | 63,0 | 48,1 | 1,31 | 13.716 | **143%** |

**Rentangnya 66% sampai 143% — lebih dari dua kali lipat.**

### Kenapa overbore menang

1. **Klep lebih besar** (luas berskala dengan bore)
2. **Putaran lebih tinggi** (stroke pendek = MPS rendah di rpm tertentu)

### Kerugian overbore

- Jalur api lebih panjang (detonasi naik)
- Rugi panas lebih besar
- Piston lebih berat
- Terbatas crankcase

### Rekomendasi untuk matic drag

| Prioritas | Pilihan |
|---|---|
| Tenaga maksimum | overbore, B/S 1,15–1,35 |
| Seimbang | square sampai ringan overbore |
| Kompresi sangat tinggi | square |
| Harian + sesekali balap | square |

## 2. Kapasitas besar dengan klep kecil — KESALAHAN

Bore dinaikkan tapi head tidak diubah. Konsekuensinya:

| Hasil | Ketika bore 150cc → 200cc dengan head tetap |
|---|---|
| Torsi bawah naik | kapasitas naik |
| Tenaga puncak turun | head tercekik lebih awal |
| Puncak bergeser turun | mesin jadi "berat di atas" |

**Aturan praktis:** naikkan kapasitas dan luas throat **bersama-sama**.

## 3. Jumlah klep

| Arsitektur | Luas klep isap / bore | Keuntungan | Kekurangan |
|---|---|---|---|
| **2 klep** | 0,24–0,30 | sederhana, murah | terbatas di bore kecil |
| **3 klep** | ~0,26 | lebih baik dari 2 | klep buang panas |
| **4 klep** | 0,30–0,35 | **terbesar** | valvetrain rumit |

### Hukuman bore kecil

Yang membatasi adalah **bore**, bukan jumlah klep. Pada bore kecil, ruang tetap (busi, seat, gasket) memakan porsi besar relatif terhadap bore.

| Mesin | Bore | Klep isap | Luas klep/bore |
|---|---|---|---|
| Drag V8 big, 2 klep | 119 mm | 65 mm | **0,297** |
| Mesin Contoh A, 2 klep | 63 mm | 31 mm | **0,242** |
| Mesin Contoh B, 4 klep | 57,3 mm | 22 mm ×2 | **0,295** |

**Implikasi praktis:**
| Bore | Keuntungan pindah ke 4 klep |
|---|---|
| < 60 mm | **besar** — naik 25% |
| 60–80 mm | sedang |
| > 90 mm | kecil — 2 klep sudah cukup |

---

# TAHAP 3 — ALIRAN: KEPALA SILINDER

## 1. Kenapa head menentukan segalanya

```
Tenaga ≈ CFM × 0,43–0,50        [4 langkah, NA]
```

Kalau head-mu mengalirkan 85 CFM, tidak ada cam, knalpot, atau ECU yang bisa membuatnya menghasilkan 50 HP. Plafonnya sekitar 38 HP.

## 2. Throat: pembatas yang sesungguhnya

### Pada lift rendah, luas tirai yang membatasi
```
A_tirai = n_klep × π × D_klep × lift
```

### Pada lift tinggi, throat yang membatasi
```
A_throat = n_klep × π/4 × D_throat²
```

### Titik silang adalah lift kritis
```
lift_kritis = A_throat / (n_klep × π × D_klep)
```

### Membesarkan throat

**Ini satu-satunya perubahan yang menaikkan plafon flow.** Bentuk port hanya menentukan seberapa dekat ke plafon itu.

Batasnya lebar seat:
```
lebar_seat = (D_klep − D_throat) / 2
```

| Lebar seat | Keterangan |
|---|---|
| ≥ 1,2 mm | konservatif |
| 0,9–1,2 mm | balap lazim |
| 0,7–0,9 mm | agresif |
| < 0,7 mm | berisiko |

### Contoh penerapan

Mesin Contoh B: throat 19,5 mm → 20,2 mm.

| | Sebelum | Sesudah |
|---|---|---|
| Throat | 19,5 mm | 20,2 mm |
| Gain | — | **+7,4%** |
| CFM @28" | 84,5 | 90,7 |
| Potensi HP | 38,0 | ~41 |

## 3. CSA port — dua jangkar

**Jangkar kecepatan:**
```
CSA = luas_piston × MPS / MGV_target
```

**Jangkar rasio:**
```
CSA = rasio_port_throat_acuan × A_throat_baru
```

Kalau hasilnya berdekatan, kepercayaan naik. Kalau berbeda jauh, ada asumsi yang salah.

## 4. Short-turn radius

```
R_short_turn minimum ≈ 0,40 × tinggi port
```

**Menggerus short-turn terlalu tajam adalah kesalahan porting paling umum.**

---

# TAHAP 4 — TIMING: CAMSHAFT

## 1. Empat kejadian katup

| # | Kejadian | Menentukan |
|---|---|---|
| **1** | **IVC** | kompresi dinamis, rpm efisiensi |
| **2** | **Durasi + lift** | berapa banyak yang bisa lewat |
| **3** | **Overlap** | pembilasan |
| **4** | **EVO** | tukar kerja vs rugi pemompaan |

## 2. IVC dan kompresi dinamis

```
DCR = 1 + (V_sapu_saat_IVC / Vd) × (CR − 1)
```

IVC lebih telat → DCR lebih rendah.

**Konsekuensi penting:**
> **RPM sasaran, kompresi, dan bahan bakar adalah satu paket yang tidak bisa dipilih terpisah.**

Menaikkan rpm sasaran memaksa durasi lebih panjang → IVC lebih telat → DCR turun.

## 3. Durasi dari time-area

Yang harus dipertahankan adalah **jendela aliran per siklus per cc**:

```
time-area ∝ (A_throat × durasi) / (kapasitas × rpm)

durasi_baru = durasi_acuan × (A_thr_acuan / A_thr_baru)
                            × (Vd_baru / Vd_acuan)
                            × (rpm_baru / rpm_acuan)
```

### Hasil yang berlawanan intuisi

| Mesin | Kapasitas | Throat | RPM | Durasi |
|---|---|---|---|---|
| Contoh A | 199,5 cc | 661 mm² | 10.000 | 281° |
| Contoh B | 149,6 cc | 641 mm² | 12.000 | **261°** |

**Durasi turun walau rpm naik** — karena head 4 klep bernapas 29% lebih lega per cc.

## 4. Overlap

```
overlap = IVO_BTDC + EVC_ATDC
```

Yang harus dipertahankan adalah **luas tirai overlap per cc**:

```
luas_per_cc = n_klep × π × D_klep × lift_di_TDC / kapasitas
```

## 5. Kelegaan klep-piston

```
kebutuhan(θ) = lift_klep(θ) − turun_piston(θ)
kantong = maks(kebutuhan) × 1,25 + kelegaan_minimum
```

| Kelegaan minimum | Nilai |
|---|---|
| Isap | 1,0–1,5 mm |
| Buang | 1,5–2,0 mm |

> **Selalu cek dengan clay atau lilin sebelum mesin diputar. Tanpa pengecualian.**

---

# TAHAP 5 — KOMPRESI DAN BAHAN BAKAR

## 1. Tiga angka kompresi

| Istilah | Definisi | Menentukan |
|---|---|---|
| **CR** | rasio volume BDC/TDC | rasio ekspansi |
| **DCR** | di posisi piston saat IVC | **detonasi** |
| **Rasio ekspansi** | sama dengan CR konvensional | efisiensi termal |

## 2. Anggaran volume ruang bakar

```
Vc_total = V_pentroof + V_gasket + V_deck + V_kantong − V_dome
```

**Kantong klep ikut menambah volume ruang bakar** — pada contoh, 14% anggaran.

> **Urutan yang benar: cam dulu → kantong klep → baru dome atau papasan.**

## 3. Bahan bakar

### Yang menentukan potensi tenaga

Bukan energi per kg bahan bakar, tapi **energi per kg UDARA**.

```
Energi per kg udara = LHV / AFR
```

### Perbandingan

| Bahan bakar | AFR stoich | AFR puncak | MJ/kg udara | vs bensin |
|---|---|---|---|---|
| Bensin 92 RON | 14,70 | 12,50 | 3,48 | 100% |
| **Avgas 100LL** | 14,90 | 12,80 | 3,40 | 98% |
| **Metanol** | 6,45 | 4,80 | **4,15** | **+19%** |

**Oktan tinggi tidak menambah tenaga** — ia memberi izin menaikkan kompresi dan memajukan pengapian.

**Metanol +19% energi per kg udara**, plus pendinginan muatan. Ongkosnya: konsumsi 2,45× lipat.

### Lambda lebih berguna daripada AFR

```
λ = AFR / AFR_stoikiometri
```

| λ | Artinya |
|---|---|
| 1,00 | stoikiometri |
| < 1,00 | kaya |
| > 1,00 | miskin |

**Target lambda hampir sama untuk semua bahan bakar (0,74–0,89)**, sementara target AFR berbeda total.

## 4. Mengkalibrasi batas detonasi

**Kalibrasi ke mesin terbukti**, bukan ke tabel umum.

Mesin Contoh A: CR 16:1, DCR 12,83, avgas 100LL — **terbukti bertahun-tahun**.

Tabel umum bilang 12,83 harus metanol. Mesin itu jalan dengan bensol.

---

# TAHAP 6 — PENGAPIAN DAN CAMPURAN

## 1. Lambda dan target AFR

**Puncak torsi di λ 0,87**, tapi kurvanya datar.

| Kondisi | λ |
|---|---|
| Idle | 0,98–1,02 |
| Cruise | 1,00–1,05 |
| Beban sedang | 0,90–0,95 |
| **Beban penuh, margin aman** | **0,80–0,85** |

**Untuk drag dengan kompresi tinggi:** λ 0,80–0,85. Kehilangan torsi ~1% dibanding puncak, tapi margin detonasi jauh lebih baik.

## 2. Sudut pengapian (MBT)

**MBT** = Minimum advance for Best Torque — sudut paling kecil yang sudah memberi torsi maksimum.

| Kondisi | Akibat |
|---|---|
| Kurang maju dari MBT | tenaga hilang |
| Tepat di MBT | tenaga maksimum |
| Lebih maju dari MBT | tenaga **turun**, detonasi naik |

**Memajukan pengapian melewati MBT tidak menambah tenaga** — ia cuma menambah tekanan dan risiko.

### Apa yang menggeser MBT

| Faktor | Efek pada MBT |
|---|---|
| RPM naik | **lebih maju** |
| Beban naik | **kurang maju** |
| Kompresi naik | **kurang maju** |
| Campuran lebih miskin | **lebih maju** |

## 3. Busi

### Heat range

| Busi | Karakter |
|---|---|
| **Panas** | insulator panjang, panas lambat keluar |
| **Dingin** | insulator pendek, panas cepat keluar |

**Aturan praktis:** satu tingkat lebih dingin untuk tiap kenaikan besar kompresi atau tenaga.

### Gap

| Kondisi | Gap |
|---|---|
| Standar | 0,7–0,9 mm |
| Kompresi tinggi | 0,6–0,7 mm |
| Kompresi sangat tinggi / metanol | 0,5–0,6 mm |

## 4. Koil pengapian

| Jenis | Durasi percikan | Kecepatan tegangan |
|---|---|---|
| **TCI** | panjang (1–2 ms) | sedang |
| **CDI** | pendek (0,1–0,3 ms) | **sangat cepat** |
| **Smart coil** | panjang | **tertinggi** |

**Untuk kompresi tinggi + rpm tinggi:** smart coil atau TCI berenergi tinggi.

## 5. ECU

### Batasan ECU standar

- Resolusi map kasar
- Rev limiter terkunci
- Closed loop dipaksa ke stoikiometri
- Rentang pengapian terbatas
- Sudut injeksi tidak bisa diubah

### Tiga tingkat solusi

**Remap ECU standar** — ubah nilai di tabel asli. Murah, reversibel, tapi terbatas.

**Piggyback** — alat yang mencegat sinyal sensor. Kompromi, bisa ada interaksi aneh.

**Standalone ECU** — kontrol penuh. Mahal, butuh wiring ulang, perlu tuner yang paham.

### Kapan naik tingkat

| Kondisi | Solusi |
|---|---|
| Knalpot + filter, cam standar | remap |
| Cam ringan, kompresi naik sedikit | remap atau piggyback |
| Cam balap, kompresi tinggi, rpm naik | **standalone** |
| Metanol atau race gas beroksigen | **standalone** |

---

# TAHAP 7 — SALURAN MASUK DAN BUANG

## 1. Throttle body

### Kecepatan target — kalibrasi, bukan tabel

Aturan umum menyebut 105 m/s. Mesin Contoh A berjalan di **61 m/s** dan tidak bermasalah.

### Kenapa mengecilkan TB TIDAK menaikkan gas speed di port

**Kecepatan di port tidak bergerak sama sekali.**

| TB | v di TB | **v di port** | Rugi TB | Flow |
|---|---|---|---|---|
| 34 mm | 76 m/s | **97 m/s** | 872 Pa | −6,7% |
| 38 mm | 61 m/s | **97 m/s** | 559 Pa | −1,8% |
| 40 mm | 55 m/s | **97 m/s** | 455 Pa | 0,0% |

Kecepatan di port ditentukan oleh **luas port**. Debit sama, luas sama, kecepatan sama.

**Rugi port mendominasi rugi TB 4:1.** Port adalah tempat mencari tenaga, bukan TB.

## 2. Panjang runner isap

```
L = c × θ_durasi / (12 × n × rpm)
c = 20,05 × √(T[K])
```

**Kecepatan suara:** pakai suhu **dalam runner** (45°C), bukan ambient (25°C). Selisih 3% pada c berarti 3% pada panjang.

### Menentukan harmonik

**Model gelombang tidak bisa memberitahu harmonik mana yang dipakai mesinmu.**

Ukur panjang runner mesin yang sudah terbukti, cocokkan dengan tabel pada rpm mesin itu. Baris yang cocok adalah harmonik yang terbukti.

### Manifold standar sangat pendek

Manifold standar motor matic 150cc: **43 mm** dari port ke TB. Untuk sasaran 12.000 rpm butuh **155 mm** — hampir empat kali lipat.

## 3. Velocity stack dan plenum

### Radius bellmouth

```
R_bellmouth ≥ 0,15–0,20 × diameter saluran
```

| R/D | Cf |
|---|---|
| 0 (tajam) | ~0,60 |
| 0,05 | ~0,80 |
| 0,10 | ~0,90 |
| **0,15–0,20** | **~0,97** |
| 0,25+ | ~0,98 (jenuh) |

### Susunan pelebaran yang benar

**Melebar bertahap dan mulus**, dari kecil ke besar:

```
throat → port head → manifold → throttle body → velocity stack
```

Aliran mempercepat terus-menerus. Sekali ada pelebaran di tengah, aliran melambat dan separasi terjadi.

**JANGAN buat TB lebih kecil dari port lalu melebar lagi.**

## 4. Sistem buang

### Port buang

Port buang jauh lebih besar relatif terhadap throat-nya dibanding port isap, karena gas buang panas volumenya berlipat.

Rasio port/throat port buang: **1,49** (vs port isap **1,035**).

### Panjang header

```
t = (180 + EVO_BBDC) / (6 × rpm)
L = c_gas × t / (2n)
c_gas ≈ 550–700 m/s
```

Gelombang tekanan positif melari menyusuri header. Di ujung (transisi ke muffler), memantul sebagai gelombang negatif dan kembali. Kalau tiba saat overlap, ia menarik sisa gas buang keluar dan muatan segar masuk.

**Panjang header adalah tersangka utama** kalau hasil jauh di bawah potensi head.

---

# TAHAP 8 — MEKANIK, MATERIAL, DAN KEANDALAN

## 1. Batas mekanis

```
MPS = 2 × stroke[m] × rpm / 60
a_TDC = ω² × r × (1 + r/L)
```

| MPS | Keterangan |
|---|---|
| < 20 m/s | aman |
| 20–22 | tinggi tapi wajar drag |
| 22–24 | sangat tinggi |
| > 24 | ekstrem |

## 2. Material piston

| Jenis | Pemuaian | Kekuatan | Clearance | Cocok untuk |
|---|---|---|---|---|
| **Cor** | rendah | rendah | 0,0015–0,002 mm/mm | standar |
| **Hypereutectic** | sangat rendah | sedang | 0,0015–0,002 | harian performa |
| **Tempa 4032** | sedang | tinggi | 0,002–0,0025 | jalanan |
| **Tempa 2618** | **tinggi** | **tertinggi** | 0,0035–0,005 | **balap penuh** |

### Massa piston adalah tuas paling murah

Turun dari 120 ke 80 gram memangkas beban rod **33%** — setara menurunkan rpm dari 13.000 ke 11.000, tanpa kehilangan tenaga sedikit pun.

## 3. Material klep

| Material | Densitas | Karakter |
|---|---|---|
| **Stainless** | 7,8 | umum, tahan panas cukup |
| **Inconel** | 8,2 | tahan panas tinggi |
| **Titanium** | 4,5 | **40% lebih ringan** |

### Pengaruh massa klep

Klep titanium menaikkan batas floating **4.200 rpm** dengan per yang sama.

## 4. Ring piston

### Single vs double ring

| | Single (1 kompresi) | Double (2 kompresi) |
|---|---|---|
| Gesekan | **lebih rendah** | lebih tinggi |
| Blowby | lebih tinggi | **lebih rendah** |
| Umur | lebih pendek | lebih panjang |
| Cocok untuk | **drag sprint** | endurance, harian |

### Ring end gap

```
gap = faktor × bore
```

| Aplikasi | Faktor ring atas | Faktor ring kedua |
|---|---|---|
| Balap NA | 0,0045–0,0055 | 0,0050–0,0060 |

**Ring kedua selalu diberi gap lebih besar** — kalau lebih kecil, ring flutter.

### Ring kedua gap HARUS lebih besar dari ring atas

> **Kedua ujung expander ring oli harus BERTEMU, tidak boleh saling tumpang tindih.**

## 5. Per klep

### Floating

Kalau per tidak mampu melawan inersia klep, follower terlepas dari cam. Klep memantul dan bisa menyentuh piston.

```
percepatan nose = (lift/2) × (2π/Φ_cam)² × ω_cam²
gaya inersia = massa × a
per dibutuhkan = F × 1,3–1,5
```

### Spring surge

Per punya frekuensi alami. Kalau beresonansi dengan harmonik cam, per bergetar hebat dan kehilangan kontrol.

**Solusinya:** per beehive, per ganda, atau damper.

### Coil bind

```
tinggi_terpasang − lift_maksimum ≥ 0,5–1,0 mm
```

Kalau kurang, per akan tertekan sampai lilitan menempel dan valvetrain akan hancur.

---

# TAHAP 9 — PENYALURAN TENAGA: CVT

## 1. Kenapa CVT mengubah aturan tuning

Motor bergigi: tiap pindah gigi jatuh putaran. Butuh pita lebar.

**CVT:** rasio berubah kontinu, mesin bisa ditahan di satu titik.

> **Pada CVT, yang perlu dioptimalkan adalah tenaga di SATU titik putaran, bukan lebar pita.**

## 2. Menyetel CVT

### Berat roller

| Roller | Efek |
|---|---|
| **Lebih berat** | terlempar keluar di rpm lebih rendah → mesin ditahan **lebih rendah** |
| **Lebih ringan** | terlempar lebih lambat → mesin ditahan **lebih tinggi** |

**Aturan praktis:** ubah 1 gram per langkah. Setel ke rpm tenaga puncak.

### Per torsi

| Per | Efek |
|---|---|
| **Lebih keras** | mesin ditahan rpm lebih tinggi |
| **Lebih lunak** | rasio bergeser mudah → rpm lebih rendah |

**Efek samping:** per terlalu keras → belt tertekan kuat, panas naik, tenaga terbuang.

### Per kopling

Menentukan **rpm sambungan** di mana kopling sentrifugal menggigit.

**Untuk drag:** rpm sambungan sekitar **60–70% dari rpm tenaga puncak**.

## 3. Rasio dan gear

```
v [km/h] = 0,06 × π × D_roda[m] × rpm / i_total
```

### Temuan yang mengejutkan

Simulasi akselerasi 500 m dengan 30 HP:

| i_total | v batas | Waktu | v finish |
|---|---|---|---|
| 6,5 | 195 km/h | **14,23 s** | 160 km/h |
| 7,5 | 169 | **14,23 s** | 160 |
| 8,5 | 149 | 14,45 s | 149 (mentok) |

**Selama limiter tidak tersentuh, rasio gear TIDAK mempengaruhi akselerasi.**

### Aturan praktis

> **Pilih gear supaya kecepatan di garis finish PAS mendekati kecepatan batas**, dengan margin 5–10%.

## 4. Di mana tenaga hilang di CVT

| Sumber | Besarnya |
|---|---|
| Slip belt | 3–15% |
| Gesekan belt–puli | 3–5% |
| Gesekan roller | 1–2% |
| Final gear | 2–3% |
| Kopling slip | 0–10% |

**Total 10–30%** — itulah selisih antara tenaga mesin dan tenaga di roda.

---

# TAHAP 10 — SIMULASI DAN VALIDASI

## 1. Alat yang tepat untuk pertanyaan yang tepat

| Pertanyaan | Alat |
|---|---|
| Panjang runner, header | **simulasi 1D** atau perhitungan gelombang |
| Diameter TB, CSA port | **perhitungan** |
| Mana bentuk short-turn lebih baik | **CFD 3D** |
| Berapa HP | **dyno** — bukan simulasi |

> **CFD kuat untuk MEMBANDINGKAN, lemah untuk memprediksi angka mutlak.**

## 2. Jebakan yang mahal

### Aturan yang paling penting

> **Jalankan kasus berjawaban pasti LEBIH DULU, bukan terakhir.**

Pipa bundar lurus dengan boundary condition sama **harus** memberi Cf 0,85–0,95.

**Diagnostik numerik tidak menangkap apa pun** — selama sebelas kasus yang salah, semua indikator hijau (mesh OK, ketimpangan massa 0%, residual turun 4 dekade).

Yang akhirnya menangkap bug:
1. **Nilai Cf yang tidak masuk akal fisika**
2. **Melihat tanda kecepatan aksial**, bukan besarnya (aliran balik −15,7 m/s terbaca "lambat")

> **Keseimbangan massa 0,000% bukan bukti hasilnya benar.**

### Lima bug yang ditemukan dan penjaganya

**Bug 1:** Pusat tutup bellmouth tidak sebidang dengan cincin penampang.
*Penjaga:* toleransi pusat 0,001 mm.

**Bug 2:** Klasifikasi patch outlet dengan uji jarak sederhana.
*Penjaga:* pakai normal segitiga, luas patch outlet ±10% luas throat.

**Bug 3:** Plenum berupa bola yang digeser ke depan mulut (62% aliran lewat 0,42% luas).
*Penjaga:* luas patch inlet ±20% dari luas setengah bola.

**Bug 4:** Bidang flange mewarisi refinement dinding (mesh 123 ribu → 615 ribu).
*Penjaga:* beri bidang flange region sendiri.

**Bug 5:** Mask plot terlalu ketat menciptakan lubang palsu.
*Penjaga:* ambang mask > diagonal sel terkasar.

---

# LAMPIRAN — DAFTAR PERIKSA DAN DATA

## Daftar Periksa Sebelum Merancang

**Data mesin acuan (yang sudah terbukti jalan)**
- [ ] Bore, stroke, panjang rod
- [ ] Diameter klep isap dan buang
- [ ] **Diameter dalam seat (throat)** isap dan buang
- [ ] **CSA port di titik tersempit** — isap dan buang
- [ ] Timing cam lengkap **dan pada lift berapa diukur**
- [ ] Kompresi statis **terukur dengan buret**
- [ ] Jenis bahan bakar
- [ ] **Panjang runner isap**
- [ ] **Panjang header** — dari klep sampai titik pelebaran
- [ ] RPM tenaga puncak
- [ ] Hasil terukur (dyno atau lintasan)

**Yang paling sering hilang:**
| Data | Akibat |
|---|---|
| Throat | perhitungan meleset 40% |
| Lift acuan cam | durasi salah baca 20° |
| Panjang header | harmonik tidak bisa ditentukan |
| Vc terukur | kompresi meleset 1–2 angka |

## Daftar Periksa Sebelum Diputar

- [ ] **Cek clay kelegaan klep-piston** — wajib
- [ ] Kalau rod aluminium, tambah margin 0,25 mm
- [ ] Verifikasi volume ruang bakar dengan buret
- [ ] Mesin diputar tangan 2 putaran tanpa hambatan
- [ ] Tekanan oli terbaca sebelum dinyalakan

## Mesin Contoh A — 199cc, 2 klep, drag matic

| Parameter | Nilai | Status |
|---|---|---|
| Bore × stroke | 63 × 64 mm = 199,5 cc | [UKUR] |
| Klep isap / buang | 31 / 27 mm | [UKUR] |
| **Throat isap** | **29 mm** | [UKUR] |
| Port isap | Ø29,5 mm (683 mm²) | [UKUR] |
| Lift | 10,8 mm | [UKUR] |
| **Kompresi statis** | **16:1** | [UKUR] |
| **DCR** | **12,83** | [HITUNG] |
| Bahan bakar | avgas 100LL | [UKUR] |
| Hasil | 500 m 15,4 s, trap 158 km/h | [UKUR] |

**Besaran jangkar kalibrasi:**
- Luas klep isap / bore: 0,242
- Kecepatan gas port isap: 97 m/s
- Rasio port/throat isap: 1,035
- Potensi: ~28 HP crank, ~140 HP/L

## Mesin Contoh B — 150cc, 4 klep, rancangan

| Parameter | Nilai |
|---|---|
| Bore × stroke × rod | 57,3 × 58 × 95 mm = 149,6 cc |
| Klep isap / buang | 22 / 19 mm |
| **Throat isap / buang** | **20,2 / 16,7 mm** |
| CSA port isap | 615–665 mm² |
| Cam in / ex | **261° / 261°** (bukan 281°!) |
| **CR statis** | **14:1** (DCR 12,07, margin +0,76) |
| Dome piston | usir 2,45 cc |
| Runner isap | 155 mm |
| Header dalam | 29,1 mm |
| RPM sasaran | 12.000 |
| Potensi | ~41 HP (~274 HP/L) |

---

## KESIMPULAN

Ada satu benang yang menyatukan buku ini:

> **Ukur mesinmu sendiri. Itu sumber data terbaik yang kamu punya.**

Setiap kali buku ini memilih antara tabel umum dan pengukuran dari mesin yang sudah terbukti, pengukuran yang menang.

**Tiga pelajaran utama:**

1. **Ukur mesin acuan** — throat, lift acuan cam, panjang header, volume ruang bakar terukur. Yang paling sering hilang dan paling merugikan.

2. **Kalibrasi perhitunganmu ke mesin terbukti**, bukan ke tabel umum. Tabel umum meleset dengan cara yang merugikan.

3. **Diagnostik yang hijau bukan bukti hasilnya benar.** Periksa kewarasan fisika, lihat datanya sendiri.

**Bangun. Ukur. Kalibrasi ulang. Bangun lagi.**

---

*Dokumen ini disusun tanpa gambar. Diagram, grafik dyno contoh, dan visualisasi medan aliran dapat ditambahkan pada revisi berikutnya.*

*Terakhir diperbarui: 2026-08-18*