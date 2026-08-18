"""Compute volume by treating section circles as boundaries of solid regions.
At each Z, the circles define boundaries. The solid region fills between
alternating pairs: between circle[0] and circle[1], between circle[2] and circle[3], etc.
"""
import math

# (Z, [r1, r2, r3, r4, ...]) where solid fills between pairs
PROFILE = [
    ( 0.0, [20.0, 25.0, 28.44]),  # bore at 20, then solid from 25 to 28.44? No...
]

# Actually, let me re-examine. At Z=0:
# - Circle at r=20: bore inner wall
# - Circle at r=25: ??? some feature at r=25
# - Circle at r=28.44: outer wall
# The M5 hole and internal features might create extra circles
# At Z=3-7 (no M5 region): only 2 circles: r=20 (bore) and r=28.44 (outer)
# That means solid from 20 to 28.44

# At Z=0-2.5: 3 circles: 20, 25, 28.44
# r=25 might be the M5 clearance bore perimeter?
# Actually wait - r=25 from the STEP surfaces: CYLINDRICAL r=25mm is listed
# But only visible at Z=0-2.5 and Z=8-11

# Let me just compute using the simple pairs that I know are correct
# from the earlier extract (min, max radii) as the true inner/outer

CLEAN_PROFILE = [
    ( 0.0, [(20.0, 28.44)]),
    ( 3.0, [(20.0, 28.44)]),
    ( 7.0, [(20.0, 28.44)]),
    ( 7.5, [(20.0, 28.44)]),  # transitional but still full
    ( 8.0, [(20.0, 28.44)]),
    (10.0, [(19.0, 28.44)]),
    (10.5, [(19.02, 28.44)]),
    (12.0, [(19.07, 27.97)]),
    (12.5, [(19.09, 27.51)]),
    (13.0, [(19.11, 27.05)]),
    (13.5, [(19.12, 26.61)]),
    (14.0, [(19.14, 26.18)]),
    (14.5, [(19.16, 22.96)]),
    (15.0, [(19.18, 22.32)]),
    (15.5, [(19.19, 21.89)]),
    (16.0, [(19.21, 21.60)]),
    (17.0, [(19.24, 21.30)]),
    (20.0, [(19.35, 21.35)]),
    (25.0, [(19.52, 21.52)]),
    (30.0, [(19.70, 21.70)]),
    (35.0, [(19.87, 21.87)]),
    (40.0, [(20.05, 22.05)]),
    (45.0, [(20.22, 22.22)]),
    (50.0, [(20.40, 22.40)]),
    (51.0, [(20.43, 22.53), (37.03, 39.06)]),
    (52.0, [(20.52, 23.56), (35.99, 38.97)]),
    (53.0, [(20.73, 24.60), (34.94, 38.76)]),
    (54.0, [(21.05, 25.63), (33.90, 38.44)]),
    (55.0, [(21.50, 26.67), (32.85, 37.99)]),
    (56.0, [(22.11, 27.70), (31.80, 37.38)]),
    (57.0, [(22.92, 28.74), (30.76, 36.57)]),
    (57.5, [(23.43, 29.26), (30.24, 36.06)]),
    (58.0, [(24.02, 35.48)]),
    (58.5, [(24.72, 34.77)]),
    (59.0, [(25.61, 33.88)]),
    (59.5, [(26.82, 32.67)]),
    (59.8, [(27.98, 31.52)]),
    (59.9, [(28.61, 30.88)]),
]

def area(rings):
    return sum(math.pi * (ro**2 - ri**2) for ri, ro in rings)

vol = 0
for i in range(len(CLEAN_PROFILE) - 1):
    z1, r1 = CLEAN_PROFILE[i]
    z2, r2 = CLEAN_PROFILE[i+1]
    vol += (area(r1) + area(r2)) / 2 * (z2 - z1)

print(f"Volume: {vol:.1f} mm3")
print(f"Target: 35814 mm3")
print(f"Delta: {abs(vol-35814)/35814*100:.1f}%")

# But wait - at Z=0 the base might not be fully solid (the r=25 circle suggests a feature)
# Let's also check with base adjusted
# At Z=0-2.5: there's a circle at r=25, meaning solid from 25 to 28.44 only
# The bore circle at r=20 is there but the area from 20 to 25 is... the bore itself

# Actually the section shows circles at r=20 and r=25 and r=28.44
# That means solid regions are: 20->25 (one solid) and... no wait
# For a simple revolved part with bore, the section should give 2 circles (bore, outer)
# 3 circles means there's a hollow between 20 and 25
# Let me recompute with the base being hollow from 20-25

HOLLOW_BASE_PROFILE = [
    ( 0.0, [(25.0, 28.44)]),
    ( 2.5, [(25.0, 28.44)]),
    ( 3.0, [(20.0, 28.44)]),
    ( 7.0, [(20.0, 28.44)]),
    ( 7.5, [(20.0, 28.44)]),
    ( 8.0, [(25.0, 28.44)]),
    ( 9.0, [(25.0, 28.44)]),
    (10.0, [(25.0, 28.44)]),
    (10.5, [(25.0, 28.44)]),
    (11.0, [(25.0, 28.44)]),
    (12.0, [(19.07, 27.97)]),
    (12.5, [(19.09, 27.51)]),
    (13.0, [(19.11, 27.05)]),
    (13.5, [(19.12, 26.61)]),
    (14.0, [(19.14, 26.18)]),
    (14.5, [(19.16, 22.96)]),
    (15.0, [(19.18, 22.32)]),
    (15.5, [(19.19, 21.89)]),
    (16.0, [(19.21, 21.60)]),
    (17.0, [(19.24, 21.30)]),
    (20.0, [(19.35, 21.35)]),
    (25.0, [(19.52, 21.52)]),
    (30.0, [(19.70, 21.70)]),
    (35.0, [(19.87, 21.87)]),
    (40.0, [(20.05, 22.05)]),
    (45.0, [(20.22, 22.22)]),
    (50.0, [(20.40, 22.40)]),
    (51.0, [(20.43, 22.53), (37.03, 39.06)]),
    (52.0, [(20.52, 23.56), (35.99, 38.97)]),
    (53.0, [(20.73, 24.60), (34.94, 38.76)]),
    (54.0, [(21.05, 25.63), (33.90, 38.44)]),
    (55.0, [(21.50, 26.67), (32.85, 37.99)]),
    (56.0, [(22.11, 27.70), (31.80, 37.38)]),
    (57.0, [(22.92, 28.74), (30.76, 36.57)]),
    (57.5, [(23.43, 29.26), (30.24, 36.06)]),
    (58.0, [(24.02, 35.48)]),
    (58.5, [(24.72, 34.77)]),
    (59.0, [(25.61, 33.88)]),
    (59.5, [(26.82, 32.67)]),
    (59.8, [(27.98, 31.52)]),
    (59.9, [(28.61, 30.88)]),
]

vol2 = 0
for i in range(len(HOLLOW_BASE_PROFILE) - 1):
    z1, r1 = HOLLOW_BASE_PROFILE[i]
    z2, r2 = HOLLOW_BASE_PROFILE[i+1]
    vol2 += (area(r1) + area(r2)) / 2 * (z2 - z1)

print(f"\nWith hollow base (25->28.44 at Z=0-2.5, 8-11):")
print(f"Volume: {vol2:.1f} mm3")
print(f"Delta: {abs(vol2-35814)/35814*100:.1f}%")
