# D25 — A curvature–slope certificate for the ORIGINAL weighted-216 Hensel root, and a first-digit test of Gauss-root identification

Date: 2026-11-04 (+08). **AUTHOR-DERIVED / EXACT SCOPED ALGEBRA / 77-PRIME EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.**

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; immutable publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research logical lane: `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance). Parent mother target is `Delta_p=R_p mod p` for primes `p=13,19 mod24`, equivalent under the frozen bridge to `W_(p-1)=p mod p^3`. No change to this target or the original 216 coefficients. This is an author-side portable continuation of `20261104_onhour_d25_cm_weighted216_simple_root_hensel_digit.md` at immutable commit `7e529b7f873b82b684d4cc8a259fa7951e0a9e1e`.

## Original objects and consumed inputs

Let `p=6r+1 >=13` be prime in one of the two target classes, and `z_0=1/2` in `Z_p`. Put
[
c_k=\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3},\qquad
B_p(z)=\sum_{k=0}^{p-1}(6k+1)c_k z^k,
]
and the *separate terminating Gauss surrogate*
[
F_r(z)={}_2F_1(-r,-2r;1-p/2;z).
]
The previously established coefficient-level Clausen congruence is
[
B_p(z)\equiv F_r(z)\bigl(F_r(z)+12zF_r'(z)\bigr)\pmod p.
]
Consume the previously established CM-inert zero `F_r(z_0)=0 mod p`, its simplicity `F_r'(z_0)!=0 mod p`, and the **accepted first digit** `B_p(z_0)=p mod p^2`. We do not consume any unproved second-digit cancellation.

## Theorem 1 — Exact universal curvature ratio at the target CM zero

