"""
BRC multiplier-ordering benchmark (EM-DIRECT-5D08CB / DIRECT-RSA270):
N-only direction-prior ordering vs mechanical order vs ridge-distance order,
with RSA-270 as the target.

Orderings over m = 1..100 (direction = the coprime factor pair of the squarefree kernel):
  mechanical: 1,2,...,100
  direction-prior: band directions first (a/b in [1.765, 2.266], ab <= 100) sorted by
    band-max cost coefficient c (cost-field minimax table, journal 5b8f1a), each followed
    by its square-scalings s^2 * k; then the remaining m by ridge distance.
  ridge-distance: all m sorted by |a/b - 2.0| (band midpoint).

Hit metric: rank of the first m whose direction ratio a/b is within eps of the true q/p.
Benchmark: synthetic prior-consistent semiprimes with q/p sampled across the band;
mean/median hit position per ordering; RSA-270: the ordered lists + expected rank of the
first band direction under the band-uniform prior.
"""
import math, random
from math import gcd, isqrt

def coprime_pairs(k):
    """all coprime factor pairs (a,b), a>=b, a*b=k."""
    out = []
    for d in range(1, isqrt(k) + 1):
        if k % d == 0:
            a, b = k // d, d
            if gcd(a, b) == 1:
                out.append((a, b))
    return out

def directions(k):
    return coprime_pairs(k)

BAND = (1.765, 2.266)
def band_k(mmax=100):
    """k whose direction SET contains a ratio in the band; the best such direction."""
    out = []
    for k in range(1, mmax + 1):
        best = None
        for (a, b) in coprime_pairs(k):
            r = a / b
            if BAND[0] <= r <= BAND[1]:
                c = band_max_c(a, b) if (a, b) != (2, 1) else band_max_c(a, b)
                if best is None or c < best[1]:
                    best = ((a, b), c)
        if best is not None:
            out.append((k, best[0], best[1]))
    return out

def c_of(a, b, r):
    return (math.sqrt(a) - math.sqrt(b * r)) ** 2

# band-max coefficient per direction (from the cost-field table, 5b8f1a)
def band_max_c(a, b):
    return max(c_of(a, b, r) for r in (1.765, 1.8, 1.9, 2.0, 2.1, 2.2, 2.266))

# 1) mechanical
mech = list(range(1, 101))

# 2) direction-prior: band-k first (sorted by their best band direction's band-max c),
#    then non-band k by ridge distance of their best direction
band_k_list = band_k(100)
band_k_sorted = sorted(band_k_list, key=lambda t: t[2])
dprior = [k for k, ab, c in band_k_sorted]
used = set(dprior)
nonband = [k for k in range(1, 101) if k not in used]
def ridge_key(k):
    ds = coprime_pairs(k)
    return min(abs(a / b - 2.0) for a, b in ds)
nonband.sort(key=ridge_key)
dprior += nonband

# 3) ridge-distance
ridge = sorted(range(1, 101), key=ridge_key)

print("== ordered lists ==")
print("direction-prior first 30:", dprior[:30])
print("ridge-distance first 15:", ridge[:15])

print("\n== RSA-270 target analysis (prior band) ==")
print("band k <= 100 with their best band direction (a,b) and band-max c:")
for (k, (a, b), c) in band_k_sorted:
    print(f"  k={k:3d}  direction ({a},{b})  ratio {a/b:.4f}  band-max c = {c:.4f}")
print("mechanical positions of band-k:", sorted(k for k, ab, c in band_k_list))
print("direction-prior positions of band-k:", [i + 1 for i, k in enumerate(dprior) if k in {t[0] for t in band_k_list}])

print("\n== benchmark: hit position (synthetic band-consistent semiprimes) ==")
def is_prime_mr(n, rounds=15):
    if n < 2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % p == 0: return n == p
    d = n-1; r = 0
    while d % 2 == 0: d//=2; r+=1
    rng = random.Random(20260907)
    for _ in range(rounds):
        a = rng.randrange(2, n-2)
        x = pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(r-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True

def hit_position(order, r_true, eps=0.10):
    for i, k in enumerate(order):
        for (a, b) in coprime_pairs(k):
            if abs(a / b - r_true) <= eps:
                return i + 1
    return len(order)

rng = random.Random(7)
res_mech, res_dprior, res_ridge = [], [], []
for t in range(200):
    r = rng.uniform(BAND[0], BAND[1])
    # generate p,q ~ 2^20 with ratio r and prior residues
    while True:
        p = rng.randrange(1 << 19, 1 << 20) | 1
        q = rng.randrange(int(p * r * 0.97), int(p * r * 1.03)) | 1
        if p % 6 == 5 and q % 6 == 5 and p != q and is_prime_mr(p) and is_prime_mr(q):
            break
    rt = q / p
    res_mech.append(hit_position(mech, rt))
    res_dprior.append(hit_position(dprior, rt))
    res_ridge.append(hit_position(ridge, rt))
print(f"  mechanical   : mean {sum(res_mech)/len(res_mech):.1f}  median {sorted(res_mech)[len(res_mech)//2]}")
print(f"  direction-prior: mean {sum(res_dprior)/len(res_dprior):.1f}  median {sorted(res_dprior)[len(res_dprior)//2]}")
print(f"  ridge-distance: mean {sum(res_ridge)/len(res_ridge):.1f}  median {sorted(res_ridge)[len(res_ridge)//2]}")
print("  (eps = 0.10 direction-ratio tolerance; hit = first multiplier within eps of the true ratio)")

# CSV output
import csv, os
csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "research_artifacts", "brc_multiplier_ordering_benchmark_20260907.csv")
with open(csv_path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["sample", "mechanical_hit", "direction_prior_hit", "ridge_distance_hit"])
    for t, (a, b, c) in enumerate(zip(res_mech, res_dprior, res_ridge), 1):
        w.writerow([t, a, b, c])
print("CSV written: research_artifacts/brc_multiplier_ordering_benchmark_20260907.csv")
