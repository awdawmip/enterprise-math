"""Prime-BRC canonical divisor frontier for consecutive-square basins.

Owner-local L3 research support.  No prime-existence theorem is claimed.

For n in I_k=(k^2,(k+1)^2), sqrt(n) lies strictly between k and k+1.  Hence
there is a canonical adjacent divisor pair across the root threshold:

    A(n) = max {d|n : d<=k},
    C(n) = n/A(n) = min {d|n : d>k}.

Writing p=spf(C), m=C/p gives a fixed-depth normal form n=A*p*m with A,m<=k.
The cases prime / large-prime-tail / fully-k-smooth are separated exactly by
(A,m,p).

For an anchor-surviving mirror pair M+-r, the lower frontier factors on opposite
sides are coprime odd integers.  If both states are composite and A<B, the
complementary factors are reverse ordered and swapping them sends one product
strictly below k^2 and the other strictly above (k+1)^2.
"""

from __future__ import annotations

from math import gcd, isqrt


def _divisors(n: int) -> list[int]:
    small=[]; large=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            small.append(d)
            if d*d!=n:
                large.append(n//d)
    return small+large[::-1]


def _spf(n: int) -> int:
    if n<2: raise ValueError("n>=2 required")
    for d in range(2,isqrt(n)+1):
        if n%d==0: return d
    return n


def frontier(k: int, n: int) -> dict[str,int|str]:
    if k<2 or not k*k<n<(k+1)*(k+1):
        raise ValueError("require n in open square basin")
    ds=_divisors(n)
    A=max(d for d in ds if d<=k)
    C=n//A
    if C<=k:
        raise AssertionError("frontier complement failed C>k")
    if any(A<d<=k for d in ds):
        raise AssertionError("A is not maximal below root threshold")
    if any(k<d<C for d in ds):
        raise AssertionError("C is not minimal above root threshold")
    p=_spf(C); m=C//p
    if m>k:
        raise AssertionError("largest proper divisor C/spf(C) must be <=k")
    if A*p<=k:
        raise AssertionError("A*spf(C) would contradict maximality of A")
    if m==1:
        if p<=k:
            raise AssertionError("prime frontier complement C>k must exceed k")
        kind="PRIME" if A==1 else "LARGE_PRIME_TAIL_COMPOSITE"
    else:
        if p>k:
            raise AssertionError("p>k would make p itself a smaller >k divisor than C")
        kind="FULLY_K_SMOOTH_COMPOSITE"
    return {"k":k,"n":n,"A":A,"C":C,"p":p,"m":m,"kind":kind}


def mirror_frontier_escape(k: int, r: int) -> dict[str,int|bool]:
    """Cross-factor escape for an anchor-surviving double-composite mirror pair."""
    if k<2 or not 1<=r<k:
        raise ValueError("require k>=2 and 1<=r<k")
    M=k*(k+1)
    if gcd(r,M)!=1:
        raise ValueError("radius must survive anchor sieve")
    lo=M-r; hi=M+r
    f0=frontier(k,lo); f1=frontier(k,hi)
    if f0["kind"]=="PRIME" or f1["kind"]=="PRIME":
        raise ValueError("escape interface here requires both mirror states composite")
    A=int(f0["A"]); C=int(f0["C"])
    B=int(f1["A"]); D=int(f1["C"])
    if gcd(A,B)!=1 or A%2==0 or B%2==0 or A==B:
        raise AssertionError("surviving composite frontier cores must be distinct coprime odd")
    # Reorder rows so a<b; the corresponding complements must reverse order.
    if A<B:
        a,c,b,d=A,C,B,D
    else:
        a,c,b,d=B,D,A,C
    if b-a<2:
        raise AssertionError("distinct odd frontier cores lost spacing >=2")
    # Ratio inequality: a/b <= a/(a+2) < k^2/(k+1)^2.
    if not a*(k+1)*(k+1) < b*k*k:
        raise AssertionError("frontier spacing failed ratio separation")
    if not c>d:
        raise AssertionError("frontier complements failed reverse ordering")
    lower_cross=a*d
    upper_cross=b*c
    if not lower_cross<k*k:
        raise AssertionError("lower cross product failed to escape below basin")
    if not upper_cross>(k+1)*(k+1):
        raise AssertionError("upper cross product failed to escape above basin")
    return {
        "k":k,"r":r,"small_core":a,"large_core":b,
        "large_complement":c,"small_complement":d,
        "lower_cross":lower_cross,"upper_cross":upper_cross,
        "escape":True,
    }
