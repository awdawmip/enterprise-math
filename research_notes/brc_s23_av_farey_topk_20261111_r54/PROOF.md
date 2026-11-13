# R54 — Exact Farey-neighbor successor for the k rightmost labelled phase cuts

Status: author-side proved mathematical derivation and exact integer validation (2026-11-11). Scientific input remains pinned to Enterprise Math commit 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Predecessors: R51 PR #2014 (Floor Sum rank/select), R52 PR #2018 (exact cut incidence), R53 PR #2022 (indexed source-state sweep and semiconvergent-only obstruction).

## Question

Given an irrational 0 < theta < 1, a finite phase cut set {s theta}, 1 <= s <= K, and an output budget 1 <= k <= K, enumerate the k indices s with *smallest strictly positive upper phase errors*

    epsilon_s = ceil(s theta) - s theta = {-s theta}.

Do so in exact rank order, with each original index preserved and without sorting all K phases. The R53 witness theta = sqrt(2)-1, K=12, s=9 must be generated as the fourth answer.

This is an external irrational-rotation auxiliary model with a declared labelled-age observer, not an asserted native X6 dynamics realization. P000 and observer provenance remain unchanged.

## Theorem R54-A: Farey-neighbor successor permutation

Let a/i < theta < c/j be reduced Farey neighbors, with i,j positive, ci-aj=1, i<=K, j<=K and i+j>K. Let

    u = i theta - a > 0,       v = c - j theta > 0.

Then the first upper phase is the cut with index s_1=j. For every 1<=s<=K, define

    T(s) = s-i       if s>i;
         = s+j       if s+j<=K;
         = s+j-i     otherwise.

Starting at s_1=j and repeatedly applying T visits all K cut indices exactly once, in strictly increasing circular epsilon phase, and then returns to j. Consequently the first k iterates are exactly the k smallest positive epsilon values, in increasing order.

The circular distance epsilon_{T(s)}-epsilon_s (mod 1) is respectively u, v or u+v. With K>1 all are strictly between 0 and 1. At K=1 the one-point cyclic return has distance 1.

### Proof

Since ci-aj=1, the integer vectors (i,a) and (j,c) form a unimodular basis of Z^2. For any two distinct indices s,t in {1,...,K}, write d=t-s and the positive circular phase difference delta={-d theta} in (0,1). There is a unique integer h with delta=h-d theta. Thus

    (d,h) = alpha (i,a) + beta (j,c),    alpha,beta in Z,

and

    delta = -alpha u + beta v.

Both alpha and beta cannot be positive: otherwise d>=i+j>K, contrary to |d|<K. Both cannot be negative: otherwise d<=-i-j<-K. If alpha>0 and beta<=0 then delta<0, impossible. If alpha=0,beta<0 then delta<0. The only surviving possibility is alpha<=0,beta>=0, not both zero. Put h0=-alpha>=0 and b0=beta>=0. Every candidate forward circular displacement therefore has the **exact** form

    delta = h0*u + b0*v,     t = s - h0*i + b0*j,

with t in {1,...,K}.

If s>i, then s-i is feasible and gives delta=u; because i+j>K, s+j>K, so no candidate with h0=0,b0>=1 is feasible. Every other candidate has delta>=u. Thus T(s)=s-i is the immediate successor.

If s+j<=K, then s+j gives delta=v. This inequality and i+j>K imply s<=K-j<i, so no candidate with h0>=1,b0=0 is feasible. Every other candidate has delta>=v. Hence T(s)=s+j is the immediate successor.

In the remaining case, s<=i and s+j>K. Neither pure step is feasible; every possible candidate has h0>=1 and b0>=1 and hence delta>=u+v. The candidate t=s+j-i obeys 1<=t<=j<=K and attains delta=u+v, so T(s)=s+j-i is the immediate successor.

For the first point, take the positive displacement from index zero to s; the same decomposition forces b0>=1 (because s>0), so epsilon_s>=v. The index s=j attains v. Thus the first index is j.

Every step is the unique immediate circular successor, since the irrationality of theta makes the K phases distinct. Iterating from the smallest positive phase visits all K points in order and returns to j. QED.

The proof also works for a rational p/q with no phase collisions among indices 1,...,K, such as gcd(p,q)=1 and q>K. This is the finite rational domain in the exhaustive checker.

## Corollary R54-B: exact three-gap multiplicities

