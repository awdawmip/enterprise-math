"""
Deep research round 2 (EM-DIRECT-5D08CB / DIRECT-RSA270):
full layer x alignment interior atlas + layer-optimal alignment + information accounting.
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

print("== interior atlas: per-layer metric distribution and layer-optimal alignment ==")
print(f"  {'mod':5s} {'|F|':5s} {'log2|F|':8s} {'min metric':10s} {'achiever':10s} {'min residual':12s} {'log2(res)':9s}")
for mod in (8, 9, 16, 24, 27, 72, 144, 216, 432):
    F = fiber(mod)
    best = None
    for (a, b, c, d) in pairs:
        Fp = [((a*p + b*q) % mod, (c*p + d*q) % mod) for p, q in F]
        Pset = {u for u, v in Fp}; Qset = {v for u, v in Fp}
        m = len(Pset) * len(Qset)
        resid = min(len(Pset), len(Qset))
        if best is None or (m, resid) < best[0]:
            best = ((m, resid), (a, b, c, d), resid)
    (m, resid), ach, r = best
    print(f"  {mod:5d} {len(F):5d} {math.log2(len(F)):8.2f} {m:10d} ({ach[0]:2d},{ach[1]:2d}) {resid:12d} {math.log2(resid) if resid>1 else 0.0:9.2f}")

print("\n== information accounting ==")
print("  72-divisor layers: mod 8 -> gap 2 classes (1 bit) ; mod 9 -> gap 3 classes (1.58 bits)")
print("  combined gap mod 72 = 6 classes = log2(6) = 2.58 bits (CRT-consistent)")
print("  forced sum = S = 16 mod 72 -> 6.17 bits total lattice; the residual ambiguity inside the")
print("  lattice is exactly the gap axis (2.58 bits), the rest (3.58 bits) is the forced sum.")
print("  => the alignment atlas quantifies the interior: sum-coordinate carries the forcing,")
print("     gap-coordinate carries the residual; the best alignment per layer achieves min residual.")
