# EC49FEU — Complete signature-support census for late-mixed 23-path native X6/BRC systems

Date: 2026-11-08. Status: **AUTHOR FINITE EXACT CLASSIFICATION / NOT INDEPENDENTLY REVIEWED / NOT ADMITTED**. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Question and exact domain

Continue EC49FEP (H2 mixed), EC49FEQ–FET (H3 mixed) by relocating the unique three-signature observation support to a **late window H4–H9**. Keep the original six-operation ordered signed X6 microsteps, the original nine-state observer, endpoint (+2,0,0,0,0,0), positive *complete* forward BRC keys, at most five distinct full keys, all eight observation horizons H2–H9, and exactly 23 complete operation words.

The observer's inclusion-minimal nine-rank supports are the high pair {16,32}, the mixed triple **B={1,8,16}**, its involution partner **C={2,4,32}**, and the low quartet {1,2,4,8}. Exactly one window uses a mixed triple, four use high pairs, and three low quartets. The five high-bearing horizons each require a distinct key with sum `x+y=h+1`. For the late-mixed case, H2 is a low quartet and H3 is a high pair. Four of H4–H9 are high-bearing, one of those four is mixed, and the other two late horizons are low quartets. All signatures are counted by *existence of an original complete legal word*, and different required signatures may freely select different keys from the fixed five-key inventory.

This is a **signature-feasibility classification**, not an optimization of native-prefix edge cost. It supplies the exact finite candidate set for the next cost proof.

## New exact census theorem

For type B, enumerate all candidate five-key inventories from one required early key `(3,1,1)`; one high-pair key for each of three ordinary late high horizons; and one key supporting signature 16 at the mixed horizon. For each of the 60 (mixed horizon, four-high set) placements, the exhaustive finite signature test gives:

| Mixed horizon | Candidate typed inventories | All required signatures feasible | Mixed signatures missing | Low-quartet signatures missing |
|---|---:|---:|---:|---:|
| H4 | 28,224 | **8,800** | 12,800 | 6,624 |
| H5 | 34,344 | **15,812** | 7,800 | 10,732 |
| H6 | 42,192 | **18,426** | 5,184 | 18,582 |
| H7 | 43,008 | **20,568** | 4,272 | 18,168 |
| H8 | 46,016 | **26,652** | 7,104 | 12,260 |
| H9 | 45,360 | **0** | 45,360 | 0 |
| **Type B total** | **239,144** | **90,258** | **82,520** | **66,366** |

Original word involution `I=(c d)(f g)`, full-key involution `J(x,y,z)=(y+2z,x-2z,z)`, and its observer action send B to C and preserve legality and native signed prefix count. Therefore **type C has the identical 90,258 feasible inventories**. The two typed late-mixed families together contain **478,288 typed candidate configurations**, of which **180,516 are signature-feasible** and 297,772 are signature-infeasible. Type B and C are different *typed supports*, not necessarily disjoint untyped key sets.

Per-horizon late high-*pair* full-key counts for H4..H9 are `(2,4,6,9,12,16)`; late signature-16-bearing full-key counts are `(4,6,9,12,16,20)`. The latter must be used at the mixed horizon, because a key that supports 16 need not support 32. This expansion is needed for a complete inventory census.

**Analytic late-horizon elimination.** H9 is necessarily high-bearing: if all five high-bearing horizons are before H9, their five required key sums satisfy `x+y<=9`; any legal nine-operation word needs `x+y>=10`. Moreover **H9 cannot be the mixed horizon**. In that case one of the five keys has sum 10 (the H9 high key), all others have smaller sums. Every legal H9 word must use the sum-10 key and then has `#c+#d=x+y-9-1=0`. The original DFA restricted to operations a,e,f,g reaches only states 1,4,5 after the first step, whose nonzero terminal labels are 16,32. Thus neither the B-required labels 1,8 nor the C-required 2,4 can occur. This is a direct structural proof; the exhaustive census independently returns 0/45,360 for H9 mixed type B.

