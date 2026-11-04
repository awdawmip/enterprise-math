#!/usr/bin/env python3
"""Exact check for CM(-24) one-scalar Hasse first-jet; portable author-side only."""
from math import isqrt
Q_REDUCE=(-1,140,-294,140)
def primes(n):
    for p in range(5,n+1):
        if p%8==5 and all(p%d for d in range(2,isqrt(p)+1)):yield p
def calc(p):
    one=(1,0,0,0);zero=(0,0,0,0);t=(0,1,0,0)
    def k(v):return (v%p,0,0,0)
    def add(a,b):return tuple((a[i]+b[i])%p for i in range(4))
    def neg(a):return tuple(-v%p for v in a)
    def sub(a,b):return add(a,neg(b))
    def mul(a,b):
        s=[0]*7
        for i in range(4):
            for j in range(4):s[i+j]+=a[i]*b[j]
        for j in range(6,3,-1):
            v=s[j]
            for i in range(4):s[j-4+i]+=v*Q_REDUCE[i]
        return tuple(v%p for v in s[:4])
    def power(a,n):
        z=one
        while n:
            if n&1:z=mul(z,a)
            a=mul(a,a);n>>=1
        return z
    tinv=add(add(k(140),mul(k(-294),t)),add(mul(k(140),power(t,2)),neg(power(t,3))))
    assert mul(t,tinv)==one
    y=add(t,tinv)
    assert sub(sub(power(y,2),mul(k(140),y)),k(-292))==zero
    u=mul(add(y,k(2)),k(pow(24,-1,p)))
    assert power(y,p)==sub(k(140),y)
    assert mul(u,power(u,p))==one
    m=(p-1)//2;r=(p-1)//4;n=r+1
    H=Hp=zero;mon=old=one;b=1
    for j in range(m+1):
        w=b*b%p
        H=add(H,mul(k(w),mon))
        if j:Hp=add(Hp,mul(k(j*w),old))
        old=mon;mon=mul(mon,t)
        if j<m:b=b*(m-j)*pow(j+1,-1,p)%p
    t2=mul(t,t)
    C=add(mul(mul(k(16),mul(t,sub(one,t2))),Hp),mul(sub(add(one,mul(k(2),t)),mul(k(7),t2)),H))
    D=mul(power(tinv,n),C)
    f=power(t,p)
    s=neg(mul(add(one,f),mul(k(pow(2,-1,p)),power(add(one,t),p*p-2))))
    gamma=neg(mul(k(4),power(s,m+2)))
    assert power(C,p)==mul(gamma,C),(p,'old first jet')
    assert power(D,p)==mul(power(u,2*r),D),(p,'new Frobenius')
    d1=-D[3]%p;d0=(D[0]-140*d1)%p
    assert D==add(k(d0),mul(k(d1),y)),(p,'reciprocity')
    avec=mul(power(u,r),D)
    assert avec[1:]==(0,0,0),(p,'not scalar')
    a=avec[0]
    assert D==mul(k(a),power(power(u,p),r)),(p,'reconstruct')
    norm=(d0*d0+140*d0*d1+292*d1*d1)%p
    assert norm==a*a%p,(p,'square norm')
    return {'p':p,'a':a,'d0':d0,'d1':d1,'norm':norm,'split':p%24==5}
def main(limit=5000):
    tot=split=inert=0;examples=[]
    for p in primes(limit):
        z=calc(p);tot+=1;split+=z['split'];inert+=not z['split']
        if p in (5,13,29,37,53,373):examples.append(z)
    print('ALL_PASS',{'primes':tot,'split':split,'inert':inert,'limit':limit,'examples':examples})
if __name__=='__main__':main()
