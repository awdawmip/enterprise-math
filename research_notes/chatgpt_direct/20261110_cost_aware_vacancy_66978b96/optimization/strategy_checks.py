"""Finite exact control checks for cost-aware vacancy evidence.

This module checks integer observation/weight models. Original BRC execution is
recorded separately by the integration program.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


def weight(key: int, width: int) -> int:
    return 2*key.bit_count()+4*(1-((key>>(width-1))&1))


def word_constant(slots: int) -> tuple[int, int, int]:
    colors=slots+1
    width=(colors-1).bit_length()
    full_width=(3*colors).bit_length()
    return width, full_width, 8*width+2*full_width+38


def check_weights() -> dict:
    weight_cells=dp_cells=0
    selected=[]
    for slots in range(2,64):
        colors=slots+1
        width,full_width,constant=word_constant(slots)
        high=1<<(width-1)
        weights={key:weight(key,width) for key in range(1,colors+1)}
        assert [k for k,v in weights.items() if v==2]==[high]
        assert weights[high+1]==4
        assert all(v>=4 for k,v in weights.items() if k!=high)
        weight_cells+=len(weights)
        dp=weights.copy()
        for horizon in range(1,65):
            expected=3*horizon-(horizon%2)
            assert min(dp.values())==expected
            dp_cells+=len(dp)
            if horizon in (1,2,8,32) and slots in (2,3,6,14,30,62):
                selected.append(dict(slots=slots,width=width,full_width=full_width,
                                     horizon=horizon,weight_minimum=expected,
                                     original_command_formula=8*slots+constant*horizon+expected))
            dp={key:value+min(cost for prior,cost in dp.items() if prior!=key)
                for key,value in weights.items()}
    return dict(slot_domain=[2,63],horizon_domain=[1,64],
                legal_key_weight_cells=weight_cells,dp_state_cells=dp_cells,
                selected_formula_values=selected)


def check_information() -> dict:
    preparations=states=under_budget_states=certificates=0
    domains=[]
    for slots in (2,3,4):
        width,_,_=word_constant(slots)
        high=1<<(width-1)
        masks=tuple(itertools.product(range(1<<width),repeat=slots))
        short_masks=[ms for ms in masks if sum(m.bit_count() for m in ms)<slots]
        rows=0
        for actual in itertools.product(range(high),repeat=slots):
            preparations+=1;rows+=1
            for ms in short_masks:
                under_budget_states+=1
                safe=[key for key in range(1,slots+2)
                      if all((value^key)&mask for value,mask in zip(actual,ms))]
                assert safe==[]
                untouched=next(i for i,m in enumerate(ms) if not m)
                # Replacing the untouched slot by any candidate leaves every
                # observed bit unchanged, and the candidate is then retained.
                for key in range(1,slots+2):
                    changed=list(actual);changed[untouched]=key
                    assert all((a&mask)==(v&mask)
                               for a,v,mask in zip(actual,changed,ms))
            ms=(high,)*slots
            safe=[key for key in range(1,slots+2)
                  if all((value^key)&mask for value,mask in zip(actual,ms))]
            assert high in safe and high+1 in safe
            certificates+=1
        states+=rows*len(masks)
        domains.append(dict(slots=slots,width=width,actual_value_range=[0,high-1],
                            preparations=rows,mask_states_per_preparation=len(masks),
                            tested_under_budget_masks_per_preparation=len(short_masks)))
    return dict(domains=domains,preparations=preparations,
                complete_mask_state_domain_size=states,
                under_budget_mask_states_actually_checked=under_budget_states,
                high_bit_certificates_checked=certificates,
                note='All under-r probe masks in each declared domain; other masks are counted as domain size, not executed')


def check_fixed_entry() -> dict:
    horizons=first_even_cases=0
    rows=[]
    for width in range(3,9):
        modulus=1<<width;slots=modulus-2;half=slots//2;high=modulus//2
        prefix=tuple(range(1,modulus,4))
        assert min((weight(k,width),k) for k in prefix)==(4,high+1)
        assert min(weight(k,width) for k in prefix if k!=high+1)==6
        acquisition=8*(half-1)
        for horizon in range(1,257):
            no_probe=5*horizon-horizon%2
            before_first=8*half+3*horizon-horizon%2
            candidates=[no_probe,before_first]
            for j in range(1,horizon):
                lower=(5*j-j%2)+acquisition+(3*(horizon-j)-(horizon-j)%2)
                candidates.append(lower);first_even_cases+=1
            expected=no_probe if horizon==1 else min(no_probe,acquisition+3*horizon+horizon%2)
            assert min(candidates)==expected
            horizons+=1
            if horizon in (1,2,2*slots-5,2*slots-4,2*slots-3,2*slots-2):
                rows.append(dict(slots=slots,horizon=horizon,without_expansion=no_probe,
                                 with_round2_expansion=None if horizon==1 else acquisition+3*horizon+horizon%2,
                                 minimum=expected))
    return dict(width_domain=[3,8],horizon_domain=[1,256],horizons=horizons,
                first_even_use_lower_bound_cases=first_even_cases,selected=rows)


def run() -> dict:
    return dict(status='PASS',model='FINITE_INTEGER_CONTROL_ONLY',
                formula='8r+(8b+2q+41)T-(T mod2)',
                source='strategy_proofs.md',
                weights=check_weights(),information=check_information(),
                fixed_entry=check_fixed_entry())


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('strategy_checks.json'))
    args=parser.parse_args()
    result=run()
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('weights','information','fixed_entry')}))
