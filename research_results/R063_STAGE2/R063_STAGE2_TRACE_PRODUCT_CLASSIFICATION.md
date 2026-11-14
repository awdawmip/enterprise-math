# R063 Stage 2 — Multiplicative Trace Product Classification

Status: `ORIENTATION-CONDITIONAL EXACT PRODUCT / CHOICE-FREE DESCENT NO-GO`

## 1. Two different trace operations must not be merged

The frozen R061 trace already has its native additive composition

`T_{a,b}^{(ij)} * T_{c,d}^{(ij)} = T_{a+c,b+d}^{(ij)}`.

Representative word concatenation and interleaving belong to this additive-component operation.

Stage 2 studies a different operation induced by norm-root multiplication. These operations are not the same and use different symbols.

## 2. Oriented multiplicative trace product

Fix an ordered sector orientation and the exact component product `star_i` from the unit-quotient classification. Define

`T_r odot_i T_s = T_{r star_i s}`.

This gives

`Trace_E(A) x Trace_E(B) -> Trace_E(AB)`

on the frozen sector-local trace carrier.

Because trace identity is exactly the ordered component trace and `star_i` is associative, commutative and norm-graded,

- `odot_i` is well defined;
- `odot_i` is associative;
- `odot_i` is commutative;
- identity is `T_{1,0}`;
- norm grading is multiplicative.

This is an exact theorem **conditional on the ordered sector orientation**. It is not a global Enterprise-plane native multiplication claim.

## 3. Mandatory discriminator and orientation-free no-go

For `A=B=2`, the only ordered nonnegative source root is `(1,1)`. Under the `i` orientation,

`T_{1,1} odot_i T_{1,1}=T_{0,2}`.

Under the swap-conjugate orientation,

`T_{1,1} odot_j T_{1,1}=T_{2,0}`.

Both targets represent the same unit orbit, but they are distinct frozen R061 component traces.

Let `sigma(T_{a,b})=T_{b,a}`. The input trace is fixed by `sigma`, while neither norm-4 target trace is fixed. Therefore no single-valued trace product can simultaneously:

1. lift the `URoot` product;
2. retain the full ordered Stage 1 trace fiber; and
3. be equivariant under component swap.

Hence the strongest choice-free statement is a no-go. A specific ordered-sector convention breaks the symmetry and yields the exact conditional product `odot_i`.

## 4. Distinction from path concatenation

At the same mandatory witness,

`T_{1,1} * T_{1,1}=T_{2,2}`

under frozen R061 additive composition, whereas

`T_{1,1} odot_i T_{1,1}=T_{0,2}`

under Stage 2 norm-root multiplication.

Thus

`TRACE_MULTIPLICATIVE_PRODUCT != PATH_CONCATENATION_TRACE_PRODUCT`.

No cardinality comparison can erase this typing difference.

## 5. Classification

`ORIENTATION_CONDITIONAL_MULTIPLICATIVE_TRACE_PRODUCT = PROVED`.

`TRACE_PRODUCT_IS_FROZEN_ADDITIVE_CONCATENATION = FALSE`.

`ORIENTATION_FREE_ORDERED_TRACE_MULTIPLICATION = NO_GO_UNDER_COMPONENT_SWAP_EQUIVARIANCE`.

Semantic verdict: `CONDITIONAL_DERIVED`.
