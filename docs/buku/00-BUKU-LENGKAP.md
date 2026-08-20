# ADVANCED ENGINE TUNING
## Panduan Membangun Mesin 1 Cylinder Matic

**Dokumen Lengkap — 36.900 kata, 14 bab + Lampiran**

---

## DAFTAR ISI

1. **00-PENGANTAR** — Ruang lingkup, peringatan, peta belajar
2. **01-KAMUS-ISTILAH** — 21 istilah dalam 6 kelompok
3. **02-TAHAP1-MENGUKUR** — Torsi vs tenaga, dyno, pengumpulan data
4. **03-TAHAP2-KONFIGURASI** — Bore/stroke, jumlah valve, rasio rod
5. **04-TAHAP3-ALIRAN** — Head, valve, throat, port, porting
6. **05-TAHAP4-CAMSHAFT** — Timing, durasi, overlap, kelegaan valve
7. **06-TAHAP5-KOMPRESI-BBM** — Kompresi dinamis, bahan bakar, detonasi
8. **07-TAHAP6-PENGAPIAN-AFR** — Spark, AFR, spark plug, coil, ECU
9. **08-TAHAP7-SALURAN** — Throttle body, runner, stack, exhaust
10. **09-TAHAP8-MEKANIK** — Material, ring, valve spring, keandalan
11. **10-TAHAP9-CVT** — Transmisi, penyetelan, gear selection
12. **11-TAHAP10-SIMULASI** — CFD, validasi, jebakan simulasi
13. **12-TAHAP11-KALIBRASI** — Cam card, prediksi rpm, crank vs wheel HP, uji BMEP, rancang plenum
14. **13-LAMPIRAN** — Rumus, perkakas, daftar periksa, data mesin

---

# PENGANTAR
**Bagian 0 — Pengantar dan Peta Belajar**

---

## 0.1 Ruang lingkup

Buku ini khusus untuk **mesin 1 cylinder, 4 langkah, transmisi CVT (matic)**, dengan konfigurasi valve:

- **2 valve** (1 isap + 1 buang)
- **3 valve** (2 isap + 1 buang)
- **4 valve** (2 isap + 2 buang)

Kapasitas yang jadi acuan: **125–250 cc**. Prinsipnya berlaku lebih luas, tapi semua angka contoh diambil dari rentang ini.

**Yang TIDAK dibahas:** mesin multi-cylinder, 2 langkah, transmisi manual gear, turbo/supercharger, dan mesin diesel. Sebagian prinsip tetap berlaku, tapi angkanya tidak.

**Kenapa CVT dipisahkan:** transmisi CVT mengubah cara sebuah mesin harus ditala. Pada motor gear, rentang rpm bertenaga (powerband) yang lebar sangat penting karena putaran jatuh tiap kali pindah gear. Pada CVT, mesin bisa ditahan di satu titik putaran sepanjang akselerasi — sehingga **tenaga puncak jauh lebih penting daripada rentang rpm yang lebar**. Ini mengubah pilihan cam, port, dan throttle body secara mendasar.

---

## 0.2 PERINGATAN — baca ini sebelum melanjutkan

> **Buku ini memberi BASELINE, bukan jaminan.**

Setiap angka di buku ini adalah **titik awal yang beralasan**, bukan hasil akhir yang pasti. Mesin nyata selalu berbeda dari perhitungan, dan perbedaannya bisa besar.

**Kenapa perhitungan tidak pernah 100% tepat:**

| Sumber perbedaan | Besarnya |
|---|---|
| Toleransi manufaktur (bore, stroke, valve, port) | ±0,5–2% |
| Kualitas pengerjaan porting | ±5–15% |
| Suhu udara, kelembaban, tekanan udara | ±3–5% |
| Kualitas bahan bakar antar batch | ±2–5% |
| Kondisi CVT, timing chain, kebocoran | ±5–10% |
| Model matematis yang menyederhanakan realita | ±5–20% |

Digabungkan, **selisih 10–25% antara hitungan dan kenyataan itu normal**, bukan tanda perhitungannya salah.

**Cara memakai buku ini dengan benar:**

1. Pakai perhitungan untuk **menentukan titik awal** dan **menghindari kesalahan besar**
2. Bangun mesinnya
3. **Ukur di dyno** — ini tidak bisa dilewati
4. Sesuaikan berdasarkan hasil ukur, bukan berdasarkan hitungan
5. Kalibrasi ulang perhitunganmu dengan hasil nyata

Perhitungan menghemat waktu dan uang dengan menyingkirkan pilihan yang jelas salah. Ia tidak menggantikan pengukuran.

**Yang paling berbahaya bukan hitungan yang meleset, tapi hitungan yang dipercaya buta.** Kalau perhitungan bilang kompresi 14:1 aman dan mesinmu jebol di run pertama, yang salah bukan cuma angkanya — tapi keputusan untuk tidak memverifikasi.

---

## 0.3 Peta belajar — urutan yang benar

Ini bagian terpenting dari pengantar. Banyak orang gagal bukan karena kurang ilmu, tapi karena **belajar dalam urutan yang salah** — misalnya menghabiskan bulanan menggerus port padahal exhaust-nya salah panjang.

Urutan di bawah disusun berdasarkan **dampak per usaha** dan **ketergantungan antar topik**.

### TAHAP 1 — Memahami apa yang diukur
*Sebelum mengubah apa pun, pahami dulu apa yang sedang dikejar.*

- Torsi versus tenaga — dan kenapa keduanya bukan hal yang sama
- Powerband dan artinya untuk CVT
- Dyno: jenisnya, kenapa wajib, cara membaca grafiknya
- Data apa yang harus dikumpulkan sebelum mulai

**Kenapa ini pertama:** tanpa alat ukur dan kemampuan membaca hasilnya, semua langkah berikutnya cuma tebakan. Perubahan 3% tidak terasa di jalan tapi jelas di grafik dyno.

**Waktu belajar:** 1–2 minggu. **Bisa dilewati?** Tidak.

---

### TAHAP 2 — Memilih konfigurasi dasar
*Keputusan yang tidak bisa diubah setelah mesin dibangun.*

- Square, overbore, overstroke — dan mitos "stroke panjang lebih bertorsi"
- Rasio rod dan konsekuensinya
- Jumlah valve: 2, 3, atau 4
- Kapasitas besar dengan valve kecil — kombinasi yang sering salah
- Inersia crankshaft

**Kenapa ini kedua:** semua keputusan berikutnya bergantung pada bore, stroke, dan jumlah valve. Mengubahnya nanti berarti membangun ulang dari nol.

**Waktu belajar:** 1 minggu. **Bisa dilewati?** Tidak, kalau kamu punya pilihan basis mesin.

---

### TAHAP 3 — Aliran: cylinder head
*Menentukan plafon tenaga mesin.*

- Valve dan batas geometri
- Throat — pembatas yang sesungguhnya
- Port: luas penampang dan kecepatan gas
- Bentuk port, short-turn radius, bowl
- Lift kritis

**Kenapa ini ketiga:** head menentukan **berapa banyak udara yang bisa masuk**, dan udara adalah batas mutlak tenaga. Cam, pengapian, dan exhaust cuma menentukan seberapa dekat kamu ke plafon itu.

**Waktu belajar:** 3–4 minggu. Ini bagian paling teknis. **Bisa dilewati?** Tidak.

---

### TAHAP 4 — Timing: camshaft
*Menentukan di putaran berapa plafon itu tercapai.*

- Empat kejadian valve dan urutan kepentingannya
- IVC dan kompresi dinamis
- Durasi dari time-area
- Overlap, LSA, ICL
- Kelegaan valve-piston

**Kenapa setelah head:** durasi cam yang benar bergantung pada luas throat. Memilih cam sebelum head selesai berarti menebak.

**Waktu belajar:** 3–4 minggu. **Bisa dilewati?** Tidak.

---

### TAHAP 5 — Kompresi dan bahan bakar
*Dua hal yang harus diputuskan bersamaan.*

- Kompresi statis, dinamis, dan rasio ekspansi
- Anggaran volume ruang bakar
- Jenis bahan bakar: bensin SPBU, bensol/avgas, VP Q16, VP M5, metanol, nitrometana
- Mengkalibrasi batas detonasi
- Knocking dan fuel dilution

**Kenapa setelah cam:** kompresi dinamis ditentukan oleh IVC, dan IVC ditentukan oleh cam. Memilih kompresi sebelum cam adalah kesalahan urutan yang paling umum.

**Waktu belajar:** 2 minggu. **Bisa dilewati?** Tidak.

---

### TAHAP 6 — Pengapian dan campuran
*Menyalakan yang sudah masuk, pada waktu yang tepat.*

- Stoikiometri dan AFR
- AFR untuk torsi maksimum versus tenaga maksimum
- Lambda — kenapa lebih berguna daripada AFR
- Spark angle dan MBT
- Injection angle
- Spark plug: heat range, gap, elektroda
- Coil: TCI, CDI, smart coil
- ECU standar, remap, dan ECU aftermarket

**Kenapa di sini:** ini bagian yang **paling murah** untuk memberi tenaga, dan **paling cepat** merusak mesin kalau salah. Bisa dipelajari paralel dengan Tahap 5.

**Waktu belajar:** 2–3 minggu. **Bisa dilewati?** Tidak.

---

### TAHAP 7 — Saluran masuk dan buang
*Memanfaatkan gelombang tekanan.*

- Throttle body
- Panjang intake runner dan tuning gelombang
- Velocity stack dan plenum
- Port buang, header, panjang exhaust

**Kenapa setelah cam:** panjang runner dan header ditala terhadap timing valve. Tanpa cam yang pasti, panjangnya tidak bisa dihitung.

**Waktu belajar:** 2 minggu. **Bisa dilewati?** Tidak — ini sering jadi sumber kehilangan tenaga terbesar yang tidak disadari.

---

### TAHAP 8 — Mekanik, material, dan keandalan
*Supaya yang sudah dibangun tidak jebol.*

- Batas mekanis: kecepatan piston, percepatan, gaya inersia
- Material: piston, rod, valve — aluminium, baja, stainless, titanium
- Coating pada piston dan valve
- Ring piston: single versus double, cara pemasangan
- Clearance piston dan ring
- Pemuaian termal
- Valve spring: pemilihan, pengukuran, floating
- Massa berputar dan bolak-balik

**Kenapa di sini:** setelah tahu berapa rpm yang dikejar, baru bisa ditentukan material dan clearance yang dibutuhkan.

**Waktu belajar:** 3 minggu. **Bisa dilewati?** Tidak, kalau kamu ingin mesinnya bertahan.

---

### TAHAP 9 — Penyaluran tenaga: CVT
*Tenaga yang tidak sampai ke roda tidak ada artinya.*

- Cara kerja CVT
- Roller, centrifugal spring, CVT spring
- Rasio, kecepatan puncak, akselerasi
- Menyesuaikan CVT ke powerband

**Kenapa terakhir:** CVT ditala ke powerband mesin. Menala CVT sebelum mesinnya jadi adalah pekerjaan yang harus diulang.

**Waktu belajar:** 2 minggu. **Bisa dilewati?** Tidak — pada matic, CVT bisa menghilangkan 20–30% tenaga yang sudah dibuat.

---

### TAHAP 10 — Simulasi dan validasi
*Opsional, tapi mempercepat kalau dipakai benar.*

- CFD: cara kerja dan batasnya
- Menyiapkan flowbench virtual
- Jebakan yang mahal
- Validasi di dyno dan lintasan

**Kenapa terakhir:** simulasi berguna untuk **memilih antar alternatif**, bukan untuk menentukan dimensi dasar. Tanpa pemahaman Tahap 3–7, hasil simulasi tidak bisa ditafsirkan.

**Waktu belajar:** 4+ minggu. **Bisa dilewati?** **Ya.** Ini satu-satunya tahap yang benar-benar opsional.

---

### TAHAP 11 — Kalibrasi: membaca mesin nyata
*Mengubah data lapangan yang berantakan jadi angka yang bisa dipercaya.*

- Membaca cam card dari data yang tidak lengkap atau bertentangan
- Memprediksi rpm peak power dari spesifikasi (rumus time-area dibalik)
- Kenapa data mesin sendiri selalu mengalahkan acuan dari mesin lain
- Mengecek kecukupan throttle body dari spesifikasi
- **Crank HP vs Wheel HP** — kesalahan paling mudah terjadi di dyno chassis
- Mendiagnosis efek plenum dan piping dari rasa berkendara
- **Uji BMEP** — menguji kewarasan sheet dyno dari dua angka yang selalu ada di situ
- **Membedakan salah kalibrasi dari salah rasio** pada dyno matic tanpa locked pulley
- Merancang plenum dari sasaran, bukan dari acuan pabrikan

**Kenapa terakhir:** tahap ini mengasumsikan seluruh Tahap 1–10 sudah dipahami — isinya tentang menerapkan rumus-rumus itu ke data lapangan yang tidak ideal, bukan rumus baru.

**Waktu belajar:** 1 minggu. **Bisa dilewati?** Tidak, kalau kamu akan sering kerja dari data dyno chassis atau spek mesin yang tidak lengkap.

---

## 0.4 Ringkasan urutan

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
11. Kalibrasi        → membaca data lapangan yang tidak ideal
```

**Kesalahan urutan yang paling sering terjadi:**

| Kesalahan | Akibat |
|---|---|
| Beli cam sebelum head selesai | durasi salah, harus beli lagi |
| Tentukan kompresi sebelum cam | DCR meleset, detonasi atau kurang tenaga |
| Porting habis-habisan tapi exhaust standar | 20–30% tenaga hilang di exhaust |
| Bangun mesin tanpa akses dyno | tidak tahu apakah berhasil |
| Tala CVT sebelum mesin final | pekerjaan diulang |
| Naikkan rpm tanpa hitung beban mekanis | jebol |

---

## 0.5 Notasi dan penandaan

**Satuan:** milimeter untuk panjang, mm² untuk luas, cc untuk volume, m/s untuk kecepatan, derajat crank untuk sudut, rpm untuk putaran, Nm untuk torsi, HP atau PS untuk tenaga.

**Penandaan kepercayaan** — dipakai konsisten sepanjang buku:

| Tanda | Arti |
|---|---|
| **[UKUR]** | hasil pengukuran langsung — dipercaya |
| **[HITUNG]** | diturunkan dari [UKUR] — dipercaya sejauh asumsinya benar |
| **[ASUMSI]** | ditebak dari praktik lazim — **harus diverifikasi** |
| **[SIM]** | dari simulasi — bagus untuk membandingkan, lemah untuk angka mutlak |

Kalau sebuah angka tidak diberi tanda, anggap [ASUMSI].

---

## 0.6 Mesin contoh

Sepanjang buku dipakai tiga mesin contoh. Angkanya nyata, diambil dari mesin yang benar-benar dibangun dan diukur, tapi **dipakai sebagai contoh — bukan resep untuk ditiru mentah-mentah.**

### Mesin Contoh A — 199cc, 2 valve, drag matic

| | |
|---|---|
| Bore × stroke | 63 × 64 mm = 199,5 cc |
| Valve isap / buang | 31 / 27 mm |
| Throat isap | 29 mm (rasio 0,935) |
| Port isap | bundar Ø29,5 mm |
| Port buang | Ø29 mm |
| Lift | 10,8 mm |
| Cam | IN 38 BTDC / 63 ABDC, EX 63 BBDC / 38 ATDC |
| Durasi | 281° / 281° @1mm |
| Overlap | 76°, LSA 102,5° |
| Kompresi statis | 16:1 |
| Bahan bakar | bensol / avgas 100LL |
| Throttle body | 38 mm |
| Header dalam | 30 mm, inlet muffler 50 mm |
| Hasil | 500 m dalam 15,4 detik, trap 158 km/h |

**Peran dalam buku:** mesin acuan kalibrasi. Semua besaran tak-berdimensi diambil dari sini.

### Mesin Contoh B — 150cc, 4 valve, rancangan

| | |
|---|---|
| Bore × stroke × rod | 57,3 × 58 × 95 mm = 149,6 cc |
| Valve isap / buang | 22 / 19 mm |
| Throat isap / buang | 20,2 / 16,7 mm |
| Kompresi statis | 14:1 |
| RPM sasaran | 12.000 |

**Peran dalam buku:** contoh penerapan seluruh metode dari awal sampai akhir.

### Mesin Contoh C — 155cc, 3 valve, basis standar

| | |
|---|---|
| Bore × stroke | 58 × 58,6 mm = 154,8 cc |
| Valve | 3 valve (2 isap + 1 buang) |
| Pendingin | udara |
| Kompresi standar | 10,5:1 |
| Tenaga standar | 12,7 HP @ 7.750 rpm |

**Peran dalam buku:** contoh arsitektur 3 valve dan batasannya.

---

## 0.7 Daftar berkas

| Berkas | Isi |
|---|---|
| `00-PENGANTAR.md` | ruang lingkup, peringatan, peta belajar (berkas ini) |
| `01-KAMUS-ISTILAH.md` | 21 istilah dalam 6 kelompok |
| `02-TAHAP1-MENGUKUR.md` | torsi vs tenaga, powerband, dyno |
| `03-TAHAP2-KONFIGURASI.md` | bore/stroke, rod, jumlah valve, crankshaft |
| `04-TAHAP3-ALIRAN.md` | valve, throat, port, bentuk |
| `05-TAHAP4-CAMSHAFT.md` | timing, durasi, overlap, kelegaan |
| `06-TAHAP5-KOMPRESI-BBM.md` | kompresi, bahan bakar, detonasi |
| `07-TAHAP6-PENGAPIAN-AFR.md` | AFR, spark, injeksi, spark plug, coil, ECU |
| `08-TAHAP7-SALURAN.md` | throttle body, runner, stack, exhaust |
| `09-TAHAP8-MEKANIK.md` | material, ring, clearance, valve spring, massa |
| `10-TAHAP9-CVT.md` | CVT, rasio, top speed, akselerasi |
| `11-TAHAP10-SIMULASI.md` | CFD dan validasi |
| `12-TAHAP11-KALIBRASI.md` | membaca cam card, prediksi rpm, crank vs wheel HP, uji BMEP, rancang plenum |
| `13-LAMPIRAN.md` | rumus, perkakas, daftar periksa |
| `build/XMAX-344-BUILD-SPEC.md` | contoh build spec lengkap hasil penerapan metode buku ini |

---

*Buku ini disusun tanpa gambar. Diagram dan grafik dapat ditambahkan pada revisi berikutnya.*

---

# KAMUS ISTILAH

*21 istilah dalam 6 kelompok. Baca sekali sekarang, rujuk kembali saat dibutuhkan.*

Tiap entri memuat: **satuan**, **rumus**, **diukur di mana**, **kenapa penting**, **rentang khas**, dan **kesalahpahaman yang umum terjadi**. Bagian terakhir itu yang paling sering menyelamatkan.

---

## KELOMPOK 1 — UKURAN DAN GEOMETRI

*Besaran yang bisa dipegang dengan sigmat. Statis, tidak berubah saat mesin berputar.*

---

### CSA — *Cross-Sectional Area*
**Luas penampang saluran**

**Satuan:** mm²

**Rumus:**
```
Penampang bundar : CSA = π/4 × D²
Penampang oval   : CSA ≈ 0,92 × lebar × tinggi
```
Faktor 0,92 untuk bentuk superelips — di antara elips murni (0,785) dan kotak (1,00). Port hasil porting biasanya mendekati angka ini.

**Diukur di mana:** di **titik tersempit** sepanjang saluran, bukan di flange dan bukan di bowl. Titik tersempit inilah yang menentukan kecepatan gas dan menjadi pembatas.

Untuk port bercabang (4 valve), yang dipakai adalah CSA **runner bersama** sebelum pecah dua — bukan CSA tiap cabang.

**Kenapa penting:** CSA menentukan kecepatan gas, dan kecepatan gas menentukan pengisian cylinder. Ini variabel desain port yang paling berpengaruh.

**Rentang khas:** untuk mesin balap kecil, CSA port isap berkisar 0,90–1,10 × luas throat.

**Kesalahpahaman yang umum:**

*Menyebut ukuran port dalam diameter, bukan luas.* Menyesatkan karena luas berskala dengan **kuadrat** diameter. Menaikkan port dari 28 ke 30 mm terdengar kecil (+7%), padahal luasnya naik **15%**. Selalu berpikir dalam mm².

*Mengukur di tempat yang salah.* Banyak orang mengukur di mulut flange karena paling mudah dijangkau. Titik tersempit biasanya di dekat short-turn atau tepat sebelum bowl.

**Contoh:** Mesin Contoh A punya port isap bundar Ø29,5 mm → CSA 683 mm². Mesin Contoh B dirancang 615–665 mm² dengan penampang oval 22,7 × 29,5 mm.

---

### Throat
**Diameter dalam seat valve**

**Satuan:** mm untuk diameter, mm² untuk luas

**Rumus:**
```
A_throat = n_valve × π/4 × D_throat²
```

**Diukur di mana:** lubang paling sempit di dalam seat, tepat di bawah permukaan yang bersentuhan dengan valve. Bukan diameter valve, bukan diameter luar seat.

**Kenapa penting:** pada lift tinggi, throat adalah **pembatas sesungguhnya**. Membesarkan throat adalah satu-satunya perubahan yang menaikkan plafon flow head — bentuk port tidak bisa melakukannya.

**Rentang khas:**

| Rasio throat/valve | Keterangan |
|---|---|
| 0,85–0,88 | konservatif, umum di buku |
| 0,88–0,92 | balap lazim |
| 0,92–0,94 | agresif |
| > 0,94 | seat sangat tipis, berisiko |

Batasnya lebar seat: `lebar = (D_valve − D_throat) / 2`. Di bawah 0,7 mm berisiko, terutama sisi buang.

**Kesalahpahaman yang umum:**

*Mengira aturan 0,85–0,90 itu hukum mati.* Mesin Contoh A berjalan di **0,935** bertahun-tahun pada kompresi 16:1. Yang menentukan bukan rasionya, tapi lebar seat dalam milimeter dan kualitas materialnya.

*Menyamakan sisi isap dan buang.* Sisi buang selalu butuh seat lebih lebar — seat itulah jalan panas valve buang keluar.

---

### Bore, Stroke, Rod
**Diameter cylinder, panjang langkah, panjang stang piston**

**Satuan:** mm

**Rumus turunan:**
```
Kapasitas   : Vd = π/4 × bore² × stroke
Luas piston : A_p = π/4 × bore²
Rasio rod   : R = panjang_rod / stroke
```

**Kenapa penting:**

**Bore** menentukan berapa besar valve yang muat — itu plafon napas mesin. Bore besar juga memperpanjang jalur api, menurunkan toleransi detonasi.

**Stroke** menentukan kecepatan piston pada rpm tertentu. Stroke pendek = rpm tinggi lebih murah secara mekanis.

**Rod** mempengaruhi percepatan piston dan side thrust. Efeknya ke kompresi dinamis kecil.

**Rentang khas rasio rod:**

| Rasio | Keterangan |
|---|---|
| < 1,6 | sangat pendek |
| 1,6–1,75 | pendek, khas mesin kecil |
| 1,75–1,9 | umum |
| > 1,9 | panjang, khas mesin balap besar |

**Kesalahpahaman yang umum:**

*Mengira rod panjang selalu lebih baik.* Rod pendek memang menaikkan side thrust dan percepatan puncak, tapi juga membuat piston menjauh dari TDC lebih cepat — yang **melonggarkan kelegaan valve** dan **memperpendek waktu untuk detonasi berkembang**.

---

## KELOMPOK 2 — KECEPATAN DAN ALIRAN

*Muncul hanya saat mesin berputar. Semuanya bergantung rpm.*

---

### MPS — *Mean Piston Speed*
**Kecepatan piston rata-rata**

**Satuan:** m/s

**Rumus:**
```
MPS = 2 × stroke[m] × rpm / 60
```
Faktor 2 karena piston menempuh satu stroke naik dan satu turun tiap putaran.

**Kenapa penting:** **indikator umur mesin** paling sederhana dan paling berguna. Semua beban mekanis berskala dengan besaran ini.

**Rentang khas:**

| MPS | Keterangan |
|---|---|
| < 20 m/s | aman, bisa harian |
| 20–22 | tinggi, umur pendek tapi wajar untuk drag |
| 22–24 | sangat tinggi, butuh part serius |
| 24–26 | ekstrem |
| 30+ | drag profesional, mesin sekali pakai |

**Kesalahpahaman yang umum:**

*Mengira MPS adalah kecepatan puncak piston.* Bukan. Kecepatan **sesaat** puncak terjadi sekitar 70–80° dari TDC dan besarnya sekitar **1,6× MPS**.

*Membandingkan rpm antar mesin tanpa memperhitungkan stroke.* Mesin 19.000 rpm berstroke 39,8 mm (MPS 25,2) dan mesin 12.000 rpm berstroke 58 mm (MPS 23,2) sebenarnya hampir sama beratnya secara mekanis. **RPM sendirian tidak berarti apa-apa.**

---

### MGV — *Mean Gas Velocity*
**Kecepatan gas rata-rata**

**Satuan:** m/s

**Rumus:**
```
MGV = (luas piston / CSA) × MPS
```

**Diukur di mana — INI PENTING:** ada dua konvensi, dan angkanya berbeda jauh.

| Konvensi | CSA yang dipakai | Nilai khas |
|---|---|---|
| **Di port** | CSA port di titik tersempit | 90–115 m/s |
| **Di throat** | luas throat | 95–135 m/s |

Buku ini memakai **konvensi port** kecuali disebut lain.

**Kenapa penting:** MGV menentukan **momentum muatan** yang masuk cylinder. Momentum itu yang terus mengisi cylinder bahkan setelah piston melewati BDC — efek ram yang menaikkan efisiensi volumetrik.

Terlalu rendah: momentum tidak cukup, pengisian lemah.
Terlalu tinggi: restriksi mencekik, rugi tekanan melonjak (rugi berskala dengan v²).

**Rentang khas (konvensi port):**

| MGV | Keterangan |
|---|---|
| 70–85 m/s | jalanan, torsi bawah |
| 85–100 | serbaguna |
| 100–115 | balap, putaran atas |
| > 120 | sangat agresif |

**Kesalahpahaman yang umum:**

*Mengira mengecilkan throttle body menaikkan MGV di port.* **Tidak.** MGV di port ditentukan oleh CSA port. Debit sama, luas sama, kecepatan sama.

*Mengira mesin besar butuh kecepatan gas berbeda.* Kalau semua proporsi diskalakan ke bore, **bore hilang dari persamaan**. Mesin 3 liter dan 150 cc dengan proporsi sama punya MGV identik.

---

### Cf — Koefisien Flow
**Perbandingan aliran nyata terhadap aliran teoretis**

**Satuan:** tak berdimensi (0–1)

**Rumus:**
```
Cf = Q_nyata / (A_acuan × √(2Δp/ρ))
```

**Diukur terhadap apa — INI PENTING:** Cf tidak berarti apa-apa tanpa menyebut luas acuannya.

| Acuan | Nilai khas head bagus |
|---|---|
| Luas **throat** | 0,55–0,70 |
| Luas **payung valve** | 0,45–0,55 |
| Luas **tirai** pada lift tertentu | bervariasi |

Buku ini selalu memakai **luas throat**.

**Kenapa penting:** Cf memisahkan "berapa besar lubangnya" dari "seberapa baik bentuknya". Juga berguna sebagai **penjaga kewarasan** — nilai di luar 0,45–0,90 hampir pasti menandakan ada yang salah secara struktural.

**Rentang khas:**

| Cf (acuan throat) | Keterangan |
|---|---|
| < 0,50 | jelek, ada masalah |
| 0,55 | standar pabrikan |
| 0,62 | porting bagus |
| 0,70 | porting sangat bagus |
| 0,85–0,95 | saluran tanpa valve |

---

### K — Koefisien Rugi Tekanan

**Satuan:** tak berdimensi

**Rumus:**
```
K = (v_teoretis / v_nyata)² − 1
Δp_rugi = K × ½ × ρ × v²
```

**Kenapa penting:** memungkinkan **membandingkan** rugi dari komponen berbeda pada skala yang sama.

**Rentang khas:**

| Komponen | K |
|---|---|
| Pipa lurus mulus 70 mm | ~0,07 |
| Mulut bellmouth | 0,05 |
| Mulut rata bertepi tajam | 0,5 |
| Mulut menonjol ke dalam plenum | 0,8–1,0 |
| Tikungan port 37° radius wajar | 0,4 |
| Butterfly throttle body WOT | 0,25 |

---

### VE — *Volumetric Efficiency*
**Efisiensi volumetrik**

**Satuan:** fraksi atau persen

**Definisi:** perbandingan massa udara yang benar-benar terjebak di cylinder terhadap massa udara yang mengisi kapasitas cylinder pada kondisi atmosfer.

**Kenapa penting:** VE adalah **hasil akhir** dari semua yang dibahas di buku ini.

**Rentang khas:**

| VE | Keterangan |
|---|---|
| 0,75–0,85 | mesin standar |
| 0,85–0,95 | mesin diporting |
| 0,95–1,05 | mesin balap tertala baik |
| > 1,05 | tuning gelombang bekerja sangat baik |

VE di atas 1,00 dimungkinkan karena momentum dan gelombang tekanan mendorong lebih banyak muatan masuk daripada yang bisa dilakukan tekanan atmosfer sendirian.

---

## KELOMPOK 3 — KOMPRESI

---

### CR — *Compression Ratio*
**Rasio kompresi statis**

**Satuan:** rasio, ditulis 14:1

**Rumus:**
```
CR = (Vd + Vc) / Vc
```

**Vc mencakup apa saja — INI SERING SALAH:**
```
Vc = pent-roof + gasket + deck clearance + kantong valve − dome piston
```

**Kenapa penting:** CR menentukan **rasio ekspansi**, dan itu menentukan efisiensi termal:
```
η = 1 − 1/CR^0,4
```

**Rentang khas:**

| CR | Keterangan |
|---|---|
| 9–11 | mesin standar bensin |
| 11–13 | tune-up, bensin oktan tinggi |
| 13–16 | balap, bensin balap / avgas |
| 16+ | metanol, atau IVC sangat telat |

**Kesalahpahaman yang umum:**

*Melupakan kantong valve.* Kesalahan paling mahal. Empat kantong sedalam 2,7 mm menambah 1,58 cc — pada target Vc 11,50 cc itu **14% anggaran**.

**Urutan yang benar:** tentukan cam dulu → hitung kantong valve → baru hitung dome atau papasan.

*Mengira CR statis menentukan detonasi.* Tidak. Yang menentukan adalah DCR.

---

### DCR — *Dynamic Compression Ratio*
**Rasio kompresi dinamis**

**Satuan:** rasio

**Rumus:**
```
DCR = 1 + (V_sapu_saat_IVC / Vd) × (CR − 1)
```
dengan posisi piston:
```
s(θ) = r(1 − cos θ) + L − √(L² − (r sin θ)²)     θ = 180° + IVC_ABDC
```

**Kenapa penting:** **DCR yang menentukan detonasi, bukan CR.** Kompresi baru mulai setelah valve isap menutup.

**Kesalahpahaman yang umum:**

*Mengira DCR berubah dengan rpm.* **Tidak.** DCR murni geometri + timing. Tidak ada rpm dalam rumusnya.

*Mengira CR tinggi selalu berarti DCR tinggi.* Mesin Contoh A berjalan CR 16:1 tapi DCR-nya 12,83 karena IVC sangat telat (63° ABDC).

*Melupakan bahwa DCR, rpm, dan bahan bakar itu satu paket.* Menaikkan rpm sasaran memaksa durasi lebih panjang → IVC lebih telat → DCR turun.

---

## KELOMPOK 4 — REFERENSI SUDUT CRANK

---

### TDC dan BDC

**TDC** — *Top Dead Center* — piston paling atas.
**BDC** — *Bottom Dead Center* — piston paling bawah.

**Yang sering membingungkan:** dalam satu siklus 4 langkah, piston melewati TDC **dua kali**:

| | Kapan | Sebutan |
|---|---|---|
| TDC pertama | akhir kompresi | **firing TDC** |
| TDC kedua | akhir buang | **overlap TDC** |

Timing cam selalu dirujuk ke **overlap TDC**.

---

### BTDC / ATDC
**Sebelum / sesudah titik mati atas**

Dipakai untuk: IVO (biasanya BTDC), EVC (biasanya ATDC), ICL (selalu ATDC), pengapian (selalu BTDC).

"IVO 28° BTDC" = valve isap mulai membuka 28 derajat crank **sebelum** piston sampai TDC.

---

### BBDC / ABDC
**Sebelum / sesudah titik mati bawah**

Dipakai untuk: EVO (biasanya BBDC), IVC (biasanya ABDC).

"IVC 53° ABDC" = valve isap menutup 53 derajat **setelah** piston melewati BDC.

**Kenapa IVC selalu ABDC:** momentum muatan masih mendorong masuk walau piston sudah mulai naik. Menutup tepat di BDC membuang momentum itu.

---

## KELOMPOK 5 — KEJADIAN VALVE

---

### IVO / IVC — *Intake Valve Open / Close*

**Satuan:** derajat crank

**IVO — kenapa penting:** menentukan **overlap**. Lebih awal = overlap besar, pembilasan kuat, tapi muatan segar bisa lolos di rpm rendah.

**IVC — kenapa penting:** **kejadian terpenting di seluruh camshaft.** Menentukan kompresi dinamis, rpm efisiensi penjebakan puncak, dan karakter bawah versus atas.

**Rentang khas:**

| | Jalanan | Balap |
|---|---|---|
| IVO | 5–15° BTDC | 25–45° BTDC |
| IVC | 35–50° ABDC | 50–75° ABDC |

**Kesalahpahaman yang umum — INI YANG PALING SERING:**

*Membandingkan timing tanpa menyebut pada lift berapa diukur.*

| Titik ukur | Nama umum | Efek |
|---|---|---|
| 0,15 mm | *seat-to-seat* | durasi terbesar |
| 1,00 mm | **@1mm** — standar Eropa/Asia | acuan buku ini |
| 1,27 mm (0,050") | **@0.050"** — standar Amerika | ~10–20° lebih kecil |

Cam yang sama bisa disebut "300 derajat" atau "260 derajat". **Selalu tanyakan pada lift berapa.**

---

### EVO / EVC — *Exhaust Valve Open / Close*

**EVO — kenapa penting:** menentukan kapan *blowdown* dimulai. Terlalu awal membuang kerja ekspansi; terlalu telat menambah rugi pemompaan. EVO juga titik lahir gelombang tekanan untuk tuning exhaust.

**EVC — kenapa penting:** bersama IVO menentukan overlap.

**Rentang khas:**

| | Jalanan | Balap |
|---|---|---|
| EVO | 35–50° BBDC | 50–75° BBDC |
| EVC | 5–15° ATDC | 25–45° ATDC |

**Kesalahpahaman yang umum:**

*Mengira sisi buang selalu butuh durasi lebih panjang.* Tergantung **rasio throat ex/in**:

| Rasio throat ex/in | Tindakan |
|---|---|
| < 0,63 | tambah 8–12° durasi ex |
| 0,63–0,72 | cam simetris aman |
| > 0,72 | sisi buang lega |

---

### Durasi

**Rumus:**
```
durasi_in = IVO_BTDC + 180 + IVC_ABDC
durasi_ex = EVO_BBDC + 180 + EVC_ATDC
```

**Cara menentukannya dengan benar:**
```
durasi_baru = durasi_acuan × (A_thr_acuan / A_thr_baru)
                            × (Vd_baru / Vd_acuan)
                            × (rpm_baru / rpm_acuan)
