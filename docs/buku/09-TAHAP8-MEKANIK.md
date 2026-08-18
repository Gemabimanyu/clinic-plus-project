# TAHAP 8 — MEKANIK, MATERIAL, DAN KEANDALAN

*Supaya yang sudah dibangun tidak jebol.*

---

## 1. Batas mekanis

### 1.1 Kecepatan piston

```
MPS = 2 × stroke[m] × rpm / 60
```

| MPS | Keterangan |
|---|---|
| < 20 m/s | aman, bisa harian |
| 20–22 | tinggi, umur pendek tapi wajar untuk drag |
| 22–24 | sangat tinggi, butuh part serius |
| 24–26 | ekstrem |
| 30+ | drag profesional, mesin sekali pakai |

### 1.2 Percepatan piston

```
a_TDC = ω² × r × (1 + r/L)
ω = 2π × rpm / 60,   r = stroke/2,   L = panjang rod
```

Percepatan di TDC selalu lebih besar dari di BDC — faktor `(1 + r/L)` menjadi `(1 − r/L)` di BDC.

**Mesin Contoh B** (stroke 58, rod 95): [HITUNG]

| RPM | g di TDC |
|---|---|
| 11.000 | 5.121 |
| 12.000 | 6.093 |
| 12.500 | 6.612 |
| 13.000 | 7.151 |

### 1.3 Gaya inersia

```
F = massa_bolak_balik × a_TDC
```

Massa bolak-balik = piston + ring + pin + klip + ujung kecil rod.

Pada 12.000 rpm:

| Massa | Gaya di TDC |
|---|---|
| 80 g | 487 kgf |
| 100 g | 609 kgf |
| 120 g | 731 kgf |

Ini beban yang ditahan pin, rod, dan bearing **pada langkah buang** — saat tidak ada tekanan gas yang melawan.

### 1.4 Massa piston adalah tuas paling murah

Turun dari 120 ke 80 gram memangkas beban rod **33%** — setara menurunkan rpm dari 13.000 ke 11.000, **tanpa kehilangan tenaga sedikit pun**.

Kalau mengincar 12.500+ rpm, piston ringan bukan opsi tapi keharusan.

### 1.5 Membandingkan ke mesin yang sudah terbukti

Ini cara paling berguna memakai angka di atas:

| Mesin | RPM | g di TDC |
|---|---|---|
| Contoh A (stroke 64, rod 95) | 11.250 | 6.052 |
| **Contoh B (stroke 58, rod 95)** | **12.000** | **6.093** |

Selisih 0,7%. Artinya 12.000 rpm di Mesin B berada **di dalam amplop yang sudah terbukti**, bukan wilayah baru.

**Selalu bandingkan begini** sebelum memutuskan rpm sasaran. Angka mutlak sulit ditafsirkan; perbandingan ke mesin yang sudah jalan jauh lebih berarti.

---

## 2. Material piston

### 2.1 Jenis

| Jenis | Pemuaian | Kekuatan | Clearance | Cocok untuk |
|---|---|---|---|---|
| **Cor (cast)** | rendah | rendah | 0,0015–0,002 mm/mm | standar, harian |
| **Hypereutectic** | sangat rendah | sedang | 0,0015–0,002 | harian performa |
| **Tempa 4032** (Si 12%) | sedang | tinggi | 0,002–0,0025 | jalanan/balap ringan |
| **Tempa 2618** (Si rendah) | **tinggi** | **tertinggi** | 0,0035–0,005 | balap penuh |

### 2.2 Pertukarannya

**4032** mengandung silikon tinggi → pemuaian rendah → clearance kecil → mesin **lebih senyap saat dingin**, oli lebih sedikit lolos. Kekuatannya cukup untuk sebagian besar aplikasi.

**2618** silikon rendah → lebih ulet, lebih tahan detonasi dan beban kejut → tapi memuai lebih banyak → butuh clearance besar → **berisik saat dingin** dan lebih banyak blowby saat dingin.

**Untuk drag:** 2618 kalau kompresi tinggi dan rpm ekstrem. 4032 kalau mesin juga dipakai jalan.

### 2.3 Clearance piston

```
clearance = faktor × bore
```

Untuk bore 57,3 mm: [HITUNG]

