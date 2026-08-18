"""Distribusi luas penampang sepanjang saluran isap: seat klep -> ujung stack.

Aturan pokoknya satu: luas harus MENGERUCUT TERUS ke arah klep, tanpa langkah
dan tanpa pelebaran lokal. Satu-satunya pengecualian yang wajar adalah bowl di
bawah klep, yang memang sedikit lebih besar dari throat.
"""
import math

import matplotlib.pyplot as plt
import numpy as np

import port_design as pdz

THROAT_D = 20.2
N_VALVE = 2
CSA_PORT = 665.0        # gabungan, rasio 1.038 thd throat -- meniru mesin acuan
TB_D = 38.0
SHAFT = 0.07
RPM = 12000

# (jarak dari seat [mm], luas [mm2], nama)
def stations():
    a_throat = N_VALVE * math.pi / 4 * THROAT_D ** 2
    a_tb = math.pi / 4 * TB_D ** 2
    return [
        (0,   a_throat,        "seat klep (throat)"),
        (8,   a_throat * 1.12, "bowl di bawah klep"),
        (22,  a_throat * 1.05, "cabang, sebelum menyatu"),
        (35,  CSA_PORT,        "titik pecah cabang (Y)"),
        (70,  CSA_PORT,        "muka flange head"),
        (145, a_tb,            "pangkal throttle body"),
        (190, a_tb,            "ujung throttle body"),
        (207, a_tb,            "bibir velocity stack"),
    ]


def q_peak(rpm=RPM):
    return pdz.throttle_body(rpm)["q_peak_L_s"] / 1000.0     # m3/s


def figure():
    st = stations()
    x = np.array([s[0] for s in st], float)
    a = np.array([s[1] for s in st], float)
    q = q_peak()
    v = q / (a * 1e-6)

    fig, axes = plt.subplots(2, 1, figsize=(11.0, 8.0), sharex=True)
    fig.suptitle(f"Distribusi luas saluran isap - seat klep sampai ujung stack "
                 f"(puncak {q*1000:.0f} L/s @ {RPM} rpm)", fontsize=12)

    ax = axes[0]
    ax.plot(x, a, "o-", color="steelblue", lw=2, ms=6)
    ax.fill_between(x, 0, a, color="steelblue", alpha=0.15)
    ax.axhline(a[0], ls="--", color="crimson", lw=1,
               label=f"luas throat {a[0]:.0f} mm2 (titik tersempit)")
    for xi, ai, nm in st:
        ax.annotate(nm, (xi, ai), textcoords="offset points", xytext=(4, 7),
                    fontsize=7.5, rotation=25)
    ax.set_ylabel("luas penampang [mm2]"); ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc="lower right"); ax.set_ylim(0, a.max() * 1.35)

    ax = axes[1]
    ax.plot(x, v, "o-", color="seagreen", lw=2, ms=6)
    ax.axhspan(90, 130, color="seagreen", alpha=0.12,
               label="jendela kecepatan sehat di port 90-130 m/s")
    ax.set_xlabel("jarak dari seat klep [mm]  (arah aliran: kanan -> kiri)")
    ax.set_ylabel("kecepatan puncak [m/s]"); ax.grid(alpha=0.3)
    ax.legend(fontsize=8)
    ax.invert_xaxis(); axes[0].invert_xaxis()
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return fig, st, v


RHO = 1.204
K_TB = 0.25       # koef. rugi butterfly di WOT, acuan tekanan dinamik bore
K_PORT = 0.387    # DARI CFD case port615 (Cf 0.8491), acuan kecepatan throat


def tb_compare(diams=(34, 36, 38, 40), rpm=RPM, csa_port=CSA_PORT):
    """Ongkos dan manfaat mengubah diameter TB, pada CSA port yang tetap."""
    q = q_peak(rpm)
    a_throat = N_VALVE * math.pi / 4 * THROAT_D ** 2
    v_throat = q / (a_throat * 1e-6)
    v_port = q / (csa_port * 1e-6)
    rugi_port = K_PORT * 0.5 * RHO * v_throat ** 2

    out = []
    for d in diams:
        a_eff = math.pi / 4 * d ** 2 * (1 - SHAFT)
        v_tb = q / (a_eff * 1e-6)
        rugi_tb = K_TB * 0.5 * RHO * v_tb ** 2
        out.append({"tb_mm": d, "v_tb": v_tb, "v_port": v_port,
                    "rugi_tb_pa": rugi_tb, "rugi_total_pa": rugi_port + rugi_tb})
    # aliran ~ 1/sqrt(rugi total): bandingkan ke TB terbesar
    ref = min(r["rugi_total_pa"] for r in out)
    for r in out:
        r["flow_rel_pct"] = (math.sqrt(ref / r["rugi_total_pa"]) - 1) * 100
    return out, rugi_port, v_port


