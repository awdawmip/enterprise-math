# X6 R151 — exact irredundant six-direction BRC bridge atlas

Date: 2026-11-24 (Asia/Shanghai). Status: AUTHOR ANALYTIC PROOF / EXACT FRACTION CROSSCHECK PASS; independent mathematical review NOT_REVIEWED. Formal Result/Review NOT_SUBMITTED.

## Immutable model and scope

Continue R150 at `enterprise-math@3b274f1bacca95c8eee2fe4188e46a9515666527:research_notes/portable_direct/2026-11-23_r2_x6_r150_complete_six_near_support.md`. Scientific input pins **unchanged**: R121 at `8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd` and R122 at `0687aa24f5402da3b35f914dd6907967a9805b94`. P000 V5 and the ACTIVE six-native-axis Heartbeat worldview are preserved. This is a **conditional static centered-three-axis, six-pair BRC observer** theorem; `(x,y,z)` is a restricted three-axis slice of X6, not native physical time, a complete Cell address, a residual attribution, or a claim about six-dimensional rotations.

For each nonzero integer triple `v=(x,y,z)` with `q(v)=max(sum positive entries,sum absolute negative entries)<=10`, identify only v and -v (not integer multiples). There are precisely 1,935 unoriented vectors. With
`h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z)`, use all six absolute pair gaps `g(v)=(|h1-h0|,|h2-h0|,|h3-h0|,|h2-h1|,|h3-h1|,|h3-h2|)`.
For positive weights `(136,B,176,D)`, set capacities `s=(136+B,312,136+D,B+176,B+D,176+D)`, `F_v=max_i g_i(v)/s_i`, `eta=min_v F_v`, and **strict** near-set `N={v:F_v<3 eta/2}`.

R150 already proves for all B>=20,D>=528 that the complete near-set belongs to six vectors. Denote them (different from weight symbols):

```text
A=(1,0,0)    gaps=(1,3,7,2,6,4)
J=(4,-1,0)   gaps=(1,0,11,1,12,11)
C=(5,-4,1)   gaps=(1,3,5,2,6,8)
K=(5,-1,0)   gaps=(2,3,4,1,6,7)
E=(6,-4,1)   gaps=(0,0,12,0,12,12)
H=(9,-5,1)   gaps=(0,3,6,3,6,3)
```

## R151 theorem — irredundant exact member conditions

On the **entire open-in-B, half-open-in-D bridge strip**
```text
20 < B < 136,       528 <= D < 1872-B                         (R)
```
define
```text
T_E(B) = min(704+3B, 832-B),
T_H(B) = 528+2B       when 20<B<=32,
         1056+5B     when 32<B<136.
```
Then, for **every real B,D satisfying (R)**, the complete strict Port-10 near-set is exactly

```text
N(B,D) =
  ({A,C} if D<1584+8B else {})
  union ({K} if D<1224+8B else {})
  union ({H} if D<T_H(B) else {})
  union ({J,E} if D>T_E(B) else {}).
```

No other Port-10 direction enters. Every equality in the displayed predicates is excluded for the corresponding direction(s). In particular, J and E are **inseparable strict-near members** throughout (R), joining together across a lower envelope of two affine walls. Near counts attained in (R) are 2,3,4,5,6.

**Nontrivial phase change at B=32.** For 20<B<=32, H exits at `D=528+2B` *before* J/E enter at `D=T_E`. For 32<B<136, J/E enter *before* H exits at `D=1056+5B`. At the exact B=32 and D=1000, H has `F_H=3/208=(3/2)(1/104)=(3/2)eta` and is excluded; at every sufficiently small B>32 with D=1000 it is included. This equality-sensitive boundary is not a sampling artifact.

## Analytic proof

1. **Exact score reduction.** Throughout (R), the six fixed gap vectors give

