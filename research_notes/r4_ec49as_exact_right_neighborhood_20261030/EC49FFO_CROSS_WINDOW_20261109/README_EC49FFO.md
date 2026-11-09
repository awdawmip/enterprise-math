# EC49FFO — H4/H5 exact cross-window BRC prefix optimum and extension ladder

Date: 2026-11-09; status: AUTHOR_EXACT_INTEGER_DP + ANALYTIC_CONSTRUCTION, pending independent Driver review and native Result.
Frozen science `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Model: original six ordered signed X6 operations and 9-state DFA from EC49FFJ native model (blob `6350340fbe869f17b5a50bd1ba30640db44a3a99`). P000 and ACTIVE worldview unchanged.

## 1. Exact H4/H5 theorem (unrestricted key budget)

Require one eligible operation word for each signature {1,2,4,8} at H4 and again at H5: eight horizon/observer demands. Cost C_native is the cardinality of the union of **nonempty ordered signed X6 microstep prefixes**. Each word has its original complete BRC key K=(x,y,z). Then

**min C_native = 40**, even with no key-number limit. The minimum is achievable with two complete keys: H4 (4,2,1), H5 (4,3,1). Consequently it is also the exact minimum under <=5 or <=2 keys for this eight-demand subproblem.

Upper witness, output order 4/2/8/1:
- H4: `fegc`, `fegd`, `gfec`, `gfed` (key (4,2,1), native length 12)
- H5: `fegcg`, `fegdg`, `gfecg`, `gfedg` (key (4,3,1), native length 14).

The H4 prefix union has 32 edges; four distinct final native paths each append the native `g=(+E2,-E2)` microstep pair, giving eight new edges, hence 40.

Lower proof: Original admissible operation counts at window h are
`#a=z-1, #e=z, #c+#d=x+y-h-1>=1, #f=h+1-y-2z>=0, #g=h+1-x>=0`.
These imply `1<=z<=floor((h+1)/2)`, `2z<=x<=h+1`, `0<=y<=h+1-2z`. Exhaustive enumeration covers *every* legal key: seven at H4 and thirteen at H5, producing 176 and 950 eligible low-signature operation words (1,126 total). Expand every word into its exact ordered signed native microsteps, and merge their prefixes into one rooted trie of **4,903 nodes including its root**.

Each terminal trie node carries its exact subset of eight horizon/signature demand labels. For every node u and demand subset S, DP_u(S) is the minimal number of edges below u needed to connect u to terminals realizing S. Initially DP_u(empty)=0 and DP_u(S)=0 for every subset of the labels at u. For each child v combine disjoint demand subsets A,B with
`DP_u(A union B) = min(DP_u(A union B), DP_u(A)+DP_v(B)+1)` when B is nonempty. A child used for no demand contributes zero. Any feasible selected terminal set can assign each demand to one selected terminal; overlapping demand assignments can be made disjoint without increasing its edge union. Induction over trie subtrees therefore proves the recurrence exact. The executable pure-integer verifier's root/full-8-mask result is **40**, with reconstructed witnesses whose native prefix union is recounted independently of the DP. This is a finite *complete-domain* lower certificate, not an extrapolation from individual-window optima. See `VERIFY_EC49FFO.py` and `EXACT_REPORT_EC49FFO.json`.

## 2. Analytic window-extension lemma

For any valid word w at window h, key (x,y,z), whose 9-state DFA terminal is noninitial, appending `g` leaves its signature unchanged. At h+1 the new complete key is (x,y+1,z), because #g increases by one while the other counts stay fixed. Its ordered native microstep path appends (+E2,-E2) and keeps its X6 endpoint. The symmetric `f` append moves key to (x+1,y,z) and adds (+E1,-E1). The source DFA has both f and g acting as identity on every noninitial terminal state.

Given four distinct same-length low-signature terminal paths, one same-letter g-extension per path adds precisely 8 prefixes: their terminal nodes are different, and the new two levels are disjoint. Repeating the extension yields a rigorously defined multiwindow family, without collapsing ordered provenance.

## 3. Explicit 22-path / five-key / 70-edge *alternative quota* family

For integer m>=1, windows h=4+j (j=0,...,m), use K_j=(4,2+j,1). At each window, four low words (signatures 4/2/8/1) are `fegc g^j`, `fegd g^j`, `gfec g^j`, `gfed g^j` with spaces removed. At **H5** add two high words with key K_0=(4,2,1): signature 16 word `fegfg` and signature 32 word `gfefg`.

Then the exact counts are **m+1 complete keys**, **4(m+1)+2 separate horizon/signature witnesses**, and
`C_native=38+8*m`. Proof: base H4 prefix union 32, every new window's four distinct terminal extensions add eight edges, and the two additional H5 high paths add six edges at native depths 10,11,12 (two each). Subsequent extended low branches occur after the high paths terminate and add exactly eight per window. The independent DFA/native verifier checks the complete identities and directly recounts the union for every m=1,...,32.

At m=4: **22 words, 5 complete keys, C_native=70** for the specific quota mask (all four low signatures H4-H8, both high signatures H5). The original mother task's 22-path templates require **different H2/H3 and later high-signature placements**, for which existing 94-edge certificates remain intact. This is a constructive demonstration of the quota-sensitivity of lower bounds and a reusable prefix-sharing mechanism; it is not an attainment claim for the mother's original quota mask.

## 4. Executed evidence / next question

Original local execution: two independent executable scripts; 8-demand H4/H5 exhaustive integer trie DP (7+13 keys, 1,126 words, 4,903 nodes, optimum 40, witness reconstruction), and independent direct model verifier for m=1..32, including m=4 yielding 70 edges. See `VERIFY_EC49FFO.py`, `VERIFY_EC49FFO_LADDER.py`, `EXACT_REPORT_EC49FFO.json`; local originals and full run logs also retained in turn evidence package. Shared Source activity registration is separate from Result/Driver acceptance.

Next: take the mother's **exact** H2/H3 and later high-window quotas; test if an f/g extension can share with those forced witnesses, then use a key-budget-aware colored native trie algorithm to search a new unclassified admissible quota pattern. Avoid replacing mother quotas by this alternative family.
