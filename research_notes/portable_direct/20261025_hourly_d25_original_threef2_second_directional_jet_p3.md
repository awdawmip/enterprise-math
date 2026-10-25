# D25/LIFT — original 3F2 all-rank p³ double directional jet and two-zero source recovery

Date 2026-10-25. TASK_RESEARCH author-derived/author-exact-checked/UNREVIEWED/NOT_ADMITTED/PORTABLE_ONLY. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; stable logical Research lane chatgpt-research-hourly-enterprise-math-20260923 (not maintenance). Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. No native winning CLAIM, OPEN, Source checkpoint or CM experiment.

## Consumed facts and exact next scientific question

The already-proved **first** directional parameter bridge restores original full-rank A_p(z) from a terminating p-deformed Clausen T_p(z) through mod p², including all previously invisible ranks 2m<n<=3m. The denominator-resonance identity T_p=U_p²+pU_p H_p mod p² is also established. Both are consumed, not re-credited here. The missing unit is the full **next digit** and source-rank 3m<n<=4m.

Fix p=6m+1>=7 prime and theta=z d/dz. Let

\[
A_p(z)=\sum_{n=0}^{p-1}\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3}z^n,\qquad
W_p=[(1+6\theta)A_p]_{z=1/2}.
\]

Use the p-local finite hypergeometric family

\[
\mathcal T(\mathbf a;\mathbf d;z)=\sum_{n=0}^{p-1}
\frac{(a_1)_n(a_2)_n(a_3)_n}{(d_1)_n(d_2)_n n!}z^n,
\quad
\mathbf a^*=(-2m,-4m,-3m),\
\mathbf d^*=(1-p/2,1-p),
\]
and exact parameter direction
\[
\mathfrak D=\tfrac13\partial_{a_1}+
\tfrac23\partial_{a_2}+\tfrac12\partial_{a_3}
+\tfrac12\partial_{d_1}+\partial_{d_2}.
\]

Write
\(T_p=\mathcal T|_*, D_p=\mathfrak D\mathcal T|_*\), and **second Taylor coefficient**
\(E_p=\tfrac12\mathfrak D^2\mathcal T|_*\). The name E_p here is local to this note and is **not** the earlier second-moment endpoint variable.

### Theorem A: exact second-digit source recovery, all n<p

Coefficientwise in the p-local polynomial ring,

\[
\boxed{A_p(z)\equiv T_p(z)+pD_p(z)+p^2E_p(z)\pmod{p^3}.}
\]

The source support is sharply stratified:
\[
\deg T_p=2m,\qquad\deg D_p=3m,\qquad\deg E_p=4m.
\]

For each 3m<n<=4m, the *full* explicit exceptional coefficient is

\[
\boxed{
[z^n]E_p=
\frac{(-1)^m(2m)!(3m)!(n-2m-1)!(n-3m-1)!\,(-4m)_n}
{6(1-p/2)_n(1-p)_n n!}
}
\]

and is a p-unit. On this rank branch, \([z^n]A_p\equiv p^2[z^n]E_p\pmod{p^3}\), of exact p-valuation two. For n>4m, all three original top factors have crossed a p-zero and their combined valuation is at least three; the full original coefficients vanish modulo p³. Thus **the new second directional jet is necessary to recover the exact original ranks 3m<n<=4m** when observing at p³ precision.

### Theorem B: second-order Clausen denominator resonance

Let
\[
U_p(z)={}_2F_1(-m,-2m;1;z)=\sum_{n=0}^m u_nz^n,
\]
\[
H_p(z)=\sum_{n=0}^m u_nH_nz^n,\quad
J_p(z)=\sum_{n=0}^m u_n\bigl(H_n^2+H_n^{(2)}\bigr)z^n,
\]
where \(H_n=\sum_{j=1}^n1/j,\ H_n^{(2)}=\sum_{j=1}^n1/j^2\).

The Clausen-compatible terminating 2F1 is
\(C_p={}_2F_1(-m,-2m;1-p/2;z)\), with the already-proved exact rational identity \(C_p^2=T_p\). Then

\[
\boxed{C_p\equiv U_p+\frac p2H_p+\frac{p^2}{8}J_p\pmod{p^3}},
\]
\[
\boxed{T_p\equiv U_p^2+pU_pH_p+
\frac{p^2}{4}(H_p^2+U_pJ_p)\pmod{p^3}}.
\]

Consequently the complete **original** weighted second-digit observer satisfies the all-prime identity

