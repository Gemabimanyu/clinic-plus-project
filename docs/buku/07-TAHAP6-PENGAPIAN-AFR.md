# TAHAP 6 — PENGAPIAN DAN CAMPURAN

*Bagian paling murah untuk menambah tenaga, dan paling cepat merusak mesin kalau salah.*

---

## 1. Stoikiometri dan AFR

### 1.1 Definisi

**AFR** (*Air-Fuel Ratio*) adalah perbandingan massa udara terhadap massa bahan bakar.

**Stoikiometri** adalah AFR di mana semua bahan bakar dan semua oksigen habis bereaksi — tidak ada sisa.

| Bahan bakar | AFR stoikiometri |
|---|---|
| Bensin | 14,70 |
| Avgas 100LL | 14,90 |
| Race gas beroksigen | ~12,90 |
| Metanol | 6,45 |
| Nitrometana | 1,70 |

### 1.2 Lambda — dan kenapa lebih berguna

```
λ = AFR / AFR_stoikiometri
```

| λ | Artinya |
|---|---|
| 1,00 | stoikiometri |
| < 1,00 | kaya |
| > 1,00 | miskin |

**Kenapa lambda lebih berguna daripada AFR:**

Angka AFR tenaga puncak berbeda-beda tiap bahan bakar — 12,5 untuk bensin, 4,8 untuk metanol. Tapi dalam lambda, semuanya berkumpul di **0,74–0,89**.

Artinya kalau kamu pindah bahan bakar, **target lambda-mu hampir tidak berubah** sementara target AFR berubah total.

> **Selalu setel dan catat dalam lambda kalau alatmu mendukung.** Ini menghilangkan satu sumber kesalahan besar.

**Kesalahan yang sering terjadi:** memakai race gas beroksigen dengan mapping AFR bensin biasa. Karena stoikiometrinya 12,9 bukan 14,7, campuran yang dikira "12,5 kaya" sebenarnya **λ 0,97 — hampir stoikiometri**, jauh terlalu miskin untuk beban penuh.

---

## 2. AFR untuk torsi dan tenaga

### 2.1 Kurva torsi terhadap lambda

Torsi mencapai puncak pada campuran yang **sedikit kaya**, bukan stoikiometri.

| λ | Torsi relatif | Keterangan |
|---|---|---|
| 1,10 | ~96% | miskin, hemat, panas |
| 1,00 | ~98% | stoikiometri |
| **0,87** | **100%** | **puncak torsi** |
| 0,80 | ~99% | kaya, lebih dingin |
| 0,70 | ~95% | terlalu kaya, boros |

Kurvanya **datar di sekitar puncak** — antara λ 0,80 dan 0,90 selisih torsinya cuma 1%.

### 2.2 Kenapa puncaknya di sisi kaya

Pencampuran udara-bahan bakar di silinder tidak pernah sempurna. Sedikit kelebihan bahan bakar memastikan setiap molekul oksigen menemukan pasangan.

Kelebihan bahan bakar juga **mendinginkan muatan** lewat penguapan, menaikkan kerapatan dan menambah margin detonasi.

### 2.3 Target praktis

| Kondisi | λ | AFR bensin |
|---|---|---|
| Idle | 0,98–1,02 | 14,4–15,0 |
| Cruise, hemat | 1,00–1,05 | 14,7–15,4 |
| Beban sedang | 0,90–0,95 | 13,2–14,0 |
| **Beban penuh, tenaga puncak** | **0,85–0,88** | **12,5–12,9** |
| **Beban penuh, margin aman** | **0,80–0,85** | **11,8–12,5** |
| Kompresi sangat tinggi / panas | 0,78–0,82 | 11,5–12,1 |

**Untuk drag dengan kompresi tinggi:** setel di **λ 0,80–0,85**. Kehilangan torsi cuma ~1% dibanding puncak, tapi margin detonasi dan pendinginan piston jauh lebih baik.

