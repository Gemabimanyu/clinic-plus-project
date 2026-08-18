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

Torsi berasal dari tekanan pembakaran yang bekerja pada luas piston, dikali jari-jari engkol:

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

### 2.2 Lebar pita versus tinggi puncak

Ini pertukaran mendasar dalam tuning:

| | Pita lebar | Pita sempit |
|---|---|---|
| Durasi cam | pendek | panjang |
| Overlap | kecil | besar |
| LSA | besar (108–116°) | kecil (98–104°) |
| Panjang runner | sedang | ditala tajam |
| Puncak tenaga | lebih rendah | lebih tinggi |
| Cocok untuk | motor gear, harian | CVT, drag |

### 2.3 Kenapa CVT mengubah aturannya

Pada motor gear, setiap pindah gear menjatuhkan putaran mesin. Kalau pitanya sempit, mesin jatuh keluar pita dan akselerasi hilang. Karena itu motor gear butuh pita lebar.

**CVT tidak punya masalah itu.** Rasio berubah kontinu, sehingga mesin bisa ditahan di satu titik putaran sepanjang akselerasi.

Konsekuensinya sangat besar:

> **Pada CVT, yang perlu dioptimalkan adalah tenaga di SATU titik putaran, bukan lebar pita.**

Ini memberi kebebasan yang tidak dimiliki motor gear: cam durasi panjang, overlap besar, LSA sempit, runner ditala tajam — semua yang membuat pita sempit tapi puncaknya tinggi.

**Syaratnya:** CVT harus benar-benar mampu menahan mesin di titik itu. CVT yang salah setelan akan membiarkan putaran jatuh, dan mesin berpita sempit akan terasa jauh lebih lambat daripada mesin standar. Bahasan di Tahap 9.

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

**Stopwatch di lintasan bukan pengganti dyno.** Waktu lintasan dipengaruhi launch, traksi, angin, dan pengendara — variasinya sering lebih besar dari efek yang mau diukur.

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
4. Pada CVT, **tenaga puncak lebih penting daripada lebar pita**.
5. Perubahan 2–5% tidak bisa dirasakan tapi menumpuk jadi besar — karena itu dyno wajib.
6. Satu perubahan per sesi dyno. Ini aturan yang paling sering dilanggar.
7. Bandingkan hanya run di hari yang sama, dyno yang sama.
8. Kumpulkan data lengkap sebelum mulai. Yang paling sering hilang: **throat, lift acuan cam, dan panjang header**.

**Berikutnya:** Tahap 2 — memilih konfigurasi dasar yang tidak bisa diubah lagi setelah mesin dibangun.
