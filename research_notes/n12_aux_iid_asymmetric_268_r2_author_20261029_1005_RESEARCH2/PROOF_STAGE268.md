# Stage268 — exact adjacent Bellman face across L5–L6 (external ternary IID, N=12)

Date: 2026-10-29. Portable author identity: `EM-R2-268-20261029-1005-LOCAL` (locally assigned, not Source issued). Scientific predecessor: Stage267 at immutable commit `fc0571e84e783d334433970ca3358acd1a7a3b63`, Draft PR #1571. Evidence grade: **AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**. This is a theorem for an external IID auxiliary decision model, not a native P000 six-dimensional Heartbeat/Cell theorem.

## Frozen sources and authority
GLOBAL_KNOWLEDGE_V1 `main@4235656a960a3d2261c9681749b6de3c2a401708` and Enterprise Math `main@1cc7e0320a6bdef2d956d4140d41d18af4f77390` were remotely verified by connected main-ref reads. Consulted the global bootstrap/manual, project router, TASK_RESEARCH role, P000 original and startup projection (same original Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`), ACTIVE worldview, EM AGENTS, portable research and automation protocols. The native service reports `research_authority_granted=false`, `CODE_REVIEW_REQUIRED`, active jobs 5/5; owner inventory returned `CONTROL_QUOTA`, hence active owner unverified. No Source claim, native Result, review, or protected-state publication is asserted.

## Exact model and statement
Alphabet `{0,1,2}` with strictly positive IID laws `P=(1/8,1/24,5/6)`, `Q=(1/12,1/12,5/6)`; observe at most `N=12` symbols. Every randomized full ordered-history policy may stop to declare P or Q, or continue before N. Write `eP=P(declare Q)`, `eQ=Q(declare P)`, `tP=E_P[T]`, `tQ=E_Q[T]`. For all real caps `a,b in [0,1]`, define `V12(a,b)=min max(tP,tQ)` over feasible policies `eP<=a,eQ<=b`, and infinity if infeasible.
At the Stage268 exterior caps `a268=134248354729/1761205026816`, `b268=215912422795/278628139008`, the exact global optimum is **`V12(a268,b268)=66742910965/11609505792`**, approximately 5.748988127555947.

Set exact dual multipliers `lambdaP=203678720/1502937`, `lambdaQ=12317244/166993`, `thetaP=0`, `thetaQ=1` and root `H=567931401748091045/7754824802893824`. Define four full `(eP,eQ,tP,tQ)` vectors (only the first two coordinates form the cap face):

```
L5=(378878551937/5283615080448,146176716655/185752092672,
    27566628769787/5944066965504,254184258235/46438023168)
L6=(15836509331/195689447424,424845849965/557256278016,
    10156836789929/1981355655168,280280958235/46438023168)
W =(378877764437/5283615080448,146176760405/185752092672,
    27566635857287/5944066965504,254184389485/46438023168)
Z =(47509440493/587068342272,424845981215/557256278016,
    10156839152429/1981355655168,280281089485/46438023168)
```

**Full-real iff theorem:** For every real `(a,b) in [0,1]^2`, `V12(a,b)=H−lambdaP*a−lambdaQ*b` **if and only if** `(a,b)` belongs to `R268=conv(L5,L6,Z,W)` (using cap coordinates). It is a strictly convex nondegenerate parallelogram; its exact area is **`11415537109375/7667519984894950244352`**. It shares the entire `L5—L6` boundary with Stage267 `R267=conv(J5,J6,L6,L5)` and their interiors are disjoint.

## Bellman lower bound, exact verification and proof
For a *single ordered prefix* with counts `s=(i,j,k)`, define `p_s=(1/8)^i(1/24)^j(5/6)^k`, `q_s=(1/12)^(i+j)(5/6)^k`. The exact (unnormalized) backward recurrence is `B_s=min{lambdaQ*q_s,lambdaP*p_s,q_s+sum_{l=0}^2 B_(s+e_l)}` for `i+j+k<12`; at depth 12 omit the continue action. These respectively represent stop-P, stop-Q, and continue. The quotient by counts is mathematically exact for these four observables because the IID transition laws, continuation cost, and terminal costs depend on the ordered prefix only through counts; induction on remaining horizon proves the relation for every ordered history, without requiring history-blind policies.

All 455 possible count states and all 1274 legal action costs were recomputed using standard-library `fractions.Fraction` in the attached executable. There are exactly 817 strictly positive action gaps, with minimum **`311687/1985235149540818944`**, and exactly two ties: `T1=(0,0,5): stop P=continue` and `T2=(3,3,5): stop Q=continue`. Every other action is strictly suboptimal for this exact dual. Root Bellman value equals H. Backward induction yields, for *every* ordered-history randomized policy, `lambdaP*eP+lambdaQ*eQ+tQ >= H`. Therefore every feasible policy has `max(tP,tQ) >= H−lambdaP*a−lambdaQ*b` because both multipliers are positive.

To characterize equality for all histories, note that T1 is the unique five-neutral ordered prefix, whereas each optimal tie-corner policy has **exactly 21** reached ordered prefixes of counts T2. An exact reachability check from T1 with continue and all forced intervening minimizers shows T2 is unreachable from that ancestor: trajectories encounter a forced stop or increase the neutral count beyond five. Thus T1's decision cannot change any T2 prefix's reach or mass. All 21 T2 prefixes have identical P and Q likelihoods and identical optimal suffix increments. A full-history policy may set distinct continuation probabilities at these 21 histories, but its four-observer effect depends only on their average `u in [0,1]`; T1 has an independent continuation probability `r in [0,1]`. Every Bellman-equal policy therefore has exactly `Obs(r,u)=L5+r*(L6-L5)+u*(W-L5)` and `Z-L6=W-L5` in **all four observer coordinates**. No additional full-history degrees of freedom enlarge the cap face.

The four deterministic policies giving L5,L6,W,Z all satisfy `tQ>tP` and `lambdaP*eP+lambdaQ*eQ+tQ=H`. Every affine mixture has the same strict time ordering. Positive multipliers force `eP=a,eQ=b` at any policy attaining the dual bound. Conversely every cap pair in R268 arises by a Bellman-minimizing mixture and has `max(tP,tQ)=tQ=H−lambdaP*a−lambdaQ*b`. A cap outside R268 cannot attain equality because no Bellman-equal policy has both errors equal to those caps. Finite-horizon policies form a compact set of probability kernels (equivalently finite randomizations over complete deterministic history policies); error and time maps are continuous. Every feasible minimum is attained, so no limiting nonattainment creates exterior equality. This proves the full-real iff.

## Exact primal witness and area/adjacency
Randomize over complete deterministic policies with weights `49/100 L5 + 49/100 L6 + 1/50 W`. The exact four-observer tuple is

```
(134248354729/1761205026816,
 215912422795/278628139008,
 3221058988393/660451885056,
 66742910965/11609505792)
```
Its errors exactly equal (a268,b268) and `tQ−tP=5182839518543/5944066965504>0`. Its tQ matches the global lower bound H−lambdaP*a−lambdaQ*b, proving the exact optimum. The positive mixture weights place the cap pair strictly in R268's interior. `orient(L5,L6,W)=-11415537109375/7667519984894950244352`, while the old Stage267 vertex `J5=(555154589/7739670528,3425906045/4353564672)` lies on the opposite side, giving exact complete-edge adjacency and disjoint interiors.

## Reproducible evidence and BRC boundary
`STAGE268_EXACT_FACE.py` is the exact executed Python source, with executable assertions for the Bellman optimum, all legal action gaps/ties, four policies, source-ordered path masses, all observer coordinates, the full affine area, witness, and next point. Its independent second observer traverses **4786 actual ordered history nodes and 3192 terminal branches** across the four policies. Each deterministic policy has exact terminating P mass 1 and Q mass 1, and matches a separate integer count-state multiplicity propagation in all four observers. A fifth independent ordered DFS over the Stage269 exterior witness has 1216 nodes / 811 terminal branches, both source masses exactly 1. The actual saved program stdout contains `STAGE268_EXACT_ALL_REAL_FACE_PASS`. BRC-inspired positive rational source-mass and ordered-branch multiplicity fidelity are used only within this finite IID observer model. Native P000 X6 transfer would additionally require explicit native slice/third-coordinate semantics, six-axis path provenance, relation preservation and readout/update correspondence; no such native theorem is claimed.

## Stage269 successor (new feasible exterior point)
Modify the W policy only at reached count `(4,4,0)` (one ordered prefix) from stop-Q to continue. The independent full-history tuple becomes

```
U=(6062044228643/84537841287168,1754121124943/2229025112064,
   441066173811605/95105071448064,1016737558471/185752092672)
```
Mix `49/100 W + 49/100 Z + 1/50 U`. Its exact error caps are `a269=107398477982417/1408964021452800`, `b269=28788331614361/37150418534400`, with `tQ=53394354497531/9287604633600>tP`. Thus this is a **feasible exact upper bound** for Stage269, not yet the optimum. Relative to the new W—Z boundary the cap orientation is `−19967037875/2944327674199660893831168`, while L5 is on the positive side; Stage268 dual slack for U is `228242371/124077196846301184>0`. Next: compute an exact primal-dual optimum, determine the adjacent all-real region or obstruction, and independently verify P/Q full histories. Full input in `NEXT_TASK_PACKET_269.md`.

Evidence class: author exact/independent review pending. GitHub publication and remote content readback are reported in the run receipt, not inferred from this proof.
