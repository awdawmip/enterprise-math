> **Prior work / scope notice (2026-11-13):** General binary rotation-word counting and the sharp `Theta(m^4)` asymptotic were established by Frid and Jamet (2014), DOI `10.1051/ita/2014019`. R128.1–R128.2 are an independent constructive derivation of a coarser bound, not a new asymptotic result. The project-specific increment is R128.3: applying an exactly generated rotation-word candidate set to R126's signed S23 feasibility system. See [LITERATURE_RECONCILIATION.md](LITERATURE_RECONCILIATION.md). The previous suggestion to improve the free-family order below `m^4` is superseded; investigate the correlated S23 subfamily instead.\n\n# R128 — Farey-sector circular-block theorem for all joint S23 Boolean signatures

Date: 2026-11-13 (Asia/Shanghai). Author-side auxiliary mathematics continuing R126 and R127; not a native X6 event permission. Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Predecessor source: R127 author-side commit `72f6de415d45fbd9a0a3bfde7aae36ccc99d0b93`.

## Exact statement

For each integer `m>=2`, let `{z}=z-floor(z)` and define the **free rotation-threshold family**

```
B_m(alpha,beta,tau)_i = 1[{alpha+i*beta}<tau],  0<=i<m,
0<=alpha,beta,tau<1.
```

Let `U_m` be the set of its attained binary words. Let `F_m` consist of all reduced fractions `p/q in (0,1)` with `2<=q<=m-1`, and put `K_m=|F_m|=sum_{q=2}^{m-1} phi(q)`. Then:

**R128.1 (finite exact enumeration).** The following algorithm produces **exactly** `U_m`: partition `(0,1)` by the points of `F_m`; choose one rational beta strictly inside every open partition interval and beta equal to each member of `F_m`; for each choice, arrange the *distinct* positions `{i*beta}` in circular order, grouping equal positions, and output the indicator masks of all circularly contiguous blocks of these groups, including the empty and full blocks. For `beta=0`, the only words are all-zero and all-one, already present.

**R128.2 (polynomial candidate bound).** For all `m>=2`,

```
|U_m| <= (2*K_m+1)*(m*(m-1)+2) = O(m^4).
```

The bound is valid for all real alpha, beta, tau in the stated domain; the enumeration and word witnesses can use only exact rationals. It is an upper bound, not an assertion that all its separately counted words are distinct.

**R128.3 (application to signed S23).** For any rational `x,l,h` with `l<h`, any integers `N,j,a,c,d`, and any `m>=2`, put `A=N-j-a`, `E=c-a` and

```
M_i(theta) = 1[{x+(A+i*d)*theta} < {E*theta}],   theta in (l,h).
```

By R126's directed-circle rotation identity, this is the signed S23 directed-half-open-arc auxiliary observer. Every attained m-bit word belongs to `U_m`, via `alpha={x+A*theta}`, `beta={d*theta}`, `tau={E*theta}`.

Thus an *exact full signature enumeration* can test only the `O(m^4)` free-rotation candidates, discarding infeasible candidates through R126's exact three-integer mixed-linear feasibility system. Reusing R121's `|P_m|=Theta(m^3)` mechanical floor-word bound, the number of fixed-three-integer ILP feasibility instances is `O(m^7)` for all attained signatures together (plus polynomial exact rational enumeration/preprocessing and output recovery). This replaces the naive `2^m*|P_m|=O(2^m*m^3)` candidate ILP count for all words. Coefficient bit sizes, exact fixed-dimensional ILP cost and output/witness recovery remain part of total complexity; no implementation of a production ILP backend is claimed here.

## Proof of R128.1

Fix beta. Let `p_i={i*beta}` be the m orbit positions on the circle `R/Z`. The inequality `{alpha+i*beta}<tau` is equivalent to `p_i` lying in the positively oriented arc `[-alpha, tau-alpha)` of length tau. A proper nonempty arc selects a cyclically contiguous block of the *distinct* occupied positions. Coincident indices cannot be separated, because their positions and indicators are identical. The cases tau=0 and a proper arc spanning all occupied positions give the empty and full blocks. Conversely, every contiguous block of position groups is selected by placing the two arc endpoints in the gaps immediately before and after the block. These gaps exist because there are finitely many distinct positions. To select all groups, put the short complementary arc entirely inside one gap; to select none choose tau=0. Rational beta has rational occupied positions, so rational gap midpoints and rational alpha,tau supply exact witnesses.

Now let beta vary. Two labeled orbit points `p_i,p_j` collide precisely when `(i-j)*beta` is an integer. For `0<=i<j<m`, every such beta in `(0,1)` is a reduced rational whose denominator is at most `j-i<=m-1`. Conversely every reduced `p/q` with `q<=m-1` is a collision of `p_0` and `p_q`. Hence the collision set is exactly `F_m`. On each connected component of `(0,1)\F_m`, all positions are distinct and their cyclic order is constant: a change of order requires a collision. Therefore a single rational midpoint beta for each component realizes precisely the same collection of circular-block indicator words as every beta in that component. At collision beta values, the exact grouped-order construction handles ties. At beta=0 all positions coincide, giving only empty/full. The union is exactly `U_m`. QED.

## Proof of R128.2 and R128.3

There are `K_m+1` open components and `K_m` collision points, hence `2*K_m+1` representative beta types. With n distinct position groups, the number of cyclically contiguous selections is at most `n(n-1)+2`: at each length 1 through n-1 choose one of n starts, plus empty/full. As n<=m, each beta type contributes at most `m(m-1)+2`. Summing yields the stated bound. Elementary counting gives `K_m<=sum_{q=2}^{m-1}(q-1)<m^2/2`; thus `|U_m|=O(m^4)`. The exact totient expression follows by counting reduced numerators for each denominator.

The substitution `alpha={x+A*theta}, beta={d*theta}, tau={E*theta}` satisfies the free family assumptions and reproduces each original bit exactly. It proves the superset property without assuming the three phases can vary independently in S23. R126 supplies exact acceptance/rejection of each candidate signature using `|P_m|` three-integer systems. Therefore testing all signatures needs at most `|U_m|*|P_m|=O(m^7)` such systems; no S23 signature is omitted and every accepted candidate has an S23 rational witness recovered by R126. QED.

## Validation and scope

`check_r128.py` performs exact Fraction-based construction of every candidate and an explicit rational witness `(alpha,beta,tau)`, verifying every witness. It reports exact universal word-set counts for `m=2..13`. It also tests 120 deterministic signed rational S23 parameter instances: for each, all affine floor-crossing, threshold-crossing and equality critical parameter points on `theta in (0,1)` are cut; every singleton cut and open cell midpoint is evaluated, so the enumeration is complete for each of those finite instances. Total sampled representatives: 27,480. Seed: 12820261113. Result: `R128_FAREY_CIRCULAR_BLOCK_PASS`. This finite test checks the implementation; the universal results above use the proof.

The polynomial bound is about the Boolean auxiliary observer and its exact rational feasibility encoding. It retains signed original coefficients, phase provenance and the S23-vs-native-X6 type boundary. This work does not modify P000, formal CLAIM, Result or review.

## Useful next question

Improve the `O(m^4)` union bound using the special arithmetic order of rotation orbits; characterize the exact sequence `|U_m|` and compare direct signature generation plus 3D ILP against R127's 2D special families. Implement an exact efficient three-dimensional integer-feasibility backend and record complete input preprocessing/witness costs.
