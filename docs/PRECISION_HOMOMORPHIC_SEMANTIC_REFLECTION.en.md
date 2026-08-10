# Homomorphic Syntax Preservation Is Not Semantic Reflection

Status: `RESEARCH BRIDGE / NONCANONICAL`

Coefficient collapse through a quotient homomorphism has a built-in directionality. Algebraic terms evaluate compatibly with the quotient, so exact equations map forward automatically. The quotient does not automatically reflect exact truth, witness uniqueness, branch identity or other logical properties back to the source world.

## 1. Polynomial syntax descends automatically

Let

`phi:R -> S`

be a ring homomorphism. For every polynomial term t and tuple x,

`phi(t_R(x)) = t_S(phi(x))`.

Thus quotienting coefficients/states preserves polynomial evaluation exactly.

For `R=Z`, `S=Z/MZ`, any exact equation

`t(x)=0 over Z`

implies

`t(x)==0 mod M`.

This forward soundness needs no special theorem beyond homomorphism.

## 2. Quotient truth means kernel membership, not exact truth

In `R/I`, the statement

`t(x)=0`

means only

`t(x) in I`

in the source ring.

Therefore quotient truth is an **I-thickening** of exact zero.

For every finite integer modulus M, even the identity equation supplies an immediate reflection failure:

`x=M` is nonzero in Z but zero modulo M.

So no fixed finite quotient reflects exact zero on all unbounded integers.

## 3. Independent bounds can restore reflection

If a source value z is independently known to satisfy

`|z|<=B`,

then any modulus

`M>B`

has the property

`z==0 mod M iff z=0`.

This is the smallest form of the bounded-world principle seen throughout the local-global line:

`forward quotient soundness + independent height bound -> exact reflection on the admissible set`.

The bound comes from world structure, not from the quotient itself.

## 4. Equational syntax and logical interpretation are different layers

The quotient can preserve the written polynomial term while invalidating a logical implication used to interpret it.

Example over an integral domain:

`ab=0 -> a=0 OR b=0`.

The product term and equality to zero descend syntactically to every quotient ring. The disjunctive branch interpretation does not.

For `R/I`, the implication holds for all coefficient values exactly when I is prime.

So the same homomorphic quotient can be:

- perfectly sound for polynomial evaluation;
- unsound for recovering the branch logic that the source domain attached to that polynomial.

## 5. Integer modular specialization

For

`Z -> Z/MZ`,

generic product/disjunction reflection holds exactly at prime moduli.

- M prime: quotient is a field/domain;
- M composite, including `p^e` with `e>1`: zero divisors create product-zero false branches;
- M=1: trivial zero-ring collapse, not a faithful logical world.

Thus greater p-adic numeric depth can coexist with lower generic branch-law faithfulness.

## 6. Forward preservation and backward reflection must be named separately

A safe precision architecture should distinguish at least:

### Forward preservation

If an exact source state satisfies the law, its collapsed image satisfies the quotient law.

Polynomial/equational syntax receives this automatically under homomorphism.

### Backward reflection

If a collapsed state satisfies the quotient law, does it arise from an exact source state satisfying the intended exact semantics?

This is additional structure.

Examples of reflection questions include:

- exact zero from modular zero;
- exact IMAGE reachability from modular reachability;
- branch identity from product zero;
- uniqueness/nonzeroness/cancellation;
- exact witness/state realization from profinite existence.

Each requires its own theorem or bound.

## 7. Relation to local-global precision

The affine local-global theorem is a global reflection theorem across an unbounded family of quotient precisions:

`Ax==b mod every M`

reflects

`Ax=b over Z`.

A finite family fails without additional structure; a bounded target family can restore reflection.

The nonlinear profinite ghost shows that even **all** finite quotient truths need not reflect exact existence for a general equation class.

So “homomorphism preserves the formula” and “the inverse system reflects exact semantics” are very different statements.

## 8. Relation to witness descent

For a labelled relation, a quotient may preserve the unlabelled equation while failing witness reflection.

The semantic-safe strategy is therefore:

1. identify which exact logical/witness properties matter to the future language;
2. determine which are automatically forward-preserved by the quotient;
3. separately prove the reflection properties needed to reconstruct exact semantics.

This is the coefficient analogue of safe-operation descent through a state quotient.

## 9. Precision is capability-relative

Raw quotient refinement is not a total order on semantic capability.

Moving from mod p to mod `p^2` gives more residue information, yet destroys the field/domain property needed for generic product-branch reflection.

Therefore “finer coefficient precision” is meaningful only relative to the declared observation/operation/logical language.

A structured precision profile should record not only how many residues are distinguished, but which semantic laws remain valid or reflectable after the collapse.

## 10. Prior-art boundary

Ring homomorphisms, quotient ideals, polynomial term evaluation, prime ideals and zero divisors are standard prior algebra. The Enterprise Math value is the routing distinction:

> **homomorphisms automatically preserve algebraic syntax forward; exact semantic reflection is a separate precision theorem.**