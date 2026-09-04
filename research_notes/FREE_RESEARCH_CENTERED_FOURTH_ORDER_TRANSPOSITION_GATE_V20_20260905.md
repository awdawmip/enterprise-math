# Free Research — Centered Fourth-Order Transposition Gate

Status: `FREE_RESEARCH_FRONTIER / PARITY COVARIANCE CENTERING / RAW FOURTH MOMENT REPLACED BY PAIR S3 DIRICHLET ENERGY / IMBALANCE AND RECTANGLE ERRORS LOWER ORDER / DIRICHLET DECAY OPEN / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-05`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_DEFECT_SIGNLESS_LIFT_V20_20260905.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260905`

## 1. Why the raw stopped square is too large

The first signless lift bounded `D h` by the raw second moment of `h` under the stopped pair square.  This is positive but wastes the exact cancellation of the ideal Volterra carrier.

The correct object is the variance of the folded endpoint field.  Let

\[
\pi_n(a,b)=\frac{u_au_b}{A(n)^2},
\]

\[
\varepsilon_n(a,b)=
\begin{cases}-1,&ab\le n,\\+1,&ab>n,
\end{cases}
\]

and

\[
\Phi_n(a,b)=
\begin{cases}q_{ab}(n),&ab\le n,\\q_a(n),&ab>n.
\end{cases}
\]

Then

\[
\frac{Dh(n)}{A(n)^2}
=\mathbb E_{\pi_n}\left[
\varepsilon_n(a,b)h(\Phi_n(a,b))
\right].
\tag{1.1}
\]

---

## 2. Exact parity covariance decomposition

Put

\[
F_h(a,b):=h(\Phi_n(a,b)),
\]

and

\[
\eta_n:=\mathbb E_{\pi_n}\varepsilon_n
=1-rac{2\mathcal C_2(n)}{A(n)^2}.
\]

Writing bars for `pi_n` means,

\[
\mathbb E(\varepsilon F_h)
=\mathbb E\bigl[(\varepsilon-\eta_n)(F_h-\bar F_h)\bigr]
+\eta_n\bar F_h.
\tag{2.1}
\]

Since `Var(epsilon)<=1`, Cauchy--Schwarz gives

\[
\boxed{
\frac{|Dh(n)|^2}{A(n)^4}
\le
2\operatorname{Var}_{\pi_n}(F_h)
+2\eta_n^2\|h\|_\infty^2.
}
\tag{2.2}
\]

The growing two-history mass law gives

\[
\eta_n=O(1/A(n)).
\tag{2.3}
\]

Thus the parity-imbalance term is already `O(A(n)^-2)` for bounded `h`.

---

## 3. Application to one signless edge of the first defect

Take

\[
h=\delta_cf,
\qquad
F_c(a,b):=\delta_cf(\Phi_n(a,b)).
\]

The exact deterministic-quotient lift is

\[
\delta_cDf=D\delta_cf+[Q_c,D]f.
\]

For `|f|<=B` and the rectangle constant

\[
K_C=4C+2\log2,
\]

we have

\[
|[Q_c,D]f(n)|
\le K_CA(q_c(n))B.
\]

Combining this with (2.2) and `||delta_c f||_infinity<=2B` gives

\[
\boxed{
\frac{|\delta_cDf(n)|^2}{A(n)^4}
\le
4\operatorname{Var}_{\pi_n}(F_c)
+16\eta_n^2B^2
+2K_C^2\frac{A(q_c(n))^2}{A(n)^4}B^2.
}
\tag{3.1}
\]

After normalized averaging over `c`, both explicit error terms are `O(B^2/A(n)^2)`.

---

## 4. Pair-valued `S_3` Dirichlet form

For a pair field `F(a,b)` on the product probability space `pi_n`, define

\[
\boxed{
\begin{aligned}
\mathcal D_n^{(2)}(F)
:=\frac16\mathbb E_{a,b,d}
\Big(&|F(a,b)-F(b,a)|^2\\
&+|F(a,b)-F(d,b)|^2\\
&+|F(a,b)-F(a,d)|^2\Big).
\end{aligned}}
\tag{4.1}
\]

The already established pair-valued lift--transpose--project spectrum gives

\[
\boxed{
\operatorname{Var}_{\pi_n}(F)
\le3\mathcal D_n^{(2)}(F).
}
\tag{4.2}
\]

Hence (3.1) sharpens to

\[
\boxed{
\frac{|\delta_cDf(n)|^2}{A(n)^4}
\le
12\mathcal D_n^{(2)}(F_c)
+O\!\left(\frac{B^2}{A(n)^2}
\right),
}
\tag{4.3}
\]

uniformly after averaging the displayed explicit errors.

Define the normalized fourth-order transposition packet

\[
\boxed{
\mathfrak D_4(f;n)
:=
\frac1{A(n)}
\sum_{c\le n}u_c
\mathcal D_n^{(2)}(F_c).
}
\tag{4.4}
\]

Every atom of `mathfrak D_4` is a difference of two stopped/valid, signless-edge histories before provenance recoalescence.

---

## 5. Relation to the existing carriers

The three transposition differences in (4.1) have exact meanings.

1. `F_c(a,b)-F_c(b,a)` vanishes on the valid chamber and is an ordered relation between stopped one-step endpoints on the stopped chamber.
2. `F_c(a,b)-F_c(d,b)` compares two histories with the same second slot and separates into valid/valid, stopped/stopped, and mixed cutoff chambers.
3. `F_c(a,b)-F_c(a,d)` is the corresponding common-first-slot relation.

After expanding

\[
\delta_cf(x)-\delta_cf(y)
=
\bigl(f(x)-f(y)\bigr)
+
\bigl(f(q_cx)-f(q_cy)\bigr),
\]

each term is an ordinary ordered relation field or its common-suffix transport.  The mixed chambers are precisely the moving-cutoff boundary channels isolated in V14/V15.

Thus `mathfrak D_4` introduces no new observable type.  It is the coefficient-safe fourth-order assembly of the already retained relation and tail channels.

---

## 6. Updated final reverse frame

Take even `k`, `h=k-1`, with

\[
k\to\infty,
\qquad
k=o(\sqrt{\log n}).
\]

The parity frame, alternating path telescoping, (4.3), and the automatic placement estimates yield

\[
\boxed{
\frac{|Df(n)|^2}{A(n)^4}
\preccurlyeq
\operatorname{HistAvg}_{h}
\left[
\mathfrak D_4(f;\cdot)
\right]
+o(1).
}
\tag{6.1}
\]

The `o(1)` contains:

- the factorially small high-order scalar defect;
- the `O(A^-2)` placement curvature;
- parity-mass imbalance;
- deterministic quotient rectangle errors.

For the prime error `r`, the parametrix then gives

\[
|r(n)|^2
\preccurlyeq
\operatorname{HistAvg}_{h}
\left[
\mathfrak D_4(r;\cdot)
\right]
+o(1).
\tag{6.2}
\]

---

## 7. Exact remaining gate

The last mathematical task is now the centered statement

\[
\boxed{
\operatorname{HistAvg}_{k(n)-1}
\left[
\mathfrak D_4(r;\cdot)
\right]
\longrightarrow0.
}
\]

This is strictly stronger typed and potentially smaller than the raw stopped packet `mathscr O_4` because the ideal folded mean has been removed before squaring.

A successful closure must perform a coefficient-safe chamber audit showing that the three pieces of `mathfrak D_4` are absorbed by:

- the existing `1/9` standard relation contraction;
- the V14 tail-potential lower-scale channels;
- the uniformly bounded full residual.

No native decay, quantitative prime remainder, Working Truth, Foundation status, or RH-scale conclusion is asserted yet.
