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

### 3.4 Kalibrasi time-area per mesin — dan koreksi atas "konstanta mutlak"

Rumus 3.1 bisa diringkas jadi satu angka per mesin:

```
K = A_throat[mm²] × durasi[°] / (Vd[cc] × rpm_peak)
```

Dua mesin dengan K yang sama berada di titik time-area yang sama. Rumus 3.1 sebenarnya cuma mengatakan: **anggap K mesin baru sama dengan K mesin acuan.**

> **Koreksi.** Edisi sebelumnya menulis `K = 8,0 / v_throat_sasaran` dan menyebutnya "tervalidasi pada tiga mesin" karena `K × v` keluar 8,01 di ketiganya. Klaim itu **salah**. Kolom v di tabel itu dihitung sebagai `MGV_throat × 240/durasi`, sehingga:
>
> ```
> K × v = [A·dur / (Vd·rpm)] × [Vd·rpm·240 / (30·A·dur)] = 240/30 = 8
> ```
>
> Hasilnya 8 **untuk mesin apa pun**. Itu identitas aljabar, bukan temuan — tidak ada yang tervalidasi. Kesalahan ini baru ketahuan saat rumusnya dicoba ke mesin keempat yang datanya dipublikasikan pabrikan (Tahap 11 §11).

Hubungan yang jujur — juga sebuah identitas, tapi tidak menyamar sebagai hukum:

```
MGV_throat = Vd[cc] × rpm / (30 × A_throat[mm²])      [m/s]   (= luas piston / A_throat × MPS)
K × MGV_throat = durasi / 30
```

Artinya K hanya ditentukan oleh dua hal: **seberapa keras throat dipakai di peak** (MGV throat, lihat Kamus) dan **durasi cam**. Empat mesin:

| Mesin | A_throat | Durasi | rpm peak | MGV throat | K |
|---|---|---|---|---|---|
| Mesin Contoh A (2 valve, drag) | 661 mm² | 281° | 10.000 | 101 m/s | 0,093 |
| XMAX bore-up 345cc (4 valve, seat terukur) | 1.021 mm² | 260° | ~8.400 | 95 m/s | 0,092 |
| Mesin balap 224cc (4 valve) | 726 mm²* | 261° | 11.000 | 113 m/s | 0,077 |
| Honda CRF450R 2021 (4 valve, pabrikan) | 1.837 mm²* | tidak dipublikasi | 9.300 | **76 m/s** | 0,114–0,132** |

\* throat diasumsikan dari diameter valve (TR 0,935 dan 0,90). \*\* untuk durasi 260–300°.

Dua catatan kepercayaan: rpm peak XMAX adalah hasil koreksi (sumbu rpm dyno aslinya rusak oleh rasio CVT tetap, Tahap 11 §9). rpm peak mesin 224cc dibaca dari dyno sejenis tanpa locked ratio pulley, dan pasangan tenaga-rpm-nya sendiri gagal uji jepitan (Tahap 11 §8.6) — K 0,077 dari mesin itu belum terverifikasi.

K berkisar 0,077 sampai lebih dari 0,13 — **bukan konstanta**. CRF450R memakai throat-nya jauh lebih santai (76 m/s) dibanding mesin lain: peak-nya tidak ditentukan oleh batas aliran isap, tapi oleh hal lain (knalpot, penalaan, karakter tenaga motocross).

**Yang tetap berlaku, dan cara memakainya:**

1. **Kalibrasi per mesin.** Dari satu titik terukur (throat, durasi, rpm peak dyno) didapat K mesin itu. Perubahan pada mesin yang sama lalu dihitung dengan `rpm_peak_baru = A_baru × durasi_baru / (K × Vd)`. Sah selama karakter kepalanya tidak berubah dan mesin masih dibatasi aliran isap di peak.
2. **Meminjam K mesin lain** sama dengan memakai rumus 3.1. Sah hanya bila karakter kepalanya mirip — bisa tepat sampai 1,1% (Tahap 11 §3.2), bisa meleset jauh (Tahap 11 §4).
3. **Basis harus konsisten.** `A` selalu luas throat kotor (tanpa dikurangi batang valve — batang sudah ikut terserap di kalibrasi). Durasi selalu pada konvensi lift yang sama (§3.7). Mengganti A dengan luas port pada mesin yang dikalibrasi dengan luas throat merusak seluruh angka (Tahap 11 §3.4).

### 3.5 Kenapa bore-up tanpa upgrade valve tidak menaikkan plafon HP

Ini konsekuensi langsung dari kalibrasi per mesin di atas, dan sering disalahpahami.

