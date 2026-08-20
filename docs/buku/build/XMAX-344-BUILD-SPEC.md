# XMAX 344cc — Build Spec Final

**Dokumen kerja.** Semua angka di sini diturunkan dari spesifikasi dan pengukuran mesin ini sendiri, memakai metode di *Advanced Engine Tuning* Tahap 7 (Saluran), Tahap 9 (CVT), dan Tahap 11 (Kalibrasi).

Terakhir diperbarui: 20 Agustus 2026

---

## 1. Kondisi mesin saat ini

### 1.1 Dasar

| | |
|---|---|
| Basis | Yamaha XMAX 300 (292,1cc — bore 70,0 × stroke 75,9) |
| Bore sekarang | **76,0 mm** |
| Stroke | **76,0 mm** |
| **Kapasitas** | **344,8 cc** |
| Kenaikan dari standar | +18,0% |
| Konfigurasi | 1 silinder, 4 klep, SOHC |
| Penyaluran | CVT |

### 1.2 Kepala silinder

| | |
|---|---|
| Klep isap | 28,0 mm × 2 |
| Klep buang | 22,5 mm × 2 |
| Rasio throat/klep | 0,935 |
| **Luas throat isap total** | **1.077 mm²** |
| Rasio klep isap / bore | 0,368 (2 klep × 28 / 76) |
| Porting | standar, dirapikan (tidak diperbesar) |

### 1.3 Camshaft

| | |
|---|---|
| Durasi | **260°** |
| Status | sudah dimodifikasi |

### 1.4 Saluran isap

| | |
|---|---|
| Panjang klep → ujung TB | **250 mm** |
| Throttle body | **36 mm** (standar, tidak diubah) |
| Piping TB → boks plenum | **240 mm** |
| Diameter pipa di TB | **42,5 mm** |
| **Panjang total tract** | **490 mm** |
| Volume plenum | ~3,0 L (tutup aftermarket, lebih kecil dari standar) |
| Filter mesh | 265 × 85 mm (22.525 mm²) |
| Lubang inlet | 2 slot kotak 87 × 17 mm (2.958 mm² total) |

### 1.5 Manajemen mesin

| | |
|---|---|
| ECU | MiniXX (versi Mini, bukan Super) |
| Sensor | MAP terpasang |
| Tabel RPM vs MAP | **terkunci** — tidak bisa diedit |
| Tabel RPM vs TPS | terbuka, saat ini **100 di semua sel** (netral) |
| Konsekuensi | seluruh penentuan bahan bakar berjalan lewat sinyal MAP |

---

## 2. Data dyno — dan mengapa harus dibaca ulang

### 2.1 Yang tertulis di sheet

Leads dyno inersia, 3,3 kg·m², roller Ø267 mm, **tanpa locked ratio pulley**.

```
Peak power :  40,6 hp @ 6.563 rpm
Peak torsi :  68,18 Nm @ 2.103 rpm
Kolom Ratio:  3,95 (tetap)
```

### 2.2 Uji BMEP — sheet ini tidak lolos

| Titik | Torsi | BMEP | vs KTM 690 SMC R di titik setara |
|---|---|---|---|
| 40,6 hp @ 6.563 rpm | 44,1 Nm | **16,05 bar** | 1,34× |
| 68,18 Nm @ 2.103 rpm | 68,2 Nm | **24,85 bar** | 1,86× |

Single NA yang dikembangkan penuh oleh pabrikan mencapai 11,9 bar di peak power dan 13,3 bar di peak torsi. Kedua angka di atas melampauinya.

### 2.3 Vonis: kesalahan rasio, bukan kesalahan kalibrasi

Faktor kelebihannya **tidak konstan** — 1,34× di peak power, 1,86× di peak torsi, membesar ke arah rpm rendah.

Kesalahan kalibrasi (inersia, faktor koreksi) akan memberi faktor yang **sama** di kedua titik. Yang membesar progresif ke rpm rendah adalah tanda tangan **rasio CVT yang bergeser** sementara software memakai `Ratio 3.95` yang tetap.

### 2.4 Apa yang bisa dan tidak bisa dipakai

| Besaran | Status |
|---|---|
| **Tenaga 40,6 hp** | ✅ dipakai — dihitung dari percepatan roller, tidak menyentuh rpm mesin |
| Sumbu Engine RPM | ❌ dibuang |
| Torsi 68,18 Nm | ❌ dibuang — turunan dari rpm yang rusak |
| Posisi peak di 6.563 rpm | ❌ dibuang |

### 2.5 Peak power sebenarnya

| Kalau BMEP-nya | 40,6 hp terjadi di |
|---|---|
| 11,5 bar | 9.162 rpm |
| 12,0 bar | 8.781 rpm |
| 12,5 bar | 8.429 rpm |
| 13,0 bar | 8.105 rpm |

**Rentang kerja: 7.800 – 8.800 rpm.** Diasumsikan 40,6 hp sudah crank-corrected oleh software (lazim di Leads). Kalau ternyata WHP mentah, peak bergeser ke ~9.800–10.000 rpm — tinggi untuk cam 260°, jadi bacaan crank lebih mungkin.

