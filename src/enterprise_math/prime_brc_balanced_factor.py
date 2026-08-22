"""Prime-BRC balanced-factor bridge for the P3 -> P2 frontier.

Owner-local L3 research support.  The theorem is elementary and does not by
itself improve Campbell's explicit P3 theorem.

If n is n^(1/8)-rough and Omega(n)<=3, define the balanced-divisor window

    n^(1/4) <= d <= n^(1/2).

Every triprime n=p*q*r (with multiplicity, p<=q<=r) has a proper divisor in
that window.  If p*q<=sqrt(n), then p*q is such a divisor because p,q>=n^(1/8).
If p*q>sqrt(n), then r=n/(p*q)<sqrt(n) and r>=n^(1/3)>n^(1/4).

Hence, inside the P3 universe, absence of a balanced divisor implies Omega<=2.
For n in (k^2,(k+1)^2), every integer d in the balanced window satisfies
sqrt(k)<d<=k.  This is the exact intermediate factor scale associated with the
Type-II/bilinear obstruction in the square interval.
"""

from __future__ import annotations

from math import isqrt


def factor_multiset(n: int) -> tuple[int, ...]:
    if n < 2:
        raise ValueError("n must be >=2")
    out=[]
    x=n
    p=2
    while p*p<=x:
        while x%p==0:
            out.append(p); x//=p
        p=3 if p==2 else p+2
    if x>1: out.append(x)
    return tuple(out)


def integer_balanced_divisors(n: int) -> tuple[int, ...]:
    """Proper divisors d with d^4>=n and d^2<=n."""
    if n < 2:
        raise ValueError("n must be >=2")
    out=[]
    for d in range(2,isqrt(n)+1):
        if n%d==0 and d**4>=n:
            out.append(d)
    return tuple(out)


def rough_p3_balanced_certificate(n: int) -> dict[str, object]:
    """Verify the exact balanced-divisor theorem on a concrete P3 input.

    The interface uses the integer equivalent of n^(1/8)-roughness: every prime
    factor p satisfies p^8>=n.
    """
    fs=factor_multiset(n)
    if len(fs)>3:
        raise ValueError("requires Omega(n)<=3")
    if any(p**8<n for p in fs):
        raise ValueError("requires n^(1/8)-roughness")
    balanced=integer_balanced_divisors(n)
    if len(fs)==3 and not balanced:
        raise AssertionError("rough triprime lacks balanced divisor")
    return {
        "n":n,
        "factors":fs,
        "omega":len(fs),
        "balanced_divisors":balanced,
        "empty_balanced_implies_P2": (not balanced and len(fs)<=2) or bool(balanced),
    }


def square_basin_balanced_scale(k: int, n: int, d: int) -> dict[str, object]:
    """Translate a balanced divisor of n in the k-square basin to sqrt(k)<d<=k."""
    if k<1 or not k*k<n<(k+1)*(k+1):
        raise ValueError("n must lie in the open k-square basin")
    if d<2 or n%d or d**4<n or d*d>n:
        raise ValueError("d must be a balanced divisor of n")
    if not d*d>k:
        # d > sqrt(k) is equivalent to d^2>k for integer d.
        raise AssertionError("balanced divisor failed lower square-basin scale")
    if d>k:
        raise AssertionError("balanced divisor exceeded k")
    return {
        "k":k,"n":n,"d":d,
        "d_squared_gt_k":True,
        "d_at_most_k":True,
        "complement":n//d,
        "complement_above_k": n//d>k,
    }
