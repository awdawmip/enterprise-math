# R5: exact offline max-new/min-old recourse for cuts 8 and 9

Date: 2026-11-15. Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.

Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Scope: the derived 954-event, one-dimensional, radius-two **indexed-center** observer, retaining all original event labels and the 28 closure bits. This is not asserted to be a lossless native X6 or BRC observer.

## Exact theorem

Let `Opt_B(K)` denote every optimal event-index center set of size K in gap-closure background B. Define

\[
R_i(K)=\max_{B\subseteq I\setminus\{i\}}\max_{S\in\mathrm{Opt}_{B\cup\{i\}}(K)}\min_{T\in\mathrm{Opt}_B(K)}|S\setminus T|.
\]

For each integer K=214,...,221, the exact worst necessary replacement distances for cuts i=8 and i=9 (zero-based; original gap-start event indices 110 and 116) **coincide**:

| K | R_8(K) | R_9(K) |
|---:|---:|---:|
| 214 | 7 | 7 |
| 215 | 6 | 6 |
| 216 | 6 | 6 |
| 217 | 5 | 5 |
| 218 | 5 | 5 |
| 219 | 5 | 5 |
| 220 | 5 | 5 |
| 221 | 5 | 5 |

Across the 16 effective background masks for each changed cut, the exact recourse histograms (distance: number of backgrounds) are:

| K | cut 8 | cut 9 |
|---:|---|---|
|214|3:4; 7:12|5:8; 7:8|
|215|3:4; 6:12|5:8; 6:8|
|216|3:4; 5:8; 6:4|5:12; 6:4|
|217|3:4; 5:12|5:16|
|218|3:4; 5:12|5:16|
|219|3:4; 5:12|5:16|
|220|3:4; 5:12|5:16|
|221|3:8; 5:8|5:16|

All 256 exact transitions were evaluated, maintaining the original max-new/min-old quantifiers. Together with the previously preserved results R_3(K)=3, R_10(K)=4 and R_27(K)=1, this resolves all nontrivial changed cuts in the K214..221 five-bit effective region.

## Exact finite minimax algorithm and proof

**Common-anchor factorization.** Existing R5 evidence proves that for K214..221 and all 32 masks over effective bits E={3,8,9,10,27}, every optimum center path contains center index 16 at rank 3 and center index 536 at rank K-85. The optimal prefix and suffix languages outside these anchors are common to every mask. Thus new and old paths can use identical outside-center choices. There are `m=K-89` internal centers. Write N and O for the globally optimal *internal* path languages between these anchors. Then the exact directed-Hausdorff recourse is

\[
R_i(K;B)=m-\min_{S\in N}\max_{T\in O}|S\cap T|.
\]

Both languages are layered DAGs certified by exact integer optimal-prefix and suffix tables. The old path may be selected after the complete new path is known.

**Old Viterbi response.** Fix a prefix of the new path, ending at event index j. Give each old-optimal DAG vertex (event q, rank r) weight 1 precisely when q is one of the selected internal new centers; otherwise give weight 0. The maximum old/new overlap for a completed new path is the maximum-weight path in the old DAG. Process vertices in increasing original event index (every DAG edge increases this index). At index cutoff j retain the maximum accumulated scores of those processed old vertices having an outgoing edge to a vertex beyond j. On appending the next new center j', process all old vertices with indices in (j,j'], adding weight 1 only at j'. Discard vertices unable to cross the new cutoff. Keep the terminal anchor score as the final response.

**Pareto-exact compression.** For a fixed new optimal DAG node (rank r, event j), two new prefixes may yield old-frontier score vectors u,v. If `u<=v` componentwise, appending any common new suffix updates the old max-plus automaton monotonically, so the final maximum old overlap starting from u cannot exceed that starting from v. The new optimizer minimizes this maximum, hence v is dominated and may be discarded. Keeping all componentwise nondominated vectors at each new vertex and propagating every optimal new edge yields the *exact* finite minimax value. At the final unique old anchor state, choose the minimum score. This computes offline max-new/min-old set recourse and removes the extra online rank-coupling restriction from the earlier upper certificate.

**All-background reduction.** The earlier exact optimizer-family support theorem gives dependence only on E={3,8,9,10,27} in this budget band. For each changed cut there are 16 effective old/new background pairs, which exactly cover every assignment of the other 27 original closure bits for the stated observer. The reduction preserves center labels and the max/min quantifier order.

## Computational evidence

Run `VERIFY_R5_OFFLINE_MAXMIN_RECOURSE.py` beside the existing `VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE.py` on the same Draft PR branch. It reconstructs the 954 events from the immutable 15-term R5 input; builds 32 optimal DAG families; evaluates eight budgets, 16 background masks per cut and two changed cuts. All scores are arbitrary-precision integers. For each of the 256 transitions it constructs a complete K-center new optimum witness, checks radius-two coverage and total distance `J(K)=2134-5K` over all 954 events, and independently recomputes the nearest old optimum overlap by full-layer max-plus DP. It also compares the algorithm with full enumeration on 200 deterministic small random DAG pairs.

Observed result: `PASS_EXACT_R5_OFFLINE_MAXMIN_RECOURSE`; 256 all-background cases; 200 exhaustive toy-DAG crosschecks; greatest observed old-frontier width 19; greatest nondominated-vector count per layer 30 (empirical workload properties, not general complexity bounds).

The exact 256-case per-background values and result metadata are published in `EXACT_R5_OFFLINE_MAXMIN_ALL_BACKGROUND_VALUES.json` at this commit. The committed original-byte Python verifier deterministically generates the full JSON, including complete representative 954-event K-center witnesses. The actual author-side execution generated 144,081 JSON bytes (SHA-256 `e8157e196f3d8408a11bf5f67935d4e083578844d6461433f209fed63f4e04ed`); the complete local output is also retained in the conversation artifact, while the durable project repository stores the exact compact table and source needed to regenerate it.

Frozen source and earlier science: PR #2427 at `35194004bf0bc839db02af35f7b293c6fc311b5d`, especially `ONLINE_COUPLING_EXACT_RECOURSE_THEOREM.md` and `research_notes/portable_direct/r5_global_optimizer_tomography_20261114/RESEARCH.md`.

## Control and next research

This author-side GitHub artifact is scientific preservation, not a new formal Task CLAIM, Result or independent review. Historical Activity: `RA-33C87C2B703418F0706695E9`. Any protected progress mutation still requires current authenticated task/owner authority.

Next: derive a parametric frontier-antichain complexity bound, seek further structural reductions for broader budget families, and independently review the common-anchor factorization and offline max-plus recurrence before promotion.