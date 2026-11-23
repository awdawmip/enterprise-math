# R762KP — Exact second-largest Port–Euler source fiber and parity-sensitive geometric transition

Date: 2026-11-24 (Asia/Shanghai). Status: AUTHOR_ANALYTIC_PROOF_WITH_EXACT_FINITE_CERTIFICATE / NOT_REVIEWED.

## Scientific lineage and scope

This work continues [R762KO](https://github.com/awdawmip/enterprise-math/blob/bb90f0a9fba5cd42714983b39f7f02ba177be6b8/research_notes/portable_direct/R762KO_ODD_UNIFORM_MAXIMIZER_THEOREM.md) and the group-algebra fiber formula of [R762KN](https://github.com/awdawmip/enterprise-math/blob/2ca3fe1ff671a44a1ec4ed4cb90653870a7ddaf7/research_notes/portable_direct/R762KN_M3_ARBITRARY_MULTIPLICITY_FIBER_THEOREM.md). It preserves the parent scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389 and all relevant P000/ACTIVE worldview premises.

The object is the **unsigned auxiliary M3 composite Port–Euler model** with three inactive pair-Ports 01,23,45. It is not a signed native TRIADIC_CLOSURE_E, a time-ordered BRC branch theory, or an accepted Foundation theorem.

The 12 active Ports are indexed in order 02,03,04,05,12,13,14,15,24,25,34,35 (bits 0 to 11). Forced-support boundaries generate a 512-element, rank-nine GF(2) subspace F. Eight flexible supports indexed by (i,j,k) in {0,1} cubed each admit three two-Port edge boundaries e_s1,e_s2,e_s3 whose XOR is zero. An individual flexible support contributes an **unordered edge-type multiset** of cardinality m.

For m=2r, the count of local assignments with zero boundary is A=(r+1)(r+2)/2, and the count with any specified nonzero edge boundary is B=r(r+1)/2. For m=2r+1, these are A=r(r+1)/2 and B=(r+1)(r+2)/2 respectively.

Let Q_m(b) denote the number of **connected** assignments with flexible parity b in F. KO.1 established that b=0 uniquely maximizes Q_m for all integers m>=2. We determine the second-largest value, its exact formula, and all its maximizing boundary locations.

## Theorem KP.1 (exact runner-up)

If **m=3**, the second-largest fiber is **64,800**, attained precisely at three nonzero boundaries

    51, 204, 3840.

Each boundary is the full four-vertex set of exactly one of the three forced-component Port grids; the other two grids are empty. The gap from Q_3(0)=71,197 is 6,397.

If **m=2 or any integer m>=4**, the second-largest fiber is attained precisely at these twelve nonzero boundaries:

    3,12,17,34,48,68,136,192,768,1280,2560,3072.

They each select two adjacent vertices (one row or column) in one four-vertex Port grid and leave the other grids empty.

With A=A_m, B=B_m, the exact runner-up value in this second case is

    S_m = 6 B^8 + 8 A B^7 + 6 A^2 B^6
          + 8 A^3 B^5 + 2 A^4 B^4 + 2 A^6 B^2.

By subtracting the KO.2 exact zero-fiber formula, the **sharp first-to-second gap** for m=2 or m>=4 is

    Q_m(0)-S_m
      = A^8 - 2 A^6 B^2 + 4 A^4 B^4 - 8 A^3 B^5
        + 10 A^2 B^6 - 8 A B^7 + 3 B^8 - 3.

In the parameter t=A/B this equals

    B^8 (t-1)^2 (t^2+1) (t^4+2t^3-2t+3) - 3.

These formulas are exact over the stated integer multiplicity domain, not fitted asymptotics.

## Proof: finite symbolic classification with exact sign certificates

In the GF(2) group algebra, let

    p_b(t)=[X^b] PROD_s (t+X^e_s1+X^e_s2+X^e_s3).

The forced components are internally connected; the only three disconnected flexible choices are the monochromatic quotient-edge configurations. Their total multiplicity is 8m (even), so all have parity zero. Consequently

    Q_m(b)=B^8 p_b(A/B) - 3 * indicator(b=0).

Direct multiplication of the eight linear factors over the 12-bit GF(2) boundary group gives exactly **19 distinct coefficient polynomials** on all 512 b in F, including b=0. The two candidate nonzero classes have

    p_3(t)  = 6+8t+6t^2+8t^3+2t^4+2t^6,
    p_51(t) = 8+16t^2+8t^4.

The full classes represented by 3 and 51 contain, respectively, the twelve adjacent-pair boundaries and the three full-grid boundaries listed above.

For every nonzero class except the one represented by 3, the difference p_3(t)-p_b(t) is divisible by (t-1)^2. Let q_b(t) denote the quotient. The attached exact Python source independently reconstructs all Port vectors, all 512 forced boundaries, and the complete group-algebra polynomial map, and confirms by integer coefficient identity that each quotient has degree <=6.

Its sign certificates are the degree-six Bernstein coefficients of q_b, calculated in exact rational arithmetic, separately on intervals [1/2,1] and [1,3]. All coefficients are nonnegative; all are strictly positive in 16 of the 17 competitor classes. The remaining class, represented by boundary 18, has

    q_18(t) = 2(t-1)^2(t+1)^2,

which is strictly positive for t != 1. Thus p_3(t)>p_b(t) for all competing nonzero classes throughout [1/2,3], except at t=1.

The complete certificate table is below. Each row gives (class representative, class multiplicity, minimum degree-six Bernstein coefficient on [1/2,1], minimum on [1,3]).

| Representative | Multiplicity | Min left | Min right |
|---:|---:|---:|---:|
| 15 | 6 | 9/2 | 8 |
| 18 | 6 | 0 | 0 |
| 29 | 48 | 27/8 | 8 |
| 51 | 3 | 5/8 | 8 |
| 60 | 6 | 9/8 | 8 |
| 63 | 72 | 45/8 | 16 |
| 85 | 12 | 37/16 | 8 |
| 86 | 36 | 45/16 | 8 |
| 255 | 3 | 77/8 | 24 |
| 783 | 36 | 63/8 | 16 |
| 831 | 12 | 85/8 | 24 |
| 839 | 112 | 27/4 | 16 |
| 857 | 16 | 67/8 | 16 |
| 874 | 16 | 41/8 | 16 |
| 887 | 96 | 81/8 | 24 |
| 1023 | 18 | 117/8 | 32 |
| 4095 | 1 | 149/8 | 40 |

For even multiplicity m=2r>=2, t=(r+2)/r lies in (1,3]. For odd m=2r+1>=5, t=r/(r+2) lies in [1/2,1). Every one of these integer cases therefore has the **unique nonzero maximizing class** p_3, with its twelve boundaries. Substituting A/B into p_3 proves the formula for S_m. Combining it with KO.2 proves the sharp gap expression.

The sole remaining integer m>=2 is m=3, with t=1/3. The attached exact algorithm evaluates **all 512** coefficient polynomials with integer weights A=1,B=3. The largest value among b!=0 is exactly 64800, attained only for b=51,204,3840. Exhaustiveness follows because the eight-factor group-algebra multiplication accounts for every legal local boundary choice once with its exact multiset multiplicity, and F contains every possible forced parity boundary. This proves both cases.

## Geometric crossover

The two relevant class polynomials satisfy the exact identity

    p_3(t)-p_51(t)
      =2(t-1)^2(t^2+1)(t^2+2t-1).

The nontrivial positive crossing is t=sqrt(2)-1. Of the admissible integer uniform multiplicities, only m=3 lies strictly between 0 and this threshold. Every m=2 or m>=4 has t larger than this threshold. The algebra thus identifies a precise **parity-sensitive finite-scale transition** in the source-fiber ordering.

| m | Q_m(0) | Second fiber | Its maximizing nonzero boundaries | Exact gap |
|---:|---:|---:|---:|---:|
| 2 | 7,197 | 1,920 | 12 adjacent pairs | 5,277 |
| 3 | 71,197 | 64,800 | 3 full grids | 6,397 |
| 4 | 2,788,422 | 1,771,470 | 12 adjacent pairs | 1,016,952 |
| 5 | 22,471,422 | 21,257,640 | 12 adjacent pairs | 1,213,782 |
| 12 | 2,511,291,435,622 | 2,415,163,378,950 | 12 adjacent pairs | 96,128,056,672 |

The m=1 case is excluded: t=0 and the zero boundary is not the global maximum (Q_1(0)=6 versus nonzero maximum 8).

## Exact verification, source fidelity, and continuation

Reproducer: [R762KP_SECOND_FIBER_VERIFY.py](R762KP_SECOND_FIBER_VERIFY.py), using only the Python standard library. It reconstructs all 512 forced parity targets, all 19 polynomial classes, 17 exact Bernstein certificates, the isolated m=3 maximizers, and integer regressions for m=1..12. The sign proof is parameter-uniform for all integer m>=2; the 12 regression cases are additional checks rather than its foundation.

BRC relevance: an observer that retains only support inventory, forced parity and connectivity identifies distinct unordered edge-source multisets within fibers. The theorem supplies exact leading and runner-up fiber sizes, candidate provenance-residual geometry and sharp separation. No signed native evolution, time-ordered provenance transport, Cell/Link/Port dynamics or observer-factorization law is claimed from this auxiliary result.

**Next questions:** obtain a small structural classification of the *third and lower* fiber orders and their crossings; build an optimal composable provenance rank/unrank representation with a declared future-operation family; then test a fully typed signed TRIADIC_CLOSURE_E and ordered BRC lift.

**Control boundary:** scientific authorship here is current-turn derivation with local exact verification; predecessor files retain their historical authorship. Independent review NOT_REVIEWED. GitHub branch/PR preservation does not imply Result acceptance, shared CLAIM/RUN or Foundation admission.
