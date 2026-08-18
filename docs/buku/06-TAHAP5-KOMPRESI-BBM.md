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
Vc_total = V_pentroof + V_gasket + V_deck + V_kantong_klep − V_dome_piston
```

| Komponen | Rumus |
|---|---|
| Pent-roof | luas_bore × tinggi_efektif (3–4 mm untuk 4 klep) |
| Gasket | luas_bore × tebal_gasket |
| Deck | luas_bore × jarak piston di bawah deck di TDC |
| Kantong klep | n_kantong × luas_kantong × kedalaman × ~0,40 |
| Dome piston | negatif — mengurangi volume |

Faktor 0,40 pada kantong klep karena bentuknya cekungan dangkal, bukan silinder penuh.

### 2.2 Contoh nyata

Mesin Contoh B, bore 57,3 mm, target CR 14:1 pada 149,6 cc → Vc harus **11,50 cc**. [HITUNG]

| Komponen | Volume |
|---|---|
| Pent-roof (3,5 mm) | 9,03 cc |
| Gasket 0,8 mm | 2,06 cc |
| Deck 0,5 mm | 1,29 cc |
| 4 kantong klep 2,71 mm | 1,58 cc |
| **Total** | **13,95 cc** |

→ CR tanpa dome: **11,72:1**, bukan 14:1.

**Dome piston harus mengusir 2,45 cc** (tinggi rata-rata 0,95 mm).

### 2.3 Pelajaran

**Kantong klep ikut menambah volume ruang bakar.** Pada contoh di atas 14% anggaran; dengan overlap lebih besar bisa 20%.

Akibatnya nyata: head dipapas untuk mengejar kompresi, lalu kantong klep digerus untuk cam baru, dan sebagian kompresi yang baru didapat langsung hilang lagi.

> **Urutan yang benar: cam dulu → kantong klep → baru dome atau papasan.**

### 2.4 Cara mengukur Vc yang benar

Jangan pakai angka dari spesifikasi. Ukur.

1. Pasang piston di TDC persis (pakai dial indicator)
2. Pasang head dengan gasket yang akan dipakai, kencangkan sesuai torsi
3. Pasang klep dan busi
4. Isi ruang bakar lewat lubang busi dengan buret berisi minyak ringan atau alkohol
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

Catatan penting: **timbal pada avgas melapisi elektroda busi dan sensor lambda.** Kalau memakai wideband untuk tuning, umurnya jauh lebih pendek. Busi juga perlu lebih sering diperiksa.

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

Bukan untuk mesin konversi. Butuh piston, rod, kruk as, dan sistem bahan bakar yang dirancang khusus. Tekanan pembakaran berlipat kali lipat bensin.

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
| Busi di tengah (4 klep) | jalur api merata |
| RPM lebih tinggi | waktu untuk detonasi berkembang lebih pendek |
| Pendingin cair | suhu dinding lebih stabil |
| Campuran lebih kaya | pendinginan muatan |
| Squish yang baik | turbulensi mempercepat pembakaran |
| Suhu udara masuk rendah | muatan lebih dingin |

**Menurunkan toleransi:**

| Faktor | Sebabnya |
|---|---|
| Bore besar | jalur api panjang |
| Ruang bakar asimetris (2/3 klep) | busi menepi |
| Dome piston tinggi | jalur api panjang, titik panas |
| Suhu udara masuk tinggi | muatan panas |
| Beban berkelanjutan | akumulasi panas |
| Deposit karbon | titik panas dan menaikkan CR efektif |

**Penerapan:** head 3 klep punya busi menepi dan ruang bakar asimetris, jadi disarankan **1 angka DCR lebih rendah** dari 4 klep pada bahan bakar yang sama.

---

## 5. Knocking (detonasi)

### 5.1 Apa yang terjadi

Pembakaran normal: api menyebar dari busi secara teratur ke seluruh ruang bakar.

Detonasi: sebagian muatan di ujung ruang bakar (*end gas*) menyala **sendiri** karena tekanan dan suhu, sebelum api dari busi sampai. Dua front api bertabrakan, menghasilkan gelombang kejut.

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
| Busi terlalu panas | ganti heat range lebih dingin |
| Bahan bakar oktan turun | ganti batch, cek penyimpanan |

### 5.4 Cara mendeteksi

**Membaca busi** — cara paling murah dan cukup andal:

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

Bahan bakar yang tidak terbakar mengalir turun di dinding silinder, melewati ring, dan mencampur dengan oli di bak.

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
2. **Kantong klep ikut menambah volume ruang bakar** — 14–20% anggaran. Hitung cam dulu.
3. **Ukur Vc dengan buret**, jangan pakai angka spesifikasi. Selisihnya bisa 1–2 cc.
4. **Oktan tinggi tidak menambah tenaga** — ia memberi izin menaikkan kompresi dan memajukan pengapian.
5. **Bensin, avgas, dan race gas non-oksigenat praktis sama** potensi tenaganya (98–100%).
6. **Metanol +19% energi per kg udara** plus pendinginan 228 K, dengan ongkos konsumsi 2,45×.
7. **Pakai lambda, bukan AFR** — target lambda hampir sama untuk semua bahan bakar (0,74–0,89).
8. **Kalibrasi batas DCR ke mesinmu sendiri.** Tabel oktan umum terlalu konservatif.
9. **Detonasi ringan bisa berlangsung lama tanpa terdengar.** Baca busi dan piston.
10. **Kalau ragu: mundurkan 2°, perkaya 0,02 lambda.**

**Berikutnya:** Tahap 6 — pengapian dan campuran, bagian paling murah untuk menambah tenaga dan paling cepat merusak mesin.
