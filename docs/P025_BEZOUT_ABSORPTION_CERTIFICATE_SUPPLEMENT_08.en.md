# P025 Supplement 08 — Constructive Bezout Certificates for the Absorption Floor

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-abc-support-collapse`  
Depends on: P025 Supplements 04–07  
Hard block: `NONE`

## 1. Question

Supplements 04–07 separate the exact arithmetic floor

\[
\eta_{\min}
\]

from the minimum lattice radius

\[
\nu
\]

needed to attain that floor.

The next question is deliberately constructive:

> Can one produce an absorption-optimal witness by finite exact integer arithmetic, without searching an expanding witness ball?

The answer is yes. The construction is elementary Bezout/syzygy algebra. The more important negative result is that the resulting explicit witness can be very far from norm-optimal.

## 2. Pair syzygies

Let

\[
\alpha=\widehat\alpha\in\mathbb Z^s
\]

be the primitive additive normal and

\[
\beta=\beta_{\rm raw}\in\mathbb Z^s
\]

the canonically scaled Wronskian row.

For `i<j`, define the pair syzygy

\[
\boxed{
 t_{ij}=\alpha_j e_i-\alpha_i e_j.
}
\]

Then

\[
\alpha\cdot t_{ij}=0,
\]

so every `t_ij` belongs to the additive witness lattice

\[
T=\ker_{\mathbb Z}\alpha.
\]

Define the signed minor

\[
\boxed{
m_{ij}=\alpha_i\beta_j-\alpha_j\beta_i.}
\]

Then

\[
\boxed{
\beta\cdot t_{ij}=-m_{ij}.
}
\]

These are the same Pluecker/minor coordinates whose gcd appeared in Supplement 04.

## 3. P025-T23 — Bezout floor certificate

Let the nonzero minors be

\[
m_1,\ldots,m_N,
\]

with corresponding pair syzygies

\[
t_1,\ldots,t_N.
\]

Let

\[
d=\gcd(m_1,\ldots,m_N)>0.
\]

Choose ordinary integer Bezout coefficients `z_i` such that

\[
\sum_{i=1}^N z_i m_i=d.
\]

Define

\[
\boxed{
x_B=-\sum_{i=1}^N z_i t_i.}
\]

Then

\[
\boxed{
\alpha\cdot x_B=0,
\qquad
\beta\cdot x_B=d.
}
\]

Therefore `x_B` is a non-degenerate additive witness attaining the positive generator of the Wronskian image, and hence

\[
\boxed{
\eta(x_B)=\eta_{\min}.
}
\]

### Proof

Every `t_i` lies in `ker(alpha)`, so their integer linear combination `x_B` does as well. Moreover,

\[
\beta\cdot x_B
=-\sum_i z_i(\beta\cdot t_i)
=\sum_i z_i m_i
=d.
\]

Supplement 04 identifies `d` as the positive generator of `beta(T)`, so `d=M eta_min`. Therefore the constructed witness attains the exact absorption floor. ∎

### Scope discipline

Bezout identities, syzygy generation and gcds of minors are standard integer algebra. P025 makes no priority claim for the construction itself.

The project-side value is that the exact certificate can be generated from the compact rows `alpha,beta`, making absorption optimality finitely checkable without an unbounded search.

## 4. P025-T24 — explicit radius upper bound

The same construction gives

\[
\|t_{ij}\|_\infty
=\max(|\alpha_i|,|\alpha_j|).
\]

Hence

\[
\boxed{
\nu
\le
\|x_B\|_\infty
\le
\sum_i |z_i|\,
\max(|\alpha_{p_i}|,|\alpha_{q_i}|).
}
\]

So any explicit Bezout identity among the nonzero minors supplies a fully integer upper bound for the absorption-access radius.

This bound is constructive but is not generally sharp.

## 5. Exact examples where the simple construction is sharp

### `2+3=5`

With prime coordinates `(2,3,5)`,

\[
\alpha=(1,1,-1),
\qquad
\beta=(-3,2,0).
\]

The signed nonzero minors are

\[
(5,-3,2),
\]

whose gcd is one. A Bezout identity gives an absorption-optimal witness of radius `2`. This equals the exact value

\[
\nu=2.
\]

### `2+7=9`

With coordinates `(2,3,7)`,

\[
\alpha=(1,-6,1),
\qquad
\beta=(-7,0,2).
\]

The minors are

\[
(-42,9,-12),
\]

with gcd `3`. One explicit identity is

\[
(-42)+5\cdot9=3.
\]

The resulting certificate is

\[
\boxed{x_B=(1,1,5)}
\]

with

\[
\|x_B\|_\infty=5,
\qquad
\eta(x_B)=1.
\]

Supplement 07 established

\[
\nu=5,
\]

so this Bezout construction is norm-optimal in this example.

## 6. P025-N06 — constructive existence can be extremely far from minimum precision

Consider again

\[
1+242=243.
\]

The exact rows on coordinates `(2,3,11)` are

\[
\alpha=(121,-405,44),
\qquad
\beta=(121,0,44).
\]

The nonzero minors are

\[
49005,
\qquad
-17820,
\]

and

\[
\gcd(49005,17820)=4455.
\]

A simple extended-Euclidean identity is

\[
-49005+3\cdot17820=4455.
\]

The corresponding canonical implementation produces

\[
\boxed{
x_B=(-405,11,1215)}
\]

with

\[
\eta(x_B)=5
\]

but

\[
\boxed{\|x_B\|_\infty=1215.}
\]

An independent exact bounded search finds a floor-attaining witness already at

\[
\boxed{\nu=27.}
\]

For example one such witness is

\[
(-27,-11,-27),
\]

up to sign/convention.

Thus this valid constructive floor witness has absolute radius overhead

\[
\boxed{1215-27=1188.}
\]

### Architectural consequence

A proof that a certificate exists below some explicit radius does **not** identify the minimal precision required to access the certificate.

This is the same distinction that appears elsewhere in Enterprise Math between:

- a valid sufficient refinement/certificate; and
- the coarsest/minimal task-relative refinement.

Here the gap is not philosophical: it is an exact integer quantity larger than forty times the optimum in this small example.

## 7. Why the gap appears

The gcd identity lives in **minor space**. Mapping a Bezout coefficient vector back through pair syzygies into the witness lattice can create large coordinate cancellation/amplification.

Therefore minimizing

\[
\left|\sum z_i m_i\right|=d
\]

is not the same optimization problem as minimizing

\[
\left\|\sum z_i t_i\right\|_\infty.
\]

The first is an arithmetic ideal-generation problem; the second is a normed lattice/coset optimization problem.

This gives a sharper decomposition than Supplement 07:

\[
\boxed{
\text{image generator known}
\not\Rightarrow
\text{minimum-radius generator preimage known}.
}
\]

## 8. Next mathematical form of `nu`

Fix

\[
d=\operatorname{cont}(\alpha\wedge\beta).
\]

Then the absorption-optimal witness set is exactly the affine integer slice

\[
\boxed{
\mathcal A_d
=
\{x\in\mathbb Z^s:
\alpha\cdot x=0,
\ \beta\cdot x=\pm d\}.
}
\]

Therefore

\[
\boxed{
\nu
=
\min_{x\in\mathcal A_d}
\|x\|_\infty.
}
\]

So after Supplements 04–06 have removed the arithmetic uncertainty in `d`, the remaining problem is a concrete closest-vector / affine-lattice minimum problem in a codimension-two integer system.

That reduction uses standard lattice optimization language. The project research question is whether the special abc row structure makes this affine minimum substantially more explicit than generic CVP-style machinery.

## 9. Executable assets

Added:

- `src/enterprise_math/abc_absorption_bezout.py`
  - exact multi-integer extended gcd coefficients;
  - pair syzygies;
  - nonzero Wronskian minors;
  - constructive floor-attaining witness;
  - triangle radius bound;
  - explicit comparison with an independently established optimal radius.
- `tests/test_abc_absorption_bezout.py`
  - exact reconstruction of the gcd identity;
  - sharp constructions for `2+3=5` and `2+7=9`;
  - the `1215` versus `27` non-optimality boundary for `1+242=243`;
  - rank-one calibration.

## 10. Prior-art boundary

The following are established mathematics and not P025 novelty:

- extended Euclidean / Bezout algorithms;
- syzygies of one integer row;
- determinantal divisors;
- affine lattice closest-vector/minimum-norm problems;
- Geometry-of-Numbers methods for short vectors, including Pasten's arithmetic-derivative application. citeturn379997academia11

The exact use of the floor image generator, the access radius `nu`, and the quantified existence-versus-minimum-precision gap remain `NOVELTY_UNVERIFIED` as an Enterprise Math synthesis.

## 11. Next frontier

There is no hard block. Continue with:

1. solve the affine minimum for all rank-two witness lattices (`omega(abc)=3`) as explicitly as possible;
2. derive a two-variable modular/Bezout normal form for `nu` that avoids cubic brute-force enumeration;
3. compare this exact optimum with Pasten/Minkowski norm bounds;
4. classify when the direct Bezout-minor certificate is already norm-optimal;
5. search for families with unbounded constructive-over-optimal radius ratio;
6. only after that determine whether `nu` or `delta_abs` yields useful independent control in abc-quality arguments.