Satu persen tenaga jauh lebih murah daripada satu piston.

### 2.4 Mengukur AFR

**Wideband lambda sensor wajib.** Sensor narrowband bawaan motor hanya akurat di sekitar λ 1,00 — tidak berguna untuk beban penuh.

**Posisi pemasangan:**
- Di header, 15–30 cm dari klep buang
- Miring ke atas minimal 10° supaya kondensasi tidak menggenang di sensor
- Jangan terlalu dekat ke ujung knalpot — udara luar bisa masuk dan bikin pembacaan miskin palsu

**Peringatan avgas:** bahan bakar bertimbal **memperpendek umur sensor wideband** secara drastis. Sensor bisa mati dalam hitungan jam pemakaian. Pakai untuk sesi tuning saja, lepas setelahnya.

---

## 3. Sudut pengapian (spark angle)

### 3.1 MBT

**MBT** = *Minimum advance for Best Torque* — sudut pengapian paling kecil yang sudah memberi torsi maksimum.

| Kondisi | Akibat |
|---|---|
| Kurang maju dari MBT | tenaga hilang, EGT naik, panas terbuang ke knalpot |
| Tepat di MBT | tenaga maksimum |
| Lebih maju dari MBT | tenaga **turun** dan risiko detonasi naik |

**Poin penting:** memajukan pengapian melewati MBT **tidak menambah tenaga**. Ia cuma menambah tekanan puncak dan risiko. Ini kesalahpahaman yang sangat umum — "makin maju makin kencang" salah.

### 3.2 Apa yang menggeser MBT

| Faktor | Efek pada MBT |
|---|---|
| RPM naik | **lebih maju** — durasi bakar tetap dalam milidetik, tapi lebih banyak derajat crank berlalu |
| Beban naik (throttle lebih besar) | **kurang maju** — muatan padat terbakar lebih cepat |
| Kompresi naik | **kurang maju** — muatan padat terbakar lebih cepat |
| Campuran lebih miskin | **lebih maju** — bakar lebih lambat |
| Campuran lebih kaya (dari stoich) | sedikit lebih maju |
| Squish bagus / turbulensi tinggi | **kurang maju** |
| Busi di tengah (4 klep) | **kurang maju** dari 2 klep |
| Bore besar | lebih maju — jalur api panjang |

### 3.3 Rentang khas

Untuk mesin 1 silinder kecil kompresi tinggi pada tenaga puncak:

| Kompresi | Sudut khas di rpm puncak |
|---|---|
| 10–11:1 | 30–36° BTDC |
| 12–13:1 | 26–32° BTDC |
| 14–15:1 | 22–28° BTDC |
| Metanol 15:1+ | 28–36° BTDC (bakar lebih lambat) |

**Perhatikan metanol:** walau kompresinya lebih tinggi, metanol butuh pengapian **lebih maju** karena kecepatan bakarnya lebih lambat dari bensin.

### 3.4 Mencari MBT di dyno

1. Mulai dari sudut yang **konservatif** (5–8° di bawah perkiraan)
2. Naikkan **2° per run**
3. Catat torsi tiap run
4. Berhenti saat torsi **berhenti naik** — itu MBT
5. Mundurkan **2°** dari situ sebagai margin

**Kalau detonasi muncul sebelum torsi berhenti naik**, mesinmu *knock-limited*. Artinya kamu tidak bisa mencapai MBT dengan bahan bakar itu. Pilihan: bahan bakar oktan lebih tinggi, kompresi turun, atau terima tenaga yang ada.

**Jangan pernah** mencari MBT dengan menaikkan 5° sekaligus. Detonasi bisa merusak dalam hitungan detik.

### 3.5 Bentuk kurva pengapian

Kurva pengapian yang benar untuk mesin balap kecil, kira-kira:

| RPM | Sudut relatif |
|---|---|
| Idle (1.500) | 10–15° BTDC |
| 3.000 | naik cepat |
| 5.000–7.000 | mendekati puncak |
| 8.000–puncak | datar atau sedikit turun |

