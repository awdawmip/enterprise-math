# X6 R70 — Finite cone reduction for all weighted positive-BRC star moments; exact D=4 five-step precision staircase

Date: 2026-11-21 (Asia/Shanghai). Scientific status: CONDITIONAL_AUTHOR_PROOF / EXACT_RATIONAL_FINITE_AUTHOR_CHECK / NOT_INDEPENDENTLY_REVIEWED.

Research line: R61–R69, extending R68's heteroscedastic common-bias ambiguity formula and R69's D=3 five-vector special case.

Frozen scientific premise: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`. Preserve six signed native axes, independent time, native Cell and Link provenance, the joint-observer preservation constraint and whole-triad \`TRIADIC_CLOSURE_E\`. The model below concerns a **conditional, typed two-source BRC observation**, not an asserted native physical reset law. All claims of histogram sufficiency are restricted to this observation and target; the original labeled network remains available for future Cell/Link operations.

## Model and sharp weighted ambiguity radius

Fix integers \`p >= D >= 2\`. A relation between \`p\` named A Ports and B Ports has A-row degrees \`d in {0,...,D}\`, histogram \`c_d\` and normalized positive-weight star moments \`m_t = sum_d c_d d^t\` for \`t=1,...,D\`. The repeated B resets are independent conditional on the **same** named A Port. Known positive branch weights \`u,v\` allow normalization from \`Z_t=(uv)^t m_t\`; no signed cancellation is used.

The observed channels are \`Y_t=m_t+b+e_t\`, with one unknown shared \`b\`, independent bounds \`|e_t| <= eta*w_t\`, and arbitrary \`w_t>0\`. The target is the high-degree histogram \`(c_2,...,c_D)\`.

For two distinct target histograms write \`a_d=c_d-c'_d\` (\`d=2,...,D\`) and
\`q(a)=max(sum_d max(a_d,0), sum_d max(-a_d,0))\`. Exactly those nonzero integer differences with \`q(a)<=p\` are realizable: assign positive and negative degree counts to opposite models and pad degree-zero A rows to \`p\`; choose the first \`d\` distinct B Ports for each row of degree \`d\`.

Let \`z_1(a)=0\`, \`z_t(a)=sum_{d=2}^D a_d(d^t-d)\` for \`2<=t<=D\`, and \`G_{ij}(a)=|z_j(a)-z_i(a)|\`. The unknown common bias and free degree-one residual have been eliminated. Two models' bounded-error observation boxes intersect exactly when
\`2 eta (w_i+w_j) >= G_{ij}(a)\` for every \`1<=i<j<=D\`. Consequently, extending R68,

\`\`\`
eta*_{p,D}(w) =
 min_{a in Z^(D-1), a != 0, q(a)<=p}
    (1/2) max_{1<=i<j<=D} G_ij(a)/(w_i+w_j).
\`\`\`

At the threshold ambiguity is possible; strictly below it all high-degree histograms are identifiable. The formula makes no assertion that a particular numerical recovery algorithm is efficient.

## Theorem A — explicit, weight-independent finite reduction in every dimension

Put \`n=D-1\`, \`M=D^D-D\` and
\`Q_D=n^2 (n-1)! M^(n-1)\` (including the convention \`0!=1\`). For **every** \`p>=D\` and every positive real weight vector \`w\`, the minimum in the displayed formula is unchanged when the search is restricted to

\`\`\`
0 < q(a) <= min(p,Q_D).
\`\`\`

Moreover there is a finite set \`H_D\` depending **only** on \`D\`, such that for every \`p,w\` at least one optimal difference belongs to \`{h in H_D : q(h)<=p}\`. The threshold therefore stabilizes simultaneously for all positive weight profiles once \`p>=Q_D\`. The explicit \`Q_D\` is conservative, not claimed sharp.

**Proof.** The integer linear map \`B:Z^n -> Z^{D(D-1)/2}\` sends \`a\` to the signed differences \`z_j(a)-z_i(a)\`. Its coefficients are \`d^j-d^i\` (\`2<=d<=D,\ 1<=i<j<=D\`) and have modulus at most \`M\`. Form the stacked map \`T(a)=(a,Ba)\`. Fix the sign (positive, zero or negative) of each coordinate of \`T(a)\`. Its inverse-image sign cone \`C\` is a pointed rational polyhedral cone: it is pointed because the identity block fixes signs of the original \`a\` coordinates.

Each extreme ray of \`C\` has a primitive integral generator \`r\`. In the ambient dimension \`n\`, a ray is determined by \`n-1\` independent active integer hyperplanes from the rows of \`T\`. The cofactor construction gives a nonzero integer direction with every component bounded by \`(n-1)!M^(n-1)\`; division by its gcd only decreases that bound. Thus \`||r||_1 <= n(n-1)!M^(n-1)\`. This also holds for lower-dimensional cones because their defining equality hyperplanes contribute active independent rows.

Triangulate \`C\` into finitely many simplicial subcones using its extreme rays. Any nonzero integer \`a in C\` lies in one and has \`a=sum_{k=1}^s lambda_k r_k\`, \`lambda_k>=0\`, \`s<=n\`. If some \`lambda_k>=1\`, take \`h=r_k\`; then \`a-h in C\`. If all \`lambda_k<1\`, take \`h=a\`, whose \`l1\` norm is at most \`sum_k ||r_k||_1<=Q_D\`. In either case \`h\` is a nonzero integer vector, \`q(h)<=q(a)\`, \`q(h)<=Q_D\`, and each \`|B h|_{ij}<=|B a|_{ij}\`: all coordinates of \`T(a)\` and of the conformal summands have fixed signs. Hence for any positive \`w\`, the weighted max-score of \`h\` is no greater than that of \`a\`. Finiteness follows by collecting all \`0<q(h)<=Q_D\` (or Pareto-minimal members); it is independent of \`p,w\`. QED.

This is a constructive finite reduction rather than a small-complexity claim; it generalizes the weight-independent finite-candidate phenomenon of R69 without assuming that five candidates suffice beyond \`D=3\`.

## Theorem B — exact D=4 precision staircase for w=(50,1,1,1)

For every integer \`p>=4\`, when \`D=4\` and channel precision weights are \`w=(50,1,1,1)\`, the globally sharp radius is

| Port count p | exact eta* |
|---|---:|
| p=4 | 3 |
| p=5 | 2 |
| 6<=p<=10 | 3/2 |
| 11<=p<=38 | 1/2 |
| p>=39 | 2/17 |

**Proof.** Write \`a=(a_2,a_3,a_4)\` and \`z=(0,z_2,z_3,z_4)\`, with
\`\`\`
[z2,z3,z4]^T =
[ 2,  6,  12 ] [a2]
[ 6, 24,  60 ] [a3]
[14, 78, 252 ] [a4].
\`\`\`
All \`z_t\` and their differences are even integers. Three low-weight pairs \`(2,3),(2,4),(3,4)\` each have denominator \`w_i+w_j=2\`. Therefore if \`eta_pair(a)<1/2\`, necessarily \`z_2=z_3=z_4=C\`. The displayed nonsingular integer matrix yields exactly
\`a=C(3,-4/3,1/4)\`. Integrality forces \`C=12k\`, \`a=k(36,-16,3)\`, so \`q(a)=39|k|\`. Nonzero such \`a\` requires \`p>=39\`, and the smallest possible radius on that sublattice is \`(1/2)*12/51=2/17\`. The \`k=1\` candidate achieves this value at \`p=39\`; every candidate outside the equal-low-channel sublattice has radius at least \`1/2\`. This proves the entire \`p>=39\` plateau and the lower bound for \`11<=p<=38\`. The candidate \`a=(10,-5,1)\`, \`q=11\`, \`z=(0,2,0,2)\`, has radius \`1/2\`, proving the middle plateau.

For the only remaining \`p=4,...,10\`, exhaust all integer \`a in [-p,p]^3\` with \`0<q(a)<=p\` and evaluate the displayed rational radius using exact fractions. The accompanying standalone verifier enumerates respectively \`308,560,922,1414,2056,2868,3870\` feasible signed vectors and returns minima \`3,2,3/2,3/2,3/2,3/2,3/2\`. Every feasible \`a\` is covered, because \`q(a)<=p\` implies \`|a_d|<=p\`; the implementation performs exact integer and rational arithmetic and asserts every result. This is a finite exhaustive certificate with explicit domain, completing the proof. QED.

At \`p=39\` the winning difference \`(36,-16,3)\` has \`z=(0,12,12,12)\`: the cheap channels agree exactly while the sole noisy channel carries the residual. This is a concrete new aliasing pattern beyond the prior D=3 five-vector theorem.

## Validation, provenance, scope

Reproduce with Python 3 standard library: \`python x6_r70_weighted_cone_d4_verify.py\`. The script uses \`fractions.Fraction\`, enumerates all signed candidates for \`p=4..10\`, verifies two analytic witnesses, and emits \`x6_r70_weighted_cone_d4_results.json\`. Its exact observed execution returned \`PASS\` (seven exhaustive domains). The general all-\`D\` cone proof is deductive, not validated by this finite computation.

Theorem A uses the conventional mathematical fact that a pointed rational polyhedral cone admits a finite ray triangulation; this is supplied within the proof's stated mathematical model, not an extra P000 physical law. Neither theorem establishes an original native Cell/Link/triadic reset map. In the frozen P000 setting, preserve the full joint relation and event provenance wherever later observations can distinguish them.

Previous exact references: R68 \`2026-11-21_x6_r68_heteroscedastic_common_bias_star_moments.md\` and R69 \`2026-11-21_x6_r69_d3_heteroscedastic_five_vector_theorem.md\`, in \`research_notes/portable_direct/\`. R70 is independent portable derivation, not an authorized formal Result/review/Claim.

Research provenance: historical \`EM-X6-214D9C\`; Activity \`RA-545183ADD4EF71C3E4698AEE\`; original Sites SID \`MCP-d467c19ce42d4d7fa65a3901db1cf6b2\`. Current formal X6 ownership belongs to a separately registered lane; no transfer or claim is inferred.

## Open questions

1. Compute a **small** canonical Hilbert/Pareto generating set \`H_4\` (or stronger sharp saturation \`P_4\`) rather than the deliberately conservative \`Q_D\`; characterize the chambers of weight space selecting each witness.
2. Compare the resulting observer compression with full Port/Cell/Link identities under admitted \`TRIADIC_CLOSURE_E\` and real reset/guard dynamics.
3. For \`D>=5\`, seek geometric/combinatorial bounds substantially below \`Q_D\` and explicit asymmetric-weight staircases.
