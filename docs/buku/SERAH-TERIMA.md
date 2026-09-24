# Serah terima proyek — Advanced Engine Tuning

Dokumen ini untuk melanjutkan proyek buku di Claude Cowork (atau sesi baru mana pun). Isinya: struktur buku, konvensi penulisan, dan **semua temuan konsultasi yang belum masuk ke buku**. Baca seluruhnya sebelum mengubah bab mana pun.

---

## 1. Struktur

| Berkas | Isi |
|---|---|
| `00-PENGANTAR.md` | Pengantar |
| `01-KAMUS-ISTILAH.md` | Kamus istilah (acuan terminologi) |
| `02` … `12` | Tahap 1–11 (mengukur, konfigurasi, aliran, camshaft, kompresi/BBM, pengapian/AFR, saluran, mekanik, CVT, simulasi, kalibrasi) |
| `13-LAMPIRAN.md` | Lampiran rumus (A.1–A.9b) |
| `00-BUKU-LENGKAP.md` | **Hasil gabungan** — jangan diedit langsung; dibuat ulang dari bab-bab |
| `build/XMAX-344-BUILD-SPEC.md` | Dokumen kerja build XMAX 344cc pemilik |
| `export/ADVANCED-ENGINE-TUNING-mobile.pdf` | PDF format layar HP (390 × 844 px) |
| `tools/render-pdf.js` | Skrip pembuat PDF |

**Membuat ulang buku gabungan:** gabungkan front matter, `00-PENGANTAR.md` (tanpa 3 baris pertama), lalu bab `01`–`13` berurutan; jumlah kata dimasukkan ke baris judul.

**Membuat ulang PDF:** lihat komentar di `tools/render-pdf.js` (Node + `marked` + Playwright/Chromium). Di Cowork, alternatifnya: ekspor `00-BUKU-LENGKAP.md` ke PDF dengan ukuran halaman 390 × 844 px, margin 14/16 px, font 12,5 px.

## 2. Konvensi

- Bahasa Indonesia. Desimal pakai koma (12,5), ribuan pakai titik (8.400).
- Istilah mengikuti `01-KAMUS-ISTILAH.md` (throat, tirai klep, time-area, BMEP, MPS, plenum, bellmouth, dll.).
- Setiap angka diturunkan dari sasaran dan pengukuran, bukan dipinjam dari "standar". Asumsi ditulis sebagai asumsi.
- Kesalahan yang ditemukan tidak dihapus diam-diam; dijadikan pelajaran (contoh: Tahap 11 §10.3).

## 3. Temuan yang BELUM masuk buku

### 3.1 Koreksi wajib — Tahap 4 §3.4 (dan Lampiran A.5)

Tabel "validasi" `K × v = 8,01` pada tiga mesin adalah **identitas aljabar**, bukan temuan. Kolom v di tabel itu dihitung sebagai `v_Heywood × 240/durasi`, sehingga:

```
K × v = [A·dur/(Vd·rpm)] × [Vd·rpm·240/(30·A·dur)] = 240/30 = 8   (untuk mesin apa pun)
```

Bukti: 344cc → 89,6 × 240/260 = 82,7 (tabel: 83); 224cc → 113,3 × 240/261 = 104,2 (tabel: 104).

Yang tetap berlaku:
- **Kalibrasi mandiri dalam satu mesin** (skala proporsional dari titik terukur).
- **Teorema bore-up tanpa upgrade klep (§3.5)** hanya untuk mesin yang peak-nya **dibatasi aliran isap**.

Yang harus menggantikan: kecepatan throat Heywood `v = Vd[cc] × rpm / (30 × A[mm²])` (tidak bergantung durasi) sebagai metrik antar-mesin; K dikalibrasi per mesin.

Juga wajib ditambahkan: **luas A di rumus time-area harus selalu luas throat kotor**, konsisten dengan kalibrasinya. Mencampur basis (mis. memakai luas port) merusak kalibrasi — kesalahan ini sempat terjadi di konsultasi XMAX (v palsu 111 m/s vs benar 87,2 m/s).

