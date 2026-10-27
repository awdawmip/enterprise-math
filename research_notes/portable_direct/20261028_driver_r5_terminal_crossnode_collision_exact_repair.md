# R5 parametric fan-in: exceptional terminal LR collision and exact observer repair

2026-10-28 (Asia/Taipei). **NONBLIND / SOURCE-EXPOSED / PORTABLE MATHEMATICAL AUDIT / UNREVIEWED / NOT_ADMITTED.** This is *not* a native Driver Review, Reference, Synthesis, Follow-up, Result, Research-Activity, CLAIM, independent clean-blind decision or task publication.

## Sources, attribution and scope

- Original author's exact two-parameter eight-leaf theorem: `research_notes/brc_r5_parametric_fanin_phase_transition_20261028_r11/PROOF.md` introduced at `b4f5102fedd6eb9df7a43b1bd328d2a0ef7a5350`, including Bellman proof of the signed support gap for `lambda=(20,10,-2,3)`; original authorship and status unchanged.
- Its deterministic checker `research_notes/brc_r5_parametric_fanin_phase_transition_20261028_r11/VERIFY.py` explicitly assumes that different t2 nodes have disjoint t3 ratios, an assertion tested only on the author's chosen rational parameter grid.
- This note isolates an interior parameter value not covered by that checker and proves why it does *not* change the published signed-support conclusion. It preserves the original mother's open equal-hull/unequal-image problem.
- All probability measures and the observer `O=(P[declare Q], Q[declare P], E_P[tau], E_Q[tau])` are the **external finite decision-tree model**, not P000's native X6 dynamical state. Keep exact positive P/Q mass and history/leaf provenance until the terminal repair has been proved.

## Exceptional cross-node terminal collision

Retain the exact original parameter domain `0<alpha<1/2`, `3/5<beta<1`. At t3 the leaf likelihood ratios are

```
AU: 1-alpha, 1+alpha            (1/2,1) and (1,3/2)
AV: 1/4, 1/4
BU: 1-beta, 1+beta             (0,2/5) and (8/5,2)
BV: 2, 2
```

The only cross-**t2-node** t3 collision inside this domain occurs exactly at `beta=3/4`, where `BU0` and both `AV` terminal leaves have the *same* terminal signature `(t=3,R=1/4)`. The already identified t2 collision `AU/BU` at `(t=2,R=1)` remains. The author's terminal-disjointness assertion is therefore not a universally valid enumeration precondition for the full open parameter rectangle. This does **not** falsify the author's algebraic Bellman theorem.

## Exact repair for the four-dimensional observer

For arbitrary local behavioral policies, let `w_h>=0` be the Q mass reaching a terminal history `h` with identical `(t=3,R=r)`, after all upstream (possibly randomized) decisions; let `theta_h` be the probability of declaring Q at that terminal history. When `W=sum_h w_h>0`, replace the history-specific decisions by the *single* ratio-based probability

```
theta_star = (sum_h w_h theta_h) / W.
```

When `W=0`, the choice is immaterial. Since all these terminal histories share the same `R=r` and stopping time `tau=3`, their four coordinates are

```
e_P = r * sum_h(w_h theta_h),
e_Q = sum_h(w_h (1-theta_h)),
T_P = 3r * sum_h w_h,
T_Q = 3 * sum_h w_h.
```

Pooling leaves every coordinate exactly unchanged. The shared probability is fixed by the upstream policy, not by a persistent shared random seed or knowledge of the hidden history. Therefore the terminal collision at `beta=3/4` can be repaired **without changing the actual four-dimensional behavioral observation image**, for every `alpha` in the stated open interval and for arbitrary real behavioral parameters. This is an exact application of the previously known terminal-collision repair principle, not a novel claim that terminal histories are independently observable.

Example with both relevant routes reached: `w_AV=1/3`, `w_BU0=1/8`. The fictitious separate terminal decisions `AV:Q`, `BU0:P` are replaced by the common Q-declaration probability `8/11`. Both yield exactly
```
(e_P,e_Q,T_P,T_Q) = (1/12,1/8,11/32,11/8).
```

## Independent exact arithmetic at the exceptional parameter

For `alpha=1/10, beta=3/4`, the five distinct terminal LR signatures are `1/4, 9/10, 11/10, 7/4, 2`. An independent standard-library `fractions.Fraction` program enumerated all `3^5 * 2^5=7776` deterministic *global signature assignment descriptions*: choices for roots A/B, shared t2 AU/BU gate, separate t2 AV/BV gates, and the five truly distinct terminal LR gates. Their observations reduce to **324 distinct four-coordinate vectors**.

For the original signed direction `lambda=(20,10,-2,3)`, exact support minima are

```
V_full = 233/24;
V_seedless-LR = 79/8 = 237/24;
V_seedless-LR - V_full = 1/6.
```

Thus the author's positive-gap conclusion survives this missing deterministic-enumerator boundary case. The full-history minimum here was recomputed from the exact independent per-node Bellman minima, retaining both optional t1 stopping actions; the compressed minimum came from *valid* LR assignments that enforce the terminal collision. Multi-affinity of finite behavioral strategies implies that deterministic global policies suffice for a linear support minimum; the separate terminal-pooling argument establishes the stronger actual-observation repair.

Reproduction: `research_notes/portable_direct/20261028_driver_r5_terminal_crossnode_collision_exact_repair.py` (stdlib only; exact fractions). Local executable output: `valid_seedless_deterministic_points=324`, `full_history_min=233/24`, `seedless_min=79/8`, `support_gap=1/6`, `terminal_common_Q_probability=8/11`.

## Precise consequence and next action

Do not promote the original R5 author proof or this audit as an admitted theorem merely from finite checking. The original parametric support formula remains compatible with the exceptional terminal collision; any future finite enumerator claiming **full-domain four-dimensional policy coverage** must identify actual `(time,LR)` equivalence classes *at the chosen parameters*, or prove an exact terminal-repair reduction before treating terminal decisions separately. This matters particularly when distinguishing convex hulls from nonconvex behavioral observation images.

No new V2 successor Task is published here: the mother target still needs a separate strictly positive tree with an all-signed hull-equality certificate and a genuine all-real behavioral-image separation, if one exists. Independently credentialed native Driver review must use the exact frozen Result/review set and current DA; this source-exposed check creates neither authority nor a new review entry.

Author-level note writer: current source-exposed Driver automation conversation; do not confer independence by renaming the logical session.