```text
F_A=max(1/104, 7/(D+136), 2/(B+176), 6/(B+D)),
F_K=max(2/(B+136),1/104,6/(B+D),7/(D+176)),
F_H=3/(B+176),
F_J=F_E=12/(B+D).
```
The J=E identity follows by checking the remaining four gap ratios of J against `12/(B+D)`: `D<1872-B<1632+11B` (since B>20), and `D>=528, B<136` control the D-dependent terms. Further, `F_A<=F_C`, because `7/(D+136)<=8/(D+176)` for D>=528, and each other A gap term is bounded by a corresponding C gap term or its larger sixth term. When D>=656, both have the same simplified score `max(1/104,2/(B+176),6/(B+D))`.

2. **A and C membership.** Monotonicity gives `F_A<=F_A(20,528)=3/274 < 3/(2*104)`; each of K and H has score at least `1/104`, and C>=A. Thus A needs comparison only with J/E. Precisely `F_A < 18/(B+D)` holds iff `D<1584+8B` within (R); the constant `1/104` term is strict since B+D<1872, and the other terms are automatically strict. For D>=656, C=A. For 528<=D<=656, every W6 candidate has score >=1/104 and `F_C<=F_C(20,528)=1/88<3/208`, so C is unconditionally near. Since D<1584+8B automatically there, C has exactly the same stated membership as A.

3. **K membership.** Monotonicity gives `F_K<=F_K(20,528)=1/78<3/208`, whereas A,C,H have scores >=1/104. Hence K only needs comparison with J/E. Its four-term maximum obeys `F_K<18/(B+D)` iff `D<1224+8B` in (R), proving its indicator.

4. **H membership.** Since `F_K>=2/(B+136)`, `F_H=3/(B+176)<(3/2)F_K`; comparison to C is redundant because C>=A. H vs J/E gives `D<1056+5B`. H vs A requires `2/(B+176)<F_A`; for B>32 this holds strictly from `1/104`, while for 20<B<=32 it is equivalent to `D<528+2B` (the possible third-gap threshold `D<480+7B/2` is weaker there). The two bounds combine to the piecewise `T_H` above.

5. **Simultaneous J/E entry.** Since `F_J=F_E=12/(B+D)`, each is strict-near exactly when `8/(B+D)<F_A,F_C,F_K,F_H`. It is enough to test A,K,H because C>=A. The inequalities reduce to

```text
against A: D>min(704+3B,832-B),
against K: D>min(544+3B,832-B),
against H: D>(5B+1408)/3.
```
For 20<B<136, the first threshold is at least the other two (at the B=32 crossing the equality is consistent). Thus only `D>T_E(B)` remains.

R150's complete 1,935-integer-direction exclusion theorem ensures that no outsider could be missing from these six membership tests. All transformations above use exact rational inequalities with positive denominators; they establish the theorem over **all real** parameters in (R), not just the verification samples.

## Exact independent replay and state

Companion standalone Python stdlib `Fraction` verifier: `research_notes/portable_direct/x6_r151_bridge_exact_atlas_verify.py`. Actually executed on 2026-11-24 with 1,935-vector full enumeration at **464 rational (B,D) configurations** including every relevant equality wall, both sides of B=32 and B=72, lower edge and rational off-boundary cases. Result:

```text
R151 EXACT BRIDGE SIX-DIRECTION ATLAS PASS
population 1935 full-exact-cases 464 counts_observed {2: 12, 3: 50, 4: 162, 5: 137, 6: 103}
B=32 equality and B=32+ jump, all threshold equalities checked by Fraction
```

These samples crosscheck the analytic proof; the all-real claim depends on the exact R150 finite-support theorem plus the score inequalities, not on extrapolation from samples.

**Unresolved/review:** independent mathematics review NOT_REVIEWED; canonical X6 native dynamics not addressed; formal task ownership and Result/Review are separate. **Next:** connect the `D=1872-B` boundary and its post-strip optimizer/membership to the known R147/R148 high-D tail; examine whether a unified positive-quadrant atlas admits a smaller globally irredundant chamber decomposition. Preserve R121/R122 science pins and P000.
