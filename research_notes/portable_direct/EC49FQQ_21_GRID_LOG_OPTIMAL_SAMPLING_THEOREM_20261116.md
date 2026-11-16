# EC49FQQ — Five exact BRC price sections and a jointly optimal logarithmic sampling-grid theorem

**Date:** 2026-11-16. **Frozen native scientific source:** awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. **Predecessor:** EC49FQP / PR #2562, 61 reused exact integer Bellman certificates. **Scientific status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Native problem and fixed competing policies

Native BRC class 16943 contains 310 original configurations grouped into 141 complete named-root response profiles. All 228 legal physical scalar actions (144 terminal, 84 named-root) are retained, with 209 distinct response partitions. A finite correct adaptive tree identifies the complete named-root profile, with both native response provenance and observation costs. There is no terminal-only quotient. Let the terminal and named-root prices be t>0 and r>0, with x=r/t. For profile i let m_i be its original-configuration multiplicity and p_lambda(i)=(1-lambda)/141+lambda*m_i/310, 0<=lambda<=1. Define v(lambda,x) as unrestricted global optimal expected cost divided by t.

The three inherited feasible correct full-tree policies have the following normalized expectation:

\[
\begin{aligned}
A(\lambda,x)&=(1-\lambda)(6x+290)/141+\lambda(6x+751)/310,\\
B(\lambda,x)&=(1-\lambda)(5x+293)/141+\lambda(5x+704)/310,\\
C(\lambda,x)&=(1-\lambda)(5x+295)/141+\lambda(5x+685)/310,\\
F(\lambda,x)&=\min\{A,B,C\},\\
\beta&=620/3299,\quad K(x)=7557-169x,\quad
\gamma(x)=310(3-x)/K(x).
\end{aligned}
\]

On 1<=x<=3, the feasible envelope F selects A for lambda<gamma(x), B for gamma(x)<lambda<beta, and C for lambda>beta, with ties at boundaries. The prior proof certifies v=F on 16 complete price slices and the whole high-price ray x>=3. Feasibility always gives v<=F.

## Theorem 1: five complete exact all-prior price slices

At x in {13/12, 5/4, 17/12, 31/12, 11/4}, **for every real lambda in [0,1]**, v(lambda,x)=F(lambda,x). All globally optimal *physical first observation indices* are exactly:

| Prior region | All optimal first indices |
| --- | --- |
| 0<=lambda<gamma(x) | 32, 34 |
| lambda=gamma(x) | 32, 34, 140, 142 |
| gamma(x)<lambda<beta | 140, 142 |
| lambda=beta | 16, 23, 140, 142 |
| beta<lambda<=1 | 16, 23 |

The five exact switch values gamma(x), in listed x order, are 7130/88487, 2170/29383, 5890/87811, 310/17089, and 310/28369.

**Proof.** At each rational price x, exact unrestricted integer Bellman recursion on the original 141 profiles with all 228 first physical actions is computed at four rational priors 0, gamma(x), beta, and 1. This produces 20 new exact case certificates. Independently implemented weighted Bellman dynamic programming reconstructs all 209 distinct response partitions directly from the two frozen original native files, recomputes the exact global integer optimum at each anchor, enumerates all optimal physical first indices, and replays every tied-first complete valid decision tree. Every anchor optimum equals the relevant witness cost A, B, or C, and its entire physical-first set is as in the table.

For a fixed price, every particular complete adaptive tree's cost is affine in lambda. If a witness tree is optimal at the endpoints of an interval, its cost minus every competing tree's cost has the same sign throughout the interval. Hence every real prior in each adjacent anchor interval is solved. A competing tree attaining equality strictly inside an interval must attain equality at both endpoints; therefore the first-index set there is the intersection of the exactly enumerated endpoint sets, and replayed witnesses attain every listed index. QED.

## Theorem 2: exact coverage of the continuous price–prior rectangle

The combined certified price mesh is

\[
G_{21}=\{1,13/12,7/6,5/4,4/3,17/12,3/2,13/8,7/4,15/8,
2,17/8,9/4,19/8,5/2,31/12,8/3,11/4,17/6,23/8,3\}.
\]

For each consecutive a<b in G21, the global unrestricted v equals A on [a,b]×[0,gamma(b)], equals B on [a,b]×[gamma(a),beta], and equals C on [a,b]×[beta,1]. In the respective strict interiors, all optimal first-action sets are {32,34}, {140,142}, and {16,23}.

The only potentially uncertified subset of [1,3]×[0,1] lies in 20 open curved bands a<x<b, gamma(b)<lambda<gamma(a). Their total axis-coordinate area is bounded exactly by

\[
S_{21}=\sum_{a,b\text{ consecutive}}(b-a)(\gamma(a)-\gamma(b))
=\frac{8225130100163500705}{924851487022880082561}.
\]

The rectangle has area 2; hence the certified fraction is at least

\[
1-S_{21}/2
=\frac{1841477843945596664417}{1849702974045760165122}
\approx99.55532697867847\%.
\]

**Proof.** For every fixed competitor tree, its cost difference from a fixed feasible witness tree is bilinear in x and lambda. On each certified rectangle the four corner differences are nonnegative by the exact price-section certificates; bilinear interpolation expresses an interior difference as their nonnegative convex combination. This proves unrestricted global optimality. A strictly interior zero forces all four corners to be zero, so the first-index sets are intersections of the corresponding certified corner first-index sets. The complement is contained in the stated bands; summing widths times endpoint gamma drops yields the exact displayed rational area. QED.

