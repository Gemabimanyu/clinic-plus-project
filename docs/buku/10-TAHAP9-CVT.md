# TAHAP 9 — PENYALURAN TENAGA: CVT

*Tenaga yang tidak sampai ke roda tidak ada artinya. Di sini 20–30% bisa hilang tanpa disadari.*

---

## 1. Cara kerja CVT

### 1.1 Komponen

| Bagian | Fungsi |
|---|---|
| **Pulley primer (drive)** | dua permukaan kerucut, satu bisa bergerak; roller di dalamnya |
| **Roller** | pemberat yang terlempar keluar oleh gaya sentrifugal |
| **V-belt** | menyalurkan tenaga antar pulley |
| **Pulley sekunder (driven)** | dua permukaan kerucut + torque spring + torque cam |
| **Torque spring (contra spring)** | melawan pergeseran rasio |
| **Centrifugal clutch** | menghubungkan mesin ke roda pada rpm tertentu |
| **Clutch spring** | menentukan rpm sambungan |
| **Final gear** | reduksi tetap dari pulley sekunder ke roda |

### 1.2 Urutan kejadiannya

**Diam:** belt berada di posisi paling dalam pada pulley primer, paling luar pada sekunder. Rasio paling berat (reduksi terbesar).

**RPM naik:** roller terlempar keluar oleh gaya sentrifugal, mendorong permukaan pulley primer yang bisa bergerak. Belt terdorong ke posisi lebih luar pada primer.

**Belt naik di primer:** karena panjang belt tetap, belt otomatis turun ke posisi lebih dalam pada sekunder. Rasio jadi lebih ringan.

**Torque spring melawan:** menjaga tegangan belt dan menahan rasio agar tidak terlalu cepat berubah.

**Hasilnya:** rasio berubah **kontinu**, dan mesin bisa ditahan di satu putaran sepanjang akselerasi.

---

## 2. Kenapa CVT mengubah aturan tuning

### 2.1 Perbedaan dari motor gear

Pada motor gear, tiap perpindahan gear menjatuhkan putaran mesin. Kalau rentang rpm bertenaga sempit, mesin jatuh keluar powerband dan akselerasi hilang. Karena itu motor gear butuh **rentang rpm yang lebar**.

CVT tidak punya masalah itu. Rasio berubah kontinu, jadi mesin bisa ditahan **persis di satu titik**.

> **Konsekuensi: pada CVT, yang perlu dioptimalkan adalah tenaga di SATU titik putaran, bukan rentang rpm yang lebar.**

Ini memberi kebebasan yang tidak dimiliki motor gear: cam durasi panjang, overlap besar, LSA sempit, runner ditala tajam — semua yang membuat rentang rpm sempit tapi puncaknya tinggi.

### 2.2 Titik mana yang dipilih

**Putaran tenaga puncak**, bukan torsi puncak.

Percepatan berbanding lurus dengan tenaga (lihat Tahap 1). Menahan mesin di torsi puncak berarti membuang putaran yang tersedia.

### 2.3 Syaratnya

CVT harus **benar-benar mampu** menahan mesin di titik itu. CVT yang salah setelan akan membiarkan putaran jatuh, dan mesin dengan rentang rpm sempit akan terasa **jauh lebih lambat** daripada mesin standar.

Inilah kenapa banyak mesin yang bagus di dyno mengecewakan di lintasan.

---

## 3. Menyetel CVT

### 3.1 Berat roller

Ini penyetelan paling berpengaruh.

| Roller | Efek |
|---|---|
| **Lebih berat** | terlempar keluar di rpm lebih rendah → rasio berubah lebih awal → **mesin ditahan di rpm lebih rendah** |
| **Lebih ringan** | rasio berubah lebih lambat → **mesin ditahan di rpm lebih tinggi** |

**Cara menyetelnya:**

1. Pasang wideband atau tachometer yang bisa dibaca saat jalan
2. Lakukan akselerasi penuh
3. Catat rpm yang **ditahan** CVT selama akselerasi
4. Bandingkan dengan rpm tenaga puncak dari grafik dyno
5. Kalau CVT menahan terlalu rendah → **roller lebih ringan**
6. Kalau terlalu tinggi (mentok limiter) → **roller lebih berat**

**Aturan praktis:** ubah 1 gram per langkah. Perubahan 2 gram sudah terasa jelas.

### 3.2 Torque spring (contra spring)

| Spring | Efek |
|---|---|
| **Lebih keras** | melawan pergeseran rasio → mesin ditahan di rpm lebih tinggi, cengkeraman belt lebih kuat |
| **Lebih lunak** | rasio bergeser lebih mudah → rpm lebih rendah |

