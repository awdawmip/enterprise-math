# P017 — Rigorous positive main margin for the `a=5` Iwaniec–Laborde packet

Status: `PROVED_WIP MAIN-TERM POSITIVITY / NOT CANONICAL / ANALYTIC REMAINDER CONSTANTS STILL NONEXPLICIT`

Date: `2026-08-24`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

This note upgrades the previous numerical main-term diagnostic for

\[
\theta=\frac{49}{100},\quad a=5,\quad d=\frac35,\quad b=3,\quad c=\frac{13}{3}
\]

to a rigorous positive lower bound using only the standard Jurkat–Richert delay equations, elementary integration, monotonicity of one explicit geometric kernel, and certified rational bounds for logarithms.

## 1. Normalization

Put

\[
C=2e^\gamma.
\]

For the standard dimension-one linear-sieve functions,

\[
F(s)=\frac Cs\qquad(0<s\le3),
\]

and

\[
f(s)=\frac{C\log(s-1)}s\qquad(2<s\le4).
\]

For larger arguments they satisfy

\[
(sF(s))'=f(s-1),\qquad (sf(s))'=F(s-1).
\]

Only `F` on `(0,4]` and `f(5)` are needed for the present packet.

## 2. Elementary envelope for F on [3,4]

For `2<=v<=3`,

\[
\log(v-1)\le v-2\le \frac v3,
\]

hence

\[
f(v)=C\frac{\log(v-1)}v\le\frac C3.
\]

Therefore for `3<=s<=4`,

\[
sF(s)
=3F(3)+\int_3^s f(u-1)\,du
\le C+\frac C3(s-3)
=\frac{Cs}{3}.
\]

Thus

\[
\boxed{F(s)\le C/3\quad(3\le s\le4).}
\]

Together with the exact formula below 3 this gives the usable upper envelope

\[
F(s)\le
\begin{cases}
C/s,&0<s\le3,\\
C/3,&3\le s\le4.
\end{cases}
\]

## 3. Elementary lower bound for f(5)

Since `(sF(s))'=f(s-1)>=0`, for `3<=s<=4` one has

\[
sF(s)\ge3F(3)=C,
\]

so

\[
F(s)\ge C/s.
\]

Also `4f(4)=C log 3`. Hence

\[
5f(5)
=4f(4)+\int_4^5F(u-1)\,du
\ge C\log3+C\int_3^4\frac{dv}{v}
=C\log4.
\]

Therefore

\[
\boxed{f(5)\ge \frac{C\log4}{5}.}
\]

## 4. The p.53 W1 brace

For the fixed packet, write the general Iwaniec–Laborde p.53 brace as `B`:

\[
W_1\ge e^{-\gamma}\frac y{\log D}\frac a{2c-b-1}\,(B-E),
\]

where `E=o(1)` and

\[
\begin{aligned}
B={}&(2c-b-1)f(a)\\
&-(c-b)I_1-I_2-I_3-I_4.
\end{aligned}
\]

The four `I_j` are exactly the four positive integrals displayed in the first inequality on p.53 of the 1981 paper.

For `a=5,b=3,c=13/3`, the positive coefficient is

\[
2c-b-1=\frac{14}{3}.
\]

By §3,

\[
\frac1C(2c-b-1)f(5)
\ge \frac{28}{15}\log2.
\]

## 5. Upper bound for I1

Here the `F` argument is `5(1-t)`, with `t in [1/5,3/5]`; the threshold `F`-argument `3` occurs at `t=2/5`. The envelope in §2 gives exactly

\[
\frac{I_1}{C}
\le
J_1
:=
-\frac1{15}\log2+\frac25\log3.
\]

Since `c-b=4/3`, its contribution to the normalized lower bound is `-(4/3)J_1`.

## 6. Upper bound for I3

The `F` argument is `(1-t)/t`, with `t in [1/5,2/5]`; it equals `3` at `t=1/4`. Splitting there and integrating the same envelope gives

