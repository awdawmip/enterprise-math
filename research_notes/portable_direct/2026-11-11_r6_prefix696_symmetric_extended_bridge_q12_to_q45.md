# PREFIX-696-R6 — BRC crossing: symmetric extension and strict concavity for 12 ≤ q ≤ 45

Date: 2026-11-11 (Asia/Shanghai). Frozen scientific source: enterprise-math commit f42f2906d77f24085c123f3ccfe9667d41caa96d. Status: AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED. Independent TASK_RESEARCH contribution; this publication makes no shared Task CLAIM.

## Definitions and inherited exact inputs

The frozen 189-level, 9,529-live-cell survivor model preserves the labelled joint-clock observer branches Y(z,z) and Y(0,z) and their exact mean/variance. Put

\[
A(z)=\mathrm{Var}(Y(z,z))-\mathrm{Var}(Y(0,z)),\quad B(z)=E[Y(z,z)]-E[Y(0,z)],
\]
\[
F_q(z)=qA(z)-B(z),\qquad Q(z)=B(z)/A(z).
\]

The sampled-variance difference is q F_q(z) for q>0. These two parameters are an *auxiliary observer chart*, not native spatial axes or physical time. PREFIX-693/694 certified strict bridge uniqueness, convex Q and concave inverse on I=[0.0528706,0.0530659] for q=12 through q=24. PREFIX-695 independently replayed all inherited integer-kernel jets and reconciled the A fifth-derivative floor.

Let b=53/1000, h=1/6250, and

\[
J=[b-h,b+h]=[1321/25000,1329/25000]=[0.05284,0.05316].
\]

**Theorem 696.1.** For every real z in the enlarged closed bridge J,

\[
0.16<A(z)<0.72,\quad -1870<A'(z)<-1490,\quad |A''(z)|<5600000;
\]
\[
7.87<B(z)<7.92,\quad 128<B'(z)<129,\quad |B''(z)|<1500.
\]

Consequently, Q is analytic, strictly increasing and strictly convex on J, and

\[
\boxed{Q''(z)>8000000\quad(z\in J).}
\]

**Theorem 696.2.** Every *real* q in the entire closed band [12,45] has exactly one crossing z(q) in the open interval (0.05284,0.05316): F_q(z(q))=0. On (12,45), z(q) is real analytic, strictly increasing and strictly concave, in particular z''(q)<0. This strictly extends the former certified spatial bridge at both endpoints and the previously certified upper q=24 to q=45.

## Reproducible proof: exact global jets and Taylor inequalities

At b, define integer floors a_j=floor(10^8 A^(j)(b)) and c_j=floor(10^8 B^(j)(b)). The verified PREFIX-695 exact 189-row integer-kernel replay returned, for j=0,...,5,

a = [44000296, -168056589514, -6667624082229, 39352687679231, 3189837819999830, -36266294695911132]

c = [789752024, 12845959424, -99127959112, -1326952329685, -14895243921676, -1960958310350017].

PREFIX-693 proved global sixth-derivative envelopes on [0,1]:

\[
M_A=201273663850076722544640,\quad M_B=17896441402901698560.
\]

For G=A or B, write g_j for the matching integer floors and M_G for its sixth-derivative bound. Then g_j/10^8 <= G^(j)(b) < (g_j+1)/10^8. For each k=0,1,2, Taylor's theorem gives, uniformly for |z-b|<=h,

\[
\frac{g_k}{10^8}-E_{G,k}<G^{(k)}(z)<\frac{g_k+1}{10^8}+E_{G,k},
\]
\[
E_{G,k}=\sum_{j=k+1}^{5}\frac{\max(|g_j|,|g_j+1|)}{10^8}\frac{h^{j-k}}{(j-k)!}
+\frac{M_Gh^{6-k}}{(6-k)!}.
\]

The attached checker evaluates these six exact rational enclosures, proving all strict inequalities of Theorem 696.1 without floats.

The derivative identity

\[
Q''=\frac{N}{A^3},\quad
N=B''A^2-BAA''-2B'AA'+2B(A')^2
\]

has its third numerator term strictly positive because B'>0,A>0,A'<0. Discarding that favorable contribution and using the preceding bounds gives the exact strict lower bound

\[
N>2(7.87)(1490)^2-(7.92)(0.72)(5600000)-1500(0.72)^2
=\frac{15050782}{5}>3000000.
\]

Since 0<A<0.72, the exact rational inequality

\[
Q''>\frac{(15050782/5)}{(0.72)^3}>8000000
\]

proves strict convexity. Likewise Q'=(B'A-BA')/A²>0.

## Endpoint signs and entire continuous parameter range

At t=±h, construct lower/upper fifth-order Taylor sums with the correct sign for each term t^j/j! and the two possible 10^8 jet-floor endpoints, then add the sixth-order remainder ±M_G|t|^6/6!. Denote the resulting exact bounds by A_-(b+t)<A(b+t)<A_+(b+t) and B_-(b+t)<B(b+t)<B_+(b+t).

Exact Fraction cross-products establish

\[
F_{12}(b-h)>12A_-(b-h)-B_+(b-h)
=\frac{4297200825270804597454052487}{7629394531250000000000000000}>0.56
\]

and

\[
F_{45}(b+h)<45A_+(b+h)-B_-(b+h)
=-\frac{324326338261353735951982633}{7152557373046875000000000000}<-0.045.
\]

Because A>0 across J, for any real 12<=q<=45,

\[
F_q(b-h)=F_{12}(b-h)+(q-12)A(b-h)>0,
\]
\[
F_q(b+h)=F_{45}(b+h)+(q-45)A(b+h)<0.
\]

On the whole bridge F'_q=qA'-B'<-1490q-128<0. Intermediate-value existence and strict derivative sign imply exactly one crossing for every such q. Q'>0 and the analytic inverse theorem give z'(q)>0 and

\[
z''(q)=-Q''(z(q))/Q'(z(q))^3<0.
\]

This completes both theorems.

## Verification, scope and continuation

Companion Python checker: research_notes/portable_direct/PREFIX696_R6_SYMMETRIC_BRIDGE_CERTIFICATE.py; its generated result: PREFIX696_R6_RESULTS.json. All comparisons use standard-library Fraction with integer-floor inputs; local author-side execution returned ALL_CHECKS_PASS PREFIX696-R6. The method is a polynomial analytic bound on the exact BRC-produced auxiliary readout; it does not replace the native BRC update by classical Taylor evolution, run π/trigonometric reference calculations, or claim native residual attribution. It *reuses* PREFIX-695 jets and PREFIX-693 sixth-order certificates rather than independently recomputing survivor rows this round; there is no independent review or formal Result/Review acceptance.

Next scientific unit: refine q endpoints through exact endpoint BRC observer evaluation, or establish local Bernstein certificates beyond J towards 0.052<=z<=0.054. Then feed the enlarged one-parameter crossing geometry into the PREFIX-675 mother objective: global sampled-variance maximization over the *auxiliary* triangular chart 0<=p<=z<=1/2. Preserve frozen science pin, P000 and ACTIVE worldview.
