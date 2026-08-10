# P025 Supplement 43 — Exact Projective Efficiency and Effective-Derivative Overhead Decomposition

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-certificate-index-stage34`  
Depends on: P025 Supplements 24, 42  
Hard block: `NONE`

## 1. `mu/eta_min` still mixes different difficulties

Supplement 42 defines the effective first-witness resource

\[
\mu_{\rm eff}=\mu/\eta_{\min}.
\]

This is already weaker than the ordinary minimum norm `mu`, but it still mixes:

1. how efficiently a witness **direction** converts `L_infinity` radius into Wronskian magnitude;
2. how early an integer witness can approximate that direction;
3. how much absorption redundancy remains at the first nondegenerate radius.

The present supplement separates these exactly.

## 2. Homogeneous projective witness cost

For any nondegenerate integer witness `x`,

\[
\eta(x)=|W(x)|/M,
\qquad
M=m(a)m(b)m(c).
\]

Define the homogeneous cost

\[
\boxed{
\sigma(x)=\frac{\|x\|_\infty}{\eta(x)}
=\frac{M\|x\|_\infty}{|W(x)|}.
}
\]

For every nonzero integer `k`,

\[
\sigma(kx)=\sigma(x).
\]

Thus this is a projective direction cost rather than an access-radius cost.

## 3. P025-T105 — integer and real projective optima agree

Let the real additive relation hyperplane be

\[
V=\{x\in\mathbb R^S:\alpha\cdot x=0\}.
\]

The set

\[
V\cap[-1,1]^S
\]

is a rational polytope and the Wronskian is a rational linear functional.

A maximum of `|W|` is attained at a rational vertex. Scaling that vertex by a common positive denominator gives an integer relation witness with the same homogeneous ratio.

Hence

\[
\boxed{
\inf_{x\in T\setminus T^\circ}
\frac{\|x\|_\infty}{\eta(x)}
=
\frac{M}{
\max_{x\in V,\ \|x\|_\infty\le1}|W(x)|
}.
}
\]

There is no integrality gap at the **projective** level. Integrality matters only when one asks how early the optimal or near-optimal direction becomes accessible.

## 4. P025-T106 — LP duality reduces the operator norm to three pair capacities

The ordinary dual norm identity gives

\[
\max_{\alpha x=0,\ \|x\|_\infty\le1}|\beta x|
=
\min_{t\in\mathbb R}
\|\beta-t\alpha\|_1.
\]

For primitive abc, the coordinatewise ratios `beta_p/alpha_p` take only three values:

\[
-b\quad(p\mid a),
\qquad
a\quad(p\mid b),
\qquad
0\quad(p\mid c).
\]

Let

\[
U_n
=
\sum_{p\mid n}
\frac{n v_p(n)}p
=m(n)C(n).
\]

The weighted `L_1` median can therefore be chosen among `-b,0,a`. Evaluating at these three values gives

\[
P_{ab}=aU_b+bU_a,
\]

\[
P_{ac}=aU_c+cU_a,
\]

\[
P_{bc}=bU_c+cU_b.
\]

Thus the exact Wronskian operator norm is

\[
\boxed{
L=\min\{P_{ab},P_{ac},P_{bc}\}.
}
\]

## 5. P025-D27 — exact projective efficiency

Define

\[
\boxed{
\sigma_{\rm proj}
=
\frac{M}{L}.
}
\]

Using

\[
P_{ab}=m(a)m(b)K_{ab}
\]

and its cyclic analogues gives the equivalent formula

\[
\boxed{
\sigma_{\rm proj}
=
\max\left\{
\frac{m(c)}{K_{ab}},
\frac{m(b)}{K_{ac}},
\frac{m(a)}{K_{bc}}
\right\}.
}
\]

This is an **explicit factor/valuation state**. It contains no witness search.

## 6. P025-T107 — exact three-factor decomposition of `mu_eff`

Let

\[
\eta_\mu=E(\mu)
\]

be the smallest absorption redundancy attained at the first nondegenerate radius.

Then

\[
\frac{\mu}{\eta_{\min}}
=
\underbrace{\sigma_{\rm proj}}_{\text{continuous projective pressure}}
\cdot
\underbrace{
\frac{\mu/\eta_\mu}{\sigma_{\rm proj}}
}_{G_{\rm align}}
\cdot
\underbrace{
\frac{\eta_\mu}{\eta_{\min}}
}_{G_{\rm abs}}.
\]

That is,

\[
\boxed{
\mu_{\rm eff}
=
\sigma_{\rm proj}
G_{\rm align}
G_{\rm abs}.
}
\]

Both discrete overhead factors satisfy

\[
\boxed{G_{\rm align}\ge1,
\qquad
G_{\rm abs}\ge1.}
\]

They measure different phenomena:

- `G_align`: the first accessible integer witness direction has not yet reached the best projective Wronskian efficiency;
- `G_abs`: the first radius has not yet descended to the complete intrinsic Wronskian-image floor.

## 7. Exact calibrations

### `2+7=9`

\[
\sigma_{\rm proj}=1/3,
\qquad
\mu=1,
\qquad
\eta_\mu=3,
\qquad
\eta_{\min}=1.
\]

Therefore

\[
\boxed{G_{\rm align}=1,
\qquad
G_{\rm abs}=3.}
\]

The first witness already uses the best projective direction; all effective overhead is absorption-level delay.

### `3+125=128`

\[
\sigma_{\rm proj}=32/7,
\qquad
\mu=6,
\qquad
\eta_\mu=\eta_{\min}=1.
\]

Hence

\[
\boxed{
G_{\rm align}=21/16,
\qquad
G_{\rm abs}=1.
}
\]

This is an intrinsically saturated hard case; the entire gap is integer direction alignment.

### `1+242=243`

\[
\sigma_{\rm proj}=27/5,
\qquad
\mu/\eta_{\min}=27/5.
\]

Thus

\[
\boxed{G_{\rm align}=G_{\rm abs}=1.}
\]

The first witness simultaneously attains the projective optimum and the intrinsic absorption floor.

### `1+512=513`

\[
\sigma_{\rm proj}=64/15,
\qquad
\mu/\eta_{\min}=13/3,
\]

with

\[
\boxed{
G_{\rm align}=65/64,
\qquad
G_{\rm abs}=1.
}
\]

Only a very small alignment loss remains.

## 8. Negative boundary: covolume ratio alone does not control alignment

A tempting shortcut is to use only the covolumes of the additive witness lattice and the Wronskian-degenerate sublattice.

Small exact searches produce counterexamples: triples with small or favorable determinant ratios can still have first nondegenerate radius `mu` strictly larger than any bound depending only on that scalar ratio.

Thus the integer alignment factor cannot generically be replaced by one covolume quotient. Preimage/coset geometry remains necessary.

This agrees with earlier P025 negative results: image content does not determine minimum preimage access.

## 9. Architectural consequence

The small-derivative problem is no longer one undifferentiated shortest-vector task. It has three independent layers:

\[
\boxed{
\text{continuous factor/radical pressure}
\to
\text{integer projective alignment}
\to
\text{absorption-level descent}.
}
\]

A successful route may attack these separately.

## 10. Prior-art discipline

Linear-programming duality, quotient norms and weighted medians are standard convex analysis. P025 claims no priority for those tools.

The project-side candidate is their exact specialization to Pasten's relation-adapted arithmetic Wronskian together with the finite-precision factorization of `mu/eta_min`. Historical novelty remains unverified.

## 11. Executable assets

Added:

- `src/enterprise_math/abc_projective_efficiency.py`;
- `tests/test_abc_projective_efficiency.py`.

## 12. Next frontier

No hard block exists. Continue with:

1. exact integer alignment in low-support slices;
2. modular corner obstructions in `(1,2,1)` support;
3. the hard saturated subfamily `eta_min=1`;
4. whether `G_align` or `G_abs` admit subpower control in high-quality families;
5. prior-art audit of the explicit projective normalization.
