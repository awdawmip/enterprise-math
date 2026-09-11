"""Exact small checks of independently observed square-root BRC states.

Only integer geometry and small positive N are studied. No factor routines.
"""
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
import sys


def residue(n):
    j = isqrt(n)
    return n-j*j


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--enterprise-root',type=Path,required=True)
    parser.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent)
    args=parser.parse_args()
    sys.path.insert(0,str(args.enterprise_root/'src'))
    from enterprise_math.brc_multiplier_basin import point_cost_state, square_multiplier_law

    counters=Counter()
    down=Counter()
    all_residuals=Counter()
    down_k=Counter()
    up_k=Counter()
    sample=[]
    horizon=32
    for j in range(1,horizon+1):
        costs_down=[]
        costs_up=[]
        for r in range(2*j+1):
            n=j*j+r
            state=point_cost_state(n,1)
            assert (state.target_root,state.subtraction_cost,state.addition_cost)==(j,r,2*j+1-r)
            counters['existing_point_state_checks']+=1
            all_residuals[r]+=1
            if r==0:
                mode='SQUARE'
            elif r<=j:
                mode='DOWN_CHEAPER'
                down[r]+=1
                down_k[j]+=1
                costs_down.append(r)
                for t in range(j+1):
                    assert isqrt(n+t)==j
                    counters['root_only_forward_checks']+=1
                for t in range(r+1):
                    assert residue(n+t)==r+t
                    counters['residual_only_forward_checks']+=1
            else:
                mode='UP_CHEAPER'
                up_k[j]+=1
                costs_up.append(2*j+1-r)
            if j<=6:
                sample.append({'N':n,'J':j,'R':r,'mode':mode})
        assert down_k[j]==up_k[j]==j
        assert costs_down==costs_up[::-1]
        assert Fraction(sum(costs_down),j)==Fraction(j+1,2)
        counters['partition_and_reflection_basins']+=1
        # At j=1 the down-cheaper population is a singleton.
        assert isqrt(j*j+j+(j+1))==j+1
        if j>=2:
            assert isqrt(j*j+1+(j+1))==j
            counters['root_window_sharpness_pairs']+=1
        for s in range(1,5):
            law=square_multiplier_law(j,s)
            assert law.support_size==min(s,2*j+1)
            counters['existing_root_support_law_checks']+=1

    for r in range(2*horizon+1):
        expected=max(0,horizon-max(1,(r+1)//2)+1)
        assert all_residuals[r]==expected
        assert down[r]==(max(0,horizon-r+1) if r>=1 else 0)
        counters['pooled_residual_frequency_checks']+=1

    fibers=[]
    for r in range(1,33):
        first=max(1,(r+1)//2)
        ks=list(range(first,r+4))
        ns=[j*j+r for j in ks]
        assert all(residue(n)==r for n in ns)
        assert sum(r>j for j in ks)==r//2
        assert all(ns[i+2]-2*ns[i+1]+ns[i]==2 for i in range(len(ns)-2))
        left=r*r+r
        right=(r+1)**2+r
        assert residue(left+r+1)==0
        assert residue(right+r+1)==2*r+1
        counters['residual_fibers_and_sharpness_checks']+=1
        if r<=6:
            fibers.append({'R':r,'first_J':first,'up_cheaper_J_count':r//2,
                           'down_cheaper_from_J':r,'first_values':ns[:5]})

    # Mixed-state projections fail under +1.
    assert isqrt(4)==isqrt(8)==2
    assert isqrt(5)==2 and isqrt(9)==3
    assert residue(3)==residue(6)==2
    assert residue(4)==0 and residue(7)==3
    # At r=3, conditioning on down-cheaper gives a common 3-step update window.
    down_residue_example=[]
    for n in (12,19,28):
        assert residue(n)==3 and residue(n)<=isqrt(n)
        down_residue_example.append({'N':n,'R_at_t_0_to_4':[residue(n+t) for t in range(5)]})

    module=args.enterprise_root/'src/enterprise_math/brc_multiplier_basin.py'
    result={
        'researcher_id':'EM-HME-0CE4FD',
        'global_snapshot':'18b20e346491fdbb47f2c99da19b1a63198fc107',
        'reference_note_snapshot':'c5d6e6ed4aa4c899706e2a895f55733dc2eb3cb8',
        'executed_module_sha256':sha256(module.read_bytes()).hexdigest(),
        'scope':'positive-integer square-root BRC; direction means edit-cost preference, not a replacement of canonical floor collapse',
        'basin_horizon':horizon,'maximum_basin_N':(horizon+1)**2-1,
        'maximum_auxiliary_fiber_N':(horizon+3)**2+horizon,
        'checks':dict(counters),
        'residual_fiber_examples':fibers,
        'down_residue_update_example':down_residue_example,
        'visual_fixture':sample,
        'verdict':'PASS_EXACT_STATE_SEPARATION_LAWS_AND_SMALL_CHECKS',
    }
    args.output_dir.mkdir(parents=True,exist_ok=True)
    (args.output_dir/'brc_state_separated_sqrt_laws_20260908.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({key:result[key] for key in ('checks','residual_fiber_examples','down_residue_update_example','verdict')},indent=2))


if __name__=='__main__':
    main()

