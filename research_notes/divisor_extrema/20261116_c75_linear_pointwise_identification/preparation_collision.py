"""Two-block c=5 fixed-preparation collision, directly from all three tail columns."""
from fractions import Fraction as Q
from math import prod
import json


def rising(n,k):
    return prod(range(n,n+k))


def step(z,n,s,K):
    rho=4*prod((Q(4*j+K,4*(j+K)) for j in range(s,n+1)),start=Q(1))
    tau=rho*Q(28*(4*s+K-1)*rising(s+K,3*K),(s+K-1)*rising(n+K+1,3*K))
    return (rho+tau*z)/(1+tau*z)


def columns(c,v,w):
    y=prod((Q(4*j+1,4*(j+1)) for j in range(3,w+1)),start=Q(1))
    u=Q(840,(w+2)*(w+3)*(w+4))
    z=[y*(u*a+b)/(1+u*y*a) for a,b in [(Q(3,32),Q(15,32)),(Q(3,2),Q(15,8)),(Q(6),Q(3))]]
    return [step(step(t,v,w,3),c,v,5) for t in z]


def main():
    c=5
    templates=[(3,2),(5,5)]
    endpoints=[(min(z),max(z)) for z in (columns(c,*t) for t in templates)]
    (x,h),(u,k)=endpoints
    d,e=h-x,k-u
    beta=(e-d)/(d*(u-1)-e*(x-1))
    assert 0 < beta < 1
    values=[(1-beta+beta*h)/(1-beta+beta*l) for l,h in endpoints]
    assert values[0]==values[1] and h/x!=k/u
    return dict(stock=c, templates=templates, alpha='0', beta=str(beta),
                endpoints=[[str(l),str(h)] for l,h in endpoints],H=str(values[0]),
                original_H=[str(h/l) for l,h in endpoints])

if __name__=='__main__':
    print(json.dumps(main(),indent=2))
