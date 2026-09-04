# Free Research — Exact Finite Rational-Reflection Intertwiner

Status: `FREE_RESEARCH_FRONTIER / EXACT STOPPED-TO-VALID PATH LIFT / FLOOR SAFE / ENDPOINT PRESERVED / POSITIVE RATIONAL HOLONOMY / MIXED-CHAMBER CARRIER CLOSED / WEIGHT GAUGE INTERTWINER OPEN / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-05`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_CUBE_SIMPLEX_SPACINGS_INTERTWINER_V18_20260905.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Executive advance

The mixed stopping chambers do admit an exact common finite history carrier. No asymptotic approximation and no removal of the floor operation is needed.

Every finite stopped history of integer prime-power actions can be transformed into a fully valid history of positive rational actions that:

1. has the same number of slots;
2. visits the sorted proposal states;
3. has exactly the same final integer endpoint;
4. retains the sorting permutation as provenance;
5. preserves the original history weight by pushforward.

Thus the V18 arithmetic common-lift obstruction is not an endpoint or path-existence problem. It is solely a comparison between two positive gauges on the common rational-history carrier:

- the reflected pushforward of the prime-action cube measure;
- the factorial canonical valid-history measure.

---

## 2. Stopped integer history

Fix an integer top state `N>=1` and integer actions

\[
a_1,\ldots,a_d\in\{1,\ldots,N\}.
\]

Define the stopped history recursively by

\[
x_0=N
\]

and

\[
 x_j=
\begin{cases}
\lfloor x_{j-1}/a_j\rfloor,&a_j\le x_{j-1},\\
x_{j-1},&a_j>x_{j-1}.
\end{cases}
\tag{2.1}
\]

For each slot define its proposal state

\[
 y_j=
\begin{cases}
\lfloor x_{j-1}/a_j\rfloor,&a_j\le x_{j-1},\\
a_j,&a_j>x_{j-1}.
\end{cases}
\tag{2.2}
\]

A valid proposal is the actual descended endpoint; an invalid proposal is placed above the current state.

---

## FRR-T01 — Running-minimum identity

For every slot,

\[
\boxed{x_j=\min(x_{j-1},y_j).}
\tag{3.1}
\]

Indeed:

- in the valid case, `y_j=x_j<=x_(j-1)`;
- in the invalid case, `y_j=a_j>x_(j-1)=x_j`.

Induction gives

\[
\boxed{
x_d=\min\{N,y_1,\ldots,y_d\}.}
\tag{3.2}
\]

Since the first action is at most `N`, the first step is valid and `y_1<=N`; hence

\[
\boxed{x_d=\min_j y_j.}
\tag{3.3}
\]

This identity is exact with natural-number division.

---

## 4. Sorted proposal chain

Choose a stable sorting permutation `sigma in S_d` such that

\[
 z_1:=y_{\sigma(d)}
\ge z_2:=y_{\sigma(d-1)}
\ge\cdots
\ge z_d:=y_{\sigma(1)}.
\tag{4.1}
\]

Thus

\[
z_d=x_d.
\tag{4.2}
\]

Define positive rational actions

\[
\boxed{
 b_1:=N/z_1,
\qquad
 b_j:=z_{j-1}/z_j
\quad(2\le j\le d).
}
\tag{4.3}
\]

All ratios are at least one.

For a positive rational action `b>=1`, define its exact rational quotient on a positive integer state by

\[
Q_b(x):=\lfloor x/b\rfloor.
\tag{4.4}
\]

---

## FRR-T02 — Fully valid rational path

The first transformed action satisfies

\[
Q_{b_1}(N)
=\left\lfloor\frac{N}{N/z_1}\right\rfloor
=z_1.
\]

For every later slot,

\[
Q_{b_j}(z_{j-1})
=\left\lfloor
\frac{z_{j-1}}{z_{j-1}/z_j}
\right\rfloor
=z_j.
\]

Therefore the transformed path is

\[
oxed{
N\longrightarrow z_1\longrightarrow z_2
\longrightarrow\cdots\longrightarrow z_d=x_d.
}
\tag{5.1}
\]

Every step is valid, every state is an integer, and the terminal endpoint agrees exactly with the original stopped history.

The total rational holonomy is

\[
\boxed{
b_1b_2\cdots b_d=N/x_d.}
\tag{5.2}
\]

No floor error appears in the transformed chain.

---

## FRR-T03 — Depth-two reflection

