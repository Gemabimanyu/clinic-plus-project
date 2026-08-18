# ADVANCED ENGINE TUNING
## Panduan Membangun Mesin 1 Silinder Matic

**Bagian 0 — Pengantar dan Peta Belajar**

---

## 0.1 Ruang lingkup

Buku ini khusus untuk **mesin 1 silinder, 4 langkah, transmisi CVT (matic)**, dengan konfigurasi katup:

- **2 klep** (1 isap + 1 buang)
- **3 klep** (2 isap + 1 buang)
- **4 klep** (2 isap + 2 buang)

Kapasitas yang jadi acuan: **125–250 cc**. Prinsipnya berlaku lebih luas, tapi semua angka contoh diambil dari rentang ini.

**Yang TIDAK dibahas:** mesin multi-silinder, 2 langkah, transmisi manual bergigi, turbo/supercharger, dan mesin diesel. Sebagian prinsip tetap berlaku, tapi angkanya tidak.

**Kenapa CVT dipisahkan:** transmisi CVT mengubah cara sebuah mesin harus ditala. Pada motor bergigi, lebar pita tenaga sangat penting karena putaran jatuh tiap kali pindah gigi. Pada CVT, mesin bisa ditahan di satu titik putaran sepanjang akselerasi — sehingga **tenaga puncak jauh lebih penting daripada lebar pita**. Ini mengubah pilihan cam, port, dan throttle body secara mendasar.

---

## 0.2 PERINGATAN — baca ini sebelum melanjutkan

> **Buku ini memberi BASELINE, bukan jaminan.**

Setiap angka di buku ini adalah **titik awal yang beralasan**, bukan hasil akhir yang pasti. Mesin nyata selalu berbeda dari perhitungan, dan perbedaannya bisa besar.

**Kenapa perhitungan tidak pernah 100% tepat:**

| Sumber perbedaan | Besarnya |
|---|---|
| Toleransi manufaktur (bore, stroke, klep, port) | ±0,5–2% |
| Kualitas pengerjaan porting | ±5–15% |
| Suhu udara, kelembaban, tekanan udara | ±3–5% |
| Kualitas bahan bakar antar batch | ±2–5% |
| Kondisi CVT, rantai keteng, kebocoran | ±5–10% |
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

Ini bagian terpenting dari pengantar. Banyak orang gagal bukan karena kurang ilmu, tapi karena **belajar dalam urutan yang salah** — misalnya menghabiskan bulanan menggerus port padahal knalpotnya salah panjang.

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
- Jumlah klep: 2, 3, atau 4
- Kapasitas besar dengan klep kecil — kombinasi yang sering salah
- Inersia kruk as

**Kenapa ini kedua:** semua keputusan berikutnya bergantung pada bore, stroke, dan jumlah klep. Mengubahnya nanti berarti membangun ulang dari nol.

**Waktu belajar:** 1 minggu. **Bisa dilewati?** Tidak, kalau kamu punya pilihan basis mesin.

---

### TAHAP 3 — Aliran: kepala silinder
*Menentukan plafon tenaga mesin.*

- Klep dan batas geometri
- Throat — pembatas yang sesungguhnya
- Port: luas penampang dan kecepatan gas
- Bentuk port, short-turn radius, bowl
- Lift kritis

**Kenapa ini ketiga:** head menentukan **berapa banyak udara yang bisa masuk**, dan udara adalah batas mutlak tenaga. Cam, pengapian, dan knalpot cuma menentukan seberapa dekat kamu ke plafon itu.

**Waktu belajar:** 3–4 minggu. Ini bagian paling teknis. **Bisa dilewati?** Tidak.

---

### TAHAP 4 — Timing: camshaft
*Menentukan di putaran berapa plafon itu tercapai.*

- Empat kejadian katup dan urutan kepentingannya
- IVC dan kompresi dinamis
- Durasi dari time-area
- Overlap, LSA, ICL
- Kelegaan klep-piston

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
- Busi: heat range, gap, elektroda
- Koil: TCI, CDI, smart coil
- ECU standar, remap, dan ECU aftermarket

**Kenapa di sini:** ini bagian yang **paling murah** untuk memberi tenaga, dan **paling cepat** merusak mesin kalau salah. Bisa dipelajari paralel dengan Tahap 5.

**Waktu belajar:** 2–3 minggu. **Bisa dilewati?** Tidak.

---

### TAHAP 7 — Saluran masuk dan buang
*Memanfaatkan gelombang tekanan.*

- Throttle body
- Panjang intake runner dan tuning gelombang
- Velocity stack dan plenum
- Port buang, header, panjang knalpot

