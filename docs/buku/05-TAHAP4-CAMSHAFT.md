# TAHAP 4 — TIMING: CAMSHAFT

*Menentukan di putaran berapa plafon head tercapai.*

---

## 1. Apa yang sebenarnya diatur cam

Cam tidak "mengisi ruang bakar". Head sudah menentukan plafonnya. Cam mengatur **kapan** klep membuka dan menutup relatif terhadap piston dan gelombang tekanan.

Empat kejadian, urut menurut kepentingannya:

| # | Kejadian | Menentukan |
|---|---|---|
| **1** | **IVC** — klep isap menutup | kompresi dinamis, rpm efisiensi penjebakan puncak |
| **2** | **Durasi + lift** | berapa banyak yang bisa lewat (time-area) |
| **3** | **Overlap** di TDC | pembilasan sisa gas buang |
| **4** | **EVO** — klep buang membuka | tukar kerja ekspansi dengan rugi pemompaan |

Ditambah satu yang bukan soal tenaga sama sekali: **kelegaan klep-piston**. Ini soal mesin pecah atau tidak.

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
| Contoh A (2 klep) | 199,5 cc | 661 mm² | 10.000 | 281° |
| Contoh B (4 klep) | 149,6 cc | 641 mm² | 12.000 | **261°** |

**Durasi turun walau rpm naik.**

Sebabnya: head 4 klep bernapas 29% lebih lega per cc (4,28 vs 3,31 mm²/cc). Butuh waktu lebih sedikit untuk memasukkan jumlah yang sama.

Ini contoh kenapa aturan jempol "rpm tinggi = durasi panjang" bisa menyesatkan. Yang benar: rpm tinggi **dan luas klep tetap** butuh durasi panjang.

### 3.3 Tabel durasi terhadap RPM

Mesin Contoh B: [HITUNG]

| RPM sasaran | Durasi isap @1mm |
|---|---|
| 11.000 | 239° |
| 11.500 | 250° |
| **12.000** | **261°** |
| 12.500 | 271° |
| 13.000 | 282° |

Mesin Contoh C (3 klep, luas klep isap/bore cuma 0,262):

| RPM | Durasi isap |
|---|---|
| 10.000 | 238° |
| 12.000 | **285°** |

Selisih 24° pada rpm yang sama — itu ongkos nyata dari 11% luas klep yang hilang.

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

LSA 102,5° ketat — khas mesin drag yang mengejar puncak, bukan lebar pita.

### 4.3 Menskalakan overlap

Yang harus dipertahankan adalah **luas tirai overlap per cc**:

```
luas_per_cc = n_klep × π × D_klep × lift_di_TDC / kapasitas
```

Ini krusial untuk 4 klep. Dua klep isap memberi luas tirai jauh lebih besar per milimeter lift dibanding satu klep besar.

**Contoh:** Mesin Contoh A punya 1 klep 31 mm dengan lift TDC 1,83 mm pada 199,5 cc. Mesin Contoh B dengan 2 klep 22 mm pada 149,6 cc perlu lift TDC **0,97 mm** — bukan 1,83, dan bukan 2,55 (yang keluar kalau diskalakan lewat diameter saja).

### 4.4 Jebakan penafsiran "lift overlap"

Angka lift overlap yang beredar sering ambigu: lift **satu klep** atau **gabungan in + ex**?

Cara memastikannya: hitung dari sudut. Dengan profil harmonik,
```
lift(θ) = lift_maks × sin²(π × θ_dari_bukaan / durasi)
```

Untuk Mesin Contoh A (IVO 38 BTDC, durasi 281°, lift 10,8 mm):
```
lift di TDC = 10,8 × sin²(π × 38/281) = 1,83 mm per klep
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

## 5. Kelegaan klep-piston

### 5.1 Kenapa kantong klep dibutuhkan

Di dekat TDC piston hampir tidak bergerak. Untuk stroke 58 mm rod 95 mm: [HITUNG]

| Sudut dari TDC | Turun piston |
|---|---|
| 4° | 0,09 mm |
| 8° | 0,28 mm |
| 14° | 1,10 mm |
| 20° | 2,27 mm |

Sementara klep sudah bergerak beberapa milimeter. Titik paling kritis biasanya **7–10° setelah TDC**.

### 5.2 Perhitungan

```
kebutuhan(θ) = lift_klep(θ) − turun_piston(θ)
kantong = maks(kebutuhan) × faktor_aman + kelegaan_minimum
```

| Parameter | Nilai |
|---|---|
| Faktor aman | 1,25 — profil harmonik meremehkan lift di sisi flank |
| Kelegaan minimum isap | 1,0–1,5 mm |
| Kelegaan minimum buang | 1,5–2,0 mm (klep buang memuai lebih banyak) |

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
- Sudut klep terhadap sumbu silinder
- Bentuk kubah piston
- Deformasi valvetrain pada rpm tinggi (rocker melentur, rantai keteng meregang)
- Profil cam sebenarnya, yang lebih agresif dari model harmonik
- Pemuaian termal rod (bisa 0,1 mm — cukup untuk mengubah kelegaan)

> **Selalu cek dengan clay atau lilin sebelum mesin diputar. Tanpa pengecualian.**

**Cara cek clay:**
1. Pasang piston, rod, head, cam dengan timing final
2. Tempel clay setebal 3–4 mm di area kantong klep
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
| Lift di TDC | 0,97 mm per klep isap |
| Kantong klep | 2,71 mm |

Dibandingkan dengan Mesin Contoh A: durasi turun dari 281° ke 261°, overlap dari 76° ke 55°. Bukan karena lebih jinak, tapi karena dua klep isap memberi luas tirai jauh lebih besar per derajat.

LSA-nya sendiri dipertahankan persis di 102,5° — sama seperti cam yang terbukti.

---

## 7. Memesan cam

Yang harus disebutkan ke pembuat cam:

- [ ] **Durasi in dan ex, PADA LIFT BERAPA** (@1mm, @0.050", atau seat-to-seat)
- [ ] **Lift maksimum in dan ex** — di klep, bukan di lobe (kalau ada rocker ratio)
- [ ] **Rocker ratio**, kalau ada
- [ ] **ICL dan LSA** yang diinginkan
- [ ] **Base circle** — kalau diubah, clearance rocker berubah
- [ ] **Jenis lifter** (flat, roller, bucket)
- [ ] **RPM maksimum** — menentukan agresivitas ramp yang aman
- [ ] **Per klep yang akan dipakai** — menentukan apakah ramp bisa seagresif itu

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
8. **Kantong klep dihitung sebelum menghitung dome piston** — kantong ikut menambah volume ruang bakar.
9. **Cek clay wajib.** Perhitungan tidak menggantikannya.

**Berikutnya:** Tahap 5 — kompresi dan bahan bakar, yang tidak bisa ditentukan sebelum cam final.
