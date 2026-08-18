# Project Rundown — Aset Visual & Animasi untuk Aplikasi Mobile

*Buku: Advanced Engine Tuning — Panduan Membangun Mesin 1 Cylinder Matic*

---

## Tujuan dokumen

Buku ini (13 bab + lampiran, ~30.000 kata) akan ditampilkan di aplikasi mobile dengan gambar dan animasi di tiap penjelasan. Dokumen ini adalah **daftar lengkap aset visual yang perlu dibuat**, disusun per bab sesuai urutan kemunculan di buku, supaya sesi berikutnya bisa langsung eksekusi tanpa perlu membaca ulang seluruh buku dari awal.

Setiap aset punya:
- **ID** — kode unik untuk dirujuk di kode/desain (mis. `CH04-03`)
- **Rujukan** — bagian/section di buku yang dijelaskan
- **Tipe** — lihat Legenda
- **Prioritas** — lihat Legenda
- **Deskripsi** — apa yang harus ditampilkan
- **Catatan animasi** — untuk tipe animasi, state/transisi kunci yang harus ada
- **Status** — placeholder untuk sesi berikutnya (semua masih `Belum dikerjakan`)

## Legenda

**Tipe:**
| Kode | Arti |
|---|---|
| **SD** | Static Diagram — gambar/ilustrasi diam (SVG/PNG) |
| **AD** | Animated Diagram — animasi loop pendek (Lottie/GIF/CSS/canvas), menjelaskan proses |
| **INT** | Interactive — pengguna bisa geser slider/tap untuk mengubah parameter dan melihat hasilnya berubah |
| **CG** | Chart/Graph — grafik data (bisa statis atau animasi saat scroll masuk) |

**Prioritas:**
| Kode | Arti |
|---|---|
| **P0** | Inti — tanpa ini penjelasan sulit dipahami. Kerjakan duluan. |
| **P1** | Penting — menambah pemahaman signifikan. |
| **P2** | Pelengkap — bagus untuk polish, bisa menyusul. |

---

## Ringkasan jumlah aset per bab

| Bab | Jumlah aset | P0 | P1 | P2 |
|---|---|---|---|---|
| 00 — Pengantar | 3 | 1 | 2 | 0 |
| 01 — Kamus Istilah | 15 | 8 | 6 | 1 |
| 02 — Tahap 1: Mengukur | 5 | 3 | 2 | 0 |
| 03 — Tahap 2: Konfigurasi | 5 | 3 | 2 | 0 |
| 04 — Tahap 3: Aliran | 7 | 5 | 2 | 0 |
| 05 — Tahap 4: Camshaft | 6 | 5 | 1 | 0 |
| 06 — Tahap 5: Kompresi & BBM | 5 | 3 | 2 | 0 |
| 07 — Tahap 6: Pengapian & AFR | 7 | 3 | 3 | 1 |
| 08 — Tahap 7: Saluran | 6 | 4 | 2 | 0 |
| 09 — Tahap 8: Mekanik | 8 | 3 | 4 | 1 |
| 10 — Tahap 9: CVT | 6 | 4 | 2 | 0 |
| 11 — Tahap 10: Simulasi | 5 | 1 | 3 | 1 |
| 12 — Lampiran | 2 | 0 | 1 | 1 |
| **Total** | **80** | **43** | **32** | **5** |

**Rekomendasi urutan pengerjaan lintas-bab (kalau mau kerja per prioritas, bukan per bab):**
1. Semua **P0** di bab 01 (Kamus Istilah) dulu — ini pondasi visual yang dipakai ulang (referenced) di bab-bab berikutnya.
2. **P0** bab 04, 05, 10 — tiga bab paling teknis dan paling bergantung pada visual (aliran, cam, CVT).
3. Sisa **P0** bab lain.
4. Baru **P1**, lalu **P2**.

---

## 00 — Pengantar

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH00-01 | 0.3 Peta belajar | SD/INT | P1 | Diagram alur 10 tahap belajar (flowchart vertikal: Mengukur → Konfigurasi → Head → Cam → Kompresi+BBM → Pengapian → Saluran → Mekanik → CVT → Simulasi). Tiap node bisa di-tap untuk lompat ke bab itu. | — |
| CH00-02 | 0.1 Kenapa CVT dipisahkan | AD | P0 | Dua motor berdampingan: motor gear rpm-nya "jatuh" tiap pindah gigi (garis rpm bergerigi turun-naik) vs motor CVT rpm-nya rata lurus sepanjang akselerasi. Ini visual paling penting di seluruh pengantar karena jadi dasar seluruh filosofi buku. | Loop: kedua motor start bareng, motor gear grafik rpm zig-zag (naik-jatuh-naik), motor CVT grafik rpm datar di titik puncak. |
| CH00-03 | 0.6 Mesin contoh | SD | P1 | Kartu spesifikasi 3 mesin contoh (A/B/C) sebagai infografis ringkas — dipakai berulang sebagai "kartu referensi" di bab-bab lain saat menyebut "Mesin Contoh A/B/C". | — |

