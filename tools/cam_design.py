"""Perhitungan camshaft: kompresi dinamis, durasi, overlap, dan kelegaan klep.

Empat hal yang benar-benar diatur cam, berurutan menurut kepentingannya:

  1. IVC (klep in menutup) -- MENENTUKAN kompresi dinamis dan rpm puncak.
     Ini kejadian terpenting di seluruh camshaft. Kompresi statis 14:1 itu
     angka di atas kertas; yang dirasakan mesin adalah kompresi dinamis, dan
     IVC yang menentukannya.
  2. Durasi + lift -- menentukan berapa banyak yang BISA lewat (time-area).
  3. Overlap di TDC -- menentukan pembilasan sisa gas buang.
  4. Kelegaan klep-piston -- bukan soal tenaga, soal mesin pecah atau tidak.

Semua diskalakan dari mesin acuan Gema yang terbukti, bukan dari angka umum.
"""
import math

# ------------------------------------------------------------------ MESIN
BORE = 57.3
STROKE = 58.0
ROD = 95.0             # TERUKUR. rod/stroke = 1.64 -- pendek, khas mesin kecil
CR_STATIS = 14.0
N_KLEP_IN = 2
KLEP_IN_DIA = 22.0
LIFT = 9.0
RPM_TARGET = 12000

# --------------------------------------------------------------- ACUAN
REF_DUR = 278.0        # deg @1mm
REF_LIFT = 10.8
REF_KLEP = 31.0
REF_N_KLEP = 1
REF_OVERLAP_LIFT = 3.6
REF_THROAT_A = math.pi / 4 * 29.0 ** 2
REF_VD = 199.5
REF_RPM = 10000

THROAT_A = N_KLEP_IN * math.pi / 4 * 20.2 ** 2
VD = math.pi / 4 * BORE ** 2 * STROKE / 1000.0      # cc
VC = VD / (CR_STATIS - 1.0)                          # cc ruang bakar


def piston_dari_tdc(theta_deg, stroke=STROKE, rod=ROD):
    """Jarak piston dari TDC [mm]. theta diukur dari TDC."""
    r = stroke / 2.0
    t = math.radians(theta_deg)
    return r * (1 - math.cos(t)) + rod - math.sqrt(rod ** 2 - (r * math.sin(t)) ** 2)


def dcr(ivc_abdc, cr_statis=CR_STATIS):
    """Kompresi dinamis: rasio volume saat klep in MENUTUP terhadap ruang bakar."""
    s = piston_dari_tdc(180.0 + ivc_abdc)
    v = VC + math.pi / 4 * BORE ** 2 * s / 1000.0
    return v / VC


def durasi_dari_skala(rpm=RPM_TARGET):
    """Durasi yang dibutuhkan, diskalakan dari cam acuan lewat time-area.

    Syaratnya: (luas throat x durasi) / (kapasitas x rpm) harus sama, karena
    itulah 'jendela aliran per siklus per cc' yang menentukan pengisian.
    """
    ref = REF_THROAT_A * REF_DUR / (REF_VD * REF_RPM)
    return ref * VD * rpm / THROAT_A


def lift_pada(theta_dari_bukaan, durasi, lift_max=LIFT):
    """Profil lift pendekatan (harmonik). Cam balap sungguhan lebih agresif --
    lift di sisi flank lebih tinggi dari ini, jadi kelegaan klep yang dihitung
    dgn profil ini TERLALU OPTIMIS. Pakai faktor keamanan."""
    if theta_dari_bukaan <= 0 or theta_dari_bukaan >= durasi:
        return 0.0
    return lift_max * math.sin(math.pi * theta_dari_bukaan / durasi) ** 2


def overlap_lift_setara():
    """Lift di TDC yang memberi LUAS TIRAI overlap per cc setara mesin acuan.

    Penting: 4-klep punya DUA klep in, jadi untuk luas yang sama lift-nya
    lebih kecil. Menskalakan lift lewat diameter saja (3.6 x 22/31 = 2.55mm)
    itu KELIRU -- luasnya jadi dua kali lipat.
    """
    a_ref = REF_N_KLEP * math.pi * REF_KLEP * REF_OVERLAP_LIFT / REF_VD
    return a_ref * VD / (N_KLEP_IN * math.pi * KLEP_IN_DIA)


