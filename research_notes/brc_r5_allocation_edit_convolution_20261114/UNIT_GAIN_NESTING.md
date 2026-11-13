# Frozen R5 saturation: universal unit-gain extension theorem

Date: 2026-11-14. Addendum to the blockwise optimal-allocation edit result in this directory. This is a finite metric-space theorem, specialized below to the pinned R5 integer event-boundary metric. It reuses the all-budget exact frontier of Draft PR #2302; no new assumption about P000 is introduced.

## Theorem (minimum-separation marginal gain forces universal nesting)

Let \`X\` be a finite metric space with \`N\` points and pairwise minimum separation \`λ>0\`. Fix a radius \`R\` and assume \`S⊆X\` with \`|S|=K<N\` is feasible (every point within distance \`R\` from a center in \`S\`). Define \`J(S)=Σ_(x∈X) d(x,S)\` and \`J_R(K)=min_{|S|=K, feasible}J(S)\`.

**Theorem.** If the exact marginal optimum gain obeys

\`\`\`
J_R(K)-J_R(K+1)=λ,
\`\`\`

then **every** optimal \`K\`-center set \`S\` and **every** \`t∈X\S\` satisfy

\`\`\`
S∪{t} ∈ Opt(K+1).
\`\`\`

Consequently, \`ρ_K=0\` and every optimal \`K\`-center set admits at least \`N-K\` distinct optimal single-center extensions.

**Proof.** Adding a center preserves radius feasibility. At the newly selected point \`t\`, its previous nearest-center distance was at least \`λ\`, and becomes zero. All other nearest-center distances can only decrease, so

\`\`\`
J(S∪{t}) ≤ J(S)-λ = J_R(K)-λ = J_R(K+1).
\`\`\`

By the definition of \`J_R(K+1)\`, a feasible set of \`K+1\` centers cannot have a lower cost. Equality follows, making \`S∪{t}\` optimal. The choice of \`S\` and \`t\` was arbitrary. QED.

There is no converse assertion: universal nesting may hold at a marginal gain larger than the minimum pairwise separation.

## Application to frozen R5

The event-boundary centers are distinct integers; the minimum distinct-coordinate separation is \`1\`. For radius \`2\`, the exact all-budget results in Draft PR #2302 give \`K_min(2)=213\`, \`D_1=351\`, and

\`\`\`
J_2(K)=954-K  for 351≤K≤954.
\`\`\`

Thus \`J_2(K)-J_2(K+1)=1\` for every \`K=351,...,953\`. The theorem gives

\`\`\`
ρ_K=0 for all 603 transitions K=351,...,953.
\`\`\`

Indeed, starting from **any** optimal 351-center set, add the remaining 603 points in **any order**: every intermediate center set remains globally cost-optimal. This is a path-connected nested high-budget region in the sense of extension chains, not an assertion that every optimal set of a lower cardinality contains all smaller optimal sets.

The previously computed complete R5 one-step gain histogram is 603 occurrences of gain 1, plus 36 of gain 2, 23 of gain 3, 70 of gain 4, 8 of gain 5 and 1 of gain 6. Accordingly, the 603 unit-gain transitions are all exactly certified nested. The remaining 138 transitions \`K=213,...,350\` form the nontrivial reconfiguration region; 79 of them are already forced nonnested by the sharp single-addition gain bound in Draft PR #2312, and 59 transitions with marginal gain 2 or 3 require specific edit-distance analysis.

## Check

The theorem is proved for all finite metric spaces with positive minimum separation. A supplementary independent finite check enumerated \`X={0}∪Y\`, \`Y⊆{1,...,8}\`, \`2≤|X|≤6\` (218 point sets), and all radius-two optimal center subsets. Of 540 adjacent feasible-budget comparisons, 361 had exact gain one; all 361 satisfied the universal extension claim for every optimal old center set and every unselected point. This check is illustrative and not needed for the theorem proof.

Next: compute the precise \`ρ_K\` for the remaining 59 low-gain transitions and the remaining gain-4/5/6 region, using the blockwise coupled algorithm rather than enumerating full optimal-set families. Preserve the native 28-coordinate/8192-query benchmark as a separate unresolved performance objective.
