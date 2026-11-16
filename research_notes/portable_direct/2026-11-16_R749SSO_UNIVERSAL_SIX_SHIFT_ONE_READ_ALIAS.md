# R749SSO — Every cutoff has a six-shift one-read alias

**Date:** 2026-11-16. **Status:** AUTHOR_EXACT_NOT_REVIEWED (author analytic proof and exact symbolic certificate; independent review pending).

**Scientific pin:** `a72226e2430ffa4786321ac86e7f0c599d5f0389`, unchanged from R749SSM and R749SSN. Source five labeled weights \((1,1,2,3,6)\). R749SSN [PR #2573](https://github.com/awdawmip/enterprise-math/pull/2573) is a prerequisite for the source definition and its exact rational reconstruction code. This unit does not use native signed-X6 kinematics.

## Model

Put \(\Omega_q=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le q-1\}\), \(C_q=|\Omega_q|\) and \(T_q=\sum_{k\in\Omega_q}k_1\). With \(S(q)=18q^4+54q^3-345q^2+2070q-16315\), for integers \(q\ge6\) and real \((e,d)\in[-2,2]^2\), define

\[
Y_q(e,d)=q^3\frac{T_q+e}{C_q+d}-\frac{S(q)}{108},
\qquad I_q=Y_q([-2,2]^2)=[L_q,U_q],
\]

where

\[
L_q=q^3\frac{T_q-2}{C_q+2}-\frac{S(q)}{108},\qquad
U_q=q^3\frac{T_q+2}{C_q-2}-\frac{S(q)}{108}.
\]

Monotonicity in \(e\) and \(d\) and continuity establish the interval identity, with \(C_q>2\) and \(T_q>2\) throughout.

## Universal strict-overlap theorem

**For every integer \(q\ge6\),**

\[
\boxed{\max(L_q,L_{q+6})<\min(U_q,U_{q+6}).}
\]

Thus the two distinct candidate cutoffs \(q\) and \(q+6\) have overlapping one-read image intervals with nonempty interior. In fact, for **each** such integer \(q\) there exist *rational*, strictly interior calibration pairs \((e,d),(e',d')\in(-2,2)^2\) such that

\[
\boxed{Y_q(e,d)=Y_{q+6}(e',d').}
\]

This supplies an infinite family of exact one-read unknown-cutoff collisions even though R749SSN proves that **adjacent** cutoffs at \(q\ge501\) can be distinguished with a single read.

## Complete analytic positivity proof

Strict overlap of the closed intervals is equivalent to the pair of inequalities

\[
U_{q+6}-L_q>0,\qquad U_q-L_{q+6}>0.
\]

Write \(p=q+6\), \(c=C_q,t=T_q,c'=C_p,t'=T_p\). Multiplying by positive denominators yields respectively

\[
\begin{aligned}
N_1={}&108p^3(t'+2)(c+2)-108q^3(t-2)(c'-2)\\
&-[S(p)-S(q)](c'-2)(c+2),\\
N_2={}&108q^3(t+2)(c'+2)-108p^3(t'-2)(c-2)\\
&-[S(q)-S(p)](c-2)(c'+2).
\end{aligned}
\]

More precisely, \(U_p-L_q=N_1/[108(c'-2)(c+2)]\) and \(U_q-L_p=N_2/[108(c-2)(c'+2)]\). The denominators are strictly positive.

From the exact source generating functions

\[
\sum_{q\ge0}C_qz^q=\frac{z}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},
\quad
\sum_{q\ge0}T_qz^q=\frac{z^2}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)},
\]

the source counts \(C_{6n+r}\) and \(T_{6n+r}\) are exact polynomials in \(n\) of degree at most 5 and 6 for each residue \(r=0,\dots,5\), for every integer \(n\ge1\). Thus \(N_1,N_2\), at fixed residue \(r\), are *degree-nine* polynomials in \(n\).

For \(q=6n+r\) substitute \(n=u+1\), where \(u\ge0\). The companion executable certificate computes all coefficients of the resulting 12 polynomials. **Every one of the 120 exact rational coefficients is strictly positive**, not just the leading coefficients. Specifically, the ascending coefficient sign vectors of both \(N_1(u+1)\) and \(N_2(u+1)\) are `++++++++++` for all six residues, and the exact constant terms are:

| \(r\) | \(N_1(1)\) | \(N_2(1)\) |
|---:|---:|---:|
| 0 | 51,706,512 | 125,163,792 |
| 1 | 114,090,444 | 276,766,308 |
| 2 | 263,295,360 | 537,560,064 |
| 3 | 545,565,132 | 997,232,148 |
| 4 | 1,017,984,240 | 1,807,885,872 |
| 5 | 1,808,122,932 | 3,153,147,372 |

The leading coefficient of each of the twelve polynomial expressions is \(839808/5\). Every coefficient is computed and sign-checked using rational SymPy arithmetic; the asserted quasi-polynomial identities are independently cross-checked against source counts at four integer values in each residue class. Consequently \(N_1,N_2>0\) for every integer \(n\ge1\), completing the *infinite-domain* strict-overlap proof.

## Explicit rational construction for each \(q\)

Let

\[
a=\max(L_q,L_{q+6}),\quad b=\min(U_q,U_{q+6}),
\quad y=\frac{a+b}{2}\in\mathbb Q.
\]

For each \(Q\in\{q,q+6\}\) set \(\rho_Q=y+S(Q)/108\) and

\[
\lambda_Q=\frac{\rho_Q(C_Q+2)-Q^3(T_Q-2)}
{4(\rho_Q+Q^3)},\qquad
(e_Q,d_Q)=(-2+4\lambda_Q,\,2-4\lambda_Q).
\]

Since \(L_Q<y<U_Q\) and the path \(\lambda\mapsto(e,d)=(-2+4\lambda,2-4\lambda)\) moves strictly and monotonically from the minimum to the maximum of \(Y_Q\), one has \(0<\lambda_Q<1\) and \(Y_Q(e_Q,d_Q)=y\). The formula follows by solving

\[
\rho_Q=\frac{T_Q-2+4\lambda}{C_Q+2-4\lambda}\,Q^3.
\]

Each \(C_Q,T_Q,S(Q)\) is rational/integer. Hence both distinct cutoff calibrations are **rational interior points** and give exactly the same reading.

## Verification and scope

Execute `python R749SSO_SIX_SHIFT_ALIAS_CERT.py` alongside `R749SSN_ADJACENT_SINGLE_READ_CERT.py` (Python and SymPy). The exact program reconstructs all source counts, verifies 12 × 10 positive polynomial coefficients, checks 6 × 4 endpoint equations independently against direct counts, and constructs 204 distinct q/q+6 exact rational collisions for q=6,...,209. Local execution returned `PASS`; results are in `R749SSO_SIX_SHIFT_ALIAS_RESULTS.json`. The computation is a certificate for the analytic general proof; the finite q6..209 check is a separate cross-check, not a substitute for the polynomial argument.

This is an observer-specific scalar projection statement. The two candidates are allowed **separate** fixed real error pairs; it is not a claim that one common pair must make \(Y_q=Y_{q+6}\). The full 6D native event, Cell/Link/Port incidence, labels, branch history and multi-read future are additional typed structures. By P000 and ACTIVE residual-fidelity rules, they require explicit preservation checks before BRC or native time interpretation.

**Next question:** determine the minimal observation horizon that separates *all* q and q+6 under the same per-candidate common-in-time error pair across consecutive six-shift reads, possibly with a sharp cutoff. Separately classify nonadjacent phase errors and construct a bounded-state BRC observer preserving source labels and future-observation fibers.