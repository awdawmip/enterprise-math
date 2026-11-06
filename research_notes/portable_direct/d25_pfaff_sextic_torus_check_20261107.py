"""Exact Pfaff sextic field, projective involution, and nonsplit norm-one torus verification.
Only integer / finite-field operations; not the original p=373 native H0/B0 benchmark.
"""
from math import comb, isqrt

def isprime(p):
    return p >= 2 and all(p % k for k in range(2, isqrt(p) + 1))

def value(x, p):
    return (pow(x, 5, p) * pow(x + 1, 2, p) * (2*x + 1)) % p

def pair_product_witness(p):
    x = 1
    t = (-(2*x+1) * pow(2*(x+1), -1, p)) % p
    m = (p-1)//6
    return (x, t, pow(value(x,p),m,p), pow(value(t,p),m,p))

def fp2_mul(a, b, p):
    return ((a[0]*b[0]+2*a[1]*b[1])%p,
            (a[0]*b[1]+a[1]*b[0])%p)

def fp2_inv(a, p):
    norm = (a[0]*a[0]-2*a[1]*a[1])%p
    return (a[0]*pow(norm,-1,p)%p, -a[1]*pow(norm,-1,p)%p)

def normone_witness(p):
    # Inert field F_p[r]/(r*r-2), z=(x-alpha)/(x-beta)
    assert pow(2,(p-1)//2,p)==p-1
    inv2=pow(2,-1,p)
    alpha=(-1,inv2)
    beta=(-1,-inv2)
    seen=set()
    for x in range(p):
        n=((x-alpha[0])%p,-alpha[1]%p)
        d=((x-beta[0])%p,-beta[1]%p)
        z=fp2_mul(n,fp2_inv(d,p),p)
        assert fp2_mul(z,(z[0],-z[1]),p)==(1,0)
        assert z not in seen
        seen.add(z)
        if x not in (0,p-1,(-inv2)%p):
            t=(-(2*x+1)*pow(2*(x+1),-1,p))%p
            nn=((t-alpha[0])%p,-alpha[1]%p)
            dd=((t-beta[0])%p,-beta[1]%p)
            zt=fp2_mul(nn,fp2_inv(dd,p),p)
            assert zt==((-z[0])%p,(-z[1])%p)
    assert len(seen)==p
    assert (1,0) not in seen
    return True

def check(p):
    assert isprime(p) and p%6==1 and p>3
    m=(p-1)//6
    S=sum(comb(m,k)*comb(2*m+k,k) for k in range(m+1))%p
    A=sum(pow(value(x,p),m,p) for x in range(p))%p
    B=sum(pow(value(x,p),5*m,p) for x in range(p))%p
    assert S==(-A)%p
    assert A==(pow(2,-m,p)*B)%p
    points=set(range(p))|{p}  # p encodes projective infinity
    def tau(x):
        if x==p: return p-1
        if x==p-1: return p
        return (-(2*x+1)*pow(2*(x+1),-1,p))%p
    branches={0,p-1,(-pow(2,-1,p))%p,p}
    assert {tau(x) for x in branches}==branches
    seen=set()
    orbit_sum=0
    fpcount=0
    paircount=0
    for x in points:
        t=tau(x)
        assert tau(t)==x
        if x==t: fpcount+=1
        if x in branches or x in seen: continue
        assert t not in branches
        seen.update((x,t))
        if x!=t: paircount+=1
        if x!=t:
            lhs=value(x,p)*value(t,p)%p
            rhs=pow(x*(2*x+1)*pow(x+1,-1,p),6,p)*pow(128,-1,p)%p
            assert lhs==rhs
        vx=pow(value(x,p),m,p)
        vt=pow(value(t,p),m,p)
        assert vt==(pow(2,-m,p)*pow(vx,-1,p))%p
        orbit_sum=(orbit_sum+vx+(0 if t==x else vt))%p
    assert orbit_sum==A
    assert 2*paircount+fpcount==p-3
    if pow(2,(p-1)//2,p)==p-1:
        assert fpcount==0 and paircount==(p-3)//2
    else:
        assert fpcount==2 and paircount==(p-5)//2
    if p in (13,19,373):
        normone_witness(p)
    return dict(p=p,m=m,S=S,A=A,B=B,fixed_points=fpcount,
                pairs=paircount,two_character=pow(2,(p-1)//2,p),
                x1_orbit=pair_product_witness(p))

if __name__=="__main__":
    rows=[check(p) for p in range(7,2000) if p%6==1 and isprime(p)]
    rows.append(check(5113))
    assert len(rows)==149
    inert=[r for r in rows if r['two_character']==r['p']-1]
    assert len(inert)==77
    assert all(r['S']==0 for r in inert)  # finite observation, not theorem
    print("PASS",len(rows),"exact primes; inert",len(inert),"finite zero-port observations")
    for r in rows:
        if r['p'] in (7,13,19,31,67,373,5113): print(r)
