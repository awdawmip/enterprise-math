# Affine Precision Exact Sequence: IMAGE Before FIBER

Status: `RESEARCH BRIDGE / NONCANONICAL`

This note extracts one reusable architecture rule from integer reachability, critical-denominator, modular-precision, and dynamic affine model-agreement work.

## 1. Linear exact sequences

For an integer homomorphism

`A : Z^n -> Z^m`,

the relevant short exact sequences are

`0 -> ker(A) -> Z^n -> im(A) -> 0`,

`0 -> im(A) -> Z^m -> coker(A) -> 0`.

The two ends answer different questions.

- `coker(A)` asks whether a requested target is represented at all.
- `ker(A)` asks how many hidden directions remain after a represented target is fixed.

They must be queried in that order for an affine fiber.

## 2. Affine target as a cokernel class

For equation

`A x = b`,

let `[b]` be the class of b in `coker(A)`.

There are three exact integer cases.

### Reachable

`[b]=0`.

The solution set is nonempty and is one affine torsor/coset for `ker_Z(A)`.  Its free dimension is

`n-rank_Q(A)`.

### Finite torsion IMAGE obstruction

`b` lies in the rational image but not the integer image.  Then `[b]` is a finite torsion class in the saturated-image quotient.  The least positive s such that

`s b in im_Z(A)`

is the order of `[b]`.

This is the generic form of the finite denominator / critical-class order phenomenon.

### Free cokernel obstruction

`b` is outside the rational image.  Then `[b]` has a nonzero free cokernel component; no positive integer multiple of b enters the integer image.

Adding history does not repair either image obstruction.

## 3. Modular precision changes the IMAGE question

Modulo positive M, solve

`A x == b (mod M)`.

This is equivalent to

`b in im_Z(A) + M Z^m`,

or, in the cokernel,

`[b] in M coker(A)`.

Therefore a coarse modular world may admit an affine state even when the exact integer world does not.

Example:

`2x=1`

has no integer solution.  It has no solution mod 4 but does have a solution mod 3.

So modular after-state existence is not evidence of exact integer reachability.

## 4. FIBER comes only after modular solvability

If the modular target class passes the IMAGE test, all modular solutions form one affine torsor for

`ker(A mod M)`.

If the nonzero Smith factors of A are `d_1|...|d_r`, the exact number of states in that fiber is

`M^(n-r) * product_i gcd(d_i,M)`.

If the IMAGE test fails, the solution count is zero regardless of that would-be kernel size.

Sharp pair:

`2x == 1 (mod4)` -> empty fiber;

`2x == 2 (mod4)` -> two-state fiber.

The linear Smith factor is 2 in both cases.

## 5. Modular solvability region is a different lattice object from model equality

For a fixed affine equation define

`S={M>0 : A x == b (mod M) is solvable}`.

S is downward under divisibility and closed under lcm.  Equivalently it is the finite-divisor set of a supernatural modulus

`product_p p^e_p`,

with finite or infinite prime-exponent ceilings.

Example `2x=1`: S is every odd modulus.  This is not the divisor set of a finite integer.

By contrast, for two fixed integer observation maps, the modular **indistinguishability** region is normally the finite principal down-set `divisors(g)`, where g is the gcd content of their matrix difference.

Thus IMAGE solvability and MODEL equality occupy the same divisibility precision lattice but have different region geometry.

## 6. Dynamic model agreement consumes the same exact sequence

For two total-affine dynamic models, homogeneous future-difference rows have the form

`(a_i,c_i)`.

Agreement on initial state x for every future word requires

`A_inf x = -c_inf`.

The same order applies:

1. IMAGE: is `-c_inf` in the exact/modular image?
2. FIBER: if yes, what is the exact/modular kernel torsor?

Future language can refine agreement in two independent ways:

- the linear kernel can shrink;
- the affine target can leave the image, making the agreement fiber suddenly empty without any kernel-rank change.

A sharp mod-4 example goes from two agreement states to none while the linear Smith factor remains 2.

## 7. Five-layer diagnostic placement

This exact-sequence view does not replace the existing precision-state diagnostic.

- IMAGE/COKERNEL decides target existence / representation.
- FIBER decides multiplicity after existence.
- DOMAIN asks whether the operation producing the equation is legal.
- RELATION asks whether several equations/successors are admissible rather than one.
- LEDGER describes redistribution when conserved content is carried between compartments.

The declared future/coefficient language decides which of these distinctions remain observable.

The architecture rule is:

> **Do not use kernel/fiber data to answer an image-solvability question; first establish that the affine target exists in the declared coefficient precision.**

All exact-sequence, Smith/Hermite, affine torsor, cokernel, congruence and supernatural-divisibility facts used here are standard prior mathematics.  The project value is the precision-first diagnostic routing.