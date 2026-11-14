# EC49FEX — Universal integer prefix dual excludes the full H6-mixed 23-path BRC family

Date: 2026-11-09 (Asia/Shanghai). Result status: **author finite exact proof**, pending independent Driver review. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This extends the same currently proven native grammar and pooled-key exact certificate method used by EC49FEV and EC49FEW. No changes to P000/ACTIVE Heartbeat World ontology or frozen science.

## Mathematical statement

Use the original six-operation alphabet `a,c,d,e,f,g`, ordered signed X6 microsteps, nine-state observation automaton, full *positive forward* BRC keys `(x,y,z)`, native endpoint `(+2,0,0,0,0,0)`, and at most five distinct complete keys. The 23-word signature requirements are H2 low `(1,2,4,8)`, H3 high `(16,32)`, H6 mixed type B `(1,8,16)`, and exactly three other late horizons high `(16,32)`; all remaining horizons low `(1,2,4,8)`. Different labels at one horizon may use distinct keys. `C_native` counts distinct nonempty **ordered signed microstep prefixes** of all 23 words.

**Theorem:** For *every* signature-feasible original type-B full-five-key configuration in this H6-mixed branch, `C_native >= 98`. By the existing exact operation/key involution `I=(c d)(f g)`, `J(x,y,z)=(y+2z,x-2z,z)`, the same exclusions hold for the mirror type C `(2,4,32)`. The type-B configuration census contains 42,192 inventories, of which 18,426 are signature-feasible and 23,766 are signature-infeasible. The typed C mirror has the same census (typed branches need not identify disjoint untyped inventories).

| Four late high-bearing horizons | Signature-feasible type B configurations | Exact certified lower bound | Words in pooled relaxation |
| --- | ---: | ---: | ---: |
| 4569 | 288 | 123 | 78,332 |
| 4679 | 2,142 | 98 | 72,894 |
| 4689 | 1,692 | 99 | 48,074 |
| 5679 | 5,184 | 101 | 72,262 |
| 5689 | 4,320 | 103 | 47,654 |
| 6789 | 4,800 | 102 | 31,096 |
| **Total** | **18,426** | **>=98** | **350,312** |

The four other four-high subsets have zero original signature-feasible configurations in EC49FEU's verified complete H6-mixed census; all ten placements are accounted for.

## Exact lower-bound proof

For a signature set `A`, let `K_h(A)` mean every original complete positive BRC key which can emit all signatures in A at horizon h. For a feasible four-element late-high set `S` containing 6 and 9, define the **pooled superset**

`K_pool(S) = {(3,1,1)} ∪ K_6({16}) ∪ ⋃_{h∈S\{6}} K_h({16,32}).`

The original five-key inventories are contained in this pool. Allowing every required group to select a word using *any* pooled key can only relax the cost minimization and hence yields a valid lower bound for the original problem.

There are exactly 23 required `(h,signature)` groups. Let `W_g` be all original signed words with correct native X6 endpoint, horizon, observer and pooled key for group g; `P(w)` is its set of nonempty *ordered signed* microstep prefixes. For each feasible set S, the archive supplies a finite nonnegative integer coefficient array `T_(g,p)`, positive scale `Q=1,000,000`, and 23 nonnegative integers `gamma_g` with:

1. For every exact signed native prefix p: `sum_g T_(g,p) <= Q`.
2. For every w in `W_g`: `sum_(p in P(w)) T_(g,p) >= gamma_g`.
3. `sum_g gamma_g / Q` equals the integer bound in the table.

Summing one required word from each group yields exactly:

`Q*C_native >= sum_(p in union_g P(w_g))sum_g T_(g,p) >= sum_g gamma_g`.

This is an exact finite certificate, not a numerical inference from LP optimality. The coefficient finder uses SciPy/HiGHS merely to locate candidates; the standard-library independent verifier re-enumerates all original words, exact signed X6 endpoints, positive full BRC keys, original nine-state labels, ordered signed prefixes, every word inequality and every per-prefix capacity using Python integers. All six returned `EXACT_INTEGER_PASS`.

The six pools contain 350,312 candidate original operation words and 2,021,651 group/prefix constraints, with 1,552,962 nonzero exact integer coefficients. Counts sum separate branches and may overlap across them.

## Reproduction and evidence

Run from extracted evidence directory:

`python3 VERIFY_EC49FEX.py UNIVERSAL_H6_4569.json UNIVERSAL_H6_4679.json UNIVERSAL_H6_4689.json UNIVERSAL_H6_5679.json UNIVERSAL_H6_5689.json UNIVERSAL_H6_6789.json`

`EC49FEX_VERIFICATION.jsonl` records actual six PASS outputs. Regenerate a certificate (optional, SciPy available): `OPENBLAS_NUM_THREADS=1 python3 late_mixed_dual.py 6 4569 .` and analogously for the other five sets. The complete archive contains all six full unrounded integer coefficient JSON files, actual verification records, source, scientific word-model dependencies, proof and report. Archive is split into numbered plain UTF-8 Base64 parts for GitHub transport, concatenate in order then Base64 decode, decompress tar.xz. GitHub readback of all parts is required before claiming remote preservation.

## Scientific frontier

The full H6 mixed type B/C 23-path family is excluded under the mother target `C_native <=93`, with stronger finite bound 98. Combined with earlier H4 (≥101) and H5 (≥98) complete mixed branches, the next distinct unresolved unit is H7 and H8 mixed placement exact pooled-key certificate (20,568 and 26,652 original signature-feasible typed-B configurations respectively). The existing 22-path 94-edge witness remains the better recorded upper bound for the mother target. A finite proved branch obstruction does not settle other valid input families.

## Identity / publication

Author: current native issued `EM-DIRECT-4FB3A8 / TASK_RESEARCH`; activity Source-persisted `RA-9854AC2E5AA8BFD1F95D7C37`. Current `execution_authorized=false`, no authenticated CLAIM, native Result or independent Driver mathematical admission asserted. GitHub artifact publication remains an author-side evidence contribution. No new user approval is inferred or requested.