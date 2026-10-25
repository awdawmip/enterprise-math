# D25/LIFT — reflected second-Jacobi-jet as a cross-source Jacobi operator partner

2026-10-25. TASK_RESEARCH logical lane: chatgpt-research-hourly-enterprise-math-20260923. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged.

Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / NO_NEW_NATIVE_CHECKPOINT. All z-operators here are external finite-field hypergeometric algebra, not native X6 geometry, actual CM Frobenius or a final LIFT proof.

## Question and new result

Previous work proved the original signed Clausen corner in terms of the terminating Jacobi coefficients and the reflected second parameter jet. A self-Green pairing of the terminating polynomial with its own second jet proved redundant. Here the *reflected* jet, a distinct source/rank branch, becomes an explicit negative-Laurent partner of the SAME Jacobi operator. Two unavoidable boundary terms, a universal -2 and a nonzero bottom edge, remain visible. The original signed corner becomes an exact nonnegative-rank trace of the product, rather than a self-pairing.

For p=6m+1 >=7 prime, work in F_p after the exact rational formula. Define

\[
b_n(x)=\frac{(-x)_n(-2x)_n}{(n!)^2},\quad
u_j=b_j(m)=\binom mj\binom{2m}j\ (0\le j\le m),\quad
w_n=\tfrac12 b_n''(m),\quad c_\ell=w_{p-\ell}\ (1\le\ell\le m).
\]

Consume the previously author-proved source relation Q_p/p^2 = T_jet,p (mod p), with
\[
T_{\rm jet,p}=\frac1{18}\sum_{1\le\ell\le j\le m}
(6(j-\ell)+1)u_jc_\ell\,2^{-(j+p-\ell)}\pmod p. \tag{0}
\]
This is the original signed *ordered* cutoff, not an unsigned support count.

## Theorem 1: factorial complement and recurrence

For 1<=ell<=m the exact rational double-zero derivative is
\[
w_{p-\ell}=2(-1)^m
\frac{m!(2m)!(5m-\ell)!(4m-\ell)!}{((p-\ell)!)^2}.
\tag{1a}
\]
Wilson factorial complement k!(p-1-k)!=(-1)^{k+1} modulo p gives
\[
\boxed{c_\ell=2\frac{m!(2m)!((\ell-1)!)^2}
{(m+\ell)!(2m+\ell)!}\pmod p.} \tag{1b}
\]
Consequently all c_ell are units, and
\[
\boxed{c_1=\frac{2}{(m+1)(2m+1)}=\frac{18}{5},\qquad
c_{\ell+1}=c_\ell\frac{\ell^2}{(m+\ell+1)(2m+\ell+1)}.} \tag{1c}
\]
All displayed denominators are units on precisely this finite index range.

Proof: for n>2m, the two Pochhammer products each have one simple zero at x=m (indices m and 2m). Their derivatives are (-1)^{m+1}m!(n-m-1)! and -2(2m)!(n-2m-1)!. Half the second derivative of their product equals the product of those first derivatives. Apply the stated Wilson complement to 5m-ell, 4m-ell and p-ell; keep both signs until cancellation. Take consecutive quotients. This is algebraic for every eligible prime.

## Theorem 2: cross-source differential identity and two boundary fluxes

Write theta=z d/dz and
\[
\mathcal L_m=\theta^2-z(\theta-m)(\theta-2m),\quad
U(z)=\sum_{j=0}^m u_jz^j,\quad
V(z)=\sum_{\ell=1}^m c_\ell z^{-\ell}\in\mathbb F_p[z,z^{-1}].
\]
Then, coefficientwise in the Laurent ring,
\[
\boxed{\mathcal L_mU=0,\qquad
\mathcal L_mV=-2+E_mz^{-m},\quad E_m=m^2c_m\ne0.}\tag{2}
\]
Proof: (j+1)^2u_{j+1}=(m-j)(2m-j)u_j proves L U=0 including the terminating edge. For -m< -ell <0, the L V coefficient is ell^2 c_ell-(m+ell+1)(2m+ell+1)c_{ell+1}=0 from (1c). At z^0, the uncancelled coefficient is -(m+1)(2m+1)c_1=-2. At z^{-m}, no c_{m+1} exists to cancel m^2c_m. Factorial formula (1b) proves the bottom edge is a unit; two boundary contributions may nevertheless cancel at selected observation points.