| Material | Faktor | Clearance |
|---|---|---|
| Cast | 0,0015 | 0,086 mm |
| Forged 4032 | 0,002 | 0,115 mm |
| Forged 2618 | 0,004 | 0,229 mm |

**Selalu ikuti angka dari pembuat piston**, bukan tabel umum. Tiap pabrikan punya profil dan gauge point sendiri.

**Cara mengukur:**
1. Ukur bore dengan bore gauge di 3 ketinggian × 2 arah
2. Ukur piston di **gauge point yang ditentukan pabrik** — biasanya di skirt, tegak lurus pin, pada ketinggian tertentu dari bawah
3. Clearance = bore − piston pada titik itu

**Jangan mengukur piston di bagian atas** — piston sengaja dibuat tirus dan oval.

### 2.4 Coating pada piston

**Skirt — coating anti-gesek (moly/grafit)**

| Manfaat | |
|---|---|
| Gesekan turun | 1–3% tenaga |
| Melindungi saat *break-in* | mencegah scuffing |
| Memungkinkan clearance lebih kecil | mesin lebih senyap |
| Menahan oli di permukaan | pelumasan lebih baik |

**Mahkota — thermal barrier (berbasis keramik)**

| Manfaat | |
|---|---|
| Panas dipantulkan kembali ke ruang bakar | efisiensi naik sedikit |
| Suhu piston turun 10–20% | **margin detonasi naik** |
| Melindungi dari detonasi ringan | |

| Risiko | |
|---|---|
| Kalau mengelupas, serpihannya merusak | pastikan aplikator berkualitas |
| Suhu ruang bakar naik | bisa **memperburuk** detonasi kalau tidak diimbangi |

**Bagian bawah piston — oil-shedding coating**

Membuat oli cepat mengalir turun, meningkatkan perpindahan panas dari piston ke oli. Berguna kalau ada oil jet.

---

## 3. Material rod

| Material | Densitas | Kekuatan | Catatan |
|---|---|---|---|
| Baja tempa standar | 7,85 | baik | bawaan pabrik |
| **Baja 4340 tempa** | 7,85 | sangat baik | standar balap |
| **Titanium** | 4,43 | sangat baik | 40% lebih ringan, mahal, butuh perawatan khusus |
| **Aluminium** | 2,70 | sedang | **hanya drag** — umur lelah sangat pendek |

### 3.1 Rod aluminium

Dipakai di drag karena sangat ringan dan **menyerap kejut** — melindungi bearing dari beban detonasi.

**Tapi:**
- Umur lelah dihitung dalam puluhan run, bukan ribuan
- **Memanjang jauh lebih banyak saat panas** — lihat bagian 6
- Harus diganti terjadwal, bukan menunggu rusak

### 3.2 Pengaruh massa rod

Ujung kecil rod ikut dalam massa bolak-balik; ujung besar ikut dalam massa berputar. Rod yang lebih ringan mengurangi keduanya.

Tapi pengaruhnya lebih kecil dari massa piston, karena hanya sebagian rod yang bolak-balik (kira-kira sepertiganya).

---

## 4. Material klep

| Material | Densitas | Karakter |
|---|---|---|
| **Stainless (21-4N, EV8)** | 7,8 | umum, tahan panas cukup, murah |
| **Inconel / Nimonic** | 8,2 | tahan panas tinggi — untuk klep buang beban berat |
| **Titanium** | 4,5 | **40% lebih ringan**, mahal, ujung batang harus dikeraskan |

### 4.1 Kenapa massa klep sangat penting

Percepatan klep di puncak lobe untuk Mesin Contoh B (lift 9 mm, durasi 261°, 12.000 rpm): [HITUNG]

```
percepatan = 13.519 m/s² = 1.378 g
```

Gaya yang harus ditahan per klep:

| Rakitan klep | Massa | Gaya | Per klep dibutuhkan |
|---|---|---|---|
| Stainless + retainer baja | 38 g | 514 N | **73 kgf** |
| Stainless + retainer titanium | 32 g | 433 N | **62 kgf** |
| **Titanium + retainer titanium** | **22 g** | **297 N** | **42 kgf** |

**RPM floating dengan per 65 kgf:**

| Rakitan | Floating di |
|---|---|
| Stainless 38 g | ~13.400 rpm |
| **Titanium 22 g** | **~17.600 rpm** |

