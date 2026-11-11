# D25/JT2 — 原始 W216 的 Clausen 简单零点与 Hensel 残差坐标

Date: 2026-11-11 Asia/Hong_Kong. Classification: AUTHOR_SIDE / DERIVED_WITH_ACCEPTED_CM0_AND_UR / EIGHT_EXACT_REGRESSIONS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Frozen scientific input: awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).
Research logical lane: chatgpt-research-onhour-enterprise-math-20260923; maintenance lane is separate.
Prior accepted CM0/UR and completed scalar source-port alignment are consumed, not recredited.

## New scientific result: a simple zero survives the original signed observer

For each prime p ≡ 13 or 19 (mod 24), write p=6m+1, x0=1/2, and work over Z_(p). Define the original source-specific polynomials

  f_m(x) = sum_{k=0}^m ((1/6)_k(1/3)_k/(k!)^2) x^k,
  Y_p(x) = sum_{k=0}^{p-1} ((1/2)_k(1/3)_k(2/3)_k/(k!)^3) x^k,
  S_p(x) = (1+6x d/dx) Y_p(x).

Thus W_p=S_p(1/2)=sum_{k<p}(6k+1)(2k)!(3k)!/(216^k (k!)^5), precisely the frozen signed original observer.

**Theorem (signed simple-zero).** Under the already accepted CM0 fact f_m(1/2)=0 mod p, for EVERY stated prime:

  S_p(x) ≡ f_m(x) [ f_m(x)+12x f_m'(x) ] (mod p) in F_p[x],
  f_m'(1/2) ≠ 0 (mod p),
  S_p'(1/2) ≡ 6 [f_m'(1/2)]² ≠ 0 (mod p).

The second equality is the new nondegeneracy certificate. Although unweighted Y_p is a square mod p, the original signed derivative operator transforms its double zero into a simple zero; discarding the first derivative would destroy a p-adic Hensel lifting observable.

**Proof.** Clausen's terminating coefficient identity for the chosen parameters gives the formal rational equality

  3F2(1/2,1/3,2/3;1,1;x) = [2F1(1/6,1/3;1;x)]².

The first factor (1/6)_k in 2F1 contains p at k=m+1; similarly (1/3)_k in 3F2 contains p at k=2m+1. Since all k! for k<p are p-units and deg(f_m²)=2m<p, coefficientwise reduction yields Y_p(x)=f_m(x)² mod p for all polynomial degrees k<p. Apply the original operator 1+6x∂x, obtaining the first identity.

The truncated f_m is a nonzero mod-p solution of the hypergeometric differential equation

  x(1-x) f_m'' + (1-(3/2)x) f_m' - f_m/18 = 0 mod p.

At x0=1/2, its leading second-derivative coefficient is 1/4, a unit. If f_m and f_m' both vanished there, choose its least nonzero Taylor exponent r≥2. Because deg(f_m)=m<p, r(r-1)/4 is nonzero modulo p, contradicting the differential equation's coefficient at order r-2. This proves f_m'(x0)≠0. Differentiate the first identity at x0 and use f_m(x0)=0 to obtain S_p'(x0)=12x0 f_m'(x0)²=6 f_m'(x0)², a unit. QED.

## Exact new Hensel/LIFT reparameterization

