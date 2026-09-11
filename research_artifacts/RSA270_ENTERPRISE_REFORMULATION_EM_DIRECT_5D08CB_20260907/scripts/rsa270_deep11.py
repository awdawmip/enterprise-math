"""
Deep research round 11 (EM-DIRECT-5D08CB / DIRECT-RSA270):
audit the C3 sign hazard across the remaining certificates — specifically C5 (y-sequence):
the round-5 |.|-collapsed 12-sequence set is the sign-collapsed shadow; the sign-safe set
uses per-l +-(l p0 - q0) mod 72 with the side-consistency structure:
  sign(l p - q) = + for l > r, - for l < r  (monotone in l; only l=2 straddles the prior band).
Verify: RSA-260 real sequence in the sign-safe set; RSA-270 sign-safe sequence count.
"""
import math

def primes_upto(n):
    sieve = bytearray([1]) * (n + 1); sieve[0:2] = b"\x00\x00"
    for i in range(2, math.isqrt(n) + 1):
        if sieve[i]:
            sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    return [i for i in range(2, n + 1) if sieve[i]]

N260 = int("2211282552952966643528108525502623092761208950247001539441374831912882294140"
           "2001986512729726569746599085900330031400051170742204560859276357953757185954"
           "2988389587092292384910067030341246205457845664136645406842143612930176940208"
           "46391065875914794251435144458199")
P260A = int("4397328654844826923795068102505872571721883526553349659561256924505973939597"
            "593482272505698004801207988043088656411102133523080581")
P260B = int("5028695206842569864686141618253083416610081090075366674776775706538324961364"
            "412200138116378509733307971876652984898985905923678379")
N270 = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
           "3578286788836931857711641821391926857265831491306067262691135402760979316634"
           "1626693946596196427744273886601876896313468704059066746903123910748277606548"
           "649151920812699309766587514735456594993207")

def classes_of(Nn, S72):
    return [(p0, q0) for p0 in range(72) if p0 % 6 == 5
            for q0 in range(72) if q0 % 6 == 5
            and (p0 * q0) % 72 == Nn % 72 and (p0 + q0) % 72 == S72]

Ls = primes_upto(31)
p, q = P260A, P260B
S72 = (p + q) % 72
cls = classes_of(N260, S72)
print(f"RSA-260: classes = {len(cls)} ; real r = {q/p:.4f}")

# sign-safe admissible sequences: per-l union of +-(l p0 - q0) mod 72 over classes
signsafe = set()
for (p0, q0) in cls:
    for sign in (1, -1):
        sign_consistent = True
        for l in Ls:
            # the sign must match sign(l p - q) for the REAL side; class reps can disagree per l,
            # so the sign-safe set = per-l union (sign not fixed by the class rep alone).
            pass
        signsafe.add(tuple((sign * (l * p0 - q0)) % 72 for l in Ls))
print(f"sign-safe sequence set (fixed sign per class): {len(signsafe)} sequences")

true_seq = tuple(abs(l * p - q) % 72 for l in Ls)
in_any = any(true_seq == s for s in signsafe)
print(f"real |.|-sequence in fixed-sign set: {in_any}")
# the real y = |l p - q| = sign_real(l)*(l p - q): per-l sign is real-side determined;
# the correct membership: for each l, y mod 72 in {+-(l p0 - q0) mod 72 : classes}
per_l_ok = all(abs(l * p - q) % 72 in
                {e * (l * p0 - q0) % 72 for (p0, q0) in cls for e in (1, -1)}
                for l in Ls)
print(f"per-l sign-safe membership of real sequence: {per_l_ok}")
# side-consistency: real sign(l p - q) = + for l > r, - for l < r; r=1.1436 -> all l>=2 have + sign
signs_real = [1 if (l * p - q) >= 0 else -1 for l in Ls]
print(f"real side pattern: all + for l > r (r=1.14): {all(s == 1 for s in signs_real)}")
# side-consistent admissible sequences: per-l sign = sign(l p - q) = + for l > r; the sequence
# values = (l p0 - q0) mod 72 with the per-l sign; but the class rep's own side (l p0 vs q0)
# can differ -> the side-consistent set = { seq : seq[l] = (l p0 - q0) mod 72 if l > r else (q0 - l p0) mod 72 }
side_set = set()
for (p0, q0) in cls:
    seq = tuple(((l * p0 - q0) % 72 if l * p > q else (q0 - l * p0) % 72) for l in Ls)
    side_set.add(seq)
print(f"side-consistent sequence set: {len(side_set)} sequences; real in it: {true_seq in side_set}")

# RSA-270 statement
cls270 = classes_of(N270, 16)
side_set270 = set()
for (p0, q0) in cls270:
    # prior band: l>=3 always l p > q (r < 3); l=2 straddles -> two sign choices at l=2
    for e2 in (1, -1):
        seq = tuple((2 * p0 - q0) * e2 % 72 if l == 2 else (l * p0 - q0) % 72 for l in Ls)
        side_set270.add(seq)
print(f"RSA-270 side-consistent sequence set (l=2 both signs): {len(side_set270)} sequences")
