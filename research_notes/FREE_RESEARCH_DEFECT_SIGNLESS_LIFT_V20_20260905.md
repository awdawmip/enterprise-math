# Free Research — Signless Lift of the First Volterra Defect

Status: `FREE_RESEARCH_FRONTIER / DETERMINISTIC-QUOTIENT COMMUTATOR EXPLICIT / FINAL HISTORY GRADIENT LIFTED TO POSITIVE FOURTH-ORDER PACKET / RECTANGLE ERROR LOWER ORDER / PACKET DECAY OPEN / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-05`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_LOG_RECTANGLE_COMMUTATOR_CLOSURE_V19_20260905.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260905`

## 1. Executive result

The last term in the parity-corrected reverse frame is an odd-history square function of

\[
D=[M_A,L]-L^2.
\]

It can be lifted exactly through one signless quotient edge.  Let

\[
(Q_cf)(n):=f(q_c(n)),
\qquad
\delta_c:=I+Q_c,
\]

and assume `f(0)=0`.  Then

\[
\boxed{
\delta_cDf
=D\delta_cf+[Q_c,D]f.
}\tag{1.1}
\]

The new commutator is not a large uncontrolled operator.  It is again the bounded logarithmic rectangle curvature:

\[
\boxed{
([Q_c,D]f)(n)
=
\sum_{ac\le n}u_a\,\kappa_A(n;a,c)\,
 f(q_{ac}(n)),
}\tag{1.2}
\]

where

\[
\kappa_A(n;a,c)
=A(q_a(n))+A(q_c(n))-A(n)-A(q_{ac}(n)).
\tag{1.3}
\]

Thus, under `|A-log|<=C`,

\[
|\kappa_A|\le K_C:=4C+2\log2.
\tag{1.4}
\]

The final history-gradient channel is therefore controlled by a positive stopped pair acting on the original signless edge `delta_c f`, plus a lower-order rectangle error.

---

## 2. Quotient commutation

For every positive action `c`, quotient composition gives

\[
Q_cQ_a=Q_aQ_c=Q_{ac}.
\]

On fields with `f(0)=0`, the adaptive positive operator

\[
L=\sum_au_aQ_a
\]

also commutes with `Q_c`: terms with `ac>n` land at the absorbing zero state and vanish.

Since

\[
D=[M_A,L]-L^2,
\]

and `Q_c` commutes with `L`,

\[
[Q_c,D]
=[Q_c,M_A]L-L[Q_c,M_A].
\tag{2.1}
\]

Put

\[
V_c(n):=A(n)-A(q_c(n)).
\]

Then

\[
[Q_c,M_A]=-M_{V_c}Q_c.
\]

Using quotient commutation once more gives

\[
([Q_c,D]f)(n)
=
\sum_{ac\le n}u_a
\bigl(V_c(q_a(n))-V_c(n)\bigr)f(q_{ac}(n)).
\]

The coefficient equals (1.3), proving (1.2).

---

## 3. Positive stopped-square carrier for `D`

At a state `n`, the first defect has the exact parity-fold form

\[
(Dh)(n)
=
\sum_{a,b\le n}u_au_b\varepsilon_n(a,b)
 h(\Phi_n(a,b)),
\tag{3.1}
\]

where

\[
\Phi_n(a,b)=
\begin{cases}
q_{ab}(n),&ab\le n,\\
q_a(n),&ab>n,
\end{cases}
\]

and `epsilon=-1` on the valid triangle, `+1` on the stopped complement.

The unsigned mass of the complete action square is exactly `A(n)^2`.  Hence Cauchy--Schwarz gives

\[
\boxed{
|Dh(n)|^2
\le
A(n)^2\,\mathscr O_2(h;n),
}\tag{3.2}
\]

where

\[
\boxed{
\begin{aligned}
\mathscr O_2(h;n):={}&
\sum_{ab\le n}u_au_b|h(q_{ab}(n))|^2\\
&+
\sum_{ab>n}u_au_b|h(q_a(n))|^2.
\end{aligned}}
\tag{3.3}
\]

This is the positive stopped odd-square packet already underlying the V15 scalar readout.

---

## 4. One-edge defect estimate

Apply (3.2) to

\[
h=\delta_cf.
\]

From (1.1) and `(x+y)^2<=2x^2+2y^2`,

\[
\boxed{
|\delta_cDf(n)|^2
\le
2A(n)^2\mathscr O_2(\delta_cf;n)
+2K_C^2A(q_c(n))^2\|f\|_\infty^2.
}\tag{4.1
\]

Indeed the absolute coefficient mass in (1.2) is at most

\[
K_C\sum_{a\le q_c(n)}u_a
=K_CA(q_c(n)).
\]

Summing over `c` gives

\[
\boxed{
\sum_{c\le n}u_c|\delta_cDf(n)|^2
\le
2A(n)^2\mathscr O_4(f;n)
+2K_C^2\|f\|_\infty^2
\sum_{c\le n}u_cA(q_c(n))^2,
}\tag{4.2
\]

with the explicit positive fourth-order packet

\[
\boxed{
\mathscr O_4(f;n)
:=
\sum_{c\le n}u_c\mathscr O_2(\delta_cf;n).
}\tag{4.3
\]

The second term is lower order because

\[
\sum_{c\le n}u_cA(q_c(n))^2\le A(n)^3.
\tag{4.4}
\]

Thus its normalized size relative to `A(n)^4` is `O(1/A(n))`.

---

## 5. Odd-history telescoping

Take an even integer `k`, and put `h=k-1`, so `h` is odd.  Along every valid history

\[
n=x_0\to x_1\to\cdots\to x_h,
\]

there is the exact parity telescoping identity

\[
\boxed{
Df(x_0)+Df(x_h)
=
\sum_{r=0}^{h-1}(-1)^r
\delta_{a_{r+1}}Df(x_r).
}\tag{5.1}
\]

Consequently

\[
|Df(x_0)+Df(x_h)|^2
\le
h\sum_{r=0}^{h-1}
|\delta_{a_{r+1}}Df(x_r)|^2.
\tag{5.2}
\]

Averaging (5.2) over the positive `h`-history measure and using (4.1) lifts the sole remaining V19 frame term to transported copies of `mathscr O_4(f; x_r)` plus a rectangle-error term of normalized order at most `O(h^2/A(n))` under the growing-depth mass bounds.

For the natural choice

\[
h\asymp\log\log n,
\]

the rectangle contribution tends to zero.

---

## 6. Exact provenance meaning of `mathscr O_4`

The packet (4.3) consists of four ordered action slots before recoalescence:

1. the signless suffix action `c`;
2. two parity-fold actions `a,b`;
3. the retained distinction between a valid pair endpoint `q_(ab)` and a stopped endpoint `q_a`.

On the valid part,

\[
\delta_cf(q_{ab}(n))
=f(q_{ab}(n))+f(q_{abc}(n)).
\]

On the stopped part,

\[
\delta_cf(q_a(n))
=f(q_a(n))+f(q_{ac}(n)).
\]

Thus every term is an ordinary signless quotient edge evaluated after a retained stopped/valid provenance decision.  No new analytic observable is introduced.

---

## 7. Updated closure target

Combining V19 and this note gives, for bounded `f` with bounded full residual and one even depth

\[
k(n)\to\infty,
\qquad
k(n)=o(\sqrt{\log n}),
\]

a schematic exact-positive reduction

\[
\boxed{
\frac{|Df(n)|^2}{A(n)^4}
\preccurlyeq
\operatorname{HistAvg}_{k(n)}
\left[
\frac{\mathscr O_4(f;\cdot)}{A(\cdot)^2}
\right]
+o(1).
}\tag{7.1}
\]

The unique remaining mathematical task is now:

\[
\boxed{
\text{prove decay of the transported normalized fourth-order stopped odd-square packet for }f=r.
}
\]

Equivalently, construct a positive recurrence for `mathscr O_4` or identify it as a controlled subpacket of the already retained V14/V15 multichannel energy.

This is strictly narrower than controlling an arbitrary history variance of `Df`: all commutator and coefficient mismatch terms are explicit and lower order.

No quantitative prime remainder, Working Truth, Foundation status, or RH-scale conclusion is asserted.
