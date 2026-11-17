# X6 Unit90 — named-triad gauge compatibility and four-STAR boundary

Date: 2026-11-17. State: **AUTHOR-EXACT / FINITE-EXECUTED / SOURCE-CALL-SITE-INSPECTED / UNREVIEWED / NOT_ADMITTED**. This is independently reproducible *author science*, not Native semantic PROGRESS, a Result, an accepted theorem or a P000 modification.

Parent: `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Canonical Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; immutable publication `TP2-B4A441B23DA3159232C2`. Frozen spatial input pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical corpus `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Native signed BRC kernel original blob `300a96e3dc24bf6fff73743037a0347a8bc83176`. All calculations are on the *raw named six-axis signed chart*, not nonnegative final Cell addresses or an independent lower-dimensional native world.

## Actual current source consumers

Two frozen/current executable families use distinct named triadic signed-permutation generators. Both are correct within their own original declared construction, but an exact chart bridge must not silently identify them.

1. `experiments/x6_triadic_rotation_v1_20260906/check_triadic_rotation.py` blob `c446d0327f9bf643d5796348ba46cafe96d2915d`, lines 44–50 (also `experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py`, blob `d5f6dfcfd0dedbe46feae3bc1b227185af417c2f`, lines 43–46) defines `q_triad` on sorted axes `i<j<k` by `q(e_i)=-e_j, q(e_j)=-e_k, q(e_k)=-e_i`.
2. `research_checks/20261112_x6_star_triad_group_brc_convolution.py` blob `50cccf09b5dd83cc592ba36db5bc9e14941ce0ce`, lines 20 and 30–33, defines `triad_generator` by `g(e_i)=+e_j, g(e_j)=+e_k, g(e_k)=-e_i`. Its actual carrier STAR set (zero-based axis labels) is `(0,2,5), (0,3,4), (1,2,4), (1,3,5)`.

The remaining three axes are fixed in both generators. Both have order six, and their cubes reverse the three selected signs. Same order/cube or an abstract group-size report is **not** a certificate of global signed-axis chart equivalence.

## Exact theorem: one triad and all 20

Let `D_s(e_a)=s_a e_a` for one fixed global `s in {±1}^6`. This is the explicitly scoped **named-axis-preserving diagonal sign-gauge language**. For every selected triad `i<j<k`, direct evaluation on the three named basis vectors yields

```text
D_s g_ijk D_s^{-1} = q_ijk
  iff s_i s_j = -1, s_j s_k = -1, s_k s_i = +1
  iff s_i = s_k = -s_j.
```

Every individual triad admits exactly `2 * 2^3 = 16` such gauges among 64 (2 signs for the connected triple, 2 choices for each untouched axis).

There is **no** single global `D_s` conjugating all 20 generators simultaneously. Already the pair `(0,1,2)`, `(0,2,3)` is incompatible: the first requires `s_0=s_2`, the second requires `s_0=-s_2`. Hence this conclusion needs no appeal to a large finite census. An exact enumeration of all 64 sign assignments gives the number of matched triads per gauge:

| Number of individually matched triads | 0 | 4 | 6 | 8 |
|---|---:|---:|---:|---:|
| Number of global gauges | 12 | 12 | 24 | 16 |

The maximum is 8 of 20. For all `C(20,2)=190` unordered pairs of triad types, the number of common gauges is 0 for 30 pairs, 4 for 100 pairs, and 8 for 60 pairs.

**Scope of negative finding:** This rules out a single globally defined *diagonal sign gauge fixing all named-axis labels*. It does not rule out every possible axis permutation, context-specific gauge, abstract group isomorphism or larger port/provenance-preserving representation.

## Positive theorem: the four FCC STAR generators *are* jointly compatible

For the exact four STAR choices actually consumed in `20261112_x6_star_triad_group_brc_convolution.py`, the equations have precisely two global solutions:

```text
s = (+1,+1,-1,-1,+1,+1)
s = (-1,-1,+1,+1,-1,-1).
```

The number of matched STAR triads per sign gauge has distribution `{0:18, 1:32, 2:12, 4:2}`. Thus the complete four-STAR generator set shares one global conjugacy map, even though all 20 named triads do not.

