"""Exact author-side F_p checks for D25 R24 paired W/S ports; not native CM."""
from math import factorial


def primes_below(bound):
    marks = bytearray(b"\x01") * bound
    marks[:2] = b"\x00\x00"
    for k in range(2, int(bound ** 0.5) + 1):
        if marks[k]:
            marks[k*k:bound:k] = b"\x00" * ((bound-1-k*k)//k+1)
    return [p for p in range(7, bound) if marks[p] and p % 6 == 1]


def verify(p):
    m = (p - 1) // 6
    inv3, inv6, inv8 = (pow(x, -1, p) for x in (3, 6, 8))
    a, b, c = 2 * inv3 % p, 7 * inv6 % p, 4 * inv3 % p
    fact = [1] * p
    for k in range(1, p):
        fact[k] = fact[k-1] * k % p

    # The genuinely W-sourced reflected high terms of the previous R23 theorem.
    source = []
    for j in range(2*m, 3*m):
        den = fact[2*j+1] * fact[3*j-6*m+1] % p
        val = (6*j+5) * pow(216, j, p) * pow(fact[j], 5, p)
        source.append(val * pow(den, -1, p) % p)
    C = source[0]
    assert C != 0
    assert C == (-9 * pow(216, 2*m, p) * pow(fact[2*m], 6, p)) % p

    # Well-defined r=0,...,m-1 coefficients in F_p; the first denominator
    # singularity occurs exactly at r=m, so no term is extrapolated across it.
    coeff = [1]
    for r in range(1, m):
        denom = r * (b+r-1) * (c+r-1) % p
        assert denom != 0
        coeff.append(coeff[-1] * pow(a+r-1, 3, p) * pow(denom, -1, p) % p)
    assert len(coeff) == len(source)
    assert all(source[r] == C * (2*r+1) * pow(2, r, p) * coeff[r] % p
               for r in range(m))

    # Theta-polynomial D = theta(theta+1/6)(theta+1/3)
    #                    - X(theta+2/3)^3.
    # Its exact nonzero finite-truncation source is coeff[m-1] X^m / 8.
    residual = []
    for r in range(m+1):
        left = r * (r+inv6) * (r+inv3) * coeff[r] if r < m else 0
        right = pow(r-1+a, 3, p) * coeff[r-1] if r else 0
        residual.append((left-right) % p)
    assert residual[:-1] == [0] * m
    assert residual[-1] == coeff[-1] * inv8 % p != 0

    F = sum(coeff[r] * pow(2, r, p) for r in range(m)) % p
    thetaF = sum(r * coeff[r] * pow(2, r, p) for r in range(m)) % p
    U = sum(source) % p
    assert U == C * (F + 2*thetaF) % p

    # Separate S-mid source with the SAME (2/3)_r^3 numerator but
    # different 9^r observer and three true finite-truncation denominators.
    B = []
    for j in range(2*m, 3*m):
        den = fact[4*j-6*m+2]
        B.append(2 * (8*j+7) * pow(2304, j, p) *
                 pow(fact[j], 4, p) * pow(den, -1, p) % p)
    D = 2 * pow(2304, 2*m, p) * pow(fact[2*m], 4, p)
    D = D * pow(fact[2*m+2], -1, p) % p
    d = [1]
    sb = [11*pow(12, -1, p)%p, b, 17*pow(12, -1, p)%p]
    for r in range(1, m):
        den = 1
        for v in sb:
            den = den * (v+r-1) % p
        assert den != 0
        d.append(d[-1] * pow(a+r-1, 3, p) * pow(den, -1, p) % p)
    assert all(B[r] == D * (8*r+13*inv3) * pow(9, r, p) * d[r] % p
               for r in range(m))

    # Fourth-order S Picard-Fuchs operator:
    # theta(theta-1/12)(theta+1/6)(theta+5/12)
    #    - X(theta+1)(theta+2/3)^3.
    inv12 = pow(12, -1, p)
    residualS = []
    for r in range(m+1):
        left = (r*(r-inv12)*(r+inv6)*(r+5*inv12)*d[r]) if r<m else 0
        right = (r*pow(r-1+a, 3, p)*d[r-1]) if r else 0
        residualS.append((left-right)%p)
    assert residualS[:-1] == [0]*m
    assert residualS[-1] == -d[-1]*pow(48,-1,p)%p != 0
    FS = sum(d[r]*pow(9,r,p) for r in range(m))%p
    thetaFS = sum(r*d[r]*pow(9,r,p) for r in range(m))%p
    M = sum(B)%p
    assert M == D*(13*inv3*FS+8*thetaFS)%p
    # Different source filters cannot be identified termwise: at p=13,
    # the r=0 S-mid weighted term is zero but the W-high term is not.
    if p==13:
        assert B[0]==0 and source[0]!=0
    return p,m,U,C,F,thetaF,residual[-1],M,D,FS,thetaFS,residualS[-1]


def main():
    checked = [verify(p) for p in primes_below(2000)]
    assert len(checked) == 148
    expected = {
        7: (1, 5, 5, 1, 0, 1),
        13: (2, 10, 9, 2, 1, 9),
        19: (3, 9, 13, 4, 2, 16),
        181: (30, 152, 70, 17, 171, 62),
        373: (62, 266, 203, 334, 361, 251),
        733: (122, 67, 168, 420, 665, 729),
    }
    for p, tail in expected.items():
        assert verify(p)[1:7] == tail, (p, verify(p), tail)
    print("PASS: 148 primes p=6m+1, 7<=p<2000; full source/reflection terms,")
    print("two Picard-Fuchs exact inhomogeneous residues and rank-jet readouts.")
    for row in checked:
        if row[0] in expected:
            print("p,m,U,C,Fw,thetaFw,bW,M,D,Fs,thetaFs,bS:", row)


if __name__ == "__main__":
    main()
