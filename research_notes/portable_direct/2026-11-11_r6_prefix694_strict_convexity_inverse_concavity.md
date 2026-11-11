# PREFIX-694-R6 — Strict convexity of the BRC crossover parameter and concavity of its inverse

Date: 2026-11-11 (Asia/Shanghai). Scientific input frozen at `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Mode: independent TASK_RESEARCH author derivation, **not** an alteration of the shared owner/CLAIM. Status: `AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED`.

## 1. Model and reusable certified frontier

Keep the separately labelled, joint-clock first-stop readouts `Y(z,z)` and `Y(0,z)` in the frozen 189-level BRC observer. Define

\[
A(z)=\operatorname{Var}(Y(z,z))-\operatorname{Var}(Y(0,z)),\quad
B(z)=E[Y(z,z)]-E[Y(0,z)],\quad
F_q(z)=qA(z)-B(z).
\]

The sampled-variance difference is `q F_q(z)` for positive `q`. The two real variables are parameters of an auxiliary observer, not two native spatial axes.

For the entire closed bridge `I=[L,R]=[0.0528706,0.0530659]`, the exact author-side certificates PREFIX-688, 692 and 693 establish

\[
0.329<A<0.657,\quad 7.85<B<7.95,\quad
-1751<A'<-1611,\quad128<B'<129.\tag{1}
\]

PREFIX-693 also gives the exact fifth-order jets at `b=53/1000`, each as an integer floor after multiplication by `10^8`, and the sixth derivative envelopes

\[
|A^{(6)}|\le 201273663850076722544640,\qquad
|B^{(6)}|\le17896441402901698560\quad(z\in I).\tag{2}
\]

The derivative floors, for orders `j=2,3,4,5`, are respectively:

\[
\begin{array}{c|rrrr}
j&2&3&4&5\\\hline
10^8 A^{(j)}\text{ floor}&-6667624082229&39352687679231&3189837819999830&-36266294695911132\\
10^8 B^{(j)}\text{ floor}&-99127959112&-1326952329685&-14895243921676&-1960958310350017
\end{array}
\]

**Source discrepancy and conservative resolution.** The PREFIX-693 paper and its Python assertion give the last `A` floor as `-36266294695911132`, whereas its RESULTS.json records `-36266294695911140` (eight floor units apart). In all calculations below we use the *larger absolute bound* from both reported alternatives, `|A^{(5)}(b)|<362662946.95911140`; the numerical certificate works under either reading. The exact row-by-row provenance of this last-floor discrepancy remains a concrete reconciliation item. No altered science pin or false independent replay is claimed.

## 2. Exact second-derivative envelopes

**Lemma 694.1.** Under the inherited jets and bound (2), for all real `z\in I`,

\[
\boxed{|A''(z)|<2500000,\qquad |B''(z)|<1500}.\tag{3}
\]

**Proof.** Set `T=max(|L-b|,|R-b|)=647/5000000`. For `G=A,B` let `g_j` denote the certified integer floors, using the conservative `A,j=5` lower alternative. Taylor's theorem applied to `G''`, with the sixth derivative remainder, gives

\[
|G''(z)|\le
\sum_{j=2}^{5}
\frac{\max(|g_j|,|g_j+1|)}{10^8}
\frac{T^{j-2}}{(j-2)!}
+\frac{M_{G,6}T^4}{4!}=:E_{G,2}.
\]

All comparisons below were checked in `fractions.Fraction` with exact integer cross-products:

\[
E_{A,2}=
\frac{9067699749950917699861066550924771}{3750000000000000000000000000}
<2500000,
\]

\[
E_{B,2}=
\frac{90155123982766821526069827687191}{75000000000000000000000000000}
<1500.
\]
This proves the lemma.

## 3. Uniform strict convexity of the crossover parameter

Define the continuously valid crossover parameter `Q(z)=B(z)/A(z)` on `I`.

**Theorem 694.2.** For every real `z\in I`,

\[
\boxed{29000<Q'(z)<130000},\qquad
\boxed{90000000<Q''(z)<1800000000}.\tag{4}
\]

In particular `Q` is strictly increasing and **strictly convex** on the entire bridge.

**Proof.** By `A>0`, differentiating gives

\[
Q'=\frac{B'A-BA'}{A^2},\qquad
Q''=\frac{N}{A^3},\quad
N=B''A^2-BAA''-2B'AA'+2B(A')^2.
\]

Since `A'<0`, `B'>0`, all the term `-2B'AA'` contributes positively. Use (1) and (3) to bound the complete numerator:

\[
N>2\cdot7.85\cdot1611^2
-7.95\cdot0.657\cdot2500000
-1500\cdot0.657^2
=\frac{55376034453}{2000}>0,
\]

\[
N<1500\cdot0.657^2
+7.95\cdot0.657\cdot2500000
+2\cdot129\cdot0.657\cdot1751
+2\cdot7.95\cdot1751^2
=\frac{124209486759}{2000}.
\]

Dividing by the corresponding positive `A^3` bounds yields `90000000<Q''<1800000000`. The first derivative formula likewise gives

\[
Q'>\frac{128\cdot0.329+7.85\cdot1611}{0.657^2}
=\frac{12688462000}{431649}>29000,
\]

\[
Q'<\frac{129\cdot0.657+7.95\cdot1751}{0.329^2}
=\frac{14005203000}{108241}<130000.
\]
Every inequality is strict, completing the proof.

## 4. Strict concavity and numerical curvature bounds of the inverse

Let `q_L=Q(L)`, `q_R=Q(R)`. Theorem 694.2 makes `Q:(L,R)\to(q_L,q_R)` a real-analytic increasing bijection. Previous PREFIX-690/693 endpoint signs establish the containment

\[
[q_-,q_+]\subset(q_L,q_R),\quad
q_-={63055771\over5256000},\quad
q_+={660614143\over27500000}.
\]

**Theorem 694.3.** For every real `q\in(q_L,q_R)`, `z(q)=Q^{-1}(q)` has `z'(q)>0`, and on the full verified band `q\in[q_-,q_+]`,

