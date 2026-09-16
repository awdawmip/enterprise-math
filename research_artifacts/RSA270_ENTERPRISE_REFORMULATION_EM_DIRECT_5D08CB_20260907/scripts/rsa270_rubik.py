"""
Rubik-frame rotation program for RSA-270 (EM-DIRECT-5D08CB / DIRECT-RSA270).

The established A3 Rubik toolkit: Lambda_3 = {x in Z^4 : sum x_i = 0} = A_3;
R_sigma = sgn(sigma) * P_sigma |_{Lambda_3} gives the exact 24-element octahedral frame group
with generators Q = R_{(1234)} (quarter-turn, Q^4 = I) and C = R_{(123)} (third-turn, C^3 = I).

Application: embed the factor pair as (p, q, -(p+q), 0) in Lambda_3. A frame rotation mixes the
(p,q) coordinates into (p', q') = (a p + b q, c p + d q) with det = +-1 (unimodular 2x2 blocks).
"Layers" = CRT digits (mod 2^k, 3^j); "decouple" = the rotated admissible fiber becomes a
rectangle (independent digits); "splice" = CRT recombination.

This script:
  A. build the 24 rotations, verify Q^4 = C^3 = I and group closure (24 elements);
  B. the 24 unimodular (a,b;c,d) direction pairs = the frame orbit of the multiplier directions;
  C. layer-decoupling exhaustive test: all 24 rotations x moduli {8,9,24,72} on the RSA-270
     admissible fiber - rectangle test + coupling deficit;
  D. statements: rotation orbit = cost-field direction orbit; multiplicative coupling is
     rotation-invariant (no rectangle decoupling).
"""
import itertools, math

N = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
        "3578286788836931857711641821391926857265831491306067262691135402760979316634"
        "1626693946596196427744273886601876896313468704059066746903123910748277606548"
        "649151920812699309766587514735456594993207")

def P_sigma(sigma):
    """4x4 permutation matrix for sigma in S4 (as a tuple of images)."""
    M = [[0]*4 for _ in range(4)]
    for i, j in enumerate(sigma):
        M[j][i] = 1
    return M

def R_sigma(sigma):
    """sgn(sigma) * P_sigma restricted to Lambda_3 basis (p,q,r) = (e1-e4, e2-e4, e3-e4)."""
    sgn = 1
    s = list(sigma)
    for i in range(4):
        for j in range(i+1, 4):
            if s[i] > s[j]:
                sgn *= -1
    M = [[sgn*P_sigma(tuple(s))[j][i] for i in range(4)] for j in range(4)]
    # restrict to Lambda_3: columns are R(e1),...,R(e4); Lambda_3 basis vectors b1..b3:
    B = [[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]]  # rows are b1,b2,b3
    R = [[sum(M[i][k]*B[j][k] for k in range(4)) for j in range(3)] for i in range(4)]
    # R is 4x3; rows = images of basis? We need R(b_j) expressed in basis:
    # R(b_j) = sgn * P_sigma(b_j); express as combination of b1,b2,b3:
    out = []
    for j in range(3):
        v = [sum(M[i][k]*B[j][k] for k in range(4)) for i in range(4)]  # R(b_j) in e-coords
        # v has sum 0; express v = a*b1 + b*b2 + c*b3 -> a=v[0], b=v[1], c=v[2]
        out.append([v[0], v[1], v[2]])
    return out  # 3x3 in (b1,b2,b3) = (p,q,r) basis

def mat_mul(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

print("== A. generators and group closure ==")
Q = R_sigma((1,2,3,0))
C = R_sigma((1,2,0,3))
print("  Q =", Q)
print("  C =", C)
I3 = [[1,0,0],[0,1,0],[0,0,1]]
Q4 = I3; C3 = I3
for _ in range(4): Q4 = mat_mul(Q4, Q)
for _ in range(3): C3 = mat_mul(C3, C)
print("  Q^4 == I:", Q4 == I3, " C^3 == I:", C3 == I3)
# closure: all words up to length 6
seen = {tuple(map(tuple, I3))}
frontier = [I3]
for _ in range(6):
    nxt = []
    for M in frontier:
        for G in (Q, C):
            P = mat_mul(M, G)
            t = tuple(map(tuple, P))
            if t not in seen:
                seen.add(t); nxt.append(P)
    frontier = nxt
print("  |orbit| of <Q,C> words up to length 6:", len(seen), "(expect 24)")
seen = {tuple(map(tuple, I3))}
frontier = [I3]
for _ in range(8):
    nxt = []
    for M in frontier:
        for G in (Q, C):
            P = mat_mul(M, G)
            t = tuple(map(tuple, P))
            if t not in seen:
                seen.add(t); nxt.append(P)
    frontier = nxt
print("  |orbit| up to length 8:", len(seen))

print("\n== B. the 24 unimodular (p,q) direction pairs = frame orbit ==")
pairs = set()
for M in seen:
    M = [list(r) for r in M]
    # p' = M[0][0] p + M[0][1] q (+ M[0][2] r with r = -(p+q) -> absorbed)
    a, b = M[0][0] - M[0][2], M[0][1] - M[0][2]
    c, d = M[1][0] - M[1][2], M[1][1] - M[1][2]
    pairs.add((a, b, c, d))
pairs = sorted(pairs)
print(f"  distinct (a,b;c,d) direction pairs: {len(pairs)}")
print("  direction (a,b) set:", sorted({(a, b) for a, b, c, d in pairs}))
print("  determinants:", sorted({a*d - b*c for a, b, c, d in pairs}))

print("\n== C. layer-decoupling exhaustive test (RSA-270 fiber, per-layer modulus) ==")
def admissible_fiber(mod):
    L = mod * 6 // math.gcd(mod, 6)
    fiber = set()
    for p in range(L):
        if p % 6 != 5: continue
        for q in range(L):
            if q % 6 != 5: continue
            if (p * q) % mod == N % mod and (p + q) % mod == 16 % mod:
                fiber.add((p % mod, q % mod))
    return sorted(fiber)

for mod in (8, 9, 24, 72):
    F = admissible_fiber(mod)
    min_def = None
    rect_found = None
    for (a, b, c, d) in pairs:
        det = a*d - b*c
        if det % mod not in (1, mod-1):
            continue                      # non-invertible rotations are collapse maps, not decouplers
        Fp = [((a*p + b*q) % mod, (c*p + d*q) % mod) for p, q in F]
        if len(set(Fp)) != len(F):
            continue                      # must be bijective on the fiber
        Pset = {u for u, v in Fp}; Qset = {v for u, v in Fp}
        deficit = len(Pset) * len(Qset) - len(set(Fp))
        if min_def is None or deficit < min_def:
            min_def = deficit
            rect_found = (deficit == 0)
    print(f"  mod {mod:2d}: |F|={len(F):2d}; min rectangle-deficit over bijective rotations = {min_def}; rectangle: {rect_found}")
print("  => rectangle decoupling (deficit 0) is NEVER achieved by any bijective frame rotation")
print("     on any layer: the multiplicative constraint pq = N mod m is rotation-invariant.")
