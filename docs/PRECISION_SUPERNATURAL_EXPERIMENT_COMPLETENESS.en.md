# Supernatural LCM Completeness for Modular Precision

Status: `RESEARCH BRIDGE / NONCANONICAL`

A finite modular family, all prime moduli, and one power ladder `R,R^2,...` are not three unrelated precision mechanisms. They are three shapes of one object: the **supernatural least common multiple** of the declared modulus family.

## 1. Supernatural precision profile

Let `M_family` be any nonempty family of positive integers, finite or infinite. For every prime `p`, define

`q_p = sup_{M in M_family} v_p(M)`

with values in `N union {infinity}`.

Its supernatural lcm is

`Q = product_p p^(q_p)`.

`Q` is an ordinary finite integer exactly when only finitely many `q_p` are nonzero and every nonzero `q_p` is finite. Otherwise call `Q` **infinite supernatural**.

The family has exactly two precision resources relevant to integer affine IMAGE certification:

1. whether `Q` is infinite supernatural — this is the resource that can eliminate an unbounded free integer coordinate;
2. the depth `q_p` at each prime — this is the resource that can eliminate finite p-primary torsion.

## 2. Intersection theorem for finitely generated abelian groups

Let

`G ~= Z^f direct_sum T`

be finitely generated abelian, and write the p-primary exponent of `T` as `p^(a_p)`.

For the declared modulus family:

`intersection_{M in M_family} M G`

splits primewise.

### Free part

`intersection_M M Z = D Z`

if the supernatural lcm is the finite integer `D`, while

`intersection_M M Z = {0}`

if `Q` is infinite supernatural.

Equivalently, a nonzero integer is divisible by every declared modulus exactly when the family has a finite ordinary lcm dividing that integer.

### p-primary torsion part

On a finite p-primary group `T_p`, prime-to-p factors act invertibly, so only `v_p(M)` matters. Hence

`intersection_M M T_p = p^(q_p) T_p`,

with the conventions that the result is zero when `q_p>=a_p` or `q_p=infinity`.

Therefore

`intersection_M M G = {0}`

iff

- `f=0` **or** `Q` is infinite supernatural; and
- `q_p>=a_p` for every torsion prime `p`.

This is the complete modular-experiment resource criterion.

## 3. Exact affine IMAGE completeness

For

`A:Z^n -> Z^m`, `G=coker(A)`,

modular solvability is

`A x == b (mod M)` solvable

iff

`[b] in M G`.

Thus the experiment family decides exact reachability for **every** integer target iff

`intersection_M M coker(A) = {0}`.

Write

`coker(A) ~= Z^f direct_sum T`,

and

`E=exp(T)=product_p p^(a_p)`.

Then the exact all-target criterion is

`(f=0 or Q is infinite supernatural)`

and

`a_p<=q_p for every p|E`.

For targets already known rationally reachable, their free cokernel coordinate is zero, so only the torsion-depth condition remains.

## 4. Finite families are one special case

For a finite family,

`Q=D=lcm(M_family)`

is an ordinary finite integer. Therefore it can never separate an unrestricted free cokernel coordinate.

The all-target criterion becomes

`f=0 and E|D`.

For rationally reachable targets it becomes simply

`E|D`.

This recovers the exact finite-family theorem and explains why the number of tested moduli is irrelevant once their lcm is fixed.

## 5. All primes are another special case

For the family of every prime modulus once,

`Q = product_p p`.

This supernatural number is infinite because it has infinitely many prime factors, so the family separates every nonzero free integer coordinate.

At every prime, however,

`q_p=1`.

Therefore all prime-level tests are uniformly complete exactly when every torsion depth satisfies `a_p<=1`, i.e. exactly when the torsion exponent `E` is squarefree.

This recovers the prime-breadth / p-adic-depth theorem.

## 6. A power ladder is a third special case

For

`M_family={R,R^2,R^3,...}`

with `R>1`,

`q_p=infinity` for primes `p|R`,

and

`q_p=0` otherwise.

Its supernatural lcm is infinite, so it separates the free part. It kills the torsion part exactly when every torsion prime divides R:

`rad(E)|R`.

This is why one tailored unbounded ladder can replace the full modulus lattice for a fixed cokernel obstruction spectrum. The ladder is **not** cofinal in the entire divisibility lattice; it is separating because its supernatural precision dominates the primes/depths actually present in that cokernel.

## 7. FIBER specialization has no torsion-depth coordinate

For an integer observation map

`O:Z^n -> Z^m`,

exact state agreement is governed by

`Z^n / ker(O) ~= im(O)`.

The image is free abelian. Therefore the modular family uniformly decides exact state-output equality iff

- `O=0`, or
- its supernatural lcm `Q` is infinite.

There is no p-primary torsion-depth requirement on this FIBER quotient. This is the algebraic reason the IMAGE and FIBER precision profiles are asymmetric.

## 8. Multi-task precision joins

For several affine IMAGE tasks, each task contributes:

- one free-separation flag;
- finite required depths `a_p`.

A shared experiment family must dominate the coordinatewise join:

- free requirement = OR across tasks;
- p-depth requirement = maximum across tasks.

In supernatural terms, the least required torsion part is the supernatural/ordinary lcm of the individual torsion exponents. If every task has full row rank, this is the ordinary finite modulus

`lcm(E_1,...,E_k)`.

If any unrestricted task has a free cokernel, the shared experiment profile must additionally have an infinite supernatural lcm.

## 9. Precision interpretation

This gives one exact distinction between **finite precision**, **unbounded precision**, and **exact integer structure**.

A modular experiment family does not need to contain every modulus. It needs to dominate the obstruction spectrum relevant to the declared task:

- infinite supernatural extent if a free integer direction must be eliminated;
- sufficient p-adic depth at each finite torsion prime.

Finite modular no-go theorems arise precisely when the declared experiment profile fails one of these coordinates.

Conversely, local-global positive theorems arise when the experiment profile dominates them.

Supernatural numbers, primary decomposition, finitely generated abelian groups and profinite topology are standard prior mathematics. The Enterprise Math value is the precision-resource interpretation and the exact unification of previously separate modular experiment shapes.