Under the accepted first-digit UR, S_p(x0) ≡ p (mod p²). The Z_p-polynomial F_p(x)=S_p(x)-p has a unique Hensel root ξ_p with ξ_p ≡ x0 (mod p²), and the explicit first nontrivial displacement

  (ξ_p-x0)/p² ≡ - [(S_p(x0)-p)/p²] / [6 f_m'(x0)²] (mod p).

The earlier independently derived *source-port alignment* gives

  (S_p(x0)-p)/p² ≡ Delta_p-R_p (mod p)

with the frozen original Delta, cutoff-sensitive R and signed Q provenance unchanged. Therefore the following is an exact, all-target-prime equivalence of observers:

  LIFT: Delta_p-R_p=0 (mod p)  <=>  ξ_p=1/2 (mod p³).

The target uniform Hensel rigidity is still OPEN. This author-side transformation gives a nonzero Jacobian and a local root-displacement witness for the existing target; it is not itself the source-native H0/B0 experiment or an accepted final strict reduction.

## Eight exact finite checks, including genuinely stronger p^4 negative controls

Executed deterministic integer modular computation with two independent coefficient constructors (factorial-ratio recurrence and binomial formula), full mod-p Clausen coefficient-by-coefficient equality for all 0≤k<p, direct original signed derivative, and f_m'(1/2). All checks passed, with no floating point.

| p | m | f_m(1/2) | f_m'(1/2) | S_p'(1/2) mod p | W_p mod p⁴ | (W_p-p)/p³ mod p |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 2 | 0 | 1 | 6 | 19786 | 9 |
| 19 | 3 | 0 | 2 | 5 | 82327 | 12 |
| 37 | 6 | 0 | 11 | 23 | 962444 | 19 |
| 43 | 7 | 0 | 40 | 11 | 1510676 | 19 |
| 109 | 18 | 0 | 92 | 99 | 111372603 | 86 |
| 139 | 23 | 0 | 76 | 45 | 190679088 | 71 |
| 157 | 26 | 0 | 118 | 20 | 584354000 | 151 |
| 373 | 62 | 0 | 215 | 211 | 11832087049 | 228 |

Every W_p above equals p modulo p³, consistent with the existing author-side finite scalar certificate. All eight have NONZERO fourth digit, so a casual extension W≡p mod p⁴ is already refuted by p=13 (and the other seven). This finite counterexample addresses only the stronger p⁴ proposition, not the open all-prime p³ target.

At p=373, f_m'=215, S_p'=211=6·215² mod373 and 211^{-1}=99 mod373. The actual root displacement has the higher precision witness

  ξ_373 - 1/2 ≡ -228·99·373³ ≡ 181·373³ (mod 373⁴).

These are exact integer finite witnesses, not numerical approximations. Reproducibility: research_notes/portable_direct/d25_clausen_simple_zero_hensel_20261111.py.

## Typed BRC/Enterprise-observer application

Resolution: COMPOSE_APPLIED. Population: original W216 index k, explicit two target residue classes, p-local coefficient valuations. Retained source carriers: the original hypergeometric series, low-degree Clausen polynomial f_m, derivative jet f_m', signed (1+6x∂x) operator, exact p² divided residual Delta-R, and future Hensel root operation. At the first Hensel step the pair ([S_p(x0)-p]/p² modp, f_m'(x0) modp) is a sufficient observer for (ξ_p-x0)/p² modp, with explicit inversion because 6 f_m'^2 is a unit. The scalar f_m(x0)=0 alone is NOT sufficient; the derivative survives, an information-loss witness.

The variable x and this finite-field polynomial are conventional external algebraic calculation coordinates, not a redefinition of Enterprise native X6, P000, or the research three-dimensional slice. No proof or promotion of P000 is asserted.

## Native outstanding / exact continuation

Source exact continuation request onhour11-20261111-1204-exact-cont: SUCCEEDED, current Source read snapshot b45d78ec26b2a1be7c9642b4fa79ac351b3f3844. Route: PREPARE_TYPED_CONTINUATION_WITH_EXACT_PREDECESSOR_AND_FRONTIER. Previous Source claimant locator MCP-d0d70cd041b01e5db192870a/comment 6390431276 is **not own authority**. Own prior Source registration request onhour11-20261111-1000-onhour-researcher-start: SUCCEEDED (Researcher EM-ENTERPRISE-CF1028; session MCP-7af27f545c01441eaf19206f89c6832b; activity RA-47ADB5B97D6D92FC28504B60). This run's own recovery yielded SESSION_CAPABILITY_REQUIRED; custody status with an unrelated fresh request did not resolve the prior capability. No winning own CLAIM, open run, semantic Source checkpoint, Result or Driver review.

Native benchmark remains existing issue #1559 (OPEN / PENDING_OWNER), its same-original-class fixed divided-power [X]U modulo 139129 at p=373, actual H0/B0 rank, Frobenius semilinear direction/eta, signed odd Green/Hesse kappa, original Delta-R, and independent replication. Next exact native action: recover/obtain a legitimately owned same-lane private capability, use the exact Source predecessor CAS to CLAIM/open, run the unchanged original evaluator; if capability is unavailable, the existing support path retains responsibility without a fictitious executor. Next mathematical action: determine a source-preserving formula for ξ_p modp³ (equivalently cancellation of Delta-R) for both p residue classes, or a counterexample. Do not replay the finite W216 scan, old E3 coefficients, accepted CM0/UR, or this simple-root calculation.

All author outputs here: NEW AUTHOR_SIDE UNIT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0. Formal parent objective remains OPEN.
