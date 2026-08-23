#!/usr/bin/env python3
"""Exact checker for sharp-nine endpoint holography and dual-tangent local sieve."""

from __future__ import annotations

import itertools
import math


def alpha(j: int, chi: int) -> int:
    num = 3*j*j + (chi if j % 2 else 0)
    assert num % 2 == 0
    return num // 2


def packet_from_center(r: int, c: int):
    chi = 1 if r % 2 == 0 else -1
    return [c + 3*r*j + alpha(j, chi) for j in range(-4,5)]


def recover_from_endpoints(a: int, b: int):
    assert (b-a) % 24 == 0
    r = (b-a)//24
    c = (a+b-48)//2
    chi = 1 if r % 2 == 0 else -1
    h = c - (3*r*r)//2 - 1 - ((1-chi)//4)
    return r,h,c,packet_from_center(r,c)


def local_allowed(q: int, chi: int) -> int:
    out=0
    for r in range(q):
        for c in range(q):
            if all((c+3*j*r+alpha(j,chi)) % q for j in range(-4,5)):
                out += 1
    return out


def obstruction_primes(chi: int):
    out=set()
    vals=set()
    js=range(-4,5)
    for j,k in itertools.combinations(js,2):
        if (j-k) % 2:
            continue
        for l in js:
            if l in (j,k) or (l-j)%2==0:
                continue
            if j%2==0:
                v=3*(l-j)*(l-k)+chi
            else:
                v=3*(l-j)*(l-k)-chi
            v=abs(v)
            vals.add(v)
            d=2
            n=v
            while d*d<=n:
                while n%d==0:
                    out.add(d); n//=d
                d+=1
            if n>1: out.add(n)
    return vals,out


def main() -> None:
    even=[
        171283421,171315481,171347543,171379609,171411677,
        171443749,171475823,171507901,171539981,
    ]
    odd=[
        17434825207,17435148641,17435472079,17435795519,17436118963,
        17436442409,17436765859,17437089311,17437412767,
    ]

    r,h,c,p=recover_from_endpoints(even[0],even[-1])
    assert (r,h,c)==(10690,-2474,even[4]) and p==even
    r,h,c,p=recover_from_endpoints(odd[0],odd[-1])
    assert (r,h,c)==(107815,7624,odd[4]) and p==odd

    for packet in (even,odd):
        for i in range(6):
            assert packet[i+3]==packet[i+2]+packet[i+1]-packet[i]+6
        for i in range(5):
            assert packet[i+4]-2*packet[i+2]+packet[i]==12

    expected_vals={2,4,8,10,14,16,20,22,26,28,44,46,62,64,104,106}
    for chi in (1,-1):
        vals,ps=obstruction_primes(chi)
        assert vals==expected_vals
        assert {q for q in ps if q>7}=={11,13,23,31,53}

    exceptional={
        11:(51,51),
        13:(84,85),
        23:(354,353),
        31:(716,716),
        53:(2366,2366),
    }
    for q,(ep,em) in exceptional.items():
        assert local_allowed(q,1)==ep
        assert local_allowed(q,-1)==em

    # Generic exact count: test enough primes to cover all post-exception regimes.
    for q in (17,19,29,37,41,43,47,59,61,67,71,73,79,83,89,97,101,107):
        want=q*q-9*q+36
        assert local_allowed(q,1)==want
        assert local_allowed(q,-1)==want

    print("ENDPOINT_HOLOGRAPHY=PASS")
    print("CURVATURE_FLATTENING_RECURRENCES=PASS")
    print("DUAL_TANGENT_EXCEPTIONAL_PRIMES=11,13,23,31,53")
    print("FINAL_EXCEPTIONAL_PRIME=53")
    print("ONLY_CHIRAL_COUNT_DETECTORS=13,23")
    print("LOCAL_PRODUCT_RATIO_PLUS_MINUS=29736/30005")


if __name__ == "__main__":
    main()