---

## 01 — Kamus Istilah

*Bab ini adalah glosarium 21 istilah dalam 6 kelompok. Aset di sini akan MUNCUL ULANG (reused) di bab-bab teknis berikutnya, jadi prioritas mengerjakannya lebih dulu tinggi.*

### Kelompok 1 — Ukuran dan geometri

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH01-01 | CSA | SD | P0 | Potongan melintang port menunjukkan CSA diukur di **titik tersempit**, bukan di flange atau bowl. Tampilkan juga perbandingan penampang bundar vs oval dengan luas yang sama. | — |
| CH01-02 | Throat | SD | P0 | Potongan valve+seat dari samping, label jelas: diameter valve, lebar seat, diameter throat. Highlight throat sebagai titik tersempit. | — |
| CH01-03 | Bore, Stroke, Rod | AD | P0 | Piston-rod-crank bergerak satu putaran penuh, dengan label bore (diameter piston), stroke (jarak TDC-BDC), panjang rod. | Loop 1 putaran crank penuh, angka stroke muncul sebagai garis vertikal TDC↔BDC yang "digambar" saat piston bergerak. |

### Kelompok 2 — Kecepatan dan aliran

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH01-04 | MPS (Mean Piston Speed) | AD | P0 | Piston bergerak naik-turun dengan speedometer kecil di samping menunjukkan kecepatan berubah (nol di TDC/BDC, puncak di tengah stroke). | Sinkron dengan rotasi crank; speedometer needle mengikuti kecepatan piston real-time. |
| CH01-05 | MGV (Mean Gas Velocity) | AD | P0 | Partikel udara mengalir dari port ke cylinder, kecepatan partikel divisualisasikan (jarang/rapat mengikuti CSA). Tampilkan dua skenario: CSA besar (partikel lambat/jarang) vs CSA kecil (partikel cepat/rapat) — TAPI dengan debit sama. Ini untuk membantah miskonsepsi "TB kecil = gas lebih cepat". | Loop partikel mengalir dengan kecepatan berbeda di 2 kondisi CSA berdampingan. |
| CH01-06 | Cf — Koefisien Flow | SD/INT | P1 | Perbandingan visual "lubang ideal" (aliran laminar sempurna) vs "lubang nyata" (dengan turbulensi/separasi di tepi) pada luas yang sama, tunjukkan Cf sebagai rasio debit nyata/ideal. Slider interaktif nilai Cf 0.5–0.95 mengubah visual "kehalusan" aliran. | — |
| CH01-07 | K — Koefisien Rugi Tekanan | SD | P2 | Bar chart perbandingan nilai K untuk tiap bentuk (pipa lurus, bellmouth, mulut tajam, tikungan 37°, butterfly TB). | — |
| CH01-08 | VE — Volumetric Efficiency | SD | P1 | Silinder dengan "level pengisian udara" seperti gelas — VE 80% = gelas terisi 80%, VE 105% = meluap sedikit (dibantu efek gelombang/momentum). | — |

### Kelompok 3 — Kompresi

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH01-09 | CR vs DCR | AD | P0 | Piston bergerak dari BDC ke TDC. Tunjukkan DUA garis waktu: CR dihitung dari BDC penuh (garis putus-putus, "tidak nyata"), DCR dihitung baru mulai dari titik IVC (garis solid, "yang sebenarnya terjadi"). Valve isap digambar tertutup tepat di titik IVC. | Scrub/slider: geser titik IVC di sepanjang stroke, DCR berubah real-time. Ini kandidat kuat jadi **INT**. |

