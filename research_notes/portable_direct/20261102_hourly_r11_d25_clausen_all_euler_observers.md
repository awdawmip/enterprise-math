# D25: arbitrary Euler-polynomial observers of the finite Clausen cutoff (2026-11-02)

Status: AUTHOR-DERIVED / EXACT-PROVED / EXACT-CHECKED (207 primes, degrees 0..4) / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Research logical ID chatgpt-research-hourly-enterprise-math-20260923, separate from maintenance.

## General theorem

For prime p=6r+1≥7, put h_k=(1/6)_k(1/3)_k/(k!)², a_k=(1/2)_k(1/3)_k(2/3)_k/(k!)³, G_p(z)=Σ_{k<p}h_kz^k, F_p(z)=Σ_{k<p}a_kz^k, and θ=z d/dz. The coefficientwise Clausen theorem proved in the companion first note yields E_p(z)=(G_p²−F_p)/p² in Z_(p)[z] and

    E_p(z) ≡ 2 Σ_{s=1}^r c_s z^(p−s) Σ_{j=s}^r h_j z^j (mod p),  (1)

with c_s=r!(2r)!(s−1)!²/[18(r+s)!(2r+s)!] modp, all p-unit denominators.

**For every polynomial φ(T)∈Z_(p)[T] of finite arbitrary degree**, the complete Euler-polynomial readout is

    [φ(θ)E_p] at z=1/2
       ≡ Σ_{s=1}^r c_s 2^s Σ_{j=s}^r φ(j−s) h_j 2^(−j) (mod p). (2)

For monomial operators θ^d, define

    D_d := [θ^d E_p] at z=1/2
       ≡ Σ_{s=1}^r c_s 2^s Σ_{j=s}^r (j−s)^d h_j 2^(−j) (mod p). (3)

**Proof:** θ is diagonal on the monomial z^n, acting with eigenvalue n. Apply φ(θ) to (1): each ordered pair has degree n=p−s+j, which is congruent to j−s modp. Evaluate at z=1/2, use Fermat 2^(p−1)=1 modp. All operations are exact modulo p. QED.

For fixed max degree D, precompute suffix moments Y_t(s)=Σ_{j=s}^r j^t h_j 2^(−j), 0≤t≤D. Then

    D_d = Σ_{s=1}^r c_s 2^s Σ_{t=0}^d binom(d,t)(−s)^(d−t) Y_t(s) (mod p),

using c_1=[18(r+1)(2r+1)]⁻¹ and c_(s+1)/c_s=s²/[(r+s+1)(2r+s+1)]. This reconstructs D_0..D_D with O(D²p) modular field operations, O(Dp) retained moments. It measures only this observer construction, not full solving complexity.

## Provenance and essential correction

The **signed original R cutoff was already established** in research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN_20260827.md and explicitly tied to frozen Delta_p/R_p in research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md. Those are predecessor research, not new contributions in this run.

The original kernel C_s=2^(s−1)(s−1)!²/[18(5/6)_s(2/3)_s] obeys C_s≡2^(s−1)c_s modulo p because 5/6≡r+1 and 2/3≡2r+1. For B_j=h_j2^(−j), old original R_p=2Σ_{j=1}^r B_j Σ_{s=1}^j [1+6(j−s)]C_s. Equations (2)-(3) give

    R_p = D_0+6D_1 (mod p).                                    (4)

The first note's Θ_373=196 is exactly the earlier known frozen R_373=196. Its signed special case is an alternative representation/check of prior accepted research; this unit extends the **operator family**, not the old R fact. Previously accepted CM0/UR sources have already supplied target-class p|G_p(1/2), so that premise need not be reproved. The original second-digit LIFT remains unproved.

## Executed exact checks

The companion Python stdlib checker computes d=0..4 independently through the integer mod-p³ product derivative Σ_{t=0}^d binom(d,t)(θ^tG)(θ^(d−t)G)−θ^dF, divides by p² and compares against (3) using low-index suffix moments. All 207 primes ≤3000 with p≡1 mod6 pass. Example (D0,D1,D2,D3,D4): p=13 (6,12,12,12,12), p=19 (18,18,0,2,6), p=373 (132,135,181,37,117), p=1171 (831,447,1042,821,969). These finite digit values are exact observations, distinct from the general symbolic theorem.

## Continuation

The real remaining objective is cancellation of the source-faithful original signed second digit, not rederivation of R or CM0. Test whether new higher D2/D3 ports contribute a closed finite CM/Frobenius relation, and examine independent Cauchy K0=0 / K1=−1/2 conjectures for combination. Retain original R provenance, immutable science pin, P000 and ACTIVE worldview. Current native gateway status 2026-11-02: version 0.6.11, CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED; research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5. Historical Research #6637 recovery was read-only; #6638 continuation definitely failed. Existing support enterprise-math#1558 is responsible for control repair and #1559 for native H0/B0. No new native session, CLAIM, OPEN, checkpoint, Result, review or acceptance; author evidence only.