#!/usr/bin/env python3
"""Exact author-side D25 signed tail/cutoff duality checker (no native experiments)."""
from math import isqrt


def prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def check(p):
    assert p >= 13 and p % 24 in (13, 19) and prime(p)
    m = (p-1)//6
    modulus = p**3
    b = [1]
    for k in range(p-1):
        b.append(b[-1] * (6*k+1) * (3*k+1) * pow(36*(k+1)**2, -1, modulus) % modulus)
    g, h = sum(b) % modulus, sum((12*k+1)*x for k,x in enumerate(b)) % modulus
    g_lo = sum(b[:2*m+1]) % modulus
    h_lo = sum((12*k+1)*b[k] for k in range(2*m+1)) % modulus
    assert g % p == g_lo % p == 0
    assert (g//p * h) % p == 1
    assert (g_lo//p * h_lo) % p == 1
    delta = ((g//p * h) % (p*p)-1)//p % p
    delta_lo = ((g_lo//p * h_lo) % (p*p)-1)//p % p
    hbar = h_lo % p
    bs = [x%p for x in b[:m+1]]
    assert sum(bs)%p == 0
    assert hbar == sum((12*i+1)*x for i,x in enumerate(bs))%p
    assert hbar != 0 and bs[m] != 0
    v = [0] + [(b[p-a] // (p*p)) % p for a in range(1,4*m+1)]
    assert all(b[p-a] % (p*p) == 0 for a in range(1,4*m+1))
    T = sum(v)%p
    assert T == sum((b[k]//(p*p)) for k in range(2*m+1,p))%p
    C = [0]*(m+1)
    C[1] = pow(10,-1,p)
    for a in range(1,m):
        C[a+1] = C[a]*36*a*a*pow((6*a+5)*(3*a+2),-1,p)%p
    assert v[1:m+1] == C[1:]
    Vs = Js = R = 0
    for i in range(1,m+1):
        Vs = (Vs+C[i]) % p
        Js = (Js+i*C[i]) % p
        R = (R+2*bs[i]*((6*i+1)*Vs-6*Js))%p
    # Full list of frozen original R coefficients, independent of the prefix rewrite.
    Rsensitivity = [0] + [2*sum((1+6*(i-a))*bs[i] for i in range(a,m+1))%p
                           for a in range(1,m+1)]
    assert R == sum(C[a]*Rsensitivity[a] for a in range(1,m+1))%p
    assert Rsensitivity[m] == 2*bs[m]%p
    P = M = K_head = 0
    for a in range(1,m+1):
        # Prefix includes exactly ranks 0 <= i < a.
        idx = a-1
        P = (P+bs[idx])%p
        M = (M+idx*bs[idx])%p
        S = (6*M+(1-6*a)*P)%p
        assert (hbar-Rsensitivity[a])%p == (2*S)%p
        K_head = (K_head + 2*v[a]*S)%p
    K_bulk = hbar*sum(v[m+1:])%p
    K = (K_head+K_bulk)%p
    assert K == (hbar*T-R)%p
    assert (delta-R)%p == (delta_lo+K)%p
    # Rank-two proof at the literal two coordinates a=m,m+1.
    # The 2x2 submatrix of (T,R) is [[1,1],[2*b_m,0]], determinant = -2*b_m.
    assert (2*bs[m])%p != 0
    if p in (13,19,157,373):
        a=1
        A=0
        for n in range(p):
            A=(A+(6*n+1)*a)%modulus
            if n<p-1:
                a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,modulus)%modulus
        assert A% (p*p) == p
        assert (delta-R)%p == ((A-p)%(p**3))//(p*p)%p
    return dict(p=p, m=m, hbar=hbar, T=T, R=R, delta=delta,
                low_digit=delta_lo, head=K_head, bulk=K_bulk,
                repaired=(delta_lo+K_head+K_bulk)%p,
                det=(-2*bs[m])%p)


def main():
    rows = [check(p) for p in range(13,5000) if p%24 in (13,19) and prime(p)]
    assert len(rows)==166 and {q['p']%24 for q in rows}=={13,19}
    assert all(q['repaired'] == (q['delta']-q['R'])%q['p'] for q in rows)
    print('PASS_D25_SIGNED_TAIL_CUTOFF_CM_PREFIX_DUALITY_EXACT')
    print('target_primes',len(rows),'class13',sum(q['p']%24==13 for q in rows),
          'class19',sum(q['p']%24==19 for q in rows))
    for p in (13,19,37,157,373):
        q = next(q for q in rows if q['p']==p)
        print('witness', ' '.join(f'{k}={v}' for k,v in q.items()))

if __name__=='__main__':
    main()
