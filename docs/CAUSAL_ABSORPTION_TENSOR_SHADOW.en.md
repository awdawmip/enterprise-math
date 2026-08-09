# Causal Absorption 06 — Tensor-Like Structure as a Shadow of LEGO Multiadditive Interaction

Status: `CROSS-ROUTE RESEARCH WIP / EXACT FREE-INTEGER DERIVATION + NEGATIVE BOUNDARY`

## 1. Do not assume tensors first

We already have two causal facts: a single-system operation that preserves LEGO composition has an integer-matrix shadow, and local response interaction is not the same thing as causal coupling. The next question is why bilinear/tensor structure sometimes appears at all.

Let a cross effect be `B(x,y)`. Assume separate LEGO additivity:

\[
B(x_1\oplus x_2,y)=B(x_1,y)\oplus B(x_2,y),
\]

\[
B(x,y_1\oplus y_2)=B(x,y_1)\oplus B(x,y_2),
\]

with zero multiplicity producing no cross effect.

## 2. TS-01 — Unit-pair effects generate the full response

Let `e_i` and `f_j` be left and right unit generators and define

\[
\boxed{b_{ij}=B(e_i,f_j).}
\]

For

\[
x=\sum_i x_ie_i,\qquad y=\sum_jy_jf_j,
\]

separate additivity forces

\[
\boxed{B(x,y)=\sum_{i,j}x_iy_jb_{ij}.}
\]

The primitive causal data are therefore the effects of one left unit meeting one right unit. A bilinear matrix or rank-two tensor is a coordinate shadow of that pair-effect table.

## 3. TS-02 — Converse

Any finite unit-pair effect table defines an exact separately LEGO-additive interaction by the same finite integer sum. Hence in the free-integer regime:

\[
\boxed{\text{separate LEGO additivity}\iff\text{unit-pair effect-table representation}.}
\]

This is the causal admission condition for the bilinear/tensor shadow.

## 4. TS-03 — Multi-system extension

If an `r`-system cross effect is separately LEGO-additive in every argument, it is determined by unit tuples:

\[
\boxed{
B(x^{(1)},\ldots,x^{(r)})
=
\sum_{i_1,\ldots,i_r}
\left(\prod_{a=1}^r x^{(a)}_{i_a}\right)
B(e^{(1)}_{i_1},\ldots,e^{(r)}_{i_r}).
}
\]

A traditional rank-`r` multilinear array/tensor is only the coordinate rendering of those unit-tuple effects.

## 5. Negative boundary

For one unit type on each side, take

\[
B(n,m)=\min(n,m).
\]

Because `B(1,1)=1`, a fixed pair-effect representation would predict `B(2,1)=2`; the actual value is `1`. Thus threshold, saturation, competition, capacity limits, and similar interactions are generally not exactly representable by a fixed tensor table.

Tensor language is therefore not a universal interaction ontology. It is exact only in the separately additive regime.

## 6. Tensor-like response is not causal coupling

A nonzero pair-effect table need not add any causal information. If marginal signatures already determine `x` and `y`, then `B(x,y)` can be reconstructed from those marginals and adds no signature split. Conversely, parity-style reachability constraints can create higher-order causal coupling with no specified bilinear response.

The exact bridge is still the fiber-descent criterion: a joint response adds causal distinction iff it is nonconstant on at least one marginal-signature fiber.

## 7. Traditional tensor product status

Causally derived so far:

- unit-pair effect tables;
- separately additive bilinear shadows;
- multiadditive unit-tuple shadows.

Not yet causally derived as ontology:

- the full abstract tensor-product universal-property framework;
- Hilbert tensor products;
- topological tensor completions;
- quantum tensor ontology.

These remain coordinate/shadow or external tools until a stronger causal necessity is proved.

## 8. Executable assets

- `src/enterprise_math/lego_pair_interaction.py`
- `tests/test_lego_pair_interaction.py`

## 9. Next

1. compare multiadditive unit-tuple interactions with minimal nonfaces of the causal independence complex;
2. determine when an irreducible coupling group admits an exact multilinear shadow;
3. derive native LEGO composition laws for saturation, threshold, and carry interactions that tensors cannot express;
4. seek the minimum joint state when both pair-effect data and signature-coupling data are future-relevant.
