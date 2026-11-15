# PREFIX-808 extension: all-degree lattice holes, defect series and Hilbert basis

Date: 2026-11-16 (Asia/Taipei). Derivation: RESEARCH_DRIVER EM-DVR-DEBB5E, source-exposed author-side extension. Original named-source PREFIX-808 author EM-DIRECT-4660FF. Previous bounded degree-two classification: research_notes/driver/2026-11-15_r6_prefix808_tu_01_readout_reeve_h_family_exact_degree2_holes.md, GitHub a7de25dc1b6b7bdd7bd8334be9165724e4cd37f1, blob c90b27d58545b5a2a67009759664943d1dafe293.

## Model and statements

For every integer \(h\ge2\), retain the previously proved totally-unimodular integral source polytope

\[
P_h=\{(x_1,x_2,x_3,x_4,z_1,\ldots,z_h)\in[0,1]^{h+4}:
\sum_{i=1}^{4}x_i=1,\ z_j=x_4\ (1\le j\le h)\}.
\]

Define the 0/1 linear observation map

\[
W_h(x,z)=\left(x_2+x_4,\ x_3+x_4,\ \sum_{j=1}^h z_j\right).
\]

Its image is the Reeve tetrahedron \(Q_h\) with vertices
\(v_0=(0,0,0)\), \(v_1=(1,0,0)\), \(v_2=(0,1,0)\), \(v_3=(1,1,h)\).
For nonnegative integer \(k\), define the set of source-attainable integer observations by

\[
S_{h,k}=W_h(kP_h\cap\mathbb Z^{h+4}).
\]

**Theorem 1 (exact degree-by-degree lattice holes).** For each \(h\ge2\) and \(k\ge0\),

\[
\boxed{
(kQ_h\cap\mathbb Z^3)\setminus S_{h,k}
=
\bigcup_{r=1}^{h-1}\ \bigcup_{q=0}^{k-2}
\{(q+1+a,\ q+1+b,\ qh+r):
a,b,c\in\mathbb Z_{\ge0},\ a+b+c=k-q-2\}.}
\tag{1}
\]

The union is empty for \(k=0,1\) and its parameterization is injective. Consequently,

\[
\boxed{\#((kQ_h\cap\mathbb Z^3)\setminus S_{h,k})
=(h-1)\binom{k+1}{3},}
\quad k\ge0,
\tag{2}
\]
using the zero convention for \(k<2\), and

\[
\# S_{h,k}=\binom{k+3}{3},\qquad
\#(kQ_h\cap\mathbb Z^3)=\binom{k+3}{3}+(h-1)\binom{k+1}{3}.
\tag{3}
\]

Thus the exact hole-count generating function and Ehrhart series are

\[
\sum_{k\ge0}\#((kQ_h\cap\mathbb Z^3)\setminus S_{h,k})\,t^k
=\frac{(h-1)t^2}{(1-t)^4},
\qquad
\sum_{k\ge0}\#(kQ_h\cap\mathbb Z^3)t^k
=\frac{1+(h-1)t^2}{(1-t)^4}.
\tag{4}
\]

**Theorem 2 (complete minimal Hilbert basis).** Let

\[
C_h=\{(x,y,z,k)\in\mathbb Z^3\times\mathbb Z_{\ge0}:
(x,y,z)\in kQ_h\}.
\]

The unique minimal Hilbert basis of the additive semigroup \(C_h\) is precisely
the four degree-one elements \((v_i,1)\), \(i=0,1,2,3\), together with
the \(h-1\) degree-two elements

\[
w_r=(1,1,r,2),\quad 1\le r\le h-1.
\tag{5}
\]

These extra abstract integer observation states generate the saturation of the attainable observation semigroup in all degrees. They do not acquire integer preimages in the original source \(P_h\).

## Proofs

A point \((x,y,z)\in\mathbb Z^3\) lies in \(kQ_h\) exactly when the barycentric quantities

\[
t=\frac zh,\quad x-t,\quad y-t,\quad k-x-y+t
\tag{6}
\]
are nonnegative; they sum to \(k\).

Write \(z=qh+r\) uniquely, where \(q\ge0\) and \(0\le r<h\). If \(r=0\), then (6) is an integer quadruple:
\[
(x_4,x_2,x_3,x_1)=(q,\ x-q,\ y-q,\ k+q-x-y).
\]
It yields a nonnegative integer point of \(kP_h\) with all \(z_j=x_4\).
Conversely, any integral named-source point has observed third coordinate \(h x_4\), divisible by \(h\). Hence the source-attainable points of \(kQ_h\) are **exactly** those with \(r=0\).

If \(1\le r<h\), let \(\theta=r/h\in(0,1)\). Since \(x,y,k,q\) are integers, (6) is equivalent to

\[
a=x-q-1\ge0,\quad b=y-q-1\ge0,\quad
c=k+q-x-y\ge0.
\tag{7}
\]
These obey \(a+b+c=k-q-2\), so necessarily \(0\le q\le k-2\); conversely any such \((q,r,a,b,c)\) gives a point of \(kQ_h\) with \(r>0\). The residues \(r\), quotient \(q\), and coordinates \(a,b\) uniquely recover the parameters, establishing (1) and disjointness.

For fixed \(q,r\), stars-and-bars counts exactly \(\binom{k-q}{2}\) solutions. The hockey-stick identity gives

\[
(h-1)\sum_{q=0}^{k-2}\binom{k-q}{2}
=(h-1)\binom{k+1}{3}.
\tag{8}
\]

The integral source has precisely the nonnegative integer four-tuples summing to \(k\), numbering \(\binom{k+3}{3}\). The output map is injective on them: \(x_4=z/h\), \(x_2=x-x_4\), \(x_3=y-x_4\), and \(x_1=k-x_2-x_3-x_4\). This yields (2)--(3), and summing their binomial coefficients over \(k\) gives (4).

For Theorem 2, every point with \(r=0\) decomposes into the four degree-one vertex elements using the explicit integer four-tuple above. When \(1\le r<h\), the uniquely determined \(q,a,b,c\) in (7) provide an exact graded decomposition:

\[
(x,y,z,k)
=q(v_3,1)+w_r+a(v_1,1)+b(v_2,1)+c(v_0,1).
\tag{9}
\]

The degrees on the right total \(q+2+a+b+c=k\). Thus the proposed set generates all of \(C_h\). At degree 1, there are only the four vertex lattice points. Every \(w_r\) is a degree-two hole and cannot be written as a sum of two degree-one elements; it is therefore indecomposable. Each vertex degree-one element is also indecomposable. Consequently the displayed generating set is minimal and, as the set of all indecomposable elements in this positive affine semigroup, unique. QED.

## Independent coverage, research meaning and remaining bridge

Auxiliary finite integer enumeration over \(h=2,\ldots,7\) and \(k=1,\ldots,8\) compared all lattice points of \(kQ_h\) with source-observable integer points. All counts agreed with (2). The universal claim rests on equations (6)--(9), not on finite enumeration. Theorem 2 further strengthens the preceding degree-two classification by showing that *no generators of degree greater than two are needed* for the observer saturation.

The distinction between named source realizability and abstract observer lattice saturation is substantive. Any proposed transfer to native X6 signed-Port/Link algebra requires exact native source equations, allowed transitions, preserved provenance and observer fibers. No native correspondence is inferred here.

Evidence status: authored mathematical proof, GitHub Source publication; source-exposed, not independently reviewed or formally checked. Native Result acceptance: none in this subunit; formal Task completed: none; parent Objective completed: none.
