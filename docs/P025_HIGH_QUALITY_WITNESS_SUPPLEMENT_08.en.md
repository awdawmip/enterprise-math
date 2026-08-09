# P025 Supplement 08 — Exact Witness Precision for a High-Quality ABC State

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-high-quality-witness-exact`  
Parent dependency: `program/p025-degeneracy-overhead@32756663`  
Prior-art status: arithmetic derivatives / restricted minima / lattice reduction are prior art; the exact finite instance certificate is a P025 result

## 1. Goal

The previous supplements separated four finite quantities:

\[
\lambda_{abc}
\le
\max(\lambda_{abc},\rho)
\le
\mu
\le
U_2,
\]

where `lambda_abc` is an arithmetic-demand floor, `rho` is the ordinary additive-lattice first radius, `mu` is the first non-degenerate witness radius, and `U_2` is a simple two-coordinate generator ceiling.

Small examples prove these layers can differ. The next pressure test should use a genuinely high-quality `abc` state rather than another tiny triple.

This supplement studies the exact identity

\[
\boxed{
2+3^{10}\cdot109=23^5.
}
\]

Put

\[
a=2,
\qquad
b=3^{10}\cdot109=6{,}436{,}341,
\qquad
c=23^5=6{,}436{,}343.
\]

Its radical is

\[
\operatorname{rad}(abc)=2\cdot3\cdot23\cdot109=15{,}042.
\]

Direct integer comparison gives

\[
c^2=41{,}426{,}511{,}213{,}649
>
3{,}403{,}429{,}454{,}088
=\operatorname{rad}(abc)^3.
\]

Thus this state satisfies the P025 rational high-quality predicate for exponent `3/2`.

The main result is

\[
\boxed{
\mu(a,b,c)=601.
}
\]

The proof is an exact finite lattice certificate; no floating point, logarithm, or unbounded search is used.

## 2. Exact arithmetic-demand floor

The prime-power data are

\[
\begin{array}{c|ccc}
n&\operatorname{rad}(n)&m(n)&\widehat A(n)\\
\hline
2&2&1&1\\
3^{10}\cdot109&327&19{,}683&1{,}093\\
23^5&23&279{,}841&5
\end{array}
\]

with

\[
\widehat A(n)=
\sum_{p\mid n}\frac{\operatorname{rad}(n)}p v_p(n).
\]

Supplement 06 gives the normalized complementary capacities

\[
\begin{aligned}
K_{b,c}&=26{,}774,\\
K_{a,c}&=33,\\
K_{a,b}&=2{,}513.
\end{aligned}
\]

Hence the three target demand floors are

\[
\lambda_a=1,
\qquad
\lambda_b=\left\lceil\frac{19{,}683}{33}\right\rceil=597,
\qquad
\lambda_c=\left\lceil\frac{279{,}841}{2{,}513}\right\rceil=112.
\]

Therefore

\[
\boxed{\lambda_{abc}=597.}
\]

Before any lattice reduction, the simple two-coordinate construction of Supplement 06 gives only

\[
\boxed{U_2=59{,}049,}
\]

so the initial certified interval is

\[
597\le\mu\le59{,}049.
\]

The rest of this supplement closes almost all of that gap exactly.

## 3. Prime-coordinate generator rows

Use the ordered prime coordinates

\[
(2,3,23,109).
\]

For a relation-adapted arithmetic derivative, the additivity condition

\[
d^\psi(a)+d^\psi(b)=d^\psi(c)
\]

has primitive integer normal

\[
\boxed{
\alpha=
(1,\ 21{,}454{,}470,\ -1{,}399{,}205,\ 59{,}049).
}
\]

Indeed,

\[
\begin{aligned}
d^\psi(2)&=x_2,\\
d^\psi(3^{10}\cdot109)
&=21{,}454{,}470x_3+59{,}049x_{109},\\
d^\psi(23^5)&=1{,}399{,}205x_{23}.
\end{aligned}
\]

For the Wronskian orientation `(a,b)`, the primitive degeneracy row is

\[
\boxed{
\beta=(-327,\ 2180,\ 0,\ 6).
}
\]

Thus

\[
T=\ker_{\mathbb Z}(\alpha),
\qquad
T^\circ=T\cap\ker_{\mathbb Z}(\beta),
\]

and `mu` is exactly the restricted first `L_infinity` minimum of `T` outside `T^circ`. Restricted successive minima are established Geometry-of-Numbers prior art [SRC-HENK-THIEL-2014-RESTRICTED-MINIMA].

## 4. An exact unimodular basis of the additive lattice

Because the first coordinate of `alpha` is `1`, an obvious integer basis of `T` is

\[
\begin{aligned}
e_1&=(-21{,}454{,}470,1,0,0),\\
e_2&=(1{,}399{,}205,0,1,0),\\
e_3&=(-59{,}049,0,0,1).
\end{aligned}
\]

Apply the integer matrix

\[
U=
\begin{pmatrix}
3&46&0\\
0&23&545\\
-20&-310&-79
\end{pmatrix}.
\]

Its determinant is

\[
\boxed{\det U=-1,}
\]

so this is a unimodular change of basis, not a finite-index approximation.

The resulting exact basis is

\[
\begin{aligned}
v_1&=(20,3,46,0),\\
v_2&=(10,0,23,545),\\
v_3&=(721,-20,-310,-79).
\end{aligned}
\]

Therefore every `x in T` has a unique representation

\[
\boxed{x=Av_1+Bv_2+Cv_3,\qquad A,B,C\in\mathbb Z.}
\]

The degeneracy row becomes particularly simple:

\[
\boxed{
\beta(v_1)=0,
\qquad
\beta(v_2)=0,
\qquad
\beta(v_3)=-279{,}841=-23^4.
}
\]

Hence

\[
\boxed{x\notin T^\circ\iff C\ne0.}
\]

This isolates the non-degeneracy condition into one exact integer coordinate.

## 5. P025-T24 — no non-degenerate witness has radius at most 600

Assume for contradiction that

\[
x=Av_1+Bv_2+Cv_3\notin T^\circ
\]

satisfies

\[
\|x\|_\infty\le600.
\]

Since `C neq 0`, the beta equation gives

\[
279{,}841|C|
=|\beta(x)|.
\]

The `L_1` norm of the primitive beta row is

\[
327+2180+6=2513.
\]

Therefore

\[
279{,}841|C|
\le2513\cdot600
=1{,}507{,}800.
\]

But

\[
6\cdot279{,}841
=1{,}679{,}046
>1{,}507{,}800,
\]

so

\[
\boxed{1\le|C|\le5.}
\]

By replacing `x` by `-x`, which preserves the radius and non-degeneracy, assume

\[
1\le C\le5.
\]

### The fourth coordinate forces `B in {0,1}`

From the basis formula,

\[
x_{109}=545B-79C.
\]

Thus

\[
|545B-79C|\le600.
\]

For `1<=C<=5`,

\[
\frac{-600+79C}{545}>-1
\]

and

\[
\frac{600+79C}{545}
\le\frac{995}{545}<2.
\]

Since `B` is integral,

\[
\boxed{B\in\{0,1\}.}
\]

### The remaining ten cases have incompatible `A` intervals

The first and third coordinates are

\[
\begin{aligned}
x_2&=20A+10B+721C,\\
x_{23}&=46A+23B-310C.
\end{aligned}
\]

The radius bound gives

\[
A
\le
\left\lfloor
\frac{600-10B-721C}{20}
\right\rfloor
\]

from `x_2<=600`, while `x_23>=-600` gives

\[
A
\ge
\left\lceil
\frac{-600-23B+310C}{46}
\right\rceil.
\]

For the only possible values `C=1,...,5`, `B=0,1`, the exact bounds are

\[
\begin{array}{c|c|c|c}
C&B&A_{\min}\text{ from }x_{23}&A_{\max}\text{ from }x_2\\
\hline
1&0&-6&-7\\
1&1&-6&-7\\
2&0&1&-43\\
2&1&0&-43\\
3&0&8&-79\\
3&1&7&-79\\
4&0&14&-115\\
4&1&14&-115\\
5&0&21&-151\\
5&1&21&-151
\end{array}
\]

Every row has

\[
A_{\min}>A_{\max}.
\]

Thus no such integer `A` exists. This proves

\[
\boxed{\mu\ge601.}
\]

The argument is a complete finite certificate, not evidence from a search range.

## 6. P025-T25 — an explicit radius-601 non-degenerate witness

Take

\[
(A,B,C)=(6,0,-1).
\]

Then

\[
x=6v_1-v_3
=
\boxed{(-601,\ 38,\ 586,\ 79)}.
\]

Its radius is

\[
\|x\|_\infty=601.
\]

By construction `alpha*x=0`, and directly

\[
\beta(x)=279{,}841\ne0.
\]

Therefore it is a valid non-degenerate relation-adapted witness, so

\[
\boxed{\mu\le601.}
\]

Combining with P025-T24:

\[
\boxed{\mu=601.}
\]

## 7. P025-T26 — the high-quality witness profile is nearly demand-saturated

We already proved

\[
\lambda_{abc}=597.
\]

The additive lattice contains `v_1=(20,3,46,0)`, so

\[
\rho\le46<597.
\]

Hence without even solving the unrestricted shortest-vector problem exactly,

\[
\max(\lambda_{abc},\rho)=597.
\]

Together with `mu=601`:

\[
\boxed{
\mu-\max(\lambda_{abc},\rho)=4.
}
\]

Thus for this high-quality state, arithmetic multiplicity demand explains almost all of the exact certificate precision. The independent relation/degeneracy layer contributes only four additional `L_infinity` units beyond the strongest certified lower floor.

This sharply contrasts with the tiny state `1+53=54`, where the independent non-degeneracy overhead is `18`.

At the same time, the elementary two-coordinate ceiling remains extremely loose:

\[
U_2=59{,}049.
\]

So compact local generator minors are enough to prove finiteness but can be far from the true restricted minimum in a four-coordinate state. Full lattice relations can be dramatically stronger than the cheapest coordinate-pair certificate.

## 8. What was gained relative to the earlier architecture

This example closes a complete chain on a genuinely high-quality integer state:

\[
\boxed{
\text{radical/residual state}
\to
\text{arithmetic demand }597
\to
\text{relation/degeneracy flag}
\to
\text{exact restricted witness }601.
}
\]

The result has three useful implications.

First, the P025 witness precision is now connected to an actual hard `abc`-quality sample by an exact value, not only by bounded toy examples.

Second, the certificate sandwich can be quantitatively diagnostic: here the arithmetic lower certificate is nearly tight while the naive sparse upper certificate is not.

Third, the precise source of the remaining uncertainty can be isolated. The additive lattice already has small states; the four-unit difference is a genuine certificate restriction above the demand floor, whereas most of the earlier `U_2` gap is merely construction inefficiency.

## 9. Prior-art and novelty boundary

Pasten's arithmetic derivative/witness framework is prior art [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES]. The interpretation of `mu` as a shortest lattice point avoiding `T^circ` is a restricted-successive-minimum specialization and therefore belongs to the Henk--Thiel / Geometry-of-Numbers prior-art neighborhood [SRC-HENK-THIEL-2014-RESTRICTED-MINIMA]. Unimodular lattice basis changes and lattice reduction are also established mathematics.

P025 does not claim those methods as new.

The project-side mathematical payload is the explicit exact certificate for this fixed `abc` state and its integration with the previously proved P025 quantities `lambda_abc`, `rho`, and `U_2`. Historical priority of the value `601` for this particular arithmetic-derivative witness problem has not been audited; it should therefore be treated as a project instance result, not a historical-first claim.

## 10. Executable assets

This generation adds

- `src/enterprise_math/abc_high_quality_witness.py`;
- `tests/test_abc_high_quality_witness.py`.

The executable certificate checks:

- the exact high-quality inequality;
- generator rows `alpha,beta`;
- the canonical and reduced lattice bases;
- unimodularity `det U=-1`;
- diagonalization of the degeneracy functional on the reduced basis;
- the complete ten-row radius-600 obstruction table;
- the explicit radius-601 witness;
- `lambda_abc=597`, additive radius certificate `<=46`, and `U_2=59049`.

No exhaustive search to radius 601 is needed by the proof.

## 11. Next frontier

The exact value `mu=601` creates a much more focused next problem:

1. explain the four-unit gap `mu-lambda_abc=4` directly from the quotient/flag geometry, rather than from a one-off reduced basis;
2. test other high-quality or exceptional triples to see whether `mu/lambda_abc` tends to be near one or can be large;
3. compare Henk--Thiel general restricted-minimum bounds with P025's arithmetic-specific lower floor and exact reduced-basis certificates;
4. search for a theorem that predicts when the arithmetic floor is within `O(1)` of the restricted minimum, but aggressively seek counterexamples before formulating any asymptotic conjecture;
5. keep the result as a pressure test, not as evidence that the abc conjecture has been proved.
