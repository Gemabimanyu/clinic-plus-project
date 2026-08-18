# ADVANCED ENGINE TUNING
## Metode Perhitungan Berbasis Kalibrasi

*Dokumentasi pembelajaran — disusun dari perhitungan dan simulasi nyata*

---

## DAFTAR ISI

**BAGIAN 0 — CARA MEMBACA BUKU INI**
- 0.1 Untuk siapa buku ini
- 0.2 Filosofi pokok
- 0.3 Notasi, satuan, dan penandaan kepercayaan
- 0.4 Kamus istilah — 6 kelompok, penjelasan rinci tiap istilah

**BAGIAN I — FONDASI**
- 1. Kenapa angka buku sering menyesatkan
- 2. Prinsip kalibrasi
- 3. Besaran pokok yang menentukan segalanya

**BAGIAN II — KEPALA SILINDER**
- 4. Klep dan batas geometri
- 5. Throat: pembatas yang sesungguhnya
- 6. Port: luas penampang dan kecepatan gas
- 7. Bentuk port
- 8. Lift kritis

**BAGIAN III — CAMSHAFT**
- 9. Empat kejadian dan urutannya
- 10. IVC dan kompresi dinamis
- 11. Durasi dari time-area
- 12. Overlap, LSA, dan ICL
- 13. Kelegaan klep-piston

**BAGIAN IV — KOMPRESI**
- 14. Statis, dinamis, dan efektif
- 15. Anggaran volume ruang bakar
- 16. Mengkalibrasi batas detonasi

**BAGIAN V — SALURAN MASUK**
- 17. Throttle body
- 18. Panjang runner dan tuning gelombang
- 19. Velocity stack, plenum, dan manifold

**BAGIAN VI — SALURAN BUANG**
- 20. Port dan header
- 21. Panjang header dan harmonik

**BAGIAN VII — BATAS MEKANIS**
- 22. Kecepatan dan percepatan piston
- 23. Rasio rod dan konsekuensinya

**BAGIAN VIII — PERBANDINGAN DUNIA**
- 24. F1, MotoGP, Pro Stock
- 25. Kenapa semua berkumpul di angka yang sama

**BAGIAN IX — CFD**
- 26. Cara kerja dan batasnya
- 27. Menyiapkan flowbench virtual
- 28. Jebakan yang mahal

**BAGIAN X — STUDI KASUS**
- 29. Mesin acuan: 199cc 2-klep drag
- 30. Build: 150cc 4-klep
- 31. Alternatif: Vespa iGet 3-klep

**LAMPIRAN**
- A. Rumus ringkas
- B. Daftar perkakas hitung
- C. Daftar periksa build
- D. Data terukur vs asumsi

---

# BAGIAN 0 — CARA MEMBACA BUKU INI

## 0.1 Untuk siapa buku ini

Buku ini untuk orang yang sudah bisa membangun mesin dan ingin berhenti menebak.

Bukan untuk pemula. Diasumsikan kamu sudah paham siklus 4-langkah, sudah pernah bongkar-pasang head, dan tahu apa itu noken as. Yang ditawarkan di sini adalah **cara menghitung**, bukan cara memasang.

Seluruh isinya berasal dari perhitungan yang benar-benar dijalankan pada satu kasus nyata: pengembangan head 4-klep 150cc untuk drag 500m, dikalibrasi ke mesin 199cc 2-klep yang sudah terbukti menempuh 500m dalam 15,4 detik dengan trap 158 km/h.

## 0.2 Filosofi pokok

Ada satu gagasan yang mendasari seluruh buku ini:

> **Mesin yang sudah terbukti jalan adalah sumber data yang lebih dipercaya daripada tabel di buku mana pun.**

Buku teks tuning ditulis dari populasi mesin tertentu — biasanya V8 Amerika, atau mesin mobil Eropa. Angka-angkanya benar untuk populasi itu. Untuk mesin kecil berputaran tinggi dengan CVT dan bahan bakar avgas, angka itu bisa meleset jauh.

Sepanjang buku ini akan berulang pola yang sama:

1. Ambil besaran tak-berdimensi dari mesin yang sudah terbukti
2. Skalakan ke mesin baru
3. Bandingkan dengan angka buku — kalau berbeda, **percayai mesinmu**

Bab 16 memuat contoh paling tajam: tabel oktan umum menyatakan kompresi dinamis di atas 12,5 mustahil dengan bensin. Mesin acuan dalam buku ini berjalan di 12,83 dengan bensol/avgas 100LL, tanpa masalah, selama bertahun-tahun.

## 0.3 Notasi, satuan, dan penandaan kepercayaan

**Satuan:** milimeter untuk panjang, mm² untuk luas, cc untuk volume, m/s untuk kecepatan, derajat crank untuk sudut, rpm untuk putaran.

**Singkatan:** dijelaskan lengkap di Bagian 0.4. Ringkasannya:

| Singkatan | Arti |
|---|---|
| CSA | *cross-sectional area* — luas penampang |
| MGV | *mean gas velocity* — kecepatan gas rata-rata |
| MPS | *mean piston speed* — kecepatan piston rata-rata |
| CR | *compression ratio* — rasio kompresi statis |
| DCR | *dynamic compression ratio* — rasio kompresi dinamis |
| IVO / IVC | *intake valve open / close* |
| EVO / EVC | *exhaust valve open / close* |
| BTDC / ATDC | sebelum / sesudah titik mati atas |
| BBDC / ABDC | sebelum / sesudah titik mati bawah |
| ICL / ECL | *intake / exhaust centerline* — puncak lobe |
| LSA | *lobe separation angle* |
| Cf | koefisien flow |
| K | koefisien rugi tekanan |

**Penandaan kepercayaan** — ini penting dan dipakai konsisten:

| Tanda | Arti |
|---|---|
| **[UKUR]** | Angka hasil pengukuran langsung. Dipercaya. |
| **[HITUNG]** | Diturunkan dari angka [UKUR] lewat perhitungan. Dipercaya sejauh asumsinya benar. |
| **[ASUMSI]** | Ditebak dari praktik lazim. **Harus diverifikasi.** |
| **[CFD]** | Dari simulasi. Bagus untuk membandingkan, lemah untuk angka mutlak. |

Kalau sebuah angka tidak diberi tanda, anggap [ASUMSI].

---

## 0.4 Kamus istilah

Bagian ini menjelaskan setiap istilah secara rinci, dikelompokkan menurut jenisnya. Baca sekali sekarang, lalu rujuk kembali saat dibutuhkan.

Tiap entri memuat: **satuan**, **rumus**, **diukur di mana**, **kenapa penting**, **rentang khas**, dan **kesalahpahaman yang umum terjadi**. Bagian terakhir itu yang paling sering menyelamatkan.

---

### KELOMPOK 1 — UKURAN DAN GEOMETRI

Besaran yang bisa kamu pegang dengan sigmat. Semuanya statis, tidak berubah saat mesin berputar.

---

#### CSA — *Cross-Sectional Area*
**Luas penampang saluran**

**Satuan:** mm²

**Rumus:**
```
Penampang bundar : CSA = π/4 × D²
Penampang oval   : CSA ≈ 0,92 × lebar × tinggi
```
Faktor 0,92 untuk bentuk superelips — di antara elips murni (0,785) dan kotak (1,00). Port hasil porting biasanya mendekati angka ini.

**Diukur di mana:** di **titik tersempit** sepanjang saluran, bukan di flange dan bukan di bowl. Titik tersempit inilah yang menentukan kecepatan gas dan menjadi pembatas.

Untuk port bercabang (4-klep), yang dipakai adalah CSA **runner bersama** sebelum pecah dua — bukan CSA tiap cabang.

**Kenapa penting:** CSA menentukan kecepatan gas, dan kecepatan gas menentukan pengisian silinder. Ini variabel desain port yang paling berpengaruh.

**Rentang khas:** untuk mesin balap kecil, CSA port isap berkisar 0,90–1,10 × luas throat.

**Kesalahpahaman yang umum:**

*Menyebut ukuran port dalam diameter, bukan luas.* Ini menyesatkan karena luas berskala dengan **kuadrat** diameter. Menaikkan port dari 28 ke 30 mm terdengar kecil (+7%), padahal luasnya naik **15%**. Selalu berpikir dalam mm², bukan mm.

*Mengukur di tempat yang salah.* Banyak orang mengukur di mulut flange karena itu yang paling mudah dijangkau. Padahal titik tersempit biasanya di dekat short-turn atau tepat sebelum bowl.

**Contoh dari buku ini:** mesin acuan punya port isap bundar Ø29,5 mm → CSA 683 mm². Build 4-klep dirancang 615–665 mm² dengan penampang oval 22,7 × 29,5 mm.

---

#### Throat
**Diameter dalam seat klep**

**Satuan:** mm untuk diameter, mm² untuk luas

**Rumus:**
```
A_throat = n_klep × π/4 × D_throat²
```

**Diukur di mana:** lubang paling sempit di dalam seat, tepat di bawah permukaan seat yang bersentuhan dengan klep. Bukan diameter klep, bukan diameter luar seat.

**Kenapa penting:** pada lift tinggi, throat adalah **pembatas sesungguhnya**. Membesarkan throat adalah satu-satunya perubahan yang menaikkan plafon flow head — bentuk port tidak bisa melakukannya.

**Rentang khas:** dinyatakan sebagai rasio terhadap diameter klep.

| Rasio throat/klep | Keterangan |
|---|---|
| 0,85–0,88 | konservatif, umum di buku |
| 0,88–0,92 | balap lazim |
| 0,92–0,94 | agresif |
| > 0,94 | seat sangat tipis, berisiko |

Batasnya adalah lebar seat: `lebar = (D_klep − D_throat) / 2`. Di bawah 0,7 mm berisiko, terutama sisi buang.

**Kesalahpahaman yang umum:**

*Mengira aturan 0,85–0,90 itu hukum mati.* Mesin acuan dalam buku ini jalan di **0,935** selama bertahun-tahun pada kompresi 16:1. Yang menentukan bukan rasionya, tapi lebar seat dalam milimeter dan kualitas materialnya.

*Menyamakan sisi isap dan buang.* Sisi buang selalu butuh seat lebih lebar, karena seat itulah jalan panas klep buang keluar.

---

#### Bore, Stroke, Rod
**Diameter silinder, panjang langkah, panjang stang piston**

**Satuan:** mm

**Rumus turunan:**
```
Kapasitas     : Vd = π/4 × bore² × stroke × n_silinder
Luas piston   : A_p = π/4 × bore²
Rasio rod     : R = panjang_rod / stroke
```

**Kenapa penting:**

**Bore** menentukan berapa besar klep yang muat — dan itu plafon napas mesin. Bore besar juga memperpanjang jalur api, yang menurunkan toleransi detonasi.

**Stroke** menentukan kecepatan piston pada rpm tertentu. Stroke pendek = rpm tinggi lebih murah secara mekanis. Ini rahasia F1: stroke 39,8 mm membuat 19.000 rpm terasa seperti 12.000 rpm di mesin berstroke 58 mm.

**Rod** mempengaruhi percepatan piston dan side thrust. Efeknya ke kompresi dinamis kecil.

**Rentang khas rasio rod:**

| Rasio | Keterangan |
|---|---|
| < 1,6 | sangat pendek |
| 1,6–1,75 | pendek, khas mesin kecil |
| 1,75–1,9 | umum |
| > 1,9 | panjang, khas mesin balap besar |

**Kesalahpahaman yang umum:**

*Mengira rod panjang selalu lebih baik.* Rod pendek memang menaikkan side thrust dan percepatan puncak, tapi juga membuat piston menjauh dari TDC lebih cepat — yang justru **melonggarkan kelegaan klep** dan **memperpendek waktu untuk detonasi berkembang**.

---

### KELOMPOK 2 — KECEPATAN DAN ALIRAN

Besaran yang muncul hanya saat mesin berputar. Semuanya bergantung rpm.

---

#### MPS — *Mean Piston Speed*
**Kecepatan piston rata-rata**

**Satuan:** m/s

**Rumus:**
```
MPS = 2 × stroke[m] × rpm / 60
```
Faktor 2 karena piston menempuh satu stroke naik dan satu stroke turun tiap putaran.

**Kenapa penting:** ini **indikator umur mesin** paling sederhana dan paling berguna. Semua beban mekanis — inersia, gesekan, tegangan rod — berskala dengan besaran ini.

MPS juga jadi satu dari dua faktor yang menentukan kecepatan gas (lihat MGV).

**Rentang khas:**

| MPS | Keterangan |
|---|---|
| < 20 m/s | aman, bisa harian |
| 20–22 | tinggi, umur pendek tapi wajar untuk drag |
| 22–24 | sangat tinggi, butuh part serius |
| 24–26 | ekstrem |
| 30+ | Pro Stock, mesin sekali pakai |

**Kesalahpahaman yang umum:**

*Mengira MPS adalah kecepatan puncak piston.* Bukan. Kecepatan **sesaat** puncak terjadi sekitar 70–80° dari TDC dan besarnya sekitar **1,6× MPS**. MPS adalah rata-rata sepanjang stroke.

*Membandingkan rpm antar mesin tanpa memperhitungkan stroke.* Mesin 19.000 rpm berstroke 39,8 mm (F1 V10, MPS 25,2) sebenarnya **lebih santai** secara mekanis daripada mesin 12.000 rpm berstroke 58 mm... tidak, keduanya hampir sama (23,2). Itu justru poinnya: **rpm sendirian tidak berarti apa-apa.** Bandingkan MPS-nya.

**Contoh:** mesin acuan pada 11.250 rpm (stroke 64) memberi MPS 24,0 m/s. Build baru pada 12.000 rpm (stroke 58) memberi 23,2 m/s — **lebih rendah**, walau rpm-nya 750 lebih tinggi.

---

#### MGV — *Mean Gas Velocity*
**Kecepatan gas rata-rata**

**Satuan:** m/s

**Rumus:**
```
MGV = (luas piston / CSA) × MPS
```

**Diukur di mana — INI PENTING:** ada dua konvensi yang beredar, dan angkanya berbeda jauh.

| Konvensi | CSA yang dipakai | Nilai khas |
|---|---|---|
| **Di port** | CSA port di titik tersempit | 90–115 m/s |
| **Di throat** | luas throat | 95–135 m/s |

Buku ini memakai **konvensi port** kecuali disebut lain. Kalau membandingkan angka dengan sumber lain, **pastikan dulu konvensinya sama** — kalau tidak, itu apel versus jeruk.

**Kenapa penting:** MGV menentukan **momentum muatan** yang masuk silinder. Momentum itu yang terus mengisi silinder bahkan setelah piston melewati BDC — inilah efek ram yang menaikkan efisiensi volumetrik. Momentum yang sama juga menggerakkan gelombang tekanan untuk tuning.