Untuk kepala yang sama, K-nya tetap. Substitusikan `rpm_peak = A × durasi / (K × Vd)` dari §3.4 ke rumus tenaga (`HP ∝ BMEP × Vd × rpm`):

```
HP  ∝  BMEP × Vd × [A_throat × durasi / (K × Vd)]
     =  BMEP × A_throat × durasi / K
```

**Vd habis dibagi.** Selama BMEP dan K kepala itu tidak berubah, plafon tenaga cuma ditentukan oleh **luas throat dan durasi cam** — kapasitas silinder tidak muncul lagi di rumusnya.

**Syaratnya:** mesin harus **dibatasi aliran isap** di peak-nya. Mesin yang throat-nya masih longgar di peak (MGV throat rendah, seperti CRF450R di §3.4) peak-nya diatur hal lain, dan teorema ini tidak berlaku untuknya.

Konsekuensinya, untuk kepala yang sama dibesarkan kapasitasnya (bore atau bore+stroke) **tanpa mengganti valve**:

| Tindakan | Yang terjadi pada peak rpm | Yang terjadi pada plafon HP |
|---|---|---|
| Cam dibiarkan | **turun** — mesin kehabisan napas lebih cepat relatif kapasitasnya | tetap, dicapai di rpm lebih rendah |
| Cam durasi dinaikkan untuk mengembalikan rpm semula | kembali ke titik semula | **tetap juga** — cuma dicapai lagi di rpm semula, bukan lebih tinggi |

Contoh: kepala 2 valve 29/23 di basis 150cc square dibesarkan ke 180cc (bore naik, stroke tetap) dan 200cc (bore dan stroke naik), tanpa ganti valve:

| Kapasitas | Peak rpm (cam tetap) | Durasi yang dibutuhkan untuk kembali ke rpm semula |
|---|---|---|
| 150cc | 9.202 (acuan) | 240° (acuan) |
| 180cc | 7.689 (**−16%**) | 287° (**+47°**) |
| 200cc | 6.919 (**−25%**) | 319° (**+79°**) |

Plafon HP-nya, dihitung independen lewat rumus CFM (Tahap 3 §1), **sama di ketiga kapasitas** — karena rumus itu juga cuma fungsi luas throat, bukan Vd.

**Yang benar-benar berubah dari bore-up polos:** torsi bawah-tengah naik nyata (Vd lebih besar mengisi lebih banyak udara per siklus di rpm yang belum menyentuh batas throat), dan cam oversize berguna untuk memulihkan titik peak yang bergeser turun akibat mismatch. Tapi cam **tidak bisa mencetak luas throat yang tidak ada** — untuk menaikkan plafon sungguhan, satu-satunya jalan tetap membesarkan valve/port (Tahap 3).

> **Catatan batas model:** turunan ini mengasumsikan BMEP konstan berapapun durasi cam-nya. Di dunia nyata cam yang sangat panjang (200°-an lebih dari acuan) biasanya sedikit menurunkan BMEP puncak karena pengisian dinamis yang kurang efisien di overlap besar — jadi pemulihan plafon lewat cam oversize sedikit di bawah 100% secara praktik, ditambah ongkos nyata di idle dan respons rpm rendah.

### 3.6 Durasi buang

Ditentukan oleh **rasio throat buang/isap** (lihat Tahap 3, bagian 3.4):

| Rasio throat ex/in | Tindakan |
|---|---|
| < 0,63 | tambah 8–12° durasi ex |
| 0,63–0,72 | **cam simetris** |
| > 0,72 | sisi buang lega |

Mesin Contoh A (rasio 0,671) berjalan simetris 281/281. Mesin Contoh B (rasio 0,685) juga simetris 261/261.

### 3.7 Konvensi durasi dan kepenuhan lobe

Semua rumus di atas memakai satu angka durasi. Satu angka itu menyembunyikan dua hal yang bisa menggeser hasil lebih besar daripada seluruh perhitungannya.

**Konvensi lift.** Durasi tanpa keterangan lift acuan adalah angka setengah jadi. Tabel Mesin Contoh B di §3.3 memakai **@1 mm**. Banyak pembuat cam aftermarket mengutip durasi *advertised* (seat-to-seat, sekitar 0,15–0,25 mm). Konversi kasar dari advertised:

| Konvensi | Selisih dari advertised | Tergantung ramp |
|---|---|---|
| @1,00 mm | −15 s/d −25° | ramp landai −25 s/d −35°, ramp agresif −10 s/d −18° |
| @0,050" (1,27 mm, SAE) | −20 s/d −30° | idem |

