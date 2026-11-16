# EC49FQX — Three exact BRC price slices and a 43-node global enclosure

Date: 2026-11-17 (Asia/Shanghai). Evidence status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Fixed scientific scope and provenance

Frozen scientific pin: awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Predecessor: EC49FQW, PR #2580 (40 price nodes). Original master SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e. Original profile CSV SHA256: a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f.

Static native typed BRC experiment, class 16943: 310 original configurations, 141 complete distinguishable named-root profiles, 228 physically labeled queries (144 terminal, 84 named-root, 209 response partitions). A legal finite adaptive decision tree must identify the *full* profile, preserving its named-root semantics and frozen original branch provenance. No new physical dynamics are asserted; P000/Heartbeat X6 ontology remains unchanged.

For terminal price t>0 and root price r=xt, x>=1, the exact prior is p_lambda(i)=(1-lambda)/141+lambda*m_i/310, 0<=lambda<=1, where m_i are the 310 original configuration multiplicities. V(lambda,x) is the unrestricted minimum expected cost divided by t.

Three previously constructed and physically replayed complete BRC decision-tree families have costs:
A=(1-lambda)*(6x+290)/141+lambda*(6x+751)/310 (first queries 32,34);
B=(1-lambda)*(5x+293)/141+lambda*(5x+704)/310 (first 140,142);
C=(1-lambda)*(5x+295)/141+lambda*(5x+685)/310 (first 16,23).
Let K(x)=7557-169x, gamma(x)=310(3-x)/K(x) on 1<=x<=3, and beta=620/3299.

## Theorem 1 — all-real-prior optimality at three new prices

For x in {79/32,93/32,95/32}, and *every real* lambda in [0,1],
V(lambda,x)=min(A(lambda,x),B(lambda,x),C(lambda,x)).

| x | gamma(x) | beta |
| --- | --- | --- |
| 79/32 | 5270/228473 | 620/3299 |
| 93/32 | 310/75369 | 620/3299 |
| 95/32 | 310/225769 | 620/3299 |

**Complete physically labeled optimal first-query sets**: {32,34} for 0<=lambda<gamma; {32,34,140,142} at gamma; {140,142} for gamma<lambda<beta; {16,23,140,142} at beta; {16,23} for beta<lambda<=1.

Proof: For each price, exact unrestricted integer subset-Bellman optimization was performed at four prior anchors: 0, gamma(x), beta, 1. The 12 full native certificates and a structurally separate exact weighted-subset Bellman verifier agree on the integer optimal objective and the *entire physically labeled* first-query minimizer set among all 228 queries. At these anchors the optima equal respectively A, A=B, B=C, and C. All tied-first trees were replayed on 141 complete named-root profiles with the original weights summing to 310. The recursive Bellman domain is finite: every nontrivial observation strictly partitions the current profile subset, and each has positive cost. It enumerates all finite adaptive trees without imposing a depth cutoff.

For fixed x, the cost of any one legal tree is affine in lambda; the infimum V is therefore concave in lambda, and each feasible A/B/C branch is an affine upper bound. Equality at both endpoints forces equality throughout [0,gamma], [gamma,beta], and [beta,1]. For each fixed physically labeled initial query, its constrained optimal cost is also concave, so its gap above the affine optimal branch is nonnegative and is strictly positive throughout an open interval whenever strictly positive at at least one endpoint. This proves the complete first-label classification, including all phase-boundary ties. QED.

## Theorem 2 — 43-node continuously certified region

Insert the three new prices into the 40 exact previous grid nodes in [1,3]. There are 43 distinct nodes and 42 adjacent intervals. A fixed tree's cost is bilinear in (lambda,x), as is its difference from one of A/B/C. Its nonnegativity at the four corners of any rectangle extends throughout by bilinear interpolation. At every adjacent interval [a,b], the endpoint Bellman slices imply A exact for 0<=lambda<=gamma(b), B exact for gamma(a)<=lambda<=beta and C exact for beta<=lambda<=1. Possible unproved portions lie inside the 42 strips gamma(b)<lambda<gamma(a).

The sum of the containing-strip areas, computed as exact rational arithmetic, is:
S_43 = sum_{[a,b]} (b-a)*(gamma(a)-gamma(b))
     = 56160233186339700335/13277756713266011935728.

Therefore at least:
1-S_43/2 = 26499353193345684171121/26555513426532023871456
         = 99.7885176148383968...%
of [1,3] x [0,1] has a globally optimal native BRC strategy certified. The predecessor 40-node bound was 99.7757682719307552...%.

## Theorem 3 — global strategy-regret guarantee

For all real lambda in [0,1], all x=r/t>=1 and t>0:
0 <= C_strategy-C_optimal
  <= [25/8 / (sqrt(57245/8)+sqrt(114321/16))^2] * t
   = 0.00010926049625923169947... t.

Proof: EC49FQW's chord-versus-optimal-concavity certificate bounds the strategy regret on every exact-price interval [a,b] by
M(a,b)=50*(b-a)/(sqrt(K(a))+sqrt(K(b)))^2 * t.
The inherited exact x>=3 theorem gives zero regret in the tail. Exact fractions and integer-square-root enclosures (scale 10^18) compare all 42 interval bounds. The unique largest bound occurs on [19/8,39/16]; its *certified lower bound* strictly exceeds each other interval's *certified upper bound*. This improves the predecessor upper certificate 0.0001107326670272307635... t by about 1.32948%. This constant is an upper guarantee, not an attained regret claim. QED.

## Recalculation and scope

12 native integer Bellman endpoint certificates: 3 prices x 4 prior anchors. All 12 were independently recalculated using a separate exact weighted-subset dynamic program and all optimal first-label native decision trees were exhaustively replayed. Input identity is protected by the frozen exact source hashes, and the 141-state/228-query/310-multiplicity scope was asserted. The 43-node geometry comparison uses exact rational arithmetic and certified rational enclosures for square roots. Project-independent mathematical review and formal Result admission are pending.

The full new witness JSONs, exact generator, independently executed verifier, 43-grid geometry program, local logs, frozen inputs, prior EC49FQW complete inherited archive, and SHA256 manifest are also bundled in the conversation artifact EC49FQX_THREE_SLICES_43GRID_COMPLETE_EVIDENCE_20261117.tar.xz (archive SHA256 0c46337029c4cc6cd598f8c763e3b38bf49ea00af91e63a405d95ea551e4ba7b). This repository text and the accompanying compact index constitute a portable mathematical source; GitHub blob/commit readback attests publication, not mathematical review.

## Next exact problem and control state

The largest remaining interval regret certificate is [19/8,39/16]. Prioritize a rational midpoint chosen in log K, or derive a parameterized Bellman lower bound that closes all 42 residual strips. A genuine counterexample to the candidate full two-dimensional phase curve is a legal, complete, physically labeled original-BRC adaptive decision tree with exact expected cost below min(A,B,C) at a specified interior (x,lambda).

The current native read-only RS-EC49AS control continuation request r4-ec49fqx-20261117-0033-continuation-read-01 returned FAILED / CANONICAL_REJECTED: unknown current immutable task publication. This scientific publication is an independent portable artifact, not a formal CLAIM, Result, Review, or Activity scientific checkpoint.