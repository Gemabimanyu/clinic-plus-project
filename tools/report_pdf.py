"""Susun laporan PDF: spesifikasi, geometri port, medan CFD, dan analitik."""
import math

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import cfd_case
import port_design as pd
import report_geom_fig as rg
import report_case
import slice_fig as sf

CSA = 615.0
ASPECT = 1.30
STR = 0.40
THROAT = 20.2
CASE_PORT = "port615"
CASE_PIPA = "pipa2"
TSTEP = "3000"

A4 = (11.69, 8.27)      # lanskap


def _halaman_teks(pdf, judul, blok):
    fig = plt.figure(figsize=A4)
    fig.text(0.06, 0.93, judul, fontsize=17, weight="bold")
    y = 0.855
    for sub, baris in blok:
        if sub:
            fig.text(0.06, y, sub, fontsize=11.5, weight="bold", color="#1a4d80")
            y -= 0.038
        for kiri, kanan in baris:
            fig.text(0.08, y, kiri, fontsize=9.5, family="monospace")
            fig.text(0.52, y, kanan, fontsize=9.5, family="monospace")
            y -= 0.030
        y -= 0.022
    pdf.savefig(fig); plt.close(fig)


def build(path="../cfd/laporan_port.pdf"):
    g = pd.geometry()
    r = pd.ref_metrics()
    s12 = pd.scaled_recommendation(12000)
    port = report_case.summarize(f"//wsl.localhost/Ubuntu/root/cfd/{CASE_PORT}", THROAT)
    pipa = report_case.summarize(f"//wsl.localhost/Ubuntu/root/cfd/{CASE_PIPA}", THROAT)
    k = lambda cf: (1.0 / cf ** 2) - 1.0

    with PdfPages(path) as pdf:
        # ---------------------------------------------------- 1. ringkasan
        _halaman_teks(pdf, "Desain Port 4-Klep untuk Drag 500m - Ringkasan", [
            ("Mesin sasaran", [
                ("bore x stroke", f"{pd.BORE_MM} x {pd.STROKE_MM} mm  ({g['displacement_cc']:.1f} cc)"),
                ("klep in", f"2 x {pd.VALVE_DIA_MM} mm, throat {THROAT} mm"),
                ("luas throat gabungan", f"{2*math.pi/4*THROAT**2:.0f} mm2"),
                ("luas klep / luas bore", f"{g['valve_per_bore_area']:.3f}   (4-klep bagus 0.30-0.35)"),
                ("penggerak", "matic CVT"),
            ]),
            ("Mesin acuan (terbukti 500m 15.4 s @ 158 km/h)", [
                ("bore x stroke", f"{pd.REF['bore']} x {pd.REF['stroke']} mm  ({r['displacement_cc']:.1f} cc)"),
                ("klep in / throat", f"{pd.REF['valve_dia']} / 29.0 mm   (rasio {pd.REF['throat_ratio']:.3f})"),
                ("port", "bulat 29.5 mm  (port/throat 1.035)"),
                ("lift / durasi / TB", f"{pd.REF['lift']} mm / {pd.REF['duration']} deg / {pd.REF['tb_dia']} mm"),
                ("kecepatan gas di port", f"{r['v_port']:.0f} m/s  <- angka kalibrasi utama"),
            ]),
            ("Rekomendasi (diskalakan dari mesin acuan, bukan textbook)", [
                ("CSA port", f"{CSA:.0f} mm2   (rentang 560-665)"),
                ("penampang", f"22.7 W x 29.5 H mm, aspect {ASPECT} - oval tinggi"),
                ("throat", f"{THROAT} mm  (dari 19.5 -> +7.4% luas)"),
                ("throttle body", "36 mm"),
                ("lift", "9.0 mm  (praktik lokal 4-klep)"),
                ("panjang runner", "155 mm  (harmonik 4 @ 12.000 rpm)"),
                ("short-turn radius min", "11.8 mm (port penuh) / 8.3 mm (per cabang)"),
            ]),
        ])

        # ---------------------------------------------------- 2. geometri
        fig, _ = rg.figure(CSA, ASPECT, STR, THROAT,
                           judul=f"Geometri port - CSA {CSA:.0f} mm2, aspect {ASPECT}, "
                                 f"short-turn {STR}, throat {THROAT} mm")
        fig.set_size_inches(*A4); pdf.savefig(fig); plt.close(fig)

        # ---------------------------------------------------- 3. medan CFD
        fig, _ = sf.figure(CASE_PORT, TSTEP, zoom=(-15, 60, -5, 80),
                           judul="Medan CFD di bidang simetri - port CSA 615, aspect 1.30")
        fig.set_size_inches(*A4); pdf.savefig(fig); plt.close(fig)

        # ---------------------------------------------------- 4. hasil CFD
        _halaman_teks(pdf, "Hasil CFD dan Rantai Validasi", [
            ("Setelan simulasi", [
                ("solver", "OpenFOAM 1912 simpleFoam, k-omega SST"),
                ("model", "satu cabang port (simetri di sekat), TANPA klep"),
                ("depresi simulasi", f'{cfd_case.RUN_INH2O:.0f}" H2O  (Mach 0.19)'),
                ("dilaporkan pada", f'{cfd_case.BENCH_INH2O:.0f}" H2O (konversi akar rasio tekanan)'),
                ("plenum", "setengah bola R80 mm, mulut di bidang flange datar"),
            ]),
            ("Kasus acuan berjawaban pasti - pipa lurus 20.2 mm", [
                ("Cf terukur", f"{pipa['Cf']:.4f}   (harapan 0.85-0.95)  LULUS"),
                ("K", f"{k(pipa['Cf']):.3f}"),
                ("kecepatan inti", "63 m/s  (teoretis 64.3)"),
                ("aliran balik", "0.2% titik"),
            ]),
            ("Port sungguhan - CSA 615, aspect 1.30, short-turn 0.40", [
                ("Cf", f"{port['Cf']:.4f}"),
                ("K", f"{k(port['Cf']):.3f}"),
                ("kecepatan throat", f"{port['v_throat_ms']:.1f} m/s"),
                ("CFM per cabang @ 28\"", f"{port['cfm_28']:.1f}"),
                ("CFM total (2 cabang)", f"{port['cfm_28']*2:.1f}"),
                ("ongkos tikungan 37 deg", f"{(1-port['Cf']/pipa['Cf'])*100:.1f}% vs pipa lurus"),
            ]),
            ("Pemeriksaan kelayakan", [
                ("ketimpangan massa", f"{port['imbalance_pct']:.3f} %   (batas 1.0)"),
                ("luas patch outlet", "316.9 mm2 vs 320.5 geometri"),
                ("luas patch inlet", "40982 mm2 vs 40212 setengah bola"),
                ("nut / nu", "maks 282, rata2 63   (wajar 50-500)"),
                ("checkMesh", "Mesh OK, non-ortho maks 64.7, skewness 2.7"),
            ]),
        ])

        # ---------------------------------------------------- 5. catatan
        _halaman_teks(pdf, "Batasan dan Cara Membaca Angka Ini", [
            ("Yang TIDAK dimodelkan", [
                ("klep dan seat", "Cf 0.849 adalah plafon port telanjang."),
                ("", "Head lengkap dgn klep di lift 9mm akan jauh lebih rendah"),
                ("", "(tipikal 0.55-0.65). Port BUKAN pembatasnya."),
                ("sekat pemisah cabang", "rugi ujung sekat sama utk semua varian,"),
                ("", "tidak menggeser peringkat"),
                ("kompresibilitas", "solver incompressible; disimulasikan di 10\" H2O"),
                ("", "(Mach 0.19) lalu dikonversi, jadi kesalahannya kecil"),
            ]),
            ("Keandalan", [
                ("kuat", "PERBANDINGAN antar bentuk port"),
                ("lemah", "angka CFM absolut tanpa kalibrasi flowbench"),
                ("cara pakai", "kalibrasi sekali ke satu hasil flowbench nyata,"),
                ("", "setelah itu prediksi relatifnya jauh lebih dipercaya"),
            ]),
            ("Temuan terpenting dari sisi desain", [
                ("1", "Throat 19.5 -> 20.2 mm menaikkan plafon flow +7.4%."),
                ("", "Ini satu-satunya perubahan yang menaikkan plafon;"),
                ("", "bentuk port tidak bisa melakukan itu."),
                ("2", "Dgn lift 9 mm, tirai klep 2x luas throat -> throat"),
                ("", "adalah pembatas 100%."),
                ("3", "CSA 665 mm2 mereproduksi rasio port/throat 1.035"),
                ("", "mesin terbuktimu; 615 mm2 mereproduksi kecepatan gas."),
                ("", "Sweep 36 case dirancang menjawab mana yang menang."),
            ]),
        ])

    return path


if __name__ == "__main__":
    p = build()
    print(f"  laporan -> {p}")
