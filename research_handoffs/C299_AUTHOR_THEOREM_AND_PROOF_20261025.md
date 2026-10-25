# C299 — Two exact pole cancellations in 125 auxiliary rational paths

**Date:** 2026-10-25. **Scope:** C195/H168 positive-rational 79-node auxiliary model on the frozen C293 125 dyadic parameter strips. **Status:** author-level proof and exact arithmetic, not Source-admitted, not Driver-reviewed, no native CLAIM. Not a theorem about signed/phase GF(2)-BRC or native P000 six-dimensional Cell dynamics.

## Frozen authority and inputs

GLOBAL_KNOWLEDGE_V1 canonical main was read at `a23e21ac467a11ceef7eeb4902ba931bc48c21a5`, including `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, `projects/enterprise-math/P000_STARTUP.json` and the original P000 metadata, and ACTIVE worldview. Enterprise Math control main was read at `89710e353e7aa0093fc56afde73eaf30de54e4cc`; portable research protocol: `docs/PORTABLE_RESEARCH_PROTOCOL.md`. The fixed mathematical input is C275/C284/C288/C293 with inherited author-level C297 outward-width and C298 integer shared-denominator results. The actual C293 record hash is `03083a77480e6be5615797c2f4ffc503eee6603e9e60cbad1f11fb3ea83b3c89`; C284 hash `fcdad45cb2ed5df659b1a153762d358e2b7fa4df3e14c1be3eb505d4209ef576`.

## New theorem: at least two integral polynomial cancellations per path

Four moving nodes occupy positions `5,50,55,56` of the totally ordered 79-node model. For each path C298 constructs an integer polynomial presentation
[
 f_i(t)=F(v_i(t))/2^{128}=A_i(t)/D_i(t),\quad A_i,D_i\in\mathbb Z[t],\quad D_i(t)>0
]
on its physical strip, with `D_i=S_i∏_q q(t)^{e_q}` using positive primitive integer denominator factors and `deg(D_i)≤354`.

Define `q_{i,02}` and `q_{i,13}` as the positive-on-strip primitive linear factors for moving-moving gaps (node positions 5,55) and (50,56). For each of 125 paths, both are distinct, genuinely degree one, occur to exponent exactly one in the C298 shared denominator, and **both divide its numerator in `Z[t]`**.

Proof: On a strip every absolute-value denominator has fixed sign, providing a rational continuation. At the collision of moving slots `k<m`, the two moving-branch terms have identical self-weight and numerator factors at the coincident coordinate; denominator orientations differ by one sign for every *other full-list node* strictly between the slots. Thus the ratio of their nonzero residues is `(-1)^(m-k-1)` with indices in the entire 79-node ordered list. Between positions 5 and 55 there are 49 intermediate nodes; between 50 and 56 there are 5. Both counts are odd, so each of the two individually nonzero residues cancels its partner exactly. For each frozen affine path, exact rational arithmetic verifies that these are the sole two terms containing the relevant primitive factor, no other factor vanishes at its rational pole, and its two residue values are nonzero and sum to zero. Since each factor is simple in `D_i`, the absence of a pole forces a root of `A_i`; primitive linear divisibility and Gauss's lemma give integer polynomial quotients. The two factors are distinct and hence coprime.

Therefore
[
 A_i'=A_i/(q_{i,02}q_{i,13}),\qquad D_i'=D_i/(q_{i,02}q_{i,13})\in\mathbb Z[t],
]
`f_i=A_i'/D_i'`, and `D_i'>0` on the original strip. The **constructed denominator degree** is 352 on 124 paths and 265 on path 28; so the **fully reduced denominator degree is at most** that value. Further cancellation on other paths is not ruled out.

## Improved positive height and dyadic sign precision

For the C298 integer 1-norm majorant `M_i=S_i∏_q ||q||_1^{e_q}`, exact division by the two positive-factor 1-norms yields `M_i'=M_i/(||q02||_1 ||q13||_1)`. On every frozen interval,
[
 0<D_i'(t)\le M_i'<2^{13713}.
]
All 125 exact integer calculations pass; the previous uniform exponent was 13799.

If dyadic `t=k/2^b` is in the strip and `f_i(t)≠1`, the integer polynomial `A_i'-D_i'` of degree at most `d_i'≤352` gives
[
 |A_i'(t)-D_i'(t)|\ge2^{-d_i'b},\qquad |f_i(t)-1|>2^{-d_i'b-H_i'}.
]
Using the **inherited C297 author-level** full-interval outward-evaluator width `<2^(134-P)`, a uniform sufficient sign precision is
[
\boxed{P=352b+13713+134}.
]
At `b=512`: 194071 bits, versus C298's 195181 bits, a reduction of 1110 sufficient-precision bits. It does not establish the same ratio of actual runtime or memory savings. No finite P can determine a strict sign at an exact threshold equality.

## Sharpness at three *selected* paths only

For `i=0,28,124`, a separate modular polynomial calculation at `p=998244353` reconstructs integer `A_i,D_i` modulo p from all 79 factorized branch terms; confirms exact modular denominator division and full `deg(D_i mod p)=deg(D_i)`; and returns `deg gcd(A_i mod p,D_i mod p)=2`. The characteristic-zero proof above gives gcd degree at least 2. The degree-preserving modular reduction gives at most 2: an integral primitive common factor would retain degree and divide both polynomials modulo p. Hence the *exact reduced* rational denominator degrees of these three paths are 352, 265, 352. **No 125-path sharpness claim:** the remaining 122 paths have the rigorous upper bound only.

## BRC/observer residual: real information-loss witness

At each cancelled pole the two individual moving-branch residues are `(r,-r)` with `r≠0`. Their scalar sum is zero, but a permitted future operation observing or reweighting either branch separately can distinguish the ordered pair. Hence cancelling the rational singularity in the auxiliary scalar **does not authorize deleting the underlying branch identity** for a provenance-sensitive observer. This is an exact auxiliary-branch carrier witness, **not** a transfer theorem to native signed GF(2)-BRC, phases, ports, six-dimensional X6 updates or P000.

## Validation, limits, next problem

New exact checks: **125/125** factor inventories and height majorants, **250/250** nonzero opposite rational-residue pairs; 124 paths with constructed denominator degree 352 and one with degree 265. Three independently generated finite-field gcd degree certificates for indices 0,28,124. Local portable ZIP isolated extraction, input SHA256 verification and both programs executed successfully. The continuous width lemma from C297 remains an explicitly inherited author-level dependency, not independently re-proved.

Native `em_control_tasks` returned `CONTROL_QUOTA`. Native `em_session_start(RESEARCHER)` returned `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. GitHub research activity was separately registered; it grants no TASK CLAIM, review, Result, Working Truth, Foundation or mathematical acceptance.

**C300:** decide the exact coprime reduced denominator degrees for the *other* 122 paths, using a more efficient modular pole/evaluation certificate; alternatively obtain a genuine signed/provenance-preserving native BRC observer bridge. Preserve the existing 125-path certified two-factor reduction without assuming further cancellation.
