# EC49FBQ — Exact H2/H3-root-aware H8/H9 native X6 prefix union

**Date:** 2026-11-05. **Mode:** author-side TASK research, finite exact proof. **Frozen science input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Scientific predecessor:** EC49FBP at `c7e366fd4c9158e7d05f49231b858c7ff522ead0`. P000 and the six-axis native signed semantics remain unchanged.

## Selected mathematical question

Fix the existing H2 paths `fe,ge` and H3 paths `feg,gef`. Their set R of ordered signed-native primitive-prefix edges has exactly **16 edges**. For each H9-eligible complete BRC key M=(x,10-x,z,0,0,0), measure the **minimum total union of R plus H8/H9 observation witnesses**. H8 requires signatures 1,2,4,8; H9 requires signatures 16,32. This is the first controlled step toward the 27+28 complete H2–H9 key schedules, but it does not impose any uncomputed H4–H7 cost.

The native expansions, preserved as signed ordered axes, are
`a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2)`.
The nine-state observer and operation-count constraints are the unchanged frozen EC49FBP definitions. The 16-key domain is
`1<=z<=4; 2z+1<=x<=9; y=10-x`.

## Finite exact theorem

Let C_root89(M) be the minimum number of distinct native prefix edges in R union six chosen observation-accepted H8/H9 paths. Then

```
C_root89(x,10-x,z) =
   50 + 4z,  1<=z<=3 and 2z+2<=x<=8;
   80 + 8z,  1<=z<=3 and (x=2z+1 or x=9);
   132,      z=4, x=9.
```

The complete evaluation is:

| z | x values | exact C_root89 |
|---|---|---:|
| 1 | 3,9 | 88 |
| 1 | 4,5,6,7,8 | 54 |
| 2 | 5,9 | 96 |
| 2 | 6,7,8 | 58 |
| 3 | 7,9 | 104 |
| 3 | 8 | 62 |
| 4 | 9 | 132 |

Compared with EC49FBP's six-signature H8/H9-alone optimum C89, adding the four fixed H2/H3 paths adds **zero** edges for ten keys and **two** edges for the six boundary keys with 1<=z<=3. The witnesses in the machine-readable certificate achieve every value; in particular, M=(7,3,2) retains a total cost **58** even after the fixed root is included.

## Exact proof and completeness of coverage

For horizon h, key M=(x,y,z,0,0,0) and a single chosen c or d, the exact operation counts are:
`#a=z-1, #e=z, #f=h+1-y-2z, #g=h+1-x, #(c+d)=x+y-h-1`.
At H8 this has exactly one c or d; at H9 neither. Enumerate **every distinct multiset permutation** of these counts, apply the frozen nine-state DFA after each operation, retain precisely the relevant accepted signatures, and expand all retained words into ordered signed primitive axes. Since the native words are finite, these operations completely specify the candidate domain. The H9 word candidates satisfy both F/G requirements by their signature.

Build the rooted native-prefix trie of all accepted paths. Let w(v,u)=0 when the child edge's full oriented native prefix already lies in R and w(v,u)=1 otherwise. For each node v and signature mask S in {0,...,63}, D_v[S] is the minimum *additional* edge cost below v that connects an exact-OR signature selection S. Initialize D_v[0]=0 and each terminal's own signature singleton at cost 0. Merge each child u by

`D'_v[A | B] = min(D'_v[A | B], D_v[A] + D_u[B] + w(v,u))` for `B != 0`,

also retaining the option not to use that child. Induction from leaves proves this finds the minimum additional edge cost for every exact-OR signature mask. The answer is `16+D_root[63]`, and all six signatures are nonzero singleton labels. One terminal per needed signature suffices because edge weights are nonnegative; the verifier checks exactly six selected witnesses and recomputes the native-prefix union.

A pure-Python enumerator/trie DP and an independently written Node.js count-recursion/array-DP were executed on **all 16 keys**; exact minima, candidate counts and trie node counts agreed. The largest candidate trie had **94,607 nodes**, and the aggregate trie count is **517,876** across the 16 disjoint key experiments. All witness unions, native endpoints (2,0,0,0,0,0), six-axis operation lengths and signatures are checked in the Python verifier.

This establishes the finite theorem relative to the frozen original observer and BRC key model. The unchanged mother target remains a complete H2–H9 rank-nine arrangement with at most five BRC keys, minimizing all distinct primitive-prefix edges.

## Reproduction, provenance, remaining question

Run `python VERIFY_EC49FBQ.py` and `node CROSSCHECK_EC49FBQ.js`. The Python program regenerates the 16-key JSON certificate `EXACT_REPORT_EC49FBQ.json`, including explicit optimal operation words, and the Node.js program independently recomputes the 16 minima. Exact machine-readable results and witnesses accompany this note.

**Next executable scientific unit:** introduce H7's four rank clauses and H4–H6's L/M key schedules into the same native-prefix mask optimization, retaining the fixed H2/H3 roots, and compare complete H2–H9 totals for the 27+28 horizon-feasible configurations. Separate author-side computation from independent Driver acceptance and Source Result rights.