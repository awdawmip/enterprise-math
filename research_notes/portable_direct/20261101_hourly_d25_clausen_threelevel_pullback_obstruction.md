# D25: three-level Clausen cutoff and no direct rational pullback (author-side, 2026-11-01)

Research lineage: original 216 weighted 3F2, Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, immutable scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3. This note CONSUMES, without re-crediting, research_notes/portable_direct/20261101_hourly_d25_clausen_symmetric_square_cutoff_transfer.md and 20261101_hourly_d25_original_216_weighted_terminal_resonance.md. Status AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING. All statements are external auxiliary algebra, not native X6 or the original H0/B0 benchmark.

## A. Full high-cutoff filtration and exact source

For prime p>=7, p≡1 (mod 6), put r=(p-1)/6, s=(p-1)/3, u_i=(1/6)_i(1/3)_i/(i!)²,
Y=Σ_(i=0)^(p-1) u_i z^i,
U=Σ_(i=0)^(p-1) (1/2)_i(1/3)_i(2/3)_i/(i!)³ z^i,
K=Y²-U, k_n=[z^n]K,
L3=θ³-z(θ+1/2)(θ+1/3)(θ+2/3),
e=-(p-5/6)(p-2/3)u_(p-1), θ=z d/dz.

The already-proved infinite Clausen identity implies k_n=0 for 0<=n<p and k_(2p-1)=0.

THEOREM A1 (three sharp valuation bands). For every n,
- p<=n<=p+r-1: v_p(k_n)>=2;
- p+r<=n<=p+s-1: v_p(k_n)>=3;
- p+s<=n<=2p-2: v_p(k_n)>=4.

Each bound is sharp at the last coefficient of the band. Precisely in F_p, with all p-adic division BEFORE reduction,

k_(p+r-1)/p² ≡ u_r/5 ≠ 0,
k_(p+s-1)/p³ ≡ (u_s/p)/5 ≠ 0,
k_(2p-2)/p⁴ ≡ 1/100 ≠ 0 (mod p).

Proof. For 0<=i<p, v_p(u_i)=1_(i>r)+1_(i>s), since the two numerator progressions each meet a single p-factor, and i! is a p-unit. For n>=p,
k_n=Σ_(i=n-(p-1))^(p-1) u_i u_(n-i).
At least one index exceeds s since 2s<p, giving bound 2. If n>=p+r neither index may be <=r, giving bound 3. If n>=p+s neither may be <=s, giving bound 4. At n=p+r-1, only the two symmetric endpoint indices (r,p-1) have valuation sum 2; at n=p+s-1, only (s,p-1) have valuation sum 3; at n=2p-2 the coefficient is u_(p-1)^2. The earlier Wilson calculation u_(p-1)/p²≡1/10 (mod p) proves the three sharp equalities. Both u_r and u_s/p are p-units.

THEOREM A2 (all high-index source valuations, not just first omitted term). For every 1<=j<p,
S_j=[z^(p+j)]L3 K = 2 e (p+3j)u_j EXACTLY over Q,
v_p(S_j)=2+1_(j>r)+1_(j>s),
S_j/p^(2+v_p(u_j)) ≡ -(j/3)(u_j/p^v_p(u_j)) ≠ 0 (mod p).

Proof. Consume the exact symmetric-square/weighted intertwiner: all n=p+j>p coefficients of the weighted output vanish, so the exact unweighted cutoff response is 2e(3n-2p)u_(n-p). The scalar multiplier (6n-5)(6n+1) is nonzero in Q. The previous Wilson result e/p²≡-1/18 is a unit; p+3j≡3j is also a unit for 1<=j<p, and the valuation statement follows. The source identity DOES NOT include j=0: the weighted original has its distinct nonzero z^p terminal source.

This is a strict BRC observer/operation witness (COMPOSE_APPLIED): with future operation L3 and precision through p^5, the three indexed p-adic layers are all nonempty. Merely recording the p² layer loses future p³ and p⁴ responses. Population p≡1 mod6 and index j; retain original signed rational data, valuations, source/port labels and operator. This is not a general minimality claim or an embedding in native X6.

