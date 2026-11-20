#!/usr/bin/env python3
"""EC49FUU: exact polynomial/Bernstein certificate for n=30 pure-E high-width phase.

Standard library only. Every sign check uses fractions.Fraction. 14 full intervals;
no floating point or sampled assertions enter the proof.
"""
from fractions import Fraction as F
from math import comb

N = 30
B = F(3, 637)
E = F(31597745, 1653649)
U_A, U_B, U_C = 21829245984, 45529434409, 456083905
DEN = 10**12
# Rational strict root brackets from EC49FUT, here independently rechecked.
BRACKETS = {
    16:(433405288408,433405288409),
    17:(474356338011,474356338012),
    18:(515357839408,515357839409),
    19:(556358678282,556358678283),
    20:(597318517188,597318517189),
    21:(638205356397,638205356398),
    22:(678993711821,678993711822),
    23:(719663237873,719663237874),
    24:(760197675211,760197675212),
    25:(800584038553,800584038554),
    26:(840811983841,840811983842),
    27:(880873310863,880873310864),
    28:(920761569134,920761569135),
    29:(960471743261,960471743262),
}

def add(a,b):
    return tuple((a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b))))

def neg(a): return tuple(-v for v in a)
def sub(a,b): return add(a, neg(b))

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        if not v: continue
        for j,w in enumerate(b):
            if w: out[i+j]+=v*w
    return tuple(out)

def scale(a,t): return tuple(t*v for v in a)

def powers(a):
    out=[(F(1),)]
    for _ in range(N): out.append(mul(out[-1],a))
    return out

def prob_polys(theta):
    u=F(U_A,1)/(F(U_B)-U_C*theta)
    # T(x)=(1-x)(1+B*(theta-1)*x)=1+(B*(theta-1)-1)x-B*(theta-1)x^2
    b=B*(theta-1)
    T=(F(1), b-1, -b)
    p=sub((F(1),),T)
    q=sub((F(1),),scale(T,u))
    return p,q

def signed_mass_polys(theta):
    p,q=prob_polys(theta)
    pp,qp = powers(p),powers(q)
    pm,qm = powers(sub((F(1),),p)), powers(sub((F(1),),q))
    return [scale(sub(mul(qp[k],qm[N-k]),mul(pp[k],pm[N-k])),comb(N,k)) for k in range(N+1)]

def eval_poly(a,x):
    v=F(0)
    for c in reversed(a):v=v*x+c
    return v

def delta_eval(k,x,theta):
    u=F(U_A,1)/(F(U_B)-U_C*theta)
    T=(1-x)*(1-B*x+B*x*theta)
    p,q=1-T,1-u*T
    return comb(N,k)*(q**k*(1-q)**(N-k)-p**k*(1-p)**(N-k))

def bernstein_coeffs(poly,a,b):
    # Express poly(a+(b-a)t) in powers of t by exact Horner, then
    # convert t^r = sum_{k=r}^d C(k,r)/C(d,r)*B_{k,d}(t).
    # Drop polynomial leading zeros to preserve exact degree.
    poly=list(poly)
    while len(poly)>1 and poly[-1]==0: poly.pop()
    d=len(poly)-1
    transformed=(F(0),)
    for c in reversed(poly):
        transformed=add(mul(transformed,(a,b-a)),(c,))
    transformed=transformed[:d+1]
    assert len(transformed)==d+1
    # Fundamental transform identity: the endpoint values agree exactly.
    assert transformed[0]==eval_poly(poly,a)
    assert sum(transformed,F(0))==eval_poly(poly,b)
    out=[]
    for k in range(d+1):
        out.append(sum((transformed[r]*F(comb(k,r),comb(d,r)) for r in range(k+1)),F(0)))
    assert out[0]==eval_poly(poly,a)
    assert out[-1]==eval_poly(poly,b)
    return out

def divide_one_minus_x(poly):
    assert sum(poly,F(0))==0
    out=[]; accum=F(0)
    for c in poly[:-1]:
        accum+=c
        out.append(accum)
    assert poly[-1]==-accum
    return tuple(out)

def verify():
    assert 0<E and 0<B<1
    for k,(lo,hi) in BRACKETS.items():
        a,b=F(lo,DEN),F(hi,DEN)
        assert 0<a<b<1
        assert delta_eval(k,a,E)>0>delta_eval(k,b,E), ('root bracket',k)
    for k in range(16,29):
        assert BRACKETS[k][1] < BRACKETS[k+1][0]
    Z,E_mass=signed_mass_polys(F(0)),signed_mass_polys(E)
    g={}; cumulZ=(F(0),);cumulE=(F(0),)
    for j in range(N,-1,-1):
        cumulZ=add(cumulZ,Z[j]);cumulE=add(cumulE,E_mass[j])
        g[j]=sub(cumulE,cumulZ)
    assert all(v==0 for v in g[0]), 'total signed-mass difference must vanish'
    details=[]
    for j in range(17,31):
        a=F(BRACKETS[j-1][0], DEN)
        b=F(BRACKETS[j][1], DEN) if j<=29 else F(1)
        poly=neg(g[j])
        if j==30:
            # remove its exact zero at x=1 and prove -(G_30)/(1-x)>0
            poly=divide_one_minus_x(poly)
        coeff=bernstein_coeffs(poly,a,b)
        assert all(c>0 for c in coeff), ('nonpositive Bernstein coefficient',j)
        details.append((j,len(coeff),len(poly)-1,a,b))
        print('PASS j=%2d Bernstein=%d/%d positive, degree=%d, interval=[%s,%s]%s'%(
          j,len(coeff),len(coeff),len(poly)-1,a,b,' G/(1-x)' if j==30 else ''),flush=True)
    # Check one exact representative against direct binomial tails, catching
    # accidental coefficient-vs-probability representation errors.
    for j,count,deg,a,b in details:
        test=(a+b)/2
        direct=sum((delta_eval(k,test,E)-delta_eval(k,test,F(0)) for k in range(j,N+1)),F(0))
        assert eval_poly(g[j],test)==direct
        assert direct<0
    assert len(details)==14 and sum(r[1] for r in details)==853
    print('ALL PASS: 14 complete rational intervals; 853 strictly positive Bernstein coefficients; roots 16..29 independently bracketed')

if __name__=='__main__':verify()
