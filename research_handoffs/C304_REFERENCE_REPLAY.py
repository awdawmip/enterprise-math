#!/usr/bin/env python3
"""C304 exact reference using frozen C301 portable input directory.
Usage: python C304_REFERENCE_REPLAY.py [start end]  (default: 0 125)
No native BRC execution, Source claim or independent Driver acceptance.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as F
from math import gcd
import json,sys
import C298_SHARED_DENOMINATOR_EXACT as base
import C288_ISOLATING_BOXES_EXACT as c288
import C275_STANDALONE_EXACT_REPLAY as src

def height(U):
    h=max(0,U.numerator.bit_length()-U.denominator.bit_length()+1)
    while U >= (1<<h):h+=1
    while h and U < (1<<(h-1)):h-=1
    return h

def one(i,path,k,W):
    lo=F(k,1<<24);hi=F(k+1,1<<24)
    terms=base.make_terms(path,lo,hi,W)
    _, (s,groups) = base.certificate_one(i,path,k,W)
    occurs=defaultdict(set)
    for j,(_,facs) in enumerate(terms):
        for n,d in facs:occurs[base.primitive_factor(d)[1]].add(j)
    canceled={q for q in groups if len(q)==2
              and occurs[q] in ({75,77},{76,78})}
    assert len(canceled)==2
    degree=sum((len(q)-1)*exp for q,exp in groups.items())-2
    assert degree in (265,352)
    roots={-q[0]//q[1] for q in groups
           if len(q)==2 and q[1] and (-q[0])%q[1]==0}
    choices=(T for T in range(-2400,2401)
             if not any(T<=r<=T+degree for r in roots))
    T=min(choices,key=lambda z:(max(abs(z),abs(z+degree)),abs(z),z))
    def numerator_at(t):
        D=F(s)
        for q,exp in groups.items():
            if q not in canceled:D*=base.poly_eval(q,t)**exp
        val=F(0)
        for coeff,facs in terms:
            v=coeff
            for n,d in facs:v*=base.poly_eval(n,t)/base.poly_eval(d,t)
            val+=v
        result=D*val
        assert result.denominator==1,(i,t)
        return result.numerator
    vals=[numerator_at(T+j) for j in range(degree+1)]
    g=s;factorial=1
    for j in range(degree+1):
        if j:factorial*=j
        b,r=divmod(vals[0],factorial)
        assert r==0,(i,j)
        g=gcd(g,b)
        if j<degree:
            vals=[vals[k+1]-vals[k] for k in range(len(vals)-1)]
    assert s%g==0
    U=F(s//g)
    for q,exp in groups.items():
        if q not in canceled:
            qlo=base.poly_eval(q,lo);qhi=base.poly_eval(q,hi)
            assert qlo>0 and qhi>0
            U*=max(qlo,qhi)**exp
    return [i,T,str(g),height(U)]

def main():
    lo,hi=map(int,sys.argv[1:3]) if len(sys.argv)>1 else (0,125)
    cert=json.loads(Path('C293_125_REFINED_BRACKETS.json').read_text())
    paths,_=c288.build_paths();W,_=src.floor_fixed_masses()
    assert len(paths)==len(cert['records'])==125
    out=[]
    for i in range(lo,hi):
        assert cert['records'][i][0]==i
        ans=one(i,paths[i],int(cert['records'][i][1]),W)
        out.append(ans)
        print('C304_EXACT_ROW',i,'g_bits',int(ans[2]).bit_length(),
              'strip_H',ans[3],flush=True)
    if (lo,hi)==(0,125):
        assert max(r[3] for r in out)==13400
        assert min(int(r[2]).bit_length() for r in out)==273
        assert max(int(r[2]).bit_length() for r in out)==418
    Path(f'C304_REFERENCE_OUTPUT_{lo}_{hi}.json').write_text(
        json.dumps(out,separators=(',',':'))+'\n')
    print('C304_REFERENCE_EXACT_PASS',lo,hi,len(out))
if __name__=='__main__':main()
