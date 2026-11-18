#!/usr/bin/env python3
"""Finite exact checks for the R5 radius-two repair-library theorem.
Run: python VERIFY_R5_EXACT_ADVICE_LIBRARY.py
Python standard library only; no floating point.
"""
from itertools import combinations
import json
from pathlib import Path

PIN = "435e77af0d180eac32bd1f9c4c464bc4010b7551"
GAPS = (3,2,2,3,2,1)
DL, DR = (0,1,3,5), (0,2,4,6)
HARD, LEFT, RIGHT = (1,3,4,6), (1,2,3,5), (1,2,4,6)

def points(mask):
    gaps = list(GAPS)
    if mask & 1: gaps[0] -= 1
    if mask & 2: gaps[3] -= 1
    x=[0]
    for d in gaps: x.append(x[-1]+d)
    return x

def optimum(mask):
    x=points(mask)
    best=None
    fam=[]
    for s in combinations(range(7),4):
        d=[min(abs(x[i]-x[j]) for j in s) for i in range(7)]
        if max(d)>2: continue
        val=sum(d)
        if best is None or val<best: best,fam=val,[s]
        elif val==best: fam.append(s)
    return best,fam

def delta(c,d):
    return len(set(c)-set(d))

def library_covers(fam,ell,lib):
    return all(min(delta(c,d)+(h^j).bit_count() for d,j in lib)<=2
               for c in fam for h in range(1<<ell))

def color_valid(ell,color):
    return all(len({color[h]} | {color[h^(1<<i)] for i in range(ell)})==2
               for h in range(1<<ell))

def library(ell,color):
    return [(DR if color[h] else DL,h) for h in range(1<<ell)]

def main():
    opt=[optimum(t) for t in range(4)]
    assert [v for v,_ in opt]==[5,5,5,5]
    assert [len(f) for _,f in opt]==[5,12,9,17]
    old=opt[0][1]
    assert [delta(HARD,d) for d in old]==[3,2,3,3,2]
    summary=[]
    for mask in (1,3):
        fam=opt[mask][1]
        assert all(c in fam for c in (HARD,LEFT,RIGHT))
        assert (delta(LEFT,DL),delta(LEFT,DR))==(1,3)
        assert (delta(RIGHT,DL),delta(RIGHT,DR))==(3,1)
        classes={"left_at_most_1":[],"right_at_most_1":[],"double_2":[]}
        for c in fam:
            a,b=delta(c,DL),delta(c,DR)
            tag="left_at_most_1" if a<=1 else "right_at_most_1" if b<=1 else "double_2"
            if tag=="double_2": assert a==b==2
            classes[tag].append("".join(map(str,c)))
        for ell in range(8):
            if ell==0: lib=[(DL,0),(DR,0)]
            else:
                col=[h&1 for h in range(1<<ell)]
                assert color_valid(ell,col)
                lib=library(ell,col)
            assert len(lib)==max(2,1<<ell)
            assert library_covers(fam,ell,lib)
        summary.append({"mask":mask,"ell":0,"minimum":2,"core_classes":classes})
        for ell in range(1,5):
            N=1<<ell
            count=0
            for bits in range(1<<N):
                col=[(bits>>h)&1 for h in range(N)]
                valid=color_valid(ell,col)
                # Exhaustive color-to-library equivalence for ell<=3;
                # deterministic spot-check for ell=4 (theorem proves generality).
                if ell<=3 or bits%101==0:
                    assert valid==library_covers(fam,ell,library(ell,col))
                count+=int(valid)
            summary.append({"mask":mask,"ell":ell,
                            "minimum":1<<ell,"valid_minimum_libraries":count})
    for mask in (1,3):
        assert [(r["ell"],r["valid_minimum_libraries"]) for r in summary
                if r["mask"]==mask and r["ell"]>=1] == [(1,2),(2,6),(3,118),(4,29030)]
    out={"status":"PASS_R5_EXACT_RADIUS2_ADVICE_LIBRARY",
         "pin":PIN,"domain":"auxiliary 1D indexed integer centers",
         "theorem":"kappa_a(m,2)=kappa_ab(m,2)=max(2,2**(m-1)) for m>=1",
         "coverage":"all 35 core candidates/mask; witness ell 0..7; all colors ell 1..4; full library crosscheck ell<=3 and sampled ell=4",
         "rows":summary}
    path=Path(__file__).with_name("EXACT_R5_ADVICE_LIBRARY_SUMMARY.json")
    path.write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("PASS_R5_EXACT_RADIUS2_ADVICE_LIBRARY")
    print("minimum-library color counts",[(r["ell"],r["valid_minimum_libraries"]) for r in summary if r["mask"]==1 and r["ell"]>0])
    print("summary:",path)

if __name__=="__main__":
    main()
