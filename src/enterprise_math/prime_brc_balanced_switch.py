"""Canonical balanced divisor switching for rough P3 states in a square basin.

Owner-local L3 research support.

For a rough triprime a=p*q*r, p<=q<=r, define the canonical factor below sqrt(a)
by

    d*=p*q  if p*q<sqrt(a),
    d*=r    if r<sqrt(a).

(The equality case cannot occur for Omega(a)=3.)  Then m*=a/d* is the other
block.  Roughness p,q,r>=a^(1/8) yields a^(1/4)<=d*<sqrt(a)<m*<=a^(3/4).

Inside (k^2,(k+1)^2), integer d* therefore satisfies sqrt(k)<d*<=k and m*>k.
For fixed m>k the square basin contains at most two m-multiples, with consecutive
multipliers.  If the state is z-rough for any z>2, its multiplier is odd, so at
most one of those two hits can be rough.  Consequently the canonical large block
m* is an injective index for rough triprime states in one square basin.

This is a coefficient/source-multiplicity theorem, not a P2 existence theorem.
"""

from __future__ import annotations

from math import isqrt


def prime_factor_multiset(n:int)->tuple[int,...]:
    if n<2: raise ValueError("n>=2 required")
    out=[]; x=n; p=2
    while p*p<=x:
        while x%p==0:
            out.append(p); x//=p
        p=3 if p==2 else p+2
    if x>1: out.append(x)
    return tuple(out)


def canonical_triprime_split(n:int)->dict[str,int]:
    fs=prime_factor_multiset(n)
    if len(fs)!=3:
        raise ValueError("requires Omega(n)=3")
    p,q,r=fs
    pq=p*q
    if pq*pq<n:
        d=pq; m=r
    else:
        # pq^2>n; equality would make n a square, impossible for Omega=3.
        if pq*pq==n:
            raise AssertionError("triprime unexpectedly square")
        d=r; m=pq
    if d*d>=n or m*m<=n or d*m!=n:
        raise AssertionError("canonical split failed strict sqrt orientation")
    return {"p":p,"q":q,"r":r,"d":d,"m":m}


def rough_triprime_balanced_switch(k:int,n:int)->dict[str,object]:
    """Certificate for an n^(1/8)-rough triprime inside the k-square basin."""
    if k<2 or not k*k<n<(k+1)*(k+1):
        raise ValueError("n must lie in the open k-square basin")
    data=canonical_triprime_split(n)
    fs=(data["p"],data["q"],data["r"])
    if any(p**8<n for p in fs):
        raise ValueError("requires n^(1/8)-roughness")
    d=data["d"]; m=data["m"]
    if d**4<n:
        raise AssertionError("balanced lower bound d>=n^(1/4) failed")
    if m**4>n**3:
        raise AssertionError("balanced upper bound m<=n^(3/4) failed")
    if not (d*d>k and d<=k<m):
        raise AssertionError("square-basin balanced scale failed")
    return {**data,"k":k,"n":n,"d_squared_gt_k":True,"m_above_k":True}


def multiplier_window(k:int,m:int)->tuple[int,...]:
    """All d with k^2 < d*m < (k+1)^2."""
    if k<1 or m<1: raise ValueError("positive k,m required")
    lo=k*k//m+1
    hi=k*(k+2)//m
    if hi<lo: return ()
    return tuple(range(lo,hi+1))


def odd_multiplier_decode(k:int,m:int)->int|None:
    """Unique odd basin multiplier when m>k, if one exists."""
    if m<=k: raise ValueError("requires m>k")
    window=multiplier_window(k,m)
    if len(window)>2:
        raise AssertionError("m>k produced more than two basin multipliers")
    odds=[d for d in window if d%2]
    if len(odds)>1:
        raise AssertionError("two consecutive multipliers both odd")
    return odds[0] if odds else None


def canonical_large_block_injection(k:int,triprimes:tuple[int,...])->dict[str,object]:
    """Verify injectivity n -> m* on a supplied rough-triprime family."""
    decoded={}
    for n in triprimes:
        data=rough_triprime_balanced_switch(k,n)
        m=data["m"]; d=data["d"]
        if odd_multiplier_decode(k,m)!=d:
            raise AssertionError("large block failed to decode its canonical odd multiplier")
        if m in decoded:
            raise AssertionError("two rough triprimes share one canonical large block")
        decoded[m]=n
    return {"k":k,"count":len(triprimes),"large_block_to_state":decoded,"injective":True}
