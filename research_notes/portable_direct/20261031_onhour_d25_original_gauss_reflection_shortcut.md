# D25 / Original Gauss reflected-tail shortcut — derivative-free source certificate

**2026-10-31 · AUTHOR-SIDE PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.** This is an independently checkable shorter proof kernel for the **already frozen** signed reflector, not a new Result or a proof of LIFT. Parent `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** unchanged.

## Theorem and proof

For any prime p=6l+1≥7, set b_k=(1/6)_k(1/3)_k/(2^k(k!)²) for 0≤k<p, g=Σ b_k, h=Σ(12k+1)b_k, and A_p=Σ_{n<p}(6n+1) binom(2n,n)² binom(3n,n)/216^n. All are p-local rationals. Define G_i=binom(l,i)binom(2l,i)2^{-i} (mod p), 1≤i≤l; d_1=1/10 (mod p), d_{a+1}/d_a=36a²/[(6a+5)(3a+2)] (mod p). Every indicated denominator is a p-unit. Retain, **without renaming or modifying it**, the previously source-defined signed reflector

    R_p = 2 Σ_{i=1}^l G_i Σ_{a=1}^i [1+6(i-a)] d_a  (mod p).

**Exact new derivative-free proof route:**

    (g h - A_p)/p² = R_p  (mod p).                              [1]

Clausen's *formal coefficient* identity `_2F1(1/6,1/3;1;z)^2=_3F2(1/2,1/3,2/3;1,1;z)`, applied only to the finite polynomial Σ_{k<p}b_k(2z)^k and its (1+6z∂_z) readout at z=1/2, yields an **exact rational** upper-triangle identity

    g h - A_p = Σ_{0≤i,j<p, i+j≥p} [6(i+j)+1] b_i b_j.          [2]

There is no unlicensed evaluation of an infinite series. The original recurrence is b_{k+1}/b_k=(6k+1)(3k+1)/[36(k+1)²]. Thus v_p(b_k) is 0 for 0≤k≤l, 1 for l<k≤2l, and 2 for 2l<k<p. Among i+j≥p, all terms have valuation ≥2; those of valuation **exactly** 2 must be i≤l, j=p-a with 1≤a≤i, or vice versa. So the quotient [2]/p² modulo p equals twice Σ_{i=1}^l (b_i mod p)Σ_{a=1}^i[1+6(i-a)](b_{p-a}/p² mod p).

For low i, -l≡1/6 and -2l≡1/3 (mod p), whence b_i≡G_i. For the reflected top coefficients, the single zero factors in (1/6)_{p-1} and (1/3)_{p-1}, together with Wilson/Fermat, give b_{p-1}/p²≡(1/5)(1/2)=1/10 modulo p. Backward application of the exact coefficient recurrence gives

    (b_{p-a-1}/p²)/(b_{p-a}/p²)
      ≡ 36a² / [(6a+5)(3a+2)]  (mod p), 1≤a<l.

Consequently b_{p-a}/p²≡d_a for all 1≤a≤l. The upper-tail quotient is precisely the **existing signed** R_p. This proves [1] for the entire p≡1 (mod 6) class, without requiring the supersingular/UR premise, any first/second parameter jet, Green-current integration, or native Frobenius.

On the frozen p≡13,19 (mod24) subset, **consume** the accepted UR fact G_p h≡1 (mod p), G_p=g/p. Then the *already known* LIFT equivalence follows by the shorter dependency chain:

    Δ_p-R_p ≡ (A_p-p)/p² (mod p),
    Δ_p=(G_p h-1)/p.                                           [3]

[3] **does not prove the remaining right side is zero**. The all-target LIFT remains OPEN.

## One terminal-only observer optimization

For precisely the signed scalar R (not its future reversible state), define S_a=Σ_{i=a}^l G_i and T_a=Σ_{i=a}^l iG_i. Then

    R_p = 2 Σ_{a=1}^l d_a [(1-6a)S_a+6T_a]  (mod p).           [4]

Backward suffix accumulation evaluates [4] in O(l) ring operations. BRC: COMPOSE_APPLIED / TERMINAL_SCALAR_ONLY. This is **not** a safe replacement for the earlier reversible four-state transfer in arbitrary future operations, and not a native H0/B0 rank/Frobenius/κ readout.

## Exact check and source limits

A self-contained independent Python standard-library check in the current conversation evidence attachment `d25_original_gauss_tail_reflection_20261031.py` was **actually executed**: every p≡1 (mod6) prime in [7,397] (37 primes); full original 216 integer-binomial A_p mod p³; every exact valuation tier; original finite Clausen upper-convolution; every top reflection coefficient; original double-sum R; and terminal O(l) suffix R. All passed. Witnesses (p,R,upper-tail mod p³): (13,0,0), (19,12,4332), (37,11,15059), (67,21,94269), (373,196,27269284). At 373 the signed tail is exactly 139129×196 mod 373³. Finite checks are **not** a universal LIFT proof.

External related prior art: Zhi-Hong Sun, *AIMS Mathematics* 7 (2022) 2729–2781, Conjecture 5.28, DOI 10.3934/math.2022153, gives an **unweighted** 216 binomial-sum conjecture for the D=-24 residue classes; it is not this weighted (6n+1) claim and is NOT used as a theorem.

**Recovery:** Research lane `chatgpt-research-onhour-enterprise-math-20260923`, distinct from maintenance `chatgpt-hourly-enterprise-math-20260921`. Historical read-only recovery `awdawmip/kimi-query-bridge#6632` verified **no own current CLAIM/run**; original dispatch `#6633` FAILED UPSTREAM_CODE_REVIEW_REQUIRED, not replayed. Fresh Site gateway static-machine-readonly, research_authority_granted=false. Old neutral staging is independent. Publishing this author-side note is NOT Source checkpoint, registration, Result, review, or admission. Native benchmark `awdawmip/enterprise-math#1559` remains OPEN/PENDING_OWNER: original p373 H0/B0 divided power [X]U mod139129, rank, actual semilinear Frobenius/eta, signed Green/Hesse, κ and independent replay **NOT_EXECUTED**. Next actual math: derive all-target WZ/CM proof of A_p=p mod p³ (or exact counterexample), rather than extending completed boundary identities. Current task schedule/notifications untouched.
