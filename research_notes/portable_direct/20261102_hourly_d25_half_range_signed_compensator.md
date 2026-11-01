# D25: an exact signed 216 upper-half compensator and 216/2304 reduced bridge

Date 2026-11-02 +08. TASK_RESEARCH portable author derivation; AUTHOR-DERIVED / CLASSICAL-COMPARATOR-DEPENDENT / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific frozen Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Historical Research logical lane chatgpt-research-hourly-enterprise-math-20260923, distinct from CONTROL_PLANE_MAINTENANCE. This is external arithmetic, not native X6 or H0/B0.

THEOREM A (all primes p=6r+1 >=7). Define
  A_k=(6k+1)*(2k)!*(3k)! / ((k!)^5*216^k),
  S_full=sum_{k=0}^{p-1} A_k, S_half=sum_{k=0}^{3r} A_k,
and the precisely p-integral finite-field correction
  sigma_p = sum_{k=3r+1}^{4r}
       (6k+1)*(2k-p)!*(3k-p)! / ((k!)^5*216^k)   in F_p.
Every denominator above is a unit modulo p. Then
  S_full - S_half = p^2*sigma_p (mod p^3).          (A)

PROOF. For 0<=k<p, p>=7, Legendre's formula gives v_p((2k)!)=floor(2k/p), v_p((3k)!)=floor(3k/p), as 3k<p^2. The denominator is a p-unit. The unique zero modulo p of weight 6k+1 in this range occurs at k=r, so weights in k>3r are units. For 3r<k<=4r, 2k=p+s and 3k=p+t (0<=s,t<p), giving valuation precisely two; for 4r<k<p, 3k>=2p and the valuation is >=3. Wilson gives (p+s)!/p = -(s)! modulo p for 0<=s<p, and similarly for t. Both signs cancel, yielding exactly the summand for sigma_p as A_k/p^2 modulo p. Higher indices vanish individually mod p^3. QED.

THEOREM B (a literature-dependent full bridge reduction). Define
  B_k=(8k+1)*(4k)! / ((k!)^4*2304^k),
  T_full=sum_{k=0}^{p-1} B_k, T_half=sum_{k=0}^{3r} B_k.
Guo--Zudilin, "A q-microscope for supercongruences", Advances in Mathematics 346 (2019), 329-358, DOI 10.1016/j.aim.2019.02.008, arXiv:1803.01830, proved BOTH
  T_full = p*(-3/p) = T_half (mod p^3), for every prime p>3.
Hence their published theorem, together with author Theorem A, yields
  S_full-T_full = (S_half-T_half)+p^2*sigma_p (mod p^3).   (B)
In the frozen target p mod24 = 13 or 19, (-3/p)=+1. Therefore
  S_full = p (mod p^3)
  iff S_half - T_half = -p^2*sigma_p (mod p^3).          (C)
Equation (C) is a proved equivalence, **not a universal proof that its RHS holds**.

PROVENANCE / BRC COMPOSE_APPLIED. Population is the two source-labeled exact signed rational summand lists, with k, valuation, weight, unit, and denominator. Observer: weighted sum difference modulo p^3; future operation: half-range deletion plus explicit p^2 sigma repair. The full 2304 upper-half deletion is certified by the two published Guo--Zudilin truncation congruences. The p13 weighted resonance k*=(5p-1)/8 lies ABOVE half (valuation3, discardable here); the p19 weighted resonance k*=(3p-1)/8 lies WITHIN half (valuation2, retained). The 216 resonance k=r (valuation1) is retained in both. Other derivative, Clausen and native operators have separate observation requirements; no P000 or X6-native transfer is asserted. The first omitted 2304 Clausen-square coefficient for p13 remains a distinct source channel.

ACTUAL EXACT EXECUTION. The companion Python checker separately computes both complete and half finite sums by exact p^3 rational recurrences and computes sigma using factorial units; a third direct binomial/factorial implementation checks small primes. All 207 primes p<=3000 with p=1 mod6 passed (A), 2304 half/full comparison, and algebraic support. The 107 original target-class primes (53 p13, 54 p19) also pass (C), a *finite check* of the still-open target. sigma was nonzero in all 107 checked target cases; this is not a general nonvanishing theorem.

Witnesses (p, sigma mod p, S_half-T_half mod p^3):
 (13,10,507); (19,9,3610); (37,20,23273);
 (61,17,163724); (373,266,14886803).
At p373, p^2*sigma=37008314 and 373^3=51895117, so the corrected half difference vanishes exactly modulo p^3.

NEXT: derive a general CM/character/WZ certificate for (C) using the half-range ensembles and explicit r-term sigma. At least check candidate source maps at p13 and p19; keep both distinct resonances, 216 weighted cancellation, and proven independent Guo--Zudilin source. Do not repeat CM selector, full filtrations, first-digit Green, or previously verified computations. Native H0/B0 p373 is separately pending #1559.

CONTROL as read 2026-11-02: authenticated Gateway 0.6.11 research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED. Original own recovery #6637 historical SUCCEEDED; continuation #6638 definitively FAILED; no blind replay. Control support #1558; no new native CLAIM, OPEN, Source checkpoint, Result, review or admission. Prior session/contributions and neutral staging preserved. P000, ACTIVE worldview, task's frozen scientific source pin and existing task scheduling/notifications unchanged.
