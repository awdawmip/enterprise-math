# R5 exact simultaneous two-gap closure: recourse is the maximum single-gap cost

Date: 2026-11-15. Researcher-side status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_INDEPENDENTLY_REVIEWED**. Frozen scientific pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.

This note **advances** the earlier `RESEARCH.md` in this directory: the previously derived triangle **intervals** for closing cuts 8 and 9 are now replaced by exact values computed directly from the joint-closure optimizer language. The old interval bounds remain valid certificates and historical mathematical progress.

## Definition and scope

Fix the previously frozen 954-event *derived* ordered-integer model with radius `rho=2` and centers chosen from original event indices. Its 28 possible gap closures are indexed from zero. For any closure set B and center count K let `O_B(K)` denote the **entire** family of optimal K-element index sets; the prior fixed-budget cost is `J(K)=2134-5K` for K=214..221.

Define directed set-replacement recourse

```
d_K(C,A) = max_{S in O_C(K)} min_{T in O_A(K)} |S \ T| .
r_i(K,B) = d_K(B+i,B).
D_89(K,B) = d_K(B+{8,9},B).
```

All maxima/minima use exact labeled event indices and preserve **max over new, min over old**, with the old response chosen after the entire new optimum is known.

## Exact finite theorem

**For every integer K=214,...,221 and every B subset of the other 26 gap indices (excluding 8 and 9),**

```
D_89(K,B) = max(r_8(K,B),r_9(K,B)).
```

Moreover the common exact value is:

| K | Original cut 10 open | Original cut 10 closed |
|---:|---:|---:|
| 214 | 7 | 7 |
| 215 | 6 | 6 |
| 216 | 6 | 5 |
| 217 | 5 | 5 |
| 218 | 5 | 5 |
| 219 | 5 | 5 |
| 220 | 5 | 5 |
| 221 | 5 | 5 |

The result is independent of all other closure bits in the stated derived observer. The 64 effective-background cases have histogram `5:44, 6:12, 7:8`. **This equality is a property of this frozen instance and budget range, not a universal identity for arbitrary center-set languages or native X6.**

### Proof: finite exact algorithm, coupled with prior coverage theorem

**Step 1 (lossless reduction to 64 cases).** The prior exact R5 optimizer-family support theorem proves `O_B(K)` depends only on E=`{3,8,9,10,27}` for K214..221, with labeled optimizer sets retained. Hence the other 23 bits may be suppressed without changing any exact recourse. Holding bits 8 and 9 initially open leaves `2^3=8` background configurations over `{3,10,27}` per each of eight K values: precisely 64 complete effective cases, representing **all original 26-bit backgrounds**.

**Step 2 (exact optimizer languages).** The standalone `VERIFY_R5_JOINT_CLOSURE_OFFLINE.py` reconstructs the frozen 15-term rational event generator from the numerical coefficients, exactly regenerating 954 event indices and 28 gap-3 cut positions. Closing an indexed gap changes subsequent integer coordinates, not event labels. For each of the 32 effective masks it reconstructs the entire minimum-total-distance optimizer as a rank-labeled acyclic center-path language using arbitrary-precision-integer prefix and suffix Bellman recurrences. The graph includes exactly the feasible consecutive-center arcs, plus prefix/tail cover costs; the original full-distance semantics is separately checked for each representative.

**Step 3 (lossless anchor factorization).** Prior R5 exact evidence supplies common unique-ranked anchors center index 16 at rank 3 and center index 536 at rank K-85 for all 32 masks and K214..221; optimal prefix and suffix options outside these anchors are common. All full optimizer languages therefore factor into a common outside language and an **internal** path language of `K-89` centers. The common outside centers can be chosen identically between old and new, and these shared unweighted anchors do not change the directed max-new/min-old distance. The code checks both anchors as *unique* optimizer vertices for each old/new pair. This factorization is a load-bearing earlier author-side result, not an independent proof of that lemma in this note.

