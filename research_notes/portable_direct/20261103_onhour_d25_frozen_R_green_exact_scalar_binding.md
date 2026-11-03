# D25 — Frozen R is the negative finite Clausen–Green observer (2026-11-03)

TASK_RESEARCH portable author-side result for logical Research lane \`chatgpt-research-onhour-enterprise-math-20260923\`. Scope: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, immutable publication \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. **AUTHOR-DERIVED / SCOPED EXACT PROOF / EXACT FINITE CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. No native Source claim, execution, admission or experiment.

## Exact frozen inputs, distinct observers

For prime p=6r+1≥7 let B_k=(1/6)_k(1/3)_k/[2^k(k!)²], g=Σ_{k=0}^{p−1}B_k, h=Σ_{k=0}^{p−1}(12k+1)B_k. The frozen target is

R_p = 2 Σ_{i=1}^r B_i Σ_{s=1}^i (1+6(i−s)) C_s (mod p),
C_s=2^{s−1}(s−1)!²/[18(5/6)_s(2/3)_s].

For p≡13,19 (mod24), accepted UR gives p|g and (g/p)h≡1 (mod p). Define Δ_p=[(g/p)h−1]/p (mod p). The immutable Source definition of R and the exact finite Clausen valuation/reflection are in frozen \`research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN_20260827.md\` and \`...INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE_RETURN_20260827.md\` at the above input pin.

Keep the *original* weighted 216 endpoint W_p=Σ_{k=0}^{p−1}(6k+1)binom(2k,k)²binom(3k,k)/216^k, and let θ=z d/dz. Define G(z)=Σ_{k=0}^{p−1}(1/6)_k(1/3)_k z^k/(k!)², F(z)=Σ_{k=0}^{p−1}(1/2)_k(1/3)_k(2/3)_k z^k/(k!)³. Then G(1/2)=g, [(1+12θ)G](1/2)=h, [(1+6θ)F](1/2)=W_p.

## Theorem A — New exact cross-source R/Green binding

Consume the previously proved finite Green boundary law \`20261103_onhour_d25_gauss_clausen_inhomogeneous_green_port.md\` (immutable author commit \`cd6e0d6ed4d009a4c93e38e3241d7bbc9fa230f8\`). Its unique polynomial K_p(z)∈F_p[z] with deg K_p<r is computed by

K_r=0, Q_t=(2t−1)(3t−2)(3t−1)/18,
K_{t−1}=Q_t^{-1}[t³K_t−(t/3)binom(r,t)binom(2r,t)], t=r,…,1.

The Q_t are units on this range. That proved finite coefficientwise Clausen identity (division after p² divisibility) gives the weighted defect

E_p=(W_p−gh)/p² ≡ (1/2)[(1+6θ)K_p](1/2) (mod p).

**New theorem, all p=6r+1≥7 prime:**

R_p ≡ −(1/2)[(1+6θ)K_p](1/2) (mod p).

**Proof.** The original frozen finite Clausen identity is the exact rational equality W_p=gh−T_p with signed convolution
T_p=Σ_{0≤i,j<p,i+j≥p}(1+6(i+j))B_iB_j.
Its frozen valuation 0×2 / 2×0 support and exact reflection give T_p/p²≡R_p (mod p). Therefore E_p=(W_p−gh)/p²=−T_p/p²≡−R_p. Substitute the already proved Green formula, retaining the sign and (1/2)^p≡1/2 (mod p). QED. No CM normalizer, new source axiom, or sampled sign is inserted.

## Theorem B — Mother LIFT is exactly original 216 second digit

For every p≡13,19 (mod24), under accepted first-digit UR:

**(W_p−p)/p² ≡ Δ_p−R_p (mod p).**

**Proof.** W_p−p = p[(g/p)h−1]−T_p exactly, with both bracket and T_p/p² divisible as specified by the accepted UR and frozen reflected-tail theorem. Divide by p² *before* reduction and obtain Δ_p−R_p. QED.

Consequently LIFT ⇔ W_p≡p (mod p³), strictly at the accepted frozen scalar interface. Compose the already proved 216-high Q3 tail and Guo–Zudilin 2019's *both* full and half 2304 theorem (as matched in \`20261103_onhour_d25_2304_q4_literature_discharge.md\`) to obtain the equivalent **single still-open** original 216 half/high cancellation:

(W_{(p−1)/2}−p)/p² + (χ_p(6)/9)[(4+6θ_x)Q3_p](1) ≡ 0 (mod p).

Here θ_x=x d/dx, the Q3 finite polynomial and coefficient/source labels retain their previously proved definitions. This closes the previously missing *observer equivalence* rather than claiming the cancellation solved.

## Exact check and BRC provenance

The companion Python standard-library program was actually run: **77/77 target primes p≤2000** passed, verifying frozen R from the original signed triangular convolution, the p² Clausen tail, the independent finite Green backward recurrence, and the Δ-to-W relation. For p=13,19,37,43,373, W was independently calculated again from integer binomials and R by the original nested sum. Selected records (p;Δ,R;K(1/2),θK(1/2);E_green;W mod p³):
13;0,0;1,2;0;13
19;12,12;2,2;7;19
37;11,11;9,1;26;37
43;15,15;18,35;28;43
373;196,196;109,103;177;373.
At p=373, −(109+6·103)/2≡196 (mod373), exactly the original frozen R_373. This is finite regression, not a universal proof or an independent mathematical review.

BRC \`COMPOSE_APPLIED\`: source populations (k) and ordered reflected (i,s), valuation bands 0/1/2, signs, derivative ports and cutoffs retained. The final scalar Green observer is sufficient for the specifically proved signed tail/LIFT readout; it is not a general native Frobenius or X6 state. No P000 promotion.

## Unfinished original objective and control status

The full two-class p³ cancellation remains OPEN. Smallest next science: find a source-preserving terminating WZ/adjoint or direct frozen Δ−R proof of the single 216 half/high cancellation, checking sign, cutoff and derivative first at 13,19,373. Do not reprove accepted D24 UR or the already literature-discharged 2304 tail.

Native benchmark support issue #1559 still requires original p=373 H0/B0 divided-power [X]U mod139129, rank, *actual* semilinear Frobenius, signs, and independent verification. Issue #1558 tracks control support. On 2026-11-03 08:04:45Z, Sites returned \`research_authority_granted=false\`, \`write_relay_enabled=false\`; own checkpoint_list ACCESS_DENIED, old control_result CONTROL_REQUEST_NOT_FOUND, exact continuation CONTROL_QUOTA. Historical request \`research-onhour-20261031-0205-dispatch-r15\` was outer COMPLETE / inner FAILED UPSTREAM_CODE_REVIEW_REQUIRED; no replay. No native session/CLAIM/open/run/Source checkpoint/Result/review/admission. Original scheduler and notification settings were not modified.