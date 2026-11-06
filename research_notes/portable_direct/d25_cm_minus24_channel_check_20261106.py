#!/usr/bin/env python3
"""Independent finite-field tests of the D25 CM(-24) channel theorem.
Integer modular arithmetic only, including Fp[u]/(2u*u-1).
The classical Deuring/CM input is a theorem used by the note, not proved by this test.
"""
def primes(n):
    a=[True]*(n+1); a[0]=a[1]=False
    for d in range(2,int(n**.5)+1):
        if a[d]:
            for x in range(d*d,n+1,d): a[x]=False
    return [p for p in range(7,n+1) if a[p] and p%6==1]

def ext_add(a,b,p): return ((a[0]+b[0])%p,(a[1]+b[1])%p)
def ext_mul(a,b,p):
    return ((a[0]*b[0]+a[1]*b[1]*pow(2,-1,p))%p,(a[0]*b[1]+a[1]*b[0])%p)
def eprod_poly(a,b,limit,p):
    out=[(0,0)]*min(len(a)+len(b)-1,limit+1)
    for i,ai in enumerate(a):
        if ai==(0,0): continue
        for j,bj in enumerate(b[:len(out)-i]):
            if bj!=(0,0): out[i+j]=ext_add(out[i+j],ext_mul(ai,bj,p),p)
    return out
def e_pow_poly(base,exp,limit,p):
    res=[(1,0)]
    while exp:
        if exp&1: res=eprod_poly(res,base,limit,p)
        exp//=2
        if exp: base=eprod_poly(base,base,limit,p)
    return res
def F_mod(p):
    m=(p-1)//6; z=pow(2,-1,p)
    t=1; sm=1
    for k in range(m):
        t=t*(m-k)*(2*m-k)*z*pow(k+1,-2,p)%p
        sm=(sm+t)%p
    return sm
def P_even_mod(p):
    m=(p-1)//6
    a=(1,0); b=(0,1)
    for n in range(1,2*m):
        nb=ext_add(ext_mul((0,2*n+1),b,p),((-n*a[0])%p,(-n*a[1])%p),p)
        c=((nb[0]*pow(n+1,-1,p))%p,(nb[1]*pow(n+1,-1,p))%p)
        a,b=b,c
    return b
def quartic_hasse(p,sign):
    # y²=(X+2*sign)(X³-3X-2u), u²=1/2, coefficients ascending.
    base=[(0,(-4*sign)%p),((-6*sign)%p,-2%p),(-3%p,0),
          (2*sign%p,0),(1,0)]
    return e_pow_poly(base,(p-1)//2,p-1,p)[p-1]
ps=primes(10007)
assert len(ps)==611, len(ps)
inert=0; elliptic_tested=0
for p in ps:
    f=F_mod(p); chi=pow(2,(p-1)//2,p)
    if chi==p-1: inert+=1
    assert (f==0)==(chi==p-1),(p,f,chi)
    if p<=199:
        even=P_even_mod(p)
        assert even==(f,0),(p,even,f)
        for sign in (1,-1):
            h=quartic_hasse(p,sign)
            assert (h==(0,0))==(chi==p-1),(p,sign,h,chi)
        elliptic_tested+=1
print({'primes':len(ps),'target_inert':inert,'split':len(ps)-inert,
       'elliptic_cases_each_quotient':elliptic_tested,'status':'PASS'})
for p in (7,13,19,31,37,43,67,139,373,997):
    print(p, 'chi2', -1 if pow(2,(p-1)//2,p)==p-1 else 1, 'F', F_mod(p),
          'quartic_Hasse_plus',quartic_hasse(p,1) if p<=199 else 'not tested')