```

**Kesalahpahaman yang umum:**

*Mengira rpm tinggi selalu butuh durasi panjang.* Yang benar: rpm tinggi **dan luas valve tetap** butuh durasi panjang. Mesin Contoh B butuh durasi **lebih pendek** (261° vs 281°) walau rpm-nya lebih tinggi, karena head-nya bernapas 29% lebih lega per cc.

---

### Overlap

**Rumus:**
```
overlap = IVO_BTDC + EVC_ATDC
```

**Kenapa penting:** selama overlap, aliran gas buang bisa **menarik** muatan segar masuk — pembilasan (*scavenging*).

**Rentang khas:**

| Overlap | Karakter |
|---|---|
| 10–30° | jalanan, idle halus |
| 40–70° | balap, idle kasar |
| 70–110° | drag, tidak bisa idle stasioner |

**Cara menskalakannya dengan benar:** yang dipertahankan adalah **luas tirai overlap per cc**:
```
luas_per_cc = n_valve × π × D_valve × lift_di_TDC / kapasitas
```

**Kesalahpahaman yang umum:**

*Menskalakan lift overlap lewat diameter valve saja.* Untuk head 4 valve ini keliru dua kali lipat, karena dua valve isap memberi luas tirai jauh lebih besar per milimeter lift.

*Ambiguitas angka "lift overlap".* Angka yang beredar sering tidak jelas: lift satu valve atau gabungan in + ex? Contoh: angka "3,6 mm" pada Mesin Contoh A ternyata **gabungan** (1,83 mm per valve). Kalau ditafsirkan sebagai satu valve, target overlap jadi dua kali terlalu besar.

**Cara memastikan:** hitung dari sudut, bukan dari angka lift. Sudut tidak ambigu.

---

## KELOMPOK 6 — KARAKTER CAMSHAFT

---

### ICL / ECL — *Intake / Exhaust Centerline*

**Satuan:** derajat crank. **ICL selalu ATDC, ECL selalu BTDC.**

**Rumus:**
```
ICL = durasi_in / 2 − IVO_BTDC        (ATDC)
ECL = durasi_ex / 2 − EVC_ATDC        (BTDC)
```

**Kenapa penting:** ICL menentukan **di mana cam ditempatkan** relatif terhadap piston. Ini yang diubah dengan *adjustable sprocket*.

| Perubahan ICL | Efek |
|---|---|
| ICL lebih kecil (cam dimajukan) | IVC lebih awal → DCR naik, tenaga bergeser ke bawah |
| ICL lebih besar (cam dimundurkan) | IVC lebih telat → DCR turun, tenaga bergeser ke atas |

**Rentang khas:**

| ICL | Karakter |
|---|---|
| 95–102° ATDC | maju, torsi bawah |
| 102–108° | umum |
| 108–115° | mundur, putaran atas |

---

### LSA — *Lobe Separation Angle*

**Satuan:** derajat camshaft

**Rumus:**
```
LSA = (ICL + ECL) / 2
```

**Rentang khas:**

| LSA | Karakter |
|---|---|
| 98–104° | overlap besar, rentang rpm sempit, drag |
| 104–110° | seimbang |
| 110–116° | overlap kecil, rentang rpm lebar, jalanan |

**Perbedaan pokok dengan ICL — INI YANG PALING SERING TERTUKAR:**

| | LSA | ICL |
|---|---|---|
| Sifat | **tergerinda di cam** | **posisi pemasangan** |
| Bisa diubah? | **tidak**, harus ganti cam | ya, dengan adjustable sprocket |
| Mengubah apa | karakter dasar, overlap | keseimbangan bawah/atas |

Kalau cam-mu LSA 102° dan ingin overlap lebih kecil, memutar sprocket **tidak akan membantu** — sprocket menggeser ICL dan ECL bersama-sama, LSA tetap.

---

### Lift dan Lift Kritis

**Rumus lift kritis:**
```
lift_kritis = A_throat / (n_valve × π × D_valve)
```

**Artinya:** di bawah lift kritis, **luas tirai** yang membatasi. Di atasnya, **throat** yang membatasi.

**Kenapa mesin balap tetap memakai lift jauh di atas lift kritis:** yang dibayar bukan flow puncak, tapi **time-area**. Menahan valve tinggi lebih lama mengisi cylinder lebih banyak.

**Rentang khas kelipatan:**

| Kelipatan lift kritis | Keterangan |
|---|---|
| 1,0–1,3× | jalanan |
| 1,5–2,0× | balap |
| 2,0–2,5× | drag, beban valvetrain tinggi |

**Kesalahpahaman yang umum:**

*Mempercayai aturan "lift maksimum berguna = 0,25 × diameter valve".* Benar untuk **flow puncak steady**, salah untuk mesin balap.

*Menyamakan kebutuhan lift sisi isap dan buang:*

| Arsitektur | Lift kritis in | Lift kritis ex | Konsekuensi |
|---|---|---|---|
| 4 valve | 4,64 mm | 3,68 mm | valve buang butuh lift **lebih rendah** |
| 3 valve | 4,59 mm | 5,03 mm | valve buang butuh lift **lebih tinggi** |

---

### Time-Area

**Rumus praktis:**
```
time-area ∝ (A_throat × durasi) / (kapasitas × rpm)
```

**Kenapa penting:** ini **besaran yang benar-benar menentukan pengisian**, bukan durasi sendirian dan bukan lift sendirian. "Jendela aliran per siklus per cc".

**Kesalahpahaman yang umum:**

*Membandingkan durasi antar mesin berbeda.* Durasi 280° di mesin throat kecil tidak setara dengan 280° di mesin throat besar. Yang setara adalah time-area-nya.

---

## RINGKASAN HUBUNGAN ANTAR ISTILAH

```
GEOMETRI                    →   ALIRAN              →   HASIL
──────────────────────────────────────────────────────────────
bore, stroke                →   MPS                 →   umur mesin
CSA, luas piston, MPS       →   MGV                 →   pengisian
throat, bentuk port         →   Cf, K               →   flow
──────────────────────────────────────────────────────────────
CAM                         →   EFEK                →   KONSEKUENSI
──────────────────────────────────────────────────────────────
IVO + EVC                   →   overlap             →   pembilasan
IVC                         →   DCR                 →   bahan bakar
durasi × A_throat           →   time-area           →   rpm puncak
ICL                         →   keseimbangan        →   bawah vs atas
LSA                         →   karakter dasar      →   lebar rentang rpm
lift vs lift kritis         →   time-area           →   beban valvetrain
──────────────────────────────────────────────────────────────
KOMPRESI                    →   EFEK
──────────────────────────────────────────────────────────────
CR                          →   rasio ekspansi      →   efisiensi termal
DCR                         →   tekanan puncak      →   batas detonasi
```

**Tiga rantai sebab-akibat yang paling penting diingat:**

1. **CSA port → MGV → pengisian.** Bukan diameter TB.
2. **IVC → DCR → bahan bakar.** Bukan CR statis.
3. **A_throat × durasi → time-area → rpm puncak.** Bukan durasi sendirian.

---

# TAHAP 1 — MEMAHAMI APA YANG DIUKUR

*Sebelum mengubah apa pun, pahami dulu apa yang sedang dikejar.*

---

## 1. Torsi versus tenaga

Ini konsep yang paling sering disalahpahami di dunia tuning, dan kesalahpahamannya menyebabkan keputusan yang salah.

### 1.1 Definisi

**Torsi** adalah gaya putar. Seberapa **keras** mesin memutar poros.

```
Torsi = gaya × jari-jari          [Nm atau kgf·m]
```

**Tenaga** adalah laju kerja. Seberapa **cepat** kerja itu dilakukan.

```
Tenaga = torsi × kecepatan sudut
```

Dalam satuan praktis:

```
HP  = (Nm × rpm) / 7127
PS  = (Nm × rpm) / 7024
kW  = (Nm × rpm) / 9549
```

### 1.2 Hubungan keduanya

Torsi dan tenaga bukan dua hal yang bersaing. **Tenaga adalah torsi dikali putaran.** Kalau kamu tahu kurva torsi, kurva tenaga sudah otomatis tertentukan — dan sebaliknya.

Artinya: mengejar "torsi" atau "tenaga" bukan pilihan strategi. Yang benar-benar bisa dipilih adalah **di putaran berapa torsi puncak terjadi**.

### 1.3 Kenapa kedua kurva berpotongan

Pada grafik dyno, kurva torsi dan tenaga selalu berpotongan di satu titik. Banyak orang mengira titik itu punya arti teknis. **Tidak ada.**

| Satuan | Titik potong |
|---|---|
| lb-ft dan HP | 5252 rpm |
| Nm dan PS | 7024 rpm |
| Nm dan HP | 7127 rpm |

Titik potong itu **artefak satuan**, bukan fenomena fisika. Kalau torsi diplot dalam kgf·m, titik potongnya pindah. Jangan membaca apa pun dari situ.

### 1.4 Mana yang penting untuk akselerasi

**Tenaga.** Bukan torsi.

Percepatan kendaraan:

```
a = (Tenaga_di_roda − rugi) / (massa × kecepatan)
```

Torsi mesin tidak muncul langsung dalam rumus ini. Torsi di **roda** yang penting, dan torsi di roda = torsi mesin × rasio total. Karena rasio bisa diubah (apalagi dengan CVT), yang tersisa sebagai batasan sejati adalah **tenaga**.

Cara memahaminya: torsi mesin bisa dilipatgandakan oleh rasio gear. Tenaga tidak bisa — tenaga di roda selalu lebih kecil daripada tenaga mesin (karena rugi gesek), tidak pernah lebih besar.

### 1.5 Mitos "stroke panjang lebih bertorsi"

Ini keyakinan yang sangat umum dan **sebagian besar salah**.

Torsi berasal dari tekanan pembakaran yang bekerja pada luas piston, dikali jari-jari crank:

```
Torsi ∝ tekanan × luas_piston × (stroke/2)
```

Perhatikan: `luas_piston × stroke` adalah **kapasitas**. Jadi untuk kapasitas yang sama, torsi teoretisnya sama — tidak peduli square, overbore, atau overstroke.

**Yang sebenarnya berbeda adalah di putaran berapa torsi puncak terjadi.** Mesin overstroke punya bore kecil, jadi luas valve-nya terbatas, jadi napasnya habis di putaran lebih rendah — dan torsi puncaknya turun ke rpm rendah. Itu yang terasa "bertorsi".

Kalau dibandingkan **torsi per liter pada rpm puncak masing-masing**, mesin overbore dan overstroke praktis sama.

Bahasan lengkap di Tahap 2.

---

## 2. Powerband

### 2.1 Definisi

**Powerband** adalah rentang putaran di mana mesin menghasilkan tenaga yang berguna. Definisi praktisnya: rentang di mana tenaga berada di atas ~90% dari puncaknya.

### 2.2 Rentang rpm lebar versus puncak tinggi

Ini pertukaran mendasar dalam tuning:

| | Rentang rpm lebar | Rentang rpm sempit |
|---|---|---|
| Durasi cam | pendek | panjang |
| Overlap | kecil | besar |
| LSA | besar (108–116°) | kecil (98–104°) |
| Panjang runner | sedang | ditala tajam |
| Puncak tenaga | lebih rendah | lebih tinggi |
| Cocok untuk | motor gear, harian | CVT, drag |

### 2.3 Kenapa CVT mengubah aturannya

Pada motor gear, setiap pindah gear menjatuhkan putaran mesin. Kalau rentang rpm-nya sempit, mesin jatuh keluar powerband dan akselerasi hilang. Karena itu motor gear butuh rentang rpm yang lebar.

**CVT tidak punya masalah itu.** Rasio berubah kontinu, sehingga mesin bisa ditahan di satu titik putaran sepanjang akselerasi.

Konsekuensinya sangat besar:

> **Pada CVT, yang perlu dioptimalkan adalah tenaga di SATU titik putaran, bukan rentang rpm yang lebar.**

Ini memberi kebebasan yang tidak dimiliki motor gear: cam durasi panjang, overlap besar, LSA sempit, runner ditala tajam — semua yang membuat rentang rpm sempit tapi puncaknya tinggi.

**Syaratnya:** CVT harus benar-benar mampu menahan mesin di titik itu. CVT yang salah setelan akan membiarkan putaran jatuh, dan mesin dengan rentang rpm sempit akan terasa jauh lebih lambat daripada mesin standar. Bahasan di Tahap 9.

### 2.4 Titik mana yang dipilih

Untuk CVT drag, jawabannya adalah **putaran tenaga puncak**, bukan torsi puncak.

Alasannya kembali ke 1.4: percepatan berbanding lurus dengan tenaga. Menahan mesin di torsi puncak berarti membuang putaran yang tersedia.

---

## 3. Dyno

### 3.1 Kenapa dyno wajib

Tanpa dyno, kamu tidak punya cara mengetahui apakah sebuah perubahan berhasil.

| Besar perubahan | Terasa di jalan? | Terlihat di dyno? |
|---|---|---|
| 1–2% | tidak | ya, kalau prosedurnya benar |
| 3–5% | hampir tidak | jelas |
| 5–10% | mungkin | sangat jelas |
| > 10% | ya | jelas |

Masalahnya, sebagian besar perubahan tuning berada di rentang 2–5%. Porting ulang bowl, ganti panjang header 50 mm, geser ICL 3 derajat — semuanya di rentang yang **tidak bisa dirasakan** tapi menumpuk jadi signifikan.

Tanpa dyno, kamu akan:
- Menganggap berhasil sesuatu yang sebenarnya merugikan
- Membuang perubahan yang sebenarnya menguntungkan
- Tidak pernah tahu mana dari lima perubahan sekaligus yang berpengaruh

**Stopwatch di lintasan bukan pengganti dyno.** Waktu lintasan dipengaruhi launch, traksi, angin, dan pengendara — variasinya sering lebih besar daripada efek yang mau diukur.

### 3.2 Jenis dyno

**Dyno inersia** (*inertia dyno*)

Mesin memutar drum bermassa besar yang diketahui momen inersianya. Dari percepatan drum, tenaga dihitung:

```
Tenaga = I × α × ω
```

| Kelebihan | Kekurangan |
|---|---|
| Murah, sederhana | Tidak bisa menahan putaran tetap |
| Cepat — satu run beberapa detik | Sulit untuk tuning AFR/ignition per titik |
| Bagus untuk perbandingan sebelum/sesudah | Beban tidak bisa diatur |

**Dyno beban** (*brake dyno* — eddy current, water brake, AC)

Ada rem yang bisa diatur, sehingga putaran mesin bisa **ditahan** di satu titik selama yang dibutuhkan.

| Kelebihan | Kekurangan |
|---|---|
| Bisa tuning steady-state per titik | Lebih mahal |
| Bisa simulasi beban jalan | Butuh pendinginan serius |
| Wajib untuk mapping ECU yang benar | Run lebih lama, mesin lebih panas |

**Dyno mesin versus dyno chassis**

| | Dyno mesin | Dyno chassis |
|---|---|---|
| Yang diukur | tenaga di crankshaft | tenaga di roda |
| Perlu bongkar mesin | ya | tidak |
| Termasuk rugi CVT | tidak | ya |
| Untuk matic | jarang dipakai | standar |

Untuk matic, **dyno chassis** yang relevan — karena CVT adalah bagian dari sistem yang ditala, dan rugi CVT bisa 10–20%.

### 3.3 Membaca grafik dyno

**Sumbu:** putaran mesin (atau kecepatan roda) di horizontal, torsi dan tenaga di vertikal.

**Yang harus dilihat, berurutan:**

**1. Bentuk kurva torsi.** Ini cerminan langsung efisiensi volumetrik. Puncaknya di mana? Ada lembah?

Lembah (*dip*) di kurva torsi hampir selalu berarti **gelombang tekanan bekerja melawan**, bukan masalah mekanis. Penyebab tersering: panjang runner atau header yang harmoniknya meleset di putaran itu.

**2. Letak puncak tenaga.** Ini yang harus dicocokkan dengan setelan CVT.

**3. Apakah kurva masih naik saat run berhenti.** Kalau tenaga masih naik di rpm tertinggi, mesin belum menunjukkan puncaknya — datanya belum lengkap.

**4. Kurva AFR** (kalau ada). Ini sering lebih informatif daripada kurva tenaga. AFR yang menyimpang di titik tertentu menjelaskan lembah di kurva torsi.

**5. Konsistensi antar run.** Tiga run berturut-turut harus berimpit dalam 1–2%. Kalau tidak, ada yang tidak stabil — suhu, CVT slip, atau kebocoran.

### 3.4 Faktor koreksi

Tenaga mesin bergantung pada kerapatan udara, yang bergantung pada suhu, tekanan udara, dan kelembaban. Dyno menerapkan **faktor koreksi** untuk menormalkan ke kondisi standar.

| Standar | Kondisi acuan |
|---|---|
| SAE J1349 | 25 °C, 99 kPa kering |
| DIN 70020 | 20 °C, 101,3 kPa |
| JIS D1001 | 20 °C, 101,3 kPa |
| EEC 80/1269 | 25 °C, 99 kPa |

Selisih antar standar bisa **3–5%**. Angka "20 HP SAE" dan "20 HP DIN" bukan mesin yang sama.

**Aturan praktis:** saat membandingkan hasil, pastikan standar koreksinya sama. Kalau tidak disebutkan di grafik, tanyakan.

**Lebih baik lagi:** bandingkan hanya run yang dilakukan di **hari yang sama, dyno yang sama, back-to-back**. Faktor koreksi apa pun tidak sebaik menghilangkan variabelnya sejak awal.

### 3.5 Prosedur yang benar

Supaya angkanya berarti:

1. **Panaskan sampai suhu kerja stabil**, lalu jaga tetap di situ. Mesin dingin dan mesin panas bisa berbeda 5%.
2. **Run pertama sebagai pemanasan**, jangan dicatat.
3. **Minimal tiga run** yang dicatat, ambil rata-rata atau median.
4. **Dinginkan antar run** sampai suhu sama seperti run sebelumnya.
5. **Satu perubahan per sesi.** Kalau mengubah tiga hal sekaligus lalu tenaga naik 5%, kamu tidak tahu yang mana yang bekerja — atau apakah dua di antaranya justru merugikan.
6. **Catat semuanya**: suhu udara, kelembaban, bahan bakar, tekanan ban, setelan CVT, jam.

Poin 5 adalah yang paling sering dilanggar dan paling merugikan.

### 3.6 Yang TIDAK bisa dilakukan dyno

- **Tidak mengukur launch dan traksi.** Motor yang lebih kuat di dyno bisa lebih lambat di lintasan kalau launch-nya buruk.
- **Tidak menangkap efek aerodinamis.** Pada trap 150+ km/h, aero memakan porsi besar tenaga.
- **Tidak mensimulasi beban sebenarnya** kecuali dyno beban yang diatur benar.
- **Tidak mendeteksi masalah keandalan.** Mesin bisa memberi angka bagus lalu jebol di run berikutnya.

Dyno menjawab "berapa tenaganya". Lintasan menjawab "apakah menang".

---

## 4. Data yang harus dikumpulkan sebelum mulai

Sebelum mengubah apa pun, kumpulkan data ini. Tanpa data ini, seluruh perhitungan di buku ini tidak bisa dikalibrasi.

### 4.1 Dari mesin yang sudah ada

**Geometri dasar**
- [ ] Bore, stroke, panjang rod
- [ ] Kapasitas sebenarnya
- [ ] Volume ruang bakar (diukur dengan buret, bukan dari spesifikasi)

**Cylinder head**
- [ ] Diameter valve isap dan buang
- [ ] Diameter dalam seat (throat) isap dan buang
- [ ] CSA port di titik tersempit — isap dan buang
- [ ] Lebar seat

**Camshaft**
- [ ] IVO, IVC, EVO, EVC — **dan pada lift berapa diukur**
- [ ] Lift maksimum isap dan buang
- [ ] Lift di TDC overlap

**Kompresi dan bahan bakar**
- [ ] Kompresi statis terukur
- [ ] Jenis bahan bakar
- [ ] Apakah pernah ada gejala detonasi

**Saluran**
- [ ] Diameter throttle body
- [ ] Panjang runner isap (dari valve ke mulut)
- [ ] Diameter dalam header
- [ ] **Panjang header** — dari valve buang ke titik pelebaran
- [ ] Diameter inlet muffler

**Pengapian dan campuran**
- [ ] Jenis coil
- [ ] Spark plug: merek, heat range, gap
- [ ] Kurva pengapian (kalau bisa dibaca)
- [ ] AFR pada beban penuh (butuh wideband)

**Hasil**
- [ ] Grafik dyno, atau
- [ ] Waktu dan trap speed lintasan, plus berat motor + pengendara

### 4.2 Kenapa lengkap begini

Setiap angka di atas dipakai untuk **mengkalibrasi** perhitungan di tahap berikutnya. Yang paling sering hilang dan paling merugikan:

| Data yang hilang | Akibat |
|---|---|
| Throat (bukan diameter valve) | seluruh perhitungan port meleset sampai 40% |
| Lift acuan timing cam | durasi salah baca sampai 20° |
| Panjang header | harmonik exhaust tidak bisa ditentukan |
| Volume ruang bakar terukur | kompresi meleset 1–2 angka penuh |
| AFR beban penuh | tidak tahu apakah aman atau kurang |

### 4.3 Alat ukur minimum

| Alat | Untuk apa | Wajib? |
|---|---|---|
| Sigmat digital | semua dimensi | ya |
| Buret 50 cc + plat kaca | volume ruang bakar | ya |
| Dial indicator + magnetic base | lift cam, deck clearance | ya |
| Degree wheel | timing cam | ya |
| Bore gauge | clearance piston | ya kalau merakit sendiri |
| Feeler gauge | ring gap, valve clearance | ya |
| Wideband lambda | AFR | ya untuk mesin injeksi |
| Timing light | verifikasi pengapian | ya |
| Flowbench | Cf head | tidak, tapi sangat membantu |

---

## 5. Ringkasan Tahap 1

**Yang harus kamu kuasai sebelum lanjut:**

1. Tenaga = torsi × rpm. Keduanya bukan pilihan yang bersaing.
2. Untuk akselerasi, **tenaga** yang menentukan — bukan torsi.
3. Titik potong kurva torsi dan tenaga tidak punya arti fisika.
4. Pada CVT, **tenaga puncak lebih penting daripada rentang rpm yang lebar**.
5. Perubahan 2–5% tidak bisa dirasakan tapi menumpuk jadi besar — karena itu dyno wajib.
6. Satu perubahan per sesi dyno. Ini aturan yang paling sering dilanggar.
7. Bandingkan hanya run di hari yang sama, dyno yang sama.
8. Kumpulkan data lengkap sebelum mulai. Yang paling sering hilang: **throat, lift acuan cam, dan panjang header**.

**Berikutnya:** Tahap 2 — memilih konfigurasi dasar yang tidak bisa diubah lagi setelah mesin dibangun.

---

# TAHAP 2 — MEMILIH KONFIGURASI DASAR

*Keputusan yang tidak bisa diubah setelah mesin dibangun.*

---

## 1. Square, overbore, overstroke

### 1.1 Definisi

| Istilah | Rasio bore/stroke |
|---|---|
| **Overstroke** (*undersquare*) | < 1,0 — stroke lebih panjang daripada bore |
| **Square** | = 1,0 |
| **Overbore** (*oversquare*) | > 1,0 — bore lebih besar daripada stroke |

### 1.2 Perbandingan pada kapasitas sama

Semua konfigurasi di bawah berkapasitas **150 cc**, 4 valve, dengan batas kecepatan piston 22 m/s. [HITUNG]

| Konfigurasi | Bore | Stroke | B/S | Valve isap | Throat | mm²/cc | RPM maks | Potensi |
|---|---|---|---|---|---|---|---|---|
| Overstroke | 52,0 | 70,6 | 0,74 | 19,8 | 17,8 | 3,31 | 9.344 | **66%** |
| Square | 57,6 | 57,6 | 1,00 | 21,9 | 19,7 | 4,06 | 11.465 | **100%** |
| Overbore ringan | 60,0 | 53,1 | 1,13 | 22,8 | 20,5 | 4,41 | 12.441 | **118%** |
| Overbore | 63,0 | 48,1 | 1,31 | 23,9 | 21,5 | 4,86 | 13.716 | **143%** |

*Potensi = luas throat × rpm maksimum, relatif terhadap square.*

Rentangnya **66% sampai 143%** — lebih dari dua kali lipat, dari kapasitas yang sama persis.

### 1.3 Kenapa selisihnya sebesar itu

Overbore menang dua kali:

**Pertama, valve lebih besar.** Diameter valve berskala dengan bore. Bore 63 mm memberi valve isap 23,9 mm sementara bore 52 mm cuma 19,8 mm. Dalam luas, selisihnya 46%.

**Kedua, putaran lebih tinggi.** Stroke pendek berarti kecepatan piston rendah pada rpm tertentu. Pada batas 22 m/s, bore 63 bisa 13.716 rpm sementara bore 52 cuma 9.344 rpm.

Karena tenaga ≈ aliran × rpm, dan overbore unggul di keduanya, keunggulannya berlipat.

### 1.4 Kenapa overbore tidak selalu menang

| Kerugian overbore | Sebabnya |
|---|---|
| **Jalur api lebih panjang** | api harus menempuh jarak lebih jauh dari spark plug ke tepi bore → risiko detonasi naik, batas kompresi turun |
| **Rugi panas lebih besar** | rasio permukaan terhadap volume ruang bakar lebih jelek |
| **Piston lebih berat** | diameter besar berarti mahkota lebih luas dan lebih tebal |
| **Ring lebih panjang** | keliling ring lebih besar → gesekan naik, blowby naik |
| **Terbatas crankcase** | bore tidak selalu bisa diperbesar tanpa ganti block |
| **Squish sulit** | ruang bakar lebar susah dibuat squish efektif |

| Keuntungan overstroke | Sebabnya |
|---|---|
| **Jalur api pendek** | toleransi detonasi lebih tinggi → kompresi bisa lebih tinggi |
| **Rugi panas kecil** | ruang bakar lebih kompak |
| **Piston ringan** | diameter kecil |
| **Torsi puncak di rpm rendah** | terasa lebih responsif di putaran bawah |

### 1.5 Mitos "stroke panjang lebih bertorsi"

Torsi berasal dari tekanan pembakaran yang bekerja pada luas piston dikali jari-jari crank:

```
Torsi ∝ tekanan × luas_piston × (stroke/2)
```

Karena `luas_piston × stroke` adalah **kapasitas**, maka untuk kapasitas yang sama **torsi teoretisnya sama** — tidak peduli konfigurasinya.

Yang benar-benar berbeda adalah **di putaran berapa torsi puncak terjadi**. Overstroke punya bore kecil → luas valve terbatas → napasnya habis lebih awal → torsi puncak turun ke rpm rendah.

**Itu yang terasa "bertorsi", padahal sebenarnya "kehabisan napas lebih awal".**

Sensasinya nyata, kesimpulannya salah. Kalau kamu memilih overstroke untuk drag dengan CVT, kamu membuang 34% potensi tanpa mendapat apa pun sebagai gantinya — karena CVT tidak butuh torsi bawah.

### 1.6 Rekomendasi untuk matic drag

| Prioritas | Pilihan |
|---|---|
| Tenaga puncak maksimum | overbore, B/S 1,15–1,35 |
| Kompromi seimbang | square sampai overbore ringan, B/S 1,0–1,15 |
| Kompresi sangat tinggi | square, jangan overbore ekstrem |
| Harian + sesekali balap | square |

**Batas praktisnya bukan teori, tapi crankcase.** Kebanyakan mesin matic tidak bisa dibore lebih dari 4–6 mm dari standar tanpa mengganti block atau membuat liner khusus.

---

## 2. Kapasitas besar dengan valve kecil

Ini kesalahan paling umum dalam bore-up, dan layak dibahas sendiri.

### 2.1 Apa yang terjadi

Bore dinaikkan tapi head tidak diubah. Kapasitas naik, luas valve tetap.

| Kapasitas | Bore | Throat per cc | MGV @ 9.000 rpm |
|---|---|---|---|
| 150 cc | 57,6 | 4,06 mm²/cc | 72 m/s |
| 165 cc | 60,4 | 3,69 | 79 m/s |
| 180 cc | 63,1 | 3,39 | 86 m/s |
| 200 cc | 66,5 | 3,05 | 96 m/s |

[HITUNG] — stroke tetap, head 150cc tidak diubah.

### 2.2 Akibatnya

Kecepatan gas naik terus. Pada 200 cc, MGV sudah 96 m/s di 9.000 rpm — padahal di 150 cc masih 72 m/s.

Konsekuensinya:

1. **Torsi bawah naik** — karena kapasitas naik dan kecepatan gas di rpm rendah jadi lebih sehat
2. **Tenaga puncak turun atau stagnan** — karena head sudah tercekik di rpm yang lebih rendah
3. **Puncak tenaga bergeser turun** — mesin jadi "berat di atas"

Ini kenapa banyak bore-up terasa lebih bertenaga di putaran bawah tapi **tidak lebih cepat** di lintasan.

### 2.3 Kapan bore-up masuk akal

| Kondisi | Bore-up masuk akal? |
|---|---|
| Head juga diporting dan valve dibesarkan | **ya** |
| Head standar, kejar torsi bawah harian | ya |
| Head standar, kejar tenaga puncak | **tidak** |
| Sudah mentok bore, head belum diporting | **porting dulu** |

**Aturan praktis:** naikkan kapasitas dan luas throat **bersama-sama**, jaga rasio mm²/cc tetap. Kalau kapasitas naik 33%, luas throat harus naik 33% juga — dan itu biasanya berarti valve lebih besar, bukan cuma porting.

### 2.4 Contoh nyata dari mesin contoh

**Mesin Contoh A** (199 cc, 2 valve): throat 3,31 mm²/cc
**Mesin Contoh B** (150 cc, 4 valve): throat 4,28 mm²/cc

Mesin B berkapasitas 25% lebih kecil tapi bernapas **29% lebih lega per cc**. Itu sebabnya potensi tenaganya lebih tinggi (41 vs 35 HP) walau kapasitasnya lebih kecil.

**Pelajarannya:** menambah kapasitas bukan satu-satunya cara — dan sering bukan cara terbaik.

---

## 3. Rasio rod

### 3.1 Definisi

```
rasio rod = panjang rod / stroke
```

Diukur dari pusat pin ke pusat big end.

| Rasio | Keterangan |
|---|---|
| < 1,6 | sangat pendek |
| 1,6–1,75 | pendek, khas mesin kecil |
| 1,75–1,9 | umum |
| > 1,9 | panjang, khas mesin balap besar |

### 3.2 Pengaruhnya

**Rod pendek — merugikan:**

- **Side thrust lebih besar.** Sudut rod terhadap sumbu cylinder lebih besar, sehingga gaya menekan piston ke dinding liner lebih kuat. Akibatnya gesekan naik dan keausan liner lebih cepat.
- **Percepatan puncak di TDC lebih tinggi.** Faktor `(1 + r/L)` dalam rumus percepatan membesar.

**Rod pendek — menguntungkan:**

- **Piston menjauh dari TDC lebih cepat.** Ini melonggarkan kelegaan valve-piston — kantong valve bisa lebih dangkal.
- **Dwell di TDC lebih singkat.** Waktu untuk detonasi berkembang lebih pendek, sedikit menambah margin.

**Yang TIDAK banyak berubah:**

- **Kompresi dinamis.** Untuk stroke 58 mm, perbedaan rod 95 vs 102 mm cuma menggeser DCR sebesar 0,05. Praktis tidak berarti.
- **Torsi.** Rasio rod tidak mengubah torsi secara berarti — ini mitos yang mirip dengan mitos stroke panjang.

### 3.3 Percepatan piston

```
a_TDC = ω² × r × (1 + r/L)
ω = 2π × rpm / 60,    r = stroke/2
```

Contoh untuk stroke 58 mm: [HITUNG]

| Rod | Rasio | g di TDC @12.000 rpm |
|---|---|---|
| 90 mm | 1,55 | 6.219 |
| 95 mm | 1,64 | 6.093 |
| 105 mm | 1,81 | 5.892 |
| 115 mm | 1,98 | 5.746 |

Selisih rod 90 ke 115 mm cuma **8%** pada percepatan. Rasio rod bukan variabel yang menentukan — kecepatan piston dan rpm jauh lebih berpengaruh.

### 3.4 Praktisnya

Pada mesin matic, panjang rod biasanya **sudah ditentukan** oleh block dan crankshaft yang tersedia. Rod aftermarket dengan panjang berbeda ada, tapi mengubahnya berarti mengubah deck height juga.

**Kesimpulan praktis:** jangan menghabiskan usaha mengejar rasio rod. Pengaruhnya kecil dibanding bore/stroke, head, dan cam.

---

## 4. Jumlah valve

### 4.1 Perbandingan arsitektur

| Arsitektur | Luas valve isap / bore | Kelebihan | Kekurangan |
|---|---|---|---|
| **2 valve** | 0,24 (bore kecil) – 0,30 (bore besar) | sederhana, murah, valvetrain ringan | luas valve terbatas di bore kecil |
| **3 valve** | ~0,26 | lebih baik daripada 2 valve, valvetrain sederhana | valve buang tunggal panas, spark plug menepi |
| **4 valve** | 0,30–0,35 | luas valve terbesar, spark plug di tengah | valvetrain rumit, lebih berat |

### 4.2 Hukuman bore kecil

Ini yang paling penting dipahami dan paling sering disalahpahami.

Orang menyalahkan "2 valve" padahal yang membatasi adalah **bore**.

| Mesin | Bore | Valve isap | Valve/bore (diameter) | Luas valve/bore |
|---|---|---|---|---|
| Drag V8 besar, 2 valve | 119 mm | 65 mm | 0,545 | **0,297** |
| Mesin Contoh A, 2 valve | 63 mm | 31 mm | 0,492 | **0,242** |
| Mesin Contoh B, 4 valve | 57,3 mm | 22 mm ×2 | 0,384 | **0,295** |

Mesin drag V8 dengan **2 valve** mencapai luas valve/bore yang **sama dengan mesin 4 valve** — karena bore-nya 119 mm.

Kenapa? Spark plug, lebar seat, dan lahan gasket memakan ruang yang hampir tetap dalam milimeter. Pada bore kecil, ruang tetap itu porsinya jauh lebih besar.

**Implikasi praktis:**

| Bore | Keuntungan pindah ke 4 valve |
|---|---|
| < 60 mm | **besar** — 0,24 → 0,30, naik 25% |
| 60–80 mm | sedang |
| > 90 mm | kecil — 2 valve sudah cukup |

Untuk mesin matic 125–250 cc yang bore-nya 50–70 mm, **4 valve memberi keuntungan besar**.

### 4.3 Karakter 3 valve

Arsitektur 3 valve (2 isap + 1 buang) punya sifat khas:

**Kelemahannya ada di sisi ISAP, bukan buang.** Ini sering salah dipahami.

| | 3 valve | 4 valve |
|---|---|---|
| Luas valve isap / bore | **0,262** | **0,295** |
| Rasio throat buang/isap | 0,679 | 0,661 |
| Lift kritis isap | 4,59 mm | 4,81 mm |
| **Lift kritis buang** | **5,03 mm** | 3,68 mm |

Rasio throat buang/isap 3 valve justru **sehat** — sebanding dengan 4 valve. Yang berkurang adalah sisi isap: minus 11%, karena valve buang tunggal yang besar memakan lahan bore.

**Konsekuensi ke cam:** 3 valve butuh durasi lebih panjang untuk rpm yang sama.

| RPM | Durasi isap 3 valve | Durasi isap 4 valve |
|---|---|---|
| 10.000 | 238° | ~217° |
| 12.000 | **285°** | **261°** |

Durasi lebih panjang berarti overlap lebih besar dan rentang rpm lebih sempit.

**Konsekuensi ke lift:** pada 3 valve, **valve buang butuh lift lebih tinggi daripada valve isap** — kebalikan dari 4 valve. Sebabnya satu valve besar punya keliling total lebih kecil daripada dua valve kecil berluas sama.

**Batasan lain 3 valve:**

1. **Valve buang tunggal memikul seluruh panas.** Kalau ditambah pendingin udara, ini titik lemah utamanya.
2. **Spark plug tidak di tengah.** Ruang bakar asimetris, jalur api ke sisi isap panjang. Kompresi harus **1 angka lebih rendah** dibanding 4 valve pada bahan bakar yang sama.

### 4.4 Ringkasan pemilihan

| Sasaran | Pilihan |
|---|---|
| Tenaga puncak maksimum, bore < 70 mm | **4 valve** |
| Basis sudah 3 valve, budget terbatas | 3 valve, terima batasannya |
| Basis 2 valve bore besar (> 90 mm) | 2 valve cukup |
| Basis 2 valve bore kecil, kejar puncak | **ganti ke 4 valve kalau ada** |

---

## 5. Inersia crankshaft

### 5.1 Apa yang disimpan

Crankshaft yang berputar menyimpan energi kinetik:

```
E = ½ × I × ω²
I = Σ m × r²
```

Perhatikan `r²` — **massa di jari-jari besar jauh lebih berpengaruh** daripada massa di dekat sumbu. Memangkas 100 gram di tepi bandul setara memangkas beberapa ratus gram di dekat poros.

### 5.2 Besarannya

Untuk crankshaft mesin 150 cc dengan I ≈ 0,010 kg·m² pada 12.000 rpm:

```
ω = 2π × 12000/60 = 1257 rad/s
E = ½ × 0,010 × 1257² = 7.900 J
```

Sebagai pembanding, energi kinetik motor + pengendara (150 kg) pada 33 km/h adalah sekitar 6.300 J.

Artinya: **energi yang tersimpan di crankshaft sebanding dengan energi motor pada kecepatan sedang.** Itu bukan jumlah yang bisa diabaikan.

### 5.3 Pertukarannya

| | Inersia tinggi | Inersia rendah |
|---|---|---|
| Putaran naik | lambat | cepat |
| Launch | lebih mudah, energi tersimpan membantu | mudah bogging |
| Traksi awal | lebih halus | lebih mudah spin |
| Getaran | lebih halus | lebih kasar |
| Akselerasi setelah launch | sedikit terhambat | lebih baik |

### 5.4 Untuk matic drag

CVT sedikit memisahkan mesin dari roda, tapi tidak sepenuhnya. Pertimbangannya:

**Saat launch:** inersia crankshaft membantu — energi tersimpan dilepas saat centrifugal clutch menggigit, memberi dorongan awal.

**Saat akselerasi:** CVT menahan mesin di rpm tetap, jadi crankshaft **tidak perlu terus dipercepat**. Di fase ini inersia hampir tidak merugikan.

**Kesimpulan:** untuk matic drag, memangkas crankshaft habis-habisan **tidak memberi keuntungan sebesar** yang diperoleh motor gear. Memangkas secukupnya untuk mengurangi beban bearing lebih masuk akal daripada memangkas untuk "responsif".

### 5.5 Balance factor

Mesin 1 cylinder tidak bisa diseimbangkan sempurna. Massa bolak-balik (piston, ring, pin, ujung kecil rod) menghasilkan gaya vertikal yang tidak bisa dilawan penuh oleh massa penyeimbang yang berputar.

```
balance factor = massa penyeimbang / massa bolak-balik
```

| Balance factor | Akibat |
|---|---|
| 0% | getaran vertikal maksimum |
| **50–65%** | **kompromi umum** |
| 100% | getaran vertikal hilang, tapi muncul getaran horizontal penuh |

Menyeimbangkan 100% cuma **memindahkan** getaran dari vertikal ke horizontal, tidak menghilangkannya. Karena itu semua mesin 1 cylinder memakai kompromi.

Nilai yang tepat bergantung pada bagaimana mesin dipasang di rangka dan rpm kerjanya. Untuk mesin putaran tinggi, faktor yang lebih rendah (50–55%) umum dipakai.

**Kalau mengganti piston dengan yang lebih ringan**, balance factor berubah — dan crankshaft perlu diseimbangkan ulang. Ini sering dilupakan, dan akibatnya getaran di rpm tinggi.

---

## 6. Ringkasan Tahap 2

**Yang harus kamu putuskan sebelum lanjut:**

1. **Bore dan stroke.** Overbore memberi potensi sampai 143% dari square; overstroke cuma 66%. Untuk CVT drag, condong ke overbore selama crankcase mengizinkan.
2. **Jangan bore-up tanpa membesarkan head.** Kapasitas naik dengan head tetap memindahkan tenaga ke bawah, bukan menambahnya.
3. **Rasio rod pengaruhnya kecil.** Jangan habiskan usaha di sini.
4. **Jumlah valve:** untuk bore < 70 mm, 4 valve memberi keuntungan besar. Kelemahan 3 valve ada di sisi isap, bukan buang.
5. **Inersia crankshaft** kurang kritis pada CVT dibanding motor gear. Kalau ganti piston ringan, seimbangkan ulang.

**Mitos yang harus dibuang:**

| Mitos | Kenyataan |
|---|---|
| Stroke panjang lebih bertorsi | torsi per cc sama; yang beda letak puncaknya |
| Rasio rod panjang lebih bertenaga | pengaruhnya < 8% pada percepatan |
| Bore-up selalu menambah tenaga | tanpa head, tenaga puncak bisa turun |
| 2 valve selalu kalah daripada 4 valve | di bore besar, 2 valve bisa setara |

**Berikutnya:** Tahap 3 — cylinder head, yang menentukan plafon tenaga mesin.

---

# TAHAP 3 — ALIRAN: CYLINDER HEAD

*Menentukan plafon tenaga mesin.*

---

## 1. Kenapa head menentukan segalanya

Tenaga mesin berbanding lurus dengan **massa udara** yang bisa masuk dan terbakar. Semua komponen lain — cam, pengapian, exhaust, CVT — cuma menentukan seberapa dekat kamu ke plafon yang sudah ditetapkan head.

```
Tenaga ≈ CFM × 0,43–0,50        [4 langkah, NA]
```

Aturan kasar ini cukup akurat untuk perencanaan. CFM di sini adalah flow head pada depresi acuan (28 inH₂O).

**Konsekuensinya:** kalau head-mu mengalirkan 85 CFM, tidak ada cam, exhaust, atau ECU yang bisa membuatnya menghasilkan 50 HP. Plafonnya sekitar 38 HP, titik.

---

## 2. Valve dan batas geometri

### 2.1 Berapa besar valve yang muat

| Arsitektur | Valve isap (× bore) | Valve buang (× bore) |
|---|---|---|
| 2 valve bore kecil | 0,49 | 0,43 |
| 2 valve bore besar | 0,545 | 0,47 |
| 3 valve (2 in + 1 ex) | 0,33–0,37 per valve | 0,41–0,46 |
| 4 valve | 0,37–0,40 per valve | 0,32–0,35 |

### 2.2 Ukuran yang benar-benar penting

Bukan diameter valve, tapi **luas valve isap dibagi luas bore**:

```
rasio = n_valve × (D_valve / bore)²
```

| Rasio | Keterangan |
|---|---|
| 0,24 | 2 valve bore kecil — terbatas |
| 0,26 | 3 valve |
| 0,297 | 2 valve bore besar, ATAU 4 valve bore kecil |
| 0,30–0,35 | 4 valve bagus |

**Ini plafon geometri.** Tidak bisa dilampaui tanpa mengganti head atau bore.

### 2.3 Rasio valve buang terhadap isap

```
rasio luas = (n_ex × D_ex²) / (n_in × D_in²)
```

Nilai lazim 0,70–0,80.

Tapi yang lebih menentukan keputusan cam bukan rasio valve, melainkan **rasio throat** — dibahas di 3.4.

---

## 3. Throat: pembatas yang sesungguhnya

### 3.1 Kenapa throat, bukan valve

Pada lift rendah, **luas tirai** yang membatasi:
```
A_tirai = n_valve × π × D_valve × lift
```

Pada lift tinggi, **throat** yang membatasi:
```
A_throat = n_valve × π/4 × D_throat²
```

Titik silangnya adalah **lift kritis**:
```
lift_kritis = A_throat / (n_valve × π × D_valve)
```

### 3.2 Membesarkan throat

**Ini satu-satunya perubahan yang menaikkan plafon flow.** Bentuk port hanya menentukan seberapa dekat kamu ke plafon itu.

Batasnya lebar seat:
```
lebar_seat = (D_valve − D_throat) / 2
```

| Lebar seat | Keterangan |
|---|---|
| ≥ 1,2 mm | konservatif, tahan lama |
| 0,9–1,2 mm | praktik balap lazim |
| 0,7–0,9 mm | agresif, butuh material bagus |
| < 0,7 mm | berisiko, terutama sisi buang |

### 3.3 Contoh penerapan

Mesin Contoh B, valve isap 22 mm, throat awal 19,5 mm (rasio 0,886).

Rasio 0,935 yang terbukti di Mesin Contoh A memberi throat 20,6 mm — tapi lebar seat tinggal 0,71 mm, terlalu tipis untuk valve sekecil itu.

Kompromi: **throat 20,2 mm**, lebar seat 0,9 mm.

| | Sebelum | Sesudah |
|---|---|---|
| Throat | 19,5 mm | 20,2 mm |
| Luas throat (2 valve) | 597 mm² | 641 mm² |
| Gain | — | **+7,4%** |
| CFM @28" | 84,5 | 90,7 |
| Potensi HP | 38,0 | ~41 |

Tujuh persen dari satu perubahan yang tidak menambah ongkos apa pun — cuma cara menggerinda seat yang berbeda.

### 3.4 Rasio throat buang terhadap isap

Ini yang menentukan apakah cam boleh simetris:

```
rasio = A_throat_ex / A_throat_in
```

| Rasio | Tindakan |
|---|---|
| < 0,63 | sisi buang sempit — tambah 8–12° durasi ex |
| 0,63–0,72 | **cam simetris aman** |
| > 0,72 | sisi buang lega |

Contoh: Mesin Contoh A punya rasio 0,671 dan berjalan dengan cam simetris 281/281. Mesin Contoh B punya rasio 0,685 — selisih 2,1%, jadi cam simetris tetap benar.

**Throat buang jangan digerus sebesar throat isap.** Seat buang butuh lebar untuk membuang panas valve. Rasio throat/valve sisi buang yang lazim: **0,86–0,90**, lebih konservatif daripada sisi isap.

---

## 4. Lift kritis

### 4.1 Kenapa mesin balap melampauinya jauh

| Mesin | Lift kritis in | Lift dipakai | Kelipatan |
|---|---|---|---|
| Contoh A (2 valve) | 6,78 mm | 10,8 mm | 1,59× |
| Contoh B (4 valve) | 4,64 mm | 9,0 mm | 1,94× |
| Contoh C (3 valve) | 4,59 mm | — | — |

Semua berjalan **jauh di atas** lift kritis. Sebabnya: yang dibayar di mesin balap bukan flow puncak steady, tapi **time-area** — integral luas terhadap waktu.

Ini koreksi penting terhadap aturan umum "lift maksimum berguna = 0,25 × diameter valve". Aturan itu benar untuk flow puncak, salah untuk mesin balap.

### 4.2 Perbedaan antar arsitektur

| Arsitektur | Lift kritis in | Lift kritis ex |
|---|---|---|
| 4 valve (2 in, 2 ex) | 4,64 mm | **3,68 mm** |
| 3 valve (2 in, 1 ex) | 4,59 mm | **5,03 mm** |

Pada 3 valve, valve buang tunggal butuh **lift lebih tinggi** daripada valve isap. Satu valve besar punya keliling total lebih kecil daripada dua valve kecil berluas sama, jadi butuh lift lebih tinggi untuk membuka tirai yang sama.

**Praktisnya untuk 3 valve:** lift ex sekitar 15% lebih tinggi daripada lift in.
**Praktisnya untuk 4 valve:** lift ex bisa 10–15% lebih rendah daripada lift in tanpa rugi flow — menghemat beban valvetrain.

---

## 5. Port: luas penampang dan kecepatan gas

### 5.1 Rumus pokok

```
MGV = (luas piston / CSA port) × MPS
```

Untuk port bercabang (4 valve), CSA yang dipakai adalah CSA **runner bersama** sebelum pecah dua.

### 5.2 Dua jangkar untuk menentukan CSA

Pakai keduanya. Kalau hasilnya berdekatan, kepercayaan naik. Kalau berbeda jauh, ada asumsi yang salah.

**Jangkar kecepatan:**
```
CSA = luas_piston × MPS / MGV_target
```

**Jangkar rasio:**
```
CSA = rasio_port_throat_acuan × A_throat_baru
```

### 5.3 Contoh penerapan

Mesin Contoh B pada 12.000 rpm:

| Jangkar | Hasil |
|---|---|
| Kecepatan gas (97 m/s dari Contoh A) | 615 mm² |
| Rasio port/throat (1,035 dari Contoh A) | 663 mm² |

Selisih 7,8% — cukup dekat untuk dipercaya, cukup jauh untuk jadi **rentang desain yang jujur: 615–665 mm²**.

**Peringatan penting:** sebelum data throat sebenarnya diketahui, jangkar kecepatan memberi 427 mm² karena throat Mesin Contoh A ditebak 0,86 (padahal 0,935). Selisihnya **40%**, dan seluruhnya dari satu asumsi yang salah.

**Pelajarannya:** pemeriksaan silang tidak cuma menaikkan kepercayaan, tapi **mendeteksi asumsi busuk**.

### 5.4 Rasio port/throat: menyempit atau melebar

| Rasio | Artinya | Akibat |
|---|---|---|
| > 1,0 | port lebih besar daripada throat | aliran **mempercepat** menuju throat — stabil, menempel |
| < 1,0 | port lebih kecil daripada throat | titik sempit pindah ke port; ada **pelebaran** sebelum valve — cenderung lepas |

Mesin Contoh A: 1,035 — port sedikit lebih besar. Ini kondisi yang benar.

Pada Mesin Contoh B, CSA 615 mm² memberi rasio 0,96 (melebar) sementara 665 mm² memberi 1,04 (menyempit). Ini alasan kuat untuk condong ke **ujung atas rentang**.

### 5.5 Port buang

Port buang jauh lebih besar relatif terhadap throat-nya dibanding port isap, karena gas buang panas volumenya berlipat.

| | Mesin Contoh A |
|---|---|
| Throat buang | 23,8 mm (443 mm²) |
| Port buang | 29 mm (660 mm²) |
| **Rasio port/throat** | **1,49** |
| Kecepatan gas port buang | 101 m/s |

Perhatikan: port buang 29 mm hampir sama besar dengan port isap 29,5 mm, walau valve buangnya lebih kecil.

Kecepatan gas buang 101 m/s hampir identik dengan port isap 97 m/s — konsistensi yang bagus dan bisa dipakai sebagai jangkar.

**Untuk Mesin Contoh B:** dua jangkar memberi 594–653 mm², atau sekitar **28 mm diameter setara**.

---

## 6. Bentuk port

### 6.1 Penampang: bundar atau oval

Untuk port 4 valve bercabang, penampang **tinggi-sempit** (aspect tinggi:lebar sekitar 1,3) secara teori lebih baik daripada bundar. Port yang tinggi membuat short-turn radius lebih landai relatif terhadap tinggi port, sehingga aliran tidak mudah lepas di lantai.

Tapi Mesin Contoh A memakai port **bundar** 29,5 mm dan berhasil. Ini bukan hukum mati.

Rumus luas superelips:
```
Luas ≈ 0,92 × lebar × tinggi
tinggi = √(CSA / (0,92 × aspect)) × aspect
```

Untuk CSA 615 mm² dengan aspect 1,30: **22,7 W × 29,5 H mm**.

### 6.2 Short-turn radius

Bagian dalam tikungan port — lantainya — adalah tempat aliran paling mudah lepas.

```
R_short_turn minimum ≈ 0,40 × tinggi port
```

Untuk port setinggi 29,5 mm: **R minimum 11,8 mm**.

**Menggerus short-turn terlalu tajam adalah kesalahan porting paling umum.** Yang terlihat seperti "melancarkan jalan" justru menciptakan zona separasi yang menutup sebagian penampang efektif — port jadi lebih besar tapi mengalir lebih sedikit.

### 6.3 Bowl di bawah valve

```
Luas bowl maksimum ≈ 1,10–1,15 × luas throat
```

Menggerus bowl lebih besar menurunkan kecepatan tepat di tempat yang paling butuh kecepatan.

Untuk Mesin Contoh B: **maksimum 669 mm²**.

### 6.4 Taper

Port harus menyempit atau melebar **secara halus dan monoton**. Perubahan mendadak, terutama dekat throat, menciptakan separasi.

Perubahan luas sebaiknya mengikuti kurva halus, bukan garis lurus — taper linear memberi perubahan mendadak di kedua ujungnya.

### 6.5 Mulut port di flange manifold

Bentuk mulut port di bidang flange berpengaruh besar — sering lebih besar daripada rugi tikungan seluruh port.

Sambungan manifold ke head yang **tidak sebidang** atau **bertepi tajam** bisa memakan lebih banyak flow daripada short-turn radius yang digerus susah payah.

**Ini perbaikan paling murah yang paling sering diabaikan.** Pastikan:
- Manifold dan head benar-benar sebidang (pakai dowel atau bikin sendiri)
- Tidak ada step di sambungan
- Tepi mulut port diberi radius, bukan dibiarkan tajam
- Gasket tidak menonjol ke dalam saluran

---

## 7. Memperkirakan flow tanpa flowbench

Kalau tidak punya akses flowbench, flow bisa diperkirakan dari luas throat:

```
v_teoretis = √(2 × Δp / ρ)
Q_teoretis = A_throat × v_teoretis
CFM        = Q × 2118,88
CFM_nyata  = CFM_teoretis × Cf
```

Untuk depresi 28 inH₂O: `v_teoretis = 107,6 m/s`

| Cf | Keterangan |
|---|---|
| 0,55 | standar pabrikan |
| 0,62 | porting bagus |
| 0,70 | porting sangat bagus |

**Contoh Mesin Contoh B:** throat 641 mm², Cf 0,62
```
Q = 641e-6 × 107,6 = 0,0690 m³/s
CFM = 0,0690 × 2118,88 = 146,1 teoretis
CFM nyata = 146,1 × 0,62 = 90,6
Potensi HP = 90,6 × 0,45 = 40,8
```

**Perhatikan:** ini **perkiraan**, bukan pengukuran. Cf sebenarnya bisa berbeda ±15% tergantung kualitas pengerjaan. Pakai untuk perencanaan, jangan untuk menjanjikan hasil.

---

## 8. Urutan pengerjaan porting

Urutan ini penting — mengerjakan dengan urutan terbalik bisa merusak yang sudah benar.

**1. Ukur dulu, semuanya.** Throat, CSA di beberapa titik, tinggi dan lebar port, radius short-turn. Catat.

**2. Tentukan target CSA** dengan dua jangkar (5.2).

**3. Kerjakan seat dan throat lebih dulu.** Ini menentukan plafon. Multi-angle atau radius, throat sesuai target, lebar seat sesuai tabel 3.2.

**4. Bentuk bowl.** Jangan lebih dari 1,15 × luas throat. Haluskan transisi dari throat ke bowl.

**5. Short-turn radius.** Jangan lebih tajam dari 0,40 × tinggi port. Kalau ragu, tinggalkan lebih tebal — bisa digerus lagi nanti, tidak bisa dikembalikan.

**6. Badan port menuju CSA target.** Jaga taper halus dan monoton.

**7. Mulut port dan sambungan manifold.** Sebidang, tanpa step, tepi diberi radius.

**8. Ukur lagi.** Bandingkan dengan target. Catat selisihnya.

**Aturan emas porting:** **material bisa dibuang, tidak bisa dikembalikan.** Kalau ragu, kerjakan setengahnya dulu, ukur, baru lanjutkan.

---

## 9. Ringkasan Tahap 3

1. **Head menentukan plafon tenaga.** Tenaga ≈ CFM × 0,43–0,50.
2. **Luas valve isap / luas bore** adalah plafon geometri. 0,24 untuk 2 valve bore kecil, 0,30+ untuk 4 valve.
3. **Throat adalah pembatas sesungguhnya**, dan membesarkannya adalah satu-satunya cara menaikkan plafon.
4. **Batas throat adalah lebar seat**, bukan rasio. 0,9 mm untuk isap, lebih lebar untuk buang.
5. **CSA port ditentukan dengan dua jangkar.** Kalau berbeda jauh, ada asumsi yang salah.
6. **Rasio port/throat sebaiknya > 1,0** — port sedikit lebih besar daripada throat.
7. **Short-turn radius minimum 0,40 × tinggi port.** Menggerusnya terlalu tajam adalah kesalahan paling umum.
8. **Mulut port di flange sering lebih berpengaruh** daripada bentuk port di dalamnya.
9. **Kerjakan seat dan throat dulu**, badan port terakhir.

**Berikutnya:** Tahap 4 — camshaft, yang menentukan di putaran berapa plafon ini tercapai.

---

# TAHAP 4 — TIMING: CAMSHAFT

*Menentukan di putaran berapa plafon head tercapai.*

---

## 1. Apa yang sebenarnya diatur cam

Cam tidak "mengisi ruang bakar". Head sudah menentukan plafonnya. Cam mengatur **kapan** valve membuka dan menutup relatif terhadap piston dan gelombang tekanan.

Empat kejadian, urut menurut kepentingannya:

| # | Kejadian | Menentukan |
|---|---|---|
| **1** | **IVC** — valve isap menutup | kompresi dinamis, rpm efisiensi penjebakan puncak |
| **2** | **Durasi + lift** | berapa banyak yang bisa lewat (time-area) |
| **3** | **Overlap** di TDC | pembilasan sisa gas buang |
| **4** | **EVO** — valve buang membuka | tukar kerja ekspansi dengan rugi pemompaan |

Ditambah satu yang bukan soal tenaga sama sekali: **kelegaan valve-piston**. Ini soal mesin pecah atau tidak.

---

## 2. IVC dan kompresi dinamis

### 2.1 Posisi piston

```
s(θ) = r(1 − cos θ) + L − √(L² − (r sin θ)²)
```
dengan `r = stroke/2`, `L = panjang rod`, `θ` diukur dari TDC.

### 2.2 Kompresi dinamis

```
DCR = 1 + (V_sapu_saat_IVC / Vd) × (CR − 1)
```
dengan `V_sapu_saat_IVC = luas_piston × s(180° + IVC_ABDC)`

### 2.3 Pengaruh IVC

Mesin Contoh B (149,6 cc, bore 57,3, stroke 58, rod 95, CR 14:1): [HITUNG]

| IVC (ABDC) | DCR |
|---|---|
| 35° | 13,13 |
| 45° | 12,56 |
| 55° | 11,86 |
| 65° | 11,02 |
| 75° | 10,10 |

**Rentangnya lebar. Kompresi statis sendirian tidak berarti apa-apa tanpa IVC.**

### 2.4 Konsekuensi yang sering terlewat

Durasi lebih panjang mendorong IVC lebih telat, dan IVC lebih telat menurunkan DCR. Maka:

> **RPM sasaran, kompresi, dan bahan bakar adalah satu paket yang tidak bisa dipilih terpisah.**

Menaikkan rpm sasaran memaksa durasi lebih panjang → IVC lebih telat → DCR turun → kompresi statis boleh lebih tinggi, atau oktan bahan bakar boleh lebih rendah.

---

## 3. Durasi dari time-area

### 3.1 Prinsip

Yang harus dipertahankan antar mesin adalah **jendela aliran per siklus per cc**:

```
time-area ∝ (A_throat × durasi) / (kapasitas × rpm)
```

Membalik untuk mencari durasi mesin baru:

```
durasi_baru = durasi_acuan × (A_thr_acuan / A_thr_baru)
                            × (Vd_baru / Vd_acuan)
                            × (rpm_baru / rpm_acuan)
