# EC49FAB — Four exact 76-edge signed-native X6/BRC witnesses; strict-cutoff census

**Author-side date:** 2026-11-04. **Mother problem:** frozen H8/M5/S≤6 native signed-six-axis path-prefix minimization. **Prior author frontier:** EC49FAA at `480ed27a8a56abfa428f46496c5ea33606846263` (Draft PR #1730). **Status:** `AUTHOR_EXPLICIT_CONSTRUCTION / INDEPENDENT_LOCAL_INTEGER_AND_MODULAR_RANK_CHECK_PASS / EXACT_INTEGER_DP_BATCH / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`.

## 1. Exact theorem FAB-1: a 76-edge feasible signed-native construction

Under the existing frozen seven-operation language with horizons `h=2,...,8`, exactly five full six-axis *positive-step* BRC cache keys, at most six distinct nine-history transfer signatures, rank-nine observation per horizon and cost `E` equal to the union of ordered **signed primitive** nonempty prefixes, there exist four explicitly enumerated feasible arrangements with **E=76**. Hence, for the existing mother problem,

\[\boxed{63\le E^*\le 76}.\]

The lower bound 63 is the prior source-bound lower theorem; the new upper bound is established **constructively** here. No claim of global optimality at 76 is made. The 76-edge constructions are also exactly optimal for their **fixed** cache arrangements under the frozen solver's exact integer OR-mask DP (zero improvement below 76).

Primitive operation expansion (six-axis coordinates, with axes 4–6 unchanged):

```
a = (-1,-1)                  b = (-2,-2) [unused]
c = (+1,+2,-1,-2)           d = (+2,+1,-2,-1)
e = (+3,+1,+1,-3)           f = (+1,-1)          g = (+2,-2)
```

For the first explicit witness (`rank=1512` within the immutable EXY source-ranked candidate list), the required selected operation words are:

| Horizon | Full BRC key `(u,v,w,0,0,0)` | Required selected operation words |
|---|---|---|
| h2 | (3,1,1,0,0,0) | `de ed ce ec` |
| h3 | (3,1,1,0,0,0) | `feg gef` |
| h4 | (4,2,1,0,0,0) | `defg edfg fegc gefc` |
| h5 | (4,2,1,0,0,0) | `fegfg geffg` |
| h6 | (4,3,1,0,0,0) | `fegfgg geffgg` |
| h7 | (4,4,1,0,0,0) | `fegfggg geffggg` |
| h8 | (4,5,1,0,0,0) | `fegfgggg geffgggg` |

The second witness (`1513`) uses the same h2–h5 words but extends with positive/negative axis-1 loop `f` instead of axis-2 `g` at h6–h8. A third and fourth pair (`2200,2203`) uses double-collision horizons (2,3) and (5,6), with explicit words in the independent checker and source JSON. Each is distinct as an arrangement.

**Verification law.** Expand each word to a signed axis-step tuple `s`. The positive histograms satisfy exactly the listed six-axis key; the signed displacement is `(2,0,0,0,0,0)`; each word has operation length h. The full nine-history observer's transfer signature is reconstructed from the 9 declared initial states, not guessed from the operation word. The four-signature horizons are h2 and h4 for cases 1512/1513; h2 and h5 for cases 2200/2203. The other horizons have two signatures. Their union has exactly six signatures. The resulting nine-row indicator observation matrix has full row rank **9 over F101**, which implies rank 9 over Q. The pre-paid h2 core paths `ce,de,ec,ed` contribute exactly 28 distinct nonempty signed prefixes. The cumulative union of selected prefixes is:

- `1512,1513`: (h2..h8) **28,42,58,64,68,72,76**;
- `2200,2203`: (h2..h8) **28,42,46,62,68,72,76**.

These claims can be independently checked by running `python3 VERIFY_EC49FAB_STANDALONE.py`; its only dependencies are Python's standard library. Exact generated witness JSON, the traceback solver and execution output are retained with the research materials. The standalone script reads only its own hardcoded words, reconstructs signs and observer signatures, and computes prefix unions and modular rank without importing the earlier word generator or optimizer.

## 2. Exact finite cutoff census: 1,506 new cases

Reused the published EXY 12,356-row double-collision classification and EXZ source-ranking, and the unchanged EC49EXJ native word generator and exact C++17 integer OR-mask prefix-tree optimizer. For **1,506 previously untouched distinct source-ranked arrangements** with `B_EXY<78`, use strict cutoff `E<78`:

| Exact local solver outcome | Arrangements | Mathematical implication |
| --- | ---: | --- |
| `BOUND_PASS minimum_total_at_least=78` | **1,492** | Fixed arrangements exclude E<78; therefore also E<76 |
| `PASS min_extra=48 total=76` | **4** | Exact fixed-arrangement minimum 76; independent explicit witnesses recovered |
| timeout at capped per-case execution | **10** | Open |
| **Total executed** | **1,506** | input hashes, exact source rows, solver stdout and timeouts recorded |

Execution ranges: ranked `[200,255)`, `[255,600)`, `[600,1200)` and `[1200,2310)`; the last run was interrupted after rank 2309, with durable per-case results retained. Within these ranges the exact recorded population is selected by the script: `B_EXY<78`, color count ≤22, excludes the 10 FAA ranks and the earlier EXZ first-200 cases. **Do not infer that excluded colors or later ranks were tested.** The 10 timed-out ranks were `272,273,387,517,914,915,950,951,1002,1003`. The four explicit successful ranks were `1512,1513,2200,2203`.

The solver uses a signed primitive-step trie with nonnegative exact integer edge costs. At a node, a state gives the minimum paid extra edges realizing an OR-mask of observer-color demands. Combining child subtrees preserves the OR-mask and adds a child-edge cost when selected and non-prepaid. Pruning entries of extra cost ≥50 (baseline 28 edges) is sound for strict `E<78`. Its `BOUND_PASS` proves nonexistence of a strict-improving selection in the fully generated fixed arrangement. A `PASS` cost is exact below the cutoff; all four successful arrangements yield 28+48=76. This is an **author-side finite computation**, not an external theorem admission.

**Accounting correction:** EC49FAA reported 7,900 unresolved arrangements for `E<78` after excluding 4,282 necessary-bound cases, 164 prior exact-negative cases and 10 FAA cases. Its count omitted the **two previous EXZ fixed arrangements exactly optimal at 78**: they are also excluded for strict improvement below 78. Therefore the correct prior unresolved count was **7,898**.

For the newly improved **strict target `E<76`**, the disjoint ledger is:

\[12,356-(4,282+166+10+1,492+4)=\boxed{6,402}.\]

Here 166 is all first-200 prior exact outcomes with `B_EXY<78`, including the two exact-78 arrangements, and 4 is the new exact-76 arrangements. The remaining 6,402 are **not yet excluded** for E<76 (including the 10 current timeouts), not 6,402 confirmed feasible arrangements. Prior complete triple-collision exclusion chain is unchanged.

## 3. Evidence, frozen sources and reproducibility

- **Frozen scientific input:** Global account source `773d538180bfb49e24cffeb35c3ee75eb0628e2e`; EM source `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Later behavioral rules are separately read from canonical main.
- **Immediate prior author frontier:** [EC49FAA](https://github.com/awdawmip/enterprise-math/blob/480ed27a8a56abfa428f46496c5ea33606846263/research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FAA_H8_M5_CUTOFF78_TEN_EXACT/README_EC49FAA.md).
- **Census source:** previous EXY immutable TSV Git Blob `61ffbcdba1679479fade3cfd052c2d9d6bbf30ce`. Reproduction programs preserve the actual published source-ranked list and native generator semantics.
- **Full local evidence:** four batch files `fab_run_*.json/jsonl` include all 1,506 case rows, input SHA256 hashes, trie nodes, colors, exact solver stdout/timeouts. `EC49FAB_CENSUS_REPORT.json` gives their per-file SHA256 and scope.
- **Constructive proof:** `VERIFY_EC49FAB_STANDALONE.py` executes without external dependencies. `EC49FAB_EXPLICIT_76_WITNESSES.json` retains four complete primitive-step expansions/keys, signatures and solver node traces. `EC49FAB_INDEPENDENT_VERIFY_REPORT.json` records the independent checker outputs; the standalone checker is the shortest sufficient external replication input.
- **Exact computation:** local `EXACT_OR_MASK_DP.cpp` and `WITNESS_OR_MASK_DP.cpp` mirror prior verified GitHub sources; standalone checker independently validates feasibility. The untouched published generator and optimizer source are the canonical reexecution references.

## 4. Actual authority and scientific status

GitHub authenticated login `awdawmip`, branch write permitted under existing PR; original task research backend remains read-only from this connector with `research_authority_granted=false`, and current active-owner listing returned `CONTROL_QUOTA`. No native CLAIM, Result or independent Driver review is asserted. P000 and ACTIVE six-axis worldview were read and left unchanged.

## 5. EC49FAC — next discriminating research unit

Search strict `E<76` (i.e. ≤75) among the 6,402 still-unexcluded double-collision arrangements using the same immutable EXY rows; prioritize color-18/20 affordable source ranks. At any `PASS` recover full signed words and check all 9-history observation matrices, six-axis positive keys, signs and prefix union via standalone verifier. For `BOUND_PASS` retain cutoff, exact input hash and finite-domain scope; keep timeouts open. Improve memoization/early cut bounds for 24/26-color inputs; a 26-bit mask fits unsigned 32-bit arithmetic but state explosion remains a separate complexity question. Keep the global lower bound 63 and upper bound 76 until stronger evidence is found.