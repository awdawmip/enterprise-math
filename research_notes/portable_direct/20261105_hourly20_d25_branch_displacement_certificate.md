# D25 — Signed Clausen branch-displacement certificate for the original 216 LIFT

Date: 2026-11-05 (+08). TASK_RESEARCH author-side exact algebra. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen input c47e13e4aba0e006366f989d6334d443f6333ae3. UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM.

## The branch-displacement two-stage certificate

For prime \(p=6n+1\ge7\), inherit the exact previously proved signed six-port congruence

\[
W_p\equiv S+p(A_{\rm port}+B_{\rm port})+
p^2(C_{\rm port}+D_{\rm port}+E_{\rm port})\pmod{p^3},
\]

and the finite Clausen/harmonic identity

\[
S\equiv\Psi(x)-p\alpha-p^2\beta\pmod{p^3},
\quad
x=\tfrac12,\quad
\alpha=\tfrac32U_1,\quad
\beta=\tfrac18(9U_{11}+5U_2).
\]

Here \(G(z)={}_2F_1(-n,-2n;1-p/2;z)\), \(\Psi(z)=G(z)[G(z)+12zG'(z)]\), and all ports retain their original source/precision. Define

\[
F=A_{\rm port}+B_{\rm port}-\alpha\pmod{p^2},
\qquad
H=C_{\rm port}+D_{\rm port}+E_{\rm port}-\beta\pmod p.
\]

Assume \(\Psi(x)\equiv0\pmod p\), as supplied by the frozen first-digit theorem for the target \(p\equiv13,19\pmod{24}\). Let \(x_p\) be the unique Hensel root in \(x+p\mathbb Z_p\), and put

\[
K=\Psi'(x)\in\mathbb Z_p^\times,\qquad
\delta=x-x_p\in p\mathbb Z_p,\qquad
\mu=\delta/p\pmod{p^2}.
\]

From the preceding *one-jet curvature theorem*, select the still-explicit vanishing-factor branch \(\varepsilon\in\{G,L\}\) and its coefficient \(c_G=2/3\), \(c_L=10/3\). Taylor expansion around \(x\) at its root yields

\[
\Psi(x)\equiv K\delta-Kc_\varepsilon\delta^2\pmod{p^3}.
\]

It follows that

\[
\boxed{
\frac{W_p-p}{p}\equiv
K\mu+F-1+
p(H-Kc_\varepsilon\mu^2)\pmod{p^2}.}
\]

This provides a **branch-adapted exact two-stage equivalent certificate** for \(W_p\equiv p\bmod p^3\):

\[
\boxed{K\mu+F-1\equiv0\pmod p,}
\]

then, when the first condition holds,

\[
\boxed{
\frac{K\mu+F-1}{p}+H-Kc_\varepsilon\mu^2\equiv0\pmod p.}
\]

Division by \(p\) in the second stage means any integer/p-adic representative of the full expression \(K\mu+F-1\) computed modulo \(p^2\), not separate reductions of \(K,\mu,F\) modulo \(p\). This is a representation-level equivalent certificate under the inherited identities, not yet a uniform proof of either vanishing condition.

## Proof and information retention

Substitute the harmonic expression for \(S\) into the six-port expression to get \(W_p\equiv\Psi(x)+pF+p^2H\pmod{p^3}\). Since \(x_p=x-\delta\) is a root and \(\delta\in p\mathbb Z_p\), Taylor gives \(0\equiv\Psi(x)-K\delta+B\delta^2\pmod{p^3}\), where \(B=\Psi''(x)/2\). The one-jet theorem gives \(B\equiv Kc_\varepsilon\pmod p\). Consequently \(\Psi(x)\equiv K\delta-Kc_\varepsilon\delta^2\pmod{p^3}\), proving the displayed relation after \(\delta=p\mu\). The first and second conditions are exactly the two base-\(p\) digits of the right-hand side, completing the equivalence. QED.

The observer is \((p,\varepsilon,K,\mu,F,H)\) with precision \((p,p^2,p^2,p^2,p)\) as appropriate, supported by the underlying source-preserving signed \(A_{\rm port},\ldots,E_{\rm port}\) and harmonic sums. Replacing \(c_\varepsilon\) by a branch-independent value is not permitted: the two branches have different curvature. This *local algebraic reparameterization* does not assert a lossless replacement for the original native H0/B0 or full six-dimensional state.

## Precise finite check, inherited-input scope

The companion script d25_branch_displacement_reduction_20261105.py was actually run locally with exact modular integer arithmetic. It re-evaluates \(G,G'\), the Hensel displacement, the harmonic \(U_1,U_{11},U_2\), and combines those with the **previously published** six-port \((A_{\rm port},B_{\rm port},C_{\rm port},D_{\rm port},E_{\rm port})\) check-table values at \(p=13,19,373\). Thus it is an exact composition check of the new formula, not an independent recalculation of the inherited six-port table.

| p | branch | \(\mu\bmod p\) | \(K\bmod p\) | \(F\bmod p^2\) | \(H\bmod p\) | stage 1 | stage 2 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 13 | G | 2 | 6 | 15 | 5 | 0 | 0 |
| 19 | G | 12 | 5 | 283 | 5 | 0 | 0 |
| 373 | G | 83 | 211 | 130196 | 317 | 0 | 0 |

All three yield \(W_p\equiv p\pmod{p^3}\). This finite evidence verifies the correct signs and placement of the curvature term in the new coordinate; a uniform cancellation proof remains open.

## Exact continuation

The next research question is to derive a non-tautological evaluation of \(F,H\) in the branch-local coordinates, looking for a uniform sum telescoper or parameter derivative identity that enforces the displayed second stage for both target classes. Retain original frozen \(\Delta_p-R_p\) observer, original-class p373 H0/B0 and \([X]U\bmod139129\), native Frobenius/\(\eta,\kappa\) and independent review obligations. The new local calculation is portable author-side work; native Source claimant, persisted checkpoint and historical contributors are untouched.
