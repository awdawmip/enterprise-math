# EC49FLC — Complete matched-distance-five two-key BRC neighborhood

**Date:** 2026-11-12. **Frozen science:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Status:** AUTHOR_EXACT_FINITE_COMPUTATION, independent Driver review pending.

## Theorem

Use the frozen original nine-state signed X6 BRC catalogue: 178,850 lawful labeled operation words, 24 observation labels and 94 complete raw cache keys. The EC49FKX 84-prefix witness uses
`K*={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}`.

Delete two distinct keys `a,b` from K* and insert two distinct keys `u,v` from the remaining 87. The matched distance is
`d=min(||a-u||_1+||b-v||_1,||a-v||_1+||b-u||_1)`.

**Exact distance-five shell:** Among all **2,305** distinct two-key replacements with matched distance **exactly 5**, precisely **473** cover all 24 labels and **1,832** fail necessary coverage. An exhaustive exact original signed-native prefix tree dynamic program computes the 473 optimal costs; their minimum is **94**, reached in exactly one case. All 473 thus have optimum at least 94. The unique 94 case, index **162**, deletes `(5,3,1),(6,4,1)` and inserts `(5,5,1),(5,6,1)`. The two 96-cost cases are indices 373 and 458.

Together with EC49FLB's completed `d<=4` shell, all **4,042** two-key replacements with `d<=5` are classified: **883** coverable and **3,159** not coverable. The smallest feasible cost in this combined neighborhood is **84** at the unique EC49FLB distance-four case; the EC49FKX original witness supplies the separate 84-prefix baseline. The global unrestricted seven-key question remains open with `C_min(7)<=84`.

## Complete finite enumeration

`MAKE_EC49FLC.py` imports the existing frozen enumerator `../EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py` and recomputes for every lawful word its exact demand label, full raw key, and sequence of literal ordered **signed** six-axis microsteps. Every pair of deleted keys and every unordered pair of added keys is visited once; both matchings are checked; bitwise union of the demand-coverage masks decides feasibility. The deterministic case order is `(number of signed first-step roots, deleted pair, added pair)`. Among the 473 feasible cases, 210 have 3 signed native first-step roots and 263 have 4. `COSTS_EC49FLC.json` stores all 473 optima in this exact order.

## Exact optimization proof and evidence

For a fixed first signed microstep, form the trie whose nodes are literal nonempty signed-X6 microstep prefixes of all legal candidate words with an allowed full raw key. The subset-mask DP at node v stores the minimum number of selected native prefixes covering an exact subset of available labels. The child combination is min-plus convolution over bitwise OR; using a nonempty mask at a nonempty node adds one edge/prefix. Convert exact masks to superset-cover minima. Enumerate all 24-demand assignments to signed first-step roots capable of supplying their labels and minimize the sum of the disjoint-root costs. Every lawful 24-word cover induces such an assignment; conversely the computed root subsolutions yield lawful words and the charged union of raw prefixes. This is an exact finite optimization, with no displacement-only quotient, floating point or approximate solver.

The **unchanged original EC49FKY C++17 solver** `../EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112/SCAN_7KEY_GENERAL.cpp` was compiled with `g++ -O3 -std=c++17` and executed for all cases: 0–209 in one completed run, and 210–472 in eleven completed consecutive batches. `COSTS_EC49FLC.json` and `EXACT_SUMMARY_EC49FLC.json` retain the full cost array and histogram.

An independent Python standard-library checker `VERIFY_EC49FLC_INDEPENDENT.py` rebuilt the frozen catalogue and byte-prefix tries, with separate mask-DP code; it was actually executed at indices **0,15,162,210,373,458,472**, including the unique minimum and two 96-cost minima, and agreed exactly with all seven C++ results. Independent Python coverage is 7 selected cases; exhaustive C++ coverage is 473 cases.

**Exact cost histogram:** `94:1 96:2 98:31 102:2 104:79 106:25 108:21 112:179 114:2 116:39 118:4 120:2 121:3 122:1 124:15 125:1 126:3 128:1 129:1 132:1 133:6 134:2 137:7 138:7 139:1 140:2 141:3 142:3 143:1 145:2 146:12 148:1 149:3 151:1 155:1 156:2 157:3 169:2 174:1`.

## Reproduce / next

Run `python MAKE_EC49FLC.py` to generate the deterministic indexed inputs; compile the referenced unchanged C++17 solver, run it on `EC49FLC_CASES.txt`, and match all 473 integer costs against `COSTS_EC49FLC.json`. Then run `python VERIFY_EC49FLC_INDEPENDENT.py` for the independently executed selected checks.

Next: enumerate/test matched-distance 6 and more distant two-key sets for a genuine 83-prefix-or-better witness, or derive exact local lower bounds. Preserve the frozen scientific pin and full path/key identity. This is author-side GitHub research evidence; formal Source CLAIM/Result and independent Driver audit retain their own authority.
