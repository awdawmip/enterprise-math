"""R5 N^20 coefficient for the q=±i pole pair; exact Gaussian-integer arithmetic.
Fixed source: 256 named hypotheses, repeatable prices 214..314.
Run: python VERIFY_N20.py
"""
from fractions import Fraction
from itertools import product
from math import comb

S0=(214,215,216,217,218)
S1=(214,216,217,218,219,220,221)
S2=(215,216,217,218,219,220,221)
SETS=tuple(map(set,(S0,S1,S2)))
E0=tuple(range(219,315))
E1=(215,)+tuple(range(222,315))
E2=(214,)+tuple(range(222,315))
EH=tuple(range(222,315))

def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def scale(a,x):return a[0]*x,a[1]*x
def rotate(a,k):
    x,y=a
    return ((x,y),(-y,x),(-x,-y),(y,-x))[k%4]

ZERO=(0,0)
ID=(1,0)
Z4=(ZERO,)*4
I4=(ID,ZERO,ZERO,ZERO)

def add4(x,y):return tuple(add(a,b) for a,b in zip(x,y))

def multiply_monomial(a,c):
    # q=i(1-s), so q^c=i^c * sum_r (-1)^r binom(c,r) s^r.
    t=tuple(rotate(x,c) for x in a)
    return tuple(
        tuple(sum(t[k][part]*((-1)**(r-k))*comb(c,r-k) for k in range(r+1)) for part in (0,1))
        for r in range(4))

def event_moments(S,m):
    dp={0:I4}
    for p in S:
        nd={}
        for count, a in dp.items():
            for n in range(m-count):
                t=count+n
                nd[t]=add4(nd.get(t,Z4),multiply_monomial(a,p*n))
        dp=nd
    result=Z4
    for a in dp.values():result=add4(result,a)
    return result

def overlap_moments(m):
    dp={(0,0,0):I4}
    for p in range(214,222):
        mem=tuple(int(p in S) for S in SETS)
        nd={}
        for count,a in dp.items():
            for n in range(m):
                co=tuple(min(m,count[k]+n*mem[k]) for k in range(3))
                if sum(t<m for t in co)<2:continue
                nd[co]=add4(nd.get(co,Z4),multiply_monomial(a,p*n))
        dp=nd
    result=Z4
    for count,a in dp.items():
        weight=max(sum(t<m for t in count)-1,0)
        result=add4(result,tuple(scale(x,weight) for x in a))
    return result

def single_free_factor(p):
    # Normalize (1-q^p)^(-1) at q=i(1-s) as 1+u*s+v*s^2+...
    if p%4==0:
        u=Fraction(p-1,2)
        return (u,0),(u*u-Fraction((p-1)*(p-2),6),0)
    w=rotate(ID,p)
    d=add(ID,scale(w,-1))
    inv=scale((d[0],-d[1]),Fraction(1,d[0]**2+d[1]**2))
    rho=mul(w,inv)
    u=scale(rho,-p)
    v=add(mul(u,u),scale(rho,Fraction(p*(p-1),2)))
    return u,v

def free_bc(E):
    b,c=ZERO,ZERO
    for p in E:
        u,v=single_free_factor(p)
        c=add(c,add(v,mul(b,u)))
        b=add(b,u)
    return b,c

def free_bc_independent(E):
    # Independent logarithmic differentiation, no free-factor product recurrence.
    b,ell=ZERO,ZERO
    for p in E:
        if p%4==0:
            u=(Fraction(p-1,2),0)
            ell2=(u[0]*u[0]/2-Fraction((p-1)*(p-2),6),0)
        else:
            w=rotate(ID,p)
            d=add(ID,scale(w,-1))
            rho=mul(w,scale((d[0],-d[1]),Fraction(1,d[0]**2+d[1]**2)))
            u=scale(rho,-p)
            ell2=add(scale(mul(u,u),Fraction(1,2)),
                     scale(rho,Fraction(p*(p-1),2)))
        b=add(b,u)
        ell=add(ell,ell2)
    return b,add(ell,scale(mul(b,b),Fraction(1,2)))

def coefficients(m):
    assert m>=2 and m%2==0
    moments=(event_moments(S0,m),event_moments(S1,m),
             event_moments(S2,m),overlap_moments(m))
    assert moments[0][0]==ZERO
    frees=(E0,E1,E2,EH)
    leading=(24,23,23,23)
    multipliers=((1,0),(220,-220),(220,0),(-440,0))
    poles=[ZERO]*4  # 24,23,22,21
    for h,E,order,lam in zip(moments,frees,leading,multipliers):
        b,c=free_bc(E)
        for r in range(4):
            v=h[r]
            if r>=1:v=add(v,mul(b,h[r-1]))
            if r>=2:v=add(v,mul(c,h[r-2]))
            if order-r>=21:
                j=24-(order-r)
                poles[j]=add(poles[j],mul(lam,v))
    assert poles[0]==ZERO
    D,L,M=poles[1:]
    E=add(L,scale(D,Fraction(23,2)))
    T=add(add(M,scale(L,11)),scale(D,Fraction(391,6)))
    return D,E,T

def direct_event(S,m):
    out=Z4
    for ns in product(range(m),repeat=len(S)):
        if sum(ns)>=m:continue
        out=add4(out,multiply_monomial(I4,sum(p*n for p,n in zip(S,ns))))
    return out

def direct_overlap(m):
    out=Z4
    for ns in product(range(m),repeat=8):
        w=max(sum(sum(ns[p-214] for p in S)<m for S in SETS)-1,0)
        if w:
            v=multiply_monomial(I4,sum((p+214)*n for p,n in enumerate(ns)))
            out=add4(out,tuple(scale(x,w) for x in v))
    return out

def prior_D(m):
    if m%4==2:
        t=(m-2)//4
        return (t+1)*(436*t+656),-2*(t+1)
    t=(m-4)//4
    return 436*(t+1)*(t+2),220*(t+1)*(t+2)

if __name__=="__main__":
    expected_B=(((12780,-24),(Fraction(241568173,3),-306732)),
        ((12558,Fraction(169,2)),(Fraction(932657689,12),Fraction(4244773,4))),
        ((Fraction(25115,2),-23),(Fraction(233172997,3),-288834)),
        ((Fraction(24901,2),-23),(Fraction(229176226,3),-286373)))
    for free,want in zip((E0,E1,E2,EH),expected_B):
        assert free_bc(free)==want
        assert free_bc_independent(free)==want
    for m in (2,4):
        for S in (S0,S1,S2):
            assert event_moments(S,m)==direct_event(S,m)
        assert overlap_moments(m)==direct_overlap(m)
    prior_E={2:(8033772,-41336),4:(10499400,4893440),
             22:(134531112,-685096),24:(141021240,42794640)}
    for m in range(2,25,2):
        D,E,T=coefficients(m)
        assert D==prior_D(m)
        if m in prior_E:assert E==prior_E[m]
        print(m,"D=",D,"E=",E,"T=",T)
    print("PASS: 12 exact DP values, independent full-tuple m=2,4, all free second-order coefficients, prior regressions")
