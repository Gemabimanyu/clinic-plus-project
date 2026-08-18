"""Sizing port 4-klep: luas penampang, gas speed, CFM potensial, throttle body.

Filosofi: klep sudah fixed, jadi yang dicari adalah luas penampang port yang
memaksimalkan flow TANPA membunuh kecepatan gas. Dua hal itu berlawanan --
port besar = flow naik, velocity turun, torsi bawah hilang. Tool ini
menunjukkan trade-off-nya dalam angka, bukan feeling.

Jalankan:  python port_design.py
"""
import math

# ---------------------------------------------------------------- ENGINE
BORE_MM       = 57.3
STROKE_MM     = 58.0
N_CYL         = 1
N_INT_VALVE   = 2       # 4-klep = 2 klep in
VALVE_DIA_MM  = 22.0    # diameter payung klep in
THROAT_DIA_MM = 19.5    # diameter dalam seat (throat)
INTAKE_DUR    = 250     # durasi klep in (deg crank)
VE            = 0.95    # 4-klep porting bagus

# ------------------------------------------------------------ KALIBRASI
AIR_TEMP_C    = 45.0    # suhu di dalam port (panas mesin, bukan ambient)
FLOW_COEF     = 0.62    # Cf head 4-klep di lift maks. 0.55 jelek, 0.62 bagus, 0.70 sangat bagus
TB_VEL_TARGET = 105.0   # kecepatan puncak throttle body [m/s]
TB_SHAFT_BLOCK= 0.07    # fraksi luas TB tertutup poros butterfly
HP_PER_CFM    = 0.45    # rule 4-klep NA @28"H2O. Kalibrasi ke dyno kalau ada
BENCH_INH2O   = 28.0    # depresi flowbench acuan


def sound_speed(t_c):
    return 20.05 * math.sqrt(t_c + 273.15)


def geometry():
    a_piston = math.pi / 4 * BORE_MM ** 2
    a_valve = N_INT_VALVE * math.pi / 4 * VALVE_DIA_MM ** 2
    a_throat = N_INT_VALVE * math.pi / 4 * THROAT_DIA_MM ** 2
    vd = a_piston * STROKE_MM * N_CYL / 1000.0            # cc
    # lift saat luas tirai (curtain) = luas throat -> di atas ini throat jadi
    # pembatas, nambah lift tidak nambah flow banyak
    lift_crit = a_throat / (N_INT_VALVE * math.pi * VALVE_DIA_MM)
    return {
        "displacement_cc": vd,
        "a_piston_mm2": a_piston,
        "a_valve_mm2": a_valve,
        "a_throat_mm2": a_throat,
        "throat_per_valve_ratio": THROAT_DIA_MM / VALVE_DIA_MM,
        "valve_per_bore_area": a_valve / a_piston,
        "lift_kritis_mm": lift_crit,
        "lift_maks_berguna_mm": 0.27 * VALVE_DIA_MM,
    }


def mean_gas_velocity(csa_mm2, rpm):
    """Kecepatan gas rata-rata lewat penampang csa selama langkah isap.
    MGV = (luas piston / luas port) * mean piston speed."""
    mps = 2 * (STROKE_MM / 1000.0) * rpm / 60.0
    return (math.pi / 4 * BORE_MM ** 2) / csa_mm2 * mps


def rpm_for_velocity(csa_mm2, target_v):
    """RPM di mana port dengan luas csa mencapai kecepatan target."""
    ratio = (math.pi / 4 * BORE_MM ** 2) / csa_mm2
    return target_v / ratio / (2 * (STROKE_MM / 1000.0)) * 60.0


def flow_potential(cf=FLOW_COEF, inh2o=BENCH_INH2O):
    """CFM potensial head ini di depresi flowbench. Teoretis lewat throat,
    dikali koefisien flow."""
    dp = inh2o * 249.089                       # inH2O -> Pa
    rho = 1.204
    v_theo = math.sqrt(2 * dp / rho)
    a = geometry()["a_throat_mm2"] * 1e-6      # m2
    q_theo = a * v_theo                        # m3/s
    cfm_theo = q_theo * 2118.88
    return {
        "cfm_teoretis": cfm_theo,
        "cfm_realistis": cfm_theo * cf,
        "hp_potensial": cfm_theo * cf * HP_PER_CFM,
    }


