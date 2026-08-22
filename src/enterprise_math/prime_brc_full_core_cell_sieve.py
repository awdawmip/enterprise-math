"""Exact local sieve inside one Prime-BRC/L053 full-core mirror cell.

Owner-local L3 research support.

Fix an anchor-surviving double-composite mirror full-core cell

    A=S_-, B=S_+, gcd(A,B)=1, gcd(AB,M)=1, M=k(k+1).

All radii in the corresponding CRT cell are

    r=r0+j*A*B.

Writing the two residual tails at j=0 as u,v, every lift has

    L_-(j)=u-B*j,
    L_+(j)=v+A*j,

and the exact invariant

    A*L_-(j)+B*L_+(j)=2M.

Because A,B are the *full* <=k smooth cores, a lift belongs to this same cell
with both sides composite iff both residual tails are >k and have no prime
divisor <=k.  Since each tail is <k^2 when its core is >1, this is equivalent
to both tails being prime >k.

For each prime ell<=k, the number nu_ell of forbidden j-residue classes is

    nu_ell=1  if ell | M*A*B,
    nu_ell=2  otherwise.

If ell|A or ell|B, one linear form is constant nonzero mod ell and the other
forbids one residue.  If ell|M and ell∤AB, the two roots coincide because the
weighted sum is 2M.  Otherwise they are distinct.

In particular ell=2 always gives exactly one forbidden parity class, so valid
prime-tail lifts occupy at most one parity of j.
"""

from __future__ import annotations

from math import gcd, isqrt


def is_prime(n:int)->bool:
    if n<2:return False
    for d in range(2,isqrt(n)+1):
        if n%d==0:return False
    return True


def primes_up_to(n:int)->tuple[int,...]:
    return tuple(x for x in range(2,n+1) if is_prime(x))


def local_forbidden_residues(k:int,A:int,B:int,u:int,v:int,ell:int)->tuple[int,...]:
    """Return j mod ell for which either residual tail is divisible by ell."""
    if not is_prime(ell) or ell>k:
        raise ValueError("ell must be prime <=k")
    M=k*(k+1)
    if gcd(A,B)!=1 or gcd(A*B,M)!=1:
        raise ValueError("require coprime full cores transverse to M")
    if A*u+B*v!=2*M:
        raise ValueError("tail base point must satisfy A*u+B*v=2M")
    bad=[]
    for j in range(ell):
        if (u-B*j)%ell==0 or (v+A*j)%ell==0:
            bad.append(j)
    expected=1 if (M*A*B)%ell==0 else 2
    if len(bad)!=expected:
        raise AssertionError("local forbidden-residue count disagrees with theorem")
    return tuple(bad)


def cell_local_sieve_certificate(k:int,A:int,B:int,r0:int)->dict[str,object]:
    """Construct the two tail forms and all local nu_ell values for one CRT cell."""
    M=k*(k+1)
    if not (1<=r0<k):
        raise ValueError("require 1<=r0<k")
    if gcd(A,B)!=1 or gcd(A*B,M)!=1:
        raise ValueError("require coprime transverse cores")
    if (M-r0)%A or (M+r0)%B:
        raise ValueError("r0 must realize the core divisibilities")
    u=(M-r0)//A
    v=(M+r0)//B
    if A*u+B*v!=2*M:
        raise AssertionError("cell weighted-tail conservation failed")
    data={}
    for ell in primes_up_to(k):
        bad=local_forbidden_residues(k,A,B,u,v,ell)
        data[ell]={"nu":len(bad),"bad_residues":bad}
    if data[2]["nu"]!=1:
        raise AssertionError("parity did not remove exactly one j class")
    return {"k":k,"A":A,"B":B,"r0":r0,"u":u,"v":v,"local":data}


def raw_cell_lifts(k:int,A:int,B:int,r0:int)->tuple[tuple[int,int,int,int],...]:
    """Return bounded positive-radius CRT lifts as (j,r,Lminus,Lplus)."""
    M=k*(k+1); step=A*B
    out=[]
    # all integers j for which 1<=r0+j*step<k
    lo=-(r0-1)//step-2
    hi=(k-1-r0)//step+2
    for j in range(lo,hi+1):
        r=r0+j*step
        if 1<=r<k:
            lm=(M-r)//A if (M-r)%A==0 else None
            lp=(M+r)//B if (M+r)%B==0 else None
            if lm is None or lp is None:
                raise AssertionError("CRT lift left core divisibility")
            out.append((j,r,lm,lp))
    return tuple(sorted(out))


def prime_tail_lifts(k:int,A:int,B:int,r0:int)->tuple[tuple[int,int,int,int],...]:
    """Exact lifts whose two tails are prime >k; a finite replay, not an analytic bound."""
    return tuple(x for x in raw_cell_lifts(k,A,B,r0) if x[2]>k and x[3]>k and is_prime(x[2]) and is_prime(x[3]))


def parity_capacity_bound(k:int,A:int,B:int,r0:int)->dict[str,object]:
    lifts=raw_cell_lifts(k,A,B,r0)
    js=[x[0] for x in lifts]
    # Since A,B are odd (2|M and gcd(AB,M)=1), both tails flip parity each j-step.
    bound=(len(lifts)+1)//2
    valid=prime_tail_lifts(k,A,B,r0)
    if len(valid)>bound:
        raise AssertionError("prime-tail occupancy exceeded parity capacity")
    if len({j%2 for j,_,_,_ in valid})>1:
        raise AssertionError("valid prime-tail lifts occupy both j parities")
    return {"raw_capacity":len(lifts),"parity_capacity":bound,"prime_tail_count":len(valid),"valid_lifts":valid}
