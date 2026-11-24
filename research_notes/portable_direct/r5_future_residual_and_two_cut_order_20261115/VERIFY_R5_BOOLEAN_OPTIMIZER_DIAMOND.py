#!/usr/bin/env python3
"""Exact Boolean diamond of complete optimizer languages under cuts 8 and 9.
Uses the frozen 954-event generator and optimizer DP in adjacent solver module.
All counts are unbounded Python integers, no floating point.
"""
import json
from VERIFY_R5_JOINT_CLOSURE_OFFLINE import frozen, close, optimizer, language, E


def count_lang(lang):
    levels, edges, _ = lang
    states = {i: 1 for i in levels[0]}
    for row in edges:
        nxt = {}
        for i, cnt in states.items():
            for q in row[i]:
                nxt[q] = nxt.get(q, 0) + cnt
        states = nxt
    return sum(states.values())


def intersect_lang(a,b):
    al, ae, cost_a = a
    bl, be, cost_b = b
    assert cost_a == cost_b
    levels = [x & y for x,y in zip(al, bl)]
    edges = [{i: tuple(sorted(set(ae[r][i]) & set(be[r][i])))
              for i in levels[r]} for r in range(len(ae))]
    return levels, edges, cost_a


def subset_lang(a,b):
    al,ae,ac=a;bl,be,bc=b
    return (ac==bc and all(x<=y for x,y in zip(al,bl)) and
            all(set(ae[r][i]) <= set(be[r][i])
                for r in range(len(ae)) for i in al[r]))


def run():
    x,cuts=frozen()
    dp = {}
    for mask in range(32):
        closures=sum(1 << e for j,e in enumerate(E) if (mask>>j)&1)
        dp[mask] = optimizer(close(x,cuts,closures))
    rows=[]; checks=0
    for K in range(214,222):
        L={mask: language(dp[mask],K) for mask in range(32)}
        for b in range(32):
            if b & 6: continue
            B, X, Y, Z = L[b], L[b|2], L[b|4], L[b|6]
            assert subset_lang(B,X) and subset_lang(B,Y)
            assert subset_lang(X,Z) and subset_lang(Y,Z)
            n0,n8,n9,n89=map(count_lang,(B,X,Y,Z))
            inter=count_lang(intersect_lang(X,Y))
            assert n0==inter, (K,b,n0,inter)
            assert n89==n8+n9-inter,(K,b,n89,n8+n9-inter)
            rows.append(dict(K=K,old_effective_mask=b,base_count=str(n0),
                             cut8_count=str(n8),cut9_count=str(n9),
                             joint_count=str(n89),intersection_count=str(inter)))
            checks+=1
    assert checks==64
    result={'status':'PASS_R5_BOOLEAN_OPTIMIZER_DIAMOND',
            'frozen_science_commit':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
            'model':'954-event derived indexed-center 1D radius-2',
            'cases':checks,'every_case_intersection_equals_base':True,
            'every_case_joint_equals_union':True,
            'all_counts_exact_arbitrary_precision_integers':True,
            'results':rows,
            'review':'AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED'}
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':run()
