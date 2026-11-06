"""Exact inert sixth-character 3-value orbit classification and finite balance test."""
from math import comb, isqrt

def prime(p):
    return p>1 and all(p%d for d in range(2,isqrt(p)+1))

def run(p):
    assert p>3 and prime(p) and p%6==1 and pow(2,(p-1)//2,p)==p-1
    m=(p-1)//6
    c=pow(2,-m,p)
    mu6=[v for v in range(1,p) if pow(v,6,p)==1]
    assert len(mu6)==6 and pow(c,3,p)==p-1
    sigmas={(v+c*pow(v,-1,p))%p for v in mu6}
    assert len(sigmas)==3 and 0 in sigmas
    t=min(v for v in sigmas if v)
    assert sigmas=={0,t,(-t)%p}
    labels={-1:0,0:0,1:0}
    seen=set()
    cover=set()
    half=pow(2,-1,p)
    branches={0,p-1,-half%p}
    for x in range(p):
        if x in branches or x in seen:continue
        tx=(-(2*x+1)*pow(2*(x+1),-1,p))%p
        assert tx not in branches and tx!=x
        seen.update((x,tx))
        cover.update((x,tx))
        f=pow(x,5,p)*pow(x+1,2,p)*(2*x+1)%p
        v=pow(f,m,p)
        assert v in mu6
        s=(v+c*pow(v,-1,p))%p
        assert s in sigmas
        label=0 if not s else (1 if s==t else -1)
        labels[label]+=1
    assert len(cover)==p-3 and sum(labels.values())==(p-3)//2
    S=sum(comb(m,k)*comb(2*m+k,k) for k in range(m+1))%p
    assert S==(-t*(labels[1]-labels[-1]))%p
    assert (S==0)==(labels[1]==labels[-1])
    return p,t,labels[1],labels[-1],labels[0],S

if __name__=="__main__":
    vals=[run(p) for p in range(7,2000) if p%6==1 and prime(p) and pow(2,(p-1)//2,p)==p-1]
    assert len(vals)==77 and all(x[2]==x[3] for x in vals)
    print("PASS",len(vals),"inert primes; 3-valued orbit identity and finite count equality")
    for v in vals:
        if v[0] in (13,19,37,43,67,109,139,373):print(v)
