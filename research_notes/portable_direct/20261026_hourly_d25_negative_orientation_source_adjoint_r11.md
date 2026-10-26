# D25/LIFT — Unit-safe lower-orientation Ward adjoint for original signed Clausen weight

Date: 2026-10-26. Research lane: `chatgpt-research-hourly-enterprise-math-20260923`.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** This is an external corrected-Clausen finite-rank algebra result. It is NOT original-class CM/Frobenius computation, formal WZ closure, native Source checkpoint, or mathematics admission.

## Precisely consumed input

Use without re-credit the exact oriented corrected-Clausen rank recurrence and two cutoff sources in `20261026_hourly_d25_diagonal_rank_moment_closed_recurrence_r11.md`, together with `20261026_hourly_d25_diagonal_one_digit_resonance_r11.md`. For integer `m>=1`, `p=6m+1`, `L=1-2m`, let

\[
M_n^{ab,s}=\sum_{\substack{1\le j,\ell\le2m\\\ell-j=n}}j^s u_{a,j}u_{b,p-\ell},\quad
Y_n^{ab}=M_n^{ab,1}-\frac{p-n}{2}M_n^{ab,0},\quad
S_n^{ab}=J_n^{ab}+E_n^{ab}.
\]

The imported, **exact rational** Ward law, with both true finite source faces, is

\[
(p-2n)Y_n-(p-2n-1)Y_{n+1}=S_n\quad (L\le n<2m).
\]

Channels below are `(0,2),(1,2),(0,3)`; negative/positive orientation refers to `n=ell-j`, not an unlabeled symmetrization.

## Theorem — exact lower-oriented discrete adjoint, with no p division

Set `w_n=2^n`. Define the **backward** adjoint weights by

\[
\lambda_0=0,\qquad
\lambda_{k-1}=\frac{(p-2k)\lambda_k-2^k}{p-2k+1}
\quad(k=0,-1,\ldots,L+1),\qquad
\delta=2^L-(p-2L)\lambda_L.
\]

Then, for every Hasse channel and every integer `m>=1`, the following is an **exact identity over Q**, not merely a congruence:

\[
\boxed{\sum_{n=L}^{0}2^nY_n
=\sum_{n=L}^{-1}\lambda_n S_n+\delta Y_L.}\tag{A}
\]

Every adjoint denominator `p-2k+1` is a unit at primes `p=6m+1`: for `L+1<=k<=0`, its reduction lies among nonzero `1,3,5,...,4m-3` modulo `p`. Thus (A) is a **p-integral**, unit-safe lower-triangle transport modulo every positive power of `p`; it does not cross the `n=0` forward resonance by dividing by `p`.

**Proof.** Multiply the exact Ward equation at `n` by `lambda_n` and sum `n=L,...,0`. Reindex the shifted `Y_{n+1}` term. For `L<n<=0`, its coefficient becomes
`(p-2n)lambda_n-(p-2n+1)lambda_{n-1}=2^n`
by construction. The `Y_1` term vanishes because `lambda_0=0`; the `Y_L` coefficient on the source side is `(p-2L)lambda_L`. Add the exact correction `delta Y_L` to recover the missing `2^L Y_L`. This proves (A) and retains the left tagged cutoff; it makes no assumption about vanishing of `J`, `E`, or signed source terms. QED.

## Corollary — explicit interface to the original three-channel scalar reflection

Define the **original lower-oriented Laurent weights** and the first-rank companion

\[
U_{ab}=\sum_{n=L}^{0}2^n M_n^{ab,0},\quad
T_{ab}=\sum_{n=L}^{0}2^n(1-6n)M_n^{ab,0},\quad
K_{ab}=\sum_{n=L}^{0}2^n M_n^{ab,1}.
\]

Then

\[
\boxed{
T_{ab}=(1-6p)U_{ab}+12K_{ab}
-12\left(\sum_{n=L}^{-1}\lambda_n S_n^{ab}+\delta Y_L^{ab}\right).
}\tag{B}
\]

**Proof.** The definition of `Y` gives
`R:=sum 2^nY_n=K-(p/2)U+(U-T)/12`; solve for `T` and substitute (A). QED.

Equation (B) is a genuine **source-tagged adjoint decomposition** for each of `T02,U02,T12,T03`. It retains the independently needed companion `K`, which is reconstructible from the true mass arrays and finite boundary inputs via the previously established p-unit first-moment recurrence. It is **not** a boundary-only scalar cancellation theorem. In particular, no infinity port is deleted or silently identified with the adjoint. The earlier positive-orientation Ward flux and its `p`-valuation remain a *different observer*.

## Exact author test / information-loss witness

The companion exact Fraction verifier independently constructs Hasse jets from the corrected rank recurrence; constructs signed labelled `M^{s}`; computes the genuine `J+E` terms **from their separate rank formulas**; verifies the imported Ward equation and both new (A),(B) over Q for all three channels, for every target prime `p=6m+1` with `1<=m<=12`. **711 exact assertions PASS** across nine primes `7,13,19,31,37,43,61,67,73` (the per-prime assertions grow with carrier size). This is author-only verification.

At `p=13`, modulo `p²=169`, the triples `(U,T,K,R, negative-source-adjoint, delta*Y_L)` are

- `(0,2): (138,130,99,104,104,0)`
- `(1,2): (80,41,154,102,30,72)`
- `(0,3): (69,113,13,96,96,0)`.

For channel `(1,2)`, **the genuine boundary contributes 72 mod169**, so suppressing it changes this adjoint readout. The other two channels have exactly zero left edge, as inherited. The particular value 72 is not asserted universal for all primes.

## BRC, limits, exact next unit

**BRC COMPOSE_APPLIED**: population ordered `(j,ell)` with separate Hasse channels, signed orientation and p-local valuations; future operations include Hasse parameter coupling and original signed scalar reflection. The compressed `Y` and companion `K` carry exactly the information required by (B), but do not independently recover arbitrary quadratic rank operators or native X6 physical dynamics. Auxiliary Laurent `z` is external symbolic algebra, not a primitive P000 plane.

**Next exact unit**: join (B) with the existing p² Green source quotient and full corrected rank/Hasse `k-1,k-2` coupling; examine separately `T02,U02,T12,T03` and the independently tagged infinity ports. Prove an all-prime cancellation only if it survives these observer distinctions; otherwise retain a source-tagged counterexample. The canonical mother objective separately requires actual original-class `H0/B0`, `[X]U mod p²`, Frobenius direction/normalization `eta`, `kappa`, and `Delta_p-R_p`, native experiment and independent review.

The 2026-10-26 Research-lane continuation read returned `SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED` with `NEEDS_DISPATCH` but `execution_authorized=false`; historic last claim `MCP-d0d70cd041b01e5db192870a` differs from checkpoint predecessor `MCP-87631b892b41fa18d799f2d8`. This portable note is not a new native CLAIM/run/checkpoint. Control support remains `awdawmip/enterprise-math#1558`.
