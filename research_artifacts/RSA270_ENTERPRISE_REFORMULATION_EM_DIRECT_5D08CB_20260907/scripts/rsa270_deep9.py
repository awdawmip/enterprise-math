"""
Deep research round 9 (EM-DIRECT-5D08CB / DIRECT-RSA270):
  A. parity certificate: x = y (mod 2) always (from x^2 - y^2 = 4 l N = 0 mod 4);
     y(l) odd iff l = 2; y even for odd l; x even for odd l, x odd for l = 2.
  B. complete certificate-suite integration test on RSA-260 (all entries at once).
"""
import math, random

def primes_upto(n):
    sieve = bytearray([1]) * (n + 1); sieve[0:2] = b"\x00\x00"
    for i in range(2, math.isqrt(n) + 1):
        if sieve[i]:
            sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    return [i for i in range(2, n + 1) if sieve[i]]

def is_probable_prime(n, rounds=20):
    if n < 2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % p == 0: return n == p
    d = n-1; r = 0
    while d % 2 == 0: d//=2; r+=1
    rng = random.Random(20260906)
    for _ in range(rounds):
        a = rng.randrange(2, n-2)
        x = pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(r-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True

print("== A. parity certificate (synthetic) ==")
ok = True
for (p, q) in [(3, 5), (5, 7), (11, 13), (17, 23), (13, 29)]:
    for l in primes_upto(31):
        x, y = l * p + q, abs(l * p - q)
        if (x - y) % 2 != 0:
            ok = False
        if (y % 2 == 1) != (l == 2):
            ok = False
        if (x % 2 == 1) != (l == 2):
            ok = False
print("  x=y mod 2; y odd iff l=2; x odd iff l=2:", "PASS" if ok else "FAIL")

print("\n== B. complete certificate-suite integration test on RSA-260 ==")
N260 = int("2211282552952966643528108525502623092761208950247001539441374831912882294140"
           "2001986512729726569746599085900330031400051170742204560859276357953757185954"
           "2988389587092292384910067030341246205457845664136645406842143612930176940208"
           "46391065875914794251435144458199")
P260A = int("4397328654844826923795068102505872571721883526553349659561256924505973939597"
            "593482272505698004801207988043088656411102133523080581")
P260B = int("5028695206842569864686141618253083416610081090075366674776775706538324961364"
            "412200138116378509733307971876652984898985905923678379")

def full_suite(Nn, p, q, verbose=False):
    checks = []
    if p * q != Nn: return False, [("p*q=N", False)]
    checks.append(("p*q=N", True))
    checks.append(("primality", is_probable_prime(p) and is_probable_prime(q)))
    checks.append(("2 mod 3", p % 3 == 2 and q % 3 == 2))
    # forced lattice
    cls = []
    for p0 in range(72):
        if p0 % 6 != 5: continue
        for q0 in range(72):
            if q0 % 6 != 5: continue
            if (p0 * q0) % 72 == Nn % 72 and (p0 + q0) % 72 == ((p + q) % 72):
                cls.append((p0, q0))
    checks.append(("forced lattice class", (p % 72, q % 72) in cls))
    # branch certificates
    ok_branch = True
    for l in primes_upto(31):
        x, y = l * p + q, abs(l * p - q)
        if x * x - 4 * l * Nn != y * y: ok_branch = False
        if {x + y, x - y} != {2 * l * p, 2 * q}: ok_branch = False
        if (x - y) % 2 != 0: ok_branch = False
        if (y % 2 == 1) != (l == 2): ok_branch = False
        if (x + y) % (2 * l) not in (0, (2 * q) % (2 * l)): ok_branch = False
        if y % p not in (q % p, (-q) % p): ok_branch = False
        if y % q not in ((l * p) % q, (-l * p) % q): ok_branch = False
        joint = {((l * p0 + q0) % 72, abs(l * p0 - q0) % 72) for p0, q0 in cls}
        if (x % 72, y % 72) not in joint: ok_branch = False
    checks.append(("branch certificates l<=31 (square/sumdiff/parity/side/CRT/joint)", ok_branch))
    # Plucker
    okp = all((l1*p+q - (l2*p+q)) * (l1*(l2*p+q) - l2*(l1*p+q)) == (l1-l2)**2 * Nn
              for l1 in (3, 5, 7) for l2 in (11, 13))
    checks.append(("two-l Plucker", okp))
    return all(c for _, c in checks), checks

okR, chkR = full_suite(N260, P260A, P260B)
print("  RSA-260 real factors: full suite:", "PASS" if okR else "FAIL")
for name, c in chkR:
    print(f"    - {name}: {c}")
okW, chkW = full_suite(N260, P260A, P260B + 144)
print("  RSA-260 wrong factors (q+144): full suite:", "FAIL as expected" if not okW else "UNEXPECTED PASS")
