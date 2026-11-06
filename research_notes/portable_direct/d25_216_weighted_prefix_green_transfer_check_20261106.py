#!/usr/bin/env python3
"""D25 exact original 216 weighted-prefix Green transfer.
Portable author-side calculation, not native H0/B0 original-class benchmark.
"""
from fractions import Fraction
def arrays(m,mod=None):
    def rat(a,b):return Fraction(a,b) if mod is None else a*pow(b,-1,mod)%mod
    d=[rat(1,1)];e=[rat(0,1),rat(1,10)];a=[rat(1,1)]
    for i in range(m):
        q=rat((6*i+1)*(3*i+1),36*(i+1)**2)
        d.append(d[-1]*q if mod is None else d[-1]*q%mod)
    for r in range(1,m):
        q=rat(36*r*r,(6*r+5)*(3*r+2))
        e.append(e[-1]*q if mod is None else e[-1]*q%mod)
    for k in range(1,m+1):
        q=rat((2*k-1)*(3*k-2)*(3*k-1),36*k**3)
        a.append(a[-1]*q if mod is None else a[-1]*q%mod)
    return d,e,a,rat
def verify(m,p=None):
    mod=None if p is None else p*p
    p=6*m+1 if p is None else p
    d,e,a,rat=arrays(m,mod)
    A=p*(3*m+1)*d[m]
    P=[0]
    for k in range(m):P.append(P[-1]+(6*k+1)*a[k])
    bulk=0;endpoint=0
    for t in range(1,m+1):
        inv_a=1/a[t] if mod is None else pow(a[t],-1,mod)
        factor=rat(1,36*t**3)*inv_a*P[t]
        bulk+=3*t*d[t]*factor
        endpoint+=A*(3*t-2*m-2)*e[m+1-t]*factor
    direct=sum((1+6*(i-r))*d[i]*e[r]
               for i in range(1,m+1) for r in range(1,i+1))
    if mod is None:
        assert bulk+endpoint==direct,(m,"rational")
        return direct,bulk,endpoint
    assert (bulk+endpoint-direct)%mod==0,(p,"modular")
    return direct%mod,bulk%mod,endpoint%mod
def prime(p):return p>1 and all(p%k for k in range(2,int(p**0.5)+1))
def main():
    for m in range(1,9):
        j,b,e=verify(m)
        print("rational",m,"J",j,"bulk",b,"endpoint",e)
    primes=[p for p in range(7,998) if p%6==1 and prime(p)]
    assert len(primes)==80
    for p in primes:
        j,b,e=verify((p-1)//6,p)
        if p in (13,19,67,373):print("modp2",p,j,b,e)
    assert verify(3,19)[0]%19==6
    assert verify(62,373)[0]%373==98
    print("ALL_CHECKS_PASS",len(primes))
if __name__=="__main__":main()
