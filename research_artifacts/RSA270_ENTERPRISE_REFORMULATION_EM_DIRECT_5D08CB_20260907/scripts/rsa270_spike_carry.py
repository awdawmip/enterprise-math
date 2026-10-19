"""
RSA-270 shortcut hunt round 3 (EM-DIRECT-5D08CB / DIRECT-RSA270):
discrete-derivative concentration, BRC carry automaton, native-coordinate spike reading.

Discrete philosophy: P(u) is {0,2,4}-valued on a step-2 lattice; its discrete derivative
  dP(e) = P(e) - P(e-2)  =  +2*(delta_{e=+A} + delta_{e=-A})  - 2*(delta_{e=+(N+1)/2} + delta_{e=-(N+1)/2})
  with A = S/2 = Fermat midpoint (enterprise native axis-difference reading).
  => the two positive spikes (unknown position +-A) carry all factor information;
     the two negative spikes (+-(N+1)/2) are N-only computable.
  => factoring <=> locating the positive spike pair of dP.

BRC: the 2-adic/3-adic towers are the carry automaton of N + (S+1) = sigma(N):
  states = carries; branches = digit pairs; collapse = carry quotient; doubling = information loss.
"""
import math

RSA270 = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
             "3578286788836931857711641821391926857265831491306067262691135402760979316634"
             "1626693946596196427744273886601876896313468704059066746903123910748277606548"
             "649151920812699309766587514735456594993207")
N = RSA270

def profile_poly(Nn, p, q):
    S = p + q
    P = {}
    for s, m in [((Nn + 3)//2, 2), ((S + 2)//2, 2)]:
        for j in range(s - 1):
            e = 2 - s + 2*j
            P[e] = P.get(e, 0) + m
    return P

print("== 1. discrete-derivative spike theorem (synthetic verification) ==")
ok = True
for (Nn, p, q) in [(35, 5, 7), (143, 11, 13), (391, 17, 23), (899, 29, 31), (3599, 59, 61)]:
    S = p + q
    P = profile_poly(Nn, p, q)
    emin, emax = min(P), max(P)
    spikes = {}
    for e in range(emin, emax + 3, 2):
        d = P.get(e, 0) - P.get(e - 2, 0)
        if d != 0:
            spikes[e] = d
    expected = {-(S - 2)//2: +2, (S + 2)//2: -2, -(Nn - 1)//2: +2, (Nn + 3)//2: -2}
    if spikes != expected:
        ok = False
        print(f"  N={Nn}: spikes={spikes} expected={expected}")
print("  spike theorem:", "PASS (5 semiprimes)" if ok else "FAIL")

print("\n== 2. RSA-270 spike positions (native coordinate reading) ==")
print("  factor spike pair: e* = +-A, A = S/2,  S = 16 mod 72 -> A = 8 mod 36")
print("  N-only spike pair : e = +-(N+1)/2 = +-", (N + 1)//2)

print("\n== 3. BRC carry automaton (addition N + (S+1) = sigma(N)) ==")
print("  2-adic pair/sum tower (unconditional; N mod 8 = 7):")
for k in range(1, 9):
    mod = 1 << k
    pairs = []
    for a in range(1, mod, 2):
        for b in range(1, mod, 2):
            if (a * b) % mod == N % mod:
                pairs.append((a, b))
    sums = sorted({(a + b) % mod for a, b in pairs})
    print(f"    k={k}: pair-classes={len(pairs):3d}  S-classes={sums}  (count={len(sums)})")
print("  3-adic pair/sum tower (prior p,q==2 mod 3; N mod 9 = 1):")
for j in range(1, 5):
    mod = 3 ** j
    pairs = []
    for a in range(mod):
        if a % 3 != 2: continue
        for b in range(mod):
            if b % 3 != 2: continue
            if (a * b) % mod == N % mod:
                pairs.append((a, b))
    sums = sorted({(a + b) % mod for a, b in pairs})
    print(f"    j={j}: pair-classes={len(pairs):3d}  S-classes={sums}  (count={len(sums)})")

print("\n== 4. forced lattice recap (this round's synthesis input) ==")
print("  unconditional: S = 0 mod 8 ;  prior: S = 16 mod 72 (maximal forced modulus 72 = 2^3*3^2)")
print("  spike position A = S/2 = 8 mod 36 ;  the unknown is the single scalar S (equivalently A)")
