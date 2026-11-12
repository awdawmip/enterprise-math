#!/usr/bin/env python3
"""LP028: exact typed R063 fixed-positive chart -> signed X6 Cell adapter.

Uses unchanged current Git source modules. Covers the 60 *labelled* pair/sign
charts and removes repeated axial endpoints only when taking their union.
This checks a bounded programmatic contract; it does not edit frozen R063.
"""
from __future__ import annotations

from collections import defaultdict
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parents[1]
GON = ROOT / 'experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py'
X6_DIR = ROOT / 'experiments/x6_signed_native_spatial_v16_20260905'
PINNED_BLOBS = {
    GON: '643b2bac659a445891dcb5588b647972977104e0',
    X6_DIR / 'x6_signed.py': 'ac32f6d82a91db99297e587cf63b0df95cece514',
    X6_DIR / 'signed_brc.py': '300a96e3dc24bf6fff73743037a0347a8bc83176',
}


def git_blob_sha1(path: Path) -> str:
    content = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(content)).encode('ascii') + b'\0' + content).hexdigest()


def require_source_pins() -> None:
    for path, sha in PINNED_BLOBS.items():
        actual = git_blob_sha1(path)
        if actual != sha:
            raise AssertionError(f'SOURCE_BLOB_CHANGED {path} {actual} != {sha}')


sys.path[:0] = [str(ROOT / 'experiments'), str(X6_DIR)]
from tool_discovery_native_geometry_of_numbers_minima_calculus_20260822 import groots_square, path_fiber_size
from x6_signed import Spatial6, full_distance_squared
from signed_brc import shortest_path_multiplicity, endpoint_multiplicity, spatial_norm_squared


def embed_chart(start: Spatial6, axes: tuple[int,int], signs: tuple[int,int], root: tuple[int,int]):
    """Preserve native start, ordered selected axes and two sign labels.

    Root is a positive-sector ordered component pair, NOT an X6 endpoint.
    Return a genuinely signed native Cell and native signed displacement.
    """
    if not isinstance(start, Spatial6):
        raise TypeError('explicit native Cell start required')
    if not isinstance(axes, tuple) or len(axes) != 2 or any(type(i) is not int or i not in range(6) for i in axes) or axes[0] >= axes[1]:
        raise ValueError('distinct sorted X6 axis labels required')
    if not isinstance(signs, tuple) or len(signs) != 2 or any(type(s) is not int or s not in (-1,1) for s in signs):
        raise ValueError('two signed native directions required')
    if not isinstance(root, tuple) or len(root) != 2 or any(type(x) is not int or x < 0 for x in root):
        raise ValueError('ordered nonnegative component root required')
    target = start
    for axis, sign, count in zip(axes, signs, root):
        for _ in range(count):
            target = target.step(axis, sign)
    delta = start.displacement_to(target)
    return target, delta


def exhaustive_labelled_charts(r: int, start: Spatial6):
    roots = groots_square(r)
    multiplicities = defaultdict(set)
    counts = defaultdict(int)
    checks = 0
    for axes in combinations(range(6), 2):
        for signs in product((-1,1), repeat=2):
            for root in roots:
                end, delta = embed_chart(start, axes, signs, root)
                length = root[0] + root[1]
                mult = path_fiber_size(root)
                assert full_distance_squared(start,end) == spatial_norm_squared(delta) == r*r
                assert sum(map(abs,delta)) == length
                assert shortest_path_multiplicity(delta) == mult
                assert endpoint_multiplicity(length,delta) == mult
                multiplicities[delta].add(mult)
                counts[delta] += 1
                checks += 1
    assert all(len(ms)==1 for ms in multiplicities.values())
    weighted_union = sum(next(iter(ms)) for ms in multiplicities.values())
    labelled_mass = sum(counts[d]*next(iter(multiplicities[d])) for d in multiplicities)
    local_mass = sum(path_fiber_size(root) for root in roots)
    assert labelled_mass == 60 * local_mass
    assert labelled_mass - weighted_union == 108  # twelve axial states, multiplicity ten
    assert len(multiplicities) == 60*(len(roots)-2)+12
    axial = {d: n for d,n in counts.items() if sum(x!=0 for x in d)==1}
    assert len(axial)==12 and set(axial.values())=={10}
    assert all(n==1 for d,n in counts.items() if sum(x!=0 for x in d)==2)
    return {'r':r, 'roots':len(roots), 'labelled':checks,
            'unique':len(multiplicities), 'labelled_mass':labelled_mass,
            'union_mass':weighted_union, 'overcount':labelled_mass-weighted_union}


def direct_words_check():
    # Exact distinct words of the positive (3,4) root, one selected signed chart.
    start=Spatial6((11,-5,0,2,-3,8))
    outcomes=set()
    for positions_i in combinations(range(7),3):
        target=start
        for step in range(7):
            if step in positions_i: target=target.step(1,-1)
            else: target=target.step(4,+1)
        assert target.coords==(11,-8,0,2,1,8)
        outcomes.add(positions_i)
    assert len(outcomes)==35==comb(7,3)


def rejects_bad_input():
    start=Spatial6()
    bad=[(start,(1,1),(1,1),(3,4)), (start,(1,0),(1,1),(3,4)),
         (start,(0,6),(1,1),(3,4)), (start,(0,1),(0,1),(3,4)),
         (start,(0,1),(1,1),(-3,4)), (start,(0,1),(1,1),(True,4))]
    for args in bad:
        try: embed_chart(*args)
        except (TypeError,ValueError): pass
        else: raise AssertionError('accepted invalid signed native chart')
    try: embed_chart((0,)*6,(0,1),(1,1),(3,4))
    except TypeError: pass
    else: raise AssertionError('accepted non-Cell start')


def main():
    require_source_pins()
    rejects_bad_input()
    direct_words_check()
    origin=Spatial6()
    checked=0
    for r in range(1,129):
        cert=exhaustive_labelled_charts(r,origin)
        checked+=cert['labelled']
        if r in (1,5,50,128):
            print('CERT',cert)
    for start in [Spatial6((4,-3,0,2,2,6)), Spatial6((-10,-6,-2,-1,0,7))]:
        cert=exhaustive_labelled_charts(50,start)
        assert cert['unique']==252 and cert['union_mass']==6641732296455342852372
        checked+=cert['labelled']
    print(f'PASS_SIGNED_PATHSQRT_CURRENT_SOURCE_IMPORT radius_1_to_128=128 chart_branch_checks={checked} all_pairs_at_r50=252 union_mass_50=6641732296455342852372 axial_doublecount_correction=108 source_blobs=3')


if __name__=='__main__': main()
