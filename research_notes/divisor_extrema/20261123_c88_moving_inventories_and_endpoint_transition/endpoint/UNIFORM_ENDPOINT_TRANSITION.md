# C88: a uniform endpoint transition for the auxiliary Haar functions

## Scope and notation

The native observation problem remains the original integer arrangements and
their original `H(0,1)` readouts. This note concerns the auxiliary Haar
functions already defined in C84. A lattice of covolume `a` has displacement
marks

\[
\ell_\theta(u,v)=(u,(1-\theta)u+\theta v,v),\qquad 0\le\theta\le1,
\]

and the three source phases are independently uniform in the unit cube.
Their mean uniqueness probability is \(F_\theta(a)\). The endpoint definition
retains three independent phases. It is not the finite experiment that
repeats the same exact readout at two fixed rounding origins.

The results below hold for these auxiliary functions. A joint limit involving
the original inventory `c`, precision, and moving position requires a separate
native bridge. In particular, none of the limits below silently establishes
uniformity of the C84 fixed-position bridge.

Write \(p(P)\) for the probability that a covolume-one affine Haar lattice
has exactly one point in the bounded window \(P\). Define

\[
K_{u,\rho}=\{(X,Y):X\ge0,\ 0\le Y\le1,\ X+\rho Y\le u\},
\quad u\ge0,\ \rho\ge0,
\]

and the new transition function

\[
\boxed{\mathscr D(\rho)=2\int_0^\infty p(K_{u,\rho})\,du.}\tag{1}
\]

All coordinates here are auxiliary joint-readout coordinates; all points in
one lattice remain correlated.

## 1. Main uniform theorem

Put \(s=\max(\theta,1-\theta)\), \(t=\min(\theta,1-\theta)\). There is an
absolute finite constant \(C\), independent of \(a\) and \(\theta\), such that

\[
\boxed{\left|F_\theta(a)-a^2s\,
\mathscr D\!\left(\frac{t}{as}\right)\right|\le Ca^3,
\qquad a>0,\quad 0\le\theta\le1.}\tag{2}
\]

The bound is intended for small \(a\); its validity for large \(a\) merely
allows a large right-hand side. The transition function is finite, positive,
and continuous on \([0,\infty)\). Its two ends are

\[
\boxed{\mathscr D(0)=C_{\rm end}
=2\int_0^\infty F_2(v)v^{-3}\,dv,}\tag{3}
\]

\[
\boxed{\mathscr D(\rho)=\frac{\kappa_3}{\sqrt2}\sqrt\rho
+O(\rho^{-1})\qquad(\rho\to\infty).}\tag{4}
\]

Here \(F_2\), \(\kappa_3\), and \(C_{\rm end}\) have their C83 and C85
normalizations. Formula (2), including its error uniform in the whole closed
position interval, is the new statement; the endpoint identity (3) was
already implicit in C85.

## 2. A uniform integrable tail

C83 proves the following affine-lattice lemma: if a family of convex windows
\(P\) has a common positive inradius and uniformly bounded diameter, then

\[
p(rP)=O(r^{-4}).\tag{5}
\]

The proof uses a shortest primitive vector and its complete lattice rows,
not independent point events. Its constant depends only on those two
geometric bounds. Increasing the constant makes (5) valid for every \(r>0\).

For \(u\ge\rho\), the window \(K_{u,\rho}\) contains the triangle with
vertices \((0,0),(u,0),(0,1)\) and is contained in
\([0,u]\times[0,1]\). Apply the determinant-one map
\((X,Y)\mapsto(X/\sqrt u,\sqrt u Y)\). After extracting the overall scale
\(\sqrt u\), the remaining body contains a fixed triangle and lies in the
unit square. Haar invariance and (5) therefore give

\[
p(K_{u,\rho})\le C_0u^{-2},\qquad u\ge\rho.\tag{6}
\]

The same bound with a common constant applies to

\[
K_{u,\rho}\cap\{X\le h\}
\quad\text{whenever}\quad u\ge\rho,\qquad u/2\le h\le u.
\tag{7}
\]

