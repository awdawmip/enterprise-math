# PREFIX-1018 — All-length strict positive-port dominance for the frozen X6 BRC Link observer

Date: 2026-11-23 (Asia/Shanghai). Research grade: **AUTHOR_EXACT_COMPUTER_ASSISTED_PROOF / SYMBOLIC_RATIONAL_AND_INTEGER_CHECKED / NOT_REVIEWED**. Continuation of PREFIX-1016–1017, with frozen P000 V5 and the existing Stage46 candidate BRC model. All numerical and symbolic checks specified below were executed locally with exact arithmetic. This source is an author research note, not a Result, Review or Foundation promotion.

## 1. Exact inherited scientific input and claimed observer

Frozen P000 V5: [immutable foundation](https://github.com/awdawmip/enterprise-math/blob/f42f2906d77f24085c123f3ccfe9667d41caa96d/p000_reality_foundation.json). The X6 state has six native signed axes, twelve primitive directions, initial chart-relative Cell 0 and incoming port −e1. The candidate Stage46 signed BRC kernel has weight w(h,d)=1−6[h=d]. Both orientations of the native Link {0,e1} are absorbed. Grade k=1 contains exactly one negative native step. Signed contributions interfere only within the same joint Cell–terminal-port fibre before their squares are summed.

For n≥5, let Q⁺_{n,1} be the integer square-numerator mass for the distinguished positive terminal port and Q⁺_{n,j} the mass for any **single** other positive port j=2,…,6. By the five-axis permutation symmetry the latter are equal. The normalized port masses are Q⁺/36^n.

**THEOREM (new).** For every integer n≥5 and every j=2,…,6,

\[
\boxed{Q^+_{n,1}-Q^+_{n,j}>0.}
\]

The proof reduces an infinite family of coherent-square inequalities to a rational invariant interval and nine exact integer cases. This closes the all-length sign question left open in PREFIX-1016–1017. The distinct negative-port analogue was proved in PREFIX-1015.

## 2. Previous exact collision reduction (not reproved)

Define the six-label collision count

\[
A(r)=A_6(r)=\sum_{a_1+\cdots+a_6=r}\left(\frac{r!}{a_1!\cdots a_6!}\right)^2>0.
\]

Put m=n−4≥1 and Δ⁺_n=Q⁺_{n,1}−Q⁺_{n,j}. The frozen joint-Cell–port Laurent proof of [PREFIX-1016](https://github.com/awdawmip/enterprise-math/blob/f92e6bcc26ce177ac70648adb62a0cf0aa7ef37c/research_notes/portable_direct/2026-11-22_r6_prefix1016_positive_port_three_A6_shifts.md) gives

\[
\Delta^+_{m+4}=c_1(m)A(m+1)+c_2(m)A(m+2)+c_3(m)A(m+3)
\]

with exact coefficients

\[
\begin{aligned}
c_1(m)&=-\frac{72(72m^2+163m+80)}{5(m+1)},\\
c_2(m)&=\frac{2(144m^3+1135m^2+2367m+1310)}{5(m+1)(m+2)},\\
c_3(m)&=-\frac{2(m+8)(2m+5)}{5(m+2)}.
\end{aligned}
\]

Only the sign of this already verified final-observer contrast is studied here. The original BRC path/branch/port provenance remains in the source model for later operations.

## 3. New order-three exact recurrence for the collision integers

**Lemma 1.** For every integer r≥2,

\[
\boxed{\begin{aligned}
(r+1)^5 A(r+1)={}&2(2r+1)(14r^4+28r^3+28r^2+14r+3)A(r)\\
&-4r^3(196r^2+59)A(r-1)\\
&+1152(2r-1)r^2(r-1)^2A(r-2).
\end{aligned}}
\]

The starting terms are A(0)=1, A(1)=6, A(2)=66.

**Proof.** Introduce formal power series g(t)=Σ_{r≥0}t^r/(r!)² and f(t)=g(t)^6=Σ_{r≥0}A(r)t^r/(r!)². Direct coefficient comparison yields tg''+g'−g=0. The seven exact states v_j=g^{6−j}(g')^j, j=0,…,6, satisfy

\[
t v_j'=(6-j)t v_{j+1}+j(v_{j-1}-v_j),
\]

with missing boundary terms set to zero. Write each derivative of f=v_0 as a rational seven-state row. Differentiating and eliminating those rows gives the explicit polynomial differential identity

\[
\begin{aligned}
0={}&t^6f^{(7)}+21t^5f^{(6)}
-28t^4(2t-5)f^{(5)}
-350t^3(2t-1)f^{(4)}\\
&+7t^2(112t^2-344t+43)f^{(3)}
+21t(224t^2-116t+3)f''\\
&-(2304t^3-5724t^2+516t-1)f'
-6(576t^2-170t+1)f.
\end{aligned}
\]

The companion executable checks this full symbolic seven-state row identity, avoiding a recurrence guessed from data. For t^q f^{(j)}, the coefficient of t^r is

\[
\frac{(r+j-q)^{\underline j}\,A(r+j-q)}{((r+j-q)!)^2}.
\]

Collecting the four shifts −2,−1,0,1 in the polynomial identity produces, respectively, the coefficient polynomials

\[
-1152(2r-1),\quad4r(196r^2+59),\quad
-2(2r+1)(14r^4+28r^3+28r^2+14r+3),\quad
(r+1)^7.
\]

Multiply by (r!)² and rearrange to obtain the displayed recurrence. All four polynomials are independently checked symbolically by the script. ∎

## 4. New uniform rational enclosure for every adjacent ratio

Put R_r=A(r+1)/A(r). Define

\[
L(r)=36-\frac{90}{r}+\frac{180}{r^2}-\frac{360}{r^3}-\frac{2500}{r^4},
\quad
U(r)=36-\frac{90}{r}+\frac{180}{r^2}-\frac{360}{r^3}+\frac{2500}{r^4}.
\]

**Lemma 2.** For all integers r≥9, the strict inequalities L(r)<R_r<U(r) hold.

**Proof.** Lemma 1 becomes

\[
R_r=F_r(R_{r-1},R_{r-2})
=\alpha_r-\frac{\beta_r}{R_{r-1}}
+\frac{\gamma_r}{R_{r-1}R_{r-2}},
\]

where

\[
\alpha_r=\frac{2(2r+1)(14r^4+28r^3+28r^2+14r+3)}{(r+1)^5},
\quad
\beta_r=\frac{4r^3(196r^2+59)}{(r+1)^5},
\quad
\gamma_r=\frac{1152(2r-1)r^2(r-1)^2}{(r+1)^5}.
\]

For r≥11, L(r−2)>3, while

\[
3r(196r^2+59)-288(2r-1)(r-1)^2
=3(4r^3+480r^2-325r+96)>0.
\]

Consequently \(\gamma_r/\beta_r<3\), and on the proposed positive interval

\[
\partial_x F_r=(\beta_r-\gamma_r/y)/x^2>0,
\qquad \partial_y F_r=-\gamma_r/(xy^2)<0.
\]

The two initial exact ratios are

\[
R_9=\frac{352460311743}{12687888953},\qquad
R_{10}=\frac{3345302764586}{117486770581}.
\]

Both lie strictly between their stated L and U bounds, checked using independently enumerated integer collision coefficients.

Assume the interval holds at r−1 and r−2. The stated derivative signs reduce the induction to

\[
F_r(L(r-1),U(r-2))-L(r)>0,
\]

\[
U(r)-F_r(U(r-1),L(r-2))>0.
\]

For each rational expression, cancel common factors, substitute r=z+11 and expand both numerator and denominator as integer polynomials in z. The exact symbolic computation verifies that **every coefficient is strictly positive**. The two reduced numerators have degree 13, and the two denominators have degree 17. The complete coefficient extraction and all assertions are in the separately published Python reproducer; it emits a JSON certificate including every integer polynomial coefficient. For z≥0 the strict rational inequalities follow. Induction proves the lemma for all r≥9. ∎

## 5. New positivity certificate for all large lengths

Set a=R_{m+1} and b=R_{m+2}. Dividing the exact three-shift formula by positive A(m+3) yields

\[
D_m(a,b)=\frac{\Delta^+_{m+4}}{A(m+3)}
=\frac{c_1(m)/a+c_2(m)}{b}+c_3(m).
\]

**Lemma 3.** For every real m≥10,

\[
\frac{c_1(m)}{L(m+1)}+c_2(m)>0,
\qquad
\boxed{\frac{c_1(m)/L(m+1)+c_2(m)}{U(m+2)}+c_3(m)>0.}
\]

**Exact sign certificate.** Reduce each expression to its numerator/denominator as rational polynomials, substitute m=z+10, and expand in nonnegative powers of z. Every coefficient of each resulting numerator and denominator is **strictly positive**. Their degree pairs are (7,6) and (9,10). The reproducer evaluates the full four coefficient arrays, checks their signs with exact symbolic integers, and writes those arrays to the JSON certificate.

Since c_1(m)<0, D_m(a,b) increases with a. The first strict inequality ensures D_m decreases with b on the bounded region. Hence by Lemma 2

\[
D_m(R_{m+1},R_{m+2})
\ge D_m(L(m+1),U(m+2))>0\quad(m\ge10).
\]

Thus Δ⁺_n>0 for all n≥14. ∎

## 6. The only nine remaining finite cases

Compute A_d(r) independently with the exact multinomial-splitting identity

\[
A_1(r)=1,\qquad A_d(r)=\sum_{k=0}^r \binom rk^2 A_{d-1}(r-k).
\]

The unchanged PREFIX-1016 three-shift formula gives the exact contrast integers:

| n | Δ⁺_n |
|---:|---:|
| 5 | 25,620 |
| 6 | 386,028 |
| 7 | 7,124,592 |
| 8 | 149,251,656 |
| 9 | 3,398,043,852 |
| 10 | 81,969,197,100 |
| 11 | 2,063,490,736,128 |
| 12 | 53,703,289,713,528 |
| 13 | 1,436,011,181,064,216 |

All nine are positive. Combining them with Lemma 3 completes the theorem for **every integer n≥5**. QED.

## 7. Executed scope, exact evidence, contribution and continuation

Executable: [PREFIX1018_R6_GLOBAL_POSITIVE_PORT_CERT.py](https://github.com/awdawmip/enterprise-math/blob/d7ba86ad707381a128184876e3fb208d416c6a96/research_notes/portable_direct/PREFIX1018_R6_GLOBAL_POSITIVE_PORT_CERT.py).

The reproducibility program (Python 3 and SymPy) verifies the seven-state differential annihilator, extracts all four recurrence polynomials, checks independent integer collision coefficients and the ratio seeds, proves the two ratio-interval invariants and two contrast inequalities by coefficientwise positive symbolic polynomials, computes the nine finite differences, and generates the full JSON coefficient certificate. Its executed local version passed all checks. No floating point enters the mathematical proof.

This new author-side computer-assisted exact proof upgrades PREFIX-1017's eventual strict sign and finite 300-term checks to an **all-integer-length theorem**. The order-three collision recurrence and rational ratio enclosure are independently reusable mathematical outputs.

Next open question: characterize a smallest future-operation-safe signed Gram/Cell–port state preserving the same terminal asymmetry under a second BRC update or for combined negative-step grades. An observer-specific final square compression has not established an arbitrary-future-state equivalence.

The mother question B_fix,odd(32)∈{19,20} remains OPEN. Frozen P000 and the Stage46 candidate are unchanged. Review remains NOT_REVIEWED. Historical author provenance: EM-DIRECT-FBEA5D; Activity RA-3FB2D033BE6048D8712FF056; original SID MCP-45ad6d29cd534c1aad25595a72e3c532. GitHub publication does not itself authorize a new Task CLAIM, PROGRESS, independent review or Activity mutation.