### 2.6 Cek silang — rentang itu wajar

| rpm | v throat isap | v TB | MPS |
|---|---|---|---|
| 7.800 | 77 m/s | 81 m/s | 19,8 m/s |
| 8.100 | 80 m/s | 85 m/s | 20,5 m/s |
| 8.500 | 84 m/s | 89 m/s | 21,5 m/s |
| 8.800 | 87 m/s | 92 m/s | 22,3 m/s |

Semua di bawah batas. Throat masih di bawah rentang kerja mesin tertala (97–115 m/s), MPS masih di bawah Mesin Contoh A (21,3 m/s @ 10.000 rpm). **Lolos.**

---

## 3. Tumpukan rugi — di mana restriksi sebenarnya

**@8.400 rpm, aliran puncak** (`ρ` = 1,184 kg/m³, VE 0,85):

| Titik | K | v | Δp | Bisa diubah? |
|---|---|---|---|---|
| **Mulut pipa menonjol ke plenum** | 0,9 | 62,9 m/s | **2.108 Pa** | ✅ ya |
| TB butterfly 36 mm | 0,25 | 87,7 m/s | 1.138 Pa | ❌ TB tetap standar |
| Mulut pipa rata bertepi tajam | 0,5 | 62,9 m/s | 1.171 Pa | ✅ ya |
| Penyempitan 42,5 → 36 tepi tajam | 0,141 | 87,7 m/s | 643 Pa | ✅ ya |
| Slot inlet (aliran teredam boks) | 0,5 | 13,9 m/s | 57 Pa | ✅ ya |

**Setelah diperbaiki:**

| Titik | K | Δp |
|---|---|---|
| Mulut pipa dengan bellmouth | 0,05 | 117 Pa |
| Penyempitan dikerucutkan | 0,05 | 228 Pa |
| Slot inlet diradius | 0,2 | 23 Pa |

```
Total dapat diperbaiki  : ~2.400 Pa  = 2,4% tekanan atmosfer
Rugi TB (tidak diubah)  :  1.138 Pa
```

**Yang bisa diperbaiki lebih besar daripada rugi throttle body itu sendiri.**

> ⚠️ Angka mulut pipa mengasumsikan pipanya saat ini **menonjol masuk ke dalam boks** (K = 0,9). **Ini harus diperiksa langsung dulu.** Kalau ternyata sudah rata (K = 0,5) hematnya jadi ~1.050 Pa; kalau sudah beradius, item ini hilang dari daftar.

---

## 4. Yang akan diubah

### 4.1 Prioritas 1 — Bellmouth di mulut pipa plenum

| | |
|---|---|
| Radius | **7,5 mm** (0,18 × 42,5 → Cf ~0,97) |
| Bentuk | torus penuh, menyatu mulus ke bore pipa, **tanpa step** |
| OD mulut jadi | ~62 mm |
| Ruang bebas depan | **≥ 42 mm** ke dinding seberang (ideal 64 mm) |
| Ruang bebas radial | **≥ 21 mm** ke segala arah |
| Nilai | **~1.990 Pa** @8.400 rpm |

**Ruang bebas ini wajib.** Bellmouth yang mulutnya rapat ke dinding hanya tepi tajam yang mahal.

### 4.2 Prioritas 2 — Kerucut 42,5 → 36 masuk TB

| | |
|---|---|
| Bentuk | kerucut landai atau radius generous, bukan step |
| K | 0,141 → 0,05 |
| Nilai | **415 Pa** @8.400 rpm |

### 4.3 Prioritas 3 — Boks plenum

| | |
|---|---|
| **Volume** | **3,0 – 6,0 L** (rentang sah dari kriteria dekopling + responsivitas inlet) |
| Sasaran | sisi atas rentang, **4,5–5,0 L**, karena ECU speed-density tabel terkunci |
| Riak yang dicapai | 9,8% → **5,9–6,5%** |
| **Prioritas** | **ruang bebas bellmouth di atas mengejar liter** |
| Proporsi | dimensi internal terpanjang ≤ ~400 mm |
| **Orientasi pipa** | masuk lewat **muka ujung kecil**, mengarah menyusuri sisi terpanjang |
| Filter | di muka lebar, tegak lurus sumbu bellmouth — tidak boleh menyemprot langsung ke mulut |
| Dinding | **kaku dan berusuk** — lenturan mengaburkan sinyal MAP |

Dimensi internal usulan (sesuaikan packaging, pertahankan urutan prioritasnya):

```
                    filter 265 x 85  (muka atas)
        ┌──────────────────────────────────────────┐
        │  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░            │
   ═════╡)                                         │   internal:
  pipa  │ ^bellmouth R7,5                          │   300 (P) x 155 (L) x 110 (T)
  Ø42,5 │  mulut masuk ~28mm ke dalam boks         │   = 5,1 liter
        │                                          │
        └──────────────────────────────────────────┘
        │←────────── 300mm, sumbu pipa ───────────→│

   ruang bebas: radial 46/24mm, depan ~270mm  ✅
```

### 4.4 Prioritas 4 — Nipel MAP diberi peredam