def bagi_timing(durasi, overlap_lift):
    """Dari durasi + target lift di TDC -> IVO dan IVC.

    Ini pertukaran pokok di cam: dgn durasi tetap, overlap lebih besar berarti
    IVO lebih awal, yang memaksa IVC lebih awal juga -> kompresi dinamis naik.
    """
    if overlap_lift >= LIFT:
        raise ValueError("lift overlap tidak boleh >= lift maksimum")
    # balik dari lift(theta) = L sin^2(pi theta/dur)
    frac = math.asin(math.sqrt(overlap_lift / LIFT)) / math.pi
    ivo_btdc = frac * durasi
    ivc_abdc = durasi - 180.0 - ivo_btdc
    return ivo_btdc, ivc_abdc


def kantong_klep(durasi, ivo_btdc, kelegaan_min=1.2, faktor_aman=1.25):
    """Kedalaman kantong klep di piston yang dibutuhkan [mm].

    Dihitung sepanjang sumbu klep, disederhanakan. Ini PERKIRAAN AWAL --
    pengecekan sungguhan wajib pakai lilin/clay, karena sudut klep 13 deg dan
    bentuk kubah piston tidak dimodelkan di sini.
    """
    terburuk = 0.0
    sudut_terburuk = 0.0
    for i in range(-600, 601):
        th = i / 10.0                       # -60 .. +60 deg dari TDC
        lift = lift_pada(th + ivo_btdc, durasi)
        piston = piston_dari_tdc(abs(th))
        butuh = lift - piston
        if butuh > terburuk:
            terburuk, sudut_terburuk = butuh, th
    return max(0.0, terburuk * faktor_aman + kelegaan_min), sudut_terburuk


def anggaran_ruang_bakar(kantong_mm, gasket_tebal=0.8, deck=0.5,
                         pentroof_tinggi=3.5, n_klep_total=4, klep_rata=20.5):
    """Anggaran volume ruang bakar untuk mencapai CR statis yang diinginkan.

    KANTONG KLEP IKUT MENAMBAH volume ruang bakar -- ini yang paling sering
    dilupakan. Pada bore 57.3 mm dgn target 11.5 cc, empat kantong sedalam 4 mm
    bisa memakan seperempat anggaran dan menjatuhkan CR beberapa angka penuh.
    """
    a_bore = math.pi / 4 * BORE ** 2
    v_gasket = a_bore * gasket_tebal / 1000.0
    v_deck = a_bore * deck / 1000.0
    v_pentroof = a_bore * pentroof_tinggi / 1000.0
    # kantong: cekungan dangkal, rata-rata ~40% dari kedalaman maksimum
    a_kantong = math.pi / 4 * (klep_rata + 1.0) ** 2
    v_kantong = n_klep_total * a_kantong * kantong_mm * 0.40 / 1000.0
    total = v_gasket + v_deck + v_pentroof + v_kantong
    return {
        "gasket": v_gasket, "deck": v_deck, "pentroof": v_pentroof,
        "kantong": v_kantong, "total_tanpa_dome": total,
        "target_vc": VC,
        "dome_dibutuhkan": total - VC,
        "cr_tanpa_dome": 1 + VD / total,
    }


def bbm_dari_dcr(d):
    if d < 9.0:
        return "Pertamax 92-95 cukup"
    if d < 10.0:
        return "butuh 98 RON (Pertamax Turbo)"
    if d < 11.0:
        return "butuh 100+ RON / campuran avgas"
    if d < 12.5:
        return "butuh bensin balap 102+ atau METANOL"
    return "METANOL saja, bensin akan detonasi"


def _selfcheck():
    # piston: 0 di TDC, penuh stroke di BDC
    assert abs(piston_dari_tdc(0)) < 1e-9
    assert abs(piston_dari_tdc(180) - STROKE) < 1e-6, piston_dari_tdc(180)
    # dekat TDC piston bergerak lambat -- inilah kenapa kantong klep perlu
    assert piston_dari_tdc(10) < 0.8, piston_dari_tdc(10)
    # IVC makin telat -> kompresi dinamis makin rendah
    assert dcr(40) > dcr(60) > dcr(80)
    # DCR tidak boleh melebihi CR statis
    assert dcr(0) <= CR_STATIS + 1e-9, dcr(0)
    # durasi naik kalau rpm target naik
    assert durasi_dari_skala(13000) > durasi_dari_skala(11000)
    # overlap setara harus LEBIH KECIL dari skala-diameter yg keliru (2.55mm)
    o = overlap_lift_setara()
    assert 0.5 < o < 2.55, o
    # bagi_timing harus konsisten bolak-balik
    ivo, ivc = bagi_timing(280.0, 2.0)
    assert abs(lift_pada(ivo, 280.0) - 2.0) < 1e-9, lift_pada(ivo, 280.0)
    assert abs(ivo + 180 + ivc - 280.0) < 1e-9
    # kantong lebih dalam -> volume ruang bakar naik -> CR turun
    a = anggaran_ruang_bakar(2.0)["cr_tanpa_dome"]
    b = anggaran_ruang_bakar(5.0)["cr_tanpa_dome"]
    assert a > b, (a, b)
    # dan komponennya harus menjumlah
    r = anggaran_ruang_bakar(4.0)
    assert abs(r["gasket"] + r["deck"] + r["pentroof"] + r["kantong"]
               - r["total_tanpa_dome"]) < 1e-9
    print("selfcheck OK\n")