For either displayed sign assignment and **any ordered word** `w=t_L...t_1` of those four STAR generators, the algebraic identity extends without length limit:

`D_s (g_{t_L}...g_{t_1}) D_s^{-1} = q_{t_L}...q_{t_1}`.

The checker also verifies every one of `1+4+16+64=85` STAR words of lengths 0–3 exactly. The all-length theorem follows from conjugation being a homomorphism, not from extrapolating the finite test.

This exact signed permutation is an algebraic bridge **after transporting all signed letter labels**. Consequently the signed raw native `sum |z_a|` and `sum z_a^2` are invariant and the positive BRC endpoint/path counts are carried bijectively for correspondingly transformed endpoints and words. That does not identify the original `q` and `g` programs at *identical untransformed signed endpoints*, nor prove physical event-time serialization, original 160-event triadic closure, or native force equilibrium.

## Sharp observer boundary: min-zero quotient does not descend

For `rho(z)=z-min(z)*1`, the nonuniform sign gauge has `D_s 1` not proportional to `1`. The pair `z=0`, `z'=1=(1,1,1,1,1,1)` has `rho(z)=rho(z')=0` but `rho(D_s z)=0` whereas `rho(D_s z')` contains both 0 and 2. Therefore no function `F` on min-zero relative states can satisfy `rho(D_s z)=F(rho(z))` for all signed native states. This is a rigorous **fiber-constancy counterexample**, not merely a componentwise formula mismatch.

A lossless transport retains the common depth `h=min(z)` alongside `rho(z)`, reconstructs `z=rho(z)+h*1`, applies `D_s`, and computes the desired observer afterward. If future operations require native Cell identity, additionally preserve the signed native chart and actual operation provenance.

## Reproducible exact certificate and sources

Checker: `research_checks/X6_UNIT90_NAMED_TRIAD_GAUGE_COMPATIBILITY_CHECK_20261117.py`. Machine-readable summary: `research_checks/X6_UNIT90_NAMED_TRIAD_GAUGE_COMPATIBILITY_RESULTS_20261117.json`. Independent exact integer enumeration covers 64 sign gauges, 20 generators, 190 triad pairs, 85 STAR words, and 729 test displacements for native `G,T` invariance. It checks the analytic two-triad impossibility and the observer fiber witness. The local equivalent checker was executed with ordinary CPython, `-O` and `-OO`, with identical output; the meaningful `assert` verification was run in ordinary mode. Original R063/Helly native benchmarks **not reexecuted**.

Sources retain frozen blob refs; current repository HEAD may have unrelated concurrent advances. The raw sextuple basis vectors and signs are computational representatives and must not be silently promoted to the project nonnegative final address interface.

## Parent-objective disposition and exact continuation

Unit89 established a typed terminal-displacement bridge between 160 triadic event types and constrained primitive 3-block paths. Unit90 instead resolves a *previously unverified named-generator interoperability question* at real consumer call sites: four-STAR global signed-gauge transport works, full-20 global signed-gauge transport fails, and min-zero observer erasure is unsafe. These facts enable more precise 28-LP consumer auditing without accusing correct callers.

No invalid current consumer line was established by this pass. LP011/LP019 purported **historical** erroneous calls remain `UNRESOLVED_PROVENANCE`; earlier source/line discovery or independent Driver `REQUEST_REVISION` must distinguish a real current error from a merely nonfactorizing interface. Formal Native Units77–90 PROGRESS and author Activity association require original X6 owner-authorized path. Researcher SID/CLAIM/RUN from historical provenance are **not** a current capability receipt; this artifact is neutral author evidence, `UNREVIEWED / NOT_ADMITTED`.

Next executable scientific action: inspect the **actual call chain** from the 4-STAR `triad_generator` into signed native `endpoint_multiplicity`, `CoverState`, min-zero observers and 20-triad consumers, and test whether named-axis `D_s` and its `(rho,h)` repair are explicitly applied at any conversion. If no conversion exists, preserve that negative bounded audit; do not patch correct code just to produce a fix. Continue the remaining 28-LP exact consumer/source issue and independent Driver review. The original hourly task settings and notification behavior are untouched.