For two actions `a,b`, suppose the second action is rejected after the first, and write

\[
x=\lfloor N/a\rfloor,
\qquad b>x.
\]

The proposal states are `x` and `b`, so the reflected valid pair is

\[
\boxed{
(N/b,\ b/x).
}
\tag{6.1}
\]

It gives

\[
N\xrightarrow{N/b}b
\xrightarrow{b/x}x,
\]

exactly preserving the stopped endpoint.

A second floor-safe factorization is

\[
(N/b,\ ab/N),
\]

because

\[
\left\lfloor
b/(ab/N)
\right\rfloor
=\lfloor N/a\rfloor=x.
\]

The sorted-proposal factorization (6.1) has the advantage of extending canonically to every depth.

---

## 7. Finite carrier and recoverability

The reflected state retains

\[
\boxed{
(a_1,\ldots,a_d;
 y_1,\ldots,y_d;
 \sigma;
 b_1,\ldots,b_d;
 x_d).
}
\tag{7.1}
\]

If the original action tuple is retained, the reflection is a deterministic derived channel and no information is lost. The sorting permutation records equal-value tie order and is part of provenance.

The carrier is finite at every finite cutoff. Rational actions are represented exactly by finite prime-valuation vectors in the group completion of the positive holonomy monoid.

They are not new spatial axes and are not asserted to be primitive prime births.

---

## 8. Weight pushforward

Give the original action tuple product weight

\[
w(a_1,\ldots,a_d)
=\prod_{j=1}^du_{a_j}.
\]

Push this weight unchanged through the reflection map. This produces a positive measure on fully valid rational histories whose endpoint law is exactly the original stopped endpoint law.

Thus

\[
\boxed{
\mu_{N,d}^{\rm stop}
=(\operatorname{endpoint})_*
\widetilde\Pi_{N,d}^{\rm rational-valid}
}
\tag{8.1}
\]

with equality at every finite cutoff.

The factorial canonical valid measure

\[
d!\,J_N^d
\]

is a different positive gauge on valid histories. The stopped/Beta defect is the difference between these two gauges after endpoint projection.

---

## 9. Exact common-history relation field

Because both gauges now live on valid histories of the same depth, define a common rational-history relation field before endpoint recoalescence. For two reflected/canonical histories `h,h'`, retain

\[
Z_{h,h'}
=w_hw_{h'}
\bigl(f(\operatorname{end}h)-
 f(\operatorname{end}h')\bigr).
\]

The six depth-four normal-ordering contexts are all readouts of this common carrier under different marginal gauges.

This closes the state-typing part of the mixed-chamber lift:

\[
\boxed{
\text{MIXED STOPPING CHAMBERS}
\longrightarrow
\text{FULLY VALID RATIONAL PROVENANCE HISTORIES}.
}
\]

No endpoint-dependent value needs to be reconstructed after recoalescence.

---

## 10. Remaining gauge theorem

The rational reflection does not by itself show that the reflected gauge is close to the canonical prime-power valid gauge for arbitrary readouts.

The remaining theorem is now precisely a positive gauge comparison on one common finite carrier. Valid forms include:

1. a Hoeffding/Gram domination of their centered relation fields;
2. a tail-capacity potential absorbing their Radon--Nikodym mismatch;
3. a growing-depth signed cancellation of the gauge difference;
4. a block Poincare inequality on the rational-holonomy factorization graph.

The path, endpoint, floor, and recoverability issues have all been removed.

---

## 11. Relation to the ideal spacings map

Under logarithmic Haar measure, the proposal reflection is measure preserving. Sorting the proposal states and taking ratios is exactly the multiplicative form of the cube-to-simplex spacings map.

The `d!` sorting chambers then push to the same valid-history gauge, so the reflected and canonical measures coincide.

For prime-winding weights, their difference is the arithmetic gauge curvature measured by the commutator defects `D_(N,k)`.

---

## 12. Classification

Closed exactly:

1. proposal-state construction;
2. stopped endpoint as a running minimum;
3. stable sorting provenance;
4. positive rational spacing actions;
5. fully valid transformed history;
6. exact floor-safe endpoint preservation;
7. finite recoverable carrier;
8. positive weight pushforward;
9. common rational-history relation carrier.

Open:

1. comparison of reflected and canonical gauges;
2. a block spectral gap on their centered difference;
3. coefficient-safe composition with the four-level Mellin state;
4. a promoted native remainder.
