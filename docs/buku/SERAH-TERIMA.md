# Serah terima proyek — Advanced Engine Tuning

Dokumen ini untuk melanjutkan proyek buku di Claude Cowork (atau sesi baru mana pun). Isinya: struktur buku, konvensi penulisan, peta di mana temuan konsultasi sudah dimasukkan, dan apa yang masih tersisa. Baca seluruhnya sebelum mengubah bab mana pun.

---

## 1. Struktur

| Berkas | Isi |
|---|---|
| `00-PENGANTAR.md` | Pengantar |
| `01-KAMUS-ISTILAH.md` | Kamus istilah (acuan terminologi) |
| `02` … `12` | Tahap 1–11 (mengukur, konfigurasi, aliran, camshaft, kompresi/BBM, pengapian/AFR, saluran, mekanik, CVT, simulasi, kalibrasi) |
| `13-LAMPIRAN.md` | Lampiran: rumus ringkas (A), daftar periksa (C), data mesin (D), pembanding (E) |
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

## 3. Temuan konsultasi — semuanya sudah dimasukkan ke buku (26 September 2026)

| Temuan | Lokasi di buku |
|---|---|
| Koreksi "validasi K × v = 8" (identitas aljabar); K dikalibrasi per mesin; MGV throat | Tahap 4 §3.4, Lampiran A.5, Kamus (Time-Area, MGV) |
| Teorema bore-up hanya untuk mesin yang dibatasi aliran isap | Tahap 4 §3.5 |
| Konvensi durasi, kepenuhan lobe Φ, lift tinggi melandai, prosedur ukur, proksi | Tahap 4 §3.7, §7, Kamus (Durasi, Lift Kritis), Lampiran A.5 |
| Rasio port/throat < 1 sebagai tuas rpm peak; step anti-reversion | Tahap 3 §5.4, §6.5 |
| Batang valve & boss guide | Tahap 3 §6.6 |
| Plain bearing; "tempa ≠ ringan"; rumus massa vs rpm | Tahap 8 §1.4, §1.6, §2.2 |
| Salah basis luas (port vs throat) | Tahap 11 §3.4 |
| Jangkar TB dari mesin pabrikan; batas hadiah TB | Tahap 11 §5.3 |
| Studi pembanding CRF450R; dyno kemungkinan membaca tinggi | Tahap 11 §11, Lampiran E |
| Koreksi baris Mesin Contoh A di Lampiran E (109/105 → 100/97 m/s) | Lampiran E |
| Sisi buang: rasio 4 valve pabrikan, pembanding kecepatan dengan basis yang sama, tuas aman di bawah batas rpm | Tahap 3 §2.3, §5.5 |
| Luas setara-aliran, kecepatan rata vs pinch disengaja, hambatan seri | Tahap 3 §5.6, Tahap 7 §3.3, Lampiran A.3 |
| Porting dengan batas rpm: anggaran, pinch di manifold cetak, port dulu cam belakangan; finishing | Tahap 3 §8, §8.1 |
| Jangkar TB ~60–80 m/s; downdraft & panjang tersedia; bellmouth (datum, ruang bebas, oval, menyatu dinding); taper ≤7°; koreksi arah step manifold; material saluran & suhu udara | Tahap 7 §1.2, §2.8, §3.2–3.6, Lampiran A.7c |
| Stroke panjang menutup rpm; di bawah batas rpm tinggal BMEP | Tahap 8 §1.1 |
| Powerband lebar di CVT harian | Tahap 9 §2.4 |
| Skala Pa → hp, suhu, harmonik, material | Tahap 11 §10.3 |
| Data Vespa 150 terukur (throat, port), panjang saluran untuk durasi 270° | Lampiran D.3 |
| Rancangan Vespa 3 valve 204cc trek | Lampiran D.4 |
| Aerox 224cc (dan status verifikasinya) | Lampiran D.5 |
| Kartu data XMAX 345cc | Lampiran D.6 |
| Status build XMAX: throat terukur, flange port, batas 9.000 rpm, spesifikasi porting, powerband CVT | `build/XMAX-344-BUILD-SPEC.md` |

Catatan konvensi durasi: tabel Mesin Contoh B memakai **@1 mm**; data durasi kiriman pemilik (XMAX 260°, Aerox 261/270°) konvensinya tidak diketahui. Karena itu K selalu dikalibrasi per mesin dengan cam yang sama.

**Masih ditunggu dari pemilik XMAX:** **luas flange isap yang sebenarnya** (801 mm² kalau elips, ~938 kalau oval bersudut — menentukan seluruh ukuran porting), rasio kompresi, ukuran knalpot + durasi buang, panjang rod, jenis bantalan crank, berat paket piston, peta CSA port (cetakan silikon + scan), satu motor acuan di dyno yang sama.

## 4. Yang tidak bisa dipulihkan

Transkrip percakapan sebelum 8 September 2026 tidak tersimpan. Temuan dari periode itu sudah masuk buku lewat PR #3, kecuali tiga jawaban yang angkanya tidak tercatat di mana pun:

- **Ukuran klep kepala 4 valve untuk 63 × 70 mm** — hitung ulang dengan Tahap 3 §2 (rasio luas valve/bore dan cek muat) dan §3.4 (rasio throat buang/isap).
- **Panjang runner Vespa 150 untuk cam 270°** — tabel panjang per harmonik sudah ada di Lampiran D.3; rpm sasarannya perlu K yang dikalibrasi.
- **Latihan konversi 200cc 2 valve → 3 valve** (sempat diusulkan sebagai "Mesin Contoh D") — rinciannya tidak tersimpan.
