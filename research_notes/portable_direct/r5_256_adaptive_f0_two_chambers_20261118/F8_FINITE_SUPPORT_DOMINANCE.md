# Finite maximal-support reduction for the R5 arbitrary-error adaptive problem

Date: 2026-11-18 (Asia/Shanghai). Status: AUTHOR_PROVED, model-internal exact lemma / NOT_REVIEWED. Science pin: \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`. This lemma applies to the general finite named-hypothesis / interval-response model, not only zero errors.

## State and action semantics

There are finitely many named hypotheses \`H\`, positively priced queries \`k\`, and nonempty sets of good observations \`G_h(k)\` for each h. The true named hypothesis is fixed; across an arbitrary adaptive transcript at most \`f\` responses may lie outside \`G_h(k)\`, unmarked. A response not in \`G_h(k)\` contributes precisely one required corruption under candidate h. Define \`e_h\` as the number of observed responses inconsistent with candidate h, clipped to \`f+1\`. The named candidate is still feasible exactly when \`e_h≤f\`. The full vector \`e=(e_h)_{h∈H}\`, not only its feasible support, is a sufficient information state for future guaranteed identification in this declared observer language. No distribution on corruptions is assumed.

For query k and response y, put \`R_k(y)={h:y∈G_h(k)}\`. The transition is
\`(T_{k,R} e)_h = min(f+1, e_h + 1_{h∉R})\`.

## Proposition 1 — monotone uncertainty

For two vectors e and e' over the same named set, if \`e_h≤e'_h\` for every h then the guaranteed worst-case future cost from e is at least that from e'. Proof: any transcript continuation that is feasible for an h after e' has at least as much remaining error allowance after e; thus every strategy that correctly distinguishes all candidates and allowed continuations from e is still correct from e'. Minimize costs to obtain the order.

## Proposition 2 — maximal correct-response supports suffice for all f

For a fixed k, order all possible response support sets R by inclusion and retain only inclusion-maximal sets \`M_k\`. Every support R is contained in some \`C∈M_k\` (the set of distinct supports is finite, as H is finite). Since \`T_{k,C}e≤T_{k,R}e\` coordinatewise, Proposition 1 gives

\`V(T_{k,C}e)≥V(T_{k,R}e)\`.

Consequently
\`max_{y feasible} V(T_{k,R_k(y)}e) = max_{C∈M_k feasible} V(T_{k,C}e)\`,
where feasibility requires at least one remaining named candidate with updated count ≤f. If a smaller R is feasible, any containing C is feasible. This remains valid for unmarked arbitrary corruptions, for every f≥0, for every current vector e and for adaptive action selection.

In the frozen scalar observer \`G_h(k)=[N_h(k)-τ/2,N_h(k)+τ/2]\`, the maximal supports are maximal center windows of width τ. They are computed exactly by two-pointer scanning sorted integer counts, independently checkable by sweeping endpoints \`2N_h(k)±τ\`. The accompanying \`VERIFY_R5_ADAPTIVE_ZERO_ERROR.py\` independently checks agreement of both constructions for **all 101 budgets** at both endpoints of the fifth and near-critical chambers. These support sets can be used unchanged in a future f=8 verifier, provided the full 256-component mismatch vector is retained.

## Consequence — rigorous finite f=8 recursion and a safe pruning rule

Let \`V(e)\` be the minimum worst-case remaining cost until at most one named h has \`e_h≤f\`. A finite minimax recursion may enumerate only C in \`M_k\`, update all 256 counters, and take the maximum over feasible C.

If some C leaves the **entire clipped vector e unchanged**, querying k cannot reduce the optimal worst-case cost because the adversary can choose that outcome; with positive query cost, the continuation with the same state is available without paying k. Such an action can be omitted from the minimization. Different vectors with the same surviving hypotheses **cannot generally be merged**, since their remaining corruption budgets differ. Similarly, two configurations sharing current scalar readouts are not merged unless their future observer/evolution scope has an exact preservation certificate.

This is a reduction in the number of **response branches**, not a claim that f=8 is computationally solved: the unresolved full256 fifth-chamber optimal cost remains \`8335≤C_8^*≤8343\`. Future implementation should combine exact maximal-support branching, per-hypothesis error counters and verified native residual/fiber constraints. The supporting f=0 exact verifier and all-f previous bounds are in the same source branch PR #2427.

## Scope and relation to P000

The result is about scalar query transcripts derived from a fixed X6-related model; the named h retain distinct identity. It asserts no general disappearance of signed, branch, temporal, composite, path or provenance residuals outside the exact scalar-observer horizon. The P000 native six-dimensional and current ACTIVE observer-fidelity contracts remain in force.
