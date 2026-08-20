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
