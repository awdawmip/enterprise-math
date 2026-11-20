# X6 时间动力学：带符号三元端口的 S6 轨道与未来观察者最小状态
Date: 2026-11-21. Task `RS-X6-NATIVE-TIME-DYNAMICS`, publication `TP2-91D4A7C2F63805BE21A3`, parent `PO-X6-UPPER-STRUCTURE-20260906`.
Research lane: `chatgpt-research-onhour-enterprise-math-20260923`; original author `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`.
Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Frozen boundary
Taskbook: `f41c2690daba467ecbde99615a1337e67be46ffd:research_tasks/RS_X6_NATIVE_TIME_DYNAMICS_20260906.md`. P000: `a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json` and `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`. Same pin: `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`. Native signed axes, the unsigned S6 axis-permutation skeleton and primitive triadic closure are prescribed. The concrete admissible Cell/Link/Port triadic incidence and physical transition remain open.

This theorem studies an **explicit conditional port-incidence model**, not a new physical closure axiom. Let D consist of unordered triples of three **distinct** axes with individual signs ±1; the three quanta are equal magnitude. There are C(6,3)2^3=160 candidate signed triples. An indicator I(q) is a permitted-port query, not automatically an admitted physical `TRIADIC_CLOSURE_E`. Only the S6 skeleton, which permutes axes **without changing signs**, is used.

## Theorem 1 — all bare S6-covariant triad predicates
Two q in D are in the same S6 orbit iff they have the same number r of positive signs. Orbit sizes for r=0,1,2,3 are respectively **20,60,60,20**. Proof: the image of a distinct-axis signed triad is specified by a 3-subset of 6 indices and the choice of r positive positions, giving C(6,3)C(3,r). A permutation realizes any such choice.

Consequently an S6-invariant scalar predicate I:D→{0,1} is constant on each of these four orbits; there are exactly **2^4=16** invariant laws (15 nonempty). A rule that admits exactly one +++ triad while rejecting another +++ triad cannot be an invariant predicate on bare signed-axis labels. Selective incidence requires a carried incidence field, additional frame/port datum, or explicitly reduced symmetry. This classification is of the stated candidate family only.

## Theorem 2 — sharp frame compression for a marked triadic-port observer
Fix a single marked signed triad q_*∈D with r positive signs. An S6 frame σ answers the local query q by
`O_q(σ)=1 iff σ·q=q_*`.
Allowed future operations: any finite sequence of right frame rotations σ→σh, with h∈S6, and any signed-triad membership query. There are **no Cell-step queries** in this observer.

Then
`σ ~ τ iff σ^{-1}q_* = τ^{-1}q_*`.

Sufficiency: the local preimage m=σ^{-1}q_* completely determines all current answers. After right rotation h, it updates by `m→h^{-1}m`; hence future answers remain equal. Necessity: if the two preimages differ, the query q equal to the first preimage distinguishes them immediately.

The stabilizer of q_* permutes r marked positive axes, (3-r) marked negative axes, and three unused axes; it has size r!(3-r)!3!. Therefore the exact number of future-distinguishable frame states is
`N_r=720/[r!(3-r)!3!]=20*C(3,r)`,
and optimal fixed-length memory is `ceil(log2 N_r)`: **5 bits** for r=0,3 and **6 bits** for r=1,2. This is an explicit, deterministic Markov quotient with transition `m→h^{-1}m`. For unrestricted future signed-Cell-axis-step observations, the previously proved S6 frame quotient requires **720 states / 10 bits**; those observations change the observer contract and invalidate this 5/6-bit reduction.

## Exact counterexample and time semantics
With 0-based indices, q1={(0,+),(1,+),(2,+)} and q2={(0,+),(1,+),(3,+)} have the same r=3. The sign-count projection merges them. Yet future membership query q=q1 yields 1 for singleton mark {q1}, and 0 for mark {q2}. Thus an invariant *scalar law* and a transported *selective relation field* are different objects; preserving ordered local frame rotations and the mark m is necessary for the latter observer.

Physical Cell coordinate, ordered BRC paths, trivalent incidence field, time-event order and precision/root address remain separate typed carriers. The model gives a reusable finite-state frame/guard interface but does not declare an admissible P000 physical transition, and does not replace any native R063 benchmark.

## Reproducible exact enumeration
Independent Python enumeration checks the whole 720-element group, all 160 candidate signed triples, 16 invariant laws and representative future-rotation transitions:
- 1,843,200 predicate/rotation checks;
- 460,800 local-triad query checks;
- 8,640 representative right-rotation equivariance checks;
- **0 inconsistencies**.
Files: `research_checks/X6_TIME_SIGNED_TRIAD_S6_PORT_OBSERVER_REPRO_20261121_0500.py`, `research_checks/X6_TIME_SIGNED_TRIAD_S6_PORT_OBSERVER_RESULTS_20261121_0500.json`. General proof uses orbit-stabilizer and exact future-observer distinguishability, not an empirical extrapolation.

## Evidence debt and next exact action
Determine from a **specific admitted, pinned** native Cell/Link/Port source whether physical triad incidence is invariant as a scalar or transported as an internal field, and evaluate its actual time-ordered event guards and post-rotation future observers. Without such a law, the present result remains a conditional signed-triad port unit. Source-backed native PROGRESS for this unit, Activity record, and independent Driver review each require their own valid process and acknowledgments. Preserve original Research session/claim/run and request IDs; never use maintenance conversation identity. Consume prior guard/trace, S6 Cell-step and Viète clock results without rerunning them.
