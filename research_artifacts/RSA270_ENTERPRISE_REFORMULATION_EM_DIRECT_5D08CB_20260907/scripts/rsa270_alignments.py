"""
Alignment study (EM-DIRECT-5D08CB / DIRECT-RSA270): the 24 Rubik frame alignments and
their effects on the interior (the transformed fiber structure at each layer).

For each rotation (a,b;c,d): transformed coordinates (p', q') = (a p + b q, c p + d q).
Measure per layer m: |P'|, |Q'| (coordinate class counts) -> alignment type:
  sum-type   : one coordinate constant (|P'|=1 or |Q'|=1)  -> forced linear form revealed
  gap-type   : one coordinate has 6 classes (the gap axis)
  pure-type  : both 12 classes (no decoupling)
  mixed-type : other splits
Classify all 24 at mod 72; check the classification is N-independent (RSA-260).
"""
import math, itertools

N270 = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
           "3578286788836931857711641821391926857265831491306067262691135402760979316634"
           "1626693946596196427744273886601876896313468704059066746903123910748277606548"
           "649151920812699309766587514735456594993207")
N260 = int("2211282552952966643528108525502623092761208950247001539441374831912882294140"
           "2001986512729726569746599085900330031400051170742204560859276357953757185954"
           "2988389587092292384910067030341246205457845664136645406842143612930176940208"
           "46391065875914794251435144458199")

def R_sigma(sigma):
    sgn = 1; s = list(sigma)
    for i in range(4):
        for j in range(i+1, 4):
            if s[i] > s[j]: sgn *= -1
    M = [[0]*4 for _ in range(4)]
    for i, j in enumerate(sigma):
        M[j][i] = sgn
    B = [[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]]
    out = []
    for j in range(3):
        v = [sum(M[i][k]*B[j][k] for k in range(4)) for i in range(4)]
        out.append([v[0], v[1], v[2]])
    return out

def mat_mul(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

I3 = [[1,0,0],[0,1,0],[0,0,1]]
Q = R_sigma((1,2,3,0)); C = R_sigma((1,2,0,3))
seen = {tuple(map(tuple, I3))}; frontier = [I3]
for _ in range(8):
    nxt = []
    for M in frontier:
        for G in (Q, C):
            P = mat_mul(M, G)
            t = tuple(map(tuple, P))
            if t not in seen:
                seen.add(t); nxt.append(P)
    frontier = nxt

def pairs_of(seen):
    out = set()
    for M in seen:
        M = [list(r) for r in M]
        a, b = M[0][0] - M[0][2], M[0][1] - M[0][2]
        c, d = M[1][0] - M[1][2], M[1][1] - M[1][2]
        out.add((a, b, c, d))
    return sorted(out)

def fiber(Nn, S72, mod):
    L = math.lcm(6, math.lcm(mod, 72))
    out = set()
    for p in range(L):
        if p % 6 != 5: continue
        for q in range(L):
            if q % 6 != 5: continue
            if (p * q) % L == Nn % L and (p + q) % 72 == S72:
                out.add((p % mod, q % mod))
    return sorted(out)

pairs = pairs_of(seen)
print(f"== alignment classification at mod 72 (RSA-270, S=16 mod 72) ==")
print(f"  {'(a,b;c,d)':22s} {'|P|':4s} {'|Q|':4s} {'type':16s} {'forced form'}")
types = {}
for (a, b, c, d) in pairs:
    F = fiber(N270, 16, 72)
    Fp = [((a*p + b*q) % 72, (c*p + d*q) % 72) for p, q in F]
    Pset = {u for u, v in Fp}; Qset = {v for u, v in Fp}
    if len(Pset) == 1: typ, form = "sum-type", f"p' = {a}p{b:+d}q = {list(Pset)[0]} (forced)"
    elif len(Qset) == 1: typ, form = "sum-type", f"q' = {c}p{d:+d}q = {list(Qset)[0]} (forced)"
    elif len(Pset) == 6: typ, form = "gap-type", f"p' = gap axis ({len(Pset)} classes)"
    elif len(Qset) == 6: typ, form = "gap-type", f"q' = gap axis ({len(Qset)} classes)"
    elif len(Pset) == 12 and len(Qset) == 12: typ, form = "pure-type", "no decoupling"
    else: typ, form = "mixed-type", f"split {len(Pset)}/{len(Qset)}"
    types[(a, b, c, d)] = typ
    print(f"  ({a:2d},{b:2d};{c:2d},{d:2d})       {len(Pset):4d} {len(Qset):4d} {typ:16s} {form}")
from collections import Counter
print("\n  type counts at mod 72:", dict(Counter(types.values())))

print("\n== N-independence check (RSA-260, S=40 mod 72) ==")
types260 = {}
for (a, b, c, d) in pairs:
    F = fiber(N260, 40, 72)
    Fp = [((a*p + b*q) % 72, (c*p + d*q) % 72) for p, q in F]
    Pset = {u for u, v in Fp}; Qset = {v for u, v in Fp}
    if len(Pset) == 1 or len(Qset) == 1: typ = "sum-type"
    elif 6 in (len(Pset), len(Qset)): typ = "gap-type"
    elif len(Pset) == 12 and len(Qset) == 12: typ = "pure-type"
    else: typ = "mixed-type"
    types260[(a, b, c, d)] = typ
print("  type counts (RSA-260):", dict(Counter(types260.values())))
same = all(types[k] == types260[k] for k in types)
print("  classification identical across N (type structure N-independent):", same)