**Step 4 (exact offline max-new/min-old DP).** For a fixed new internal prefix and an old optimal frontier at event-index cut j, retain for each rank-labeled old crossing tail the maximum overlap with that new prefix over all old prefixes reaching it. A new next center processes the intervening old DAG vertices in original-index order using max-plus predecessor transitions; a coincidence with the new chosen index scores one. Every old optimum has exactly one path through these crossing-frontier transitions, and conversely every reachable old prefix can concatenate with its old suffix. Thus the terminal scalar equals `max_old |S ∩ T|` for that **complete** new center path S. The new player minimizes that scalar, keeping all componentwise nondominated score vectors at each fixed new optimizer node. Max-plus continuation is monotone, so any vector componentwise >= another at the same node is never better for the minimizer; Pareto deletion preserves every attainable minimal terminal value. Finally `D=K-89-min_new max_old internal-overlap`. The program iterates **all** new-optimal arcs, not a sample, so the computed value is the original directed Hausdorff max-new/min-old distance.

**Step 5 (finite result and crosschecks).** The execution rebuilt all 32 optimizer families and recomputed **256** previous single-cut 8/9 results. It asserted equality to all 256 values in the previously committed exact compact table. Then it evaluated all **64 direct joint-closure transitions**, asserting `D_89=max(r8,r9)` in each case and the triangle bounds derived in the earlier note. For each case it reconstructed a complete new-optimum K-center path, checked radius-two feasibility and the exact cost `J(K)=2134-5K` over **all 954 events**, and independently recomputed that witness's nearest old-optimum overlap via a separate full rank-layer max-plus DP. Every check passed.

The local execution returned `PASS_R5_JOINT_OFFLINE_MAXMIN`, with **64** direct joint tests, **256** rebuilt single-cut tests, and maximum observed Pareto-vector aggregate per rank **23**. Its 23,956-byte full JSON stdout has SHA-256 `954afd931f7995c8ee14611c6802ab5940092d473a727b92671ced73f6257c2b`. The exact 64-row compact table is committed at `EXACT_R5_TWO_CUT_JOINT_RECOURSE_SUMMARY.json`; the standalone Python reproducer deterministically regenerates witnesses and every finite value.

### Reproduction

Run in Python 3 using the standard library:

```sh
python VERIFY_R5_JOINT_CLOSURE_OFFLINE.py \
  ../r5_low_budget_unit_recourse_20261115/EXACT_R5_OFFLINE_MAXMIN_ALL_BACKGROUND_VALUES.json \
  > JOINT_OUT.json
```

Run from this directory: the relative `../r5_low_budget_unit_recourse_20261115/` path is correct when both folders live under `research_notes/portable_direct/`. The program has no nonstandard dependencies, and the source embeds all frozen generator parameters; it reads the previous compact table **for crosschecking**, not for selecting the joint optimum.

Verification classes: mathematical derivation and finite exact integer exhaustive state DP, author-side reproduction; the generator, optimality-DAG completeness and anchor factorization follow the cited frozen-model definitions and prior author proofs. The independent reviewer/Driver review remains `NOT_REVIEWED`; no formal native Task/CLAIM/Activity Result or Foundation promotion is claimed.

## New scientific frontier

1. Determine whether an exact *structural* sufficient condition forces `d_K(B+{i,j},B)=max(r_i,r_j)` in more general nested optimal set families, and construct sharp counterexamples when it fails.
2. Implement and benchmark the companion **future-language residual quotient** from `RESEARCH.md` on the actual rank-labeled old optimizer DAGs, to distinguish true suffix-language identity/inclusion from mere scalar frontiers. No runtime improvement is claimed without such implementation.
3. Independently review the old/new optimizer-language reconstruction, anchor factorization, graph completeness and offline Pareto transition. Preserve the original auxiliary-observer scope and full P000/X6 distinction.

Cited prior material: `research_notes/portable_direct/r5_low_budget_unit_recourse_20261115/OFFLINE_MAXMIN_EXACT_RECOURSE_THEOREM.md`, `VERIFY_R5_OFFLINE_MAXMIN_RECOURSE.py`, `EXACT_R5_OFFLINE_MAXMIN_ALL_BACKGROUND_VALUES.json`, `research_notes/portable_direct/r5_global_optimizer_tomography_20261114/RESEARCH.md`. Prior branch snapshot `f397ff3067c5857e374fd82547379373a6aa9c79` on existing Draft PR #2427.
