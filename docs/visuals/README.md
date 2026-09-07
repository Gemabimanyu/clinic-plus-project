# Advanced Engine Tuning - Visual Diagrams

Koleksi diagram dan visualisasi interaktif untuk mendukung buku "Advanced Engine Tuning - Panduan Membangun Mesin 1 Silinder Matic".

## File Diagram

### advanced-engine-tuning-visuals.html
Canvas interaktif yang berisi 7 diagram utama:

1. **Overview** - Pengantar koleksi diagram
2. **Torque vs Power** - Hubungan dan perbedaan antara kurva torsi dan tenaga
   - Mesin contoh: 150cc
   - Menunjukkan titik potong kurva (artefak satuan)
   - Berguna untuk Tahap 1 (Mengukur)

3. **Engine Cross-Section** - Penampang melintang mesin 4-langkah
   - Detail: Inlet valve, exhaust valve, piston, crankshaft
   - Combustion chamber dan spark plug
   - Rumus volume: Vd = π/4 × bore² × stroke
   - Berguna untuk Tahap 2-3 (Konfigurasi & Aliran)

4. **Valve Timing Diagram** - Kurva lift katup terhadap crank angle
   - Contoh: IN 38 BTDC / 63 ABDC
   - Menunjukkan overlap zone
   - Durasi: 281° @ 1mm lift
   - Berguna untuk Tahap 4 (Camshaft)

5. **AFR Curve** - Air-Fuel Ratio untuk torsi vs tenaga maksimum
   - Lambda (λ) reference
   - Peak torque pada λ ≈ 0.93 (rich)
   - Peak power pada λ ≈ 1.05 (lean)
   - Berguna untuk Tahap 6 (Pengapian & AFR)

6. **Compression Ratio** - Visualisasi rasio kompresi statis
   - Perbandingan CR 10:1 vs CR 14:1
   - Pengaruh terhadap efisiensi, tenaga, dan risiko detonasi
   - Berguna untuk Tahap 5 (Kompresi & BBM)

7. **CVT Ratio Curve** - Kurva rasio transmisi terhadap RPM mesin
   - Ratio dari 5.2:1 (idle) ke 2.0:1 (top speed)
   - Power band zone
   - Strategi CVT untuk performa optimal
   - Berguna untuk Tahap 9 (Penyaluran Tenaga: CVT)

## Cara Menggunakan

### Membuka Diagram
1. Buka file `advanced-engine-tuning-visuals.html` di browser
2. Gunakan pan/zoom untuk navigasi canvas
3. Klik artboard untuk focus pada diagram tertentu

### Mengekspor Diagram
Setiap artboard dapat di-ekspor sebagai:
- **PNG** - Untuk presentasi dan dokumentasi
- **PDF** - Untuk cetak atau sharing

### Menyesuaikan Diagram
Jika visual saving enabled, Anda dapat:
- Edit nilai langsung dalam diagram (klik elemen)
- Ubah warna dan styling
- Tambah anotasi
- Save perubahan (akan tersimpan untuk semua viewer)

## Integrasi dengan Buku

Diagram-diagram ini dirancang untuk:
- **Tahap 1 (Mengukur)**: Torque vs Power diagram
- **Tahap 2-3 (Konfigurasi & Head)**: Engine cross-section
- **Tahap 4 (Camshaft)**: Valve timing diagram
- **Tahap 5 (Kompresi & BBM)**: Compression ratio visualization
- **Tahap 6 (Pengapian & AFR)**: AFR curve
- **Tahap 9 (CVT)**: CVT ratio curve

## Spesifikasi Teknis

**Format**: Design Component Canvas (DC)
**Artboards**: 7 (Main, TorquePower, EngineSection, ValveTiming, AFRCurve, CompressionRatio, CVTRatio)
**Layout**: Multi-artboard pan/zoom canvas
**Capability**: Self (artifact) + Downloads

## Rencana Pengembangan

Diagram tambahan yang dapat ditambahkan di masa depan:
- [ ] Port flow characteristics (Tahap 3)
- [ ] Intake/exhaust manifold tuning (Tahap 7)
- [ ] Piston speed limits (Tahap 8)
- [ ] Mechanical stress visualization (Tahap 8)
- [ ] Simulation CFD results (Tahap 10)

## Catatan

Semua diagram dalam canvas ini dapat disesuaikan dengan parameter spesifik mesin Anda:
- Bore dan stroke
- Displacement (cc)
- RPM target
- Compression ratio
- AFR/lambda values

Untuk menyesuaikan, edit nilai dalam diagram melalui properties panel (jika saving enabled) atau hubungi developer untuk custom modifications.
