"""Prime-BRC proper-large-factor switching ladder.

Owner-local L3 research support.  This module records exact finite arithmetic
behind the P_s -> P_{s-1} large-carry branch multiplicity and the squarefree
P3 Richert penalty for Campbell's k2=3.17, lambda=0.83 parameters.

It does not prove a P2 theorem; an analytic upper bound for the switched carry
mass is still required, and repeated-factor triprimes require a separate error.
"""

from __future__ import annotations

from math import isqrt


def factor_list(n:int)->tuple[int,...]:
    if n<2: return ()
    out=[]; v=n; p=2
    while p*p<=v:
        while v%p==0:
            out.append(p); v//=p
        p=3 if p==2 else p+2
    if v>1: out.append(v)
    return tuple(out)


def omega(n:int)->int:
    return len(factor_list(n))


def proper_large_pj_count(k:int,n:int,j:int)->int:
    """C_j^o(n): proper divisors D with k<D<n and Omega(D)=j.

    In an open square basin, isqrt(n)=k.  Hence every divisor pair has one
    member <=k and the complementary member >k.  Enumerate the small side and
    count its complementary large divisor; do not try to enumerate integers in
    the empty interval (k,sqrt(n)].
    """
    if k<2 or not k*k<n<(k+1)*(k+1):
        raise ValueError("n must lie in the square basin")
    if j<1: raise ValueError("j>=1 required")
    seen=set()
    for d in range(1,k+1):
        if n%d: continue
        D=n//d
        if k<D<n and omega(D)==j:
            seen.add(D)
    return len(seen)


def squarefree_prime_factors(n:int)->tuple[int,...]:
    fs=factor_list(n)
    if len(set(fs))!=len(fs):
        raise ValueError("n must be squarefree")
    return fs


def switching_ladder_certificate(k:int,n:int)->dict[str,object]:
    """For odd squarefree P_s, certify C_{s-1}^o >= s-1."""
    fs=squarefree_prime_factors(n)
    s=len(fs)
    if s<2 or n%2==0 or not k*k<n<(k+1)*(k+1):
        raise ValueError("require odd squarefree basin P_s with s>=2")
    # Two factors >k would already force n >= (k+1)^2.
    if sum(p>k for p in fs)>1:
        raise AssertionError("more than one prime factor exceeded k")
    branches=[]
    for p in fs:
        D=n//p
        if D>k and D<n and omega(D)==s-1:
            branches.append(D)
    if len(branches)<s-1 or len(set(branches))!=len(branches):
        raise AssertionError("proper-large branch ladder failed")
    if proper_large_pj_count(k,n,s-1)!=len(branches):
        raise AssertionError("direct proper-large count disagrees with deleted-prime branches")
    return {"k":k,"n":n,"omega":s,"branches":tuple(sorted(branches)),"count":len(branches)}


def p3_type_and_branch_count(k:int,n:int)->dict[str,object]:
    fs=squarefree_prime_factors(n)
    if len(fs)!=3 or n%2==0 or not k*k<n<(k+1)*(k+1):
        raise ValueError("require odd squarefree triprime in basin")
    p,q,r=fs
    if q>k:
        raise AssertionError("middle triprime prime must satisfy q<=k")
    if p*q<r:
        typ="A"
        if p*q>k:
            raise AssertionError("A-type pq<r forces pq<=k")
        expected=2
    else:
        typ="B"
        if p*q<=k:
            raise AssertionError("B-type r<pq forces pq>k")
        expected=3
    c=proper_large_pj_count(k,n,2)
    if c!=expected:
        raise AssertionError("P3 proper-large P2 branch count mismatch")
    return {"k":k,"n":n,"factors":fs,"type":typ,"C2_proper":c}


def richert_weight_prime_factors(primes:tuple[int,...],X:float,k2:float=3.17,lam:float=0.83)->float:
    y=X**(1.0/k2)
    total=lam
    from math import log
    for p in set(primes):
        if p<y:
            total-=1.0-log(p)/log(y)
    return total


def p3_richert_penalty_certificate(k:int,n:int,k2:float=3.17,lam:float=0.83)->dict[str,object]:
    """Statewise squarefree P3 bound w <= (lambda/3) C2^o.

    The proof behind the executable check is:
      A type pq<r => pq<sqrt(n)<sqrt(X), so either q<y (two weight
      subtractions) or q>=y (then p<X^(1/2-1/k2)); both give
      w < 2-k2/2 = lambda/2 for lambda=4-k2.
      B type uses the trivial w<=lambda.
    """
    data=p3_type_and_branch_count(k,n)
    X=float((k+1)*(k+1))
    fs=tuple(data["factors"])
    w=richert_weight_prime_factors(fs,X,k2,lam)
    c=int(data["C2_proper"])
    rhs=lam*c/3.0
    if data["type"]=="A" and not w < lam/2.0+1e-12:
        raise AssertionError("A-type Richert half-lambda bound failed")
    if w>rhs+1e-12:
        raise AssertionError("Richert P3 proper-P2 penalty bound failed")
    return {**data,"weight":w,"penalty_bound":rhs,"lambda":lam,"k2":k2}
