# D25 — exact three-source decomposition of the first weighted Hensel digit

Date 2026-11-01 +08. Status AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING. Research lane \`chatgpt-research-hourly-enterprise-math-20260923\`. Frozen scientific source pin \`c47e13e4aba0e006366f989d6334d443\` remains unchanged. This is a portable math result, not an authorized native run, Source checkpoint, review or H0/B0 experiment.

## Theorem

Let p=6r+1>=7 be prime, and Y_p(z)=sum_{k=0}^{p-1} ((1/6)_k (1/3)_k/(k!)^2) z^k. Let A_k=binom(r,k) binom(2r,k) / 2^k for 0<=k<=r, considered as p-integral rationals, S=sum_{k=0}^r A_k. Under the *now-proved* CM condition Y_p(1/2)=0 mod p, equivalently p mod24 in {13,19}, S lies in p Z_(p). Then the first digit of the original truncated Gauss series decomposes into exactly three sources:

    a_0 := Y_p(1/2)/p = C_leg + H_low + R_mid (mod p)

    C_leg = (S/p) (mod p),

    H_low = sum_{k=0}^r A_k [
        (1/6) sum_{j=0}^{k-1} 1/(j-r) +
        (1/3) sum_{j=0}^{k-1} 1/(j-2r)
    ] (mod p),

    R_mid = sum_{k=r+1}^{2r}
        (-1)^(r+k) r! (k-r-1)! (2r)! /
        [6*(2r-k)!*(k!)^2*2^k] (mod p).

All denominators in H_low and R_mid are p-units. C_leg is a genuine integer/rational p-adic carry; it cannot be discarded because S=0 mod p.

**Proof.** The exact identities 1/6=-r+p/6 and 1/3=-2r+p/3 hold over Q. For 0<=k<=r, write the original two rising factorials as products of perturbed (-r)_k and (-2r)_k and expand modulo p². All base factors are p-units. The constant term after division by (k!)² 2^k is A_k, while their p-linear terms are exactly the two harmonic sums in H_low. For r<k<=2r, exactly one factor, at index j=r of (1/6)_k, contributes a p. Deleting it and reducing the remaining product modulo p yields the R_mid factorial expression (including its sign). For k>2r, each rising factorial contributes a p, and the coefficient is divisible by p². Summing these three disjoint index ranges proves the formula. The independent CM selector supplies the hypothesis S in p Z_(p). QED.

## Consequence for the weighted target

The earlier Legendre-neighbor theorem says d_0=(theta Y_p)(1/2)=-r B mod p, with B=P_{2r-1}(t)/t, 2t²=1, and B nonzero for p mod24 in {13,19}. The still-open weighted first-digit condition 12 a_0 d_0=1 mod p is therefore equivalent to the explicit finite-source certificate

    -12*r*B*(C_leg + H_low + R_mid) = 1 (mod p).

This representation retains a Legendre lift carry, low-degree harmonic deformation and the first resonant interval as separately observable p-adic sources. It does NOT prove the first-digit condition universally.

## Exact finite check, residual obligations

Independent exact integer Python code recomputed original Y_p(1/2) modulo p² and all three independent source contributions for all 107 target-class primes p<=3000, with PASS on every comparison. Witnesses (p,C_leg,H_low,R_mid,a_0):
(13,7,3,1,11), (19,6,6,15,8), (37,21,27,12,23),
(61,29,55,1,24), (109,24,101,62,78), (373,340,352,78,24).
The nonzero resonance at 373 proves that the middle-range contribution cannot generally be ignored.

Next precise action: construct a universal CM/trace or WZ certificate for the displayed first weighted digit, then the previously derived second digit including exact integer carry and signed high-index cutoff C_p. Frozen mother target W_p(1/2)=p mod p³ for all p mod24 in {13,19} remains open. Original p=373 native H0/B0 belongs to #1559. Prior exact continuation bridge #6638 is terminal UPSTREAM_CODE_REVIEW_REQUIRED and handled by #1558; no Source authority, current claim, open or admission is inferred.

Prior D25 input: research_notes/portable_direct/20261101_hourly_d25_legendre_hensel_observer_inverse.md.
This-turn selector proof: research_notes/portable_direct/20261101_hourly_d25_cm24_cubic_hasse_selector_unweighted_p2.md.
