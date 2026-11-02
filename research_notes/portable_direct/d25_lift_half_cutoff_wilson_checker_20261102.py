"""D25 exact original-observer and Wilson-reflection regression (author-side; not Source admission).
Run: python d25_lift_half_cutoff_wilson_checker_20261102.py
Python standard library only. Prints a JSON finite certificate.
"""
import json
from math import comb

def primes_under(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for q in range(2, int(n**0.5) + 1):
        if sieve[q]:
            sieve[q*q:n+1:q] = b"\x00" * ((n-q*q)//q+1)
    return [p for p in range(n+1) if sieve[p]]

def reflected_tail(p):
    assert p > 3 and p % 6 == 1
    m = (p-1)//6
    eps = pow(6, (p-1)//2, p)
    eps = -1 if eps == p-1 else 1
    u = eps * pow(9, -1, p) % p
    total = 0
    for r in range(1, m+1):
        total = (total + (6*r-2)*u) % p
        if r < m:
            u = u*r*(6*r-1)*(6*r+1)*pow(9*(2*r+1)**3, -1, p) % p
    return total

def original_tail(p):
    assert p % 6 == 1
    m = (p-1)//6
    H,E = 3*m,4*m
    mod = p**3
    a, total = 1, 0
    for k in range(E+1):
        if H < k:
            assert a % (p*p) == 0
            total = (total + (6*k+1)*(a//(p*p))) % p
        if k < E:
            a = a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3, -1, mod) % mod
    return total

def full_bridge(p, direct=False):
    assert p > 3 and p % 24 in (13,19)
    m,H,E = (p-1)//6,(p-1)//2,4*((p-1)//6)
    p2,p3 = p*p,p*p*p
    inv = lambda x: pow(x,-1,p3)
    b,g,h,low = 1,0,0,[]
    for k in range(p):
        g=(g+b)%p3
        h=(h+(12*k+1)*b)%p3
        if k <= m: low.append(b%p)
        if k+1 < p:
            b=b*(6*k+1)*(3*k+1)*inv(36*(k+1)**2)%p3
    assert g%p==0
    G=(g//p)%p2
    assert (G*h-1)%p==0
    delta=((G*h-1)%p2)//p
    cr,cs,rs,R = 0,0,0,0
    for r in range(1,m+1):
        if r == 1: cr=pow(10,-1,p)
        else:
            cr=cr*36*(r-1)**2*pow((6*r-1)*(3*r-1),-1,p)%p
        cs=(cs+cr)%p
        rs=(rs+r*cr)%p
        R=(R+2*low[r]*((1+6*r)*cs-6*rs))%p
    aw,ass,W,WH,S,SH,B2 = 1,1,0,0,0,0,0
    for k in range(p):
        wk=(6*k+1)*aw%p3
        sk=(8*k+1)*ass%p3
        W=(W+wk)%p3; S=(S+sk)%p3
        if k<=H:
            WH=(WH+wk)%p3; SH=(SH+sk)%p3
        if H<k<=E:
            assert aw%p2==0
            B2=(B2+(6*k+1)*(aw//p2))%p
        if k+1<p:
            aw=aw*(2*k+1)*(3*k+1)*(3*k+2)*inv(36*(k+1)**3)%p3
            ass=ass*(4*k+1)*(4*k+2)*(4*k+3)*inv(576*(k+1)**3)%p3
    assert W%p2==p and WH%p2==p
    assert S==p and SH==p
    assert (W-WH-p2*B2)%p3==0
    assert B2==reflected_tail(p)
    J=((WH-p)%p3)//p2
    K=((WH-2*SH+p)%p3)//p2
    residual=(delta-R)%p
    assert J==K and (J+B2)%p==residual
    assert ((W-p)%p3)//p2==residual
    if direct:
        wdir,sdir,whdir,shdir=0,0,0,0
        for k in range(p):
            wn=(6*k+1)*comb(2*k,k)**2*comb(3*k,k)
            sn=(8*k+1)*comb(2*k,k)**2*comb(4*k,2*k)
            wd=wn*pow(216,-k,p3)%p3
            sd=sn*pow(2304,-k,p3)%p3
            wdir=(wdir+wd)%p3; sdir=(sdir+sd)%p3
            if k<=H:
                whdir=(whdir+wd)%p3; shdir=(shdir+sd)%p3
        assert (wdir,sdir,whdir,shdir)==(W,S,WH,SH)
    return dict(p=p,R=R,Delta=delta,B2_W=B2,J_H=J,W_half=WH,
                G_mod_p2=G,h_mod_p2=h%p2,Delta_minus_R=residual,
                S_half=SH,independent_direct_binom=direct)

if __name__=="__main__":
    primes=primes_under(3000)
    target=[p for p in primes if p%24 in (13,19)]
    all_sixth=[p for p in primes if p%6==1]
    assert len(target)==107 and len(all_sixth)==207
    for p in all_sixth:
        assert original_tail(p)==reflected_tail(p),p
    rows=[full_bridge(p, p in (13,19,37,43,373)) for p in target]
    assert all(row["Delta_minus_R"]==0 for row in rows)
    sample=[row for row in rows if row["p"] in (13,19,37,43,373,1171)]
    print(json.dumps(dict(schema="D25_AUTHOR_SIDE_HALF_WILSON_CHECK_V1",
        count_target=len(target),count_all_sixth=len(all_sixth),
        max_prime=max(all_sixth),direct_binomial_p=[13,19,37,43,373],
        mismatches=0,target_lift_finite_failures=0,samples=sample),
        indent=2,ensure_ascii=False))
