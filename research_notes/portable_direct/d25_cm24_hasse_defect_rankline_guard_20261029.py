#!/usr/bin/env python3
"""Exact author-side CM(-24) Hasse-lift rank-line probe; no native H0/B0 execution."""
from math import comb, isqrt


def primes_below(n):
    sieve = bytearray(b'\x01') * n
    sieve[:2] = b'\x00\x00'
    for d in range(2, isqrt(n - 1) + 1):
        if sieve[d]:
            sieve[d * d:n:d] = b'\x00' * len(sieve[d * d:n:d])
    return [p for p in range(5, n) if sieve[p]]


def hasse_pair(p):
    """H_p(t) mod (p², 36t²-36t+1), exact integral coefficient formula."""
    mod = p * p
    k = (p - 1) // 2
    e = k // 2
    inv4 = pow(4, -1, mod)
    inv36 = pow(36, -1, mod)
    # s=(1-t)/4; t²=t-1/36, so s²=s/4-1/576.
    def mul(x, y):
        a, b = x
        c, d = y
        return ((a*c - b*d*inv36) % mod, (a*d + b*c + b*d) % mod)

    s = (inv4, -inv4 % mod)
    power = (1, 0)
    c = 1
    A = B = 0
    # c_j=binom(k,2j)binom(2j,j), exact integer ratio at each j.
    for j in range(e + 1):
        A = (A + c*power[0]) % mod
        B = (B + c*power[1]) % mod
        if j < e:
            c = c * (k-2*j)*(k-2*j-1) * pow((j+1)**2, -1, mod) % mod
            power = mul(power, s)
    return A, B


def original_companion_and_jet(p):
    """Original beta_n z^n recurrence at z=1/9, n<=b, modulo p²."""
    mod = p*p
    r1 = next(r for r in range(p) if (8*r+1) % p == 0)
    r3 = next(r for r in range(p) if (8*r+3) % p == 0)
    b = max(r1, r3)
    coeff = 1
    K = D = 0
    for n in range(b + 1):
        K = (K + coeff) % mod
        D = (D + n*coeff) % mod
        if n < b:
            coeff = (coeff*(8*n+1)*(8*n+3)
                     *pow(576*(n+1)**2, -1, mod)) % mod
    return K, D


def independent_hasse(p):
    """Short exact factorial/binomial coefficient check, distinct from ratio path."""
    mod = p*p
    k = (p-1)//2
    inv36, inv4 = pow(36, -1, mod), pow(4, -1, mod)
    A = B = 0
    a, b = 1, 0
    for j in range(k//2 + 1):
        c = comb(k, 2*j)*comb(2*j, j)
        A = (A+c*a) % mod
        B = (B+c*b) % mod
        a, b = ((a+b*inv36)*inv4) % mod, (-a*inv4) % mod
    return A, B


def lucas_defect_scalar(p):
    """Integer Lucas recurrence for L(H)=B-2A, reduced only at the end."""
    m=p*p
    k=(p-1)//2
    e=k//2
    v0,v1=-2,-432  # v_j=576^j L(s^j): v_(j+2)=144 v_(j+1)-576 v_j
    vs=[v0,v1]
    for j in range(2,e+1):
        vs.append(144*vs[-1]-576*vs[-2])
    total=0
    iz=pow(576,-1,m)
    z=1
    for j in range(e+1):
        total=(total+comb(k,2*j)*comb(2*j,j)*vs[j]*z)%m
        z=z*iz%m
    return total


def main():
    stats={13:[], 17:[], 19:[], 23:[]}
    for p in primes_below(10000):
        residue=p%24
        if residue not in stats:
            continue
        A,B=hasse_pair(p)
        assert (A%p,B%p)==(0,0), (p,A,B)
        K,D=original_companion_and_jet(p)
        assert ((K==0)==(residue in (13,23))), (p,K)
        assert D%p!=0, (p,D)
        stats[residue].append((p,A//p,B//p,(B//p-2*(A//p))%p,(K//p)%p,D%p))
        if p in (13,17,19,23,37,373):
            assert (A,B)==independent_hasse(p)
            assert (B-2*A)%(p*p)==lucas_defect_scalar(p)
    for residue, rows in stats.items():
        zero=sum(row[3]==0 for row in rows)
        root2=sum(row[4]==0 for row in rows)
        print(f'p_mod24={residue} count={len(rows)} Hasse_line_zero={zero} companion_root2={root2}')
        print(' sample',rows[:2], 'last',rows[-1])
        if residue==13:
            assert zero==len(rows) and root2==len(rows)
            assert all(row[1]!=0 for row in rows)
        else:
            assert zero==0
    assert sum(map(len,stats.values()))==616
    # Exact composite falsifier: residue 13 mod 24 alone does not suffice.
    H85 = independent_hasse(85)
    assert H85 == (3451, 3281)
    assert (H85[1]-2*H85[0])%(85*85) == 3604
    assert any(row[0]==373 and row[1:]==(14,28,0,0,5) for row in stats[13])
    print('PASS_FINITE_CM24_HASSE_P2_LINE_616_PRIMES_P_LT_10000')

if __name__=='__main__':
    main()
