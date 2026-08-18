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

Untuk port bercabang (4 klep), yang dipakai adalah CSA **runner bersama** sebelum pecah dua — bukan CSA tiap cabang.

**Kenapa penting:** CSA menentukan kecepatan gas, dan kecepatan gas menentukan pengisian silinder. Ini variabel desain port yang paling berpengaruh.

**Rentang khas:** untuk mesin balap kecil, CSA port isap berkisar 0,90–1,10 × luas throat.

**Kesalahpahaman yang umum:**

*Menyebut ukuran port dalam diameter, bukan luas.* Menyesatkan karena luas berskala dengan **kuadrat** diameter. Menaikkan port dari 28 ke 30 mm terdengar kecil (+7%), padahal luasnya naik **15%**. Selalu berpikir dalam mm².

*Mengukur di tempat yang salah.* Banyak orang mengukur di mulut flange karena paling mudah dijangkau. Titik tersempit biasanya di dekat short-turn atau tepat sebelum bowl.

**Contoh:** Mesin Contoh A punya port isap bundar Ø29,5 mm → CSA 683 mm². Mesin Contoh B dirancang 615–665 mm² dengan penampang oval 22,7 × 29,5 mm.

---

### Throat
**Diameter dalam seat klep**

**Satuan:** mm untuk diameter, mm² untuk luas

**Rumus:**
```
A_throat = n_klep × π/4 × D_throat²
```

**Diukur di mana:** lubang paling sempit di dalam seat, tepat di bawah permukaan yang bersentuhan dengan klep. Bukan diameter klep, bukan diameter luar seat.

**Kenapa penting:** pada lift tinggi, throat adalah **pembatas sesungguhnya**. Membesarkan throat adalah satu-satunya perubahan yang menaikkan plafon flow head — bentuk port tidak bisa melakukannya.

**Rentang khas:**

| Rasio throat/klep | Keterangan |
|---|---|
| 0,85–0,88 | konservatif, umum di buku |
| 0,88–0,92 | balap lazim |
| 0,92–0,94 | agresif |
| > 0,94 | seat sangat tipis, berisiko |

Batasnya lebar seat: `lebar = (D_klep − D_throat) / 2`. Di bawah 0,7 mm berisiko, terutama sisi buang.

**Kesalahpahaman yang umum:**

*Mengira aturan 0,85–0,90 itu hukum mati.* Mesin Contoh A berjalan di **0,935** bertahun-tahun pada kompresi 16:1. Yang menentukan bukan rasionya, tapi lebar seat dalam milimeter dan kualitas materialnya.

*Menyamakan sisi isap dan buang.* Sisi buang selalu butuh seat lebih lebar — seat itulah jalan panas klep buang keluar.

---

### Bore, Stroke, Rod
**Diameter silinder, panjang langkah, panjang stang piston**

**Satuan:** mm

**Rumus turunan:**
```
Kapasitas   : Vd = π/4 × bore² × stroke
Luas piston : A_p = π/4 × bore²
Rasio rod   : R = panjang_rod / stroke
```

**Kenapa penting:**

**Bore** menentukan berapa besar klep yang muat — itu plafon napas mesin. Bore besar juga memperpanjang jalur api, menurunkan toleransi detonasi.

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

*Mengira rod panjang selalu lebih baik.* Rod pendek memang menaikkan side thrust dan percepatan puncak, tapi juga membuat piston menjauh dari TDC lebih cepat — yang **melonggarkan kelegaan klep** dan **memperpendek waktu untuk detonasi berkembang**.

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

**Kenapa penting:** MGV menentukan **momentum muatan** yang masuk silinder. Momentum itu yang terus mengisi silinder bahkan setelah piston melewati BDC — efek ram yang menaikkan efisiensi volumetrik.

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
| Luas **payung klep** | 0,45–0,55 |
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
| 0,85–0,95 | saluran tanpa klep |

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

