# Engine Tuning Research — Project Resume / Handoff

_Terakhir diperbarui: 2026-08-18. Sumber tunggal untuk melanjutkan pekerjaan ini._

> **Catatan:** ini thread yang **berbeda** dari `PROJECT_RESUME.md` (app Android / Velocity Stack modeller)
> dan `GENERATOR-RESUME.md` (generator intake manifold parametrik). Ketiganya berdiri sendiri.

---

## 1. Apa proyek ini

Riset dan perkakas untuk **membangun mesin 1 silinder matic (CVT) berperforma tinggi**, dengan tiga keluaran:

1. **Perkakas hitung** — 32 skrip Python yang mengubah tebakan jadi angka yang bisa diverifikasi
2. **Pipeline CFD** — flowbench virtual berbasis OpenFOAM untuk membandingkan bentuk port
3. **Buku dokumentasi** — 30.763 kata, 13 berkas, tersusun sebagai jalur belajar 10 tahap

**Filosofi pokoknya:** kalibrasi ke mesin yang sudah terbukti jalan, bukan ke tabel di buku.
Empat kali dalam proyek ini, tabel umum meleset dengan cara yang merugikan (lihat bagian 6).

---

## 2. Status sekarang

| Item | Status |
|---|---|
| Perkakas hitung analitik | ✅ 32 skrip, semua punya `_selfcheck()` |
| Buku dokumentasi | ✅ 13 berkas, 30.763 kata |
| Toolchain CFD (WSL + OpenFOAM) | ✅ terpasang dan tervalidasi |
| Generator geometri port untuk CFD | ✅ 6 penjaga otomatis |
| Validasi CFD pada kasus berjawaban pasti | ✅ pipa lurus Cf 0,879 |
| Hasil CFD port pertama yang berlaku | ✅ Cf 0,849 |
| **Sweep 36 case** | ⏸️ **ditahan atas permintaan** — pipeline siap |
| Diagram/grafik untuk buku | ❌ belum — buku sengaja dibuat tanpa gambar dulu |
| Panjang header mesin acuan | ❌ **belum diukur — variabel besar yang belum terkalibrasi** |

---

## 3. Mesin yang jadi acuan

### Mesin Contoh A — 199cc 2 klep drag matic (TERBUKTI)

Ini jangkar kalibrasi untuk seluruh proyek.

| Parameter | Nilai |
|---|---|
| Bore × stroke | 63 × 64 mm = 199,5 cc |
| Klep isap / buang | 31 / 27 mm |
| Throat isap | 29 mm (rasio 0,935) |
| Port isap / buang | Ø29,5 / Ø29 mm |
| Lift | 10,8 mm |
| Cam | IN 38 BTDC / 63 ABDC, EX 63 BBDC / 38 ATDC (281°/281°) |
| Overlap / LSA | 76° / 102,5° |
| Kompresi statis | 16:1 → **DCR 12,83** |
| Bahan bakar | bensol / avgas 100LL |
| TB / header / muffler | 38 / 30 / 50 mm |
| **Hasil** | **500 m 15,4 detik, trap 158 km/h** |

**Besaran turunan yang dipakai sebagai jangkar:**
kecepatan gas port isap **97 m/s**, port buang **101 m/s**, rasio port/throat isap **1,035**,
buang **1,49**, rasio throat ex/in **0,671**, kecepatan puncak TB **61 m/s**, **DCR terbukti 12,83**.

### Mesin Contoh B — 150cc 4 klep (RANCANGAN)

| Parameter | Nilai |
|---|---|
| Bore × stroke × rod | 57,3 × 58 × 95 mm = 149,6 cc |
| Klep isap / buang | 22 / 19 mm |
| **Throat** | **20,2 / 16,7 mm** (dinaikkan dari 19,5) |
| CSA port isap | 615–665 mm², oval 22,7 × 29,5 |
| CSA port buang | 594–653 mm², Ø setara ~28 mm |
| Cam | 261°/261°, IN 28 BTDC / 53 ABDC, EX 53 BBDC / 28 ATDC |
| ICL / LSA / overlap | 102,5° / 102,5° / 55° |
| Lift | 9,0 mm (ex boleh 7,6–9,0) |
| CR statis | 14:1 → DCR 12,07, **margin +0,76** |
| Kantong klep / dome | 2,71 mm / usir 2,45 cc |
| TB / runner / header | 36 / 155 / 29,1 mm |
| RPM sasaran | 12.000 (6.093 g di TDC) |
| Potensi | 90,7 CFM @28", ~41 HP |

### Mesin Contoh C — 155cc 3 klep (ALTERNATIF)

