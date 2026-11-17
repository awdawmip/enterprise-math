#!/usr/bin/env python3
"""Independent pure-integer model audit of a pinned X6 CoverState.step source guard.

The current source file is externally read by immutable Git blob. This standalone
checker models exactly its min-zero lift/step/quotient transition and independently
checks a strict type guard. It is not an execution of the project module or the
frozen R063/Helly benchmark. No asserts with side-effects.
"""
from itertools import product
import json

N=6
MODULI=(0,1,2,3,4)

def require(p, message):
    if not p:
        raise RuntimeError(message)

def normalize(z):
    h=min(z)
    return tuple(x-h for x in z),h

def key(z,m):
    r,h=normalize(z)
    return r,h if m==0 else h%m

def source_guard(axis, direction):
    """Verbatim Boolean logic of pinned x6_cover.CoverState.step."""
    return not (type(axis) is not int or axis not in range(N) or direction not in (-1,1))

def signed_native_guard(axis,direction):
    """Verbatim Boolean logic of pinned x6_signed.Spatial6.step."""
    return not (type(axis) is not int or axis not in range(N) or type(direction) is not int or direction not in (-1,1))

def cover_step(state,axis,direction,modulus):
    require(source_guard(axis,direction),'invalid CoverState.step input')
    r,h=state
    lift=[x+h for x in r]
    lift[axis]+=direction
    low=min(lift)
    relative=tuple(x-low for x in lift)
    require(all(type(x) is int for x in relative),'source Coord6 exact integer guard rejected')
    return relative,low if modulus==0 else low%modulus

def typed_cover_step(state,axis,direction,modulus):
    require(signed_native_guard(axis,direction),'signed direction must be exact int +/-1')
    return cover_step(state,axis,direction,modulus)

def main():
    comparisons=0
    for z in product((-1,0,1), repeat=N):
        for m in MODULI:
            s=key(z,m)
            for axis in range(N):
                for sign in (-1,1):
                    raw=list(z);raw[axis]+=sign
                    expected=key(raw,m)
                    got=typed_cover_step(s,axis,sign,m)
                    require(got==expected,f'corrected transition mismatch {(z,m,axis,sign,got,expected)}')
                    comparisons+=1
    orig=key((0,)*N,0)
    require(source_guard(0,True),'original guard should accept Python True under equality')
    require(not signed_native_guard(0,True),'native signed guard should reject Python True')
    require(cover_step(orig,0,True,0)==cover_step(orig,0,1,0),'True silently aliases +1 in original guard')
    try:
        typed_cover_step(orig,0,True,0)
    except RuntimeError:
        pass
    else:
        raise RuntimeError('typed corrected adapter accepted boolean direction')
    require(not source_guard(True,1),'original guard should reject boolean axis')
    require(not source_guard(0,False),'original guard should reject false direction')
    result={'schema':'X6_UNIT93_COVER_SIGNED_STEP_TYPE_BOUNDARY_MODEL_V1',
            'task_id':'RS-X6-LEGACY-PLANE-RECONCILIATION',
            'pin_cover_blob_sha1':'171baf1cee7f1aceaf38c73d0c0659a25fd8d7bd',
            'pin_signed_blob_sha1':'405d9bc752bbf45582f2d0a6d9f91bff9cc5f89e',
            'source_guard_is_reconstructed_not_module_executed':True,
            'signed_native_integer_directions_checked':comparisons,
            'tested_raw_states':3**N,'tested_moduli':list(MODULI),
            'legacy_bool_true_aliases_positive_step':True,
            'typed_wrapper_rejects_bool_true':True,
            'native_R063_or_Helly_executed':False,
            'classification':'AUTHOR-EXACT / MODEL-EXECUTED / NATIVE-SOURCE-STATIC-READ / UNREVIEWED / NOT_ADMITTED'}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
if __name__=='__main__':main()
