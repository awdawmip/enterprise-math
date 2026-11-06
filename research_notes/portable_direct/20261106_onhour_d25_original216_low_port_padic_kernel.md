# D25 — Original-216 low-port transfer kernel, including its first p-adic deformation

Date 2026-11-06. Role: author-side TASK_RESEARCH `chatgpt-research-onhour-enterprise-math-20260923`; no maintenance identity. Scientific frozen pin `c47e13e4aba0e006366f989d6334d443f6333ae3`, Task `TP2-B6F4FC938FF94941C1B7`. Status: algebra PROVED, finite arithmetic VERIFIED, Source admission UNREVIEWED / NOT_ADMITTED. This note consumes the new exact endpoint moment certificate at `c8a36bd133ac6397ce1e6d37859ae52764427837`, and earlier E1/E3 at `37f417a0fbfad1806b092d0c685d2f3c310e71fe`.

## The original-index low-port theorem

Let p=6m+1>3 prime; `gamma_k=binom(2k,k)^2 binom(3k,k)`, `a_k=gamma_k/216^k`. Let `b_0=1`, `b_n/b_(n-1)=6(6n-5)(3n-2)/n^2`. Let `B=b_p`, and for 1<=k<=2m define
`lambda_k=216^k b_(p-k)/p^2 in Z_(p)`.
The p-integrality is precisely the E3 valuation-two low band.

**Exact rational recurrence (not merely modulo p):**
`
lambda_1 = 36 B/[(6p-5)(3p-2)],
lambda_(k+1)/lambda_k =
  36(p-k)^2/[(6(p-k)-5)(3(p-k)-2)], 1<=k<2m.    (1)
`
Proof: apply the exact b backward recurrence and divide successive lambda values. The relevant denominators are p-units throughout 1<=k<=2m; moreover k itself is a unit.

Set, for k>=1,
`
H_1=108/5,
H_(k+1)=H_k*36k^2/[(6k+5)(3k+2)],                 (2)
sigma_k=-2/k+6/(6k+5)+3/(3k+2),
Sigma_1=0, Sigma_k=sum_(j=1)^(k-1) sigma_j.
`
All are rational numbers with p-unit denominators for 1<=k<=2m. By the preceding exact moment theorem, B=6 (mod p). Define the integer `beta_p=(B-6)/p (mod p)`.

**New universal first p-adic deformation, all p=6m+1>3 and 1<=k<=2m:**
`
lambda_k = H_k [1+p*(beta_p/6+27/10+Sigma_k)] (mod p^2). (3)
`
Proof: expand the unit initial value `lambda_1=36(6+p beta_p)/(10-27p+18p^2)` modulo p^2, obtaining `H_1(1+p(beta_p/6+27/10))`. Expand each ratio (1) at p=0: `36k^2/[(6k+5)(3k+2)]*(1+p*sigma_k)`; multiply finitely. Every displayed division is by a p-unit.

**Exact original 216 transfer as an observed finite function:**
`
( gamma_k*b_(p-k) /p^2 )
 = a_k H_k [1+p*(beta_p/6+27/10+Sigma_k)] (mod p^2),
for 1<=k<=2m.                                             (4)
`
The equality is in Z_(p), with original gamma and a coefficients and preserved reflected b-index, valuation two, and k weight. It is a branchwise transfer rather than an invalid global unit scalar: the high p^3 M/U bands and the original signed J_p remain separate.

## Recover beta from the original 216 coefficients

The exact weighted cubic endpoint identity of the preceding note implies
`
beta_p = (3/2)*sum_(k=1)^(2m) k a_k H_k (mod p).      (5)
`
Indeed `gamma_p=12 (mod p^3)` by the classical binomial congruence; compare `(gamma_p-2B)/p` to the low-branch `-3 sum k gamma_k b_(p-k)/p^2` modulo p and substitute (4). Thus formula (3) is a **self-contained original-index calculation**: compute beta from (5), then calculate every low-port lambda modulo p².

There is also a useful **externally conditioned simplification**. If the mixed-CM cubic coefficient congruence `A_p=18 (mod p^2)` holds (as claimed more strongly modulo p^4 by Alex Shvets, arXiv:2605.19773, 2026-05-19), then `A_p=gamma_p+B+sum_(1<=k<p)gamma_k b_(p-k)`, whose interior is p²-divisible. Consequently `B=6 (mod p²)`, `beta_p=0`, and
`
sum_(k=1)^(2m) k a_k H_k =0 (mod p),               (6)
lambda_k = H_k [1+p*(27/10+Sigma_k)] (mod p²).   (7)
`
The elementary implication (6)-(7) is proved; its all-prime assertion uses the stated external coefficient congruence, preserved as independently attributed source, not a substitute for original `W_p`.

## Actual arithmetic

An independent second standard-library integer test computed all low-band lambda from the actual b_(p-k)/p² and from (2)-(5), and compared both `lambda_k` and `a_k lambda_k` modulo p². All **80 primes p<=997, p=1 mod6** passed; 45 in frozen p=13,19 mod24. It also checked `beta_p=0` for all 80 as a **finite observation** consistent with the external preprint. At p=19: beta=0, lambda_1=90, lambda_m=26, lambda_(2m)=359 (mod 361). At p=373: beta=0, lambda_1=127513, lambda_m=81473, lambda_(2m)=84572 (mod 139129). No floating-point steps.

BRC use: COMPOSE_APPLIED, original-index exact 216 coefficient + valuation-two low port + first-order deformation; preserves signed index provenance and distinct middle/upper M/U bands. No claim that a low-band transfer alone proves the third digit of original full evaluation.

## Next smallest exact scientific action

Investigate a **finite source-preserving adjoint from original full W_p** to mixed-CM cubic A_p using kernel (4) only where licensed, then explicitly represent or prove an obstruction for the remaining M/U (valuation three) and signed original J_19=6, J_373=98. Parent goal still `Delta_p-R_p=0 mod p`, p=13,19 mod24, equivalently original `W_p=p mod p^3` under frozen scalar interface. Native original same-class p373 H0/B0 divided-power [X]U, semilinear Frobenius/eta, kappa, and independent replica are still NOT_EXECUTED/PENDING_OWNER at Issue #1559. No role claim, native run or admission is asserted here.
