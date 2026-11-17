# R762CU — Odd-path obstruction and minimal equivariant Port marking for P000 X6 triads

**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. **Researcher:** EM-X6-3050F6 (continuation of existing Run RUN-2f66fcc8f96765967a2e8cae). **Date:** 2026-11-17. **Status:** complete elementary proofs and author-side exact finite verification; independent review NOT_REVIEWED. **Predecessor:** R762CT, PR #2617 @ 0e19a5c924100daaeefe0ea5dbcd9b1ab518743e.

**Frozen inputs:** P000 V5, `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`; `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`, `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` at the same pin. Exact taskbook `@e3f42efac29a2da2d95be391f3231a664e2fade0`. Current behavioral rules are read separately, not science repins.

## Exact typed setup

Let X be the P000 affine Cell torsor over Z^6. A primitive spatial Link step is ±e_i. Define an **equal-quantum, distinct-support candidate Force-Port triad at a single Cell c** by an unordered set

T = {(i_1,ε_1),(i_2,ε_2),(i_3,ε_3)},  i_j in {1,...,6}, ε_j in {+1,-1}, and i_j pairwise distinct.

Write \(\Omega\) for the candidate set, with \(|\Omega|=\binom63\,2^3=160\); \(\Omega_c=\{c\}\times\Omega\). This is a *candidate incidence type*, not an assertion that every member satisfies native TRIADIC_CLOSURE_E. Distinct native supports give the P000 pairwise PERP_E constraint. Axis permutations \(S_6\) act by \(\pi(i,\epsilon)=(\pi(i),\epsilon)\); translations change the anchor c. Signs remain signed source labels, not extra axes.

The distinction between a Force-Port *attached at a Cell* and a spatial Link *leaving that Cell* is essential. We ask which event laws are forced by this substrate before imposing any additional native closure licence.

## Theorem 1 — sharp odd-step spatial-return obstruction

For any sequence of an odd number of primitive signed axis Link steps in X, the endpoint Cell differs from the initial Cell. In particular **no three primitive unit Links can form a closed Cell path**, even if steps repeat axes or directions. For a candidate T with distinct supports, the sum of its three corresponding step displacements has precisely three nonzero entries ±1, so its squared native axis-component readout is exactly 3 and never 0, independent of step order.

**Proof.** Choose any Cell anchor to identify relative displacements with Z^6. The parity character \(\chi(x)=\sum_{i=1}^6x_i\bmod 2\) flips on every ±e_i step. After an odd number of steps \(\chi\) changes, so the endpoint cannot equal the start. With distinct supports, no component cancellation can occur, and the P000 declared component quadratic readout gives \(L_E^2=\sum_i(\Delta x_i)^2=3\). Translations of the anchor do not affect either statement. QED.

**Consequence:** A canonical three-force balance, if realized at the primitive level, must be expressed by a typed Force-Port incidence/closure relation (possibly with internal channels or state), rather than identified with a three-Link spatial return. This is a *no-return theorem for an explicit proposed realization*, not a rejection of P000 triadic balance.

## Theorem 2 — exact S6-orbit classification of equal-quantum candidate triads

For \(k\in\{0,1,2,3\}\), let \(\Omega_k\) consist of triads with exactly k negative orientations. The \(S_6\)-orbits are precisely \(\Omega_0,\ldots,\Omega_3\), of sizes

\[
(|\Omega_0|,|\Omega_1|,|\Omega_2|,|\Omega_3|)=(20,60,60,20).
\]

Consequently, the number of Boolean closure predicates \(C:\Omega\to\{0,1\}\) that depend only on these typed inputs and are \(S_6\)-equivariant is **exactly 2^4 = 16**. Requiring at least one accepted candidate leaves 15 such predicates.

