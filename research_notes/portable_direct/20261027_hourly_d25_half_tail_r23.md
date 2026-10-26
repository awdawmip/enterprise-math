# D25/LIFT R23 — Half-truncation port cancellation and reflected W high-jet

Date 2026-10-27, Asia/Hong_Kong. Logical Research conversation `chatgpt-research-hourly-enterprise-math-20260923`. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`; mother goal OPEN. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / EXTERNAL_PROVED_INPUT / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is NOT Source checkpoint, native CM, Result or independent Driver review.

## Exact previous and published input

Consume R22, `research_notes/portable_direct/20261027_hourly_d25_ws_extra_tail_valfiltration_r22.md` @ `953a90bc8d1d8cf252c1e671741a4b7d5e3625e8`; do not recredit it. For all primes p=6m+1>=7, in Z_(p), let

    w_k=(6k+1)(2k)!(3k)!/((k!)^5 216^k);
    s_k=(8k+1)(4k)!/((k!)^4 2304^k);
    W_p=sum_(k=0..p-1) w_k; S_p=sum_(k=0..p-1) s_k.

External **proved** theorem, not original to this research: V. J. W. Guo and W. Zudilin, *A q-microscope for supercongruences*, Adv. Math. 346 (2019) 329–358, arXiv:1803.01830, proves BOTH S(p−1) and S((p−1)/2) are congruent to p(-3/p) mod p^3 for p>3. Hence the actual S upper half sums to zero mod p^3. This does NOT prove W=S.

## Theorem A: S has two source-labeled high ports that cancel in the declared full-sum observer

Put L=3m=(p-1)/2, K=4m, H=floor((3p-1)/4), J0=floor(3m/2), j=p-1-k. For J0<=j<=3m-1 define in F_p (factorial denominators are units)

    B_j = 2(8j+7)2304^j(j!)^4 / (4j-6m+2)!.

The exact termwise reflection is s_(p-1-j)/p^2 == B_j (mod p). The already-known R22 S-only tail T_p is sum_(j=J0..2m-1)B_j. **New complementary port** M_p=sum_(j=2m..3m-1)B_j equals p^(-2)sum_(k=3m+1..4m)s_k mod p. The published TWO-truncation theorem plus elementary valuation cutoffs proves, for every p=6m+1>=7,

    M_p+T_p==0 (mod p),
    sum_(j=J0..3m-1) B_j==0 (mod p).             [A]

Proof: in L+1<=k<=H, 2p<=4k<3p, so (4k)!/p^2 == 2(4k-2p)! (mod p) using Wilson. For j=p-1-k, the complement 4j-6m+2 is even and (4k-2p)! == -1/(4j-6m+2)!, whereas (k!)^(-4)==(j!)^4, 8k+1==-(8j+7), 2304^(-k)==2304^j. Signs cancel. For k>H, s_k=0 mod p^3. Guo–Zudilin's equality S(p-1)=S(L) mod p^3 therefore makes the sum of these source-distinct ports zero. This is an aggregate identity, NOT termwise erasure. QED.

## Theorem B: genuinely W-sourced reflected high jet and the reduced all-prime bridge

For 2m<=j<=3m-1, put

    A_j = (6j+5)216^j(j!)^5 / ((2j+1)!(3j-6m+1)!) in F_p,
    U_p = sum_(j=2m..3m-1) A_j.

Termwise w_(p-1-j)/p^2 == A_j (mod p). Proof: for k=p-1-j, 3m+1<=k<=4m, both 2k and 3k are in [p,2p). Wilson gives (2k)!/p==-(2k-p)! and (3k)!/p==-(3k-p)!; their complements give (2k-p)!==1/(2j+1)! and (3k-p)!==(-1)^j/(3j-6m+1)!. Also (k!)^(-5)==(-1)^(j+1)(j!)^5, 6k+1==-(6j+5), 216^(-k)==216^j. The signs cancel, with every denominator a p-unit. QED.

Combining this with [A], and the cutoff w_k=0 mod p^3 for k>4m, yields the new sharp identity

    W_p-S_p == sum_(k=0..3m)(w_k-s_k) + p^2 U_p   (mod p^3). [B]

Therefore the still-OPEN all-prime bridge W_p==S_p mod p^3 is **equivalent** to the smaller OPEN obligation

    sum_(k=0..3m)(w_k-s_k) == -p^2 U_p            (mod p^3). [C]

[B] is proved, [C] is not. Under the specified p^3 full-sum observer the S-only R22 tail has a proven compensating S-mid port, while the genuinely unmatched high coordinate is W-sourced U. Neither port may be deleted from a richer source observer.

For the indicated interiors, both streams admit cross-multiplied holonomic identities (including zero-weight cases):

    (6j+5)(2j+3)(3j+4)(3j+5)A_(j+1)
      ==36(6j+11)(j+1)^3 A_j;
    (8j+7)(4j+5)(4j+6)(4j+7)B_(j+1)
      ==576(8j+15)(j+1)^3 B_j                 (mod p).

These are direct factorial ratios with 6m==-1 mod p, NOT themselves a WZ bridge.

## Explicit source-preserving numerical certificate, including p=181 exception

At p=181 (target class 13 mod24), T=0 and M=0 but U=152 mod181; low-half sum_(k=0..90)(w_k-s_k)==950069 modulo 181^3=5929741; p^2 U=4,979,672, adding to 5,929,741. So the exceptional S-tail zero does **not** erase the W-high source.

Other exact finite observations, rows (p: U,M,T,low-difference mod p^3):
13:10,7,6,507; 19:9,3,16,3610; 181:152,0,0,950069; 373:266,92,281,14886803; 733:67,174,559,357834474.

An author-side Python standard-library exact checker was **actually executed** locally on all 80 primes 7<=p<=997, p=1 mod6: 15,267 termwise reflected W/S coefficients, modular valuations, both recurrences, two-source S half-cancellation and six independent direct huge-integer binomial cases p=7,13,19,181,373,733; all PASS. Its scope is finite; all-prime Theorem A uses the named external published theorem, Theorem B uses exact factorial algebra, and the global [C] remains unproved. No native experiment, external independent review, formal checker or axioms were run/assumed.

BRC: COMPOSE_APPLIED to the precise two-series, branch/index-j-reflection and p-adic filtration carrier; its aggregate full-sum observer admits cancellation [A], but full source provenance remains needed under other observations/future operations. These indices do not represent P000 native spatial axes; ACTIVE P000/worldview unchanged.

**Continuation.** Next portable unit: seek a genuine finite p^3 WZ/creative-microscoping transfer for [C] in p=13,19 mod24, or exact fully labeled counterexample; retain original z=2 six Hasse 3+2+1 source ports, finite faces, positive infinity and ordered high/high. Original native H0/B0, [X]U modp^2, semilinear Frobenius eta/kappa, native p373 and Driver pending. Formal Source checkpoint/claim/Result unchanged; issue enterprise-math#1558 owns historical CLAIM CAS fault. Activity checkpoint pending separate validation, not equated to GitHub publication.