Mengganti klep ke titanium menaikkan batas floating **4.200 rpm** dengan per yang sama.

### 4.2 Perhatian klep titanium

- **Ujung batang harus dikeraskan** (biasanya dilapis chrome atau DLC) — titanium lunak dan cepat aus di kontak rocker
- **Seat harus cocok** — titanium tidak boleh langsung ke seat besi cor keras tanpa lapisan
- **Jangan dipakai untuk buang** kecuali dilapis thermal barrier — titanium tidak tahan panas gas buang sebaik Inconel

### 4.3 Coating pada klep

| Bagian | Coating | Manfaat |
|---|---|---|
| Batang | DLC atau chrome | gesekan turun, aus berkurang |
| Muka klep buang | thermal barrier | suhu klep turun, umur naik |
| Payung sisi ruang bakar | thermal barrier | mengurangi transfer panas ke klep |

Coating thermal barrier pada klep buang adalah salah satu perbaikan keandalan paling efektif untuk mesin kompresi tinggi.

---

## 5. Ring piston

### 5.1 Single ring versus double ring

Yang dimaksud adalah jumlah **ring kompresi** (ring oli tetap ada).

| | Single (1 kompresi) | Double (2 kompresi) |
|---|---|---|
| Gesekan | **lebih rendah** — 3–5% total gesekan mesin | lebih tinggi |
| Massa bolak-balik | lebih rendah | lebih tinggi |
| Blowby | lebih tinggi | **lebih rendah** |
| Penyegelan saat beban lama | kurang | **lebih baik** |
| Umur | lebih pendek | lebih panjang |
| Cocok untuk | **drag, sprint pendek** | endurance, harian |

**Untuk drag 500 m** yang cuma 15 detik, single ring masuk akal — blowby yang lebih tinggi tidak sempat jadi masalah, dan gesekan yang lebih rendah langsung jadi tenaga.

**Untuk mesin yang juga dipakai jalan**, double ring lebih tepat.

### 5.2 Ring end gap

```
gap = faktor × bore
```

| Aplikasi | Faktor ring atas | Faktor ring kedua |
|---|---|---|
| Harian NA | 0,0035–0,0045 | 0,0045–0,0055 |
| **Balap NA** | **0,0045–0,0055** | **0,0050–0,0060** |
| Nitrous / turbo | 0,0060–0,0070 | 0,0065–0,0075 |

Untuk bore 57,3 mm, balap NA: [HITUNG]

| Ring | Gap |
|---|---|
| Atas | 0,26–0,32 mm |
| Kedua | 0,29–0,34 mm |

**Ring kedua selalu diberi gap lebih besar dari ring atas.** Kalau lebih kecil, tekanan terperangkap di antara kedua ring dan bisa mengangkat ring atas dari alurnya — *ring flutter*.

**Gap terlalu kecil:** ring memuai saat panas, kedua ujungnya bertemu (*butting*), ring menekan dinding liner → gores dalam, piston rusak.

**Gap terlalu besar:** blowby, kompresi turun, oli terkontaminasi.

### 5.3 Cara mengukur gap

1. Masukkan ring ke dalam bore **tanpa piston**
2. Dorong lurus dengan piston terbalik supaya ring tegak lurus (*square*)
3. Ukur di kedalaman tempat ring akan bekerja — biasanya 20–30 mm dari atas
4. Ukur dengan feeler gauge
5. Kalau kurang, kikir **satu sisi saja** dengan alat kikir ring, sedikit demi sedikit, lalu ukur ulang

Ujung yang dikikir harus tetap **tegak lurus dan tanpa gerigi** — ujung yang miring atau berduri akan menggores liner.

### 5.4 Cara memasang ring

Ini bagian yang sering dilakukan sembarangan dan berakibat fatal.

**Urutan pemasangan:**

1. **Ring oli dulu** — expander (pegas) lebih dulu, lalu rail atas dan bawah
2. **Ring kedua** — perhatikan tanda "TOP" atau titik, harus menghadap atas
3. **Ring atas** — perhatikan tanda "TOP"

**Aturan wajib pada ring oli expander:**

> **Kedua ujung expander harus BERTEMU, tidak boleh saling tumpang tindih.**

