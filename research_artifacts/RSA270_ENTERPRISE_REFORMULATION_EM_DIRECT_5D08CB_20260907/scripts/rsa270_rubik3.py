"""
Rubik splice demonstration (EM-DIRECT-5D08CB / DIRECT-RSA270): after the sum/difference
decoupling, splice the gap digits and attempt to assemble the composite N's low digits.

Splice = the Fermat identity (S+g)(S-g) = 4N in the sum/gap frame:
  N = (S^2 - g^2)/4.  With S = 16 mod 72 (forced) and g mod 72 in 6 classes:
  6 candidate reconstructions of N mod 1296; the true N mod 1296 must be among them.
Layer-144 splice check: g^2 = S^2 - 4N mod 144  =>  g0^2 = 256 - 4N mod 144 (N-only).
Splice tower: for larger M, the (S,g) candidates = the admissible classes at level M;
the relation is exactly the fiber constraint -> no refinement beyond the class data.
"""
import math

N = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
        "3578286788836931857711641821391926857265831491306067262691135402760979316634"
        "1626693946596196427744273886601876896313468704059066746903123910748277606548"
        "649151920812699309766587514735456594993207")

def fiber(mod):
    L = math.lcm(6, math.lcm(mod, 72))
    out = set()
    for p in range(L):
        if p % 6 != 5: continue
        for q in range(L):
            if q % 6 != 5: continue
            if (p * q) % L == N % L and (p + q) % 72 == 16:
                out.add((p % mod, q % mod))
    return sorted(out)

print("== A. splice at certificate scale (mod 1296, full (S,g) class data) ==")
F72 = fiber(72)
gaps = sorted({(p - q) % 72 for p, q in F72})
print(f"  gap classes mod 72: {gaps} ({len(gaps)})")
Fm = fiber(1296)
SG = sorted({((p + q) % 1296, (p - q) % 1296) for p, q in Fm})
cands = {(((S * S - g * g) // 4) % 1296) for S, g in SG}
print(f"  |(S,g) mod 1296 pairs| = {len(SG)} ; distinct N mod 1296 reconstructions = {len(cands)}")
print(f"  true N mod 1296 = {N % 1296} -> in candidates: {N % 1296 in cands}")
print("  (earlier 6-candidate construction was flawed: S mod 1296 contributes beyond S mod 72)")

print("\n== B. layer-144 splice check (N-only constraint) ==")
rhs = (256 - 4 * N) % 144
ok = all((g0 * g0) % 144 == rhs for g0 in gaps)
print(f"  g0^2 = 256 - 4N mod 144 = {rhs} ; all 6 gap classes satisfy: {ok}")
print("  => the splice constraint is automatically satisfied by the admissible classes")
print("     (the Fermat identity IS the fiber constraint; no extra refinement).")

print("\n== C. splice tower ==")
for M in (144, 216, 432, 1296):
    Fm = fiber(M)
    SG = {( (p+q) % M, (p-q) % M) for p, q in Fm}
    # check: every (S,g) pair satisfies g^2 = S^2 - 4N mod M (Fermat splice)
    viol = sum(1 for S, g in SG if (g * g - S * S + 4 * N) % M != 0)
    print(f"  M={M:4d}: |(S,g) pairs|={len(SG)}  splice violations={viol}")
print("  => splice = the fiber; assembling the composite's digits works exactly at every level,")
print("     but the digit content beyond the 72-lattice is the class ambiguity (the wall).")
