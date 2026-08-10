# P025 Supplement 64 — de Bruijn Tail for the Projective Capacity Observable

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-paired-square-tail-stage61`  
Depends on: P025 Supplements 59, 61, 62  
Hard block: `NONE`

## 1. Replace a power threshold by an arbitrary projective threshold

Work on the dyadic range

\[
X/2<c\le X
\]

and let

\[
1\le T\le X.
\]

Suppose

\[
\sigma_{\rm proj}\ge T.
\]

For a non-unit triple, the Stage-61 argument does not require `T=c^eta`. It gives directly two distinct components `x,y` with

\[
\boxed{
m(x)m(y)\ge\frac{Tc}{2}.}
\]

Hence

\[
\operatorname{rad}(xy)
=
\frac{xy}{m(x)m(y)}
\le
\frac{2xy}{Tc}
<
\boxed{\frac{4X}{T}}.
\]

Thus every large projective state produces one pair product

\[
xy\le X^2
\]

whose radical is only of order `X/T`.

For a unit triple, the Stage-50 one-component argument gives analogously a non-unit component `n<=X` with

\[
\operatorname{rad}(n)\ll X/T.
\]

## 2. P025-T130 — external de Bruijn input gives a `T^-1` tail

Apply the classical de Bruijn radical-counting estimate to the non-unit pair product and to the one-variable unit state [SRC-BERNERT-BROWNING-LICHTMAN-TERAVAINEN-2026-ABC-EXCEPTIONAL-CURRENT; SRC-LICHTMAN-2025-ABC-ALMOST-ALWAYS].

The pair product lies below `X^2` and has radical `O(X/T)`. The external estimate therefore gives, after an arbitrary `X^epsilon` loss, only

\[
O_\varepsilon\left(\frac{X^{1+\varepsilon}}T\right)
\]

possible pair products. A standard divisor-bound loss reconstructs the labelled factor pair, and the additive relation determines the third component.

The unit slice has the same or smaller scale. Therefore

\[
\boxed{
N_X(\sigma_{\rm proj}\ge T)
\ll_\varepsilon
\frac{X^{1+\varepsilon}}T,
\qquad
1\le T\le X.
}
\]

This is an unconditional tail theorem for the explicit P025 projective observable, conditional only on importing the external de Bruijn radical-counting theorem as prior art.

It strictly improves the internal elementary Stage-59 tail

\[
N_X(\sigma_{\rm proj}\ge T)
\ll
\frac{X^2}{\sqrt T}.
\]

## 3. P025-C13 — normalized moments are controlled for every fixed order below two

The projective observable satisfies the trivial finite bound

\[
0<\sigma_{\rm proj}\le X
\]

on height `X`.

Let

\[
0<\theta<2.
\]

The contribution from `sigma_proj<1` is at most the ambient `O(X^2)` triple count. For the tail above one, layer-cake gives

\[
\sum \sigma_{\rm proj}^{\theta}
\ll
X^2
+
X^{1+\varepsilon}
\int_1^X t^{\theta-2}\,dt.
\]

If `theta<1`, the integral is bounded; if `theta=1`, it is logarithmic; if `1<theta<2`, it is `O(X^(theta-1))`. In all cases one may choose `epsilon>0` sufficiently small relative to `2-theta` to obtain

\[
\boxed{
X^{-2}
\sum_{X/2<c\le X}
\sigma_{\rm proj}^{\theta}
=O_\theta(1)
\qquad(0<\theta<2).
}
\]

The sum may be restricted to primitive triples.

This should be read as the **moment range proved by the present tail estimate**. It is not a claim that `theta=2` is the true analytic critical order.

## 4. Comparison with Stage 59

Stage 59 used only the elementary one-square tail and obtained a uniform moment statement for orders below `1/2`.

After the Stage-61 paired reduction and the external de Bruijn input, the proved range becomes

\[
\boxed{0<\theta<2.}
\]

The gain comes from two independent improvements:

1. the additive relation turns one residual into a paired residual product;
2. de Bruijn counts the resulting small-radical pair product directly instead of union-bounding all square divisors.

Thus a theorem imported from prior number theory changes not only an exponent but the effective precision dimension of the exceptional-state count.

## 5. Architecture interpretation

The tail route can be written as

\[
\boxed{
\sigma_{\rm proj}\ge T
\to
\text{paired residual pressure}
\to
\text{pair product }xy
\to
\operatorname{rad}(xy)\ll X/T
\to
\text{de Bruijn count}.
}
\]

Each arrow discards information, but every discarded coordinate is irrelevant to the declared future query "how many states exceed projective threshold T?".

This is a worked example where an external theorem becomes useful only after the project has compiled its fine witness state into the theorem's natural input language.

## 6. Prior-art boundary

The radical-counting theorem, divisor bound, layer-cake identity, and classical/modern abc exceptional-set results are prior mathematics. P025 does not claim them.

The project-specific result is only the exact compiler from `sigma_proj>=T` to a pair-product radical state and the resulting application of those prior tools to the P025 observable. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 7. Executable assets

Added:

- `src/enterprise_math/abc_projective_debruijn_tail.py`;
- `tests/test_abc_projective_debruijn_tail.py`.

The implementation records exact paired reductions and rational moment-range calculus. It deliberately does not fake an implementation of the external asymptotic de Bruijn theorem.

## 8. Next frontier

No hard block exists. Continue with:

1. seek lower-bound or structured families before calling `theta=2` a true moment boundary;
2. compare the pair-product radical state with the modern anatomic decomposition of integer exponent layers;
3. use the stronger tail for PCC-specific average questions, not as a substitute for the much stronger ordinary abc exceptional-set literature;
4. backflow the staged `fine state -> theorem-native coarse state` compiler pattern to A2/P023.
