#!/usr/bin/env python3
"""Exact standard-library Lehmer prime-count check for the sharp-nine plateau witness."""

from __future__ import annotations

import functools
import math

TARGET=152_412_931_746
EXPECTED_PI=6_169_167_536


def build_lehmer(max_n: int):
    lim=math.isqrt(max_n)+100
    mark=bytearray(b"\x01")*(lim+1)
    mark[:2]=b"\x00\x00"
    for p in range(2,math.isqrt(lim)+1):
        if mark[p]:
            mark[p*p:lim+1:p]=b"\x00"*(((lim-p*p)//p)+1)
    primes=[i for i in range(2,lim+1) if mark[i]]
    pi=[0]*(lim+1)
    c=0
    for i in range(lim+1):
        if mark[i]: c+=1
        pi[i]=c

    @functools.lru_cache(maxsize=None)
    def phi(x: int,s: int) -> int:
        if s==0: return x
        if s==1: return x-x//2
        return phi(x,s-1)-phi(x//primes[s-1],s-1)

    @functools.lru_cache(maxsize=None)
    def lehmer(x: int) -> int:
        if x<=lim:
            return pi[x]

        # exact integer roots corrected around floating initial guesses
        a0=int(x**0.25)
        while (a0+1)**4<=x: a0+=1
        while a0**4>x: a0-=1
        a=lehmer(a0)

        b=lehmer(math.isqrt(x))

        c0=int(round(x**(1/3)))
        while (c0+1)**3<=x: c0+=1
        while c0**3>x: c0-=1
        cidx=lehmer(c0)

        total=phi(x,a)+((b+a-2)*(b-a+1))//2
        for i in range(a,b):
            w=x//primes[i]
            total-=lehmer(w)
            if i<cidx:
                lim2=lehmer(math.isqrt(w))
                for j in range(i,lim2):
                    total-=lehmer(w//primes[j])-j
        return total

    return lehmer


def main() -> None:
    pi=build_lehmer(TARGET)
    got=pi(TARGET)
    assert got==EXPECTED_PI,(got,EXPECTED_PI)
    print(f"PI_{TARGET}={got}")
    print("SHARP9_PLATEAU_CHANNEL_LOWER_BOUND=6169167536")

if __name__=="__main__":
    main()