\[
\boxed{-\frac8{100000}<z''(q)<-\frac4{100000000}<0}.\tag{5}
\]

**Proof.** Analytic inverse differentiation gives

\[
z'(q)=\frac1{Q'(z(q))},\qquad
z''(q)=-\frac{Q''(z(q))}{(Q'(z(q)))^3}.
\]

The exact comparisons

\[
\frac{90000000}{130000^3}>\frac4{100000000},\qquad
\frac{1800000000}{29000^3}<\frac8{100000}
\]

combined with (4) prove (5). In fact (5) holds throughout `(q_L,q_R)`, because (4) holds throughout the entire spatial bridge. Thus the previously proved globally unique, increasing `q=12..24` root branch is now also strictly concave.

**Independent prior-bracket consistency check.** PREFIX-688 and PREFIX-691 give strict certified brackets

\[
z_{12}<0.0528708,\quad z_{18}>0.053000730,\quad z_{24}<0.0530659.
\]

Since `18=(12+24)/2`, these imply the rigorous strengthened midpoint inequality

\[
\boxed{z_{18}-\tfrac12(z_{12}+z_{24})>
\frac{1619}{50000000}=0.00003238}.\tag{6}
\]

This independently verifies the predicted concavity orientation at three widely spaced sampling parameters.

## 5. Reproduction, status and next discriminating unit

Run `python PREFIX694_R6_CURVATURE_CERTIFICATE.py` with the standard library. It uses only integer and `Fraction` calculations on previously published frozen-model jets and global sixth-order bounds; it prints `ALL_CHECKS_PASS PREFIX694-R6` in the output JSON. Its companion `PREFIX694_R6_RESULTS.json` contains the exact rational enclosures.

Mathematical scope: **conditional on the inherited author-side exact 189-level BRC polynomial observer certificate**; this round does not rerun the survivor acceptance predicate or claim native physical dynamics. Joint-clock branch labels, ordered survivor histories, positive kernels and the mean/variance readout are preserved. No new result/review admission is claimed.

Next: (i) reconcile the fifth derivative floor in PREFIX-693's checker/RESULTS.json by exact rerun or corrected JSON provenance; (ii) use local high-order or Bernstein derivative certificates to extend strict convexity, or find precise sign-change boundaries, in `0.052\le z\le0.054`; (iii) feed the resulting branch/variance sign geometry into PREFIX-675's complete `0\le p\le z\le1/2` sampled-variance maximum problem. The `(p,z)` variables remain an auxiliary chart inside the retained P000/ACTIVE Heartbeat World research basis.
