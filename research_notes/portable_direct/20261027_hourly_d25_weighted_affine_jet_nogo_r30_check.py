"""Author-side exact check: W/S Hadamard weighted observer affine-jet obstruction.

This is external finite-field algebra, not a native Enterprise Math experiment.
Python 3 standard library only. The finite sweep is evidence, not a proof of
any all-prime supercongruence or native task acceptance.
"""
from fractions import Fraction
from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def determinant3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def residue(f, p):
    f = Fraction(f)
    assert f.denominator % p
    return f.numerator * pow(f.denominator, -1, p) % p


def h_prefix(r):
    val = Fraction(1)
    for t in range(1, r + 1):
        val *= Fraction(t * (3*t + 1) * 144,
                        3 * (12*t - 1) * (12*t + 5))
    return val


H = [h_prefix(r) for r in range(3)]
S = [(Fraction(13, 3) + 8*r) * 9**r * H[r] for r in range(3)]
W = [(2*r + 1) * 2**r for r in range(3)]
assert H == [Fraction(1), Fraction(192, 187),
             Fraction(129024, 124729)]
assert S == [Fraction(13, 3), Fraction(21312, 187),
             Fraction(212502528, 124729)]
assert W == [1, 6, 20]
D = determinant3([[S[r], r*S[r], Fraction(W[r])]
                  for r in range(3)])
assert D == Fraction(2692858746624, 23324323)
N = 3506326493
assert D.numerator == 2**8 * 3 * N
assert D.denominator == 11**2 * 17**2 * 23 * 29
# Fully exhaustive, exact integer divisibility certificate through sqrt(N).
assert isqrt(N) == 59214
assert is_prime(N)
assert N % 6 == 5

n_primes = 0
n_19class = 0
examples = {}
for p in range(7, 2000, 6):
    if not is_prime(p):
        continue
    n_primes += 1
    m = (p-1) // 6
    if p == 7:
        assert m == 1 and residue(S[0], p) == 2
        continue
    if p == 13:
        assert m == 2 and residue(S[0], p) == 0
        assert W[0] % p == 1
        continue
    assert m >= 3
    dmod = residue(D, p)
    assert dmod != 0
    if p in (19, 31, 37, 61, 67, 181, 373, 733):
        examples[p] = dmod
    if p % 24 != 19:
        continue
    n_19class += 1
    hs = 1
    R = []
    for r in range(m):
        if r:
            hs = (hs * r * (3*r + 1) * pow(3, -1, p)
                  * pow((12*r-1)*(12*r+5), -1, p) * 144) % p
        s_r = ((8*r + residue(Fraction(13,3),p)) * pow(9,r,p) * hs) % p
        w_r = ((2*r + 1) * pow(2,r,p)) % p
        assert s_r != 0
        R.append(w_r * pow(s_r,-1,p) % p)
        if r:
            A = 216*(2*r-1)*(24*r+13)*r*(3*r+1)
            B = (2*r+1)*(24*r-11)*(12*r-1)*(12*r+5)
            assert (A*R[r]-B*R[r-1]) % p == 0
    differences = R[:]
    degree = -1
    for order in range(m):
        if differences[0] % p:
            degree = order
        differences = [(differences[j+1]-differences[j])%p
                       for j in range(len(differences)-1)]
    assert degree >= m-5  # proved algebraically for all p%24=19
    if p in (19,43,67,139,163,211,307,379,523,739):
        print('degree witness', p, m, degree)

assert n_primes == 148
print('EXHAUSTIVE N PRIME DIVISION CHECK PASS; sqrt bound', isqrt(N))
print('R30 exact rational determinant PASS', D)
print('all p=1(mod6), p<2000: ', n_primes)
print('p=19(mod24) interpolation/recurrence checks:', n_19class)
print('selected determinant residues:', examples)
print('AUTHOR_EXACT_CHECK_PASS')
