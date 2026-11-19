"""Stopped native bit/work caller, exact mass checks and first-one separation.
python landing_check.py --core /path/to/src/enterprise_math/brc_weighted_recurrent.py
"""
import argparse
from collections import Counter
from fractions import Fraction as F
from math import isqrt
import json
from pathlib import Path
from random import Random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'seventh'))
from decoding_check import CORE_SHA, Digits, certify


def survive(d,Q):
    v,r=divmod(Q,d)
    return F((d-r)*v*v+r*(v+1)**2,Q*Q)


def atom(d,Q):
    r=Q%d
    return F(min(r,d-r),2*Q*Q)


def law(d,width):
    return [atom(d,1<<t) for t in range(width)]+[survive(d,1<<width)]


def sqrt_interval(x):
    scale=1<<90
    lo=isqrt((x.numerator*scale*scale)//x.denominator)
    return F(lo,scale),F(lo+1,scale)


def delta2(x,y):
    l,u=sqrt_interval(x);v,w=sqrt_interval(y)
    return max(l-w,v-u,0)**2,max(abs(l-w),abs(u-v))**2


def arithmetic():
    masses=info=0;enclosures=[]
    for d in range(1,180,2):
        prev=F(1)
        for t in range(21):
            Q=1<<t;post=survive(d,Q*2)
            assert atom(d,Q)==prev-post;prev=post;masses+=1
    for k in range(3,12):
        q=1<<k
        for u in range(1,min(q//2,55)-1,2):
            for h in (0,1,2,4,8,12):
                l0,u0=delta2(F(u),F(u+2))
                lead=(1-F(1,2**h))/(q*q)
                lows=ups=0
                for x,y in zip(law(q+u,k+h),law(q+u+2,k+h)):
                    a,b=delta2(x,y);lows+=a;ups+=b
                err=32*F(u+2,q**3)
                assert lows>=lead*u0-err and ups<=lead*l0+err
                if (k,u,h) in [(5,3,1),(5,3,8),(9,5,1),(9,5,8),(11,1,12)]:
                    sc=10**12
                    enclosures.append([q,u,h,int(lows*sc),-((-ups*sc)//1)])
                info+=1
    return dict(exact_nested_mass_comparisons=masses,fixed_point_Hellinger_tests=info,
                squared_Hellinger_intervals_times_1e12=enclosures)


def rows(h,N,a,s,q):
    n=(N-1).bit_length();L=n+(n+s-1)//s;m=L-n+1;k=q.bit_length()-1
    powers=[a]
    for _ in range(1,L):powers.append(h.mm(powers[-1],powers[-1],N))
    counts={1:1};bank=[];data=[]
    for t in range(m):
        Q=1<<t
        multiplier=powers[L-1-t]
        move={z:h.mm(z,multiplier,N) for z in counts}
        shifted={w:counts[z] for z,w in move.items()}
        assert len(shifted)==len(counts)
        nxt={};draw={}; positive=negative=both=0
        norm=sum(h.mul(c,c) for c in counts.values())
        for z in sorted(set(counts)|set(shifted)):
            x=counts.get(z,0);y=shifted.get(z,0)
            plus=h.add(x,y);minus=h.distance(x,y)
            a2=h.mul(plus,plus);b2=h.mul(minus,minus);total=h.add(a2,b2)
            assert total==2*(x*x+y*y)
            nxt[z]=plus;draw[z]=(a2,total)
            positive=h.add(positive,a2);negative=h.add(negative,b2)
            both+=bool(x and y)
        assert positive+negative==4*norm and sum(nxt.values())==2*Q
        data.append([t,norm,positive,negative,len(nxt),both])
        bank.append((move,draw)); counts=nxt
    stop=min(k+1,m)
    return n,L,m,stop,powers[n-1],bank,data


def replay(h,N,a,s,q,seed,repetitions):
    start=h.cells
    n,L,m,cap,base,bank,data=rows(h,N,a,s,q)
    prep=h.cells-start
    rng=Random(seed)
    freq=Counter();moves=steps=0
    for _ in range(repetitions):
        work=1
        for t,(move,draw) in enumerate(bank[:cap]):
            steps+=1
            if rng.getrandbits(1):
                work=move[work];moves+=1
            top,den=draw[work]
            if rng.randrange(den)>=top:
                freq[t]+=1;break
        else:freq[cap]+=1
    # Only these integer counts, the public width, and q pass to the decoder.
    # All finite routine examples have public U <= 5. Oracle order used only after inference.
    U={8:3,16:3,32:5}[q]
    candidate=None
    if cap>q.bit_length()-1:
        hit=freq[q.bit_length()-1]
        candidate=q+min(range(1,U+1,2),key=lambda u:abs(2*q*q*hit-repetitions*u))
    certified=certify(h,N,a,base,candidate) if candidate is not None else None
    return dict(N=N,base=a,public_q=q,s=s,n=n,L=L,width=m,observed_cap=cap,
                seed=seed,trials=repetitions,stopped_calls=dict(sorted(freq.items())),
                source_proposals=steps,issued_moves=moves,all_plus_and_first_minus=data,
                cached_source_columns=sum(len(d) for d,_ in bank),
                native_adder_cells_prepare=prep,native_adder_cells_verify=h.cells-start-prep,
                inferred=candidate,certified_order_and_optional_factor=certified)


def run(core):
    h=Digits(core);N=199
    # The comparison caller emits one Bernoulli bit. Reading its hidden two full
    # addresses as a stream can violate all-zero prefix nesting.
    check=(h.power(175,0,N)==h.power(175,9,N) and
           h.power(h.mm(175,175,N),0,N)!=h.power(h.mm(175,175,N),4,N))
    assert check
    cases=[]
    for N,a,q,d in [(199,175,8,9),(199,125,8,11),(647,300,16,17),(647,104,16,19),
                    (427351,284799,32,33),(427351,30288,32,35),(427351,389548,32,37)]:
        for s in (1,2,4):
            row=replay(h,N,a,s,q,75000+17*a+s,65536)
            for t,norm,positive,negative,labels,both in row['all_plus_and_first_minus']:
                Q=1<<t
                assert F(norm,Q*Q)==survive(d,Q) and F(negative,4*Q*Q)==atom(d,Q)
            if row['inferred'] is not None:
                assert row['certified_order_and_optional_factor']==(d,None)
            cases.append(row)
    return {'BRC_core_sha256':CORE_SHA,'source_feedback':'identity on the surviving all-zero history',
            'two_addresses_are_not_a_nested_caller':{'N':199,'base':175,'full_addresses':[0,9],
                'prefix_addresses':[0,4],'endpoints_full_equal':True,'prefix_endpoints_equal':False},
            'theory_checks':arithmetic(),'native_stopped_runs':cases}


if __name__=='__main__':
    arg=argparse.ArgumentParser()
    arg.add_argument('--core',type=Path,default=Path('src/enterprise_math/brc_weighted_recurrent.py'))
    print(json.dumps(run(arg.parse_args().core),indent=2))
