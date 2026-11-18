#!/usr/bin/env python3
"""Replay the frozen 3-region codec and max-norm A3 source against exact torus counts."""
import argparse
from collections import Counter, defaultdict
from hashlib import sha1, sha256
from itertools import permutations, product
import json
from math import comb
from pathlib import Path
import runpy
import sys

FILES = {
    "scripts/check_a3_recursive_shell_alignment_tomography.py": "ff0f0a5a77d1935206b25dfaf137cdaaff12cd83",
    "src/enterprise_math/cell_address.py": "fc77f374ed8b7948dac2d5a0bfcad87ee828e97b",
    "src/enterprise_math/_cell_slice_codec.py": "2aa70d8f8509dc31d73f6891b97f9fdf7377df2a",
    "coordinate_address_contract.json": "186895a2545b9c5f31de6dc0944aef157f4b35d1",
}
LEAN = "EnterpriseMath/CellAddress/ThreeRegionSlice.lean"
LEAN_HASH = "2971ea97ba60f0a528a915c06152cb4aec9824fa85fae0bb88c0e76e4e921b02"


def residues(v,m):
    return tuple(x%m for x in v)


def box(R,d):
    for t in product(range(-R,R+1),repeat=d-1):
        last = -sum(t)
        if abs(last)<=R:
            yield t+(last,)


def by_bound(r,m,R):
    if R<0:
        return 0
    h=sum(r)//m
    lows=[-((R+a)//m) for a in r]
    hi=[(R-a)//m for a in r]
    caps=[b-a for a,b in zip(lows,hi)]
    if min(caps)<0:
        return 0
    wanted=-h-sum(lows)
    total=0
    for bits in product((0,1),repeat=len(r)):
        rem=wanted-sum(z*(1+b) for z,b in zip(bits,caps))
        if rem>=0:
            total+=(-1)**sum(bits)*comb(rem+len(r)-1,len(r)-1)
    return total


def by_band(r,m,R):
    if any(R<a<m-R for a in r):
        return 0
    forced=sum(a>R for a in r)
    free=sum(m-R<=a<=R for a in r)
    k=sum(r)//m-forced
    return comb(free,k) if 0<=k<=free else 0


def radius_mod(r,m):
    h=sum(r)//m
    if h==0:
        return 0
    s=sorted(r)
    return max(s[len(s)-h-1],m-s[len(s)-h])


def fiber_checks(src):
    report={}
    for d in (3,4):
        tested=0
        mdata={}
        for m in range(2,11):
            keys=[t+((-sum(t))%m,) for t in product(range(m),repeat=d-1)]
            truth_min={k:None for k in keys}
            for R in range(m+2):
                if d==4:
                    orig=src["ball"](R)
                else:
                    orig=(x[:3] for x in src["slice_ball"](R))
                counts=Counter(residues(x,m) for x in orig)
                closed=all(v==1 for v in counts.values())
                assert closed==(2*R<m)
                sphere=list(box(R,d))
                shell=Counter(residues(x,m) for x in sphere if max(map(abs,x))==R)
                assert (max(shell.values())==1)==(2*R<m)
                radial=defaultdict(set)
                for x in sphere:
                    radial[residues(x,m)].add(max(map(abs,x)))
                assert all(len(s)==1 for s in radial.values())==(R<=m//2)
                for r in keys:
                    f=by_bound(r,m,R)
                    assert f==counts[r] and f-by_bound(r,m,R-1)==shell[r]
                    if R<m:
                        assert by_band(r,m,R)==f
                    if f and truth_min[r] is None:
                        truth_min[r]=R
                    tested+=1
            assert all(radius_mod(r,m)==z for r,z in truth_min.items())
            diam=max(truth_min.values())
            assert diam==(d-1)*m//d
            mdata[str(m)]={"classes":len(keys),"diameter":diam,
                           "farthest_classes":sum(v==diam for v in truth_min.values())}
        report[str(d)]={"ball_fibers_checked":tested,"moduli":mdata}
    return report


def codec_checks(api):
    out={}
    for m in range(2,13):
        seen=defaultdict(set)
        am=range(-2*m-1,2*m+2)
        for x,y in product(am,repeat=2):
            addr=api.encode_raw_slice((x,y))
            assert api.decode_raw_slice(addr)==(x,y)
            key=residues(addr.coordinates[:3],m)
            seen[key].add((x%m,y%m))
        hist=Counter(map(len,seen.values()))
        assert hist=={1:3*(m-1)**2,2:3*(m-1),3:1}
        for (a,b,c),got in seen.items():
            candidates=set()
            if a==0:
                candidates.add(residues((1-c,b-c),m))
            if b==0:
                candidates.add(residues((1+a-c,1-c),m))
            if c==0:
                candidates.add(residues((a,b),m))
            assert candidates==got
        x,y=api.encode_raw_slice((1,1)),api.encode_raw_slice((m+1,1))
        na,nb=api.step_cell(x,"E1_REVERSE"),api.step_cell(y,"E1_REVERSE")
        assert residues(x.coordinates,m)==residues(y.coordinates,m)
        assert residues(na.coordinates,m)!=residues(nb.coordinates,m)
        out[str(m)]={"decoded_candidates_1_2_3":[hist[i] for i in (1,2,3)],
                     "after_E1minus":[residues(na.coordinates,m)[:3],residues(nb.coordinates,m)[:3]]}
    return out


def pointers(src):
    histogram=Counter()
    for m in range(2,25):
        for R in range(1,2*m+1):
            x=src["anchor"](R)
            ro=residues(x,m)
            size=sum(residues(src["r_act"](p,x),m)==ro for p in permutations(range(4)))
            assert size==(24 if R%m==0 else 4 if 2*R%m==0 else 2)
            histogram[size]+=1
    return dict(sorted(histogram.items()))


def farthest_counts():
    out={}
    for m in range(2,41):
        D=3*m//4
        total=0
        for a,b,c in product(range(m),repeat=3):
            total+=radius_mod((a,b,c,(-a-b-c)%m),m)==D
        if m>=10:
            delta=4*((m+3)//4)-m
            assert total==2*comb(delta+3,3)
        else:
            assert total==[7,8,2,40,20,8,2,40][m-2]
        out[str(m)]=total
    return out


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--json",type=Path)
    args=p.parse_args()
    for name,expected in FILES.items():
        data=(args.repo/name).read_bytes()
        assert sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()==expected
    assert sha256((args.repo/LEAN).read_bytes()).hexdigest()==LEAN_HASH
    sys.path.insert(0,str(args.repo/"src"))
    from enterprise_math import cell_address as api
    src=runpy.run_path(str(args.repo/next(iter(FILES))))
    res={"frozen_blobs":FILES,"lean_sha256":LEAN_HASH,"codec":codec_checks(api),
         "shell":fiber_checks(src),"pointer_stabilizer_sizes":pointers(src),
         "rank_three_farthest_classes":farthest_counts()}
    out=json.dumps(res,indent=2)+"\n"
    if args.json:
        args.json.write_text(out)
    else:
        print(out,end="")


if __name__=="__main__":
    main()
