# D25: finite Clausen-square high–low defect at the original signed 216 observer (2026-11-02)

Status: AUTHOR-DERIVED / EXACT-PROVED (conditional algebraic identities) / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Logical research lane: chatgpt-research-hourly-enterprise-math-20260923, distinct from CONTROL_PLANE_MAINTENANCE. Mother D25: Δ_p-R_p≡0 (mod p), p mod 24∈{13,19}, equivalent to original signed S_p≡p (mod p³). External p-adic calculation; no X6/P000 native theorem or native Source checkpoint is claimed.

## Definitions and exact input

Let p=6r+1≥7 be prime. Work in Z_(p); θ=z d/dz. Define

    h_k=(1/6)_k (1/3)_k/(k!)²,
    a_k=(1/2)_k (1/3)_k (2/3)_k/(k!)³,
    G_p(z)=Σ_{0≤k<p} h_k z^k,
    F_p(z)=Σ_{0≤k<p} a_k z^k.

Classical Clausen identity in Q[[z]]:

    [₂F₁(1/6,1/3;1;z)]² = ₃F₂(1/2,1/3,2/3;1,1;z).

In particular, Σ_{k=0}^n h_k h_{n-k}=a_n exactly for all n≥0. Original 216 terms are A_k=a_k2^(-k)=binom(2k,k)²binom(3k,k)/216^k, and

    S_p=[(1+6θ)F_p(z)]_{z=1/2}=Σ_{k<p}(6k+1)A_k.

## Theorem 1: polynomial p² truncation and exact first surviving defect

For k<p, v_p(h_k) equals 0 on [0,r], 1 on [r+1,2r], 2 on [2r+1,p-1]. Hence as an entire polynomial (not just an evaluation),

    G_p(z)² ≡ F_p(z) (mod p²).                                      (1)

For 1≤s≤r all factorial denominators below are p-units. Put

    c_s = r!(2r)!(s-1)!²/[18(r+s)!(2r+s)!] (mod p).                  (2)

Then the exact reflected high-coefficient unit is

    h_{p-s}/p² ≡ c_s (mod p).                                       (3)

The whole polynomial quotient is p-integral coefficientwise and satisfies

    (G_p(z)²-F_p(z))/p²
      ≡ 2 Σ_{s=1}^r c_s z^(p-s) Σ_{j=s}^r h_j z^j (mod p).           (4)

**Proof.** In (1/6)_k the unique p-multiple appears as p/6 at factor index r, and in (1/3)_k as p/3 at index 2r. k! is a p-unit for k<p. Thus the valuation tiers are exact. At degrees n<p, the truncated convolution is the full Clausen coefficient a_n. At n≥p, the coefficient has p-adic valuation at least 2, because pairs with both indices ≤2r sum to ≤4r<p, and a 0-valuation paired with 1-valuation index sums to at most 3r<p. This proves (1).

Among all n≥p, valuation exactly 2 can arise only from an ordered valuation-2 / valuation-0 pair. Write the high index k=p-s, the low index j≤r. The degree condition k+j≥p forces s≤j≤r, with s≥1. All other degree≥p pairs have valuation≥3. The two ordered counterparts produce the factor 2 in (4).

For (3), remove p/6 and p/3 at indices t=r and t=2r from h_{p-s}. Reducing all other factors modulo p gives

    h_{p-s}/p² ≡ (-1)^r r!(2r)!(5r-s)!(4r-s)! /
                    [18((p-s)!)²] (mod p).

Wilson reflection a!(p-1-a)!≡(-1)^(a+1) (mod p) transforms (5r-s)! to (r+s)!, (4r-s)! to (2r+s)!, and (p-s)! to (s-1)!. The signs cancel and give (2) and (3). Substitution gives (4). QED.

## Theorem 2: signed operator and linear-time source-preserving reconstruction