**Definisi:** perbandingan massa udara yang benar-benar terjebak di silinder terhadap massa udara yang mengisi kapasitas silinder pada kondisi atmosfer.

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
Vc = pent-roof + gasket + deck clearance + kantong klep − dome piston
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

*Melupakan kantong klep.* Kesalahan paling mahal. Empat kantong sedalam 2,7 mm menambah 1,58 cc — pada target Vc 11,50 cc itu **14% anggaran**.

**Urutan yang benar:** tentukan cam dulu → hitung kantong klep → baru hitung dome atau papasan.

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

**Kenapa penting:** **DCR yang menentukan detonasi, bukan CR.** Kompresi baru mulai setelah klep isap menutup.

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

"IVO 28° BTDC" = klep isap mulai membuka 28 derajat crank **sebelum** piston sampai TDC.

---

### BBDC / ABDC
**Sebelum / sesudah titik mati bawah**

Dipakai untuk: EVO (biasanya BBDC), IVC (biasanya ABDC).

"IVC 53° ABDC" = klep isap menutup 53 derajat **setelah** piston melewati BDC.

**Kenapa IVC selalu ABDC:** momentum muatan masih mendorong masuk walau piston sudah mulai naik. Menutup tepat di BDC membuang momentum itu.

---

## KELOMPOK 5 — KEJADIAN KATUP

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

**EVO — kenapa penting:** menentukan kapan *blowdown* dimulai. Terlalu awal membuang kerja ekspansi; terlalu telat menambah rugi pemompaan. EVO juga titik lahir gelombang tekanan untuk tuning knalpot.

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

*Mengira rpm tinggi selalu butuh durasi panjang.* Yang benar: rpm tinggi **dan luas klep tetap** butuh durasi panjang. Mesin Contoh B butuh durasi **lebih pendek** (261° vs 281°) walau rpm-nya lebih tinggi, karena head-nya bernapas 29% lebih lega per cc.

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
luas_per_cc = n_klep × π × D_klep × lift_di_TDC / kapasitas
```

**Kesalahpahaman yang umum:**

*Menskalakan lift overlap lewat diameter klep saja.* Untuk head 4 klep ini keliru dua kali lipat, karena dua klep isap memberi luas tirai jauh lebih besar per milimeter lift.

*Ambiguitas angka "lift overlap".* Angka yang beredar sering tidak jelas: lift satu klep atau gabungan in + ex? Contoh: angka "3,6 mm" pada Mesin Contoh A ternyata **gabungan** (1,83 mm per klep). Kalau ditafsirkan sebagai satu klep, target overlap jadi dua kali terlalu besar.

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
| 98–104° | overlap besar, pita sempit, drag |
| 104–110° | seimbang |
| 110–116° | overlap kecil, pita lebar, jalanan |

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
lift_kritis = A_throat / (n_klep × π × D_klep)
```

**Artinya:** di bawah lift kritis, **luas tirai** yang membatasi. Di atasnya, **throat** yang membatasi.

**Kenapa mesin balap tetap memakai lift jauh di atas lift kritis:** yang dibayar bukan flow puncak, tapi **time-area**. Menahan klep tinggi lebih lama mengisi silinder lebih banyak.

**Rentang khas kelipatan:**

| Kelipatan lift kritis | Keterangan |
|---|---|
| 1,0–1,3× | jalanan |
| 1,5–2,0× | balap |
| 2,0–2,5× | drag, beban valvetrain tinggi |

**Kesalahpahaman yang umum:**

*Mempercayai aturan "lift maksimum berguna = 0,25 × diameter klep".* Benar untuk **flow puncak steady**, salah untuk mesin balap.

*Menyamakan kebutuhan lift sisi isap dan buang:*

| Arsitektur | Lift kritis in | Lift kritis ex | Konsekuensi |
|---|---|---|---|
| 4 klep | 4,64 mm | 3,68 mm | klep buang butuh lift **lebih rendah** |
| 3 klep | 4,59 mm | 5,03 mm | klep buang butuh lift **lebih tinggi** |

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
LSA                         →   karakter dasar      →   lebar pita
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
