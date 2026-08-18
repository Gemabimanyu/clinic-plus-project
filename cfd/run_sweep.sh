#!/bin/bash
# Jalankan seluruh sweep. Pakai: ./run_sweep.sh <run_dir> [n_bersamaan] [n_proc]
# 3 case bersamaan x 6 proc = 18 core dari 20. Lebih banyak proc per case tidak
# menolong: mesh cuma ~123k sel, di atas ~6 proc jadi terikat komunikasi.
set -uo pipefail
RUN_DIR="$1"
JOBS="${2:-3}"
NP="${3:-6}"
HERE="$(cd "$(dirname "$0")" && pwd)"
LOG="/root/cfd/sweep.log"

mkdir -p /root/cfd
: > "$LOG"

find "$RUN_DIR" -maxdepth 1 -mindepth 1 -type d -name 'csa*' | sort | \
    xargs -P "$JOBS" -I{} bash -c \
    'n=$(basename "$1"); if bash "$2/run_case.sh" "$1" "$3" > "/root/cfd/$n.log" 2>&1; then
        echo "OK   $n" >> "$4"
     else
        echo "GAGAL $n" >> "$4"
     fi; tail -1 "$4"' _ {} "$HERE" "$NP" "$LOG"

echo "=== RINGKASAN ==="
sort "$LOG" | uniq -c | sort -rn
echo "gagal: $(grep -c '^GAGAL' "$LOG" || true) / $(wc -l < "$LOG")"