Setelah rpm tenaga puncak, sudut sering **diturunkan sedikit** karena efisiensi pengisian turun dan risiko detonasi berubah.

---

## 4. Sudut injeksi (injection angle)

### 4.1 Apa yang diatur

Bukan berapa banyak bahan bakar, tapi **kapan** disemprotkan dalam siklus. Biasanya yang diatur adalah **akhir injeksi** (*end of injection*, EOI).

### 4.2 Dua strategi

**Injeksi klep tertutup** (*closed-valve injection*)

Bahan bakar disemprot ke punggung klep isap yang masih tertutup. Bahan bakar punya waktu menguap sebelum klep membuka.

| Kelebihan | Kekurangan |
|---|---|
| Pencampuran lebih baik | pendinginan muatan lebih kecil |
| Bagus untuk rpm rendah-menengah | sebagian bahan bakar menempel dinding port |
| Respons throttle lebih halus | pada rpm tinggi waktunya tidak cukup |

**Injeksi klep terbuka** (*open-valve injection*)

Bahan bakar disemprot saat klep isap sedang terbuka, langsung masuk ke silinder.

| Kelebihan | Kekurangan |
|---|---|
| **Pendinginan muatan lebih besar** | pencampuran kurang merata |
| Tidak ada bahan bakar membasahi dinding | respons rpm rendah kurang halus |
| Lebih baik di rpm tinggi | butuh atomisasi injektor yang bagus |

### 4.3 Praktisnya

Pada rpm tinggi, waktu satu siklus sangat pendek sehingga **injeksi klep tertutup menjadi mustahil** — durasi injeksi sudah memakan sebagian besar siklus.

Untuk mesin balap putaran tinggi, injeksi otomatis jatuh ke mode klep terbuka atau campuran keduanya.

**Yang bisa ditala:**
- Pada rpm rendah-menengah, geser EOI untuk mencari respons terbaik
- Pada rpm tinggi, geser EOI untuk mencari torsi terbaik — bisa memberi 1–3%

**Peringatan:** tidak semua ECU standar mengizinkan pengaturan sudut injeksi. Ini salah satu alasan pindah ke ECU aftermarket.

### 4.4 Posisi injektor

| Posisi | Karakter |
|---|---|
| Dekat klep, menyemprot ke punggung klep | standar pabrikan, pencampuran baik |
| Lebih jauh di runner | pencampuran lebih baik, pendinginan lebih merata |
| **Injektor kedua di velocity stack** | dipakai balap — injektor utama untuk rpm rendah, injektor atas untuk rpm tinggi |

Sistem dua injektor (*staged injection*) memberi pendinginan muatan maksimum di rpm tinggi tanpa mengorbankan respons rendah. Butuh ECU yang mendukung.

---

## 5. Busi

### 5.1 Heat range

**Heat range** menunjukkan seberapa cepat busi membuang panas ke kepala silinder. Bukan seberapa "panas" apinya.

| Busi | Karakter |
|---|---|
| **Panas** (heat range rendah) | insulator panjang, panas lambat keluar, tahan kotor |
| **Dingin** (heat range tinggi) | insulator pendek, panas cepat keluar, tahan beban tinggi |

**Konvensi angka:** pada merek Jepang yang umum, **angka lebih besar = lebih dingin**. Merek lain bisa terbalik — selalu cek katalognya.

### 5.2 Memilih heat range

**Aturan praktis:** satu tingkat lebih dingin untuk tiap kenaikan besar pada kompresi atau tenaga.

| Kondisi | Arah |
|---|---|
| Kompresi naik 2+ angka | 1 tingkat lebih dingin |
| Tenaga naik 50%+ | 1 tingkat lebih dingin |
| Balap durasi panjang | 1 tingkat lebih dingin |
| Sering idle dan rpm rendah | jangan terlalu dingin |

