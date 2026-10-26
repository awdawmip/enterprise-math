"""Author-side exact audit of the published companion half-cut bridge.
Not a native H0/B0 run, Source claim, proof of all-prime LIFT, or independent review.
Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
The theorem-backed S_full == S_half comes from Guo--Zudilin, arXiv:1803.01830.
"""
from math import comb, factorial
from hashlib import sha256
import json

PRIMES = (13, 19, 37, 43, 61, 67, 211, 373)

def verify(p):
    assert p >= 13 and p % 24 in (13, 19)
    m = (p - 1) // 6
    q = (3*p - 1) // 4
    M = p**3
    w_terms = [
        ((6*n+1) * comb(2*n,n)**2 * comb(3*n,n) * pow(216,-n,M)) % M
        for n in range(p)
    ]
    s_terms = [
        ((8*n+1) * comb(4*n,2*n) * comb(2*n,n)**2 * pow(2304,-n,M)) % M
        for n in range(p)
    ]
    s_half = sum(s_terms[:3*m+1]) % M
    s_full = sum(s_terms) % M
    s_high = sum(s_terms[3*m+1:]) % M
    low = sum(w_terms[n]-s_terms[n] for n in range(3*m+1)) % M
    w_high = sum(w_terms[3*m+1:4*m+1]) % M
    H = sum(
        ((6*n+1) * factorial(2*n-p) * factorial(3*n-p)
         * pow(factorial(n), -5, p) * pow(216, -n, p))
        for n in range(3*m+1,4*m+1)
    ) % p
    assert s_half == s_full == p, (p, s_half, s_full)
    assert s_high == 0 and all(v == 0 for v in s_terms[q+1:])
    assert w_high == p*p*H and all(v == 0 for v in w_terms[4*m+1:])
    assert low % (p*p) == 0
    assert (sum(w_terms)-p) % M == (low+p*p*H) % M
    if p == 373:
        s_mid = sum(s_terms[3*m+1:4*m+1]) % M
        s_gap = sum(s_terms[4*m+1:q+1]) % M
        assert (s_mid//(p*p), s_gap//(p*p)) == (92,281)
        assert (low,w_high,s_high) == (14886803,37008314,0)
    return [p,m,3*m,4*m,q,(low//(p*p))%p,H,
            ((low//(p*p))+H)%p,s_high]

def main():
    rows = [verify(p) for p in PRIMES]
    expected = [
        [13,2,6,8,9,3,10,0,0],
        [19,3,9,12,14,10,9,0,0],
        [37,6,18,24,27,17,20,0,0],
        [43,7,21,28,32,8,35,0,0],
        [61,10,30,40,45,44,17,0,0],
        [67,11,33,44,50,9,58,0,0],
        [211,35,105,140,158,9,202,0,0],
        [373,62,186,248,279,107,266,0,0]]
    assert rows == expected
    digest = sha256(json.dumps(rows,separators=(",",":")).encode()).hexdigest()
    assert digest == "906c1683c3f0b08e42596a8711613e00fe721cd9525404f33264c5bd9c4408c1"
    print("PASS: 8 exact crosschecks; SHA256:",digest)
    for row in rows:
        print(row)

if __name__ == "__main__":
    main()
