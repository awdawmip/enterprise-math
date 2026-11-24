#!/usr/bin/env python3
"""Exact minimum cost-eight root in the fixed R3 progression.

The all-prime classification in ../prefix and ../tail supplies the two
structural alternatives. This calculator verifies all 320 retained-prefix
CRT starts, then excludes every smaller R3 root by the four compulsory
period-seven coordinates of the other alternative.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import permutations, product
import json
from math import gcd, lcm, prod
from pathlib import Path

A2 = 9807947978443488306255509703402695727949968778703073231931137913705883712843
S2 = 11356718000553566643685496313583434507970452519839503606327232707476034989690
T = 35095524795781473254136196580356738045833417602831290421525609131
RT = 21450781839625171583347380029424471704699683386785900439176732195
B = {0,3,5,8,10,15,21,23,26,28,30,31,33}
F7 = (29,43,1429,5419)
FAMILIES = (
    ('binary',(193,1153,6337,22253377,38941695937,278452876033),(0,4),8,((2,1),(4,2))),
    ('ternary',(33975937,138991501037953),(0,2),6,((2,1),(3,1))),
    ('mod5',(61681,4562284561,168692292721,469775495062434961),(0,6,8),10,((2,1),)),
)
ORDERS = {193:96,1153:288,6337:288,22253377:96,38941695937:288,
          278452876033:288,33975937:216,138991501037953:216,
          61681:40,4562284561:120,168692292721:360,469775495062434961:360,
          29:28,43:14,1429:84,5419:42}


def crt(pairs):
    root, modulus = 0, 1
    for residue, q in pairs:
        assert gcd(modulus,q) == 1
        root += modulus*((residue-root)*pow(modulus,-1,q) % q)
        modulus *= q
    return root, modulus


def factors(n):
    out, d = set(), 2
    while d*d <= n:
        while n % d == 0:
            out.add(d)
            n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


def root_phase(q,w):
    return pow(pow(2,16+18*w,q),-1,q)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('minimum_certificate.json'))
    args=parser.parse_args()
    a3,s3=crt([(A2,S2),(RT,T)])
    assert 0<a3<s3 and s3==S2*T
    for q,d in ORDERS.items():
        assert pow(2,d,q)==1
        assert all(pow(2,d//p,q)!=1 for p in factors(d))
    all_rows=[]; family_results=[]
    for name,primes,phases,period,fixed in FAMILIES:
        common=lcm(35,period,*(h for h,c in fixed))
        rows=[]; pattern_count=0
        for chosen in permutations(primes,len(phases)):
            assert all(ORDERS[q]//gcd(ORDERS[q],36)==period for q in chosen)
            coverage_rows=fixed+tuple((period,p) for p in phases)
            assert all(any(w%h==c for h,c in coverage_rows)
                       for w in range(common) if w%35 in B)
            pattern_count+=1
            for signs in product((1,-1),repeat=len(phases)):
                extra=[(sgn*root_phase(q,w)%q,q) for q,w,sgn in zip(chosen,phases,signs)]
                root,step=crt([(a3,s3)]+extra)
                assert root%s3==a3 and 0<root<step
                assert all(root*root*pow(2,32+36*w,q)%q==1 for q,w in zip(chosen,phases))
                row={'family':name,'primes':chosen,'phases_w':phases,'signs':signs,
                     'root_residues':[r for r,q in extra],'root':str(root),
                     'modulus':str(step),'digits':len(str(root))}
                rows.append(row)
        family_results.append({'family':name,'phase_dictionaries':pattern_count,
                               'progressions':len(rows),'coverage_w_period':common,
                               'minimum':min(rows,key=lambda x:int(x['root']))})
        all_rows+=rows
    assert [x['phase_dictionaries'] for x in family_results]==[30,2,24]
    assert [x['progressions'] for x in family_results]==[120,8,192]
    assert len(all_rows)==320
    minimum=min(all_rows,key=lambda x:int(x['root']))
    candidate=int(minimum['root']);bound=(candidate-a3)//s3
    assert a3+s3*bound==candidate and bound==63706

    # These are every possible root residue for an active f=7 channel on
    # n=8+12v. Even phases missing the A-set are counted, making the necessary
    # condition deliberately weaker and therefore safe for exclusion.
    active={q:{r for v in range(7)
               for r in (pow(pow(2,4+6*v,q),-1,q),
                         (-pow(pow(2,4+6*v,q),-1,q))%q)} for q in F7}
    assert all(len(active[q])==14 for q in F7)
    histogram=[0]*5;passing=[];stream=sha256()
    for k in range(bound):
        root=a3+s3*k
        mask=sum(1<<i for i,q in enumerate(F7) if root%q in active[q])
        histogram[mask.bit_count()]+=1
        stream.update(k.to_bytes(8,'big')+bytes([mask]))
        if mask==15:
            passing.append(k)
    assert histogram==[21939,31370,10276,121,0]
    assert not passing and sum(histogram)==bound
    assert minimum['primes']==(1153,193) and minimum['root_residues']==[885,63]
    result={'schema':'riesel-r3-global-minimum-eight-v1','status':'PASS',
            'A3':str(a3),'S3':str(s3),'families':family_results,
            'retained_prefix_progressions':all_rows,'minimum':minimum,
            'minimum_scope':'All a in historical R3 with delta_P(a)=8, using the complete prefix dichotomy and tail classification.',
            'minimum_R3_progression_index':bound,'smaller_R3_roots_checked':bound,
            'compulsory_f7_primes':F7,'active_f7_root_residues':{q:sorted(active[q]) for q in F7},
            'smaller_root_active_count_histogram':histogram,'all_four_active_indices':passing,
            'lower_root_mask_stream_sha256':stream.hexdigest(),
            'supplement':[5,13,19,73,38737,487824887233,1153,193],
            'delta_P':8,'tau_upper_bound':28,
            'proof_dependencies':['../prefix/proof.md','../tail/proof.md'],
            'native_execution_claimed_by_this_calculator':False}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','minimum':minimum,'smaller_roots_checked':bound,
                      'active_count_histogram':histogram,'output':str(args.output)},indent=2))


if __name__=='__main__':
    main()
