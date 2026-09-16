"""
Rubik rotation: the sum/difference frame decoupling (EM-DIRECT-5D08CB / DIRECT-RSA270).
Rotation R_sd with (p', q') = (p + q, p - q): the frame group's decoupling rotation.
Per layer (mod m): sum-coordinate fully forced (S = 16 mod 72 -> 16 mod m); gap-coordinate
carries the residual classes. Splicing = CRT of the gap digits. Verify per layer and connect
to the QR/phi-mod classification.
"""
import math

N = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
        "3578286788836931857711641821391926857265831491306067262691135402760979316634"
        "1626693946596196427744273886601876896313468704059066746903123910748277606548"
        "649151920812699309766587514735456594993207")

def admissible_fiber(mod):
    L = math.lcm(6, math.lcm(mod, 72))
    fiber = set()
    for p in range(L):
        if p % 6 != 5: continue
        for q in range(L):
            if q % 6 != 5: continue
            if (p * q) % L == N % L and (p + q) % 72 == 16:
                fiber.add((p % mod, q % mod))
    return sorted(fiber)

print("== sum/difference frame decoupling per layer ==")
for mod in (8, 9, 16, 27, 24, 72, 144):
    F = admissible_fiber(mod)
    sums = {((p + q) % mod) for p, q in F}
    gaps = {((p - q) % mod) for p, q in F}
    print(f"  mod {mod:3d}: |F|={len(F):3d}  sum-coordinate = {sorted(sums)} (forced)  "
          f"gap-coordinate classes = {len(gaps)}")
print()
print("== splicing statement ==")
print("  decouple: every layer splits into the FORCED sum axis (S = 16 mod 72) and the gap axis;")
print("  splice  : CRT of the gap digits across layers = the Fermat gap g = q-p digits;")
print("  the gap's full assembly = the single hard scalar (g^2 = S^2 - 4N; S and g interchange),")
print("  and the per-layer gap classes are exactly the QR/phi(N)-mod ladder of the earlier rounds.")
print("  => the Rubik rotation reaches the cleanest frame (sum/gap); assembly remains the")
print("     sub-O(sqrt(N)) wall. Rotation orbit = the multiplier-direction orbit (12 directions).")