### 3.2 Tambahan Tahap 4 — konvensi durasi & kepenuhan lobe

- **Konvensi durasi:** konstanta dan contoh di buku memakai durasi **advertised/seat-to-seat (~0,15–0,25 mm lift)**. Konversi kasar ke @1 mm: −15 s/d −25° (ramp landai −25 s/d −35°, ramp agresif −10 s/d −18°); ke @0,050": −20 s/d −30°. Selisih 20° ≈ 7% rpm peak.
- **Lift penyeberangan:** `L = A_throat_per_klep / (π × D_klep)`. Di atas lift ini, lift tambahan tidak menambah luas alir. Contoh: Vespa klep 23 throat 21,5 → 5,03 mm; XMAX klep 28 throat 25,5 → 5,81 mm.
- **Kepenuhan efektif:** `Φ = ∫ min(π·D·L(θ), A_throat) dθ / (A_throat × durasi)`; `durasi_efektif = durasi × Φ/Φ_acuan`. Contoh ilustratif (280°, lift 8,5 mm, model sin^n): gendut Φ 0,912 → setara 317°; sedang 0,806 → 280°; kurus 0,687 → 239°. Rentang realistis Φ ≈ 0,65–0,85.
- **Prosedur ukur:** degree wheel + dial indicator, baca lift tiap 5° (2° di ramp), hitung A_eff tiap titik, integral trapesium.
- **Proksi lapangan:** selisih durasi advertised vs @1 mm kecil (10–18°) = lobe gendut; besar (28–35°) = kurus.
- **Saran pemesanan cam:** minta tabel lift-vs-derajat, bukan satu angka durasi.

### 3.3 Tambahan Tahap 4/8 — batang klep & boss bos klep

- Batang Ø5 di throat Ø25,5 = 3,8% luas. Boss OD 9–11 yang menonjol ke bowl = 12,5–18,6%.
- Hambatan langsung batang kecil (~230 Pa polos, ~42 Pa dibentuk tetesan air); kerugian besar dari **wake boss yang jatuh ke bowl** (flow bench 3–6%).
- Rumus time-area tetap memakai throat kotor (batang sudah terserap di kalibrasi). Spesifikasi luas **cabang port harus dihitung bersih** dari boss/batang.
- Aturan: pendekkan boss keluar dari bowl, ujung dibentuk tetesan air, guide tidak dipotong, sisakan 1,5–2 mm dinding.

### 3.4 Tambahan Tahap 8 — plain bearing & massa bolak-balik

- Plain bearing bukan pembatas rpm (R6 16.500, F1 20.000 rpm memakainya); pembatasnya beban inersia `F = m·r·ω²·(1+λ)` dan pasokan oli.
- "Forged" tidak berarti ringan — piston forged "street" sering 5–15% lebih berat dari cast OEM. Yang ringan adalah desain race (slipper skirt, compression height pendek, pin dinding tipis, ring tipis); forged hanya prasyaratnya.
- Untuk rpm lebih tinggi dengan beban big end yang sama: `m_baru = m_lama × (rpm_lama/rpm_baru)²`.

### 3.5 Studi kasus pembanding — Honda CRF450R 2021

Spesifikasi resmi: 96 × 62,1 mm, 449,5 cc, CR 13,5:1, klep isap 2 × 38 Ti, buang 2 × 31, TB 46 downdraft. Dyno Dirt Rider (roda): 57,21 hp @ 9.300; 35,64 lb-ft @ 6.930.

| | CRF450R | XMAX 344 |
|---|---|---|
| Throat isap per cc | 4,09 mm²/cc | 2,96 |
| v throat di peak (Heywood) | 76 m/s | 95 |
| TB / throat | 0,90 | 1,00 |
| v TB di peak | 84 m/s | 95 |
| MPS di peak | 19,3 | 21,3 |
| Buang/isap (luas klep) | 0,666 | 0,646 |