**Gejala terlalu panas:**
- Insulator putih bersih atau melepuh
- Elektroda meleleh atau membulat
- Pre-ignition (mesin menyala sendiri sebelum busi memercik)

**Gejala terlalu dingin:**
- Busi basah dan berjelaga
- Misfire di rpm rendah
- Susah start

**Untuk drag:** condong ke **lebih dingin**. Mesin cuma jalan beberapa detik, jadi masalah fouling tidak sempat terjadi, sementara beban puncaknya ekstrem.

### 5.3 Gap

| Kondisi | Gap |
|---|---|
| Standar | 0,7–0,9 mm |
| Kompresi tinggi | 0,6–0,7 mm |
| Kompresi sangat tinggi / metanol | 0,5–0,6 mm |

**Kenapa gap dikecilkan pada kompresi tinggi:** muatan yang padat lebih sulit diionisasi. Tegangan yang dibutuhkan untuk melompati gap naik seiring tekanan. Kalau gap terlalu besar, percikan bisa gagal tepat saat paling dibutuhkan.

**Tapi jangan terlalu kecil** — gap kecil memberi kernel api kecil, yang bisa memperlambat awal pembakaran.

### 5.4 Bahan elektroda

| Bahan | Karakter |
|---|---|
| **Tembaga** | konduktivitas panas terbaik, elektroda tebal, umur pendek |
| **Platinum** | umur panjang, elektroda sedang |
| **Iridium** | elektroda sangat halus → tegangan nyala lebih rendah, umur panjang |

**Untuk balap: tembaga.** Umurnya pendek tapi pembuangan panasnya terbaik dan harganya murah — dan busi balap memang harus sering diganti dan dibaca.

Iridium bagus untuk harian karena umurnya panjang, tapi elektroda halusnya lebih rentan terkikis oleh detonasi.

### 5.5 Membaca busi

Ini keterampilan diagnostik paling murah yang kamu punya.

**Cara yang benar:**
1. Pasang busi baru
2. Lakukan run beban penuh sampai rpm puncak
3. **Matikan mesin dan tarik kopling di rpm tinggi** — jangan idle dulu
4. Lepas busi dan baca segera

Kalau mesin dibiarkan idle sebelum dimatikan, jejak beban penuh terhapus.

**Yang dibaca:**

| Bagian | Yang dilihat |
|---|---|
| Ujung insulator | warna — coklat muda = baik |
| Dasar insulator (cincin) | jejak bahan bakar — cincin gelap tipis = baik |
| Elektroda ground | warna berubah sampai seberapa jauh = indikator timing |
| Titik hitam kecil | **detonasi** |
| Butiran logam mengkilap | **detonasi berat — hentikan segera** |

---

## 6. Koil pengapian

### 6.1 Tiga jenis

**TCI — *Transistor Controlled Ignition* (induktif)**

Energi disimpan dalam medan magnet koil selama *dwell*, lalu dilepas saat arus diputus.

| | |
|---|---|
| Durasi percikan | **panjang** (1–2 ms) |
| Kecepatan naik tegangan | sedang |
| Batasan | butuh waktu dwell — di rpm sangat tinggi bisa kurang |
| Umum di | motor injeksi modern |

**CDI — *Capacitor Discharge Ignition***

Energi disimpan di kapasitor, dilepas sekaligus.

| | |
|---|---|
| Durasi percikan | **pendek** (0,1–0,3 ms) |
| Kecepatan naik tegangan | **sangat cepat** |
| Kelebihan | tidak terpengaruh busi kotor, tidak butuh dwell |
| Kekurangan | durasi pendek — bisa gagal menyalakan muatan yang tidak merata |
| Umum di | motor 2 langkah, motor lama |

**Smart coil (koil dengan driver terintegrasi)**

Tipe induktif dengan transistor penggerak di dalam koil, dipasang langsung di busi.

