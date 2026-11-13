"""Exact rank and one-scalar 2-adic controls; no higher precision readings as input."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from itertools import product
from math import prod
from pathlib import Path
import json,sys
import sympy as sp

P=10**9+7


def real_limits(r,x):
    s=[1,*[v**4 for v in x]]
    roots=[1,*x]
    z,p,d,e=0,0,1,1
    for i in range(r,0,-1):
        rate=4*(roots[i]/roots[i-1])**(3*(2*(r-i+1)+1))
        b=sp.Rational(7,16)*rate**5
        a=rate/b
        d=d*b*(1-rate)/(1+b*z)**2
        z=(rate+b*z)/(1+b*z)
        e=-e*a/(1+a*p)**2
        p=1/(1+a*p)
    return d*x[-1]**-3/z,e*x[-1]**-12/p,[s[i-1]-s[i] for i in range(1,r+1)]+[s[-1]]


def reduce(rational):
    n,d=sp.fraction(rational)
    return int(n)*pow(int(d),-1,P)%P


def ranks(r):
    roots=sp.symbols('x:'+str(r))
    point={x:sp.Rational(12-i,14+i) for i,x in enumerate(roots)}
    g,j,ell=real_limits(r,roots)
    coords=[point[x]**4 for x in roots]
    s,u=coords[:2]
    if r==2:
        explicit=s**9/(112*u**12*(1+112*s**15))
    else:
        v=coords[-1]
        explicit=s**15*u**24/(112*v**12*(112*u**15+s**15)*
                                (112*s**21*u**15+u**15+s**36))
    assert abs(j.xreplace(point))==explicit
    jac=[[reduce(sp.diff(f,x).xreplace(point)) for x in roots] for f in (g,j,*ell)]
    matrices=[jac[:2]] if r==2 else [jac[:2]+[row] for row in jac[2:]]
    dets=[int(sp.Matrix(a).det())%P for a in matrices]
    assert all(dets)
    return dict(r=r,point=[str(v) for v in point.values()],explicit_shadow_matches=True,rows_mod_p=jac,
                determinants_mod_p=dets)


def adapted(c,gaps,active=None):
    """Return the z_D/z_d oriented ratio; differentiate center in one dyadic parameter."""
    r=len(gaps)-1
    stocks=[c]
    for m in gaps[:-1]:
        stocks.append(stocks[-1]-m)
    w=stocks[-1]
    assert w==gaps[-1]+2 and w>=4
    W=Q((w+2)*(w+3)*(w+4),840)
    l=Q(prod(4*n+4 for n in range(3,w+1)),prod(4*n+1 for n in range(3,w+1)))
    reached=[]
    direction=[]
    for j,u in ((Q(1,2),Q(6)),(Q(5),Q(3,32))):
        terminal=1+j*W
        if active is None:
            p=(1+l*W/u)/terminal
            dp=0
        else:
            p=1/terminal
            dp=W/(u*terminal) if active==r+1 else 0
        for i in reversed(range(r)):
            n,s,k=stocks[i],stocks[i+1],2*(r-i)+1
            a=Q(k-1+s,28*(k-1+4*s))*Q(prod(range(n+k+1,n+4*k+1)),
                                                     prod(range(s+k,s+4*k)))
            t=a*Q(4**(n-s)*prod(range(s+k,n+k+1)),prod(k+4*z for z in range(s,n+1)))
            if active is None:
                p=(1+t*p)/(1+a*p)
            else:
                dp=(-a*dp)/(1+a*p)**2+(p/(1+a*p) if active==i+1 else 0)
                p=1/(1+a*p)
        reached.append(p)
        direction.append(dp)
    h,d=reached
    x,y=direction
    return h/d,(x*d-y*h)/d**2


def valuation(x):
    def v(z):return (z&-z).bit_length()-1
    return v(x.numerator)-v(x.denominator)


def main(prior):
    sys.path.insert(0,str(prior.resolve()))
    from mixed_kernel import responses
    tests=[]
    directions=[]
    for r in (2,3):
        native=0
        for gaps in product(range(3), repeat=r+1):
            gaps=tuple(gaps[:-1])+(gaps[-1]+2,)
            c=2+sum(gaps)
            h,_=adapted(c,gaps)
            rows,_=responses(r,c,gaps)
            z=[(7*rows[0][j]+rows[1][j])/(7*rows[0][j]+rows[2][j]) for j in (3,4,5)]
            assert h==z[0]/z[2] and max(h,1/h)==max(z)/min(z)
            n,_=adapted(c,gaps,0)
            assert n!=1
            native+=1
        tests.append(dict(r=r,native_words=native,columns=3*native))
        if r==3:
            for i in range(1,r+2):
                gaps=(10,11,12,13)
                c=sum(gaps)+2
                center,deriv=adapted(c,gaps,i)
                assert deriv
                larges=tuple(80 if j==i else 180+j for j in range(1,r+2))
                c=sum(larges)+2
                obs,_=adapted(c,larges)
                cen,d=adapted(c,larges,i)
                v=valuation(obs-cen)
                assert abs(v-240)<40 and d
                directions.append(dict(shortest=i,nonzero_derivative=str(deriv),
                                       actual_residual_valuation=v,shortest_gap=80))
    return dict(prime=P,algebraic_ranks=[ranks(2),ranks(3)],
                native=tests,dyadic_first_directions=directions)


if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--prior',required=True,type=Path,help='C67/joint')
    print(json.dumps(main(p.parse_args().prior),indent=2))
