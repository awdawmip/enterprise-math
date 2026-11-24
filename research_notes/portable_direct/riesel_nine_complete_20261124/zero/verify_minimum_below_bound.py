#!/usr/bin/env python3
"""Exhaust every zero-W exact-nine root below a supplied R3 index bound.

This uses the complete 47-pattern theorem in proof.md. CRT pruning is exact:
every extension of the partial residue x modulo M has nonnegative index >=x.
It is not a scan up to a prime-size cutoff and does not omit later CRT lifts.
"""
from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import json
from math import log
from pathlib import Path
import time

from verify_zero_nine import A3,S3,GROUPS,PERIOD,patterns,eight_predicate

HERE=Path(__file__).resolve().parent


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bound',type=int,default=11380571075)
    parser.add_argument('--output',type=Path,default=HERE/'zero_nine_bounded_minimum_certificate.json')
    args=parser.parse_args()
    initial=args.bound;best=initial;minimum=None;candidate_cache={};summaries=[]
    started=time.monotonic()

    @lru_cache(None)
    def options(group,b):
        result=[]
        for q in GROUPS[group]:
            phase=b%PERIOD[q]
            positive=pow(pow(2,4+6*phase,q),-1,q)
            for sign in (1,-1):
                residue=sign*positive%q
                index=(residue-A3)*pow(S3,-1,q)%q
                if index<initial:result.append((q,index,phase,sign,residue))
        return sorted(result,reverse=True)

    @lru_cache(None)
    def inverse(m,q):return pow(m,-1,q)

    for number,pattern in enumerate(patterns()):
        local=Counter();slots=[]
        for group,b in pattern['slots']:
            op=options(group,b)
            slots.append((group,b,op))
        slots.sort(key=lambda s:-(sum(log(o[0]) for o in s[2])/len(s[2]) if s[2] else float('inf')))

        def visit(depth,x,m,used,chosen):
            nonlocal best,minimum
            local['nodes']+=1
            if depth==len(slots):
                local['full_CRT_classes_below_current_bound']+=1
                j=x
                while j<best:
                    if j not in candidate_cache:candidate_cache[j]=eight_predicate(A3+S3*j)
                    local['ordinary_root_candidates']+=1
                    if not candidate_cache[j]:
                        root=A3+S3*j
                        best=j
                        minimum={'root':str(root),'digits':len(str(root)),'R3_index':str(j),
                                 'type':pattern['type'],'pattern_number':number,
                                 'tail':[{ 'prime':q,'v_phase':b,'root_sign':sign,'root_residue':res}
                                         for q,_,b,sign,res in chosen],
                                 'complete_eight_predicate':False,'supplementary_minimum':9}
                        print(json.dumps({'new_best':str(best),'type':pattern['type'],'digits':len(str(root))}),flush=True)
                    j+=m
                return
            group,b,op=slots[depth]
            for q,residue,phase,sign,root_residue in op:
                if q in used:
                    local['duplicate_prime_prunes']+=1;continue
                y=x+m*((residue-x)*inverse(m%q,q)%q)
                if y>=best:
                    local['nonnegative_CRT_prunes']+=1;continue
                visit(depth+1,y,m*q,used|{q},chosen+[(q,residue,phase,sign,root_residue)])

        visit(0,0,1,set(),[])
        summaries.append({'pattern_number':number,'type':pattern['type'],
                          'slots':pattern['slots'],'slot_option_counts':[len(s[2]) for s in slots],
                          'statistics':dict(local),'best_after_pattern':str(best)})
    result={'schema':'RIESEL_ZERO_W_NINE_BOUNDED_MINIMUM_V15','status':'PASS',
            'initial_strict_upper_bound_index':str(initial),
            'exact_nine_found_below_initial_bound':minimum is not None,
            'minimum_below_initial_bound':minimum,
            'all_47_geometries_processed':len(summaries)==47,'patterns':summaries,
            'distinct_ordinary_root_candidates':len(candidate_cache),
            'cost_eight_candidates':sum(candidate_cache.values()),
            'pruning_lemma':'Every nonnegative extension of x modulo M is x+kM>=x; unused-prime conditions are imposed by CRT, and every complete-period lift below the current bound is checked.',
            'complete_classification_source':'proof.md',
            'elapsed_seconds':time.monotonic()-started,'native_BRC_execution':False,
            'independent_project_review':False}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','patterns':len(summaries),'minimum':minimum,
                      'distinct_candidates':len(candidate_cache),'elapsed_seconds':result['elapsed_seconds'],
                      'output':str(args.output)},indent=2))


if __name__=='__main__':main()
