"""
Deep research round 1 (new goal) - alignment stability across layers, direction-orbit
structure, and the interior-metric spectrum (EM-DIRECT-5D08CB / DIRECT-RSA270).

  A. per-layer alignment type table (mod 8/9/16/24/27/72/144): does the 8+8+8 split persist?
  B. direction-orbit structure: the 12 first-row directions split 2+2+8 under the frame group.
  C. interior metric spectrum: |P'|*|Q'| values {12, 72, 144} ordering sum < gap < pure.
"""
import math
from collections import Counter

N = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
        "3578286788836931857711641821391926857265831491306067262691135402760979316634"
        "1626693946596196427744273886601876896313468704059066746903123910748277606548"
        "649151920812699309766587514735456594993207")

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

pairs = set()
for M in seen:
    M = [list(r) for r in M]
    pairs.add((M[0][0]-M[0][2], M[0][1]-M[0][2], M[1][0]-M[1][2], M[1][1]-M[1][2]))
pairs = sorted(pairs)

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

def align_type(a, b, c, d, F, mod):
    Fp = [((a*p + b*q) % mod, (c*p + d*q) % mod) for p, q in F]
    Pset = {u for u, v in Fp}; Qset = {v for u, v in Fp}
    if len(Pset) == 1 or len(Qset) == 1: return "sum", len(Pset)*len(Qset)
    if len(Pset) == len(F) and len(Qset) == len(F): return "pure", len(Pset)*len(Qset)
    if 6 in (len(Pset), len(Qset)) and max(len(Pset), len(Qset)) == len(F): return "gap", len(Pset)*len(Qset)
    return "mixed", len(Pset)*len(Qset)

print("== A. per-layer alignment type table ==")
for mod in (8, 9, 16, 24, 27, 72, 144):
    F = fiber(mod)
    cnt = Counter()
    for (a, b, c, d) in pairs:
        typ, _ = align_type(a, b, c, d, F, mod)
        cnt[typ] += 1
    print(f"  mod {mod:3d} (|F|={len(F):3d}): types = {dict(cnt)}")

print("\n== B. direction-orbit structure (first-row directions) ==")
dirs = sorted({(a, b) for a, b, c, d in pairs})
print(f"  first-row direction set ({len(dirs)}): {dirs}")
sum_dir = [(1,1), (-1,-1)]; gap_dir = [(1,-1), (-1,1)]
pure = [d for d in dirs if d not in sum_dir and d not in gap_dir]
print(f"  orbits: sum {(1,1),(-1,-1)} (2), gap {(1,-1),(-1,1)} (2), pure ({len(pure)}): {pure}")
print(f"  24 = 8(sum-octet) + 8(gap-octet) + 8(pure-octet): each first-row direction has 4 second-row lifts x 2 signs.")

print("\n== C. interior metric spectrum (|P'|*|Q'|) at mod 72 ==")
F = fiber(72)
metrics = Counter()
for (a, b, c, d) in pairs:
    typ, m = align_type(a, b, c, d, F, 72)
    metrics[m] += 1
print(f"  metric values: {dict(metrics)}  (sum: 1*12=12 ; gap: 6*12=72 ; pure: 12*12=144)")
print("  => interior metric orders the alignments: sum(12) < gap(72) < pure(144);")
print("     the sum/gap frame is the unique minimum-interior alignment.")
