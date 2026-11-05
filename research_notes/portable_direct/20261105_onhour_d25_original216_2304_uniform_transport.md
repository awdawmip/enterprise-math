# D25 SECOND-DIGIT-LIFT: rigorous 2304 comparator and exact cross-model transport experiment

Date: 2026-11-05. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7.
Frozen scientific input: c47e13e4aba0e006366f989d6334d443f6333ae3.
Research conversation: chatgpt-research-onhour-enterprise-math-20260923.
Status: AUTHOR-SIDE EXACT REFORMULATION + EXACT CUTOFF LEMMA + FINITE EXACT EXPERIMENT; UNREVIEWED / NOT_ADMITTED. Native H0/B0 not executed.

## Fixed formulas

Original 216 weighted sum:
W_p = sum_{k=0}^{p-1} (6k+1) binom(2k,k)^2 binom(3k,k)/216^k.
Comparator 2304 weighted sum:
V_p = sum_{k=0}^{p-1} (8k+1) binom(2k,k)^2 binom(4k,2k)/2304^k.

The 2019 published Guo--Zudilin theorem is an exact match for V_p: Victor J. W. Guo and Wadim Zudilin, "A q-microscope for supercongruences", Advances in Mathematics 346 (2019), 329-358, arXiv:1803.01830v6 (2019-02-13), https://arxiv.org/abs/1803.01830 . Their established result for every prime p>3 is
    V_p = p * (-3/p) (mod p^3),
where (-3/p) is the quadratic character (also described by the paper as character modulo 3).

Consequently, for every p>3, by subtraction of this published theorem,
    W_p = p * (-3/p) (mod p^3)
    IF AND ONLY IF
    W_p = V_p (mod p^3).
This equivalence is rigorous; the cross-model congruence on the right is the remaining open scientific step, not an asserted theorem. In particular for frozen p = 13 or 19 (mod 24), (-3/p)=+1, hence the frozen W_p=p (mod p^3) is EQUIVALENT to the original-model W_p=V_p transport. Previous author-side exact source alignment at 3537262a71d7cc40442326bf07fdee17375850fc established Delta_p-R_p = (W_p-p)/p^2 (mod p) on the frozen classes. No change to the immutable source definition of R_p is made.

## Additional exact p-adic valuation / boundary lemma for V

For each prime p>3 and 0<=k<p, let
    b_k = binom(2k,k)^2 binom(4k,2k)/2304^k
        = (4k)! / [2304^k (k!)^4].
The number of occurrences of p in (4k)! is floor(4k/p), since 4k<4p and k! is a p-adic unit. Thus v_p(b_k)=floor(4k/p) EXACTLY. Therefore k>floor((3p-1)/4) implies p^3 | b_k, and
    V_p = sum_{k=0}^{floor((3p-1)/4)} (8k+1)b_k (mod p^3).
This finite cutoff preserves the original weight, index, p-valuation and observer provenance.

For the 216 model, the previous exact cutoff is k<=floor((2p-1)/3) (mod p^3), as established in 20261105_onhour_d25_uniform_character_p3_evidence.md.
This gives two native finite endpoints for a potential terminating cross-model certificate, rather than discarding their difference.

## Complete finite scan and independent checker

Executed standard C++ exact integer modular arithmetic for ALL 1227 primes 5<=p<=10000 (full sum modulo p^4, no floating point); used recurrence
    a_{k+1}/a_k = (2k+1)(3k+1)(3k+2)/(36(k+1)^3)
    b_{k+1}/b_k = (4k+1)(4k+2)(4k+3)/(576(k+1)^3).
All denominators are units for k+1<p. No failed W_p-V_p divisible-by-p^3 checks (0/1227), no failed 2304 p^3-tail checks (0/1227).
The fourth digit (W_p-V_p)/p^3 mod p is nonzero for all p>=7 in this exact set (1226 primes), and zero at p=5. Selected exact fourth-digit data: p=7:4, 11:1, 13:11, 19:6, 139:105, 373:114, 9973:1122. At p=13 original W mod 13^4=19786, V mod13^4=24180, difference=24167=11*13^3; the p^4-wide congruence fails, confirming previous branch evidence.

Independently computed BOTH models via original binomial factors (Python arbitrary precision comb, modular powers; distinct from the ratio recurrence) for all 166 primes 5<=p<=997. All 166 W, V and signed difference values modulo p^4 matched. CSV and both executable programs are packaged in the user-facing local evidence bundle.

## Next exact scientific action

Attempt a terminating, p-parametric 216-to-2304 transformation/WZ certificate for W_p-V_p=0 mod p^3, retaining both distinct original cutoffs and weight factors. Potential approach: derive a finite quadratic/transformation relation between the (1/2,1/3,2/3) and (1/2,1/4,3/4) hypergeometric series, then compute truncated boundary contribution and its valuation explicitly; compare original 216 signed R_p with transformed 2304 boundary. Claim the full frozen target only after a complete proof or exact counterexample.

Native benchmark Issue #1559: fixed p=373 original-class H0/B0 divided-power module and [X]U mod139129, rank, semilinear Frobenius, eta, kappa and independent review remain OPEN separately. Current Source request onhour11-20261105-1405-d25-cont: SUCCEEDED, execution_authorized=false; no new native Claim, Run, Source checkpoint or admitted Result.
