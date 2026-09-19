# P000 Q30 n=14 evidence recovery canonicalization gate — research return

Task: `RS-P000-Q30-N14-EVIDENCE-RECOVERY-CANONICALIZATION-GATE`  
Publication: `TP2-EB531E351C670702AD82`  
Researcher-ID: `EM-P000Q30REC-EE3C71`  
Claim: `CLM-P000Q30REC-C26BDE35D40D7AF8`  
Execution: `ER-58E795301A50DB6D3150`

## Terminal research finding

`Q30_N14_EXACT_EVIDENCE_RECOVERED_AND_REPLAY_VALIDATED`.

The immutable source package at `b90378c332e0dbf80aad0c09d363047abb2ee2f3` is recoverable under the frozen observable
`FROZEN_Q22_Q25_Q27_Q28_Q29_PRIMITIVE_RETURN_PROFILE_INITIALIZED_ORDINARY_1WL_UNCHANGED`.
No strengthened observer was used.

The recovered bounded statement is exactly the old terminal classification:
`RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N14`.
This is an `n <= 14` finite-prefix result only; it makes no claim for `n >= 15`.

## BRC execution

### Bound

The task was held to the fixed `n=14` evidence-recovery gate. The current execution did not restart the census, did not enter `n=15`, and did not introduce 2-WL, spectra, zeta, full cycle incidence or canonical labels. Exact packet equality remains the mathematical equality key; hashes are integrity pins only.

### Reduction

The old certificate reduces every graph in sector `r` by suppressing maximal degree-2 paths to a connected cubic multigraph kernel while retaining loops and parallel edges. Exact expansions restore `14-r` degree-2 vertices. Completeness is certified sectorwise by the automorphism-weighted orbit identity

`sum_G r!(14-r)! / |Aut(G)| = C_conn(3^r,2^(14-r))`,

where the right side is an independently evaluated connected labeled degree-state count on a fixed degree partition.

The current execution independently reimplemented the degree-sequence simple-graph recurrence and the connected-component subtraction recurrence locally and recomputed all seven right-hand sides from scratch. It then recomputed every orbit sum from the persisted automorphism histograms.

| r | representatives | exact packets | kernel types | orbit sum | independent connected degree-state count |
|---:|---:|---:|---:|---:|---:|
| 2 | 43 | 43 | 2 | 12,414,124,800 | 12,414,124,800 |
| 4 | 931 | 931 | 5 | 38,690,265,600 | 38,690,265,600 |
| 6 | 6,879 | 6,879 | 17 | 120,607,023,600 | 120,607,023,600 |
| 8 | 19,587 | 19,587 | 59 | 393,165,964,800 | 393,165,964,800 |
| 10 | 21,434 | 21,434 | 197 | 1,358,543,793,600 | 1,358,543,793,600 |
| 12 | 7,589 | 7,589 | 478 | 4,991,840,330,400 | 4,991,840,330,400 |
| 14 | 509 | 509 | 509 | 19,491,385,914,000 | 19,491,385,914,000 |

Global totals recompute to `1,267` kernel types, `56,972` representatives, `56,972` exact stable packets and `26,406,647,416,800` normalized connected labeled realizations. The recovered exact package records `0` nonisomorphic equal-packet collision fibers.

### Certification

The stale V2 certificate pointer `P000_Q30_N14_KERNELS_R14_V1.json` is classified as `SUPERSEDED`, not as a mathematical gap. At the same immutable old head, the later replacement package consists of five r=14 reconstruction shards with counts `105+105+105+105+89=509`, the replay supplement `P000_Q30_N14_R14_RECONSTRUCTION_REPLAY_SUPPLEMENT_V1.json`, and the executable checker `P000_Q30_N14_R14_RECONSTRUCTION_REPLAY_CHECK_20260905.py`.

The pinned r=14 checker explicitly decodes all 509 cubic graphs, checks connected simple cubic structure, recomputes primitive simple-cycle multiplicity profiles, runs the unchanged ordinary 1-WL packet construction, tests exact semantic packet equality, computes exact automorphism orders, independently computes the connected labeled cubic count, and checks the orbit cover. Its persisted replay certificate is `509` representatives / `509` exact packets / `0` collisions / orbit sum `19,491,385,914,000`, matching the independently recomputed cubic count in this execution.

The five replacement shard Git blobs, file SHA-256 values, combined kernel-code digest and packet-image digest are frozen in the current replay artifact. They are used only for immutable evidence identity/integrity; the mathematical identity test remains exact packet equality.

## Local validation performed in this execution

The current checker `research_checks/P000_Q30_N14_EVIDENCE_RECOVERY_REPLAY_CHECK_20260917.py` was executed locally. It independently evaluates the simple-degree-state recurrence and connected recurrence for every sector, recomputes every orbit sum from the persisted exact automorphism histograms, verifies representative/packet counts and global totals, and reconciles the five-shard r=14 replacement package.

Observed terminal output was a clean `PASS`; independently computed connected counts were exactly:

`r=2: 12414124800; r=4: 38690265600; r=6: 120607023600; r=8: 393165964800; r=10: 1358543793600; r=12: 4991840330400; r=14: 19491385914000`.

This gate does not pretend to be a new graph-level enumeration. The exact packet-level computation is recovered from the immutable executable source package and its pinned shards; the current execution supplies a fresh independent arithmetic/coverage replay plus provenance reconciliation. This is sufficient for the evidence-recovery/canonicalization question posed by this task and does not grant mathematical acceptance beyond the Result record pending Driver review.

## Provenance reconciliation

Primary old certificate Git blob: `9ed536a327dda4d9d6e3a21d31bb90383bf7ddc9` at source commit `b90378c332e0dbf80aad0c09d363047abb2ee2f3`.

Compact-sector Git blobs read at that immutable source pin:
- r=2 `8dd7c3515fbe78dc1e2971f0a620107520b52e37`
- r=4 `85eb41faa1e68e6edb178b4e77de93fecda9c817`
- r=6 `90969415f5511ff88509c28722efab06237e91f7`
- r=8 `d254da2c883d5efa2fce5f9779c2a21b57cf4d22`
- r=10 `94d6001f5c557586f41d88eab746728f4b4d7d0f`
- r=12 `730a8b7d30553310cbd221a9a7fcb3052f21ee3b`

r=14 replay supplement Git blob: `78c162e4e8d4103ac6fa2bd983153c640de1ced7`; replay-checker Git blob: `340777fbaa9b60a860bc3e1e536692f16f162bc7`.

The later open recovery PR `#1366` was consumed only as additional continuity/reproducibility evidence. It independently reached the same seven sector sums/global totals and the same `SUPERSEDED` classification for the stale monolithic r=14 pointer. It is not treated as Driver acceptance of this gate.

## Boundary and residue

No unresolved mismatch or provenance gap remains inside the stated `n=14` recovery gate. The first collision question for `n>=15` remains entirely outside this task. No Working Truth, Foundation, L4, canonical promotion, novelty, universal reconstruction theorem or canonical-label theorem is asserted here.

Next control action: independent Driver review of this Result at bounded strength. Researcher self-review must not mark the task accepted or complete the parent program.
