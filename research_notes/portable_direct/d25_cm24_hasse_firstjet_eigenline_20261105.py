#!/usr/bin/env python3
"""D25 exact CM(-24) first-jet Frobenius eigenline verifier; author side only."""
from math import comb, isqrt
Q = (-1,140,-294,140)
def primes(n):
    for p in range(5,n+1):
        if p%8==5 and all(p%d for d in range(2,isqrt(p)+1)):yield p
def ring(p):
    o=(1,0,0,0);z=(0,0,0,0);t=(0,1,0,0)
    def c(n):return (n%p,0,0,0)
    def add(a,b):return tuple((x+y)%p for x,y in zip(a,b))
    def neg(a):return tuple(-x%p for x in a)
    def sub(a,b):return add(a,neg(b))
    def mul(a,b):
        s=[0]*7
        for i in range(4):
            for j in range(4):s[i+j]+=a[i]*b[j]
        for k in range(6,3,-1):
            v=s[k]
            for j in range(4):s[k-4+j]+=v*Q[j]
        return tuple(x%p for x in s[:4])
    def power(a,n):
        r=o
        while n:
            if n&1:r=mul(r,a)
            a=mul(a,a);n//=2
        return r
    def inv(a):
        b=power(a,p*p-2)
        assert mul(a,b)==o,(p,a)
        return b
    def div(a,b):return mul(a,inv(b))
    return o,z,t,c,add,neg,sub,mul,power,div,inv
def main(limit=5000):
    total=split=inert=0; examples={}
    for p in primes(limit):
        m=(p-1)//2
        o,z,t,c,add,neg,sub,mul,powr,div,inv=ring(p);t2=mul(t,t)
        if p%24==5:
            f=div(sub(c(7),mul(c(5),t)),sub(c(5),mul(c(7),t)));split+=1
        else:
            f=div(sub(c(5),mul(c(7),t)),sub(c(7),mul(c(5),t)));inert+=1
        assert powr(t,p)==f,("frobenius",p)
        s=neg(div(add(o,f),mul(c(2),add(o,t))))
        assert mul(s,powr(s,p))==c(pow(4,-1,p)),("s-norm",p)
        H=A=z;tk=o
        for j in range(m+1):
            w=comb(m,j)**2%p
            H=add(H,mul(c(w),tk))
            if j:A=add(A,mul(c(j*w),powr(t,j-1)))
            tk=mul(tk,t)
        C=add(mul(mul(c(16),mul(t,sub(o,t2))),A),
              mul(sub(add(o,mul(c(2),t)),mul(c(7),t2)),H))
        B=powr(s,m);assert powr(H,p)==mul(B,H),("H",p)
        G=neg(mul(c(4),powr(s,m+2)))
        assert powr(C,p)==mul(G,C),("C",p)
        assert mul(G,powr(G,p))==o,("Gamma norm",p)
        D=neg(div(mul(c(4),mul(f,add(o,f))),mul(sub(o,t2),sub(o,f))))
        assert mul(D,powr(D,p))==o,("D norm",p)
        beta=neg(mul(c(pow(2,-1,p)),sub(div(D,add(o,f)),inv(add(o,t)))))
        h=div(sub(add(o,mul(c(2),t)),mul(c(7),t2)),
              mul(c(16),mul(t,sub(o,t2))))
        V=add(A,mul(h,H))
        assert mul(D,powr(V,p))==mul(B,V),("first jet",p)
        if p in (5,13,29,37,53,373):
            examples[p]={"C":C,"Gamma":G}
        total+=1
    print("ALL_PASS",{"primes":total,"split":split,"inert":inert,
                      "limit":limit,"examples":examples})
if __name__=="__main__":main()
