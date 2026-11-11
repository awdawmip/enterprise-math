# EC49FIX — Exact B=3 cache-key-release pair obstruction (2026-11-11)

## Frozen inputs / authoritative scope

Continue the **24-label nine-state BRC** instance pinned to
\`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`, and the two original
EC49FGJ witnesses A and B, each with seven complete raw cache keys and
94 distinct nonempty *ordered signed X6 native-microstep prefixes*.
Original grammar and witnesses are in sibling
\`EC49FGW_RADIUS5_EXACT_SCREENS_20261110/\` (24 labels, 178,850 legal words,
94 key types; 9,838 legal words with each witness's seven original keys).
Original keys are full raw keys, **not** interchangeable endpoint vectors.

For a six-label set Q (indices 0..23), let F(Q) be the union of complete
native prefixes of the 18 fixed original words. This unit concerns the
**released-original-key, B=93-|F(Q)|=3** six-label backgrounds: |F|=90.

## New exact finite theorem

For each witness, precisely 8,856 of these six-label positions release at
least one original cache key. Their 90-edge fixed backgrounds fall into
**10 distinct original-native-prefix sets**. Four groups contain exactly
one H8 label (885 positions each); the previous singleton audit already
excluded all 3,540 positions. Six groups contain exactly two H8 labels
(886 positions each, one for each pair from {18,19,20,21}).

For any of the six two-H8 groups, if the replacement words use only the
seven original complete raw keys, each demanded H8 label has exactly
**one** admissible new-prefix set of size <=3, and the union of the two
forced new-prefix sets has size **4**, verified using every legal word of
those keys. Thus no legal six-path completion using the original seven
keys adds <=3 native prefixes. The original witness adds 4. This is an
**exact 94-edge optimum within those original keys** for each of the
6 × 886 = 5,316 backgrounds per witness.

An independent finite **complete key-cover** test (all 94 raw key types)
shows that in exactly 885/886 positions of each two-H8 group, any legal
completion with <=7 total raw keys must recover all seven *original*
keys. In the remaining one per group, a different key set is possible.
Those six exceptional positions per witness were **already** excluded
by EC49FIS's separate full-six exact check and are NOT counted as new.

Therefore **5,310 new cache-key-limited six-path backgrounds per witness**
and **10,620 across A+B** have exact optimum 94. All 8,856 B=3
released-key backgrounds per witness are now covered by disjoint evidence:
3,540 previously solved singleton cases, 5,310 new forced-key pair
cases, and six previously solved genuinely reallocatable cases.
The new finite theorem is restricted to these six-replacement neighborhoods.
It does not establish the global seven-key optimum.

## Proof / evidence / reproducibility

Let P(w) be the set of full signed, ordered native prefixes of legal word
w. For fixed F, any selected two demands i,j obey

\[
 |P(w_i)\cup P(w_j)\setminus F|\le3
 \ \Longrightarrow\
 |P(w_i)\setminus F|\le3,\quad |P(w_j)\setminus F|\le3.
\]

The executable \`VERIFY_EC49FIX.py\` enumerates every legal word using
the frozen observer and seven original key types, all C(24,6)=134,596
six-subsets for each witness, every released B=3 group, and all 94
possible raw keys in the key-cover oracle. The unique size<=3
candidate sets of both H8 labels have union cardinality 4 for each
of the six two-H8 backgrounds. The exact comparison is made with
bytes representing the **ordered signed six-axis prefixes**, not endpoints.

A second, independently coded exact rooted-trie dynamic program
\`VERIFY_PAIR_EC49FIX.cpp\` computes all 276 labelled-pair minima
for every one of the ten fixed-prefix groups, using the original
seven-key 42,735-node signed-prefix tries. All twelve new H8-pair
checks (six per witness) return **4**, consistent with the Python
direct-prefix enumeration. This independent audit was actually run locally.
Its recurrence pays each native prefix edge once when a child subtree
is selected, and is exact by induction over the tree.

Reproduction from the PR branch:
1. Run \`python EC49FIX_B3_RELEASE_PAIR_20261111/VERIFY_EC49FIX.py\`
   from anywhere (it imports the frozen EC49FGW sibling) to regenerate
   \`EXACT_REPORT_EC49FIX.json\` and \`B3_REP_MASKS_{A,B}.txt\`.
2. Run \`python EC49FIO_RADIUS6_B13_FULL_DP_20261111/MAKE_INPUT_EC49FIO.py\`
   to regenerate its existing \`TRIE_{A,B}.txt\`.
3. Compile \`g++ -std=c++17 -O3 -o verify_pair
   EC49FIX_B3_RELEASE_PAIR_20261111/VERIFY_PAIR_EC49FIX.cpp\`,
   and use \`verify_pair TRIE_A.txt B3_REP_MASKS_A.txt\` (and B) to
   reproduce pair minima; for each group choose its H8 index pair from
   regenerated JSON and verify result=4.

Actual execution: portable Python verifier prints
\`EC49FIX_PROFILE_PASS A\`, \`EC49FIX_PROFILE_PASS B\`,
\`EC49FIX_EXACT_PASS new 10620\`. Independently executed C++ prints
ten completed group audits per witness; all twelve relevant H8-pair
minima equal 4. See \`EXACT_SUMMARY_EC49FIX.json\` and the regenerated
complete per-group report for the exact counts.

## Source and next objective

EC49FIR supplies the previous forced-seven-key singleton counts;
EC49FIS supplies the six genuine alternative-key B=3 cases and
their separate complete exact exclusion. EC49FIQ covers retained-key
six-path backgrounds. EC49FIW closes genuine released-key
reallocation B>=9. **Next:** reconcile all remaining forced-original-
seven-key, singleton-surviving B>=5 six-path backgrounds against
existing prefix certificates and extend the pair/triple grouped-F
calculation; then radius-seven exploration.

Author finite exact computation and proof, **unreviewed**, **not an
immutable shared Task Result**, **no CLAIM**, and no P000 change.
