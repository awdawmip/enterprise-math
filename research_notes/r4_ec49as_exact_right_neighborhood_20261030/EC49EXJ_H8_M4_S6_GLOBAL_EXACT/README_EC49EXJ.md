# EC49EXJ — Exact global H8 / M=4 / S<=6 signed-native BRC cost theorem

**Research date:** 2026-11-03, Asia/Shanghai. **Status:** `AUTHOR_FINITE_EXHAUSTIVE_PROOF / INTEGER_DP_PASS / INDEPENDENT_FAMILY_COUNT_PASS / EXACT_WITNESS_RANK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`.

**Parent:** EC49EXI, Draft PR #1730, earlier head `8c81ed682aa47a8714ed7ef5b6ad931f9f97e4a1`. **Frozen scientific input pins:** GLOBAL_KNOWLEDGE_V1 `773d538180bfb49e24cffeb35c3ee75eb0628e2e`; Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current behavioral context read separately on 2026-11-03 at global canonical main `fdb1f9982861a4065b492bb4342edbf07932ad1f`, Enterprise Math canonical main `e15cb849720aaf5388cc252ad47c14eaa015cbe8`. P000 and ACTIVE Heartbeat worldview unchanged. Research-activity / native-Owner authorization remains separate from scientific-storage publication.

## Model, precise statement

Use the exact seven-operation symbolic paired-BRC/native-X6 model of EC49EXF–EC49EXI:

- Ordered signed *primitive* native-axis paths: `a=(-1,-1)`, `b=(-2,-2)`, `c=(+1,+2,-1,-2)`, `d=(+2,+1,-2,-1)`, `e=(+3,+1,+1,-3)`, `f=(+1,-1)`, `g=(+2,-2)`. Entries are signed axis indices, not 2-D Euclidean coordinates; the displayed example stays in the E1–E3 support of the native six-axis world.
- At each integer horizon `h=2,...,8`, choose h-letter *operation* words returning full signed six-axis displacement `(2,0,0,0,0,0)`, with all words in that horizon sharing one complete six-axis **positive primitive-step count** key `p_h`. Each horizon's nine frozen seam-history observers must span rank nine over Q.
- Keep two separately indexed strictly-positive symbolic BRC factor channels `(X_p,Y_p)=(prod_i x_i^p_i,prod_i y_i^p_i)` and retain complete ordered primitive paths and observer signatures. Let `E` count distinct nonempty *primitive-step* prefixes across every selected word, `M` the number of globally distinct full keys, and `S` the number of distinct nine-history-to-five-bucket transfer signatures. These symbolic factors are not a physical time/phase simulation.

**Theorem EC49EXJ-1 (unrestricted global optimum in the frozen finite model).**

\[
\boxed{\min\{E\mid H=8,\ M=4,\ S\le 6\}=90.}
\]

The equality is global across *all* legal eight-horizon words, BRC key arrangements and observation family choices within this exact model; no specific key schedule or T4/T2 pattern is fixed in advance.

## Complete finite reduction

The previously proved EC49EXI exact finite family theorem partitions all **55,493** full-rank `H8/M4/S<=6` key+observer-family schedules (14,092 eligible four-key sets) by time of first use of key four. At h2 the four `T4` signatures are necessary and cost 28 primitive prefixes. Every later full-rank key fiber has one unique inclusion-minimal observer family: `T4` of four signatures or `T2` of two; there are no other minimal full-rank families in the frozen 411,368 returning-word universe. Omitting extra nonrequired words cannot increase minimum coverage cost. Let `k_h=4` for `T4`, `k_h=2` for `T2`.

For the **28,560** schedules introducing the fourth key only at h8, EC49EXI proved `E>=90` by `E7>=86` (the exact H7/M3/S<=6 theorem EC49EV) and the independent eighth-horizon terminal-prefix lower bound `+2 k8`.

The remaining **26,933** schedules have all four keys present by h7. For a fixed schedule prefix up to horizon j, let `F_j` be the exact *minimum* total nonempty primitive-prefix cost needed to realize its specified T4/T2 mandatory signatures. The exact values for j=5,6 are obtained by a finite connected-prefix-tree integer subset-OR dynamic program; the j=7 and j=8 pass may use a rigorous cutoff. The terminal-edge lemma of EC49EXD/EC49EXI gives `E_{h}-E_{h-1}>=2 k_h` for each subsequent h=6,7,8, **regardless of the earlier chosen words and BRC keys**. Consequently every schedule satisfies:

\[
E_8\ge F_5+2(k_6+k_7+k_8),\quad
E_8\ge F_6+2(k_7+k_8),\quad
E_8\ge F_7+2k_8.
\]

Exactly evaluated subcases, with no overlap:

| Step | Exact predecessor computation / certificate | Excluded from `E<90` | Remaining |
| --- | --- | ---: | ---: |
| EC49EXI prior first-use-at-h8 theorem | `E7>=86`, then `+2k8` | 28,560 | 26,933 |
| New H5 screen | 304 distinct H2–H5 typed key-prefixes; exact `F5` and terminal bounds h6..8 | 22,804 | 4,129 |
| New H6 screen | 554 distinct H2–H6 typed key-prefixes; exact `F6` and terminal bounds h7..8 | 3,593 | 536 |
| New H7 screen | 536 exact OR-mask predecessor instances, accepting only solutions with `F7<86`; 528 certify `F7+2k8>=90` | 528 | 8 |
| Final H8 exact bounded DP | All eight residual 20-color trie instances are infeasible below `E=90` | 8 | **0** |