At z=1/2 define D₀=[(G_p²-F_p)/p²] mod p and D₁=[θ(G_p²-F_p)/p²] mod p, Θ_p=D₀+6D₁. As 2^(p-1)≡1 (mod p), (4) becomes

    D₀ = Σ_{s=1}^r c_s 2^s Σ_{j=s}^r h_j2^(-j) (mod p),
    D₁ = Σ_{s=1}^r c_s 2^s Σ_{j=s}^r (j-s)h_j2^(-j) (mod p).      (5)

Define suffix moments X_s=Σ_{j=s}^r h_j2^(-j), Y_s=Σ_{j=s}^r j h_j2^(-j) modulo p. Then

    Θ_p = Σ_{s=1}^r c_s 2^s[(1-6s)X_s+6Y_s] (mod p),

with c₁=[18(r+1)(2r+1)]⁻¹ and c_(s+1)/c_s = s²/[(r+s+1)(2r+s+1)] (mod p). Computing the defect from the supplied low-index coefficients uses O(p) modular field operations and O(p) memory; no double loop or high-index coefficients.

Applying (1+6θ) to (4) gives the signed 216 congruence

    S_p ≡ G_p(1/2)[G_p(1/2)+12(θG_p)(1/2)]-p²Θ_p (mod p³).       (6)

If additionally G_p(1/2)≡0 (mod p), put u=G_p(1/2)/p (mod p²), v=(θG_p)(1/2) (mod p²). The frozen 216 target is *exactly equivalent under this hypothesis* to

    12uv+p(u²-Θ_p) ≡ 1 (mod p²).                                   (7)

This is a nontrivial reduced target, not a proof that (7) always holds. Finally G_p(z)≡P_r(z)=Σ_{j=0}^r binom(r,j)binom(2r,j)z^j (mod p), F_p≡P_r² (mod p). Its CM root P_r(1/2)≡0 was checked in finite target range only.

## Exact checks and independent certificates

Companion Python standard-library code d25_clausen_truncation_defect_20261102.py with saved stdout log checks all 207 primes p≤3000, p≡1 (mod 6): (1), (5)-(6), original signed sum, and O(p) kernel. All 107 target-class primes also pass the finite Hasse root. Independent coefficientwise *polynomial* convolution at p², factorial reflection, direct ordered high–low sum, and original binomial A coefficients were checked for p=7,13,19,31,37,43,61,373,1171. These tests use exact integers, not floats. In the 207-prime finite sample S_p≡p (mod p³), but that last observation is finite evidence, not a theorem established here.

Sample new defect digits (p;D₀,D₁,Θ_p):

    13: (6,12,0)
    19: (18,18,12)
    37: (14,18,11)
    373: (132,135,196)
    1171: (831,447,0).

For p=373, the signed second-digit correction is p²·196 (mod p³); the original k-index, cutoff n=k+j≥p, and two ordered source branches are retained.

## BRC, status, next action

BRC COMPOSE_APPLIED: carrier = ordered (k,j), exact factorial coefficients, valuation tiers and cutoff; operation = squaring then signed (1+6θ) readout at z=1/2 through p³; sufficient retained observer = D₀,D₁,Θ_p plus G_p and θG_p. This is external integer arithmetic, not an unprovided P000-native geometry embedding.

Prior independent source: existing 20261102_hourly_r11_d25_cauchy_truncation_carry.md and 20261102_hourly_r11_d25_cauchy_second_carry_p3.md; do not count their finished kernels as new predecessor research. Continue the smallest open science: prove or refute the CM root and (7) uniformly for p mod24=13,19, using a finite-field/CM transformation, and independently connect the quadratic defect with the older open Cauchy K₀=0, K₁=-1/2 hypotheses. Distinct predecessor contributions and frozen science pins must be maintained.

As observed 2026-11-02 through native em_status, Gateway 0.6.11 returns CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5. Historical same-lane bridge #6637 is read-only recovery and #6638 is definite failed continuation, never replay either as a write; no native CLAIM, OPEN, checkpoint, Result or review in this unit. Current responsible control support enterprise-math#1558, outstanding native H0/B0 benchmark #1559. Activity registration remains pending, with prior session/claim/staging preserved. The project Git commit is neutral author-side evidence, not Source admission.