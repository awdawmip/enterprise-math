# PREFIX-686-R6 — The first integer sample parameter enters the BRC local crossing interval

Date: 2026-11-11 Asia/Shanghai. Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Author-side independent BRC observer computation (no Task CLAIM, independent review or theorem promotion).

Let `L=2663/50000=0.0532600`, `I=[L,0.0532610]`, and `F_q(z)=q A(z)-B(z)` with
`A(z)=Var(Y(z,z))-Var(Y(0,z))`, `B(z)=E[Y(z,z)]-E[Y(0,z)]`.

## New exact rational crossing-location theorem

PREFIX-685 certifies the full frozen-model moment enclosures at L:
```text
803334881118283114227/10^24 < A(L) < 803334881118283114228/10^24
7930886194096894324395803/10^24 < B(L) < 7930886194096894324395804/10^24 .
```
PREFIX-682 certifies on I: `-1800<A'(z)<-1600`, `100<B'(z)<150`.
PREFIX-684 established strict negativity of `F'_q(z)=q A'(z)-B'(z)` for all `q>=0` and its local-root classification.

For the **first eligible integer** `q=9873`, the certified unique root `z_9873` obeys
```text
L + 247/10^13 < z_9873 < L + 278/10^13.
```
Thus the crossing is only between 2.47e-11 and 2.78e-11 to the right of the interval entrance, with a certified position bracket width of `31/10^13 = 3.1e-12`. For `q=9872`, `F_q(L)<0` and no root lies in I.

## Proof

Let `a_l,a_u,b_l,b_u` denote the four outward rational endpoint bounds above.
For `q=9873`,
```text
f_l=q*a_l-b_u > 0,
f_u=q*a_u-b_l,
-(1800*q+150) < F'_q(z) < -(1600*q+100) < 0 .
```
As the unique root is inside I, the mean value theorem between L and the root implies
```text
f_l/(1800*q+150) < z_9873-L < f_u/(1600*q+100).
```
The accompanying standard-library Fraction checker verifies the two strict endpoint implications
`247/10^13 < f_l/(1800*q+150)` and
`f_u/(1600*q+100) < 278/10^13`, as well as `9872*a_u-b_l<0`.
All comparisons are exact rational cross-products.

**Validation:** `ALL_CHECKS_PASS PREFIX686-R6`, using the already published exact 189-row moment certificate from PREFIX-685; this is an implication check, not another recurrence replay.

**Research value:** a sharply localized discrete entry event provides an exact test for future crossover branch-tracing algorithms; the same approach can bound other integer q with one endpoint evaluation and a derivative strip.

**Next:** construct signed Bernstein patches on `0.052≤z≤0.054` and connect this local high-q branch to the actual q=12,24 variance comparison. Status `AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED`.
