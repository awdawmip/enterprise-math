# BRC N=4 / S23: exactly two destructive replacement probes recover the full eleven-parameter state

Date: 2026-11-03 (Asia/Shanghai). Classification: **AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED**. Scientific input stays frozen at Enterprise Math `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This is a continuation of the global single-attenuation inverse at `ea5757d3a4e6ae8c78454df802694696e8eddcc0`. Algebraic probes below are specified observers in the frozen positive stochastic model; no native Heartbeat dynamics is asserted.

## Model and observer horizon

Let `z=(z0,...,z10)` range over the full **real** cube `[0,1]^11`. Preserve six **labeled** preparations, their ordered branch triples, and all four outcome probabilities:

```
A=(0,0,0,1,1,1), B=(2,2,3,2,2,4), C=(5,6,7,8,9,10)
R(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)).
M=((10,10,0,0,0,0), (9,11,0,0,0,0), (0,0,20,0,0,0),
   (0,0,0,10,10,0), (0,0,0,2,18,0), (0,0,0,0,0,20)).
P(z)_i=sum_{j=0}^5 M_ij R(z_Aj,z_Bj,z_Cj)/20.
```

Fix `0<beta<1`. For a subset `I` of the five upstream indices `{0,1,2,3,4}`, define `U_I(z)` by **replacing** `z_k` with `beta` for `k in I`; all other original coordinates are retained. Given a finite family `F` of such masks, the measurement is `Phi_F(z)=(P(z),(P(U_I(z)))_{I in F})`. The baseline `P(z)` is always included and is not counted as a replacement probe. No intermediate replaced value retains information about its overwritten original coordinate.

The frozen mixer is invertible: `det(M/20)=1/50`. Six unblended source rows `r_j` can be recovered from any six labeled observation rows `p_i`:

```
r0=11*p0-10*p1; r1=10*p1-9*p0; r2=p2;
r3=(9*p3-5*p4)/4; r4=(5*p4-p3)/4; r5=p5.
```

All equations apply componentwise to the four distinct outcome positions.

## Theorem 1 — exact criterion for any finite replacement family

For every fixed real `0<beta<1`, `Phi_F` is injective on **all** `[0,1]^11` if and only if the seven mask conditions below hold:

```
(M2)   some I in F has 2 notin I and (0 in I or 1 in I)
(M3)   some I in F has 0 in I and 3 notin I
(M4)   some I in F has 1 in I and 4 notin I
(C5/6) some I in F has {0,2} subset I
(C7)   some I in F has {0,3} subset I
(C8/9) some I in F has {1,2} subset I
(C10)  some I in F has {1,4} subset I.
```

**Sufficiency: constructive inverse.** Recover `z0,z1` from the first coordinate of raw source rows `r0,r3` in the baseline. For `k in {2,3,4}`, choose a witness mask from (Mk) and a raw source `j` with `B_j=k`, upstream `A_j in I`, but `k notin I`. Its second outcome is `(1-beta) z_k`; hence `z_k=r_j[1]/(1-beta)`. For each third-gate coordinate `z_Cj`, use a witness mask with `{A_j,B_j} subset I`. Its third outcome is `(1-beta)^2 z_Cj`; hence `z_Cj=r_j[2]/(1-beta)^2`. These formulas reconstruct each of the eleven original coordinates for every real input, including every boundary degeneracy.

**Necessity: explicit indistinguishable pairs.** Start from the state having all five root/middle coordinates `z0,...,z4=1` and all six downstream coordinates `z5,...,z10=0`. Failure of (M2), (M3), or (M4) means that replacing the corresponding `z_k` by `0` leaves the baseline and every selected probe invariant: any source carrying that parameter either stops at an unchanged root `1` or overwrites the parameter itself. Failure of a (C*) condition means that changing its indicated downstream coordinate from `0` to `1` is unobservable: in every selected probe at least one upstream branch gate remains `1`, so its third-gate branch is never reached. These are exact pairs of distinct states with identical **all six source-labeled probability rows** under `Phi_F`. Thus all seven conditions are necessary.

## Theorem 2 — minimum two probes and classification of all optimal families

No single constant-replacement probe suffices globally: (C5/6) requires a mask containing `2`, whereas (M2) requires a mask excluding `2`. Hence at least **two additional probes** are needed beyond baseline.

Up to exchange of the two masks, the **only** size-two families satisfying Theorem 1 are

```
I={0,1} union S,
J={0,1,2} union ({3,4} minus S),   S subset {3,4}.
```

There are exactly four unordered pairs. Encoding masks by the five-bit integer `sum(2^k for k in I)`, they are `(3,31)`, `(7,27)`, `(11,23)`, `(15,19)`.

**Proof of completeness.** (M2) forces a probe omitting `2`, while (C5/6) and (C8/9) force a probe containing `2` together with `0` and a probe containing `2` together with `1`. With only two probes, both downstream requirements must be met by the *same* second probe `J`, so `{0,1,2} subset J`; the other `I` omits `2`. The pair of conditions (M3) and (C7) forces `0` into both masks and `3` into exactly one. Similarly (M4) and (C10) forces `1` into both masks and `4` into exactly one. This gives precisely the four displayed choices. The constructive inverse establishes that all four work. QED.

## Theorem 3 — quantitative inverse stability

Let `d_F(z,w)` be the largest total-variation distance between matching labeled rows in the baseline and the two selected probes, where `TV(p,q)=sum_k |p_k-q_k|/2`. Put `epsilon=||z-w||_infinity`. For any of the four optimal families and any `0<beta<1`,

```
       (1-beta)^2 * epsilon/21  <= d_F(z,w) <= 3*epsilon.
