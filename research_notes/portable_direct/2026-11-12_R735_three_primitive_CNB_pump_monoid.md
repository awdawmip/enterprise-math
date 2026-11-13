# R735 — Free three-generator BRC return monoids and exponential hidden histories in a fixed PASS ledger

2026-11-12 · exact author-side mathematics · independent review pending.
Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5, unchanged). Derived positive 15-arc/V17 rooted-CNB carriers A = 211733226574; B = 5363347296468. Predecessor R734: commit 368f50c86c77451822d6e6b649535d297abcff25. This is a positive BRC combinatorial history/observer result; any P000 Cell/force realization is a separate next scientific question.

## Model, branch semantics, observers

Vertices are the ten sorted triples of 01234. The complete directed arc universe has 60 pairs (u,v) replacing exactly one label, ordered lexicographically. Each specified mask selects 15 arcs. Root = 012. A length-m history is a rooted closed directed walk with no immediate backtracking, including at the cyclic seam: S_(j-1) != S_(j+1). Branches are ordered paths with unit positive multiplicity. V17 slot transport moves the vacated slot ID to the entering label, yielding named S3 holonomy h(w). The complete directed arc-count observer is N(w) in N^15; the four-port pooled two-PASS observer is Y=C N in N^12 where C[r,i] = [r=floor(i/12)] + [r=i mod 12]. Repeated indices contribute twice when applicable. Allowed future operation here is rooted concatenation of these explicitly legal returns.

## Theorem 1: the three primitive returns form a free monoid

The incoming/outgoing root neighborhoods are disjoint. For A: incoming {013,123}, outgoing {014,023,024}. For B: incoming {013,014,124}, outgoing {023,123}.

Exactly three length-3 rooted cyclic-nonbacktracking returns are present in each carrier:

| Carrier | Generator 0; h | Generator 1; h | Generator 2; h |
|---|---|---|---|
| A | 012>014>013>012; 012 | 012>023>013>012; 021 | 012>023>123>012; 102 |
| B | 012>023>013>012; 021 | 012>123>013>012; 210 | 012>123>124>012; 012 |

The root neighbor separation makes the seam between *any* two rooted returns legal. Each length-3 generator block is distinguishable, and a concatenated length-3k word can be parsed at times 0,3,...,3k. Consequently this is a free monoid on three generators, with exactly 3^k distinct ordered histories at length 3k in its subcarrier. Its holonomy image contains the identity and two distinct transpositions, which generate S3.

## Theorem 2: exact three-holonomy census of count fibers

Relabel the three generators I,P,Q according to holonomies id,p,q, where p and q are two distinct transpositions. A word with generator counts (c,a,b) always has one fixed full directed count N and pooled PASS ledger Y regardless of order. The generator-count to N map is injective because each generator has an arc absent from both other generators.

Independently, the three columns of pooled 12-counter ledger increments have a nonzero 3x3 minor. For A, rows 0,1,3 give the matrix [[4,3,2],[0,1,3],[1,1,0]] with determinant -5. For B, rows 0,1,2 give [[4,3,1],[0,1,4],[1,1,1]] with determinant -1. Thus the three generator multiplicities are uniquely recoverable from Y as well, without using the ambient R733 rank result.

**Exact fiber classification:** For a,b>=2, the fiber contains exactly three different terminal S3 holonomies. If a=0 or b=0 it contains one; if a,b>0 with min(a,b)=1, it contains exactly two. Every fixed-count fiber has a common parity.

Proof: I letters are inert for holonomy. The same four-letter multiset P,P,Q,Q admits products PPQQ=id, PQPQ=(pq)^2 and QPQP=(qp)^2, giving the three different even elements of S3. Prepend the same remaining letters to all three orders, preserving distinctness. If exactly one P occurs, an arbitrary arrangement reduces (after ignoring I) to Q^u P Q^(b-u), determined by the parity of u and hence with exactly two possible outputs when b>=1. The symmetric case is identical. A single transposition type gives one output. Parity bounds any fiber at three.

For k total generators, the number of distinct full N fibers—and independently distinct pooled Y fibers—having all three holonomies is therefore

F(k) = 0 (k<=3), and F(k) = binomial(k-2,2) (k>=4),

by counting c>=0,a>=2,b>=2 with a+b+c=k. The first triple fiber of this three-step *submonoid* occurs at history length 12. R734's sharp history length 9 for the entire carrier is a separate, stronger ambient result: its early count-fiber collision necessarily uses a longer indecomposable root excursion.

## Theorem 3: exponentially many histories hide in one exact ledger

For any integer r>=1 take exactly 2r copies of P and 2r copies of Q. Every ordering has the same entire 15-counter N, the same pooled 12-counter Y and the same history length m=12r. Unique block parsing makes all binomial(4r,2r) orderings different positive BRC histories. Three terminal even holonomies all occur by using the P,P,Q,Q permutations above and a common prefix of the remaining letters.

Since the central binomial coefficient is maximal among the 4r+1 coefficients of (1+z)^(4r),

binomial(4r,2r) >= 2^(4r)/(4r+1) = 2^(m/3)/(m/3+1).

Thus any exact **history reconstruction** from either N or Y has a worst-fiber unresolved order information of at least log2 binomial(4r,2r) >= m/3 - log2(m/3+1) bits at the lengths m=12r. The terminal *named holonomy* has exactly three possibilities in the same fibers; history retention and final-relation retention have distinct minimal information budgets.

## Exact computation and reproducibility

The companion stdlib Python verifier enumerates the complete 60 arc universe from the frozen two masks, the three rooted length-3 generators, all 3^k generator words for k=1..8, their exact V17 frames, all cyclic seams and N/Y counts. It checks private arc supports, the integer nonzero pooled ledger minors, and exact classification of every observed fiber. It separately enumerates every fixed-count word with 2r copies of each transposition generator for r=1..4. These are finite checks; the all-length conclusions are the combinatorial proofs above.

| k | Length | Ordered words | Different N/Y fibers | Three-holonomy fibers |
|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 |
| 2 | 6 | 9 | 6 | 0 |
| 3 | 9 | 27 | 10 | 0 |
| 4 | 12 | 81 | 15 | 1 |
| 5 | 15 | 243 | 21 | 3 |
| 6 | 18 | 729 | 28 | 6 |
| 7 | 21 | 2187 | 36 | 10 |
| 8 | 24 | 6561 | 45 | 15 |

For r=1,2,3,4 the single fixed-ledger fiber has respectively 6,70,924,12870 histories, with relation counts (012,120,201) = (4,1,1), (36,17,17), (402,261,261), (5028,3921,3921) on both carriers. The companion reproducible program and JSON supply independently checkable inputs, result data and exact witnesses.

## Scientific continuation

Take the source-preserving three-step returns as explicit branch inputs for a P000-compliant native event interface. The next task is to specify three nonzero signed primitive action quanta, their common Cell attachment and the actual TRIADIC_CLOSURE_E incidence; then test whether two ordered root excursions compose under a single admissible event-time/port scheduler. Maintain distinct observers for abstract V17 holonomy, V29 PASS counts, native Cell identity and primitive force closure. This gives a concrete falsifier of any proposed count-only scheduler that purports to reproduce arbitrary ordered histories.

Status: mathematically proved inside the declared positive CNB/V17 carrier by finite setup plus all-length combinatorial argument, with independent review and native realization pending. GitHub author-side persistence is separate from official Task CLAIM/Result and Foundation admission.
