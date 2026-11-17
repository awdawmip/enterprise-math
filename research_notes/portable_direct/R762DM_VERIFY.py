#!/usr/bin/env python3
"""Exact integral group-ring verification for R762DM.
Finite author check only; algebraic proof is in the companion theorem file.
"""
import json, math, hashlib
from collections import defaultdict

B = ((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))

def step(dist, Q):
    nxt = defaultdict(int)
    for (x,y,z), cnt in dist.items():
        for a,b,c in B:
            nxt[((x+a)%Q,(y+b)%Q,(z+c)%Q)] += cnt
    return dict(nxt)

def vp(x, p):
    if not x: return None
    v=0
    while x%p==0:
        x//=p;v+=1
    return v

def main():
    cases = [(2,26),(4,26),(8,26),(16,26),(32,34)]
    checks, samples, point_checks = [], [], 0
    for Q, nmax in cases:
        dist={(0,0,0):1}; g=0
        for n in range(1,nmax+1):
            dist=step(dist,Q)
            assert sum(dist.values())==6**n, (Q,n,"mass")
            values=list(dist.values())
            g=math.gcd(*values)
            v=vp(g,2)
            expected=max(0, n//(Q//2)-1)
            assert v==expected,(Q,n,v,expected)
            point_checks += len(dist)
            if n%2==0:
                k=n//2
                seeds=36**k//g
                if Q==2:
                    assert seeds==2*9**k
                if n in (2,4,8,16,24,32):
                    samples.append({'Q':Q,'blocks_k':k,'gcd':str(g),'v2_gcd':v,
                                    'min_equal_seeds':str(seeds), 'support_size':len(dist)})
            checks.append({'Q':Q,'n':n,'expected_v2':expected,'actual_v2':v})
    for Q in (2,4,8,16):
        direct=defaultdict(int)
        for x,y,z in B:
            for a,b,c in B:
                direct[((x+a-1)%Q,(y+b-1)%Q,(z+c-1)%Q)] += 1
        d2=step(step({(0,0,0):1},Q),Q)
        assert len(direct)==len(d2)
        for key,num in d2.items():
            shifted=tuple((t-1)%Q for t in key)
            assert direct[shifted]==num
    obj={
        'schema':'R762DM_AUTHOR_EXACT_VERIFICATION_V1',
        'task_id':'RS-X6-TRIADIC-CLOSURE-DYNAMICS',
        'result':'PASS',
        'arithmetic':'Python arbitrary-precision integers, exact group-algebra convolution and gcd',
        'cases':[{'Q':q,'n_min':1,'n_max':n} for q,n in cases],
        'configurations':len(checks),
        'nonzero_coefficient_checks':point_checks,
        'direct_36_way_checks':4,
        'even_n_seed_checks':sum(1 for c in checks if c['n']%2==0),
        'claim':'v2(content P^n mod (X^Q,Y^Q,Z^Q)=(max(0,floor(n/(Q/2))-1))) for Q=2^a',
        'samples':samples,
        'limitations':'Finite author tests are not a proof; theorem relies on group-ring factorization and local mod-2 algebra. Does not authorize a primitive TRIADIC_CLOSURE_E event.',
        'independent_review':'NOT_REVIEWED'
    }
    path='R762DM_EVIDENCE.json'
    with open(path,'w',encoding='utf-8') as f:
        json.dump(obj,f,ensure_ascii=False,indent=2,sort_keys=True)
    print('PASS configs',len(checks),'nonzero coefficients',point_checks,'direct 36-way',4)
    print('samples',samples)
    print('sha256 evidence',hashlib.sha256(open(path,'rb').read()).hexdigest())

if __name__=='__main__': main()
