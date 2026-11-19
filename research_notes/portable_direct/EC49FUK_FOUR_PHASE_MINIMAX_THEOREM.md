# EC49FUK — Four consecutive exact composite-minimax phases for 15 clipped-price observations

Date: 2026-11-20 (Asia/Shanghai). Evidence: **AUTHOR_PROVED / EXACT_FRACTION_BERNSTEIN_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED**.

Frozen scientific input: BRC16943 at Source commit \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`, inherited unchanged from EC49FUJ Draft PR #2832 (\`5067cebf4e5a5f75847aeee0e3dcf31ba8da8c26\`). Scientific scope: its finite clipped-price **binary count observer**, not native X6/Bellman dynamics. No world axiom or parent optimization is modified. The declared observation map is a many-to-one readout; latent price origin, signed/joint native provenance and future operations remain at the parent level.

## Definitions and exact model

Fix 15 conditionally independent observations, equal H−/H+ prior probabilities, and one common unknown nuisance \(\varepsilon\le E=1048576/18958647\), shared between hypotheses and across trials. Write \(\theta=(1-a\varepsilon)^{-1}\in(0,\theta_E]\), \(a=2807259/163840\), \(\theta_E=31597745/1653649\); \(\theta=0\) denotes only \(\varepsilon\to-\infty\).

For normalized detector width \(0<x<1\), retain the inherited rational observer:

\[
T(\theta,x)=(1-x)(1-\beta x+\beta x\theta),\quad
u(\theta)=\frac{C}{H+B\theta},
\]
\[
\beta=\frac3{637},\quad (C,H,B)=(21829245984,45529434409,-456083905).
\]
Under H−, \(K\sim\operatorname{Bin}(15,p)\), \(p=1-T\). Under H+, \(K\sim\operatorname{Bin}(15,r)\), \(r=1-Tu\).
The two nuisance endpoints have

\[
u_I=\frac{21829245984}{45529434409},\quad
u_E=\frac{4822040484}{8132285009},\quad
T_I(x)=(1-x)(1-\beta x),\quad
T_E(x)=(1-x)(1+\eta x),\quad
\eta=\frac{141024}{1653649}.
\]

For \(j=1,\ldots,15\), define the exact count-tail discrimination gap

\[
F_j(z)=\sum_{k=0}^{j-1}\binom{15}{k}(1-z)^kz^{15-k},
\qquad D_j(\theta,x)=F_j(T(\theta,x))-F_j(T(\theta,x)u(\theta)).
\]
The risk of the count threshold \(\phi_j=\mathbf1_{\{K\ge j\}}\) equals \((1-D_j)/2\). The likelihood ratio at H+ versus H− for \(K=k\) at the endpoint is \(L_k=(r_E/p_E)^k u_E^{15-k}\), strictly increasing with k.

## Theorem: full K≥3,4,5,6 endpoint-Bayes phases are composite minimax

Let \(x_2\) be the exact second-count switching point from EC49FUJ, isolated by \(15172/10^6<x_2<15174/10^6\). For j=3,4,5,6, let \(x_j\) be the **unique** root in (0,1) of

\[
(1-u_E T_E(x))^j u_E^{15-j}=(1-T_E(x))^j.
\]

The newly certified rational brackets are:

| j | Strict lower bound for \(x_j\) | Strict upper bound for \(x_j\) | certifying interval \([0,L_j]\) | Bernstein lower bound \(b_{j,k}>\) |
|---|---:|---:|---:|---:|
|3|59034/1000000|59035/1000000|3/50|1/2000|
|4|121675/1000000|121676/1000000|123/1000|1/500|
|5|194151/1000000|194152/1000000|1/5|1/400|
|6|271729/1000000|271731/1000000|7/25|1/200|

For every real \(j\in\{3,4,5,6\}\) (integer j), every \(x\in[x_{j-1},x_j]\), and every finite common \(\varepsilon\le E\), the **deterministic threshold test**
\[
\boxed{\phi_j(K)=\mathbf1_{\{K\ge j\}}}
\]
is sharp composite-minimax among **all randomized tests of the complete 15-bit observation sequence**. Its risk is

\[
\boxed{R_{15}^{\mathrm{mm}}(x)=\frac{1-D_j(E,x)}{2}
=\frac12\left[1-F_j(T_E(x))+F_j(T_E(x)u_E)\right]}.
\]
The maximum risk is attained at the admissible nuisance \(\varepsilon=E\), strictly uniquely among finite nuisances for every interior width. At each boundary, endpoint Bayes ties may permit additional optimum rules, and the displayed deterministic rule remains minimax.

In particular, with the existing K≥2 theorem of EC49FUJ, **the whole interval \(x_2\le x\le x_6\) is now covered by four consecutive endpoint-minimax threshold phases**. No nuisance randomization is needed for these widths.

**Extra simplification at j=3.** Since \((15-3)/3=4\), the third-count boundary is the unique solution of the quadratic
\[
\boxed{T_E(x_3)=\frac{1-u_E^4}{1-u_E^5}},
\]
and \(59034/10^6<x_3<59035/10^6\).

## Proof

**1. Exact endpoint Bayes lower bound.** For fixed x, p_E increases strictly from 0 to 1, and
\[
\frac{r_E}{p_E}=u_E+\frac{1-u_E}{p_E}
\]
decreases strictly from infinity to 1. Thus each equation \(L_j(x)=1\), j=2,...,6, has a unique root in (0,1). The companion program checks the strict rational signs on both sides of all new roots, hence their ordering \(x_2<x_3<x_4<x_5<x_6\). On \([x_{j-1},x_j]\), \(L_{j-1}\le1\le L_j\); therefore \(\phi_j\) is Bayes-optimal for the **admissible** nuisance E. Consequently every randomized full-sequence test has worst-case risk at least \((1-D_j(E,x))/2\).

**2. Strict global concavity in the nuisance coordinate.** The derivative identities (valid for 2≤j≤14) are
\[
F'_j(z)=15\binom{14}{j-1}z^{15-j}(1-z)^{j-1}>0,
\]
\[
F''_j(z)=15\binom{14}{j-1}z^{14-j}(1-z)^{j-2}(15-j-14z).
\]
For each j=3,...,6 on its phase, \(0<x\le L_j\) and
\[
T\ge T_I(L_j)>\frac{15-j}{14},\qquad
0<S:=Tu\le u_E<\frac35<\frac{15-j}{14}.
\]
The exact rational checker verifies these bounds for all four L_j. Because \(B<0\), for \(\theta\in[0,\theta_E]\) we have \(T'>0\), \(u'>0\), \(u''>0\), \(S'=T'u+Tu'>0\), and \(S''=2T'u'+Tu''>0\). Consequently
\[
\boxed{
D_j''=F_j''(T)(T')^2-F_j''(S)(S')^2-F_j'(S)S''<0.
}
\]
Here \(F_j''(T)<0\), \(F_j''(S)>0\). Therefore \(D_j(\theta,x)\) is strictly concave in theta, and its minimum over the compactified nuisance interval lies at either theta=0 or theta=theta_E.

**3. Exact endpoint comparison for every real width.** Set
\[
J_j(x)=D_j(0,x)-D_j(\theta_E,x).
\]
Each \(J_j\) is a rational-coefficient polynomial of degree at most 30, built explicitly by substituting \(T_I,T_E,u_I,u_E\) into F_j. Put \(y=x/L_j\) and write its exact degree-30 Bernstein expansion
\[
J_j(L_j y)=\sum_{k=0}^{30} b_{j,k}\binom{30}{k}y^k(1-y)^{30-k},
\qquad
b_{j,k}=\sum_{i=0}^{k}a_{j,i}L_j^i\frac{\binom ki}{\binom{30}i},
\]
where \(J_j(x)=\sum_{i=0}^{30} a_{j,i}x^i\).
The attached standard-library **Fraction** program reconstructs all these coefficients independently of floating-point operations and verifies all **124/124 strict inequalities** \(b_{j,k}>c_j\), with \(c_j\) as in the table. Because the Bernstein basis is nonnegative and partitions unity, \(J_j(x)>c_j>0\) for every real \(0\le x\le L_j\), covering all four target phases.

Strict concavity and \(D_j(0,x)>D_j(\theta_E,x)\) now imply
\[
D_j(\theta,x)\ge D_j(\theta_E,x)
\]
throughout the entire allowed nuisance interval, with equality only at theta_E.

**4. Minimax matching.** The risk of \(\phi_j\) is at most its endpoint E risk; by step 1 every competitor's worst-case risk is at least that endpoint Bayes risk. The two bounds match. QED.

## Reproducibility, validation boundary and continuation

Run: \`python EC49FUK_FOUR_PHASE_MINIMAX_VERIFY.py\`. It checks the inherited \(x_2\) rational bracket, all four new switch brackets, exact rational derivative-domain bounds, polynomial identities, each of the 124 Bernstein inequalities, and an exact rational example risk per phase. Locally executed: **PASS**. This is an author exact-arithmetic certificate paired with the analytic argument, not an independently reviewed proof.

Previous completed results EC49FUI/J are reused without re-computation; their model validity and frozen Bellman source remain parent dependencies. The only compressed observer is the exact declared binary count K for the given fixed future task (classification of H−/H+ under this measurement), not a claim of information-complete native X6 factorization.

**Next unresolved unit:** classify the \(K\ge7\) threshold phase, then seek the first higher-count phase (if any) where endpoint E ceases to be least favorable, or identify a common certificate extending further. Recheck the shape of \(F_j''\) and the typed observer coverage when changing j. No formal immutable Task/CLAIM, native Result, or independent mathematical Review is implied by this portable result. The original Researcher and Source ancestry remain unchanged.
