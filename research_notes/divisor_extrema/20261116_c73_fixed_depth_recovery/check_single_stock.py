"""Two-block fixed single-g controls. Python 3.8+, standard library."""
from fractions import Fraction as Q
from math import prod
from functools import lru_cache


def rising(n, d):
    return prod(range(n,n+d))


@lru_cache(None)
def native_block(k,n,s):
    rho=Q(k+4*s,k+s)
    tau=Q(28*(k+4*s)*(k-1+4*s),(4*k+s)*(k-1+s))
    for j in range(s+1,n+1):
        rho*=Q(k+4*j,4*(k+j))
        tau*=Q(k+4*j,4*(4*k+j))
    return rho,tau


def trig_tail(w):
    y=prod((Q(4*i+1,4*i+4) for i in range(3,w+1)),start=Q(1))
    x=Q(840,(w+2)*(w+3)*(w+4))
    return [y*(x*a+b)/(1+x*y*a) for a,b in zip((Q(3,32),Q(3,2),Q(6)),(Q(15,32),Q(15,8),Q(3)))]


@lru_cache(None)
def outer_scale(c):
    return prod((Q(4*j+5,4*(j+5)) for j in range(3,c+1)),start=Q(1))


def parameters(k,n,s):
    return Q(k+s-1,28*(k+4*s-1))*Q(rising(n+k+1,3*k),rising(s+k,3*k))


def check_calibration(nmax):
    count=0
    for c in range(2,nmax+1):
        a=outer_scale(c)
        P=rising(c+6,15)
        for v in range(2,c+1):
            rho,tau=native_block(5,c,v)
            A=native_block(5,v,v)[0]/outer_scale(v)
            p=Q(28*(4+4*v)*rising(v+5,15),v+4)
            for w in range(2,v+1):
                b,s=native_block(3,v,w)
                tail=trig_tail(w)
                inside=[(b+s*z)/(1+s*z) for z in tail]
                outside=[(rho+tau*z)/(1+tau*z) for z in inside]
                lo,hi=min(inside)*p,max(inside)*p
                ratio=(P+hi)*(P+a*A*lo)/((P+lo)*(P+a*A*hi))
                assert max(ratio,1/ratio)==max(outside)/min(outside)
                assert P*(ratio-1)==(hi-lo)*(1-a*A)/((1+lo/P)*(1+a*A*hi/P))
                count+=1
    return count


def v2(q):
    if not q:
        return float('inf')
    return (q.numerator & -q.numerator).bit_length()-(q.denominator & -q.denominator).bit_length()


def check_center(gaps):
    a,b,c=gaps
    w=c+2
    v=w+b
    stock=v+a
    # Two original g endpoint orders respectively sorted by inner terminal index.
    original=trig_tail(w)
    alpha,beta=parameters(5,stock,v),parameters(3,v,w)
    for k,n,s in ((3,v,w),(5,stock,v)):
        r,t=native_block(k,n,s)
        original=[(r+t*z)/(1+t*z) for z in original]
    g=max(original)/min(original)
    W=Q((w+2)*(w+3)*(w+4),840)
    def center(p):
        return (1+beta*p)/(1+alpha+beta*p)
    ratio=center(1/(1+W/2))/center(1/(1+5*W))
    assert ratio>1 and g>1
    matched=max(v2(g-ratio),v2(1/g-ratio))
    assert matched>=2*min(gaps), (stock,gaps,matched)
    return stock,matched


if __name__=='__main__':
    print("calibration identities:", check_calibration(24))
    for gaps in ((39,47,62),(102,57,98),(70,32,61),(88,129,109),(150,143,64)):
        print("dyadic center ratio:",gaps,check_center(gaps))
