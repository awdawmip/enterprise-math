#!/usr/bin/env python3
"""R124.2: 3-integer relative-phase lift, with exact direct comparator."""
from fractions import Fraction as F
from itertools import product
from random import Random
from json import dumps
from pathlib import Path
from check_r124 import af, sub, feasible, floor_candidates, y_candidates, direct_signature_set, kval, floor, frac


def lifted_three(x,j,a,c,N,d,m,L,H,bits):
    # p = floor((c-a)*theta), n=floor(x+(N-j-a)*theta), k=floor(d*theta)
    checks=0
    y=[af(N+i*d-j-a,x) for i in range(m)]
    for p,n,k in product(floor_candidates(c-a,L,H),
                         y_candidates(x,N-j-a,L,H),floor_candidates(d,L,H)):
        delta=sub(af(c-a),af(0,p))
        beta=sub(af(d),af(0,k))
        base=[(delta,False),(sub(af(0,1),delta),True),
              (beta,False),(sub(af(0,1),beta),True)]
        if feasible(base,L,H) is None:continue
        for qs in product(*[range(i+1) for i in range(m)]):
            z=[sub(v,af(0,n+i*k+qs[i])) for i,v in enumerate(y)]
            cs=base+[(w,False) for w in z]+[(sub(af(0,1),w),True) for w in z]
            if feasible(cs,L,H) is None:continue
            cs += [(sub(delta,w),True) if b else (sub(w,delta),False)
                   for b,w in zip(bits,z)]
            checks+=1
            theta=feasible(cs,L,H)
            if theta is not None:
                assert all(kval(x,j,a,c,N+i*d,theta)==bits[i] for i in range(m))
                assert L<theta<H
                return theta,checks
    return None,checks


def run():
    rng=Random(1242026)
    targets=[
      (F(1,3),0,0,0,2,1,2),
      (F(1,3),0,1,1,0,2,2),
      (F(0),0,0,1,1,1,2),
      (F(1,5),1,2,-1,1,-2,3),
      (F(3,7),-1,-2,3,-2,1,3),
      (F(2,5),1,-1,2,1,-1,4),
      (F(-1,7),-2,2,-3,2,1,4)
    ]
    for _ in range(80):
        x=F(rng.randint(-4,4),rng.randint(2,8))
        j=rng.randint(-2,2);a=rng.randint(-3,3);c=rng.randint(-3,3)
        N=rng.randint(-3,3);d=rng.choice([-2,-1,1,2]);m=rng.choice([2,3])
        targets.append((x,j,a,c,N,d,m))
    tests=checks=reachable=0
    for x,j,a,c,N,d,m in targets:
        L,H=F(0),F(1)
        direct,_=direct_signature_set(x,j,a,c,N,d,m,L,H)
        for bits in product((0,1),repeat=m):
            w,nq=lifted_three(x,j,a,c,N,d,m,L,H,bits)
            checks+=nq
            assert (w is not None)==(bits in direct), (x,j,a,c,N,d,m,bits,w,direct)
            tests+=1;reachable+=w is not None
    # Large signed exact positive certificates, interpreted in shifted phase.
    big=[]
    for N,d in ((10**100+7,-(10**90+5)), (-(10**110+9),10**105+3)):
        x,j,a,c,theta,m=F(2,7),2,-3,5,F(37,101),4
        p=floor(F(c-a)*theta); n=floor(x+F(N-j-a)*theta);k=floor(F(d)*theta)
        alpha=frac(x+F(N-j-a)*theta);beta=frac(F(d)*theta)
        qs=[floor(alpha+i*beta) for i in range(m)]
        delta=F(c-a)*theta-p
        z=[x+F(N+i*d-j-a)*theta-n-i*k-qs[i] for i in range(m)]
        assert 0<=delta<1 and all(0<=v<1 for v in z)
        assert [int(v<delta) for v in z]==[kval(x,j,a,c,N+i*d,theta) for i in range(m)]
        big.append({'N_digits':len(str(abs(N))),'d_digits':len(str(abs(d))),
                    'q':qs,'signature':[int(v<delta) for v in z]})
    return {'status':'R124_RELATIVE_3D_PASS','seed':1242026,'cases':len(targets),
            'signature_tests':tests,'reachable_signatures':reachable,
            'three_integer_branch_tests':checks,'large_signed_certificates':big,
            'scope':'m=2,3 random and two m=4 targeted inputs; exact rational, (0,1) parameter'}

if __name__=='__main__':
    data=run();print(dumps(data,sort_keys=True))
    Path(__file__).with_name('verification_r124_relative_generated.json').write_text(dumps(data,indent=2,sort_keys=True)+'\n')
