#!/bin/bash
# Jalankan satu case flowbench port. Pakai: ./run_case.sh <case_dir> [n_proc]
# Case disalin ke filesystem WSL native dulu -- /mnt/c terlalu lambat untuk IO mesh.
set -euo pipefail
export WM_PROJECT_DIR=/usr/share/openfoam        # paket Debian tidak set ini
SRC="$1"
NP="${2:-8}"
NAME=$(basename "$SRC")
WORK="/root/cfd/$NAME"

rm -rf "$WORK"; mkdir -p /root/cfd
cp -r "$SRC" "$WORK"
cd "$WORK"

# jangan pernah sembunyikan kegagalan: cetak ekor log lalu keluar tidak-nol
step() {
    local name="$1"; shift
    echo ">>> $name"
    "$@" > "log.$name" 2>&1 || {
        rc=$?
        echo "GAGAL di $name (exit $rc)"
        tail -30 "log.$name"
        exit 1
    }
}

step surfaceFeatureExtract surfaceFeatureExtract
step blockMesh blockMesh
step decomposePar decomposePar
step snappyHexMesh mpirun --allow-run-as-root -np "$NP" snappyHexMesh -overwrite -parallel

# patch inlet/outlet/wall baru ada SETELAH snappy -> pasang field sekarang
echo ">>> pasang field 0.orig -> processor*/0"
for d in processor*; do rm -rf "$d/0"; cp -r 0.orig "$d/0"; done

# ponytail: tanpa potentialFoam. Itu butuh field Phi + dict potentialFlow sendiri,
# dan simpleFoam+SIMPLEC biasanya konvergen tanpanya. Tambahkan kalau ternyata liar.
step simpleFoam mpirun --allow-run-as-root -np "$NP" simpleFoam -parallel

# checkMesh & reconstruct boleh gagal tanpa membatalkan hasil
mpirun --allow-run-as-root -np "$NP" checkMesh -parallel -constant > log.checkMesh 2>&1 || true
reconstructPar -latestTime > log.reconstructPar 2>&1 || true

echo "=== SELESAI: $WORK ==="
grep -E "Overall number of cells|^Layer mesh" log.snappyHexMesh | tail -3 || true
grep -E "Max cell openness|Max aspect ratio|non-orthogonality|Max skewness|Mesh OK|\*\*\*" log.checkMesh | tail -8 || true
echo "--- iterasi: $(grep -c '^Time = ' log.simpleFoam) ---"
tail -5 log.simpleFoam