Terlalu rendah: momentum tidak cukup, pengisian lemah.
Terlalu tinggi: restriksi mencekik, rugi tekanan melonjak (rugi berskala dengan v²).

**Rentang khas (konvensi port):**

| MGV | Keterangan |
|---|---|
| 70–85 m/s | jalanan, torsi bawah |
| 85–100 | serbaguna / balap ringan |
| 100–115 | balap, putaran atas |
| > 120 | sangat agresif, restriksi mulai terasa |

**Kesalahpahaman yang umum:**

*Mengira mengecilkan throttle body menaikkan MGV di port.* **Tidak.** MGV di port ditentukan oleh CSA port. Debit sama, luas sama, kecepatan sama. Diameter TB tidak punya cara mempengaruhinya — yang naik cuma kecepatan di dalam TB itu sendiri, dan kecepatan di situ tidak melakukan pekerjaan apa pun.

*Mengira mesin besar butuh kecepatan gas berbeda.* Kalau semua proporsi diskalakan ke bore, **bore hilang dari persamaan**. F1 3 liter dan mesin 150cc dengan proporsi sama punya MGV identik. Ini dibahas tuntas di Bab 25.

---

#### Cf — Koefisien Flow
**Perbandingan aliran nyata terhadap aliran teoretis**

**Satuan:** tak berdimensi (0 sampai 1)

**Rumus:**
```
Cf = Q_nyata / (A_acuan × √(2Δp/ρ))
```

**Diukur terhadap apa — INI PENTING:** Cf tidak berarti apa-apa tanpa menyebut luas acuannya. Tiga konvensi beredar:

| Acuan | Nilai khas head bagus |
|---|---|
| Luas **throat** | 0,55–0,70 |
| Luas **payung klep** | 0,45–0,55 |
| Luas **tirai** pada lift tertentu | bervariasi |

Buku ini selalu memakai **luas throat**.

**Kenapa penting:** Cf memisahkan "berapa besar lubangnya" dari "seberapa baik bentuknya". Dua head dengan throat sama tapi Cf berbeda 10% akan berbeda tenaga 10%.

Cf juga berguna sebagai **penjaga kewarasan** di simulasi: nilai di luar 0,45–0,90 hampir pasti menandakan ada yang salah secara struktural, bukan sekadar desain jelek.

**Rentang khas:**

| Cf (acuan throat) | Keterangan |
|---|---|
| < 0,50 | jelek, ada masalah |
| 0,55 | standar pabrikan |
| 0,62 | porting bagus |
| 0,70 | porting sangat bagus |
| 0,85–0,95 | saluran tanpa klep (port telanjang) |

**Kesalahpahaman yang umum:**

*Membandingkan Cf tanpa menyamakan acuan.* Cf 0,85 dengan acuan throat dan Cf 0,85 dengan acuan payung klep adalah dua head yang sangat berbeda.

*Mengira Cf head lengkap bisa mendekati 0,9.* Tidak bisa. Klep dan seat sendiri sudah memakan banyak. Cf 0,85+ hanya untuk saluran tanpa klep.

**Contoh dari buku ini:** simulasi port telanjang memberi Cf 0,849. Head lengkap dengan klep di lift 9 mm diperkirakan turun ke 0,55–0,65.

---

#### K — Koefisien Rugi Tekanan
**Ukuran seberapa banyak energi hilang**

**Satuan:** tak berdimensi

**Rumus:**
```
K = (v_teoretis / v_nyata)² − 1
```
atau, kalau menghitung rugi dari kecepatan:
```
Δp_rugi = K × ½ × ρ × v²
```

**Kenapa penting:** K memungkinkan **membandingkan** rugi dari komponen berbeda pada skala yang sama. Rugi tikungan, rugi mulut, rugi throttle body — semuanya bisa dinyatakan dalam K dan langsung dibandingkan.

**Rentang khas:**

| Komponen | K |
|---|---|
| Pipa lurus mulus 70 mm | ~0,07 |
| Mulut bermulut lonceng (bellmouth) | 0,05 |
| Mulut rata bertepi tajam | 0,5 |
| Mulut menonjol ke dalam plenum | 0,8–1,0 |
| Tikungan port 37° radius wajar | 0,4 |
| Butterfly throttle body di WOT | 0,25 |

**Kesalahpahaman yang umum:**

*Menjumlahkan K dari komponen berbeda tanpa memperhatikan acuan kecepatannya.* K selalu dirujuk ke tekanan dinamik di suatu titik. Rugi TB dirujuk ke kecepatan di TB, rugi port ke kecepatan di throat. Menjumlahkannya butuh konversi.

**Contoh dari buku ini:** rugi port 2343 Pa vs rugi TB 559 Pa pada mesin yang sama. Port mendominasi 4:1 — artinya mengutak-atik TB itu mengurus 19% dari masalah.

---

#### VE — *Volumetric Efficiency*
**Efisiensi volumetrik**

**Satuan:** fraksi atau persen

**Definisi:** perbandingan massa udara yang benar-benar terjebak di silinder terhadap massa udara yang mengisi kapasitas silinder pada kondisi atmosfer.

**Kenapa penting:** VE adalah **hasil akhir** dari semua yang dibahas di buku ini. Port, cam, knalpot, runner — semuanya bekerja untuk menaikkan VE.

**Rentang khas:**

| VE | Keterangan |
|---|---|
| 0,75–0,85 | mesin standar |
| 0,85–0,95 | mesin diporting |
| 0,95–1,05 | mesin balap tertala baik |
| > 1,05 | tuning gelombang bekerja sangat baik |

VE di atas 1,00 dimungkinkan karena momentum dan gelombang tekanan mendorong lebih banyak muatan masuk daripada yang bisa dilakukan tekanan atmosfer sendirian.

---

### KELOMPOK 3 — KOMPRESI

Dua angka yang sering tertukar, dan salah satunya jauh lebih penting.

---

#### CR — *Compression Ratio*
**Rasio kompresi statis**

**Satuan:** rasio, ditulis seperti 14:1

**Rumus:**
```
CR = (Vd + Vc) / Vc
```
dengan Vd = kapasitas satu silinder, Vc = volume ruang bakar total di TDC.

**Vc mencakup apa saja — INI SERING SALAH:**
```
Vc = pent-roof + gasket + deck clearance + kantong klep − dome piston
```

**Kenapa penting:** CR menentukan **rasio ekspansi**, dan rasio ekspansi menentukan efisiensi termal:
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

*Melupakan kantong klep.* Ini kesalahan paling mahal. Empat kantong klep sedalam 2,7 mm menambah 1,58 cc — pada target Vc 11,50 cc, itu **14% anggaran**. Dengan overlap besar dan kantong 4 mm, porsinya naik jadi 20%.

Akibatnya nyata: head dipapas untuk mengejar kompresi, lalu kantong klep digerus untuk cam baru, dan sebagian kompresi yang baru didapat langsung hilang lagi.

**Urutan yang benar:** tentukan cam dulu → hitung kantong klep → baru hitung dome atau papasan yang dibutuhkan.

*Mengira CR statis menentukan detonasi.* Tidak. Yang menentukan adalah DCR.

---

#### DCR — *Dynamic Compression Ratio*
**Rasio kompresi dinamis**

**Satuan:** rasio

**Rumus:**
```
DCR = V_saat_IVC / Vc
```
atau bentuk yang lebih berguna, karena linear terhadap CR:
```
DCR = 1 + (V_sapu_saat_IVC / Vd) × (CR − 1)
```

V_saat_IVC dihitung dari posisi piston saat klep isap benar-benar menutup:
```
s(θ) = r(1 − cos θ) + L − √(L² − (r sin θ)²)     dengan θ = 180° + IVC_ABDC
```

**Kenapa penting:** **DCR yang menentukan detonasi, bukan CR.** Kompresi baru mulai terjadi setelah klep isap menutup; sebelum itu muatan masih bisa terdorong balik keluar.

**Rentang khas:** ini bergantung bahan bakar, dan tabel umum terlalu konservatif. Lihat Bab 16.

**Kesalahpahaman yang umum:**

*Mengira DCR berubah dengan rpm.* **Tidak.** DCR murni geometri + timing. Tidak ada rpm dalam rumusnya. Yang berubah dengan rpm adalah efisiensi penjebakan, dan itu besaran lain.

*Mengira CR tinggi selalu berarti DCR tinggi.* Mesin acuan berjalan CR 16:1 tapi DCR-nya 12,83 karena IVC-nya sangat telat (63° ABDC). Sementara build 4-klep dengan CR 14:1 dan IVC 52,8° memberi DCR 12,07 — **lebih rendah walau CR-nya lebih rendah juga**, karena IVC-nya lebih awal.

*Melupakan bahwa DCR, rpm, dan bahan bakar itu satu paket.* Menaikkan rpm sasaran memaksa durasi lebih panjang → IVC lebih telat → DCR turun. Kamu tidak bisa memilih ketiganya bebas.

---

### KELOMPOK 4 — REFERENSI SUDUT CRANK

Semua timing cam dinyatakan dalam derajat putaran crankshaft, dirujuk ke salah satu dari dua titik mati.

---

#### TDC dan BDC
**Titik mati atas dan titik mati bawah**

**TDC** — *Top Dead Center* — piston di posisi paling atas.
**BDC** — *Bottom Dead Center* — piston di posisi paling bawah.

**Yang sering membingungkan:** dalam satu siklus 4-langkah, piston melewati TDC **dua kali**:

| | Kapan | Sebutan |
|---|---|---|
| TDC pertama | akhir kompresi | **firing TDC** / TDC kompresi |
| TDC kedua | akhir buang | **overlap TDC** / TDC buang |

Timing cam selalu dirujuk ke **overlap TDC** — TDC di mana klep isap mulai membuka dan klep buang belum menutup.

Kalau ada yang bilang "overlap di TDC", yang dimaksud adalah TDC ini.

---

#### BTDC / ATDC
**Sebelum / sesudah titik mati atas**

**BTDC** — *Before Top Dead Center*. Sudut diukur **mundur** dari TDC.
**ATDC** — *After Top Dead Center*. Sudut diukur **maju** dari TDC.

**Dipakai untuk:** IVO (biasanya BTDC), EVC (biasanya ATDC), ICL (selalu ATDC), pengapian (selalu BTDC).

**Cara membacanya:** "IVO 28° BTDC" berarti klep isap mulai membuka 28 derajat putaran crank **sebelum** piston sampai di TDC.

---

#### BBDC / ABDC
**Sebelum / sesudah titik mati bawah**

**BBDC** — *Before Bottom Dead Center*.
**ABDC** — *After Bottom Dead Center*.

**Dipakai untuk:** EVO (biasanya BBDC), IVC (biasanya ABDC).

**Cara membacanya:** "IVC 53° ABDC" berarti klep isap menutup 53 derajat **setelah** piston melewati BDC.

**Kenapa IVC selalu ABDC:** karena momentum muatan masih mendorong masuk walau piston sudah mulai naik. Menutup klep tepat di BDC akan membuang momentum itu.

---

### KELOMPOK 5 — KEJADIAN KATUP

Empat kejadian yang mendefinisikan sebuah camshaft.

---

#### IVO / IVC — *Intake Valve Open / Close*
**Klep isap membuka / menutup**

**Satuan:** derajat crank. IVO biasanya BTDC, IVC biasanya ABDC.

**IVO — kenapa penting:** menentukan **overlap**. IVO lebih awal berarti overlap lebih besar, pembilasan lebih kuat, tapi juga risiko muatan segar lolos ke knalpot pada rpm rendah.

**IVC — kenapa penting:** ini **kejadian terpenting di seluruh camshaft**. Menentukan:
- Kompresi dinamis (dan karenanya kebutuhan bahan bakar)
- RPM di mana efisiensi penjebakan memuncak
- Karakter torsi bawah versus atas

**Rentang khas:**

| | Jalanan | Balap |
|---|---|---|
| IVO | 5–15° BTDC | 25–45° BTDC |
| IVC | 35–50° ABDC | 50–75° ABDC |

**Kesalahpahaman yang umum — DAN INI YANG PALING SERING:**

*Membandingkan timing tanpa menyebut pada lift berapa diukur.* Ini sumber kekacauan terbesar dalam diskusi cam.