def throttle_body(rpm, ve=VE, v_target=TB_VEL_TARGET, shaft=TB_SHAFT_BLOCK):
    vd = geometry()["displacement_cc"] * 1e-6           # m3
    q_mean = vd * (rpm / 60.0) / 2.0 * ve               # m3/s (4-tak)
    duty = min(1.0, N_CYL * INTAKE_DUR / 720.0)
    q_peak = q_mean / duty * (math.pi / 2)              # puncak sesaat
    a_need = q_peak / v_target                          # m2 efektif
    a_bore = a_need / (1 - shaft)                       # tambah rugi poros
    d = math.sqrt(4 * a_bore / math.pi) * 1000.0
    return {"q_mean_L_s": q_mean * 1000, "q_peak_L_s": q_peak * 1000,
            "tb_dia_mm": d}


def runner_length(rpm, harm, temp_c=AIR_TEMP_C, dur=INTAKE_DUR):
    """Panjang runner dari pantulan gelombang, mm."""
    return sound_speed(temp_c) * dur / (12.0 * harm * rpm) * 1000.0


# --------------------------------------------------------------- KANDIDAT
# Rasio luas port minimum (pinch) terhadap luas throat total.
# Ini SATU-SATUNYA angka desain terpenting di port. Kecil = velocity tinggi
# torsi bawah kuat; besar = flow puncak tinggi tapi bawah loyo.
CANDIDATES = [
    ("A  jalanan / torsi",  0.70),
    ("B  serbaguna",        0.78),
    ("C  balap putaran atas", 0.86),
    ("D  flow maksimum",    0.94),
]


def candidate_table():
    g = geometry()
    rows = []
    for name, ratio in CANDIDATES:
        csa = g["a_throat_mm2"] * ratio
        # port 4-klep: satu runner bersama lalu pecah dua sebelum klep.
        # tiap cabang dikasih 5% lebih supaya rugi percabangan tidak menumpuk
        branch = csa / 2 * 1.05
        rows.append({
            "nama": name,
            "rasio_thd_throat": ratio,
            "csa_runner_mm2": csa,
            "dia_setara_mm": math.sqrt(4 * csa / math.pi),
            "csa_tiap_cabang_mm2": branch,
            "dia_cabang_setara_mm": math.sqrt(4 * branch / math.pi),
            "rpm_at_100ms": rpm_for_velocity(csa, 100.0),
            "v_at_7000": mean_gas_velocity(csa, 7000),
            "v_at_9000": mean_gas_velocity(csa, 9000),
            "v_at_11000": mean_gas_velocity(csa, 11000),
        })
    return rows


def port_for_rpm(rpm, target_v=100.0):
    """Balik dari tabel kandidat: dari RPM tenaga puncak -> luas port yang pas.
    Ini cara berpikir yang benar untuk drag, di mana RPM kerja sudah ditentukan
    oleh kem + gearing/CVT, bukan dipilih dari rasa."""
    csa = rpm_for_velocity(1.0, target_v)  # dummy utk pakai relasi yg sama
    ratio = (math.pi / 4 * BORE_MM ** 2)
    mps = 2 * (STROKE_MM / 1000.0) * rpm / 60.0
    csa = ratio * mps / target_v
    g = geometry()
    return {
        "csa_mm2": csa,
        "rasio_thd_throat": csa / g["a_throat_mm2"],
        "dia_setara_mm": math.sqrt(4 * csa / math.pi),
        "csa_tiap_cabang_mm2": csa / 2 * 1.05,
        "mean_piston_speed": mps,
    }


def piston_speed_verdict(mps):
    if mps < 20:
        return "aman, bisa dipakai harian"
    if mps < 22:
        return "tinggi, umur mesin pendek tapi wajar utk drag"
    if mps < 24:
        return "sangat tinggi, butuh klep/per/rod yang serius"
    return "ekstrem, hanya utk mesin sekali pakai"


