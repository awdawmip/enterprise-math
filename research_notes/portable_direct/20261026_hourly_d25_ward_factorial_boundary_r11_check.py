#!/usr/bin/env python3
"""Author's exact p-local Green/Ward factorial boundary check (no native CM run).

The corrected Hasse Pochhammer recurrence and oriented source operator are the
same mathematical inputs as the 20261026 diagonal-one-digit source theorem;
this executable independently evaluates its new hypergeometric boundary law.
"""
from fractions import Fraction as Q
from math import factorial, isqrt, comb

CHANNELS = ((0, 2), (1, 2), (0, 3))


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def residue(q, p):
    q = Q(q)
    assert q.denominator % p, (q, p, "not p-local")
    return q.numerator * pow(q.denominator, -1, p) % p


def jets(m):
    p = 6*m + 1
    u = [[Q(0)]*4 for _ in range(p)]
    u[0][0] = Q(1)
    def get(r, k):
        return u[r][k] if 0 <= r < p and 0 <= k <= 3 else Q(0)
    for r in range(1, p):
        d = Q(r)*(r - Q(p, 2))
        b = Q(r-1-m)*(r-1-2*m)
        c = Q(3*(r-1)-4*m)
        for k in range(4):
            u[r][k] = (b*get(r-1,k) + 3*r*get(r,k-1)
                       - c*get(r-1,k-1) + 2*get(r-1,k-2))/d
    return p, u


def moments(p, m, u):
    out = {}
    for a in range(4):
        for b in range(4):
            for n in range(1-2*m, 2*m):
                jlo, jhi = max(1, 1-n), min(2*m, 2*m-n)
                vals = [u[j][a]*u[p-j-n][b] for j in range(jlo, jhi+1)]
                out[a,b,n] = (sum(vals, Q(0)), sum((j*v for j,v in zip(range(jlo,jhi+1), vals)),Q(0)))
    def get(a,b,n,s=0):
        return out.get((a,b,n),(Q(0),Q(0)))[s] if a >= 0 and b >= 0 else Q(0)
    return get


def source(m,p,u,G,n,a,b):
    def U(r,k):
        return u[r][k] if 0 <= r < p and 0 <= k < 4 else Q(0)
    j = 3*G(a-1,b,n,1)-3*G(a-1,b,n+1,1)+4*m*G(a-1,b,n+1)+2*G(a-2,b,n+1)
    j -= 3*((p-n)*G(a,b-1,n)-G(a,b-1,n,1))
    j += (14*m-3*n)*G(a,b-1,n+1)-3*G(a,b-1,n+1,1)-2*G(a,b-2,n+1)
    if n >= 0:
        e = (2*m*m*(a==0)+4*m*(a==1)+2*(a==2))*U(p-n-1,b)
        e += U(2*m-n,a)*(-6*m*m*U(4*m,b)+8*m*U(4*m,b-1)-2*U(4*m,b-2))
    else:
        e = U(-n,a)*(20*m*m*U(p-1,b)-14*m*U(p-1,b-1)+2*U(p-1,b-2))
        e += U(p-(2*m+n+1),b)*(2*m*U(2*m,a-1)-2*U(2*m,a-2))
    return j+e


def F(m):
    return Q(2**(4*m-1)*factorial(2*m-1)*factorial(2*m), factorial(4*m))


def C(a):
    return Q(4**a*factorial(a)**2, factorial(2*a))


def coeff(m,h):
    p=6*m+1
    v=Q(1,p-2*h-1)
    for k in range(h+1,2*m):
        v *= Q(p-2*k,p-2*k-1)
    return v


def all_product(m):
    p=6*m+1
    v=Q(1)
    for k in range(1-2*m,2*m):
        v *= Q(p-2*k,p-2*k-1)
    return v


def check(m):
    p,u=jets(m)
    get=moments(p,m,u)
    lo,hi=1-2*m,2*m
    f=F(m)
    count=0
    rows=[]
    for a,b in CHANNELS:
        y=lambda n:get(a,b,n,1)-Q(p-n,2)*get(a,b,n)
        s={n:source(m,p,u,get,n,a,b) for n in range(lo,hi)}
        # Check the actual finite-cutoff source recurrence, not a synthetic stream.
        for n in range(lo,hi):
            assert (p-2*n)*y(n)-(p-2*n-1)*y(n+1)==s[n]
            count+=1
        assert y(hi)==0
        left=all_product(m)*y(lo)-sum((coeff(m,h)*s[h] for h in range(lo,0)),Q(0))
        pos=sum((coeff(m,h)*s[h] for h in range(0,hi)),Q(0))
        assert left==pos
        count+=1
        if a==0:
            assert y(lo)==0  # exact Pochhammer zero beyond the first cutoff
            count+=1
        if is_prime(p):
            assert residue(f,p)!=0
            assert residue(all_product(m)/p,p)==residue(-f*C(2*m-1),p)
            count+=2
            for t in range(2*m-1):
                assert residue(coeff(m,-t-1)/p,p)==residue(-f*C(t)/Q(2*t+1),p)
                count+=1
            neg=sum((C(t)*s[-t-1]/Q(2*t+1) for t in range(2*m-1)),Q(0))
            endpoint=C(2*m-1)*y(lo)
            assert residue(pos/p/f,p)==residue(neg-endpoint,p)
            count+=1
            if (a,b)==(1,2):
                seed=Q(4*(-1)**m, comb(2*m,m)*(2*m+1)*(m+1))
                assert residue(y(lo),p)==residue(seed,p)!=0
                assert residue(endpoint,p)!=0
                count+=2
            rows.append((a,b,residue(pos/p,p),residue(neg,p),residue(endpoint,p),residue(pos/p/f,p)))
    return p,count,rows


def main():
    total=0
    for m in range(1,13):
        p,n,rows=check(m)
        total+=n
        if p==13:
            assert [row[2] for row in rows]==[8,11,2]
            assert [row[3:] for row in rows]==[(11,0,11),(2,8,7),(6,0,6)]
        print('m=',m,'p=',p,'prime=',is_prime(p),'PASS assertions=',n,'rows=',rows if p==13 else '<computed>')
    print('ALL PASS assertions=',total)

if __name__=='__main__':
    main()
