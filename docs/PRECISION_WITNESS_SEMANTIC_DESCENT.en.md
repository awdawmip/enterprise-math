# Witness-Semantic Descent Across Precision

Status: `FOUNDATION-FACING RESEARCH BRIDGE / NONCANONICAL`

This note does not add a sixth failure location. It refines how RELATION, DOMAIN and precision-completion outputs may be interpreted when the exact world law carries a witness, branch label, provenance class or other hidden existential certificate.

The central rule is:

> **Before descending a finite-precision existence statement to the exact world, first descend the witness semantics; only then descend the state inside that witness.**

## 1. Numeric existence and witnessed existence are different observations

Suppose an exact world law has labelled branches

`P(x) = OR_(lambda in Lambda) P_lambda(x)`.

The unlabelled statement

`P(x) is possible`

is weaker than

`there exists one specific lambda such that P_lambda(x) holds`.

A quotient can preserve the first while erasing, merging or changing the second.

This can happen through several mechanisms already present in the research lines:

- A4 support forgets branch/path identity;
- coefficient quotients with zero divisors can mix factors;
- different prime components can choose different branch labels;
- an infinite witness alphabet can let the label escape to larger values as precision increases.

Therefore witness identity is not automatically carried by numeric precision.

## 2. Local branch reflection is a semantic quotient condition

At one precision level M define

`S_M={lambda : branch lambda is locally realizable at M}`.

An unlabelled quotient law is branch-reflecting when its local solvability implies

`S_M!=empty`.

This is a semantic property of the quotient, not merely a syntactic reduction of the equation.

For multiplicative disjunction over a domain, generic product-zero branch reflection survives a quotient `R/I` exactly when I is prime. Over integers this means prime moduli are locally safe for the generic product/disjunction law, whereas composite and nontrivial prime-power quotients are not generically safe.

The mod15 ghost witness shows local failure sharply: the product equation has a solution while none of the three labelled factors has a mod15 solution.

## 3. Local safety is not cross-precision coherence

Even if every individual precision admits a legitimate local label, those labels may differ between precision components.

For witness supports to determine one global label, the precision system must support **joint refinement**. For modular precision this means that finite sets of observations can be compared at a common multiple/lcm precision, or more abstractly that the declared precision family is finitely directed.

All positive moduli and one `R^e` ladder are directed.

The family “all prime moduli once” is not lcm-directed. Prime-local safety therefore does not by itself produce one cross-prime witness label.

## 4. Witness compactness is a separate resource

Let W be the witness space and `S_M subseteq W` the admissible witness support at precision M.

If:

- W is compact;
- every `S_M` is nonempty and closed;
- precision is finitely directed;
- supports shrink under refinement;

then the supports have the finite-intersection property and

`intersection_M S_M != empty`.

Thus one witness survives every precision.

A finite witness alphabet is the simplest special case.

An infinite discrete witness alphabet need not work. The branch family

`P_k: 0=k`, `k=1,2,...`

has local support

`S_M={k:M divides k}`.

Every precision has witnesses, supports shrink correctly, yet their total intersection is empty. The witness escapes to infinity because the witness space is noncompact.

## 5. State descent inside a fixed witness is a second guard

A coherent witness label surviving every precision still does not guarantee an exact state.

Once a label `lambda_*` is fixed, its own local state family must pass the profinite exactness/descent guard:

`closure(exact states satisfying lambda_*)`

`= completed states satisfying lambda_*`.

Affine integer branches satisfy this through the lattice local-global theorem.

General nonlinear Diophantine branches need not.

So witness coherence and state realization are two independent descent stages.

## 6. Two-stage routing

A safe route from finite-precision existence to exact witnessed existence is:

### Stage A — semantic witness descent

Check:

1. local branch reflection;
2. directed joint precision;
3. compact/finite witness space or another witness-coherence theorem.

Output:

`one fixed witness survives every precision`.

### Stage B — state descent under that witness

Check:

1. compatible local states for the fixed witness;
2. profinite exactness or another exact descent theorem for that branch law.

Output:

`one exact state carrying the witness`.

Neither stage implies the other.

## 7. Why this is not a sixth failure layer

The existing five-location architecture remains intact.

- RELATION identifies multivalued successor/witness structure.
- DOMAIN identifies legality/definedness.
- coefficient precision may affect whether a chosen algebraic encoding still represents the RELATION faithfully.
- profinite exactness controls descent from completion to exact state.

Witness descent is a **routing discipline across these layers**, not an additional ontological category.

## 8. Quotient laws must preserve semantics, not only syntax

A coefficient quotient can preserve the written polynomial expression while invalidating an implication that the exact world used to interpret it.

Example:

`fg=0 -> f=0 or g=0`

is valid over a domain but may fail after quotienting to a ring with zero divisors.

Therefore the semantic contract of a world law includes the algebraic properties used to interpret its syntax.

A safe quotient must either:

- preserve the relevant logical implication generically;
- prove it on the route-specific reachable subset; or
- retain the witness label explicitly instead of reconstructing it from collapsed coefficients.

## 9. Precision axes are not globally monotone

More numeric precision need not preserve more logical witness precision.

Along `mod p -> mod p^2`, p-adic numeric information increases, but the coefficient ring changes from a field to a ring with zero divisors. Generic product-branch faithfulness therefore decreases.

This is a concrete reason to represent precision as a structured capability profile rather than one scalar “resolution level.”

## 10. Foundation routing checklist

Before claiming

`finite-precision existence -> exact witnessed existence`,

ask:

1. What witness/branch object does the exact law require?
2. Does each quotient reflect that witness semantics locally?
3. Are the declared precisions jointly directed enough to compare local witness choices?
4. Is the witness space finite/compact or otherwise coherence-controlled?
5. Once a witness is fixed, does its state law satisfy exact descent?

Only after all required guards are established should completion-world existence be interpreted as an exact witnessed state.

Prime ideals, compactness, directed inverse systems and profinite descent are standard prior mathematics. The Enterprise Math value is the semantic routing: **first descend the witness, then descend the state.**