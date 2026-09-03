# Free Research #1161 — internal rotation-completion constant `tau` and the remaining normalization bridge

Status: `FREE_RESEARCH_RESULT / CROSS-FAMILY CONSISTENCY + OPEN GLOBAL BRIDGE / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent issue: `#1161`
Cross-family source: free-research result `#1159`

## 1. Replace the external target question by an internal one

The #1161 recursion defines its endogenous completion constant

\[
\Pi_*:=H_\infty^2/A_\infty.
\]

Independently, #1159 defines a project-internal rotation boundary-completion constant `tau` without using classical circumference or a target numerical pi value.

One #1159 route starts from exact finite rational parity-sector determinant ratios

\[
W_N=\prod_{r=1}^N\frac{(2r)^2}{(2r-1)(2r+1)}
\]

and proves

\[
1<\frac{W_\infty}{W_N}\le\frac{4N+2}{4N+1},
\qquad
\tau=2W_\infty.
\]

Thus the strongest project-internal completion question for #1161 is not initially

`Pi_*=classical pi`,

but

\[
\boxed{\Pi_*\stackrel{?}=\tau}.
\]

Only after a separate classical identification of `tau` would that imply the familiar name `pi`.

## 2. Local cross-family geometry is already matched

The separate #1161 Viète-bisector square factorization proves that the local AGM cone update factors through the same finite normalized bisector operation used in #1158:

\[
\text{Viète bisector}
\to
\text{componentwise square}
\to
\text{Pythagorean cone completion}.
\]

This establishes a genuine common local rotation/refinement mechanism.

However, common local RG geometry does **not** imply equality of global completion constants. A normalization theorem is still required.

## 3. Exact form of the remaining global bridge

By definition,

\[
\Pi_*=\frac{H_\infty^2}{A_\infty}.
\]

Therefore

\[
\boxed{
\Pi_*=\tau
\iff
A_\infty\tau=H_\infty^2.
}
\]

This single identity is the remaining cross-family normalization bridge.

It is useful to name the completion-normalization defect

\[
\mathcal L_{\rm AGM/rot}
:=A_\infty\tau-H_\infty^2.
\]

Then

\[
\boxed{
\Pi_*=\tau
\iff
\mathcal L_{\rm AGM/rot}=0.
}
\]

At current result strength, this is an **open discrete Legendre-type bridge**, not a proved identity.

The name `Legendre-type` is descriptive of the role played by the normalization relation. No classical elliptic-integral Legendre relation is imported as a premise.

## 4. Finite no-pi cross-family consistency certificate

The #1159 finite Wallis bound gives

\[
2W_N<\tau\le 2W_N\frac{4N+2}{4N+1}.
\]

At

\[
N=10000,
\]

exact rational arithmetic proves that both endpoints lie in the same decimal cell

\[
\boxed{3.1415\le\tau<3.1416}.
\]

Independently, the #1161 integer/dyadic AGM certificate at step `n=2` proves that

\[
\Pi_*
\]

lies in the seven-decimal cell

\[
\boxed{3.1415926\le\Pi_*<3.1415927}.
\]

Hence the two independently defined internal completion constants share the certified four-decimal cell

\[
\boxed{3.1415}.
\]

No classical pi value is supplied to either finite computation.

This is a cross-family **consistency certificate only**. Agreement of finitely many decimal cells does not prove equality of limits.

## 5. Reproducibility

Cross-family checker:

`scripts/check_free_research_1161_wallis_tau_cross_consistency.py`

initial commit:

`54161d0cfaf42a4f20b6a033eb9af47e578c8c2c`

It imports the already-committed #1161 dyadic AGM checker and independently computes the exact rational #1159 Wallis partial product and tail interval.

Validated values:

- `wallis_n = 10000`;
- `tau` certified cell: `3.1415` at four decimal places;
- AGM step `n=2` certified cell: `3.1415926` at seven decimal places;
- shared four-decimal cell: `3.1415`;
- `equality_proved = False` by design.

## 6. Research consequence

#1161 is now separated into three layers:

1. **local mechanism:** exact finite bisector-square/cone RG — proved at derived G1/G2 strength;
2. **finite precision:** integer root/detail compiler + explicit double-exponential error theorem — proved;
3. **global completion normalization:** `A_inf * tau = H_inf^2` — open.

Thus any future use of elliptic integrals or the classical Legendre relation can be cleanly labeled as one possible analytic completion of layer 3, rather than being hidden inside the local AGM construction.

A successful native/project-internal closure would instead derive `mathcal L_AGM/rot=0` from finite rotation/path/determinant structure.

## 7. Frozen scope at free-research-result strength

`AGM_INTERNAL_TARGET = tau`, where `tau` is the independently defined #1159 rotation-completion constant.

`LOCAL_VIETE_AGM_BRIDGE = EXACT_DERIVED`.

`FINITE_TAU_PI_STAR_CONSISTENCY = CERTIFIED_TO_SHARED_4_DECIMAL_CELL`.

`PI_STAR_EQUALS_TAU = OPEN`.

`A_INFINITY * TAU = H_INFINITY^2 = EXACT_REMAINING_GLOBAL_BRIDGE`.

`PI_STAR_EQUALS_CLASSICAL_PI = ANALYTIC_COMPLETION_UNTIL_THE_INTERNAL_BRIDGE_AND_CLASSICAL_TAU_IDENTIFICATION_ARE_SUPPLIED`.
