# Serah terima proyek — Advanced Engine Tuning

Dokumen ini untuk melanjutkan proyek buku di Claude Cowork (atau sesi baru mana pun). Isinya: struktur buku, konvensi penulisan, peta di mana temuan konsultasi sudah dimasukkan, dan apa yang masih tersisa. Baca seluruhnya sebelum mengubah bab mana pun.

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

## 3. Temuan konsultasi — sudah dimasukkan ke buku (26 September 2026)

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
| Status build XMAX: throat terukur, flange port, batas 9.000 rpm, spesifikasi porting, powerband CVT | `build/XMAX-344-BUILD-SPEC.md` |

Catatan konvensi durasi: tabel Mesin Contoh B memakai **@1 mm**; data durasi kiriman pemilik (XMAX 260°, Aerox 261/270°) konvensinya tidak diketahui. Karena itu K selalu dikalibrasi per mesin dengan cam yang sama.

**Masih ditunggu dari pemilik XMAX:** rasio kompresi, ukuran knalpot + durasi buang, panjang rod, jenis bantalan crank, berat paket piston, peta CSA port (cetakan silikon + scan), satu motor acuan di dyno yang sama.

## 4. Belum masuk buku

- **Vespa 3 klep 67 × 58 (204,5 cc), trek 1,5 km:** klep isap ideal Ø24,25 × 2; bila mentok Ø23, throat digarap ke TR 0,935 (726 mm², hanya −2,9%). Rekomendasi: durasi ~270°, peak ~12.500 rpm, ~48,6 hp metanol; klep buang Ø26,7; piston race-spec ringan wajib (beban big end plain bearing). *Catatan: angka rpm/hp Vespa dihitung dengan `v = 104 m/s` dari rumus lama yang sudah dikoreksi (Tahap 4 §3.4) — hitung ulang dengan K terkalibrasi dari mesin serupa sebelum dipakai.*
- **Aerox 63 × 72 (224 cc):** 41 hp @ 11.000 (Pertamax Turbo), klep 23/20, TB 40, cam 261/270, CR 14.
