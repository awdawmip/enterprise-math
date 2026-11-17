# EC49FSD — Exact eight-phase q140 discount diagram with q32 and q34 half-price

**Scientific status:** AUTHOR_PROVED / EXACT_FINITE_BELLMAN_CROSSCHECKED / NOT_REVIEWED  
**Date:** 2026-11-18 (Asia/Shanghai)  
**Frozen science:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`  
**Parent:** EC49FSC partial three-price section, [PR #2672](https://github.com/awdawmip/enterprise-math/pull/2672), immutable parent commit `dfce1bfb1338c73f446fabeebdb390745cd2daac`. This is independent portable research; it does not assert a formal Task/CLAIM/Result/Review.

## Exact model

Use the original BRC class-16943 data: 141 **named** profile states derived from 310 original configurations, all 228 **physically named** native observation response vectors decoded from the frozen 94-family master. No observer quotient or factor-only replacement is used. All complete adaptive deterministic trees are admissible; each leaf must uniquely identify its named profile. The prior is uniform on the 141 profile states (not multiplicity-weighted over the 310 configurations). Let `t>0` be the base price, and set prices `q32=t/2`, `q34=t/2`, `q140=(1-z)t`, others `t`, for any real `z∈[0,1]`. Denote `F(z)=141V(z)/t`.

For a full tree `Q`, let `U(Q)` be the total number of observation calls summed over all 141 state paths, and `N_q(Q)` the number of those calls using named observation `q`. Then

```
A(Q) = U(Q) - (N32(Q)+N34(Q))/2
K(Q) = N140(Q)
F_Q(z) = A(Q) - K(Q)*z.
```

## Theorem — full real interval, eight affine phases

For every real `z∈[0,1]`, the unrestricted global optimum over all admissible complete original-native adaptive trees is

```text
0       <= z <= 1/6    : F(z) = 215   - 10 z
1/6     <= z <= 3/14   : F(z) = 217   - 22 z
3/14    <= z <= 1/4    : F(z) = 437/2 - 29 z
1/4     <= z <= 11/30  : F(z) = 219   - 31 z
11/30   <= z <= 2/5    : F(z) = 449/2 - 46 z
2/5     <= z <= 1/2    : F(z) = 453/2 - 51 z
1/2     <= z <= 33/64  : F(z) = 479/2 - 77 z
33/64   <= z <= 1      : F(z) = 545/2 -141 z
```

The exact interior phase walls are `1/6, 3/14, 1/4, 11/30, 2/5, 1/2, 33/64`. One complete tree realizes each row on its full interval. Eight *cost-vector types* are necessary and sufficient for a universal fixed-tree optimal menu: all eight slopes are distinct on nonempty open intervals. This is a minimality statement for cost-vector types, not a claim that each is the unique physical tree.

### Exact Bellman endpoint certificates

| z | Global F(z) | independently recomputed exact Bellman states |
|---:|---:|---:|
| 0 | 215 | 9,884 |
| 1/6 | 640/3 | 9,857 |
| 3/14 | 1486/7 | 9,839 |
| 1/4 | 845/4 | 9,788 |
| 11/30 | 6229/30 | 9,736 |
| 2/5 | 2061/10 | 9,707 |
| 1/2 | 201 | 9,486 |
| 33/64 | 12787/64 | 9,471 |
| 1 | 263/2 | 6,441 |

Nine endpoints were recomputed using a **separate** decoder of the full original 94-family BRC raw source and a separately implemented integer Bellman program retaining all 228 named observation IDs. All nine values matched the primary exact solver.

### Complete witness statistics

Each listed tuple is `(U,N32,N34,N140)`. For the eight phases, respectively:

| Phase | witness cost vector | first named observation | worst path length |
|---:|---|---:|---:|
| 1 | (306,41,141,10) | q34 | 4 |
| 2 | (308,41,141,22) | q34 | 4 |
| 3 | (305,32,141,29) | q34 | 3 |
| 4 | (312,45,141,31) | q34 | 4 |
| 5 | (309,28,141,46) | q34 | 3 |
| 6 | (311,28,141,51) | q34 | 3 |
| 7 | (315,10,141,77) | q34 | 3 |
| 8 | (321,18,79,141) | q140 | 3 |

All eight native decision trees were checked against **all 141 named profiles** by following their exact original response values to the correct unique leaf. The witness checker rejects repeating the same observation along a path. All named IDs and response partitions were retained.

## Proof

For each non-singleton subset `S` of the 141 original states, the optimal integer-scaled Bellman value is

```
D(S) = min over all 228 original named q that split S of
       |S| price(q) + sum over nonsingleton response fibers C⊊S of D(C).
D(singleton) = 0.
```

Every effective split makes the state subset strictly smaller, so exact recursion terminates. Every admissible complete adaptive decision tree begins with one such split, and induction on `|S|` proves Bellman gives its *unrestricted* global minimum, including zero prices at `z=1`. The two implementations each evaluate the full root domain with exact rational or denominator-cleared integer arithmetic. Their respective nine endpoint optima are tabulated above.

For every fixed admissible tree `Q`, `F_Q(z)=A(Q)-zK(Q)` is affine, hence `F(z)=min_Q F_Q(z)` is concave. On every listed closed interval `[u,v]`, the corresponding explicitly replayed complete tree has affine cost `L(z)`, and exact Bellman endpoint checks give `F(u)=L(u)` and `F(v)=L(v)`. Concavity implies `F(z)≥(1-θ)F(u)+θF(v)=L(z)` for `z=(1-θ)u+θv`, while the admissible witness gives `F(z)≤L(z)`. Thus `F(z)=L(z)` for **every real z** throughout each segment.

On each nonempty interior phase interval the displayed line is strictly below its neighboring cost-type lines. Its distinct slope `-K` is therefore necessary for any fixed-tree finite menu optimal on the entire interval, proving the lower bound of eight cost types. The eight explicit trees prove sufficiency. QED.

## Provenance, reproducibility, outstanding work

- Exact frozen input in the complete local evidence archive from the preceding run: `frozen_original_master.txt` SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e` and `EC49FPG_PROFILE.csv` SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. Original full package is inherited from EC49FSC and contains all native observation families.
- The newly archived `EC49FSD_COMPLETE_HALF_SLICE.py` resumes 13 **previously saved exact** anchors, checks their full tree paths and cost arithmetic, obtains two new exact anchors, and proves eight exact segments from nine certified corners. `EC49FSD_INDEPENDENT_VERIFY.py` independently recomputes all nine corners from separately decoded raw observation data. Machine outputs `ec49fsd_runs/CERTIFICATE.json` and `INDEPENDENT_BELLMAN_ENDPOINTS.json` record their exact values.
- This proof is author-verified, computationally crosschecked, and awaits independent mathematical review. It establishes the `a=b=1/2` **one-parameter section** of the three-observer price cube; the full `(a,b,z)∈[0,1]^3` optimal policy complex remains open.

**Next discriminating problem:** move `a=b` away from `1/2` and compute exact continuation/bifurcation of the `z=1/6` and `z=33/64` walls, retaining q32/q34/q140 observer identities. Determine whether the resulting two-dimensional section still admits a bounded finite affine menu.