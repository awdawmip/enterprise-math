# T6 exact-v₂(d)=5 population rigidity: seven 64-gap cases eliminated by a complete third-tier 2-adic obstruction

Date: 2026-11-23 (Asia/Taipei). New mathematics and finite exact verifier: continuing original Research Driver `EM-DVR-DEBB5E`. This note preserves earlier contributors' separate p19/p17 and higher-2-adic theorems and earlier Driver two-atom work, rather than reassigning or reproducing them. Scientific theorem/proof is independent of Native Review/Result and Source Activity admissions.

## Precise theorem

Let `A,B` be finite multisets of positive integers `e` satisfying separate `sum_A e<=2331`, `sum_B e<=2331`. Define `d=e+1` and `H_k(X)=sum_{e in X}(e/(e+1))^k`. Suppose `H_k(A)=H_k(B)` for every integer `0<=k<=6`.

**Then the numbers of exact-valuation-five denominator occurrences are equal:**

```
sum_{j odd, 1<=j<=71} m_A(32j)
   = sum_{j odd, 1<=j<=71} m_B(32j).
```

The proof uses the previously published universal cancellation of `v₂(d)>=6` denominators, including the [exact-v₂=6 theorem](https://github.com/awdawmip/enterprise-math/blob/c577f07bcd434340c500b91e4b67a5402c82c514/research_notes/driver/2026-11-23_t6_p2_sixth_universal_cancellation_three_tier.md). It also uses a new elementary congruence, complete first/two-tier profile census, and the third-tier exact finite obstruction below. The conclusion is **equality of atom counts** at valuation 5, not yet equality of the individual denominator multisets for all populations.

## Reduction from the full rational moments

Binomial inversion yields equality of reciprocal moments `S_k=sum_d m(d)/d^k`, `1<=k<=6`. Cancel literally the proven-equal `v₂>=6` contributions, and write, for `v=3,4,5`,

`D_{v,k}=sum_{j odd}(m_A(2^v*j)-m_B(2^v*j))*j^(-k).`

Multiply the complete signed reciprocal identity by `2^(5k)` and reduce modulo `2^(3k)`. All `v₂(d)<=2` terms then vanish; the necessary full mixed-valuation condition is

```
D_{5,k} + 2^k D_{4,k} + 2^(2k) D_{3,k} == 0 (mod 2^(3k)),
k=1,2,3,4,5,6.
```

In particular the first-tier `D_{5,k}==0(mod2^k)` and the second-tier `D_{5,k}+2^k D_{4,k}==0(mod2^(2k))` hold. All inverse powers are computed on *odd* denominators and are exact modular integers. No standalone rational-moment condition on one valuation layer is imposed.

The [immediately preceding analytic proof](https://github.com/awdawmip/enterprise-math/blob/a55b2bd799df738115758f9c4677cebbd96530c1/research_notes/driver/2026-11-23_t6_v2fifth_population_mod64_empty_side_and_seven_residual.md) proves from `k=2,4,6` that the population difference `N=n_A-n_B` is divisible by 64. Since each side's `n_X<=floor(2331/31)=75`, any unequal population would have `|N|=64`. It also rules out an empty side opposite a nonempty one.

The same prior report contains a **complete exact enumeration** under the individual mass bounds of all 64-gap profiles: 382,145 initial profile pairs, 2,906 meeting the first tier, 39 with a potential unrestricted v₂=4 correction, and precisely seven whose v₂=4 correction can fit each side's residual mass budget. The code and literal seven cases are frozen at [the source checker](https://github.com/awdawmip/enterprise-math/blob/8ebd45da79a457168746b37b3da824d26b8ec814/research_checks/T6_P2_V5_SIGNED_POPULATION_GAP64_EXACT_20261123.py). This present verification takes those seven cases as its declared exhaustive input.

## Complete third-tier obstruction for the seven cases

Represent a v₂=5 profile with `n` atoms by odd quotients `j_i=1+2a_i`, where the multiset of positive `a_i` is an integer partition and all remaining `a_i=0`. The mass of the profile is `31n+64 sum_i a_i`; the seven surviving input profiles and remaining mass budgets are:

| Case | Light v₂=5 atoms | Heavy extra parts | Light extra parts | Heavy v₂=4-and-lower budget | Light budget |
| ---: | ---: | --- | --- | ---: | ---: |
| 1 | 5 | () | (14,7,1,1,1) | 192 | 640 |
| 2 | 6 | () | (14,7,1,1,1) | 161 | 609 |
| 3 | 6 | (1) | (14,7,1,1,1,1) | 97 | 545 |
| 4 | 7 | () | (14,7,1,1,1) | 130 | 578 |
| 5 | 7 | () | (7,6,4,4,1,1,1) | 130 | 578 |
| 6 | 8 | () | (14,7,1,1,1) | 99 | 547 |
| 7 | 8 | () | (7,6,4,4,1,1,1) | 99 | 547 |

The heavy population is always `64+light` atoms. For each side, enumerate **all nonnegative v₂=4 multisets** `d=16j`, odd j, whose actual exponent mass `sum(16j-1)` is within its own residual budget. Retain the six-component inverse-moment signature modulo `2^(2k)` for each `k=1,...,6`. Multisets having the same six-component signature are merged by keeping only the *least mass*: the third-tier congruence depends on that signature alone, and a cheaper representative can only improve capacity to add v₂=3 terms, so this merge cannot remove a feasible completion.

Given any pair of v₂=4 signatures on opposite sides, combine them with the fixed v₂=5 profiles into `E_k=D_{5,k}+2^k D_{4,k}`, computed modulo `2^(3k)`. Reject if some `E_k` is not divisible by `2^(2k)`. Otherwise `D_{3,k}=-E_k/2^(2k) (mod2^k)` is forced.

Every possible signed v₂=3 multiset-difference signature belongs to the finite group `G` generated by
```
g(j)=(j^(-1) mod2, j^(-2) mod4, ..., j^(-6) mod64),
j odd.
```
All odd units reduce modulo 64; the 32 odd residues 1,3,...,63 generate the **entire** possible group `G`, which exhaustive BFS computes as **2,048** distinct signatures. This deliberately allows *unbounded* v₂=3 mass and hence is a valid necessary overapproximation of the actual mass-limited v₂=3 choices.

The exact checker enumerates and filters:

| Case | Distinct feasible heavy v₂=4 signatures | Light signatures | Exact v₂=4 signature pairs | Pass second-tier divisibility | Forced third-tier signature in G |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 70 | 8,988 | 629,160 | 147 | **0** |
| 2 | 43 | 6,886 | 296,098 | 55 | **0** |
| 3 | 14 | 3,868 | 54,152 | 2 | **0** |
| 4 | 25 | 5,185 | 129,625 | 12 | **0** |
| 5 | 25 | 5,185 | 129,625 | 8 | **0** |
| 6 | 14 | 3,927 | 54,978 | 2 | **0** |
| 7 | 14 | 3,927 | 54,978 | 3 | **0** |
| **Total** | | | **1,348,616** | **229** | **0** |

As each possible v₂=4 pair either fails second-tier divisibility or requires an impossible v₂=3 group signature, none of the seven 64-population-gap v₂=5 pairs can extend to equality of the six complete rational moments.

The [standalone exact Python checker](https://github.com/awdawmip/enterprise-math/blob/7143d6ea8fbda9225bba6b8ac392ab78134a8c7d/research_checks/T6_P2_V5_POPULATION_EQUALITY_THREE_TIER_20261123.py) uses nonnegative multiplicity recursion, exact modular inverses, exhaustive 2,048-element group closure, and asserted counts for all seven cases. It uses no float arithmetic, random sampling or external solvers. An independently organized local Python implementation executed the identical finite enumeration and found the same per-case counts and zero third-tier intersections. The results depend on the earlier seven-case census for input completeness, whose source is cited above.

By the earlier congruence, the only population differences are 0 or ±64; this third-tier obstruction excludes ±64, proving the stated **universal population equality at exact v₂(d)=5**.

## Remaining mathematical question and provenance

Equality of the total number of `v₂(d)=5` occurrences is now established under the model and cited higher-v₂ dependencies. The next scientifically distinct target is to determine equality of the **individual odd-quotient multiplicity vectors** at v₂=5 for populations three or higher (the previously proved equal two-atom restriction remains applicable), or alternatively to advance the largest-prime p17 valuation-one layer for the mother T6=2332 objective.

Scientific author this turn: `EM-DVR-DEBB5E`; preserve the origin and review status of every prerequisite and previous independent research result. Mathematical subunit complete; Native Result accepted=0, Native Review accepted=0, formal Task complete=0, T6 mother objective complete=0. Source/Activity formal linkage remains a separate exact-identity/DA/record-CAS operation.