\[
\frac{I_3}{C}
\le
J_3
:=
\frac4{15}+\frac{92}{15}\log2-\frac83\log5.
\]

## 7. Exact envelope for I4

On `t in [3/5,49/60]`, the argument `5(1-t)` is at most 2, so `F=C/[5(1-t)]` exactly. Therefore

\[
\frac{I_4}{C}
=J_4
:=
\frac{13}{15}\log\frac{49}{36}
+\frac2{15}\log\frac{11}{24}.
\]

## 8. Coarse but rigorous upper bound for the double integral I2

Throughout the double-integral domain the `F` argument lies in `[3/2,4]`. Hence the envelope gives the uniform bound

\[
F\le \frac{2C}{3}.
\]

Consequently

\[
\frac{I_2}{C}
\le\frac23 J_2,
\]

where

\[
J_2
=\int_{1/5}^{2/5}
\frac1s\log\frac{4/5-s}{s}\,ds.
\]

Let

\[
g(s)=\frac1s\log\frac{4/5-s}{s}.
\]

On `[1/5,2/5]` the logarithm is nonnegative and its derivative is negative, so

\[
g'(s)<0.
\]

Using eight equal subintervals of width `1/40`, the left Riemann sum therefore gives the rigorous bound

\[
J_2\le U_2
:=
\sum_{i=0}^{7}
\frac1{8+i}
\log\frac{24-i}{8+i}.
\]

## 9. Closed lower bound

Define

\[
L=
\frac{28}{15}\log2
-\frac43J_1
-\frac23U_2
-J_3
-J_4.
\]

Then

\[
\boxed{B\ge CL.}
\]

For the fixed packet the Lemma-6 normalized high-tail ratio is exactly

\[
R=
\frac{4(dc/a-\theta)}{3\theta-1}
=\frac{12}{47}.
\]

Since `C=2e^gamma`, after multiplying the W1 brace by `e^-gamma` the Euler constant cancels, and the normalized net main coefficient satisfies

\[
\boxed{
S_{\rm net}
\ge 2L-\left(\frac{12}{47}\right)^2.
}
\]

Using the certified logarithm enclosure described below gives

\[
\boxed{
2L-\left(\frac{12}{47}\right)^2
>0.05896564935.
}
\]

Thus the asymptotic main coefficient is rigorously positive with a fixed margin above `0.0589`. In particular the `o(1)`/`E` term in the p.53 inequality can be absorbed for sufficiently large `x`.

## 10. Certified logarithm evaluation

No floating-point assumption is needed for the sign. For any positive rational `q`, set

\[
u=\frac{q-1}{q+1}.
\]

For `q>1`,

\[
\log q
=2\sum_{n\ge0}\frac{u^{2n+1}}{2n+1},
\]

and after truncating at `n=N-1` the positive tail is bounded by

\[
0<R_N
\le
\frac{2u^{2N+1}}{(2N+1)(1-u^2)}.
\]

For `0<q<1`, use `log q=-log(1/q)`. Applying this with exact rational arithmetic to every logarithm above and `N=30` yields the certified interval

\[
0.0589656493562
<
2L-(12/47)^2
<
0.0589656493620.
\]

The companion checker implements only `Fraction` arithmetic and this positive-tail estimate.

## 11. What is and is not closed

Closed at `PROVED_WIP` scope:

- exact packet geometry (`theta=49/100,a=5,d=3/5,b=3,c=13/3`);
- strict Lemma-4/Lemma-6 exponent compatibility;
- rigorous positivity of the asymptotic `W1-W2` main coefficient with margin `>0.05896564935`;
- exact P017 odd-carry transfer `O_m-K/m=r_K(m)-r_K(2m)` from the preceding bridge note.

Still open:

- an explicit numerical `x_0`: Lemmas 2, 4 and 6 contain implicit constants and `x sufficiently large`;
- exact finite overlap with a verified consecutive-square range;
- any improvement in those constants from the special P017 square endpoint.

Therefore the route has crossed the **main-term sign gate**. The remaining frontier is now purely the effective remainder/constant gate.