58 × 58,6 mm, 3 klep, pendingin udara, CR 10,5:1, 12,7 HP @ 7.750 rpm.
Luas klep isap/bore cuma **0,262** (vs 0,295 pada 4 klep) — kelemahannya di sisi isap, bukan buang.
Potensi dengan klep maksimum: ~40 HP. CR disarankan 12,5–13:1, bukan 14 (busi menepi).

---

## 4. Perkakas hitung (`tools/`)

Semua punya `_selfcheck()` yang **harus lolos** sebelum hasilnya dipakai.

### Analitik — inti proyek

| Berkas | Fungsi | Tahap buku |
|---|---|---|
| `konfigurasi.py` | square vs overbore vs overstroke | 2 |
| `port_design.py` | sizing klep/throat/port, kalibrasi ke acuan | 3 |
| `exhaust_check.py` | proporsi ex/in, keputusan durasi ex | 3 |
| `cam_design.py` | DCR, durasi, overlap, kantong klep, anggaran ruang bakar | 4 |
| `cam_dari_acuan.py` | urai timing acuan, skalakan ke mesin baru | 4 |
| `kompresi_terkalibrasi.py` | batas DCR dari mesin terbukti | 5 |
| `bahan_bakar.py` | energi per kg udara, lambda, pendinginan muatan | 5 |
| `intake_tune.py` | panjang runner, Helmholtz, wave tuning | 7 |
| `tract_profile.py` | profil luas saluran, perbandingan TB | 7 |
| `exhaust_system.py` | port buang, header, harmonik | 7 |
| `valvetrain.py` | percepatan klep, gaya inersia, kebutuhan per | 8 |
| `cvt_gearing.py` | rasio, kecepatan, pemilihan gear | 9 |
| `spek_final.py` | rangkuman spek + beban mekanis | — |
| `hp_per_liter.py` | tenaga spesifik, perkiraan HP dari lintasan | — |
| `bandingkan_mesin.py` | perbandingan F1/MotoGP/Pro Stock | — |
| `head_3klep.py` | sizing head 3 klep | — |
| `iget150.py` | baseline dan potensi mesin 3 klep standar | — |

### CFD

| Berkas | Fungsi |
|---|---|
| `port_geom.py` | generator volume fluida port → STL, **6 penjaga otomatis** |
| `cfd_case.py` | pembangun case OpenFOAM lengkap |
| `build_sweep.py` | bangun 36 case dari 36 STL |
| `report_case.py` | tarik hasil, periksa kelayakan |
| `vtk_read.py` | parser VTP/VTU ascii minimal |
| `slice_fig.py` | irisan medan CFD |
| `report_geom_fig.py` | gambar geometri port |
| `report_pdf.py` | laporan PDF |

### Diagnostik CFD

`diag_area.py`, `diag_inlet.py`, `diag_profil.py`, `diag_stl_csa.py`,
`diag_straight.py`, `diag_turb.py`, `diag_where.py`

Dibuat saat memburu bug. `diag_profil.py` yang paling berharga — ia menampilkan
**tanda** kecepatan aksial, dan itulah yang akhirnya membongkar bug terakhir.

---

## 5. Toolchain CFD

### Terpasang

- **WSL2 + Ubuntu 24.04** — 20 core, 15 GB RAM
- **OpenFOAM 1912** dari repo resmi Ubuntu (`apt install openfoam openfoam-examples`)
- Geometri dibuat di Windows (`manifold3d` + numpy), dijalankan di WSL lewat `/mnt/c/`

### Jebakan paket Debian yang HARUS diingat

| Masalah | Solusi |
|---|---|
| Environment tidak diset | `export WM_PROJECT_DIR=/usr/share/openfoam` — **jangan** source `etc/bashrc` (rusak) |
| `scotch` cuma stub kosong | pakai `method hierarchical` |
| Crash `IOstream sha1` | **hindari functionObject apa pun** — baca `phi` langsung dari file |
| Field `0/` sebelum snappy | taruh di `0.orig`, salin ke `processor*/0` setelah meshing |
| Patch `processor` tidak terdefinisi | `#includeEtc "caseDicts/setConstraintTypes"` di tiap boundaryField |
| `reconstructPar` gagal | jalankan `reconstructParMesh -constant` dulu |

### Setelan yang tervalidasi

Depresi **10"H₂O** (bukan 28" — Mach 0,19 vs 0,31, dan 28" diverge dari start dingin),
konversi hasil dengan √(Δp ratio). SIMPLE baku (**bukan** SIMPLEC), relaksasi p 0,3 / U 0,7,
3000 iterasi. Plenum **setengah bola berpusat di mulut port**, dipotong di bidang mulut.
Refinement **volume** inti port lewat STL kedua, bukan cuma permukaan.

