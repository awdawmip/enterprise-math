# R5: Exact recourse spectra and a residual-faithful suffix quotient

Date: 2026-11-15. Scientific source pin: \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`. Model: the *auxiliary one-dimensional integer indexed-center observer* (not a native six-dimensional X6 embedding), coverage radius 2, gaps \`(3,2,2,3,(2,1)^m)\`, independently shortening zero-based gaps 0 and 3 from 3 to 2, exactly K=3+m distinct indexed centers. Research status: AUTHOR_PROVED / EXACT_FINITE_CHECKED (m=1..6) / NOT_REVIEWED.

This builds on the verified author-side product theorem \`r5_nonisolating_pair_block_20261115/COUPLED_21_UNBOUNDED_SWITCH_THEOREM.md\` at commit \`669c96f388bb2d84ef297e9a2ee09a5751c97353\`: for each mask t in {0,a,b,ab}, the *complete* optimizer family decomposes as

\[
 F_t(m)=\{S_c\cup H: S_c\in G_t,\ H\in {\cal H}_{m-1}\},
 \qquad
 {\cal H}_{m-1}=\prod_{j=1}^{m-1}\{\{5+2j\},\{6+2j\}\}.
\]

The 7-event core families G_t have sizes (5,12,9,17); every selected center set has m+3 centers and optimal cost m+4. The product is a statement about exact index sets with disjoint core/suffix support, not an assertion that the underlying spatial coordinates are independent.

## Theorem 1: entire pairwise swap-distance spectrum factorizes

For equal-cardinality sets, define the directed swap metric \(\delta(S,T)=|S\setminus T|\), and for each t define the *ordered cross-family pair spectrum*

\[
 P_t^{(m)}(z)=
 \sum_{S\in F_t(m)}\sum_{T\in F_0(m)}z^{\delta(S,T)}.
\]

For every integer m>=1,

\[
 \boxed{P_t^{(m)}(z)=P_t^{(1)}(z)\,[2(1+z)]^{m-1}}.
\]

The four exact 7-event seed polynomials, computed by exhaustive core enumeration, are

| t | P_t^(1)(z) |
|---|---|
| 0 | 5+12z+6z²+2z³ |
| a | 5+23z+22z²+10z³ |
| b | 5+19z+17z²+4z³ |
| ab | 5+30z+37z²+13z³ |

**Proof.** Write each ordered pair as \((S_c\cup H_s,T_c\cup H_t)\). As the supports are disjoint,
\(\delta(S,T)=\delta(S_c,T_c)+\delta(H_s,H_t)\). Each independent appended pair has two matching ordered choices contributing weight 1 and two mismatching ordered choices contributing weight z. Therefore its contribution to the polynomial is \(2+2z\), independently for every one of m-1 appended pairs. Multiply by the complete core cross-family sum. This proof uses only the pre-established *exact* product decomposition and elementary counting; it does not infer the product decomposition from the finite tests. QED.

In particular, if S and T are uniformly and independently selected from their respective optimizer families, the suffix contribution to their swap distance has the exact binomial law Binomial(m-1,1/2). It adds \((m-1)/2\) to the mean pairwise distance; no asymptotic approximation is involved.

## Theorem 2: nearest-old recourse is a complete core observer

Define the minimum repair distance \(d_0^{(m)}(S)=\min_{T\in F_0(m)}\delta(S,T)\) and its histogram polynomial

\[
 H_t^{(m)}(z)=\sum_{S\in F_t(m)}z^{d_0^{(m)}(S)}.
\]

Then, for every m>=1,

\[
 \boxed{d_0^{(m)}(S_c\cup H)=d_0^{(1)}(S_c)},\qquad
 \boxed{H_t^{(m)}(z)=2^{m-1}H_t^{(1)}(z)}.
\]

The exact seed histograms are

| t | H_t^(1)(z) | worst nearest-old swaps |
|---|---|---:|
| 0 | 5 | 0 |
| a | 5+6z+z² | 2 |
| b | 5+4z | 1 |
| ab | 5+10z+2z² | 2 |

**Proof.** Every old optimal response is \(T_c\cup H'\). Since both summands of
\(\delta(S_c\cup H,T_c\cup H')=\delta(S_c,T_c)+\delta(H,H')\) are nonnegative, an old response with \(H'=H\) is always at least as good as any response with different suffix. Minimizing the core term gives the first identity; each core optimum has \(2^{m-1}\) suffix extensions, giving the histogram identity. QED.

The unique 7-event joint-only optimizer is \(S_c=\{1,2,3,6\}\), at nearest-old distance 2. Thus the complete joint-only residual Q contains exactly \(2^{m-1}\) distinct center sets, **every one at nearest-old distance exactly 2**. In contrast, their number is unbounded. Exact worst recourse against F0 for t=a,b,ab is respectively **2,1,2 for all m>=1**, while |Q|=2^(m-1).

This yields an explicit *residual-faithful observer quotient*: \(\pi(S_c\cup H)=S_c\) preserves closure-state membership, the residual class Q, and the entire nearest-old repair-distance function. For those specified observables, the exponentially many suffix choices are a common fiber. Pairwise distances between arbitrary separately chosen optimizer sets retain the suffix's Hamming residual, captured by Theorem 1; therefore the quotient is deliberately observer-relative rather than an erasure of full indexed-center identity.

## Exact calculations and reproducibility

The independently written standard-library Python file \`VERIFY_R5_RECOURSE_SPECTRUM.py\` enumerates **every** K-element center subset of n=5+2m events for each of the four closure masks, discards cover-radius violations, computes exact total nearest-center distance, obtains each entire optimizer family, and verifies both polynomial identities by direct integer pair-counting and minimum-over-all-old-solutions for m=1,..,6. It also verifies the Q distance claim. Re-executed local output:

- Status: \`PASS_R5_EXACT_RECOURSE_SPECTRUM\`.
- Finite coverage: 24 complete optimizer problems, all \(\binom{5+2m}{3+m}\) possible sets for every mask and m=1..6.
- For m=6: n=17, K=9, optimum cost 10, optimizer family sizes [160,384,288,544], |Q|=32, recourse maxima [0,2,1,2].
- Complete local execution JSON: 10,380 UTF-8 bytes, SHA-256 \`98861d3b895c9e33d545158aceff62e3b33d69f56ad33c84ace8a694ff1e01a3\`. The checked-in program deterministically regenerates this JSON under standard CPython JSON formatting.
- Exact arithmetic only. The arbitrary-m statements are proved from the existing all-m product theorem; the m<=6 exhaustive run independently tests their finite instances. No independent mathematical review or native P000 promotion is claimed.

## Next questions

1. For other finite-width optimal-path families, identify checkable conditions establishing a *common freely acting suffix symmetry*, enabling a similar observer-specific quotient without enumerating the full Cartesian product.
2. For the frozen 954-event K=214..221, examine whether a bounded boundary-state kernel preserves nearest-old recourse across effective cuts 8/9 and gives a small exact certificate for the observed Boolean diamond.
3. Test constructions where suffix choices are genuinely coupled by the optimum-cost DP rather than an exact product: determine whether the distance-spectrum generating function becomes a transfer-matrix power while the nearest-repair quotient survives.

The previous P000, native X6, SOURCE firewall, formal Task/CLAIM ownership and review scope remain unchanged.
