#!/usr/bin/env python3
"""R124.3: exact two-integer resonant directed arc lift."""
from fractions import Fraction as F
from itertools import product
from random import Random
from json import dumps
from pathlib import Path
from check_r124 import af, sub, feasible, floor_candidates, y_candidates, direct_signature_set, kval


def witness2(x,j,a,c,N,d,m,L,H,bits):
    assert c-a in (d,-d)
    yi=[af(N+i*d-j-a,x) for i in range(m)]
    cnt=0
    for n,k in product(y_candidates(x,N-j-a,L,H),floor_candidates(d,L,H)):
        beta=sub(af(d),af(0,k))
        base=[(beta,False),(sub(af(0,1),beta),True)]
        if feasible(base,L,H) is None:continue
        for qs in product(*[range(i+1) for i in range(m)]):
            z=[sub(y,af(0,n+i*k+qs[i])) for i,y in enumerate(yi)]
            cs=base+[(w,False) for w in z]+[(sub(af(0,1),w),True) for w in z]
            if feasible(cs,L,H) is None:continue
            cases=[(beta,[])] if c-a==d else [(af(0),[(sub(af(0),beta),False),(beta,False)]),
                                              (sub(af(0,1),beta),[(beta,True)])]
            for delta,guards in cases:
                # For negative resonance: beta=0 -> delta=0; beta>0 -> delta=1-beta.
                full=cs+guards+[(sub(delta,w),True) if b else (sub(w,delta),False)
                                for b,w in zip(bits,z)]
                cnt+=1
                theta=feasible(full,L,H)
                if theta is not None:
                    assert all(kval(x,j,a,c,N+i*d,theta)==bits[i] for i in range(m))
                    return theta,cnt
    return None,cnt


def run():
    rng=Random(1252026)
    tests=cnt=reachable=0;cases=0
    inputs=[]
    for a in (-3,-1,0,2):
        for d in (-2,-1,1,2):
            for sign in (-1,1):
                inputs.append((F(1,3),1,a,a+sign*d,-1,d,3))
    for _ in range(80):
        x=F(rng.randint(-3,3),rng.randint(2,8))
        j=rng.randint(-2,2);a=rng.randint(-3,3)
        N=rng.randint(-3,3);d=rng.choice([-2,-1,1,2]);sign=rng.choice([-1,1])
        inputs.append((x,j,a,a+sign*d,N,d,rng.choice([2,3])))
    for x,j,a,c,N,d,m in inputs:
        L,H=F(0),F(1)
        truth,_=direct_signature_set(x,j,a,c,N,d,m,L,H)
        for bits in product((0,1),repeat=m):
            w,k=witness2(x,j,a,c,N,d,m,L,H,bits)
            tests+=1;cnt+=k;reachable+=w is not None
            assert (w is not None)==(bits in truth),(x,j,a,c,N,d,m,bits,w,truth)
        cases+=1
    return {'status':'R124_RESONANT_2D_PASS','seed':1252026,'cases':cases,
            'signature_tests':tests,'reachable_signatures':reachable,
            'two_integer_branch_tests':cnt,
            'scope':'c-a=+d or -d, signed bounded j,a,N,d, m=2,3; exact direct phase-cut crosscheck'}
if __name__=='__main__':
    data=run();print(dumps(data,sort_keys=True))
    Path(__file__).with_name('verification_r124_resonant_generated.json').write_text(dumps(data,indent=2,sort_keys=True)+'\n')
