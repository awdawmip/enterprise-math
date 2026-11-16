"""Independently form physical columns at C=30000, then recover all three jets."""
from fractions import Fraction as Q
from math import prod
from check_reconstruct_independent import reconstruct
import json


def balanced(lo,hi,multiplier,offset):
    if hi-lo<64:
        return prod(multiplier*k+offset for k in range(lo,hi))
    mid=(lo+hi)//2
    return balanced(lo,mid,multiplier,offset)*balanced(mid,hi,multiplier,offset)


def rising(n,k):
    return prod(range(n,n+k))


def shape(n):
    return Q(4*n+5,n+5)/Q(balanced(3,n+1,4,5),balanced(3,n+1,4,20))


def endpoints(v,w):
    Y=Q(balanced(3,w+1,4,1),balanced(3,w+1,4,4))
    W=Q(rising(w+2,3),840)
    tails=[(1+j*W)/(1+W/(e*Y)) for j,e in ((5,Q(3,32)),(Q(5,4),Q(3,2)),(Q(1,2),6))]
    rho=4*Q(balanced(w,v+1,4,3),balanced(w,v+1,4,12))
    alpha=Q((w+2)*rising(v+4,9),28*(4*w+2)*rising(w+3,9))
    tau=rho/alpha
    Z=[(rho+tau*T)/(1+tau*T) for T in tails]
    return min(Z),max(Z)


def scale(v):
    return 28*Q(4*v+4,v+4)*rising(v+5,15)


def search(lo,hi,goal,lookup):
    while lo<hi:
        mid=(lo+hi)//2
        if lookup(mid)<goal:
            lo=mid+1
        else:
            hi=mid
    assert lookup(lo)==goal
    return lo


def J(interval):
    low,high=sorted(abs(z-1) for z in interval)
    return high/low


def main():
    c,C=100,30000
    a=Q(balanced(3,C+1,4,5),balanced(3,C+1,4,20))
    s=1/a
    P=rising(C+6,15)
    T=5*(P-1).bit_length()+354*c+3
    tested=[]
    for v,w in ((2,2),(73,3),(96,96),(100,36)):
        z=endpoints(v,w)
        outer_rho=shape(v)*a
        outer_tau=outer_rho*scale(v)/P
        real=[(outer_rho+outer_tau*t)/(1+outer_tau*t) for t in z]
        g=max(real)/min(real)
        data=g
        coeff=[]
        for i in range(3):
            r=reconstruct(data,T)
            coeff.append(r)
            data=(data-r)/s
        hh=-coeff[2]/coeff[1]
        ee=hh+coeff[1]/coeff[0]
        kk=coeff[0]*ee/hh
        AA=(1/hh-kk/ee)/(kk-1)
        out_v=search(2,c,AA,shape)
        observed=(P/(AA*hh*scale(out_v)), P/(AA*ee*scale(out_v)))
        out_w=search(2,out_v,J(observed),lambda n:J(endpoints(out_v,n)))
        assert (out_v,out_w)==(v,w)
        tested.append([v,w])
    return dict(outer_stock=C,cap=c,templates=tested)


if __name__ == '__main__':
    print(json.dumps(main(),indent=2))
