# R5 — source-blind LR diamond: observer-quotient no-go

Status: **NONBLIND / AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING** (2026-10-29, Asia/Taipei). This is a portable mathematical derivation, **not** a native Driver Review, reference pass, frozen Result, official Task or Foundation admission.

## Source and provenance

- Enterprise Math immutable read: `main@ebcfc85472afef35901c0f0dd858b81365786787`.
- Prior author note: `research_notes/brc_r5_tree_polytope_diamond_20261029_t0140/RESEARCH.md`, Git blob `71539e75d446f5edc58136d6ea9aab25f7f68816`.
- P000 / GLOBAL_KNOWLEDGE_V1 separately frozen at `7b33f8066e9993e7c941959a9d738ed405248eb8`. The finite external statistical model makes no native Heartbeat/X6 claim.
- The earlier R5 author note was visible to the present derivation: **no clean-blind independence**.

## Theorem (all-real behavioral strategies)

Consider the following finite two-measure likelihood-ratio stopping model. Hidden initial origins `i` have fixed Q masses `a_i` and common observed root LR `r`. A root-continue kernel `mu_i` has two possibly nonterminal time-2 observed LR children `L,R`; other children terminate. From `L,R`, the origin-dependent kernels `nu_(i,L),nu_(i,R)` lead at time 3 to terminal cells except for one **merged** nonterminal observed LR state `s*`, reachable from both parents. Continuing at `s*` uses the **same source- and history-independent final Q kernel `eta`** for every incoming history and all time-4 children terminate. These are fixed action-independent kernels; every P transition is determined from Q by the child-LR/parent-LR ratio and is normalized. Forced early terminal origins are allowed.

A seedless LR policy chooses behavioral actions with fresh coins depending only on `(time,LR)`, without persistent randomness; terminal declarations also depend only on `(time,LR)`. Observe

`O=(P(declare Q), Q(declare P), E_P[tau], E_Q[tau])`.

**Claim:** The exact seedless-LR image `O_LR` is a compact **convex polytope**. Consequently,

`conv(O_full) = conv(O_LR) => O_full = O_LR`.

In particular, this entire **source-blind postmerge one-diamond** subclass cannot witness equal full/LR four-observer convex hulls with unequal actual images, even when source-resolved merge flow is rank two and nonconvex. The theorem does **not** say the full and LR hulls are equal in any specific model, and does not cover origin-dependent final kernels or further mergers.

## Proof

Let `a` be the probability of root continuation and `p,q` the **unconditional prefix continuation fractions** at the two time-2 LR children. Actual behavioral coins are `a`, `p/a`, `q/a` (zero convention), so precisely

```
0 <= a <= 1; 0 <= p <= a; 0 <= q <= a.
```

Write the fixed Q incoming coefficients at the merge as

`V = sum_i a_i mu_i(L) nu_(i,L)(s*)`,
`W = sum_i a_i mu_i(R) nu_(i,R)(s*)`.

The total Q mass reaching `s*` is `x=Vp+Wq`. The common continuation coin `gamma` sends the **aggregate** Q flow `z=gamma*x` to time 4. Since the continued kernel `eta` is source-blind, all terminal Q cell masses depend only on `(a,p,q,z)`. Replace the product `gamma*x` with the **linear constraints**

```
0 <= z <= Vp+Wq.
```

Conversely every feasible quadruple `(a,p,q,z)` is realized by a genuine seedless LR behavioral policy, choosing `gamma=z/(Vp+Wq)` for positive denominator, or zero otherwise. This is **not** a convex outer relaxation.

Indeed each observed terminal Q cell mass `M_(t,s)` is affine: root stops use `1-a`; time-2 stops/forced terminals use `a-p`, `a-q` or `a`; time-3 nonmerged terminals use `p,q`; the merged stop cell has mass `Vp+Wq-z`; and time-4 Q cells have mass `z*eta(s)`. Other forced-terminal histories add fixed constants.

Introduce aggregate terminal joint Q mass `m_(t,s)` declaring P. A single terminal LR coin `theta=m/M` implements **every** feasible `0 <= m_(t,s) <= M_(t,s)`, with the zero convention when `M=0`. Since every terminal cell of observed LR `s` has P mass `s M_(t,s)`, the four observables are linear:

```
e_P = 1 - sum_(t,s) s*m_(t,s)
e_Q = sum_(t,s) m_(t,s)
T_P = sum_(t,s) t*s*M_(t,s)
T_Q = sum_(t,s) t*M_(t,s).
```

The exact feasible region for `(a,p,q,z,m)` is a bounded closed polyhedron and the observer image is its linear projection, hence a compact convex polytope. Finally `O_LR subset O_full`, so `conv(O_full)=conv(O_LR)=O_LR` implies `O_full=O_LR`. QED.

This is an **all-real constructive proof**; the exact-rational check merely verifies arithmetic.

## Source-rank-two midpoint, erased by observer quotient

For the exact rational two-origin kernels in the cited preceding R5 note, use signatures `S=(1/2,1,3/2,5/2)` and the **same** final `eta=(1/8,1/4,3/8,1/4)` for both origins. The two incoming source vectors at the merged LR `3/2` are

`v=(11/1200,23/3600)`, `w=(1/40,1/100)`, with `det(v,w)=-49/720000`.

The source-level policies `F:(p,q,gamma)=(1,0,1)` and `G:(0,1,0)` yield `(x,y)=(v,v)` and `(w,0)`; their source-flow midpoint `((v+w)/2,v/2)` violates the shared-gamma collinearity invariant by exactly `-49/2880000`. Thus the **hidden-origin** flow image is nonconvex.

Nevertheless, the actual **LR policy**

```
H: p=1/2, q=1/2,
gamma=(v_A+v_B)/(v_A+v_B+w_A+w_B)=4/13
```

reproduces **the exact midpoint terminal (time,LR) Q mass in every cell** and therefore P masses too. Given any terminal declarations by F and G, choose `m_H=(m_F+m_G)/2` and `theta_H=m_H/M_H`, which realizes their exact four-observer midpoint. The hidden-source continued vector of H is *not* the infeasible hidden-source midpoint, but its aggregate is identical.

With F terminal-P coin `(t+j)/12` and G coin `(2t+j)/13`, signature index `j=1..4`, the checker obtains

```
O_F = (13513/21600, 523/1800, 1109/600, 2863/1800)
O_G = (9539/20800, 857/2080, 173/80, 71/40)
O_H = (608891/1123200, 65761/187200, 4813/2400, 3029/1800)
    = (O_F+O_G)/2  exactly.
```

`VERIFY.py` reconstructs both laws with standard-library `Fraction`, checks means and all terminal mass coordinates, validates this midpoint and **240 additional exact rational mixtures** including root-stopping variation. Tests are regression evidence, not a substitute for the all-real proof; output in `EXACT_OUTPUT.json`.

## Research consequence / next exact action

The previous rank-two diamond with common `eta` is **not** a promising R5 nonconvex-four-observer witness. Preserve its valid source-resolved wedge, but the quotient erases it. A discriminating next model must let the continuation from the merged LR state retain **origin/history dependence** in a kernel compatible with the observed LR and likelihood-ratio martingale, or introduce another observer-relevant merging interaction. Preserve positive rational masses; compare **all signed** full/LR support functions first, then test actual-image separation. This is a **candidate research direction, not a formally published successor**.

Control boundary at this proof: Site gateway `static_machine_readonly`, `write_relay_enabled=false`, no source-issued Driver session/DA. The original CBRC-F7 frozen Result has a separate independent-review obligation. This PR does not create or satisfy that obligation.
