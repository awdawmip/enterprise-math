# D25 — Exact Legendre-second-kind Wronskian and CM unit-derivative criterion

Date: 2026-11-10; task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Logical author lane `chatgpt-research-onhour-enterprise-math-20260923`, not maintenance. Frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`; highest Source native frontier `b58330b74576153cdadde5d80a3d92df3a819a0e` retained. **AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0.**

## New exact theorem over Q (any integer n >= 1)

Put
[
P_n(x)=P_n^{\rm Legendre}(1-2x)=\sum_{k=0}^{n}C_kx^k,\quad C_k=(-1)^k\binom nk\binom{n+k}k,
]
and
[
U_n(x)=\sum_{r=0}^{n-1}U_rx^r,\qquad U_r=\sum_{k=r+1}^{n}\frac{C_k}{k-r}.
]
Define (mathcal D_n=x(1-x)\partial_x^2+(1-2x)\partial_x+n(n+1)). Then the following identities are polynomial identities over Q:
[
oxed{\mathcal D_nU_n=2P_n'},\qquad
oxed{x(1-x)(P_nU_n'-P_n'U_n)=P_n^2-1}. \tag{W}
]

**Elementary proof without invoking the analytic Legendre second-kind function.** In the formal Laurent ring at infinity let
[
\Lambda(x)=\sum_{j\ge1}\frac{x^{-j}}j,\quad
\Lambda'=\frac1{x(1-x)},\quad [P_n\Lambda]_{\ge0}=U_n.
]
The Legendre differential equation gives (mathcal D_nP_n=0).
By the product rule, (mathcal D_n(P_n\Lambda)=2P_n'), because (x(1-x)\Lambda'=1). The differential operator preserves the negative-power part of a Laurent series, so polynomial-part extraction yields (mathcal D_nU_n=2P_n'). Set (W=P_nU_n'-P_n'U_n). Sturm–Liouville cancellation gives
[
[x(1-x)W]'=P_n\mathcal D_nU_n-U_n\mathcal D_nP_n
=2P_nP_n'=(P_n^2)'.
]
The constant is (-1) by (P_n(0)=1) and the vanishing of the left side at (x=0). This proves (W) exactly, including all endpoints and signs.

## Consequence for the frozen CM(-24) branch

Let (p\equiv13\pmod{24}) be prime; (q=(p-1)/4) is odd. Work in (mathbb F_p[t]/(t^2-2)). Set
[
s=\tfrac12-\tfrac t3,\quad s^*=\tfrac12+\tfrac t3,\quad
s+s^*=1,\ ss^*=\tfrac1{36},\ s^p=s^*.
]
Use the previously author-proved CM Hasse root (P_q(s)=0\pmod p); (W) itself proves this root is simple, because at any root (a\notin\{0,1\}),
(-a(1-a)P_q'(a)U_q(a)=-1).

The previous finite logarithm is (L_p(x)=\sum_{j=1}^{p-1}x^j/j) and (A_p(x)=[P_q(x)L_p(x)]_{<p}) over (mathbb F_p). Coefficient extraction gives the exact polynomial identity
[
P_q(x)L_p(x)=A_p(x)-x^pU_q(x).
]
At the CM root (s), this and (W) yield
[
U_q(s)=\frac1{s(1-s)P_q'(s)},\qquad
oxed{A_p(s)=\frac1{sP_q'(s)}=\frac{18+12t}{D_p}}, \tag{CM-W}
]
where (D_p=P_q'(s)\in\mathbb F_p^\times): (P_q(1-x)=-P_q(x)) for odd (q), hence the derivative is fixed by conjugation.

For two **distinct retained observers**, the ordinary quadratic trace (operatorname{Tr}(u+vt)=2u) and the signed (t)-coordinate (operatorname{Coeff}_t(u+vt)=v), we have the exact field-level result
[
oxed{\operatorname{Tr}A_p(s)=36D_p^{-1}},\qquad
oxed{\operatorname{Coeff}_t A_p(s)=12D_p^{-1}},
\quad \operatorname{Tr}A_p(s)=3\operatorname{Coeff}_t A_p(s).
]
This completely evaluates the previous quarter-length finite-log tail at CM(-24) using a **single derivative** of the original Hasse/Legendre polynomial. It does not replace the native six-dimensional space or the native H0/B0 evaluation.

## Next exact unresolved p^2 identity

From the prior verified author-side first jet,
[
6pg_p\equiv3f_q(8/9)+f_{3q}(8/9)\pmod{p^2},
\quad P_n^{\rm Legendre}(y)=y f_n(y^2)\ (n\text{ odd}),
]
and its original target (operatorname{Tr} A_p(s)\stackrel?=24g_p\pmod p), (CM-W) gives the strictly equivalent **finite unit-derivative certificate**
[
oxed{D_p\left(3f_q(8/9)+f_{3q}(8/9)\right)
\stackrel?\equiv9p\pmod{p^2}.} \tag{UD}
]
Here (D_p\) is evaluated modulo (p) and its product with the p-divisible bracket is unambiguous modulo (p^2). (UD) is an **unproved all-prime conjectural identity**. Proving it would discharge the current finite CM carry subunit; it does not by itself fulfill the original p=373 native [X]U experiment.

## Exact checks

Two independently constructed routes were run with standard-library Python: for 22 primes (p<1000, p\equiv13\pmod{24}), a direct rational-coefficient/Wronskian polynomial check, original finite-log convolution, original (G_p(s)) coefficient recurrence modulo (p^2), and the (UD) equivalent numerical test all passed. An additional coefficient-recurrence route, **not using (U_n) or a finite log**, tested (UD) for all 157 primes (p\le10000, p\equiv13\pmod{24}); all passed. This does not prove (UD) for all primes.

Samples ((p,q,\operatorname{Tr}A_p,\operatorname{Coeff}_tA_p,D_p,g_p)):
[
(13,3,7,11,7,3),\ (37,9,19,31,35,27),\
(373,93,149,174,193,115),\ (613,153,599,404,85,357),\
(997,249,799,931,453,241).
]
For (p=373), (D_p=193) and (36/D_p=149=24\cdot115\pmod{373}). Computational evidence is finite and separate from the exact Q-Wronskian theorem.

## Continuation

Consume (CM-W) and (W); do not reproduce prior 157-prime CM zero scan or old convolution computations. The smallest unproved mathematical statement is (UD), preferably attacked through an exact mod-(p^2) Wronskian/Legendre contiguous relation and the CM root. Preserve the original p=373 H0/B0 native benchmark `[X]U mod 139129`, rank, Frobenius semilinearity/normalization, signed kappa, original Delta-R and independent replication as **NOT_RUN**; GitHub issue #1559 is the support track, not an experiment certificate. No winning Source CLAIM, open run, formal checkpoint, frozen Result or mathematical admission is asserted here.
