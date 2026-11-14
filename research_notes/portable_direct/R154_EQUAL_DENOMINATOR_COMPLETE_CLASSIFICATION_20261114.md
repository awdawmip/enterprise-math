# R154 — Complete all-length classification of equal-denominator Sturmian slope supports

Date: 2026-11-14 (Asia/Shanghai). Status: author-side exact proof and reproducible exhaustive finite verification; independent review NOT_REVIEWED. Frozen input: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`, unchanged. Scope: the external scalar S23 mechanical-word observer (R146), not a native X6 correspondence.

Predecessors: R146 \`b02b0c242b274bc6a82111dbd3600126a2867319\`, \`research_notes/brc_s23_av_r146_fiber_affine_period_20261114/PROOF.md\`; R153 \`e6e436cb90f6c943b3825a4a2fe26b0500c558f8\`, \`research_notes/portable_direct/R153_DISTINCT_DENOMINATOR_RESONANCE_20261114.md\`.

## Definitions and main theorem

For a binary word w of length m, write s_0=0, s_j=sum_{i<j}w_i. The open slope-support endpoints of the finite mechanical-word factor are

\[
\alpha=\max\left(0,\max_{0\le i<j\le m}\frac{s_j-s_i-1}{j-i}\right),\quad
\beta=\min\left(1,\min_{0\le i<j\le m}\frac{s_j-s_i+1}{j-i}\right).
\]

The factor is admissible exactly when alpha<beta. Endpoints are reduced, with 0=0/1 and 1=1/1.

**Theorem R154.** For every m>=3, an admissible factor has equal reduced support-endpoint denominators **if and only if** m is even and w=(01)^(m/2) or w=(10)^(m/2). For m=2H>=4 these two words have

\[
\boxed{\alpha=(H-1)/(2H-1),\quad\beta=H/(2H-1).}
\]

The only boundary-length exceptions are the two one-letter words (m=1) and the two alternating two-letter words (m=2), which have support (0,1), denominators (1,1).

## Proof: same-denominator witnesses force alternation

First consider interior endpoints 0<alpha=a/b<beta=c/b<1, with fractions reduced, so b>=3 and 0<a<c<b.

Because a/b is the maximum of finitely many lower-factor bounds, some length tb factor has ta+1 ones. Partition that factor into t consecutive length-b blocks. At least one block has >=a+1 ones, and none can exceed a+1, since such a block would force a lower endpoint >a/b. Thus a length-b factor with exactly a+1 ones exists. Analogously the upper endpoint c/b is witnessed at length ub by a factor with uc-1 ones; partitioning gives a length-b factor with exactly c-1 ones. Every length-b factor with r ones satisfies

\[
c-1\le r\le a+1.
\tag{1}
\]

Consequently c-a is 1 or 2.

Every length-b factor with a+1 ones must begin and end with 1. Otherwise deleting an endpoint 0 yields a length-(b-1) factor with a+1 ones, whose lower-bound contribution a/(b-1)>a/b contradicts maximality. Every length-b factor with c-1 ones must begin and end with 0. Otherwise deleting an endpoint 1 gives a length-(b-1) factor with c-2 ones, whose upper-bound contribution (c-1)/(b-1)<c/b contradicts minimality. If c-a=2, one block would simultaneously satisfy both endpoint rules, impossible. Hence

\[
\boxed{c=a+1.}\tag{2}
\]

Every length-b factor now has either a or a+1 ones, and both types occur. The endpoint rules apply to each such factor. Writing r_i for the number of ones in the block starting at i, we obtain

\[
\boxed{w_i=w_{i+b-1}=r_i-a.}\tag{3}
\]

Thus every length-(b-1) factor, being a prefix or suffix of some length-b factor, contains exactly a ones; (3) also gives w_i=w_{i+b-1}, so w has period p=b-1 wherever indices overlap.

The witnessed b-blocks starting in 0 and 1 each have a length-p prefix with a ones. Deleting the first bit from these respective prefixes yields two length-(p-1) factors with a and a-1 ones. They impose

\[
(a-1)/(p-1)\le a/(p+1),\qquad (a+1)/(p+1)\le a/(p-1),
\]

hence

\[
\boxed{p-1\le2a\le p+1.}\tag{4}
\]

If p is odd, b=p+1 is even and (4) gives a=(p-1)/2 or (p+1)/2. In the first case c=a+1=b/2, in the second a=b/2, contradicting the reduced denominator b. Thus p=2h is even and (4) forces a=h, c=h+1, b=2h+1. It follows that

\[
\alpha=h/(2h+1)<1/2< (h+1)/(2h+1)=\beta.
\]

An occurrence of 11 would give alpha>=1/2, while an occurrence of 00 would give beta<=1/2. Therefore w has neither 11 nor 00: it is alternating.

For even m=2H>=4, any even-length 2t factor of an alternating word has exactly t ones. Every odd length 2t+1<=m-1 has factors with t and t+1 ones. The maximal lower odd-factor bound t/(2t+1) increases with t, and the minimal upper odd-factor bound (t+1)/(2t+1) decreases with t. Both extrema occur at odd length m-1, and dominate the even-factor bounds. Hence alpha=(H-1)/(2H-1), beta=H/(2H-1), both reduced.

For odd m=2H+1>=3, only one phase occurs at full length m and both phases occur at length m-2. The endpoints are, respectively,

\[
\begin{array}{c|cc}
w&\alpha&\beta\\
\hline
0(10)^H &(H-1)/(2H-1)&(H+1)/(2H+1)\\
1(01)^H &H/(2H+1)&H/(2H-1)
\end{array}
\]

All listed fractions are reduced (including 0/1 and 1/1 for H=1), so denominators 2H-1 and 2H+1 are distinct.

Finally, if an endpoint equals 0 or 1, both reduced denominators could be 1 only for support (0,1). For m>=3 the full-length factor of s_m ones would require s_m<=1 from alpha=0 and s_m>=m-1 from beta=1. At m=3 these imply s_m=1 and s_m=2 simultaneously; at larger m the contradiction is immediate. Direct inspection at m=1,2 yields the stated exceptional cases. QED.

## Exact implications and research frontier

For even m=2H>=4, R153.3 supplies the exact all-coefficient count alias

\[
C_{(01)^H}(K)=C_{(10)^H}(K)=\left\lceil\frac{K-1}{2H-1}\right\rceil,\quad K\ge2.
\]

**These two are the entire equal-denominator population of actual length-m Sturmian factors.** They are present from K=2 onward, so neither can be the last-missing factor in the R152B first-period certificate. Every other actual factor of length m>=3 has unequal endpoint denominators, where R153.1 proves injectivity of the *fixed-endpoint unrestricted-cut increment waveform*. Preserve absolute intercept cuts and pattern identity for any richer observer; no equivalence across different endpoint pairs is asserted.

## Exact regression

Companion \`R154_check.py\` uses integer cross-products and gcd only, enumerates all binary words of lengths 1..16 (131,070 candidates), and obtains 2,404 admissible factors, 18 with equal endpoint denominators: 2 each at m=1,2,4,6,8,10,12,14,16, none at odd lengths >=3. Verification marker: \`R154_EXACT_ALL_LENGTH_CLASSIFICATION_FINITE_CHECK_PASS\`. See \`R154_verification.json\` for per-length data. The universal statement follows from the proof, not the finite limit.

Next question: for the distinct-denominator factors, combine R153.1 with R152B's first-period absence certificate to prove or disprove the proposed saturation formula T(m)=(m-2) floor((m-1)/2)+1 for all m>=5. The mathematical review remains NOT_REVIEWED. P000 and the frozen scientific pin are unchanged.
