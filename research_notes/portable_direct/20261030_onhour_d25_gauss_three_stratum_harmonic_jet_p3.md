# D25 / SECOND-DIGIT-LIFT — a three-stratum Gauss harmonic-jet certificate modulo p^3

2026-10-30 Asia/Hong_Kong. **AUTHOR-SIDE / COEFFICIENTWISE ALGEBRAIC DERIVATION / EXECUTED EXACT CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.** This is a portable continuation of the exact signed-R Gauss–Hensel/low-root frontiers, not a claim of the original LIFT or any native H0/B0 experiment.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Research logical lane chatgpt-research-onhour-enterprise-math-20260923 (not maintenance). Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. P000 ACTIVE_LOCKED and ACTIVE worldview remain untouched. No legal Source CLAIM/session/run or mathematical admission is represented by these author notes.

## Exact question and input

For a prime p=6m+1>=7 set c_n=(1/6)_n(1/3)_n/(n!)^2 for 0<=n<p. The original Gauss polynomial is G_p(z)=sum_(n=0)^(p-1) c_n z^n. Unlike a root location reformulation, can its original coefficients be reduced **directly and source-faithfully modulo p^3**, with all valuation-zero, valuation-one and valuation-two branches retained in an explicit harmonic-jet carrier?

All rational congruences are in the p-local integers Z_(p). Write H_r=sum_(j=1)^r 1/j and H_r^(2)=sum_(j=1)^r 1/j^2, with H_0=H_0^(2)=0. All harmonic indices below are <p, so all these denominators are p-units.

## All-p coefficientwise theorem

**Stratum 0, 0<=n<=m.** Let
\[
B_n=\binom{m}{n}\binom{2m}{n},\quad
L_n=-\frac{H_m-H_{m-n}}6-\frac{H_{2m}-H_{2m-n}}3,
\quad
J_n=\frac{H_m^{(2)}-H_{m-n}^{(2)}}{36}
    +\frac{H_{2m}^{(2)}-H_{2m-n}^{(2)}}9.
\]
Then
\[
\boxed{c_n\equiv B_n\left(1+pL_n+\tfrac{p^2}{2}(L_n^2-J_n)\right)\pmod{p^3}.}
\tag{S0}
\]

**Stratum 1, m<n<=2m.** Let
\[
T_n=\frac{(-1)^{m+n}m!(n-m-1)!(2m)!}
          {6(2m-n)!(n!)^2},\quad
K_n=\frac{H_{n-m-1}-H_m}{6}
       -\frac{H_{2m}-H_{2m-n}}3 .
\]
Then
\[
\boxed{c_n\equiv pT_n(1+pK_n)\pmod{p^3}.}
\tag{S1}
\]

**Stratum 2, 2m<n<=p-1.** Let
\[
U_n=\frac{(-1)^m m!(2m)!(n-m-1)!(n-2m-1)!}{18(n!)^2}.
\]
Then
\[
\boxed{c_n\equiv p^2U_n\pmod{p^3}.}
\tag{S2}
\]

The three expressions are exact finite polynomial/rational expressions in the original indexing, not an approximation under real analysis. Each indicated T_n and U_n is a p-unit; hence the coefficients have p-adic valuations exactly 0, 1 and 2 in their respective strata. This decomposition holds for **every** p=6m+1 prime, not merely the inert target subfamilies.

**Proof.** In Z_(p) use the *exact* identities
\[
(1/6)_n=(-m+p/6)_n,\qquad (1/3)_n=(-2m+p/3)_n.
\]
For n<=m both factors have no zero at p=0. Factoring their nonzero terms yields B_n times products of (1+p x); the first and second elementary symmetric sums give L_n and (L_n^2-J_n)/2 exactly at p^2. For m<n<=2m, the first product has its unique zero-index factor p/6. The nonzero factors below and above that index have sign (-1)^m and factorial product m!(n-m-1)!, while the second Pochhammer contributes (-1)^n(2m)!/(2m-n)!. Their product gives pT_n. The p-linear logarithmic derivative of the remaining nonzero products gives (H_(n-m-1)-H_m)/6 minus (H_(2m)-H_(2m-n))/3, namely K_n. Finally, n>2m introduces the second zero-index factor p/3; multiplying the two leading p factors yields p^2U_n, and all subsequent perturbations are multiples of p^3. Since n<p, all factorials and displayed inverses are p-units. This proves (S0)–(S2).

## Exact source-preserving jet port

Define coefficient approximants q_n by (S0), (S1), (S2), and source-labeled additive ports (the value at the original argument z=1/2 and its actual derivative):
\[
M_j=\sum_{n\in I_j}q_n2^{-n}\pmod{p^3},\qquad
g_j=2\sum_{n\in I_j}nq_n2^{-n}\pmod{p^3}
\quad (j=0,1,2),
\]
where I_0=[0,m], I_1=[m+1,2m], I_2=[2m+1,p-1]. Thus
\[
G_p(1/2)\equiv M_0+M_1+M_2\pmod{p^3},\qquad
G_p'(1/2)\equiv g_0+g_1+g_2\pmod{p^3}.
\tag{J}
\]
In particular p|M_1,g_1 and p^2|M_2,g_2. For the next original second-digit residual, g_2 can be omitted **only after reducing g modulo p^2**, while M_2 cannot be omitted from M modulo p^3.

