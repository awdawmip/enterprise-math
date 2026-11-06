#!/usr/bin/env python3
"""D25 exact rational + mod-p^2 two-port Green coefficient certificate.
This is an author-side portable finite test, NOT the p373 native H0/B0 run.
"""
from fractions import Fraction

def coeffs(m, mod=None):
    def rat(x, y):
        return Fraction(x,y) if mod is None else x*pow(y,-1,mod)%mod
    d=[rat(1,1)]
    for i in range(m):
        q=rat((6*i+1)*(3*i+1),36*(i+1)**2)
        d.append(d[-1]*q if mod is None else d[-1]*q%mod)
    e=[rat(0,1),rat(1,10)]
    for r in range(1,m):
        q=rat(36*r*r,(6*r+5)*(3*r+2))
        e.append(e[-1]*q if mod is None else e[-1]*q%mod)
    return d,e

def verify(m, p=None):
    mod = None if p is None else p*p
    d,e=coeffs(m,mod)
    p=6*m+1 if p is None else p
    w,c={},{}
    for i in range(m+1):
        for r in range(1,m+1):
            k=i-r
            x=d[i]*e[r]
            w[k]=w.get(k,0)-(i+r)*x
            c[k]=c.get(k,0)+x
    for k in range(-m,m+1):
        lhs=36*k*w.get(k,0)-(18*k-9)*w.get(k-1,0)
        dk=d[k] if 0<=k<=m else 0
        dm=d[k+m] if 0<=k+m<=m else 0
        ek=e[m+1-k] if 1<=m+1-k<=m else 0
        rhs=-dk+36*m*m*e[m]*dm+p*(3*m+1)*d[m]*ek
        assert lhs==rhs if mod is None else (lhs-rhs)%mod==0,(m,p,k)
    J=sum((1+6*k)*v for k,v in c.items() if k>=0)
    return J if mod is None else J%p, w.get(0,0), c.get(0,0)

def prime(n):
    return n>1 and all(n%q for q in range(2,int(n**0.5)+1))

def main():
    for m in range(1,9):
        J,_,_=verify(m)
        print("exact-m",m,"J",J)
    tested=0
    for p in range(7,998):
        if not (p%6==1 and prime(p)): continue
        j,w,c=verify((p-1)//6,p)
        tested+=1
        if p in (13,19,67,373):
            print("prime",p,"J",j,"w0",w%(p*p),"c0",c%(p*p))
    assert tested==80
    assert verify(3,19)[0]==6
    assert verify(62,373)[0]==98
    # Fiber witness: first diagonal labeled mass r=1, second r=2.
    x1,x2,t=4,5,1
    assert x1+2*x2==(x1+2*t)+2*(x2-t)
    assert x1+x2!=(x1+2*t)+(x2-t)
    print("ALL_CHECKS_PASS",tested)

if __name__=="__main__": main()
