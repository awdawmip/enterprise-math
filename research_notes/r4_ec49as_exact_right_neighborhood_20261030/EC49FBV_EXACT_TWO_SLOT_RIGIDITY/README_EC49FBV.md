# EC49FBV — Exact radius-two rigidity of the EC49FBU 158-edge native-X6 witness

Date: 2026-11-06. Frozen science pin: \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Parent witness: EC49FBU at \`b3b43ef6abe2fd816d979792d18a67ee5d0aad50\`. Research class: author-side finite exact theorem and executable certificate.

## Proposition (a local optimality theorem)

Keep the 24 selected operation words of EC49FBU, the fixed H2/H3 words, the full positive BRC cache schedule L=(4,2,1,0,0,0) at H4/H5 and M=(7,3,2,0,0,0) at H6–H9, the frozen nine-state observer, and the signed primitive-X6 prefix objective. Each of the 20 required H4–H9 terminal-signature slots contains exactly one selected word. Allow the word in any one or any two distinct slots to be replaced by **any** legal word from that same horizon and same terminal-signature group.

**The minimum possible distinct native primitive-prefix edge cost is exactly 158, attained by the original witness.** All 16,132 distinct one-slot alternatives and all 190 unordered two-slot group combinations are covered by exhaustive finite optimization. Thus any strict improvement within this fixed 24-slot construction must replace at least three words simultaneously, or adjust the root/schedule/signature-slot design.

This is an exact neighborhood statement, not a global lower bound for all nine-window witnesses. It preserves the broader 80≤E*≤94 benchmark as a different candidate family.

## Exhaustive enumeration

For cache key (x,y,z) at horizon h, let b=#c+#d. Full native endpoint and positive-BRC counts give #e=z, #a=z−1, b=x+y−h−1, #f=x−b−2z, #g=y−b. For each nonnegative solution, split b between c and d, enumerate every distinct multiset permutation of the six operations, reject DFA state 8 and retain its exact terminal signature. This recovers 48,24,120,2520,10080,3360 accepted words for H4–H9, totaling 16,152; exactly 20 are occupied, giving 16,132 single-word substitutions. The 24 original words and every terminal-signature slot are in the JSON certificate.

The cost of a set of words is the cardinality of its union of all nonempty ordered signed primitive prefixes. The six operation expansions are unchanged: a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2). The implementation encodes signed steps as distinct letters solely as a lossless finite representation; it reconstructs native six-axis endpoints and exact positive keys for all original paths.

For one slot, remove its original word and add each accepted replacement; count the exact prefix union. The minimum in every one of the 20 slots is 158. Exactly two slots (H9 signatures 16 and 32) have one additional cost-neutral alternative each; all other single replacements increase the cost.

For two slots A,B, fix R as the primitive-prefix union of the other 22 words. For a replacement a in group A and b in group B, the cost is |R|+|(P(a)∪P(b))\R|. Build a primitive-prefix trie over every b∈B. Assign cost 0 to a trie edge already in R and cost 1 to a fresh edge, then compute at each trie node v the minimal suffix cost D(v) to any accepted B terminal. For each a, the exact cheapest new contribution from B is min D(v), over trie nodes v along the primitive prefix path of a (including the root). This follows by classifying B paths by their maximal shared prefix with a. Thus the trie DP computes the exact minimum over all |A|×|B| candidate pairs without a quadratic enumeration. All 190 slot pairs have minimum 158. For every minimizing pair the separate direct primitive-prefix union is recomputed and matches.

## Executed validation and scientific status

The accompanying \`VERIFY_EC49FBV.js\` was executed in V8 with 16,152 accepted candidate words, all 20 single-slot groups and all 190 pair-of-group optimizations: PASS, minimum 158 everywhere. Independent Python standard-library code also enumerated all 16,132 one-word substitutions, used a separate native-prefix trie DP for all 190 slot pairs, and brute-force checked 5 representative slot pairs, including one containing 388,800 literal pairs: all minimum 158. The complete machine-readable report records each slot and each pair's optimizer result.

This local rigidity gives a discriminating route choice: to reduce 158 within the same schedule, investigate coordinated ≥3-word exchanges, a joint MILP over all 20 slots, or a different L/M schedule/root witness. A local optimization minimum is not a declaration that 158 is globally optimal. BRC use is \`REUSE_EXECUTED\`: exact positive keys, observer signatures and ordered primitive branch provenance are preserved. The lossless EC49FBS trie identity remains a separate exact model for a global solve.

Source-control status: author-side research artifact; formal Source CLAIM/Result and independent Driver admission depend on current native authority, not this GitHub commit.