```

### 3.2 Hasil yang berlawanan intuisi

| Mesin | Kapasitas | Throat | RPM | Durasi |
|---|---|---|---|---|
| Contoh A (2 valve) | 199,5 cc | 661 mm² | 10.000 | 281° |
| Contoh B (4 valve) | 149,6 cc | 641 mm² | 12.000 | **261°** |

**Durasi turun walau rpm naik.**

Sebabnya: head 4 valve bernapas 29% lebih lega per cc (4,28 vs 3,31 mm²/cc). Butuh waktu lebih sedikit untuk memasukkan jumlah yang sama.

Ini contoh kenapa aturan jempol "rpm tinggi = durasi panjang" bisa menyesatkan. Yang benar: rpm tinggi **dan luas valve tetap** butuh durasi panjang.

### 3.3 Tabel durasi terhadap RPM

Mesin Contoh B: [HITUNG]

| RPM sasaran | Durasi isap @1mm |
|---|---|
| 11.000 | 239° |
| 11.500 | 250° |
| **12.000** | **261°** |
| 12.500 | 271° |
| 13.000 | 282° |

Mesin Contoh C (3 valve, luas valve isap/bore cuma 0,262):

| RPM | Durasi isap |
|---|---|
| 10.000 | 238° |
| 12.000 | **285°** |

Selisih 24° pada rpm yang sama — itu ongkos nyata dari 11% luas valve yang hilang.

### 3.4 Durasi buang

Ditentukan oleh **rasio throat buang/isap** (lihat Tahap 3, bagian 3.4):

| Rasio throat ex/in | Tindakan |
|---|---|
| < 0,63 | tambah 8–12° durasi ex |
| 0,63–0,72 | **cam simetris** |
| > 0,72 | sisi buang lega |

Mesin Contoh A (rasio 0,671) berjalan simetris 281/281. Mesin Contoh B (rasio 0,685) juga simetris 261/261.

---

## 4. Overlap, LSA, dan ICL

### 4.1 Definisi

```
durasi_in  = IVO_BTDC + 180 + IVC_ABDC
durasi_ex  = EVO_BBDC + 180 + EVC_ATDC
overlap    = IVO_BTDC + EVC_ATDC
ICL        = durasi_in / 2 − IVO_BTDC        (ATDC)
ECL        = durasi_ex / 2 − EVC_ATDC        (BTDC)
LSA        = (ICL + ECL) / 2
```

### 4.2 Contoh penguraian cam

Mesin Contoh A: EX buka 63 BBDC, EX tutup 38 ATDC, IN buka 38 BTDC, IN tutup 63 ABDC.

| | |
|---|---|
| Durasi in / ex | 281° / 281° (simetris) |
| Overlap | 76° |
| ICL / ECL | 102,5° ATDC / 102,5° BTDC |
| LSA | 102,5° |

LSA 102,5° ketat — khas mesin drag yang mengejar puncak, bukan rentang rpm yang lebar.

### 4.3 Menskalakan overlap

Yang harus dipertahankan adalah **luas tirai overlap per cc**:

```
luas_per_cc = n_valve × π × D_valve × lift_di_TDC / kapasitas
```

Ini krusial untuk 4 valve. Dua valve isap memberi luas tirai jauh lebih besar per milimeter lift dibanding satu valve besar.

**Contoh:** Mesin Contoh A punya 1 valve 31 mm dengan lift TDC 1,83 mm pada 199,5 cc. Mesin Contoh B dengan 2 valve 22 mm pada 149,6 cc perlu lift TDC **0,97 mm** — bukan 1,83, dan bukan 2,55 (yang keluar kalau diskalakan lewat diameter saja).

### 4.4 Jebakan penafsiran "lift overlap"

Angka lift overlap yang beredar sering ambigu: lift **satu valve** atau **gabungan in + ex**?

Cara memastikannya: hitung dari sudut. Dengan profil harmonik,
```
lift(θ) = lift_maks × sin²(π × θ_dari_bukaan / durasi)
```

Untuk Mesin Contoh A (IVO 38 BTDC, durasi 281°, lift 10,8 mm):
```
lift di TDC = 10,8 × sin²(π × 38/281) = 1,83 mm per valve
gabungan in + ex = 3,67 mm
```

Angka yang beredar untuk mesin ini adalah "3,6 mm" — jadi jelas itu **gabungan**.

> **Sudut selalu lebih bisa dipercaya daripada angka lift.** Kalau bisa memilih, minta data timing.

### 4.5 Pertukaran pokok

Dengan durasi tetap, overlap lebih besar memaksa IVO lebih awal, yang memaksa IVC lebih awal juga, yang menaikkan DCR.

Mesin Contoh B, lift TDC 0,97 mm: [HITUNG]

| Durasi | IVO BTDC | IVC ABDC | ICL | Overlap | DCR (CR 14) |
|---|---|---|---|---|---|
| 239° | 25,4 | 33,4 | 94,0 | 51° | 13,21 |
| 250° | 26,6 | 43,1 | 98,3 | 53° | 12,68 |
| **261°** | **27,7** | **52,8** | **102,5** | **55°** | **12,07** |
| 271° | 28,9 | 62,5 | 106,8 | 58° | 11,24 |
| 282° | 30,0 | 72,2 | 111,1 | 60° | 10,34 |

**Tidak ada cara mendapatkan overlap besar dan IVC telat tanpa menambah durasi.**

### 4.6 Pemeriksaan silang yang berhasil

Perhatikan baris 261°: ICL keluar **102,5° ATDC** — persis sama dengan ICL Mesin Contoh A.

Dua perhitungan yang sama sekali tidak berbagi rumus (time-area dan luas overlap) bertemu di angka yang sama. Itu tanda kuat penskalaannya waras.

**Selalu cari pemeriksaan silang seperti ini.** Kalau tidak ketemu, kepercayaanmu terhadap hasilnya harus lebih rendah.

### 4.7 ICL sebagai tuas penyetelan

ICL adalah satu-satunya yang bisa diubah **setelah** cam dibeli, lewat *adjustable sprocket*:

| Perubahan | Efek |
|---|---|
| ICL dikurangi (cam dimajukan) | IVC lebih awal → DCR naik, tenaga bergeser ke bawah |
| ICL ditambah (cam dimundurkan) | IVC lebih telat → DCR turun, tenaga bergeser ke atas |

**Aturan praktis:** geser 2° dulu, ukur di dyno, baru lanjut. Geseran 4° sudah terasa jelas.

**Yang TIDAK bisa diubah dengan sprocket:** LSA. Memutar sprocket menggeser ICL dan ECL bersama-sama.

---

## 5. Kelegaan valve-piston

### 5.1 Kenapa kantong valve dibutuhkan

Di dekat TDC piston hampir tidak bergerak. Untuk stroke 58 mm rod 95 mm: [HITUNG]

| Sudut dari TDC | Turun piston |
|---|---|
| 4° | 0,09 mm |
| 8° | 0,28 mm |
| 14° | 1,10 mm |
| 20° | 2,27 mm |

Sementara valve sudah bergerak beberapa milimeter. Titik paling kritis biasanya **7–10° setelah TDC**.

### 5.2 Perhitungan

```
kebutuhan(θ) = lift_valve(θ) − turun_piston(θ)
kantong = maks(kebutuhan) × faktor_aman + kelegaan_minimum
```

| Parameter | Nilai |
|---|---|
| Faktor aman | 1,25 — profil harmonik meremehkan lift di sisi flank |
| Kelegaan minimum isap | 1,0–1,5 mm |
| Kelegaan minimum buang | 1,5–2,0 mm (valve buang memuai lebih banyak) |

### 5.3 Hasil untuk Mesin Contoh B

Durasi 261°, IVO 27,7 BTDC, lift 9 mm:

| | |
|---|---|
| Kantong yang dibutuhkan | **2,71 mm** |
| Titik paling kritis | **+7° dari TDC** |

Sebagai perbandingan, dengan overlap dua kali lipat (kesalahan penskalaan), kantong yang dibutuhkan jadi **4,00 mm** — dan itu memakan 20% anggaran volume ruang bakar.

### 5.4 Peringatan wajib

Perhitungan ini adalah **perkiraan awal**, bukan pengganti pemeriksaan fisik.

Yang tidak dimodelkan:
- Sudut valve terhadap sumbu cylinder
- Bentuk kubah piston
- Deformasi valvetrain pada rpm tinggi (rocker melentur, timing chain meregang)
- Profil cam sebenarnya, yang lebih agresif daripada model harmonik
- Pemuaian termal rod (bisa 0,1 mm — cukup untuk mengubah kelegaan)

> **Selalu cek dengan clay atau lilin sebelum mesin diputar. Tanpa pengecualian.**

**Cara cek clay:**
1. Pasang piston, rod, head, cam dengan timing final
2. Tempel clay setebal 3–4 mm di area kantong valve
3. Putar mesin dua putaran penuh dengan tangan, pelan
4. Bongkar, potong clay, ukur ketebalan tersisa dengan sigmat
5. Yang tersisa itulah kelegaan sebenarnya

**Kalau kelegaan kurang dari 1,0 mm (isap) atau 1,5 mm (buang), jangan diputar.**

---

## 6. Contoh spek cam lengkap

Mesin Contoh B, sasaran 12.000 rpm: [HITUNG]

| Parameter | Nilai |
|---|---|
| Durasi in / ex | **261° / 261° @1mm** |
| IN buka / tutup | **28° BTDC / 53° ABDC** |
| EX buka / tutup | **53° BBDC / 28° ATDC** |
| ICL / ECL | 102,5° ATDC / 102,5° BTDC |
| LSA | 102,5° |
| Overlap | 55° |
| Lift maks in | 9,0 mm |
| Lift maks ex | 7,6–9,0 mm |
| Lift di TDC | 0,97 mm per valve isap |
| Kantong valve | 2,71 mm |

Dibandingkan dengan Mesin Contoh A: durasi turun dari 281° ke 261°, overlap dari 76° ke 55°. Bukan karena lebih jinak, tapi karena dua valve isap memberi luas tirai jauh lebih besar per derajat.

LSA-nya sendiri dipertahankan persis di 102,5° — sama seperti cam yang terbukti.

---

## 7. Memesan cam

Yang harus disebutkan ke pembuat cam:

- [ ] **Durasi in dan ex, PADA LIFT BERAPA** (@1mm, @0.050", atau seat-to-seat)
- [ ] **Lift maksimum in dan ex** — di valve, bukan di lobe (kalau ada rocker ratio)
- [ ] **Rocker ratio**, kalau ada
- [ ] **ICL dan LSA** yang diinginkan
- [ ] **Base circle** — kalau diubah, clearance rocker berubah
- [ ] **Jenis lifter** (flat, roller, bucket)
- [ ] **RPM maksimum** — menentukan agresivitas ramp yang aman
- [ ] **Valve spring yang akan dipakai** — menentukan apakah ramp bisa seagresif itu

**Yang paling sering menimbulkan salah paham: acuan lift durasi.** Selalu sebutkan eksplisit.

---

## 8. Ringkasan Tahap 4

1. **IVC adalah kejadian terpenting** di seluruh camshaft — menentukan DCR.
2. **Durasi dihitung dari time-area**, bukan dari aturan jempol. Head yang bernapas lega butuh durasi lebih pendek.
3. **RPM, kompresi, dan bahan bakar adalah satu paket.** Tidak bisa dipilih terpisah.
4. **Overlap diskalakan lewat luas tirai per cc**, bukan lewat lift atau diameter.
5. **Angka "lift overlap" sering ambigu** — hitung dari sudut, bukan dari angka lift yang disebut.
6. **Cari pemeriksaan silang.** Kalau dua metode independen bertemu, kepercayaan naik tajam.
7. **ICL bisa disetel dengan sprocket, LSA tidak.**
8. **Kantong valve dihitung sebelum menghitung dome piston** — kantong ikut menambah volume ruang bakar.
9. **Cek clay wajib.** Perhitungan tidak menggantikannya.

**Berikutnya:** Tahap 5 — kompresi dan bahan bakar, yang tidak bisa ditentukan sebelum cam final.

---

# TAHAP 5 — KOMPRESI DAN BAHAN BAKAR

*Dua hal yang harus diputuskan bersamaan, dan hanya setelah cam final.*

---

## 1. Tiga angka kompresi yang berbeda

| Istilah | Definisi | Menentukan |
|---|---|---|
| **Kompresi statis (CR)** | rasio volume BDC terhadap TDC | rasio ekspansi, efisiensi termal |
| **Kompresi dinamis (DCR)** | dihitung dari posisi piston saat IVC | **detonasi** |
| **Rasio ekspansi** | sama dengan CR pada mesin konvensional | efisiensi termal |

Perbedaan antara DCR dan rasio ekspansi adalah alasan **kompresi statis tinggi tetap berguna walau IVC telat**: kamu membuang sebagian kompresi tapi mempertahankan seluruh ekspansi.

### 1.1 Efisiensi termal ideal

```
η = 1 − 1/CR^(γ−1)     dengan γ ≈ 1,4
```

| CR | η ideal |
|---|---|
| 11 | 61,6% |
| 12 | 62,9% |
| 13 | 64,1% |
| 14 | 65,2% |
| 15 | 66,1% |
| 16 | 67,0% |

**Perhatikan hasil yang semakin berkurang.** Dari 14 ke 15 cuma +1,5% relatif — sekitar 0,6 HP dari 40 HP. Sering tidak sepadan dengan risiko dan kerumitan yang ditambahkan.

---

## 2. Anggaran volume ruang bakar

### 2.1 Komponennya

Volume ruang bakar bukan cuma "ruang di head":

```
Vc_total = V_pentroof + V_gasket + V_deck + V_kantong_valve − V_dome_piston
```

| Komponen | Rumus |
|---|---|
| Pent-roof | luas_bore × tinggi_efektif (3–4 mm untuk 4 valve) |
| Gasket | luas_bore × tebal_gasket |
| Deck | luas_bore × jarak piston di bawah deck di TDC |
| Kantong valve | n_kantong × luas_kantong × kedalaman × ~0,40 |
| Dome piston | negatif — mengurangi volume |

Faktor 0,40 pada kantong valve karena bentuknya cekungan dangkal, bukan cylinder penuh.

### 2.2 Contoh nyata

Mesin Contoh B, bore 57,3 mm, target CR 14:1 pada 149,6 cc → Vc harus **11,50 cc**. [HITUNG]

| Komponen | Volume |
|---|---|
| Pent-roof (3,5 mm) | 9,03 cc |
| Gasket 0,8 mm | 2,06 cc |
| Deck 0,5 mm | 1,29 cc |
| 4 kantong valve 2,71 mm | 1,58 cc |
| **Total** | **13,95 cc** |

→ CR tanpa dome: **11,72:1**, bukan 14:1.

**Dome piston harus mengusir 2,45 cc** (tinggi rata-rata 0,95 mm).

### 2.3 Pelajaran

**Kantong valve ikut menambah volume ruang bakar.** Pada contoh di atas 14% anggaran; dengan overlap lebih besar bisa 20%.

Akibatnya nyata: head dipapas untuk mengejar kompresi, lalu kantong valve digerus untuk cam baru, dan sebagian kompresi yang baru didapat langsung hilang lagi.

> **Urutan yang benar: cam dulu → kantong valve → baru dome atau papasan.**

### 2.4 Cara mengukur Vc yang benar

Jangan pakai angka dari spesifikasi. Ukur.

1. Pasang piston di TDC persis (pakai dial indicator)
2. Pasang head dengan gasket yang akan dipakai, kencangkan sesuai torsi
3. Pasang valve dan spark plug
4. Isi ruang bakar lewat lubang spark plug dengan buret berisi minyak ringan atau alkohol
5. Baca volume yang masuk sampai penuh tanpa gelembung
6. Itulah Vc sebenarnya

**Selisih antara Vc terukur dan Vc dari spesifikasi bisa 1–2 cc — cukup untuk menggeser CR satu angka penuh.**

---

## 3. Bahan bakar

### 3.1 Yang menentukan potensi tenaga

Bukan energi per kilogram bahan bakar, tapi **energi per kilogram UDARA**.

Alasannya: mesin NA cuma bisa menghisap sejumlah udara tertentu. Udara yang terbatas, bukan bahan bakar. Yang menentukan tenaga adalah berapa banyak energi yang bisa dibawa tiap kilogram udara itu.

```
Energi per kg udara = LHV / AFR
```

### 3.2 Perbandingan

[HITUNG] — pada AFR tenaga puncak masing-masing:

| Bahan bakar | AFR stoich | AFR puncak | Lambda | MJ/kg udara | vs bensin | Dingin (K) | Volume × |
|---|---|---|---|---|---|---|---|
| Bensin 92 RON | 14,70 | 12,50 | 0,85 | 3,48 | 100% | 28 | 1,00 |
| Bensin 98 RON | 14,70 | 12,60 | 0,86 | 3,45 | 99% | 28 | 0,99 |
| **Avgas 100LL** | 14,90 | 12,80 | 0,86 | 3,40 | 98% | 27 | 1,01 |
| Race gas beroksigen | 12,90 | 11,50 | 0,89 | 3,48 | 100% | 33 | 1,07 |
| **Metanol** | 6,45 | 4,80 | 0,74 | **4,15** | **119%** | **228** | 2,45 |
| **Nitrometana** | 1,70 | 1,00 | 0,59 | **11,30** | **325%** | 557 | 8,19 |

*Dingin (K) = penurunan suhu muatan akibat penguapan bahan bakar.*

### 3.3 Membaca tabelnya

**Bensin, avgas, dan race gas non-oksigenat praktis SAMA potensi tenaganya** — semuanya 98–100%.

Ini penting dan sering disalahpahami. **Oktan tinggi tidak menambah tenaga.** Oktan mengukur ketahanan terhadap detonasi, bukan kandungan energi. Avgas 100LL justru sedikit **di bawah** bensin biasa dalam energi per kg udara.

**Yang diberikan oktan tinggi adalah izin untuk menaikkan kompresi dan memajukan pengapian** — dan dari situlah tenaganya datang, bukan dari bahan bakarnya sendiri.

**Metanol memberi +19% energi per kg udara**, plus pendinginan muatan 228 K. Pendinginan itu menaikkan kerapatan udara masuk dan menambah ketahanan detonasi — sehingga kompresi bisa lebih tinggi lagi. Efek totalnya bisa +25–30% dibanding bensin.

Harganya: konsumsi volume **2,45 kali** lipat. Sistem bahan bakar harus dibesarkan — injektor, pompa, saluran.

**Nitrometana memberi 325%** karena molekulnya membawa oksigen sendiri (CH₃NO₂). Tapi konsumsinya 8,2 kali lipat, dan mesinnya harus dirancang khusus dari nol.

### 3.4 Karakter tiap bahan bakar

**Bensin SPBU (Pertamax 92 / Turbo 98)**

| | |
|---|---|
| Kelebihan | murah, tersedia di mana-mana, tidak korosif |
| Kekurangan | oktan terbatas, kualitas bervariasi antar batch |
| Batas DCR praktis | 9,5 (92 RON), 10,5 (98 RON) |
| Cocok untuk | harian, kompresi sampai ~12:1 |

**Bensol / Avgas 100LL**

| | |
|---|---|
| Kelebihan | oktan sangat tinggi, kualitas konsisten, stabil disimpan |
| Kekurangan | mengandung timbal (merusak sensor O₂ dan katalis), harga tinggi, kadang sulit didapat |
| Batas DCR praktis | **12,8** — terbukti di Mesin Contoh A |
| Cocok untuk | balap kompresi tinggi dengan bensin |

Catatan penting: **timbal pada avgas melapisi elektroda spark plug dan sensor lambda.** Kalau memakai wideband untuk tuning, umurnya jauh lebih pendek. Spark plug juga perlu lebih sering diperiksa.

**Race gas beroksigen**

Bensin balap yang mengandung oksigen dalam molekulnya. Oktan sangat tinggi, dan oksigen bawaan memberi sedikit tambahan tenaga.

| | |
|---|---|
| Kelebihan | oktan tertinggi di kelas bensin, sedikit tambahan tenaga |
| Kekurangan | mahal, AFR harus disetel ulang (lebih kaya) |
| Perhatian | **AFR stoikiometrinya berbeda** (~12,9 bukan 14,7) — kalau ECU tidak disesuaikan, campuran jadi terlalu miskin |

**Metanol**

| | |
|---|---|
| Kelebihan | +19% energi per kg udara, pendinginan muatan besar, tahan detonasi luar biasa |
| Kekurangan | konsumsi 2,45×, korosif, menyerap air dari udara, susah start dingin |
| Batas DCR | 15+ |

**Yang harus disiapkan kalau pindah ke metanol:**
- Injektor dan pompa berkapasitas 2,5× lipat
- Saluran dan seal tahan metanol (karet biasa akan hancur)
- Sistem harus dikuras setelah pemakaian — metanol menyerap air dan mengkorosi
- Oli lebih cepat terkontaminasi
- Start dingin butuh bantuan (bensin priming atau pemanas)

**Nitrometana**

Bukan untuk mesin konversi. Butuh piston, rod, crankshaft, dan sistem bahan bakar yang dirancang khusus. Tekanan pembakaran berlipat kali lipat bensin.

Disebutkan di sini untuk kelengkapan, bukan sebagai pilihan yang realistis untuk mesin matic.

### 3.5 Lambda lebih berguna daripada AFR

Perhatikan kolom lambda di tabel. Lambda adalah AFR dibagi AFR stoikiometrinya:

```
λ = AFR / AFR_stoikiometri
```

| λ | Artinya |
|---|---|
| 1,00 | stoikiometri |
| < 1,00 | kaya |
| > 1,00 | miskin |

**Kenapa lambda lebih berguna:** angka AFR tenaga puncak berbeda-beda tiap bahan bakar (12,5 bensin, 4,8 metanol), tapi dalam lambda semuanya berkumpul di **0,74–0,89**.

Artinya kalau kamu pindah bahan bakar, target lambda-mu hampir tidak berubah — sementara target AFR berubah total. Ini menghilangkan satu sumber kesalahan besar.

**Selalu setel dan catat dalam lambda kalau alatmu mendukung.**

---

## 4. Mengkalibrasi batas detonasi

### 4.1 Kenapa tabel oktan tidak cukup

Tabel umum menghubungkan DCR dengan oktan minimum:

| DCR | Bahan bakar menurut tabel umum |
|---|---|
| < 9,0 | 92–95 RON |
| 9,0–10,0 | 98 RON |
| 10,0–11,0 | 100+ RON |
| 11,0–12,5 | bensin balap 102+ |
| > 12,5 | metanol |

Tabel ini **terlalu konservatif** untuk bahan bakar balap sungguhan.

### 4.2 Data yang membantahnya

Mesin Contoh A: [UKUR]

| | |
|---|---|
| CR statis | 16:1 |
| IVC | 63° ABDC |
| Bahan bakar | bensol / avgas 100LL |
| **DCR terhitung** | **12,83** |
| Status | terbukti bertahun-tahun, tanpa masalah |

Tabel bilang 12,83 harus metanol. Mesin itu jalan dengan bensol.

Angka ini kokoh: sensitivitas terhadap asumsi panjang rod sangat kecil (DCR 12,77–12,90 untuk rod 98–112 mm).

### 4.3 Cara memakainya

Setelah punya DCR terbukti untuk bahan bakarmu:

```
CR_statis_baru = 1 + (DCR_terbukti − 1) × Vd / V_sapu_saat_IVC
```

**Contoh:** Mesin Contoh B dengan IVC 52,8° ABDC. Untuk mencapai DCR 12,83 dibutuhkan CR statis **14,9:1**.

Rencana 14:1 memberi DCR **12,07** — margin **+0,76 di bawah** batas terbukti. Rencana itu **konservatif**, bukan agresif.

### 4.4 Faktor yang menggeser batas

Batas DCR bukan angka tunggal untuk satu bahan bakar.

**Menaikkan toleransi:**

| Faktor | Sebabnya |
|---|---|
| Bore lebih kecil | jalur api lebih pendek |
| Spark plug di tengah (4 valve) | jalur api merata |
| RPM lebih tinggi | waktu untuk detonasi berkembang lebih pendek |
| Pendingin cair | suhu dinding lebih stabil |
| Campuran lebih kaya | pendinginan muatan |
| Squish yang baik | turbulensi mempercepat pembakaran |
| Suhu udara masuk rendah | muatan lebih dingin |

**Menurunkan toleransi:**

| Faktor | Sebabnya |
|---|---|
| Bore besar | jalur api panjang |
| Ruang bakar asimetris (2/3 valve) | spark plug menepi |
| Dome piston tinggi | jalur api panjang, titik panas |
| Suhu udara masuk tinggi | muatan panas |
| Beban berkelanjutan | akumulasi panas |
| Deposit karbon | titik panas dan menaikkan CR efektif |

**Penerapan:** head 3 valve punya spark plug menepi dan ruang bakar asimetris, jadi disarankan **1 angka DCR lebih rendah** daripada 4 valve pada bahan bakar yang sama.

---

## 5. Knocking (detonasi)

### 5.1 Apa yang terjadi

Pembakaran normal: api menyebar dari spark plug secara teratur ke seluruh ruang bakar.

Detonasi: sebagian muatan di ujung ruang bakar (*end gas*) menyala **sendiri** karena tekanan dan suhu, sebelum api dari spark plug sampai. Dua front api bertabrakan, menghasilkan gelombang kejut.

### 5.2 Kerusakan yang ditimbulkan

Berurutan dari ringan ke berat:

1. **Suara ketukan** — ini sudah tahap lanjut, bukan awal
2. **Erosi tepi piston** — permukaan seperti dimakan pasir
3. **Ring patah** atau macet di alurnya
4. **Lubang di mahkota piston**
5. **Gasket head jebol**
6. **Rod bengkok atau patah**

**Detonasi ringan bisa berlangsung lama tanpa suara yang terdengar** — terutama di mesin matic yang berisik dan berputaran tinggi. Saat terdengar, kerusakan biasanya sudah terjadi.

### 5.3 Penyebab, urut dari yang paling umum

| Penyebab | Cara mengatasi |
|---|---|
| Pengapian terlalu maju | mundurkan |
| Campuran terlalu miskin | perkaya |
| DCR terlalu tinggi untuk bahan bakarnya | turunkan kompresi atau ganti bahan bakar |
| Suhu udara masuk tinggi | isolasi manifold, perbaiki aliran udara |
| Pendinginan buruk | perbaiki radiator/sirip, cek aliran |
| Deposit karbon | bersihkan ruang bakar |
| Spark plug terlalu panas | ganti heat range lebih dingin |
| Bahan bakar oktan turun | ganti batch, cek penyimpanan |

### 5.4 Cara mendeteksi

**Membaca spark plug** — cara paling murah dan cukup andal:

| Tanda | Artinya |
|---|---|
| Titik-titik hitam kecil di insulator | detonasi ringan sudah terjadi |
| Insulator putih bersih dan mengkilap | terlalu miskin atau terlalu panas |
| Elektroda ground terkikis | detonasi |
| Warna coklat muda merata | **normal** |
| Basah hitam | terlalu kaya |

**Membaca piston** — setelah bongkar:

| Tanda | Artinya |
|---|---|
| Tepi mahkota seperti dimakan pasir | detonasi |
| Permukaan berlubang halus | detonasi lanjut |
| Warna merata coklat keabuan | normal |

**Knock sensor** — kalau ECU-mu mendukung. Ini deteksi paling cepat, tapi butuh kalibrasi frekuensi yang benar.

**Data logging** — EGT yang tiba-tiba turun di satu titik rpm sering menandakan detonasi.

### 5.5 Aturan praktis

> **Kalau ragu, mundurkan pengapian 2 derajat dan perkaya campuran 0,02 lambda.**
> Kehilangan 1–2% tenaga jauh lebih murah daripada piston baru.

---

## 6. Fuel dilution

### 6.1 Apa itu

Bahan bakar yang tidak terbakar mengalir turun di dinding cylinder, melewati ring, dan mencampur dengan oli di bak.

### 6.2 Akibatnya

| Akibat | Penjelasan |
|---|---|
| Viskositas oli turun | lapisan pelumas menipis |
| Keausan bearing naik | terutama big end dan main bearing |
| Tekanan oli turun | pompa memindahkan cairan lebih encer |
| Umur oli pendek | harus ganti lebih sering |

Pengenceran 5% saja bisa menurunkan viskositas oli satu tingkat penuh — dari 10W-40 jadi seperti 10W-30.

### 6.3 Penyebab

| Penyebab | Kapan terjadi |
|---|---|
| Campuran terlalu kaya | mapping salah, injektor bocor |
| Start dingin berulang | bahan bakar tidak menguap sempurna |
| Ring belum duduk | mesin baru, gap terlalu besar |
| Metanol | **jauh lebih parah** — konsumsi 2,45× dan tidak mudah menguap dari oli |
| Pengapian lemah | pembakaran tidak sempurna |

### 6.4 Untuk mesin metanol

Fuel dilution adalah **masalah utama** pada metanol, bukan masalah sampingan.

- Ganti oli jauh lebih sering — banyak yang mengganti setiap beberapa run
- Periksa bau dan warna oli setelah tiap sesi
- Metanol yang bercampur oli juga membawa air, yang mengkorosi bearing

---

## 7. Ringkasan Tahap 5

1. **DCR menentukan detonasi, bukan CR.** DCR murni geometri + timing, tidak bergantung rpm.
2. **Kantong valve ikut menambah volume ruang bakar** — 14–20% anggaran. Hitung cam dulu.
3. **Ukur Vc dengan buret**, jangan pakai angka spesifikasi. Selisihnya bisa 1–2 cc.
4. **Oktan tinggi tidak menambah tenaga** — ia memberi izin menaikkan kompresi dan memajukan pengapian.
5. **Bensin, avgas, dan race gas non-oksigenat praktis sama** potensi tenaganya (98–100%).
6. **Metanol +19% energi per kg udara** plus pendinginan 228 K, dengan ongkos konsumsi 2,45×.
7. **Pakai lambda, bukan AFR** — target lambda hampir sama untuk semua bahan bakar (0,74–0,89).
8. **Kalibrasi batas DCR ke mesinmu sendiri.** Tabel oktan umum terlalu konservatif.
9. **Detonasi ringan bisa berlangsung lama tanpa terdengar.** Baca spark plug dan piston.
10. **Kalau ragu: mundurkan 2°, perkaya 0,02 lambda.**

**Berikutnya:** Tahap 6 — pengapian dan campuran, bagian paling murah untuk menambah tenaga dan paling cepat merusak mesin.

---

# TAHAP 6 — PENGAPIAN DAN CAMPURAN

*Bagian paling murah untuk menambah tenaga, dan paling cepat merusak mesin kalau salah.*

---

## 1. Stoikiometri dan AFR

### 1.1 Definisi

**AFR** (*Air-Fuel Ratio*) adalah perbandingan massa udara terhadap massa bahan bakar.

**Stoikiometri** adalah AFR di mana semua bahan bakar dan semua oksigen habis bereaksi — tidak ada sisa.

| Bahan bakar | AFR stoikiometri |
|---|---|
| Bensin | 14,70 |
| Avgas 100LL | 14,90 |
| Race gas beroksigen | ~12,90 |
| Metanol | 6,45 |
| Nitrometana | 1,70 |

### 1.2 Lambda — dan kenapa lebih berguna

```
λ = AFR / AFR_stoikiometri
```

| λ | Artinya |
|---|---|
| 1,00 | stoikiometri |
| < 1,00 | kaya |
| > 1,00 | miskin |

**Kenapa lambda lebih berguna daripada AFR:**

Angka AFR tenaga puncak berbeda-beda tiap bahan bakar — 12,5 untuk bensin, 4,8 untuk metanol. Tapi dalam lambda, semuanya berkumpul di **0,74–0,89**.

Artinya kalau kamu pindah bahan bakar, **target lambda-mu hampir tidak berubah** sementara target AFR berubah total.

> **Selalu setel dan catat dalam lambda kalau alatmu mendukung.** Ini menghilangkan satu sumber kesalahan besar.

**Kesalahan yang sering terjadi:** memakai race gas beroksigen dengan mapping AFR bensin biasa. Karena stoikiometrinya 12,9 bukan 14,7, campuran yang dikira "12,5 kaya" sebenarnya **λ 0,97 — hampir stoikiometri**, jauh terlalu miskin untuk beban penuh.

---

## 2. AFR untuk torsi dan tenaga

### 2.1 Kurva torsi terhadap lambda

Torsi mencapai puncak pada campuran yang **sedikit kaya**, bukan stoikiometri.

| λ | Torsi relatif | Keterangan |
|---|---|---|
| 1,10 | ~96% | miskin, hemat, panas |
| 1,00 | ~98% | stoikiometri |
| **0,87** | **100%** | **puncak torsi** |
| 0,80 | ~99% | kaya, lebih dingin |
| 0,70 | ~95% | terlalu kaya, boros |

Kurvanya **datar di sekitar puncak** — antara λ 0,80 dan 0,90 selisih torsinya cuma 1%.

### 2.2 Kenapa puncaknya di sisi kaya

Pencampuran udara-bahan bakar di cylinder tidak pernah sempurna. Sedikit kelebihan bahan bakar memastikan setiap molekul oksigen menemukan pasangan.

Kelebihan bahan bakar juga **mendinginkan muatan** lewat penguapan, menaikkan kerapatan dan menambah margin detonasi.

### 2.3 Target praktis

| Kondisi | λ | AFR bensin |
|---|---|---|
| Idle | 0,98–1,02 | 14,4–15,0 |
| Cruise, hemat | 1,00–1,05 | 14,7–15,4 |
| Beban sedang | 0,90–0,95 | 13,2–14,0 |
| **Beban penuh, tenaga puncak** | **0,85–0,88** | **12,5–12,9** |
| **Beban penuh, margin aman** | **0,80–0,85** | **11,8–12,5** |
| Kompresi sangat tinggi / panas | 0,78–0,82 | 11,5–12,1 |

**Untuk drag dengan kompresi tinggi:** setel di **λ 0,80–0,85**. Kehilangan torsi cuma ~1% dibanding puncak, tapi margin detonasi dan pendinginan piston jauh lebih baik.

Satu persen tenaga jauh lebih murah daripada satu piston.

### 2.4 Mengukur AFR

**Wideband lambda sensor wajib.** Sensor narrowband bawaan motor hanya akurat di sekitar λ 1,00 — tidak berguna untuk beban penuh.

**Posisi pemasangan:**
- Di header, 15–30 cm dari valve buang
- Miring ke atas minimal 10° supaya kondensasi tidak menggenang di sensor
- Jangan terlalu dekat ke ujung exhaust — udara luar bisa masuk dan bikin pembacaan miskin palsu

**Peringatan avgas:** bahan bakar bertimbal **memperpendek umur sensor wideband** secara drastis. Sensor bisa mati dalam hitungan jam pemakaian. Pakai untuk sesi tuning saja, lepas setelahnya.

---

## 3. Sudut pengapian (spark angle)

### 3.1 MBT

**MBT** = *Minimum advance for Best Torque* — sudut pengapian paling kecil yang sudah memberi torsi maksimum.

| Kondisi | Akibat |
|---|---|
| Kurang maju dari MBT | tenaga hilang, EGT naik, panas terbuang ke exhaust |
| Tepat di MBT | tenaga maksimum |
| Lebih maju dari MBT | tenaga **turun** dan risiko detonasi naik |

**Poin penting:** memajukan pengapian melewati MBT **tidak menambah tenaga**. Ia cuma menambah tekanan puncak dan risiko. Ini kesalahpahaman yang sangat umum — "makin maju makin kencang" salah.

### 3.2 Apa yang menggeser MBT

| Faktor | Efek pada MBT |
|---|---|
| RPM naik | **lebih maju** — durasi bakar tetap dalam milidetik, tapi lebih banyak derajat crank berlalu |
| Beban naik (throttle lebih besar) | **kurang maju** — muatan padat terbakar lebih cepat |
| Kompresi naik | **kurang maju** — muatan padat terbakar lebih cepat |
| Campuran lebih miskin | **lebih maju** — bakar lebih lambat |
| Campuran lebih kaya (dari stoich) | sedikit lebih maju |
| Squish bagus / turbulensi tinggi | **kurang maju** |
| Spark plug di tengah (4 valve) | **kurang maju** daripada 2 valve |
| Bore besar | lebih maju — jalur api panjang |

### 3.3 Rentang khas

Untuk mesin 1 cylinder kecil kompresi tinggi pada tenaga puncak:

| Kompresi | Sudut khas di rpm puncak |
|---|---|
| 10–11:1 | 30–36° BTDC |
| 12–13:1 | 26–32° BTDC |
| 14–15:1 | 22–28° BTDC |
| Metanol 15:1+ | 28–36° BTDC (bakar lebih lambat) |

**Perhatikan metanol:** walau kompresinya lebih tinggi, metanol butuh pengapian **lebih maju** karena kecepatan bakarnya lebih lambat daripada bensin.

### 3.4 Mencari MBT di dyno

1. Mulai dari sudut yang **konservatif** (5–8° di bawah perkiraan)
2. Naikkan **2° per run**
3. Catat torsi tiap run
4. Berhenti saat torsi **berhenti naik** — itu MBT
5. Mundurkan **2°** dari situ sebagai margin

**Kalau detonasi muncul sebelum torsi berhenti naik**, mesinmu *knock-limited*. Artinya kamu tidak bisa mencapai MBT dengan bahan bakar itu. Pilihan: bahan bakar oktan lebih tinggi, kompresi turun, atau terima tenaga yang ada.

**Jangan pernah** mencari MBT dengan menaikkan 5° sekaligus. Detonasi bisa merusak dalam hitungan detik.

### 3.5 Bentuk kurva pengapian

Kurva pengapian yang benar untuk mesin balap kecil, kira-kira:

| RPM | Sudut relatif |
|---|---|
| Idle (1.500) | 10–15° BTDC |
| 3.000 | naik cepat |
| 5.000–7.000 | mendekati puncak |
| 8.000–puncak | datar atau sedikit turun |

Setelah rpm tenaga puncak, sudut sering **diturunkan sedikit** karena efisiensi pengisian turun dan risiko detonasi berubah.

---

## 4. Sudut injeksi (injection angle)

### 4.1 Apa yang diatur

Bukan berapa banyak bahan bakar, tapi **kapan** disemprotkan dalam siklus. Biasanya yang diatur adalah **akhir injeksi** (*end of injection*, EOI).

### 4.2 Dua strategi

**Injeksi valve tertutup** (*closed-valve injection*)

Bahan bakar disemprot ke punggung valve isap yang masih tertutup. Bahan bakar punya waktu menguap sebelum valve membuka.

| Kelebihan | Kekurangan |
|---|---|
| Pencampuran lebih baik | pendinginan muatan lebih kecil |
| Bagus untuk rpm rendah-menengah | sebagian bahan bakar menempel dinding port |
| Respons throttle lebih halus | pada rpm tinggi waktunya tidak cukup |

**Injeksi valve terbuka** (*open-valve injection*)

Bahan bakar disemprot saat valve isap sedang terbuka, langsung masuk ke cylinder.

| Kelebihan | Kekurangan |
|---|---|
| **Pendinginan muatan lebih besar** | pencampuran kurang merata |
| Tidak ada bahan bakar membasahi dinding | respons rpm rendah kurang halus |
| Lebih baik di rpm tinggi | butuh atomisasi injektor yang bagus |

### 4.3 Praktisnya

Pada rpm tinggi, waktu satu siklus sangat pendek sehingga **injeksi valve tertutup menjadi mustahil** — durasi injeksi sudah memakan sebagian besar siklus.

Untuk mesin balap putaran tinggi, injeksi otomatis jatuh ke mode valve terbuka atau campuran keduanya.

**Yang bisa ditala:**
- Pada rpm rendah-menengah, geser EOI untuk mencari respons terbaik
- Pada rpm tinggi, geser EOI untuk mencari torsi terbaik — bisa memberi 1–3%

**Peringatan:** tidak semua ECU standar mengizinkan pengaturan sudut injeksi. Ini salah satu alasan pindah ke ECU aftermarket.

### 4.4 Posisi injektor

| Posisi | Karakter |
|---|---|
| Dekat valve, menyemprot ke punggung valve | standar pabrikan, pencampuran baik |
| Lebih jauh di runner | pencampuran lebih baik, pendinginan lebih merata |
| **Injektor kedua di velocity stack** | dipakai balap — injektor utama untuk rpm rendah, injektor atas untuk rpm tinggi |

Sistem dua injektor (*staged injection*) memberi pendinginan muatan maksimum di rpm tinggi tanpa mengorbankan respons rendah. Butuh ECU yang mendukung.

---

## 5. Spark plug

### 5.1 Heat range

**Heat range** menunjukkan seberapa cepat spark plug membuang panas ke cylinder head. Bukan seberapa "panas" apinya.

| Spark plug | Karakter |
|---|---|
| **Panas** (heat range rendah) | insulator panjang, panas lambat keluar, tahan kotor |
| **Dingin** (heat range tinggi) | insulator pendek, panas cepat keluar, tahan beban tinggi |

**Konvensi angka:** pada merek Jepang yang umum, **angka lebih besar = lebih dingin**. Merek lain bisa terbalik — selalu cek katalognya.

### 5.2 Memilih heat range

**Aturan praktis:** satu tingkat lebih dingin untuk tiap kenaikan besar pada kompresi atau tenaga.

| Kondisi | Arah |
|---|---|
| Kompresi naik 2+ angka | 1 tingkat lebih dingin |
| Tenaga naik 50%+ | 1 tingkat lebih dingin |
| Balap durasi panjang | 1 tingkat lebih dingin |
| Sering idle dan rpm rendah | jangan terlalu dingin |

**Gejala terlalu panas:**
- Insulator putih bersih atau melepuh
- Elektroda meleleh atau membulat
- Pre-ignition (mesin menyala sendiri sebelum spark plug memercik)

**Gejala terlalu dingin:**
- Spark plug basah dan berjelaga
- Misfire di rpm rendah
- Susah start

**Untuk drag:** condong ke **lebih dingin**. Mesin cuma jalan beberapa detik, jadi masalah fouling tidak sempat terjadi, sementara beban puncaknya ekstrem.

### 5.3 Gap

| Kondisi | Gap |
|---|---|
| Standar | 0,7–0,9 mm |
| Kompresi tinggi | 0,6–0,7 mm |
| Kompresi sangat tinggi / metanol | 0,5–0,6 mm |

**Kenapa gap dikecilkan pada kompresi tinggi:** muatan yang padat lebih sulit diionisasi. Tegangan yang dibutuhkan untuk melompati gap naik seiring tekanan. Kalau gap terlalu besar, percikan bisa gagal tepat saat paling dibutuhkan.

**Tapi jangan terlalu kecil** — gap kecil memberi kernel api kecil, yang bisa memperlambat awal pembakaran.

### 5.4 Bahan elektroda

| Bahan | Karakter |
|---|---|
| **Tembaga** | konduktivitas panas terbaik, elektroda tebal, umur pendek |
| **Platinum** | umur panjang, elektroda sedang |
| **Iridium** | elektroda sangat halus → tegangan nyala lebih rendah, umur panjang |

**Untuk balap: tembaga.** Umurnya pendek tapi pembuangan panasnya terbaik dan harganya murah — dan spark plug balap memang harus sering diganti dan dibaca.

Iridium bagus untuk harian karena umurnya panjang, tapi elektroda halusnya lebih rentan terkikis oleh detonasi.

### 5.5 Membaca spark plug

Ini keterampilan diagnostik paling murah yang kamu punya.

**Cara yang benar:**
1. Pasang spark plug baru
2. Lakukan run beban penuh sampai rpm puncak
3. **Matikan mesin dan tarik clutch di rpm tinggi** — jangan idle dulu
4. Lepas spark plug dan baca segera

Kalau mesin dibiarkan idle sebelum dimatikan, jejak beban penuh terhapus.

**Yang dibaca:**

| Bagian | Yang dilihat |
|---|---|
| Ujung insulator | warna — coklat muda = baik |
| Dasar insulator (cincin) | jejak bahan bakar — cincin gelap tipis = baik |
| Elektroda ground | warna berubah sampai seberapa jauh = indikator timing |
| Titik hitam kecil | **detonasi** |
| Butiran logam mengkilap | **detonasi berat — hentikan segera** |

---

## 6. Coil pengapian

### 6.1 Tiga jenis

**TCI — *Transistor Controlled Ignition* (induktif)**

Energi disimpan dalam medan magnet coil selama *dwell*, lalu dilepas saat arus diputus.

| | |
|---|---|
| Durasi percikan | **panjang** (1–2 ms) |
| Kecepatan naik tegangan | sedang |
| Batasan | butuh waktu dwell — di rpm sangat tinggi bisa kurang |
| Umum di | motor injeksi modern |

**CDI — *Capacitor Discharge Ignition***

Energi disimpan di kapasitor, dilepas sekaligus.

| | |
|---|---|
| Durasi percikan | **pendek** (0,1–0,3 ms) |
| Kecepatan naik tegangan | **sangat cepat** |
| Kelebihan | tidak terpengaruh spark plug kotor, tidak butuh dwell |
| Kekurangan | durasi pendek — bisa gagal menyalakan muatan yang tidak merata |
| Umum di | motor 2 langkah, motor lama |

**Smart coil (coil dengan driver terintegrasi)**

Tipe induktif dengan transistor penggerak di dalam coil, dipasang langsung di spark plug.

| | |
|---|---|
| Durasi percikan | panjang |
| Energi | **tertinggi** |
| Rugi kabel tegangan tinggi | **tidak ada** — coil menempel di spark plug |
| Kekurangan | butuh sinyal kontrol dari ECU yang sesuai |

### 6.2 Mana yang dipilih

Untuk mesin kompresi tinggi berputaran tinggi, dua hal dibutuhkan **bersamaan**:

1. **Tegangan tinggi** — karena muatan padat sulit diionisasi
2. **Durasi cukup** — karena muatan mungkin tidak tercampur sempurna

| Kondisi | Pilihan |
|---|---|
| Kompresi tinggi, rpm tinggi | **smart coil** atau TCI berenergi tinggi |
| Metanol | **smart coil** — metanol butuh energi lebih besar |
| RPM sangat tinggi (14.000+) | CDI atau smart coil (dwell jadi kendala) |
| Motor standar, tune ringan | TCI standar cukup |

**CDI sendirian sering kurang** untuk mesin 4 langkah kompresi tinggi, karena durasi percikannya terlalu pendek.

### 6.3 Yang sering diabaikan

- **Kabel massa.** Sistem pengapian butuh jalur massa yang pendek dan bersih. Massa yang buruk menyebabkan misfire yang sulit dilacak.
- **Tegangan aki.** Coil induktif sangat sensitif terhadap tegangan. Aki lemah = energi percikan turun drastis di rpm tinggi.
- **Kabel spark plug.** Kabel resistif yang tua kehilangan energi. Kalau masih pakai kabel, ganti berkala.

---

## 7. ECU

### 7.1 Batasan ECU standar

| Batasan | Akibat |
|---|---|
| **Resolusi map kasar** | titik breakpoint sedikit → interpolasi kasar di antara titik |
| **Rev limiter terkunci** | tidak bisa ke rpm sasaran |
| **Closed loop dipaksa ke stoikiometri** | di beban tertentu ECU menarik campuran ke λ 1,00 walau kamu ingin lebih kaya |
| **Rentang pengapian terbatas** | tidak bisa memundurkan atau memajukan cukup jauh |
| **Sudut injeksi tidak bisa diubah** | kehilangan 1–3% |
| **Tidak ada datalogging** | tuning jadi buta |
| **Limiter keselamatan** | ECU menarik tenaga saat mendeteksi kondisi "aneh" |
| **Tidak mendukung injektor besar** | kalau injektor diganti, kalibrasi kacau |
| **Terkunci / terenkripsi** | tidak bisa diprogram sama sekali |

### 7.2 Tiga tingkat solusi

**Tingkat 1 — Remap ECU standar**

Mengubah isi tabel di dalam ECU asli.

| Bisa | Tidak bisa |
|---|---|
| Ubah nilai bahan bakar dan pengapian | menambah resolusi map |
| Naikkan rev limit (kadang) | menambah fitur baru |
| Matikan closed loop (kadang) | mengubah sudut injeksi |
| Murah, rapi, reversibel | mengatasi keterbatasan struktural |

**Cocok untuk:** tune ringan sampai menengah, mesin masih mendekati standar.

**Tingkat 2 — Piggyback**

Alat tambahan yang mencegat sinyal sensor dan memodifikasinya sebelum sampai ke ECU standar.

| Kelebihan | Kekurangan |
|---|---|
| Murah | ECU asli masih berjalan dengan logikanya sendiri |
| Reversibel | bisa terjadi interaksi aneh antara dua sistem |
| Tidak perlu ubah wiring | tidak bisa mengatasi limiter dan closed loop dengan bersih |
| | tuning jadi menebak-nebak: kamu mengubah sinyal, bukan hasil |

**Piggyback adalah kompromi.** Berguna kalau ECU asli terkunci dan budget terbatas, tapi jangan berharap kontrol penuh.

**Tingkat 3 — ECU aftermarket standalone**

Mengganti ECU asli sepenuhnya.

| Kemampuan yang didapat |
|---|
| Kontrol penuh map bahan bakar dan pengapian |
| Resolusi map jauh lebih tinggi |
| Rev limit bebas |
| **Sudut injeksi bisa diatur** |
| Closed loop dengan wideband, target lambda bebas |
| Datalogging lengkap |
| Launch control, shift light, dua map |
| Dukungan injektor besar dan dua injektor |
| Knock control (sebagian) |
| Kontrol coil yang lebih baik |

| Ongkosnya |
|---|
| Harga jauh lebih mahal |
| Butuh wiring ulang |
| **Butuh tuner yang paham** — ECU canggih di tangan yang salah lebih berbahaya daripada ECU standar |
| Fitur motor lain (imobilizer, panel) bisa hilang |

### 7.3 Kapan naik tingkat

| Kondisi mesin | Cukup dengan |
|---|---|
| Exhaust + filter, cam standar | remap standar |
| Cam ringan, kompresi naik sedikit | remap atau piggyback |
| Cam balap, kompresi tinggi, rpm naik | **standalone** |
| Metanol atau race gas beroksigen | **standalone** |
| Dua injektor | **standalone** |

**Aturan praktisnya:** kalau rpm sasaranmu melewati rev limit standar, atau kamu ganti bahan bakar yang stoikiometrinya berbeda, ECU standar sudah tidak cukup.

### 7.4 Yang tidak berubah walau ECU-nya canggih

ECU tidak menambah udara. Ia cuma mengatur bahan bakar dan pengapian untuk udara yang sudah masuk.

> **ECU mahal di mesin yang head-nya belum benar tidak akan memberi tenaga.** Urutan tetap: head → cam → kompresi → baru ECU.

---

## 8. Urutan tuning di dyno

Kalau semua sudah terpasang, urutan penyetelan yang benar:

**1. Pastikan mekanis sehat dulu.** Kompresi tiap cylinder, kebocoran, celah valve. Tuning mesin yang bocor cuma menyembunyikan masalah.

**2. Setel bahan bakar kasar** ke λ aman (0,82–0,85) di seluruh rentang. Jangan tuning pengapian dengan campuran yang salah.

**3. Cari MBT pengapian** di beberapa titik rpm, naik 2° per run.

**4. Haluskan bahan bakar** di sekitar rpm puncak untuk torsi maksimum.

**5. Ulangi 3 dan 4 sekali lagi** — keduanya saling mempengaruhi.

**6. Setel sudut injeksi** kalau ECU mendukung.

**7. Terakhir, mundurkan pengapian 2°** sebagai margin keselamatan.

**Satu perubahan per run.** Ini aturan yang paling sering dilanggar dan paling merugikan.

---

## 9. Ringkasan Tahap 6

1. **Pakai lambda, bukan AFR.** Target λ hampir sama untuk semua bahan bakar.
2. **Puncak torsi di λ 0,87**, tapi kurvanya datar — λ 0,80–0,85 cuma kehilangan 1% dengan margin jauh lebih baik.
3. **Wideband wajib.** Narrowband bawaan tidak berguna untuk beban penuh.
4. **Memajukan pengapian melewati MBT menurunkan tenaga**, bukan menambah.
5. **Cari MBT 2° per run.** Kalau detonasi datang duluan, mesinmu knock-limited.
6. **Metanol butuh pengapian lebih maju** walau kompresinya lebih tinggi.
7. **Spark plug: lebih dingin untuk kompresi tinggi, gap lebih kecil, tembaga untuk balap.**
8. **Baca spark plug setelah run beban penuh**, jangan setelah idle.
9. **Smart coil untuk kompresi tinggi.** CDI sendirian sering kurang durasinya.
10. **ECU standalone dibutuhkan** kalau rpm melewati limit standar atau bahan bakar berganti.
11. **ECU tidak menambah udara.** Head dulu, ECU terakhir.

**Berikutnya:** Tahap 7 — saluran masuk dan buang, tempat gelombang tekanan bekerja.

---

# TAHAP 7 — SALURAN MASUK DAN BUANG

*Memanfaatkan gelombang tekanan. Sering jadi sumber kehilangan tenaga terbesar yang tidak disadari.*

---

## 1. Throttle body

*Selanjutnya disingkat TB.*

### 1.1 Perhitungan aliran

```
Q_rata2  = Vd × (rpm/60) / 2 × VE          [4 langkah]
duty     = durasi_isap / 720
Q_puncak = Q_rata2 / duty × (π/2)
D_TB     = √(4 × Q_puncak / (π × v_target × (1 − blokade_poros)))
```

Blokade poros butterfly biasanya **6–8%** dari luas bore.

### 1.2 Kecepatan target — kalibrasi, bukan tabel

Aturan umum menyebut 105 m/s. Mesin Contoh A berjalan di **61 m/s** dan tidak bermasalah.

**Kenapa aturan umum meleset:** ditulis untuk mesin bertransmisi gear yang butuh respons part-throttle. Pada CVT yang selalu WOT, respons tidak relevan — yang dikejar restriksi minimum.

### 1.3 Kenapa mengecilkan TB TIDAK menaikkan kecepatan gas

Ini kesalahpahaman yang paling sering merugikan.

| TB | v di TB | **v di port** | Rugi TB | Flow relatif |
|---|---|---|---|---|
| 34 mm | 76 m/s | **97 m/s** | 872 Pa | −6,7% |
| 36 mm | 68 m/s | **97 m/s** | 694 Pa | −4,0% |
| 38 mm | 61 m/s | **97 m/s** | 559 Pa | −1,8% |
| 40 mm | 55 m/s | **97 m/s** | 455 Pa | 0,0% |

**Kecepatan di port tidak bergerak sama sekali.**

Kecepatan di port ditentukan oleh **luas port**. Debit sama, luas sama, kecepatan sama. Diameter TB tidak punya cara mempengaruhinya.

Yang naik cuma kecepatan **di dalam TB itu sendiri**, dan kecepatan di situ tidak melakukan pekerjaan apa pun. Udara melambat lagi di manifold sebelum sampai ke port. Energi yang dipakai mempercepatnya terbuang jadi panas.

**Perbandingan skala:** rugi port 2343 Pa vs rugi TB 559 Pa. Port mendominasi 4:1. Mengutak-atik TB itu mengurus 19% dari masalah.

### 1.4 Kalau mau menaikkan kecepatan gas, ini tuasnya

| CSA port | v di port |
|---|---|
| 560 mm² | 115 m/s |
| 615 mm² | 105 m/s |
| 665 mm² | 97 m/s |

**Kecilkan port, bukan TB.**

### 1.5 Pengecualian: karburator

Kalau memakai karburator, jawabannya **berubah**. Karburator butuh kecepatan di venturi untuk menghasilkan sinyal depresi yang menarik bahan bakar. Venturi terlalu besar = sinyal lemah = pengabutan buruk dan campuran tidak stabil.

Untuk karburator, kecepatan venturi 80–110 m/s pada rpm puncak adalah target yang wajar. Semua yang ditulis di 1.3 berlaku **hanya untuk injeksi**.

---

## 2. Panjang runner isap

### 2.1 Mekanisme

Saat valve isap membuka, gelombang tekanan negatif lari dari valve menuju ujung terbuka (mulut velocity stack). Di ujung terbuka, gelombang memantul sebagai gelombang **positif** dan kembali ke valve.

Kalau gelombang positif itu tiba saat valve masih terbuka, ia **mendorong muatan tambahan masuk** — inilah efek tuning yang bisa menaikkan VE di atas 100%.

### 2.2 Model gelombang

```
L = c × θ_durasi / (12 × n × rpm)
```
dengan `c` = kecepatan suara [m/s], `θ` = durasi isap [derajat], `n` = harmonik.

### 2.3 Kecepatan suara — jangan pakai suhu ambient

```
c = 20,05 × √(T[K])
```

Suhu **di dalam runner**, bukan ambient. Panas mesin menaikkannya 20–30 °C.

| Suhu | c |
|---|---|
| 25 °C (ambient) | 346 m/s |
| **45 °C (dalam runner)** | **357 m/s** |
| 60 °C (manifold panas) | 366 m/s |

Selisih 3% pada kecepatan suara berarti 3% pada panjang runner. Tidak besar, tapi jangan memakai suhu ambient.

### 2.4 Tabel panjang

Durasi isap 250°, c = 357 m/s: [HITUNG]

| RPM | h2 | h3 | h4 | h5 |
|---|---|---|---|---|
| 8.000 | 466 | 310 | 233 | 186 |
| 9.000 | 414 | 276 | 207 | 166 |
| 10.000 | 373 | 248 | 186 | 149 |
| 11.000 | 339 | 226 | 169 | 135 |
| 12.000 | 310 | 207 | **155** | 124 |

Batasan ruang di motor biasanya memaksa harmonik 3 atau 4.

### 2.5 Menentukan harmonik

Model gelombang **tidak bisa memberitahu harmonik mana yang dipakai mesinmu**.

**Cara mengetahuinya:** ukur panjang runner mesin yang sudah terbukti, lalu cocokkan dengan tabelnya pada rpm mesin itu. Baris yang cocok adalah harmonik yang terbukti jalan, dan mesin baru tinggal memakai baris yang sama.

Satu pengukuran mengalahkan banyak teori.

### 2.6 Panjang runner standar sebagai pembanding

Manifold standar motor matic 150 cc yang diukur: [UKUR]

| | |
|---|---|
| Port di head | Ø30,2 mm |
| Throttle body | Ø38 mm |
| **Panjang centerline port → TB** | **43 mm** |
| Sudut belok total | 34° |
| Bentuk saluran | melengkung, bukan lurus |

**Perhatikan betapa pendek runner standar itu — 43 mm.** Ini menjelaskan kenapa mesin standar puncaknya di rpm rendah, dan kenapa runner yang lebih panjang mengubah karakternya drastis.

Untuk sasaran 12.000 rpm dibutuhkan **155 mm** — hampir empat kali lipat panjang standar.

### 2.7 Model Helmholtz sebagai pemeriksaan silang

```
f_H = (c / 2π) × √(A / (V_eff × L_eff))
V_eff = V_cyl × (CR + 1) / (2 × (CR − 1))
```
Ditala saat `f_H / f_engine ≈ K`.

| K | Cocok untuk |
|---|---|
| 2,0–2,5 | mobil, manifold panjang |
| 3,5–4,5 | mesin kecil, manifold pendek |

Model ini memberi jawaban berbeda dari model gelombang. Pakai keduanya sebagai **rentang**, bukan satu angka pasti.

---

## 3. Velocity stack, plenum, dan manifold

### 3.1 Koreksi ujung

Panjang efektif kolom udara lebih panjang daripada panjang fisiknya:

```
L_efektif = L_fisik + k × jari-jari
```

| Bentuk ujung | k |
|---|---|
| Pipa polos | 0,61 |
| Bermulut lonceng (bellmouth) | 0,85 |

Untuk runner Ø28 mm dengan bellmouth: koreksi = 0,85 × 14 = **11,9 mm**. Itu 8% dari runner 155 mm — cukup berarti.

### 3.2 Radius bellmouth

```
R_bellmouth ≥ 0,15–0,20 × diameter saluran
```

| R/D | Koefisien flow |
|---|---|
| 0 (tepi tajam) | ~0,60 |
| 0,05 | ~0,80 |
| 0,10 | ~0,90 |
| **0,15–0,20** | **~0,97** |
| 0,25+ | ~0,98 — jenuh |

Di bawah 0,10 koefisien flow turun cepat. Di atas 0,25 hasilnya jenuh — menambah radius tidak menambah apa-apa.

### 3.3 Susunan pelebaran yang benar

Pertanyaan yang sering muncul: apakah port di head, manifold, TB, dan velocity stack harus sama besar lalu melebar di stack saja, atau melebar bertahap?

**Jawabannya: melebar bertahap dan mulus**, dengan urutan luas dari kecil ke besar:

```
throat (terkecil) → port head → manifold → throttle body → velocity stack (terbesar)
```

Contoh dari Mesin Contoh A, dalam **luas** bukan diameter:

| Titik | Luas | Relatif throat |
|---|---|---|
| Throat | 661 mm² | 1,00 |
| Port head | 683 mm² | 1,03 |
| Throttle body (efektif) | 1055 mm² | 1,60 |

**Kenapa harus terus melebar ke arah hulu:** aliran mempercepat terus-menerus dari mulut stack sampai throat. Percepatan yang berkelanjutan itu yang menjaga aliran menempel di dinding.

Sekali ada **pelebaran di tengah jalan**, aliran melambat, lapisan batas menebal, dan sebagian penampang jadi tidak terpakai.

**JANGAN** membuat TB lebih kecil daripada port lalu melebar lagi di stack. Itu menciptakan penyempitan-pelebaran yang merugikan dua kali.

### 3.4 Volume plenum

```
V_plenum ≈ 1,0–1,5 × kapasitas mesin
```

Untuk mesin 1 cylinder di drag, ujung atas rentang — atau **tanpa plenum sama sekali**, dengan velocity stack terbuka ke atmosfer. Ini lazim dan efektif, selama udara yang dihisap tidak panas.

### 3.5 Sambungan yang sering merusak

Berdasarkan pengukuran, **bentuk mulut port di bidang flange berpengaruh besar** — sering lebih besar daripada rugi tikungan seluruh port.

Yang harus diperiksa:

- [ ] Manifold dan head benar-benar **sebidang** — tidak ada step
- [ ] Gasket tidak menonjol ke dalam saluran
- [ ] Tepi mulut port diberi **radius**, bukan dibiarkan tajam
- [ ] Diameter manifold sama atau sedikit lebih besar daripada port head
- [ ] Tidak ada celah di sambungan yang bisa menghisap udara palsu

**Ini perbaikan paling murah yang paling sering diabaikan.** Sambungan yang meleset 1 mm bisa memakan lebih banyak flow daripada short-turn radius yang digerus berjam-jam.

---

## 4. Sistem buang

### 4.1 CSA port buang

Port buang jauh lebih besar relatif terhadap throat-nya dibanding port isap, karena gas buang panas volumenya berlipat.

Dua jangkar, sama seperti sisi isap:

```
CSA_ex = rasio_port_throat_acuan × A_throat_ex
CSA_ex = luas_piston × MPS / MGV_ex_target
```

Data acuan dari Mesin Contoh A: [UKUR]

| | |
|---|---|
| Throat buang | 23,8 mm (443 mm²) |
| Port buang | 29 mm (660 mm²) |
| **Rasio port/throat** | **1,49** |
| Kecepatan gas port buang | 101 m/s |

Perhatikan: port buang 29 mm hampir sama besar dengan port isap 29,5 mm, walau valve buangnya lebih kecil.

**Untuk Mesin Contoh B:** dua jangkar memberi **594–653 mm²**, sekitar **28 mm** diameter setara.

### 4.2 Diameter header

```
A_header ≈ 1,07 × A_port_buang
```

Dari Mesin Contoh A: header dalam 30 mm terhadap port 29 mm.

Untuk Mesin Contoh B: **29,1 mm** — praktis sama dengan 30 mm yang umum tersedia.

### 4.3 Transisi ke muffler

Mesin Contoh A: inlet muffler 50 mm terhadap header 30 mm — rasio luas **2,78×**.

**Titik transisi inilah tempat gelombang ekspansi lahir.** Posisinya menentukan panjang header efektif.

### 4.4 Panjang header

**Mekanisme:** saat valve buang membuka, gelombang tekanan positif lari menyusuri header. Di ujung terbuka (transisi ke muffler), gelombang memantul sebagai gelombang **negatif** dan kembali ke valve. Kalau tiba saat overlap, ia menarik sisa gas buang keluar dan menarik muatan segar masuk.

```
t = (180 + EVO_BBDC) / (6 × rpm)          [detik, dari EVO ke TDC]
L = c_gas × t / (2n)                       [n = harmonik]
```

**Kecepatan suara gas buang:**
```
c_gas ≈ 550–700 m/s
```
Tergantung suhu (~1100 K) dan kekayaan campuran. Panjang header berskala **langsung** dengan angka ini, jadi ketidakpastian ±8% wajar.

**Tabel** untuk Mesin Contoh B (EVO 53° BBDC, 12.000 rpm, c = 650 m/s): [HITUNG]

| Harmonik | Panjang |
|---|---|
| 1 | 1052 mm |
| 2 | **526 mm** |
| 3 | **351 mm** |
| 4 | 263 mm |

**Menentukan harmonik:** sama seperti runner isap — ukur panjang header mesin yang sudah terbukti, dari valve buang sampai titik pelebaran, lalu cocokkan.

### 4.5 Kenapa exhaust layak dicurigai

Perbandingan antara potensi head dan hasil sebenarnya pada Mesin Contoh A:

| Metode | Hasil |
|---|---|
| Dari flow head (throat 660 mm², Cf ~0,60) | ~34–39 HP |
| Dari waktu lintasan | ~28 HP |

**20–30% tertinggal di meja**, dan bukan di head.

Kalau head sudah dihitung benar tapi hasilnya jauh di bawah potensi, tersangka utamanya adalah **panjang header** dan **setelan CVT** — bukan porting lebih lanjut.

Kalau harmonik header meleset, pembilasan hilang tepat di rpm puncak, dan tidak ada porting yang bisa menggantikannya.

### 4.6 Bentuk exhaust

**Header** — pipa lurus konstan dari valve sampai titik pelebaran. Belokan tajam merugikan; kalau harus membelok, radius minimal 2,5× diameter.

**Megaphone / kerucut** — pelebaran bertahap memperkuat gelombang negatif dan melebarkan rentang rpm efektif. Sudut total 6–10°.

**Reverse cone** — penyempitan setelah megaphone menghasilkan gelombang positif pantulan yang mencegah muatan segar lolos. Berguna untuk melebarkan powerband.

**Silencer** — pada drag, hambatan silencer harus seminimal mungkin. Perhatikan bahwa silencer yang terlalu longgar bisa merusak tuning gelombang.

---

## 5. Urutan pengerjaan saluran

**1. Tentukan cam dulu.** Tanpa EVO dan durasi isap yang pasti, panjang tidak bisa dihitung.

**2. Ukur mesin acuan** — panjang runner dan panjang header yang sudah terbukti.

**3. Tentukan harmonik** dengan mencocokkan hasil ukur ke tabel.

**4. Hitung panjang untuk mesin baru** pakai harmonik yang sama.

**5. Buat dengan panjang bisa disetel** kalau mungkin — sambungan geser atau beberapa potongan.

**6. Uji ±50 mm di dyno.** Perhitungan memberi titik awal; lintasan memberi jawaban akhir.

---

## 6. Ringkasan Tahap 7

1. **Mengecilkan throttle body TIDAK menaikkan kecepatan gas di port.** Kalau mau kecepatan naik, kecilkan port.
2. **Rugi port mendominasi rugi TB 4:1.** TB bukan tempat mencari tenaga.
3. **Karburator adalah pengecualian** — venturi butuh kecepatan untuk sinyal.
4. **Runner standar sangat pendek** (43 mm terukur). Sasaran 12.000 rpm butuh ~155 mm.
5. **Pakai suhu dalam runner** untuk kecepatan suara, bukan ambient.
6. **Harmonik tidak bisa ditentukan dari teori** — ukur mesin yang sudah terbukti.
7. **Luas saluran harus melebar terus-menerus** dari throat ke mulut stack. Jangan ada pelebaran di tengah.
8. **Radius bellmouth 0,15–0,20 × diameter**, di atas itu jenuh.
9. **Sambungan manifold yang tidak sebidang** bisa memakan lebih banyak flow daripada porting berjam-jam.
10. **Port buang 1,49× throat-nya** — jauh lebih besar daripada sisi isap.
11. **Panjang header adalah tersangka utama** kalau hasil jauh di bawah potensi head.

**Berikutnya:** Tahap 8 — mekanik dan material, supaya yang sudah dibangun tidak jebol.

---

# TAHAP 8 — MEKANIK, MATERIAL, DAN KEANDALAN

*Supaya yang sudah dibangun tidak jebol.*

---

## 1. Batas mekanis

### 1.1 Kecepatan piston

```
MPS = 2 × stroke[m] × rpm / 60
```

| MPS | Keterangan |
|---|---|
| < 20 m/s | aman, bisa harian |
| 20–22 | tinggi, umur pendek tapi wajar untuk drag |
| 22–24 | sangat tinggi, butuh part serius |
| 24–26 | ekstrem |
| 30+ | drag profesional, mesin sekali pakai |

### 1.2 Percepatan piston

```
a_TDC = ω² × r × (1 + r/L)
ω = 2π × rpm / 60,   r = stroke/2,   L = panjang rod
```

Percepatan di TDC selalu lebih besar daripada di BDC — faktor `(1 + r/L)` menjadi `(1 − r/L)` di BDC.

**Mesin Contoh B** (stroke 58, rod 95): [HITUNG]

| RPM | g di TDC |
|---|---|
| 11.000 | 5.121 |
| 12.000 | 6.093 |
| 12.500 | 6.612 |
| 13.000 | 7.151 |

### 1.3 Gaya inersia

```
F = massa_bolak_balik × a_TDC
```

Massa bolak-balik = piston + ring + pin + clip + ujung kecil rod.

Pada 12.000 rpm:

| Massa | Gaya di TDC |
|---|---|
| 80 g | 487 kgf |
| 100 g | 609 kgf |
| 120 g | 731 kgf |

Ini beban yang ditahan pin, rod, dan bearing **pada langkah buang** — saat tidak ada tekanan gas yang melawan.

### 1.4 Massa piston adalah tuas paling murah

Turun dari 120 ke 80 gram memangkas beban rod **33%** — setara menurunkan rpm dari 13.000 ke 11.000, **tanpa kehilangan tenaga sedikit pun**.

Kalau mengincar 12.500+ rpm, piston ringan bukan opsi tapi keharusan.

### 1.5 Membandingkan ke mesin yang sudah terbukti

Ini cara paling berguna memakai angka di atas:

| Mesin | RPM | g di TDC |
|---|---|---|
| Contoh A (stroke 64, rod 95) | 11.250 | 6.052 |
| **Contoh B (stroke 58, rod 95)** | **12.000** | **6.093** |

Selisih 0,7%. Artinya 12.000 rpm di Mesin B berada **di dalam amplop yang sudah terbukti**, bukan wilayah baru.

**Selalu bandingkan begini** sebelum memutuskan rpm sasaran. Angka mutlak sulit ditafsirkan; perbandingan ke mesin yang sudah jalan jauh lebih berarti.

---

## 2. Material piston

### 2.1 Jenis

| Jenis | Pemuaian | Kekuatan | Clearance | Cocok untuk |
|---|---|---|---|---|
| **Cor (cast)** | rendah | rendah | 0,0015–0,002 mm/mm | standar, harian |
| **Hypereutectic** | sangat rendah | sedang | 0,0015–0,002 | harian performa |
| **Tempa 4032** (Si 12%) | sedang | tinggi | 0,002–0,0025 | jalanan/balap ringan |
| **Tempa 2618** (Si rendah) | **tinggi** | **tertinggi** | 0,0035–0,005 | balap penuh |

### 2.2 Pertukarannya

**4032** mengandung silikon tinggi → pemuaian rendah → clearance kecil → mesin **lebih senyap saat dingin**, oli lebih sedikit lolos. Kekuatannya cukup untuk sebagian besar aplikasi.

**2618** silikon rendah → lebih ulet, lebih tahan detonasi dan beban kejut → tapi memuai lebih banyak → butuh clearance besar → **berisik saat dingin** dan lebih banyak blowby saat dingin.

**Untuk drag:** 2618 kalau kompresi tinggi dan rpm ekstrem. 4032 kalau mesin juga dipakai jalan.

### 2.3 Clearance piston

```
clearance = faktor × bore
```

Untuk bore 57,3 mm: [HITUNG]

| Material | Faktor | Clearance |
|---|---|---|
| Cast | 0,0015 | 0,086 mm |
| Forged 4032 | 0,002 | 0,115 mm |
| Forged 2618 | 0,004 | 0,229 mm |

**Selalu ikuti angka dari pembuat piston**, bukan tabel umum. Tiap pabrikan punya profil dan gauge point sendiri.

**Cara mengukur:**
1. Ukur bore dengan bore gauge di 3 ketinggian × 2 arah
2. Ukur piston di **gauge point yang ditentukan pabrik** — biasanya di skirt, tegak lurus pin, pada ketinggian tertentu dari bawah
3. Clearance = bore − piston pada titik itu

**Jangan mengukur piston di bagian atas** — piston sengaja dibuat tirus dan oval.

### 2.4 Coating pada piston

**Skirt — coating anti-gesek (moly/grafit)**

| Manfaat | |
|---|---|
| Gesekan turun | 1–3% tenaga |
| Melindungi saat *break-in* | mencegah scuffing |
| Memungkinkan clearance lebih kecil | mesin lebih senyap |
| Menahan oli di permukaan | pelumasan lebih baik |

**Mahkota — thermal barrier (berbasis keramik)**

| Manfaat | |
|---|---|
| Panas dipantulkan kembali ke ruang bakar | efisiensi naik sedikit |
| Suhu piston turun 10–20% | **margin detonasi naik** |
| Melindungi dari detonasi ringan | |

| Risiko | |
|---|---|
| Kalau mengelupas, serpihannya merusak | pastikan aplikator berkualitas |
| Suhu ruang bakar naik | bisa **memperburuk** detonasi kalau tidak diimbangi |

**Bagian bawah piston — oil-shedding coating**

Membuat oli cepat mengalir turun, meningkatkan perpindahan panas dari piston ke oli. Berguna kalau ada oil jet.

---

## 3. Material rod

| Material | Densitas | Kekuatan | Catatan |
|---|---|---|---|
| Baja tempa standar | 7,85 | baik | bawaan pabrik |
| **Baja 4340 tempa** | 7,85 | sangat baik | standar balap |
| **Titanium** | 4,43 | sangat baik | 40% lebih ringan, mahal, butuh perawatan khusus |
| **Aluminium** | 2,70 | sedang | **hanya drag** — umur lelah sangat pendek |

### 3.1 Rod aluminium

Dipakai di drag karena sangat ringan dan **menyerap kejut** — melindungi bearing dari beban detonasi.

**Tapi:**
- Umur lelah dihitung dalam puluhan run, bukan ribuan
- **Memanjang jauh lebih banyak saat panas** — lihat bagian 6
- Harus diganti terjadwal, bukan menunggu rusak

### 3.2 Pengaruh massa rod

Ujung kecil rod ikut dalam massa bolak-balik; ujung besar ikut dalam massa berputar. Rod yang lebih ringan mengurangi keduanya.

Tapi pengaruhnya lebih kecil daripada massa piston, karena hanya sebagian rod yang bolak-balik (kira-kira sepertiganya).

---

## 4. Material valve

| Material | Densitas | Karakter |
|---|---|---|
| **Stainless (21-4N, EV8)** | 7,8 | umum, tahan panas cukup, murah |
| **Inconel / Nimonic** | 8,2 | tahan panas tinggi — untuk valve buang beban berat |
| **Titanium** | 4,5 | **40% lebih ringan**, mahal, ujung batang harus dikeraskan |

### 4.1 Kenapa massa valve sangat penting

Percepatan valve di puncak lobe untuk Mesin Contoh B (lift 9 mm, durasi 261°, 12.000 rpm): [HITUNG]

```
percepatan = 13.519 m/s² = 1.378 g
```

Gaya yang harus ditahan spring per valve:

| Rakitan valve | Massa | Gaya | Spring dibutuhkan |
|---|---|---|---|
| Stainless + retainer baja | 38 g | 514 N | **73 kgf** |
| Stainless + retainer titanium | 32 g | 433 N | **62 kgf** |
| **Titanium + retainer titanium** | **22 g** | **297 N** | **42 kgf** |

**RPM floating dengan spring 65 kgf:**

| Rakitan | Floating di |
|---|---|
| Stainless 38 g | ~13.400 rpm |
| **Titanium 22 g** | **~17.600 rpm** |

Mengganti valve ke titanium menaikkan batas floating **4.200 rpm** dengan spring yang sama.

### 4.2 Perhatian valve titanium

- **Ujung batang harus dikeraskan** (biasanya dilapis chrome atau DLC) — titanium lunak dan cepat aus di kontak rocker
- **Seat harus cocok** — titanium tidak boleh langsung ke seat besi cor keras tanpa lapisan
- **Jangan dipakai untuk buang** kecuali dilapis thermal barrier — titanium tidak tahan panas gas buang sebaik Inconel

### 4.3 Coating pada valve

| Bagian | Coating | Manfaat |
|---|---|---|
| Batang | DLC atau chrome | gesekan turun, aus berkurang |
| Muka valve buang | thermal barrier | suhu valve turun, umur naik |
| Payung valve, sisi ruang bakar | thermal barrier | mengurangi transfer panas ke valve |

Coating thermal barrier pada valve buang adalah salah satu perbaikan keandalan paling efektif untuk mesin kompresi tinggi.

---

## 5. Ring piston

### 5.1 Single ring versus double ring

Yang dimaksud adalah jumlah **ring kompresi** (ring oli tetap ada).

| | Single (1 kompresi) | Double (2 kompresi) |
|---|---|---|
| Gesekan | **lebih rendah** — 3–5% total gesekan mesin | lebih tinggi |
| Massa bolak-balik | lebih rendah | lebih tinggi |
| Blowby | lebih tinggi | **lebih rendah** |
| Penyegelan saat beban lama | kurang | **lebih baik** |
| Umur | lebih pendek | lebih panjang |
| Cocok untuk | **drag, sprint pendek** | endurance, harian |

**Untuk drag 500 m** yang cuma 15 detik, single ring masuk akal — blowby yang lebih tinggi tidak sempat jadi masalah, dan gesekan yang lebih rendah langsung jadi tenaga.

**Untuk mesin yang juga dipakai jalan**, double ring lebih tepat.

### 5.2 Ring end gap

```
gap = faktor × bore
```

| Aplikasi | Faktor ring atas | Faktor ring kedua |
|---|---|---|
| Harian NA | 0,0035–0,0045 | 0,0045–0,0055 |
| **Balap NA** | **0,0045–0,0055** | **0,0050–0,0060** |
| Nitrous / turbo | 0,0060–0,0070 | 0,0065–0,0075 |

Untuk bore 57,3 mm, balap NA: [HITUNG]

| Ring | Gap |
|---|---|
| Atas | 0,26–0,32 mm |
| Kedua | 0,29–0,34 mm |

**Ring kedua selalu diberi gap lebih besar daripada ring atas.** Kalau lebih kecil, tekanan terperangkap di antara kedua ring dan bisa mengangkat ring atas dari alurnya — *ring flutter*.

**Gap terlalu kecil:** ring memuai saat panas, kedua ujungnya bertemu (*butting*), ring menekan dinding liner → gores dalam, piston rusak.

**Gap terlalu besar:** blowby, kompresi turun, oli terkontaminasi.

### 5.3 Cara mengukur gap

1. Masukkan ring ke dalam bore **tanpa piston**
2. Dorong lurus dengan piston terbalik supaya ring tegak lurus (*square*)
3. Ukur di kedalaman tempat ring akan bekerja — biasanya 20–30 mm dari atas
4. Ukur dengan feeler gauge
5. Kalau kurang, kikir **satu sisi saja** dengan alat kikir ring, sedikit demi sedikit, lalu ukur ulang

Ujung yang dikikir harus tetap **tegak lurus dan tanpa gerigi** — ujung yang miring atau berduri akan menggores liner.

### 5.4 Cara memasang ring

Ini bagian yang sering dilakukan sembarangan dan berakibat fatal.

**Urutan pemasangan:**

1. **Ring oli dulu** — expander (spring) lebih dulu, lalu rail atas dan bawah
2. **Ring kedua** — perhatikan tanda "TOP" atau titik, harus menghadap atas
3. **Ring atas** — perhatikan tanda "TOP"

**Aturan wajib pada ring oli expander:**

> **Kedua ujung expander harus BERTEMU, tidak boleh saling tumpang tindih.**

Kalau tumpang tindih, expander menekan terlalu kuat, ring oli tidak bisa mengikuti dinding, dan konsumsi oli melonjak. Ini kesalahan yang sering terjadi dan sulit didiagnosis setelah mesin dirakit.

**Periksa dengan jari** sebelum memasang rail.

**Alat pemasang ring wajib dipakai.** Memasang ring dengan tangan atau obeng akan memuntir ring — ring yang terpuntir tidak akan menyegel walau terlihat baik.

### 5.5 Posisi gap ring (staggering)

Gap ring harus **disebar**, tidak boleh sejajar — kalau sejajar, gas punya jalur lurus ke bawah.

**Aturan:**

| Jangan tempatkan gap | Alasan |
|---|---|
| Di atas pin piston | area lemah, ada celah |
| Di sisi thrust | area beban tertinggi |
| Sejajar dengan gap ring lain | jalur bocor lurus |

**Susunan yang lazim** (dilihat dari atas, pin di posisi 3 dan 9):

| Ring | Posisi |
|---|---|
| Ring atas | 0° (jam 12) |
| Ring kedua | 180° (jam 6) |
| Rail oli atas | 90° dari ring atas |
| Rail oli bawah | 90° dari ring atas, sisi berlawanan |
| Expander | 45° dari rail |

**Catatan jujur:** ring akan berputar sendiri saat mesin berjalan. Posisi awal tetap penting untuk **start pertama dan break-in**, tapi jangan berharap posisinya bertahan selamanya.

---

## 6. Pemuaian termal

### 6.1 Koefisien

| Material | α (per K) |
|---|---|
| Aluminium | 23 × 10⁻⁶ |
| Baja | 12 × 10⁻⁶ |
| Titanium | 8,6 × 10⁻⁶ |
| Besi cor | 11 × 10⁻⁶ |

### 6.2 Pemuaian rod

Rod memanjang saat panas, dan itu **mengurangi kelegaan valve-piston**.

Rod 95 mm dengan kenaikan suhu 100 K: [HITUNG]

| Material rod | Pemanjangan |
|---|---|
| Baja | 0,114 mm |
| **Aluminium** | **0,219 mm** |

**Rod aluminium memanjang hampir dua kali lipat.** Ini alasan mesin ber-rod aluminium butuh kelegaan valve lebih besar — tambahkan minimal 0,25 mm dari perhitungan dingin.

Kalau kelegaan dihitung saat dingin tanpa memperhitungkan ini, valve bisa menyentuh piston saat mesin panas.

### 6.3 Pemuaian piston

Piston aluminium bore 57,3 mm dengan kenaikan 150 K:

```
Δd = 57,3 × 23e-6 × 150 = 0,198 mm
```

Liner besi cor memuai:
```
Δd = 57,3 × 11e-6 × 150 = 0,095 mm
```

Selisihnya **0,103 mm** — piston memuai lebih cepat daripada liner. Itulah sebabnya clearance dingin harus cukup besar; kalau tidak, piston macet saat panas.

Piston 2618 memuai lebih banyak lagi — itulah alasan clearance-nya jauh lebih besar.

### 6.4 Yang harus diperiksa

- [ ] Kelegaan valve-piston dicek **saat dingin** dengan margin untuk pemuaian
- [ ] Clearance piston sesuai material dan sesuai anjuran pabrik
- [ ] Ring gap diukur di bore yang sudah pada suhu ruang, bukan bore panas
- [ ] Kalau pakai rod aluminium, **tambah margin kelegaan valve 0,25 mm**

---

## 7. Valve spring

### 7.1 Fungsinya

Dua hal:
1. **Menutup valve** dan menjaganya tetap rapat di seat
2. **Menjaga follower tetap menempel pada cam** sepanjang siklus

Fungsi kedua yang menentukan batas rpm.

### 7.2 Floating

Kalau spring tidak mampu melawan inersia valve, follower **terlepas dari lobe cam**. Valve tidak lagi mengikuti profil, memantul saat menutup, dan bisa menyentuh piston.

**Gejala:**
- Tenaga hilang mendadak di atas rpm tertentu
- Suara valvetrain berubah
- Kurva dyno turun tajam, bukan melandai

**Akibat kalau dibiarkan:** valve patah, piston bolong, atau rocker hancur.

### 7.3 Menghitung kebutuhan

Percepatan valve di puncak lobe (profil harmonik):

```
a = (lift/2) × (2π/Φ_cam)² × ω_cam²
```
dengan `Φ_cam` = durasi dalam radian **cam** (setengah durasi crank), `ω_cam` = kecepatan sudut cam.

Gaya yang dibutuhkan:
```
F_perlu = massa_rakitan × a × faktor_aman
```

Faktor aman **1,3–1,5**.

**Massa rakitan** = valve + retainer + kuku + sekitar sepertiga massa spring.

### 7.4 Contoh dan pengaruh variabel

Mesin Contoh B, lift 9 mm, durasi 261°, 12.000 rpm → percepatan **1.378 g**: [HITUNG]

| Rakitan valve | Massa | Spring dibutuhkan |
|---|---|---|
| Stainless + retainer baja | 38 g | 73 kgf |
| Stainless + retainer titanium | 32 g | 62 kgf |
| Titanium + retainer titanium | 22 g | 42 kgf |

**Pengaruh lift** (valve 38 g, durasi 261°):

| Lift | Percepatan | Spring dibutuhkan |
|---|---|---|
| 8,0 mm | 1.225 g | 65 kgf |
| 9,0 mm | 1.378 g | 73 kgf |
| 10,0 mm | 1.531 g | 81 kgf |
| 11,0 mm | 1.684 g | 90 kgf |

**Pengaruh durasi** (valve 38 g, lift 9 mm):

| Durasi | Percepatan | Spring dibutuhkan |
|---|---|---|
| 240° | 1.630 g | 87 kgf |
| 261° | 1.378 g | 73 kgf |
| 290° | 1.116 g | 59 kgf |

**Perhatikan:** durasi lebih pendek dengan lift sama berarti ramp lebih curam → percepatan lebih besar → spring lebih kuat. Ini pertukaran yang sering dilupakan saat memilih cam.

### 7.5 Mengukur valve spring

Butuh **spring tester** — alat yang mengukur gaya pada ketinggian tertentu.

**Dua angka yang harus diukur:**

| | Diukur pada | Fungsi |
|---|---|---|
| **Seat pressure** | tinggi terpasang (valve tertutup) | menjaga valve rapat di seat |
| **Open pressure** | tinggi terpasang − lift maksimum | melawan inersia di puncak lobe |

**Rentang khas mesin kecil balap:**

| | Nilai |
|---|---|
| Seat pressure | 20–35 kgf |
| Open pressure | 55–85 kgf |

### 7.6 Coil bind

**Coil bind** = spring tertekan sampai semua lilitannya saling menempel. Kalau ini terjadi saat mesin berjalan, valvetrain akan hancur seketika.

**Cara memeriksa:**
1. Tekan spring sampai semua lilitan menempel, ukur tingginya
2. Hitung tinggi spring pada lift maksimum: `tinggi_terpasang − lift`
3. Selisihnya harus **minimal 0,5–1,0 mm**

Kalau kurang, pilihannya: spring lebih pendek, retainer berbeda, atau kurangi lift.

### 7.7 Spring surge

Spring punya frekuensi alami sendiri. Kalau frekuensi itu beresonansi dengan harmonik cam, spring bergetar hebat (*surge*) dan kehilangan kemampuan mengontrol — walau gaya statisnya cukup.

**Solusinya:**

| Cara | Penjelasan |
|---|---|
| **Spring beehive / conical** | diameter berubah → frekuensi alami bervariasi → tidak ada satu frekuensi yang beresonansi |
| **Dual spring** | spring dalam dan luar dengan frekuensi berbeda saling meredam |
| **Damper** | spring datar di dalam spring utama untuk meredam |

Untuk mesin berputaran tinggi, **beehive atau dual spring hampir selalu lebih baik** daripada single spring silindris.

### 7.8 Memilih spring

Urutan yang benar:

1. **Tentukan cam dulu** — lift, durasi, dan agresivitas ramp
2. **Timbang rakitan valve** yang akan dipakai
3. **Hitung gaya yang dibutuhkan** pada rpm sasaran
4. **Pilih spring** yang open pressure-nya memenuhi, dengan margin
5. **Periksa coil bind** pada lift maksimum
6. **Periksa tinggi terpasang** — mungkin butuh shim
7. **Ukur dengan tester**, jangan percaya spesifikasi katalog

**Spring yang terlalu kuat juga merugikan:** gesekan valvetrain naik, cam dan rocker cepat aus, dan tenaga terbuang. Jangan memasang spring sekuat mungkin — pasang yang **cukup**.

---

## 8. Massa berputar dan bolak-balik

### 8.1 Pembagian

| Kategori | Komponen |
|---|---|
| **Bolak-balik** | piston, ring, pin, clip, ~1/3 rod |
| **Berputar** | crankshaft, ~2/3 rod, big end bearing |

### 8.2 Pengaruh

**Massa bolak-balik** menghasilkan gaya inersia yang harus ditahan struktur (bagian 1.3), dan menghasilkan getaran yang tidak bisa diseimbangkan sempurna pada 1 cylinder.

**Massa berputar** menyimpan energi kinetik dan mempengaruhi seberapa cepat mesin bisa naik putaran.

### 8.3 Balance factor

```
balance factor = massa penyeimbang / massa bolak-balik
```

| Faktor | Akibat |
|---|---|
| 0% | getaran vertikal maksimum |
| **50–65%** | **kompromi umum** |
| 100% | getaran vertikal hilang, getaran horizontal penuh |

Menyeimbangkan 100% cuma **memindahkan** getaran, tidak menghilangkannya.

**Penting:** kalau mengganti piston dengan yang lebih ringan, balance factor berubah — crankshaft **harus diseimbangkan ulang**. Ini sering dilupakan, dan akibatnya getaran di rpm tinggi yang merusak bearing.

---

## 9. Daftar periksa perakitan

**Sebelum merakit:**
- [ ] Bore diukur di 3 ketinggian × 2 arah
- [ ] Piston diukur di gauge point yang benar
- [ ] Clearance piston sesuai anjuran pabrik
- [ ] Ring gap diukur di bore, ring dalam posisi tegak lurus
- [ ] Ring kedua gap-nya lebih besar daripada ring atas
- [ ] Rakitan valve ditimbang
- [ ] Valve spring diukur dengan tester (seat dan open)
- [ ] Coil bind clearance ≥ 0,5 mm pada lift maksimum
- [ ] Crankshaft diseimbangkan sesuai massa piston yang dipakai

**Saat merakit:**
- [ ] Ujung expander ring oli **bertemu, tidak tumpang tindih**
- [ ] Ring dipasang dengan alat, bukan tangan
- [ ] Tanda "TOP" pada ring menghadap atas
- [ ] Gap ring disebar sesuai aturan
- [ ] Semua torsi baut sesuai spesifikasi, urutan benar

**Sebelum diputar:**
- [ ] **Cek clay kelegaan valve-piston** — margin untuk pemuaian sudah dihitung
- [ ] Kalau rod aluminium, margin tambahan 0,25 mm
- [ ] Mesin diputar dengan tangan dua putaran penuh, tanpa hambatan
- [ ] Tekanan oli terbaca sebelum mesin dinyalakan

---

## 10. Ringkasan Tahap 8

1. **Bandingkan beban g ke mesin yang sudah terbukti**, jangan menilai angka mutlak.
2. **Massa piston adalah tuas paling murah** — turun 40 g memangkas beban rod 33%.
3. **2618 untuk balap penuh, 4032 untuk campuran** — bedanya di pemuaian dan clearance.
4. **Coating skirt mengurangi gesekan; coating mahkota menambah margin detonasi.**
5. **Valve titanium menaikkan batas floating 4.200 rpm** dengan spring yang sama.
6. **Single ring untuk drag, double untuk endurance.**
7. **Ring kedua gap-nya harus lebih besar daripada ring atas** — kalau tidak, ring flutter.
8. **Ujung expander ring oli harus bertemu, tidak tumpang tindih.** Kesalahan ini sulit didiagnosis setelah dirakit.
9. **Rod aluminium memanjang 0,219 mm** pada ΔT 100 K — hampir dua kali baja. Tambah margin kelegaan valve.
10. **Durasi cam lebih pendek butuh spring lebih kuat** — ramp lebih curam.
11. **Spring yang terlalu kuat juga merugikan.** Pasang yang cukup, bukan yang terkuat.
12. **Kalau ganti piston ringan, seimbangkan ulang crankshaft.**

**Berikutnya:** Tahap 9 — CVT, tempat 20–30% tenaga bisa hilang tanpa disadari.

---

# TAHAP 9 — PENYALURAN TENAGA: CVT

*Tenaga yang tidak sampai ke roda tidak ada artinya. Di sini 20–30% bisa hilang tanpa disadari.*

---

## 1. Cara kerja CVT

### 1.1 Komponen

| Bagian | Fungsi |
|---|---|
| **Pulley primer (drive)** | dua permukaan kerucut, satu bisa bergerak; roller di dalamnya |
| **Roller** | pemberat yang terlempar keluar oleh gaya sentrifugal |
| **V-belt** | menyalurkan tenaga antar pulley |
| **Pulley sekunder (driven)** | dua permukaan kerucut + torque spring + torque cam |
| **Torque spring (contra spring)** | melawan pergeseran rasio |
| **Centrifugal clutch** | menghubungkan mesin ke roda pada rpm tertentu |
| **Clutch spring** | menentukan rpm sambungan |
| **Final gear** | reduksi tetap dari pulley sekunder ke roda |

### 1.2 Urutan kejadiannya

**Diam:** belt berada di posisi paling dalam pada pulley primer, paling luar pada sekunder. Rasio paling berat (reduksi terbesar).

**RPM naik:** roller terlempar keluar oleh gaya sentrifugal, mendorong permukaan pulley primer yang bisa bergerak. Belt terdorong ke posisi lebih luar pada primer.

**Belt naik di primer:** karena panjang belt tetap, belt otomatis turun ke posisi lebih dalam pada sekunder. Rasio jadi lebih ringan.

**Torque spring melawan:** menjaga tegangan belt dan menahan rasio agar tidak terlalu cepat berubah.

**Hasilnya:** rasio berubah **kontinu**, dan mesin bisa ditahan di satu putaran sepanjang akselerasi.

---

## 2. Kenapa CVT mengubah aturan tuning

### 2.1 Perbedaan dari motor gear

Pada motor gear, tiap perpindahan gear menjatuhkan putaran mesin. Kalau rentang rpm bertenaga sempit, mesin jatuh keluar powerband dan akselerasi hilang. Karena itu motor gear butuh **rentang rpm yang lebar**.

CVT tidak punya masalah itu. Rasio berubah kontinu, jadi mesin bisa ditahan **persis di satu titik**.

> **Konsekuensi: pada CVT, yang perlu dioptimalkan adalah tenaga di SATU titik putaran, bukan rentang rpm yang lebar.**

Ini memberi kebebasan yang tidak dimiliki motor gear: cam durasi panjang, overlap besar, LSA sempit, runner ditala tajam — semua yang membuat rentang rpm sempit tapi puncaknya tinggi.

### 2.2 Titik mana yang dipilih

**Putaran tenaga puncak**, bukan torsi puncak.

Percepatan berbanding lurus dengan tenaga (lihat Tahap 1). Menahan mesin di torsi puncak berarti membuang putaran yang tersedia.

### 2.3 Syaratnya

CVT harus **benar-benar mampu** menahan mesin di titik itu. CVT yang salah setelan akan membiarkan putaran jatuh, dan mesin dengan rentang rpm sempit akan terasa **jauh lebih lambat** daripada mesin standar.

Inilah kenapa banyak mesin yang bagus di dyno mengecewakan di lintasan.

---

## 3. Menyetel CVT

### 3.1 Berat roller

Ini penyetelan paling berpengaruh.

| Roller | Efek |
|---|---|
| **Lebih berat** | terlempar keluar di rpm lebih rendah → rasio berubah lebih awal → **mesin ditahan di rpm lebih rendah** |
| **Lebih ringan** | rasio berubah lebih lambat → **mesin ditahan di rpm lebih tinggi** |

**Cara menyetelnya:**

1. Pasang wideband atau tachometer yang bisa dibaca saat jalan
2. Lakukan akselerasi penuh
3. Catat rpm yang **ditahan** CVT selama akselerasi
4. Bandingkan dengan rpm tenaga puncak dari grafik dyno
5. Kalau CVT menahan terlalu rendah → **roller lebih ringan**
6. Kalau terlalu tinggi (mentok limiter) → **roller lebih berat**

**Aturan praktis:** ubah 1 gram per langkah. Perubahan 2 gram sudah terasa jelas.

### 3.2 Torque spring (contra spring)

| Spring | Efek |
|---|---|
| **Lebih keras** | melawan pergeseran rasio → mesin ditahan di rpm lebih tinggi, cengkeraman belt lebih kuat |
| **Lebih lunak** | rasio bergeser lebih mudah → rpm lebih rendah |

Torque spring bekerja **bersama** roller. Kombinasi yang umum untuk drag: roller agak ringan + torque spring agak keras.

**Efek samping spring terlalu keras:** belt tertekan sangat kuat, gesekan naik, panas naik, dan tenaga terbuang. Jangan asal keras.

### 3.3 Clutch spring

Menentukan **rpm sambungan** — di putaran berapa centrifugal clutch mulai menggigit.

| Clutch spring | Efek |
|---|---|
| Lebih keras | sambung di rpm lebih tinggi → launch lebih agresif |
| Lebih lunak | sambung lebih awal → launch lebih halus |

**Untuk drag:** rpm sambungan harus cukup tinggi supaya mesin sudah berada di daerah bertenaga saat clutch menggigit — tapi tidak terlalu tinggi sampai roda spin atau clutch terbakar.

Titik awal yang wajar: **rpm sambungan sekitar 60–70% dari rpm tenaga puncak**.

### 3.4 Urutan penyetelan

1. **Clutch spring** dulu — tentukan rpm launch
2. **Roller** — tentukan rpm yang ditahan saat akselerasi
3. **Torque spring** — haluskan, dan perbaiki kalau rpm jatuh di tengah akselerasi
4. **Ulangi** — ketiganya saling mempengaruhi

**Satu perubahan per run.** Sama seperti di dyno.

---

## 4. Rasio, kecepatan, dan gear

### 4.1 Rumus dasar

```
v [km/h] = 0,06 × π × D_roda[m] × rpm / i_total
```

dengan `i_total` = rasio CVT × rasio final gear.

### 4.2 Mengkalibrasi rasio total

**Jangan tebak dari katalog.** Hitung dari satu titik data terukur:

```
i_total = 0,06 × π × D_roda × rpm / v_terukur
```

Contoh untuk roda Ø0,56 m: [HITUNG]

| RPM | v terukur | i_total |
|---|---|---|
| 8.500 | 110 km/h | 8,16 |
| 9.000 | 120 km/h | 7,92 |
| 10.000 | 130 km/h | 8,12 |

Konsisten di sekitar **8,1** — itulah rasio total mesin itu pada CVT rasio tertinggi.

**Ukur diameter roda saat terpasang dan terbebani**, bukan diameter nominal ban. Selisihnya bisa 3–5%.

### 4.3 Tabel kecepatan

Roda Ø0,56 m: [HITUNG]

| i_total | 10.000 rpm | 11.000 | 12.000 | 13.000 |
|---|---|---|---|---|
| 6,0 | 176 | 194 | 211 | 229 |
| 6,5 | 162 | 179 | 195 | 211 |
| 7,0 | 151 | 166 | 181 | 196 |
| 7,5 | 141 | 155 | 169 | 183 |
| 8,0 | 132 | 145 | 158 | 172 |

*(km/h)*

---

## 5. Memilih gear untuk lintasan tertentu

### 5.1 Temuan yang mengejutkan

Simulasi akselerasi 500 m dengan 30 HP di roda, massa 150 kg: [HITUNG]

| i_total | v batas | Waktu | v finish | |
|---|---|---|---|---|
| 5,5 | 230 km/h | **14,23 s** | 160 km/h | |
| 6,5 | 195 | **14,23 s** | 160 | |
| 7,5 | 169 | **14,23 s** | 160 | |
| 8,5 | 149 | 14,45 s | 149 | mentok limiter |
| 9,5 | 133 | 15,26 s | 133 | mentok limiter |
| 10,5 | 121 | 16,31 s | 121 | mentok limiter |

**Selama limiter tidak tersentuh, rasio gear TIDAK mempengaruhi waktu sama sekali.**

### 5.2 Kenapa begitu

CVT menahan mesin di tenaga puncak apa pun rasionya. Percepatan cuma bergantung pada tenaga yang tersedia, bukan pada rasio.

Ini **berbeda total dari motor gear**, di mana pemilihan gear sangat menentukan.

### 5.3 Kapan gear jadi penting

Hanya dalam dua kondisi:

**1. Gear terlalu pendek** → mentok limiter sebelum garis finish. Setelah mentok, mesin tidak bisa menambah kecepatan lagi. Ini kerugian yang jelas dan besar.

**2. Gear terlalu panjang** → CVT tidak sempat mencapai rasio tertinggi dalam jarak yang tersedia, atau clutch terlalu lama slip di awal.

### 5.4 Aturan praktis

> **Pilih gear supaya kecepatan di garis finish PAS mendekati kecepatan batas.**

Dari tabel di atas, i_total sekitar **7,5–8,0** adalah pilihan yang tepat: kecepatan batas 169 km/h, kecepatan finish 160 km/h — mendekati, tapi tidak mentok.

**Margin 5–10% di bawah batas** memberi ruang kalau kondisi lintasan lebih baik daripada perkiraan.

### 5.5 Cara memverifikasi di lintasan

Pasang datalogger atau racebox, lalu periksa:

- [ ] **RPM di garis finish** — harus mendekati rpm tenaga puncak, tidak menyentuh limiter
- [ ] **RPM selama akselerasi** — harus datar di rpm tenaga puncak, tidak naik-turun
- [ ] **RPM saat launch** — harus di daerah bertenaga

Kalau rpm naik-turun selama akselerasi, CVT-nya belum benar — bukan mesinnya.

---

## 6. Di mana tenaga hilang di CVT

### 6.1 Sumber kerugian

| Sumber | Besarnya |
|---|---|
| Slip belt | 3–15% |
| Gesekan belt–pulley | 3–5% |
| Gesekan roller di jalur | 1–2% |
| Final gear | 2–3% |
| Clutch slip (kalau tidak sempurna) | 0–10% |

**Total 10–30%** — itulah selisih antara tenaga mesin dan tenaga di roda.

### 6.2 Yang paling sering merusak

**Belt aus atau salah ukuran**

Belt yang aus jadi lebih tipis, sehingga posisinya di pulley berubah — rasio tertinggi tidak tercapai. Belt yang terlalu panjang juga sama akibatnya.

**Cek:** ukur lebar belt dan bandingkan dengan spesifikasi baru. Selisih 1 mm sudah berarti.

**Permukaan pulley aus atau tergores**

Alur bekas belt di permukaan kerucut membuat belt tidak bisa bergeser mulus. Rasio jadi tersendat.

**Cek:** raba permukaan pulley. Kalau terasa beralur, ganti atau bubut.

**Roller aus tidak merata (peyang)**

Roller yang sudah gepeng di satu sisi tidak bisa berguling dengan lancar. Perubahan rasio jadi tersendat dan rpm naik-turun.

**Cek:** roller harus bulat sempurna. Kalau ada bagian rata, ganti semuanya — jangan sebagian.

**Clutch pad glazing**

Permukaan pad yang mengkilap licin menyebabkan slip berkepanjangan.

**Cek:** permukaan pad harus kasar merata. Amplas kalau mengkilap, atau ganti.

**Pulley sekunder macet**

Permukaan yang bisa bergerak harus meluncur bebas. Kalau seret karena kotoran atau karat, rasio tidak berubah dengan benar.

### 6.3 Panas

CVT menghasilkan panas besar, dan panas mengurangi cengkeraman belt.

- Pastikan jalur ventilasi CVT tidak tersumbat
- Untuk drag, kondisi dingin di run pertama biasanya paling baik
- Belt yang terlalu panas akan slip dan kehilangan tenaga secara drastis

---

## 7. Kesalahan umum

| Kesalahan | Akibat |
|---|---|
| Menyetel CVT sebelum mesin final | pekerjaan diulang |
| Roller berat supaya "torsi bawah kuat" | mesin ditahan di bawah rpm tenaga puncak — lebih lambat |
| Torque spring sekeras mungkin | gesekan besar, panas, tenaga terbuang |
| Gear dipendekkan supaya "akselerasi galak" | mentok limiter sebelum finish |
| Belt murah atau bekas | slip, tenaga hilang tanpa terlihat |
| Menilai CVT dari rasa, bukan dari data rpm | tidak akan pernah optimal |

---

## 8. Ringkasan Tahap 9

1. **CVT menahan mesin di satu rpm** — karena itu tenaga puncak lebih penting daripada rentang rpm yang lebar.
2. **Setel CVT ke rpm tenaga puncak**, bukan torsi puncak.
3. **Roller adalah penyetelan paling berpengaruh.** Lebih ringan = rpm ditahan lebih tinggi.
4. **Kalibrasi rasio total dari data terukur**, jangan dari katalog.
5. **Selama limiter tidak tersentuh, rasio gear tidak mempengaruhi akselerasi.** Ini berbeda total dari motor gear.
6. **Gear terlalu pendek jelas merugikan** — mentok limiter sebelum garis.
7. **Pilih gear supaya kecepatan finish mendekati batas**, dengan margin 5–10%.
8. **CVT bisa memakan 10–30% tenaga.** Belt, pulley, roller, dan pad harus diperiksa.
9. **RPM yang naik-turun saat akselerasi** berarti CVT belum benar, bukan mesinnya.
10. **Setel CVT terakhir**, setelah mesin final.

**Berikutnya:** Tahap 10 — simulasi dan validasi. Tahap ini opsional.

---

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

---

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

---

# LAMPIRAN

---

## A. Rumus ringkas

### A.1 Geometri

```
Kapasitas       Vd = π/4 × bore² × stroke
Ruang bakar     Vc = Vd / (CR − 1)
Luas piston     A_p = π/4 × bore²
Luas valve      A_valve = n × π/4 × D_valve²
Luas throat     A_throat = n × π/4 × D_throat²
Luas tirai      A_tirai = n × π × D_valve × lift
Lift kritis     = A_throat / (n × π × D_valve)
Lebar seat      = (D_valve − D_throat) / 2
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
K_pelebaran_mendadak   = (1 − A_kecil/A_besar)²     [Borda-Carnot — step MELEBAR; pakai v sisi kecil]
K_penyempitan_mendadak = 0,5 × (1 − A_kecil/A_besar)   [step MENYEMPIT; pakai v sisi kecil]
```

> **Gambar arah alirannya dulu.** Dua rumus step di atas terlihat mirip dan sama-sama memberi angka yang masuk akal. Untuk rasio luas yang sama, pelebaran jauh lebih mahal daripada penyempitan. Salah arah = salah beberapa kali lipat, tanpa peringatan apapun. Lihat Tahap 11 §7.4.

**Aliran puncak vs rata-rata:** `Q_puncak` berlaku di saluran yang tersambung langsung ke klep. Di **hulu plenum**, pulsa sudah diredam — pakai aliran mendekati rata-rata (≈1–2× `Q_rata2`). Titik pemisahnya adalah plenum itu sendiri. Lihat Tahap 11 §10.6.

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

luas overlap/cc = n_valve × π × D_valve × lift_TDC / kapasitas
```

