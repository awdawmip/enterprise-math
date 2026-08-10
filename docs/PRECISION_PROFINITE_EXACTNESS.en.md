# Profinite Exactness: When Completion and Solving Commute

Status: `RESEARCH BRIDGE / NONCANONICAL`

A subtle correction is required when interpreting local-global precision through topology. **Closedness of the exact integer solution set by itself is not enough.**

The relevant question is whether two operations commute:

1. solve the world law over the exact integer world, then complete the resulting solution set;
2. first extend the world law to the profinite completion, then solve it there.

These can differ.

## 1. Two solution constructions

For an integer law or predicate `P(x)=0`, write

`S_Z={x in Z^n : P(x)=0}`

for exact integer solutions.

Its profinite closure is

`closure(S_Z) in Z_hat^n`.

Separately, extend the same integer formula continuously/coefficientwise to the profinite completion and define

`S_hat={x_hat in Z_hat^n : P(x_hat)=0}`.

Always

`closure(S_Z) subseteq S_hat`

for polynomial/continuous integer laws, because exact solutions remain solutions after completion.

The important question is whether equality holds.

## 2. Profinite exactness

Call the declared equation class **profinite-exact** for the given problem when

`closure(S_Z)=S_hat`.

Then every compatible inverse-limit solution is approximated by exact integer solutions in the relevant sense; the completion has not manufactured a new solution component invisible in the exact world.

For a zero-dimensional exact existence question, if `S_Z` is empty, profinite exactness forces `S_hat` empty as well.

This is the descent property needed to infer exact realizability from complete finite-precision coherence.

## 3. Affine integer equations are profinite-exact

For

`A x=b`,

if an integer solution exists, the exact solution set is an affine coset of `ker_Z(A)`. Its closure is the corresponding affine coset of the profinite kernel.

If no integer solution exists, the affine IMAGE local-global theorem supplies a finite modulus at which solvability already fails. Hence there is no profinite solution either.

Thus

`closure({x in Z^n:A x=b})`

`= {x_hat in Z_hat^n:A x_hat=b}`.

This is stronger and more precise than merely saying that the exact solution set is closed.

## 4. The intersective polynomial is not profinite-exact

For

`F(x)=(x^2-13)(x^2-17)(x^2-221)`,

`S_Z=empty`.

Therefore

`closure(S_Z)=empty`.

But prime-by-prime p-adic roots produce

`S_hat != empty`.

Hence

`closure(S_Z) proper_subset S_hat`.

The profinite completion contains genuine solutions of the completed equation that do not descend from any exact integer solution.

This is the exact algebraic meaning of a **profinite ghost state**.

## 5. Why modular satisfiability is not always a neighborhood thickening

For linear target membership, modular solvability of b is exactly

`b in im_Z(A)+M Z^m`,

which is a congruence thickening of one fixed exact lattice image. Taking all M therefore recovers the closed lattice.

For a nonlinear polynomial, the set

`{x mod M : F(x)==0 mod M}`

need not be the reduction or neighborhood thickening of the exact integer zero set. New finite-quotient roots can appear independently at different primes and assemble into a profinite solution component with no exact integer ancestor.

Therefore the slogan

`exact set is closed -> local-global descent`

is false in this generality.

What is needed is the stronger compatibility

`local/profinite solution functor = completion of exact solutions`,

or another theorem implying the same descent conclusion.

## 6. Foundation routing rule

When a route proposes to infer exact existence from arbitrarily refined finite precision, ask in this order:

1. What is the exact-state solution object `S_Z`?
2. What is the completed/local solution object `S_hat` induced by the finite quotients?
3. Is the natural inclusion

   `closure(S_Z) -> S_hat`

   an equality for this equation class?
4. If not, what additional axiom, bound or world law excludes the ghost components?

Linear lattice IMAGE has a positive answer. General nonlinear Diophantine predicates do not.

## 7. Bounded admissible worlds

An independent finite state bound can restore descent for a different reason. The admissible exact state set is then finite, so sufficiently fine modular reduction can be injective on that set. The finite quotient is no longer being asked to distinguish among unbounded integer lifts.

This is a bounded-world certificate, not a proof that the unbounded equation class is profinite-exact.

## 8. Prior-art boundary

Profinite completion, p-adic solution sets, integral points, local-global principles and failures of descent are standard prior mathematics. The Enterprise Math contribution is the precision-routing distinction:

> **completion of exact solutions and solutions of the completed world law are different constructions; exact finite-precision descent requires them to coincide, not merely the closedness of the exact set.**