The u step occurs K-i times (s>i), the v step occurs K-j times (s+j<=K), and the u+v step occurs i+j-K times. These numbers sum to K. The determinant relation gives j*u + i*v=1, so the sum of all circular step lengths equals exactly 1.

For the frozen S23 instance K=352, (a,i,c,j)=(43,164,59,225), giving gap counts

    (u, v, u+v) = (188, 127, 37).

The initial ranked indices are 225, 61, 286, 122, 347, 183, 19, 244, 80, 305, 141, 202. This includes the earlier R51 top-five result without ranking queries.

For theta=sqrt(2)-1, K=12, the Farey pair is 2/5 < theta < 5/12, and the exact generated order is:

    12, 7, 2, 9, 4, 11, 6, 1, 8, 3, 10, 5.

In particular the fourth candidate s=9, missed by the semiconvergent-only record family, appears automatically.

## Corollary R54-C: interval-certified ranking without individual cut comparisons

Suppose theta is known only through a rational enclosure [A/D,B/D] and both endpoints lie *strictly inside the same Farey-neighbor interval* (a/i,c/j), with i+j>K, i,j<=K. Then every theta in that enclosure (avoiding rational resonances, or for the irrational task domain automatically) has exactly the same phase-cut permutation T and the same index ranking. The checked endpoint inequalities are

    a*D < A*i,   a*D < B*i,   c*D > A*j,   c*D > B*j.

Thus one pair of certified Farey neighbors serves as a complete order certificate, including all K(K-1)/2 comparisons implicitly.

The frozen S23 envelope used for this auxiliary rotation is

    A=262204504569236716045286,
    B=262204504569236716045287, D=10^24.

At K=352, the certified Farey pair is (43/164,59/225).

## Algorithmic cost and interface

A/b, c/d are obtained by ordinary Stern–Brocot updates, batched using integer binary search for the maximal allowed run on one side. For a fixed precision input p/q the published exact implementation makes O(log K) quotient blocks with O(log K) integer comparisons per block in the conservative bound, followed by exactly k constant-count integer index updates and O(k) output words. The standard Euclidean-quotient implementation can refine this bound. All comparisons include multiplication of numbers with up to O(log(qK)) bits; interval construction and sufficient precision are charged separately. The leading output cost is Omega(k).

The resulting top-k cut stream may replace the sort/heap/Floor Sum cut oracle in R52/R53 *without changing their owner identity or original historical labels*: at each crossed cut s, apply exactly the source moves z+r=s established in R52. Full output of K cuts costs O(K) index operations, independent of comparison sorting. The R53 indexed-age data structure remains O(H+m) live words and expected O(log H) per source move with a treap; deterministic balanced sets are an alternative with worst-case guarantees.

## Executed evidence

Two independent exact scripts and certificates accompany this R54 author-side result. The published standalone verifier checks all 12,620 coprime rational p/q with 3<=q<=40 and all 1<=K<q; 300 seeded rational families with K up to 799; five strict dyadic-enclosure quadratic families; and three frozen S23 families (K=352,100000,1000000). Each generated answer is checked against an independent exact residue sort or full-range k-best heap. The S23 K=1,000,000 first twelve are [630382,154021,784403,308042,938424,462063,616084,139723,770105,293744,924126,447765], obtained with 15 quotient blocks and independently checked by one million exact residues.

The independent S23 full 352-cut labelled-owner sweep uses the generated cut order and reconstructs the 225 source memberships at every cell for *both* interval endpoints, while preserving all 128 historical labels; it records 28,800 cyclic moves (including the last cut), 290 changes of the full youngest-age vector, and exactly the three-gap multiplicities 188/127/37. This is a finite cross-check, not a new formal Result or independent peer review. Prior source R53 counted 28,672 moves when omitting the final cyclic return, consistent with the R52 exact total mH=28,800.

## Native scope and next questions

This theorem is an exact result about rotation cut rankings and therefore provides a cut oracle for an existing auxiliary computation. No quotient of full X6 native relational state is taken. It neither claims a Heartbeat native dynamics proof nor supplies a task CLAIM/Result/Review. Follow-on R55: measure complete integer-bit complexity and direct cut generation versus Floor Sum for large K; replace the sorting oracle in the frozen finite Farey risk computation; assess source age sweep through original labels and staged risk output without a hidden scalar collapse.