### A.6 Valvetrain

```
Percepatan nose a = (lift/2) × (2π/Φ_cam)² × ω_cam²
                    Φ_cam dalam radian cam = durasi_crank/2
                    ω_cam = 2π × (rpm/2) / 60
Gaya inersia    F = massa_rakitan × a
Spring dibutuhkan = F × faktor_aman / 9,81      [kgf], faktor 1,3–1,5
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
Helmholtz inlet f_inlet = (c/2π) × √(A_inlet / (V_plenum × L_inlet_eff))
                syarat f_inlet ≥ 3 × f_isap_maks     [Tahap 11 §10.2]
Frekuensi isap  f_isap = rpm / 120                   [1 silinder, 4 langkah]
```

### A.7b Plenum

```
Volume dari dekopling   V_plenum ≈ 5–10 × volume kolom runner
                        volume kolom runner = Σ (luas penampang × panjang) ke klep
Riak per langkah isap   = (Vd × VE) / V_plenum        [< 7% untuk ECU speed-density]
Ruang bebas bellmouth   depan  ≥ 1,0 × D saluran (ideal 1,5×)
                        radial ≥ 0,5 × D saluran
Radius bellmouth        R = 0,15–0,20 × D             [Tahap 7 §3.2]
```

> Aturan `V_plenum ≈ 1,0–1,5 × Vd` di Tahap 7 §3.4 berlaku untuk **plenum balap** yang menyuapi runner pendek. Airbox OEM berada di 8–15 × Vd karena membayar kendala lain — kebisingan, margin filter kotor, kalibrasi tunggal. Jangan campur keduanya. Lihat Tahap 11 §10.1.

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