\[
\boxed{\begin{aligned}
W_p\equiv\bigg[(1+6\theta)\bigg(
U_p^2+p(U_pH_p+D_p)\\
\quad +p^2\left(\frac{H_p^2+U_pJ_p}{4}+E_p\right)
\bigg)\bigg]_{z=1/2}\pmod{p^3}.
\end{aligned}}
\]

The full rank threshold, signed theta action, first and second parameter derivatives, harmonic squares and dual-zero exceptional branch remain distinct. No numerical p-interpolation is used.

## Proof

The exact target parameters are \((1/3,2/3,1/2;1,1)
=(\mathbf a^*,\mathbf d^*)+p(1/3,2/3,1/2;1/2,1)\).
Every denominator factor \((1-p/2+j)\), \((1-p+j)\), (n!) for n<p is a p-unit, so coefficientwise Taylor expansion in the single directional parameter is legal modulo p³. This proves Theorem A's first equality.

For n>2m, (-2m)_n has a simple zero. For n>3m, (-3m)_n has another distinct simple zero. A Taylor coefficient of order one cannot recover both, so T_n=D_n=0. The order-two Taylor coefficient comes solely from differentiating those two zero factors once each, giving factor (1/3)(1/2)=1/6. Removing their roots yields
\[
\frac{\partial}{\partial a_1}(a_1)_n|_{-2m}
=(2m)!(n-2m-1)!,\quad
\frac{\partial}{\partial a_3}(a_3)_n|_{-3m}
=(-1)^m(3m)!(n-3m-1)!.
\]
All other numerator factors in this rank range and all denominators are p-units; their product is the explicit E coefficient. After rank 4m the third top factor (-4m)_n has a separate zero that a second derivative cannot also remove; hence E_n=0 and the original p-valuation is at least 3. This proves the sharp degree and valuation claims.

For 0<=n<=m, the reciprocal lower Pochhammer expansion is
\[
\frac1{(1-p/2)_n}
=\frac1{n!}\prod_{j=1}^n(1-p/(2j))^{-1}
\equiv\frac1{n!}\left[1+\frac p2H_n+
\frac{p^2}{8}(H_n^2+H_n^{(2)})\right]\pmod{p^3}.
\]
Summing the finite terminating source proves the expansion for C_p; square it using exact rational Clausen to derive the T_p identity. Combine with Theorem A and apply the actual linear operator 1+6theta before evaluating z=1/2. QED.

## Exact evidence, observer discipline, limits

Companion Python checker uses the actual original source 3F2 recurrence and an **independent second-order dual-number recurrence** for the deformed five-parameter coefficient family. It checks every rank n<p modulo p³, the exact three support cuts and the nonzero second-source branch. A separate terminating Jacobi/H/H²+H2 path reconstructs the full Clausen second-harmonic correction coefficientwise and original signed weighted observer.

All 35 primes p=1(mod6) up to373, plus1327 and19963, PASS the all-rank p³ identity (37 total). For all p<=1327, the independent U/H/J coefficientwise resonance and weighted source observer PASS; for largest p=19963 the O(m²) full convolution is not rerun, but the all-rank first/second dual-number checks still pass. Examples original W_p mod p³: p=13 gives 13; p=19 gives 19; p=373 gives 373. These are **finite author checks only**, not a uniform proof of W_p=p nor of D25/LIFT. Exceptional top-rank E_(4m) mod p: p=13 12, p=19 3, p=373 262, p=1327 249, p=19963 6380.

BRC COMPOSE_APPLIED: original rank/branch, the three distinct zero-factor crossings, p-valuation, signed coefficients and allowed theta/future precision operation are preserved. The one-digit terminating quotient is not used at an incompatible p³ observer. No original native CM/Frobenius experiment was run or simulated.

## Next genuine unresolved unit

The explicit source-preserving full original W_p modulo p³ is now a three-component p-adic Jacobi/Clausen observation. The hard target for inert primes p=13,19 mod24 remains **proof of the exact signed cancellation producing W_p≡p mod p³ (and separately genuine CM/divided-power Frobenius/kappa evidence)**. The present identity is an exact reduction with all sources preserved, not a proof that this finite combination equals p. Seek a uniform signed telescoper for the displayed source combination or an authenticated finite-field Jacobi/Gauss-sum/Frobenius certificate; do not promote finite prime scans to universal inference. Independent review and native Source authorization remain pending; exact continuation CONTROL_QUOTA and historical predecessor CAS issue tracked by enterprise-math Issue #1558. D25/LIFT/JT2 OPEN. Freeze pin, prior session/contribution/history and scheduler/notices untouched.
