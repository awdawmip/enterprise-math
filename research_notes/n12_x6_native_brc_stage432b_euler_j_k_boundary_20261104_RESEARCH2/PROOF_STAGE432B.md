# Stage432-B — Exact unequal-length Euler/J/K/T transfer and class-label cost

2026-11-04. Research2. AUTHOR_SIDE_PROOF / EXACT_BIGINT_EXECUTED / UNREVIEWED / NOT_ADMITTED. Frozen scientific inputs: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Parent Stage431-B bf87b38aa1d6978a361910d92793c9af9837fc0f and Stage424-B b35d849007058e064d3dfdd1f19655295df30461. Source-labeled static native signed-X6 model; no claim about final cell addresses or time.

## Model

D={+E1,-E1,...,+E6,-E6}, twelve typed directions. Let P in D^m and Q in D^n, with p>=0, r>=1, n>=p+1 and m>=n+r. For a word w, endpoint x(w) is the signed six-vector sum, and J_w(a,b) counts the ordered adjacent occurrences of typed edge a->b. K(P,Q) is the number of equal letters in the first n absolute positions. Fix m,n, both endpoints, both complete directed 12x12 J histograms, and current K=k. Group all original ordered word pairs by

T_(p,r)=(Q_(n-p),...,Q_n ; P_(n-p+1),...,P_(n+r)).

The Stage431-B theorem (author-side and pending independent review) identifies these attainable T values with future-equivalence classes under P frozen and at most p independent Q-POP and r arbitrary Q-APPEND operations, all legal interleavings and intermediate complete observations.

## Lemma 432.1: first direction is an exact endpoint/J residual

For each nonempty typed word w=(w1,...,wL),

x(w) - SUM_(a,b in D²) J_w(a,b) vec(b) = vec(w1).

Every symbol after the first appears exactly once as a directed edge destination, proving the identity. The twelve native signed-axis direction vectors are distinct. Thus the residual uniquely recovers the first symbol whenever the full (endpoint,J) fiber is nonempty; an invalid residual implies an empty fiber. This eliminates an otherwise tempting cyclic-Euler multiplicity.

## Theorem 432.2: exact all-fiber directed-Euler/J/K/T count

The program REPRO_STAGE432B.js computes for every possible T value t the exact integer

F(t) = #{(P,Q): endpoint(P)=xP, endpoint(Q)=xQ, J(P)=JP, J(Q)=JQ, K(P,Q)=k, T_(p,r)(P,Q)=t}.

Algorithm: recover both initial symbols via Lemma 432.1. Recursively consume one outgoing typed edge in P and Q at every common absolute position 2..n; update K by testing equality of the two chosen destination symbols and record the boundary symbols when their absolute indices enter the T window. After Q ends, consume P alone until length m while retaining its window. Memoize the remaining multiplicities of each directed edge type, both last symbols, partial K and partial T strings. A terminal state contributes one exactly when both edge-count vectors vanish and K equals the target.

Proof: each original word with a fixed first symbol and directed J corresponds to precisely one sequence of typed outgoing edge choices. Two copies of an identical directed-edge TYPE do not create two distinguishable words and therefore have weight one, rather than an additional multiplicity factor. Conversely a full legal choice sequence reconstructs one word with the prescribed J, and Lemma 432.1 guarantees its endpoint. The joint recursion has exactly one interleaving for the first n positions and then one P-only continuation. Its K increments equal the exact absolute-position matches and its window capture equals T. The partition of continuations by their next typed edge is disjoint and exhaustive; induction on the number of remaining edges proves every path pair counted once. All additions use exact nonnegative BigInt. This statement is independent of any unreviewed future-equivalence theorem.

BRC interpretation: retain the positive integer mass of each labeled future-observer class. Summing over T yields the coarser current-observer count and can erase distinctions relevant to future APPEND/POP. No phase/amplitude or physical cancellation claim is made.

## Corollary 432.3: exact fixed-length class-label width in a fiber

