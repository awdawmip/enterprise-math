#!/usr/bin/env python3
"""Executable LP026 actual-source consumer integration certificate.

Imports the unchanged, SHA-pinned canonical Source modules CoverState, Coord6,
Signed-BRC and the previously published logarithmic-depth recovery algorithm.
All tests use exact integers. This is author-side evidence, not native Result.
"""
from __future__ import annotations

from collections import defaultdict
from hashlib import sha1
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
COORD = ROOT / 'experiments' / 'x6_native_coordinate_completion_v7_20260905'
SIGNED = ROOT / 'experiments' / 'x6_signed_native_spatial_v16_20260905'
CHECKS = ROOT / 'research_checks'
PINS = {
    COORD / 'x6_coordinate.py': 'dd6dd7e74b83be09bb7545ee92357eda445c6ca3',
    COORD / 'x6_cover.py': '171baf1cee7f1aceaf38c73d0c0659a25fd8d7bd',
    SIGNED / 'signed_brc.py': '300a96e3dc24bf6fff73743037a0347a8bc83176',
    CHECKS / 'X6_LP026_CYCLIC_G_FAST_INTERVAL_RECOVERY_20261112_ONHOUR.py':
       '496764aa8ebdb19bb03b7d40b82128a82be0ed84',
}

for file, pin in PINS.items():
    raw = file.read_bytes()
    actual = sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    assert actual == pin, (str(file),actual,pin)
sys.path[:0] = [str(COORD), str(SIGNED), str(CHECKS)]
from x6_coordinate import Coord6, canonical  # noqa: E402
from x6_cover import CoverState  # noqa: E402
from signed_brc import endpoint_multiplicity, spatial_norm_squared  # noqa: E402
from X6_LP026_CYCLIC_G_FAST_INTERVAL_RECOVERY_20261112_ONHOUR import (  # noqa: E402
    recover_native_norm_fast, NoReachableNativeLift, AmbiguousNativeNorm,
)

D=6
ZERO=(0,)*D
STEPS=tuple((i,d) for i in range(D) for d in (-1,+1))

def key(z,m):
    h=min(z)
    return tuple(v-h for v in z),h if m==0 else h%m

def source_key_step(k,axis,d,m):
    r,h=k
    s=CoverState(Coord6(r),h,m).step(axis,d)
    return s.coordinate.values,s.depth

def expected_key_step(k,axis,d,m):
    r,h=k
    z=[x+h for x in r]
    z[axis]+=d
    return key(z,m)

def native_next(native):
    result=defaultdict(int)
    for z,v in native.items():
        for axis,d in STEPS:
            zz=list(z);zz[axis]+=d
            result[tuple(zz)]+=v
    return dict(result)

def projected(native,m):
    result=defaultdict(int)
    for z,count in native.items():
        result[key(z,m)] += count
    return dict(result)

def main(max_n=6):
    native={ZERO:1}
    cover={m:{key(ZERO,m):1} for m in range(6)}
    state_checks=0
    transition_checks=0
    native_brc_checks=0
    fast_g_checks=0
    g_ambiguous=0
    old_section_distinctions=0
    for n in range(max_n+1):
        assert sum(native.values())==12**n
        for z,v in native.items():
            assert endpoint_multiplicity(n,z)==v,(n,z,v)
            native_brc_checks+=1
        for m in range(6):
            groups=defaultdict(set)
            for z in native:
                groups[key(z,m)].add(spatial_norm_squared(z))
            actual=cover[m]
            assert actual==projected(native,m),(n,m)
            assert sum(actual.values())==12**n,(n,m)
            for k,v in actual.items():
                assert v>0
                r,h=k
                assert canonical(r)==r
                s=CoverState(Coord6(r),h,m)
                assert (s.coordinate.values,s.depth)==k
                try:
                    g=recover_native_norm_fast(r,h,m,n)
                except AmbiguousNativeNorm:
                    assert len(groups[k])>1,(n,m,k,groups[k])
                    g_ambiguous+=1
                except NoReachableNativeLift as e:
                    raise AssertionError(('reachable key rejected',n,m,k)) from e
                else:
                    assert groups[k]=={g},(n,m,k,groups[k],g)
                fast_g_checks+=1
                # The section observer can differ from the native norm, even
                # where the native norm is individually recoverable.
                if len(groups[k])==1 and s.coordinate.norm_squared()!=next(iter(groups[k])):
                    old_section_distinctions+=1
                state_checks+=1
                if n<max_n:
                    for axis,d in STEPS:
                        k2=source_key_step(k,axis,d,m)
                        assert k2==expected_key_step(k,axis,d,m),(n,m,k,axis,d,k2)
                        transition_checks+=1
        if n<max_n:
            native=native_next(native)
            for m,states in tuple(cover.items()):
                nxt=defaultdict(int)
                for k,count in states.items():
                    for axis,d in STEPS:
                        nxt[source_key_step(k,axis,d,m)] += count
                cover[m]=dict(nxt)
    # Exact witnesses of the observer distinction.
    reverse=(-1,0,0,0,0,0)
    section=CoverState(Coord6(canonical(reverse)),-1,1)
    assert section.coordinate.norm_squared()==5
    assert spatial_norm_squared(reverse)==1
    assert recover_native_norm_fast(section.coordinate.values,section.depth,1,1)==1
    # Two lifts of the same m=3, exact length N=9 class carry the same norm
    # but distinct signed-BRC multiplicities.
    a=(-3,-3,0,-1,-1,-1)
    b=(0,0,3,2,2,2)
    assert key(a,3)==key(b,3)
    assert spatial_norm_squared(a)==spatial_norm_squared(b)==21
    assert (endpoint_multiplicity(9,a),endpoint_multiplicity(9,b))==(10080,7560)
    assert recover_native_norm_fast(*key(a,3),3,9)==21
    print('PASS_X6_LP026_CURRENT_COVER_FAST_G_NATIVE_BRC_IMPORT')
    print('pinned_git_blobs', {str(p.relative_to(ROOT)):v for p,v in PINS.items()})
    print('n0_to_n6_native_brc_checks',native_brc_checks)
    print('n0_to_n6_cover_state_checks',state_checks)
    print('n0_to_n5_source_step_transition_checks',transition_checks)
    print('n0_to_n6_fast_native_norm_import_checks',fast_g_checks,'ambiguous',g_ambiguous)
    print('section_norm_not_native_when_unambiguous_cases',old_section_distinctions)
    print('reverse_axis_section_and_native_norm',5,1)
    print('n9_equal_native_norm_distinct_BRC',21,10080,7560)

if __name__=='__main__':
    main()
