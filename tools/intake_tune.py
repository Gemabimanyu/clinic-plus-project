"""Kalkulator sizing intake 1D: runner, plenum, throttle body, velocity stack.

Model: Helmholtz (Engelman) + wave-reflection (quarter-wave), plus aturan
kecepatan gas rata-rata untuk diameter port. Semua SI internal, output mm.

Jalankan:  python intake_tune.py
Ubah angka di blok ENGINE / KALIBRASI di bawah.
"""
import math

# ---------------------------------------------------------------- ENGINE
BORE_MM        = 58.0    # Vario 150 std = 58.0
STROKE_MM      = 57.9    # Vario 150 std = 57.9
N_CYL          = 1
STROKES        = 4       # 4 atau 2
COMP_RATIO     = 10.6
RPM_TARGET     = 8500    # RPM yang mau dikuatkan torsinya
INTAKE_DUR_DEG = 240     # durasi bukaan klep in (deg crank). Std ~230-250, racing 260-290
VE             = 0.90    # volumetric efficiency di RPM target (0.85 std, 0.95+ porting)

# ------------------------------------------------------------ KALIBRASI
# Knob untuk mencocokkan model ke hasil dyno/flowbench nyata. Jangan diabaikan:
# model 1D selalu perlu ditarik ke realita mesin spesifik.
AIR_TEMP_C   = 45.0   # suhu udara DI DALAM runner (bukan ambient! panas mesin naikkan ~20-30C)
# Rasio Helmholtz/engine freq. Engelman klasik 2.0-2.5 (mobil, runner panjang).
# Skuter/motor kecil dengan manifold pendek nyatanya duduk di K ~ 3.5-4.5.
# K besar -> runner pendek. Ini knob yang WAJIB dikalibrasi ke mesin nyata.
HELM_RATIO_K = 4.0
WAVE_HARM    = 3      # harmonik pantulan gelombang (2=panjang/torsi bawah, 3-4=RPM tinggi)
MGV_TARGET   = 100.0  # mean gas velocity target di port [m/s]. 90=torsi bawah, 110-120=race
TB_VEL_TARGET= 105.0  # kecepatan puncak di throttle body [m/s]. >130 = ngempet
END_CORR     = 0.85   # koreksi ujung bellmouth (flanged 0.85*r, pipa polos 0.61*r)


def sound_speed(temp_c):
    return 20.05 * math.sqrt(temp_c + 273.15)


def run(bore_mm=BORE_MM, stroke_mm=STROKE_MM, n_cyl=N_CYL, strokes=STROKES,
        cr=COMP_RATIO, rpm=RPM_TARGET, dur_deg=INTAKE_DUR_DEG, ve=VE,
        temp_c=AIR_TEMP_C, k=HELM_RATIO_K, harm=WAVE_HARM,
        mgv=MGV_TARGET, tb_vel=TB_VEL_TARGET, end_corr=END_CORR):
    b, s = bore_mm / 1000.0, stroke_mm / 1000.0
    c = sound_speed(temp_c)
    a_piston = math.pi / 4 * b * b
    v_cyl = a_piston * s                      # m3 per silinder
    v_total = v_cyl * n_cyl

    # --- diameter port/runner dari mean gas velocity ---
    # MGV = (A_piston / A_port) * mean piston speed
    mps = 2 * s * rpm / 60.0
    a_port = a_piston * mps / mgv
    d_port = math.sqrt(4 * a_port / math.pi)

    # --- panjang runner: Helmholtz (Engelman) ---
    # V efektif = volume silinder rata-rata selama intake
    v_eff = v_cyl * (cr + 1) / (2 * (cr - 1))
    f_engine = rpm / (30.0 * strokes)         # 4T: rpm/120, 2T: rpm/60
    omega = 2 * math.pi * k * f_engine
    l_eff_helm = a_port * c * c / (omega * omega * v_eff)
    l_helm = l_eff_helm - end_corr * (d_port / 2)

    # --- panjang runner: pantulan gelombang (quarter-wave) ---
    # waktu bukaan t = dur/(6*rpm) s ; 2L/c = t/harm
    l_wave = c * dur_deg / (12.0 * harm * rpm)
    l_wave -= end_corr * (d_port / 2)

    # --- aliran & throttle body ---
    q_mean = v_total * (rpm / 60.0) / (strokes / 2.0) * ve   # m3/s
    duty = min(1.0, n_cyl * dur_deg / (180.0 * strokes))
    q_peak = q_mean / duty * (math.pi / 2)                   # puncak sesaat, sinusoidal
    d_tb = math.sqrt(4 * q_peak / (math.pi * tb_vel))

    # --- plenum & velocity stack ---
    plenum_lo, plenum_hi = v_total * 1.0, v_total * 1.5
    stack_r = 0.18 * d_port          # radius bellmouth minimum untuk Cd ~0.98
    stack_len = 0.5 * d_port         # panjang lurus setelah radius, bagian dari l_runner

    mm = lambda x: x * 1000.0
    return {
        "kecepatan_suara_m_s": round(c, 1),
        "displacement_cc": round(v_total * 1e6, 1),
        "mean_piston_speed_m_s": round(mps, 1),
        "airflow_rata2_L_s": round(q_mean * 1000, 1),
        "airflow_puncak_L_s": round(q_peak * 1000, 1),
        "diameter_port_mm": round(mm(d_port), 1),
        "runner_helmholtz_mm": round(mm(l_helm), 1),
        f"runner_wave_h{harm}_mm": round(mm(l_wave), 1),
        "throttle_body_mm": round(mm(d_tb), 1),
        "plenum_cc": (round(plenum_lo * 1e6), round(plenum_hi * 1e6)),
        "bellmouth_radius_min_mm": round(mm(stack_r), 1),
        "stack_lurus_mm": round(mm(stack_len), 1),
    }


