"""Bandingkan bahan bakar: energi per kg UDARA, bukan per kg bahan bakar.

Ini pembeda yang menentukan. Udara yang terbatas, bukan bahan bakar. Mesin
NA cuma bisa menghisap sejumlah udara tertentu; yang menentukan tenaga adalah
berapa banyak energi yang bisa dibawa tiap kilogram udara itu.
"""
import math

CP_UDARA = 1.005        # kJ/kg.K

# nama, LHV MJ/kg, AFR stoikiometri, AFR tenaga puncak, panas laten kJ/kg, densitas kg/L
BBM = [
    ("Bensin 92 RON",      43.5, 14.7, 12.5,  350, 0.745),
    ("Bensin 98 RON",      43.5, 14.7, 12.6,  350, 0.750),
    ("Avgas 100LL",        43.5, 14.9, 12.8,  350, 0.720),
    ("Race gas beroksigen", 40.0, 12.9, 11.5,  380, 0.760),
    ("Metanol",            19.9,  6.45, 4.80, 1100, 0.792),
    ("Nitrometana",        11.3,  1.70, 1.00,  560, 1.137),
]


def analisa(lhv, afr_st, afr_power, laten, densitas):
    e_per_udara_st = lhv / afr_st                    # MJ per kg udara
    e_per_udara_pk = lhv / afr_power
    lambda_pk = afr_power / afr_st
    # pendinginan muatan: panas laten yang diserap per kg udara
    dingin = laten / afr_power / CP_UDARA            # K penurunan suhu
    return {
        "e_st": e_per_udara_st, "e_pk": e_per_udara_pk,
        "lambda_pk": lambda_pk, "dingin": dingin,
        "konsumsi_massa": 1.0 / afr_power,
        "konsumsi_volume": 1.0 / afr_power / densitas,
    }


def _selfcheck():
    b = dict((n, analisa(*a)) for n, *a in BBM)
    # metanol harus bawa energi lebih per kg udara walau LHV-nya kecil
    assert b["Metanol"]["e_pk"] > b["Bensin 92 RON"]["e_pk"], b
    # nitro harus jauh di atas semuanya
    assert b["Nitrometana"]["e_pk"] > 3 * b["Bensin 92 RON"]["e_pk"]
    # pendinginan muatan metanol harus jauh lebih besar
    assert b["Metanol"]["dingin"] > 5 * b["Bensin 92 RON"]["dingin"]
    # lambda tenaga puncak bensin harus 0.84-0.88
    assert 0.83 < b["Bensin 92 RON"]["lambda_pk"] < 0.89
    print("selfcheck OK\n")


if __name__ == "__main__":
    _selfcheck()
    dasar = analisa(*BBM[0][1:])
    hdr = (f"  {'bahan bakar':22s} {'AFR st':>7s} {'AFR pk':>7s} {'lambda':>7s} "
           f"{'MJ/kg udara':>12s} {'vs bensin':>10s} {'dingin K':>9s} {'vol x':>7s}")
    print(hdr); print("  " + "-" * (len(hdr) - 2))
    for nm, *a in BBM:
        r = analisa(*a)
        print(f"  {nm:22s} {a[1]:7.2f} {a[2]:7.2f} {r['lambda_pk']:7.2f} "
              f"{r['e_pk']:12.2f} {r['e_pk']/dasar['e_pk']*100:9.0f}% "
              f"{r['dingin']:9.0f} {r['konsumsi_volume']/dasar['konsumsi_volume']:7.2f}")
    print("\n  MJ/kg udara pada AFR tenaga puncak = potensi tenaga sesungguhnya")
    print("  dingin K = penurunan suhu muatan dari penguapan bahan bakar")
    print("  vol x    = kebutuhan volume bahan bakar relatif terhadap bensin")
