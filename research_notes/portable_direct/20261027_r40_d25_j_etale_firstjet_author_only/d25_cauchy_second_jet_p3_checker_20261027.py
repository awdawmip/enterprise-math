"""Reproduce D25 Cauchy finite second jet mod p^3; author-side, not native H0/B0."""
from math import comb
import json

def mul(a,b,q):
    o=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: o[i+j]=(o[i+j]+x*y)%q
    return o

def tail(a,p,q):
    return sum((3*n-1)*x for n,x in enumerate(a) if n>=p)%q

def check(p):
    q=p**3; m=(p-1)//2; a=(p-1)//3; b=(2*p+2)//3
    c=[1]
    for k in range(1,p):
        num=(3*k)*(3*k-1)*(3*k-2)*(2*k)*(2*k-1)
        c.append(c[-1]*num*pow(216*k**5,-1,q)%q)
    u=[1]
    for j in range(1,p): u.append(u[-1]*(2*j-1)*pow(4*j,-1,q)%q)
    P=[comb(m,i)*pow(-2,-i,q)%q for i in range(m+1)]
    L=[0]+[pow(i*pow(2,i,q),-1,q) for i in range(1,p)]
    LL=mul(L,L,q)
    rho=pow(2**(m+1),-1,q)
    ell=sum(L)%q; d=(1-pow(pow(2,p-1,q),-1,q))%q
    E=(1+p*pow(2,-1,q)*ell+p*p*pow(8,-1,q)*ell*ell)%q
    C=sum(c)%q; W=sum((6*k+1)*x for k,x in enumerate(c))%q
    C2=[0]*(m+1)+c[m+1:b]
    F=tail(mul(P,C2,q),p,q)
    G=tail(mul(mul(P,c[:m+1],q),L,q),p,q)
    H=tail(mul(mul(P,c[:a+1],q),LL,q),p,q)
    formula=(rho*((W-3*p*C)*E+3*p*C*d)-F-p*pow(2,-1,q)*G-p*p*pow(8,-1,q)*H)%q
    S=sum((3*(j+k)-1)*u[j]*c[k] for k in range(p) for j in range(p-k))%q
    PL=mul(P,L,q); PLL=mul(P,LL,q)
    U2=[((P[i] if i<len(P) else 0)+p*pow(2,-1,q)*(PL[i] if i<len(PL) else 0)+p*p*pow(8,-1,q)*(PLL[i] if i<len(PLL) else 0))%q for i in range(p)]
    assert all((U2[j]-u[j])%q==0 for j in range(p)),(p,"jet")
    assert formula==S,(p,"formula",formula,S)
    assert d%p==0 and all(c[k]%p==0 for k in range(a+1,p))
    assert all(c[k]%(p*p)==0 for k in range(m+1,p))
    assert all(c[k]%q==0 for k in range(b,p))
    assert tail(mul(P,c,q),p,q)==F
    assert (tail(mul(mul(P,c,q),L,q),p,q)-G)%(p*p)==0
    assert (tail(mul(mul(P,c,q),LL,q),p,q)-H)%p==0
    D=(S-W)%q
    return {"p":p,"S_mod_p3":S,"W_mod_p3":W,"diff_mod_p3":D,
            "diff_over_p2_mod_p":D//(p*p) if D%(p*p)==0 else None}

if __name__=="__main__":
    primes=[5,7,11,13,19,31,37,43,61,67,73,79,103,109,211,373,997]
    print(json.dumps({"status":"PASS","scope":"AUTHOR_EXACT_CHECKED / NOT_NATIVE",
      "checks":[check(p) for p in primes]},indent=2))
