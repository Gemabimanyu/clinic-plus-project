import math

# Master per-slice volumes
MASTER_SLICE = {
    0: 379.9, 1: 759.9, 2: 759.9, 3: 746.0, 4: 727.7,
    # Z=5-7 missing due to boolean issues, estimate from Z=8 cumulative
    8: 759.9, 9: 759.9, 10: 820.6, 11: 877.7, 12: 865.0,
    13: 846.2, 14: 710.9, 15: 414.8, 16: 309.2, 17: 263.6,
    51: 577.1, 52: 1121.1, 53: 1434.8, 54: 1703.8, 55: 1922.9,
    56: 2083.1, 57: 2168.3, 58: 2091.7, 59: 1527.0, 60: 343.6,
}

# My runner profile annulus area at key Z values
def a(ri, ro):
    return math.pi * (ro**2 - ri**2)

# Runner
my_areas = {
    0:  a(25.00, 28.44),   # 577.5
    3:  a(20.00, 28.44),   # 1284.4
    8:  a(25.00, 28.44),   # 577.5
    10: a(19.00, 28.44),   # 1408.7 (undercut opens bore to r=19)
    12: a(19.07, 27.97),
    14: a(19.14, 26.18),
    17: a(19.24, 21.30),
    50: a(20.40, 22.40),
}

print("Z   Master/mm  My_area  Ratio")
for z in sorted(my_areas):
    if z in MASTER_SLICE:
        ratio = my_areas[z] / MASTER_SLICE[z] if MASTER_SLICE[z] > 0 else 0
        print(f"{z:3d}  {MASTER_SLICE[z]:8.1f}  {my_areas[z]:7.1f}  {ratio:.2f}")

# Bellmouth comparison
print("\nBellmouth (runner ring + bell ring):")
bell_data = {
    51: (a(20.43, 22.53) + a(37.03, 39.06)),
    52: (a(20.52, 23.56) + a(35.99, 38.97)),
    53: (a(20.73, 24.60) + a(34.94, 38.76)),
    54: (a(21.05, 25.63) + a(33.90, 38.44)),
    55: (a(21.50, 26.67) + a(32.85, 37.99)),
    56: (a(22.11, 27.70) + a(31.80, 37.38)),
    57: (a(22.92, 28.74) + a(30.76, 36.57)),
    58: a(24.02, 35.48),
    59: a(25.61, 33.88),
    60: a(28.61, 30.88),  # approximate
}
for z in sorted(bell_data):
    if z in MASTER_SLICE:
        ratio = bell_data[z] / MASTER_SLICE[z]
        print(f"{z:3d}  {MASTER_SLICE[z]:8.1f}  {bell_data[z]:7.1f}  {ratio:.2f}")

# Key issue: at Z=10, master has 820.6 mm3/mm but my area with r_in=19.0 is:
print(f"\nZ=10 with r_in=19: {a(19.0, 28.44):.1f}")
print(f"Z=10 with r_in=25: {a(25.0, 28.44):.1f}")
print(f"Master Z=10 slice: 820.6")
# 820.6 is between 577.5 (r=25) and 1408.7 (r=19).
# The section at Z=10 showed r_in=19 and r_out=28.44 plus an extra circle at r=20 and r=25
# So the actual solid might be: (19, 20) gap + (25, 28.44)
# area = a(19,20) + a(25,28.44) = π*(400-361) + 577.5 = π*39 + 577.5 = 122.5 + 577.5 = 700
# Hmm, 700 vs master 820.6... not right either

# The Z=10 section data: [(19.0, 19.0), (20.0, 20.0), (25.0, 28.44)]
# This means 3 circles: r=19 (undercut inner), r=20 (bore), r=25-28.44 (outer wall)
# Solid fills between alternating boundaries from outside:
# Outside: r=28.44 → r=25 = solid ring (577.5)
# Then: r=25 → r=20 = air/void? But 25-20=5mm gap
# Then: r=20 → r=19 = solid ring (122.5)
# Total = 577.5 + 122.5 = 700.0
# But master says 820.6. So there's more material than this simple model.
# The section extraction might not capture ALL circles.

print(f"\nZ=10 solid = (19,20)+(25,28.44): {a(19,20)+a(25,28.44):.1f}")
print(f"Z=10 solid = (19,28.44): {a(19,28.44):.1f}")