Indeed, the truncated body still contains the triangle with vertices
\((0,0),(u/2,0),(0,1)\). These are the only window families needed below.
Thus all tails are controlled by one integrable bound, with no degenerating
inradius hidden in a position-dependent constant.

For a fixed finite interval of \(\rho\)'s, the tail (6) is uniform once
\(u\) exceeds that interval. On a bounded \(u\)-interval, changing \(\rho\)
changes the window continuously in symmetric-difference area. The affine
Siegel mean gives

\[
|p(P)-p(Q)|\le\mathbb E N_{P\triangle Q}=|P\triangle Q|.\tag{8}
\]

This proves continuity of \(\mathscr D\) by dominated convergence. Its
finiteness follows from (6). For positivity, choose any small interval of
positive \(u\)'s for which \(0<|K_{u,\rho}|<1\). C83's elementary second
moment inequality gives \(p(K)\ge |K|-|K|^2>0\) there.

## 3. Exact slicing and the uniform remainder

By symmetry it suffices to take \(0\le\theta\le1/2\), so
\(s=1-\theta\), \(t=\theta\). C84's exact phase-slice identity is

\[
F_\theta(a)=a\int_{-1}^1
\Pr_{\rm affine,covol=a}\{N_{P_z}=1\}\,dz,
\]

where

\[
P_z=[0,1]^2\cap\{z\le sx+ty\le z+1\}.
\]

The positive and negative halves are centrally congruent. On \(z\ge0\),
put \(\varepsilon=1-z\), \(X=(1-x)/a\), \(Y=1-y\). The transformed affine
lattice has covolume one, and its window is

\[
0\le X\le1/a,\quad 0\le Y\le1,\quad
sX+(t/a)Y\le\varepsilon/a.
\]

Consequently, for \(\rho=t/(as)\), the exact formula is

\[
\boxed{F_\theta(a)=2a^2s\int_0^{1/(as)}
p\bigl(K_{u,\rho}\cap\{X\le1/a\}\bigr)\,du.}\tag{9}
\]

For \(u\le1/a\) the cutoff \(X\le1/a\) does nothing. For
\(1/a\le u\le1/(as)\), we have

\[
\rho=\frac{t}{as}\le\frac1a\le u,
\qquad \frac u2\le su\le\frac1a\le u.
\]

Thus (6) and (7) control both windows on the entire region where (9)
differs from the infinite integral (1). In particular,

\[
\begin{aligned}
|F_\theta(a)-a^2s\mathscr D(\rho)|
&\le 2a^2s\left[
\int_{1/a}^{1/(as)}C_0u^{-2}\,du
+\int_{1/a}^{\infty}C_0u^{-2}\,du\right]\\
&\le4C_0a^3.
\end{aligned}
\]

This proves (2). It also proves the uniform error without first asserting
pointwise convergence and then exchanging an uncontrolled infinite integral.

## 4. The two ends of the transition

At \(\rho=0\), \(K_{u,0}\) is the rectangle \([0,u]\times[0,1]\). Haar
invariance and the affine single-point/Palm identity give

\[
p(K_{u,0})=uF_2(1/u).
\]

Inserting this in (1) and changing variables gives (3).

For \(\rho>0\) and \(0\le u\le\rho\), the window is a triangle with
legs \(u\) and \(u/\rho\). A determinant-one linear map sends it to
\((u/\sqrt\rho)T\), where \(T\) is C83's unit right triangle. With
\(\psi(r)=p(rT)\), this gives the exact decomposition

\[
\mathscr D(\rho)=2\sqrt\rho\int_0^{\sqrt\rho}\psi(r)\,dr
+2\int_\rho^\infty p(K_{u,\rho})\,du.\tag{10}
\]

C83 proves \(\psi(r)=O(r^{-4})\) and
\(\kappa_3=2\sqrt2\int_0^\infty\psi(r)\,dr\). The omitted triangle
tail is therefore \(O(\rho^{-1})\); (6) bounds the trapezoid term by
\(O(\rho^{-1})\) as well. Formula (4) follows. In particular there is a
global bound