Torque spring bekerja **bersama** roller. Kombinasi yang umum untuk drag: roller agak ringan + torque spring agak keras.

**Efek samping spring terlalu keras:** belt tertekan sangat kuat, gesekan naik, panas naik, dan tenaga terbuang. Jangan asal keras.

### 3.3 Clutch spring

Menentukan **rpm sambungan** — di putaran berapa centrifugal clutch mulai menggigit.

| Clutch spring | Efek |
|---|---|
| Lebih keras | sambung di rpm lebih tinggi → launch lebih agresif |
| Lebih lunak | sambung lebih awal → launch lebih halus |

**Untuk drag:** rpm sambungan harus cukup tinggi supaya mesin sudah berada di daerah bertenaga saat clutch menggigit — tapi tidak terlalu tinggi sampai roda spin atau clutch terbakar.

Titik awal yang wajar: **rpm sambungan sekitar 60–70% dari rpm tenaga puncak**.

### 3.4 Urutan penyetelan

1. **Clutch spring** dulu — tentukan rpm launch
2. **Roller** — tentukan rpm yang ditahan saat akselerasi
3. **Torque spring** — haluskan, dan perbaiki kalau rpm jatuh di tengah akselerasi
4. **Ulangi** — ketiganya saling mempengaruhi

**Satu perubahan per run.** Sama seperti di dyno.

---

## 4. Rasio, kecepatan, dan gear

### 4.1 Rumus dasar

```
v [km/h] = 0,06 × π × D_roda[m] × rpm / i_total
```

dengan `i_total` = rasio CVT × rasio final gear.

### 4.2 Mengkalibrasi rasio total

**Jangan tebak dari katalog.** Hitung dari satu titik data terukur:

```
i_total = 0,06 × π × D_roda × rpm / v_terukur
```

Contoh untuk roda Ø0,56 m: [HITUNG]

| RPM | v terukur | i_total |
|---|---|---|
| 8.500 | 110 km/h | 8,16 |
| 9.000 | 120 km/h | 7,92 |
| 10.000 | 130 km/h | 8,12 |

Konsisten di sekitar **8,1** — itulah rasio total mesin itu pada CVT rasio tertinggi.

**Ukur diameter roda saat terpasang dan terbebani**, bukan diameter nominal ban. Selisihnya bisa 3–5%.

### 4.3 Tabel kecepatan

Roda Ø0,56 m: [HITUNG]

| i_total | 10.000 rpm | 11.000 | 12.000 | 13.000 |
|---|---|---|---|---|
| 6,0 | 176 | 194 | 211 | 229 |
| 6,5 | 162 | 179 | 195 | 211 |
| 7,0 | 151 | 166 | 181 | 196 |
| 7,5 | 141 | 155 | 169 | 183 |
| 8,0 | 132 | 145 | 158 | 172 |

*(km/h)*

---

## 5. Memilih gear untuk lintasan tertentu

### 5.1 Temuan yang mengejutkan

Simulasi akselerasi 500 m dengan 30 HP di roda, massa 150 kg: [HITUNG]

| i_total | v batas | Waktu | v finish | |
|---|---|---|---|---|
| 5,5 | 230 km/h | **14,23 s** | 160 km/h | |
| 6,5 | 195 | **14,23 s** | 160 | |
| 7,5 | 169 | **14,23 s** | 160 | |
| 8,5 | 149 | 14,45 s | 149 | mentok limiter |
| 9,5 | 133 | 15,26 s | 133 | mentok limiter |
| 10,5 | 121 | 16,31 s | 121 | mentok limiter |

**Selama limiter tidak tersentuh, rasio gear TIDAK mempengaruhi waktu sama sekali.**

### 5.2 Kenapa begitu

CVT menahan mesin di tenaga puncak apa pun rasionya. Percepatan cuma bergantung pada tenaga yang tersedia, bukan pada rasio.

Ini **berbeda total dari motor gear**, di mana pemilihan gear sangat menentukan.

### 5.3 Kapan gear jadi penting

Hanya dalam dua kondisi:

**1. Gear terlalu pendek** → mentok limiter sebelum garis finish. Setelah mentok, mesin tidak bisa menambah kecepatan lagi. Ini kerugian yang jelas dan besar.

**2. Gear terlalu panjang** → CVT tidak sempat mencapai rasio tertinggi dalam jarak yang tersedia, atau clutch terlalu lama slip di awal.

### 5.4 Aturan praktis

> **Pilih gear supaya kecepatan di garis finish PAS mendekati kecepatan batas.**

Dari tabel di atas, i_total sekitar **7,5–8,0** adalah pilihan yang tepat: kecepatan batas 169 km/h, kecepatan finish 160 km/h — mendekati, tapi tidak mentok.

