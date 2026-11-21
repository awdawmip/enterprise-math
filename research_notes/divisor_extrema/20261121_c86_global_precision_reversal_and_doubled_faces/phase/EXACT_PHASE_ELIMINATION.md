# C86: exact phase and scale elimination for rational lattice bases

## 1. Result and interpretation

Let \(B=A/d\) be a rational two-by-two basis of determinant one, where
\(A\) has integer entries, \(d>0\), and \(\det A=d^2\). Let
\(\theta=p/q\in(0,1)\) be rational. The three readout marks of a lattice
vector \(v=(v_0,v_2)\) are

\[
\bigl(v_0,(1-\theta)v_0+\theta v_2,v_2\bigr).
\]

The program `exact_phase_moment.py` eliminates all three source phases and
the full scale variable by exact finite arithmetic. It returns the complete
phase-averaged uniqueness function as piecewise cubic polynomials and the
critical moment

\[
H_\theta(B)=\mathbb E_\alpha S_\theta(B,\alpha)^{1/10}
\]

as a rational linear combination of rational tenth roots. No random
sampling is used. Every integer competitor is covered by the finite
reduction proved below. The lattice is the auxiliary readout object of
C84–C85; it does not replace the project's original integer arrangements
or native-space definitions.

One exact application is a sign reversal under rotation of the same
square lattice. The unit square has

\[
H_{1/4}(I)-H_{1/2}(I)
=\frac{100}{7161}-\frac5{462}2^{-1/10}>0,
\]

whereas

\[
B=\frac15\begin{pmatrix}3&-4\\4&3\end{pmatrix},\qquad B^TB=I,
\]

has \(H_{1/4}(B)-H_{1/2}(B)<0\). Thus even after every source phase is
averaged, orientation relative to the readout coordinates matters within
one Euclidean lattice shape. This secondary result is separate from the
full Haar comparison proved elsewhere in C86.

## 2. Complete integer candidate set

For columns \(v,w\) of a determinant-one basis put

\[
C(B)=\frac12\max_j(|v_j|+|w_j|),
\qquad t=\min(\theta,1-\theta).
\]

C85's `lattice/COMPACT_FINITE_REDUCTION.md` proves that it suffices,
uniformly in all phases, to retain primitive vectors satisfying

\[
\|Bn\|_\infty\le\frac{4C(B)}t. \tag{1}
\]

For clarity, the coverage argument is as follows. If the three phases are
\(\alpha\), set \(z=(1-\theta)\alpha_0+\theta\alpha_2-\alpha_1\) and
\(\delta=1-|z|\). The convex endpoint section contains a square of side
\(\delta\), while each of its coordinate widths is at most \(\delta/t\).
Rounding the basis coordinates bounds the covering radius in sup norm by
\(C(B)\). At every scale smaller than \(\delta/(4C(B))\), two disjoint
interior balls inside that square contain two distinct translated lattice
points, at least one a competitor. Therefore the critical scale is at
least \(\delta/(4C(B))\). Any improving vector must satisfy (1). A
nonprimitive vector may always be replaced by its same-sign primitive
divisor. Null boundary phases do not affect phase integration.

Write

\[
A=\begin{pmatrix}a&b\\c&e\end{pmatrix},\quad
u=am+bn,\quad v=cm+en.
\]

Then (1) is the exact integer endpoint condition

\[
\max(|u|,|v|)\le
R:=\frac{2q\max(|a|+|b|,|c|+|e|)}{\min(p,q-p)}.
\]

The inverse matrix gives the complete finite index box

\[
|m|\le\left\lfloor\frac{R(|e|+|b|)}{d^2}\right\rfloor,
\qquad
|n|\le\left\lfloor\frac{R(|c|+|a|)}{d^2}\right\rfloor.
\tag{2}
\]

The program enumerates every primitive index in (2), applies the exact
endpoint filter, and stores one orientation of each pair \(\{n,-n\}\).
Both signs are restored before phase integration.

## 3. Two exact event containment reductions

The integer mark triple is

\[
m(n)=(qu,(q-p)u+pv,qv).
\]

Set \(\lambda=\sigma/(qd)\); the three actual displacement coordinates
are \(\lambda m(n)\). All comparisons in this section are uniform in
\(\lambda\) and in the phases.

**Single-vector containment.** Suppose the coordinates of \(m(w)\) have
the same weak signs as those of \(m(v)\) and no larger absolute values.
Every phase collision caused by \(v\) is then also caused by \(w\).
The zero-coordinate case means exactly that the corresponding coordinate
of \(w\) is zero. The test permits either orientation of a retained vector.

**Two-vector coverage.** Suppose two retained vectors \(w_+,w_-\) have
endpoint coordinates between zero and the corresponding endpoint of
\(v\), coordinate by coordinate. They are endpoint-eligible whenever
\(v\) is. Write their opposite middle marks as \(P>0\) and \(-N<0\).
Their middle collision intervals are

\[
[0,1-\lambda P],\qquad [\lambda N,1].
\]

Any collision of \(v\) requires
\(\lambda\le1/M(v)\), where
\(M(v)=\max(|m_0(v)|,|m_2(v)|)\). Consequently

\[
P+N\le M(v) \tag{3}
\]

implies that those two intervals cover every middle phase. The event of
\(v\) is therefore contained in the union of the events of these two
retained vectors. A retained endpoint-smaller vector with zero middle
mark alone has the same coverage property.

Vectors are processed in increasing endpoint maximum, then increasing
sum of absolute marks. A discarded event is contained in already
retained events. The same argument applied to all negated marks covers
the opposite orientation. These are exact containments of correlated
events, rather than an approximation by independent competitors.

## 4. Elimination of the middle phase

