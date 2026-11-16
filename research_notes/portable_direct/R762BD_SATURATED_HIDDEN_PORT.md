# R762BD — Saturated-axis filter, exact hidden-Port eligibility, and conditional BRC sampling

Date: 2026-11-15. Task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`; publication \`TP2-8B7E13C5904A2D6F1142\`. Author-side mathematical result, **NOT_REVIEWED**.

## Frozen scientific setting and source provenance

Source: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\` and its signed-X6 Cell, axis orthogonality, and triadic balance definitions. Taskbook: \`awdawmip/enterprise-math@d5eb171f15801f54c0659a2bbf4e42844ba2d527:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md\`. Immediate frontier: [R762BC PR #2474](https://github.com/awdawmip/enterprise-math/pull/2474), immutable scientific commit \`c497df6e460f0dde699ef357c9542feb849c4ee0\`.

We retain R762BC's *candidate* typed relational \`TRIADIC_CLOSURE_E\`: one Cell, one positive quantum weight, six unsigned native axes with arbitrary retained signs and named Port/Link identities, and a disjoint partition of \`3n\` named quanta into \`n\` unordered triples on three distinct axes. No classical vector-sum-zero hypothesis is introduced. The 120-degree \`PERP_E\` relation and minimum primitive arity three are the fixed P000 premises. Full named triples are preserved for future observers; any count-only statistic below is expressly observer-typed.

Let \`a=(a_1,...,a_6)\`, \`sum a_i=3n\`, \`0<=a_i<=n\`, \`n>=1\`. Put \`T(a)={i:a_i=n}\` (saturated axes), and \`supp(a)={i:a_i>0}\`. Fix two distinct observed **named** quanta \`u,v\` on axes \`r,s\` with \`a_r,a_s>0\`. Write \`J_{r,s}(a)\` for the possible unsigned axes of a third quantum sharing a triple with \`u,v\` in at least one complete partition, and \`D_n(a)\` and \`L_n(a;u,v)\` as in R762BC.

## BD1. Exact saturated-axis filter

For every admissible count profile,
\[
\boxed{J_{r,s}(a)=\{k\in\mathrm{supp}(a)\setminus\{r,s\}:\ T(a)\setminus\{r,s\}\subseteq\{k\}\}.}
\]
Consequently there are exactly three cases:

1. If \`T(a)\setminus\{r,s\}=\varnothing\`, **every** occupied third axis other than \`r,s\` is eligible.
2. If \`T(a)\setminus\{r,s\}=\{t\}\`, **only** axis \`t\` is eligible.
3. If \`|T(a)\setminus\{r,s\}|>=2\`, the hidden-axis fiber is empty.

**Proof.** The R762BC partition existence theorem says a residual population of \`3(n-1)\` records decomposes precisely when its largest axis count is at most \`n-1\`. Upon removing the observed axes \`r,s\` and proposed hidden axis \`k\`, a formerly unsaturated axis already has at most \`n-1\` records. Each formerly saturated axis must be one of the three removed axes. Thus the residual is feasible precisely when all saturation axes lie in \`{r,s,k}\`; also \`a_k>0\` and \`k\notin\{r,s\}\` are required. This proves both directions. The global assumption \`sum a_i=3n\` and \`max a_i<=n\` ensures the first case has some occupied third axis, since \`a_r+a_s<=2n<3n\`. QED.

**Sharp examples.** For \`n=2\`, \`a=(2,1,1,1,1,0)\`, the observed pair \`(r,s)=(3,4)\` forces hidden unsigned axis 1; the two named axis-1 records give \`L_2=2\` compatible partitions (the global total is \`D_2=6\`). For \`a=(2,2,1,1,0,0)\` and the same observed pair \`(3,4)\`, both saturated axes 1 and 2 remain outside the visible pair; hence \`J_{3,4}=\varnothing\` despite \`D_2>0\`.

## BD2. Exact joint matched-pair multiplicity at two saturated axes

Suppose \`a_r=a_s=n\`. Every triad must contain exactly one \`r\` record and one \`s\` record, and its third record belongs to the remaining population of size \`n\`. Fix \`0<=t<=n\` distinct labelled \`r\` records \`u_1,...,u_t\` and distinct labelled \`s\` records \`v_1,...,v_t\`. Impose that \`u_j,v_j\` occupy the same triad for all \`j\`.

For an ordered prescribed sequence of hidden **unsigned axes** \`k_1,...,k_t\notin\{r,s\}\`, let \`c_k\` count occurrences of axis \`k\` in that sequence and \`(m)_q=m(m-1)...(m-q+1)\`, with \`(m)_0=1\`. The exact number of compatible full named partitions is
\[
\boxed{H_t(k_1,...,k_t) = ((n-t)!)^2\,\prod_{k\notin\{r,s\}}(a_k)_{c_k}.}
\]

**Proof.** The \`t\` fixed pairs determine \`t\` distinct r-anchored triads. For the other \`n-t\` named \`r\` records, match the remaining \`s\` records in \`(n-t)!\` ways. For the prescribed hidden-axis sequence, assign pairwise distinct named third records from each axis \`k\` in \`(a_k)_{c_k}\` ways. Assign the remaining \`n-t\` named third records bijectively to the other \`r\` slots, in another \`(n-t)!\` ways. Every complete partition appears once because each triad is uniquely anchored by its named \`r\` member. QED.

Summing over the axis sequences gives the exact count for the fixed \`t\` partner relations:
\[
\boxed{\sum_{k_1,\ldots,k_t}H_t(k_1,\ldots,k_t)=n!(n-t)!}.
\]
Indeed the sum of the falling-factorial products over all ordered \`t\` choices equals \`(n)_t\`. As \`D_n=(n!)^2\` in this saturated case (R762BC), a *uniformly sampled full named partition* has probability \`1/(n)_t\` of satisfying all these partner relations. Conditional on those relations, its ordered hidden-axis sequence has probability
\[
\boxed{\Pr(k_1,\ldots,k_t\mid u_j\sim v_j\ \forall j)=\frac{\prod_k(a_k)_{c_k}}{(n)_t}.}
\]
This is precisely finite sampling **without replacement** from the retained third-source ledger. It is a combinatorial counting measure, not an assertion of physical stochastic dynamics.

For \`t=1\`, \`L_n(a;u,v)=n!(n-1)!\` and the hidden-axis distribution is \`a_k/n\`. For example, \`n=3\`, \`a=(3,3,1,1,1,0)\`, observed axes \`(r,s)=(1,2)\`: there are \`36\` full partitions, \`12\` containing one specified \`r,s\` pair, and exactly \`4\` of these for each hidden axis 3,4,5. For two specified matched pairs and a prescribed ordered third-axis sequence \`(3,4)\` there is one complete partition; sequence \`(3,3)\` has zero.

## BD3. Scope-typed BRC observer residual

For the observer \`O_{\mathrm{exist}}\` asking only *which hidden unsigned axes can complete a fixed named visible pair in some partition*, the triple \`(\mathrm{supp}(a),T(a),r,s)\` suffices by BD1. For the observer \`O_{\mathrm{count}}\` asking exact partition/lift counts, the six populations \`a\` and visible pair axes determine the results via R762BC and BD2. The *named future Link-membership observer* retains full partition provenance: distinct partitions with the same \`a\` can produce distinct future answers. Thus the compressed values are observer-safe only for their declared queries.

These results sharpen the existing four-/eight-source fiber analysis by adding global-resource constraints, without changing the original symmetry-unbroken assumptions of R762BA/BB. Signs are preserved as named attributes but do not constrain this candidate's triple eligibility; admitting a native signed closure predicate or a V17/V29/V39 scheduler will add actual semantic conditions.

## Verification

Run \`node research_notes/portable_direct/R762BD_SATURATED_HIDDEN_PORT_VERIFY.js\` with a standard Node.js runtime. It constructs every six-axis profile \`sum a_i=3n\`, \`n=1,2,3\`; independently enumerates **named triad partitions**, verifies existence, compares every occupied visible-pair hidden-axis set with BD1, and checks the full ordered multivariate BD2 coefficient formula for saturated pairs and \`0<=t<=n\`. Exact integer operations use BigInt, no floating approximation. The generated JSON certificate records 2,520 profiles, 5,925 visible-pair checks, 510 saturated-pair profile checks, and 6,270 ordered sequence tests; all passed. BD1–BD2 prove the claims for all \`n>=1\` under the stated candidate model; this finite verifier is an independent crosscheck.

## Next discriminating question

Identify an actual authenticated admissible signed \`TRIADIC_CLOSURE_E\` Cell/Link/Port update predicate and V17/V29/V39 transport action on named force histories. Ask whether its native sign and order restrictions preserve BD1's saturation filter, and if not, identify the smallest signed/ordered Port counterexample plus an enlarged sufficient provenance residual. Preserve the frozen P000 scientific pin; no working-truth/Foundation promotion or independent review has occurred.
