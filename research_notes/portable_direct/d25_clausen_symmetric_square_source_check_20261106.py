#!/usr/bin/env python3
"""D25 finite symmetric-square 216-operator source: exact rational and p².
Portable author-side check; not original H0/B0 native execution.
"""
from fractions import Fraction
def coeffs(m,mod=None):
    def rat(a,b):return Fraction(a,b) if mod is None else a*pow(b,-1,mod)%mod
    d=[rat(1,1)]
    for i in range(m):
        q=rat((6*i+1)*(3*i+1),36*(i+1)**2)
        d.append(d[-1]*q if mod is None else d[-1]*q%mod)
    e=[rat(0,1),rat(1,10)]
    for r in range(1,m):
        q=rat(36*r*r,(6*r+5)*(3*r+2))
        e.append(e[-1]*q if mod is None else e[-1]*q%mod)
    return d,e
def go(m,p=None,diagnostic=False):
    mod=None if p is None else p*p
    p=6*m+1 if p is None else p
    d,e=coeffs(m,mod)
    c={}
    for i in range(m+1):
        for r in range(1,m+1):
            k=i-r
            c[k]=c.get(k,0)+d[i]*e[r]
    def reduced(x):return x if mod is None else x%mod
    def dv(k):return d[k] if 0<=k<=m else 0
    def ev(k):return e[k] if 1<=k<=m else 0
    B=36*m*m*e[m]; A=p*(3*m+1)*d[m]
    def src(k):return -3*k*dv(k)+B*(3*k+2*m)*dv(k+m)-A*(3*k-2*m-2)*ev(m+1-k)
    def fac(k):return (2*k-1)*(3*k-2)*(3*k-1)
    for k in range(-m,m+1):
        lhs=36*k**3*c.get(k,0)-fac(k)*c.get(k-1,0)
        assert reduced(lhs-src(k))==0,(p,k)
    rec={m:0}
    for k in range(m,0,-1):
        t=36*k**3*rec[k]-src(k)
        rec[k-1]=t/fac(k) if mod is None else t*pow(fac(k),-1,mod)%mod
        assert reduced(rec[k-1]-c.get(k-1,0))==0,(p,k,"backward")
    J=sum((1+6*k)*rec[k] for k in range(m))
    assert reduced(J-sum((1+6*k)*c.get(k,0) for k in range(m)))==0
    if diagnostic and mod:
        noA={m:0}
        for k in range(m,0,-1):
            other=-3*k*dv(k)+B*(3*k+2*m)*dv(k+m)
            noA[k-1]=(36*k**3*noA[k]-other)*pow(fac(k),-1,mod)%mod
        removed=sum((1+6*k)*noA[k] for k in range(m))%mod
        print("ablation",p,"true",J%mod,"without_low_endpoint",removed,
              "difference_over_p",((J-removed)%mod)//p)
    return J if mod is None else J%p
def prime(n):return n>1 and all(n%k for k in range(2,int(n**0.5)+1))
def main():
    for m in range(1,9): print("rational",m,"J",go(m))
    ps=[q for q in range(7,998) if q%6==1 and prime(q)]
    assert len(ps)==80
    for q in ps:
        r=go((q-1)//6,q)
        if q in (13,19,67,373):print("prime",q,"J",r)
    assert go(3,19)==6 and go(62,373)==98
    go(3,19,True);go(62,373,True)
    print("ALL_CHECKS_PASS",len(ps))
if __name__=="__main__":main()
