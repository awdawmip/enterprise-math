# Frozen R5 exact nesting phase boundary: 79 forced nonnested, 662 nested

Date: 2026-11-14. Scientific source pinned to \`awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551\`. This is the original integer event-boundary sampling model with radius 2, not a native 28-coordinate benchmark. It synthesizes the sharp single-insertion bound of Draft PR #2312, blockwise marginal concavity of #2307, full budget frontier of #2302 and the coupled optimal-path lemma in the present PR.

## Exact classification theorem (frozen R5)

Let \`ρ_K = min_{S∈Opt(K),T∈Opt(K+1)} |S\T|\`, for globally cost-minimizing radius-two subsets of the 954 strictly increasing integer event coordinates.

**New exact conclusion:**

\`\`\`
K=213,...,291:   ρ_K >= 1   (79 transitions, forced nonnested)
K=292,...,953:   ρ_K = 0    (662 transitions, nested optimum pair exists)
\`\`\`

Consequently, **K=292 is the first consecutive-budget transition that admits a nested pair of globally optimal center sets**, and *every* consecutive-budget transition from 292 through 953 admits at least one nested optimum pair. No assertion that *every* optimal K-center set extends optimally is made for K292..350; the stronger universal-extension statement applies to K351..953 by the unit-gain theorem.

The frozen marginal gain distribution in strictly descending order is:

| K (from budget) | J_2(K)-J_2(K+1) | Count | Status |
|---|---:|---:|---|
| 213 | 6 | 1 | nonnested |
| 214..221 | 5 | 8 | nonnested |
| 222..291 | 4 | 70 | nonnested |
| 292..314 | 3 | 23 | nested pair |
| 315..350 | 2 | 36 | nested pair |
| 351..953 | 1 | 603 | universally extendable |

## Proof, with only two exceptional local witnesses

**High gains (79 transitions).** Draft PR #2312 proves that inserting a single new center into any radius-two feasible center set of distinct integers improves nearest-center cost by at most 3. If a globally optimal \`K\` set were contained in a globally optimal \`K+1\` set, the gain could not exceed 3. Since all 79 transitions K213..291 have gain 4, 5 or 6, they are all forced nonnested.

**Unit gain (603 transitions).** The independently proved universal unit-gain theorem in \`UNIT_GAIN_NESTING.md\` shows that every optimal K-center set can be extended by any unselected center when the gain equals the minimum pairwise distance 1. Therefore K351..953 all have \`ρ_K=0\`.

**Intermediate gains (59 transitions).** The frozen radius-two input splits into 29 independent blocks. Every block's exact marginal cost savings as centers are added are nonincreasing (verified by exact local DP; original method in #2307). Thus to minimize total cost at a global budget, take a prefix of the largest remaining marginal gains in every block; ties at a gain level can be distributed across eligible blocks.

For any positive gain \`g\`, let \`L_i\` be the number of local marginal gains strictly greater than g in block i and \`C_i\` the number equal to g. Write \`L=Σ L_i\`, \`C=Σ C_i\`. Each transition within that tie level has \`u=K-213=L+r\` with \`r=0,...,C-1\`. A designated block i carrying **exactly one** gain-g unit (\`C_i=1\`) can remain at its pre-gain allocation \`k_i^{min}+L_i\` for every \`r\`: allocate the other r equal-gain units arbitrarily across the remaining blocks, whose total capacity is C-1. The new budget adds the designated unit. If the designated block admits a nested pair of optimal local sets across that one-center step, combining identical optimal local sets in all other blocks produces a globally nested optimum pair.

For **g=3** (23 global transitions), zero-based block **1** has a single gain-3 unit, at local budget \`4→5\` (3 minimum + 1 already extra), with local cost \`12→9\`. It has the explicit nested witness, relative to its block origin:

\`\`\`
old S3 = {1,4,7,12}
new T3 = {1,4,7,9,12} = S3 ∪ {9}.
\`\`\`

For **g=2** (36 global transitions), zero-based block **0** has a single gain-2 unit at local budget \`6→7\` (4 minimum + 2 already extra), with local cost \`14→12\`. Explicit witness:

\`\`\`
old S2 = {1,6,9,12,15,18}
new T2 = {1,2,6,9,12,15,18} = S2 ∪ {2}.
\`\`\`

For each transition within either tied-gain band, distribute all other chosen equal-gain units over the other 28 blocks (possible for every \`0≤r≤C-1\`). Choose the same locally optimal center sets in these other blocks in both budgets. This yields \`S⊂T\`, \`|T|=|S|+1\`, and exact global costs \`J_2(K),J_2(K+1)\`. Thus \`ρ_K=0\` for all 59 intermediate transitions. Combined with the two other cases proves the complete 741-transition classification. QED.

## Finite exact verification

The new companion program \`CLASSIFY_R5_NESTING.py\` recomputes the frozen 15-atom input, all 29 exact local DPs and all 741 marginal gains; asserts local diminishing returns; checks local optimum-language subset witnesses for the two tie-level units; and for **each of the 59 gain-2/3 transitions** constructs complete old and new global center sets, checks actual center-set nesting, and directly recomputes all 954 point-to-center nearest distances in integer arithmetic, verifying radius-two feasibility and the exact global optimal costs. The local optimum-path product uses exact DP predecessor equality, not family enumeration.

Local-run observation: \`PASS_EXACT_GLOBAL\`; 954 boundaries, 29 blocks, gain histogram \`{1:603,2:36,3:23,4:70,5:8,6:1}\`, 59 complete directly checked global witness pairs, 662 nested and 79 nonnested transitions. Only two distinct local optimal-path subset queries were needed for the 59 constructive cases. Previous small exhaustive validations covered the local pair language separately.

**Scope:** Exact conditional theorem for the pinned frozen R5 event-boundary instance. Program proof checks, author computations, repository publication, authenticated Task CLAIM and independent mathematical review remain distinct. Source inputs and the original 2,520-byte compressed certificate / 28-coordinate / 8,192-query native end-to-end performance question remain unchanged.

**Next:** For K213..291, calculate exact positive values of \`ρ_K\` (the classification gives the sharp zero/nonzero decision only). Develop a direct all-budget histogram of edit distances with cost-sensitive witnesses, and perform the original complete prefix-query benchmark separately.
