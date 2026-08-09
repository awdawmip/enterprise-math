# P025 Supplement 13 — Three-Block Compression of the Absorption Floor

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-abc-support-collapse`  
Depends on: P025 Supplements 05–06  
Hard block: `NONE`

## 1. Motivation

Supplement 05 gave the exact cross-prime formula

\[
\eta_{\min}
=
\gcd_{\text{cross-block }p,q}
\frac{R e_p e_q}{g p q},
\]

where `R=rad(abc)`, `e_p=v_p(abc)`, and `g` is the content of the raw additive row.

This is already finite, but it still appears to require all prime-pair data. The present supplement proves that, for the future observable `eta_min`, all prime coordinates **inside each one of the three abc support blocks** collapse to one integer content.

Thus the entire absorption floor can be recovered from at most three block-pair integers.

## 2. P025-D04 — normalized block derivative content

For a positive integer `n>1`, write

\[
R_n=\operatorname{rad}(n),
\qquad
m_n=\frac n{R_n}.
\]

For a prime-coordinate arithmetic derivative,

\[
d_x(n)
=n\sum_{p\mid n}\frac{v_p(n)}p x_p.
\]

Dividing by the compulsory multiplicity residual gives

\[
\boxed{
\frac{d_x(n)}{m_n}
=
\sum_{p\mid n}
 v_p(n)\frac{R_n}{p}x_p.
}
\]

Define

\[
\boxed{
h(n)
=
\gcd_{p\mid n}
\left(
 v_p(n)\frac{R_n}{p}
\right).}
\]

For the unit block define

\[
h(1)=0.
\]

We call `h(n)` the **normalized block derivative content**.

## 3. P025-T36 — one integer ideal is the complete block image

For `n>1`, as the local prime-coordinate vector `x` ranges over

\[
\mathbb Z^{\operatorname{supp}(n)},
\]

the normalized derivative values are exactly

\[
\boxed{
\left\{
\frac{d_x(n)}{m_n}:x\right\}
=h(n)\mathbb Z.
}
\]

### Proof

The normalized derivative is an integer linear form with coefficient list

\[
\left\{
 v_p(n)R_n/p:p\mid n
\right\}.
\]

Every value is divisible by their gcd `h(n)`. Conversely Bezout's identity for that coefficient list produces an integer coordinate vector whose value is exactly `h(n)`, and scaling gives every multiple. ∎

### Interpretation

For any future language that sees a block only through the normalized derivative value, the full within-block prime-coordinate state can be replaced exactly by the principal ideal generator `h(n)`.

This is a quotient statement, not an approximation.

## 4. P025-T37 — the raw additive-row content is also block-compressed

Within the support block of `n`, the raw additive-relation coefficients are

\[
\frac{n v_p(n)}p
=
 m_n\left(v_p(n)\frac{R_n}p\right).
\]

Therefore their block content is

\[
\boxed{m_n h(n).}
\]

For a primitive abc triple, the full raw additive-row content is consequently

\[
\boxed{
g
=
\gcd\bigl(
 m_a h(a),
 m_b h(b),
 m_c h(c)
\bigr),}
\]

where a unit block contributes zero to the gcd.

Thus even the normalization needed to form `alpha_hat` does not require the individual prime coordinates once `h(a),h(b),h(c)` have been computed.

## 5. P025-T38 — at most three block-pair generators determine `eta_min`

Let

\[
R_a=\operatorname{rad}(a),
\quad
R_b=\operatorname{rad}(b),
\quad
R_c=\operatorname{rad}(c),
\]

and abbreviate

\[
h_a=h(a),
\quad
h_b=h(b),
\quad
h_c=h(c).
\]

For each pair of nonempty support blocks, define

\[
\boxed{
E_{ab}=\frac{R_c h_a h_b}{g},
\qquad
E_{ac}=\frac{R_b h_a h_c}{g},
\qquad
E_{bc}=\frac{R_a h_b h_c}{g},
}
\]

omitting any term whose paired blocks are empty.

Then each retained `E_ij` is a positive integer and

\[
\boxed{
\eta_{\min}
=
\gcd(E_{ab},E_{ac},E_{bc})
}
\]

over the retained positive terms.

### Proof

Consider the cross-prime terms from Supplement 05 for one fixed pair of blocks, say `a,b`:

\[
K_{p,q}
=
\frac{R_aR_bR_c}{g}
\left(\frac{v_p(a)}p\right)
\left(\frac{v_q(b)}q\right).
\]

Rewrite them as

\[
K_{p,q}
=
\frac{R_c}{g}
\left(v_p(a)\frac{R_a}p\right)
\left(v_q(b)\frac{R_b}q\right).
\]

The gcd over all `p|a`, `q|b` factors multiplicatively because the two indices vary independently:

\[
\gcd_{p,q}K_{p,q}
=
\frac{R_c}{g}
\left(
\gcd_{p|a}v_p(a)R_a/p
\right)
\left(
\gcd_{q|b}v_q(b)R_b/q
\right),
\]

which is exactly

\[
E_{ab}=R_c h_a h_b/g.
\]

The other two block pairs are identical. Taking the gcd across all cross-prime pairs is therefore the gcd of at most these three block-pair generators. ∎

## 6. Compression theorem

Combining P025-T36–T38, the exact absorption floor is a function of only

\[
\boxed{
\Sigma_{\rm block}(a,b,c)
=
\bigl(
(R_a,m_a,h_a),
(R_b,m_b,h_b),
(R_c,m_c,h_c)
\bigr).
}
\]

No individual prime-pair minor is needed once this state is known.

This is strictly coarser than the full prime-coordinate witness generator in general.

It is sufficient for `eta_min`, but it is **not** sufficient for the full witness lattice, the minimum witness radius `mu`, the access radius `nu`, or the full Pareto frontier. Those richer future observables still depend on the geometry of the prime-coordinate coefficients.

## 7. Examples

### `1+242=243`

For the unit block:

\[
(R_a,m_a,h_a)=(1,1,0).
\]

For

\[
242=2\cdot11^2,
\]

one has

\[
R_b=22,
\quad
m_b=11,
\]

and normalized derivative coefficients

\[
11,\ 4,
\]

so

\[
h_b=1.
\]

For

\[
243=3^5,
\]

\[
R_c=3,
\quad
m_c=81,
\quad
h_c=5.
\]

Thus

\[
g=\gcd(0,11,405)=1,
\]

and the only retained block-pair generator is

\[
E_{bc}=R_a h_b h_c=5.
\]

Therefore

\[
\boxed{\eta_{\min}=5.}
\]

The internal prime pair `(2,3)` versus `(11,3)` no longer needs to be stored for this observable.

### `2+7=9`

\[
h_a=1,
\qquad
h_b=1,
\qquad
h_c=2,
\qquad
g=1.
\]

The three block generators are

\[
E_{ab}=3,
\qquad
E_{ac}=14,
\qquad
E_{bc}=4.
\]

Hence

\[
\eta_{\min}=\gcd(3,14,4)=1.
\]

### `5+7=12`

Here

\[
h_a=h_b=1,
\qquad
h_c=2,
\qquad
g=1,
\]

so

\[
(E_{ab},E_{ac},E_{bc})=(6,14,10)
\]

and

\[
\boxed{\eta_{\min}=2.}
\]

## 8. Relation to second-order support closure

The block content

\[
h(n)=\gcd_p v_p(n)R_n/p
\]

makes the Stage-06/second-order phenomenon more concrete.

Its prime factors can come from:

- primes already in `R_n`;
- prime factors of valuation exponents `v_p(n)`.

It cannot acquire a genuinely new prime label from any other source because it is a gcd of products of exactly those integers.

Thus the block-compressed formula is consistent with the second-order support-closure theorem:

\[
\operatorname{supp}(\eta_{\min})
\subseteq
\operatorname{supp}(R)
\cup
\bigcup_p\operatorname{supp}(v_p(abc)).
\]

## 9. Architectural meaning

P025 has now produced two very different kinds of compression from the same fine prime-coordinate state:

### Arithmetic-floor language

If the future task asks only for `eta_min`, then

\[
\boxed{
\text{prime-coordinate valuation state}
\to
\text{three block contents }h_a,h_b,h_c
\to
\eta_{\min}
}
\]

is exact.

### Geometric-access language

If the future task asks for `mu`, `nu`, a witness itself, or the Pareto frontier, the same block compression is generally too coarse.

So this is another concrete instance of P023's principle:

> the coarsest legal precision is not an intrinsic property of the number alone; it is indexed by the future observable that must remain exact.

## 10. Executable assets

Added:

- `src/enterprise_math/abc_absorption_block.py`
  - normalized block derivative coefficients;
  - block image content `h(n)`;
  - raw additive block content `m(n)h(n)`;
  - at-most-three block-pair absorption generators;
  - compact block state sufficient for `eta_min`.
- `tests/test_abc_absorption_block.py`
  - exact block image examples;
  - reconstruction of raw additive content;
  - worked absorption examples;
  - exhaustive agreement of block formula and cross-prime formula for primitive triples with `c<100`.

## 11. Prior-art discipline

The image of one integer linear form being the gcd-generated ideal is elementary Bezout algebra. Grouping a gcd of separable pair products by independent block gcds is also elementary arithmetic.

P025 does not claim these algebraic identities themselves as new mathematics.

The project-specific candidate is the observation that the `abc` arithmetic-Wronskian absorption floor admits this much smaller exact precision state while the witness-access geometry does not. That task-indexed compression remains `NOVELTY_UNVERIFIED` as a project synthesis.

## 12. Next frontier

No hard block exists. Continue with:

1. characterize when two distinct fine triples have the same block absorption state but different access radius `nu`, giving a direct minimality/no-go witness for the block compression;
2. derive local-prime obstruction formulas directly from `(R_i,m_i,h_i)` rather than from all exponent coordinates;
3. test whether `h(n)` itself has useful recursive precision structure under multiplication or exponentiation;
4. compare block derivative content with Pasten's chosen lattice bases and norm bounds;
5. determine whether analogous block-content compression appears for other relation-conditioned witness systems outside abc.
