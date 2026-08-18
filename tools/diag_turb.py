"""Periksa besar viskositas turbulen. nut yang kelewat besar bikin aliran
seolah sangat kental dan rugi jadi tidak masuk akal, padahal geometri benar."""
import re
import sys

import numpy as np

NU_LAMINAR = 1.5e-5


def internal(path):
    t = open(path).read()
    m = re.search(r"internalField\s+nonuniform[^(]*\((.*?)\)\s*;", t, re.S)
    if m:
        return np.fromstring(m.group(1), sep=" ")
    m = re.search(r"internalField\s+uniform\s+([-\d.eE+]+)\s*;", t)
    return np.array([float(m.group(1))]) if m else None


def main(case, tstep):
    root = f"//wsl.localhost/Ubuntu/root/cfd/{case}/{tstep}"
    for f in ("nut", "k", "omega"):
        v = internal(f"{root}/{f}")
        if v is None:
            print(f"  {f}: tidak terbaca")
            continue
        print(f"  {f:6s} min {v.min():12.5g}  max {v.max():12.5g}  "
              f"rata2 {v.mean():12.5g}")
        if f == "nut":
            print(f"         nut/nu  maks {v.max()/NU_LAMINAR:10.0f}  "
                  f"rata2 {v.mean()/NU_LAMINAR:10.0f}   (wajar 50-500)")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "core_bengkok",
         sys.argv[2] if len(sys.argv) > 2 else "3000")