### Hasil tervalidasi

| Kasus | Cf | K |
|---|---|---|
| Pipa lurus (kontrol berjawaban pasti) | **0,879** | 0,295 |
| Port CSA 615, aspect 1,30, ST 0,40 | **0,849** | 0,387 |

**Ongkos tikungan 37° cuma 3,4%** → port bukan pembatasnya; throat yang membatasi.

---

## 6. Temuan utama

### 6.1 Empat kali tabel umum meleset

| Tabel umum | Mesin nyata | Kerugian kalau ikut tabel |
|---|---|---|
| Throat maks 0,90 × klep | jalan di **0,935** | **7,4% flow hilang** |
| Kecepatan TB 105 m/s | jalan di **61 m/s** | **TB 8 mm terlalu kecil** |
| DCR maks 12,5 untuk bensin | jalan di **12,83** dengan avgas | kompresi diturunkan tanpa perlu |
| Lift berguna maks 0,25 × klep | jalan di **1,6–2,5× lift kritis** | cam terlalu jinak |

### 6.2 Temuan desain

- **Throat 19,5 → 20,2 mm menaikkan plafon flow +7,4%.** Satu-satunya perubahan yang menaikkan plafon.
- **Dengan lift 9 mm, tirai klep 2× luas throat** → throat pembatas 100%.
- **Mengecilkan TB tidak menaikkan gas speed di port.** Rugi port : rugi TB = 4 : 1.
- **Durasi cam turun** (281° → 261°) walau rpm naik, karena head 4 klep bernapas 29% lebih lega per cc.
- **Pada CVT, rasio gear tidak mempengaruhi akselerasi** selama limiter tidak tersentuh.
- **Overbore 143% vs overstroke 66%** potensi tenaga, pada kapasitas sama.
- **Klep titanium menaikkan batas floating 4.200 rpm** dengan per yang sama.
- **Selisih 20–30%** antara potensi head Mesin A (~35 HP) dan hasil nyata (~28 HP) →
  tersangka: panjang header dan setelan CVT, bukan porting.

### 6.3 Pelajaran metodologi (mahal)

**Sebelas simulasi CFD berturut-turut memberi hasil salah** sebelum penyebabnya ketemu.
Selama itu, **semua diagnostik numerik hijau**: mesh OK, ketimpangan massa 0,000%,
residual turun 4 dekade, viskositas turbulen normal.

Yang akhirnya membongkar:
1. **Nilai Cf yang tidak masuk akal secara fisika**
2. **Melihat TANDA kecepatan aksial**, bukan besarnya — aliran balik −15,7 m/s terbaca sebagai "lambat"

> **Aturan yang paling mahal kalau dilanggar: jalankan kasus berjawaban pasti LEBIH DULU, bukan terakhir.**

Lima bug yang ditemukan, semuanya buatan sendiri, semuanya sekarang dijaga assertion di `port_geom.py`:
tutup mulut berbentuk kerucut, klasifikasi patch outlet lewat uji jarak, plenum yang jadi jet,
flange mewarisi refinement dinding, dan mask plot yang bikin lubang palsu.

---

## 7. Buku (`docs/buku/`)

13 berkas, **30.763 kata**, tanpa gambar. Ruang lingkup: **1 silinder matic 125–250 cc, 2/3/4 klep**.

| Berkas | Kata | Isi |
|---|---|---|
| `00-PENGANTAR.md` | 1.942 | ruang lingkup, peringatan akurasi, peta 10 tahap |
| `01-KAMUS-ISTILAH.md` | 3.014 | 21 istilah, 6 kelompok |
| `02-TAHAP1-MENGUKUR.md` | 2.101 | torsi vs tenaga, powerband, dyno |
| `03-TAHAP2-KONFIGURASI.md` | 2.505 | bore/stroke, rod, jumlah klep, kruk as |
| `04-TAHAP3-ALIRAN.md` | 2.028 | klep, throat, port, bentuk |
| `05-TAHAP4-CAMSHAFT.md` | 1.939 | timing, durasi, overlap, kelegaan |
| `06-TAHAP5-KOMPRESI-BBM.md` | 2.433 | kompresi, bahan bakar, detonasi |
| `07-TAHAP6-PENGAPIAN-AFR.md` | 2.956 | AFR, spark, injeksi, busi, koil, ECU |
| `08-TAHAP7-SALURAN.md` | 2.115 | TB, runner, stack, knalpot |
| `09-TAHAP8-MEKANIK.md` | 3.359 | material, ring, clearance, per klep |
| `10-TAHAP9-CVT.md` | 1.772 | CVT, rasio, gear |
| `11-TAHAP10-SIMULASI.md` | 1.562 | CFD dan validasi |
| `12-LAMPIRAN.md` | 3.037 | rumus, perkakas, daftar periksa, data |

