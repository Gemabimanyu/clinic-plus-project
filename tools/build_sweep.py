"""Bangun 36 case OpenFOAM dari 36 STL hasil port_geom.sweep()."""
import csv
import os
import sys

import cfd_case

STL_DIR = "../cfd/stl"
RUN_DIR = "../cfd/run"


def main(n_proc=6):
    with open(os.path.join(STL_DIR, "cases.csv")) as f:
        cases = list(csv.DictReader(f))
    os.makedirs(RUN_DIR, exist_ok=True)
    for i, c in enumerate(cases, 1):
        stl = os.path.join(STL_DIR, c["case"] + ".stl")
        out = os.path.join(RUN_DIR, c["case"])
        cfd_case.build(stl, out, n_proc=n_proc)
        print(f"  [{i:2d}/{len(cases)}] {c['case']}")
    print(f"{len(cases)} case dibangun di {RUN_DIR} ({n_proc} proc/case)")
    return cases


if __name__ == "__main__":
    cfd_case._selfcheck()
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 6)
