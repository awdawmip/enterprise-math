"""Rational model checks for the single unidentified raw-column theorem."""
import argparse
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path
import sys
import sympy as sp

P=10**9+7

def limits(xs):
    xs=(sp.Integer(1),*xs)
    r=len(xs)-1
    real=sp.Integer(0)
    center=sp.Integer(0)
    for i in range(r,0,-1):
        rate=4*(xs[i]/xs[i-1])**(3*(2*(r-i+1)+1))
        scale=sp.Rational(7,16)*rate**5
        real=(rate+scale*real)/(1+scale*real)
        center=1/(1+rate/scale*center)
    return real,center,[xs[j-1]**4-xs[j]**4 for j in range(1,r+1)]+[xs[-1]**4]

def residue(q):
    n,d=map(int,q.as_numer_denom())
    return n*pow(d,-1,P)%P

def ranks(r):
    xs=sp.symbols('x:'+str(r))
    point={x:sp.Rational(12-i,14+i) for i,x in enumerate(xs)}
    real,center,gaps=limits(xs)
    def row(f):
        return [residue(f.diff(x).xreplace(point)) for x in xs]
    base=[row(real),row(center)]
    rows=[base] if r==2 else [base+[row(g)] for g in gaps]
    det=[int(sp.Matrix(tab).det())%P for tab in rows]
    assert all(det)
    return det

def controls(prior):
    sys.path.insert(0,str(prior.resolve()))
    from mixed_kernel import responses
    total=0
    for r in (2,3):
        for word in product(range(3),repeat=r+1):
            c=2+sum(word);v=c
            params=[]
            for i,m in enumerate(word[:-1]):
                k=2*(r-i)+1;w=v-m
                rho=Q(1);tau=Q(28*(k-1+4*w),k-1+w)
                for n in range(w,v+1):
                    rho*=Q(k+4*n,k+n)
                    tau*=Q(k+4*n,4*k+n)
                params.append((rho/4**m,tau/4**m))
                v=w
            x=Q(840,(v+2)*(v+3)*(v+4))
            y=Q(1)
            for n in range(3,v+1): y*=Q(4*n+1,4*n+4)
            rows,_=responses(r,c,word)
            for i,(u,b) in enumerate(zip([Q(3,32),Q(3,2),6],[Q(15,32),Q(15,8),3])):
                z=y*(b+u*x)/(1+u*x*y)
                for rho,tau in reversed(params):z=(rho+tau*z)/(1+tau*z)
                assert z==(7*rows[0][3+i]+rows[1][3+i])/(7*rows[0][3+i]+rows[2][3+i])
                total+=1
    return total

if __name__=='__main__':
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--prior',required=True,type=Path)
    args=cli.parse_args()
    print(json.dumps(dict(prime=P,r2=ranks(2),r3=ranks(3),actual_raw_columns=controls(args.prior)),indent=2))