Berkas lama `docs/BUKU-ADVANCED-ENGINE-TUNING.md` (15.441 kata, versi satu-berkas)
**digantikan** oleh `docs/buku/`. Boleh dihapus.

**Konvensi:** tiap angka diberi tanda [UKUR] / [HITUNG] / [ASUMSI] / [SIM].
Lampiran F memuat daftar lengkap mana yang mana.

---

## 8. Yang belum selesai

### Prioritas tinggi

**Ukur panjang header Mesin Contoh A** — dari klep buang sampai titik pelebaran ke 50 mm.
Ini satu-satunya variabel besar yang belum terkalibrasi. Tabel harmoniknya sudah siap
di `exhaust_system.py`; begitu diukur, panjang header mesin baru langsung terkunci.

Kandidatnya: kalau hasil ukur ~650 mm → harmonik 2 → header baru **526 mm**.
Kalau ~440 mm → harmonik 3 → header baru **351 mm**.

### Prioritas sedang

- **Sweep 36 case CFD** — pipeline siap, 36 STL sudah dibuat, estimasi ~1,5–2 jam.
  Matriks: CSA 560/615/665 × aspect 1,00/1,15/1,30/1,45 × short-turn 0,30/0,40/0,55.
  Menjawab: bundar vs oval, dan CSA mana yang menang (615 velocity-anchored vs 665 ratio-anchored).
- **Diameter klep buang Mesin C** — angka 21/26 mm masih [ASUMSI], bukan data pabrik.
- **Massa piston rencana Mesin B** — menentukan apakah 12.500+ rpm masuk akal.

### Prioritas rendah

- Diagram dan grafik untuk buku (sengaja ditunda)
- Konversi buku ke PDF berformat cetak
- Model CFD dengan klep dan seat (untuk angka CFM absolut, bukan cuma perbandingan)

---

## 9. Cara melanjutkan

### Menjalankan perkakas hitung

```
cd "C:\Users\Clinic plus\Desktop\CLAUDE PROJECT\tools"
python spek_final.py          # rangkuman spek Mesin Contoh B
python bahan_bakar.py         # perbandingan bahan bakar
python valvetrain.py          # kebutuhan per klep
```

Semua berkas menjalankan `_selfcheck()` lebih dulu. **Kalau selfcheck gagal, jangan pakai hasilnya.**

### Menjalankan satu case CFD

```
cd "C:\Users\Clinic plus\Desktop\CLAUDE PROJECT\tools"
python -c "import port_geom as pg, cfd_case; pg.generate('../cfd/stl/x.stl', 615.0, 1.30, 0.40, 20.2); cfd_case.build('../cfd/stl/x.stl', '../cfd/run/x', n_proc=10)"
```

```bash
wsl -d Ubuntu -u root -- bash -c "cd '/mnt/c/Users/Clinic plus/Desktop/CLAUDE PROJECT/cfd' && bash run_case.sh '/mnt/c/Users/Clinic plus/Desktop/CLAUDE PROJECT/cfd/run/x' 10"
```

### Melepas sweep 36 case

```
cd tools; python port_geom.py        # regenerate 36 STL
python build_sweep.py 6              # bangun 36 case
```

```bash
wsl -d Ubuntu -u root -- bash -c "cd '/mnt/c/.../cfd' && bash run_sweep.sh '/mnt/c/.../cfd/run' 3 6"
```

### Mengubah mesin sasaran

Ubah blok konstanta di atas berkas — `port_design.py`, `cam_design.py`, `head_3klep.py`
semuanya punya blok `# ---- MESIN ----` di bagian atas.

---

## 10. Catatan penting

**Jangan percayai angka tanpa tanda.** Kalau tidak ada [UKUR], anggap [ASUMSI].

**Jangan lepas sweep CFD tanpa menjalankan kasus kontrol dulu.** Pipa lurus harus
memberi Cf 0,85–0,95. Kalau tidak, setup-nya yang salah.

**Jangan tambahkan functionObject ke case OpenFOAM.** Build v1912 ini crash pada
functionObject apa pun.

**Perhitungan di proyek ini adalah baseline, bukan jaminan.** Selisih 10–25% antara
hitungan dan kenyataan itu normal. Dyno tetap wajib.

---

Terkait: `PROJECT_RESUME.md` (app Android), `GENERATOR-RESUME.md` (generator manifold),
memory `cfd-port-flowbench-pitfalls`, `openfoam-wsl-toolchain`.
