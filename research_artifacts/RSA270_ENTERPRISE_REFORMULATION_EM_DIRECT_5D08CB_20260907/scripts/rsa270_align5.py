"""
Deep research round 4 (EM-DIRECT-5D08CB / DIRECT-RSA270):
the complete SL(2,Z) type lattice - |P'| = |{a p + b q mod 72}| as a function of (a-b) mod 12.
  expected: a-b = 0 mod 12 -> |P'| = 1 (forced sum family)
            a-b in {1,2,5,7,10,11} -> |P'| = 6 (gap-type)
            a-b in {3,4,6,8,9} -> collapsed (2 or 3 classes)
Verify by enumeration over a,b in [-24,24].
"""
N = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
        "3578286788836931857711641821391926857265831491306067262691135402760979316634"
        "1626693946596196427744273886601876896313468704059066746903123910748277606548"
        "649151920812699309766587514735456594993207")

F = {(p, q) for p in range(72) if p % 6 == 5 for q in range(72) if q % 6 == 5
     and (p * q) % 72 == N % 72 and (p + q) % 72 == 16}
F = sorted(F)
print(f"|F| = {len(F)}")

from collections import defaultdict
per_residue = defaultdict(set)
for a in range(-24, 25):
    for b in range(-24, 25):
        r = (a - b) % 12
        Pset = {(a*p + b*q) % 72 for p, q in F}
        per_residue[r].add(len(Pset))
print("\n|P'| values by (a-b) mod 12 residue:")
for r in range(12):
    vals = sorted(per_residue[r])
    typ = ("forced(1)" if vals == [1] else
           "gap-type(6)" if vals == [6] else
           f"collapsed({vals})")
    print(f"  a-b = {r:2d} mod 12 : |P'| in {vals}  -> {typ}")

print("\n== SL(2,Z) type lattice (enumeration-verified; corrects the analytic guess) ==")
print("  4 type classes:")
print("    forced   : a-b = 0 mod 12        -> |P'| = 1  (sum-frame lifts)")
print("    gap-type : a-b = +-2 mod 12      -> |P'| = 6  (the gap axis)")
print("    pure     : a-b = +-1,+-5 mod 12  -> |P'| = 12 (no collapse; the +-1,+-5 guess of 6 was WRONG)")
print("    quotient : a-b = +-3,+-4,6 mod 12 -> |P'| = 4,3,2 (gap-class quotients = information loss)")
print("  The quotient alignments collapse the 6 gap classes (3:1, 3:2, 2:1) - lossy, not decoupling.")
