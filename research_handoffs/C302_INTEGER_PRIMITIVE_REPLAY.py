#!/usr/bin/env python3
"""C302: exact scalar numerator content for 125 C195/H168 auxiliary paths.

Companion inputs from the C301 portable bundle:
C298_SHARED_DENOMINATOR_EXACT.py, C288_ISOLATING_BOXES_EXACT.py,
C275_STANDALONE_EXACT_REPLAY.py, C293_125_REFINED_BRACKETS.json.
Runs author-level exact Z[t] arithmetic; not a native BRC or admitted Result.
Usage: python C302_INTEGER_PRIMITIVE_REPLAY.py 0 1 ... 124
(no indices defaults to all 125; suitable for splitting into bounded chunks).
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import gcd
from time import monotonic
import json, hashlib, sys
import C298_SHARED_DENOMINATOR_EXACT as base
import C288_ISOLATING_BOXES_EXACT as c288
import C275_STANDALONE_EXACT_REPLAY as src

def strip(v):
    while len(v)>1 and v[-1]==0: v.pop()
    return v

def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: z[i+j]+=x*y
    return strip(z)

def divide_exact(a,b):
    a=a[:]; b=strip(list(b))
    m=len(b)-1
    assert len(a)>=len(b)
    quo=[0]*(len(a)-m)
    for k in range(len(quo)-1,-1,-1):
        q,r=divmod(a[k+m],b[m])
        assert r==0, ('nonintegral Z[t] quotient',k,r)
        quo[k]=q
        if q:
            for j,y in enumerate(b): a[k+j]-=q*y
    assert not any(a), 'nonzero polynomial remainder'
    return strip(quo)

def eval_poly(poly,t):
    x=0
    for a in reversed(poly): x=x*t+a
    return x

def one(i,paths,records,weights):
    path=paths[i]; row=records[i]; assert row[0]==i
    lo=F(row[1],1<<24);hi=F(row[1]+1,1<<24)
    terms=base.make_terms(path,lo,hi,weights)
    s,groups=base.certificate_one(i,path,int(row[1]),weights)[1]
    occurrence=defaultdict(set)
    encoded=[]
    for j,(coefficient,factors) in enumerate(terms):
        den=coefficient.denominator; divs=[]; numpoly=[1]
        for n,d in factors:
            c,q=base.primitive_factor(d)
            den*=c;divs.append(q);numpoly=mul(numpoly,n)
            occurrence[q].add(j)
        assert s%den==0
        encoded.append((coefficient.numerator*(s//den),divs,numpoly))
    canceled=sorted(q for q in groups
                    if len(q)==2 and occurrence[q] in ({75,77},{76,78}))
    assert len(canceled)==2
    P=[1]
    for q,exp in sorted(groups.items()):
        for _ in range(exp): P=mul(P,q)
    assert len(P)-1 in (267,354)
    A=[0]*len(P)
    cached={}
    for c,denfactors,num in encoded:
        key=tuple(sorted(denfactors))
        if key not in cached:
            pol=P
            for q in key: pol=divide_exact(pol,q)
            cached[key]=pol
        term=mul(cached[key],num)
        assert len(term)<=len(A)
        for k,x in enumerate(term): A[k]+=c*x
    A=strip(A)
    for q in canceled: A=divide_exact(A,q)
    for q in canceled: P=divide_exact(P,q)
    assert len(A)<=len(P)
    # The 79-term rational extension identity at two integer test points.
    for t in (0,1):
        D=s*eval_poly(P,t);n=eval_poly(A,t)
        assert D
        v=F(0)
        for c,factors in terms:
            z=c
            for nn,dd in factors:
                z*=F(eval_poly(nn,t),eval_poly(dd,t))
            v+=z
        assert F(n,D)==v
    numerator_content=0
    for x in A: numerator_content=gcd(numerator_content,abs(x))
    g=gcd(numerator_content,s)
    assert g>0 and s%g==0
    # Exact equality: numerator_content is a positive multiple of g
    # with the same bit length, hence must be g.
    assert numerator_content.bit_length()==g.bit_length()
    assert numerator_content==g
    witness=hashlib.sha256(('\n'.join(map(str,A))+'\n').encode()).hexdigest()
    return {'index':i,'degree':len(P)-1,'numerator_degree':len(A)-1,
            'scalar_bits':s.bit_length(),'gcd_bits':g.bit_length(),
            'primitive_numerator':True,'gcd_decimal':str(g),
            'numerator_coefficients_sha256':witness}

def main(indices):
    records=json.loads(Path('C293_125_REFINED_BRACKETS.json').read_text())['records']
    paths,_=c288.build_paths()
    weights,_=src.floor_fixed_masses()
    assert len(paths)==len(records)==125
    if not indices: indices=list(range(125))
    assert len(indices)==len(set(indices))
    result=[]
    for i in indices:
        assert 0<=i<125
        r=one(i,paths,records,weights)
        result.append(r)
        print('C302_EXACT_COEFFICIENT_PASS',i,'gcd_bits',r['gcd_bits'],flush=True)
    output={'schema':'EM_C302_PRIMITIVE_NUMERATOR_EXACT_REPLAY_V1',
            'count':len(result),'rows':result,'not_admitted':True}
    Path('C302_REPLAY_OUTPUT.json').write_text(
        json.dumps(output,sort_keys=True,ensure_ascii=False,indent=2)+'\n')
    print('C302_EXACT_PASS',len(result),flush=True)

if __name__=='__main__':
    main(list(map(int,sys.argv[1:])))