For late mixed horizons H4–H8, all 90,258 feasible type-B candidate inventories include H9 as one of the four late high-bearing horizons. The next search may safely focus on these five placements and the fixed 90,258 exact inputs (plus C mirrors), instead of repeating the eliminated sets.

## Exact calculation and reproducibility

`EC49FEU_STANDALONE.py` is a Python-standard-library, self-contained finite enumerator. It uses the complete original key count relations

```
a = z-1
c+d = x+y-h-1
f = h+1-y-2z
g = h+1-x
```

and directly expands all reachable nine-state DFA states over the six operation multiplicities, requiring exact nonnegative counts. A legal key is generated exhaustively by `z>=1`, `r=c+d>=0`, `f>=0`, `g>=0`, and `h=2z-1+r+f+g`. It checks every required observation label against the union of complete-key signatures. The deterministic program validates the grand totals and emits full 60-branch results and sample inventory keys.

Run: `python3 EC49FEU_STANDALONE.py > EC49FEU_STANDALONE_REPORT.json`.

Two *independently organized* exact local computations agreed on every six-horizon aggregate and every mixed-horizon total: (i) the prior EC49FEQ recursively memoized signature DP (used by `EC49FEU_LATE_MIXED_CENSUS.py`) and (ii) an independently written breadth-first multiplicity-state enumerator (retained as the standalone source). No floating point arithmetic, randomized sampling or solver tolerances enter this census.

A separate original signed-X6 witness search also produced a **129-edge**, 23-word type-B H4-mixed *valid example*, with full key inventory `[(3,1,1),(3,2,1),(3,3,1),(3,4,1),(4,6,1)]`. Its 23 words are retained in `EC49FEU_EXPLICIT_WITNESS.json`. The value 129 is only the edge count of that example, not a family optimum; the mother-problem's previously known 94-edge witness remains strictly better.

## Meaning and next task

The old 22-path family is already classified in EC49FEO (minimum 94 for its exact domain). The H2-mixed and H3-mixed 23-path families were classified separately in EC49FEP and EC49FET (both exclude native-prefix cost <=93). This EC49FEU result covers the *remaining possible placements of a single mixed triple in the exactly-23-word regime at signature-feasibility level*, while preserving full keys and native operation order. It does **not** imply a new cost bound for H4–H8 mixed families.

Next: apply the group-aware native signed-prefix dual certificate of EC49FET or conservative depthwise sieve to the **90,258 type-B signature-feasible inventories**, starting with a bounded batch at H4/H8; test any <=93-surviving case with exact joint-prefix optimization and original six-axis witness checker. Transfer all results to C by the verified involution. Keep the global mother objective `<=5` full BRC keys and `C_native<=93`.

Source evidence: frozen science SHA above; current author-side historical evidence EC49FEO, EC49FEP, EC49FEQ, EC49FES, EC49FET on PR #1730. P000/ACTIVE worldview unchanged. Source native claim and independent Driver review must be checked under their *actual* current authority; author-side GitHub persistence is not formal task-machine Result/Review.

## Control-state observation, not a theorem premise

At 2026-11-08 (current run), the native service advertised `research_authority_granted=false`; an exact task-inventory query returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE` with `operation_sent=false`. Nevertheless the session registration subsequently finished with a verified canonical Source readback: real researcher `EM-DIRECT-998F74`, activity `RA-4BED150AB52F9F8C3B9177BD`, session `MCP-a510c4044c9946b886da2075bf0935f2`, canonical registration commit `8b3cf66ff1cd1a2992897916b20e2081093e2a00`, activity recorded `2026-11-08T15:35:46.287653Z`. Native `execution_authorized=false` and `claim=false`; no formal CLAIM/Result/Review or confirmed active task owner is asserted. GitHub writer identity: `awdawmip`. Researcher activity registration and author-side source publication are separate from formal admission.