Kalau tumpang tindih, expander menekan terlalu kuat, ring oli tidak bisa mengikuti dinding, dan konsumsi oli melonjak. Ini kesalahan yang sering terjadi dan sulit didiagnosis setelah mesin dirakit.

**Periksa dengan jari** sebelum memasang rail.

**Alat pemasang ring wajib dipakai.** Memasang ring dengan tangan atau obeng akan memuntir ring — ring yang terpuntir tidak akan menyegel walau terlihat baik.

### 5.5 Posisi gap ring (staggering)

Gap ring harus **disebar**, tidak boleh sejajar — kalau sejajar, gas punya jalur lurus ke bawah.

**Aturan:**

| Jangan tempatkan gap | Alasan |
|---|---|
| Di atas pin piston | area lemah, ada celah |
| Di sisi thrust | area beban tertinggi |
| Sejajar dengan gap ring lain | jalur bocor lurus |

**Susunan yang lazim** (dilihat dari atas, pin di posisi 3 dan 9):

| Ring | Posisi |
|---|---|
| Ring atas | 0° (jam 12) |
| Ring kedua | 180° (jam 6) |
| Rail oli atas | 90° dari ring atas |
| Rail oli bawah | 90° dari ring atas, sisi berlawanan |
| Expander | 45° dari rail |

**Catatan jujur:** ring akan berputar sendiri saat mesin berjalan. Posisi awal tetap penting untuk **start pertama dan break-in**, tapi jangan berharap posisinya bertahan selamanya.

---

## 6. Pemuaian termal

### 6.1 Koefisien

| Material | α (per K) |
|---|---|
| Aluminium | 23 × 10⁻⁶ |
| Baja | 12 × 10⁻⁶ |
| Titanium | 8,6 × 10⁻⁶ |
| Besi cor | 11 × 10⁻⁶ |

### 6.2 Pemuaian rod

Rod memanjang saat panas, dan itu **mengurangi kelegaan klep-piston**.

Rod 95 mm dengan kenaikan suhu 100 K: [HITUNG]

| Material rod | Pemanjangan |
|---|---|
| Baja | 0,114 mm |
| **Aluminium** | **0,219 mm** |

**Rod aluminium memanjang hampir dua kali lipat.** Ini alasan mesin ber-rod aluminium butuh kelegaan klep lebih besar — tambahkan minimal 0,25 mm dari perhitungan dingin.

Kalau kelegaan dihitung saat dingin tanpa memperhitungkan ini, klep bisa menyentuh piston saat mesin panas.

### 6.3 Pemuaian piston

Piston aluminium bore 57,3 mm dengan kenaikan 150 K:

```
Δd = 57,3 × 23e-6 × 150 = 0,198 mm
```

Liner besi cor memuai:
```
Δd = 57,3 × 11e-6 × 150 = 0,095 mm
```

Selisihnya **0,103 mm** — piston memuai lebih cepat dari liner. Itulah sebabnya clearance dingin harus cukup besar; kalau tidak, piston macet saat panas.

Piston 2618 memuai lebih banyak lagi — itulah alasan clearance-nya jauh lebih besar.

### 6.4 Yang harus diperiksa

- [ ] Kelegaan klep-piston dicek **saat dingin** dengan margin untuk pemuaian
- [ ] Clearance piston sesuai material dan sesuai anjuran pabrik
- [ ] Ring gap diukur di bore yang sudah pada suhu ruang, bukan bore panas
- [ ] Kalau pakai rod aluminium, **tambah margin kelegaan klep 0,25 mm**

---

## 7. Per klep

### 7.1 Fungsinya

Dua hal:
1. **Menutup klep** dan menjaganya tetap rapat di seat
2. **Menjaga follower tetap menempel pada cam** sepanjang siklus

Fungsi kedua yang menentukan batas rpm.

### 7.2 Floating

Kalau per tidak mampu melawan inersia klep, follower **terlepas dari lobe cam**. Klep tidak lagi mengikuti profil, memantul saat menutup, dan bisa menyentuh piston.

**Gejala:**
- Tenaga hilang mendadak di atas rpm tertentu
- Suara valvetrain berubah
- Kurva dyno turun tajam, bukan melandai

**Akibat kalau dibiarkan:** klep patah, piston bolong, atau rocker hancur.

### 7.3 Menghitung kebutuhan

Percepatan klep di puncak lobe (profil harmonik):

