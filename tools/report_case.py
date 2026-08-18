"""Tarik angka hasil dari satu case CFD dan periksa apakah layak dipakai."""
import sys
import cfd_case as c

THROAT = 20.2


def summarize(case_dir, throat_mm=THROAT):
    qo, t, nfo = c.read_patch_flux(case_dir, "outlet")
    qi, _, nfi = c.read_patch_flux(case_dir, "inlet")
    imb = abs(qo + qi) / max(abs(qo), 1e-30) * 100.0
    return {
        "time": t,
        "q_outlet_m3s": qo, "n_face_outlet": nfo,
        "q_inlet_m3s": qi, "n_face_inlet": nfi,
        "imbalance_pct": imb,
        "cfm_28": c.cfm_from_flux(qo),
        "cfm_run": c.cfm_from_flux(qo, c.RUN_INH2O, c.RUN_INH2O),
        "Cf": c.flow_coefficient(qo, throat_mm),
        "v_throat_ms": abs(qo) / (3.14159265 / 4 * (throat_mm / 1000.0) ** 2),
    }


if __name__ == "__main__":
    c._selfcheck()
    case = sys.argv[1] if len(sys.argv) > 1 else "//wsl.localhost/Ubuntu/root/cfd/validasi"
    r = summarize(case)
    print(f"\n  waktu akhir       {r['time']}")
    print(f"  debit outlet      {r['q_outlet_m3s']:.6e} m3/s ({r['n_face_outlet']} face)")
    print(f"  debit inlet       {r['q_inlet_m3s']:.6e} m3/s ({r['n_face_inlet']} face)")
    print(f"  ketimpangan massa {r['imbalance_pct']:.3f} %")
    print(f"  kecepatan throat  {r['v_throat_ms']:.1f} m/s")
    print(f"  CFM @ {c.RUN_INH2O:.0f}\"H2O     {r['cfm_run']:.1f}")
    print(f"  CFM @ 28\"H2O      {r['cfm_28']:.1f}")
    print(f"  Cf                {r['Cf']:.4f}")
    verdict = "LAYAK" if r["imbalance_pct"] < 1.0 else "TIDAK LAYAK (mesh bocor?)"
    print(f"  verdict           {verdict}")
