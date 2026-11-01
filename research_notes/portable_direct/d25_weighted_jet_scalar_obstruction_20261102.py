"""Finite p-adic endpoint-jet witnesses for D25. Stdlib exact modular arithmetic only.

Check 107 target primes <=3000. Characteristic-zero monodromy is in the proof note.
This is not an H0/B0 native experiment or an infinite-prime proof.
"""
from fractions import Fraction


def primes(n):
    sieve = bytearray(b'\x01') * (n+1)
    sieve[:2] = b'\x00\x00'
    for q in range(2, int(n**.5)+1):
        if sieve[q]:
            sieve[q*q::q] = b'\x00' * ((n-q*q)//q+1)
    return [i for i in range(n+1) if sieve[i]]


def jet(p, kind):
    """Moments of f=sum_{0 <= k<p} A_k z_0^k, theta^j f for j<=3."""
    coeff = 1
    ans = [0, 0, 0, 0]
    for k in range(p):
        for j in range(4):
            ans[j] = (ans[j] + (k**j) * coeff) % p
        if k == p-1:
            break
        if kind == 'A':
            numer = (2*k+1)*(3*k+1)*(3*k+2)
            denom = 36 * (k+1)**3
        else:
            numer = (4*k+1)*(2*k+1)*(4*k+3)
            denom = 288 * (k+1)**3
        coeff = coeff * numer * pow(denom, -1, p) % p
    return ans


def check(p, kind):
    v = jet(p, kind)
    if kind == 'A':
        w, z0 = 6, Fraction(1, 2)
        predicted = (0, 6*v[2] % p, 10*v[2] % p)
    else:
        w, z0 = 8, Fraction(1, 9)
        predicted = (0, 8*v[2] % p, 5*pow(2, -1, p)*v[2] % p)
    weighted = [(v[i] + w*v[i+1]) % p for i in range(3)]
    e1, e0 = (
        (Fraction(13, 18), Fraction(1, 9))
        if kind == 'A'
        else (Fraction(11, 16), Fraction(3, 32))
    )

    def F(x):
        return x.numerator*pow(x.denominator, -1, p) % p

    assert (
        F(1-z0)*v[3]
        - F(z0)*(F(Fraction(3, 2))*v[2] + F(e1)*v[1] + F(e0)*v[0])
    ) % p == 0, (p, kind, "PF")

    if v[0] == 0 and v[1] == 0:
        assert weighted == list(predicted), (p, kind, weighted, predicted)
    return v, weighted


def main():
    ps = [p for p in primes(3000) if p % 24 in (13, 19)]
    shown = {13, 19, 37, 43, 61, 67, 109, 139, 211, 373, 1171}
    for p in ps:
        a, ya = check(p, 'A')
        b, zb = check(p, 'B')
        assert a[0] == a[1] == b[0] == b[1] == 0, (p, a, b)
        assert a[2] != 0 and b[2] != 0, (p, a, b)
        scalar = zb[1] * pow(ya[1], -1, p) % p
        assert ((scalar*ya[2] - zb[2]) % p == 0) == (p == 13), p
        if p in shown:
            qratio = b[2]*pow(a[2], -1, p) % p
            print(f'p={p}: A_q={a[2]}, B_q={b[2]}, CM-ratio={qratio}, A_weighted_jet={ya}, B_weighted_jet={zb}')
    print(f'PASS: {len(ps)} target primes p<=3000; double zeros, nonzero second jets, PF,')
    print('weighted CM rays and p=13-only scalar coincidence verified exactly.')
    print('Finite-prime evidence does not prove B-model all-prime double-zero statement.')


if __name__ == '__main__':
    main()
