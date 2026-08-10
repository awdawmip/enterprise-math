# P025 Supplement 61 — Paired Residual Pressure and the Two-Square Tail

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-paired-square-tail-stage61`  
Base: frozen Stage-60 semantic head `ff04a826c5ea87c28f769cb378d8189687e686b0`  
Depends on: P025 Supplements 47, 50  
Hard block: `NONE`

## 1. Stage 50 discarded usable additive information

Stage 50 starts from a failed cyclic Projective Capacity Condition term

\[
\frac{m(n_i)}{K_{jk}}\ge c^\eta
\]

and keeps only `K_jk>=1`, obtaining one large multiplicity residual.

For a non-unit primitive relation

\[
a+b=c,\qquad a,b>1,
\]

the additive geometry forces more: the denominator contains a radical of a *different* component, and that radical cancels against the residual of a large complementary component.

The result is a two-component pressure theorem.

## 2. P025-T126 — every non-unit PCC failure forces a large residual pair

Fix rational

\[
\eta=p/q,\qquad 0<p<q.
\]

Assume `PCC_eta` fails.

The three cyclic projective ratios are

\[
\rho_c=\frac{m(c)}{K_{ab}},\qquad
\rho_b=\frac{m(b)}{K_{ac}},\qquad
\rho_a=\frac{m(a)}{K_{bc}}.
\]

At least one is at least `c^eta`.

### Case 1: the `c`-oriented term fails

Let `j` be the larger of `a,b`, so

\[
j\ge c/2.
\]

Because both complementary blocks are non-unit,

\[
K_{ab}=R_b C(a)+R_a C(b)\ge R_j,
\]

where `R_j=rad(j)` and every non-unit block capacity is at least one.

Thus

\[
m(c)\ge c^\eta R_j.
\]

Also

\[
m(j)=\frac{j}{R_j}\ge\frac{c}{2R_j}.
\]

Multiplication cancels the complementary radical:

\[
\boxed{
m(c)m(j)\ge\frac12c^{1+\eta}.
}
\]

### Case 2: the `a`- or `b`-oriented term fails

If, for example, `rho_a>=c^eta`, then

\[
K_{bc}\ge R_c,
\]

so

\[
m(a)\ge c^\eta R_c.
\]

Since `m(c)=c/R_c`,

\[
\boxed{
m(a)m(c)\ge c^{1+\eta}.
}
\]

The `b` case is identical.

Therefore in every non-unit PCC failure there are distinct components `x,y` with

\[
\boxed{
m(x)m(y)\ge\frac12c^{1+\eta}.
}
\]

This is strictly stronger than Stage 50's one-component conclusion.

## 3. P025-T127 — two large square-divisor roots

Let

\[
q_2(n)=\prod_p p^{\lfloor v_p(n)/2\rfloor}.
\]

Stage 50 proves

\[
q_2(n)^2\ge m(n).
\]

Hence the pair from P025-T126 satisfies

\[
(q_2(x)q_2(y))^2
\ge
m(x)m(y)
\ge
\frac12c^{1+\eta}.
\]

Thus

\[
\boxed{
q_2(x)q_2(y)
\ge
\frac1{\sqrt2}c^{(1+\eta)/2}.
}
\]

The projective failure is therefore supported by two square-divisor directions, not merely one large square divisor.

## 4. P025-T128 — elementary dyadic two-square tail

Restrict to

\[
X/2<c\le X.
\]

For `eta=p/q`, define `Y=Y_{p/q}(X)` as the least positive integer satisfying

\[
\boxed{
2^{2q+p}Y^{2q}\ge X^{q+p}.
}
\]

Then every non-unit PCC failure has two component square-divisor roots `s,t` with

\[
st\ge Y.
\]

There are three unordered component pairs. For one fixed labelled pair and fixed `s,t`, the number of possible component values is at most

\[
\left\lfloor\frac X{s^2}\right\rfloor
\left\lfloor\frac X{t^2}\right\rfloor.
\]

The additive relation can only reduce this count. Hence

\[
N^{\rm nonunit}_{\rm fail}(X)
\le
3\sum_{\substack{s,t\le\sqrt X\\st\ge Y}}
\left\lfloor\frac X{s^2}\right\rfloor
\left\lfloor\frac X{t^2}\right\rfloor.
\]

Now

\[
\sum_{st\ge Y}\frac1{s^2t^2}
\ll
\frac{\log(2Y)}Y.
\]

Since

\[
Y\asymp_\eta X^{(1+\eta)/2},
\]

we obtain

\[
\boxed{
N^{\rm nonunit}_{\rm fail}(X/2<c\le X)
=
O_\eta\!\left(
X^{3/2-\eta/2}\log X
\right).
}
\]

For the unit slice, Stage 50's one-component square-divisor argument has no free second additive coordinate, so its contribution is only

\[
O_\eta(X^{1-\eta/2}),
\]

and is smaller. Dyadic summation preserves the leading power. Therefore the complete elementary PCC-failure bound is

\[
\boxed{
N_{\rm fail}(c\le X)
=
O_\eta\!\left(
X^{3/2-\eta/2}\log X
\right).
}
\]

This improves the internal Stage-50 exponent `2-eta/2` by a full factor `X^(1/2)` up to logarithms.

## 5. Exact small calibration: `3+125=128`

At exponent

\[
\eta=1/10,
\]

the c-oriented projective ratio equals

\[
\rho_c=32/7>128^{1/10}.
\]

The paired residual witness is

\[
m(128)=64,\qquad m(125)=25,
\]

so

\[
m(128)m(125)=1600.
\]

The largest square-divisor roots are

\[
q_2(128)=8,\qquad q_2(125)=5,
\]

and their product is exactly `40`.

This is a compact exact regression fixture for the paired mechanism.

## 6. What this result does and does not mean

P025-T126–T128 are elementary consequences of the explicit PCC state and the additive relation. They do not prove pointwise PCC and do not prove abc.

More importantly, they should not be advertised as competitive abc exceptional-set theory. Classical radical-counting estimates already give much stronger bounds for ordinary abc/Oesterle exceptional sets. Stage 62 audits that prior-art boundary explicitly.

The project-side value is architectural: preserving the cyclic denominator instead of immediately erasing it exposes a *paired* hidden-information certificate and changes the finite exceptional-incidence exponent.

## 7. Executable assets

Added:

- `src/enterprise_math/abc_projective_paired_square_tail.py`;
- `tests/test_abc_projective_paired_square_tail.py`.

The implementation contains only integer/rational tests and an explicit finite dyadic two-square union envelope.

## 8. Next frontier

No hard block exists. Continue with:

1. compare P025-T128 with de Bruijn radical counting and classify it as `ADOPT / WEAK / COMPARABLE` rather than making a novelty claim;
2. compress the paired residual statement into a pair-radical product state;
3. determine whether that pair state gives a sharper unconditional PCC-specific count when de Bruijn is imported;
4. update the Stage-60 almost-all benchmark only as an internal architecture comparison, not as competitive analytic number theory.
