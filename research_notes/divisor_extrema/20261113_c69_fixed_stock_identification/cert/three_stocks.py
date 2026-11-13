"""Exact inversion with a named raw tail measured at arbitrary three stocks."""
from argparse import ArgumentParser
from fractions import Fraction as F
from functools import cache
from itertools import combinations
from math import comb,prod
from pathlib import Path
import json
import sys

@cache
def constants(r,c):
    k=2*r+1
    a=prod((F(k+4*n,4*(k+n)) for n in range(3,c+1)),start=F(1))
    p=prod(c+j for j in range(k+1,4*k+1))
    return a,p

def decode(r, stocks, values, block):
    lines=[]
    for c,x in zip(stocks,values):
        a,p=constants(r,c)
        lines.append(((1-x)/p, x/a))
    i,j=next((i,j) for i,j in combinations(range(3),2) if lines[i][0]!=lines[j][0])
    beta=(lines[j][1]-lines[i][1])/(lines[j][0]-lines[i][0])
    alpha=lines[i][1]-beta*lines[i][0]
    assert beta>0 and all(alpha+beta*u==v for u,v in lines)
    v=next(s for s in range(2,min(stocks)+1) if block(r,s,0)[0]/constants(r,s)[0]==alpha)
    a,p=constants(r,v)
    return v, beta*a/(p*block(r,v,0)[1])

def main(prior):
    sys.path.insert(0,str(prior.resolve()))
    from stock_shift import points,block,words
    verified=0;cases=0
    samples=[]
    for r in range(1,5):
        for c in range(2,12):
            tests=[(c,c+1,c+2), (c,c+3,c+8),(c+1,c+5,c+14)]
            for w in words(r,c):
                cases+=1
                v=c-w[0]
                suffix=points(r-1,v,w[1:])
                for stocks in tests:
                    rows=[points(r,n,(w[0]+n-c,)+w[1:]) for n in stocks]
                    for label in range(3):
                        got=decode(r,stocks,[z[label] for z in rows],block)
                        assert got==(v,suffix[label])
                        verified+=1
                        if (r,c,w,stocks,label)==(2,7,(1,2,2),(7,10,15),2):
                            samples.append(dict(stock=stocks,measured=[str(z[label]) for z in rows],
                                                landing=got[0],suffix_column=str(got[1])))
    entire=0
    input_ratios=0
    for r in range(1,5):
        for c in range(2,9):
            for w in words(r,c):
                for label in range(3):
                    base=points(r,c,w)[label];value=base;stock=c
                    recovered=[]
                    for ix in range(r):
                        adds=(2*ix+2,2*ix+5)
                        measurements=[value]
                        for delta in adds:
                            current=c+delta
                            perturbed=tuple(t+(delta if i==ix else 0) for i,t in enumerate(w))
                            raw=points(r,current,perturbed)[label]
                            for j,m in enumerate(recovered):
                                rho,tau=block(r-j,current,m)
                                raw=(raw-rho)/(tau*(1-raw))
                                current-=m
                            assert current==stock+delta
                            measurements.append(raw)
                        v,value=decode(r-ix,(stock,stock+adds[0],stock+adds[1]),measurements,block)
                        recovered.append(stock-v)
                        stock=v
                    assert tuple(recovered)+(stock-2,)==w
                    entire+=1
                    input_ratios+=2*r+1
    anonymous_cases=0
    anonymous_values=0
    for r in range(1,4):
        for c in range(2,8):
            for w in words(r,c):
                recovered=[]
                base=points(r,c,w)[(r+c)%3]
                for i in range(r):
                    measurements=[base]
                    for delta in range(1,19):
                        edited=tuple(m+(delta if j==i else 0) for j,m in enumerate(w))
                        measurements.append(points(r,c+delta,edited)[(r+delta+2*i)%3])
                    ccut=c-sum(recovered)
                    for k,z in enumerate(measurements):
                        stock=c+k
                        for j,m in enumerate(recovered):
                            rho,tau=block(r-j,stock,m)
                            z=(z-rho)/(tau*(1-z))
                            stock-=m
                        measurements[k]=z
                    possible=set()
                    for candidate in words(r-i,ccut):
                        if all(z in points(r-i,ccut+k,(candidate[0]+k,)+candidate[1:]) for k,z in enumerate(measurements)):
                            possible.add(candidate[0])
                    assert len(possible)==1
                    recovered.append(possible.pop())
                assert tuple(recovered)+(c-2-sum(recovered),)==w
                anonymous_cases+=1
                anonymous_values+=18*r+1
    # A sharp algebraic degeneracy for continuous, positive alpha,beta.
    # Chords of the graph a/P imply that at x=.8 in stocks (c,c+1),
    # the design necessarily degenerates. Build two positive supports.
    r,c=2,11
    a,p=constants(r,c)
    a1,p1=constants(r,c+1)
    a2,p2=constants(r,c+2)
    x=F(4,5)
    def val(A,B,a,p):
        return (a*A+(a/p)*B)/(1+(a/p)*B)
    models=[(x/a-b*(1-x)/p,b) for b in (F(1),F(37))]
    rows=[[val(A,B,t,q) for t,q in ((a,p),(a1,p1),(a2,p2))] for A,B in models]
    assert rows[0][:2]==rows[1][:2] and rows[0][2]!=rows[1][2] and all(A>0 for A,B in models)
    return dict(original_templates=cases,successful_named_three_stock_decodings=verified,
                complete_word_and_label_recoveries=entire,complete_word_raw_ratios=input_ratios,
                anonymous_complete_words=anonymous_cases,anonymous_unlabeled_ratios=anonymous_values,
                nonconsecutive_example=samples,
                planted_continuous_two_match=[list(map(str,row)) for row in rows])
if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--prior',type=Path,required=True,help='C68/twoblocks directory')
    print(json.dumps(main(p.parse_args().prior),indent=2))
