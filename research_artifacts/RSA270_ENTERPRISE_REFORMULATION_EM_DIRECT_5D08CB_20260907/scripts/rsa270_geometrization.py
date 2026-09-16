"""
Direction 2 (EM-DIRECT-5D08CB / DIRECT-RSA270): geometrize primes/semiprimes.

  Silhouette: profile P(u) = sum_{d|N} W_{(d+N/d+2)/2}(u)  (axis-difference silhouette).
    prime p     -> divisors {1,p} -> ONE plateau  (width p, boundary (p-1)/2)
    semiprime pq -> divisors {1,N,p,q} -> TWO plateaus (outer (N-1)/2, inner (S-2)/2)
  Counts (four-layer/X6, native):  sigma(p) = p+1 ;  sigma(pq) = N+S+1.
  External-Euclidean picture (honest label): (x,y) = (sqrt p, sqrt q) lies on the KNOWN
    hyperbola xy = sqrt(N) and the UNKNOWN circle x^2+y^2 = S; factorization = locating the
    point among the finite set defined by primality. The Fermat offset = (x-y)^2/2 + rounding.
  Native reading: the multiplier lattice (a,b) carries the BRC add-cost field
    g(a,b) = sqrt(abpq)*(x+1/x-2), x = sqrt(ap/(bq))  [Direction 1]; its ridge a/b = q/p
    is the factor direction; the cost field is the discrete geometric encoding of (p,q).
"""
import math

def W_support(s):
    return (2 - s, s - 2)   # min and max exponents (both inclusive), step 2

print("== A. silhouette classification (plateau boundaries) ==")
for (Nn, label) in [(13, "prime 13"), (17, "prime 17"), (143, "semiprime 11*13"), (899, "semiprime 29*31")]:
    divs = [d for d in range(1, math.isqrt(Nn) + 1) if Nn % d == 0]
    divs = sorted(set(divs + [Nn // d for d in divs]))
    plats = []
    for d in divs:
        s = (d + Nn // d + 2) // 2
        lo, hi = W_support(s)
        plats.append((lo, hi))
    outer = max(hi for lo, hi in plats)
    inner_list = [hi for lo, hi in plats if hi < outer]
    inner = max(inner_list) if inner_list else None
    print(f"  {label:16s}: divisors={divs} -> outer boundary={outer}, inner boundary={inner}"
          + ("" if inner is not None else "  [SINGLE plateau = prime signature]"))

print("\n== B. four-layer count identity (direct enumeration, small N) ==")
def T_(x): return x * (x + 1) // 2
def four_layer_count(Nn):
    m = (Nn - 1) // 2
    cnt = 0
    amax = int((math.isqrt(8 * m + 1) - 1) // 2)
    for a in range(amax + 1):
        r1 = m - T_(a)
        if r1 < 0: break
        for b in range(int((math.isqrt(8 * r1 + 1) - 1) // 2) + 1):
            r2 = r1 - T_(b)
            if r2 < 0: break
            for c in range(int((math.isqrt(8 * r2 + 1) - 1) // 2) + 1):
                r3 = r2 - T_(c)
                if r3 < 0: break
                disc = 8 * r3 + 1
                s = math.isqrt(disc)
                if s * s == disc and (s - 1) % 2 == 0:
                    cnt += 1
    return cnt
for (Nn, sigma_expected) in [(13, 14), (15, 24), (143, 168), (391, 432)]:
    c = four_layer_count(Nn)
    print(f"  N={Nn:3d}: four-layer count={c:3d}  sigma(N)={sigma_expected}  match={c == sigma_expected}")

print("\n== C. geometrization statements ==")
print("  C1 (external Euclidean): (sqrt p, sqrt q) = intersection of known hyperbola xy=sqrt(N)")
print("      with unknown circle x^2+y^2=S;  Fermat offset T ~ (x-y)^2/2.")
print("  C2 (native): profile = axis-difference silhouette; plateau count = #nontrivial divisor pairs;")
print("      inner boundary (S-2)/2 = the Fermat midpoint coordinate.")
print("  C3 (BRC cost field, Direction 1): multiplier lattice field g(a,b) with ridge a/b=q/p;")
print("      the 64-branch rho_k tree of the original experiment = first-step samples of this field;")
print("      the k=20 valley is provably off-ridge (endpoint cost exceeds Fermat's across the band).")
print("  C4: primality as support count: C_X(p) = p+1 (one window), C_X(pq) = N+S+1 (two windows);")
print("      the second window is exactly the factor signal; its width = S.")
