# TAHAP 7 — SALURAN MASUK DAN BUANG

*Memanfaatkan gelombang tekanan. Sering jadi sumber kehilangan tenaga terbesar yang tidak disadari.*

---

## 1. Throttle body

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

### 1.3 Kenapa mengecilkan TB TIDAK menaikkan gas speed

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

### 1.4 Kalau mau menaikkan gas speed, ini tuasnya

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

Panjang efektif kolom udara lebih panjang dari panjang fisiknya:

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

**JANGAN** membuat TB lebih kecil dari port lalu melebar lagi di stack. Itu menciptakan penyempitan-pelebaran yang merugikan dua kali.

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
- [ ] Diameter manifold sama atau sedikit lebih besar dari port head
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

**Reverse cone** — penyempitan setelah megaphone menghasilkan gelombang positif pantulan yang mencegah muatan segar lolos. Berguna untuk melebarkan pita.

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
