"""Exact p-adic source-carry certificates for frozen D25 216/2304 Gauss squares.
Pure modular arithmetic; no native Enterprise Math authority is asserted.
"""
from __future__ import annotations

def is_prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))

def coeffs(p: int, family: str) -> list[int]:
    mod=p**3
    out=[1]
    for k in range(p-1):
        if family == "A":
            num,den=(6*k+1)*(3*k+1),18*(k+1)**2
        elif family == "B":
            num,den=(8*k+1)*(8*k+3),64*(k+1)**2
        else: raise ValueError(family)
        out.append(out[-1]*num*pow(den,-1,mod)%mod)
    return out

def v(x: int, p: int) -> int:
    if x%(p**3)==0: return 3
    if x%(p**2)==0: return 2
    if x%p==0: return 1
    return 0

def strata(p: int, family: str, k: int) -> int:
    if family=="A":
        m=(p-1)//6
        return int(k>m)+int(k>2*m)
    if p%8==3:
        r,s=(p-3)//8,(3*p-1)//8
    else:
        r,s=(5*p-1)//8,(7*p-3)//8
    return int(k>r)+int(k>s)

def carry(vals: list[int], p: int) -> list[int]:
    out=[0]*(2*p-1)
    for i,a in enumerate(vals):
        for j in range(max(p-i,0),p):
            out[i+j]=(out[i+j]+a*vals[j])%(p**3)
    return out

def check(p: int) -> dict:
    assert is_prime(p) and p%24 in (13,19)
    a=coeffs(p,"A"); b=coeffs(p,"B")
    for family,cs in (("A",a),("B",b)):
        assert all(v(x,p)==strata(p,family,i) for i,x in enumerate(cs))
    ca=carry(a,p);cb=carry(b,p);m=(p-1)//6
    at=p-1+m
    assert all(x%(p*p)==0 for x in ca[p:])
    assert all(x==0 for x in ca[at+1:])
    assert v(ca[at],p)==2 and ca[at]==(2*a[m]*a[p-1])%(p**3)
    result={"p":p,"A_top":at,"A_unit":ca[at]//(p*p)}
    if p%8==3:
        r=(p-3)//8; bt=p-1+r
        assert all(x%(p*p)==0 for x in cb[p:])
        assert all(x==0 for x in cb[bt+1:])
        assert v(cb[bt],p)==2 and cb[bt]==2*b[r]*b[p-1]%(p**3)
        result.update(B_degree_p=None,B_degree_p2=None,B_degree_p3=bt,B_unit=cb[bt]//(p*p))
    else:
        r=(5*p-1)//8;s=(7*p-3)//8;d0=2*r;d1=r+s;d2=2*s
        assert all(x%p==0 for x in cb[d0+1:])
        assert all(x%(p*p)==0 for x in cb[d1+1:])
        assert all(x==0 for x in cb[d2+1:])
        assert v(cb[d0],p)==0 and v(cb[d1],p)==1 and v(cb[d2],p)==2
        assert cb[d0]%p==b[r]*b[r]%p
        assert cb[d1]%(p*p)==2*b[r]*b[s]%(p*p)
        assert cb[d2]==b[s]*b[s]%(p**3)
        U0=cb[d0]%p; U1=(cb[d1]//p)%p; U2=(cb[d2]//(p*p))%p
        assert U1==5%p and 4*U0*U2%p==25%p
        result.update(B_degree_p=d0,B_degree_p2=d1,B_degree_p3=d2,U0=U0,U1=U1,U2=U2)
    return result

if __name__=="__main__":
    primes=[p for p in range(13,500) if p%24 in (13,19) and is_prime(p)]
    r={p:check(p) for p in primes}
    assert len(r)==23
    print("EXACT_REGRESSION",len(r),"PASS", "range p<500")
    for p in (13,19,37,43,109,373):
        print(r[p])
