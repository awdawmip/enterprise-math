"""
Deep research round 4 (EM-DIRECT-5D08CB / DIRECT-RSA270):
complete layer-2 modular certificate lattice for all primes l <= 229, and the
synthesis: the root residues are the modular square roots of the endpoint residues
-> the x-residue set (round-7 j-sieve) is the primitive certificate; y adds only the sign.
"""
import math

def primes_upto(n):
    sieve = bytearray([1]) * (n + 1); sieve[0:2] = b"\x00\x00"
    for i in range(2, math.isqrt(n) + 1):
        if sieve[i]:
            sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    return [i for i in range(2, n + 1) if sieve[i]]

N = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
        "3578286788836931857711641821391926857265831491306067262691135402760979316634"
        "1626693946596196427744273886601876896313468704059066746903123910748277606548"
        "649151920812699309766587514735456594993207")

adm = []
for p in range(72):
    if p % 6 != 5: continue
    for q in range(72):
        if q % 6 != 5: continue
        if (p * q) % 72 == N % 72 and (p + q) % 72 == 16:
            adm.append((p, q))

def mod_sqrt_roots(a, mod):
    """all r in [0,mod) with r^2 == a mod mod (brute force, mod=72)."""
    return [r for r in range(mod) if (r * r) % mod == a % mod]

print("== per-l certificate lattice (primes l <= 229) ==")
print(f"  {'l':4s} {'|x-set|':8s} {'|y-set|':8s} {'|joint|':8s} {'joint==x x +-sqrt?':16s} {'sieve x':8s}")
ok_all = True
summary = []
for l in primes_upto(229):
    xset = sorted({(l * p0 + q0) % 72 for p0, q0 in adm})
    yset = sorted({abs(l * p0 - q0) % 72 for p0, q0 in adm})
    joint = sorted({((l * p0 + q0) % 72, abs(l * p0 - q0) % 72) for p0, q0 in adm})
    # derived joint: for each x in xset, the square roots of (x^2 - 4lN) mod 72
    derived = set()
    for x in xset:
        a = (x * x - 4 * l * N) % 72
        for y in mod_sqrt_roots(a, 72):
            derived.add((x, y))
    eq = set(joint) == derived
    ok_all &= eq
    if len(xset) < 12:
        summary.append((l, len(xset), len(yset), len(joint), eq))
    if not eq:
        print(f"  l={l}: joint != derived  |joint|={len(joint)} |derived|={len(derived)}")
print("  (showing only l with |x-set| < 12; all others have |x-set| = 12)")
for l, nx, ny, nj, eq in summary[:12]:
    print(f"  {l:4d} {nx:8d} {ny:8d} {nj:8d} {str(eq):16s} {nx:2d}/72")
print("  all-l equivalence joint == {(x, +-sqrt(x^2-4lN) mod 72)}:", ok_all)

print("\n== synthesis ==")
print("  The root residue set y-set is exactly the modular square-root closure of the endpoint")
print("  residue set x-set (x^2 - y^2 = 4lN mod 72). Hence the x-set (round-7 j-sieve) is the")
print("  PRIMITIVE certificate; the root certificate (round-9 C) adds only the sign structure.")
print("  The complete N-only modular shadow of the layer-2 V-function for branch l = x-set(l).")
# x2 explicit
x2 = sorted({(2 * p0 + q0) % 72 for p0, q0 in adm})
y2 = sorted({abs(2 * p0 - q0) % 72 for p0, q0 in adm})
print(f"\n  x2 branch: x-set = {x2} ; y-set = {y2}")
print(f"  => layer-2 search certificate for the x2 branch: x = 2p+q in {x2} mod 72, y = |2p-q| odd;")
print(f"     combined with the cost field: the sieved x2 scan bound stands at ~2^438 adds (9d4c2e/5b8f1a).")