For the target classes p≡13,19 (mod24), **conditional on the already consumed original CM0/first-digit and signed reflection source-port identities** (the source-aligned exact Clausen relation A_p=M(M+6g)-Q and Q/p^2≡R_p mod p), let
\[
M=(M_0+M_1+M_2)\bmod p^3,\quad h=M/p\bmod p^2,\quad
g=(g_0+g_1)\bmod p^2.
\]
The original, unaltered 216 weighted LIFT is equivalent to the **explicit finite harmonic-port congruence**
\[
\boxed{\quad6h\,g+p(h^2-R_p)\equiv1\pmod{p^2}.\quad}
\tag{L}
\]
Here R_p is **exactly** the pre-frozen signed reflected observation, not a value fitted to finite test data:
\[
R_p=2\sum_{i=1}^m (c_i2^{-i})
       \sum_{a=1}^i[1+6(i-a)]C_a\pmod p,\quad
C_1=1/10,\quad C_{a+1}/C_a=\frac{36a^2}{(6a+5)(3a+2)}.
\]
The reduction (L) itself is not a proof that its right-hand side vanishes for all target primes; it is a **root-free, explicit finite harmonic-jet representation of exactly the same remaining obligation**. The p^2 tail, signed R and derivative ports are separately retained.

### Fixed integer certificate at p=373

Here m=62, p^3=51895117. Modulo p^3, the executed original-index ports are
\[
(M_0,M_1,M_2)=(15144919,26185346,35060508),
\]
\[
(g_0,g_1,g_2)=(20358555,28136882,43269119).
\]
Consequently M=24495656, h=M/p=65672 modulo p^2, g=78545 modulo p^2, R_373=196 modulo p and M_2/p^2=252 modulo p (the previously source-labeled high tail F_373). The full original 216 sum computed **independently** gives A_373≡373 (mod 373^3), and both sides of the prior exact signed residual transport agree. The nonzero M_1 and M_2 ports must not be deleted when forming this p^3 witness.

## Actual execution and scope

The exact Python standard-library script d25_gauss_three_strata_harmonic_jet_20261030.py was **executed**. It checked every p≡1 (mod6) prime 7<=p<1000: **80 primes**, comparing every q_n against an independently computed original Gauss coefficient modulo p^3 and comparing all three value/derivative source ports. On the **45** primes p≡13,19 (mod24) in this range, it independently evaluated the original weighted 216 binomial sum and frozen signed R double-sum recurrence, verified the first digit, and checked the exact signed second-residual port relation. Execution ended PASS_D25_THREE_STRATUM_HARMONIC_JET_ALL_COEFFICIENTS. This is finite exact verification of the algebraic derivation, not a universal test of (L), a native experiment, or independent review.

BRC resolution: **COMPOSE_APPLIED**, a source-indexed, p-valuated, signed rational coefficient carrier with alternative (strata) and additive derivative/value ports. Observer: the frozen signed p^3 residual A_p-p and R_p. Allowed operations: p-local addition, multiplication, derivative evaluation at 1/2 and lossless provenance transport at p^3; coarse total-only projection is unsafe before the nonlinear M(M+6g) operation. This external arithmetic application does not assert a native X6 or H0/B0 transfer.

## Frontier and unperformed work

**Next smallest mathematical action:** establish or refute a **uniform cancellation identity among the three explicit harmonic ports in (L)**, ideally by a finite hypergeometric creative-telescoping/CM deformation that retains R_p, rather than another equivalence reformulation. Start by isolating the p^2 second-digit coefficient of 6h g+p(h^2-R_p)-1, and do not assume it vanishes. Keep p=13,19 and p=373 as exact witnesses, then prove a general target-class cancellation or provide an exact counterexample.

**Native top frontier unchanged:** support issue #1559, fixed p=373 **original-class** H0/B0 divided-power [X]U modulo 139129, module rank, genuine semilinear Frobenius/eta, signed odd Green/Hesse, kappa and independent repetition. This finite arithmetic script is not that experiment. Original research Source access in this run remains static read-only: research_authority_granted=false, write_relay_enabled=false; self checkpoint listing failed ACCESS_DENIED. No Source session/claim/run/request ownership or formal checkpoint was recovered or modified. Existing pending IDs, unknown effects and staging must be reconciled on their original paths only after actual authorization; no mutation retry or maintenance-lane identity use. These notes are author-side, unreviewed, not admitted, and not a scheduler/control change.

Source consumed: prior original-R-corrected low-root note and original Gauss–Hensel note in research_notes/portable_direct/, source pin above, and current ACTIVE docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md. Previous completed CM/Clausen and endpoint results are reused without claimed re-proof.
