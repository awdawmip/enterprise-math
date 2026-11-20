# X6 R53 — Parametric globally optimal BRC Port-ambiguity radius

Date: 2026-11-20 (Asia/Shanghai). Line: RS-X6-NATIVE-TIME-DYNAMICS; historical researcher EM-X6-214D9C; historical Activity RA-545183ADD4EF71C3E4698AEE. Scientific status: CONDITIONAL_AUTHOR_PROOF / EXACT_FRACTION_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.

## 1. Fixed scientific input and problem

Keep frozen P000 premises unchanged. This statement is about the conditional R44 once-only, two-named-source, whole-triad p-Port positive BRC branch grammar, including candidate release R and reoccupation T. At the rooted observer, all A_i/B_i are projected to F, while R and T remain public. The exact four short-word BRC masses in order (F,FT,FF,FRF) are the established R47 coefficients:

\[
A_p(S,P)=(pS,(p-1)S,2(p^2-1)P,2pP),\quad
S=\alpha+\beta,\quad P=\alpha\beta,\quad \alpha,\beta>0.
\]

A measurement has one unknown common real additive bias b, plus four independent errors of absolute value at most eta:

\[
z=A_p(S,P)+b\mathbf1+\varepsilon,\quad |\varepsilon_i|\le\eta.
\]

A competing Port number q may have its own strictly positive source weights and common bias. For one fixed true (p,S,P), define eta_crit as the infimum radius at which the same four-channel vector z is consistent with the true system and some rival integer q != p. Equality counts whenever an admissible witness exists.

R51 corrected the R50 contrast norm and refuted its old claimed radius; R52 gave one exact optimum at (p,S,P)=(4,1,99/10000). We extend this instance to a full interval.

## 2. New exact theorem

**R53 (parametric global optimum).** For p=4, S=1 and every real number

\[
\boxed{\frac{19}{2158}\le P<\frac{79}{378}},
\]

the true source weights are the positive roots of u^2-u+P=0. Against **every** integer q>=1, q!=4, and all rival positive weights and arbitrary common offsets, the exact minimax ambiguity radius is

\[
\boxed{\eta_{\mathrm{crit}}(P)=\frac{19+42P}{400}}.
\]

Every measurement with eta strictly below this number uniquely identifies p=4; at equality a q=5 model gives the same measurement. In this interval eta_crit increases strictly with the source-weight product P.

### Proof I — exclude all q other than 5

For q>=1 write C_q=q^2-q-1 and use R51's corrected offset-invariant BRC contrast

\[
L_q(z)=(d-h)-C_q\left[(x-y)-\frac{x-h}{q}\right].
\]

For every exact q-model, L_q(A_q+b\mathbf1)=0. For q>=2 its exact coefficient l1 norm is N_q=2q(q-1), with coefficient vector

\[
(-C_q(1-1/q),\,C_q,\,1,\,-1-C_q/q).
\]

If a single measurement is within eta of both a true model and a q-model, then

\[
\eta\ge\frac{|L_q(A_4(1,P))|}{2N_q}
=\frac{|4-q|\,[C_q+2P(4q+1)]}{4q^2(q-1)}. \tag{1}
\]

For q=5 this is (19+42P)/400. For q=2 the right side is at least 1/8; for q=3 at least 5/72. For every integer q>=6 it is at least 29/360, since the positive function (1-4/q) C_q/[4(C_q+1)] increases with q>=6. The upper interval condition gives

\[
\frac{19+42P}{400}<\frac5{72}<\frac{29}{360}<\frac18.
\]

For q=1, the true BRC difference D-H=22P>0, but any positive one-Port candidate has D-H=-2P_1<0. Each radius-eta four-channel error box changes a D-H difference by at most 2eta. Overlap requires 22P+2P_1 <=4eta, hence strictly eta>11P/2. The lower interval condition is equivalent to (19+42P)/400 <= 11P/2, so q=1 is excluded at and below the proposed eta_crit.

These cases cover all positive integers q other than 4 and 5, without a numerical enumeration cutoff. Equation (1) excludes q=5 below eta_crit.

### Proof II — an admissible q=5 witness at equality

Construct a five-Port rival of total positive weight S_5, product P_5, and common offset b_5:

\[
S_5=\frac{81-42P}{100},\qquad
P_5=\frac{1+118P}{200},\qquad
b_5=\frac{378P-29}{200}.
\]

These parameters produce two strictly positive source weights. Indeed S_5,P_5>0 and their discriminant is

\[
S_5^2-4P_5=\frac{1764P^2-30404P+6361}{10000}>0.
\]

The numerator is decreasing across the theorem's closed endpoint enclosure [19/2158,79/378], and at 79/378 it equals 47500/567>0.

Define the true mass vector V=(4,3,30P,8P), and let W=A_5(S_5,P_5)+b_5\mathbf1. Direct exact substitution gives

\[
V-W=2\eta_{\mathrm{crit}}(P)(1,-1,-1,1).
\]

Consequently the **same** measurement z=(V+W)/2 is within eta_crit of both admissible systems, with opposite extremal channel errors. Explicitly,

\[
z=\left(\frac{1581-42P}{400},\frac{1219+42P}{400},
\frac{19+12042P}{400},\frac{3158P-19}{400}\right).
\]

Thus the necessary lower bound is attained by a positive-weight rival with a common offset. This proves the global optimum and the equality statement. QED.

At P=99/10000 the exact radius is 97079/2000000, reproducing R52 and extending its one-point result to a continuum of exact optima.

## 3. Reproducibility and scope

Executable Python Fraction checker: research_notes/portable_direct/x6_r53_parametric_ambiguity_verify.py.
Exact JSON: research_notes/portable_direct/x6_r53_parametric_ambiguity_results.json.

The verifier checked 252 exact rational parameter instances, including the lower endpoint and R52's instance. It recalculated root BRC mass coefficients, rival discriminants, common-bias witnesses, all four simultaneous errors, and contrast exclusions for q=2,...,1000, with PASS. The **unbounded** q>=6 exclusion is proved by the monotonicity argument above; finite tests corroborate that proof. This is author proof plus author computation; no independent reviewer or formal checker is claimed.

The source observer is **positive BRC path mass**, not Boolean support, source-labeled histories or signed amplitudes. The p-Port grammar is conditional; neither its candidate R/T events nor its four-Port instance have yet been mapped to an admissible native frozen-P000 TRIADIC_CLOSURE_E Cell/Link/Port trace in a defined 3D slice of the six-dimensional space. Time here denotes event ordering. The frozen science input has not been altered.

## 4. Next mathematical questions

Determine the exact ambiguity radius below P=19/2158 (where the q=1 sign gap becomes competitive) and above P=79/378 (where q=3 becomes competitive), with explicit positivity/discriminant feasibility rather than contrast bounds alone. Generalize the correlated common-offset Chebyshev projection to arbitrary p,S,P and classify attained versus unattained infima. Independently test any proposed R/T native triadic operation against Cell, Link, named Port, provenance and whole-triad constraints, before attributing these conditional BRC results to physical time dynamics.

Source lineage: R51 correction (2026-11-20_x6_r51_r50_contrast_norm_erratum.md, blob 4154d05d451e8c8929aa2f50a2595c2730479d89); R52 exact instance (2026-11-20_x6_r52_exact_optimal_ambiguity_radius.md at immutable Source c0a755942af9bbfb7a27a1159731e1cc233bc0d6); R47 BRC coefficient law; frozen P000 and current portable research protocol. Historical researcher/Activity references record provenance, not a new execution CLAIM or PROGRESS.
