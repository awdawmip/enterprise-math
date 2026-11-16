"""Exact rational controls of the two recovered center invariants, Python 3.9+."""
from fractions import Fraction as Q
from math import prod
import json

def parameters(k, n, v):
    a = Q(k-1+v,28*(k-1+4*v))*Q(prod(range(n+k+1,n+4*k+1)),prod(range(v+k,v+4*k)))
    t = a*Q(4**(n-v)*prod(range(v+k,n+k+1)),prod(4*i+k for i in range(v,n+1)))
    return a,t

def compose(m,n):
    a,b,c,d=m
    e,f,g,h=n
    return a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h

def image(m,z):
    a,b,c,d=m
    return (a*z+b)/(c*z+d)

def dyadic(x):
    def valuation(n): return (n & -n).bit_length()-1
    assert x
    return valuation(x.numerator)-valuation(x.denominator)

def check(gaps):
    n=sum(gaps)+2
    stocks=[n]
    params=[]
    prefixes=[(Q(1),Q(0),Q(0),Q(1))]
    for j,g in enumerate(gaps[:-1]):
        v=n-g
        a,t=parameters(17-2*j,n,v)
        params.append((a,t))
        prefixes.append(compose(prefixes[-1],(0,1,a,1)))
        stocks.append(v)
        n=v
    w=n
    W=Q((w+2)*(w+3)*(w+4),840)
    l=Q(prod(4*q+4 for q in range(3,w+1)),prod(4*q+1 for q in range(3,w+1)))
    d,D=Q(1,2),Q(5)
    p,q=1/(1+d*W),1/(1+D*W)
    X,Y=image(prefixes[8],p),image(prefixes[8],q)
    roots=[image(m,0) for m in prefixes]
    a,t=params[-1]
    assert roots[2]<roots[4] and roots[2]==1/(1+params[0][0])
    A,B=roots[8],roots[6]
    assert A>B and image(prefixes[8],-1/a)==B
    T=((X-A)/(X-B))/((Y-A)/(Y-B))
    assert T>1 and (D-d*T)/(T-1)==(1+a)/W
    physical=prefixes[0]
    for b,small in params:
        physical=compose(physical,(small,1,b,1))
    least=min(gaps[:7])
    valuations=[]
    for tail,constant in [(p,Q(6)),(q,Q(3,32))]:
        tail=tail*(1+l*W/constant)
        z=image(physical,tail)
        corrected=image(prefixes[7],(1+t*tail)/(1+a*tail))
        val=dyadic(z-corrected)
        assert abs(val-3*least)<48
        valuations.append(val)
    return dict(gaps=gaps,order_after_exact_tail_removal=valuations,leading_length_times_three=3*least)

if __name__=="__main__":
    controls=[check(g) for g in [
        (52,60,67,74,81,88,95,16,39),
        (88,49,79,94,71,82,66,11,35),
        (69,78,85,97,51,80,62,14,42),
        (46,99,85,17,89,113,72,68,77),
    ]]
    assert Q(125,204)+2*Q(1,136)==Q(32,51)
    b=[Q(1),Q(13,36)]
    w=[Q(0),Q(5,17)]
    for n in range(10,14):
        b.append((b[-1]+b[-2])/n)
        w.append((w[-1]+w[-2])/(n+8))
    assert b[1]+w[1]==Q(401,612)
    assert b[2]+w[2]==Q(311,2040)
    print(json.dumps(dict(controls=controls,depth_8_including_third_gap="401/612",
                          lower_bounds=[str(x+y) for x,y in zip(b,w)]),indent=2))
