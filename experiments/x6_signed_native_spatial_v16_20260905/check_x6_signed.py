#!/usr/bin/env python3
"""Exact P000-V4 signed X6 spatial regression."""
from collections import Counter
from itertools import product

from x6_signed import (
    ALL_SLICES, AXES, DIAGONAL, ORIGIN, S6, Spatial6, canonical,
    depth_carry, diagonal_step, from_hidden_slice_coordinates,
    from_residual_depth, full_distance_squared, hidden_slice_coordinates,
    joint_slice_difference_is_diagonal, joint_slice_equal,
    positive_path_multiplicity, relative_endpoint_multiplicity,
    triangle_displacement,
)


def main():
    checks=0
    probes=(
        ORIGIN,
        Spatial6((3,-1,7,0,-5,2)),
        Spatial6((-4,2,0,5,1,-3)),
        Spatial6((11,0,-4,9,2,8)),
    )

    # Signed primitive axis adjacency, reversibility and P000 full norm symmetry.
    for state in probes:
        nbr=set()
        for i in AXES:
            f=state.step(i,+1); b=state.step(i,-1)
            assert f.step(i,-1)==state and b.step(i,+1)==state
            assert full_distance_squared(state,f)==1
            assert full_distance_squared(state,b)==1
            nbr.add(f); nbr.add(b)
            checks+=4
        assert len(nbr)==12; checks+=1

    # All 720 axis permutations preserve signed norm and primitive adjacency.
    for p in S6:
        for state in probes:
            moved=state.rotate(p)
            assert moved.norm_squared_from_origin()==state.norm_squared_from_origin()
            checks+=1
        for i in AXES:
            assert ORIGIN.step(i).rotate(p)==ORIGIN.step(p[i])
            assert ORIGIN.step(i,-1).rotate(p)==ORIGIN.step(p[i],-1)
            checks+=2

    # Every selected 3-axis positive observer has a lossless full chart with
    # local min-zero triple + common visible offset + 3 omitted signed coords.
    roundtrips=0
    for state in probes:
        for S in ALL_SLICES:
            visible,common,hidden=hidden_slice_coordinates(state,S)
            assert visible==state.observe(S)
            assert from_hidden_slice_coordinates(S,visible,common,hidden)==state
            roundtrips+=1; checks+=2
            H=triangle_displacement(S)
            assert H.observe(S)==(0,0,0)
            comp=triangle_displacement(tuple(i for i in AXES if i not in S))
            assert tuple(a+b for a,b in zip(H.coords,comp.coords))==DIAGONAL
            checks+=2

    # Joint 20-slice observer equality iff full states differ by global diagonal.
    finite=[]
    for z in product(range(-1,2),repeat=6): finite.append(Spatial6(z))
    for idx,a in enumerate(finite):
        # avoid quadratic 729^2 cost: test all diagonal mates and deterministic nonmates
        for h in range(-3,4):
            b=diagonal_step(a,h)
            assert joint_slice_equal(a,b)
            assert joint_slice_difference_is_diagonal(a,b)
            checks+=2
        for j in (0,1,2,3,4,5):
            b=a.step(j)
            assert not joint_slice_equal(a,b)
            assert not joint_slice_difference_is_diagonal(a,b)
            checks+=2

    # Residual + signed common depth is exact and carry is the section cocycle.
    residuals=[]
    for z in product(range(-2,3),repeat=6):
        if sum(abs(x) for x in z)>5: continue
        state=Spatial6(z)
        r,h=state.relative_residual_depth()
        assert from_residual_depth(r,h)==state
        residuals.append(r)
        checks+=1
    residuals=list(dict.fromkeys(residuals))[:80]
    for a in residuals:
        for b in residuals:
            c=depth_carry(a,b)
            raw=tuple(x+y for x,y in zip(a,b))
            assert min(raw)==c
            assert from_residual_depth(canonical(raw),c)==Spatial6(raw)
            checks+=2

    # Full diagonal is nonzero real signed spatial displacement but invisible to all slices.
    D=Spatial6(DIAGONAL)
    assert D!=ORIGIN and D.norm_squared_from_origin()==6
    assert all(D.observe(S)==(0,0,0) for S in ALL_SLICES)
    checks+=3

    # Old relative BRC formula exactly agrees with aggregation of full endpoints at fixed length.
    dist=Counter({(0,0,0,0,0,0):1})
    for m in range(0,10):
        assert sum(dist.values())==6**m; checks+=1
        aggregated=Counter()
        for n,count in dist.items():
            assert count==positive_path_multiplicity(n)
            aggregated[canonical(n)]+=count
            checks+=1
        for r,count in aggregated.items():
            assert count==relative_endpoint_multiplicity(m,r)
            checks+=1
        if m<9:
            nxt=Counter()
            for n,count in dist.items():
                for i in AXES:
                    z=list(n); z[i]+=1
                    nxt[tuple(z)]+=count
            dist=nxt

    # No nonzero positive path returns full signed origin; balanced length-6 paths end at D.
    assert positive_path_multiplicity((0,0,0,0,0,0))==1
    assert positive_path_multiplicity(DIAGONAL)==720
    assert Spatial6(DIAGONAL)!=ORIGIN
    checks+=3

    print("PASS_X6_SIGNED_NATIVE_SPATIAL_V16")
    print("checks=",checks)
    print("full_translation_group=Z^6")
    print("primitive_signed_neighbours=12")
    print("joint_positive_slice_kernel=Z*(1,1,1,1,1,1)")
    print("relative_observer=Z^6/Z*1")
    print("full_diagonal_norm_squared=6")
    print("length6_balanced_positive_paths_to_diagonal=720")
    print("full_positive_return_nontrivial=false")


if __name__=="__main__": main()