**Margin 5–10% di bawah batas** memberi ruang kalau kondisi lintasan lebih baik daripada perkiraan.

### 5.5 Cara memverifikasi di lintasan

Pasang datalogger atau racebox, lalu periksa:

- [ ] **RPM di garis finish** — harus mendekati rpm tenaga puncak, tidak menyentuh limiter
- [ ] **RPM selama akselerasi** — harus datar di rpm tenaga puncak, tidak naik-turun
- [ ] **RPM saat launch** — harus di daerah bertenaga

Kalau rpm naik-turun selama akselerasi, CVT-nya belum benar — bukan mesinnya.

---

## 6. Di mana tenaga hilang di CVT

### 6.1 Sumber kerugian

| Sumber | Besarnya |
|---|---|
| Slip belt | 3–15% |
| Gesekan belt–pulley | 3–5% |
| Gesekan roller di jalur | 1–2% |
| Final gear | 2–3% |
| Clutch slip (kalau tidak sempurna) | 0–10% |

**Total 10–30%** — itulah selisih antara tenaga mesin dan tenaga di roda.

### 6.2 Yang paling sering merusak

**Belt aus atau salah ukuran**

Belt yang aus jadi lebih tipis, sehingga posisinya di pulley berubah — rasio tertinggi tidak tercapai. Belt yang terlalu panjang juga sama akibatnya.

**Cek:** ukur lebar belt dan bandingkan dengan spesifikasi baru. Selisih 1 mm sudah berarti.

**Permukaan pulley aus atau tergores**

Alur bekas belt di permukaan kerucut membuat belt tidak bisa bergeser mulus. Rasio jadi tersendat.

**Cek:** raba permukaan pulley. Kalau terasa beralur, ganti atau bubut.

**Roller aus tidak merata (peyang)**

Roller yang sudah gepeng di satu sisi tidak bisa berguling dengan lancar. Perubahan rasio jadi tersendat dan rpm naik-turun.

**Cek:** roller harus bulat sempurna. Kalau ada bagian rata, ganti semuanya — jangan sebagian.

**Clutch pad glazing**

Permukaan pad yang mengkilap licin menyebabkan slip berkepanjangan.

**Cek:** permukaan pad harus kasar merata. Amplas kalau mengkilap, atau ganti.

**Pulley sekunder macet**

Permukaan yang bisa bergerak harus meluncur bebas. Kalau seret karena kotoran atau karat, rasio tidak berubah dengan benar.

### 6.3 Panas

CVT menghasilkan panas besar, dan panas mengurangi cengkeraman belt.

- Pastikan jalur ventilasi CVT tidak tersumbat
- Untuk drag, kondisi dingin di run pertama biasanya paling baik
- Belt yang terlalu panas akan slip dan kehilangan tenaga secara drastis

---

## 7. Kesalahan umum

| Kesalahan | Akibat |
|---|---|
| Menyetel CVT sebelum mesin final | pekerjaan diulang |
| Roller berat supaya "torsi bawah kuat" | mesin ditahan di bawah rpm tenaga puncak — lebih lambat |
| Torque spring sekeras mungkin | gesekan besar, panas, tenaga terbuang |
| Gear dipendekkan supaya "akselerasi galak" | mentok limiter sebelum finish |
| Belt murah atau bekas | slip, tenaga hilang tanpa terlihat |
| Menilai CVT dari rasa, bukan dari data rpm | tidak akan pernah optimal |

---

## 8. Ringkasan Tahap 9

1. **CVT menahan mesin di satu rpm** — karena itu tenaga puncak lebih penting daripada rentang rpm yang lebar.
2. **Setel CVT ke rpm tenaga puncak**, bukan torsi puncak.
3. **Roller adalah penyetelan paling berpengaruh.** Lebih ringan = rpm ditahan lebih tinggi.
4. **Kalibrasi rasio total dari data terukur**, jangan dari katalog.
5. **Selama limiter tidak tersentuh, rasio gear tidak mempengaruhi akselerasi.** Ini berbeda total dari motor gear.
6. **Gear terlalu pendek jelas merugikan** — mentok limiter sebelum garis.
7. **Pilih gear supaya kecepatan finish mendekati batas**, dengan margin 5–10%.
8. **CVT bisa memakan 10–30% tenaga.** Belt, pulley, roller, dan pad harus diperiksa.
9. **RPM yang naik-turun saat akselerasi** berarti CVT belum benar, bukan mesinnya.
10. **Setel CVT terakhir**, setelah mesin final.

**Berikutnya:** Tahap 10 — simulasi dan validasi. Tahap ini opsional.
