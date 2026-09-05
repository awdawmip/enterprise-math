#!/usr/bin/env python3
"""Exact regression for the X6 six-coordinate completion research candidate.

This checker intentionally reuses the already-main-backed six-axis derived V2
`local_charts` / `reconstruct` implementation as a cross-check rather than
reimplementing that layer.
"""
from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(HERE))
sys.path.insert(0,str(ROOT/"experiments"/"six_axis_foundation_v2_20260905"))

from x6_coordinate import (
    ALL_SLICES, AXES, Coord6, ORIGIN_COORD, axis_step, brc_endpoint_multiplicity,
    complement_slice, from_hidden_chart, hidden_chart, k4_s4_axis_permutations,
    k4_slice_type, local_step, positive_return_count, slice_holonomy,
)
import six_axis as old_v2


def main():
    checks=0

    # Canonical-section / old V2 atlas compatibility over all [0,3]^6 raw lifts.
    for raw in product(range(4), repeat=6):
        state=Coord6.from_integer_lift(raw)
        charts=old_v2.local_charts(raw)
        assert charts==old_v2.local_charts(state.values)
        assert old_v2.reconstruct(dict(enumerate(charts)))==state.values
        checks+=3

    # Translation, immediate reversal, global commutativity and all-six loop.
    probes=(
        ORIGIN_COORD,
        Coord6((3,1,7,0,5,2)),
        Coord6((0,2,0,5,1,3)),
        Coord6((11,0,4,9,2,8)),
    )
    for state in probes:
        directed=set()
        for i in AXES:
            f=state.step(i,+1); b=state.step(i,-1)
            assert f.step(i,-1)==state
            assert b.step(i,+1)==state
            directed.add(f); directed.add(b)
            checks+=4
        assert len(directed)==12
        checks+=1
        for i in AXES:
            for j in AXES:
                assert state.step(i).step(j)==state.step(j).step(i)
                checks+=1
        loop=state
        for i in AXES:
            loop=loop.step(i)
        assert loop==state
        checks+=1

    # All 20 slice observations: visible equivariance, omitted invisibility,
    # lossless visible+hidden chart, and triangle hidden holonomy.
    chart_roundtrips=0
    for state in probes:
        for S in ALL_SLICES:
            visible=state.observe(S)
            v,h=hidden_chart(state,S)
            assert v==visible
            assert from_hidden_chart(S,v,h)==state
            chart_roundtrips+=1
            checks+=2
            for i in AXES:
                observed=state.step(i).observe(S)
                if i in S:
                    assert observed==local_step(visible,S.index(i),+1)
                else:
                    assert observed==visible
                checks+=1
            hol=slice_holonomy(S)
            assert hol.observe(S)==(0,0,0)
            comp=slice_holonomy(complement_slice(S))
            assert hol.inverse_displacement()==comp
            assert hol.grade_c6==3 and comp.grade_c6==3
            checks+=4

    # Reversal projection recovers the old 3-axis (0,1,1)-type reverse decode.
    for i in AXES:
        reverse=axis_step(i,-1)
        assert reverse.norm_squared()==5
        for S in ALL_SLICES:
            if i in S:
                local=reverse.observe(S)
                assert sorted(local)==[0,1,1]
                checks+=1

    # Exact S6 axis permutation implementation: all 720 preserve norm/grade and
    # move each axis step to the correspondingly permuted axis.
    from x6_coordinate import S6
    for p in S6:
        for state in probes:
            moved=state.rotate(p)
            assert moved.norm_squared()==state.norm_squared()
            assert moved.grade_c6==state.grade_c6
            checks+=2
        for i in AXES:
            assert axis_step(i).rotate(p)==axis_step(p[i])
            checks+=1

    # Existing carrier S4 subgroup has 24 elements and gives 4/4/12 orbits/types
    # on the 20 native three-axis selections.
    s4=k4_s4_axis_permutations()
    assert len(s4)==24
    type_counts=Counter(k4_slice_type(S) for S in ALL_SLICES)
    assert type_counts==Counter({"PATH":12,"STAR":4,"FACE":4})
    checks+=2
    for p in s4:
        for S in ALL_SLICES:
            moved=tuple(sorted(p[i] for i in S))
            assert k4_slice_type(moved)==k4_slice_type(S)
            checks+=1

    # BRC kernel: independent dynamic endpoint recurrence against closed form.
    dist={ORIGIN_COORD:1}
    brc_checks=0
    for length in range(0,13):
        assert sum(dist.values())==6**length
        for endpoint,count in dist.items():
            assert count==brc_endpoint_multiplicity(length,endpoint)
            brc_checks+=1
        # Closed formula must be zero for bounded candidate addresses outside support.
        for raw in product(range(0,min(length,2)+1),repeat=6):
            endpoint=Coord6.from_integer_lift(raw)
            formula=brc_endpoint_multiplicity(length,endpoint)
            assert formula==dist.get(endpoint,0)
            brc_checks+=1
        if length<12:
            nxt=Counter()
            for endpoint,count in dist.items():
                for i in AXES:
                    nxt[endpoint.step(i)]+=count
            dist=dict(nxt)
    checks+=brc_checks

    assert positive_return_count(0)==1
    assert positive_return_count(1)==0
    assert positive_return_count(3)==0
    assert positive_return_count(6)==720
    assert positive_return_count(12)==7484400
    checks+=5

    print("PASS_X6_NATIVE_COORDINATE_COMPLETION_V7")
    print("checks=",checks)
    print("v2_raw_lifts_cross_checked=4096")
    print("native_three_axis_selections=20")
    print("hidden_kernel_per_slice=Z^3")
    print("chart_roundtrips=",chart_roundtrips)
    print("axis_permutation_skeleton=S6 (720 elements)")
    print("fcc_preserving_subgroup=S4 (24 elements); slice types 4+4+12")
    print("full_reverse_axis_norm_squared=5; local_projection_reverse_norm_squared=2")
    print("return_6=720; return_12=7484400")


if __name__=="__main__":
    main()
