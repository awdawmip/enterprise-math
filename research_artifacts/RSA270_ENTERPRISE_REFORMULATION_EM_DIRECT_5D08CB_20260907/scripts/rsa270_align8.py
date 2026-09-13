"""
Deep research round 7 (EM-DIRECT-5D08CB / DIRECT-RSA270):
affine-rank classification of the transformed fiber under each alignment (the interior
geometry of the fiber), + alignment-program consolidation record.
"""
import math

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

F = [(p, q) for p in range(72) if p % 6 == 5 for q in range(72) if q % 6 == 5
     and (p * q) % 72 == N % 72 and (p + q) % 72 == 16]
print(f"fiber (integer lifts): {F}")

def affine_rank(pts):
    if len(pts) <= 1: return 0
    v0 = pts[0]
    vecs = [[x - v0[0], y - v0[1]] for x, y in pts[1:]]
    # rank via determinant of the 2D vector span
    max_rank = 0
    for v in vecs:
        if v[0] != 0 or v[1] != 0:
            max_rank = max(max_rank, 1)
    for i in range(len(vecs)):
        for j in range(i+1, len(vecs)):
            if vecs[i][0]*vecs[j][1] - vecs[i][1]*vecs[j][0] != 0:
                return 2
    return max_rank

print("\naffine rank of the transformed fiber per alignment (integer lifts):")
from collections import Counter
ranks = Counter()
for (a, b, c, d) in pairs:
    pts = [(a*p + b*q, c*p + d*q) for p, q in F]
    r = affine_rank(pts)
    ranks[r] += 1
    Pset = {u % 72 for u, v in pts}      # residue-level coordinate classes (correct type basis)
    typ = "sum" if len(Pset) == 1 else ("gap" if len(Pset) == 6 else "pure")
    print(f"  ({a:2d},{b:2d};{c:2d},{d:2d}): rank={r}  type={typ}")
print(f"\ninteger affine-rank distribution: {dict(ranks)}")
print("=> geometric/modular dichotomy: the integer-lift fiber is affine rank 2 under EVERY alignment;")
print("   the sum-type 'line collapse' exists only at the RESIDUE level (p' = 16 mod 72 is a modular")
print("   line, since the integer lifts carry S in {16, 88}); the decoupling is a modular phenomenon,")
print("   not a geometric one. The type classification is the modular-rank classification.")
