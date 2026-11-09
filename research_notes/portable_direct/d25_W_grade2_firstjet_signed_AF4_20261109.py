"""D25: exact original 216 grade2 first-jet and signed AF4 second layer.
Run from research_notes/portable_direct next to previous first-bridge code.
No native benchmark, Source CLAIM, Result or review is asserted.
"""
from math import comb
from d25_W_grade2_finitefield_bridge_20261109 import primes_to, grade2_recurrence

def original_w2(p):
    m=(p-1)//6; mod=p**4
    return sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,mod) for n in range(3*m+1,4*m+1))%mod

def original_v2(p):
    mod=p**4
    return sum((8*n+1)*comb(4*n,2*n)*comb(2*n,n)**2*pow(2304,-n,mod) for n in range((p+1)//2,(3*p-1)//4+1))%mod

def signed_firstjet(p):
    m=(p-1)//6; N=m-1; n0=3*m+1; r=n0+1; mod=p*p
    f=1
    for i in range(1,n0+1): f=f*i%mod
    faclast=1
    for i in range(1,p): faclast=faclast*i%mod
    assert (faclast+1)%p==0
    wp=((faclast+1)//p)%p
    hr=sum(pow(i,-1,p) for i in range(1,r+1))%p
    K0=r*pow(f,-4,mod)*pow(216,-n0,mod)%mod
    K2=K0*(1+p*(1+hr-2*wp))%mod
    raw0=comb(2*n0,n0)**2*comb(3*n0,n0)*pow(216,-n0,p**4)%(p**4)
    assert raw0%(p*p)==0
    assert K2==raw0//(p*p)
    g,S=1,0
    total,J0=0,0
    for j in range(N+1):
        a=6*j+4
        J0=(J0+a*g)%p
        total=(total+g*(a+p*(3+a*S)))%mod
        if j<N:
            E=(pow(2*j+2,-1,p)+3*pow(6*j+5,-1,p)+3*pow(6*j+7,-1,p)-3*pow(2*j+3,-1,p))%p
            den=9*(2*j+3)**3
            g=g*(j+1)*(6*j+5)*(6*j+7)*pow(den,-1,mod)%mod
            S=(S+E)%p
    return K2,total,K2*total%mod,J0,wp,hr

def run(limit=1000):
    out={}
    for p in primes_to(limit):
        raw=original_w2(p)
        assert raw%(p*p)==0
        w=raw//(p*p)
        K2,J,jet,J0,wp,hr=signed_firstjet(p)
        assert w==jet,(p,w,jet)
        assert w%p==grade2_recurrence(p),(p,w)
        v=original_v2(p)
        assert v%(p**3)==0,(p,v,"V2")
        q=v//(p**3)
        b=(w-2*p*q)%(p*p)
        out[p]=(K2,J,w,q,b,J0,wp,hr)
    return out

if __name__=="__main__":
    out=run()
    print("FIRSTJET PASS",len(out),"p=1 mod6 primes up to 1000")
    for p in (7,13,19,37,43,73,373,379,997):
        if p in out: print(p,out[p])