### A.9b Uji kewarasan angka dyno

```
BMEP            = 4π × T / Vd          [4 langkah; T dalam Nm, Vd dalam m³, hasil Pa]
T dari tenaga   T = P / (rpm × 2π/60)  [P dalam Watt]
Dyno inersia    P = I × ω_roller × (dω_roller/dt)   [rpm mesin TIDAK muncul di sini]
```

**Jangkar BMEP dari mesin produksi nyata:**

| Mesin | Titik | BMEP |
|---|---|---|
| Yamaha XMAX 300 std (292cc) | peak power | 11,5 bar |
| Honda CBR250RR (249,7cc) | peak power | 10,7 bar |
| KTM 690 SMC R (693cc) | peak power | 11,9 bar |
| KTM 690 SMC R (693cc) | peak torsi | 13,3 bar |

Rentang praktis **di peak power**: OEM 10–12 bar, tertala baik 12–13, balap serius 13–14. Di atas 15 bar = bukan aspirasi alami. BMEP di peak power selalu lebih rendah daripada di peak torsi — **bandingkan di titik yang setara.**

**Kalau BMEP kelewat tinggi, hitung faktor kelebihan di ≥2 titik:**

| Pola faktor | Vonis |
|---|---|
| Konstan di semua titik | salah kalibrasi (inersia, faktor koreksi, satuan) |
| Membesar ke rpm rendah | salah rasio (dyno matic tanpa *locked ratio pulley*) |

