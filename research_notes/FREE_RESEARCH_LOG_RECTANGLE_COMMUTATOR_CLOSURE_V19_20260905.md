# Free Research — Log-Rectangle Closure of the Placement Curvature

Status: `FREE_RESEARCH_FRONTIER / DOUBLE COMMUTATOR EXPLICIT / RECTANGLE DEFECT UNIFORMLY BOUNDED / PLACEMENT CHANNEL AUTOMATICALLY SMALL / ONE PARITY-HISTORY CHANNEL REMAINS / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-05`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_COMMUTATOR_PLACEMENT_FRAME_V19_20260905.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260905`

## 1. Executive result

Let

\[
(Lf)(n)=\sum_{a\le n}u_a f(q_a(n)),
\qquad
A(n)=\sum_{a\le n}u_a,
\qquad
(M_Af)(n)=A(n)f(n),
\]

with nonnegative prime-winding weights `u_a=Lambda(a)/a`, and define

\[
D=[M_A,L]-L^2.
\]

The placement curvature from the reverse frame is

\[
[L,D]=[L,[M_A,L]].
\]

After the two ordered histories `(a,b)` and `(b,a)` are recoalesced at their common endpoint, this operator has the exact kernel

\[
\boxed{
([L,D]f)(n)
=
\sum_{ab\le n}u_au_b\,\kappa_A(n;a,b)\,
 f(q_{ab}(n)),
}\tag{1.1}
\]

where

\[
\boxed{
\kappa_A(n;a,b)
=A(q_a(n))+A(q_b(n))-A(n)-A(q_{ab}(n)).
}\tag{1.2}
\]

If

\[
|A(x)-\log x|\le C
\qquad(x\ge1),
\]

then

\[
\boxed{
|\kappa_A(n;a,b)|\le K_C:=4C+2\log2
}\tag{1.3}
\]

uniformly for every valid pair `ab<=n`.

Thus the placement curvature is a bounded coefficient on the ordinary positive two-history carrier.  In the growing-depth reverse frame its normalized contribution is `O(K_C^2/A(n)^2)`, hence tends to zero automatically.

---

## 2. Exact double-commutator expansion

Since

\[
D=M_AL-LM_A-L^2,
\]

and `L` commutes with its own powers,

\[
\begin{aligned}
[L,D]
&=L(M_AL-LM_A-L^2)
 -(M_AL-LM_A-L^2)L\\
&=2LM_AL-L^2M_A-M_AL^2.
\end{aligned}
\tag{2.1}
\]

Applied at `n`, the first expression gives the ordered-pair coefficient

\[
2A(q_a(n))-A(q_{ab}(n))-A(n).
\]

Because the weight and endpoint are invariant under `a<->b`, averaging the two ordered descriptions is exact and yields (1.1)--(1.2).

This is an instance where recoalescence is safe only after the placement relation has been formed: the individual ordered coefficient is not uniformly logarithmically flat, while the symmetric rectangle coefficient is.

---

## 3. Uniform logarithmic rectangle bound

Write

\[
A(x)=\log x+E(x),
\qquad |E(x)|\le C.
\]

For every real `t>=1`,

\[
\frac t2\le\lfloor t\rfloor\le t,
\]

so

\[
-\log2
\le
\log\lfloor t\rfloor-\log t
\le0.
\tag{3.1}
\]

For `ab<=n`, put

\[
m_a=q_a(n),\quad m_b=q_b(n),\quad m_{ab}=q_{ab}(n).
\]

The ideal logarithms cancel:

\[
\log(n/a)+\log(n/b)-\log n-\log(n/(ab))=0.
\]

The three floor errors contribute at most `2 log 2` in absolute value, while the four discrepancy terms contribute at most `4C`.  Hence (1.3).

---

## 4. Positive history-mass domination

Let

\[
\mathcal C_k(n):=L^k1(n)
=
\sum_{a_1\cdots a_k\le n}
\prod_{i=1}^ku_{a_i}.
\]

For every placement `0<=j<=k-2` and every bounded real field `f`, (1.1) gives

\[
\boxed{
\left|
L^j[L,D]L^{k-2-j}f(n)
\right|
\le
K_C\mathcal C_k(n)\|f\|_\infty.
}\tag{4.1)
\]

Each term is one ordered `k`-history packet with one bounded rectangle coefficient; no extra combinatorial multiplicity occurs for a fixed placement.

Consequently

\[
\sum_{j=0}^{k-2}
\left|
L^j[L,D]L^{k-2-j}f(n)
\right|^2
\le
(k-1)K_C^2\mathcal C_k(n)^2\|f\|_\infty^2.
\tag{4.2}
\]

---

## 5. Closure inside the reverse frame

The placement term in the V19 frame is

\[
\mathsf P_k
:=
\frac{2(k-1)(2k-1)}{3k\mathcal C_{k-1}(n)^2}
\sum_{j=0}^{k-2}
|L^j[L,D]L^{k-2-j}f(n)|^2.
\tag{5.1}
\]

The growing-depth factorial law gives, uniformly for

\[
k=o(\sqrt{\log n}),
\]

\[
\frac{\mathcal C_k(n)}{\mathcal C_{k-1}(n)}
=
\frac{A(n)}k
\exp\!\left(O\!\left(\frac{k^2}{\log n}\right)\right).
\tag{5.2}
\]

Combining (4.2) and (5.2),

\[
\boxed{
\frac{\mathsf P_k}{A(n)^4}
\le
\left(\frac43+o(1)\right)
\frac{K_C^2}{A(n)^2}
\|f\|_\infty^2.
}\tag{5.3}
\]

In particular,

\[
\boxed{
\mathsf P_k/A(n)^4\to0
}
\tag{5.4}
\]

uniformly for every growing depth in the factorial regime.

Thus condition `k mathfrak P_k -> 0` from the first V19 frame note is not an independent arithmetic hypothesis; it follows from the bounded first-mass discrepancy and boundedness of the field.

---

## 6. Updated reverse estimate

For bounded `f` and any `k=k(n)` with

\[
k\to\infty,
\qquad
k=o(\sqrt{\log n}),
\]

the first two terms of the reverse frame satisfy

\[
\frac{\text{high-order scalar term}}{A(n)^4}
=O(k^{-4})\|f\|_\infty^2,
\]

and

\[
\frac{\text{placement-curvature term}}{A(n)^4}
=O(A(n)^{-2})\|f\|_\infty^2.
\]

Therefore

\[
\boxed{
\frac{|Df(n)|^2}{A(n)^4}
\le
\frac{2}{\mathcal C_{k-1}(n)A(n)^4}
\sum_{\mathbf a}w_{\mathbf a}
|Df(n)-Df(q_{\mathbf a}(n))|^2
+o(1).
}\tag{6.1}
\]

The entire native closure problem has collapsed to one history-gradient channel.

---

## 7. Parity correction of the remaining channel

If `k` is even, the history length `k-1` is odd.  Use the parity-twisted history mean instead of the unsigned mean.  The same proof gives

\[
\boxed{
\frac{|Df(n)|^2}{A(n)^4}
\le
\frac{2}{\mathcal C_{k-1}(n)A(n)^4}
\sum_{|\mathbf a|=k-1}w_{\mathbf a}
|Df(n)+Df(q_{\mathbf a}(n))|^2
+o(1).
}\tag{7.1}
\]

The endpoint plus sign is the correct orientation for an approximate `-1` return mode.

Along each odd path

\[
n=x_0\to x_1\to\cdots\to x_{k-1},
\]

there is the exact alternating telescoping identity

\[
\boxed{
Df(x_0)+Df(x_{k-1})
=
\sum_{r=0}^{k-2}(-1)^r
\bigl(Df(x_r)+Df(x_{r+1})\bigr).
}\tag{7.2}
\]

Hence the remaining term is a positive, transported signless-edge square function for the first defect.

---

## 8. Updated unique gate

Closed:

1. explicit double-commutator kernel;
2. uniform boundedness of its coefficient;
3. automatic decay of the entire placement-curvature channel;
4. parity-corrected one-channel reverse frame.

Open:

\[
\boxed{
\text{control the odd-history signless square function of }Df
\text{ by the retained prime-winding energy and bounded residual.}
}
\]

Equivalently, for one even depth `k(n)` in the growing factorial regime, prove

\[
\frac1{\mathcal C_{k-1}(n)A(n)^4}
\sum_{|\mathbf a|=k-1}w_{\mathbf a}
|Df(n)+Df(q_{\mathbf a}(n))|^2
\to0.
\]

This is now the sole mathematical bridge.  No quantitative remainder, Working Truth, Foundation status, or RH-scale conclusion is asserted.
