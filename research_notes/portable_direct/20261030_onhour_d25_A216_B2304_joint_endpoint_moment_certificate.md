# D25 / SECOND-DIGIT-LIFT — joint A216/B2304 endpoint and cubic-moment certificate

2026-10-30 Asia/Hong_Kong. Research lane: chatgpt-research-onhour-enterprise-math-20260923, not the maintenance lane. AUTHOR-SIDE / PROVED ELEMENTARY IDENTITIES / EXACT FINITE CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains untouched.

## Attribution and scope

The A216 cubic-moment identity and its -2p³ endpoint were already established in research_notes/portable_direct/20261030_onhour_d25_A216_fourth_digit_moment_endpoint.md (commit 5d0f3204ef441d3bc51390c0d12f2654640d9206): reused, NOT newly claimed. Guo–Zudilin proved the original B2304 weighted sum mod p³ (Adv. Math. 346 (2019), 329–358, arXiv:1803.01830), not re-proved here. New in this research unit: the B2304 exact cubic-moment endpoint, a shared A/B endpoint normalization lemma, and their p⁴ homogeneous coupled consequence. None proves the original D25 bridge.

## Elementary factorial lemma and sources

For p prime and 2 ≤ r < p,

\[
v_p((r(p-1))!)=r-1,\qquad
\boxed{(r(p-1))!/p^{r-1}\equiv-1\pmod p.}\tag{L}
\]

Proof: after removing multiples p, the factorial consists of r-1 complete blocks of nonzero residues and a final block of p-r factors. The normalized residue is
\[
(r-1)!((p-1)!)^{r-1}(p-r)!\pmod p.
\]
Wilson's identity gives (p-r)!(-1)^{r-1}(r-1)!=-1, so the displayed residue is -1. The valuation follows because exactly r-1 multiples of p occur and r<p.

For every prime p≥5 let, in the p-local rationals,
\[
a_n={\binom{2n}{n}^{2}\binom{3n}{n}\over216^n}
={(2n)!(3n)!\over(n!)^5\,216^n},\quad
b_n={\binom{2n}{n}^{2}\binom{4n}{2n}\over2304^n}
={(4n)!\over(n!)^4\,2304^n}.
\]
Both 216 and 2304 are p-units. Apply (L) for r=2,3,4, Wilson for (p-1)! and Fermat for both denominator bases:
\[
\boxed{v_p(a_{p-1})=v_p(b_{p-1})=3,\quad
a_{p-1}/p^3\equiv b_{p-1}/p^3\equiv-1\pmod p.}\tag{E}
\]
In particular, the **two last-index source ports** obey a_{p-1}-b_{p-1}≡0 mod p⁴. This is NOT a termwise identity for other indices, a total-sum theorem or a native CM identification.

## Two finite telescopers, exact in Q

Write A_j(N)=sum_{n=0}^N n^j a_n and B_j(N)=sum_{n=0}^N n^j b_n, j=0,1,2,3. Ratios:
\[
36(n+1)^3a_{n+1}=(2n+1)(3n+1)(3n+2)a_n,
\]
\[
576(n+1)^3b_{n+1}=(4n+1)(4n+2)(4n+3)b_n.
\]
Shift and sum each recurrence. For every N≥0, INCLUDING the n=0 coefficient,
\[
\boxed{18A_3(N)-27A_2(N)-13A_1(N)-2A_0(N)
=-(2N+1)(3N+1)(3N+2)a_N,}\tag{A}
\]
\[
\boxed{512B_3(N)-96B_2(N)-44B_1(N)-6B_0(N)
=-(4N+1)(4N+2)(4N+3)b_N.}\tag{B}
\]
(A) is the previously published identity; (B) is the second-source result. Put N=p-1 and use (E). The terminal polynomial factors are -2 and -6 modulo p, respectively. Thus
\[
I_A:=18A_3-27A_2-13A_1-2A_0\equiv-2p^3\pmod{p^4},
\]
\[
I_B:=512B_3-96B_2-44B_1-6B_0\equiv-6p^3\pmod{p^4},
\]
and the **new coupled zero-boundary consequence**
\[
\boxed{3I_A-I_B\equiv0\pmod{p^4}}\tag{AB4}
\]
or explicitly
\[
54A_3-81A_2-39A_1-6A_0-512B_3+96B_2+44B_1+6B_0\equiv0\pmod{p^4}.
\]
This is cancellation of two source-labeled terminal defects, not of the internal coefficient streams.

## Executed arithmetic and limitations

Executed Python standard-library checker:
research_notes/portable_direct/d25_A216_B2304_joint_endpoint_guard_20261030.py. Exact Fraction telescopers for N=0,...,8; small exact factorial checks for (L); all 237 primes 5≤p<1500, 60 of them in frozen p≡13,19 (mod24), with arithmetic mod p⁴; independent original integer-binomial endpoints for p=5,7,13,19,373. All checked cases PASS. For p=13 the normalized tuple (I_A/p³,I_B/p³,a_last/p³,b_last/p³) is (11,7,12,12) mod13; for p=19 it is (17,13,18,18); for p=373 it is (371,367,372,372). This is exact *finite evidence*, not an all-prime computational proof; the above argument establishes all-prime identities.

BRC/Enterprise-coordinates resolution: COMPOSE_APPLIED to the signed p-local carrier (model source, original index, factorial block, valuation, unit residue, moment weight). Joint arithmetic coordinates are observer labels, not newly asserted P000 spatial axes. Combining signed endpoint defects at precision p⁴ is permitted; positive-mass BRC, total-only projections or H0/B0 substitution are not. Internal index/source information remains necessary for further Green/Hesse/Frobenius operations.

## Remaining hard target and recovery

The actual frozen target is still
\[
D_p=\sum_{n=0}^{p-1}(6n+1)a_n
-2\sum_{n=0}^{p-1}(8n+1)b_n
+p\left({-3\over p}\right)\equiv0\pmod{p^3},
\quad p\equiv13,19\pmod{24}.
\]
AB4 is an independently checkable necessary compatibility for a future *coupled* p-adic WZ transformation; not a proof of D_p≡0. The fixed p=373 original-class native H0/B0 divided-power Frobenius, rank, odd Green/Hesse and κ benchmark (#1559) is still NOT_RUN / PENDING_OWNER. Neither the scalar proof nor its tests satisfy this native gate.

Source recovery remains pending. The Site returns no Researcher write authority and own checkpoint list ACCESS_DENIED; do not invent a new session, claim, run or formal Source checkpoint. Preserve original request IDs where known; do not use the maintenance conversation_id, do not move the frozen source pin, do not alter schedule or notifications.