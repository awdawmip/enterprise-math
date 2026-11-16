# EC49FQI — Exact BRC class-16943 prior-interpolation phase theorem at equal query prices

**Date:** 2026-11-16. **Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. **Frozen input pin:** \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. This result continues EC49FQH (PR #2536), without altering P000 or accepting a formal Task/Result.

## Exact finite model

The frozen BRC native class 16943 contains 310 original legal configurations and 141 distinguishable *complete named-root cost profiles* indexed \(i\). A profile occurs with multiplicity \(m_i\ge1\), \(\sum_i m_i=310\). Available adaptive scalar observations retain all 228 native physical indices: 144 full-terminal observations \(q=0,\ldots,143\) and 84 named-root observations \(q=144,\ldots,227\). There are 209 distinct response partitions. The identification target is the 141 *profiles*, not distinctions among original configurations that have the same full profile. Both types have fixed equal price \(r=t=1\).

For \(\lambda\in[0,1]\), change only the prior distribution:
\[
p_\lambda(i) = \frac{1-\lambda}{141}+\frac{\lambda m_i}{310}.
\]
At \(\lambda=a/b\), the exact integer weight used by the solver is \(W_i=310(b-a)+141am_i\) and total weight \(141\cdot310b\). No model, response partition or science pin is changed.

## Theorem: two sharp transitions on the entire prior continuum

Let \(V(\lambda)\) be the globally minimum expected query count across **all finite adaptive exact-identification trees**. Define these three feasible tree costs:
\[
\begin{aligned}
F_A(\lambda)&=(1-\lambda)\frac{296}{141}+\lambda\frac{757}{310},\\
F_B(\lambda)&=(1-\lambda)\frac{298}{141}+\lambda\frac{709}{310},\\
F_C(\lambda)&=(1-\lambda)\frac{300}{141}+\lambda\frac{690}{310}.
\end{aligned}
\]
Then, for every real \(0\le\lambda\le1\),
\[
\boxed{V(\lambda)=\min\{F_A(\lambda),F_B(\lambda),F_C(\lambda)\}}.
\]
The two **exact**, non-numerical switching parameters are \(\alpha=155/1847\) and \(\beta=620/3299\). On \([0,\alpha]\) the minimum equals \(F_A\); on \([\alpha,\beta]\) it equals \(F_B\); on \([\beta,1]\) it equals \(F_C\). At each shared endpoint the neighboring lines agree.

The three witnessing native decision trees have these integer unnormalized numbers of root and terminal reads:

| Witness tree | Uniform 141-profile prior (R,T) | Multiplicity 310-config prior (R,T) | First physical observation |
|---|---|---|---|
| A | (6, 290) | (6, 751) | 32 |
| B | (5, 293) | (5, 704) | 140 |
| C | (5, 295) | (5, 685) | 16 |

**All** globally optimal first-query physical indices are classified (not just one representative):

| Parameter region | All optimal first query indices |
|---|---|
| \(0\le\lambda<155/1847\) | {32,34} |
| \(\lambda=155/1847\) | {32,34,140,142} |
| \(155/1847<\lambda<620/3299\) | {140,142} |
| \(\lambda=620/3299\) | {16,23,140,142} |
| \(620/3299<\lambda<1\) | {16,23} |
| \(\lambda=1\) | {16,23,124,131} |

In particular, 140/142 are optimal precisely in the intermediate prior phase (plus its boundary ties) despite not being optimal at **either pure prior** \(\lambda=0\) or \(\lambda=1\). Indices 124/131 remain endpoint-only at \(\lambda=1\) when \(r=t\). This is a *prior* bifurcation, different from the EC49FQH two-price bifurcation with a fixed prior.

## Proof and exact validation boundary

For any non-singleton surviving set \(S\) of profiles and positive integer weights \(w_i\), write \(w(S)=\sum_{i\in S}w_i\). Let \(S_{q,z}\) be the fiber of query \(q\)'s response \(z\). The exact finite unrestricted Bellman recurrence at unit query price is
\[
C_w(\{i\})=0,\quad C_w(S)=w(S)+
  \min_{q:\ q\text{ splits }S}\sum_{z:S_{q,z}\ne\emptyset}C_w(S_{q,z}).
\]
All recursive masks are strict subsets. Non-informative queries cannot improve a positive-price strategy; partition-duplicate physical queries can be collapsed for internal optimization but their actual physical indices are restored for argmin reporting. This covers arbitrary finite decision-tree depth, not just bounded depth 3.

Two independently implemented exact integer dynamic programs evaluated the full native 228-action response set at **seven** rational priors:
\[
0,\quad 1/16,\quad 155/1847,\quad 1/8,\quad 620/3299,\quad 1/4,\quad 1.
\]
The unrestricted integer Bellman minima (before division by \(141\cdot310b\)) and all physical optimal first observations are:

| \(\lambda=a/b\) | Integer minimum | Complete optimal first indices |
|---|---:|---|
| 0 | 91760 | 32,34 |
| 1/16 | 1483137 | 32,34 |
| 155/1847 | 171802155 | 32,34,140,142 |
| 1/8 | 746629 | 140,142 |
| 620/3299 | 309466800 | 16,23,140,142 |
| 1/4 | 376290 | 16,23 |
| 1 | 97290 | 16,23,124,131 |

The original frozen master is SHA256 \`cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e\`; its native root-cost table is SHA256 \`a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f\`. Each full certificate contains a globally optimal response-labeled tree. Native response reconstruction and independent tree replay check each of the 141 distinct profiles, carrying the original multiplicities to all 310 configurations. The independent verifier recomputes *all seven* unrestricted Bellman values and complete first-query argmins instead of trusting only the primary solver's stored minima.

To extend the finite rational computation to **every real** \(\lambda\), observe that every fixed tree's expected cost is affine in \(\lambda\), and \(V\), as their pointwise infimum, is concave. At the four anchors \(0,\alpha,\beta,1\), the exact Bellman values agree respectively with the feasible lines \(F_A(0)\), \(F_A(\alpha)=F_B(\alpha)\), \(F_B(\beta)=F_C(\beta)\), \(F_C(1)\). On each pair of adjacent anchor parameters the concavity chord is a lower bound while its corresponding feasible tree line is an equal upper bound. Therefore \(V=F_A,F_B,F_C\) on their **entire** closed segments.

For completeness of *all* first queries, let \(L\) be a certified affine optimum over a segment \([a,b]\). The cost \(f_\pi-L\) of any fixed strategy \(\pi\) is affine and nonnegative at both endpoints. If it is zero at any strictly interior parameter, it must vanish identically over \([a,b]\). So every interior-optimal first query must also be in the intersection of the endpoint argmin sets. These intersections are precisely {32,34}, {140,142}, {16,23}. The three independent interior Bellman computations at \(1/16,1/8,1/4\) respectively realize **every** member of those intersections; each such witness stays optimal throughout the open segment by the same affine gap argument. The endpoint tie sets are independently exhaustive. This proves the full physical first-action classification.

Finally \(F_A=F_B\) gives \(2(1-\lambda)/141=48\lambda/310\), hence \(\alpha=155/1847\). Likewise \(F_B=F_C\) gives \(2(1-\lambda)/141=19\lambda/310\), hence \(\beta=620/3299\).

## Verification material and next mathematical question

Reproduction input: the self-contained EC49FQI evidence archive includes both frozen original inputs, seven full Bellman certificates with response-labeled trees, the primary mixed-prior solver, an **independently implemented scalar exhaustive Bellman verifier**, native data reconstruction, the exact continuum phase/first-action audit, their real execution logs and per-file SHA256 manifest. Tested outcomes: \`EC49FQI_INDEPENDENT_EXHAUSTIVE_BELLMAN_PASS 7\` and \`EC49FQI_FULL_PRIOR_CONTINUUM_AND_PHYSICAL_FIRST_ACTIONS_PASS\`. Finite exact, not peer-reviewed; no extrapolation to other BRC classes or physical systems.

**Next research**: study the two-parameter \((r/t,\lambda)\) phase diagram; first test whether the new index-140/142 intermediate prior phase persists under small unequal-price perturbations, and find exact rational/algebraic transition curves. Preserve all physical-index and descendant-query distinctions. The topic label \`RS-EC49AS\` has no current immutable publication (native continuation read \`FAILED / CANONICAL_REJECTED\`); this independent scientific contribution does **not** establish a formal Task CLAIM, Result or review. Previous author provenance: \`EM-DIRECT-E78124\`; original Activity \`RA-D62DDE05DA91C7CB0E8C8919\`; current native research write authority not inferred.