# ---------------------------------------------- MESIN ACUAN (TERBUKTI)
# Mesin drag Gema yang sudah jalan: 500m @ 15.4s, trap 158 km/h.
# Semua rekomendasi diskalakan dari sini, BUKAN dari angka textbook.
# Ini jauh lebih dipercaya daripada target kecepatan generik.
REF = {
    "nama": "2-klep 199cc drag (terbukti)",
    "bore": 63.0, "stroke": 64.0, "n_valve": 1,
    "valve_dia": 31.0,
    "throat_ratio": 29.0 / 31.0,   # DIUKUR: seat dalam 29mm. Agresif (0.935), bukan 0.86 textbook
    "port_csa": math.pi / 4 * 29.5 ** 2,  # DIUKUR: port bulat 29.5mm
    "lift": 10.8,
    "duration": 278,
    "tb_dia": 38.0,
    "rpm_peak": 10000,
    "ve": 0.95,
}


def ref_metrics(ref=REF):
    a_piston = math.pi / 4 * ref["bore"] ** 2
    throat_d = ref["valve_dia"] * ref["throat_ratio"]
    a_throat = ref["n_valve"] * math.pi / 4 * throat_d ** 2
    vd = a_piston * ref["stroke"] / 1000.0
    mps = 2 * (ref["stroke"] / 1000.0) * ref["rpm_peak"] / 60.0
    q_mean = vd * 1e-6 * (ref["rpm_peak"] / 60.0) / 2.0 * ref["ve"]
    duty = ref["duration"] / 720.0
    q_peak = q_mean / duty * (math.pi / 2)
    a_tb = math.pi / 4 * (ref["tb_dia"] / 1000.0) ** 2 * (1 - TB_SHAFT_BLOCK)
    return {
        "displacement_cc": vd,
        "a_throat_mm2": a_throat,
        "mean_piston_speed": mps,
        "v_throat": a_piston / a_throat * mps,
        "port_csa": ref["port_csa"],
        "v_port": a_piston / ref["port_csa"] * mps,
        "port_per_throat": ref["port_csa"] / a_throat,
        "tb_per_port": (math.pi / 4 * ref["tb_dia"] ** 2 * (1 - TB_SHAFT_BLOCK)) / ref["port_csa"],
        "q_peak_m3s": q_peak,
        "v_throttle_body": q_peak / a_tb,
        "lift_per_valve_dia": ref["lift"] / ref["valve_dia"],
        "lift_curtain_limit": a_throat / (ref["n_valve"] * math.pi * ref["valve_dia"]),
        "throat_per_bore_area": a_throat / a_piston,
    }


def scaled_recommendation(rpm):
    """Skalakan spek mesin baru dari mesin acuan yang terbukti, pada rpm target.
    Yang diskalakan: kecepatan throat, kecepatan TB, dan rasio lift/diameter klep."""
    r = ref_metrics()
    g = geometry()
    a_piston = g["a_piston_mm2"]
    mps = 2 * (STROKE_MM / 1000.0) * rpm / 60.0

    # --- throttle body: samakan kecepatan puncak TB dengan mesin acuan ---
    t = throttle_body(rpm)
    a_tb_need = (t["q_peak_L_s"] / 1000.0) / r["v_throttle_body"]     # m2 efektif
    d_tb = math.sqrt(4 * (a_tb_need / (1 - TB_SHAFT_BLOCK)) / math.pi) * 1000

    # --- port CSA: samakan kecepatan gas di port dengan mesin acuan (DIUKUR) ---
    v_ref_port = r["v_port"]
    csa = a_piston * mps / v_ref_port

    # --- throat yang SEHARUSNYA, kalau pakai rasio throat/klep seagresif acuan ---
    throat_d_bisa = VALVE_DIA_MM * REF["throat_ratio"]
    a_throat_bisa = N_INT_VALVE * math.pi / 4 * throat_d_bisa ** 2
    seat_width = (VALVE_DIA_MM - throat_d_bisa) / 2

    return {
        "rpm": rpm,
        "mean_piston_speed": mps,
        "tb_dia_mm": d_tb,
        "tb_dia_by_port_ratio": math.sqrt(
            4 * (r["tb_per_port"] * csa / (1 - TB_SHAFT_BLOCK)) / math.pi),
        "csa_port_mm2": csa,
        "rasio_csa_thd_throat": csa / g["a_throat_mm2"],
        "lift_mm": r["lift_per_valve_dia"] * VALVE_DIA_MM,
        "overlap_lift_mm": 3.6 * VALVE_DIA_MM / REF["valve_dia"],
        "v_port": v_ref_port,
        "throat_dia_bisa_mm": throat_d_bisa,
        "a_throat_bisa_mm2": a_throat_bisa,
        "gain_throat_pct": (a_throat_bisa / g["a_throat_mm2"] - 1) * 100,
        "seat_width_mm": seat_width,
    }