| | |
|---|---|
| Durasi percikan | panjang |
| Energi | **tertinggi** |
| Rugi kabel tegangan tinggi | **tidak ada** — koil menempel di busi |
| Kekurangan | butuh sinyal kontrol dari ECU yang sesuai |

### 6.2 Mana yang dipilih

Untuk mesin kompresi tinggi berputaran tinggi, dua hal dibutuhkan **bersamaan**:

1. **Tegangan tinggi** — karena muatan padat sulit diionisasi
2. **Durasi cukup** — karena muatan mungkin tidak tercampur sempurna

| Kondisi | Pilihan |
|---|---|
| Kompresi tinggi, rpm tinggi | **smart coil** atau TCI berenergi tinggi |
| Metanol | **smart coil** — metanol butuh energi lebih besar |
| RPM sangat tinggi (14.000+) | CDI atau smart coil (dwell jadi kendala) |
| Motor standar, tune ringan | TCI standar cukup |

**CDI sendirian sering kurang** untuk mesin 4 langkah kompresi tinggi, karena durasi percikannya terlalu pendek.

### 6.3 Yang sering diabaikan

- **Kabel massa.** Sistem pengapian butuh jalur massa yang pendek dan bersih. Massa yang buruk menyebabkan misfire yang sulit dilacak.
- **Tegangan aki.** Koil induktif sangat sensitif terhadap tegangan. Aki lemah = energi percikan turun drastis di rpm tinggi.
- **Kabel busi.** Kabel resistif yang tua kehilangan energi. Kalau masih pakai kabel, ganti berkala.

---

## 7. ECU

### 7.1 Batasan ECU standar

| Batasan | Akibat |
|---|---|
| **Resolusi map kasar** | titik breakpoint sedikit → interpolasi kasar di antara titik |
| **Rev limiter terkunci** | tidak bisa ke rpm sasaran |
| **Closed loop dipaksa ke stoikiometri** | di beban tertentu ECU menarik campuran ke λ 1,00 walau kamu ingin lebih kaya |
| **Rentang pengapian terbatas** | tidak bisa memundurkan atau memajukan cukup jauh |
| **Sudut injeksi tidak bisa diubah** | kehilangan 1–3% |
| **Tidak ada datalogging** | tuning jadi buta |
| **Limiter keselamatan** | ECU menarik tenaga saat mendeteksi kondisi "aneh" |
| **Tidak mendukung injektor besar** | kalau injektor diganti, kalibrasi kacau |
| **Terkunci / terenkripsi** | tidak bisa diprogram sama sekali |

### 7.2 Tiga tingkat solusi

**Tingkat 1 — Remap ECU standar**

Mengubah isi tabel di dalam ECU asli.

| Bisa | Tidak bisa |
|---|---|
| Ubah nilai bahan bakar dan pengapian | menambah resolusi map |
| Naikkan rev limit (kadang) | menambah fitur baru |
| Matikan closed loop (kadang) | mengubah sudut injeksi |
| Murah, rapi, reversibel | mengatasi keterbatasan struktural |

**Cocok untuk:** tune ringan sampai menengah, mesin masih mendekati standar.

**Tingkat 2 — Piggyback**

Alat tambahan yang mencegat sinyal sensor dan memodifikasinya sebelum sampai ke ECU standar.

| Kelebihan | Kekurangan |
|---|---|
| Murah | ECU asli masih berjalan dengan logikanya sendiri |
| Reversibel | bisa terjadi interaksi aneh antara dua sistem |
| Tidak perlu ubah wiring | tidak bisa mengatasi limiter dan closed loop dengan bersih |
| | tuning jadi menebak-nebak: kamu mengubah sinyal, bukan hasil |

**Piggyback adalah kompromi.** Berguna kalau ECU asli terkunci dan budget terbatas, tapi jangan berharap kontrol penuh.

**Tingkat 3 — ECU aftermarket standalone**

Mengganti ECU asli sepenuhnya.

