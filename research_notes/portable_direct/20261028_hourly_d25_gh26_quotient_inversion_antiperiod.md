# D25/LIFT GH-26 — one-variable quotient and inversion-antisymmetric F moment

2026-10-28. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Auxiliary finite-field source mathematics, not native Source checkpoint or reviewed Result. Predecessors GH-22 and GH-24/25. Research logical lane chatgpt-research-hourly-enterprise-math-20260923, not maintenance chatgpt-hourly-enterprise-math-20260921. Preserve frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3, task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7 and open Objective.

## GH-26 (theorem)

Let p=8m+3>=11 be prime, chi its quadratic character, U=F_p\{0,-1,-1/9}. Retain GH-22's *labeled* source and GH-24's quotient observer:
\[
h(x)=\chi(x)[x(1+x)]^{3m+1}(1+9x)^m,\qquad
v=\phi(x)=\frac{1+9x}{9x(1+x)}.
\]

**(a) Source-preserving pointwise collapse.** For every x in U,
\[
\boxed{h(x)=9^m\phi(x)^m\chi(1+x).}\tag{GH-26a}
\]
Proof: 1+9x=9v x(1+x), hence h=9^m v^m chi(x)[x(1+x)]^(4m+1). Because 4m+1=(p-1)/2 and chi(x)^2=1 on U, the latter is 9^m v^m chi(1+x). No zero denominator or excluded source is used.

**(b) Exact quotient-fiber discriminant and character trace.** For v in F_p^×, put t=1+x. The fiber phi(x)=v is exactly the root set of
\[
9v t^2-9(v+1)t+8=0.
\]
Define D(v)=9v^2-14v+9, n(v)=1+chi(D(v)), and
\[
\Sigma(v)=\sum_{\phi(x)=v}\chi(1+x).
\]
Since the quadratic discriminant is 9D(v), n(v) is exactly 0, 1 or 2, the number of *rational* roots. For two distinct roots t,t', tt'=8/(9v), so chi(t)chi(t')=chi(2)chi(v)=-chi(v), using p=3(mod8). Thus Sigma(v)=0 whenever chi(v)=+1; when chi(v)=-1 and the fiber is occupied, the root characters agree. For such a fiber choose either x_v and define sigma(v)=chi(1+x_v); then Sigma(v)=n(v)sigma(v), independent of root choice. A repeated root can occur only in a nonsquare-v fiber, because its product is a square.

**(c) Exact inversion anti-period.** The GH-24 involution B(x)=1/(9x) maps phi(x)=v to phi(Bx)=v^{-1}, while 1+Bx=v(1+x). Consequently
\[
\boxed{\Sigma(v^{-1})=\chi(v)\Sigma(v).}\tag{GH-26b}
\]
For occupied nonsquare fibers this is strict anti-invariance. The only nonsquare self-inverse v can be -1 (because chi(-1)=-1); it has no F_p fiber, since D(-1)=32 and chi(32)=chi(2)=-1.

Let R choose one representative of each inversion pair {v,v^-1} of *occupied nonsquares*. The complete original GH-22 F moment has the **exact single-variable source-aware representation**
\[
\boxed{S_F:=\sum_{x\in F_p}h(x)
=9^m\sum_{v\in R}(v^m-v^{-m})n(v)\sigma(v).}\tag{GH-26c}
\]
Proof: by GH-26a, S_F=9^m sum_{v in F_p^×}v^m Sigma(v), since all three excluded affine x have h=0. Square-v fibers have zero Sigma. Pair each occupied nonsquare v with its distinct inverse using GH-26b, yielding v^m Sigma(v)+v^-m Sigma(v^-1)=(v^m-v^-m)n(v)sigma(v). Under a change of pair representative, both factors reverse sign, so the product is canonical. QED.

**Careful meaning.** This does NOT replace source signs by the positive multiplicity n(v). The sign repair sigma(v), original x labels and the G port remain necessary. GH-22's G weight is h(x)(5-9x)/(1+9x) on U, and at p=11 its excluded point x=-1/9 contributes 3 modulo 11, so an F-only quotient cannot silently prove G-channel cancellation or its finite endpoints.

## Exact nontrivial finite certificates

At p=11 (m=1), the only occupied nonsquare inversion pair is (v,v^-1)=(7,8), n=1, Sigma(7)=-1, yielding contribution S_F=9 (mod11), not zero. At p=19 (m=2), the three representative pairs, with columns (v,v^-1,n,Sigma(v),weighted contribution), are
(2,10,2,2,9), (8,12,2,2,17), (14,15,1,-1,12).
Their sum is 9+17+12=38=0(mod19), although every individual contribution is nonzero. This strengthens GH-24's exact obstruction: the target global zero requires cancellation among *distinct signed quotient fibers*, not each fiber vanishing.

The companion pure Python standard-library checker exhaustively verified weight collapse, every quadratic fiber, inversion transport and complete moment formula for **all 76 primes p<2000 with p=3(mod8)**. It reported PASS_GH26_EXACT_POINTWISE_WEIGHT_COLLAPSE_AND_FIBER_DISCRIMINANT and PASS_GH26_INVERSION_ANTISYMMETRIC_QUOTIENT_MOMENT. Finite checking is not a proof of the universal claim; the preceding argument is.

BRC: COMPOSE_APPLIED GH-22 signed original source + GH-24 V4 quotient and a mandatory sign/branch observer (v,n,sigma,inversion_pair). Keep (p,m,x,phi,chi(1+x),F/G source) and excluded endpoint labels, not merely multiplicity n or the elliptic trace. This proves only finite-field auxiliary scalar formulas, no complete X6 native dynamics, Hasse/W/S transfer or p=373 native experiment.

**Next exact action:** find an actual prime-dependent relation among the surviving signed inverse pairs that forces the GH-26c total to vanish for all p=19(mod24), or construct a counterexample. Do not invoke the order-three Möbius symmetry excluded by GH-23, or characteristic-zero CM on GH-25's proved non-CM E. Only after closing the F-branch should GH-15/16 Laurent counterterms, GH-20/21 p-adic moments, R23/R36 Green coupling and H0/B0/[X]U/Frobenius/native p373 obligations be advanced as such. Current Site research grant absent and one read-only continuation returned CONTROL_QUOTA, so native CLAIM/open/Source checkpoint and independent Driver admission remain unverified.