def port_shape_spec(csa_mm2, aspect=1.30):
    """Bentuk penampang port di pinch. 4-klep: port TINGGI-SEMPIT lebih baik
    daripada bundar -- short turn jadi lebih landai, aliran tidak lepas di lantai.
    aspect = tinggi/lebar."""
    # superelips ~ luas = 0.92 * w * h (antara elips 0.785 dan kotak 1.0)
    w = math.sqrt(csa_mm2 / (0.92 * aspect))
    h = w * aspect
    return {"lebar_mm": w, "tinggi_mm": h,
            "short_turn_radius_min_mm": 0.40 * h,
            "bowl_csa_mm2": geometry()["a_throat_mm2"] * 1.12}


def _selfcheck():
    g = geometry()
    assert 145 < g["displacement_cc"] < 155, g["displacement_cc"]
    assert 0.80 < g["throat_per_valve_ratio"] < 0.95, g["throat_per_valve_ratio"]
    # port lebih kecil -> gas lebih cepat
    assert mean_gas_velocity(400, 9000) > mean_gas_velocity(600, 9000)
    # rpm_for_velocity harus invers dari mean_gas_velocity
    r = rpm_for_velocity(500, 100.0)
    assert abs(mean_gas_velocity(500, r) - 100.0) < 1e-6
    # runner lebih pendek di harmonik lebih tinggi
    assert runner_length(9000, 4) < runner_length(9000, 3)
    # bentuk port harus mereproduksi luasnya
    s = port_shape_spec(500)
    assert abs(0.92 * s["lebar_mm"] * s["tinggi_mm"] - 500) < 1e-6
    # port_for_rpm harus konsisten dgn mean_gas_velocity (bolak-balik)
    p = port_for_rpm(10500, 100.0)
    assert abs(mean_gas_velocity(p["csa_mm2"], 10500) - 100.0) < 1e-6
    print("selfcheck OK\n")


