#!/usr/bin/env python3
"""R005-A ambient closure complex / non-forced shadow exact verifier.

On square basin B_k=(k^2,(k+1)^2), assume the fourth-root core is forced.

Ambient arithmetic closure:
- vertices are primes q with C4<q<=k;
- an ambient block is the distinct-prime support of an odd Omega=3 basin
  integer abc with C4<a<=b<=c<=k.
- any two distinct vertices in a block determine the third multiplicity
  coordinate through oddFloor(U/(pq)); hence the squarefree sector is a
  partial Steiner triple system and the full support system is a linear
  rank<=3 hypergraph (with 2-edges for repeated-prime products).

Arithmetic truth shadow:
- NF_k is the set of non-forced candidate witnesses.
- residual blocks are exactly ambient blocks whose vertices all lie in NF_k.

Repair:
- after the forced core, a repair T is safe iff T hits every residual block.
"""

from __future__ import annotations

import importlib.util
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
SRC = HERE / "r005a_p2_exact_residual_family.py"
spec = importlib.util.spec_from_file_location("p2family", SRC)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load {SRC}")
family = importlib.util.module_from_spec(spec)
spec.loader.exec_module(family)


def odd_floor(num: int, den: int) -> int:
    t = num // den
    return t if t % 2 else t - 1


def ambient_blocks(k: int) -> dict[tuple[int, ...], int]:
    A = k*k
    U = A + 2*k
    C4 = family.integer_root(U,4)
    A3 = family.integer_root(A,3)
    primes = [q for q in family.BASE_PRIMES if C4 < q <= k]
    roots = [q for q in primes if q <= A3]

    blocks: dict[tuple[int,...],int] = {}
    for a in roots:
        for b in primes:
            if b < a:
                continue
            if a*b*b > U:
                break
            c = odd_floor(U,a*b)
            if c < b or c > k or not family.is_prime(c):
                continue
            N = a*b*c
            if not (A < N <= U):
                continue
            S = tuple(sorted(set((a,b,c))))
            if S in blocks:
                assert blocks[S] == N
            blocks[S] = N
    return blocks


def nonforced_vertices(k: int, vertices) -> set[int]:
    return {q for q in vertices if not family.witness_forced(k,q)}


def direct_expected(k: int) -> dict[tuple[int,...],int]:
    out={}
    for kk,N,factors in family.CERTIFICATES:
        if kk != k:
            continue
        S=tuple(sorted(p for p,e in factors))
        out[S]=N
    return out


def transversal_number(blocks: list[set[int]]) -> tuple[int,list[tuple[int,...]]]:
    if not blocks:
        return 0,[()]
    V=sorted(set().union(*blocks))
    for r in range(1,len(V)+1):
        sols=[]
        for T in combinations(V,r):
            ST=set(T)
            if all(ST & B for B in blocks):
                sols.append(T)
        if sols:
            return r,sols
    raise AssertionError


def main():
    basins=sorted({k for k,_,_ in family.CERTIFICATES})
    total_ambient=0
    total_residual=0
    ambient_2=ambient_3=ambient_1=0
    residual_2=residual_3=0
    pair_owner_checks=0
    rows=[]

    for k in basins:
        U=k*k+2*k
        C4=family.integer_root(U,4)
        assert all(
            family.witness_forced(k,q)
            for q in family.BASE_PRIMES
            if q<=C4
        )

        H=ambient_blocks(k)
        vertices=set().union(*(set(S) for S in H)) if H else set()
        NF=nonforced_vertices(k,vertices)
        R={S:N for S,N in H.items() if set(S)<=NF}
        expected=direct_expected(k)
        assert R==expected

        owner={}
        for S,N in H.items():
            if len(S)==1:
                ambient_1+=1
            elif len(S)==2:
                ambient_2+=1
            elif len(S)==3:
                ambient_3+=1
            else:
                raise AssertionError
            for p,q in combinations(S,2):
                pair=(p,q)
                if pair in owner:
                    assert owner[pair]==S
                owner[pair]=S
                pair_owner_checks+=1

        for S in R:
            if len(S)==2: residual_2+=1
            elif len(S)==3: residual_3+=1
            else: raise AssertionError(("residual singleton impossible",k,S))

        blocks=[set(S) for S in R]
        tau,repairs=transversal_number(blocks)
        assert tau==1

        rows.append({
            "k":k,
            "ambient_blocks":len(H),
            "ambient_vertices":len(vertices),
            "nonforced_ambient_vertices":len(NF),
            "residual_blocks":len(R),
            "repair_number_tau":tau,
            "minimum_repairs":repairs[:20],
        })
        total_ambient+=len(H)
        total_residual+=len(R)

    H1781=ambient_blocks(1781)
    U=1781*1781+2*1781
    C4=family.integer_root(U,4)
    vertices=set().union(*(set(S) for S in H1781))
    NF=nonforced_vertices(1781,vertices)
    R1781={S:N for S,N in H1781.items() if set(S)<=NF}
    containing_101={S:N for S,N in R1781.items() if 101 in S}
    assert containing_101 == {
        (101,311): 3172511,
        (101,149,211): 3175339,
    }
    for S,N in containing_101.items():
        for pair in combinations(S,2):
            matches=[T for T,M in H1781.items() if set(pair)<=set(T)]
            assert matches==[S]

    result={
        "status":"R005-A AMBIENT CLOSURE COMPLEX x NONFORCED SHADOW EXACT CHECK",
        "verified_basins":len(basins),
        "ambient_block_total":total_ambient,
        "residual_block_total":total_residual,
        "ambient_rank_counts":{"rank1":ambient_1,"rank2":ambient_2,"rank3":ambient_3},
        "residual_rank_counts":{"rank2":residual_2,"rank3":residual_3},
        "ambient_linearity_pair_checks":pair_owner_checks,
        "theorems":{
            "induced_shadow":"R_k = H_k[NF_k] on the fourth-root-forced slice",
            "linearity":"distinct ambient support blocks intersect in at most one witness",
            "squarefree_sector":"rank-3 ambient blocks form a partial Steiner triple system",
            "repair":"forced core union T is safe iff T is a transversal of R_k",
            "pair_minimality":"a factor pair determines its ambient block, but one witness need not determine a residual block",
        },
        "single_witness_negative_boundary":{
            "k":1781,
            "witness":101,
            "distinct_residual_blocks": [
                {"support":list(S),"N":N}
                for S,N in containing_101.items()
            ],
            "conclusion":"k plus one witness is insufficient for generic residual-block reconstruction"
        },
        "current_certificate_repair_observation":{
            "all_49_no_least_basins_have_tau":1,
            "not_a_global_theorem":True,
        },
        "rows":rows,
    }
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
