#!/usr/bin/env python3
"""Unit91 exact finite gauge-atlas minimality: all 20 named signed X6 triads.

A chart is a GLOBAL diagonal sign gauge D_s preserving six named axes.
One chart covers triad i<j<k iff s_i=s_k=-s_j, by Unit90.
Checks do not execute R063/Helly native benchmarks or admit physics.
"""
from itertools import combinations, product
from collections import Counter
import json

TRIADS = tuple(combinations(range(6),3))
FULL = (1 << len(TRIADS)) - 1
STAR = ((0,2,5), (0,3,4), (1,2,4), (1,3,5))
STAR_GAUGE = (-1,-1,1,1,-1,-1)
ATLAS = (
    (-1,-1,-1,-1,1,-1),
    (-1,-1,1,-1,1,1),
    (-1,-1,1,1,-1,-1),
    (-1,1,-1,-1,-1,-1),
)

def mask(s):
    return sum(1 << i for i,(a,b,c) in enumerate(TRIADS)
               if s[a] == s[c] == -s[b])

def compatible(s, t):
    a,b,c=t
    return s[a]==s[c]==-s[b]

def main():
    signs = tuple(product((-1,1),repeat=6))
    mask_reps = {}
    for s in signs:
        x=mask(s)
        if x:
            mask_reps.setdefault(x,s)
    masks = tuple(sorted(mask_reps))
    assert len(signs)==64
    assert len(TRIADS)==20
    assert len(masks)==26
    size_hist=Counter(x.bit_count() for x in masks)
    assert dict(size_hist)=={4:6,6:12,8:8}
    assert max(size_hist)==8
    assert all((a|b|c)!=FULL for a,b,c in combinations(masks,3))
    four_covers=[p for p in combinations(masks,4)
                 if (p[0]|p[1]|p[2]|p[3])==FULL]
    assert len(four_covers)==165
    star_mask=mask(STAR_GAUGE)
    assert star_mask.bit_count()==8
    assert all(compatible(STAR_GAUGE,t) for t in STAR)
    assert sum(star_mask in p for p in four_covers)==42

    atlas_masks=tuple(map(mask,ATLAS))
    assert [x.bit_count() for x in atlas_masks]==[4,4,8,4]
    assert (atlas_masks[0]|atlas_masks[1]|atlas_masks[2]|atlas_masks[3])==FULL
    assert sum(x.bit_count() for x in atlas_masks)==20
    assert all((x&y)==0 for x,y in combinations(atlas_masks,2))
    assert ATLAS[2]==STAR_GAUGE
    assigned=[
      {"gauge_signs":list(s),
       "triple_count":mask(s).bit_count(),
       "triples":[list(t) for t in TRIADS if compatible(s,t)]}
      for s in ATLAS
    ]
    # The gauge transition between consecutive local charts is a
    # named diagonal-sign operator, not an extra native spatial axis.
    for a,b in combinations(ATLAS,2):
        transition=tuple(a[i]*b[i] for i in range(6))
        assert all(x in (-1,1) for x in transition)

    result={
      "schema":"X6_UNIT91_FOUR_SIGN_GAUGE_ATLAS_V1",
      "date":"2026-11-17",
      "status":"AUTHOR_FINITE_EXACT_EXECUTED_UNREVIEWED_NOT_ADMITTED",
      "six_axis_sign_gauges":64,
      "named_triads":20,
      "nonempty_distinct_gauge_compatibility_masks":len(masks),
      "mask_size_histogram":{str(k):v for k,v in sorted(size_hist.items())},
      "three_chart_combinations_checked":len(tuple(combinations(masks,3))),
      "three_chart_cover_count":0,
      "four_chart_combinations_checked":len(tuple(combinations(masks,4))),
      "four_chart_cover_count":len(four_covers),
      "minimum_charts":4,
      "four_chart_covers_including_fcc_star_gauge":42,
      "explicit_disjoint_atlas":assigned,
      "atlas_pairwise_intersections_zero":True,
      "physical_time_or_primitive_balance_admission":False,
      "native_R063_Helly_benchmarks_executed":False
    }
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,separators=(",",":")))

if __name__ == "__main__":
    main()