The eight final cases have `F7=84`, `k8=2`, so the generic last-horizon lower bound alone is 88. Direct full eight-horizon DP discharges precisely these eight cases; 2, 6 of the final inputs have 4,098 and 7,256 trie nodes respectively, each with exactly 20 terminal colors. For all eight, the executable integer kernel returns `BOUND_PASS minimum_total_at_least=90`. Thus the lower bound holds for all 55,493 schedules.

### Why the DP and cutoffs are exact

For a fixed typed schedule, enumerate every legal operation word with the schedule's full six-component positive key and one of its required T4/T2 signatures. Expand every candidate word to the *full ordered signed primitive-axis path*; put all candidates into a rooted trie with terminal bit colors encoding the required `(h,signature)` pairs. The h2 mandatory core `ce,de,ec,ed` is prepaid at **28** edges. At each trie node the finite DP stores the least number of unprepaid edges needed for each exact union mask. Combining child masks uses bitwise OR, sums their nonnegative integer costs, and charges each active nonprepaid incoming edge exactly once. Induction from leaves proves this DP optimizes over *all* possible selected word subsets.

The bounded implementation discards a state whose paid-extra cost is already `>= cutoff_total - 28`; every remaining edge charge is nonnegative, so any completion of that state also exceeds the cutoff. A root result `BOUND_PASS minimum_total_at_least=T` therefore proves there is no solution with total edge cost `<T`. This is a finite integer certificate, not an approximate or floating-point optimizer. H5/H6 compute actual exact values; H7 cuts at total 86, and final H8 at total 90. All 536 H7 instances were solved; 528 have `F7>=86` while eight have exact `F7=84`.

### Attainment and independent observation check

The earlier EC49EXH explicit native word witness achieves E=90, M=4, S=6:

```
h2: ce de ec ed
h3: feg gef
h4: fegd gefd gefc fegc
h5: fegfg geffg
h6: geffgd geffgc fegfgd fegfgc
h7: fegfgfg geffgfg
h8: fegfgfgg geffgfgg
```

The independent exact `fractions.Fraction` rank routine confirms rank 9 for each horizon, with respective cumulative primitive-prefix costs **28,42,58,64,80,86,90**, exactly four complete six-axis positive BRC keys and six transfer signatures. The JavaScript independent family-key enumerator reproduces 14,092/55,493/28,560/26,933 families from the operation occurrence equation, and an independent analytical scan reproduces all 923 all-T4-through-h7 schedules already contained in the new partition. These replicate a separate part of the proof rather than claiming independent Driver review.

## Reproducible source and evidence

Same-folder sources: `ANALYTIC_EC49EXJ.py`, `SCREEN_H5_EC49EXJ.py`, `SCREEN_H6_EC49EXJ.py`, `SCREEN_H7_EC49EXJ.py`, `FINAL_EC49EXJ.py`, `EXACT_OR_MASK_DP.cpp`, and `VERIFY_EC49EXJ_INDEPENDENT.js`. Local execution: `python ANALYTIC_EC49EXJ.py; python SCREEN_H5_EC49EXJ.py; python SCREEN_H6_EC49EXJ.py; python SCREEN_H7_EC49EXJ.py; python FINAL_EC49EXJ.py; node VERIFY_EC49EXJ_INDEPENDENT.js`. Python 3.10+, Node.js and C++17 compiler required for complete numerical replay; the proof statement can be read without a particular execution environment. Preserve the source tree together, as the scripts import their siblings.

`EC49EXJ_ANALYTIC_EXECUTED.json` and `EC49EXJ_COMPLETE_EXECUTED.json` contain small direct outputs and the eight final cases. `EC49EXJ_ALL_STAGE_DATA.json.gz.b64` is a **complete lossless UTF-8 JSON/Gzip/Base64 archive of the full per-prefix stage results** (H5=304, H6=554, H7=536 cases) plus source-independent summary; decode by `base64 -d | gzip -d > EC49EXJ_ALL_STAGE_DATA.json` or a standard base64/gzip reader. The total stage counts and each instance's `key_family`, node count, eligible words, exact/bounded DP output are preserved. `SHA256SUMS_EC49EXJ.txt` records SHA256 of local original files; the separately gzipped data's SHA is recorded to distinguish the archive representation. The full report is not an empty placeholder.

All statements concern the frozen finite native path/observer/BRC model. Source publication is scientific storage; no native CLAIM/Result, Owner authorization, independent Driver review or Foundation promotion is implied. The missing control authority must be handled through the canonical native router without borrowing another writer's identity. **Next research unit EC49EXK:** reuse EC49EXJ as the strict H8/M4/S6 point; investigate H8/M5/S6 exact cost and the pending H8/M3/S4 144-edge integer certificate, then build the H8 non-dominated frontier, with independent review as a separate work item.