**Kenapa setelah cam:** panjang runner dan header ditala terhadap timing katup. Tanpa cam yang pasti, panjangnya tidak bisa dihitung.

**Waktu belajar:** 2 minggu. **Bisa dilewati?** Tidak — ini sering jadi sumber kehilangan tenaga terbesar yang tidak disadari.

---

### TAHAP 8 — Mekanik, material, dan keandalan
*Supaya yang sudah dibangun tidak jebol.*

- Batas mekanis: kecepatan piston, percepatan, gaya inersia
- Material: piston, rod, klep — aluminium, baja, stainless, titanium
- Coating pada piston dan klep
- Ring piston: single versus double, cara pemasangan
- Clearance piston dan ring
- Pemuaian termal
- Per klep: pemilihan, pengukuran, floating
- Massa berputar dan bolak-balik

**Kenapa di sini:** setelah tahu berapa rpm yang dikejar, baru bisa ditentukan material dan clearance yang dibutuhkan.

**Waktu belajar:** 3 minggu. **Bisa dilewati?** Tidak, kalau kamu ingin mesinnya bertahan.

---

### TAHAP 9 — Penyaluran tenaga: CVT
*Tenaga yang tidak sampai ke roda tidak ada artinya.*

- Cara kerja CVT
- Roller, per sentri, per CVT
- Rasio, kecepatan puncak, akselerasi
- Menyesuaikan CVT ke pita tenaga

**Kenapa terakhir:** CVT ditala ke pita tenaga mesin. Menala CVT sebelum mesinnya jadi adalah pekerjaan yang harus diulang.

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
```

**Kesalahan urutan yang paling sering terjadi:**

| Kesalahan | Akibat |
|---|---|
| Beli cam sebelum head selesai | durasi salah, harus beli lagi |
| Tentukan kompresi sebelum cam | DCR meleset, detonasi atau kurang tenaga |
| Porting habis-habisan tapi knalpot standar | 20–30% tenaga hilang di knalpot |
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

### Mesin Contoh A — 199cc, 2 klep, drag matic

| | |
|---|---|
| Bore × stroke | 63 × 64 mm = 199,5 cc |
| Klep isap / buang | 31 / 27 mm |
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

### Mesin Contoh B — 150cc, 4 klep, rancangan

| | |
|---|---|
| Bore × stroke × rod | 57,3 × 58 × 95 mm = 149,6 cc |
| Klep isap / buang | 22 / 19 mm |
| Throat isap / buang | 20,2 / 16,7 mm |
| Kompresi statis | 14:1 |
| RPM sasaran | 12.000 |

**Peran dalam buku:** contoh penerapan seluruh metode dari awal sampai akhir.

### Mesin Contoh C — 155cc, 3 klep, basis standar

| | |
|---|---|
| Bore × stroke | 58 × 58,6 mm = 154,8 cc |
| Katup | 3 klep (2 isap + 1 buang) |
| Pendingin | udara |
| Kompresi standar | 10,5:1 |
| Tenaga standar | 12,7 HP @ 7.750 rpm |

**Peran dalam buku:** contoh arsitektur 3 klep dan batasannya.

---

## 0.7 Daftar berkas

| Berkas | Isi |
|---|---|
| `00-PENGANTAR.md` | ruang lingkup, peringatan, peta belajar (berkas ini) |
| `01-KAMUS-ISTILAH.md` | 21 istilah dalam 6 kelompok |
| `02-TAHAP1-MENGUKUR.md` | torsi vs tenaga, powerband, dyno |
| `03-TAHAP2-KONFIGURASI.md` | bore/stroke, rod, jumlah klep, kruk as |
| `04-TAHAP3-ALIRAN.md` | klep, throat, port, bentuk |
| `05-TAHAP4-CAMSHAFT.md` | timing, durasi, overlap, kelegaan |
| `06-TAHAP5-KOMPRESI-BBM.md` | kompresi, bahan bakar, detonasi |
| `07-TAHAP6-PENGAPIAN-AFR.md` | AFR, spark, injeksi, busi, koil, ECU |
| `08-TAHAP7-SALURAN.md` | throttle body, runner, stack, knalpot |
| `09-TAHAP8-MEKANIK.md` | material, ring, clearance, per klep, massa |
| `10-TAHAP9-CVT.md` | CVT, rasio, top speed, akselerasi |
| `11-TAHAP10-SIMULASI.md` | CFD dan validasi |
| `12-LAMPIRAN.md` | rumus, perkakas, daftar periksa |

---

*Buku ini disusun tanpa gambar. Diagram dan grafik dapat ditambahkan pada revisi berikutnya.*
