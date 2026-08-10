# Profinite Exactness as a Descent Guard

Status: `FOUNDATION-FACING RESEARCH BRIDGE / NONCANONICAL`

The profinite local-global architecture needs one explicit guard against overgeneralization. For subgroup membership, modular refinement is literally a system of congruence thickenings of one exact subgroup, and closedness controls the limit. For a general world law, solving after completion can create new solutions that are not completions of exact solutions.

This is not a sixth failure location. It is a **routing condition on whether finite-precision completion may be descended back to the exact world.**

## 1. Two operations must be distinguished

For an integer law `P(x)=0`, define

`S_Z={x in Z^n:P(x)=0}`.

There are two constructions in the profinite world.

### Solve first, then complete

Take the profinite closure

`closure(S_Z) subseteq Z_hat^n`.

These points are limits of exact-world solutions.

### Complete first, then solve

Extend the law to `Z_hat^n` and form

`S_hat={x_hat in Z_hat^n:P(x_hat)=0}`.

These are solutions permitted by the completed world law.

For continuous integer laws there is a natural inclusion

`closure(S_Z) subseteq S_hat`,

but equality is an additional theorem.

## 2. Profinite exactness / descent property

The relevant positive condition is

`closure(S_Z)=S_hat`.

Call this **profinite exactness** for the declared problem.

When it holds, completion introduces no ghost solution component. In particular, if `S_Z` is empty then `S_hat` is empty.

When it fails, all finite precision layers may be mutually compatible while the corresponding inverse-limit state exists only in the completion, not in the exact integer world.

## 3. Linear affine equations satisfy the guard

For

`A x=b`,

integer solvability is lattice IMAGE membership. The affine local-global theorem gives:

- if no integer solution exists, some finite modulus already has no solution;
- if one integer solution exists, the exact solution set is an affine coset of the integer kernel and its closure is the corresponding profinite affine-kernel coset.

Thus

`closure({integer solutions})={profinite solutions}`.

The positive local-global results in the linear IMAGE/FIBER route are therefore safe.

## 4. A nonlinear ghost violates the guard

For

`F(x)=(x^2-13)(x^2-17)(x^2-221)`,

there is no integer root, so

`S_Z=empty`

and

`closure(S_Z)=empty`.

Yet there are compatible p-adic roots at every prime, hence

`S_hat!=empty`.

Therefore

`closure(S_Z) proper_subset S_hat`.

This shows why “the exact set is closed” is not enough: the exact zero set here is empty and therefore closed. The failure is that the completed solution functor is larger than the completion of exact solutions.

## 5. Correct reading of the closed/open architecture

The closed/open results remain exact for the objects to which they were proved.

### Subgroup / lattice IMAGE membership

Local modular sets are actual thickenings

`H + M Z^n`.

Then closedness of H exactly says the intersection of all finite thickenings recovers H.

### General equation classes

Local solution sets need not be thickenings of one exact solution set. New quotient solutions can appear at different primes and assemble into a profinite ghost.

Therefore one must not replace a route-specific local-global/descent theorem by the generic statement “exact solution set is closed.”

## 6. Routing checklist before exact descent

Before inferring exact existence or identity from arbitrarily refined finite precision, ask:

1. **Exact object:** what is `S_Z`?
2. **Completed object:** what finite-quotient/inverse-limit semantics defines `S_hat`?
3. **Natural map:** is `closure(S_Z) -> S_hat` known to be surjective?
4. **Descent theorem:** what structure proves equality?
5. **Ghost boundary:** if equality is not proved, what completion-only states remain admissible?

Possible positive mechanisms include:

- subgroup/lattice structure and separability;
- a valid equation-class local-global principle;
- a route-specific Hasse/descent theorem;
- an independent finite state/height bound that changes the admissible world to a finite one.

## 7. Bounded worlds do not require global profinite exactness

If the admissible exact state family is independently finite, sufficiently fine modular reduction can be injective on that finite family. Exact decisions may then be recovered from one finite quotient even if the unbounded equation class has profinite ghosts.

This is a different mechanism:

`finite admissible world -> finite injective precision`,

not

`unbounded equation class -> profinite exactness`.

## 8. Precision interpretation

The current hierarchy should therefore be read as:

`finite quotients`

`-> inverse-limit / completion semantics`

`-> [descent guard]`

`-> exact-world realization`.

The first arrow can exist without the second.

So the strongest safe statement is:

> **arbitrarily refined finite precision determines an exact world only when the declared route proves that solutions of the completed law descend from exact states.**

Profinite completion, p-adic solutions, local-global principles and failures of descent are standard prior mathematics. The Enterprise Math value is the routing distinction and the explicit prevention of a false generic inference.