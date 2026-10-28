# D25/LIFT — exact kernel-pair research route: p³ matching, p⁴ and analytic no-go

Date: 2026-10-28 21:23 Asia/Hong_Kong.
Mode: AUTHOR-SIDE / ONE EXACT ANALYTIC NO-GO PROOF / 781 FINITE PRIME TRANSPORT CHECKS / NOT A UNIVERSAL p³ PROOF / UNREVIEWED / NOT_ADMITTED / NATIVE_NOT_EXECUTED.
Logical Research conversation: chatgpt-research-onhour-enterprise-math-20260923, not the maintenance lane.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
P000 and ACTIVE six-axis/3D-slice worldview remain unchanged; both are external auxiliary signed scalar sums.

## Two different original full-cutoff kernels

For every prime p>3, set
\[
A_p=\sum_{n=0}^{p-1}(6n+1)
\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n},
\qquad
B_p=\sum_{n=0}^{p-1}(8n+1)
\frac{\binom{2n}{n}^{2}\binom{4n}{2n}}{48^{2n}}.
\]
Thus the previously studied original-216 W_p equals A_p. Denominators 216 and 2304 are p-units.

The **published external theorem** of Guo–Zudilin, "A q-microscope for supercongruences", Advances in Mathematics 346 (2019), 329–358, arXiv:1803.01830, proves
\[
B_p\equiv p\Bigl(\frac{-3}{p}\Bigr)\pmod{p^3}
\quad\text{for all primes }p>3,
\]
both full p-1 and shorter (p-1)/2 truncations. See https://arxiv.org/abs/1803.01830 and https://www.arxiv.symmetricfunctions.com/paper/1803.01830v6 .
This theorem is for B, **not** the original A. Its import requires the still-unproved original-full-cutoff transport
\[
\boxed{A_p\stackrel?{\equiv}B_p\pmod{p^3}.}\tag{transport conjecture}
\]
PROVING this transport would directly close the scalar original-216 character conjecture using published prior art; merely checking finite primes does not prove it.

Exact finite work: a freshly executed standard-library checker compared A and B modulo p³ on all 781 primes 5<=p<6000, retaining both entire n=0,...,p-1 ranges, and found equality in every case. Of those 194 were p=13,19 mod24. Original B was independently evaluated with its integer binomial formula at eight primes. For p=373, A=B=373 modulo 373³. This is an experimentally supported reduction route, not an accepted theorem.

## Proved no-go: naive exact analytic equality is impossible

Let A_n and B_n be the positive individual summands for n>=0 from the *infinite real series* corresponding to A and B. They are absolutely convergent: the respective successive unweighted term ratios approach 1/2 and 1/9.

For every n>=1,
\[
\frac{A_n}{B_n}=
\frac{6n+1}{8n+1}\left(\frac92\right)^n
\frac{(1/3)_n(2/3)_n}{(1/4)_n(3/4)_n}.
\]
Each factor [(j+1/3)(j+2/3)]/[(j+1/4)(j+3/4)] exceeds 1 for integer j>=0, because
\[
(j+1/3)(j+2/3)-(j+1/4)(j+3/4)=2/9-3/16=5/144>0.
\]
Furthermore (6n+1)/(8n+1)>3/4, so the summand ratio exceeds (3/4)*(9/2)^n >=27/8>1. Therefore A_n>B_n for all n>=1. At n=1,
\[
A_1-B_1=\frac7{18}-\frac3{32}=\frac{85}{288}.
\]
The n>=2 differences are strictly positive. Hence the **exact** no-go theorem
\[
\boxed{\sum_{n=0}^{\infty} A_n-\sum_{n=0}^{\infty} B_n>\frac{85}{288}>0.}
\]
Consequently, a proof of the p-adic transport cannot simply assert that the two ordinary analytic Ramanujan series coincide termwise or as full series without a nontrivial prefactor/transform and correctly treated finite-cutoff error.

## Precise p⁴ counterexample to an overstrong transport

A **separate executed, exact-integer** computation shows
\[
A_7-B_7\equiv4\cdot7^3\pmod{7^4},
\quad
A_{373}-B_{373}\equiv114\cdot373^3\pmod{373^4}.
\]
Thus the superficially stronger A_p=B_p mod p⁴ claim is **false**, including the original p=373 target-class witness. The expected transport precision must remain mod p³; replacing this with an unproved p⁴ claim would be incorrect.

Original hypergeometric recurrence for the 216 kernel:
t_(n+1)/t_n=(2n+1)(3n+1)(3n+2)/[36(n+1)^3].
For the published 2304 kernel:
s_(n+1)/s_n=(2n+1)(4n+1)(4n+3)/[288(n+1)^3].
The two distinct weights 6n+1 and 8n+1 must be retained. The natural operator statement is [(1+6theta) 3F2(1/2,1/3,2/3;1,1;z)] at z=1/2 versus [(1+8theta)3F2(1/2,1/4,3/4;1,1;z)] at z=1/9, with full finite truncations.

## Reproduction and BRC/observers

Exact checker: research_notes/portable_direct/d25_onhour_dual_kernel_transport_p4_falsifier_20261028.py.
Actual stdout:
PASS_MOD_P3_INTER_KERNEL_OBSERVATION 781 primes <6000; frozen target count 194
EXACT_ANALYTIC_NAIVE_IDENTITY_FALSIFIED A_infinity-B_infinity > 85/288
P4_COUNTEREXAMPLE_CERTIFICATES [(5, 0), (7, 4), (13, 11), (19, 6), (31, 11), (37, 28), (43, 31), (61, 34), (67, 61), (73, 23), (211, 96), (373, 114)]
P373 (373, 373) delta_p4_digit 114

BRC COMPOSE_APPLIED to paired, labeled term sequences (n,A_n,B_n), not a quotient equating their individual terms: readout is (A_p-B_p) mod p³ and, separately, its p⁴ residual. The p⁴ residual and positive real-series defect are exact witnesses that the observer changes under precision extension/analytic completion. These do not invalidate the narrower p³ finite conjecture. Keep indexed signs, multiplication constants, prime valuations and the original tail.

## Continuation/authorization

Preserve prior author-side fixed-row moment note at EM immutable commit 8a393235fff0a578ab9af1d8a73f31e09c67ec88 and all accepted parent D24 UR work without recredit. Next narrow proof obligation: construct a finite p³ weighted hypergeometric transformation/WZ pair proving A_p-B_p=0 modulo p³ with its full p-1 endpoints; check the resulting p⁴ defect at p=7 and 373 as mandatory negative controls. Source authority remains absent for this Site client; no Source CLAIM, run, Result or Research-Activity claimed. Native support Issue #1559 still requires an actual authorized original p373 H0/B0 divided-power [X]U mod139129, rank, Frobenius and signed Green/Hesse/kappa/Delta-R, PENDING_OWNER at last read. Formal checkpoint and independent review remain pending.
