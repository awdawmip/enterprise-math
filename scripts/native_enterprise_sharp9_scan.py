#!/usr/bin/env python3
"""Exhaustive sharp-nine scan on the two exact mod-30 extremal channels.

Default scan: central shell r<=350000.
For this range all tested values are <2^64, so the deterministic Miller-Rabin
base set used here is exact.
"""

from __future__ import annotations

import argparse
import csv

FILTER_PRIMES=(7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97)


def is_prime64(n: int) -> bool:
    if n<2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%p==0: return n==p
    d=n-1; s=0
    while d%2==0:
        s+=1; d//=2
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a%n==0: continue
        x=pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1: break
        else:
            return False
    return True


def C(r: int, h: int) -> int:
    if r%2==0:
        return h+3*r*r//2+1
    return h+3*(r*r+1)//2


def valid_h_bounds(central_r: int):
    # Nine-run begins at central_r-4; this smallest typed shell gives the tight bounds.
    s=central_r-4
    lo=-((s+1)//2)
    hi=s//2-1
    return lo,hi


def channel_residue(r: int):
    # Exact sharp-nine mod30 channels in central-shell coordinates.
    if r%10==0:
        return 16,1
    if r%10==5:
        return 4,-1
    return None


def scan(rmax: int):
    hits=[]
    survivors=0
    for r in range(5,rmax+1):
        ch=channel_residue(r)
        if ch is None:
            continue
        hres,chi=ch
        lo,hi=valid_h_bounds(r)
        h0=lo+((hres-lo)%30)
        if h0>hi:
            continue
        n=(hi-h0)//30+1
        alive=bytearray(b"\x01")*n

        # For r>=100 every value is larger than all filter primes, so ordinary
        # divisibility marking is safe. Small r are replayed directly below.
        if r>=100:
            for q in FILTER_PRIMES:
                inv30=pow(30,-1,q)
                bad=set()
                for j in range(-4,5):
                    const=C(r+j,0)%q
                    bad.add(((-h0-const)*inv30)%q)
                for k in bad:
                    if k<n:
                        alive[k::q]=b"\x00"*(((n-1-k)//q)+1)

        for idx,ok in enumerate(alive):
            if not ok: continue
            survivors+=1
            h=h0+30*idx
            vals=[C(r+j,h) for j in range(-4,5)]
            if all(is_prime64(v) for v in vals):
                assert vals[-1]-vals[0]==24*r
                hits.append((r,h,chi,vals))
    return hits,survivors


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--r-max",type=int,default=350000)
    ap.add_argument("--csv",default="")
    args=ap.parse_args()

    hits,survivors=scan(args.r_max)
    plus=sum(chi==1 for _,_,chi,_ in hits)
    minus=len(hits)-plus
    print(f"R_MAX={args.r_max}")
    print(f"POST_WHEEL_CANDIDATES={survivors}")
    print(f"SHARP_NINE_HITS={len(hits)}")
    print(f"CHI_PLUS={plus}")
    print(f"CHI_MINUS={minus}")
    for r,h,chi,vals in hits:
        print(r,h,chi,vals[0],vals[-1])

    if args.r_max==350000:
        expected=[
            (10690,-2474),(19700,-9494),(32850,-2774),(69670,-5714),
            (74210,18646),(76910,-21584),(96900,-36794),(107815,7624),
            (109165,11134),(147300,34066),(149890,2566),(162025,-12266),
            (168675,55564),(171965,-46496),(176935,-61826),(262915,-83456),
            (265560,-69464),(279480,125176),(312045,-44456),(318765,69064),
        ]
        assert [(r,h) for r,h,_,_ in hits]==expected
        print("FROZEN_R350000_SCAN=PASS")

    if args.csv:
        with open(args.csv,"w",encoding="utf-8",newline="") as fh:
            w=csv.writer(fh,lineterminator="\n")
            w.writerow(["central_shell_r","h","chirality"]+[f"p{j}" for j in range(-4,5)])
            for r,h,chi,vals in hits:
                w.writerow([r,h,chi,*vals])


if __name__=="__main__":
    main()
