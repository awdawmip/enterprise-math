# EC49FBB — H9 cache-budget forces 38 early native edges even with mixed H4/H5 keys

Date: 2026-11-05 Asia/Shanghai. Status: AUTHOR_EXACT_FINITE_DP_CHECKED; NOT_INDEPENDENTLY_REVIEWED; NOT_ADMITTED.

Scientific input frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Continues EC49FBA at `8ea1d8680c71af8040671e00f3abe6674f8da760`, with EC49FAZ's complete 112-edge nine-window witness as an attainment example. P000, ACTIVE Heartbeat World, signed native X6 and the declared six-signature observer are unchanged.

## Exact theorem, complete qualification

Fix H2={`fe`,`ge`} and H3={`feg`,`gef`}. In any valid H2–H9 construction under the frozen seven-operation model and at most **five** distinct complete positive-step six-axis BRC keys, allow arbitrary finite word subsets and arbitrary mixtures of keys inside both H4 and H5. Require each window's rational nine-history observation matrix to have rank 9; paths end at signed displacement (+2,0,0,0,0,0). Counting distinct **signed primitive X6 prefix edges** across H2–H5 gives

```
             E(H2..H5) >= 38.
```

The bound is attained in an actual full nine-window construction: H4={`fegc`,`fegd`,`gefc`,`gefd`}, H5={`feggf`,`gefgf`}, and H6–H9 use the remaining key (6,4,1,0,0,0) per EC49FAZ's 112-edge witness. The early prefix union has 38 native edges.

## Necessary H9-key classification and exhaustive proof

The fixed H2/H3 words already occupy 16 distinct native-prefix edges and three keys: (2,1,1), (3,0,1), (3,1,1). At every length h, any complete key (x,y,z,0,0,0) of a valid word satisfies `#c+#d=x+y-h-1 >=0`. Thus an H9 key must have x+y>=10, and none of the three original keys can cover H9.

Enumerate all 6^4 + 6^5=9072 ordered H4/H5 operation words over `acdefg`; expand each into the signed primitive steps from EC49FBA, calculate the endpoint, complete positive-step key and nine-state observer. Exactly **206 H4 words** and **1,062 H5 words** have the required endpoint and an allowed signature. Outside the original three keys, exactly **27** different complete keys appear in this 1,268-word pool. Among these, the **only** key with x+y>=10 is (6,4,1,0,0,0).

A complete nine-window construction with five global keys must therefore fall under one of two covering relaxations for H4/H5:

1. Its actual H9 key is unused at H4/H5. The early pool may use the original three keys and at most one new key `q`. Evaluate every one of the 27 choices.
2. Its actual H9 key occurs in H4/H5. It must be (6,4,1,0,0,0). The early pool may use the original three keys, this H9-compatible key, and at most one additional new key `q`. Evaluate the 26 other choices; the case with no other key is already in case 1.

The two exhaustions yield: **7/27 feasible early key pools, minimum 38** in case 1; **9/26 feasible relaxed pools, minimum 38** in case 2. A pool is feasible when both H4 and H5 individually meet the four-clause nine-history rank criterion. Pool membership alone is not counted as using the key; thus allowing unused keys makes the search a valid lower-bound relaxation.

For a fixed pool, insert every eligible ordered word into a trie of original **signed primitive steps**, tagging an H4 terminal with its six-signature mask and H5 terminal with the mask shifted left six positions. Mark the 16 fixed H2/H3 edges as already paid. The subtree DP state `D_v[m]` minimizes additional distinct edges for exact terminal OR mask `m`. Initialize empty selection and each terminal; convolve children under bitwise OR, adding costs, and add the incoming edge once for every nonempty selected subtree. Induction on trie height proves that this is the exact finite minimum; at the root retain masks satisfying the rank-four-clause criterion in both six-bit halves. The two covering cases prove the theorem. `VERIFY_EC49FBB.js` is the executed script and `EXACT_REPORT_EC49FBB.json` holds all 53 pool results, state counts and witnesses.

The best pool in both relaxations permits `q=(4,2,1,0,0,0)`; the optimal terminals give masks 15 and 48 and a prefix-union recount of 38 native edges. These four clauses are equivalent to the frozen rational-rank-nine test by EC49FAR. All operations and trie costs use integers and preserve primitive order/branch identity.

## Value and next mathematical question

This strengthens the EC49FBA one-key-per-H4/H5 result to **arbitrary H4/H5 key mixing**, conditional on the actual five-key H9 budget. The earlier 24-edge H2–H5 local solutions occupy key configurations that cannot meet that global budget in the present fixed H2/H3 scheme. The full H9 global author-side interval remains 80<=E*<=94.

Next: allow the H2/H3 structure to vary, or optimize both remaining key choices for H6–H9 jointly. This theorem supplies an exact 38-edge necessary frontier for the fixed-H2/H3 branch and a reproducible list of admissible early key pools. No mathematical admission, formal CLAIM or independent Driver review is asserted.