## B. Exact obstruction to a simple 216-to-2304 Gauss pullback

Let HA be Gauss 2F1(a,b;c;z) differential equation with (a,b;c)=(1/6,1/3;1) and HB that with (a,b;c)=(1/8,3/8;1). Their local exponent differences at z=0,1,infinity are

HA: (0, 1/2, 1/6)
HB: (0, 1/2, 1/4).

THEOREM B. Neither entire rank-two differential equation can be obtained from the other by a nonconstant rational independent-variable pullback z=phi(w) followed by a nonzero scalar algebraic/meromorphic gauge prefactor. This includes degree-two rational pullbacks.

Proof. At a regular point the exponent difference is 1. At a preimage of a singular or ordinary point under a rational map with integer ramification index e>=1, the exponent difference is e times its source value. A scalar gauge shifts both exponents equally. For a pullback of HA, every local difference belongs to {0,e/2,e/6,e}, so in reduced form its denominator divides 6. HB requires a difference of 1/4 at infinity, impossible. In the reverse direction all source differences have reduced denominator dividing 4; HA requires 1/6 at infinity, equally impossible. Apparent singularities and scalar prefactors do not remove this denominator obstruction.

Scope: characteristic-zero direct rational scalar-pullback equivalence of the entire two-dimensional solution spaces only. This does NOT preclude finite-p congruences, a p-dependent source-preserving map, product/symmetric-square representations, differential/matrix intertwiners, or non-rational algebraic correspondences. The classical exponent-pair formula is NIST DLMF 15.10 (https://dlmf.nist.gov/15.10).

## Checks / exact next action

Executable stdlib checker d25_clausen_threelevel_pullback_check_20261101.py: all high-cutoff coefficients, sharp endpoints, exact L3K identity and normalized source levels modulo p^5 for 80/80 primes 7<=p<=997, p≡1 mod6; independent exact Fraction endpoints at p=7,13,19. Illustrative (p, tier2, tier3, tier4) modulo p: (13,9,3,3), (19,4,4,4), (37,22,15,10), (373,368,188,235). Finite diagnostic of exponent differences e<=99 is not the universal proof. Native same-class p=373 H0/B0 remains NOT_RUN (#1559).

NEXT scientific obligation: search an explicitly source-preserving NONSCALAR matrix/differential or higher-rank correspondence from the original 216 Gauss/Clausen model to the distinct 2304 (1/8,3/8) model; preserve the signed K cutoff, terminal source, j-indexed p-adic digits, 13/19 class normalization, original Δ-R and Frobenius/Green-Hesse evidence; require an actual operator identity before inferring a common coordinate. Frozen mother target A_p≡p mod p³ for p mod24 in {13,19} stays OPEN. Do not repeat the consumed old Clausen terminal lemma.

CONTROL, independently observed 2026-11-01 11:25 UTC: Gateway 0.6.11 reported research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED, active_jobs=5/5. Gateway EM source pin 76e2ebe9125f7dd4318d020494197bbd65bd3d91 matched independently read GitHub EM main 76e2ebe9125f7dd4318d020494197bbd65bd3d91. The separately cached global-knowledge pin 7b33f8066e9993e7c941959a9d738ed405248eb8 was older than the directly verified global-knowledge main 6ef7efbdd894833174176d06eff64a36da31dfa1. Historical own-lane recovery issue awdawmip/kimi-query-bridge#6637 contained service session MCP-06f7ad61a8d841d9ba1ba1ef4d088d94 with no own pending/run/unopened claim and execution_authorized=false at that read; exact continuation #6638 was definitively rejected with UPSTREAM_CODE_REVIEW_REQUIRED. These old transport receipts do NOT authenticate a fresh role session in this turn. Support awdawmip/enterprise-math#1558. Preserve old session/staging, original requests and Source pins; NO new native CLAIM/OPEN/checkpoint/Result/review is claimed by this portable research note.