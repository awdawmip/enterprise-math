# Stage460-B — Two-POP-each exact positive-BRC quotient and grouped ranking

Date: 2026-11-06. Classification: **author-side exact proof and executed finite checks**; independent mathematical review/Source Result admission pending.

## Frozen scientific sources and current rule boundary

Parent: Stage459-B, commit 5a9236730eae032c6742dd3c6b7cca2e8a8895ff, research_notes/n12_x6_native_brc_stage459b_one_one_pop_rank_20261106_RESEARCH2/PROOF_STAGE459B.md. Scientific pins retained: global knowledge bf84bd7c61a2444b59b1da96be57df0e9ae47e53, Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, frozen P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current behavioral norms read independently on 2026-11-06.

## Model, BRC carrier, observer and operations

The native spatial basis is six signed integer axes in X6. The original source-ordered histories are two *distinct* words P,Q over A=+E1, B=-E1 of lengths 2 <= m < n. Both words begin and end with A and have pairwise nonadjacent interior B defects. Fix exact counts kP, kQ, and exactly d positional mismatches among indices 1..m. The population F consists of all such ordered history pairs; each pair is a separate positive BRC branch with weight 1 in the finite natural-number semiring. All operations are exact integer additions/multiplications; support is the strictly-positive projection. No signed-amplitude cancellation or heartbeat physical-time evolution is being evaluated.

The initial full observer is both lengths, both 6D signed endpoints, both 12x12 *directed* edge histograms, and K = sum_{i<=m} [P_i=Q_i] = m-d. Every future prefix carries labeled POP_P and POP_Q operations, each available at most twice, with POP of an empty path disallowed; **APPEND budgets are both zero**. The observer is read after every legal prefix, including paths of length zero. P and Q provenance and multiplicities are retained until quotient support and mass are computed.

## Lemma 460.1 — Commuting POP grid

For any history, POP_P and POP_Q act on separate sources, so the resulting current histories depend only on the counts (a,b) of each POP operation, not their interleaving. For the present budgets, each reachable count pair is represented by

O(P[1:m-a], Q[1:n-b]), 0 <= a <= min(2,m), 0 <= b <= min(2,n).

Thus equality of all labeled future observer trees is equivalent to equality at the at most nine grid cells. Every grid cell is reachable by an actual legal labeled sequence. This is an exact equivalence, not a finite-sample approximation.

## Theorem 460.2 — Minimal exact repair coordinates inside a fixed initial fiber

Form the sorted, deduplicated index sets

I_P = {m-2,m-1} intersect {1,...,m-1},

I_Q = {m-1,m,n-2,n-1} intersect {1,...,n-1},

and the binary repair key

R_460(P,Q) = ((P_i)_{i in I_P}, (Q_i)_{i in I_Q}).

**For every fixed initial full-observer fiber F**, two original history pairs have identical observers after *all* legal future POP sequences iff their repair keys coincide. The key uses at most six bits, hence q_F <= 64. For m=2, the missing P_(m-2) entry is omitted; all positions 1 and endpoints are genuinely fixed A. For n=m+1, overlapping Q indices are retained only once.

### Sufficiency

From initial O, removing a terminal original step updates each source endpoint by subtracting the original direction and updates its directed edge histogram by subtracting the unique edge from its penultimate direction to the removed terminal direction. For up to two POPs these directions are included in R_460 (or are the fixed terminal A); all source lengths are known. After a,b POPs, current overlap length is L = min(m-a,n-b), which satisfies L >= m-2, as n>=m+1 and both budgets are at most two. Thus the only original match indicators that can be subtracted from initial K are at positions m-1,m. Their P and Q letters are exactly in the repair key or fixed A. Therefore every grid observer is an exact function of (initial O,R_460). Lemma 460.1 completes sufficiency.

### Necessity

The observer difference when P is POPped once uniquely identifies P_(m-1) via the deleted directed edge (P_(m-1), A). If P can be POPped twice, the second deleted edge identifies P_(m-2), because P_(m-1) has already been recovered. Correspondingly, one and two Q POPs recover Q_(n-1) and Q_(n-2) from the directed-edge histogram differences. The initial-to-one-P-POP change in K identifies [A=Q_m]; in the binary original alphabet this identifies Q_m. The one-to-two-P-POP change in K identifies [P_(m-1)=Q_(m-1)]; P_(m-1) already known and the alphabet is binary, so it identifies Q_(m-1). Every applicable nonconstant repair coordinate is therefore a function of the future-observer grid. Fixed coordinates (first A, endpoint A, and coinciding positions) remain known. Necessity follows. **Minimal** means coordinates necessary as a universal sufficient key across these fibers, up to algebraically forced duplicates/constants; individual specific fibers may constrain additional key bits.

