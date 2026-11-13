# R126 — Rotation normal form for the signed S23 directed-arc observer

Date: 2026-11-13 (Asia/Shanghai). Author-side auxiliary mathematical result. Prior R124 source: \`9357b4bf473ca21a92b9a0bee09a59eaa2616c28\`; R125 correction/extension: \`a99ea452ce1972b36319fd1a8509b0c0ec89214a\`. Frozen science pin: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. P000, ACTIVE worldview, original native X6 semantics and task-owner state unchanged.

## R126.1 Exact directed-circle rotation

Let \`{v}=v-floor(v)\`. For \`u,v in [0,1)\`, let \`[u,v)_directed\` mean \`[u,v)\` when \`u<v\`, \`[u,1) union [0,v)\` when \`u>v\`, and the **empty set** when \`u=v\`.

For all real \`y,A,B\`,

\`{y} in [{A},{B})_directed  iff  0 <= {y-A} < {B-A}\`.

Proof: translation by \`-{A}\` on the oriented circle \`R/Z\` sends the positively directed arc to \`[0,{B-A})\`. It is a bijection, preserves half-open endpoints and handles zero-length arcs exactly. No approximation or endpoint exception occurs.

## R126.2 Three-integer exact feasibility for any signed affine endpoint coefficients

Let \`x,l,h in Q\`, \`l<h\`, \`a,c,j,N,d in Z\`, and \`m>=1\`. On \`I=(l,h)\`, define the S23 auxiliary observer

\`Y_i(theta)=x+(N+i*d-j)*theta;\`
\`M_i(theta)=1[{Y_i(theta)} in [{a*theta},{c*theta})_directed]\`, \`0<=i<m\`.

Put \`E=c-a\`, \`Z_i(theta)=x+(N+i*d-j-a)*theta\`, and \`L(theta)={E*theta}\`. By R126.1,

\`M_i(theta)=1[{Z_i(theta)}<L(theta)]\`.

For a prescribed joint bit word \`b in {0,1}^m\`, define the finite floor-word vocabulary

\`P_m={(floor(alpha+i*beta))_(i=0,...,m-1): 0<=alpha,beta<1}\`.

For each \`w in P_m\`, the following is a **single** rational mixed-linear feasibility system with only three integer unknowns \`n,k,r\` and one real \`theta\`:

- \`l<theta<h\`;
- \`0<=Z_0(theta)-n<1\`, \`0<=d*theta-k<1\`, \`0<=E*theta-r<1\`;
- \`z_i=Z_i(theta)-n-i*k-w_i\` and \`0<=z_i<1\` for every i;
- if \`b_i=1\`, impose \`z_i<E*theta-r\`; if \`b_i=0\`, impose \`z_i>=E*theta-r\`.

**Soundness:** the first three floor inequalities identify the true \`n=floor(Z_0)\`, \`k=floor(d*theta)\`, \`r=floor(E*theta)\`. The \`z_i\` bounds force \`n+i*k+w_i=floor(Z_i)\`, so \`z_i={Z_i}\` and \`E*theta-r=L(theta)\`. Hence all prescribed bits are genuine.

**Completeness:** for every genuine witness \`theta\`, take these three true floors, \`alpha={Z_0}\`, \`beta={d*theta}\` and \`w_i=floor(alpha+i*beta)\`. This \`w\` belongs to \`P_m\` and satisfies every inequality. Thus feasibility of the original joint signature equals the union of at most \`|P_m|\` such systems. There is **no** separate endpoint order/equality case, and no independent binary segment choice per bit. This includes negative/zero \`d\`, negative coefficients, \`a=c\`, endpoint collisions and wrapped arcs.

## Complexity and witness recovery

There are O(m) affine constraints per \`w\`. Rational Fourier–Motzkin elimination of the single real \`theta\` produces O(m^2) rational inequalities in \`n,k,r\`, with strictness preserved if either contributing bound is strict. Clearing positive denominators and transforming strict integral comparisons to inclusive bounds shifted by one yields exact **three-variable integer linear feasibility**. Pairwise elimination and rational bit sizes are polynomial in the explicit input lengths.

The finite mechanical-word count used and attributed in R121-LIT is

\`|P_1|=1; |P_m|=1+sum_(v=1)^(m-1) (m-v)*phi(v)=Theta(m^3) (m>=2)\`.

Therefore an exact fixed-**three**-dimensional ILP algorithm gives a polynomial-bit-cost decision-and-rational-witness procedure for **one explicitly supplied m-bit word**, even with arbitrary signed \`a,c,j,N,d\` of large magnitude. The classical fixed-dimensional ILP theorem is H. W. Lenstra Jr., *Integer programming with a fixed number of variables*, Mathematics of Operations Research **8** (1983), 538–548, DOI \`10.1287/moor.8.4.538\`. Given a feasible integer triple, recover \`theta\` by intersecting the original rational affine bounds, taking an interior rational midpoint if available or a common rational weak endpoint when the intersection is a singleton.

The earlier R125 four-integer bound had \`O(2^m*m^3)\` feasibility systems per prescribed word because of endpoint branch choices. R126 uses \`O(m^3)\` three-integer systems for the same Boolean observer, preserving its original \`a,c\` input for any later provenance-sensitive operation. Explicit enumeration of **all** attained m-bit words additionally pays its output cost. The bundled checker is a finite exact enumerator, not a production Lenstra solver or a runtime benchmark.

## R126.3 Two-integer special family

If \`c-a=d\`, then \`r=k\`, so substitute \`r=k\` in the same constraints. Only **two** integers remain, with no further branch. If \`a=c\`, then \`L(theta)=0\` and every bit is zero. More generally \`c-a=s*d\` with fixed signed integer \`s\` implies

\`r=s*k+floor(s*beta)\`, \`beta=d*theta-k in [0,1)\`.

Branching on the at most \`|s|+1\` values of \`floor(s*beta)\` gives exact two-integer systems. This is a scoped Boolean observer reduction; it does not delete native relational or later-operation source information.

## Independent finite tests and predecessor edge case

\`check_r126.py.gz.b64\` contains a gzip/base64-encoded standalone Python 3 verifier using \`fractions.Fraction\` only. It compares the literal directed arc to the rotated observer; independently computes all realized joint words by **complete affine critical cuts** of \`Z_i\`, \`Z_i-E*theta\`, \`E*theta\`, including singleton cuts; and compares them with exhaustive bounded \`n,k,r\` feasibility using exact weak/strict interval intersections. It uses the safe floor enclosure \`floor(min(endpoint values))..floor(max(endpoint values))\`, incorporating R125's correction of R123's constant-integral false negative.

Deterministic seed \`12620261113\` yielded \`R126_ROTATION_THREE_INTEGER_PASS\` with 40 signed full comparisons, 1,054 critical-atom representatives, 352 exhaustive prescribed word checks, 174 valid three-integer witnesses, 406 direct rotation checks, seven \`a=c\` instances, 13 negative d and six zero d instances; six separate ~100-digit signed forward certificates. A further 24-case exact \`c-a=d\` comparison found 140 valid two-integer witnesses, matching all reference joint word sets. Total checked candidate systems: 39,181; total exact recovered witnesses: 314. Full integer exhaustive testing is **finite** evidence; the universal statements are proved above.

## Scope and next frontier

The translation is an exact invertible circle coordinate change for each theta. It preserves the joint S23 membership observer and the original parameters and witnesses. It does not establish native X6 Cell/Link/Port permission or mathematical reviewer acceptance.

Next: implement a genuine exact three-dimensional lattice-feasibility solver with strict-facet witness recovery and compare end-to-end coefficient preprocessing, bit operations, wall-clock runtime, provenance handling and memory against R125 four-dimensional branching. Probe signed large endpoints, coincident endpoint fibers and nonproportional E,d special families for further rank reduction.