| | |
|---|---|
| Orifis | **Ø0,8 – 1,0 mm** di jalur selang |
| Volume redam | kecil, setelah orifis |
| Alasan | 1 silinder speed-density = kasus riak terburuk, dan tabel dasarmu terkunci |
| Nilai | bukan tenaga — tapi menentukan apakah tenaga itu terbakar dengan AFR benar |

### 4.5 Prioritas 5 — Tepi slot inlet

| | |
|---|---|
| Luas | **tidak diubah** — 2.958 mm² sudah lolos uji responsivitas sampai > 6 L |
| Tindakan | radiuskan tepinya, R ≥ 3 mm |
| Nilai | ~34 Pa |

Kerjakan hanya karena boks memang sudah terbuka.

### 4.6 Piping — **tidak diubah**

| Tala h2 ke | L total | Pipa |
|---|---|---|
| 7.800 rpm | 496 mm | **246 mm** |
| 8.100 rpm | 477 mm | 227 mm |
| 8.400 rpm | 460 mm | 210 mm |
| 8.800 rpm | 439 mm | 189 mm |

**Pipa 240 mm yang terpasang sekarang sudah berada di dalam rentang** — setara menala h2 ke ~7.900 rpm.

**Tindakan:** pertahankan 240 mm, tapi **buat bisa ditukar** (siapkan 240 / 210 / 190 mm). Potong ke ~210 mm hanya kalau tacho jalan menunjukkan CVT menahan di 8.400+.

---

## 5. Yang TIDAK dikerjakan, dan alasannya

| Tidak dikerjakan | Alasan |
|---|---|
| Memperbesar throttle body | keputusan yang sudah diambil; rugi 1.138 Pa, lebih kecil dari yang bisa dihemat di plenum |
| Memperbesar luas slot inlet | sudah lolos uji responsivitas inlet sampai > 6 L |
| Mengejar volume plenum > 6 L | di luar rentang dekopling; mengorbankan ruang bebas bellmouth demi liter adalah pertukaran yang rugi |
| Memperpendek tract ke ~180 mm | rekomendasi lama yang berdasar plafon TB karangan; TB tidak pernah mentok, cuma pelan-pelan makin mahal |
| Memperpanjang piping ke 345 mm | rekomendasi lama yang menala ke 6.500 rpm — rpm yang mesin ini tidak pernah datangi |
| Velocity stack panjang di dalam boks | menambah panjang efektif, menggeser tangga harmonik turun, melawan sasaran |

---

## 6. Yang masih perlu diukur

| # | Yang diukur | Cara | Mengunci apa |
|---|---|---|---|
| 1 | **Bentuk mulut pipa di dalam plenum** | buka boks, lihat langsung: menonjol / rata-tajam / beradius? | apakah item Prioritas 1 bernilai 1.990 / 1.050 / 0 Pa |
| 2 | **Rpm tahan CVT** saat akselerasi penuh | tacho yang bisa dibaca saat jalan (Tahap 9 §3.1) | panjang pipa final |
| 3 | **Volume plenum aktual** | isi air/beras lalu takar | posisi di rentang 3–6 L |
| 4 | **Run dyno locked ratio pulley** | atau umpankan rpm asli dari pickup pengapian | seluruh sumbu rpm dan kurva torsi |

Nomor 1 dan 2 murah dan mengunci dua keputusan terbesar. Nomor 4 menyelesaikan semuanya permanen.

---

## 7. Urutan kerja

1. **Periksa mulut pipa** (nomor 1 di atas) — sebelum apapun dibeli atau dipotong
2. **Ukur rpm tahan CVT** dengan tacho jalan
3. Bangun boks: **bellmouth + ruang bebas** dulu, volume mengikuti
4. Kerucutkan peralihan 42,5 → 36
5. Pasang orifis peredam MAP
6. Radiuskan tepi slot inlet
7. Pasang, jalankan, lalu **pakai tabel RPM vs TPS** (yang masih 100 semua) sebagai koreksi bahan bakar
8. Run dyno ulang — **dengan locked ratio pulley kali ini**

---

## 8. Ringkasan angka

| | Sekarang | Setelah |
|---|---|---|
| Kapasitas | 344,8 cc | tidak berubah |
| Throttle body | 36 mm | tidak berubah |
| Panjang tract | 490 mm | tidak berubah (pipa jadi bisa ditukar) |
| Volume plenum | ~3,0 L | 4,5 – 5,0 L |
| Riak MAP | 9,8% | 5,9 – 6,5% |
| Rugi saluran yg dapat diperbaiki | ~2.808 Pa | ~368 Pa |
| Perkiraan gain di rpm atas | — | **~2,4% VE** |
| Peak power sebenarnya | 40,6 hp @ 7.800–8.800 rpm | penalaan tetap di rentang itu |

---

*Metode: Advanced Engine Tuning — Tahap 7 §1.2 (kecepatan TB), §3.2 (bellmouth), §3.4 (volume plenum); Tahap 9 §2–3 (rpm kerja CVT); Tahap 11 §7 (studi kasus plenum), §8–9 (uji BMEP & rasio), §10 (rancang plenum dari sasaran).*
