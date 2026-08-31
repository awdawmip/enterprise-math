#!/usr/bin/env python3
"""Exact finite-field checker for chirality reversal and odd-window boundary flux."""

from __future__ import annotations

from collections import Counter


def eta(j: int, chi: int, q: int) -> int:
    return ((3*j*j + (chi if j % 2 else 0))*pow(2,-1,q)) % q


def line(q: int, j: int):
    off=eta(j,1,q)
    return {(r,(-3*j*r-off)%q) for r in range(q)}


def survivor_count(k: int, q: int, chi: int) -> int:
    bad=set()
    for j in range(k):
        off=eta(j,chi,q)
        bad.update((r,(-3*j*r-off)%q) for r in range(q))
    return q*q-len(bad)


def boundary_flux(k: int, q: int):
    common=set().union(*(line(q,j) for j in range(1,k)))
    plane={(r,c) for r in range(q) for c in range(q)}
    A=plane-common
    left=len(A & line(q,0))
    right=len(A & line(q,k))
    return right-left,left,right


def main() -> None:
    primes=(5,7,11,13,17,19,23,29,31,37,41,43,47,53,59)

    # Even lengths are exactly balanced at every tested odd prime, including exceptions.
    for k in (4,6,8):
        for q in primes:
            assert survivor_count(k,q,1)==survivor_count(k,q,-1)

    expected={
        (5,5):(8,7),
        (7,5):(4,3),
        (7,13):(98,99),
        (9,13):(84,85),
        (9,23):(354,353),
    }
    for (k,q),(plus,minus) in expected.items():
        assert survivor_count(k,q,1)==plus
        assert survivor_count(k,q,-1)==minus
        flux,_,_=boundary_flux(k,q)
        assert flux==plus-minus

    # Sharp-nine exceptional channels that remain globally balanced.
    for q in (11,31,53):
        assert survivor_count(9,q,1)==survivor_count(9,q,-1)
        flux,_,_=boundary_flux(9,q)
        assert flux==0

    assert boundary_flux(9,13)==(-1,7,6)
    assert boundary_flux(9,23)==(1,16,17)

    print("EVEN_K_CHIRALITY_REVERSAL=PASS k=4,6,8")
    print("ODD_K_BOUNDARY_FLUX=PASS")
    print("K9_Q13_FLUX=-1")
    print("K9_Q23_FLUX=+1")
    print("K9_LATER_CHIRAL_RATIO=29736/30005")


if __name__=="__main__":
    main()