## Constructive information-loss witnesses

The following pairs share (m,n,kP,kQ,d), hence the entire initial full observer. Both sources remain A-ended and their B defects are isolated. Deleting the indicated repair coordinate while keeping all other coordinates gives two different future grid observations.

**Q_m witness**: (m,n,kP,kQ,d)=(3,6,0,1,1), P=AAA in both, Q=ABAAAA versus AABAAA. Both have identical P/Q predecessor tails, but after one P POP their match counts are respectively 1 and 2. Here Q_m separates the two.

**Q_(m-1) witness**: (4,7,0,1,1), P=AAAA in both, Q=ABAAAAA versus AABAAAA. They agree on all repair bits except Q_3; after two P POPs match counts are respectively 1 and 2.

**P_(m-2) witness**: (5,8,1,0,1), Q=AAAAAAAA in both, P=ABAAA versus AABAA. They agree on all repair bits except P_3, but after two P POPs the deleted directed edge differs. The match count in this particular distinguishing state is 2 in both; directed adjacency is essential.

## Theorem 460.3 — Exact grouped BRC masses, support, rank/unrank

For every binary key w, impose its P/Q original-index constraints and run a source-ordered product automaton over original positions i=1..n. Its state is (a,b,h,prevP,prevQ), where a,b count B defects separately, h counts source mismatches for i<=m, and prevP,prevQ are the immediately preceding original directions. Every source choice extends a state by its natural-number mass, rejects BB joins in either source, and enforces fixed first/last A. For i>m, only Q extends, while P's previous original direction remains retained. The terminal sum at a=kP,b=kQ,h=d is the exact positive BRC population M(w).

Each original pair has exactly one key and one DP path. Conversely, every successful DP path reconstructs one eligible ordered source pair. Consequently |F| = sum_w M(w), q_F = sum_w [M(w)>0], and all class populations are nonnegative integers with distinct source histories counted individually.

A binary prefix-support recursion visits at most the 2^s possible key assignments, s<=6, and memoizes subtree (positive-class-count, raw-mass). Rank and unrank compare A-before-B subtree-support counts and require at most s branch decisions after this precomputation. No raw history list or stored class roster is required; the algorithm still evaluates up to 64 candidate key leaves, a **constant-sized** scan in this fixed two-POP model.

The automaton has O((kP+1)(kQ+1)(d+1)) possible counters and four boundary-letter combinations per position; each has at most four transitions. A full count/rank table therefore costs O(2^6 n (kP+1)(kQ+1)(d+1)) natural-number operations, with maximum integer value at most 2^(m+n) and O(m+n)-bit operands. With schoolbook arithmetic, additions incur O(m+n) bit complexity per operation. Working automaton memory is O((kP+1)(kQ+1)(d+1)) integers plus <=127 support tree nodes. This statement accounts for preprocessing, input length, integer bit length, and output rank bit length (<=6) within the frozen model.

## Executed evidence and coverage

Reproduce with python3 STAGE460B.py > STAGE460B_EXECUTED.json using Python 3 standard library. Source and exact stdout were compared before publication. The checker builds an **independent** original-history enumerator and computes 6D endpoints, full 12x12 directed adjacency and match statistics at all reachable POP-grid states. Its equality oracle does not call the counting DP. Comparison is exhaustive for tested parameter fibers; the mathematical proofs above establish general statements under the stated hypotheses.

Actual run: 1115 small parameter fibers, 396 nonempty, 1856 original history pairs, 1182 supported-key population/rank/unrank checks, 1856 future-grid signature checks, including 14 nonempty POP-to-empty fibers and all gaps n-m in {1,2,3,4}. All assertions passed. Larger exact counts: (m,n,kP,kQ,d)=(64,80,15,17,1) gives q=21, |F|=5,061,384,194,832,966; (92,126,20,25,3) gives q=27, |F|=1,121,449,082,621,221,549,433,213,976. Both rank/unrank at first, median, and last passed. Initial source population agrees with Stage459-B and Stage458-B for the same fibers, and 21 refines Stage459-B's six classes for one-POP-each with zero APPEND.

## Open target

Stage461-B: Add signed native APPEND budgets (rP,rQ) beginning with (1,0) and (1,1), preserving all twelve original future direction choices, dual predecessor tails and newly probeable cross-match windows. Build a polynomial grouped-support/ranking automaton whose key can grow with budgets, with the same provenance, boundary and exact population accounting. Compare complexity when visible key length is no longer bounded by six; construct and retain any shortest failed-join witness. Native authenticated claim/Result and independent Driver admission remain separate from this author-side proof.