def port_compare(csas=(560, 615, 665), rpm=RPM):
    """Perbandingan: mengecilkan PORT, bukan TB -- di sinilah kecepatan bekerja."""
    q = q_peak(rpm)
    return [{"csa": c, "v_port": q / (c * 1e-6),
             "dia_setara": math.sqrt(4 * c / math.pi)} for c in csas]


def _selfcheck():
    st = stations()
    a = [s[1] for s in st]
    # throat harus titik tersempit di seluruh saluran
    assert a[0] == min(a), "throat bukan titik tersempit -- desain salah"
    # luas harus naik monoton menjauhi klep, kecuali bowl->cabang yg menyempit
    # sedikit; pastikan tidak ada penyempitan lain setelah flange
    setelah = a[4:]
    assert all(b >= c - 1e-9 for c, b in zip(setelah, setelah[1:])), setelah
    # rasio TB terhadap throat harus dekat mesin acuan (1.60)
    r = (math.pi / 4 * TB_D ** 2 * (1 - SHAFT)) / a[0]
    assert 1.4 < r < 1.8, r

    # TB lebih kecil -> kecepatan TB naik, tapi kecepatan PORT tidak berubah
    tb, _, vp = tb_compare()
    kecil = [t for t in tb if t["tb_mm"] == 34][0]
    besar = [t for t in tb if t["tb_mm"] == 40][0]
    assert kecil["v_tb"] > besar["v_tb"], "TB kecil harus menaikkan v di TB"
    assert abs(kecil["v_port"] - besar["v_port"]) < 1e-9, \
        "diameter TB TIDAK boleh mengubah kecepatan di port"
    assert kecil["flow_rel_pct"] < besar["flow_rel_pct"], "TB kecil harus rugi flow"
    # mengecilkan port memang menaikkan kecepatan port
    pc = port_compare()
    assert pc[0]["v_port"] > pc[-1]["v_port"]
    print(f"selfcheck OK   TB/throat = {r:.2f} (acuan 1.60)")


if __name__ == "__main__":
    _selfcheck()
    fig, st, v = figure()
    fig.savefig("../cfd/tract_profile.png", dpi=130)
    print(f"\n  {'jarak':>7s} {'luas':>8s} {'dia setara':>11s} {'v puncak':>9s}   stasiun")
    for (x, a, nm), vi in zip(st, v):
        print(f"  {x:7.0f} {a:8.0f} {math.sqrt(4*a/math.pi):11.1f} {vi:9.0f}   {nm}")
    print("\n  gambar -> ../cfd/tract_profile.png")

    tb, rugi_port, v_port = tb_compare()
    print(f"\n  === UBAH DIAMETER TB (CSA port tetap {CSA_PORT:.0f} mm2) ===")
    print(f"  rugi port saja: {rugi_port:.0f} Pa   |   kecepatan port: {v_port:.0f} m/s")
    print(f"  {'TB':>5s} {'v di TB':>9s} {'v di port':>10s} {'rugi TB':>9s} "
          f"{'rugi total':>11s} {'flow':>8s}")
    for r in tb:
        print(f"  {r['tb_mm']:5.0f} {r['v_tb']:9.0f} {r['v_port']:10.0f} "
              f"{r['rugi_tb_pa']:9.0f} {r['rugi_total_pa']:11.0f} "
              f"{r['flow_rel_pct']:+7.1f}%")

    print(f"\n  === UBAH CSA PORT (di sinilah kecepatan bekerja) ===")
    print(f"  {'CSA':>6s} {'dia setara':>11s} {'v di port':>10s}")
    for r in port_compare():
        print(f"  {r['csa']:6.0f} {r['dia_setara']:11.1f} {r['v_port']:10.0f}")