| Titik ukur | Nama umum | Selisih durasi |
|---|---|---|
| 0,15 mm | *seat-to-seat* | paling besar |
| 1,00 mm | **@1mm** — standar Eropa/Asia | acuan buku ini |
| 1,27 mm (0,050") | **@0.050"** — standar Amerika | ~10–20° lebih kecil dari seat-to-seat |

Cam yang sama bisa disebut "300 derajat" (seat-to-seat) atau "260 derajat" (@0.050"). **Selalu tanyakan pada lift berapa.**

Buku ini memakai **@1mm** secara konsisten.

---

#### EVO / EVC — *Exhaust Valve Open / Close*
**Klep buang membuka / menutup**

**Satuan:** derajat crank. EVO biasanya BBDC, EVC biasanya ATDC.

**EVO — kenapa penting:** menentukan kapan *blowdown* dimulai. Membuka terlalu awal membuang kerja ekspansi yang masih tersisa; membuka terlalu telat membuat piston harus mendorong gas keluar melawan tekanan (rugi pemompaan).

EVO juga titik lahir gelombang tekanan yang dipakai untuk tuning knalpot (Bab 21).

**EVC — kenapa penting:** bersama IVO menentukan overlap.

**Rentang khas:**

| | Jalanan | Balap |
|---|---|---|
| EVO | 35–50° BBDC | 50–75° BBDC |
| EVC | 5–15° ATDC | 25–45° ATDC |

**Kesalahpahaman yang umum:**

*Mengira sisi buang selalu butuh durasi lebih panjang.* Tergantung **rasio throat ex/in**. Kalau rasionya di sekitar 0,67–0,72, cam simetris justru benar. Mesin acuan berjalan simetris 281/281 pada rasio 0,671.

Aturan praktisnya:

| Rasio throat ex/in | Tindakan |
|---|---|
| < 0,63 | tambah 8–12° durasi ex |
| 0,63–0,72 | cam simetris aman |
| > 0,72 | sisi buang lega, simetris atau kurangi |

---

#### Durasi
**Lamanya klep terbuka**

**Satuan:** derajat crank

**Rumus:**
```
durasi_in = IVO_BTDC + 180 + IVC_ABDC
durasi_ex = EVO_BBDC + 180 + EVC_ATDC
```

**Kenapa penting:** durasi menentukan **jendela waktu** yang tersedia untuk mengalirkan muatan. Dipadukan dengan luas throat, ini yang disebut *time-area*.

**Cara menentukannya dengan benar:**
```
durasi_baru = durasi_acuan × (A_thr_acuan / A_thr_baru)
                            × (Vd_baru / Vd_acuan)
                            × (rpm_baru / rpm_acuan)
```

**Kesalahpahaman yang umum:**

*Mengira rpm tinggi selalu butuh durasi panjang.* Yang benar: rpm tinggi **dan luas klep tetap** butuh durasi panjang. Build 4-klep dalam buku ini butuh durasi **lebih pendek** (261° vs 281°) walau rpm-nya lebih tinggi (12.000 vs 10.000), karena head-nya bernapas 29% lebih lega per cc.

---

#### Overlap
**Periode kedua klep terbuka bersamaan**

**Satuan:** derajat crank

**Rumus:**
```
overlap = IVO_BTDC + EVC_ATDC
```

**Kenapa penting:** selama overlap, aliran gas buang yang keluar bisa **menarik** muatan segar masuk. Ini pembilasan (*scavenging*) — cara membuang sisa gas buang dan mengisi silinder lebih penuh.

Terlalu kecil: sisa gas buang banyak tertinggal, mengencerkan muatan.
Terlalu besar: muatan segar lolos langsung ke knalpot pada rpm rendah, mesin brebet dan boros.

**Rentang khas:**

| Overlap | Karakter |
|---|---|
| 10–30° | jalanan, idle halus |
| 40–70° | balap, idle kasar |
| 70–110° | drag, tidak bisa idle stasioner |

**Cara menskalakannya dengan benar:** yang dipertahankan adalah **luas tirai overlap per cc**, bukan sudut dan bukan lift:
```
luas_per_cc = n_klep × π × D_klep × lift_di_TDC / kapasitas
```

**Kesalahpahaman yang umum:**

*Menskalakan lift overlap lewat diameter klep saja.* Untuk head 4-klep ini keliru dua kali lipat, karena dua klep isap memberi luas tirai jauh lebih besar per milimeter lift dibanding satu klep besar.

*Ambiguitas angka "lift overlap".* Angka yang beredar di bengkel sering tidak jelas: lift satu klep, atau gabungan in + ex? Contoh dari buku ini: angka "3,6 mm" ternyata **gabungan** (1,83 mm per klep). Kalau ditafsirkan sebagai lift satu klep, target overlap jadi dua kali terlalu besar.

**Cara memastikannya:** hitung dari sudut, bukan dari angka lift yang disebut. Sudut tidak ambigu.

---

### KELOMPOK 6 — KARAKTER CAMSHAFT

Besaran yang menggambarkan "kepribadian" sebuah camshaft.

---

#### ICL / ECL — *Intake / Exhaust Centerline*
**Titik puncak lobe**

**Satuan:** derajat crank. **ICL selalu ATDC, ECL selalu BTDC** — perhatikan arah acuannya berbeda.

**Rumus:**
```
ICL = durasi_in / 2 − IVO_BTDC        (ATDC)
ECL = durasi_ex / 2 − EVC_ATDC        (BTDC)
```

**Kenapa penting:** ICL menentukan **di mana cam ditempatkan** relatif terhadap piston. Ini yang diubah saat kamu memajukan atau memundurkan cam dengan *adjustable sprocket*.

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

**Kesalahpahaman yang umum:**

*Mengira ICL dan LSA adalah hal yang sama.* Bukan. LSA adalah sifat **cam-nya** (sudah tergerinda, tidak bisa diubah). ICL bisa diubah dengan memutar sprocket. Lihat entri LSA.

*Lupa bahwa acuan ICL dan ECL berlawanan arah.* ICL diukur ATDC, ECL diukur BTDC. Cam simetris punya ICL = ECL secara angka, tapi arahnya berbeda.

---

#### LSA — *Lobe Separation Angle*
**Sudut pemisahan lobe**

**Satuan:** derajat **camshaft**, bukan derajat crank. (Pada mesin 4-tak, cam berputar setengah kecepatan crank — tapi LSA konvensionalnya ditulis dalam derajat cam. Angka yang beredar sudah dalam konvensi ini.)

**Rumus:**
```
LSA = (ICL + ECL) / 2
```

**Kenapa penting:** LSA menentukan **karakter dasar** cam — seberapa tajam pita tenaganya.

| LSA | Karakter |
|---|---|
| 98–104° | overlap besar, pita sempit, drag/balap |
| 104–110° | seimbang |
| 110–116° | overlap kecil, pita lebar, jalanan |

**Perbedaan pokok dengan ICL — INI YANG PALING SERING TERTUKAR:**

| | LSA | ICL |
|---|---|---|
| Sifat | **tergerinda di cam** | **posisi pemasangan** |
| Bisa diubah? | **tidak**, harus ganti cam | ya, dengan adjustable sprocket |
| Mengubah apa | karakter dasar, overlap | keseimbangan bawah/atas |

Kalau cam-mu LSA 102° dan kamu ingin overlap lebih kecil, memutar sprocket **tidak akan membantu** — memutar sprocket menggeser ICL dan ECL bersama-sama, LSA tetap. Kamu harus mengganti cam.

**Contoh dari buku ini:** cam acuan LSA 102,5°, simetris tanpa maju/mundur (ICL = ECL = 102,5°). Cam yang dirancang untuk mesin baru juga jatuh di LSA 102,5° — hasil dari dua penskalaan independen yang bertemu, bukan disamakan dengan sengaja.

---

#### Lift dan Lift Kritis
**Tinggi bukaan klep, dan titik di mana throat mengambil alih**

**Satuan:** mm

**Rumus lift kritis:**
```
lift_kritis = A_throat / (n_klep × π × D_klep)
```

**Artinya:** di bawah lift kritis, **luas tirai** yang membatasi aliran. Di atasnya, **throat** yang membatasi — menambah lift hampir tidak menambah flow puncak.

**Kenapa mesin balap tetap memakai lift jauh di atas lift kritis:** karena yang dibayar bukan flow puncak, tapi **time-area** — integral luas terhadap waktu. Menahan klep tinggi lebih lama mengisi silinder lebih banyak walau flow puncaknya tidak bertambah.

**Rentang khas kelipatan lift terhadap lift kritis:**

| Kelipatan | Keterangan |
|---|---|
| 1,0–1,3× | jalanan |
| 1,5–2,0× | balap |
| 2,0–2,5× | drag, beban valvetrain tinggi |

**Kesalahpahaman yang umum:**

*Mempercayai aturan "lift maksimum berguna = 0,25 × diameter klep".* Aturan ini benar untuk **flow puncak steady**, salah untuk mesin balap. Mesin acuan berjalan di 1,59× lift kritis pada sisi isap dan 2,07× pada sisi buang.

*Menyamakan kebutuhan lift sisi isap dan buang.* Tergantung arsitektur:

| Arsitektur | Lift kritis in | Lift kritis ex | Konsekuensi |
|---|---|---|---|
| 4-klep (2 in, 2 ex) | 4,64 mm | 3,68 mm | klep buang butuh lift **lebih rendah** |
| 3-klep (2 in, 1 ex) | 4,59 mm | 5,03 mm | klep buang butuh lift **lebih tinggi** |

Sebabnya: satu klep besar punya keliling total lebih kecil daripada dua klep kecil berluas sama.

---

#### Time-Area
**Integral luas bukaan terhadap waktu**

**Satuan:** proporsional, biasanya dipakai sebagai perbandingan

**Rumus praktis:**
```
time-area ∝ (A_throat × durasi) / (kapasitas × rpm)
```

**Kenapa penting:** ini **besaran yang benar-benar menentukan pengisian**, bukan durasi sendirian dan bukan lift sendirian. Time-area adalah "jendela aliran per siklus per cc".

**Cara memakainya:** untuk menskalakan cam antar mesin, pertahankan time-area — lalu hitung durasi yang dibutuhkan.

**Kesalahpahaman yang umum:**

*Membandingkan durasi antar mesin berbeda.* Durasi 280° di mesin dengan throat kecil sama sekali tidak setara dengan 280° di mesin dengan throat besar. Yang setara adalah time-area-nya.

---

### RINGKASAN HUBUNGAN ANTAR ISTILAH

Bagaimana semuanya saling terkait:

```
GEOMETRI                    →   ALIRAN                  →   HASIL
─────────────────────────────────────────────────────────────────
bore, stroke                →   MPS                     →   umur mesin
CSA, luas piston, MPS       →   MGV                     →   pengisian
throat, bentuk port         →   Cf, K                   →   flow
─────────────────────────────────────────────────────────────────
CAM                         →   EFEK                    →   KONSEKUENSI
─────────────────────────────────────────────────────────────────
IVO + EVC                   →   overlap                 →   pembilasan
IVC                         →   DCR                     →   bahan bakar
durasi × A_throat           →   time-area               →   rpm puncak
ICL                         →   keseimbangan            →   bawah vs atas
LSA                         →   karakter dasar          →   lebar pita
lift vs lift kritis         →   time-area               →   beban valvetrain
─────────────────────────────────────────────────────────────────
KOMPRESI                    →   EFEK
─────────────────────────────────────────────────────────────────
CR                          →   rasio ekspansi          →   efisiensi termal
DCR                         →   tekanan puncak          →   batas detonasi
```

**Tiga rantai sebab-akibat yang paling penting diingat:**

1. **CSA port → MGV → pengisian.** Bukan diameter TB.
2. **IVC → DCR → bahan bakar.** Bukan CR statis.
3. **A_throat × durasi → time-area → rpm puncak.** Bukan durasi sendirian.

---

# BAGIAN I — FONDASI

## 1. Kenapa angka buku sering menyesatkan

### 1.1 Contoh nyata: rasio throat

Buku porting umum menyatakan diameter dalam seat klep (throat) sebaiknya 0,85–0,90 dari diameter klep. Lebih dari itu, katanya, seat jadi terlalu tipis dan tidak tahan panas.

Mesin acuan dalam buku ini: klep isap 31 mm, throat 29 mm. Rasionya **0,935** — jauh di atas batas buku. Mesin itu jalan bertahun-tahun di kompresi 16:1.

Konsekuensi dari mempercayai buku: head 4-klep baru dirancang dengan throat 19,5 mm pada klep 22 mm (rasio 0,886). Setelah dikalibrasi ke praktik yang sudah terbukti, throat bisa dibuka ke **20,2 mm** — menaikkan plafon flow **7,4%** tanpa risiko baru.

Tujuh persen itu setara 3 HP dari 41 HP. Hilang, hanya karena mempercayai tabel.

### 1.2 Contoh kedua: kecepatan di throttle body

Aturan umum: kecepatan puncak di throttle body sebaiknya sekitar 105 m/s.

Mesin acuan: throttle body 38 mm, kecepatan puncak terhitung **61 m/s**. Jauh di bawah "aturan".

Kalau aturan itu diikuti, throttle body mesin baru akan disarankan 28 mm. Setelah dikalibrasi ke mesin nyata, angkanya **36 mm**. Selisih 8 mm pada diameter berarti selisih 39% pada luas.

Kenapa aturan umum meleset? Karena ditulis untuk mesin bertransmisi gigi yang butuh respons part-throttle. Pada CVT yang selalu WOT, respons tidak relevan; yang dikejar cuma restriksi minimum.

### 1.3 Kapan buku tetap benar

Bukan berarti semua tabel salah. Yang perlu dipahami adalah **untuk populasi mesin apa tabel itu ditulis**.

Aturan kecepatan gas di port 90–110 m/s, misalnya, ternyata **benar** — mesin acuan berjalan di 97 m/s, dan F1 di 90–95 m/s. Itu aturan yang berlaku universal, karena diturunkan dari batas fisika yang sama untuk semua orang (Bab 25).

Bedakan:
- Aturan yang berasal dari **fisika universal** → biasanya benar
- Aturan yang berasal dari **kebiasaan populasi tertentu** → verifikasi dulu

## 2. Prinsip kalibrasi

### 2.1 Prosedurnya

**Langkah 1 — Kumpulkan data mesin acuan.** Yang minimum diperlukan:

- Bore, stroke, panjang rod
- Diameter klep isap dan buang
- Diameter dalam seat (throat) isap dan buang
- CSA port di titik tersempit
- Timing cam lengkap (IVO, IVC, EVO, EVC) dan lift maksimum
- Kompresi statis
- Bahan bakar
- Diameter throttle body
- Diameter port buang, diameter dalam header, panjang header
- RPM tenaga puncak
- Hasil terukur (waktu dan trap speed, atau dyno)

**Langkah 2 — Hitung besaran tak-berdimensi.** Yang berguna:

- Luas klep isap / luas bore
- Throat / diameter klep
- CSA port / luas throat
- Kecepatan gas di port pada rpm puncak
- Kompresi dinamis
- Time-area cam
- Luas tirai overlap per cc

**Langkah 3 — Skalakan ke mesin baru.** Pertahankan besaran tak-berdimensi, hitung ukuran mutlaknya.

**Langkah 4 — Periksa silang.** Kalau dua metode penskalaan berbeda memberi jawaban yang mirip, kepercayaan naik tajam. Kalau berbeda jauh, salah satu asumsimu keliru — cari tahu yang mana sebelum lanjut.

### 2.2 Contoh pemeriksaan silang yang berhasil

Menentukan CSA port mesin baru, dua jalur independen:

**Jalur A — samakan kecepatan gas.** Mesin acuan berjalan 97 m/s di port pada rpm puncak. Untuk mesin baru pada 12.000 rpm, CSA yang memberi 97 m/s adalah **615 mm²**.

**Jalur B — samakan rasio port/throat.** Mesin acuan punya rasio 1,035. Dikalikan luas throat mesin baru (641 mm²) menghasilkan **663 mm²**.

Selisih 7,8%. Cukup dekat untuk dipercaya, cukup jauh untuk jadi rentang desain yang jujur: **615–665 mm²**.

Bandingkan dengan hasil sebelum data throat sebenarnya diketahui: jalur A memberi 427 mm² karena throat mesin acuan ditebak 0,86 (padahal 0,935). Selisihnya 40% — dan seluruhnya berasal dari satu asumsi yang salah.

**Pelajaran:** pemeriksaan silang tidak cuma menaikkan kepercayaan, tapi juga **mendeteksi asumsi busuk**.

### 2.3 Contoh pemeriksaan silang yang menyelamatkan

Menentukan durasi cam, dua jalur:

**Jalur A — time-area.** Menghasilkan durasi 261° dan, setelah dibagi menurut target overlap, ICL **102,5° ATDC**.

**Jalur B — timing cam acuan yang diurai.** ICL cam acuan = **102,5° ATDC**.

Identik. Dua perhitungan yang sama sekali tidak berbagi rumus bertemu di angka yang sama. Itu tanda kuat bahwa penskalaannya waras.

## 3. Besaran pokok yang menentukan segalanya

Kalau harus memilih lima angka saja untuk memahami sebuah mesin, ini pilihannya.

### 3.1 Luas klep isap / luas bore

```
rasio = (n_klep × π/4 × D_klep²) / (π/4 × Bore²)
      = n_klep × (D_klep / Bore)²
```

Ini **plafon geometri** mesin. Tidak bisa dilampaui tanpa mengganti head atau bore.

| Arsitektur | Rasio khas |
|---|---|
| 2-klep bore kecil | 0,24 |
| 2-klep bore besar (Pro Stock) | 0,30 |
| 3-klep | 0,26 |
| 4-klep bagus | 0,30–0,35 |
| F1 / MotoGP | 0,29–0,30 |

Yang mengejutkan: F1 dan Pro Stock berada di angka yang sama, 0,297. Batas geometrinya universal — dua lingkaran tidak bisa dijejalkan lebih rapat ke dalam satu bore.

### 3.2 Mean piston speed

```
MPS = 2 × stroke[m] × rpm / 60
```

Ini **plafon mekanis**. Menentukan berapa lama mesinmu bertahan.

| MPS | Keterangan |
|---|---|
| < 20 m/s | aman, bisa harian |
| 20–22 | tinggi, umur pendek tapi wajar untuk drag |
| 22–24 | sangat tinggi, butuh part serius |
| 24–26 | ekstrem |
| 30+ | Pro Stock, mesin sekali pakai |

### 3.3 Kecepatan gas di port

```
MGV = (luas piston / CSA port) × MPS
```

Ini yang **menentukan pengisian silinder**. Terlalu rendah, momentum tidak cukup untuk terus mengisi setelah BDC. Terlalu tinggi, restriksi mencekik.

Rentang sehat: **90–115 m/s** pada rpm tenaga puncak.

Sifat menarik: kalau semua proporsi diskalakan ke bore, **bore hilang dari persamaan**. Mesin 3 liter dan 150cc dengan proporsi sama punya kecepatan port identik.

### 3.4 Kompresi dinamis

```
DCR = (V_saat_IVC + V_ruang_bakar) / V_ruang_bakar
```

Ini yang **menentukan detonasi** — bukan kompresi statis. Dibahas penuh di Bab 14.

### 3.5 Time-area

```
time-area ∝ (luas throat × durasi) / (kapasitas × rpm)
```

Ini **jendela aliran per siklus per cc**. Menentukan durasi cam yang dibutuhkan. Dibahas di Bab 11.

---

# BAGIAN II — KEPALA SILINDER

## 4. Klep dan batas geometri

### 4.1 Berapa besar klep yang muat

Diameter klep dibatasi oleh bore, dan proporsinya cukup stabil antar arsitektur:

| Arsitektur | Klep isap (× bore) | Klep buang (× bore) |
|---|---|---|
| 2-klep bore kecil | 0,49 | 0,43 |
| 2-klep bore besar | 0,545 | 0,47 |
| 3-klep (2 in + 1 ex) | 0,33–0,37 per klep | 0,41–0,46 |
| 4-klep | 0,37–0,40 per klep | 0,32–0,35 |

Contoh mesin acuan: klep isap 31 mm pada bore 63 mm = 0,492. Head 4-klep baru: 22 mm pada 57,3 mm = 0,384. Keduanya di rentang wajar arsitekturnya.

### 4.2 Hukuman bore kecil

Ini sering disalahpahami. Orang menyalahkan "2-klep" padahal yang membatasi adalah **bore**.

Pro Stock berkapasitas 8,2 liter dengan bore 119 mm, 2 klep pushrod. Klep isapnya 65 mm = **0,545 × bore**. Luas klep / bore = 0,297 — **sama dengan F1 yang 4-klep**.

Mesin acuan kita: bore 63 mm, klep 31 mm = 0,492 × bore. Luas klep / bore cuma **0,242**.

Kenapa bisa 0,545 di bore besar tapi cuma 0,492 di bore kecil? Karena busi, lebar seat, dan lahan gasket memakan ruang yang hampir tetap dalam milimeter — pada bore kecil, ruang tetap itu porsinya jauh lebih besar.

**Implikasi praktis:** pindah dari 2-klep ke 4-klep di bore kecil memberi lompatan besar (0,242 → 0,295, naik 22%). Di bore besar, keuntungannya jauh lebih kecil. Itulah kenapa Pro Stock masih pakai 2 klep dan tidak rugi.

### 4.3 Rasio klep buang terhadap isap

```
rasio luas = (n_ex × D_ex²) / (n_in × D_in²)
```

Nilai lazim 0,70–0,80 untuk 4-klep, 0,72–0,80 untuk 2-klep.

Yang lebih penting bukan rasio klep, tapi **rasio throat** (Bab 5).

## 5. Throat: pembatas yang sesungguhnya

### 5.1 Kenapa throat, bukan klep

Pada lift rendah, luas tirai (curtain area) yang membatasi:

```
A_tirai = n_klep × π × D_klep × lift
```

Pada lift tinggi, tirai jadi lebih besar dari lubang throat, dan throat yang membatasi:

```
A_throat = n_klep × π/4 × D_throat²
```

Titik silangnya disebut **lift kritis**:

```
lift_kritis = A_throat / (n_klep × π × D_klep)
```

Di atas lift kritis, menambah lift hampir tidak menambah flow puncak.

### 5.2 Angka nyata

| Mesin | Lift kritis in | Lift dipakai | Kelipatan |
|---|---|---|---|
| Acuan 2-klep | 6,78 mm | 10,8 mm | 1,59× |
| Build 4-klep | 4,64 mm | 9,0 mm | 1,94× |
| Vespa 3-klep | 4,59 mm | — | — |

Semua mesin balap berjalan **jauh di atas** lift kritisnya. Kenapa?

Karena yang dibayar di mesin balap bukan flow puncak, tapi **time-area** — integral luas terhadap waktu. Menahan klep tinggi lebih lama mengisi silinder lebih banyak, walau flow puncaknya tidak bertambah.

Ini koreksi penting terhadap saran umum "lift maksimum berguna = 0,25 × diameter klep". Aturan itu benar untuk flow puncak steady, salah untuk mesin balap.

### 5.3 Membesarkan throat

Throat adalah **satu-satunya perubahan yang menaikkan plafon flow**. Bentuk port tidak bisa melakukannya; bentuk port hanya menentukan seberapa dekat kamu ke plafon itu.

Batasnya lebar seat:

```
lebar_seat = (D_klep − D_throat) / 2
```

| Lebar seat | Keterangan |
|---|---|
| ≥ 1,2 mm | konservatif, tahan lama |
| 0,9–1,2 mm | praktik balap lazim |
| 0,7–0,9 mm | agresif, butuh material bagus |
| < 0,7 mm | berisiko, terutama sisi buang |

Sisi buang selalu perlu seat lebih lebar dari sisi isap — klep buang membuang panasnya ke seat, dan klep buang kepanasan adalah penyebab jebol nomor satu di mesin kompresi tinggi.

Contoh: head 4-klep dengan klep 22 mm. Rasio terbukti 0,935 memberi throat 20,6 mm, lebar seat 0,71 mm — terlalu tipis untuk klep sekecil itu. Kompromi yang diambil: **throat 20,2 mm, lebar seat 0,9 mm**, gain flow +7,4%.

## 6. Port: luas penampang dan kecepatan gas

### 6.1 Rumus pokok

```
MGV = (luas piston / CSA port) × MPS
```

Untuk port bercabang (4-klep), CSA yang dipakai adalah CSA **runner bersama** sebelum pecah dua.

### 6.2 Dua jangkar untuk menentukan CSA

**Jangkar kecepatan:**
```
CSA = luas_piston × MPS / MGV_target
```

**Jangkar rasio:**
```
CSA = rasio_port_throat_acuan × A_throat_baru
```

Pakai keduanya. Hasilnya rentang, bukan satu angka — dan rentang itu jujur.

### 6.3 Angka nyata

| Mesin | CSA port | Throat | Rasio | MGV |
|---|---|---|---|---|
| Acuan 2-klep @10.000 | 683 mm² | 661 mm² | 1,035 | 97 m/s |
| Build 4-klep @12.000 | 615–665 mm² | 641 mm² | 0,96–1,04 | 94–105 m/s |

### 6.4 Rasio port/throat: menyempit atau melebar

Kalau CSA port **lebih besar** dari luas throat (rasio > 1), aliran mempercepat menuju throat. Ini kondisi stabil — aliran yang mempercepat cenderung menempel.

Kalau CSA port **lebih kecil** dari throat (rasio < 1), titik tersempit pindah dari seat ke port. Throat yang susah payah dibesarkan jadi tidak terpakai penuh, dan ada pelebaran tepat sebelum klep yang cenderung melepas aliran.

Mesin acuan: 1,035 — port sedikit lebih besar. Ini kondisi yang benar.

Pada build 4-klep, CSA 615 mm² memberi rasio 0,96 (melebar) sementara 665 mm² memberi 1,04 (menyempit). Ini alasan kuat untuk condong ke ujung atas rentang.

### 6.5 Port buang

Port buang jauh lebih besar relatif terhadap throat-nya dibanding port isap, karena gas buang panas volumenya berlipat.

Mesin acuan: port buang 29 mm, throat 23,8 mm. Rasio **1,49**.

Perhatikan: port buang 29 mm hampir sama besar dengan port isap 29,5 mm, walau klep buangnya lebih kecil.

Kecepatan gas di port buang mesin acuan: **101 m/s** — hampir identik dengan port isap (97 m/s). Ini konsistensi yang bagus dan bisa dipakai sebagai jangkar.

## 7. Bentuk port

### 7.1 Penampang: bundar atau oval

Untuk port 4-klep bercabang, penampang **tinggi-sempit** (aspect tinggi:lebar sekitar 1,3) secara teori lebih baik daripada bundar. Alasannya: port yang tinggi membuat short-turn radius lebih landai relatif terhadap tinggi port, sehingga aliran tidak mudah lepas di lantai port.

Mesin acuan memakai port **bundar** 29,5 mm dan berhasil. Jadi ini bukan hukum mati.

Rumus luas superelips (antara elips dan kotak, eksponen 2,5):

```
Luas ≈ 0,92 × lebar × tinggi
tinggi = √(CSA / (0,92 × aspect)) × aspect
```

Untuk CSA 615 mm² dengan aspect 1,30: **22,7 W × 29,5 H mm**.

### 7.2 Short-turn radius

Bagian dalam tikungan port — lantainya — adalah tempat aliran paling mudah lepas.

```
R_short_turn_minimum ≈ 0,40 × tinggi port
```

Untuk port setinggi 29,5 mm: **R minimum 11,8 mm**.

Menggerus short-turn terlalu tajam adalah kesalahan porting paling umum. Yang terlihat seperti "melancarkan jalan" justru menciptakan zona separasi yang menutup sebagian penampang efektif.

### 7.3 Bowl di bawah klep

```
Luas bowl maksimum ≈ 1,10–1,15 × luas throat
```

Menggerus bowl lebih besar dari ini menurunkan kecepatan tepat di tempat yang paling butuh kecepatan.

### 7.4 Taper

Port harus menyempit atau melebar **secara halus dan monoton**. Perubahan mendadak, terutama dekat throat, menciptakan separasi.

Pada model parametrik yang dipakai di simulasi buku ini, perubahan luas mengikuti kurva cosinus, bukan garis lurus — taper linear memberi perubahan mendadak di kedua ujungnya.

### 7.5 Mulut port di flange manifold

Temuan dari simulasi: bentuk mulut port di bidang flange berpengaruh besar. Mulut bertepi tajam yang menonjol ke dalam plenum menciptakan rugi masuk yang setara atau lebih besar dari rugi tikungan seluruh port.

Praktisnya: sambungan manifold ke head yang tidak sebidang, atau bertepi tajam, bisa memakan lebih banyak flow daripada short-turn radius yang digerus susah payah. Ini perbaikan murah yang sering diabaikan.

## 8. Lift kritis

Sudah dibahas di 5.1. Ringkasan praktisnya:

```
lift_kritis = A_throat / (n_klep × π × D_klep)
```

**Perbandingan penting antar arsitektur:**

Pada 3-klep dengan satu klep buang besar, lift kritis sisi buang **lebih tinggi** dari sisi isap:

| | Lift kritis in | Lift kritis ex |
|---|---|---|
| 4-klep (2 in, 2 ex) | 4,64 mm | 3,68 mm |
| 3-klep (2 in, 1 ex) | 4,59 mm | 5,03 mm |

Sebabnya: satu klep besar punya keliling total lebih kecil daripada dua klep kecil berluas sama. Untuk membuka luas tirai yang sama, butuh lift lebih tinggi.

**Konsekuensi desain cam:** pada 3-klep, klep buang butuh lift **lebih tinggi** daripada klep isap. Pada 4-klep, kebalikannya.

---

# BAGIAN III — CAMSHAFT

## 9. Empat kejadian dan urutannya

Cam tidak "mengisi ruang bakar". Bore, head, dan port sudah menentukan plafonnya. Cam mengatur **kapan** klep membuka dan menutup relatif terhadap piston dan gelombang tekanan.

Empat kejadian, urut menurut kepentingannya:

**1. IVC — klep isap menutup.** Kejadian terpenting di seluruh camshaft. Menentukan kompresi dinamis dan rpm di mana efisiensi penjebakan memuncak.

**2. Durasi dan lift.** Menentukan berapa banyak yang bisa lewat (time-area).

**3. Overlap di TDC.** Menentukan pembilasan sisa gas buang.

**4. EVO — klep buang membuka.** Menukar kerja ekspansi dengan rugi pemompaan.

Ditambah satu yang bukan soal tenaga sama sekali: **kelegaan klep-piston** (Bab 13). Ini soal mesin pecah atau tidak.

## 10. IVC dan kompresi dinamis

### 10.1 Posisi piston

```
s(θ) = r(1 − cos θ) + L − √(L² − (r sin θ)²)
```
dengan `r = stroke/2`, `L = panjang rod`, `θ` diukur dari TDC.

### 10.2 Kompresi dinamis

```
V_saat_IVC = V_ruang_bakar + luas_piston × s(180° + IVC_ABDC)
DCR = V_saat_IVC / V_ruang_bakar
```

Bentuk yang lebih berguna, karena linear terhadap CR:

```
DCR = 1 + (V_sapu_saat_IVC / V_displacement) × (CR − 1)
```

Dari sini, membalik untuk mencari CR statis yang dibutuhkan jadi mudah.

### 10.3 Contoh pengaruh IVC

Mesin 149,6 cc, bore 57,3, stroke 58, rod 95, CR statis 14:1:

| IVC (ABDC) | DCR |
|---|---|
| 35° | 13,13 |
| 45° | 12,56 |
| 55° | 11,86 |
| 65° | 11,02 |
| 75° | 10,10 |

Rentangnya lebar. **Kompresi statis sendirian tidak berarti apa-apa tanpa IVC.**

### 10.4 Konsekuensi yang sering terlewat

Karena durasi lebih panjang mendorong IVC lebih telat, dan IVC lebih telat menurunkan DCR:

> **RPM sasaran, kompresi, dan bahan bakar adalah satu paket yang tidak bisa dipilih terpisah.**

Menaikkan rpm sasaran memaksa durasi lebih panjang, yang menurunkan DCR, yang membolehkan kompresi statis lebih tinggi — atau bahan bakar oktan lebih rendah.

## 11. Durasi dari time-area

### 11.1 Prinsip

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

### 11.2 Hasil yang berlawanan intuisi

| Mesin | Kapasitas | Throat | RPM | Durasi |
|---|---|---|---|---|
| Acuan 2-klep | 199,5 cc | 661 mm² | 10.000 | 281° |
| Build 4-klep | 149,6 cc | 641 mm² | 12.000 | **261°** |

**Durasi turun walau rpm naik.**

Sebabnya: head 4-klep bernapas 29% lebih lega per cc (4,28 vs 3,31 mm²/cc). Butuh waktu lebih sedikit untuk memasukkan jumlah yang sama.

Ini contoh bagus kenapa aturan jempol "rpm tinggi = durasi panjang" bisa menyesatkan. Yang benar adalah rpm tinggi **dan luas klep tetap** butuh durasi panjang.

### 11.3 Untuk arsitektur yang lebih sempit

Head 3-klep dengan luas klep isap/bore cuma 0,262 butuh **285°** untuk 12.000 rpm — 24° lebih panjang dari 4-klep. Itu ongkos nyata dari 11% luas klep yang hilang: overlap lebih besar, pita tenaga lebih sempit.

## 12. Overlap, LSA, dan ICL

### 12.1 Definisi

```
durasi_in  = IVO_BTDC + 180 + IVC_ABDC
durasi_ex  = EVO_BBDC + 180 + EVC_ATDC
overlap    = IVO_BTDC + EVC_ATDC
ICL        = durasi_in / 2 − IVO_BTDC        (ATDC)
ECL        = durasi_ex / 2 − EVC_ATDC        (BTDC)
LSA        = (ICL + ECL) / 2
```

### 12.2 Contoh penguraian

Cam acuan: EX buka 63 BBDC, EX tutup 38 ATDC, IN buka 38 BTDC, IN tutup 63 ABDC.

| | |
|---|---|
| Durasi in / ex | 281° / 281° (simetris) |
| Overlap | 76° |
| ICL / ECL | 102,5° ATDC / 102,5° BTDC |
| LSA | 102,5° |

LSA 102,5° itu ketat — khas mesin drag yang mengejar puncak, bukan lebar pita.

### 12.3 Menskalakan overlap

Yang harus dipertahankan adalah **luas tirai overlap per cc**, bukan lift-nya:

```
luas_per_cc = n_klep × π × D_klep × lift_di_TDC / kapasitas
```

Ini penting untuk 4-klep. Dua klep isap memberi luas tirai jauh lebih besar per milimeter lift dibanding satu klep besar. Menskalakan lift lewat diameter saja akan memberi overlap dua kali lipat terlalu besar.

Contoh: acuan 1 klep 31 mm dengan lift TDC 1,83 mm pada 199,5 cc. Mesin baru 2 klep 22 mm pada 149,6 cc perlu lift TDC **0,97 mm** — bukan 1,83 dan bukan 2,55.

### 12.4 Jebakan penafsiran "lift overlap"

Angka lift overlap yang beredar di bengkel sering ambigu: apakah itu lift **satu klep** atau **gabungan in + ex**?

Cara memastikannya: hitung dari timing. Dengan profil harmonik,

```
lift(θ) = lift_maks × sin²(π × θ_dari_bukaan / durasi)
```

Untuk cam acuan dengan IVO 38 BTDC dan durasi 281°, lift di TDC = 1,83 mm per klep = 3,67 mm gabungan. Angka yang disebut adalah "3,6 mm" — jadi jelas itu **gabungan**.

**Sudut selalu lebih bisa dipercaya daripada angka lift.** Kalau bisa memilih, minta data timing.

### 12.5 Pertukaran pokok

Dengan durasi tetap, overlap lebih besar memaksa IVO lebih awal, yang memaksa IVC lebih awal juga, yang menaikkan DCR.

| Durasi | IVO BTDC | IVC ABDC | DCR (CR 14) |
|---|---|---|---|
| 250° | 38,0 | 32,0 | 13,3 |
| 270° | 41,0 | 49,0 | 12,3 |
| 290° | 44,1 | 65,9 | 10,9 |

Tidak ada cara mendapatkan overlap besar **dan** IVC telat tanpa menambah durasi.

## 13. Kelegaan klep-piston

### 13.1 Kenapa kantong klep dibutuhkan

Di dekat TDC piston hampir tidak bergerak. Untuk mesin stroke 58 mm rod 95 mm:

| Sudut dari TDC | Turun piston |
|---|---|
| 4° | 0,09 mm |
| 8° | 0,28 mm |
| 14° | 1,10 mm |
| 20° | 2,27 mm |

Sementara klep sudah bergerak beberapa milimeter. Titik paling kritis biasanya **7–10° setelah TDC**.

### 13.2 Perhitungan

```
kebutuhan(θ) = lift_klep(θ) − turun_piston(θ)
kantong = maks(kebutuhan) × faktor_aman + kelegaan_minimum
```

Faktor aman 1,25 diperlukan karena profil harmonik meremehkan lift di sisi flank — cam balap sungguhan lebih agresif. Kelegaan minimum 1,0–1,5 mm untuk isap, 1,5–2,0 mm untuk buang (klep buang memuai lebih banyak).

### 13.3 Hasil nyata

Build 4-klep, durasi 261°, IVO 27,7 BTDC, lift 9 mm:

- Kantong yang dibutuhkan: **2,71 mm**
- Titik paling kritis: **+7° dari TDC**

Sebagai perbandingan, dengan overlap dua kali lipat (kesalahan penskalaan awal), kantong yang dibutuhkan jadi **4,00 mm** — dan itu memakan 20% anggaran volume ruang bakar.

### 13.4 Peringatan wajib

Perhitungan ini adalah **perkiraan awal**, bukan pengganti pemeriksaan fisik. Yang tidak dimodelkan: sudut klep, bentuk kubah piston, deformasi valvetrain pada rpm tinggi, dan profil cam sebenarnya.

**Selalu cek dengan clay atau lilin sebelum mesin diputar.**

---

# BAGIAN IV — KOMPRESI

## 14. Statis, dinamis, dan efektif

### 14.1 Tiga angka berbeda

**Kompresi statis** — rasio volume di BDC terhadap volume di TDC. Angka di atas kertas.

```
CR = (Vd + Vc) / Vc
```

**Kompresi dinamis** — dihitung dari posisi piston saat klep isap benar-benar menutup. Ini yang **dirasakan mesin** dan yang menentukan detonasi.

**Rasio ekspansi** — sama dengan CR statis pada mesin konvensional. Ini yang menentukan efisiensi termal.

Perbedaan antara DCR dan rasio ekspansi adalah alasan kompresi statis tinggi tetap berguna walau IVC telat: kamu membuang sebagian kompresi tapi mempertahankan seluruh ekspansi.

### 14.2 Efisiensi termal ideal

```
η = 1 − 1/CR^(γ−1)     dengan γ ≈ 1,4
```

| CR | η ideal |
|---|---|
| 12 | 62,9% |
| 13 | 64,1% |
| 14 | 65,2% |
| 15 | 66,1% |
| 16 | 67,0% |

Perhatikan **hasil yang semakin berkurang**. Dari 14 ke 15 cuma +1,5% relatif — sekitar 0,6 HP dari 40 HP. Sering tidak sepadan dengan risiko dan kerumitan yang ditambahkan.

## 15. Anggaran volume ruang bakar

### 15.1 Komponennya

Volume ruang bakar bukan cuma "ruang di head". Anggarannya:

```
Vc_total = V_pentroof + V_gasket + V_deck + V_kantong_klep − V_dome_piston
```

| Komponen | Rumus |
|---|---|
| Pent-roof | luas_bore × tinggi_efektif (3–4 mm untuk 4-klep modern) |
| Gasket | luas_bore × tebal_gasket |
| Deck | luas_bore × jarak_piston_di_bawah_deck |
| Kantong klep | n_kantong × luas_kantong × kedalaman × ~0,40 |
| Dome piston | negatif — mengurangi volume |

Faktor 0,40 pada kantong klep karena kantong berbentuk cekungan dangkal, bukan silinder penuh.

### 15.2 Contoh nyata

Bore 57,3 mm, target CR 14:1 pada 149,6 cc → Vc harus **11,50 cc**.

| Komponen | Volume |
|---|---|
| Pent-roof (3,5 mm) | 9,03 cc |
| Gasket 0,8 mm | 2,06 cc |
| Deck 0,5 mm | 1,29 cc |
| 4 kantong klep 2,71 mm | 1,58 cc |
| **Total** | **13,95 cc** |

→ CR tanpa dome: **11,72:1**, bukan 14:1.

**Dome piston harus mengusir 2,45 cc** (tinggi rata-rata 0,95 mm).

### 15.3 Pelajaran

**Kantong klep ikut menambah volume ruang bakar.** Ini yang paling sering dilupakan. Pada contoh di atas, kantong memakan 14% anggaran; pada versi dengan overlap lebih besar, 20%.

Konsekuensi praktis: kalau kamu memapas head untuk mengejar kompresi lalu menggerus kantong klep untuk cam baru, sebagian kompresi yang baru didapat langsung hilang lagi.

**Urutan yang benar:** tentukan cam dulu → hitung kantong klep → baru hitung dome/papasan yang dibutuhkan.

## 16. Mengkalibrasi batas detonasi

### 16.1 Kenapa tabel oktan tidak cukup

Tabel umum menghubungkan DCR dengan oktan minimum:

| DCR | Bahan bakar (menurut tabel umum) |
|---|---|
| < 9,0 | 92–95 RON |
| 9,0–10,0 | 98 RON |
| 10,0–11,0 | 100+ RON |
| 11,0–12,5 | bensin balap 102+ |
| > 12,5 | metanol |

Tabel ini **terlalu konservatif** untuk bahan bakar balap sungguhan.

### 16.2 Data nyata yang membantahnya

Mesin acuan:

| | |
|---|---|
| CR statis | **16:1** [UKUR] |
| IVC | 63° ABDC [UKUR] |
| Bahan bakar | bensol / avgas 100LL [UKUR] |
| **DCR terhitung** | **12,83** [HITUNG] |
| Status | terbukti, bertahun-tahun, tanpa masalah |

Tabel bilang 12,83 harus metanol. Mesin itu jalan dengan bensol.

Kokohnya angka ini: sensitivitas terhadap asumsi panjang rod sangat kecil (DCR 12,77–12,90 untuk rod 98–112 mm). Jadi walau rod acuan belum diukur, kesimpulannya tetap.

### 16.3 Cara memakainya

Setelah punya DCR terbukti untuk bahan bakarmu:

```
CR_statis_baru = 1 + (DCR_terbukti − 1) × Vd / V_sapu_saat_IVC
```

Contoh: build 4-klep dengan IVC 52,8° ABDC. Untuk mencapai DCR 12,83 dibutuhkan CR statis **14,9:1**.

Rencana 14:1 memberi DCR **12,07** — margin **+0,76 di bawah** batas terbukti. Artinya rencana itu **konservatif**, bukan agresif.

### 16.4 Faktor yang menggeser batas

Batas DCR bukan angka tunggal untuk satu bahan bakar. Yang menggesernya:

**Menaikkan toleransi:**
- Bore lebih kecil (jalur api lebih pendek)
- Busi di tengah (4-klep) vs menepi (2-klep, 3-klep)
- RPM lebih tinggi (waktu untuk detonasi berkembang lebih pendek)
- Pendingin cair vs udara
- Campuran lebih kaya
- Squish yang baik

**Menurunkan toleransi:**
- Bore besar
- Ruang bakar asimetris
- Dome piston tinggi (memperpanjang jalur api, menambah titik panas)
- Suhu udara masuk tinggi
- Beban berkelanjutan (endurance vs sprint)

Contoh penerapan: head 3-klep punya busi menepi dan ruang bakar asimetris, jadi disarankan **1 angka lebih rendah** dari 4-klep pada bahan bakar yang sama.

---

# BAGIAN V — SALURAN MASUK

## 17. Throttle body

### 17.1 Perhitungan aliran

```
Q_rata2  = Vd × (rpm/60) / 2 × VE          [4-tak]
duty     = n_silinder × durasi_isap / 720
Q_puncak = Q_rata2 / duty × (π/2)
```

Faktor π/2 mengasumsikan profil aliran sinusoidal selama langkah isap.

```
D_TB = √(4 × Q_puncak / (π × v_target × (1 − blokade_poros)))
```

Blokade poros butterfly biasanya 6–8% dari luas bore.

### 17.2 Kecepatan target — kalibrasi, bukan tabel

Aturan umum menyebut 105 m/s. Mesin acuan berjalan di **61 m/s**.

Untuk CVT yang selalu WOT, respons part-throttle tidak relevan; yang dikejar restriksi minimum. Kecepatan rendah di TB tidak merugikan.

### 17.3 Kenapa mengecilkan TB tidak menaikkan gas speed

Ini kesalahpahaman umum yang layak dibahas tuntas.

| TB | v di TB | **v di port** | Rugi TB | Flow relatif |
|---|---|---|---|---|
| 34 mm | 76 m/s | **97 m/s** | 872 Pa | −6,7% |
| 36 mm | 68 m/s | **97 m/s** | 694 Pa | −4,0% |
| 38 mm | 61 m/s | **97 m/s** | 559 Pa | −1,8% |
| 40 mm | 55 m/s | **97 m/s** | 455 Pa | 0,0% |

**Kecepatan di port tidak bergerak sama sekali.**

Kecepatan di port ditentukan oleh luas port. Debit sama, luas sama, kecepatan sama. Diameter TB tidak punya cara mempengaruhinya.

Yang naik hanya kecepatan di dalam TB itu sendiri — dan kecepatan di situ tidak melakukan pekerjaan apa pun. Udara melambat lagi di manifold sebelum sampai ke port. Energi yang dipakai mempercepatnya terbuang jadi panas.

**Perbandingan skala:** rugi port 2343 Pa vs rugi TB 559 Pa. Port mendominasi 4:1.

**Kalau mau menaikkan gas speed, tuasnya adalah CSA port**, bukan TB:

| CSA port | v di port |
|---|---|
| 560 mm² | 115 m/s |
| 615 mm² | 105 m/s |
| 665 mm² | 97 m/s |

**Pengecualian:** kalau memakai karburator, bukan injeksi, jawabannya berubah. Karburator butuh kecepatan di venturi untuk sinyal pengabutan, jadi mengecilkan bisa masuk akal.

## 18. Panjang runner dan tuning gelombang

### 18.1 Dua model

**Model gelombang (quarter-wave):** gelombang tekanan lahir saat klep isap membuka, lari ke ujung terbuka, memantul, dan kembali. Ditala supaya pantulan tiba saat klep masih terbuka.

```
L = c × θ_durasi / (12 × n × rpm)
```
dengan `c` = kecepatan suara [m/s], `θ` = durasi isap [deg], `n` = harmonik.

**Model Helmholtz:** kolom udara di runner bersama volume silinder membentuk resonator.

```
f_H = (c / 2π) × √(A / (V_eff × L_eff))
V_eff = V_cyl × (CR + 1) / (2 × (CR − 1))
```
Ditala saat `f_H / f_engine ≈ K`, dengan K sekitar 2 untuk mobil bermanifold panjang, 3,5–4,5 untuk mesin kecil bermanifold pendek.

### 18.2 Kecepatan suara — jangan pakai suhu ambient

```
c = 20,05 × √(T[K])
```

Suhu **di dalam runner**, bukan ambient. Panas mesin menaikkannya 20–30 °C. Pada 45 °C, c = 357 m/s, bukan 343.

### 18.3 Contoh

Mesin 149,6 cc, durasi isap 250°, c = 357 m/s:

| RPM | h2 | h3 | h4 | h5 |
|---|---|---|---|---|
| 8.000 | 466 | 310 | 233 | 186 |
| 10.000 | 373 | 248 | 186 | 149 |
| 12.000 | 310 | 207 | 155 | 124 |

Batasan ruang di motor biasanya memaksa harmonik 3 atau 4.

### 18.4 Kalibrasi harmonik

Model gelombang tidak bisa memberitahu harmonik mana yang dipakai mesinmu. Cara mengetahuinya: **ukur panjang runner mesin yang sudah terbukti**, lalu cocokkan dengan tabel. Baris yang cocok adalah harmonik yang terbukti jalan, dan mesin baru tinggal memakai baris yang sama.

Ini prinsip yang sama dengan seluruh buku: satu pengukuran mengalahkan banyak teori.

## 19. Velocity stack, plenum, dan manifold

### 19.1 Koreksi ujung

Panjang efektif kolom udara lebih panjang dari panjang fisiknya:

```
L_efektif = L_fisik + k × jari-jari
```

| Bentuk ujung | k |
|---|---|
| Pipa polos | 0,61 |
| Bermulut lonceng (bellmouth) | 0,85 |

### 19.2 Radius bellmouth

```
R_bellmouth ≥ 0,15–0,20 × diameter
```

Di bawah ini, koefisien flow turun cepat. Di atas 0,25, hasilnya jenuh.

### 19.3 Volume plenum

```
V_plenum ≈ 1,0–1,5 × kapasitas mesin
```

Untuk mesin 1 silinder di drag, ujung atas rentang atau bahkan tanpa plenum (velocity stack terbuka ke atmosfer) lazim dipakai.

### 19.4 Data manifold standar sebagai referensi

Dari pengukuran manifold Honda Vario 150 standar (hasil rekayasa balik dari file CAD):

| | |
|---|---|
| Port di head | Ø30,2 mm |
| Throttle body | Ø38 mm |
| Panjang centerline port→TB | **43 mm** |
| Sudut belok total | **34°** |
| Bentuk saluran | melengkung, bukan lurus |

Perhatikan betapa **pendek** runner standar itu — 43 mm. Ini menjelaskan kenapa mesin standar puncaknya di rpm rendah dan kenapa runner yang lebih panjang mengubah karakternya drastis.

Pelebaran dari 30,2 mm di head ke 38,8 mm di TB berlangsung mulus sepanjang saluran — bukan melebar mendadak di satu titik.

### 19.5 Susunan pelebaran yang benar

Pertanyaan yang sering muncul: apakah port di head, manifold, TB, dan velocity stack harus sama besar lalu melebar di stack saja, atau melebar bertahap?

Jawaban dari data: **melebar bertahap dan mulus**, dengan urutan luas dari kecil ke besar:

```
throat (terkecil) → port head → manifold → throttle body → velocity stack (terbesar)
```

Contoh dari mesin acuan (dalam luas, bukan diameter):

| Titik | Luas | Relatif throat |
|---|---|---|
| Throat | 661 mm² | 1,00 |
| Port head | 683 mm² | 1,03 |
| Throttle body (efektif) | 1055 mm² | 1,60 |

Aliran mempercepat terus-menerus dari mulut stack sampai throat. Percepatan yang terus-menerus itu yang menjaga aliran menempel di dinding. Sekali ada pelebaran di tengah jalan, aliran melambat, lapisan batas menebal, dan sebagian penampang jadi tidak terpakai.

**Jangan** membuat TB lebih kecil dari port lalu melebar lagi di stack — itu menciptakan penyempitan-pelebaran yang justru merugikan.

---

# BAGIAN VI — SALURAN BUANG

## 20. Port dan header

### 20.1 CSA port buang

Dua jangkar, sama seperti sisi isap:

```
CSA_ex = rasio_port_throat_acuan × A_throat_ex_baru
CSA_ex = luas_piston × MPS / MGV_ex_target
```

Data acuan: rasio port/throat **1,49**, MGV port buang **101 m/s**.

Perhatikan rasio 1,49 jauh lebih besar dari sisi isap (1,035). Gas buang panas volumenya berlipat, jadi butuh penampang lebih besar untuk kecepatan yang sama.

### 20.2 Diameter header

```
A_header ≈ 1,07 × A_port_buang
```

Dari data acuan: header dalam 30 mm terhadap port 29 mm.

### 20.3 Transisi ke muffler

Data acuan: inlet muffler 50 mm terhadap header 30 mm — rasio luas **2,78×**.

Titik transisi inilah tempat gelombang ekspansi lahir. Posisinya menentukan panjang header efektif.

## 21. Panjang header dan harmonik

### 21.1 Mekanisme

Saat klep buang membuka, gelombang tekanan positif lari menyusuri header. Di ujung terbuka (transisi ke muffler), gelombang itu memantul sebagai gelombang **negatif** dan kembali ke klep. Kalau tiba saat overlap, ia menarik sisa gas buang keluar dan menarik muatan segar masuk — inilah pembilasan.

```
t = (180 + EVO_BBDC) / (6 × rpm)          [detik, dari EVO ke TDC]
L = c_gas × t / (2n)                       [n = harmonik]
```

### 21.2 Kecepatan suara gas buang

```
c_gas ≈ 550–700 m/s
```

Tergantung suhu (~1100 K) dan kekayaan campuran. Panjang header berskala **langsung** dengan angka ini, jadi ketidakpastian ±8% wajar.

### 21.3 Contoh

Mesin baru, EVO 53° BBDC, 12.000 rpm, c = 650 m/s:

| Harmonik | Panjang |
|---|---|
| 1 | 1052 mm |
| 2 | 526 mm |
| 3 | 351 mm |
| 4 | 263 mm |

### 21.4 Menentukan harmonik

Sama seperti runner isap: **ukur panjang header mesin yang sudah terbukti** — dari klep buang sampai titik pelebaran — dan cocokkan dengan tabelnya pada rpm mesin itu. Baris yang cocok adalah harmoniknya.

### 21.5 Kenapa knalpot layak dicurigai

Pada studi kasus di buku ini, ditemukan selisih besar antara potensi head dan hasil sebenarnya:

| Metode | Hasil |
|---|---|
| Dari flow head | ~35 HP |
| Dari waktu lintasan | ~28 HP |

Selisih 20–30% yang tertinggal di meja. Kalau head sudah dihitung benar, tersangka utamanya adalah **panjang header** dan **setelan CVT** — bukan porting lebih lanjut.

Kalau harmonik header meleset, pembilasan hilang tepat di rpm puncak, dan tidak ada porting yang bisa menggantikannya.

---

# BAGIAN VII — BATAS MEKANIS

## 22. Kecepatan dan percepatan piston

### 22.1 Mean piston speed

```
MPS = 2 × stroke[m] × rpm / 60
```

Ini indikator umur mesin yang paling sederhana dan paling berguna.

### 22.2 Percepatan di TDC

```
a_TDC = ω² × r × (1 + r/L)
ω = 2π × rpm / 60,   r = stroke/2,   L = panjang rod
```

Percepatan di TDC selalu lebih besar dari di BDC, karena faktor `(1 + r/L)` menjadi `(1 − r/L)` di BDC. Rod pendek memperparah ketimpangan ini.

### 22.3 Gaya inersia

```
F = massa_piston_assy × a_TDC
```

Ini beban yang harus ditahan pin, rod kecil, rod besar, dan bearing — pada langkah buang, tanpa tekanan gas yang melawan.

### 22.4 Angka nyata

Mesin baru, stroke 58 mm, rod 95 mm:

| RPM | g di TDC |
|---|---|
| 12.000 | 6.093 |
| 12.500 | 6.612 |
| 13.000 | 7.151 |

Gaya inersia pada 12.000 rpm:

| Massa piston | Gaya |
|---|---|
| 80 g | 487 kgf |
| 100 g | 609 kgf |
| 120 g | 731 kgf |

**Massa piston adalah tuas paling murah yang tersedia.** Turun dari 120 ke 80 gram memangkas beban rod 33% — setara menurunkan rpm dari 13.000 ke 11.000, tanpa kehilangan tenaga sedikit pun.

### 22.5 Membandingkan ke mesin yang sudah terbukti

Ini cara paling berguna memakai angka di atas:

| Mesin | RPM | g di TDC |
|---|---|---|
| Acuan (stroke 64, rod 95) | 11.250 | 6.052 |
| **Baru (stroke 58, rod 95)** | **12.000** | **6.093** |

Selisih 0,7%. Artinya 12.000 rpm di mesin baru berada **di dalam amplop yang sudah terbukti**, bukan wilayah baru. Stroke yang lebih pendek membayar rpm yang lebih tinggi.

## 23. Rasio rod dan konsekuensinya

```
rasio_rod = panjang_rod / stroke
```

| Rasio | Keterangan |
|---|---|
| < 1,6 | sangat pendek |
| 1,6–1,75 | pendek, khas mesin kecil |
| 1,75–1,9 | umum |
| > 1,9 | panjang, khas mesin balap besar |

**Rod pendek — merugikan:**
- Side thrust piston lebih besar → gesekan dan keausan liner naik
- Percepatan puncak di TDC lebih tinggi

**Rod pendek — menguntungkan:**
- Piston menjauh dari TDC lebih cepat → kelegaan klep sedikit lebih longgar
- Dwell di TDC lebih singkat → waktu untuk detonasi berkembang lebih pendek

Efek rod terhadap kompresi dinamis kecil: untuk stroke 58 mm, perbedaan rod 95 vs 102 mm menggeser DCR cuma 0,05.

---

# BAGIAN VIII — PERBANDINGAN DUNIA

## 24. F1, MotoGP, Pro Stock

Semua angka di bawah dihitung dengan definisi yang sama, dari spesifikasi bore/stroke/rpm publik. Diameter klep dan CSA port **tidak dipublikasikan pabrikan** — dipakai proporsi lazim di kelasnya, jadi ini perkiraan beralasan, bukan data pabrik.

| Mesin | MPS | Klep/bore | v throat | v port |
|---|---|---|---|---|
| F1 V10 2005 (19.000 rpm) | 25,2 | 0,296 | 105 | 95 |
| F1 V8 2008 (18.000 rpm) | 23,9 | 0,296 | 99 | 90 |
| F1 V6 turbo (13.000 rpm) | 23,0 | 0,289 | 98 | 89 |
| MotoGP 1000 (18.000 rpm) | 29,1 | 0,296 | 121 | 112 |
| NHRA Pro Stock (10.500 rpm) | 32,0 | 0,297 | 133 | 106 |
| Acuan 2-klep 199cc | 21,3 | 0,242 | 109 | 105 |
| Build 4-klep 150cc | 23,2 | 0,295 | 97 | 94 |

## 25. Kenapa semua berkumpul di angka yang sama

### 25.1 Pengamatan

Kecepatan port semua mesin di atas jatuh di **89–112 m/s**. F1 justru lebih rendah dari mesin drag matic.

### 25.2 Sebabnya

```
v_port = (luas_piston / CSA_port) × MPS
```

Kedua faktornya punya plafon keras:

**Luas klep / luas bore** mentok di 0,30–0,35 untuk 4-klep. Itu batas geometri murni. Kolom "klep/bore" di tabel menunjukkan F1, MotoGP, Pro Stock, dan build 4-klep semuanya **0,289–0,297**. Tidak ada yang bisa melewatinya.

**Mean piston speed** mentok di 25–32 m/s karena inersia dan material.

Hasil kalinya jatuh di 90–120 m/s untuk siapa pun.

### 25.3 Bore hilang dari persamaan

Kalau semua proporsi diskalakan ke bore, `bore²` saling menghapus:

```
v_port = bore² / (n × (rasio_klep × rasio_throat × bore)² × rasio_port) × MPS
```

Bore lenyap. **Mesin 3 liter dan 150cc dengan proporsi sama punya kecepatan port identik.**

### 25.4 Jadi apa yang sebenarnya dilakukan F1

Bukan menaikkan kecepatan port. **Memperpendek stroke.**

F1 V10: stroke **39,8 mm**. Di 19.000 rpm mean piston speed cuma 25,2 m/s — nyaris sama dengan mesin 150cc di 12.000 rpm (23,2). Mereka mendapat 7.000 rpm ekstra **gratis** dalam hal kecepatan gas, karena pistonnya menempuh jarak jauh lebih pendek tiap putaran.

Itu tuas yang tidak tersedia kalau stroke sudah ditentukan.

### 25.5 Tenaga spesifik

| Mesin | Liter | HP | HP/L |
|---|---|---|---|
| F1 V10 2005 | 3,0 | 950 | 317 |
| F1 V8 2008 | 2,4 | 750 | 312 |
| MotoGP 1000 | 1,0 | 290 | 290 |
| NHRA Pro Stock | 8,19 | 1350 | 165 |
| *F1 V6 turbo (ICE)* | *1,6* | *900* | *562 — turbo* |

Pro Stock paling rendah di antara yang NA. Kehebatannya bukan di tenaga spesifik tapi di tenaga absolut. Dengan 2 klep pushrod di 10.500 rpm, 165 HP/L sudah mendekati batas arsitekturnya.

Yang membuat F1 dan MotoGP tiga kali lipat lebih tinggi bukan sihir: **putaran**. Tenaga = torsi × rpm, dan torsi per liter semua mesin NA yang bagus mirip-mirip.

---

# BAGIAN IX — CFD

## 26. Cara kerja dan batasnya

### 26.1 Alur kerjanya

1. **Geometri** — ambil volume *fluida*, bukan bendanya
2. **Meshing** — potong volume jadi jutaan sel; wajib ada lapisan prisma di dinding
3. **Solver** — selesaikan persamaan Navier-Stokes tiap sel secara iteratif
4. **Model turbulensi** — k-ω SST paling umum untuk saluran
5. **Boundary condition** — ini yang paling sering bikin hasil ngaco
6. **Post-processing** — mass flow, koefisien flow, peta kecepatan, zona separasi

### 26.2 Seberapa akurat

| Kasus | Akurasi absolut |
|---|---|
| Flow port head (steady, vs flowbench) | ±3–8% |
| Koefisien flow throttle body / stack | ±5% |
| Pressure drop plenum & airbox | ±5–10% |
| Tumble / swirl ratio | ±10–15% |
| Panjang runner optimal (wave tuning) | **buruk** — salah alat, pakai 1D |
| Prediksi HP absolut | **buruk** — butuh kalibrasi dyno |

### 26.3 Aturan emasnya

> **CFD kuat untuk membandingkan, lemah untuk memprediksi angka absolut tanpa kalibrasi.**

Kalau CFD bilang bellmouth R8 lebih baik 4% dari R5 — percaya arahnya. Kalau CFD bilang "tenaga 18,3 HP" — jangan percaya.

### 26.4 Alat yang tepat untuk pertanyaan yang tepat

**Pakai simulasi 1D** (GT-Power, Ricardo WAVE, OpenWAM, atau perhitungan di Bab 18/21) untuk yang **panjang dan volume**: panjang runner, volume plenum, diameter TB, panjang header.

**Pakai CFD 3D** untuk yang **bentuk**: radius bellmouth, short-turn radius, separasi di belokan, distribusi aliran di plenum.

Alur kerja yang benar: **1D dulu untuk dimensi utama → 3D untuk menghaluskan bentuk → flowbench/dyno untuk kalibrasi.**

## 27. Menyiapkan flowbench virtual

### 27.1 Susunan yang benar

```
plenum setengah bola  →  mulut port di bidang flange datar  →  port  →  keluar throat
   (tekanan total)              (dinding)                              (tekanan statik 0)
```

**Plenum harus setengah bola berpusat di mulut port**, dipotong tepat di bidang mulut. Bidang datar di sekelilingnya menjadi muka flange (dinding). Dengan begini batas masuk berjarak sama ke segala arah dan aliran masuk dari reservoir yang benar-benar tenang.

### 27.2 Depresi yang dipakai

Jalankan di **10"H₂O**, bukan 28".

Alasannya dua-duanya nyata:
- Di 28" kecepatan throat ~107 m/s = Mach 0,31 — terlalu tinggi untuk solver incompressible
- Di 10" jadi ~64 m/s = Mach 0,19, jauh lebih sah
- Start dingin dengan beda tekanan besar bikin solver diverge

Konversi ke depresi acuan pakai akar rasio tekanan — ini praktik baku flowbench, bukan akal-akalan:

```
CFM_28 = CFM_10 × √(28/10)
```

Sah karena pada Re > 10⁵ koefisien flow praktis tidak tergantung Re.

### 27.3 Model satu cabang

Port 4-klep bercabang simetris terhadap sekat pemisah. Modelkan **satu cabang saja** dengan bidang simetri di sekat: satu cabang membawa separuh aliran dan separuh CSA.

Yang hilang cuma rugi di ujung sekat — dan itu sama untuk semua varian, jadi tidak menggeser peringkat.

### 27.4 Setelan numerik

| Parameter | Nilai |
|---|---|
| Solver | simpleFoam (steady, incompressible) |
| Turbulensi | k-ω SST |
| Skema | bounded Gauss linearUpwind untuk U |
| SIMPLE | `consistent no` (bukan SIMPLEC) |
| Relaksasi | p 0,3 / U 0,7 |
| Iterasi | 3000 |
| Lapisan prisma | 6 lapis, ekspansi 1,2 |

SIMPLEC dengan relaksasi 0,9 diverge di iterasi ~69 dari start dingin. Jangan dinaikkan tanpa alasan.

### 27.5 Refinement volume, bukan cuma permukaan

Ini krusial dan mudah terlewat. `refinementSurfaces` hanya menghaluskan **permukaan**. Dinding port dapat sel halus dan lapisan prisma rapi, tapi **inti port** — tempat aliran utama lewat — bisa tertinggal di sel background yang kasar.

Solusinya: STL kedua berisi volume port saja, dipakai sebagai refinement region dengan mode `inside`.

## 28. Jebakan yang mahal

Bagian ini adalah yang paling berharga dari seluruh bab CFD. Semua yang tertulis di sini ditemukan dengan cara mahal: **sebelas simulasi berturut-turut memberi hasil yang salah** sebelum penyebabnya ketemu.

### 28.1 Aturan yang paling penting

> **Jalankan kasus berjawaban pasti LEBIH DULU, bukan terakhir.**

Pipa bundar lurus dengan boundary condition yang sama **harus** memberi Cf 0,85–0,95. Kalau tidak, setup-mu yang salah — bukan geometri yang sedang kamu pelajari.

Dalam pengembangan buku ini, sebelas kasus port dijalankan dan dianalisis sebelum pemeriksaan itu dilakukan. Semuanya tidak berlaku. Saat pipa lurus akhirnya dijalankan, hasilnya Cf 0,387 — langsung menunjuk ke setup, bukan ke geometri port yang sudah dituduh empat hipotesis berturut-turut.

### 28.2 Diagnostik numerik tidak menangkap apa pun

Selama sebelas kasus yang salah itu, **semua indikator hijau**:

| Diagnostik | Status |
|---|---|
| `checkMesh` | "Mesh OK" |
| Ketimpangan massa | 0,000–0,004% |
| Residual | turun 4 dekade |
| nut/nu | 63 rata-rata (normal) |

Yang akhirnya menangkap bug:
1. **Nilai Cf yang tidak masuk akal secara fisika**
2. **Melihat medan dengan TANDA kecepatan aksial**, bukan besarnya

Poin kedua layak digarisbawahi. Selama hanya |U| yang dilihat, aliran balik −15,7 m/s di tengah port terbaca sebagai "aliran lambat". Begitu tandanya dibuka, penyumbatnya langsung terlihat.

> **Keseimbangan massa 0,000% bukan bukti hasilnya benar. Itu cuma bukti mesh-nya tidak bocor.**

### 28.3 Daftar bug dan penjaganya

**Bug 1 — Pusat tutup tidak sebidang dengan cincinnya.**
Saat bellmouth ditambahkan, cincin pertama pindah ke hulu tapi pusat tutupnya tidak ikut. Tutup mulut port jadi **kerucut yang menyumbat**. Ini yang paling merusak: ia membuat setiap perbaikan yang benar tampak memperburuk keadaan.
*Penjaga:* pusat tutup wajib sebidang dengan cincin yang ditutupnya, toleransi 0,001 mm.

**Bug 2 — Klasifikasi patch outlet dengan uji jarak `|z| < tol`.**
Cakram keluar throat tegak lurus **sumbu klep** yang miring 13°, jadi uji terhadap z hanya menangkap pita tipis; sisa cakram jadi dinding yang menyumbat throat.
*Penjaga:* klasifikasi pakai arah normal segitiga, dan luas patch outlet wajib ±10% luas throat.

**Bug 3 — Plenum berupa bola yang digeser ke depan mulut.**
Permukaannya cuma 5 mm dari mulut port. 62% aliran masuk lewat 0,42% luas patch pada 72 m/s — itu jet, bukan plenum.
*Penjaga:* luas patch inlet wajib ±20% dari 2πR² setengah bola.

**Bug 4 — Bidang flange mewarisi refinement dinding.**
Mesh membengkak 123 ribu → 615 ribu sel, waktu jalan 82 menit per case.
*Penjaga:* beri bidang flange region sendiri di level rendah.

**Bug 5 — Mask plot yang terlalu ketat.**
Membuang segitiga bersisi > 3 mm padahal sel background 5 mm punya diagonal 8,7 mm — menciptakan "lubang" palsu yang mudah disalahartikan sebagai cacat mesh.
*Penjaga:* ambang mask harus di atas diagonal sel terkasar.

### 28.4 Jebakan perangkat lunak

Untuk OpenFOAM 1912 dari repo Ubuntu:

| Masalah | Solusi |
|---|---|
| Environment tidak diset | export `WM_PROJECT_DIR=/usr/share/openfoam`; jangan source `etc/bashrc` (rusak di paket ini) |
| `scotch` cuma stub kosong | pakai `method hierarchical` |
| Crash `IOstream sha1` | **hindari functionObject apa pun**; ukur debit dengan membaca file `phi` langsung |
| Field `0/` sebelum snappy | taruh di `0.orig`, salin ke `processor*/0` setelah meshing |
| Patch `processor` tidak terdefinisi | tambahkan `#includeEtc "caseDicts/setConstraintTypes"` di tiap boundaryField |
| `reconstructPar` gagal | jalankan `reconstructParMesh -constant` dulu |

### 28.5 Hasil setelah semua diperbaiki

| Kasus | Cf | K |
|---|---|---|
| Pipa lurus (acuan berjawaban pasti) | **0,879** | 0,295 |
| Port bengkok 37° | **0,849** | 0,387 |

Ongkos tikungan cuma **3,4%**.

Ini temuan desain yang penting: dengan short-turn radius yang wajar, **port bukan pembatasnya**. Cf 0,849 adalah plafon port telanjang; head lengkap dengan klep di lift 9 mm akan turun ke 0,55–0,65.

Artinya usaha menggerus bentuk port memberi hasil kecil dibandingkan **membesarkan throat**.

---

# BAGIAN X — STUDI KASUS

## 29. Mesin acuan: 199cc 2-klep drag

Semua angka di bagian ini [UKUR] kecuali ditandai lain.

### 29.1 Spesifikasi

| | |
|---|---|
| Bore × stroke | 63 × 64 mm = 199,5 cc |
| Katup | 2 klep |
| Klep in / ex | 31 / 27 mm |
| Throat in | 29 mm (rasio 0,935) |
| Port in | bundar Ø29,5 mm |
| Port ex | Ø29 mm |
| Lift | 10,8 mm |
| Cam | IN 38 BTDC / 63 ABDC, EX 63 BBDC / 38 ATDC |
| Durasi | 281° / 281° |
| Overlap | 76°, LSA 102,5° |
| CR statis | 16:1 |
| Bahan bakar | bensol / avgas 100LL |
| Throttle body | 38 mm |
| Header dalam | 30 mm |
| Inlet muffler | 50 mm |
| Penggerak | matic CVT |

### 29.2 Hasil terukur

500 m dalam **15,4 detik**, trap **158 km/h**.

### 29.3 Besaran turunan

| | Nilai | Catatan |
|---|---|---|
| Mean piston speed @10.000 | 21,3 m/s | |
| Luas klep in / bore | 0,242 | rendah — hukuman bore kecil |
| Kecepatan gas port in | 97 m/s | jangkar utama |
| Kecepatan gas port ex | 101 m/s | konsisten |
| Rasio port/throat in | 1,035 | |
| Rasio port/throat ex | 1,49 | |
| Rasio throat ex/in | 0,671 | |
| Kecepatan puncak di TB | 61 m/s | jauh di bawah "aturan" |
| Lift kritis in / ex | 6,78 / 5,23 mm | |
| Kelipatan lift in / ex | 1,59× / 2,07× | |
| **DCR** | **12,83** | batas terbukti untuk bensol |

### 29.4 Perkiraan tenaga

Dari neraca energi lintasan (asumsi massa 150 kg, CdA 0,35, Crr 0,02):

```
E_total = ½mv² + rugi_aero + rugi_gelinding
```

| Massa | HP roda | HP crank | HP/L |
|---|---|---|---|
| 140 kg | 23,6 | 26,9 | 135 |
| 150 kg | 24,8 | 28,2 | 141 |
| 165 kg | 26,5 | 30,1 | 151 |

Rincian energi (150 kg): kinetik 144 kJ, aero 69 kJ, gelinding 15 kJ. **Aero sudah memakan 30%** — pada trap 158 km/h, posisi tubuh dan fairing berpengaruh besar.

### 29.5 Selisih yang menarik

| Metode | Hasil |
|---|---|
| Dari flow head (throat 660 mm², Cf ~0,60) | ~34–39 HP |
| Dari lintasan | ~28 HP |

Head mampu mengalirkan untuk ~35 HP tapi mesin menghasilkan ~28. **20–30% tertinggal di meja**, dan bukan di head.

Tersangka: timing kem, knalpot, mapping, setelan CVT.

**Ini pelajaran penting:** sebelum memporting lebih jauh, pastikan dulu bagian lain sudah benar. Head yang sudah bagus tidak akan memberi tenaga kalau knalpotnya salah harmonik.

## 30. Build: 150cc 4-klep

### 30.1 Data yang diberikan

| | |
|---|---|
| Bore × stroke × rod | 57,3 × 58 × 95 mm = 149,6 cc |
| Klep in / ex | 22 / 19 mm, 4 klep |
| Throat in awal | 19,5 mm |
| Lift rencana | 9 mm |
| CR statis rencana | 14:1 |
| Sasaran | drag 500 m, CVT |

### 30.2 Analisis awal

| | |
|---|---|
| Luas klep in / bore | 0,295 — setara F1/MotoGP |
| Throat/klep | 0,886 — **di bawah praktik terbukti 0,935** |
| Potensi flow | 84,5 CFM @28" |
| Potensi tenaga | ~38 HP |

### 30.3 Temuan utama: throat bisa dibesarkan

Praktik terbukti 0,935 memberi throat 20,6 mm, tapi lebar seat tinggal 0,71 mm — terlalu tipis untuk klep 22 mm.

Kompromi: **throat 20,2 mm**, lebar seat 0,9 mm.

| | Sebelum | Sesudah |
|---|---|---|
| Throat | 19,5 mm | 20,2 mm |
| Luas throat | 597 mm² | 641 mm² (+7,4%) |
| CFM @28" | 84,5 | 90,7 |
| Potensi HP | 38,0 | ~41 |

**Ini satu-satunya perubahan yang menaikkan plafon.** Bentuk port tidak bisa melakukannya.

### 30.4 Spek final

| Bagian | Nilai |
|---|---|
| **Throat in / ex** | 20,2 / 16,7 mm |
| **Port isap** | 615–665 mm², oval 22,7 W × 29,5 H |
| **Short-turn radius** | ≥ 11,8 mm |
| **Bowl maksimum** | 669 mm² |
| **Port buang** | 594–653 mm², Ø setara ~28 mm |
| **Cam in** | 261° @1mm, buka 28 BTDC, tutup 53 ABDC |
| **Cam ex** | 261° @1mm, buka 53 BBDC, tutup 28 ATDC |
| **ICL / LSA** | 102,5° ATDC / 102,5° |
| **Overlap** | 55° |
| **Lift in / ex** | 9,0 / 7,6–9,0 mm |
| **Lift di TDC** | 0,97 mm per klep in |
| **CR statis** | 14:1 (DCR 12,07, margin +0,76) |
| **Kantong klep** | 2,71 mm |
| **Dome piston** | usir 2,45 cc |
| **Throttle body** | 36 mm |
| **Runner isap** | 155 mm |
| **Header dalam** | 29,1 mm |
| **Bahan bakar** | bensol / avgas 100LL |
| **RPM sasaran** | 12.000 |

### 30.5 Verifikasi silang yang berhasil

| Pemeriksaan | Hasil |
|---|---|
| ICL dari time-area vs dari cam acuan | 102,5 vs 102,5 — identik |
| CSA port: jangkar kecepatan vs jangkar rasio | 615 vs 663 mm² — selisih 7,8% |
| Rasio throat ex/in vs acuan | 0,685 vs 0,671 — selisih 2,1% |
| Beban g di TDC vs acuan | 6.093 vs 6.052 — selisih 0,7% |
| DCR vs batas terbukti | 12,07 vs 12,83 — margin +0,76 |

Semua konsisten. Ini yang memberi kepercayaan bahwa spek ini bukan tebakan.

### 30.6 Hasil CFD

| | Cf | K | CFM @28" |
|---|---|---|---|
| Pipa lurus (kontrol) | 0,879 | 0,295 | — |
| Port CSA 615, aspect 1,30 | 0,849 | 0,387 | 124 (2 cabang) |

## 31. Alternatif: Vespa iGet 3-klep

### 31.1 Spesifikasi standar

| | |
|---|---|
| Bore × stroke | 58 × 58,6 mm = 154,8 cc |
| Katup | 3 klep (2 in + 1 ex) |
| Pendingin | **udara** |
| CR | 10,5:1 |
| Tenaga | 12,7 HP @ 7.750 rpm = 82 HP/L |

### 31.2 Perbandingan arsitektur

| | 3-klep | 4-klep 150cc |
|---|---|---|
| **Luas klep in / bore** | **0,262** | **0,295** |
| Rasio throat ex/in | 0,679 | 0,661 |
| Lift kritis in | 4,59 mm | 4,81 mm |
| **Lift kritis ex** | **5,03 mm** | 3,68 mm |

### 31.3 Temuan

**Kelemahan pokoknya ada di sisi isap, bukan buang.** Ini sering disalahpahami. Rasio throat ex/in-nya 0,679 — praktis sama dengan 0,671 yang terbukti. Sisi buangnya sehat.

Yang berkurang adalah sisi isap: 0,262 vs 0,295, **minus 11%**. Klep buang tunggal yang besar memakan lahan bore, sehingga dua klep isapnya harus mengecil.

Konsekuensinya di durasi cam:

| RPM | v port isap | Durasi in |
|---|---|---|
| 10.000 | 89 m/s | 238° |
| 12.000 | 98 m/s | **285°** |

285° vs 261° untuk 4-klep. Durasi lebih panjang = overlap lebih besar = pita lebih sempit.

**Klep buang butuh lift lebih tinggi dari klep isap** — kebalikan dari 4-klep. Satu klep besar punya keliling total lebih kecil daripada dua klep kecil berluas sama.

### 31.4 Potensi

Dengan klep isap maksimum yang muat (21,5 mm):

| | |
|---|---|
| Throat | 20,1 mm |
| Luas throat | 632 mm² |
| CFM @28" | 89 |
| Potensi HP | ~40 |
| Per cc | 3,91 mm²/cc |

Bandingkan: build 4-klep 4,28 mm²/cc, acuan 2-klep 3,31 mm²/cc.

**Head iGet yang dikembangkan penuh bernapas 18% lebih lega per cc daripada mesin yang sekarang menempuh 15,4 detik.** Di bawah 4-klep (−9%), tapi jelas di atas basis 2-klep.

### 31.5 Batasan khusus

1. **Klep buang tunggal + pendingin udara.** Satu klep memikul seluruh panas tanpa bantuan air.
2. **Busi tidak di tengah.** Ruang bakar asimetris, jalur api ke sisi isap panjang. Ini yang membatasi kompresi — disarankan **12,5–13:1**, bukan 14:1.
3. **Semua yang standar harus diganti.** CR 10,5 → 12,5+, cam standar puncaknya 7.750 rpm, ECU ada rev limit.
4. **Ketersediaan part.** Pertanyaan praktis, bukan teknis.

---

# LAMPIRAN

## A. Rumus ringkas

### Geometri
```
Vd            = π/4 × bore² × stroke × n_silinder
Vc            = Vd / (CR − 1)
A_piston      = π/4 × bore²
A_klep        = n × π/4 × D_klep²
A_throat      = n × π/4 × D_throat²
A_tirai       = n × π × D_klep × lift
lift_kritis   = A_throat / (n × π × D_klep)
```

### Kinematika
```
MPS           = 2 × stroke[m] × rpm / 60
s(θ)          = r(1 − cos θ) + L − √(L² − (r sin θ)²)
a_TDC         = ω² × r × (1 + r/L)
```

### Aliran
```
MGV           = (A_piston / CSA) × MPS
Q_rata2       = Vd × (rpm/60) / 2 × VE
duty          = n_sil × durasi / 720
Q_puncak      = Q_rata2 / duty × (π/2)
Cf            = Q_nyata / (A_throat × √(2Δp/ρ))
K             = (v_teoretis / v_nyata)² − 1
```

### Kompresi
```
DCR           = 1 + (V_sapu_IVC / Vd) × (CR − 1)
CR_untuk_DCR  = 1 + (DCR − 1) × Vd / V_sapu_IVC
η_ideal       = 1 − 1/CR^0,4
```

### Cam
```
durasi        = buka + 180 + tutup
overlap       = IVO_BTDC + EVC_ATDC
ICL           = durasi_in/2 − IVO_BTDC
LSA           = (ICL + ECL)/2
lift(θ)       = lift_maks × sin²(π θ / durasi)       [pendekatan harmonik]
durasi_baru   = durasi_acuan × (A_thr_acuan/A_thr_baru)
                              × (Vd_baru/Vd_acuan)
                              × (rpm_baru/rpm_acuan)
```

### Gelombang
```
c             = 20,05 × √(T[K])
L_runner      = c × durasi / (12 × n × rpm)
L_header      = c_gas × (180 + EVO) / (12 × n × rpm)
L_efektif     = L_fisik + k × jari-jari      [k: 0,61 polos, 0,85 bellmouth]
```

### Konversi
```
CFM           = m³/s × 2118,88
CFM_28        = CFM_10 × √2,8
1 inH₂O       = 249,089 Pa
```

## B. Daftar perkakas hitung

Semua ada di direktori `tools/`, ditulis dengan Python. Tiap berkas punya `_selfcheck()` yang harus lolos sebelum hasilnya dipakai.

| Berkas | Fungsi |
|---|---|
| `port_design.py` | sizing klep, throat, port, kalibrasi ke mesin acuan |
| `intake_tune.py` | panjang runner, Helmholtz, wave tuning |
| `tract_profile.py` | profil luas sepanjang saluran, perbandingan TB |
| `cam_design.py` | DCR, durasi, overlap, kantong klep, anggaran ruang bakar |
| `cam_dari_acuan.py` | urai timing acuan, skalakan ke mesin baru |
| `kompresi_terkalibrasi.py` | batas DCR dari mesin terbukti |
| `spek_final.py` | rangkuman spek + beban mekanis |
| `exhaust_check.py` | proporsi ex/in, keputusan durasi ex |
| `exhaust_system.py` | port buang, header, harmonik panjang |
| `head_3klep.py` | sizing head 3-klep |
| `iget150.py` | baseline dan potensi Vespa iGet |
| `bandingkan_mesin.py` | perbandingan F1/MotoGP/Pro Stock |
| `hp_per_liter.py` | tenaga spesifik, perkiraan HP dari lintasan |
| `port_geom.py` | generator volume fluida port untuk CFD |
| `cfd_case.py` | pembangun case OpenFOAM |
| `report_case.py` | tarik hasil CFD, periksa kelayakan |
| `slice_fig.py` | irisan medan CFD |
| `diag_profil.py` | profil kecepatan melintang bertanda |

## C. Daftar periksa build

### Sebelum merancang
- [ ] Ukur bore, stroke, panjang rod mesin acuan **dan** mesin baru
- [ ] Ukur diameter klep in dan ex
- [ ] Ukur diameter dalam seat (throat) in dan ex
- [ ] Ukur CSA port di titik tersempit
- [ ] Catat timing cam lengkap (bukan cuma durasi)
- [ ] Catat kompresi statis dan bahan bakar
- [ ] Ukur panjang runner isap dan panjang header
- [ ] Catat rpm tenaga puncak dan hasil terukur

### Saat merancang
- [ ] Hitung DCR terbukti dari mesin acuan → itu batas bahan bakarmu
- [ ] Tentukan rpm sasaran dari mean piston speed yang sudah terbukti
- [ ] Hitung durasi dari time-area, bukan dari aturan jempol
- [ ] Periksa silang ICL dengan cam acuan
- [ ] Hitung CSA port dengan **dua** jangkar; kalau berbeda jauh, cari asumsi busuk
- [ ] Periksa rasio port/throat — jangan sampai port lebih kecil dari throat
- [ ] Hitung kantong klep **sebelum** menghitung dome piston
- [ ] Hitung anggaran volume ruang bakar lengkap
- [ ] Periksa beban g di TDC terhadap mesin yang sudah terbukti

### Sebelum memutar mesin
- [ ] **Cek clay untuk kelegaan klep-piston** — wajib, tanpa pengecualian
- [ ] Verifikasi volume ruang bakar dengan buret
- [ ] Periksa lebar seat, terutama sisi buang
- [ ] Periksa kelegaan per klep pada lift maksimum
- [ ] Periksa massa piston terhadap perhitungan gaya inersia

### Setelah jalan
- [ ] Baca busi dan kondisi piston setelah run pertama
- [ ] Uji variasi panjang header ±50 mm
- [ ] Kalibrasi ulang model dengan hasil dyno kalau ada

## D. Data terukur vs asumsi

Tabel ini penting untuk kejujuran intelektual. Jangan memperlakukan semua angka di buku ini sama.

### Terukur — dipercaya

| Data | Nilai |
|---|---|
| Acuan: bore × stroke | 63 × 64 mm |
| Acuan: klep in / ex | 31 / 27 mm |
| Acuan: throat in | 29 mm |
| Acuan: port in / ex | 29,5 / 29 mm |
| Acuan: lift | 10,8 mm |
| Acuan: timing cam | 38/63/63/38 |
| Acuan: CR statis | 16:1 |
| Acuan: bahan bakar | bensol / avgas 100LL |
| Acuan: TB / header / muffler | 38 / 30 / 50 mm |
| Acuan: hasil | 500 m 15,4 s @ 158 km/h |
| Baru: bore × stroke × rod | 57,3 × 58 × 95 mm |
| Baru: klep in / ex | 22 / 19 mm |
| Vario 150: manifold | port 30,2 → TB 38, panjang 43 mm, belok 34° |
| iGet: bore × stroke, CR, tenaga | 58 × 58,6, 10,5:1, 12,7 HP |

### Asumsi — verifikasi sebelum dipakai

| Data | Nilai dipakai | Catatan |
|---|---|---|
| Acuan: panjang rod | 105 mm | pengaruh ke DCR kecil (±0,07) |
| Acuan: throat ex | 0,88 × klep | tidak diukur |
| Acuan: panjang header | tidak diketahui | **paling penting untuk diukur** |
| Acuan: massa motor + rider | 150 kg | menggeser perkiraan HP ±10% |
| Acuan: CdA | 0,35 | menggeser perkiraan HP |
| Baru: tinggi pent-roof | 3,5 mm | menggeser anggaran ruang bakar |
| Baru: tebal gasket | 0,8 mm | ukur |
| Baru: deck clearance | 0,5 mm | ukur |
| F1/MotoGP/Pro Stock: klep & port | proporsi lazim | **bukan data pabrik** |
| iGet: diameter klep | 21 / 26 mm | **bukan data pabrik** |
| Kecepatan suara gas buang | 650 m/s | ±8% ketidakpastian |
| Koefisien rugi butterfly | K = 0,25 | perkiraan |

### Dari CFD — kuat untuk membandingkan

| Data | Nilai |
|---|---|
| Cf pipa lurus (kontrol) | 0,879 |
| Cf port 615/1,30/0,40 | 0,849 |
| Koefisien rugi port | K = 0,387 |
| Ongkos tikungan 37° | 3,4% |

---

## PENUTUP

Ada satu benang yang menyatukan seluruh buku ini, dan layak ditulis ulang di akhir:

> **Ukur mesinmu sendiri. Itu sumber data terbaik yang kamu punya.**

Setiap kali buku ini bisa memilih antara tabel umum dan pengukuran dari mesin yang sudah terbukti jalan, pengukuran yang menang — dan setiap kali, tabel umum ternyata meleset dengan cara yang merugikan:

- Rasio throat: buku bilang maksimum 0,90, mesin nyata jalan di 0,935 → **7,4% flow hilang** kalau menurut buku
- Kecepatan throttle body: buku bilang 105 m/s, mesin nyata di 61 → **TB 8 mm terlalu kecil** kalau menurut buku
- Batas kompresi dinamis: buku bilang 12,5 maksimum untuk bensin, mesin nyata di 12,83 → **kompresi diturunkan tanpa perlu** kalau menurut buku
- Lift maksimum berguna: buku bilang 0,25 × diameter klep, mesin balap jalan di 1,6–2,5× lift kritis → **cam terlalu jinak** kalau menurut buku

Empat dari empat. Bukan karena bukunya salah, tapi karena buku itu ditulis untuk mesin lain.

Dan pelajaran kedua, dari bagian CFD:

> **Diagnostik yang hijau bukan bukti hasilnya benar.** Periksa kewarasan fisikanya, dan lihat datanya sendiri — bukan cuma ringkasannya.

Sebelas simulasi berturut-turut memberi hasil salah sementara setiap indikator numerik menyatakan sehat. Yang membongkarnya cuma dua hal: satu angka yang tidak masuk akal, dan keberanian untuk melihat medan alirannya langsung.

---

*Dokumen ini disusun tanpa gambar. Diagram, grafik, dan visualisasi medan CFD dapat ditambahkan pada revisi berikutnya.*