## Theorem 3: global policy error is below 0.0002213 terminal-price units

For every real lambda in [0,1] and x>=1, the complete feasible policy F satisfies

\[
0\le F(\lambda,x)-v(\lambda,x)\le M_{21}
=\frac{25/4}{(\sqrt{56569/8}+\sqrt{7050})^2}
=0.000221299772391955569735752\ldots.
\]

In actual price units, its maximum certified excess expected cost is M21*t, improving EC49FQP's worst guaranteed 0.0002937481599011876*t by approximately 24.6634%. This is an exact bound on the *secant-certificate envelope*, not a witness that some alternate BRC tree achieves that improvement.

**Proof.** For fixed lambda, v is the infimum of affine-in-x tree costs and therefore concave. The secant between the two exact endpoint Bellman values lower-bounds v and the feasible F upper-bounds it. For a consecutive interval [a,b], maximizing F minus that secant in lambda occurs at lambda=gamma(x); direct algebra gives

\[
D_{a,b}(x)=\frac{50(x-a)(b-x)}{(b-a)K(x)},\quad
M_{a,b}=\max_{a\le x\le b}D_{a,b}(x)
=\frac{50(b-a)}{(\sqrt{K(a)}+\sqrt{K(b)})^2}.
\]

Every G21 interval has width at most 1/8. Among width-1/8 intervals M increases with the left endpoint, so [23/8,3] is the worst. Each narrower interval has width at most 1/12 and its M is less than 50*(1/12)/(4*K(3)), which is less than 50*(1/8)/(4*K(23/8)), itself a lower bound on M_[23/8,3]. Substituting K(23/8)=56569/8 and K(3)=7050 proves the formula. For x>=3 the inherited BRC theorem gives v=F. QED.

## Theorem 4: one unique logarithmic mesh minimizes both worst gap and uncertified area

Fix n>=1 intervals with 1=x_0<x_1<...<x_n=3. Imagine their price endpoints have been certified exactly as above (this is an explicitly conditional grid-design theorem; it does not claim uncomputed endpoint Bellman values). Among all real meshes with n intervals, the **same unique grid** minimizes both: (i) max_j M_[x_(j-1),x_j], the worst secant-envelope error bound, and (ii) S=sum_j (x_j-x_(j-1))(gamma(x_(j-1))-gamma(x_j)), the uncertain-area bound.

Write H=log(7388/7050). The optimizer is uniform in logarithmic K-coordinates:

\[
K(x_j)=7388(7050/7388)^{j/n},
\qquad x_j=(7557-K(x_j))/169,\quad 0\le j\le n.
\]

The exact theoretical minima are

\[
M_{n,\min}=\frac{50}{169}\tanh\!\left(\frac{H}{4n}\right),
\quad
S_{n,\min}=\frac{2\cdot2185500\,n}{169^2}
\bigl(\cosh(H/n)-1\bigr).
\]

**Proof.** Set h_j=log(K(x_(j-1))/K(x_j))>0. Then sum h_j=H, and elementary simplification of the exact M formula yields M_j=(50/169)tanh(h_j/4). Since tanh is strictly increasing for h>0, max_j M_j is minimized uniquely by equal h_j=H/n.

The Möbius identity

\[
\gamma(a)-\gamma(b)=
2185500(b-a)/(K(a)K(b))
\]

also gives

\[
S=\frac{2\cdot2185500}{169^2}
\sum_{j=1}^n(\cosh(h_j)-1).
\]

Strict convexity of cosh and Jensen's inequality give the *same unique* equal-h optimizer, with the stated S value. QED.

For 20 intervals the theoretical minimax gap is approximately 0.0001731857994231647*t. The 21 **actually certified rational nodes** above have gap 0.0002212997723919556*t. A rational approximation to the optimal mesh can be selected for future full-native Bellman checks. No statement about an uncertified real node's exact Bellman value is made.

## Reproducibility, status and next question

The independently reproduced 20 new Bellman certificates and 61 SHA256-verified inherited ones, the two frozen original source files, complete trees, original and independent Python checkers, all logs, exact rational geometry checks and per-file checksums are in the evidence package EC49FQQ_BRC_21_NODE_LOG_OPTIMAL_GRID_EVIDENCE_20261116.tar.xz (SHA256 0a2daccc28b6759e36714c8077f2fea8a2d5f1fa7cb521ad10f79390c9f871c9). Run the bundled independent verifier in the unpacked evidence directory. This manuscript's algebra is human-checkable and the finite anchors are exact; external independent mathematical review remains pending.

**Frontier:** Find a parameterized native-BRC Bellman lower bound eliminating the 20 remaining bands or construct a correct native full-response decision tree with strictly smaller expected cost in one band. The canonical control query for RS-EC49AS at Source cc871bc74328416d97ae5ecb7988df1a0390dc4f returned NO_CANONICAL_PUBLICATION_DIRECTORY on 2026-11-16T06:29:34.137085Z; this portable work does not invent CLAIM, Result, Review, or a new owner. A historical Researcher-ID without current session authorization is retained as provenance only.