Lihat Tahap 11 §8–§9.

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
| `port_design.py` | sizing valve, throat, port, kalibrasi | 3 |
| `exhaust_check.py` | proporsi ex/in, keputusan durasi ex | 3 |
| `cam_design.py` | DCR, durasi, overlap, kantong valve, anggaran ruang bakar | 4 |
| `cam_dari_acuan.py` | urai timing acuan, skalakan ke mesin baru | 4 |
| `kompresi_terkalibrasi.py` | batas DCR dari mesin terbukti | 5 |
| `bahan_bakar.py` | energi per kg udara, lambda, pendinginan muatan | 5 |
| `intake_tune.py` | panjang runner, Helmholtz, wave tuning | 7 |
| `tract_profile.py` | profil luas sepanjang saluran, perbandingan TB | 7 |
| `exhaust_system.py` | port buang, header, harmonik panjang | 7 |
| `valvetrain.py` | percepatan valve, gaya inersia, kebutuhan spring | 8 |
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
- [ ] Diameter valve isap dan buang
- [ ] **Diameter dalam seat (throat)** isap dan buang
- [ ] **CSA port di titik tersempit** — isap dan buang
- [ ] Timing cam lengkap **dan pada lift berapa diukur**
- [ ] Lift maksimum
- [ ] Kompresi statis **terukur dengan buret**
- [ ] Jenis bahan bakar
- [ ] Diameter throttle body
- [ ] **Panjang runner isap**
- [ ] Diameter dalam header
- [ ] **Panjang header** — dari valve sampai titik pelebaran
- [ ] RPM tenaga puncak
- [ ] Hasil terukur (dyno atau lintasan + berat)

