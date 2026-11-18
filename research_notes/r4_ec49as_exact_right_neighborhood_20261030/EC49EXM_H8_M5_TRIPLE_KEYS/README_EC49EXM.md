# EC49EXM — H8 / five complete BRC keys: exact triple-collision assignment theorem

2026-11-03 · Author-side portable mathematics · Parent EC49EXL (8257acd0473a1a80a39453e571b131f79c09e8d6) · Draft PR #1730

**Scientific source pins (unchanged):** GLOBAL_KNOWLEDGE_V1 `773d538180bfb49e24cffeb35c3ee75eb0628e2e`; Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current behavioral rules were read separately from canonical main. P000 and ACTIVE worldview were not modified.

## Exact statement

For the signed native-X6 seven-operation model and horizons h=2,...,8, each horizon has Q-rank 9 in the nine-history/five-observation incidence matrix and exactly one full positive symbolic BRC key K=(u,v,w,0,0,0). Exactly five distinct keys are used globally, and all observations come from the six EC49EXL signature types T2/T4. Restrict to the equality shape of one key occurring on exactly three horizons and the other four keys each occurring once.

**Theorem 1 (complete finite assignment count).** There are exactly eight realizable threefold equality skeletons, with **123,147 distinct labeled full-key assignments** in total. Here a full-key assignment specifies K at each of the seven horizons; equality at exactly those horizons prescribed by its skeleton is required. The eight triple blocks, their admissible common-key counts and injective full-key assignment counts are:

| triple horizons | candidate common keys | distinct full-key assignments |
|---|---:|---:|
| 3,4,5 | 1 | 71,799 |
| 4,5,6 | 3 | 23,502 |
| 4,5,7 | 1 | 4,983 |
| 4,6,7 | 1 | 2,905 |
| 5,6,7 | 7 | 10,158 |
| 5,6,8 | 3 | 3,015 |
| 5,7,8 | 3 | 1,917 |
| 6,7,8 | 13 | 4,868 |
| **total** | — | **123,147** |

The candidate common keys are explicitly printed by `VERIFY_EC49EXM.py` and stored in the complete original executed JSON evidence. The h=2 key (3,1,1,0,0,0) cannot be common to any triple of horizons.

**Theorem 2 (one-way T4/T2 type law for a fixed key).** For the same fixed K at increasing admissible horizons, write r_h=u+v-h-1. Then r_h decreases strictly by one per horizon. Rank-9 eligible occurrences have type T4 when r_h>=1, and may have type T2 only if r_h=0, f_h>=1 and g_h>=1. Consequently a repeated key's occurrence types are all T4 except possibly its last occurrence, which may be T2; after a T2 occurrence that key has no later admissible occurrence. Any triple block therefore requires T4 at the first two horizons in that block.

## Analytic reduction and finite certificate

Native signed-X6 return requires count(b)=0 and count(e)=count(a)+1. Let w=count(e), r=count(c)+count(d). The complete symbolic key is (u,v,w,0,0,0), with
`r=u+v-h-1; count(a)=w-1; f=h+1-v-2w; g=h+1-u`.
For h in 2,...,8, EC49EXL directly checked **all 411,368** legal returning operation words, their complete keys and exact nine-history rational ranks, proving the finite eligibility criterion
`r>=1 (T4)` or `r=0 and f>=1 and g>=1 (T2)`.
Its rank-eligible key set sizes at horizons 2,...,8 are 1,4,9,17,28,43,62. This proof reuses that verified finite criterion (it does not rerun the native-word rank audit).

Enumerate every restricted-growth-string partition of the seven labeled horizons into five blocks (140=S(7,5)). For a block B, define the complete-key candidate set C_B as the intersection of the eligible key sets of its horizons. Only partitions with a triple block are considered. The count for each partition is the number of injective maps from its five labeled blocks to the union of the five candidate sets, with block B mapped inside C_B. Positive counts occur exactly for the eight triples above.

Two actually executed exact-integer algorithms agree on each of the eight counts: a Python DFS assigns each block a yet-unused key, and an independent Node.js key-first 5-bit subset DP. In the DP, D_k[m] counts assignments of the first k complete keys to the occupied subset m of the five blocks. For each next full key, either skip it, or assign it to one still-empty eligible block j, performing D_(k+1)[m|(1<<j)] += D_k[m]. Initial D_0[0]=1 and final D_N[31] gives the injective count. The two algorithms independently output 123147 and PASS.

Theorem 2 follows algebraically since r_h=u+v-h-1 and r_h>=0 is necessary for return. Once r_h=0 any larger h has r<0, precluding a legal word with that K.

## Reproduction and research frontier

Reproduce using `python3 VERIFY_EC49EXM.py > EC49EXM_EXECUTED.json` and `node VERIFY_EC49EXM_INDEPENDENT.js > EC49EXM_INDEPENDENT_EXECUTED.json` (standard library / built-in integer arithmetic). The independent JS checker is committed here; original Python checker, two actual outputs, all eight triples and SHA256 inventory are in the provided complete author evidence archive.

**Scope of the increment:** 123147 is the exact count of full-key assignments across the eight triple-block shapes, not the number of native operation-word selections and not an E-cost optimum. The global five-key / six-signature H8 optimum remains between the previously established E=63 lower and E=80 witness upper bound. Native signed-primitive-prefix OR-mask optimization of the triple-key assignments and the 32 two-pair skeletons is the next scientific question; see NEXT_EC49EXN.md.

**Authority:** Github author-side artifact only. Native owner/CLAIM/Result/independent Driver review not established; no mathematical admission implied.
