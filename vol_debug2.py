"""Compare my profile's volume per Z against master's measured per-slice volumes."""
import math

# Master cumulative volumes at integer Z (from boolean cut)
MASTER_CUM = {
    0: 379.9, 1: 1139.8, 2: 1899.7, 3: 2645.7, 4: 3373.4,
    8: 6325.5, 9: 7085.4, 10: 7906.0, 11: 8783.7, 12: 9648.7,
    13: 10494.9, 14: 11205.8, 15: 11620.6, 16: 11929.8, 17: 12193.4,
    20: 12959.7, 25: 14245.7, 30: 15542.7, 35: 16850.6, 40: 18169.5,
    45: 19499.4, 50: 20840.3, 51: 21417.4, 52: 22538.5, 53: 23973.3,
    54: 25677.1, 55: 27600.0, 56: 29683.1, 57: 31851.4, 58: 33943.1,
    59: 35470.1, 60: 35813.7,
}

# My runner profile cross-section area at each Z
# At Z=0-2.5: annulus r=25 to r=28.44
# At Z=3-7: annulus r=20 to r=28.44
# At Z=8-10: annulus r=25 to r=28.44

def annulus(ri, ro):
    return math.pi * (ro**2 - ri**2)

# What the master says per integer Z
print("Master volume per mm:")
for z in sorted(MASTER_CUM):
    if z > 0 and z-1 in MASTER_CUM:
        print(f"  Z={z-1}-{z}: {MASTER_CUM[z] - MASTER_CUM[z-1]:.1f} mm3")

print("\nMy profile areas:")
# Z=0: r_in=25, r_out=28.44 → area = π(28.44²-25²) = π(808.9-625) = π*183.9 = 577.9
print(f"  Z=0 (25,28.44): {annulus(25,28.44):.1f}")
# Z=3: r_in=20, r_out=28.44 → area = π(28.44²-20²) = π(808.9-400) = π*408.9 = 1284.8
print(f"  Z=3 (20,28.44): {annulus(20,28.44):.1f}")
# Z=8: r_in=25, r_out=28.44
print(f"  Z=8 (25,28.44): {annulus(25,28.44):.1f}")
# Z=17: r_in=19.24, r_out=21.30
print(f"  Z=17 (19.24,21.30): {annulus(19.24,21.30):.1f}")

# Master slice Z=0-1 = 760 mm3. My area at Z=0 is 578.
# 578 is less than 760. So master has MORE material at Z=0-1.
# Master at Z=0 = 380 (half slice), Z=1 = 760 (full slice)
# 760 mm3/mm implies area = 760 mm2. My area is 578.
# So master base is DENSER than (25, 28.44)

# Actually master Z=0 slice = 379.9 (this is from Z=-0.5 to Z=0.5 effectively)
# Z=1 slice = 759.9 (Z=0 to Z=1... no, it's cumulative: cum at Z=1 - cum at Z=0)
# So Z=0 to Z=1 has 759.9 mm3. That means area ≈ 760 mm2
# But annulus(25, 28.44) = 577.9. So 760 - 578 = 182 mm3 missing.
# Maybe the M5 hole boss adds material? Or the bore is not r=25 everywhere.

# Let me check: at Z=0.5, the section shows [(20.0, 20.0), (25.0, 28.44)]
# That means a circle at r=20 and a ring from r=25 to r=28.44
# But wait - there are likely more edges I'm not capturing.
# The r=20 circle and r=25 circle define the BORE: a cylinder from r=0 to r=20 (air)
# and then solid from r=25 to r=28.44... but what about r=20 to r=25?

# In a revolved profile, at Z=0.5:
# - The bore hole is r=0 to r=20 (empty)
# - r=20 to r=25: could be empty (shoulder/channel) or solid
# - r=25 to r=28.44: solid wall

# 3 circles means the cross-section has 3 boundaries:
# Outside to in: r=28.44 (outer wall), r=25 (inner wall start), r=20 (bore)
# For a solid with one bore: solid is from r=20 to r=28.44 = 1284.8 mm2
# For a solid with a channel: solid from r=25 to r=28.44 = 577.9 mm2

# Master Z=0-1 volume = 760. If area = 760, that's between 578 and 1285.
# 760 / π ≈ 241.9 → ro²-ri² = 241.9
# If ri=20: ro = sqrt(400+241.9) = sqrt(641.9) = 25.34 → outer r=25.34? doesn't match 28.44
# If ri=25: ro²=625+241.9=866.9, ro=29.44? too big

# Hmm. Maybe the slice volume measurement is wrong because of the M5 hole
# and other features. The boolean cut at Z=5 failed, suggesting geometry issues.

# Better approach: compute my model's analytical volume
# My profile: base (r=25→28.44) from Z=0-2.5, then (r=20→28.44) Z=3-7, etc.
# Ignore step transitions for now

base_vol = annulus(25, 28.44) * 2.5  # Z=0 to 2.5
base_vol += annulus(20, 28.44) * 4.0  # Z=3 to 7
base_vol += annulus(25, 28.44) * 2.0  # Z=8 to 10
print(f"\nBase Z=0-10 volume (simple): {base_vol:.1f}")
print(f"Master Z=0-10 volume: {MASTER_CUM[10]:.1f}")
print(f"Excess: {base_vol - MASTER_CUM[10]:.1f}")
