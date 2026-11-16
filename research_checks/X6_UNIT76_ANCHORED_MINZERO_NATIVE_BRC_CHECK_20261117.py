#!/usr/bin/env python3
"""X6 Unit76: execute the current pinned diagonal_quotient.py against an anchored
two-axis native subspace. Pass --source to the exact Git blob content for local use.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path

EXPECTED_BLOB = "a527e347e33d0a0039258a9b25f48b1f1466d149"

def load_original(path: Path):
    source = path.read_bytes()
    digest = hashlib.sha1(b"blob " + str(len(source)).encode() + b"\0" + source).hexdigest()
    if digest != EXPECTED_BLOB:
        raise ValueError(f"input original source blob mismatch: {digest}")
    spec = importlib.util.spec_from_file_location("unit76_pinned_diagonal_quotient", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def embed(j, a, b, c=0):
    rest = [i for i in range(3) if i != j]
    z = [0] * 3
    z[j] = c
    z[rest[0]] = a
    z[rest[1]] = b
    return tuple(z)

def reconstruct(r, j, c=0):
    return tuple(value + c - r[j] for value in r)

def native_brc(z):
    counts = [abs(v) for v in z]
    return math.factorial(sum(counts)) // math.prod(math.factorial(a) for a in counts)

def exact_check(mod, n=12, pair_n=4, anchor_n=3):
    total_single=total_pair=total_shift=0
    first_nonfaithful=None
    anchored_cases=0
    for j in range(3):
        for a in range(-n, n+1):
            for b in range(-n, n+1):
                z=embed(j,a,b)
                r=mod.canonical_min_zero(z)
                if not mod.is_canonical_min_zero(r):
                    raise AssertionError(("not canonical",j,z,r))
                if reconstruct(r,j)!=z:
                    raise AssertionError(("not invertible on anchor",j,z,r))
                if mod.diagonal_chart(r)!=mod.diagonal_chart(z):
                    raise AssertionError(("quotient chart not preserved",j,z,r))
                rr=mod.inverse_canonical(r)
                if reconstruct(rr,j)!=tuple(-v for v in z):
                    raise AssertionError(("inverse does not commute",j,z,rr))
                if native_brc(z)!=native_brc(tuple(-v for v in z)):
                    raise AssertionError(("native reversal BRC",j,z))
                total_single+=1
                for c in range(-anchor_n,anchor_n+1):
                    zz=embed(j,a,b,c=c)
                    if reconstruct(mod.canonical_min_zero(zz),j,c)!=zz:
                        raise AssertionError(("affine anchored reconstruction",j,c,zz))
                    anchored_cases+=1
                if j==2 and a>=0 and b>=0:
                    M=max(a,b,0)
                    if rr!=(M-a,M-b,M):
                        raise AssertionError(("historical R061 reverse quotient",j,a,b,rr))
                    if first_nonfaithful is None and native_brc(tuple(-v for v in z))!=native_brc(rr):
                        first_nonfaithful={"a":a,"b":b,"native":native_brc(z),"relative":native_brc(rr)}
        for a in range(-pair_n,pair_n+1):
            for b in range(-pair_n,pair_n+1):
                z=embed(j,a,b)
                r=mod.canonical_min_zero(z)
                for x in range(-pair_n,pair_n+1):
                    for y in range(-pair_n,pair_n+1):
                        w=embed(j,x,y)
                        s=mod.canonical_min_zero(w)
                        q=mod.compose_canonical(r,s)
                        expected=tuple(z[i]+w[i] for i in range(3))
                        if reconstruct(q,j)!=expected:
                            raise AssertionError(("compose does not commute",j,z,w,q))
                        total_pair+=1
    z=(3,4,0)
    r=mod.inverse_canonical(mod.canonical_min_zero(z))
    if r!=(1,0,4) or reconstruct(r,2)!=(-3,-4,0):
        raise AssertionError("R061 3-4-5 native inverse lift")
    if native_brc(z)!=35 or native_brc(reconstruct(r,2))!=35 or native_brc(r)!=5:
        raise AssertionError("R061 35-vs-5 counterexample")
    # Without the fixed native coordinate, can3 has infinite integer fibers.
    if mod.canonical_min_zero((3,4,0))!=mod.canonical_min_zero((4,5,1)):
        raise AssertionError("global loss witness")
    # A +e_j action breaks the chosen fixed-coordinate subspace.
    if embed(2,3,4)[2]+1==0:
        raise AssertionError("wrong exit witness")
    return {
        "schema":"EM_X6_UNIT76_ANCHORED_MINZERO_EXACT_CHECK_V1",
        "current_source_path":"src/enterprise_math/diagonal_quotient.py",
        "current_source_git_blob_sha1":EXPECTED_BLOB,
        "domain":"selected signed two-axis native subspace of the signed 3-axis slice within P000 V5 X6; omitted selected-axis coordinate pinned",
        "single_signed_state_checks":total_single,
        "affine_pinned_coordinate_checks":anchored_cases,
        "native_composition_checks":total_pair,
        "native_inverse_checks":total_single,
        "native_reversal_count_checks":total_single,
        "all_assertions":"PASS",
        "R061_reverse_witness":{
            "raw":z,"relative_reverse_minzero":r,
            "recovered_native_reverse":reconstruct(r,2),
            "native_G":25,"relative_reverse_G":17,
            "native_BRC_both_directions":35,"relative_positive_word_count":5
        },
        "unanchored_global_noninjective_pair":[[3,4,0],[4,5,1]],
        "first_positive_sector_relative_mass_mismatch":first_nonfaithful,
        "R061_source_line":"definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md historical 235-246 at fd2bcff10ca6e147348b6c1236027fc0d2877df3",
        "scientific_status":"AUTHOR_EXACT_FINITE_EXECUTED_UNREVIEWED_NOT_ADMITTED"
    }

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--source",type=Path,default=Path("src/enterprise_math/diagonal_quotient.py"))
    args=parser.parse_args()
    result=exact_check(load_original(args.source))
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,separators=(",",":")))

if __name__=="__main__":
    main()
