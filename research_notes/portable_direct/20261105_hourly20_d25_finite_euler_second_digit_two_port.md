# D25 — Finite Gauss–Jacobi Euler second digit, cutoff-tail supports and two-port CM transport

Date: 2026-11-05. TASK_RESEARCH author-side portable evidence; task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. AUTHOR-DERIVED / EXACT POLYNOMIAL PROOF / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED. Consumes earlier three-band Gauss–Hasse and CM first-jet notes, not native H0/B0.

## First-digit finite Euler remainder as a genuine p² source

Let p=8q+5 be prime >=5, ell=(5p-1)/8, N=(p+1)/2. In the p-local ring modulo p² set
\[
f_k={(1/8)_k(3/8)_k\over (k!)^2},\quad F_p^{lo}(x)=\sum_{k=0}^{\ell}f_kx^k,\quad
G_q(x)=\sum_{j=0}^q {q\choose j}{3q+1\choose j}x^j=J_p(9x).
\]
The earlier coefficientwise finite Euler congruence \(F_p^{lo}\equiv(1-x)^N G_q\pmod p\) defines the unique polynomial
\[
\boxed{K_p(x)=[F_p^{lo}(x)-(1-x)^NG_q(x)]/p\bmod p.}\tag{1}
\]
It has K_p(0)=0 and exact first coefficient
\[
\boxed{[x]K_p={3(18-p)\over64}\equiv{27\over32}\ne0\pmod p.}\tag{2}
\]
Proof: \(f_1=3/64\), the first coefficient of G is \(q(3q+1)=(3p^2-22p+35)/64\), and the first coefficient of (1-x)^N is minus N. Subtract and divide by p.

Write \(u=(8/9)^N\). Evaluating and differentiating (1) in the full polynomial ring (prior to choosing an algebraic branch) proves the two exact ports
\[
\boxed{F_p^{lo}(1/9)\equiv uJ_p(1)+pK_p(1/9)\pmod{p^2},}\tag{3}
\]
\[
\boxed{(F_p^{lo})'(1/9)\equiv u[9J_p'(1)-9N J_p(1)/8]+pK_p'(1/9)\pmod{p^2}.}\tag{4}
\]

## Precisely supported upper cutoff tail

Extend the recurrence \(f_k=f_{k-1}(8k-7)(8k-5)/(64k^2)\) to k<p. The first numerator p-factor appears at k=ell+1=5q+4 (8k-7=5p); the second appears at k=7q+5 (8k-5=7p). Consequently all coefficients after ell vanish mod p, and all coefficients at k>=7q+5 vanish mod p². Define
\[
\boxed{U_p(x)=\sum_{k=\ell+1}^{7q+4}(f_k/p\bmod p)x^k.}\tag{5}
\]
At p=5, the first 5p is p², so U_5=0. At every p>5 the coefficient f_(ell+1)/p is a p-unit. This exact exception is necessary.

For the *full* p-term Gauss polynomial,
\[
\boxed{F_p^{full}(x)=\sum_{k=0}^{p-1}f_kx^k
\equiv(1-x)^NG_q(x)+p[K_p(x)+U_p(x)]\pmod{p^2}.}\tag{6}
\]
All identities are coefficientwise, so are preserved by differentiation. In particular, the lower Euler remainder K and high-index cutoff U are distinct valuation/provenance ports.

## Original coordinate and CM jet synthesis

Reuse p-adic carry \(S_p=[B_p-a^pH_m]/p\pmod p\) from the preceding note, where \(a=t^2-6t+1\), \(B_p=(1+t)^dF_p^{lo}(x(t))\), \(d=(5p-1)/2\), \(H_m=\sum_{j=0}^m\binom mj^2t^j\), \(m=(p-1)/2\), \(x(t)=16t(1-t)^2/(1+t)^4\). Let \(Q=t^4-140t^3+294t^2-140t+1\), \(L=16t(1-t^2)\), \(c=1+2t-7t^2\), \(\mathcal D=L\partial_t+c\), \(C_m=\mathcal DH_m\), \(A_0=c(1+t)+dL\).

At Q=0, x=1/9 and Lx'=16a/9. Substitution of (3),(4) into the previously proved p² Gauss–Hasse first-jet equation gives the *exact* two-digit identity in \((\mathbb Z/p^2)[t]/Q\):
\[
\boxed{\begin{aligned}
a^{p+1}C_m\equiv&(1+t)^{d-1}\bigg\{
\frac{16a^2(1+t)}9\Big[u\big(9J_p'(1)-\frac{9N}{8}J_p(1)\big)+pK_p'(1/9)\Big]\\
&\qquad\qquad\quad+aA_0\big[uJ_p(1)+pK_p(1/9)\big]\bigg\}\\
&-p\{a\mathcal DS_p+La'(1+t)^duJ_p(1)\}\pmod{(p^2,Q)}.
\end{aligned}}\tag{7}
\]
The p-multiplied S_p terms use any integral lift of its modulo-p polynomial coefficients, differentiated **before quotient Q**. To substitute the full p-term Gauss F instead of F_lo, also use pU_p(1/9), pU'_p(1/9). The vector (branch, J, J', K, K', U, U', S, S', prefactor) retains all subsequent observer information and is a typed BRC source-preserving transformation in an auxiliary classical model.

## Exact checks, boundaries, and next task

Companion pure-stdlib checker computes f coefficients modulo p², Euler difference polynomial K and high-band U and independently checks BOTH first-jet ports, for all 11 listed primes p=5,13,29,37,53,61,101,149,173,197,373: PASS. An additional joint checker recomputes the CM quartic source using the earlier Gauss–Hasse script and verifies equation (7) in \((\mathbb Z/p^2)[t]/Q\) for all five split primes p=5,29,53,101,149: PASS.

For p373 q46, ell233, N187: K(1/9)=265, K'(1/9)=202, U(1/9)=232, (K+U)(1/9)=124, and (x∂_x)(K+U)(1/9)=176 modulo373. For p5 K(1/9)=3,U=0. Values here are from this finite Gauss truncation's definition. Earlier Green note's e0=119,e1=71 belong to another normalization; no unsourced identification is made.

The original frozen D24/LIFT mother objective remains \(\Delta_p-R_p\equiv0\pmod p\) for primes p mod24 in {13,19}. Next: compare (7) with earlier short Jacobi Green–Wronskian W(1) at the **same p and normalization**, keeping exact cutoff, Euler and inverse-branch signs, and produce a proof or exact counterexample. Native original-class p373 H0/B0, [X]U mod p², Frobenius direction, eta/kappa and independent review remain separate. No native new Researcher session, CLAIM, OPEN, Source checkpoint, Result or mathematical admission is asserted.