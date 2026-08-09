# Causal LEGO Fiber Composition — One Fiber Law Generates Sum-Product, Min-Plus, and Boolean Shadows

Status: `ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT FINITE LEGO THEOREMS`

## 1. Core correction

Do not begin with a preferred algebra merely because dynamic programming, semirings, or convolution are familiar. The prior object is the fine-lift decomposition of a LEGO coarse block.

For `m` nonnegative fine slots and coarse total `c`, define

\[
\mathcal F_m(c)=\{(a_1,\ldots,a_m)\in\mathbb N^m:\sum_i a_i=c\}.
\]

The unit remains `1`; `m` records how many fine relation slots the same units may occupy.

## 2. FC-01 — Fiber composition law

Split `m+n` slots into a left block of size `m` and a right block of size `n`. Every full lift uniquely determines a left total `a`, a left lift in `F_m(a)`, and a right lift in `F_n(c-a)`. Conversely these data uniquely reconstruct the full lift. Hence

\[
\boxed{
\mathcal F_{m+n}(c)
\cong
\bigsqcup_{a=0}^{c}
\mathcal F_m(a)\times\mathcal F_n(c-a).
}
\]

This set/fiber identity is the prior object.

## 3. FC-02 — Counting generates sum-product convolution

Let

\[
H_m(c)=|\mathcal F_m(c)|.
\]

Taking cardinality of FC-01 gives

\[
\boxed{
H_{m+n}(c)=\sum_{a=0}^{c}H_m(a)H_n(c-a).
}
\]

Alternative total splits are added, while independent left/right fine choices are multiplied. Ordinary convolution is therefore a counting shadow of one causal fiber law.

The closed form is

\[
\boxed{H_m(c)=\binom{c+m-1}{m-1}.}
\]

Stars-and-bars and Vandermonde are counting/proof tools for this fiber structure.

## 4. FC-03 — Minimum additive cost generates min-plus convolution

If each fine lift carries an additive block cost and the question asks only for the minimum, the same FC-01 decomposition gives

\[
\boxed{
\Psi_{m+n,s}(c)
=
\min_a\left[\Psi_{m,s}(a)+\Psi_{n,s}(c-a)\right].
}
\]

Min-plus is not a second geometric ontology. It is the algebraic shadow created by asking a minimum-additive-cost question of the same LEGO fiber composition.

## 5. FC-04 — Existence generates Boolean composition

For constrained fibers, if the question is only whether a fine lift exists,

\[
\boxed{
E_{m+n}(c)
=
\bigvee_a\left(E_m(a)\wedge E_n(c-a)\right).
}
\]

Boolean OR/AND convolution is therefore another observation shadow of the same prior fiber law.

## 6. FC-05 — Observation-algebra principle

Current candidate principle:

\[
\boxed{
\text{one causal fiber composition}
+
\text{different questions}
\to
\text{different traditional algebra shadows}.
}
\]

Already derived:

- counting -> sum/product;
- minimum additive cost -> min/+;
- existence -> OR/AND.

Future encounters with tropical, max-plus, generating-function, or semiring machinery should first be tested as observation shadows of a prior fiber decomposition rather than installed as ontology.

## 7. FC-06 — Exact dimension-lowering difference law

The counting shadow satisfies

\[
\boxed{H_m(c+1)-H_m(c)=H_{m-1}(c+1),\qquad m\ge2.}
\]

Pure LEGO proof: inject `F_m(c)` into `F_m(c+1)` by adding one unit to a designated slot. The states missed by this injection are exactly the `(c+1)`-unit lifts in which that slot is zero; deleting the empty slot identifies them with `F_(m-1)(c+1)`.

Thus the difference is not an approximate derivative. One exact integer difference removes one hidden slot freedom.

Repeatedly,

\[
\boxed{\Delta^rH_m(c)=H_{m-r}(c+r),}
\]

and

\[
\boxed{\Delta^{m-1}H_m(c)=1,\qquad\Delta^mH_m(c)=0.}
\]

Hence `m-1` is the exact difference depth of the hidden-allocation multiplicity. It agrees with relation-rank, contraction-depth, and earlier ball-growth dimension measurements.

## 8. FC-07 — `1` stays `1`

For one unit,

\[
H_m(1)=m.
\]

The coarse total is still exactly `1`. What increased is the number of fine placements of that one unit. Dimension increases relation/placement possibilities rather than changing the unit value itself.

## 9. FC-08 — One `(m,c)` pair generates multiple fiber observables

The tagged contraction state `(capacity m,total c)` determines:

- total fine-lift multiplicity
  \[
  H_m(c)=\binom{c+m-1}{m-1};
  \]
- minimum power/collision cost
  \[
  \Psi_{m,s}(c)=\min_{\sum a_i=c}\sum_i|a_i|^s;
  \]
- balanced minimizer count: if `c=mq+r`,
  \[
  \boxed{N_{min}(m,c)=\binom mr.}
  \]

Thus capacity is not merely a numerical value with a precision annotation. It is a structural parameter of the contraction fiber.

## 10. Relation to P011

At fixed finite total unit count, every coarse partition state has a finite fiber multiplicity. Feeding those multiplicities into

\[
J_k=\sum_{coarse\ states}\binom{H(coarse)}k
\]

makes dimension contraction another concrete role of the Causal Collapse Spectrum.

## 11. Traditional-tool status

- stars-and-bars: `COORDINATE/COUNTING TOOL`;
- Vandermonde convolution: `SHADOW_FORMULA`;
- sum-product convolution: `CAUSAL_DERIVED SHADOW`;
- min-plus convolution: `CAUSAL_DERIVED SHADOW`;
- Boolean convolution: `CAUSAL_DERIVED SHADOW`;
- generic semiring ontology: not yet admitted as a foundation object.

## 12. Executable assets

- `src/enterprise_math/lego_partition_fiber.py`
- `tests/test_lego_partition_fiber.py`
- `src/enterprise_math/dimension_contraction.py`

## 13. Next

1. define a general fiber-question/aggregator interface without promoting abstract semirings to ontology;
2. test whether P011 collision spectra themselves inherit recursive generation from FC-01;
3. reinterpret graph-ball and radial-ball high-dimensional recursions as fiber questions;
4. test threshold, min/max, carry, and material-collision rules as observation shadows of the same fiber composition;
5. determine how FC-01 is modified once the two blocks are causally coupled.