```
a = (lift/2) × (2π/Φ_cam)² × ω_cam²
```
dengan `Φ_cam` = durasi dalam radian **cam** (setengah durasi crank), `ω_cam` = kecepatan sudut cam.

Gaya yang dibutuhkan:
```
F_perlu = massa_rakitan × a × faktor_aman
```

Faktor aman **1,3–1,5**.

**Massa rakitan** = klep + retainer + kuku + sekitar sepertiga massa per.

### 7.4 Contoh dan pengaruh variabel

Mesin Contoh B, lift 9 mm, durasi 261°, 12.000 rpm → percepatan **1.378 g**: [HITUNG]

| Rakitan klep | Massa | Per dibutuhkan |
|---|---|---|
| Stainless + retainer baja | 38 g | 73 kgf |
| Stainless + retainer titanium | 32 g | 62 kgf |
| Titanium + retainer titanium | 22 g | 42 kgf |

**Pengaruh lift** (klep 38 g, durasi 261°):

| Lift | Percepatan | Per dibutuhkan |
|---|---|---|
| 8,0 mm | 1.225 g | 65 kgf |
| 9,0 mm | 1.378 g | 73 kgf |
| 10,0 mm | 1.531 g | 81 kgf |
| 11,0 mm | 1.684 g | 90 kgf |

**Pengaruh durasi** (klep 38 g, lift 9 mm):

| Durasi | Percepatan | Per dibutuhkan |
|---|---|---|
| 240° | 1.630 g | 87 kgf |
| 261° | 1.378 g | 73 kgf |
| 290° | 1.116 g | 59 kgf |

**Perhatikan:** durasi lebih pendek dengan lift sama berarti ramp lebih curam → percepatan lebih besar → per lebih kuat. Ini pertukaran yang sering dilupakan saat memilih cam.

### 7.5 Mengukur per klep

Butuh **spring tester** — alat yang mengukur gaya pada ketinggian tertentu.

**Dua angka yang harus diukur:**

| | Diukur pada | Fungsi |
|---|---|---|
| **Seat pressure** | tinggi terpasang (klep tertutup) | menjaga klep rapat di seat |
| **Open pressure** | tinggi terpasang − lift maksimum | melawan inersia di puncak lobe |

**Rentang khas mesin kecil balap:**

| | Nilai |
|---|---|
| Seat pressure | 20–35 kgf |
| Open pressure | 55–85 kgf |

### 7.6 Coil bind

**Coil bind** = per tertekan sampai semua lilitannya saling menempel. Kalau ini terjadi saat mesin berjalan, valvetrain akan hancur seketika.

**Cara memeriksa:**
1. Tekan per sampai semua lilitan menempel, ukur tingginya
2. Hitung tinggi per pada lift maksimum: `tinggi_terpasang − lift`
3. Selisihnya harus **minimal 0,5–1,0 mm**

Kalau kurang, pilihannya: per lebih pendek, retainer berbeda, atau kurangi lift.

### 7.7 Spring surge

Per punya frekuensi alami sendiri. Kalau frekuensi itu beresonansi dengan harmonik cam, per bergetar hebat (*surge*) dan kehilangan kemampuan mengontrol — walau gaya statisnya cukup.

**Solusinya:**

| Cara | Penjelasan |
|---|---|
| **Per beehive / conical** | diameter berubah → frekuensi alami bervariasi → tidak ada satu frekuensi yang beresonansi |
| **Per ganda** | per dalam dan luar dengan frekuensi berbeda saling meredam |
| **Damper** | pegas datar di dalam per untuk meredam |

Untuk mesin berputaran tinggi, **beehive atau per ganda hampir selalu lebih baik** daripada per tunggal silindris.

### 7.8 Memilih per

Urutan yang benar:

1. **Tentukan cam dulu** — lift, durasi, dan agresivitas ramp
2. **Timbang rakitan klep** yang akan dipakai
3. **Hitung gaya yang dibutuhkan** pada rpm sasaran
4. **Pilih per** yang open pressure-nya memenuhi, dengan margin
5. **Periksa coil bind** pada lift maksimum
6. **Periksa tinggi terpasang** — mungkin butuh shim
7. **Ukur dengan tester**, jangan percaya spesifikasi katalog