if __name__ == "__main__":
    _selfcheck()
    print(f"  kapasitas {VD:.1f} cc | ruang bakar {VC:.2f} cc | "
          f"CR statis {CR_STATIS}:1 | rod {ROD} mm (ASUMSI)\n")

    print("  === 1. IVC MENENTUKAN KOMPRESI DINAMIS ===")
    print(f"  {'IVC ABDC':>9s} {'DCR':>7s}   bahan bakar")
    for ivc in (35, 40, 45, 50, 55, 60, 65, 70):
        d = dcr(ivc)
        print(f"  {ivc:9.0f} {d:7.2f}   {bbm_dari_dcr(d)}")

    print("\n  === 2. DURASI DARI TIME-AREA (diskalakan dari cam acuanmu) ===")
    print(f"  acuan: {REF_DUR:.0f} deg @1mm, throat {REF_THROAT_A:.0f} mm2, "
          f"{REF_VD:.0f} cc @ {REF_RPM} rpm")
    print(f"  baru : throat {THROAT_A:.0f} mm2, {VD:.0f} cc")
    print(f"  {'rpm target':>11s} {'durasi in':>10s}")
    for rpm in (11000, 11500, 12000, 12500, 13000):
        print(f"  {rpm:11d} {durasi_dari_skala(rpm):10.0f} deg")

    ol = overlap_lift_setara()
    print(f"\n  === 3. OVERLAP ===")
    print(f"  acuan: lift {REF_OVERLAP_LIFT} mm di TDC, 1 klep in {REF_KLEP} mm")
    print(f"  baru : lift {ol:.2f} mm di TDC, 2 klep in {KLEP_IN_DIA} mm")
    print(f"  (luas tirai overlap per cc SETARA; skala diameter saja keliru)")

    print(f"\n  === 4. PERTUKARAN: durasi vs overlap vs kompresi dinamis ===")
    print(f"  {'durasi':>7s} {'IVO BTDC':>9s} {'IVC ABDC':>9s} {'DCR':>7s} "
          f"{'kantong':>8s}   bahan bakar")
    for dur in (250, 260, 270, 280, 290, 300):
        try:
            ivo, ivc = bagi_timing(dur, ol)
            d = dcr(ivc)
            k, _ = kantong_klep(dur, ivo)
            print(f"  {dur:7.0f} {ivo:9.1f} {ivc:9.1f} {d:7.2f} {k:8.2f}   "
                  f"{bbm_dari_dcr(d)}")
        except ValueError as e:
            print(f"  {dur:7.0f}   {e}")

    ivo, _ = bagi_timing(280.0, ol)
    k, sudut = kantong_klep(280.0, ivo)
    a = anggaran_ruang_bakar(k)
    print(f"\n  === 5. APAKAH 14:1 BISA DIBANGUN? (durasi 280, kantong {k:.1f} mm) ===")
    print(f"  kelegaan paling kritis di {sudut:+.0f} deg dari TDC")
    print(f"  {'komponen':16s} {'volume cc':>10s}")
    for nm, key in (("pent-roof", "pentroof"), ("gasket 0.8mm", "gasket"),
                    ("deck 0.5mm", "deck"), ("4 kantong klep", "kantong")):
        print(f"  {nm:16s} {a[key]:10.2f}")
    print(f"  {'-'*27}")
    print(f"  {'total':16s} {a['total_tanpa_dome']:10.2f}")
    print(f"  {'target 14:1':16s} {a['target_vc']:10.2f}")
    print(f"\n  -> CR tanpa dome piston: {a['cr_tanpa_dome']:.2f}:1")
    print(f"  -> dome piston harus mengusir {a['dome_dibutuhkan']:.2f} cc "
          f"(tinggi rata2 {a['dome_dibutuhkan']*1000/(math.pi/4*BORE**2):.2f} mm)")
    print(f"  -> kantong klep saja memakan "
          f"{a['kantong']/a['target_vc']*100:.0f}% dari anggaran 14:1")