Selisih 20° kira-kira setara **7% rpm peak**. Tabel ini hanya perkiraan — bentuk ramp tiap cam berbeda. Aturan praktisnya: **kalibrasi K (§3.4) dan semua perbandingan harus memakai konvensi yang sama.** Kalau durasi sebuah data tidak jelas konvensinya, anggap K dari data itu cuma berlaku untuk cam dengan sumber angka yang sama.

**Kepenuhan lobe.** Dua cam dengan durasi dan lift maksimum identik bisa bernapas sangat berbeda: yang satu "gendut" (cepat naik, lama di atas), yang lain "kurus". Ukurannya:

```
A_efektif(θ) = min( n_valve × π × D_valve × L(θ) ,  A_throat )
Φ = ∫ A_efektif(θ) dθ  /  ( A_throat × durasi )
durasi_efektif = durasi × Φ / Φ_acuan
```

`A_efektif` berhenti naik begitu lift melewati **lift kritis** (Tahap 3 §4) — di atas titik itu throat yang membatasi. Φ selalu ≤ 1; nilai realistis cam motor sekitar 0,65–0,85.

Ilustrasi (valve 2 × 23, throat Ø21,5 → lift kritis 5,03 mm; tiga bentuk lobe dengan durasi 280° dan lift 8,5 mm yang sama):

| Bentuk lobe | Derajat di atas lift kritis | Φ | Durasi efektif |
|---|---|---|---|
| gendut | 210° | 0,912 | **317°** |
| sedang (acuan) | 168° | 0,806 | 280° |
| kurus | 134° | 0,687 | **239°** |

Selisih 78° durasi efektif — jauh lebih besar daripada perdebatan konvensi. Angka Φ di atas dari bentuk lobe teoretis; nilai 0,912 menuntut akselerasi valvetrain yang sangat ekstrem.

**Lift tinggi melandai hasilnya.** Tahap 3 §4 menjelaskan kenapa mesin balap memakai lift jauh di atas lift kritis: valve bertahan lebih lama di luas penuh. Φ memperlihatkan seberapa cepat manfaat itu mengecil (lobe sedang, 280°, lift kritis 5,03 mm):

| Lift maks | Kelipatan lift kritis | Φ |
|---|---|---|
| 6,0 mm | 1,2× | 0,713 |
| 7,0 | 1,4× | 0,760 |
| 8,5 | 1,7× | 0,806 |
| 10,0 | 2,0× | 0,836 |
| 12,0 | 2,4× | 0,865 |

Dari 6 ke 7 mm Φ naik 0,047; dari 10 ke 12 mm cuma 0,029, dengan ongkos valvetrain jauh lebih besar. Di atas ~1,7× lift kritis, anggaran valvetrain lebih bernilai dipakai untuk **ramp yang lebih cepat** daripada puncak yang lebih tinggi.

**Mengukur Φ sendiri** (degree wheel + dial indicator, satu sore):

1. Baca lift tiap 5° sepanjang durasi, rapatkan jadi 2° di daerah ramp.
2. Tiap baris: `A_eff = min(n × π × D_valve × L, A_throat)`.
3. Jumlahkan dengan trapesium: `∫ ≈ Σ A_eff × 5°`.
4. `Φ = ∫ / (A_throat × durasi)`.

**Proksi lapangan:** selisih antara durasi advertised dan @1 mm. Selisih kecil (10–18°) berarti ramp curam dan lobe gendut; selisih besar (28–35°) berarti lobe kurus. Pembuat cam yang cuma mau menyebut satu angka durasi sudah memberi sinyal tersendiri.

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

**Lebih baik lagi: minta tabel lift vs derajat** dari lobe yang ditawarkan. Dari tabel itu kepenuhan lobe (§3.7) dan durasi efektifnya bisa dihitung sendiri dalam lima menit — tanpa bergantung pada satu angka di brosur.

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
10. **K time-area dikalibrasi per mesin**, bukan diambil dari konstanta universal. "Validasi K × v = 8" di edisi lama adalah identitas aljabar.
11. **Basis harus konsisten:** luas throat kotor, dan durasi pada konvensi lift yang sama.
12. **Bentuk lobe (Φ) bisa menggeser durasi efektif puluhan derajat** — lebih besar dari perdebatan konvensi. Minta tabel lift, bukan satu angka durasi.

**Berikutnya:** Tahap 5 — kompresi dan bahan bakar, yang tidak bisa ditentukan sebelum cam final.