def sweep_harmonics(**kw):
    """Panjang runner untuk tiap harmonik -> pilih yang muat di ruang mesin."""
    out = {}
    for h in (2, 3, 4, 5):
        out[h] = run(harm=h, **kw)[f"runner_wave_h{h}_mm"]
    return out


def sweep_helmholtz(ks=(2.0, 2.5, 3.0, 3.5, 4.0, 4.5), **kw):
    """Panjang runner untuk tiap rasio K. Kalibrasi: cari K yang mereproduksi
    panjang manifold standar yang sudah terbukti jalan, lalu pakai K itu."""
    return {k: run(k=k, **kw)["runner_helmholtz_mm"] for k in ks}


def sweep_rpm(rpms=(6000, 7000, 8000, 9000, 10000), **kw):
    return {r: run(rpm=r, **kw)["runner_helmholtz_mm"] for r in rpms}


def calibrate_k(known_runner_mm, **kw):
    """Balik: dari panjang runner standar yang terbukti -> nilai K mesin ini."""
    ref = run(k=1.0, **kw)
    l_eff_ref = (ref["runner_helmholtz_mm"] + END_CORR * ref["diameter_port_mm"] / 2) / 1000.0
    l_eff = (known_runner_mm + END_CORR * ref["diameter_port_mm"] / 2) / 1000.0
    return math.sqrt(l_eff_ref / l_eff)


def _selfcheck():
    r = run()
    # sanity: runner lebih panjang di RPM rendah, lebih pendek di RPM tinggi
    lo, hi = run(rpm=6000)["runner_helmholtz_mm"], run(rpm=10000)["runner_helmholtz_mm"]
    assert lo > hi, (lo, hi)
    # kedua metode beda model, tapi harus se-orde. Keluar band = salah unit/rumus.
    ratio = r["runner_helmholtz_mm"] / r[f"runner_wave_h{WAVE_HARM}_mm"]
    assert 0.3 < ratio < 3.0, ratio
    # calibrate_k harus balik konsisten dengan run()
    k_back = calibrate_k(run(k=3.0)["runner_helmholtz_mm"])
    assert abs(k_back - 3.0) < 0.02, k_back
    # displacement Vario 150 ~153cc
    assert 145 < r["displacement_cc"] < 160, r["displacement_cc"]
    # port tidak boleh lebih besar dari bore
    assert r["diameter_port_mm"] < BORE_MM, r["diameter_port_mm"]
    # kecepatan suara pada 20C harus ~343 m/s
    assert abs(sound_speed(20) - 343.0) < 2.0, sound_speed(20)
    print("selfcheck OK")


if __name__ == "__main__":
    _selfcheck()
    print(f"\n=== SIZING @ {RPM_TARGET} rpm ===")
    for key, val in run().items():
        print(f"  {key:28s} {val}")
    print(f"\n=== Panjang runner per harmonik (mm) ===")
    for h, l in sweep_harmonics().items():
        print(f"  harmonik {h}: {l}")
    print(f"\n=== Panjang runner Helmholtz per rasio K (mm) ===")
    for k, l in sweep_helmholtz().items():
        print(f"  K={k}: {l}")
    print(f"\n=== Panjang runner Helmholtz vs RPM (mm), K={HELM_RATIO_K} ===")
    for r, l in sweep_rpm().items():
        print(f"  {r} rpm: {l}")
    print("\nKALIBRASI: ukur panjang runner standar yang sudah terbukti, lalu")
    print("  calibrate_k(150.0)  ->  nilai K asli mesin ini. Pakai K itu seterusnya.")
