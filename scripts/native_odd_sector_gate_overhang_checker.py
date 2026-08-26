#!/usr/bin/env python3
"""Exact finite checker for odd-sector extra-gate overhang criteria."""

from __future__ import annotations

from math import isqrt


def factor(n: int) -> dict[int,int]:
    out={}
    d=2
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1
            n//=d
        d=3 if d==2 else d+2
    if n>1:
        out[n]=out.get(n,0)+1
    return out


def squarefree_kernel(n: int) -> frozenset[int]:
    return frozenset(p for p,e in factor(n).items() if e%2)


def gf2_rank(rows: list[list[int]]) -> int:
    if not rows:
        return 0
    M=[r[:] for r in rows]
    nr=len(M); nc=len(M[0]); rank=0
    for c in range(nc):
        pivot=next((i for i in range(rank,nr) if M[i][c]),None)
        if pivot is None:
            continue
        M[rank],M[pivot]=M[pivot],M[rank]
        for i in range(nr):
            if i!=rank and M[i][c]:
                M[i]=[a^b for a,b in zip(M[i],M[rank])]
        rank+=1
    return rank


def compatible(r: int) -> tuple[bool,int]:
    vals=[(2*u+1)**2+16*r for u in range(r)]
    kernels=[squarefree_kernel(v) for v in vals]
    primes=sorted({p for k in kernels for p in k})
    idx={p:i for i,p in enumerate(primes)}
    A=[]
    for k in kernels:
        row=[0]*len(primes)
        for p in k:
            row[idx[p]]=1
        A.append(row)
    rankA=gf2_rank(A)
    aug=[row+[1] for row in A]
    return gf2_rank(aug)==rankA,rankA


def is_square(n: int) -> bool:
    x=isqrt(n)
    return x*x==n


def main() -> None:
    # Overhang complement-discriminant identity.
    for r in range(1,50):
        for q in range(2*r+3,2*r+100,2):
            s=q-2*r
            if s<=0 or s%2==0:
                continue
            h=(s-1)//2
            for t in range(1,r+1):
                j=h+t
                u=r-t
                lhs=(4*(j*j-2*s))%q
                rhs=((2*u+1)**2+16*r)%q
                assert lhs==rhs,(r,q,s,t,lhs,rhs)

    # Every non-power-of-two r has an individual square obstruction.
    for r in range(3,301):
        if r&(r-1)==0:
            continue
        t=0
        m=r
        while m%2==0:
            t+=1
            m//=2
        assert m>1 and m%2==1
        x=abs(2**(t+2)-m)
        assert x%2==1 and 1<=x<2*r
        u=(x-1)//2
        assert 0<=u<r
        A=(2*u+1)**2+16*r
        assert A==(2**(t+2)+m)**2

    # Exact compatibility census through 300.
    good=[]
    for r in range(1,301):
        ok,rank=compatible(r)
        if ok:
            good.append((r,rank))
    assert good==[(1,1),(2,2),(4,4),(8,8),(16,16)],good

    # Explicit r=32 and r=64 odd square relations.
    vals32=[(2*u+1)**2+16*32 for u in range(32)]
    p32=vals32[0]*vals32[18]*vals32[29]
    assert p32==62073**2

    vals64=[(2*u+1)**2+16*64 for u in range(64)]
    inds=[4,21,25,34,54]
    p64=1
    for i in inds:
        p64*=vals64[i]
    assert p64==926901625**2

    print("OVERHANG_COMPLEMENT_DISCRIMINANT_IDENTITY=PASS")
    print("NON_POWER_OF_TWO_SINGLE_SQUARE_OBSTRUCTION=PASS")
    print("COMPATIBLE_OVERHANGS_R_LE_300={1,2,4,8,16}")
    print("R32_ODD_SQUARE_RELATION=PASS")
    print("R64_ODD_SQUARE_RELATION=PASS")
    print("GLOBAL_ONLY_1_2_4_8_16=CONJECTURE_NOT_PROVED")


if __name__ == "__main__":
    main()
