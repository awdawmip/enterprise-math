# P025 Supplement 50 — Unconditional Sparse-Failure Layer for the Projective Capacity Condition

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-certificate-index-stage34`  
Depends on: P025 Supplements 47, 49  
Hard block: `NONE`

## 1. Pointwise PCC remains conjectural, but its failure already has a rigid shape

For a primitive triple

\[
a+b=c,
\qquad
\gcd(a,b)=1,
\]

Supplement 47 defines

\[
\sigma_{\rm proj}
=
\max\left\{
\frac{c}{R(S(a)+S(b))},
\frac{b}{R(S(a)+S(c))},
\frac{a}{R(S(b)+S(c))}
\right\},
\]

where

\[
R=\operatorname{rad}(abc),
\qquad
S(n)=\sum_{p\mid n}\frac{v_p(n)}p.
\]

Using the equivalent residual/capacity form, each cyclic term is

\[
\frac{m(n_i)}{K_{jk}},
\]

with positive integer denominator

\[
K_{jk}\ge1.
\]

Fix a rational exponent

\[
\eta=p/q,
\qquad
0<p<q.
\]

Suppose PCC fails:

\[
\boxed{
\sigma_{\rm proj}\ge c^{p/q}.
}
\]

Then one cyclic term fails, so for some component

\[
n\in\{a,b,c\}
\]

we have

\[
\frac{m(n)}{K}\ge c^{p/q}.
\]

Since `K>=1`, necessarily

\[
\boxed{
m(n)\ge c^{p/q}.}
\]

Thus every PCC failure forces a large multiplicity residual in at least one of the three additive components.

## 2. P025-T115 — a large residual forces a large square divisor

Write

\[
n=\prod_p p^{e_p}
\]

and define

\[
\boxed{
q_2(n)=\prod_p p^{\lfloor e_p/2\rfloor}.
}
\]

Then

\[
q_2(n)^2
\]

is the largest square divisor of `n`.

Also

\[
m(n)
=
\prod_{e_p>0}p^{e_p-1}.
\]

For every exponent `e>=1`,

\[
2\lfloor e/2\rfloor
\ge
 e-1.
\]

Hence termwise

\[
\boxed{
q_2(n)^2\ge m(n).
}
\]

Combining with PCC failure gives

\[
\boxed{
q_2(n)^2
\ge
c^{p/q}.
}
\]

Equivalently,

\[
\boxed{
q_2(n)
\ge
c^{p/(2q)}.
}
\]

So every projective-capacity failure contains a component with a macroscopically large square divisor.

## 3. P025-T116 — dyadic component count has a power saving

Fix

\[
X/2<c\le X.
\]

A PCC failure forces some component `n<=X` divisible by a square

\[
s^2
\]

with

\[
s^{2q}
\ge
(X/2)^p.
\]

Let `s_0` be the smallest positive integer satisfying

\[
2^p s_0^{2q}\ge X^p.
\]

The number of integers `n<=X` divisible by at least one such square is bounded by the elementary union bound

\[
\boxed{
U_{p/q}(X)
\le
\sum_{s=s_0}^{\lfloor\sqrt X\rfloor}
\left\lfloor\frac X{s^2}\right\rfloor.
}
\]

Since

\[
\sum_{s\ge s_0}\frac1{s^2}
\ll
\frac1{s_0},
\]

and

\[
s_0\asymp_{p/q}X^{p/(2q)},
\]

we obtain

\[
\boxed{
U_{p/q}(X)
=O_{p/q}\left(X^{1-p/(2q)}\right).
}
\]

This is an unconditional power saving over the `O(X)` ambient set of possible component values.

## 4. P025-T117 — dyadic PCC-failure triples are power-saving sparse

Once a failing component `n` is fixed, there are at most `O(X)` choices for the remaining additive coordinate under

\[
a+b=c\le X.
\]

There are three possible component positions: `a`, `b`, or `c`. Therefore

\[
\boxed{
N_{\rm fail}(X/2<c\le X)
=O_{p/q}\left(X^{2-p/(2q)}\right).
}
\]

The total number of positive additive triples with `c<=X` is `Theta(X^2)`. Thus the relative incidence of PCC failures on a dyadic scale satisfies a power saving

\[
\boxed{
\frac{N_{\rm fail}}{X^2}
=O_{p/q}\left(X^{-p/(2q)}\right).
}
\]

Restricting to primitive triples only decreases the count.

Summing over dyadic scales preserves the same power exponent, so the cumulative failure set through height `X` is also

\[
\boxed{
O_{p/q}\left(X^{2-p/(2q)}\right).
}
\]

## 5. Exact working failure: `1+239^2=2*13^4`

Consider

\[
1+57121=57122.
\]

Here

\[
57121=239^2,
\qquad
57122=2\cdot13^4.
\]

Supplement 49 gives

\[
\sigma_{\rm proj}
=\frac{2197}{2}.
\]

At exponent

\[
\eta=3/5,
\]

\[
\frac{2197}{2}
>57122^{3/5},
\]

so PCC fails.

The forced large component may be taken as

\[
n=57122,
\]

whose multiplicity residual is

\[
\boxed{m(n)=13^3=2197.}
\]

Its largest square divisor is

\[
\boxed{13^4=28561,}
\]

with square-root divisor

\[
q_2(n)=13^2=169.
\]

Indeed

\[
28561\ge2197.
\]

This is an exact finite witness for the sparse-failure mechanism.

## 6. A nonfailure calibration

For

\[
1+242=243
\]

one has

\[
\sigma_{\rm proj}=27/5.
\]

At exponent `1/3`, PCC holds. The executable failure extractor therefore returns no large-residual witness at that exponent.

This emphasizes that Stage 50 is an implication **from failure**, not a claim that every repeated-prime triple is exceptional.

## 7. Architectural significance: the missing sparse-exception layer is now theorem-backed

P023 currently distinguishes exact descent / legal repair from failure. Early P025 planning suggested an intermediate semantic layer in which failure is allowed but quantitatively sparse.

Stage 50 supplies a concrete unconditional model:

\[
\boxed{
\text{pointwise PCC remains open}
\quad\text{but}\quad
\text{PCC failures are power-saving sparse at every fixed exponent}.
}
\]

This is not derived from a conjectural exceptional-set theorem. It follows from explicit projective compression plus elementary square-divisor counting.

Thus P025 now has three genuinely different semantic levels:

1. **exact certificate/quotient structure** — Stages 34–40;
2. **pointwise projective condition** — Stage 47, conjectural globally;
3. **sparse-exception control** — Stage 50, unconditional.

That hierarchy is a strong candidate for A2/P023 backflow.

## 8. Relation to existing abc exceptional-set literature

Modern analytic number theory proves stronger and more delicate exceptional-set estimates for classical abc-quality failures. Those results are external prior art and remain registered in `sources_p025_abc.json`.

Stage 50 does not compete with them. Its point is architectural and elementary: once the projective witness route is compressed to an explicit weighted-radical observable, even a very crude square-divisor argument already produces a reusable power-saving sparse-failure theorem.

## 9. Executable assets

Added:

- `src/enterprise_math/abc_projective_sparse_failure.py`
  - largest-square-divisor root;
  - exact failure-to-large-residual witness;
  - finite dyadic square-divisor union bound.
- `tests/test_abc_projective_sparse_failure.py`
  - exact failure and nonfailure calibrations;
  - square-divisor domination;
  - finite power-saving density checks.

## 10. Prior-art / novelty discipline

Square-divisor counting and union bounds are elementary established mathematics. P025 claims no priority for them.

The project-side result is the specific implication chain

\[
\text{PCC failure}
\to
\text{large multiplicity residual}
\to
\text{large square divisor}
\to
\text{power-saving sparse failure},
\]

and its use as a concrete finite-precision semantic layer. Historical novelty of this packaging remains unverified.

## 11. Next frontier

No hard block exists. Continue with:

1. sharpen the exponent using higher-power divisibility rather than only squares;
2. separate unit and nonunit failure counting using Stages 48–49;
3. compare the elementary PCC exceptional set with modern abc exceptional-set theorems without claiming competition;
4. generalize `exact / pointwise conjectural / sparse-exception` into an A2/P023 semantic interface;
5. do not mistake sparse failure for pointwise proof.
