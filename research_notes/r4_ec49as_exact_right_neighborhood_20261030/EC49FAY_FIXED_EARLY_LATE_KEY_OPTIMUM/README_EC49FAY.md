# EC49FAY — Exact 112-edge optimum for a fixed early prefix and late BRC cache key

Date: 2026-11-05 Asia/Shanghai. Status: **AUTHOR_ANALYTIC_PROOF / EXACT_FINITE_DP_CHECKED / UNREVIEWED / NOT_ADMITTED**.
Frozen science pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Previous verified author frontier: EC49FAX at `f67f2dbe6fb39372c0256fa1d51855cc2717fb9a`.

## Theorem: a complete, declared finite nine-horizon family

Work in the original frozen signed native-X6 seven-operation model (b is forced absent by terminal displacement). Fix H2, H3, H4, H5 **exactly** as follows:

~~~text
H2: fe, ge
H3: feg, gef
H4: fegc, fegd, gefc, gefd
H5: feggf, gefgf
~~~

These fixed words contribute exactly **38 distinct ordered signed primitive-prefix edges**, and their complete positive BRC cache keys are (2,1,1,0,0,0), (3,0,1,0,0,0), (3,1,1,0,0,0), (4,2,1,0,0,0).
Require all selected H6,H7,H8,H9 words to have the additional complete cache key **K=(6,4,1,0,0,0)**, the same original nine-history signed native observer, one of the six permitted signatures D,E,C,J,F,G, exact endpoint displacement (+2,0,0,0,0,0), and rational observation rank nine at each horizon.

Then the minimum total number of distinct signed primitive-prefix edges is:

**E* = 38 + 74 = 112.**

This is a **family theorem with the fixed H2–H5 words and fixed late key**; the full unrestricted nine-horizon problem retains the author's earlier range 80 <= E* <= 94.

## Exhaustive argument

At horizon h and key K=(6,4,1,0,0,0), endpoint/key balance forces #a=0, #e=1, #c+#d=9-h, #f=#g=h-5. Consequently every eligible late word belongs to the finite multiset permutation universe

  e * (c|d)^(9-h) * f^(h-5) * g^(h-5),

where this notation means **all ordered permutations** with exactly the indicated multiplicities, and all assignments of the c/d positions. Each such word uses the original ordered signed primitive expansions a=(-1,-1), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1), e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2).

The exact nine-state observer previously derived in EC49FAX filters the complete enumeration to these counts:

| Horizon | Required signatures | Eligible words |
|---:|---|---:|
| H6 | D,E,C,J | 240 |
| H7 | D,E,C,J | 1260 |
| H8 | D,E,C,J | 2240 |
| H9 | F,G | 560 |

For h=6,7,8 the count #c+#d is positive, so the nine-state transition table rules out final F or G: c or d either prevents entering F/G or causes a permanent exit from them. Therefore EC49FAR's four-clause rank-nine criterion forces all four D,E,C,J. At H9, #c+#d=0, hence only F,G are eligible and both are required.

Construct a trie of **ordered signed primitive steps**, not operation-level edges. For every terminal eligible word, attach its corresponding bit among 4+4+4+2=14 observation coverage requirements. At node v define DP_v(mask) as the smallest number of *additional* primitive-prefix edges in that subtree whose selected terminals produce precisely the bitwise-OR mask. At each terminal allow selection or omission. Combine child tables using OR and minimum of summed costs. If mask is nonzero, charge one for edge into v unless that literal signed primitive prefix already belongs to the fixed early H2–H5 set. This is the exact min-plus/OR recurrence. Bottom-up induction proves it minimizes over **all subsets of eligible late words**, with all shared prefixes counted once.

The actually executed JavaScript implementation built 26705 trie nodes (including root) and computed 16384 root coverage states; its 424124 child-table pair combinations gave exact minima 32 for H6, 44 for H6+H7, 68 for H6+H7+H8, and **74** for the complete four-window target. The complete mask is 2^14-1=16383.

## Attaining witness and verification

~~~text
H6: fegccc, fegddd, gefccc, gefddd
H7: fegccfg, fegddgf, gefccfg, gefddgf
H8: feggfgfc, feggfgfd, gefgfgfc, gefgfgfd
H9: feggfgfgf, gefgfgfgf
~~~

The program directly expands each witness word into signed X6 primitive steps, sums six signed displacement coordinates, counts all six positive cache coordinates, computes the observer signature, and checks the exact four-clause rank test. Cumulative union costs H2 through H9 are **12, 16, 32, 38, 70, 82, 106, 112**. The witness attains the computed 74-edge marginal minimum; thus the stated family optimum is exact.

Reproduce with Node.js >=18: `node VERIFY_EC49FAY.js > EXACT_REPORT_EC49FAY.json`. The report contains the full witness, signature masks/keys, enumeration sizes, trie/DP certificate summary, and the actual finite output.

## BRC application and next question

The BRC carrier here is a complete six-coordinate positive cache key with each branch distinguished by its original ordered signed-X6 primitive path. The observer is the six-signature nine-history automaton; its exact quotient was proved in EC49FAX for all future operation words. The cost observer retains all literal signed primitive prefixes and their joint provenance. Only the finite **H6–H9** candidate pool is enumerated; no phase, path order or prefix sharing is erased.

Next unit EC49FAZ: reoptimize the H4/H5 **word selection** (rather than holding it fixed), then compare other of EC49FAW's 124 cache-key pairs and the 31-edge two-key H2/H3 early construction. Seek a lower-cost exact construction or a full-family bound. The known unrelated 94-edge global witness remains valid; P000 and ACTIVE worldview are unchanged.

Authority: author-side proof/evidence only, pending native CLAIM/Result and independent Driver admission.