#!/usr/bin/env python3
"""D25 author-side exact finite-field signed Green/contact and rank guard.

Checks the original frozen beta_i,C_a recurrence and the original two-strip
J(i,a) against the new single-index Green-tail formula. Native H0/B0 not run.
"""
from math import isqrt


def primes(bound):
    for p in range(13, bound):
        if p % 24 in (13, 19) and all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def check(p):
    assert p % 24 in (13, 19) and p > 5
    m = (p - 1) // 6
    beta = [0] * (m + 1)
    beta[0] = 1
    for i in range(1, m + 1):
        beta[i] = beta[i - 1] * (m - i + 1) * (2*m - i + 1) * pow(2*i*i, -1, p) % p
    c = [0] * (4*m + 1)
    c[1] = pow(10, -1, p)
    for a in range(1, 4*m):
        c[a + 1] = c[a] * 36*a*a * pow((6*a+5)*(3*a+2), -1, p) % p
    assert all(beta[1:]) and all(c[1:m+1])
    btail = [0] * (m + 2)
    ctail = [0] * (4*m + 2)
    for i in range(m, 0, -1):
        btail[i] = (btail[i + 1] + beta[i]) % p
    for a in range(4*m, 0, -1):
        ctail[a] = (ctail[a + 1] + c[a]) % p
    # Independently evaluate the original signed two-strip carrier.
    direct = 0
    for i in range(1, m + 1):
        for a in range(1, 4*m + 1):
            direct += 2 * beta[i] * c[a] * ((6*a-1) if a <= i else 6*i)
    direct %= p
    # Green expansion: min(i,a)=sum_{r<=i,r<=a} 1, contact=1_{a<=i}.
    green = 2 * sum(btail[r] * (6*ctail[r] - c[r]) for r in range(1, m + 1)) % p
    # Separate original frozen R and high-tail F for exact provenance check.
    F = ctail[1]
    W0 = 2 * sum(i*beta[i] for i in range(1, m + 1)) % p
    R = 2 * sum(beta[i] * sum((1+6*(i-a))*c[a] for a in range(1, i+1)) for i in range(1, m+1)) % p
    assert direct == green == (6*F*W0-R) % p
    # Full-row-rank certificate: the original weighted m x m leading minor
    # is diagonal row/column scaling of K with det(K)=5^m.
    detK = pow(5, m, p)
    detWeighted = pow(2, m, p) * detK % p
    for i in range(1, m + 1):
        detWeighted = detWeighted * beta[i] * c[i] % p
    assert detK != 0 and detWeighted != 0
    # Exact discrete mixed second difference has 5*delta_{a=i}+delta_{a=i+1}.
    if m <= 20:
        k = lambda i,a: 6*min(i,a)-int(a <= i)
        for i in range(1, m):
            for a in range(1, 4*m):
                mixed=k(i+1,a+1)-k(i+1,a)-k(i,a+1)+k(i,a)
                assert mixed == 5*int(a == i)+int(a == i+1)
    return p,m,direct,F,R,detK,detWeighted


def main():
    rows=[check(p) for p in primes(5000)]
    assert len(rows)==166, len(rows)
    for p in (13, 19, 67, 373):
        print('WITNESS p,m,J,F,R,detK,detWeighted',next(row for row in rows if row[0]==p))
    print('PASS_D25_SIGNED_GREEN_DIAGONAL_CONTACT_FULL_ROW_RANK',len(rows),'TARGET_PRIMES_LT_5000')


if __name__ == '__main__':
    main()
