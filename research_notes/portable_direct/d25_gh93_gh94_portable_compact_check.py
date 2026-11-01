#!/usr/bin/env python3
"""GH-93/GH-94 p-local portable regression, no native runtime claim.
Uses published GH-91 polynomial helper in the same directory. Python stdlib.
"""
from d25_gh91_uniform_linear_source_check import (
    add, sc, mul, theta, shift, lin, concomitant, ev, primes_lt
)

def check(p):
    d=(p-3)//4; q=p**4
    c=[1]; u=[1]
    for r in range(d):
        c.append(c[-1]*pow(4*r+1,3,q)*pow((4*r+2)*(4*r+3)*(4*r+4),-1,q)%q)
        u.append(u[-1]*pow(4*r+3,3,q)*pow((4*r+4)*(4*r+5)*(4*r+6),-1,q)%q)
    c1=theta(q,c); c2=theta(q,c1)
    u1=theta(q,u); u2=theta(q,u1); u3=theta(q,u2)
    k4,k8,k16,k64=(pow(k,-1,q) for k in (4,8,16,64))
    lm=add(q,lin(q,1,-1,theta(q,c2)),sc(q,-3*k4,lin(q,1,1,c2)),
           sc(q,k16,lin(q,2,-3,c1)),sc(q,-k64,shift(q,c)))
    lp=add(q,lin(q,1,-1,u3),sc(q,k4,lin(q,3,-9,u2)),
           sc(q,k16,lin(q,2,-27,u1)),sc(q,-27*k64,shift(q,u)))
    alpha=(-(p-2)**3*c[d]*k64)%q
    beta=(-p**3*u[d]*k64)%q
    assert lm==[0]*(d+1)+[alpha]
    assert lp==[0]*(d+1)+[beta]
    B=concomitant(q,c,u); V=concomitant(q,c,u1)
    W=add(q,sc(q,64,V),sc(q,40,B))
    H=add(q,sc(q,8,u1),sc(q,5,u)); J=theta(q,H)
    T=add(q,sc(q,8,c1),c)
    K=add(q,lin(q,8,-8,c2),lin(q,-6,2,c1),
          sc(q,k8,lin(q,5,15,c)))
    rhs=add(q,mul(q,lin(q,-1,1,J),T),
            mul(q,add(q,lin(q,6,2,J),sc(q,k8,lin(q,15,1,u))),c),
            mul(q,H,K))
    assert add(q,W,sc(q,-1,rhs))==sc(q,-p**3*u[d],[0]*(d+1)+c)
    assert u[d]%p!=0  # first nonzero syzygy defect occurs exactly at p^3
    Bsrc=[0]*(2*d+2); Bsrc[0]=k8
    Wsrc=[0]*(2*d+2); Wsrc[0]=5
    naive=[0]*(2*d+2); naive[0]=5
    for j in range(d+1):
        n=d+1+j; v=u[j]*pow(n,-1,q)
        Bsrc[n]=(Bsrc[n]+alpha*v)%q
        Wsrc[n]=(Wsrc[n]+8*alpha*(8*j+5)*v)%q
        naive[n]=(naive[n]+c[d]*(8*j+5)*v)%q
    for i in range(d+1):
        n=d+1+i; v=c[i]*pow(n,-1,q)
        Bsrc[n]=(Bsrc[n]+beta*v)%q
        Wsrc[n]=(Wsrc[n]+beta*(64*(d+1)+40)*v)%q
    for i in range(d+1):
        for j in range(d+1):
            n=i+j+1
            v=(64*c[i]*u[j]*pow(j+3*k4,3,q)*pow(n,-1,q))%q
            Wsrc[n]=(Wsrc[n]+v)%q
            naive[n]=(naive[n]+v)%q
    assert add(q,B,sc(q,-1,Bsrc))==[0]
    assert add(q,W,sc(q,-1,Wsrc))==[0]
    Q=add(q,u3,sc(q,9*k4,u2),sc(q,27*k16,u1),sc(q,27*k64,u))
    wprime=add(q,sc(q,8*alpha,[0]*(d+1)+H),
               sc(q,beta*(64*(d+1)+40),[0]*(d+1)+c),
               sc(q,64,shift(q,mul(q,c,Q))))
    assert add(q,theta(q,W),sc(q,-1,wprime))==[0]
    # The old source-sum reconstruction must not be reused unchanged modulo p^2.
    delta=(ev(p*p,W,9)-ev(p*p,naive,9))%(p*p)
    return delta//p

if __name__=='__main__':
    ps=primes_lt(1000)
    deviations=[check(p) for p in ps]
    assert len(ps)==86
    print('PASS_P4_GH93_GH94',len(ps),'primes')
    print('NONZERO_P2_SOURCE_CORRECTIONS_Z9',sum(x!=0 for x in deviations))
    print('WITNESSES',[(p,check(p)) for p in (7,11,19,23,31)])