| Kemampuan yang didapat |
|---|
| Kontrol penuh map bahan bakar dan pengapian |
| Resolusi map jauh lebih tinggi |
| Rev limit bebas |
| **Sudut injeksi bisa diatur** |
| Closed loop dengan wideband, target lambda bebas |
| Datalogging lengkap |
| Launch control, shift light, dua map |
| Dukungan injektor besar dan dua injektor |
| Knock control (sebagian) |
| Kontrol koil yang lebih baik |

| Ongkosnya |
|---|
| Harga jauh lebih mahal |
| Butuh wiring ulang |
| **Butuh tuner yang paham** — ECU canggih di tangan yang salah lebih berbahaya daripada ECU standar |
| Fitur motor lain (imobilizer, panel) bisa hilang |

### 7.3 Kapan naik tingkat

| Kondisi mesin | Cukup dengan |
|---|---|
| Knalpot + filter, cam standar | remap standar |
| Cam ringan, kompresi naik sedikit | remap atau piggyback |
| Cam balap, kompresi tinggi, rpm naik | **standalone** |
| Metanol atau race gas beroksigen | **standalone** |
| Dua injektor | **standalone** |

**Aturan praktisnya:** kalau rpm sasaranmu melewati rev limit standar, atau kamu ganti bahan bakar yang stoikiometrinya berbeda, ECU standar sudah tidak cukup.

### 7.4 Yang tidak berubah walau ECU-nya canggih

ECU tidak menambah udara. Ia cuma mengatur bahan bakar dan pengapian untuk udara yang sudah masuk.

> **ECU mahal di mesin yang head-nya belum benar tidak akan memberi tenaga.** Urutan tetap: head → cam → kompresi → baru ECU.

---

## 8. Urutan tuning di dyno

Kalau semua sudah terpasang, urutan penyetelan yang benar:

**1. Pastikan mekanis sehat dulu.** Kompresi tiap silinder, kebocoran, celah klep. Tuning mesin yang bocor cuma menyembunyikan masalah.

**2. Setel bahan bakar kasar** ke λ aman (0,82–0,85) di seluruh rentang. Jangan tuning pengapian dengan campuran yang salah.

**3. Cari MBT pengapian** di beberapa titik rpm, naik 2° per run.

**4. Haluskan bahan bakar** di sekitar rpm puncak untuk torsi maksimum.

**5. Ulangi 3 dan 4 sekali lagi** — keduanya saling mempengaruhi.

**6. Setel sudut injeksi** kalau ECU mendukung.

**7. Terakhir, mundurkan pengapian 2°** sebagai margin keselamatan.

**Satu perubahan per run.** Ini aturan yang paling sering dilanggar dan paling merugikan.

---

## 9. Ringkasan Tahap 6

1. **Pakai lambda, bukan AFR.** Target λ hampir sama untuk semua bahan bakar.
2. **Puncak torsi di λ 0,87**, tapi kurvanya datar — λ 0,80–0,85 cuma kehilangan 1% dengan margin jauh lebih baik.
3. **Wideband wajib.** Narrowband bawaan tidak berguna untuk beban penuh.
4. **Memajukan pengapian melewati MBT menurunkan tenaga**, bukan menambah.
5. **Cari MBT 2° per run.** Kalau detonasi datang duluan, mesinmu knock-limited.
6. **Metanol butuh pengapian lebih maju** walau kompresinya lebih tinggi.
7. **Busi: lebih dingin untuk kompresi tinggi, gap lebih kecil, tembaga untuk balap.**
8. **Baca busi setelah run beban penuh**, jangan setelah idle.
9. **Smart coil untuk kompresi tinggi.** CDI sendirian sering kurang durasinya.
10. **ECU standalone dibutuhkan** kalau rpm melewati limit standar atau bahan bakar berganti.
11. **ECU tidak menambah udara.** Head dulu, ECU terakhir.

**Berikutnya:** Tahap 7 — saluran masuk dan buang, tempat gelombang tekanan bekerja.
