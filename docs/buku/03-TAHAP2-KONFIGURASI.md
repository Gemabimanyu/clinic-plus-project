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

Torsi berasal dari tekanan pembakaran yang bekerja pada luas piston dikali jari-jari engkol:

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