**Proof.** A permutation preserves the signs but can map any three distinct supports to any other three supports, transporting negative supports to negative supports and positive to positive. Therefore two triads lie in the same orbit iff k agrees; each orbit contains \(\binom63\binom3k\) elements. An invariant Boolean function is constant on each orbit, yielding one independent Boolean choice per orbit. QED.

**Interpretation:** Primitive arity three, distinct-support PERP_E and axis-permutation covariance alone leave these 16 combinatorial candidate relations. A genuine native TRIADIC_CLOSURE_E law must select a further specific rule, and its licence must be sourced separately. This classification does not impose sign-reversal invariance, which is not part of the specified S6 action.

## Theorem 3 — no unmarked deterministic S6-equivariant Port choice; optimal 3-sheeted repair

Restrict to the 20 all-positive triads \(\Omega_0\). There is **no** \(S_6\)-equivariant function \(f:\Omega_0\to\{+e_1,\ldots,+e_6\}\) satisfying \(f(T)\in T\) for every T.

Moreover, any \(S_6\)-equivariant extension \(p:Y\to\Omega_0\) equipped with an equivariant selected-Port map \(g:Y\to\{+e_i\}\), \(g(y)\in p(y)\), and with a nonempty fiber above every T, has at least **3 elements in every fiber**. This bound is attained by

\[
\widetilde{\Omega}_0=\{(T,a):T\in\Omega_0,\ a\in T\},\quad
p(T,a)=T,\quad g(T,a)=a.
\]

Thus one local, symmetry-preserving explicit Port selector needs **3 tagged alternatives**, or a minimum of \(\lceil\log_2 3\rceil=2\) fixed-length bits to record the chosen branch. The tag must transform with the Port under S6. Over all four sign orbits, the analogous marked candidate incidence set contains \(160\cdot3=480\) states, with a three-to-one projection.

**Proof.** Take \(T_0=\{+e_1,+e_2,+e_3\}\). Its stabilizer in S6 is \(S_3\times S_3\) of order 36, and its first factor acts transitively on the three Ports of T0. Equivariance of an unmarked f would force \(f(T_0)\) to be fixed by this stabilizer, whereas no Port of T0 is fixed. For any extension Y, the same stabilizer preserves \(p^{-1}(T_0)\). Choose y in that fiber. Its stabilizer orbit maps under g onto the full three-Port orbit, so the fiber contains at least three points. Transitivity of S6 on \(\Omega_0\) transfers the lower bound to every fiber. The displayed marked cover is equivariant, has exactly three points over each T, and provides g. QED.

**BRC significance:** If a proposed rotation/update follows one of the three equal homogeneous Ports, a one-state unmarked triad observation loses the branch identity. A 3-sheeted source-marking or a genuine three-branch positive N-BRC successor preserves it. This is an observer-specific information lower bound, not a physical-force balance equation.

## Exact verification and interfaces

`R762CU_VERIFY.py` is a standard-library-only executable exact enumeration. It verifies all 160 signed triads, the four orbit sizes and transitivity, 720 permutations × 160 sign-preservation/covariance checks, 160×6 three-step nonreturn witnesses, the 36-element stabilizer, 720×480 marked-cover equivariance checks, and 16 invariant Boolean closure candidates. `R762CU_EVIDENCE.json` records the reproducible counts.

**Native licensing still open:** P000 supplies the arity and geometry, not a specific Cell/Link/Port update or V17/V29/V39 transport. Theorems 1–3 give two exact tests for any proposed native law: (a) it must avoid identifying a triadic balance with an odd-length primitive Cell return; (b) a deterministic all-equal positive-Port choice must expose a symmetry-breaking Port mark or a declared branch, or else use a different event type. The next discriminating unit is to apply these tests to an exact sourced TRIADIC_CLOSURE_E event licence, then combine licensed source-word operations with the R762CT observer quotient and R762CH/CK path-area provenance.

**Admission:** author checked / NOT_REVIEWED; no formal Foundation promotion, native physical calibration or Source Result acceptance claimed.
