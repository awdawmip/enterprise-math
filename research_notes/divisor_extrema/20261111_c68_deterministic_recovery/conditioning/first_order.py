"""Certify worst asymptotic single-H resolution among words of budget at most 24."""
from argparse import ArgumentParser
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
import sys
import json

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'surplus'))
from precision import derivatives,matmul

P=2**61-1

class Jet:
    """a+b*t modulo t² over the rationals; strip the common visible t² before division."""
    def __init__(self,a,b=0):self.a,self.b=F(a),F(b)
    def __add__(self,w):
        w=asjet(w)
        return Jet(self.a+w.a,self.b+w.b)
    __radd__=__add__
    def __sub__(self,w):
        w=asjet(w)
        return Jet(self.a-w.a,self.b-w.b)
    def __mul__(self,w):
        w=asjet(w)
        return Jet(self.a*w.a,self.b*w.a+self.a*w.b)
    __rmul__=__mul__
    def __truediv__(self,w):
        w=asjet(w)
        return Jet(self.a/w.a,(self.b*w.a-self.a*w.b)/w.a**2)
    def __rtruediv__(self,w):return asjet(w).__truediv__(self)

def asjet(v):return v if isinstance(v,Jet) else Jet(v)

def native_variation(word):
    cells=(Jet(1),Jet(0),Jet(0),Jet(1))
    consumed=0
    for i,m in enumerate(word):
        r=len(word)-i;k=2*r+1
        likelihood=[]
        for now,following in ((F(1,4),F(1)),(F(1),F(4)),(F(4),F(4))):
            mass=Jet(1)
            for h in range(m):
                offset=consumed+h
                mass*=Jet(1,-offset)/Jet(1,k/now-offset)
            offset=consumed+m
            mass*=F(r,1)/now/Jet(1,k/now-offset)
            mass*=F(r,1)/following/Jet(1,(k-1)/following-offset)
            likelihood.append(mass)
        tau=7*likelihood[0]/likelihood[2]
        rho=likelihood[1]/likelihood[2]
        cells=matmul(cells,(tau,rho,tau,Jet(1)))
        consumed+=m
    f=Jet(1)
    for h in range(consumed):
        f*=Jet(1,1-h)/Jet(1,F(1,4)-h)
    a,b,h,d=cells
    return (f*(a/b-h/d)).b

def controls(maximum):
    count=0
    for r in range(1,maximum+1):
        diffs=[a-b for a,b in derivatives(r)]
        base=native_variation((0,)*r)
        samples=(list(product(range(3),repeat=r)) if r<=4 else
                 [tuple((i+shift)%3 for i in range(r)) for shift in range(3)])
        for word in samples:
            assert native_variation(word)-base==sum(x*m for x,m in zip(diffs,word))
            count+=1
    return count

def main(budget):
    assert 2<=budget<=24
    def residue(q):
        assert q.denominator%P
        return q.numerator*pow(q.denominator,-1,P)%P
    data=[]
    for r in range(1,budget+1):
        row=derivatives(r)
        weights=[residue(a-b) for a,b in row]
        data.append(' '.join(map(str,[r,budget-r,*weights])))
    with TemporaryDirectory() as tmp:
        exe=Path(tmp)/'jet_words'
        subprocess.run(['g++','-O3','-std=c++17',str(Path(__file__).with_name('jet_words.cpp')),
                        '-o',str(exe)],check=True)
        raw=subprocess.check_output([str(exe)],input='\n'.join(data)+'\n',text=True)
    rows=[]
    for j,line in enumerate(raw.splitlines(),1):
        r,count,dist=map(int,line.split())
        assert r==j and count==comb(budget,r) and dist==1
        rows.append(dict(depth=r,distinct_signatures=count))
    assert len(rows)==budget and sum(z['distinct_signatures'] for z in rows)==2**budget-1
    return dict(depth_plus_internal_fives_at_most=budget,modulus=P,words=2**budget-1,
                worst_separation_exponent='7/4',native_exact_dual_number_cross_checks=controls(budget),
                same_depth_counts=rows)

if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--budget',type=int,default=24)
    print(json.dumps(main(p.parse_args().budget),indent=2))
