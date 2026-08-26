# P017 — Full-Basin c=103/20 Terminal T4 Rosser Certificate

Status: `PROVED_WIP EXACT 68-STATE SUPPORT + DUSART PARTIAL-SUMMATION CERTIFICATE / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Companion checker:

`experiments/p017_p2_full_basin_c515_terminal_t4_certificate_20260826.py`

Depends on:

- the full-basin sharp-odd carry model;
- the standard beta-2 upper Rosser–Iwaniec support conditions;
- Iwaniec–Laborde (1981), equation (3), for the terminal weighted-prime term;
- Dusart (2010), explicit unconditional upper/lower bounds for `pi(x)`.

Purpose: replace the diagnostic terminal `T4` error near `0.0012372 L` for the finite-oriented rational packet

\[
\boxed{
a=6,\qquad b=\frac{93}{20},\qquad c=\frac{103}{20},\qquad b+c=\frac{49}{5}
}
\]

by a rigorous explicit upper bound at the Tier-A full-basin splice.

---

## 1. Full-basin scale and terminal interval

Put

\[
K_0=116009280740973308,
\qquad W=K_0+1,
\qquad L=2K_0,
\]

and

\[
D=W^{10/9}.
\]

For the selected packet,

\[
D^{b/a}=W^{31/36},
\qquad
D^{c/a}=W^{103/108}.
\]

Let

\[
A=W^{31/36},
\qquad
C=W^{103/108}.
\]

The terminal weighted-prime term in the Iwaniec–Laborde weight is

\[
T_4
=
\sum_{A\le p<C}
\left(c-a\frac{\log p}{\log D}\right)
S(\mathcal A_p,z),
\]

inside the overall prefactor

\[
\frac1{2c-b-1}.
\]

Here

\[
2c-b-1=\frac{93}{20}.
\]

For the sharp odd full-basin sequence, each odd congruence remainder is a one-incidence carry and obeys

\[
|e(q)|<1.
\]

Thus the terminal upper-sieve remainder may be bounded by the weighted cardinality of the upper Rosser support.

---

## 2. The upper Rosser support has exactly 68 maximal states

For the beta-2 upper Rosser–Iwaniec weight, write a support modulus as

\[
d=p_1\cdots p_r,
\qquad p_1>\cdots>p_r.
\]

A support state at upper-sieve level `Q` obeys the odd-position conditions

\[
\boxed{
 p_1\cdots p_{j-1}p_j^3<Q
 \qquad(j\text{ odd}).
}
\tag{T4-1}
\]

For an external terminal prime `p`, the inner level is

\[
Q=\frac Dp.
\]

At the lower terminal endpoint the maximal inner level is

\[
Q_{\max}
=
\frac{D}{D^{b/a}}
=W^{1/4}.
\]

Exact integer comparison gives

\[
18455<Q_{\max}<18456.
\]

The `j=1` case of (T4-1) therefore forces

\[
p_1^3<Q_{\max},
\]

so every small prime in an upper-support state belongs to the set

\[
\boxed{
\{3,5,7,11,13,17,19,23\}.
}
\]

For a chosen descending tuple define the exact activation threshold

\[
\boxed{
q_{\rm crit}
=
\max_{j\text{ odd}}
 p_1\cdots p_{j-1}p_j^3.
}
\tag{T4-2}
\]

The state is available only when

\[
q_{\rm crit}<Q=\frac Dp,
\]

or equivalently

\[
p<\frac D{q_{\rm crit}}.
\]

Enumerating the `2^8` candidate subsets under (T4-2) gives exactly

\[
\boxed{68}
\]

maximal support states, distributed by number of prime factors as

\[
\boxed{1,8,28,26,5}
\qquad(\omega=0,1,2,3,4).
\]

The distinct activation thresholds are

\[
\boxed{
\begin{aligned}
1,&27,125,343,945,1331,1485,2079,2197,2457,3861,4913,\\
&5049,5967,6859,8721,9625,11375,12167,14875,16625,17875.
\end{aligned}
}
\tag{T4-3}
\]

Thus the terminal Rosser error is not a generic smooth-modulus sum: it is a finite 68-state weighted-prime problem.

---

## 3. Reindex the entire terminal remainder by support state

Define

\[
\phi(p)
=
c-a\frac{\log p}{\log D}.
\]

Because

\[
D=W^{10/9},
\]

we may write

\[
\boxed{
\phi(p)
=
\frac{103}{20}
-
\frac{27}{5}\frac{\log p}{\log W}.
}
\tag{T4-4}
\]

For a support state of threshold `q`, put

\[
B_q
=
\min\left(C,\frac Dq\right).
\]

After interchanging the finite support sum with the external-prime sum, the terminal carry remainder is bounded by

\[
\boxed{
|R_{T_4}|
\le
\frac{1}{2c-b-1}
\sum_{\text{68 states}}
\sum_{A\le p<B_{q_{\rm crit}}}
\phi(p).
}
\tag{T4-5}
\]

This reindexing is exact at the level of the support envelope; no bilinear factorization multiplicity appears.

---

## 4. Explicit prime-count bounds

Dusart's unconditional estimates give

\[
\boxed{
\pi(x)\ge\frac{x}{\log x-1}
\quad(x\ge5393),
}
\tag{T4-6}
\]

and

\[
\boxed{
\pi(x)\le\frac{x}{\log x-1.1}
\quad(x\ge60184).
}
\tag{T4-7}
\]

The smallest terminal endpoint here is larger than

\[
4.9\times10^{14},
\]

so both estimates apply throughout.

For integer endpoints `A_0<B_0`, Abel summation and

\[
\phi'(t)
=-\frac{27}{5\log W}\frac1t
\]

give

\[
\sum_{A_0<p\le B_0}\phi(p)
=
\phi(B_0)\pi(B_0)
-\phi(A_0)\pi(A_0)
+
\frac{27}{5\log W}
\int_{A_0}^{B_0}\frac{\pi(t)}t\,dt.
\]

Applying (T4-6)–(T4-7),

\[
\boxed{
\begin{aligned}
\sum_{A_0<p\le B_0}\phi(p)
\le{}&
\phi(B_0)\frac{B_0}{\log B_0-1.1}
-
\phi(A_0)\frac{A_0}{\log A_0-1}\\
&+
\frac{27}{5\log W}
\int_{A_0}^{B_0}
\frac{dt}{\log t-1.1}.
\end{aligned}
}
\tag{T4-8}
\]

The last integrand is positive and decreasing. The checker subdivides every interval into 16 integer panels and uses the left-endpoint rectangle as a rigorous upper sum.

---

## 5. Exact arithmetic implementation

No floating-point evaluation is needed for the theorem.

The checker obtains the integer terminal endpoints by comparisons such as

\[
n^{36}<W^{31},
\qquad
n^{108}<W^{103},
\qquad
(qn)^9<W^{10}.
\]

It finds

\[
\lfloor A\rfloor
=494793856728459,
\]

\[
\lfloor C\rfloor
=18813514064055713,
\]

and

\[
\lfloor W^{1/4}\rfloor=18455.
\]

Every logarithm is enclosed with exact `Fraction` arithmetic after binary range reduction:

\[
\log x
=k\log2+\log r,
\qquad 1\le r<2,
\]

and

\[
\log r
=2\sum_{j=0}^{N}\frac{z^{2j+1}}{2j+1}+R_N,
\qquad
z=\frac{r-1}{r+1},
\]

with the elementary geometric tail bound. The frozen checker uses degree `28`, already far tighter than required.

---

## 6. Final terminal bound

Summing (T4-8) over all 68 states and restoring the terminal prefactor yields the exact rational inequality

\[
\boxed{
\frac{|R_{T_4}|}{2K_0}
<
\frac1{800}
=0.00125.
}
\tag{T4-9}
\]

For orientation only, converting the checker's final rational upper bound to decimal gives approximately

\[
0.0012435533866.
\]

The decimal is not used in the proof.

Combining with the already-frozen lower Rosser base remainder

\[
\frac{|R_0^-|}{L}<0.00145,
\]

we now have the rigorous joint finite budget

\[
\boxed{
\frac{|R_0^-|+|R_{T_4}|}{L}
<0.00270.
}
\tag{T4-10}
\]

---

## 7. Consequence and remaining frontier

The terminal `T4` error is no longer diagnostic and no longer part of the unresolved finite constant problem for the packet

\[
\boxed{b=93/20,\qquad c=103/20.}
\]

The remaining tasks are:

1. certify the corresponding source-decimal main coefficient at this `c` on the same normalization;
2. quantify the finite prime/Mertens normalization loss;
3. bound the residual `T1–T3` terms, preferentially by their actual Rosser supports rather than by the generic factorable decomposition constant;
4. compare the resulting total against the Tier-A splice.

No finite analytic P2 threshold, P2-in-every-square theorem, Legendre theorem, or canonical promotion is claimed here.