```

In particular, at `beta=1/2`, `epsilon/84 <= d_F(z,w) <= 3*epsilon` on the **complete real eleven-dimensional cube**.

**Proof.** The source-unmixing equations and TV triangle inequality give a maximum raw-row TV separation `rho <= 21*d_F` (maximum inverse-mixer row absolute sum = `21`). Difference in any single outcome-event probability is at most its row TV. The inverse formulas give root-coordinate error at most `rho`, middle-coordinate error at most `rho/(1-beta)`, and downstream-coordinate error at most `rho/(1-beta)^2`. Thus `epsilon <= 21*d_F/(1-beta)^2`. For the upper bound, couple the ordered three binary decisions in each raw source; their categorical output mismatch probability is at most the sum of differences of the three gate probabilities, each bounded by `epsilon`. Positive mixing is TV-nonexpansive, so `d_F<=3 epsilon`. The displayed constants are constructive bounds; sharpness is a separate question. QED.

## Relation to the predecessor and information preservation

The previous `A_lambda` probe scales five root/middle coordinates by `lambda` and keeps their original values recoverable, giving a **single** globally injective observation. The present constant-overwrite operation erases values at its overwritten coordinates, and the exact two-probe theorem specifies how to recover them from a complementary view. Both results use the complete labeled source rows and explicit future-observer horizons. The baseline alone has nontrivial observation fibers at boundary states.

This proof is specific to the frozen positive-probability six-source S23 realization and these algebraic replacement operations. The branch and provenance axes are kept distinct; no quotient of native BRC signed/phase/carry state is taken.

## Executed exact verification and next question

`VERIFY.py` uses Python standard-library `fractions.Fraction`; no floats, external solver or sampling-based proof are involved. It checked all 32 single masks, all 528 unordered two-mask families, constructed and re-observed an exact indistinguishable witness for each of the 524 rejected pairs, inverted every one of the 2048 binary eleven-dimensional corners for all four successful pairs (8192 checks), inverted 160 deterministic rational states per successful family (640 checks), and tested 320 exact TV stability pairs. The all-real claims are established by Theorems 1–3; finite checks test the formulas and exhaustive mask enumeration.

Next: determine sharp inverse stability constants for the four optimal families at `beta=1/2`, investigate the tradeoff between number of overwritten gates, number of probes and worst-case conditioning, and connect the certified observer horizon to joint-source decoder optimization without erasing future-relevant branch information. Preserve native claim/owner/independent-review status as separate controls.
