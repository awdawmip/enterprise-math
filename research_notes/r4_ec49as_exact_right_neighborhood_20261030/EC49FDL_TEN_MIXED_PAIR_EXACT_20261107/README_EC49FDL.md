# EC49FDL — 10 exact mixed-key five-key families and 94-edge mother-witness audit

Date: 2026-11-07. Frozen scientific input: \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`.
Status: **AUTHOR EXACT FINITE OPTIMIZATION / EXECUTED / UNREVIEWED / NOT ADMITTED**.
Predecessor: EC49FDK at PR #1730, commit \`4f0f9e69c4b9586c94cb99700cca78296a174871\`. Retain P000, ACTIVE Heartbeat World and the full signed native X6 model.

## New finite theorem

Fix H2/H3's four paths \`fe,ge,feg,gef\` (16 distinct signed primitive-prefix edges; three distinct complete positive keys). Fix an unordered pair (L,M) of two **additional full positive BRC keys**. At each of H4,...,H9 permit *every* displacement-valid ordered seven-operation word whose full six-component key is **either L or M**, allowing mixtures of the two keys *within one horizon*. Filter by the original nine-state observer and its six allowed signatures. Require rational rank nine separately for each horizon. Let C(L,M) be the minimum distinct nonempty **ordered signed-X6 primitive prefixes** among all selected words across the eight horizons.

For the following ten pairs, complete integer mixed-key optimization gives:

| Pair index in EC49FDJ | L | M | C(L,M) | Eligible words | Primitive Trie nodes |
|---|---|---|---:|---:|---:|
| 8 | (5,3,1) | (3,7,1) | 169 | 784 | 5,123 |
| 108 | (5,3,1) | (9,1,1) | 169 | 784 | 5,123 |
| 17 | (4,3,1) | (4,6,1) | 136 | 1,300 | 8,117 |
| 68 | (5,2,1) | (8,2,1) | 136 | 1,300 | 8,117 |
| 123 | (5,3,1) | (9,7,1) | 192 | 1,632 | 15,419 |
| 40 | (5,3,1) | (4,6,1) | 150 | 1,714 | 10,659 |
| 96 | (5,3,1) | (8,2,1) | 150 | 1,714 | 10,659 |
| 1 | (3,3,1) | (5,5,1) | 130 | 3,128 | 19,963 |
| 45 | (5,1,1) | (7,3,1) | 130 | 3,128 | 19,963 |
| 11 | (4,2,1) | (6,4,1) | 112 | 4,382 | 26,743 |

The scope is **10 specified pairs out of 124** exact rank-nine-feasible pairs from EC49FAW/FDJ. The first nine include nine small languages; case 11 independently reproduces the prior 112-edge pair bound with H5 mixture permitted. None of these ten produces a <=93-edge completion with this fixed H2/H3 seed.

## Exact finite argument and actual checks

Every displacement-valid length-h word with key (x,y,z) must have \`#a=z-1, #e=z, #c+#d=x+y-h-1, #f=h+1-y-2z, #g=h+1-x\`. Exhaustively enumerate each permitted ordered multiset permutation, split c/d multiplicity in every way, execute the original nine-state DFA and retain all six legal transfer signatures.

Build one Trie over the *literal ordered signed primitive steps* of **all** selected-key candidate words, not over operation symbols or endpoint coordinates. For every non-root Trie node v define a binary edge-selection variable t_v. Require t_v <= t_parent(v) for every non-root parent. The 16 fixed seed-prefix edges have zero incremental objective; all other selected primitive-prefix edges cost 1. For each h=4,...,9, impose four terminal-coverage clauses corresponding to \`(E or F), (C or F), (D or G), (J or G)\` (EC49FAR: exactly equivalent to rank nine for the six observer signatures). Minimize incremental primitive edges and add the prepaid 16.

**Equivalence proof:** Any allowed set of paths yields an ancestor-closed feasible binary Trie selection of equal cost. Conversely, every feasible binary Trie selection contains at least one legal candidate terminal for each required rank clause, whose ancestor prefixes are included, yielding a legal path system with cost no greater than the MILP objective. Integer optimum equals C(L,M) for the exact selected pair.

Actual local execution: Python 3 / SciPy 1.17 / HiGHS 0–1 \`milp\`. **All ten jobs terminated status 0/OPTIMAL, MIP gap 0**, with matching explicit integer witnesses. A fresh stand-alone portable reproducer \`REPLAY_EC49FDL_PORTABLE.py\` was executed on all ten pairs; its internal second checker rebuilds signed primitive words, full six-component keys, the nine original initial-state observation vectors and rational rank using \`fractions.Fraction\`, and recomputes the exact union of primitive prefixes. These ten witnesses all have five distinct complete keys and at most six observer signatures. Output: \`PORTABLE_REPLAY_10.jsonl\` at the original local research executor; SHA-256 \`7d9236a5540e436ecc9af47a7a6c49d083b7767b979adf1a08ded6eb1223da92\`. Source SHA-256: \`cfbd4edf2fc8e4fd1fc8ba5c393b8a6d4011d5a3ddc6fb0012ee345a3c05f848\`. The program prints all explicit selected words to regenerate the witness list directly.

The finite optimum uses HiGHS integer-optimality evidence, an explicit matching integer witness, model-equivalence proof and separate observer/prefix checks; it is not a separately formalized unsat certificate or independent Driver admission.

## 94-edge original-mother-witness audit

Independently rebuilt the four existing EC49FAJ witnesses (source ranks 1512,1513,2200,2203) from the frozen seven-operation literal step expansion. All four passed six-axis displacement, full positive five-key count, at most six global transfer signatures, **rational rank nine on each H2..H9** and native prefix census: cumulative costs \`28,42,58,64,68,72,88,94\` (first two), and \`28,42,46,62,68,72,88,94\` (other two). **Their H2 seed is \`de,ed,ce,ec\` (28 edges), not the fixed \`fe,ge\` seed** of the above ten finite families. Thus the 94-edge baseline and the ten mixed-key lower bounds concern different H2/H3 source families.

## Next discriminating scientific unit EC49FDM

Optimize additional rank-nine-feasible pair families **under intra-horizon mixtures** (114 remain), prioritize pairs by observed lower-bound potential and branch/primitive overlap rather than candidate-word count alone. A second route is to permit different lawful H2/H3 seed families, using the four 94-edge witnesses as test input; attempt an explicit five-key <=93-edge system, with complete signed paths and rational rank evidence. Source owner/CLAIM and Driver admission remain separate; native service returned \`BACKEND_IDENTITY_OR_VERSION_MISMATCH\` with \`operation_sent=false\` in this run.

## Files / reproduction

- \`REPLAY_EC49FDL_PORTABLE.py\` — self-contained enumerator, Trie MILP, and independent signed-X6 / Fraction-rank witness validator. \`OPENBLAS_NUM_THREADS=1 python REPLAY_EC49FDL_PORTABLE.py all\`.
- \`RESULTS_EC49FDL.json\` — ten checked exact optima, input scope, candidate counts, execution provenance and audit digests.
- Parent exact control and previous 186 uniform-horizon classifications remain unchanged. Original scientific source frozen at \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`.
