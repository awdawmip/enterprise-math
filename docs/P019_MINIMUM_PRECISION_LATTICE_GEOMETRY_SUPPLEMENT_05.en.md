# P019 Supplement 05 — Collision-Power Contraction Family `Psi_(m,s)`

Status: `RESEARCH WIP / FINITE IDENTITIES VERIFIED`  
Scope: graph/radial unification, hidden dimensional capacity, full collision spectrum, cross-dimensional cut-boundary recursion

## 1. Master family

For integers `m>=1`, `s>=1`, `c in Z`, define

\[
\Psi_{m,s}(c)
=
\min_{a_1+\cdots+a_m=c}
\sum_{i=1}^m |a_i|^s.
\]

If

\[
|c|=mq+r,
\qquad 0\le r<m,
\]

balanced allocation gives

\[
\boxed{
\Psi_{m,s}(c)
=(m-r)q^s+r(q+1)^s.
}
\]

Moreover,

\[
\boxed{
\Psi_{m,s}(1)=1
\quad\forall m,s.
}
\]

Thus the minimum unit remains one independently of slot capacity and collision order.

## 2. `s=1` and `s=2`

For `s=1`,

\[
\Psi_{m,1}(c)=|c|,
\]

which is independent of `m`. On zero-sum states,

\[
\sum_i|c_i|=2d_G(0,c),
\]

so primitive graph balls are the `s=1` member and block-size tags become numerically invisible under contraction.

For `s=2`,

\[
\Psi_{m,2}(c)=\psi_m(c),
\]

the tagged radial square-energy family of Supplement 04.

Thus graph and radial models are different collision orders of one `Psi_(m,s)` family.

## 3. Dimension addition remains min-plus composition

For every fixed `s>=1`,

\[
\boxed{
\Psi_{m+n,s}(c)
=
\min_{a+b=c}
\left(\Psi_{m,s}(a)+\Psi_{n,s}(b)\right).
}
\]

Hence

\[
\boxed{
\Psi_{m,s}\square\Psi_{n,s}
=\Psi_{m+n,s}.
}
\]

Integer addition of block sizes is exactly represented by min-plus composition.

## 4. Connection to the full `J_k` collision spectrum

For a nonnegative occupancy `a`,

\[
a^s
=
\sum_{j=1}^s
S(s,j)\,j!\binom aj,
\]

where `S(s,j)` is a Stirling number of the second kind.

Therefore, for an occupancy configuration,

\[
\sum_i a_i^s
=
\sum_{j=1}^s
S(s,j)\,j!
\sum_i\binom{a_i}{j}.
\]

The inner sum is exactly a P011-type `J_j` collision count.

Examples:

\[
a^2=a+2\binom a2,
\]

\[
a^3=a+6\binom a2+6\binom a3.
\]

Thus `s=1` sees only units, `s=2` first sees pair collisions, `s=3` additionally sees triple collisions, and higher `s` reads higher multiplicities through fixed integer coefficients.

## 5. Tagged collision-power balls

For a block partition

\[
\mathbf m=(m_1,\ldots,m_k),
\]

define

\[
E^{(s)}_{\mathbf m}(c)
=
\sum_i\Psi_{m_i,s}(c_i),
\qquad
\sum_i c_i=0,
\]

and

\[
B^{(s)}_{\mathbf m}(T)
=
\{c:E^{(s)}_{\mathbf m}(c)\le T\}.
\]

Fix a transfer channel `j -> i`, and merge blocks `i,j` into size `m_i+m_j`, producing `m'`. Since `Psi_(m,s)` is discretely convex, each fiber sublevel set is an integer interval, and each nonempty fiber has exactly one directed exit across the threshold.

Therefore the entire family obeys

\[
\boxed{
|C^{(s)}_{\mathbf m,j\to i}(T)|
=
|B^{(s)}_{\mathbf m'}(T)|.
}
\]

This identity has been checked by finite integer enumeration for `s=1,2,3,4`, several block partitions, and finite threshold ranges.

## 6. Current unified picture

P019 now has the integer hierarchy

\[
\boxed{
\text{unit }1
\to
\text{block capacity }m
\to
\text{collision sensitivity }s.
}
\]

Here:

- `1` remains exactly `1`;
- `m` stores dimensional slot capacity hidden by contraction;
- `s` controls how high an order of collision multiplicity is read;
- dimension merging is block-size addition;
- energy merging is min-plus convolution;
- a fixed-direction cavity cut boundary recursively becomes a lower-dimensional tagged ball.

The current strongest candidate form of “higher dimension from simple lower-dimensional operations” is therefore

\[
\boxed{
\text{dimension addition}
\leftrightarrow
\text{tag addition}
\leftrightarrow
\text{min-plus contraction}.
}
\]

## 7. Next steps

1. Formalize balanced minimization, the min-plus law, and the cut-boundary theorem in Lean.
2. Test whether the full `J_k` spectrum has stronger invariance across different contraction trees.
3. Keep `s` as an observation/tool order unless a separate argument justifies any physical interpretation.
4. Map prior art in discrete convex analysis, infimal convolution, and integer resource allocation before novelty claims.
5. Continue cavity, defect, boundary, and causal-mark pressure tests against fixed FCC/HCP interpretations.