\[
0<\mathscr D(\rho)\le C_1(1+\sqrt\rho),\qquad\rho\ge0.\tag{11}
\]

No monotonicity or closed form for \(\mathscr D\) is asserted.

## 5. Three rigorously separated low-area regimes

The following are consequences of (2), not new assumptions on native
inventory experiments. Let \(a\downarrow0\) and \(\theta(a)\to0\).

* If \(\theta/a\to0\), then
  \(F_\theta(a)\sim C_{\rm end}a^2\).
* If \(\theta/a\to\rho\in(0,\infty)\), then
  \(F_\theta(a)/a^2\to\mathscr D(\rho)\).
* If \(\theta/a\to\infty\), then
  \(F_\theta(a)\sim(\kappa_3/\sqrt2)\sqrt\theta\,a^{3/2}\).

More quantitatively, throughout \(0<\theta\le1/2\) and \(a\le\theta\),

\[
F_\theta(a)=\kappa_3\sqrt{\frac{\theta(1-\theta)}2}\,a^{3/2}
+O(a^3/\theta),\tag{12}
\]

with an absolute implied constant. Thus the relative error is
\(O((a/\theta)^{3/2})\) uniformly, up to a fixed numerical factor.
The crossover occurs at position distance comparable to the covolume
\(a\), not at an unspecified shrinking-neighborhood scale.

## 6. Consequence for the auxiliary full-source curves

Let \(\Delta=\{0<y<x<1\}\), let \(J\) be the original C82 Jacobian,
and write \(M_r=2\int_\Delta J^r\). The existing auxiliary full-source
curve is

\[
\Phi_\theta(L)=2\int_\Delta F_\theta(L^2J(X))\,dX.
\]

Define another continuous, positive transition function

\[
\mathscr E(\tau)=2\int_\Delta J(X)^2
\mathscr D\!\left(\frac\tau{J(X)}\right)\,dX.\tag{13}
\]

At \(J=0\), define the integrand to be zero. Bound (11) shows that this
extension is continuous and dominated by a constant times
\(J^2+\sqrt\tau J^{3/2}\) on bounded \(\tau\)-intervals. The boundedness
of the original Jacobian permits direct integration of (2), yielding

\[
\boxed{\Phi_\theta(L)=L^4s\,
\mathscr E\!\left(\frac{t}{sL^2}\right)+O(L^6),}
\tag{14}
\]

uniformly for the whole closed interval \(0\le\theta\le1\). Its endpoints
are

\[
\mathscr E(0)=C_{\rm end}M_2,
\qquad
\mathscr E(\tau)=\frac{\kappa_3}{\sqrt2}M_{3/2}\sqrt\tau
+O(M_3/\tau)\quad(\tau\to\infty).\tag{15}
\]

Therefore, within this auxiliary family, the full-source low-precision
crossover is \(\theta\asymp L^2\). If \(\theta/L^2\to\tau<\infty\),
then \(\Phi_\theta(L)/L^4\to\mathscr E(\tau)\). If
\(\theta/L^2\to\infty\) while \(\theta\to0\), the corresponding
interior law is

\[
\Phi_\theta(L)\sim\frac{\kappa_3}{\sqrt2}M_{3/2}\sqrt\theta\,L^3.
\]

This does not identify an arbitrary linked \(c\to\infty,L_c\to0\)
limit of the original integer experiment; such a claim needs uniform
inventory estimates in those parameters.

## 7. Uniform low-precision expansion and moving optimizers

Continuity of \(\mathscr D\) at zero and (4) at infinity imply

\[
\sup_{\rho\ge0}\left|\mathscr D(\rho)
-\frac{\kappa_3}{\sqrt2}\sqrt\rho\right|<\infty.
\]

Substituting this bounded difference into (2) gives the simpler expansion

\[
\boxed{F_\theta(a)=\kappa_3
\sqrt{\frac{\theta(1-\theta)}2}\,a^{3/2}+O(a^2),}
\tag{16}
\]

uniformly on \(0\le\theta\le1\) as \(a\downarrow0\). Its endpoint
remainder carries the actual \(a^2\) leading term; this is why the
uniform remainder differs from the sharper fixed-interior remainder.
Integration over the bounded original Jacobian gives