**Yang paling sering hilang dan paling merugikan:**

| Data hilang | Akibat |
|---|---|
| Throat (bukan diameter valve) | perhitungan port meleset sampai 40% |
| Lift acuan timing cam | durasi salah baca sampai 20° |
| Panjang header | harmonik exhaust tidak bisa ditentukan |
| Vc terukur | kompresi meleset 1–2 angka penuh |

### C.2 Saat merancang

- [ ] Hitung DCR terbukti dari mesin acuan → itu batas bahan bakarmu
- [ ] Tentukan rpm sasaran dari **beban g** yang sudah terbukti, bukan dari rpm mutlak
- [ ] Hitung durasi dari time-area, bukan aturan jempol
- [ ] **Periksa silang ICL** dengan cam acuan
- [ ] Hitung CSA port dengan **dua jangkar** — kalau berbeda jauh, cari asumsi busuk
- [ ] Periksa rasio port/throat — jangan sampai port lebih kecil daripada throat
- [ ] Periksa rasio throat ex/in → tentukan apakah cam simetris
- [ ] Hitung kantong valve **sebelum** menghitung dome piston
- [ ] Hitung anggaran volume ruang bakar lengkap
- [ ] Hitung kebutuhan valve spring dari massa rakitan dan rpm sasaran
- [ ] Tentukan panjang runner dan header dari harmonik yang terbukti