Pelajaran: Honda membeli napas lewat luas klep (throat longgar di peak); aturan "TB ≥ throat" atau "TB/throat 1,0–1,1" tidak berlaku; TB XMAX yang setara proporsi Honda ≈ Ø40; downdraft sah bila ada airbox. CRF juga jadi alat uji dyno: 40,6 hp XMAX di roller lewat CVT = 14,3–14,8 bar BMEP engkol, lebih tinggi dari CRF (~13,3) → dyno Leads kemungkinan membaca 8–12% tinggi.

## 4. Status build XMAX 344 (koreksi atas `build/XMAX-344-BUILD-SPEC.md`)

**Data terukur baru:**
- Klep isap 2 × 28, seat/throat **Ø25,5 → TR 0,911, throat 1.021 mm²** (spec lama menulis TR 0,935 / 1.077 — asumsi, salah).
- Klep buang **22,5** (pemilik sempat menyebut 23; dipakai 22,5).
- Flens port kepala **30 × 34 oval = 801 mm²** (siamese, satu lubang).
- TB 36 (1.018 mm²) dipertahankan.

**Kendala rancangan:** peak ≤ **9.000 rpm** (MPS 22,8 m/s; stroke 76 adalah batas struktural). 9.500 hanya dengan massa bolak-balik ≤ 387 g.

**Spesifikasi porting final:**

| Stasiun | Luas | Catatan |
|---|---|---|
| TB Ø36 | 1.018 mm² | tetap |
| Ujung manifold cetak = **pinch** | **860 / 870 / 882** | bisa diganti; peak ~8.770 / 8.830 / 8.900 |
| Flens kepala | 930 (32,0 × 37,0) | dibuka sekali |
| Cabang (bersih dari boss) | ≥ 475 per cabang | kotor 499–571 tergantung boss |
| Bowl → throat | 1.021 | mekar 2,2° setengah-sudut |

- Step anti-reversion: ujung manifold 0,4–0,7 mm/sisi lebih kecil dari flens.
- Dalam kepala, tidak boleh ada penampang lebih kecil dari ujung manifold → ukur via cetakan silikon + 3D scan.
- Item kualitas: short turn, bowl, boss keluar bowl, blending seat 3 sudut, bifurkasi, finishing isap 60–80 grit (jangan dipoles). Sisi buang boleh agresif dan dipoles (tidak menggeser peak).
- Cam 260° tetap; tract 460 mm efektif tetap (h2 8.408, h3 5.605).
- Perkiraan: +7% aliran, peak ~8.800–9.000, ~43,5 hp (angka dyno yang sama).

**Powerband lebar (CVT):** tract tetap 460; boks selalu terpasang; pinch 860–870; knalpot ditala ~7.000 rpm (isi celah h3–h2); mapping timing di 5.500–7.500; sprocket cam adjustable; CVT: kopling masuk ~5.500, rpm tahan 8.400–8.700.

**Ditolak (dengan alasan):** TB 43 (+0,15–0,30 hp, mahal di part-throttle; kalau naik, Ø40); downdraft tanpa boks (−2 s/d −5 hp; tract maks 280 mm hanya bisa h3); klep buang Ø25 (kebesaran; Ø24 hanya bila port isap dibuka besar).

**Masih ditunggu dari pemilik:** rasio kompresi, ukuran knalpot + durasi buang, panjang rod, jenis bantalan crank, berat paket piston, verifikasi dyno dengan motor acuan.

## 5. Konsultasi mesin lain (belum dicatat di buku)

- **Vespa 3 klep 67 × 58 (204,5 cc), trek 1,5 km:** klep isap ideal Ø24,25 × 2; bila mentok Ø23, throat digarap ke TR 0,935 (726 mm², hanya −2,9%). Rekomendasi: durasi ~270°, peak ~12.500 rpm, ~48,6 hp metanol; klep buang Ø26,7; piston race-spec ringan wajib (beban big end plain bearing).
- **Aerox 63 × 72 (224 cc):** 41 hp @ 11.000 (Pertamax Turbo), klep 23/20, TB 40, cam 261/270, CR 14.
