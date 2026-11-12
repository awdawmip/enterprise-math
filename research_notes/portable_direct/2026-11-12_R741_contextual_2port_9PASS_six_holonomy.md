# R741 — Source-conditioned two-port BRC coding, nine-PASS six-holonomy fiber, exact census

Date: 2026-11-12 (Asia/Shanghai). Author-side exact constructive theorem and integer checker; independent review pending.

Parent Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; immutable publication TP2-8B7E13C5904A2D6F1142. Frozen scientific inputs: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5, primitive triadic balance and signed X6 Cell torsor). Auxiliary V29 count grammar: awdawmip/enterprise-math@30fb16d39465708fd1b54c70a58d06ad20f310f8:research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md. Exact A/B networks, rooted generator loops and five certified-triad inventory follow R739, immutable source commit d0d37ca56ef32c5772cd7566c0826ff060d45f25 (Draft PR #2140). R740/PR #2142 is a separate X6 edge-current observer construction; the present work changes the source-aware V29 encoding interface.

## Model and assumptions

The fixed X6 Cell C has five distinctly sourced, nonzero equal-quantum signed-axis force tokens. For every selected active triad S in the five-member closure inventory, the existence of a correctly typed TRIADIC_CLOSURE_E(C;S) incidence witness is an explicit premise, as in R739. The sixth spatial axis remains present. At each instant precisely three force tokens are active. The active triad, previous vertex, source-slot frame, BRC provenance and declared codebook are retained. On an allowed directed triad transition S>T, emit one genuine off-diagonal V29 PASS and update S and its V17 slots using a **declared guarded coupling** that requires the target incidence witness. This force-triad update is a candidate decorated law, not an automatically authorized primitive of V29; the PASS count event itself remains exactly V29. Port labels are distinct from native spatial axes.

Use two local ports, with F=PASS(C;0->1) and R=PASS(C;1->0). The terminal nonnegative V29 matrix has offdiagonal entries M01=#F and M10=#R; Rin=Rout=0.

Rooted 3-arc generator loops (their V17 holonomies are I, P and Q, with P,Q distinct transpositions):

| Carrier | I | P | Q |
|---|---|---|---|
| A | 012>014>013>012 | 012>023>013>012 | 012>023>123>012 |
| B | 012>123>124>012 | 012>023>013>012 | 012>123>013>012 |

Each carrier has fifteen selected arcs inside the original 60-arc triad universe, but the union of these three rooted loops uses exactly seven directed arcs. R739's disjoint first/last nonroot-vertex property allows every concatenation of generator loops, including cyclic seams, without backtracking.

## Theorem 1 — Sharp source-conditioned coding

For a finite directed graph with maximum outdegree Δ+, an online decoder retaining the current source vertex admits an injective fixed-length ℓ offdiagonal PASS word for each outgoing arc on r local ports if and only if [r(r-1)]^ℓ ≥ Δ+. Necessity follows from counting distinguishable words at a maximally branching source; sufficiency follows by assigning distinct symbols per source and reusing them at different sources. This is an observer-scoped coding result: the source vertex is already in the dynamic state.

Both seven-arc generator unions have Δ+=2. Thus r=2 and ℓ=1 is sharp in this class: one port has no offdiagonal PASS, and an emitted arc requires a nonempty event word. Both full fifteen-arc carriers have Δ+=3, so they require r=3 for one PASS per arc or r=2 with fixed length at least two. R731b's prior global context-free bound [r(r-1)]^ℓ≥15 applies to a different decoder that must identify the arc without its source context.

Here are the explicit one-PASS-per-arc codebooks. At each common source, outgoing symbols are pairwise distinct.

| A arc | PASS | B arc | PASS |
|---|---|---|---|
| 012>014 | F | 012>023 | F |
| 012>023 | R | 012>123 | R |
| 013>012 | R | 013>012 | R |
| 014>013 | R | 023>013 | R |
| 023>013 | F | 123>013 | F |
| 023>123 | R | 123>124 | R |
| 123>012 | F | 124>012 | F |

Consequently A's generator codewords are I=FRR, P=RFR, Q=RRF; B's are I=RRF, P=FRR, Q=RFR. Each contains exactly one F and two R.

## Theorem 2 — Complete count erasure, all k

For **every** k≥0 and **every** generator word W∈{I,P,Q}^k, in either carrier,

\[
M(W)=\begin{pmatrix}0&k\\2k&0\end{pmatrix},\qquad
R_{\mathrm{in}}=R_{\mathrm{out}}=0,\qquad \Delta\Gamma=3k.
\]

Indeed, each legal root-return generator supplies precisely one F and two R increments; PASS counts add independently of event order. All 3^k distinct positive-BRC generator histories therefore share one final native count ledger. Any derived V29 observer (u,Ω) is likewise equal on that fiber. The ordered source/V17 holonomy retains distinctions lost by M.

## Theorem 3 — Sharp nine-PASS six-way observer fiber

The following six three-generator words all end at root triad 012 with the **identical** native matrix M=[[0,3],[6,0]], after nine genuine offdiagonal PASS events:

| Word | Relative group element | Named V17 relation A | Named V17 relation B |
|---|---|---|---|
| III | I | 012 | 012 |
| IIP | P | 021 | 021 |
| IIQ | Q | 102 | 210 |
| IPQ | PQ | 201 | 120 |
| IQP | QP | 120 | 201 |
| PQP | PQP | 210 | 102 |

The six results exhaust S3. Zero/one generator produces at most three relations; with two generators, possible products belong to {I,P,Q,PQ,QP}, which omits the third transposition PQP. Hence **three generators/nine PASS events are the first complete six-state fiber in this exact rooted-generator class**. Prepending I^(k-3) to the six witnesses shows that for every k≥3 all six terminal named relations coexist at M=[[0,k],[2k,0]].

**Sharp terminal observer repair.** Holding fixed the carrier, starting/ending root, k and terminal M, with M as the only observed terminal dynamic statistic, an extra register must have at least six values to reconstruct the named relation on this fiber. Six suffice by retaining the S3 element, equivalently a threefold rotation residual and one parity bit. R732/R735's three-state repair used a richer *full directed-edge count* observer which also determines parity. The present two-port terminal ledger loses that parity: III and IIP already have identical M but opposite permutation parity.

This minimality is about repairing *the specified terminal M observer*; it does not require the full stateful scheduler to discard its known current source, frame or event history.

## Theorem 4 — Exact six-state census and all-length mixing on one fixed M

Let a_k(g) count the k-generator words with final relation g∈S3. These are precisely the positive branch counts at the single common native M fiber. Write r=PQ, t=PQP and s=(-1)^k. For every integer k≥1,

\[
a_k(I)=\frac{3^k+s+2^{k+1}}6,\qquad
a_k(P)=a_k(Q)=\frac{3^k-s+2^k}6,
\]
\[
a_k(r)=a_k(r^{-1})=\frac{3^k+s-2^k}6,\qquad
a_k(t)=\frac{3^k-s-2^{k+1}}6.
\]

At k=0 only the identity history is present.

**Proof.** The exact positive branch-count element of the S3 group algebra is A=I+P+Q, and a_k(g) is the coefficient of g in A^k. The trivial representation maps A to 3 and the sign representation maps A to -1. In the standard two-dimensional representation ρ, two distinct transpositions act as reflections with product a rotation of order three; ρ(P)+ρ(Q) has eigenvalues +1 and -1. Hence ρ(A)=Id+ρ(P)+ρ(Q) has eigenvalues 2 and 0, so ρ(A)^k=2^(k-1)ρ(A) for k≥1. Finite-group Fourier inversion gives
\[
a_k(g)=\frac{3^k+\operatorname{sgn}(g)(-1)^k
+2^k[\chi(g^{-1})+\chi(g^{-1}P)+\chi(g^{-1}Q)]}{6},
\]
where the standard character is χ(I)=2, χ(transposition)=0, χ(3-cycle)=-1. Evaluating the six cases gives the displayed integers. This proves the formula for every k without extrapolation from finite tests.

| k | M01,M10 | I | each P,Q | each r,r^-1 | t | sum |
|---:|---|---:|---:|---:|---:|---:|
| 1 | 1,2 | 1 | 1 | 0 | 0 | 3 |
| 2 | 2,4 | 3 | 2 | 1 | 0 | 9 |
| 3 | 3,6 | 7 | 6 | 3 | 2 | 27 |
| 4 | 4,8 | 19 | 16 | 11 | 8 | 81 |
| 5 | 5,10 | 51 | 46 | 35 | 30 | 243 |

For μ_k(g)=a_k(g)/3^k and uniform U(g)=1/6, the **exact** total-variation distance for k≥1 is
\[
\|\mu_k-U\|_{\mathrm{TV}}=
\frac{2^{k+2}-(-1)^k}{6\,3^k}
=\frac23\left(\frac23\right)^k-\frac{(-1)^k}{6\,3^k}.
\]
Indeed the deviations for I,P,Q are positive and those for r,r^{-1},t negative; summing either side gives the formula. Thus uniform generator choices mix on a *fixed terminal V29 ledger* with explicit exponential scale (2/3)^k.

## S6 rotation skeleton, validation and next scientific unit

For σ∈S6, rotate the Cell's signed-axis labels, all five force-source tokens, closure-incidence witnesses, active triad and slot frame, **and transport the codebook** by (S>T)↦(σS>σT) while preserving F/R as separate port types. This action commutes with each guarded PASS+V17 update. It is exact S6 axis-permutation covariance of the *structured candidate law*, not a claim of a completed full native rotation dynamics.

The companion Python standard-library program rebuilds the 60 potential triad arcs and both original 15-arc bitmasks, validates the seven selected arcs, two-port local injectivity, all nine two-generator seams, exact slot names and matrices for each of the 3^k histories for k=0..8, formulas for all those k, the total-variation identity through k=20, and all 720 covariant codebook relabelings for both carriers. Output marker: R741_TWO_PORT_CONTEXT_SIX_STATE_PASS. Exact arithmetic only. The algebraic proofs above justify all nonnegative k.

The smallest unresolved **native** step remains event admissibility: specify a true permitted X6 Cell/Link/Port guarded transition that consumes a certified TRIADIC_CLOSURE_E witness, accepts one V29 PASS, updates the attached source triad and source-slot frame, and respects actual local capacity, dependencies and the native rotation interlock. Current one-PASS coding is a conditional compatible realization; authority to claim the event as a primitive remains a separate Source/foundation decision.

Persistence: author-side GitHub research branch, with independent mathematical review, Researcher activity/CLAIM and Source Result separately recorded only on actual authenticated success.