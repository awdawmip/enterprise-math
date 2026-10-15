# Unreviewed BRC result (2026-10-15)

For n labelled sources with nonnegative integer residual masses, each operation G_j=I\{j} secretly resets one included source. After an operation, report b=1 iff the residual sum is at least T=3; final success means every supported path has residual sum at least Q.

Proved sharp-pair lower bounds (not full-space upper bounds):

- Q=1, n>=3: X=(1,...,1), Y=(1,...,1,2). No policy distinguishes in n-1 steps, while an adaptive n-step policy does.
- Q=2, n>=2: X=(1,...,1,3), Y=(1,...,1,2). The same exact pair horizon n holds.

Proof ideas: for Q=1 neither state can become unsafe before all n sources have been reset. For Q=2 any unsafe path of at most n-1 steps resets the heavy source and at least n-2 light sources; until heavy reset, both feedback bits are high, after which the states coincide. Length-n separating policies repeatedly exclude source 0 (Q=1) or the heavy source (Q=2), and continue after prescribed feedback only.

Also proved the first-low-feedback suffix lemma: for any integer 1<=Q<T, any oriented separating adaptive policy admits a comb witness whose continuing feedback is some highs followed by lows, with at most T-Q moves after the first low feedback. Removing zero-progress moves preserves a Y unsafe witness and cannot invalidate X universal safety because resets only decrease mass.

Independent exact directed BFS and symmetric public-belief recursion confirm depth six for the displayed n=6 pairs at both Q=1 and Q=2 (not a universal n=6 horizon). Tested explicit strategies for Q=1,n=3..12 and Q=2,n=2..12.

Source read: GLOBAL_KNOWLEDGE_V1 main f50fe9ca; Enterprise Math main 1f17f4e3; P000, native X6, ACTIVE worldview, BRC usage and portable protocol. Native research identity denied (static read-only), so this branch note is only a preserved unreviewed auxiliary-model result, not a formal claim, review or X6 lift.

Full local evidence: EM_BRC_20261015_T3_ALLN_STRICT_PAIR_LOW_SUFFIX_EVIDENCE.zip; SHA256 9aafec0e47474ccc6d39434d080d33840e3e5450f6cb034a3acf1fb756ec3c2a.

Next: prove or disprove full H_n<=n at T=3,Q=1 or Q=2 for n>=6, preserving distinct hidden-source paths and observer semantics.
