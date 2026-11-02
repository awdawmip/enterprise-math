"""Exact finite-field certificates for D25 Cauchy carry Picard-Fuchs system."""
from math import prod

def primes_upto(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for d in range(2, int(n ** 0.5) + 1):
        if sieve[d]:
            sieve[d*d::d] = b'\x00' * ((n-d*d)//d+1)
    return [p for p in range(7, n + 1) if sieve[p] and p % 6 == 1]

def check(p):
    r = (p - 1) // 6
    inv = lambda v: pow(v % p, -1, p)
    a = b = c = 1
    u = v = 0
    k0 = [0] * (2*r + 1)
    k1 = [0] * (2*r + 1)
    dpoly = [1] + [0] * (2*r)
    for m in range(1, 2*r + 1):
        a = a * (2*m-1)*(3*m-2)*(3*m-1)*inv(18*m**3) % p
        b = b * (2*m-1)*inv(4*m) % p
        c = c * (3*m-2)*(3*m-1)*inv(9*m*m) % p
        v = (v + u) % p
        u = (u - inv(4*m*b)) % p
        k0[m] = a*u % p
        k1[m] = a*v % p
        dpoly[m] = c*pow(2, m, p) % p
    for m in range(2*r + 2):
        coefficient = lambda arr: arr[m] if m < len(arr) else 0
        previous = lambda arr: arr[m-1] if 0 <= m-1 < len(arr) else 0
        cubic = ((2*m-1)*(3*m-2)*(3*m-1)*inv(18)) % p
        quadratic = (2*(3*m-2)*(3*m-1)*inv(9)) % p
        l3k0 = (m**3*coefficient(k0) - cubic*previous(k0)) % p
        l3k1 = (m**3*coefficient(k1) - cubic*previous(k1)) % p
        l2d = (m*m*coefficient(dpoly) - quadratic*previous(dpoly)) % p
        assert l3k0 == (-inv(4)*m*m*coefficient(dpoly)) % p, (p, m, 'K0')
        assert l3k1 == cubic*previous(k0) % p, (p, m, 'K1')
        assert l2d == 0, (p, m, 'Gauss')
    half = inv(2)
    phi = 1
    for h in range(min(7, p)):
        if h:
            phi = -phi*(3*h-2)*(3*h-1)*inv(9*h) % p
        moment = sum(
            (1 if h == 0 else prod(range(k-h+1, k+1)))
            * dpoly[k]*pow(half, k, p)
            for k in range(h, 2*r+1)
        ) % p
        assert moment == phi, (p, h, 'factorial moment')
    jet0 = [sum(m**j*k0[m]*pow(half, m, p) for m in range(2*r+1)) % p for j in range(4)]
    djet = [sum(m**j*dpoly[m]*pow(half, m, p) for m in range(2*r+1)) % p for j in range(4)]
    assert djet[:4] == [1, -2*inv(9) % p, 2*inv(81) % p, 14*inv(2187) % p], (p, djet)
    assert (162*jet0[3]-243*jet0[2]-117*jet0[1]-18*jet0[0]+2) % p == 0, (p, 'source jet')
    K1 = sum(k1[m]*pow(half, m, p) for m in range(2*r+1)) % p
    eps = pow(2, (p-1)//2, p)
    assert eps in (1,p-1)
    candidate = (jet0[0] + 6*jet0[1] - 3*(eps-1)) % p
    return jet0, K1, djet, candidate

if __name__ == '__main__':
    ps = primes_upto(10000)
    passed = 0
    for p in ps:
        jets, K1, djet, candidate = check(p)
        passed += candidate == 0
        if p in (7, 13, 19, 31, 37, 43, 373, 1171):
            print(f'p={p}: K0,K0jet1,K0jet2,K0jet3={jets}; K1={K1}; Djets={djet}; candidate_diff={candidate}')
    print(f'PASS polynomial PF + Gauss moments + source jet: {len(ps)}/{len(ps)} primes p<=10000, p%6=1')
    print(f'FINITE CONJECTURE K0+6thetaK0=3((2/p)-1): {passed}/{len(ps)} primes p<=10000, p%6=1')