For every prime in scope,
[
\boxed{B_p'(z_0)\equiv6F_r'(z_0)^2\not\equiv0\pmod p,\quad
B_p''(z_0)\equiv8F_r'(z_0)^2\pmod p.}
]
Consequently,
[
\boxed{3B_p''(z_0)-4B_p'(z_0)\equiv0\pmod p.}
]

**Proof.** The terminating Gauss differential equation is
[
z(1-z)F''+[1-p/2-(1-3r)z]F'-2r^2F=0.
]
Since `r=(p-1)/6=-1/6 mod p`, its coefficient of `F'` at `z_0=1/2` is `1/4` modulo p. The coefficient of `F''` is also `1/4`; at the established simple zero this gives `F''(z_0)=-F'(z_0) mod p`. Differentiating `B=F^2+12zFF'` coefficientwise modulo p gives at the same zero
[
B'=12zF'^2=6F'^2,qquad
B''=26F'^2+36zF'F''=(26-18)F'^2=8F'^2.
]
All denominators are p-adic units for p>=13. This is a proof in the original polynomial residue ring, not a fitted relation.

## Theorem 2 — Slope-only second-digit baseline / curved-coordinate transport

Let `W=B_p(z_0)`, `D=B_p'(z_0)`, with `D` a p-adic unit. For `delta in p Z_p` define the local observer coordinate
[
u(\delta)=\delta+\tfrac23\delta^2 \pmod{p^3}.
]
By Theorem 1 and Taylor's theorem,
[
\boxed{B_p(z_0+\delta)\equiv W+D\,u(\delta)\pmod{p^3}.}
]
The unique Hensel root `zeta_p=z_0+delta_p` therefore satisfies the **explicit second-jet formula**
[
\boxed{
\delta_p\equiv-\frac WD-\frac23\left(\frac WD\right)^2\pmod{p^3}.}
]
Here inversion uses the p-adic unit `D`; only `D mod p^2` is needed. Because the accepted first digit gives `W=p mod p^2`, define the independently *specified baseline coordinate* using only the known first digit and derivative:
[
\boxed{
z_p^{\rm base}=z_0-\frac pD-\frac23\left(\frac pD\right)^2\pmod{p^3}.}
]
Then
[
\boxed{
\frac{\zeta_p-z_p^{\rm base}}{p^2}
\equiv-\bigl(D\bmod p\bigr)^{-1}
\frac{W-p}{p^2}\pmod p.}
]
The quadratic difference vanishes mod p^3 because `W-p` is a multiple of p^2. Thus **the frozen mother congruence is equivalent to coincidence of two fully specified local points modulo p^3**. In this coordinate, the prior second derivative/Hensel curvature input is eliminable: the Legendre/Gauss differential equation supplies its universal coefficient `2/3`. This is an equivalent criterion and is not an independent all-prime cancellation proof.

## Theorem 3 — Exact condition for a naive CM/Gauss-root identification

The Gauss surrogate has its own unique local root `xi_p=z_0+p a_F (mod p^2)` with
[
a_F\equiv-\frac{F_r(z_0)/p}{F_r'(z_0)}\pmod p.
]
The original weighted root has first digit
[
a_W\equiv-\frac1{6F_r'(z_0)^2}\pmod p.
]
Thus the two roots have the same first digit **if and only if**
[
\boxed{6F_r'(z_0)\,(F_r(z_0)/p)\equiv1\pmod p.}
]
This is an exact necessary-and-sufficient criterion for that particular proposed identification, with two *different source observers* explicitly retained.

**An exact counterexample to the naive identification:** at `p=13,r=2`,
[
F_2(z)=1-\frac{16}{11}z+\frac{16}{33}z^2,\quad
F_2(1/2)=\frac{13}{33},\quad
F_2'(1/2)=-\frac{32}{33}.
]
Hence `F/p=2 mod13`, `F'=1 mod13`, and the Gauss root digit is `a_F=11`. The original polynomial derivative is `D=6 mod13`, so its root digit is `a_W=2`. Consequently `xi_13 != zeta_13 mod 13^2`. No native CM/Frobenius map has been asserted here: the counterexample is only to *unmodified equality of these two explicitly defined p-adic roots*. A future Frobenius-to-weighted map must preserve the nontrivial root-transport correction rather than silently identify the points.

## Exact finite arithmetic witness

A standalone JavaScript BigInt computation was **executed** in this research run, on all 77 primes `p<=2000` in classes 13 and 19 modulo 24. It generated the Gauss coefficients by `f_k/f_(k-1)=(-r+k-1)(-2r+k-1)/[k(k-p/2)]`, and the *original weighted-216* coefficients independently from
`b_k/b_(k-1)=(2k-1)(3k-2)(3k-1)/(36 k^3)`; for derivatives each original weighted term was multiplied by `2k` and `4k(k-1)` respectively at `z_0=1/2`. Arithmetic was exact modulo `p^3`; inverse denominators were verified units by extended Euclid.

All 77 passed: Gauss differential-equation check `F''+F'=0 mod p`; two slope/curvature identities; exact quadratic Taylor root equation modulo `p^3`; and equivalence of the slope-only baseline and the original second digit. The previously known `W=p mod p^3` was independently reproduced in these *finite* cases; it is not used to prove Theorems 1–3. All **77/77 sampled first digits differ** (`a_F!=a_W`); this observed finite count is not asserted as an all-prime inequality.

|p|F/p mod p|F' mod p|D mod p|D mod p²|B'' mod p|a_F|a_W|original root mod p³|baseline mod p³|
|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
|13|2|1|6|136|8|11|2|449|449|
|19|5|2|5|195|13|7|15|1549|1549|
|37|not recorded|not recorded|not recorded|not recorded|not recorded|17|8|not recorded|same as root|
|43|not recorded|not recorded|not recorded|not recorded|not recorded|18|39|not recorded|same as root|
|373|314|215|211|29305|157|290|274|19928085|19928085|

Reproduction: reuse `research_notes/portable_direct/d25_cm_simple_root_checker_20261104.py` (published at commit `7e529b7f873b82b684d4cc8a259fa7951e0a9e1e`) and, inside each target-prime branch, assert `(3*W2-4*W1)%p==0`; compute `D=W1 mod p^2`, `q=W*inverse(D,p^3)`, `delta=-q-2*q*q/3 mod p^3`, and compare with `qbase=p*inverse(D,p^3)`, `delta_base=-qbase-2*qbase*qbase/3`. The original script already checks the literal evaluation of `B_p` at its root; the additional calculations were separately executed with JavaScript BigInt this run. No floating point, approximate sampling or native-class replacement is involved.

## Observer/provenance, result scope and next action

BRC-style carrier: `(p,k,c_k,v_p(c_k),z)`; separate observers are `F_r`, its Gauss Hensel point `xi_p`, the original weighted `B_p`, slope `D`, its root `zeta_p`, and baseline `z_p^{base}`. The map `delta -> delta+(2/3)delta^2` is invertible *on the explicit p-adic neighborhood and to precision p^3*, so it preserves exactly the second-digit residual; it is not an X6/native-space identification. The root discrepancy is a real fiber difference, not an algebraic permission to erase the CM source.

This unit resolves the specific proposed **identity map** between finite Gauss root and original weighted root (it fails at 13); it also removes an independent curvature input from the weighted second-digit Hensel baseline. The **still-open smallest scientific step** is a *source-authenticated independent CM/Frobenius-to-original-weighted-root transport* that predicts the nontrivial first displacement and then the second digit without evaluating `W mod p^3`; otherwise return to F4 signed Green/WZ cancellation. Preserving the original-class native `p=373` H0/B0 divided-power benchmark remains mandatory: module rank, original `[X]U mod139129`, semilinear Frobenius/basis eta, signed odd Green/Hesse, kappa and independent replay (support #1559; PENDING_OWNER at latest read). An ordinary Gauss/Hasse polynomial is not that native experiment.

Control: on this run GitHub author-side access was available; the MCP Site client remained static read-only with `research_authority_granted=false`, `write_relay_enabled=false`; exact Source continuation returned `CONTROL_QUOTA`, original gateway request receipt `research-onhour-20261031-0205-dispatch-r15` returned `CONTROL_REQUEST_NOT_FOUND` (previous separately recorded GitHub receipt was FAILED / UPSTREAM_CODE_REVIEW_REQUIRED). No new Source CLAIM/run/session/Result or native computation is claimed. This document is solely a proposed author-side mathematical checkpoint, never a substitution for authenticated publication/admission or reviewer independence.
