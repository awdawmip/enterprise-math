#!/usr/bin/env python3
"""Exact finite check of nested weighted isotonic pools under increasing drift."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import json
from certify_isotonic_deficit import exact_pav,mass


def maximal_pools(values,left):
    pools=exact_pav(values,left)
    merged=[]
    for u,v,s in pools:
        if merged and merged[-1][2]/mass(merged[-1][0],merged[-1][1])==s/mass(u,v):
            merged[-1][1]=v
            merged[-1][2]+=s
        else:
            merged.append([u,v,s])
    return merged


def width_at(pools,x):
    return next((v-u for u,v,_ in pools if u<x<v),0)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('pool_refinement_certificate.json'))
    args=parser.parse_args()
    drifts=(F(0),F(1,4),F(1,2),F(1))
    sequences=transitions=pivot_transitions=0
    strict_width_decreases=0
    for h in range(2,7):
        L,R=2,2+h
        for values in product((-2,0,3),repeat=h):
            old=None
            for drift in drifts:
                new=maximal_pools([F(value)+drift*n for n,value in enumerate(values,L)],L)
                if old is not None:
                    old_boundaries={v for _,v,_ in old[:-1]}
                    new_boundaries={v for _,v,_ in new[:-1]}
                    assert old_boundaries<=new_boundaries
                    for x in range(L+1,R):
                        before,after=width_at(old,x),width_at(new,x)
                        assert after<=before
                        strict_width_decreases+=after<before
                        pivot_transitions+=1
                    transitions+=1
                old=new
            sequences+=1
    result={'schema':'RH_ISOTONIC_DRIFT_REFINEMENT_V1','status':'PASS',
            'arithmetic':'Exact fractions; no floating-point decisions',
            'input_domain':'L=2; h=2,...,6; all A in {-2,0,3}^h',
            'drifts_exact':[str(x) for x in drifts],
            'sequences':sequences,'partition_transitions':transitions,
            'fixed_split_transitions':pivot_transitions,
            'strict_crossing_width_decreases':strict_width_decreases,
            'scope':'Finite implementation verification; general refinement theorem is proved in ISOTONIC_LOCALIZATION.md §6.1.'}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':main()