if __name__ == "__main__":
    _selfcheck()
    g = geometry()
    print("=== GEOMETRI DASAR ===")
    print(f"  displacement            {g['displacement_cc']:.1f} cc")
    print(f"  luas piston             {g['a_piston_mm2']:.0f} mm2")
    print(f"  luas klep in (2x)       {g['a_valve_mm2']:.0f} mm2")
    print(f"  luas throat (2x)        {g['a_throat_mm2']:.0f} mm2")
    print(f"  throat/klep             {g['throat_per_valve_ratio']:.3f}  (bagus 0.85-0.90)")
    print(f"  luas klep / luas bore   {g['valve_per_bore_area']:.3f}  (4-klep bagus 0.30-0.35)")
    print(f"  lift kritis             {g['lift_kritis_mm']:.2f} mm  (di atas ini throat jadi pembatas)")
    print(f"  lift maks berguna       {g['lift_maks_berguna_mm']:.2f} mm")

    f = flow_potential()
    print(f"\n=== POTENSI FLOW @ {BENCH_INH2O}\"H2O (Cf={FLOW_COEF}) ===")
    print(f"  teoretis                {f['cfm_teoretis']:.1f} CFM")
    print(f"  realistis               {f['cfm_realistis']:.1f} CFM")
    print(f"  potensi tenaga          ~{f['hp_potensial']:.1f} HP")

    print("\n=== KANDIDAT PORT ===")
    hdr = f"{'kandidat':22s} {'CSA':>7s} {'Dia~':>6s} {'cabang':>7s} {'100m/s':>8s} {'v@7k':>6s} {'v@9k':>6s} {'v@11k':>6s}"
    print(hdr); print("-" * len(hdr))
    for r in candidate_table():
        print(f"{r['nama']:22s} {r['csa_runner_mm2']:7.0f} {r['dia_setara_mm']:6.1f} "
              f"{r['csa_tiap_cabang_mm2']:7.0f} {r['rpm_at_100ms']:8.0f} "
              f"{r['v_at_7000']:6.0f} {r['v_at_9000']:6.0f} {r['v_at_11000']:6.0f}")
    print("  (CSA/cabang mm2, Dia~ = diameter bundar setara mm, v = m/s)")

    print("\n=== BENTUK PENAMPANG (aspect tinggi/lebar = 1.30) ===")
    for r in candidate_table():
        s = port_shape_spec(r["csa_runner_mm2"])
        print(f"  {r['nama']:22s} {s['lebar_mm']:.1f} W x {s['tinggi_mm']:.1f} H mm, "
              f"short-turn R min {s['short_turn_radius_min_mm']:.1f} mm")
    print(f"  luas bowl di bawah klep  {port_shape_spec(500)['bowl_csa_mm2']:.0f} mm2 (jangan lebih besar)")

    print("\n=== THROTTLE BODY ===")
    for rpm in (8000, 9000, 10000, 11000):
        t = throttle_body(rpm)
        print(f"  @{rpm:5d} rpm: puncak {t['q_peak_L_s']:5.1f} L/s -> TB {t['tb_dia_mm']:.1f} mm")

    print("\n=== PANJANG RUNNER (batasan kamu 150-300 mm) ===")
    print(f"  {'rpm':>6s}" + "".join(f"{'h'+str(h):>9s}" for h in (2, 3, 4, 5)))
    for rpm in (7000, 8000, 9000, 10000, 11000):
        cells = ""
        for h in (2, 3, 4, 5):
            L = runner_length(rpm, h)
            mark = "*" if 150 <= L <= 300 else " "
            cells += f"{L:8.0f}{mark}"
        print(f"  {rpm:6d}" + cells)
    print("  * = muat di batasan 150-300 mm")

    print("\n=== MODE DRAG 500M: port dari RPM tenaga puncak ===")
    hdr = (f"{'rpm':>6s} {'CSA':>6s} {'rasio':>6s} {'WxH mm':>13s} {'cabang':>7s} "
           f"{'TB':>5s} {'run h4':>7s} {'MPS':>5s}  keterangan")
    print(hdr); print("-" * len(hdr))
    for rpm in (10000, 10500, 11000, 11500, 12000):
        p = port_for_rpm(rpm)
        s = port_shape_spec(p["csa_mm2"])
        t = throttle_body(rpm)
        print(f"{rpm:6d} {p['csa_mm2']:6.0f} {p['rasio_thd_throat']:6.2f} "
              f"{s['lebar_mm']:5.1f} x{s['tinggi_mm']:5.1f} {p['csa_tiap_cabang_mm2']:7.0f} "
              f"{t['tb_dia_mm']:5.1f} {runner_length(rpm, 4):7.0f} "
              f"{p['mean_piston_speed']:5.1f}  {piston_speed_verdict(p['mean_piston_speed'])}")
    print("  rasio = CSA port / luas throat. Di atas 1.00 port lebih besar dari")
    print("  throat -> percuma, throat sudah jadi pembatas duluan.")

    r = ref_metrics()
    print(f"\n=== MESIN ACUAN: {REF['nama']} ===")
    print(f"  displacement            {r['displacement_cc']:.1f} cc")
    print(f"  luas throat             {r['a_throat_mm2']:.0f} mm2  (asumsi throat/klep {REF['throat_ratio']})")
    print(f"  throat / luas bore      {r['throat_per_bore_area']:.3f}")
    print(f"  mean piston speed       {r['mean_piston_speed']:.1f} m/s @ {REF['rpm_peak']} rpm")
    print(f"  CSA port (diukur)       {r['port_csa']:.0f} mm2  (bulat 29.5mm)")
    print(f"  port / throat           {r['port_per_throat']:.3f}  <- port LEBIH BESAR dari throat")
    print(f"  throat / klep           {REF['throat_ratio']:.3f}  (textbook bilang 0.85-0.90)")
    print(f"  kecepatan gas di throat {r['v_throat']:.0f} m/s")
    print(f"  kecepatan gas di port   {r['v_port']:.0f} m/s   <- ini angka acuan sebenarnya")
    print(f"  kecepatan puncak di TB  {r['v_throttle_body']:.0f} m/s   <- TB 38mm")
    print(f"  lift / diameter klep    {r['lift_per_valve_dia']:.3f}  (lift {REF['lift']}mm)")
    print(f"  batas curtain=throat    {r['lift_curtain_limit']:.2f} mm  "
          f"-> lift nyata {REF['lift']/r['lift_curtain_limit']:.1f}x batas itu")

    g = geometry()
    print(f"\n  PEMBANDING head baru: throat {g['a_throat_mm2']:.0f} mm2, "
          f"throat/bore {g['a_throat_mm2']/g['a_piston_mm2']:.3f}")

    print("\n=== SPEK HEAD BARU, DISKALAKAN DARI MESIN ACUAN ===")
    hdr = f"{'rpm':>6s} {'MPS':>5s} {'TB':>6s} {'CSA':>6s} {'rasio':>6s} {'lift':>6s} {'WxH mm':>13s}"
    print(hdr); print("-" * len(hdr))
    for rpm in (10500, 11000, 11500, 12000, 12400):
        s = scaled_recommendation(rpm)
        sh = port_shape_spec(s["csa_port_mm2"])
        print(f"{rpm:6d} {s['mean_piston_speed']:5.1f} {s['tb_dia_mm']:6.1f} "
              f"{s['csa_port_mm2']:6.0f} {s['rasio_csa_thd_throat']:6.2f} "
              f"{s['lift_mm']:6.1f} {sh['lebar_mm']:5.1f} x{sh['tinggi_mm']:5.1f}")
    s = scaled_recommendation(12000)
    print(f"\n  kecepatan port yang ditiru : {s['v_port']:.0f} m/s (DIUKUR dari mesin acuan)")
    print(f"  lift skala L/D             : {s['lift_mm']:.1f} mm (praktik lokal 4-klep: 9.0)")
    print(f"  overlap lift di TDC skala  : {s['overlap_lift_mm']:.2f} mm")
    print(f"  TB via rasio TB/port acuan : {s['tb_dia_by_port_ratio']:.1f} mm")

    print("\n=== PELUANG TERBESAR: BESARKAN THROAT ===")
    print(f"  throat sekarang   19.50 mm x2 = {geometry()['a_throat_mm2']:.0f} mm2  "
          f"(throat/klep {THROAT_DIA_MM/VALVE_DIA_MM:.3f})")
    print(f"  throat bisa jadi  {s['throat_dia_bisa_mm']:.2f} mm x2 = {s['a_throat_bisa_mm2']:.0f} mm2  "
          f"(pakai rasio {REF['throat_ratio']:.3f} yg sudah kamu buktikan)")
    print(f"  gain luas throat  +{s['gain_throat_pct']:.1f}%")
    print(f"  lebar seat jadi   {s['seat_width_mm']:.2f} mm  (acuan kamu: "
          f"{(REF['valve_dia']-REF['valve_dia']*REF['throat_ratio'])/2:.2f} mm)")
    f2 = flow_potential()
    scale = s["a_throat_bisa_mm2"] / geometry()["a_throat_mm2"]
    print(f"  CFM {f2['cfm_realistis']:.1f} -> {f2['cfm_realistis']*scale:.1f}   "
          f"HP ~{f2['hp_potensial']:.1f} -> ~{f2['hp_potensial']*scale:.1f}")