With D_m=L_m/z=z(1-z)d_z^2+[1+(3m-1)z]d_z-2m^2 and cross-source W=UV'-VU', the exact F_p Laurent Green identity is
\[
\boxed{z(1-z)W'+[1+(3m-1)z]W
=U(-2z^{-1}+E_mz^{-m-1}).}\tag{3}
\]
This comes from U D_m V-V D_m U, not the earlier self-Green identity. Evaluating W alone does not recover the original signed corner; rank projection is required.

## Theorem 3: the signed original Clausen trace is a projected cross-source product

Let Pi_+ retain *only* exponents >=0. Let
\[
P(z)=\Pi_+(U(z)V(z))
=\sum_{1\le\ell\le j\le m}u_j c_\ell z^{j-\ell}.
\]
Then
\[
\boxed{T_{\rm jet,p}=
\frac1{36}[(1+6\theta)P(z)]_{z=1/2}\pmod p.}\tag{4}
\]
Proof: Pi_+ implements exactly the original ordered cutoff j>=ell and preserves every signed branch; 1+6theta supplies weight 6(j-ell)+1. Evaluation gives 2^{-(j-ell)} and (0) contains the extra 2^{-p}=1/2 mod p, hence 1/36. Crucially, evaluating UV *before* projecting merges negative and nonnegative ranks and loses the declared source operation.

Computational corollary: with S0(j)=sum_{ell=1}^j 2^ell c_ell and S1(j)=sum_{ell=1}^j ell 2^ell c_ell,
\[
\boxed{T_{\rm jet,p}=\frac1{36}\sum_{j=1}^m
2^{-j}u_j[(6j+1)S0(j)-6S1(j)]\pmod p.}\tag{5}
\]
Use (1c) and the recurrence for u_j to update both signed prefix moments. This evaluates the original rank-preserving observer in O(m) modular operations and O(1) work registers, versus the O(m^2) direct corner.

## Author checks and implications

Companion exact checker compares the two independent factorial expressions for each w_{p-ell}, all coefficients of the Laurent operator, the positive-rank trace, and the O(m) signed prefix implementation. It ALSO evaluates Q_p from its *original* (1/6)_n(1/3)_n/(2^n(n!)^2) recurrence modulo p^3 with the complete signed ordered pair sum, for all 35 primes p=1 mod6 in [7,373]. All 35 match Q_p/p^2 = equation (4). The larger p=1327 and 19963 pass the reflection/operator/trace checks; the expensive original Q double sum was not run there.

Examples (p,c1,E_m,T_jet): (7,5,5,3), (13,1,11,0), (19,15,5,12), (37,11,15,11), (43,38,4,15), (373,302,245,196), (1327,269,1161,48), (19963,15974,2576,13363). Finite validation corroborates, but does not replace, the explicit all-prime algebraic proofs. No independent math review, native CM measurement or frozen Result occurred.

BRC COMPOSE_APPLIED: signed source-indexed carrier (j,ell,u_j,c_ell,j-ell), allowed future operators Pi_+, 1+6theta, z=1/2 and L_m. Retaining negative Laurent ranks, valuation/two-jet origin, both boundary terms and the actual ordered cutoff is necessary for subsequent operations. Positive mass is not signed amplitude. These external scalar z formulas are not declared a complete native three-dimensional X6 slice.

Next smallest mother-goal unit: apply (2) and projection (4) to derive a closed forced differential identity or telescoping antidifference for P, then compare its explicit signed z=1/2 trace with the independently retained B_01,p+A_2H_0/72. Only an actual all-target-prime equality closes the Jacobi LIFT; true original-class CM H_0/B_0, [X]U mod p^2, semilinear normalization and kappa mapping remain separately unverified. Current ordinary-control predecessor mismatch/quota is tracked by Enterprise Math Issue #1558; do not treat these author notes as an authorized CLAIM/run/native Source checkpoint. Keep source pin, old Source checkpoint/contribution history, scheduler and notifications unchanged.