### Kelompok 4 — Referensi sudut crank

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH01-10 | TDC/BDC + firing TDC vs overlap TDC | AD | P0 | Crank berputar 720° (2 putaran penuh = 1 siklus 4-tak) dengan piston naik-turun 2×. Highlight momen "firing TDC" (akhir kompresi) vs "overlap TDC" (akhir buang) sebagai dua titik berbeda meski piston di posisi sama. | Loop 720°, dua TDC diberi warna/label berbeda saat crank melewatinya. |
| CH01-11 | BTDC/ATDC/BBDC/ABDC | SD/INT | P0 | Lingkaran crank (jam analog) dengan 4 kuadran diberi label BTDC/ATDC (atas) dan BBDC/ABDC (bawah). Jarum menunjuk sudut tertentu sebagai contoh ("28° BTDC"). | — |

### Kelompok 5 — Kejadian valve

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH01-12 | IVO/IVC + titik ukur lift (seat-to-seat/@1mm/@0.050") | AD | P0 | Grafik lift valve vs sudut crank (kurva lonceng), dengan 3 garis horizontal di ketinggian lift berbeda (0,15mm / 1,00mm / 1,27mm) memotong kurva di titik berbeda — menunjukkan kenapa "durasi" bisa beda angka untuk cam yang sama. | Toggle antar 3 standar pengukuran, garis potong & angka durasi berubah. |
| CH01-13 | EVO/EVC | AD | P1 | Sama seperti IVO/IVC tapi untuk sisi buang, ditampilkan berdampingan (isap kiri, buang kanan) pada garis waktu crank yang sama. | — |
| CH01-14 | Overlap | AD | P0 | Dua kurva lift (isap & buang) di-overlay pada satu grafik sudut crank; area di mana KEDUANYA terbuka bersamaan (di sekitar TDC) di-highlight sebagai "jendela overlap". | Loop menunjukkan piston di TDC dengan kedua valve terbuka sedikit ("cracked") secara bersamaan. |
| CH01-15 | Time-Area | CG | P1 | Grafik luas-di-bawah-kurva (integral) dari kurva lift×waktu — bandingkan 2 cam berbeda (durasi pendek/lift tinggi vs durasi panjang/lift rendah) yang punya time-area SAMA meski kurvanya beda bentuk. | — |

### Kelompok 6 — Karakter camshaft

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH01-16 | ICL/ECL vs LSA (paling sering tertukar) | INT | P0 | "Jam cam" — diagram lingkaran ganda menunjukkan ICL & ECL sebagai dua jarum, LSA sebagai sudut TETAP di antara keduanya. Slider "putar sprocket" menggeser ICL+ECL BERSAMAAN (LSA tidak berubah) — untuk membuktikan LSA tidak bisa diubah dengan adjustable sprocket. | Interaktif: drag untuk memutar cam timing, tunjukkan LSA tetap sementara ICL/ECL bergerak bersama. |
| CH01-17 | Lift vs Lift Kritis | CG | P1 | Grafik luas tirai (garis naik lalu mendatar) vs luas throat (garis datar) — titik potongnya adalah "lift kritis". Highlight area lift balap yang jauh di atas titik itu. | — |

---

## 02 — Tahap 1: Memahami Apa yang Diukur

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH02-01 | 1.1 Torsi vs tenaga | CG | P0 | Grafik dyno klasik: kurva torsi & tenaga overlay pada sumbu rpm, dengan garis vertikal di titik potong 5252 rpm (di mana torsi=tenaga secara numerik — tunjukkan ini kebetulan matematis, bukan fisik). | Animasi saat scroll: kurva "digambar" dari kiri ke kanan. |
| CH02-02 | 2.2 Rentang rpm lebar vs puncak tinggi (powerband) | CG | P0 | Dua kurva tenaga berdampingan: kurva "rentang rpm lebar" (landai, puncak rendah) vs "rentang rpm sempit" (curam, puncak tinggi). Area di atas 90% puncak di-shade sebagai powerband. | — |
| CH02-03 | 2.3 Kenapa CVT mengubah aturannya | AD | P0 | Reuse konsep CH00-02 tapi lebih detail: overlay kurva tenaga dengan titik rpm yang "ditahan" CVT vs titik-titik rpm yang dilewati motor gear saat pindah gigi. | — |
| CH02-04 | 3.2 Jenis dyno | SD | P1 | Ilustrasi potongan inertia dyno (drum berputar) vs brake dyno (dengan rem/eddy current) berdampingan. | — |
| CH02-05 | 3.2 Prosedur dyno yang benar | SD | P2→P1 | Infografis checklist bergambar 6 langkah prosedur dyno run (pemanasan → run 1 dibuang → 3 run tercatat → dst). | — |

---

## 03 — Tahap 2: Memilih Konfigurasi Dasar

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH03-01 | 1.1 Overstroke/Square/Overbore | AD/INT | P0 | Tiga silinder berdampingan dengan kapasitas SAMA tapi proporsi beda (bore kecil+stroke panjang / seimbang / bore besar+stroke pendek). Piston bergerak, valve yang muat digambar proporsional terhadap bore. | Slider rasio bore/stroke, silinder berubah bentuk real-time, kapasitas (Vd) tetap konstan di layar. |
| CH03-02 | 1.2 Kenapa overbore menang (klep lebih besar) | SD | P0 | Perbandingan 2 head cross-section: bore kecil (valve kecil muat) vs bore besar (valve besar muat), dengan luas valve dihitung dan dibandingkan. | — |
| CH03-03 | 2. Kapasitas besar dengan valve kecil (kesalahan umum) | SD | P0 | Before/after: mesin di-bore-up (silinder membesar) tapi head+valve TETAP — tunjukkan "leher botol" secara visual (silinder besar, tapi port/valve kecil jadi titik cekik). | — |
| CH03-04 | 3. Jumlah valve (2/3/4) | SD | P1 | Tiga head cross-section dari atas (top view) menunjukkan tata letak valve 2/3/4 pada bore yang sama, dengan luas valve total dihitung untuk masing-masing. | — |
| CH03-05 | 5. Inersia crankshaft & balance factor | AD | P1 | Crank berputar dengan counterweight, menunjukkan getaran vertikal vs horizontal pada balance factor berbeda (0%/50-65%/100%) — pilih salah satu jadi highlight. | Loop 1 putaran, vektor gaya (panah) muncul menunjukkan arah getaran net. |

---

## 04 — Tahap 3: Aliran (Cylinder Head)

*Bab paling visual di seluruh buku — plafon tenaga mesin ditentukan di sini.*

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH04-01 | 1. Kenapa head menentukan segalanya | SD | P0 | Infografis "plafon tenaga": head dengan flow tertentu (CFM) digambar sebagai pipa dengan diameter tetap — apa pun yang dipasang setelahnya (cam/exhaust/ECU) tidak bisa melebihi debit yang lewat pipa itu. | — |
| CH04-02 | 2. Valve dan lift kritis | AD | P0 | Potongan valve terbuka bertahap dari 0 ke lift maksimum. Highlight area tirai (curtain area, silinder di sekeliling valve) saat lift rendah, lalu highlight throat (lingkaran) saat lift tinggi — tunjukkan momen "titik silang" (lift kritis). | Scrub lift 0→maks, area yang jadi pembatas (tirai vs throat) berganti warna otomatis di titik kritis. |
| CH04-03 | 3.2 Membesarkan throat vs lebar seat | INT | P0 | Potongan valve-seat dengan slider "besarkan throat" — throat membesar, lebar seat visual mengecil, dengan warning zone merah saat seat < 0.7mm. | Slider interaktif diameter throat, real-time hitung lebar seat & flow gain %. |
| CH04-04 | 3.4 Rasio throat buang/isap → cam simetris | SD | P1 | Dua throat (isap & buang) berdampingan dengan rasio luas ditunjukkan sebagai bar/lingkaran proporsional, dengan indikator "aman untuk cam simetris" atau tidak. | — |
| CH04-05 | 5. Bentuk port & aliran (bundar vs oval, short-turn radius) | AD | P0 | Potongan memanjang port menunjukkan aliran udara (garis alir/streamline) melewati tikungan — bandingkan short-turn radius TAJAM (aliran lepas/separasi, turbulen merah) vs radius WAJAR (aliran menempel, hijau/mulus). | Loop streamline mengalir, warna berubah merah di zona separasi. |
| CH04-06 | 6.5 Mulut port di flange (sambungan manifold) | AD | P1 | Sambungan manifold-head zoom in, bandingkan "step"/tidak sebidang (aliran tersendat) vs sebidang+radius (aliran mulus). | — |
| CH04-07 | 7. Memperkirakan flow tanpa flowbench | CG | P0 | Diagram alur kalkulasi: Throat → v_teoretis → Q → CFM → × Cf → CFM nyata → × faktor → HP. Bisa jadi kalkulator mini interaktif. | Kandidat kuat jadi **INT** (kalkulator input throat/Cf → output HP estimasi). |

---

## 05 — Tahap 4: Timing (Camshaft)

*Bab kedua paling visual — semua konsep di sini butuh animasi berbasis waktu/sudut.*

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH05-01 | 1. Empat kejadian valve (urutan kepentingan) | SD | P0 | Timeline horizontal 720° dengan 4 titik ditandai (IVC paling ditonjolkan sebagai "paling penting"), masing-masing dengan ikon kecil. | — |
| CH05-02 | 2. IVC dan DCR (tabel IVC vs DCR) | INT | P0 | Reuse & perluas CH01-09: slider posisi IVC (35°–75° ABDC) menggerakkan titik "valve menutup" pada animasi piston, DCR dihitung & ditampilkan real-time sebagai gauge/angka besar. | Interaktif penuh — ini salah satu visual paling berharga di buku karena IVC/DCR adalah konsep tersulit. |
| CH05-03 | 3. Durasi dari time-area (durasi turun walau rpm naik) | SD | P1 | Dua mesin berdampingan (2-valve vs 4-valve) dengan durasi cam berbeda tapi "jendela aliran per cc" (time-area) SAMA — tunjukkan sebagai luas area yang sama meski bentuk kurva beda. | — |
| CH05-04 | 4.3–4.4 Overlap & pertukaran IVO/DCR | AD | P0 | Reuse CH01-14 (overlap) + tambahkan slider durasi → tunjukkan efek berantai: durasi naik → IVO lebih awal → IVC lebih telat → DCR turun. Rantai sebab-akibat divisualisasikan sebagai domino/alur panah. | — |
| CH05-05 | 4.7 ICL sebagai tuas penyetelan (adjustable sprocket) | INT | P0 | Reuse CH01-16, tambahkan animasi fisik: sprocket cam diputar oleh tool, seluruh piringan cam (ICL+ECL) berotasi bersama, LSA (jarak sudut tetap) tidak berubah. | — |
| CH05-06 | 5. Kelegaan valve-piston (paling kritis untuk keselamatan) | AD | P0 | Piston mendekati TDC dengan valve isap masih terbuka (lift tersisa beberapa mm) — highlight celah antara puncak piston dan valve sebagai "clearance". Tunjukkan skenario BAHAYA: clearance terlalu kecil → valve menyentuh piston. | Loop normal (clearance aman) + versi "warning" (clearance nyaris nol, flash merah). Ini visual keselamatan paling penting di buku — jangan sampai terlewat. |

---

## 06 — Tahap 5: Kompresi dan Bahan Bakar

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH06-01 | 2. Anggaran volume ruang bakar (Vc) | SD/CG | P0 | Stacked bar / pie chart komponen Vc: pentroof + gasket + deck + kantong valve − dome, dengan Mesin Contoh B sebagai data nyata (menunjukkan kantong valve makan 14% anggaran). | Bisa dibuat **INT**: slider tiap komponen mengubah total Vc & CR real-time. |
| CH06-02 | 3.2 Perbandingan bahan bakar (energi per kg udara) | CG | P0 | Bar chart horizontal energi/kg udara untuk bensin/avgas/race gas/metanol/nitro, dengan bensin sebagai baseline 100%. | Animasi bar "tumbuh" saat scroll masuk viewport. |
| CH06-03 | 3.5 Lambda vs AFR (kenapa lambda lebih universal) | SD | P1 | Dua skala berdampingan: skala AFR (angka beda-beda tiap bahan bakar) vs skala Lambda (semua bahan bakar mengumpul di 0.74–0.89) — visual "menyatukan" skala yang berantakan jadi satu. | — |
| CH06-04 | 4. Kalibrasi batas detonasi (DCR vs tabel umum) | CG | P1 | Grafik/tabel visual: titik "tabel umum bilang X" vs titik "mesin nyata terbukti di Y" — sama seperti tabel di bagian G lampiran, dibuat visual. | — |
| CH06-05 | 5. Knocking (detonasi) | AD | P0 | Animasi pembakaran normal (api menyebar rapi dari spark plug, lingkaran membesar teratur) vs detonasi (dua front api bertabrakan + gelombang kejut/shockwave digambar sebagai garis tajam). | Loop dua skenario berdampingan atau toggle switch normal/detonasi. |

---

## 07 — Tahap 6: Pengapian dan Campuran

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH07-01 | 2.1 Kurva torsi vs lambda | CG | P1 | Grafik torsi vs lambda dengan puncak di λ 0.87, area datar di sekitarnya di-highlight. | — |
| CH07-02 | 3. MBT (spark angle) | AD | P0 | Piston bergerak dari titik penyalaan spark plug menuju TDC, dengan tekanan pembakaran (kurva naik) — tunjukkan 3 skenario: kurang maju (puncak tekanan terlambat, setelah TDC jauh), MBT (puncak tekanan pas), terlalu maju (puncak tekanan sebelum TDC, melawan piston naik). | Toggle 3 skenario, kurva tekanan & posisi piston bergerak sinkron. |
| CH07-03 | 4.2 Closed-valve vs open-valve injection | AD | P0 | Dua skenario injeksi: bahan bakar disemprot ke valve isap TERTUTUP (menguap di port dulu) vs valve TERBUKA (langsung masuk cylinder, mendinginkan muatan). | Loop partikel bahan bakar (kabut) disemprotkan pada 2 timing berbeda. |
| CH07-04 | 5.1 Heat range spark plug | SD | P0 | Potongan melintang 2 spark plug (panas vs dingin) menunjukkan panjang insulator berbeda dan jalur pembuangan panas (panah). | — |
| CH07-05 | 5.5 Membaca spark plug (diagnostik) | SD | P1 | Grid galeri 5 kondisi ujung spark plug (normal/detonasi/kaya/miskin/terlalu panas) dengan warna & tekstur berbeda — semacam "kartu diagnosa" yang bisa di-tap untuk detail. | — |
| CH07-06 | 6.1 Jenis coil (TCI/CDI/Smart coil) | SD | P1 | Diagram sederhana 3 jenis coil menunjukkan bentuk gelombang percikan (durasi & tegangan) — grafik tegangan vs waktu untuk masing-masing. | — |
| CH07-07 | 7.2 Tiga tingkat solusi ECU | SD | P2 | Infografis piramida/tangga 3 tingkat (remap → piggyback → standalone) dengan kemampuan masing-masing sebagai checklist. | — |

---

## 08 — Tahap 7: Saluran Masuk dan Buang

*Konsep gelombang tekanan di bab ini SANGAT butuh animasi — sulit dipahami dari teks/statis saja.*

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH08-01 | 1.3 Kenapa mengecilkan TB tidak menaikkan kecepatan gas | AD | P0 | Reuse & perluas CH01-05: pipa dengan penyempitan di satu titik (TB) lalu melebar lagi (manifold) sebelum port — tunjukkan kecepatan naik cuma LOKAL di TB, kembali sama di port. | Partikel mengalir melalui pipa, kecepatan (jarak antar partikel) berubah cuma di segmen TB. |
| CH08-02 | 2.1–2.2 Mekanisme gelombang tekanan intake (THE core animation) | AD | P0 | Animasi gelombang tekanan negatif merambat dari valve isap ke ujung velocity stack terbuka, memantul jadi gelombang POSITIF, kembali ke valve tepat sebelum menutup — mendorong muatan ekstra masuk. Ini animasi paling penting di bab ini. | Loop: gelombang (garis/warna) merambat pipa-mulut-kembali, valve buka-tutup sinkron, highlight "dorongan ekstra" saat gelombang tiba tepat waktu. |
| CH08-03 | 3.2 Radius bellmouth vs koefisien flow | INT | P0 | Slider radius bellmouth (0 = tajam, 0.25 = besar) mengubah bentuk mulut velocity stack + visual aliran (turbulen di R kecil, mulus di R besar) + angka Cf berubah real-time. | — |
| CH08-04 | 3.3 Susunan pelebaran (throat→port→manifold→TB→stack) | SD | P1 | Diagram corong/terompet dari kecil ke besar menuju hulu, dengan panah aliran udara searah pelebaran — vs versi SALAH (ada penyempitan-pelebaran di tengah, ditandai merah). | — |
| CH08-05 | 4.4 Mekanisme gelombang tekanan exhaust | AD | P0 | Sama seperti CH08-02 tapi untuk sisi buang: gelombang POSITIF dari valve buang ke titik pelebaran (transisi ke muffler), memantul jadi NEGATIF, kembali menarik sisa gas buang + muatan segar saat overlap. | — |
| CH08-06 | 4.6 Bentuk exhaust (header/megaphone/reverse cone) | SD | P1 | Tiga bentuk pipa buang berdampingan dengan efek gelombang pantulnya masing-masing digambarkan sebagai panah arah gelombang. | — |

---

## 09 — Tahap 8: Mekanik, Material, dan Keandalan

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH09-01 | 1.2 Percepatan piston (TDC vs BDC) | CG | P0 | Grafik percepatan piston vs sudut crank sepanjang 1 putaran, tunjukkan puncak di TDC lebih tinggi daripada di BDC. | Sinkron dengan animasi piston bergerak (bisa reuse CH01-03/CH01-04). |
| CH09-02 | 2.1–2.2 Material piston & clearance | SD | P1 | Perbandingan 2 piston (cor vs tempa 2618) dengan clearance yang digambar proporsional (celah antara piston-liner beda ketebalan visual). | — |
| CH09-03 | 2.4 Coating piston (skirt/mahkota) | SD | P2 | Potongan piston dengan layer coating berwarna berbeda di skirt (anti-gesek) dan mahkota (thermal barrier), dengan panah "panas dipantulkan". | — |
| CH09-04 | 5.2–5.5 Ring piston (gap, pemasangan, staggering) | AD | P0 | Animasi 3D/2D urutan pemasangan ring (oli dulu, lalu kedua, lalu atas) dengan orientasi tanda "TOP" benar, plus diagram posisi gap ring dari atas (jam 12/6/dst) — versi BENAR (disebar) vs SALAH (sejajar, jalur bocor merah). | — |
| CH09-05 | 6. Pemuaian termal (rod, piston) | AD | P1 | Piston & rod "memuai" secara visual (sedikit membesar dengan gradient warna panas) dibanding ukuran dingin (outline putus-putus), menunjukkan kenapa clearance dingin harus lebih besar. | Loop dingin→panas→dingin dengan ukuran berubah halus. |
| CH09-06 | 7.2 Valve spring floating | AD | P0 | Cam berputar cepat, follower/valve TIDAK bisa mengikuti profil lobe pada rpm tinggi (terlepas dari permukaan cam, lalu "jatuh" dan memantul) — visual paling jelas untuk menjelaskan floating. | Loop rpm rendah (mengikuti sempurna) vs rpm tinggi (floating/terlepas), bisa jadi toggle. |
| CH09-07 | 7.7 Spring surge & solusinya (beehive/dual spring) | SD | P1 | Perbandingan bentuk 3 jenis spring (silindris/beehive/ganda) dengan pola getaran (garis bergelombang) di sampingnya. | — |
| CH09-08 | 8.1–8.3 Massa berputar vs bolak-balik, balance factor | AD | P1 | Reuse konsep CH03-05, highlight bagian mana yang "bolak-balik" (piston, ring, pin) vs "berputar" (crank, big end) dengan warna berbeda pada animasi mekanisme piston-rod-crank. | — |

---

## 10 — Tahap 9: Penyaluran Tenaga (CVT)

*Bab paling penting untuk animasi mekanisme — CVT adalah "kotak hitam" bagi kebanyakan pembaca, animasi di sini akan jadi yang paling sering dibuka ulang pengguna.*

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH10-01 | 1.1–1.2 Cara kerja CVT (mekanisme lengkap) | AD | P0 | **Animasi utama seluruh buku.** Tampilkan pulley primer & sekunder + belt + roller secara utuh: saat rpm naik, roller terlempar keluar (gaya sentrifugal), mendorong pulley primer menutup, belt naik di primer & turun di sekunder, rasio berubah kontinu. | Loop lengkap dari diam (rasio berat) → rpm naik bertahap → rasio ringan (top speed). Kandidat kuat jadi **INT** dengan slider "rpm" yang menggerakkan seluruh mekanisme. |
| CH10-02 | 3.1 Efek berat roller | INT | P0 | Slider berat roller (ringan↔berat) mengubah titik rpm di mana pulley mulai bergeser — tunjukkan dua kurva rpm-vs-waktu berdampingan (roller ringan = rpm ditahan tinggi, roller berat = rpm ditahan rendah). | — |
| CH10-03 | 3.2 Efek torque spring | AD | P1 | Sama seperti CH10-02 tapi untuk kekerasan torque spring, digambar sebagai pegas yang menahan pulley sekunder dengan kekuatan berbeda. | — |
| CH10-04 | 3.3 Clutch spring & rpm sambungan | AD | P1 | Centrifugal clutch pada rpm rendah (tidak menggigit, terpisah) vs rpm sambungan (sepatu kopling terlempar keluar, menggigit rumah kopling). | Loop rpm naik dari idle sampai sambungan terjadi (visual "klik" saat menggigit). |
| CH10-05 | 5.1–5.2 Gearing & top speed (kenapa rasio gear tidak pengaruhi waktu) | CG | P0 | Grafik kecepatan-vs-waktu untuk beberapa rasio gear berbeda — tunjukkan garis-garis itu IDENTIK sampai satu titik (mentok limiter), baru bercabang. Ini melawan intuisi, jadi visual harus tegas. | Animasi garis "berjalan" bersamaan lalu satu-persatu mentok di titik berbeda. |
| CH10-06 | 6. Sumber kerugian tenaga di CVT | SD | P0 | Diagram aliran tenaga dari crank ke roda sebagai "pipa" yang menyempit di tiap titik kerugian (slip belt, gesekan pulley, final gear, clutch slip) — total 10-30% "bocor" sebelum sampai roda. | Bisa dibuat progress bar animasi: 100% di crank → berkurang bertahap → keluar di roda. |

---

## 11 — Tahap 10: Simulasi dan Validasi

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH11-01 | 1.1 Alat yang tepat untuk pertanyaan yang tepat | SD | P1 | Diagram alur kerja: perhitungan 1D → CFD 3D → flowbench → dyno → lintasan, dengan ikon di tiap tahap. | — |
| CH11-02 | 3.1 Setup flowbench virtual (plenum setengah bola) | SD | P1 | Potongan 3D sederhana: plenum setengah bola di depan mulut port, dengan panah aliran masuk dari segala arah menuju satu titik. | — |
| CH11-03 | 3.5 Refinement volume vs permukaan (mesh) | SD | P2 | Perbandingan visual mesh CFD: mesh halus di permukaan tapi kasar di inti (SALAH, kotak-kotak besar) vs mesh halus merata (BENAR). | — |
| CH11-04 | 4.2 Melihat tanda kecepatan, bukan besarnya (bug aliran balik) | AD | P0 | Visualisasi medan kecepatan CFD: mode "besaran saja" (semua warna sama = "lambat", termasuk aliran balik) vs mode "dengan tanda" (aliran balik jadi warna berbeda/terbalik) — ini adalah "aha moment" paling penting di bab simulasi. | Toggle antara 2 mode visualisasi pada medan aliran yang sama. |
| CH11-05 | 4.3 Bug 1 — kerucut penyumbat (cone blocking) | SD | P1 | Potongan geometri CFD menunjukkan cacat: pusat tutup mulut tidak sebidang dengan cincin, membentuk kerucut yang menyumbat — before/after perbaikan. | — |

---

## 12 — Lampiran

*Bab referensi (rumus, checklist, data) — kebutuhan visual minimal, lebih ke arah UI/UX presentasi data daripada animasi baru.*

| ID | Rujukan | Tipe | Prioritas | Deskripsi | Catatan animasi |
|---|---|---|---|---|---|
| CH12-01 | E. Perbandingan mesin balap dunia | CG | P1 | Scatter/bar chart interaktif membandingkan MPS, valve/bore, HP/L across semua mesin di tabel — bisa tap tiap mesin untuk detail. | — |
| CH12-02 | G. Penutup (tabel umum vs mesin nyata) | SD | P2 | Infografis ringkas 4 baris "yang dikatakan tabel umum vs yang dikatakan mesin nyata" sebagai kartu perbandingan bergambar. | — |

---

## Catatan produksi untuk sesi berikutnya

1. **Reusable assets dulu.** Banyak aset di bab 01 (Kamus Istilah) dipakai ulang secara konsep di bab 02–10 (mis. animasi piston-crank dasar, kurva lift valve, diagram overlap). Bangun ini sebagai komponen/template yang bisa di-parameterisasi (warna, angka, state), bukan aset sekali pakai per bab.
2. **Format teknis** — perlu diputuskan di sesi berikutnya: Lottie (JSON, ringan, bagus untuk AD sederhana) vs SVG+CSS/JS (lebih fleksibel untuk INT) vs video/GIF (paling gampang tapi berat & tidak interaktif). Rekomendasi: Lottie untuk AD, custom SVG+gesture untuk INT, PNG/SVG statis untuk SD.
3. **5 aset "wajib pertama"** kalau harus pilih titik mulai tercepat untuk validasi arah visual:
   - CH00-02 (CVT vs motor gear rpm)
   - CH01-09 / CH05-02 (CR vs DCR — konsep tersulit di buku)
   - CH04-02 (lift kritis)
   - CH08-02 (gelombang tekanan intake)
   - CH10-01 (mekanisme CVT lengkap)
4. **Konsistensi visual** — semua diagram potongan mesin (head, piston, valve) sebaiknya pakai satu gaya ilustrasi (line-art teknis atau flat-color) yang sama di seluruh 80 aset supaya terasa satu buku, bukan tempelan.