**Per yang terlalu kuat juga merugikan:** gesekan valvetrain naik, cam dan rocker cepat aus, dan tenaga terbuang. Jangan memasang per sekuat mungkin — pasang yang **cukup**.

---

## 8. Massa berputar dan bolak-balik

### 8.1 Pembagian

| Kategori | Komponen |
|---|---|
| **Bolak-balik** | piston, ring, pin, klip, ~1/3 rod |
| **Berputar** | kruk as, ~2/3 rod, big end bearing |

### 8.2 Pengaruh

**Massa bolak-balik** menghasilkan gaya inersia yang harus ditahan struktur (bagian 1.3), dan menghasilkan getaran yang tidak bisa diseimbangkan sempurna pada 1 silinder.

**Massa berputar** menyimpan energi kinetik dan mempengaruhi seberapa cepat mesin bisa naik putaran.

### 8.3 Balance factor

```
balance factor = massa penyeimbang / massa bolak-balik
```

| Faktor | Akibat |
|---|---|
| 0% | getaran vertikal maksimum |
| **50–65%** | **kompromi umum** |
| 100% | getaran vertikal hilang, getaran horizontal penuh |

Menyeimbangkan 100% cuma **memindahkan** getaran, tidak menghilangkannya.

**Penting:** kalau mengganti piston dengan yang lebih ringan, balance factor berubah — kruk as **harus diseimbangkan ulang**. Ini sering dilupakan, dan akibatnya getaran di rpm tinggi yang merusak bearing.

---

## 9. Daftar periksa perakitan

**Sebelum merakit:**
- [ ] Bore diukur di 3 ketinggian × 2 arah
- [ ] Piston diukur di gauge point yang benar
- [ ] Clearance piston sesuai anjuran pabrik
- [ ] Ring gap diukur di bore, ring dalam posisi tegak lurus
- [ ] Ring kedua gap-nya lebih besar dari ring atas
- [ ] Rakitan klep ditimbang
- [ ] Per klep diukur dengan tester (seat dan open)
- [ ] Coil bind clearance ≥ 0,5 mm pada lift maksimum
- [ ] Kruk as diseimbangkan sesuai massa piston yang dipakai

**Saat merakit:**
- [ ] Ujung expander ring oli **bertemu, tidak tumpang tindih**
- [ ] Ring dipasang dengan alat, bukan tangan
- [ ] Tanda "TOP" pada ring menghadap atas
- [ ] Gap ring disebar sesuai aturan
- [ ] Semua torsi baut sesuai spesifikasi, urutan benar

**Sebelum diputar:**
- [ ] **Cek clay kelegaan klep-piston** — margin untuk pemuaian sudah dihitung
- [ ] Kalau rod aluminium, margin tambahan 0,25 mm
- [ ] Mesin diputar dengan tangan dua putaran penuh, tanpa hambatan
- [ ] Tekanan oli terbaca sebelum mesin dinyalakan

---

## 10. Ringkasan Tahap 8

1. **Bandingkan beban g ke mesin yang sudah terbukti**, jangan menilai angka mutlak.
2. **Massa piston adalah tuas paling murah** — turun 40 g memangkas beban rod 33%.
3. **2618 untuk balap penuh, 4032 untuk campuran** — bedanya di pemuaian dan clearance.
4. **Coating skirt mengurangi gesekan; coating mahkota menambah margin detonasi.**
5. **Klep titanium menaikkan batas floating 4.200 rpm** dengan per yang sama.
6. **Single ring untuk drag, double untuk endurance.**
7. **Ring kedua gap-nya harus lebih besar dari ring atas** — kalau tidak, ring flutter.
8. **Ujung expander ring oli harus bertemu, tidak tumpang tindih.** Kesalahan ini sulit didiagnosis setelah dirakit.
9. **Rod aluminium memanjang 0,219 mm** pada ΔT 100 K — hampir dua kali baja. Tambah margin kelegaan klep.
10. **Durasi cam lebih pendek butuh per lebih kuat** — ramp lebih curam.
11. **Per yang terlalu kuat juga merugikan.** Pasang yang cukup, bukan yang terkuat.
12. **Kalau ganti piston ringan, seimbangkan ulang kruk as.**

**Berikutnya:** Tahap 9 — CVT, tempat 20–30% tenaga bisa hilang tanpa disadari.
