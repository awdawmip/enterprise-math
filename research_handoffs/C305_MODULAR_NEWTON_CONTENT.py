#!/usr/bin/env python3
"""C305: exact modular falling-factorial content certificates for C195/H168 auxiliary paths.

Author-level structural computation; does not create an EM CLAIM or grant native BRC meaning.
Source: frozen C301 portable inputs; no external network required.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from functools import reduce
from math import factorial, gcd, lcm
from pathlib import Path
import sys, hashlib, json, time, os
ROOT=Path(__file__).parent / 'EM_C301_EXACT_PORTABLE'
sys.path.insert(0,str(ROOT))
os.chdir(ROOT)
import C298_SHARED_DENOMINATOR_EXACT as c298
import C288_ISOLATING_BOXES_EXACT as c288
import C275_STANDALONE_EXACT_REPLAY as src

def eval_p(p,t):
    y=0
    for a in reversed(p):y=y*t+a
    return y

def prepare(idx,path,k24,W):
    lo=Fraction(k24,1<<24);hi=Fraction(k24+1,1<<24)
    terms=c298.make_terms(path,lo,hi,W)
    s,groups=c298.certificate_one(idx,path,k24,W)[1]
    occurs=defaultdict(set)
    prepared=[]
    for j,(coeff,factors) in enumerate(terms):
        power=Counter();den_scale=coeff.denominator; nums=[]
        for n,den in factors:
            content,q=c298.primitive_factor(den)
            den_scale*=content;power[q]+=1;nums.append(tuple(int(x) for x in n))
            occurs[q].add(j)
        assert s%den_scale==0
        prepared.append((int(coeff.numerator*(s//den_scale)),nums,power))
    cancels=sorted([q for q in groups if len(q)==2 and occurs[q] in ({75,77},{76,78})])
    assert len(cancels)==2
    degree=sum((len(q)-1)*m for q,m in groups.items())-2
    assert degree in (265,352)
    return s,groups,prepared,cancels,degree

def window_start(groups,degree):
    T=0
    while True:
        bad=False
        for q in groups:
            if len(q)==2 and q[1]!=0:
                r,num=divmod(-q[0],q[1])
                if num==0 and T<=r<=T+degree:bad=True;break
        if not bad:return T
        T+=degree+1

def numerator_residues(s,groups,terms,cancels,degree,T):
    M=s*factorial(degree)
    xs=[]
    for t in range(T,T+degree+1):
        qv={q:eval_p(q,t) for q in groups}
        assert all(x!=0 for x in qv.values()),(t,'denominator factor zero')
        Q=1
        for q,e in groups.items():Q*=qv[q]**e
        cprod=eval_p(cancels[0],t)*eval_p(cancels[1],t)
        assert cprod!=0
        N=M*abs(cprod)
        v=0
        for coeff,nums,power in terms:
            qden=1
            for q,e in power.items():qden*=qv[q]**e
            assert Q%qden==0
            term=coeff*(Q//qden)
            for n in nums:term=(term*eval_p(n,t))%N
            v=(v+term)%N
        assert v%abs(cprod)==0
        z=(v//abs(cprod))%M
        if cprod<0:z=(-z)%M
        xs.append(z)
    return M,xs

def gcd_from_newton_residues(s,degree,M,values):
    curr=list(values);facts=1;g=s
    for k in range(degree+1):
        if k:facts*=k
        assert curr[0]%facts==0,(k,'factorial congruence failure')
        bk=(curr[0]//facts)%s
        g=gcd(g,bk)
        if k<degree:
            curr=[(curr[j+1]-curr[j])%M for j in range(len(curr)-1)]
    return g

def one(idx,path,k24,W):
    tic=time.monotonic()
    s,groups,terms,cancels,d=prepare(idx,path,k24,W)
    T=window_start(groups,d)
    M,values=numerator_residues(s,groups,terms,cancels,d,T)
    g=gcd_from_newton_residues(s,d,M,values)
    assert s%g==0
    return {'index':idx,'degree':d,'sample_start':T,'sample_count':d+1,
            'scalar_bit_length':s.bit_length(),'modulus_bit_length':M.bit_length(),
            'content_gcd_dec':str(g),'content_gcd_bits':g.bit_length(),
            'method':'modular A_shared evaluation / canceled-factor exact division / Newton differences',
            'elapsed_seconds_observed':round(time.monotonic()-tic,3)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--indices',default='0,28,63');ap.add_argument('--output',default='C305_AUTHOR_MODULAR_AUDIT.json');args=ap.parse_args()
    rr=json.loads((ROOT/'C293_125_REFINED_BRACKETS.json').read_text())
    assert len(rr['records'])==125
    paths,_=c288.build_paths();W,_=src.floor_fixed_masses()
    ids=list(range(125)) if args.indices=='all' else [int(i) for i in args.indices.split(',')]
    rows=[]
    for i in ids:
        assert rr['records'][i][0]==i
        row=one(i,paths[i],int(rr['records'][i][1]),W)
        print('C305_MODULAR_PASS',i,'degree',row['degree'],'g-bits',row['content_gcd_bits'],'M-bits',row['modulus_bit_length'],'elapsed',row['elapsed_seconds_observed'],flush=True)
        rows.append(row)
    obj={'schema':'C305_MODULAR_NEWTON_AUTHOR_AUDIT_V1',
         'model':'C195/H168 79-positive-rational-branch auxiliary',
         'status':'AUTHOR_LOCAL_EXACT_NOT_DRIVER_ADMITTED',
         'source_C293_records_sha256':rr['records_sha256'],
         'path_count_checked':len(rows), 'rows':rows,
         'scope':'Exact modular integer evaluations and Newton-gcd identity; upstream C300/C301 polynomial identity conditional for application',
         'limits':'No formal native research CLAIM, no signed/phase or native X6 transfer.'}
    Path(args.output).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    print('C305_MODULAR_NEWTON_EXACT_PASS',len(rows),flush=True)
if __name__=='__main__':main()