### C.3 Sebelum merakit

- [ ] Bore diukur di 3 ketinggian × 2 arah
- [ ] Piston diukur di gauge point yang benar
- [ ] Clearance piston sesuai anjuran pabrik piston
- [ ] Ring gap diukur di bore, ring tegak lurus
- [ ] **Ring kedua gap-nya lebih besar daripada ring atas**
- [ ] Rakitan valve ditimbang
- [ ] Valve spring diukur dengan tester (seat dan open)
- [ ] Coil bind clearance ≥ 0,5 mm pada lift maksimum
- [ ] Crankshaft diseimbangkan sesuai massa piston yang dipakai

### C.4 Saat merakit

- [ ] **Ujung expander ring oli bertemu, tidak tumpang tindih**
- [ ] Ring dipasang dengan alat, bukan tangan
- [ ] Tanda "TOP" pada ring menghadap atas
- [ ] Gap ring disebar, tidak di atas pin, tidak di sisi thrust
- [ ] Torsi baut sesuai spesifikasi dan urutan

### C.5 Sebelum diputar

- [ ] **Cek clay kelegaan valve-piston** — wajib, tanpa pengecualian
- [ ] Kalau rod aluminium, tambah margin 0,25 mm
- [ ] Verifikasi volume ruang bakar dengan buret
- [ ] Periksa lebar seat, terutama sisi buang
- [ ] Mesin diputar tangan dua putaran penuh tanpa hambatan
- [ ] Tekanan oli terbaca sebelum dinyalakan

### C.6 Saat tuning

- [ ] Mekanis sehat dulu — kompresi, kebocoran, celah valve
- [ ] Bahan bakar kasar ke λ aman (0,82–0,85)
- [ ] Cari MBT pengapian, **2° per run**
- [ ] Haluskan bahan bakar di sekitar rpm puncak
- [ ] Ulangi pengapian dan bahan bakar sekali lagi
- [ ] Setel sudut injeksi kalau ECU mendukung
- [ ] **Mundurkan pengapian 2°** sebagai margin akhir
- [ ] **Satu perubahan per run**

### C.7 Setelah jalan

- [ ] Baca spark plug setelah run beban penuh (bukan setelah idle)
- [ ] Periksa kondisi piston setelah beberapa run
- [ ] Setel CVT ke rpm tenaga puncak
- [ ] Uji variasi panjang header ±50 mm
- [ ] Verifikasi rpm di garis finish — mendekati puncak, tidak mentok limiter
- [ ] **Kalibrasi ulang perhitungan** dengan hasil nyata

---

## D. Data mesin contoh

### D.1 Mesin Contoh A — 199cc, 2 valve, drag matic

| Parameter | Nilai | Tanda |
|---|---|---|
| Bore × stroke | 63 × 64 mm = 199,5 cc | [UKUR] |
| Valve isap / buang | 31 / 27 mm | [UKUR] |
| Throat isap | 29 mm (rasio 0,935) | [UKUR] |
| Port isap | bundar Ø29,5 mm (683 mm²) | [UKUR] |
| Port buang | Ø29 mm (660 mm²) | [UKUR] |
| Lift | 10,8 mm | [UKUR] |
| Cam | IN 38 BTDC / 63 ABDC, EX 63 BBDC / 38 ATDC | [UKUR] |
| Durasi | 281° / 281° | [HITUNG] |
| Overlap | 76° | [HITUNG] |
| ICL / LSA | 102,5° ATDC / 102,5° | [HITUNG] |
| Lift di TDC | 1,83 mm per valve (3,67 gabungan) | [HITUNG] |
| Kompresi statis | 16:1 | [UKUR] |
| **DCR** | **12,83** | [HITUNG] |
| Bahan bakar | bensol / avgas 100LL | [UKUR] |
| Throttle body | 38 mm | [UKUR] |
| Header dalam / muffler | 30 / 50 mm | [UKUR] |
| Hasil | 500 m 15,4 s, trap 158 km/h | [UKUR] |

**Besaran turunan yang dipakai sebagai jangkar kalibrasi:**

| | Nilai |
|---|---|
| Luas valve isap / bore | 0,242 |
| Throat per cc | 3,31 mm²/cc |
| Kecepatan gas port isap | 97 m/s |
| Kecepatan gas port buang | 101 m/s |
| Rasio port/throat isap | 1,035 |
| Rasio port/throat buang | 1,49 |
| Rasio throat ex/in | 0,671 |
| Kecepatan puncak di TB | 61 m/s |
| MPS @10.000 rpm | 21,3 m/s |
| Perkiraan tenaga | ~28 HP crank, ~140 HP/L |

### D.2 Mesin Contoh B — 150cc, 4 valve, rancangan

| Parameter | Nilai |
|---|---|
| Bore × stroke × rod | 57,3 × 58 × 95 mm = 149,6 cc |
| Valve isap / buang | 22 / 19 mm |
| Throat isap / buang | 20,2 / 16,7 mm |
| Luas valve isap / bore | 0,295 |
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
| Lift di TDC | 0,97 mm per valve isap |
| Kantong valve | 2,71 mm |
| CR statis | 14:1 (DCR 12,07, margin +0,76) |
| Dome piston | usir 2,45 cc |
| Throttle body | 36 mm |
| Runner isap | 155 mm |
| Header dalam | 29,1 mm |
| RPM sasaran | 12.000 (6.093 g di TDC) |
| Potensi flow | 90,7 CFM @28" |
| Potensi tenaga | ~41 HP (~274 HP/L) |

### D.3 Mesin Contoh C — 155cc, 3 valve, standar

| Parameter | Nilai |
|---|---|
| Bore × stroke | 58 × 58,6 mm = 154,8 cc |
| Valve | 3 valve (2 isap + 1 buang) |
| Pendingin | udara |
| CR standar | 10,5:1 |
| Tenaga standar | 12,7 HP @ 7.750 rpm (82 HP/L) |
| Luas valve isap / bore | 0,262 |
| Rasio throat ex/in | 0,679 |
| Lift kritis in / ex | 4,59 / 5,03 mm |
| Valve maksimum yang muat | isap 21,5 mm ×2, buang 26,7 mm ×1 |
| Potensi flow (valve maks) | 89 CFM @28" |
| Potensi tenaga | ~40 HP |
| CR disarankan | 12,5–13:1 (bukan 14, karena spark plug menepi) |

---

## E. Perbandingan mesin balap dunia

Semua dihitung dengan definisi yang sama dari spesifikasi bore/stroke/rpm publik. **Diameter valve dan CSA port tidak dipublikasikan pabrikan** — dipakai proporsi lazim di kelasnya. Ini perkiraan beralasan, bukan data pabrik.

| Mesin | MPS | Valve/bore | v throat | v port | HP/L |
|---|---|---|---|---|---|
| F1 V10 3.0L (19.000 rpm) | 25,2 | 0,296 | 105 | 95 | 317 |
| F1 V8 2.4L (18.000 rpm) | 23,9 | 0,296 | 99 | 90 | 312 |
| F1 V6 turbo 1.6L | 23,0 | 0,289 | 98 | 89 | 562* |
| MotoGP 1000 I4 (18.000 rpm) | 29,1 | 0,296 | 121 | 112 | 290 |
| Drag V8 8,2L NA 2 valve (10.500 rpm) | 32,0 | 0,297 | 133 | 106 | 165 |
| Mesin Contoh A | 21,3 | 0,242 | 109 | 105 | ~140 |
| Mesin Contoh B | 23,2 | 0,295 | 97 | 94 | ~274 |

*\*turbo — tidak sebanding dengan yang NA*

**Pengamatan pokok:** kecepatan port semua mesin jatuh di **89–112 m/s**, dan rasio valve/bore semua mesin 4 valve jatuh di **0,289–0,297**.

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
| Throat buang Mesin A | 0,88 × valve | tidak diukur langsung |
| **Panjang header Mesin A** | tidak diketahui | **paling penting untuk diukur** |
| Massa motor + rider | 150 kg | menggeser perkiraan HP ±10% |
| CdA | 0,35 | menggeser perkiraan HP |
| Tinggi pent-roof | 3,5 mm | menggeser anggaran ruang bakar |
| Tebal gasket | 0,8 mm | ukur |
| Deck clearance | 0,5 mm | ukur |
| Valve & port mesin balap dunia | proporsi lazim | **bukan data pabrik** |
| Valve Mesin Contoh C | 21 / 26 mm | **bukan data pabrik** |
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
| Throat maksimum 0,90 × valve | jalan di 0,935 | **7,4% flow hilang** |
| Kecepatan TB 105 m/s | jalan di 61 m/s | **TB 8 mm terlalu kecil** |
| DCR maksimum 12,5 untuk bensin | jalan di 12,83 dengan avgas | kompresi diturunkan tanpa perlu |
| Lift berguna maksimum 0,25 × valve | jalan di 1,6–2,5× lift kritis | cam terlalu jinak |

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

---

