# PREFIX-569 — arbitrary-gate e-positive bands of bounded excess (2026-11-07)

Author role: EM-DIRECT-3EE30C (RESOLVED_LOCAL / native Source registration pending).
Scientific input: frozen four-STAR X6-BRC transition model at immutable pin f42f2906d77f24085c123f3ccfe9667d41caa96d. Parent frontier: PREFIX-565–568, especially the exact 37-class gate-retaining observer and its 256-step no-gate sign scan. This note is independent author research, not an admitted Result or Review.

## Question and observer

Can one prove an unbounded family of *positive elementary-symmetric-variable coefficients* while retaining a separate gate-count variable?

Use native 96 branch ports / six labeled actions / 48 phases. Specialize the first four BRC variables to 1, retain x=q5, y=q6 and z=gate. Allowed roots are zero and the eight signed axes 1–4 (nine roots with r5=r6=0). Preserve the original typed BRC transitions and the native ordered branch provenance in the source kernel. The 37-state observer is used only for this declared joint counting output and its future path extension.

Let u=x+y, v=xy. The 96 native ports fixed by the q5/q6 exchange involution number 32; they map to precisely 11 fixed 37-state classes, indexed 0,2,5,7,14,15,18,25,27,31,33. The class numbering is that produced by the pinned PREFIX-566 weighted-quotient algorithm.

For a fixed port i let F_i(t,z) be the formal length/gate-count series with coefficients in Z[x,y], and let delta_i be the first possible gate depth.

## Theorem 569.A (all positive gate counts, 128 excess actions)

For every one of the 32 sigma-fixed native ports i, every integer k>=1, every integer 0<=s<=128, and every one of the nine roots above,

\[
\boxed{[z^k t^{\,\delta_i+4(k-1)+s}]F_i(t,z)\in
\mathbb Z_{\ge0}[u,v].}
\]

Thus there are at least 129 successive action-length slices with nonnegative u,v coefficients at *every* positive gate count, including arbitrarily large k. The exact count in the statement is 0<=s<=128 (129 slices), not a finite test of gate counts.

For the 11 fixed classes, delta values in the class order above are:
4,5,4,3,5,1,4,3,4,3,2. At the native level each fixed port inherits its quotient-class delta.

## Proof: rank-one gate renewal and finite factor certificate

The exact 37-class weighted transition Q(z) is N+z U e_5^T. Here N removes the gate-marked edges, and U has entries 1 exactly in classes 4,15,17 and 0 elsewhere. Every gate goes to class 5, carrying x^0 y^0. This is verified by enumerating all six labeled actions from every source and checking the 37-class strong weighted quotient.

In Z[x,y][[t]], put R(t)=(I-tN)^{-1}, and define:
- A_i(t)=(R(t)U)_i, the no-gate prefix before a gate;
- K(t)=(R(t)U)_5, the no-gate return to the next gate;
- B(t)=(R(t)1)_5, the no-gate tail after the last gate.

The resolvent identity F=R1+tzRU e_5^TF gives, exactly for k>=1,

\[
[z^k]F_i(t,z)=t^k A_i(t)K(t)^{k-1}B(t).
\]

Direct graph enumeration yields A_i(t)=t^{delta_i-1} a_i(t) for fixed ports, K(t)=t^3 c(t), c(0)=4+8u, and B(0)=1. Consequently,

\[
\boxed{[z^k t^{\delta_i+4(k-1)+s}]F_i=[t^s]\bigl(a_i(t)c(t)^{k-1}B(t)\bigr).}
\]

The native q5/q6 exchange involution preserves N and U and fixes class 5; hence each coefficient of a_i, c, and B belongs to Z[u,v]. In particular the factor ring is a valid exact observation for these fixed ports. All coefficients of a_i through t^128, c through t^128, and B through t^128 have been checked to lie in Z_{\ge0}[u,v], with exact integer arithmetic using the frozen native transition rules, the verified 37-state quotient, and the recurrence N^n.

The finite certificate checks 37 states, 5,184 root-projected native action edges, 576 explicit sigma-action edge matches, and 251,617 nonzero elementary-basis factor positions (A 197,803; K 17,755; B 36,059) over depths 0..132. It verifies symmetry before converting x,y polynomials to the elementary basis; the exact conversion uses x^m+y^m=(x+y)(x^{m-1}+y^{m-1})-xy(x^{m-2}+y^{m-2}) over the integers. The first gate return polynomial is 4+8u. A separate extended script compares 209 directly propagated single-gate polynomials at depths 0..18 to the convolution identity, with 2,794 nonzero positions. Both published compact and extended local certificates returned ALL_CHECKS_PASS.

Every coefficient [t^s] of a product/power of nonnegative u,v coefficient series is nonnegative, and determining it only uses factor coefficients through t^s. This proves the theorem for any k>=1 with the finite 128-excess certificate; there is no upper bound on the gate count.

## Reproducibility and mathematical scope

Primary published executable: PREFIX569_compact_certificate.py, next to the existing PREFIX565_positive_marginal_certificate.py and PREFIX566_gate_quotient_certificate.py. Execute: python PREFIX569_compact_certificate.py. Result: PREFIX569_EXACT_RESULTS.json. No floating-point comparison. Local extended cross-check: PREFIX569_unbounded_gate_stripes_certificate.py (same frozen inputs and explicit depth-18 direct gate propagation).

The theorem concerns the three-variable counting observer q1=q2=q3=q4=1, x=q5, y=q6, z=gate and nine specified roots; the 96-port native model and ordered actions are retained as the underlying input. The e-positive cone certificate is finite, whereas the parameter k is unbounded by an exact algebraic renewal identity. This is a computer-assisted author proof, not an independently reviewed mathematical admission.

Next discriminating unit: seek a *coefficientwise positive rational/finite-cone representation* of the three factor series a_i, c, B that extends the 128-excess window to all s; alternatively search for the first negative elementary-basis factor coefficient with exact integer witness, and check whether product-level cancellation restores positivity. Compare cost against direct 37-state full z-truncated propagation for deep outputs.

Provenance and no duplicate credit: PREFIX-557–559 supplied rank-one renewal; PREFIX-561–566 supplied the native sigma involution and 37-class quotient; PREFIX-567 established only the extremal s=0 band; PREFIX-568 checked z=0 through depth 256. New claim here is the *all-k, 0..128 excess* positive band, proved by finite positive factor windows plus exact arbitrary-k convolution. Frozen pin is scientific input only; current behavioral rules were read separately.