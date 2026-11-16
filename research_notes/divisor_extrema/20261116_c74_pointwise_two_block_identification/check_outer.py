"""Exact finite controls for the one-stock calibration and tail residual."""
from fractions import Fraction as Q
from math import prod
from itertools import combinations
import json

def rising(x, k):
    return prod(range(x, x+k))

def rho(n, s, k):
    return Q(prod(4*i+k for i in range(s,n+1)), 4**(n-s)*rising(s+k,n-s+1))

def alpha(n, s, k):
    return Q((s+k-1)*rising(n+k+1,3*k),28*(4*s+k-1)*rising(s+k,3*k))

def bmap(z, rate, scale):
    return (rate+scale*z)/(1+scale*z)

def ascale(n):
    return Q(prod(4*j+5 for j in range(3,n+1)),4**(n-2)*rising(8,n-2))

def raw(c, v, w):
    y=Q(prod(4*j+1 for j in range(3,w+1)),4**(w-2)*rising(4,w-2))
    x=Q(840,(w+2)*(w+3)*(w+4))
    tail=[y*(x*a+b)/(1+x*y*a) for a,b in
          [(Q(3,32),Q(15,32)),(Q(3,2),Q(15,8)),(Q(6),Q(3))]]
    ri=rho(v,w,3); si=ri/alpha(v,w,3)
    inner=[bmap(z,ri,si) for z in tail]
    rate=rho(c,v,5); scale=rate/alpha(c,v,5)
    outer=[bmap(z,rate,scale) for z in inner]
    multiplier=Q(28*(4*v+4)*rising(v+5,15), v+4)
    A=Q(4*v+5,v+5)/ascale(v)
    L,H=multiplier*min(inner), multiplier*max(inner)
    P=rising(c+6,15); a=ascale(c)
    R=(P+H)*(P+a*A*L)/((P+L)*(P+a*A*H))
    g=max(outer)/min(outer)
    assert g==max(R,1/R)
    return (A,L,H),g,R

def coeff(P, X, Y):
    A,L,H=X; B,J,K=Y
    def get(A,L,H,B,J,K):
        d=H-L
        return [d*(P+J)*P, d*(P+J)*(B*K-P*A), -d*(P+J)*A*B*K]
    return [v-w for v,w in zip(get(A,L,H,B,J,K),get(B,J,K,A,L,H))]

def order(x):
    n,d=x.numerator,x.denominator
    assert n
    return (abs(n)&-abs(n)).bit_length()-(d&-d).bit_length()

def tail_direction(n,v,w):
    a,b=alpha(n,v,5),alpha(v,w,3)
    W=Q((w+2)*(w+3)*(w+4),840)
    def partial(j,u):
        # F((1+l W/u)/(1+j W))=N(l)/D(l), low-to-high coefficients
        return (1+j*W+b,b*W/u),((1+a)*(1+j*W)+b,b*W/u)
    def polymul(x,y):
        return [x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[1]*y[1]]
    N1,D1=partial(Q(1,2),Q(6))
    N2,D2=partial(Q(5),Q(3,32))
    N=polymul(N1,D2); D=polymul(D1,N2)
    C=N[0]/D[0]; coeffs=[u-C*v for u,v in zip(N,D)]
    assert C!=1 and coeffs[0]==0 and any(coeffs[1:])
    k=next(i for i in [1,2] if coeffs[i])
    l=Q(4**(w-2)*rising(4,w-2),prod(4*j+1 for j in range(3,w+1)))
    def ev(poly):
        return poly[0]+l*poly[1]+l*l*poly[2]
    actual=ev(N)/ev(D)/C-1
    assert actual
    assert order(actual)==order(coeffs[k]/(D[0]*C))+k*order(l)
    return k,order(actual),order(l)

if __name__=='__main__':
    observed=0; pairs=0
    for c in range(2,15):
        rows=[raw(c,v,w) for v in range(2,c+1) for w in range(2,v+1)]
        observed+=len(rows)
        a=ascale(c); P=rising(c+6,15)
        for (X,g,R),(Y,g2,R2) in combinations(rows,2):
            results=[]
            for orient in (Y,(Y[0],Y[2],Y[1])):
                polys=coeff(P,X,orient)
                assert any(polys)
                clear=prod(t.denominator for t in X+orient)
                assert all((clear*t).denominator==1 for t in polys)
                results.append(polys[0]+a*polys[1]+a*a*polys[2]==0)
            assert any(results)==(g==g2)
            pairs+=1
    residuals=[dict(c=c,u=u,y=y,terms=tail_direction(c,u,y)) for c,u,y in
               [(1000,682,111),(2000,1390,203),(3000,2073,483),(3500,2420,404)]]
    print(json.dumps(dict(words=observed,different_pair_comparisons=pairs,
                          exact_tail_residual_checks=residuals),indent=2))
