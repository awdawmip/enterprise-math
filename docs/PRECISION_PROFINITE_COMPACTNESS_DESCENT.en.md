# All-Moduli Compactness versus Exact Descent

Status: `RESEARCH BRIDGE / NONCANONICAL`

The profinite ghost boundary can be sharpened by separating two logical steps. For a fixed finite system of integer polynomial equations, **local solvability at every finite modulus already guarantees one compatible profinite solution**. The remaining failure is entirely the descent from the profinite completion back to the exact integer world.

## 1. Fixed polynomial system

Let

`P_1(x_1,...,x_n)=0`, ..., `P_r(x_1,...,x_n)=0`

be a finite system with integer coefficients.

For each positive modulus M define the clopen cylinder

`C_M={x_hat in Z_hat^n : P_j(x_hat)==0 mod M for every j}`.

Equivalently, `C_M` is the full inverse image in `Z_hat^n` of the solution set modulo M.

## 2. Finite intersections are controlled by lcm

For positive M,N:

`C_M intersect C_N = C_lcm(M,N)`.

More generally, for any finite family:

`intersection_i C_(M_i) = C_lcm(M_i)`.

Reason: an integer/profinite value is zero modulo every M_i exactly when it is zero modulo their lcm.

Therefore if the equation system has a solution modulo **every** positive integer, then every finite collection of the cylinders `C_M` has nonempty intersection.

## 3. Compactness creates one compatible profinite state

`Z_hat^n` is compact. The nonempty clopen sets `C_M` have the finite-intersection property, hence

`intersection_(M>=1) C_M != empty`.

But

`intersection_M C_M`

is exactly the solution set of the completed equations in `Z_hat^n`.

Thus

`for every M, there exists a solution mod M`

iff

`there exists one profinite solution x_hat`.

The reverse implication is immediate by reducing a profinite solution modulo M.

So for fixed finite polynomial systems, compatibility is not a separate obstruction after all-moduli local solvability: compactness supplies it automatically.

## 4. The real gap is profinite-to-integer descent

The exact logical chain is therefore

`all finite moduli locally solvable`

`<=>`

`profinite completion has a solution`

`=>?`

`integer world has a solution`.

Only the second implication can fail.

The intersective polynomial

`(x^2-13)(x^2-17)(x^2-221)`

shows strict failure: every modulus is solvable, hence a profinite solution exists, but there is no integer root.

## 5. Linear affine systems satisfy the second implication

For

`A x=b`,

profinite solvability implies modular solvability at every M. The integer affine local-global theorem then implies exact integer solvability.

Hence for affine lattice equations the chain collapses to equivalence throughout:

`all moduli solvable`

`<=> profinite solution`

`<=> integer solution`.

The extra equality is the route-specific profinite exactness/descent theorem.

## 6. Quantifier discipline

This clarifies three statements that should not be mixed.

### One modulus at a time

`for every M, there exists some x_M mod M`.

The witnesses may look unrelated, but for a fixed polynomial system this already implies a compatible inverse-limit state.

### One profinite state

`there exists x_hat satisfying every finite precision simultaneously`.

This is equivalent to the first statement by compactness.

### One exact integer state

`there exists x in Z^n satisfying the exact law`.

This is stronger and requires descent.

The project should therefore place the semantic boundary **between completion and exact realization**, not between separately chosen finite witnesses and completion, for fixed finite polynomial equation systems.

## 7. When the compactness step can fail to apply

The theorem uses a fixed finite equation system whose mod-M semantics are all reductions of that same law. It does not automatically apply when:

- the declared law itself changes with precision;
- different moduli use different observation/action semantics rather than reductions of one fixed predicate;
- intermediate DOMAIN/RELATION legality is dropped or changed across precisions;
- the state spaces are not organized as a compatible inverse system.

In those cases, even the first arrow needs its own compatibility theorem.

## 8. Precision interpretation

For stable modular reductions of one fixed finite integer polynomial law:

> **all finite precision worlds already determine a coherent completion-world state whenever they are all locally nonempty.**

What they do **not** determine automatically is whether that completion state belongs to the exact integer world.

Compactness, inverse limits and polynomial congruences are standard prior mathematics. The Enterprise Math value is the quantifier routing and the exact location of the descent boundary.