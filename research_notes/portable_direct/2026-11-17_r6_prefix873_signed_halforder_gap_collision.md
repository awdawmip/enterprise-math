# PREFIX-873 — Signed half-order collision theorem for near-cofactor two-port BRC observers

Date: 2026-11-17. Researcher mode: independent portable TASK-related auxiliary science, no shared X6 claim. Predecessors: PREFIX-871/872; frozen scientific source pin f42f2906d77f24085c123f3ccfe9667d41caa96d unchanged.
Status: AUTHOR_PROVED / EXACT_INTEGER_WITNESS_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Object and problem

For p named binary sources let N=2^p and u in [0,N) encode the full binary source vector. Legal ordered transitions are (u,u) and (u,u xor 2^i), 0<=i<p. The observer uses fixed odd moduli (q1,q2) and observes (u mod q1, v mod q2). Lossless complete-transition recovery requires this map to be injective over all legal ordered transitions. The goal is to exclude whole families of modulus pairs with explicit provenance-preserving collisions, improving on the 46 individually checked extremal pairs in PREFIX-872.

This is a finite auxiliary BRC named-source observer, not a native X6 Cell/Link/Port dynamical identification. In particular the two endpoints, source bit and change direction remain typed.

## Theorem 873.A — Signed half-order near-gap obstruction (all p)

Let p>=3, N=2^p, g be a positive odd integer and qH,qL be odd integers with qL>=3 and

  qH-qL=2g.

Suppose integers m>=1 and sigma in {-1,+1} satisfy

  g divides 2^m + sigma,

and define k=(2^m+sigma)/g. Assume

  m+1 < p,              k*qH+3 < N.

Then the complete-transition observer with (q1,q2)=(qH,qL) is NOT injective. The reversed ordered modulus pair (qL,qH) is also NOT injective.

### Exact constructive proof

Set i=m+1 and j=1. As r runs over {0,1,2,3}, bit j of k*qH+r takes both possible binary values. Select r so bit j is 1 if sigma=+1 and 0 if sigma=-1. Since i>=2 and r<=3, bit i of r is 0. Form

  T0=(r, r+2^i);
  T1=(r+k*qH, (r+k*qH) xor 2).

Both are legal single-name flips; the hypotheses ensure all four endpoints lie in [0,N). The second flip is a signed increment -sigma*2 because of the chosen bit j. Consequently its endpoint v1 and the endpoint v0 of T0 satisfy

  v1-v0 = k*qH - sigma*2 - 2^(m+1)
        = k*qH - 2*(2^m+sigma)
        = k*(qH-2g)
        = k*qL.

Their old endpoints differ by k*qH. Therefore T0 and T1, although distinct, have identical observations modulo (qH,qL). Their source labels and predecessor states differ, so this is a collision of complete-transition recovery, not an approximation or an unsigned cancellation. The legal-transition relation is symmetric under time reversal; exchanging old/new endpoints and the port order yields a collision for (qL,qH). QED.

A shortest signed half-order h(g)=min{m>=1:2^m is congruent to +1 or -1 mod g} always exists for odd g (take h(1)=1), by periodicity of 2 modulo g. The theorem turns it into a failure certificate whenever the associated k fits inside the state range. For consecutive odd cofactors qH=gA and qL=g(A-2), this gives a near-necessity counterpart to the earlier sufficient separation condition h(g)>=p: if h(g)<=p-2 and the range inequality holds, such a balanced pair is impossible.

## Corollary 873.B — A complete analytical 19-bit gap-family exclusion for p=32

Take p=32, Q=2^19-1=524287. For each odd half-gap g in

  G={1,3,5,7,9,11,13,15,19,21,23,25,27,29,35,37,39,47,49,53,55,59,61},

select its shortest signed half-order m and corresponding sigma,k. Define

  MH(g) = largest odd integer <= min(Q, floor((2^32-4)/k)).

For every odd qH in [2g+3, MH(g)], the pairs (qH,qH-2g) and (qH-2g,qH) are invalid 19-bit full-transition observers. There are exactly

  C(g)=max(0,(MH(g)-(2g+3))/2+1)

unordered excluded pairs for this half-gap. Distinct g give disjoint families since qH-qL=2g is unique.

The attached exact certificate computes SUM_g C(g)=4,632,684 unordered pairs, or 9,265,368 ordered pairs. For all 17 half-gaps g<=39 in the displayed set, MH(g)=Q: the theorem excludes the ENTIRE 19-bit positive-odd near-gap family. The remaining six g=47,49,53,55,59,61 have smaller certified qH ceilings; all 23 families have nonempty certified intervals.

Important typing: g in this corollary is HALF THE MODULUS GAP, not necessarily gcd(q1,q2). The set G was chosen for comparability with the earlier PREFIX-871 gcd candidate values. This result excludes exact modulus pairs, not whole gcd classes, and does not resolve B_fix,odd(32) in {19,20}.

### Concrete high-range witness

For g=37, m=18, sigma=+1, k=7085, qH=524253 and qL=524179, the proof supplies

  T0=(1,524289),
  T1=(3714332506,3714332504).

Both transitions flip exactly one source; their observations coincide modulo (524253,524179). This independently provides a short algebraic certificate for an earlier large-fiber collision.

## Exact verification

The companion checker PREFIX873_R6_HALFORDER_CHECK.py implements the theorem's explicit two transitions, verifies old/new endpoints, named one-bit flip legality, observation equality, and the equality v1-v0=k*qL. It checks all 23 maximal-gapped candidates corresponding to PREFIX-872's extremal family, all 23 g-dependent cap endpoints in the new theorem, and a complete bounded collection of 35,134 small parameter witness instances for p in 6..12 and odd g<=31 under the theorem hypotheses. All tests use Python exact integers and assertions, no floating-point tolerance. The companion JSON records the complete 23 interval counts, cap-endpoint certificates, and check counts.

The universal theorem is an algebraic proof; the 9,265,368 excluded ordered pairs are counted analytically, rather than individually enumerated. The finite checker is an author-side regression test and does not constitute independent mathematical review.

## Prior verified sources and continuation

- PREFIX-871: https://github.com/awdawmip/enterprise-math/blob/a580bb6310cb307f4513f8fbb11c975ca5c2a4fe/research_notes/portable_direct/2026-11-17_r6_prefix871_even_p64_to_80_and_gcd_fiber_capacity.md
- PREFIX-872: https://github.com/awdawmip/enterprise-math/blob/273531bff0c408b58ede126ee8c7c14d2216dea9/research_notes/portable_direct/2026-11-17_r6_prefix872_first_port_fiber_capacity_p32_extremal_collisions.md
- Current P000 V5, ACTIVE residual-fidelity worldview and portable protocol are scientific context, not altered by this auxiliary proof.

Next: combine the binary-gap spectrum with a short k*q1-l*q2 collision sieve for the 19-bit p=32 candidate space; quantify exact exclusion coverage without double-counting; look for a congruence-class or finite CRT criterion that eliminates all surviving pairs or exhibits a valid 19-bit construction. Keep the p=62 coprime case as an independent frontier. No shared X6 CLAIM/Result/Review is asserted.