Fix \(\lambda\). Along an endpoint phase coordinate, the only relevant
cuts are \(0,1,-\lambda m_j,1-\lambda m_j\) that lie in \((0,1)\).
The Cartesian product of the two endpoint partitions has a fixed set of
eligible vectors on each cell.

For that eligible set, let \(P\) and \(N\) be the smallest positive and
smallest absolute negative middle integer marks. A missing sign gives a
cap equal to one; an eligible zero middle mark makes uniqueness
impossible. Otherwise the exact measure of middle phases without any
collision is

\[
\left(\min(1,\lambda P)+\min(1,\lambda N)-1\right)_+.
\tag{4}
\]

Thus the complete three-phase probability is the sum over endpoint cells
of their area times (4). The program uses integer evaluations at rational
midpoints to determine cell order and eligibility. The resulting widths
are stored as exact affine functions, so the integration covers each
whole cell.

## 5. Complete radial breakpoints and cubic pieces

For a fixed mark coordinate, an interior cut associated with a positive
mark has form \(1-h\lambda\), while a cut associated with a negative
mark has form \(h\lambda\), where \(h>0\). Cuts of the same type never
cross at positive scale. Opposite types cross only at

\[
\lambda=\frac1{h_i+h_j}.
\]

Entry into or exit from the unit interval has the same form with one
\(h_i=0\). The changes in (4) occur at \(1/P\), \(1/N\), or
\(1/(P+N)\), all included by the same rule in the middle coordinate.
Therefore the complete breakpoint set is obtained by taking sums of
absolute marks in each of the three coordinate columns, including zero.
No unsampled ordering change remains.

Put \(M_{\min}=\min_n\max(|m_0(n)|,|m_2(n)|)\). For
\(\lambda>1/M_{\min}\), no retained vector is endpoint-eligible, so
the probability is one. The breakpoint set only needs to be retained up
to that scale. Between successive breakpoints, two endpoint widths and
the positive middle length are affine in \(\lambda\). Hence

\[
F_\theta^B(\sigma^2)
=\sum_{k=0}^3 C_k\lambda^k
\]

on every radial interval. In this integer scaling the \(C_k\) are
integers. Adjacent pieces with identical coefficients are merged.

## 6. Exact integration of the full scale

For any \(\eta>0\), the critical-scale moment is

\[
\mathbb E S_\theta^\eta
=\eta\int_0^\infty
[1-F_\theta^B(\sigma^2)]\sigma^{\eta-1}\,d\sigma.
\]

If \([l,h]\) is one of the \(\lambda\)-intervals and its polynomial
has coefficients \(C_k\), exact integration gives

\[
\boxed{
\mathbb E S_\theta^\eta
=(qd)^\eta\left[
\lambda_{\max}^\eta
-\sum_{[l,h],k}\frac{\eta C_k}{\eta+k}
(h^{\eta+k}-l^{\eta+k})\right].} \tag{5}
\]

A rational upper cutoff is handled by shortening the final interval,
yielding \(\mathbb E\min(S_\theta,T)^\eta\). For the implemented
comparison \(\eta=1/10\), (5) is collected into rational coefficients
times rational tenth roots. Each root is enclosed by integer-power
bisection with 100 binary fractional bits. Exact rational endpoints,
not displayed decimals, decide the signs.

## 7. Executed exact examples

| Basis \(B\) | \(H_{1/4}(B)-H_{1/2}(B)\), decimal display | Sign |
|---|---:|:---:|
| \(I\) | \(+0.0038667704448956046\) | positive |
| \(\frac15\begin{pmatrix}3&-4\\4&3\end{pmatrix}\) | \(-0.004576580665574825\) | negative |
| \(\begin{pmatrix}1&1/2\\0&1\end{pmatrix}\) | \(-0.0013110149727522372\) | negative |
| \(\operatorname{diag}(1/2,2)\) | \(-0.011928164472101335\) | negative |

For the rotated square, the complete exact difference is

\[
\begin{aligned}
&-\frac{25}{63798}(5/14)^{1/10}
-\frac{25}{78771}(5/11)^{1/10}
-\frac1{2170}(1/2)^{1/10}\\
&\quad+\frac5{1848}(5/8)^{1/10}
+\frac{6635}{350889}(5/7)^{1/10}
-\frac{65}{2728}(5/4)^{1/10}<0.
\end{aligned}
\]

Its quarter-point computation starts from 154 complete unoriented
candidates, reduces them to ten, and produces six actual cubic pieces.
The midpoint computation starts from 40 candidates, keeps ten, and
produces four cubic pieces. The square and rectangle examples keep only
two unoriented directions after exact event coverage. Every output JSON
contains the coverage counts, radical expression, and exact directed
interval.

The observations do not establish a sign for every lattice, nor an
optimal middle position. They show that a phase-averaged, shape-only
comparison would lose relevant orientation information.

## 8. Reproduction and independent checks

Run one example with:

```bash
python /mnt/data/C86/phase/exact_phase_moment.py \
  --basis 3 -4 4 3 --denominator 5 \
  --output /mnt/data/C86/phase/rotated_square_exact.json
```

Run the validation and regenerate all four example files with:

```bash
python /mnt/data/C86/phase/verify_exact_phase_moment.py
```

The executed verifier checks the complete polynomial formulas for the
unit square at five rational positions. It independently integrates the
endpoint cells at 40 rational basis/position/scale settings, including
all endpoint-eligible integer vectors without primitive filtering or
event pruning. It also checks continuity at every computed radial
breakpoint, reproduces C85's exact square radical expression, certifies
all four displayed signs, and checks invariance under two unimodular
basis relabelings. These checks exercise the finite coverage and phase
elimination; the all-scale justification is the proof above.
