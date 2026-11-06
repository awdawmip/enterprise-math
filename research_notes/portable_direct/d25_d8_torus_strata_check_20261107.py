"""D25 exact D8 torus strata certificate (independent Python stdlib).
The native p373 H0/B0/Frobenius benchmark is not executed.
"""
from collections import Counter
from math import isqrt, gcd

def primes(n):
    a=bytearray(b'\1')*(n+1); a[:2]=b'\0\0'
    for i in range(2,isqrt(n)+1):
        if a[i]: a[i*i::i]=b'\0'*((n-i*i)//i+1)
    return [i for i in range(n+1) if a[i]]

def factors(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1; n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out

def phi(n):
    for q in factors(n): n=n//q*(q-1)
    return n

def mul(a,b,p):
    return ((a[0]*b[0]-a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)

def pow_pair(a,n,p):
    z=(1,0)
    while n:
        if n&1: z=mul(z,a,p)
        a=mul(a,a,p); n>>=1
    return z

def signed_order_2(d):
    t=1
    for L in range(1,d+1):
        t=t*2%d
        if t in (1,d-1): return L
    raise AssertionError(d)

def divisors(n):
    ds=[1]
    for q,e in factors(n).items(): ds=[d*q**k for d in ds for k in range(e+1)]
    return ds

def check(p):
    assert p%24 in (13,19)
    M=(p-1)//4 if p%4==1 else (p+1)//4
    assert M%2==1
    m=(p-1)//6; inv2=pow(2,-1,p)
    def T(y): return (y-1)*pow(y+1,-1,p)%p
    def J(y):
        d=(y*y+1)%p
        return None if d==0 else 4*y*y*(y*y-1)**2*pow(d,-4,p)%p
    def P(j): return None if j is None else 4*j*(1-4*j)%p
    def v(y):
        x=(y-1)*inv2%p
        return pow(x**5*(x+1)**2*y,m,p)
    X=set(range(2,p-1)); seen=set(); j_orbits={}
    for first in sorted(X):
        if first in seen: continue
        O={first}; work=[first]
        while work:
            y=work.pop()
            for z in (-y%p,T(y)):
                if z not in O: O.add(z); work.append(z)
        assert not O&seen
        seen|=O
        js={J(y) for y in O}
        assert len(js)==1
        j=js.pop()
        assert j not in j_orbits
        j_orbits[j]=O
    assert seen==X
    signed={j:sum(v(y) for y in O)%p for j,O in j_orbits.items()}
    assert {P(j) for j in j_orbits}==set(j_orbits)
    orders={}
    for j,O in j_orbits.items():
        if j is None:
            assert p%24==13 and len(O)==2
            continue
        assert len(O)==8
        y=min(O); den=(y*y+1)%p
        r=(y*y-1)*pow(den,-1,p)%p
        w=2*y*pow(den,-1,p)%p
        assert (r*r+w*w)%p==1
        h=pow_pair((r,w),4,p)
        assert pow_pair(h,M,p)==(1,0)
        d=M
        for q in factors(M):
            while d%q==0 and pow_pair(h,d//q,p)==(1,0):
                d//=q
        assert d>1
        orders[j]=d
        z3=pow_pair((r,w),3,p)
        assert z3[0]**2*z3[1]**2%p == j*(16*j-3)**2%p
        d3=d//gcd(d,3)
        j3=j*(16*j-3)**2%p
        if d3==1: assert j3==0
        else: assert j3 in j_orbits
    actual=Counter(); cycles=[]; visited=set()
    for first in j_orbits:
        if first in visited: continue
        seq=[];j=first
        while j not in visited:
            visited.add(j);seq.append(j);j=P(j)
        assert j==first
        cycles.append(seq)
        if seq==[None]:
            actual[('exception',1)]+=1
        else:
            ds={orders[t] for t in seq}
            assert len(ds)==1
            d=ds.pop()
            assert len(seq)==signed_order_2(d)
            actual[(d,len(seq))]+=1
    predicted=Counter()
    for d in divisors(M):
        if d==1: continue
        L=signed_order_2(d)
        assert phi(d)%(2*L)==0
        predicted[(d,L)]+=phi(d)//(2*L)
    if p%24==13: predicted[('exception',1)]+=1
    assert actual==predicted,(p,actual,predicted)
    return M,cycles,signed,orders,actual

if __name__=='__main__':
    ps=[p for p in primes(1999) if p%24 in (13,19)]
    assert len(ps)==77
    results={p:check(p) for p in ps}
    for p in (19,43,61,373):
        M,cycles,signed,orders,actual=results[p]
        print('p',p,'M',M,'strata',sorted((str(k),v) for k,v in actual.items()))
    M,cycles,signed,orders,actual=results[61]
    print('p61 nonzero-cycle strata:',[(orders[c[0]],c,[signed[j] for j in c]) for c in cycles
                                         if c[0] is not None and any(signed[j] for j in c)])
    print('p61 cubing transfer: J49 ->',49*(16*49-3)**2%61,
          'source A49=',signed[49],'target A41=',signed[41])
    print('verified',len(ps),'target primes, zero cycle-stratum failures')
