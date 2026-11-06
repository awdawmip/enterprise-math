"""D25 exact finite Legendre and Gauss observer verification, author-side only.
Python 3 standard library, no external network or mathematical admission.
"""
import json
from pathlib import Path

def is_prime(n):
    if n<2: return False
    for d in range(2,int(n**0.5)+1):
        if n%d==0: return False
    return True

def binomial_factor(p):
    m=(p-1)//6
    b1=b2=zpow=1; f=1; t=0
    inv2=pow(2,-1,p)
    for k in range(1,m+1):
        b1=b1*(m-k+1)*pow(k,-1,p)%p
        b2=b2*(2*m-k+1)*pow(k,-1,p)%p
        zpow=zpow*inv2%p
        term=b1*b2*zpow%p
        f=(f+term)%p
        t=(t+k*term)%p
    return f,t

def legendre_pair(p):
    m=(p-1)//6; E=O=1; Oprev=None
    inv2=pow(2,-1,p)
    for k in range(m):
        Oprev=O
        E=((4*k+3)*inv2*O-(2*k+1)*E)*pow(2*k+2,-1,p)%p
        if k+1<m:
            O=((4*k+5)*E-(2*k+2)*O)*pow(2*k+3,-1,p)%p
    return E,Oprev

def gauss_mod_p2(p):
    q=p*p; d=1; S=1; T=0
    for n in range(p-1):
        d=d*(6*n+1)*(3*n+1)*pow(36*(n+1)*(n+1),-1,q)%q
        S=(S+d)%q; T=(T+(n+1)*d)%q
    return S,T

def main():
    entries=[]; count_all=count_inert=count_split=0
    for p in range(7,10008):
        if p%6!=1 or not is_prime(p): continue
        m=(p-1)//6
        f,t=binomial_factor(p); e,o=legendre_pair(p)
        assert f==e,(p,"transform",f,e)
        assert t==m*(e-o)%p,(p,"derivative")
        assert (f+12*t)%p==(2*o-e)%p,(p,"weighted observer")
        s2,t2=gauss_mod_p2(p)
        assert s2%p==f and t2%p==t
        k2=(s2+12*t2)%(p*p); k0=(2*o-e)%p
        chi2=pow(2,(p-1)//2,p); count_all+=1
        if chi2==p-1:
            assert p%24 in (13,19)
            assert f==0 and k0!=0,(p,"inert")
            assert s2%p==0 and (s2//p)*k0%p==1,(p,"first digit")
            count_inert+=1
            if p in (13,19,37,43,67,373,9973):
                entries.append(dict(p=p,chi2=-1,m=m,E=e,Oprev=o,K0=k0,T0=t,S_mod_p2=s2,divided=s2//p))
        else:
            assert chi2==1 and p%24 in (1,7)
            assert k0==0 and e!=0,(p,"split")
            assert k2%p==0 and e*(k2//p)%p==1,(p,"first digit")
            count_split+=1
            if p in (7,31,73,79,97,103):
                entries.append(dict(p=p,chi2=1,m=m,E=e,Oprev=o,K0=k0,T0=t,K_mod_p2=k2,divided=k2//p))
    results=dict(date="2026-11-06",task="D25 SECOND-DIGIT-LIFT",
        scientific_pin="c47e13e4aba0e006366f989d6334d443f6333ae3",
        bounded_domain="prime p=6m+1, 7<=p<=10007",
        counts=dict(total=count_all,chi2_negative=count_inert,chi2_positive=count_split,assertion_failures=0),
        status="FINITE_VERIFIED_NOT_UNIFORM_THEOREM_NOT_NATIVE_H0_B0_NOT_ADMITTED",samples=entries)
    Path(__file__).with_name("20261106_onhour_d25_legendre_split_channel_results.json").write_text(json.dumps(results,indent=2)+"\n")
    print(json.dumps(results,indent=2))

if __name__=="__main__": main()
