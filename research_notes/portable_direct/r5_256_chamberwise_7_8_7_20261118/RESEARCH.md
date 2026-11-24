# R5 — Exact 7–8–7 action dominance phase diagram (full 256 states)

Date: 2026-11-18 (Asia/Shanghai). Scientific status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Provenance: frozen science commit `435e77af0d180eac32bd1f9c4c464bc4010b7551` and exact integer input `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. This extends the previously published uniform eight-action all-f theorem in this same PR.

There are 256 individually named hypotheses, with exact integer observation centers `N_h(k)`, and 101 physical actions `k=214,...,314`, each costing `k`. A correct observation is in the closed interval `[N_h(k)-tau/2,N_h(k)+tau/2]`. At most any integer `f>=0` observations may be arbitrary unmarked errors. Policies are adaptive and minimize worst-case cumulative query cost for a **known real** noise diameter `tau`.

Define
```text
L=25845652773852463277015040000
P=42621568083499305947627520000
Q=45392032647559604256815185920
U=58182461585441404127941754880
```

## New theorem

For every real `L<=tau<U` and every integer `f>=0`, at least one globally optimal full-256 adaptive policy exists using only the following phase-specific budgets:

| Tau interval | Exact undominated action core under cheaper single-query response-support refinement |
| --- | --- |
| `[L,P)` | `214,215,216,223,294,295,296` (7) |
| `[P,Q)` | `214,215,216,217,223,294,295,296` (8) |
| `[Q,U)` | `214,215,216,217,223,295,296` (7) |

The word *undominated* uses a precise criterion: an action `j<k` dominates `k` when every inclusion-maximal correct-response hypothesis support for `j` is contained in one possible correct-response support for `k`. At each noise phase, every discarded action has a directly dominating cheaper member of the displayed core, and every retained action has a counter-support against **every cheaper action**. A simulated k-observation from the cheaper response cannot acquire an extra corruption; this holds at arbitrary f and retains each named hypothesis's independent error count. These core sizes are minimal under **single-query cheaper refinement**, not asserted absolutely minimal under arbitrary multistage substitutions.

## Mechanism at the two exact boundaries

At `tau<P`, budget 216 simulates 217. At equality `tau=P`, a maximal correct budget-216 response support
```text
{2,18,34,50,66,82,98,114,128,144,160,176,192,208,224,240}
```
is contained in no budget-217 response support. All other cheaper actions are likewise excluded by enumerated witnesses. At `tau=Q`, the range of all 256 exact budget-294 centers equals exactly Q; the 294 maximal support collapses to the complete 256-state set. It therefore adds no worst-case discrimination and is dominated by every cheaper action for `tau>=Q`. The equality endpoints are handled using closed observation intervals.

## Complete exact verification

The source integer table produces 17 distinct center-gap changes inside `[L,U)`, hence 18 half-open real signatures. The included Python 3 standard-library verifier builds **1,818 maximal support families twice independently**, once by sorted-center windows and once by closed-interval event sweep; they agree at all signatures. It enumerates all cheaper-pair dominance tests, explicit replacement maps for every discarded action, and one counter-support witness for each retained-action/cheaper-action pair in each signature. It validates both transition mechanisms and emits a full per-chamber JSON certificate. Run:
```sh
python3 VERIFY_R5_CHAMBERWISE_SEVEN_CORE.py EXACT_R5_ALL_101_BUDGETS.json > RESULTS.json
```
Local exact computation returned `PASS_R5_256_CHAMBERWISE_7_8_7_ACTION_CORES_ALL_F` with exit code 0, independently confirmed in the local checker. Input file bytes are not rewritten here: the SHA-256 and frozen science pin are mandatory for reproduction. Mathematical review remains `NOT_REVIEWED`.

The fifth-chamber full-256 adaptive eight-error minimax cost remains bounded by `8335<=C_8^*<=8343`. Next: exploit the phase-specific seven-action cores in exact Bellman search, or derive multi-query/root-action pruning for the decisive eight-action middle phase. No new formal CLAIM, shared Result or native X6 collapse is asserted by this independent scientific artifact.