\[
\boxed{\Phi_\theta(L)=\kappa_3M_{3/2}
\sqrt{\frac{\theta(1-\theta)}2}\,L^3+O(L^4),}
\tag{17}
\]

uniformly over the entire closed position interval.

In particular, let \(\theta_L\) be any global maximizer of
\(\Phi_\theta(L)\) on \([0,1]\). Such a maximizer exists by the already
proved position continuity. Then

\[
\boxed{\theta_L=\frac12+O(L^{3/2})\qquad(L\downarrow0).}\tag{18}
\]

The proof first localizes all maximizers using the global remainder, and
then uses the sharper interior remainder. Put \(\delta=\theta_L-1/2\) and
\(A=\kappa_3M_{3/2}>0\). For some fixed \(C_2\), (17) and maximality
imply

\[
A\left[\frac1{2\sqrt2}
-\sqrt{\frac{\theta_L(1-\theta_L)}2}\right]L^3
\le2C_2L^4.
\]

Since \(1-\sqrt{1-x}\ge x/2\) for \(0\le x\le1\), the bracket is at
least \(\delta^2/\sqrt2\). Thus
\(|\delta|\le(2\sqrt2 C_2/A)^{1/2}\sqrt L\). In particular, for
sufficiently small \(L\), every maximizing position belongs to
\([1/4,3/4]\).

On this fixed interior interval, (12) and its reflected version have the
uniform remainder \(O(a^3)\). Since \(J\) is bounded, for sufficiently
small \(L\) the condition \(a=L^2J\le\min(\theta,1-\theta)\) holds for
every source point. Integrating (12) therefore sharpens (17) to

\[
\Phi_\theta(L)=A\sqrt{\frac{\theta(1-\theta)}2}\,L^3+O(L^6),
\qquad 1/4\le\theta\le3/4,
\]

with a uniform constant. Comparing a maximizing position with the
midpoint a second time now gives

\[
\frac{A}{\sqrt2}\delta^2L^3\le C_3L^6,
\]

which proves (18). This two-step improvement uses no derivative estimate
for the precision-dependent remainder. It permits the maximizing position
to depend on precision, strengthening a comparison between only two fixed
positions. It still concerns the auxiliary curves, with the same
native-limit qualification as above.

## 8. A useful positive bound, and what remains uncomputed

C82's primitive-direction union bound gives, for every \(v>0\),

\[
F_2(v)\ge\max\{0,1-k/v\},\qquad k=\frac{21}{4\pi^2}>\frac12.
\]

C83's short-direction calculation independently gives
\(F_2(v)\ge v^3/\pi^2\) for \(0<v<1/2\). Integrating these bounds on
the disjoint intervals \((0,1/2)\) and \((k,\infty)\) yields

\[
\boxed{C_{\rm end}\ge\frac1{\pi^2}+\frac1{3k^2}
=\frac1{\pi^2}+\frac{16\pi^4}{1323}>0.}\tag{19}
\]

The exact integral defining \(C_{\rm end}\) remains the value used here;
this note does not evaluate it in elementary constants. It likewise does
not establish monotonicity of \(\mathscr D\) or a closed form of its
trapezoid probabilities.

## Sources and verification status

* C82 `LATTICE_LIMIT.md`: Haar normalization, primitive-direction union
  bound, and the high-area formula for \(F_2\).
* C83 `HAAR_SMALL.md`: affine Palm identity, single-point second moment
  bounds, the fat-convex-body lemma, triangle integral, and the two-readout
  cubic law.
* C84 `READING_POSITION.md`: the exact three-phase slice formula and the
  original-source Jacobian normalization.
* C85 `endpoint/ENDPOINT_LIMIT.md`: the independent-phase endpoint formula
  and its previously proved expansion.

The new proof is the exact finite-width identity (9), the common integrable
tail (6)--(7), their uniform comparison, and the two-scale consequences.
These arguments do not rely on a sampled numerical curve or on a numerical
evaluation of the transition function.
