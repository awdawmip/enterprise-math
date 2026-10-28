#!/usr/bin/env python3
"""Exact supplements, never substitutes for the all-modulus proof."""
import hashlib
import itertools
import json
import math
import random
from pathlib import Path
import sympy as sp

def dot(x, y):
    return sum(a*b for a,b in zip(x,y))

def q(x):
    return dot(x,x)

def in_H(d,m):
    return all((2*z)%m==0 for z in d) and q(d)%m==0

def measured(x, offsets,m):
    return tuple(q(tuple(a+b for a,b in zip(x,t)))%m for t in offsets)

def primitive_kernel(rows):
    if not rows:
        return (1,0,0,0,0,0)
    v=sp.Matrix(rows).nullspace()[0]
    denominator=sp.ilcm(*[x.q for x in v])
    integral=[int(x*denominator) for x in v]
    g=math.gcd(*integral)
    result=tuple(x//g for x in integral)
    assert g>0 and math.gcd(*result)==1
    assert all(dot(r,result)==0 for r in rows)
    return result

def main():
    rng=random.Random(20261028)
    states=list(itertools.product((0,1),repeat=6))
    zero=(0,)*6
    basis=[tuple(int(i==j) for i in range(6)) for j in range(6)]
    upper=(zero,*basis[:5])
    vectors={measured(x,upper,4):x for x in states}
    assert len(vectors)==64
    assert len({q(x)%2 for x in states})==2
    lower_witnesses=[]
    count=0
    for k in range(1,7):
        for _ in range(50):
            offsets=[tuple(rng.randint(-12,12) for _ in range(6)) for _ in range(k)]
            a=offsets[0]
            rows=[tuple(z-t for z,t in zip(b,a)) for b in offsets[1:]]
            v=primitive_kernel(rows)
            x=tuple(-a_i-v_i for a_i,v_i in zip(a,v))
            y=tuple(-a_i+v_i for a_i,v_i in zip(a,v))
            d=tuple(2*z for z in v)
            assert all(q(tuple(z+t for z,t in zip(x,b)))==q(tuple(z+t for z,t in zip(y,b))) for b in offsets)
            for m in range(1,41):
                assert measured(x,offsets,m)==measured(y,offsets,m)
                assert in_H(d,m)==(m in (1,2,4))
                count+=1
            if len(lower_witnesses)<6:
                lower_witnesses.append({'offsets':offsets,'v':v,'x':x,'y':y})
    parity_witnesses=[]
    for k in range(1,6):
        for _ in range(100):
            offsets=[tuple(rng.randint(-8,8) for _ in range(6)) for _ in range(k)]
            a=offsets[0]
            rows=[tuple(z-t for z,t in zip(b,a)) for b in offsets[1:]]
            d=next(d for d in states if any(d) and sum(d)%2==0 and all(dot(r,d)%2==0 for r in rows))
            i=next(j for j in range(6) if d[j])
            x=[0]*6
            x[i]=(-q(d)//2-dot(a,d))%2
            y=tuple(z+t for z,t in zip(x,d))
            assert measured(x,offsets,4)==measured(y,offsets,4)
            assert not in_H(d,4)
            if len(parity_witnesses)<5:
                parity_witnesses.append({'offsets':offsets,'d':d,'x':x,'y':y})
    out={'status':'EXACT_SUPPLEMENT_PASS','complete_m4_upper_states':64,
         'integer_kernel_schemes':300,'modulus_checks':count,
         'm4_lower_schemes':500,'sample_integer_collisions':lower_witnesses,
         'sample_m4_collisions':parity_witnesses,
         'scope':'Finite exact supplementary tests; general theorem is proved in QUADRATIC_EVEN_PROBES.md.',
         'sympy_version':sp.__version__,
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    target=Path(__file__).with_name('quadratic_validation.json')
    target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if not k.startswith('sample_')},indent=2))

if __name__=='__main__':
    main()