Under the Stage431-B future-equivalence theorem and a fixed complete current-observer fiber, let q be the number of T with F(t)>0. The minimum number of bits for an injective fixed-length per-history class label equals ceil(log2(q)) (zero for q=1). Proof: the q distinguishable future classes require 2^b>=q, and any numbering of the q classes achieves that many bits. Building, saving and decoding the codebook costs additional space and computation, as does reconstructing any full original history.

## Exact small witness

Let A=+E1, B=-E1, C=+E2. m=7,n=5,p=1,r=2. Fix JP=J(AABACAA), JQ=J(AABAA), endpoints given by these two words and K=4. The complete fiber has exactly seven ordered pairs divided into five distinct T classes:

| Q_(4..5);P_(5..7) | exact number |
| --- | ---: |
| AA;AAA | 1 |
| AA;ABA | 2 |
| AA;CAA | 2 |
| BA;AAA | 1 |
| BA;ABA | 1 |

Thus its minimal fixed-length future class label requires three bits under the Stage431 hypothesis. A cheap current-(endpoint,J,K)-only collapse fails already with P=AABACAA, P'=AACAABA and the same Q=AABAA: both have identical endpoint, full directed JP, Q and K=4; after legal APPEND_Q(A), the matching counts are respectively 5 and 4. The witness distinguishes residual histories through an actual future, not merely by syntactic T inequality.

## End-to-end cost statement

Let eP,eQ be the numbers of nonzero typed directed edge entries and w(L)=max(1,ceil(log2(L+1))). One explicit sparse input codec uses exactly

B_in=16 + eP*(8+w(m)) + eQ*(8+w(n)) + 6*(1+w(m)) + 6*(1+w(n)) + 2*w(m) + 3*w(n)

bits: each type comprises two 4-bit native direction IDs and a fixed-width count; each six-vector component stores sign and magnitude; plus edge record counts, lengths and p,r,k fields. This is an explicit representation length, not an optimal binary codec. Preprocessing endpoint/J validity and initial residual are O(eP+eQ+6).

A coarse state bound for the memo recursion is

S <= PRODUCT_(e in JP)(JP[e]+1) * PRODUCT_(e in JQ)(JQ[e]+1) * 12^2 * (n+1) * 12^(2p+r+1).

The captured future window has 2p+r+1 native symbols and at most G=12^(2p+r+1) possible keys. At each state at most eP*eQ pairs of outgoing types (or eP after Q ends) are examined; a straightforward memo-map implementation has coarse bit-cost envelope O(S*(eP*eQ+eP)*G*(m+n)), with BigInt coefficient bit length bounded by ceil((m+n)*log2(12))+1. The explicit output codec uses q*(4*(2p+r+1)+w(N))+w(q) bits when N counts original path pairs; in an arbitrary input, replace w(N) by a safe O(m+n) bound. Codebook construction, output recovery and verification remain separate costs. General runtime can still be exponential in edge support and future-window size; Stage424's affine finite observations are not promoted to a general bound.

## Actual finite test and scope

Node.js v22.16.0 executed REPRO_STAGE432B.js. Independent brute-force full-word enumeration and this DP agreed on all T-count maps for 66 fibers (12 templates, all K=0..n): 844 original path-pair combinations across repeated K checks, 1331 DP memo states, 1320 transfers, 800 BigInt additions, 113 nonempty grouped terminal outputs. Maximum observed coefficient is 3 bits; largest declared input was 167 bits and largest test output 537 bits. The program asserts the same-Q different-P APPEND(A) regression. Output marker: STAGE432B_UNEQUAL_EULER_J_K_T_TRANSFER_PASS. Exact general count follows from Theorem 432.2, while the finite tests check code independently.

All files are author-side research artifacts. Formal Source CLAIM/Result and independent Driver review remain separate from publication.

## Next

Stage433-B: compute fibers across adjacent (p,r) budgets to exhibit exact strict class splits, with explicit POP/APPEND future trace witnesses. Determine instance-sensitive minimal label width and price original-word-to-class encoding and codebook construction, not only the DP state count. Preserve the frozen pins and P000.
