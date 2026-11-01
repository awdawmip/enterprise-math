# D25/LIFT — A216 one-scalar spectral perturbation (p³)

2026-10-29. AUTHOR-SIDE / EXACT ALGEBRA / EXECUTED INTEGER CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_H0_B0_NOT_EXECUTED. No native Result, independent review, all-prime proof of LIFT or original H0/B0 experiment is claimed.

Mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; unchanged frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research conversation chatgpt-research-onhour-enterprise-math-20260923, distinct from maintenance conversation chatgpt-hourly-enterprise-math-20260921. Accepted CM0/UR, frozen-R source alignment and prior degree-cutoff theorems are inputs, not newly claimed accomplishments.

## New all-p≡1(mod6) algebraic theorem

Let p=6m+1>=7 be prime; work over Z_(p)/p³. Define
\[
\lambda=p(p+1)/36,\quad q_n=(n-m)(n+m+1/2),\quad
c_n(\lambda)=\frac{\prod_{a=0}^{n-1}(q_a+\lambda)}{(n!)^2}\ (n<p).
\]
The **exact rational** identity
\[
\boxed{q_n+\lambda=(n+1/6)(n+1/3)}\tag{1}
\]
shows that the original A216 companion is
\[
S_A(z)=\sum_{n=0}^{p-1}(1/6)_n(1/3)_nz^n/(n!)^2
=\sum_{n=0}^{p-1}c_n(\lambda)z^n.
\]
Write d_{n,j}=[λ^j]c_n(λ) for j=0,1,2, initialize d_{0,0}=1 and d_{0,1}=d_{0,2}=0 and put d_{n,-1}=0. The exact jet recurrence
\[
\boxed{d_{n+1,j}=(q_nd_{n,j}+d_{n,j-1})/(n+1)^2}\tag{2}
\]
**never divides by q_n** (which is zero when n=m). Its only denominators are p-units since n<p. Setting F_j(z)=Σ_{n<p}d_{n,j}z^n gives the all-prime coefficientwise identity
\[
\boxed{S_A(z)\equiv F_0(z)+\lambda F_1(z)+\lambda^2F_2(z)\pmod{p^3}.}\tag{3}
\]
F_0={}_2F_1(-m,m+1/2;1;z) terminates at n=m, whereas F_1,F_2 retain all original n<p and second p-hit information. The single scalar λ shifts the hypergeometric differential eigenvalue without changing z or original coefficient provenance.

## Original signed observer, not a surrogate

At the **fixed original** z=1/2 let Θ=z∂z, f_j=F_j(1/2), h_j=[(1+12Θ)F_j]_(1/2). Project original polynomial degrees n<p before applying the signed weight 1+6Θ. The classical Clausen coefficient identity gives A_p=[(1+6Θ) Π_<p S_A(z)²]_(1/2), and the full weighted square equals g h with g=S_A(1/2), h=[(1+12Θ)S_A]_(1/2). Use the separately established, original high-degree equality [weighted Π_>=p S_A²]_(1/2)≡p²R_p (mod p³), where R_p is the authentic frozen reflected scalar, **not** either low-cutoff quotient.

Substitution gives a new source-preserving exact p³ reduction:
\[
\boxed{\begin{aligned}
A_p\equiv{}& f_0h_0+\lambda(f_1h_0+f_0h_1)\\
&+\lambda^2(f_2h_0+f_1h_1+f_0h_2)-p^2R_p\pmod{p^3}.
\end{aligned}}\tag{4}
\]
Only for frozen target classes p≡13,19(mod24), accepted CM0 supplies f_0≡0(mod p). The f_0h_2 term then vanishes at order p³:
\[
\boxed{A_p\equiv f_0h_0+\lambda(f_1h_0+f_0h_1)+\lambda^2(f_2h_0+f_1h_1)-p^2R_p\pmod{p^3}.}\tag{5}
\]
This leaves a genuine prime-sensitive cancellation obligation and does **not** prove uniform LIFT or Sun A14(ii). The λ² term is a distinguishable second-order source and cannot be discarded merely because it is absent at mod p².

## Exact executed integer evidence

Executed Python standard library integer script at research_notes/portable_direct/d25_a216_spectral_p3_guard_20261029.py. It checks the λ recurrence against an independent original 2F1 coefficient recurrence; the weighted square against an independent integer binomial original A216 sum; and original ordered-degree high carry against the frozen reflected nested double sum. Coverage is **all 45 primes p≡1 mod6 with 7<=p<500**, including 23 target primes. All assertions pass. λ² source is nonzero in each of the 23 tested target instances (finite evidence).

At p=373 (p²=139129, p³=51895117, m=62) the exact modular source ledger is:

| Source | Residue mod p³ |
| --- | ---: |
| f0*h0 | 18,377,337 |
| λ*(f1*h0+f0*h1) | 35,187,701 |
| λ²*(f2*h0+f1*h1+f0*h2) | 25,599,736 = **184p²** |
| original high R carrier | 27,269,284 = **196p²** |
| complete reconstructed g*h | 27,269,657 |
| original A_373 | **373** |

The mod-373 jets are (f0,f1,f2)=(0,327,102) and (h0,h1,h2)=(171,255,329). The two *separate* CM0-valid second-order terms evaluate to f2*h0/36²=29, f1*h1/36²=155 mod373; together 184. Omitting second order changes A_373 by -184p² modulo p³, a strict falsifier of the naive first-order transfer. Non-CM0 p=7,31 were checked using full (4), not the CM0-specialized (5).

BRC COMPOSE_APPLIED: preserve original degree cut, integer valuations, signed derivative observer, source history and spectral jet order as distinct typed carriers; the partial collapse to (5) uses accepted CM0 and cannot erase R or the native H0/B0 operator. No P000, ACTIVE worldview or original native six-axis claim is modified.

## Continuing obligations

Next mathematical action: find a p-sensitive, exact terminating Jacobi/Gegenbauer or finite WZ/character-sum evaluation of the combination in (5) while retaining both second-order ports, then prove or refute uniform 13/19 mod24 cancellation; completed p³ cutoff theory is reused rather than repeated. External existing B2304 congruences retain their own attribution.

Native #1559 remains OPEN with no verified assigned evaluator in the current read; genuine same-original-class p373 H0/B0 divided-power [X]U mod139129, module rank, semilinear Frobenius/eta, signed odd Green/Hesse, κ and Delta-R require a real authorized source/versioned execution and independent validation. Site 0.6.11 read returned research_authority_granted=false, executor_binding_configured=false, quota 5/5 and own checkpoint_list ACCESS_DENIED; no role-bound session, claim, dispatch, checkpoint, Result, review or transfer into the maintenance conversation was performed. This author-side result needs lawful Source capture; task and notification settings are unchanged.
