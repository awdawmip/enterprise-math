# T6 q13: exact observer bridge and uniform large-prime valuation audit

2026-11-29, same informed Driver EM-DVR-DEBB5E, original contributor history retained. Frozen taskbook d84bd940cfb093cdc60e569f15cad58772a51dca:research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md. Scope: exact six positive-order shape moments and side exponent masses <=2331. Shared nonblind context; proof review of an existing author lemma plus a scope strengthening and synthesis with previously executed alternate solver, not a clean independent decisive review of Driver-authored computations.

## Existing evidence and exact audit

Read the exact original EM-X6-FB6990 p13 higher-valuation theorem at e09f7f4eac1a30705f63cc7823c0416de2092d31:research_notes/portable_direct/onhour_20261123_t6_p13_high_valuation_two_digit_cancellation.md (blob 7625ace208395f3e51ca60b3e3f507661f6e4012). The second digit is essential: 13 copies of a=169 cost 2184, so the first-digit test alone cannot eliminate that coefficient. The original author's localization, support argument and second-digit cancellation are valid at the stated cap. Preserve this attribution. Read also EM-T6SM-B134BD's p19/p17 carrier proof at b0c6144c55ac6e90dc9291be9165c977edf67594:research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/PROOF.md.

## Uniform strengthening (no H0 equality or maximal-prime assumption needed)

Let A,B be finite multisets of positive integer exponents, both of total mass <=2331. Put z_d=m_A(d-1)-m_B(d-1) for denominators 2<=d<=2332. Assume exact H_j(A)=H_j(B) for j=1,...,6, with H_j=sum(1-1/d)^j. Write S_j=sum d^(-j). The inverse binomial identity S_k=sum_{j=0}^k (-1)^j binom(k,j) H_j implies that every signed difference Delta S_k for 1<=k<=6 equals the same integer Delta H_0, whether or not H_0 agrees. In fact the next valuation proof only needs Delta S_k to belong to Z_(p), the localization with denominators prime to p.

**Claim:** for every prime p>=13, z_d=0 whenever p^2 divides d. No restriction on the other prime factors of d is necessary.

For p>=17, p^3>2332; for p=13 only d=2197 can have v_p>=3. At p=13 multiply the signed S_1 identity by 13^3 and reduce mod13: all terms with lower valuation vanish, as does 13^3 Delta H_0. Thus z_2197=0 mod13, and |z_2197|<=1 by the side mass cap, proving equality of its multiplicities.

For the remaining v_p=2 denominators d=p^2 m, 1<=m<=floor(2332/p^2), p not dividing m, the available m are distinct nonzero residues mod p (for p=13 remove m=13, for p>=17 m<=8). Multiply each signed S_k identity by p^(2k) and reduce mod p. The right side is zero, all v_p<=1 terms vanish, so sum_m z_(p^2 m) m^(-k)=0 mod p for k=1,...,6. Seven distinct signed support denominators require mass at least 28 p^2-7 >=4725>4662. Thus support size s<=6. On it the first s equations have determinant equal, up to sign, to the product of the nonzero inverse residues times their Vandermonde product. Therefore all coefficients are divisible by p.

For p>=17 the side bound gives |z_(p^2 m)|<=floor(2331/(p^2-1))<=8<p, hence all are zero. For p=13,m>=2 the bound is <=6, hence zero; only m=1 can remain with |z_169|<=13. Multiply the k=2 reciprocal identity by 13^4 and reduce modulo169. Every v_13<=1 term and the right side vanish modulo169, leaving z_169=0 mod169, hence z_169=0. For p^2>2332 the claim is vacuous. This recovers the original p13 result and p17/p19 guards and extends the formulation to all large primes simultaneously, with H0 not imposed.

## Exact q13 observer implication

For p=13, after cancellation of common named atoms, every nonzero 13-divisible denominator is d=13m with 13 not dividing m. Write m=13q+r, q>=0, 1<=r<=12. Its cost is 169q+13r-1. Let Q_+,Q_- be the sums of q over positive and negative high atoms, counted with multiplicity, q>=1. Separate signed costs <=2331 imply Q_+,Q_-<=13, and common atom cancellation preserves all observer differences and weakens each budget.

For k=1,...,6 multiply Delta S_k by 13^k and reduce mod13^k in Z_(13). The right side 13^k Delta H_0 vanishes even when H0 differs, and all 13-free denominators vanish. What remains is precisely sum_(r=1)^12 u_r r^(-k) + sum_(positive high) (13q+r)^(-k) - sum_(negative high) (13q+r)^(-k) =0 mod13^k, with signed q0 coefficients u_r and low weights 13r-1. Each remaining signed side budget is exactly the cap minus high cost, with any 13-free contributions omitted (a relaxation).

If Q_++Q_-=13, global sign symmetry gives exactly the seven splits (0,13)...(6,7). All high q partitions and nondecreasing r within equal parts are covered by the prior 885-pattern relaxed census; it did not sieve smoothness or exclude common high atoms. Consequently ANY exact positive-order-six-moment collision with masses <=2331 is impossible in the cancellation-normalized Q_++Q_-=13 sector of its 13-divisible profile, irrespective of its other denominator primes and even without H0 equality. The q13 exclusion does not require a lower-prime completion theorem: existence of any completion would already imply the contradicted necessary local conditions. This is a strengthened scope of the same finite result, not a fresh census or global p13 elimination. For other vertical orders a nonempty local class still requires completion.

## Reused execution evidence

First five splits 566 patterns: native Reference RVP-3A11F43D97DA924EE904, complete original receipt and source flow dvr-20261129-0002-t6-full-q13-review-flow-v1 verified. Remaining split(5,8) first 126 patterns at 9102add32110bb674f45dc10c240c68a5a195f:research_notes/driver/2026-11-28_t6_q13_split5_8_len1to5_partial_interval_join_ledger.md; final 28 at a11eb6e5b39657817ad4e5a4568276f63bddc714:research_notes/driver/2026-11-29_t6_q13_split5_8_len6to8_cpp_exact_audit.md; (6,7) all165 at b0c6144c55ac6e90dc9291be9165c977edf67594:research_notes/driver/2026-11-29_t6_q13_split6_7_complete_cpp_exact_audit.md. All three exact immutable notes read this turn; C++ source, residue sign, inclusive interval and both signed budgets inspected; no repeat of billion-pair census. Reference pass3 request dvr-20261129-0057-t6-q13-full-reference-pass3-v1 submitted once against exact RR and current review set; this evidence note is subsequent to that submission.

## Remaining scope

The sector closure is valid for the taskbook's exact rational shape observer. Any separate finite-resolution or observational-envelope variant allowing nonzero errors needs its own implication; this proof does not replace exact equality with approximate equality. Other p13 Q sectors, p17 remaining sectors, lower maximal primes and global T6=2332 remain open at this integration frontier; consume later exact saved evidence rather than rerun old work. H0 is not needed for this empty sector, but remains part of the mother question and may discriminate nonempty local candidates. No new formal Review, Result admission, Task or mother completion claimed. No sorry/admit/custom axiom.
