# R5 — A single future named Set already forces eleven source-faithful controller states

Date: 2026-11-16. Scientific source pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Scope: the *auxiliary* canonical genuine-source cyclic six-node model, budget two, controls J={0,1}. Historical scientific frontier: `research_notes/portable_direct/r5_k6_unrestricted_ten_state_no_go_20261116/` at commit `dcae065958c8236f929700f632f2780632e50501`. This is independent author-side scientific preservation, not an authenticated formal CLAIM, Result or Review. Review: NOT_REVIEWED.

## Precisely stated finite-horizon theorem

Let `X={0,...,63}` denote six-bit snapshots, with cyclic edge count
`q(u)=sum_{i=0}^5 u_i*u_{(i+1) mod 6}`. For a genuine-source output label `r`, set

`G(r,u) := ((u & ~r)==0) and 0 <= q(r)-q(u) <= 2`.

The four raw actions `U_a` are `Set_0(0)`, `Set_0(1)`, `Set_1(0)`, `Set_1(1)`. An m-state deterministic Moore controller has fixed output centres `r_j`, arbitrary deterministic internal transition maps `f_a`, and an initialization relation that associates each raw `u` to at least one state `j`. An association is admissible through horizon H when the original output and the output after *every* word of length at most H are source-feasible. This does not assume idempotence, commutation, reset absorption, or disjoint initialization.

Write `N_H` for the minimum number of controller states under that precise horizon (using the inherited canonical genuine-source replacement lemma).

**Theorem (sharp horizon-one threshold).**

```
N_0 = 10;
N_H = 11  for each integer H >= 1.
```

Thus one possible future operation already separates the ten-output static source cover from fully future-safe eleven-state control. The minimum does not increase for longer horizons in this model.

## Proof: exact finite obstruction at one operation

1. For H=0 the question is minimum static coverage by feasibility masks `G_r={u:G(r,u)}`. A dominated centre can be replaced by a centre with a containing feasibility mask. Among 64 original masks, 22 are nondominated. The preceding exact certificate in `R5_K6_UNRESTRICTED_TWO_CONTROL_EXACT_ELEVEN_THEOREM.md` proves that no nine-centre cover exists. The present companion verifier independently re-enumerates **116** unordered ten-centre covers and includes an explicit ten-centre upper witness. This establishes the zero-horizon optimum using the inherited nine-centre lower bound, with the 116-case enumeration directly checked here.

2. Fix any ten-state controller and its output centres. Its labels necessarily form a static ten-centre cover. Replacing any dominated source centre by a dominating source centre cannot invalidate output feasibility at horizon one. The ten static labels must be distinct up to mask equivalence, since nine labels cannot cover X. Thus one of the 116 nondominated centre tuples can be used without sacrificing a candidate.

3. For one such tuple `C=(r_0,...,r_9)`, define `F_j={u: j is the only index for which G(r_j,u)}`. Every admissible initialization must associate every `u in F_j` to state j. Hence for each operation a, its target `f_a(j)` must belong to the *necessary* set

`T(j,a)={t : G(r_t,U_a(u)) for every u in F_j}`.

If one `T(j,a)` is empty, the tuple cannot support a one-step controller.

4. Exactly **110** of the 116 centre tuples have an empty necessary target set. For the other **six**, each `T(j,a)` is a singleton or a pair. There are exactly `4 + 256 + 4 + 128 + 128 + 64 = 584` complete deterministic transition tables satisfying all necessary unique-initialization obligations. They are all exhaustively enumerated.

5. For each such table f, calculate the exact one-step-viable initial snapshots

`V(f)={u in X : exists j, G(r_j,u) and (for all four a) G(r_{f_a(j)},U_a(u))}`.

This existential assignment is the most permissive allowed initialization, including overlapping beliefs. A one-step controller exists for that fixed table exactly when `V(f)=X`. Among all 584 tables, the largest cardinality is only **61**. The complete histogram, indexed by `|V(f)|`, is:

```json
{"56":64,"57":192,"58":128,"59":128,"60":64,"61":8}
```

Consequently no ten-state controller meets horizon one. Reusing the earlier exact coherent-cube eleven-state witness supplies correctness under all finite Set words; the new verifier independently checks its complete 16-tail by four-assignment source-feasibility table. Therefore `N_H=11` for every H>=1.

## Reproduction and scope

Run `python VERIFY_R5_K6_ONE_STEP_OBSTRUCTION.py` (standard library only) and compare its JSON output to `EXACT_R5_K6_ONE_STEP_OBSTRUCTION_EVIDENCE.json`. The result is `PASS_R5_K6_SHARP_HORIZON_ONE_NO_TEN`. The algorithm enumerates 116 covers, rejects 110 with exact necessary-image constraints and checks every remaining 584 transition table against every one of 64 raw initial states and all four named operations. No floating-point, MILP solver, sampled words, or formal theorem acceptance is needed for this finite auxiliary result.

The inherited canonical genuine-source replacement lemma is a typed prerequisite for transferring the optimum to arbitrary source libraries. This note neither changes P000 nor upgrades this six-bit auxiliary model to a complete native three-dimensional slice/X6 physical assertion.

**Next mathematical question.** Generalize the finite-horizon bound to `k>=7` and larger controlled coordinate sets: determine when a one-step future-observation test is already sufficient for the unrestricted all-words optimum, and obtain a small human-checkable obstruction certificate rather than enumerating all source covers.
