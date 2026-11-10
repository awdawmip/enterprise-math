"""D25 W216: exact finite-field quadratic twist / Laurent constant-term verifier.
Author-side experiment; this is not the native H0/B0 p=373 benchmark.
No third-party dependencies; prints prime coverage and select witnesses.
"""
from math import isqrt

def prime(n):
    if n < 2: return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0: return False
    return True

def dickson(u, m, p):
    # Binary O(log m) evaluation in Fp[Z]/(Z^2-uZ+1/2).
    q = pow(2, -1, p)
    a, b, c, d = 0, 1, 1, 0  # accumulator 1; base Z
    k = m
    while k:
        if k & 1:
            a, b = (a*c*u + a*d + b*c) % p, (b*d - a*c*q) % p
        c, d = (c*c*u + 2*c*d) % p, (d*d - c*c*q) % p
        k //= 2
    return (a*u+2*b) % p

def ct_dickson(m,p):
    inv2=pow(2,-1,p)
    # u(t)=t+5+(7/2)/t+(1/2)/t^2
    weights=((1,1),(0,5),(-1,7*inv2%p),(-2,inv2))
    if m==0:return 2%p
    prev={0:2%p}
    now=dict((k,v%p) for k,v in weights)
    for _ in range(2,m+1):
        nex={}
        for k,v in now.items():
            for d,w in weights:
                e=k+d
                nex[e]=(nex.get(e,0)+v*w)%p
        for k,v in prev.items():
            nex[k]=(nex.get(k,0)-inv2*v)%p
        prev,now=now,nex
    return now.get(0,0)

def check(p):
    assert prime(p) and p%24 in (13,19)
    m=(p-1)//6
    inv2=pow(2,-1,p)
    c1=c2=1
    J=0
    # Original finite-field binomial coefficient, independent of v/t.
    for k in range(m+1):
        J=(J+c1*c2*pow(inv2,k,p))%p
        if k<m:
            inv=pow(k+1,-1,p)
            c1=c1*(m-k)*inv%p
            c2=c2*(2*m-k)*inv%p
    # Direct rational x-branch sum.
    S=sum(pow(((x+1)**2*(x+2)*pow(x,-2,p))%p,m,p)
          for x in range(1,p) if x not in (p-1,p-2))%p
    assert J==(-pow(2,-m,p)*S)%p,(p,J,S)
    # Independent Dickson/character v-sum.
    A=T=orbit_count=0
    for v in range(p):
        if v==3:continue
        t=(v-3)%p; tinv=pow(t,-1,p)
        u=(t+5+7*inv2*tinv+inv2*tinv*tinv)%p
        dm=dickson(u,m,p)
        disc=(v*v-8)%p
        leg=pow(disc,(p-1)//2,p)
        assert leg in (1,p-1)
        if leg==1:orbit_count+=1
        A=(A+dm)%p
        T=(T+(1 if leg==1 else -1)*dm)%p
    assert orbit_count==(p-3)//2
    C=ct_dickson(m,p)
    assert A==(-C)%p,(p,A,C)
    assert J==pow(2,-m-1,p)*(C-T)%p,(p,J,C,T)
    return p,m,J,A,T,C,orbit_count

def main():
    tests=[p for p in range(13,1001) if p%24 in (13,19) and prime(p)]
    tests += [10069,10099]
    rows=[check(p) for p in tests]
    assert len(tests)==47 and all(x[2]==0 for x in rows)
    print('PASS: %d primes, including both target residue classes.'%len(rows))
    for row in rows:
        if row[0] in (13,19,37,43,373,997,10069,10099):
            print(row)

if __name__=='__main__':main()
