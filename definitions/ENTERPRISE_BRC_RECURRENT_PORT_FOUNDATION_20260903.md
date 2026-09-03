# Enterprise Math — Recurrent BRC Port Collapse Foundation Addendum

Status: `CANONICAL ALL-RESEARCH FOUNDATION ADDENDUM / MAIN-BACKED / FINITE-POSITIVE-RATIONAL`
Effective: `2026-09-03`
Parent: `ENTERPRISE_BRC_RECURRENT_INTERACTION_FOUNDATION_20260903.md`
Theorem ledger: `ENTERPRISE_BRC_RECURRENT_PORT_THEOREM_LEDGER_20260903.json`

## 1. Purpose

This addendum freezes the exact recurrent Schur/port black-box results from PRs #1152 and #1153. Generic Schur complements, stochastic complements, boundary response maps, Dirichlet-to-Neumann/Poincare-Steklov operators and network black-box reductions are classical prior art. The Enterprise Math contribution is the typed positive-rational BRC operation/context contract.

## 2. Boundary Schur collapse

For

\[
W=\begin{pmatrix}A&X\\Y&B\end{pmatrix}
\]

with stable hidden/internal block `A`, define

\[
S_I=(I-A)^{-1},
\qquad
\boxed{W_{\rm eff}=B+YS_IX}.
\]

Every effective boundary entry is the total positive mass of either a direct boundary edge or one complete internal excursion.

Then

\[
\boxed{W\text{ stable}\iff W_{\rm eff}\text{ stable}}.
\]

When stable,

\[
\boxed{(I-W)^{-1}[B,B]=(I-W_{\rm eff})^{-1}},
\]

\[
\boxed{\det(I-W)=\det(I-A)\det(I-W_{\rm eff})},
\]

and

\[
\boxed{Z_{\rm loop}(W)=Z_{\rm loop}(A)Z_{\rm loop}(W_{\rm eff})}.
\]

Canonical ID: `WBRC-T30`.

## 3. Port-context operation safety

A permitted future context may add arbitrary finite non-negative rational:

- port-to-port edges;
- port-to-new-external edges;
- new-external-to-port edges;
- new-external-to-external edges;

but no direct hidden-state connection or mutation.

For any such context, replacing the module by `W_eff` preserves exactly:

- stable/unstable outcome;
- every stable visible port/external star entry;
- all visible feedback-event kernels built from those star entries;
- feedback stability, interactions and critical radii.

Thus the current Foundation feedback calculus `WBRC-T25..T29` commutes with port collapse whenever event endpoints remain visible.

Positive rational gauge restricts naturally to the ports, and repeated stable Schur elimination is associative.

Canonical ID: `WBRC-T31`.

## 4. Minimal port signatures

For baseline-stable modules with the same labeled ports, define port-dynamic contextual equivalence by equality of stability outcome and stable visible star in every permitted finite positive-rational context.

Then

\[
\boxed{M_1\equiv_{\rm port}M_2\iff W_{{\rm eff},1}=W_{{\rm eff},2}}.
\]

Sufficiency follows from the context theorem. Necessity follows from the empty context, because the stable port star recovers

\[
\boxed{W_{\rm eff}=I-S_{\rm port}^{-1}}.
\]

If the observer additionally asks for **absolute full global** loop-zeta, retain

\[
\boxed{Z_{\rm int}=1/\det(I-A)}.
\]

The complete exact signature becomes

\[
\boxed{(W_{\rm eff},Z_{\rm int})}.
\]

For future-context zeta/Gamma **increments only**, the hidden constant cancels, so `W_eff` alone remains sufficient.

Canonical ID: `WBRC-T32`.

## 5. Hierarchical module composition

Exact black-boxing composes:

```text
leaf recurrent module
-> W_eff port signature
-> connect through visible ports
-> Schur-eliminate higher hidden layers
-> repeat
```

If absolute global zeta is observed, hidden `Z_int` factors multiply along the elimination hierarchy. The final product is order independent although stagewise attribution need not be.

Port labels are semantic. A declared port bijection acts by permutation similarity on `W_eff`; no unlabeled port identification is implicit.

## 6. Hard boundaries

Freeze:

```text
RECURRENT_PORT_COLLAPSE = POSITIVE_TOTAL_MASS_SEMANTICS
RECURRENT_PORT_COLLAPSE != CWM_COUNT_DOMINANT_PROVENANCE_SAFE
PORT_SIGNATURE_LEASE -> NO_DIRECT_FUTURE_HIDDEN_STATE_ACCESS
VISIBLE_DYNAMIC_SIGNATURE = W_EFF
VISIBLE_DYNAMIC_PLUS_ABSOLUTE_ZETA_SIGNATURE = (W_EFF,Z_INT)
WEAKER_OBSERVER_MAY_ADMIT_COARSER_SIGNATURE
RICHER_INTERNAL_OBSERVER_REQUIRES_RICHER_SIGNATURE
```

Equal `W_eff` can hide different path count/dominant/provenance structures. Direct future connections to hidden states invalidate the port lease. Signed/amplitude, complex, arbitrary irrational-exact and infinite-state contexts remain outside this addendum.

Canonical negative IDs: `WBRC-N12`, `WBRC-N13`.

## 7. Tool routing

Reusable T0 subtool:

`t0.weighted_brc_recurrent_port_collapse` -> `src/enterprise_math/brc_recurrent_ports.py`.

The port tool reuses the canonical finite-recurrent stability/star layer; it does not create a new top-level family and does not mutate deterministic `T6_OPERATION_SAFE_QUOTIENT`.
