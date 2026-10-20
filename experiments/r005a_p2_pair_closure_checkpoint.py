#!/usr/bin/env python3
"""R005-A consolidated exact verifier for p=2 local forcedness and pair closure.

Requires companion exact certificate family:
    experiments/r005a_p2_exact_residual_family.py

Checks on all 49 certified no-least square basins:
1. local forcedness theorem above the fourth-root core;
2. deterministic pair closure equals direct exhaustive residual enumeration;
3. repeated-sector quotient/remainder closure;
4. repeated-prime prime-pair parametrization;
5. correction: the earlier "inner square recursion" is algebraically
   tautological, floor(k/q)=floor(sqrt(r)).
"""

from __future__ import annotations

import importlib.util
from math import isqrt
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
SRC = HERE / "r005a_p2_exact_residual_family.py"
spec = importlib.util.spec_from_file_location("p2family", SRC)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load {SRC}")
family = importlib.util.module_from_spec(spec)
spec.loader.exec_module(family)


def next_prime_strict(num: int, den: int) -> int:
    n = num // den + 1
    if n <= 2:
        return 2
    if n % 2 == 0:
        n += 1
    while not family.is_prime(n):
        n += 2
    return n


def cofactor_gap_defect(k: int, q: int) -> tuple[int, int]:
    A = k*k
    r = next_prime_strict(A, q)
    return r, q*r - A


def local_forced_formula(k: int, q: int) -> bool:
    A = k*k
    U = A + 2*k
    _, defect = cofactor_gap_defect(k, q)
    return (A < q**3 <= U) or defect <= 2*k


def odd_floor(num: int, den: int) -> int:
    m = num // den
    return m if m % 2 else m - 1


def nonforced_set(k: int) -> tuple[int, ...]:
    return tuple(
        q for q in family.BASE_PRIMES
        if q <= k and not family.witness_forced(k, q)
    )


def pair_closure_residuals(k: int) -> dict[int, tuple[int, int, int]]:
    A = k*k
    U = A + 2*k
    C4 = family.integer_root(U, 4)
    A3 = family.integer_root(A, 3)

    assert all(
        family.witness_forced(k, q)
        for q in family.BASE_PRIMES
        if q <= C4
    )

    nf = nonforced_set(k)
    nf_set = set(nf)
    out = {}

    for a in nf:
        if a <= C4:
            continue
        if a > A3:
            break
        for b in nf:
            if b < a:
                continue
            if a*b*b > U:
                break

            d = a*b
            assert d > k
            assert 2*k < 2*d

            c = odd_floor(U, d)
            if c < b or c > k or c not in nf_set:
                continue
            if A < d*c <= U:
                out[d*c] = (a,b,c)
    return out


def direct_residuals(k: int) -> dict[int, tuple[int, int, int]]:
    A = k*k
    U = A + 2*k
    forced = {
        q for q in family.BASE_PRIMES
        if q <= k and family.witness_forced(k, q)
    }

    out = {}
    for n in range(A+1, U+1):
        x = n
        ps = []
        for q in family.BASE_PRIMES:
            if q*q > x:
                break
            while x % q == 0:
                ps.append(q)
                x //= q
            if x == 1:
                break
        if x > 1:
            ps.append(x)

        if len(ps) == 1:
            continue
        support = {q for q in set(ps) if q <= k}
        if support and not support.intersection(forced):
            assert len(ps) == 3
            out[n] = tuple(sorted(ps))
    return out


def repeated_closure(k: int, q: int) -> tuple[int, int, int]:
    U = k*k + 2*k
    qq = q*q
    t, rem = divmod(U, qq)
    r = t if t % 2 else t - 1
    rho = U - qq*r
    assert rho == (rem if t % 2 else rem + qq)
    return t, r, rho


def main() -> None:
    basins = sorted({k for k,_,_ in family.CERTIFICATES})

    local_checks = 0
    residual_total = 0
    repeated_total = 0
    odd_branch = 0
    even_branch = 0
    patterns = {"a=b<c":0, "a<b=c":0, "a<b<c":0}

    examples = []

    for k in basins:
        A = k*k
        U = A + 2*k
        C4 = family.integer_root(U, 4)

        for q in family.BASE_PRIMES:
            if q <= C4:
                continue
            if q > k:
                break
            assert family.witness_forced(k, q) == local_forced_formula(k, q)
            local_checks += 1

        pair = pair_closure_residuals(k)
        direct = direct_residuals(k)
        assert pair == direct
        residual_total += len(pair)

        for n,(a,b,c) in pair.items():
            if a == b < c:
                patterns["a=b<c"] += 1
                q,r = a,c
            elif a < b == c:
                patterns["a<b=c"] += 1
                q,r = b,a
            elif a < b < c:
                patterns["a<b<c"] += 1
                continue
            else:
                raise AssertionError(("prime cube residual",k,n,a,b,c))

            repeated_total += 1
            t, closure, rho = repeated_closure(k, q)
            assert closure == r
            assert rho < 2*k
            assert not family.witness_forced(k, q)
            assert not family.witness_forced(k, r)

            reconstructed_k = isqrt(q*q*r)
            assert reconstructed_k == k
            assert r <= q*q

            assert k // q == isqrt(r)

            if t % 2:
                odd_branch += 1
            else:
                even_branch += 1

            if len(examples) < 6:
                _, dq = cofactor_gap_defect(k,q)
                _, dr = cofactor_gap_defect(k,r)
                examples.append({
                    "k":k,"n":n,"q_repeated":q,"r_singleton":r,
                    "raw_floor_U_over_q2":t,"rho":rho,
                    "q_defect":dq,"r_defect":dr,
                    "basin_width":2*k,
                })

    assert local_checks == 19794
    assert residual_total == 50
    assert repeated_total == 45
    assert patterns == {"a=b<c":43, "a<b=c":2, "a<b<c":5}
    assert odd_branch + even_branch == 45

    result = {
        "status":"R005-A P2 PAIR-CLOSURE CONSOLIDATED EXACT CHECKPOINT",
        "verified_basin_count":len(basins),
        "local_forcedness_checks":local_checks,
        "pair_closure_equals_direct_scan":True,
        "verified_residual_count":residual_total,
        "patterns":patterns,
        "repeated_residual_count":repeated_total,
        "repeated_parity_branches":{
            "raw_quotient_odd":odd_branch,
            "raw_quotient_even_minus_one":even_branch,
        },
        "theorems":{
            "local_forcedness":"for prime C4<q<=k: forced iff k^2<q^3<=U or q*nextPrimeStrict(k^2/q)-k^2<=2k",
            "pair_closure":"under forced C4 core, no-least iff a non-forced pair a<=b closes to the unique odd non-forced prime c in (k^2/(ab),U/(ab)]",
            "minimal_factor_annulus":"C4<a<=floor((k^2)^(1/3))",
            "repeated_quotient_closure":"r=oddFloor(U/q^2), rho=U-q^2*r<2k",
            "repeated_pair_parametrization":"for distinct primes q,r with r<=q^2, k=floor(sqrt(q^2*r)); q^2*r residual iff q,r are non-forced in basin k",
        },
        "correction":"floor(k/q)=floor(sqrt(r)) for a repeated residual q^2*r, so the earlier inner-square prime-anchor interpretation is algebraically tautological and is not promoted",
        "examples":examples,
    }
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
