# Minimal Supernatural Precision Filters

Status: `RESEARCH BRIDGE / NONCANONICAL`

The supernatural completeness theorem does more than decide whether one modular experiment family is sufficient. It determines the **order geometry of all sufficient precision profiles**.

Let one affine IMAGE task have

`coker(A) ~= Z^f direct_sum T`

and finite torsion exponent

`E=product_p p^(a_p)`.

Order supernatural precision profiles by divisibility, equivalently coordinatewise p-adic depth.

## 1. Finite cokernel: one unique least exact precision

If

`f=0`,

there is no free integer direction to eliminate. Completeness is exactly

`E | Q`.

Therefore the complete precision profiles form the principal up-set

`{Q : E divides Q}`.

It has one unique least element:

`Q_min=E`.

So a finite cokernel produces a canonical least exact modular precision.

## 2. Free cokernel: completeness remains upward closed but loses its least element

If

`f>0`,

uniform completeness requires

- `E|Q`; and
- Q is infinite supernatural.

This set is still upward closed, but it is not principal and has **no least element**.

The obstruction is not that no minimal precisions exist. Rather, there are infinitely many incomparable minimal choices.

## 3. All minimal complete profiles

For every prime p, define `Q_p` by

- `v_p(Q_p)=infinity`;
- `v_q(Q_p)=a_q` for every `q!=p`.

Then `Q_p` is complete and inclusion-minimal.

Conversely, every minimal complete supernatural profile has exactly this form.

Proof sketch:

- any finite depth above a required `a_q` can be lowered;
- if two different primes have infinite depth, one can be lowered back to its finite required depth while the other still separates the free part;
- if no prime has infinite depth but infinitely many extra primes occur, finitely many of those extras can be removed and the profile remains infinite supernatural;
- therefore a minimal profile must have exactly one infinite prime depth and every other coordinate exactly at its finite torsion requirement.

Hence

`minimal complete profiles = {Q_p : p prime}`.

## 4. Distinct minimal directions have an incomplete meet

For distinct primes p and q:

`gcd(Q_p,Q_q)=E`.

If `f>0`, E is finite and therefore incomplete for the free part.

Thus the complete-profile up-set is not closed under meet once a free cokernel exists.

This gives a sharp precision-lattice phase change:

`finite cokernel -> unique least precision / principal filter`,

`free cokernel -> no least precision / infinitely many incomparable minimal unbounded directions`.

## 5. Concrete minimal experiment family

One minimal `Q_p` is realized by

`M_e=E*p^e`, `e=0,1,2,...`.

At level zero, mod E already detects every nonzero torsion class. If the target continues to pass, its torsion class is zero and any remaining obstruction is free. Increasing only one chosen p-adic depth then eventually exposes every nonzero free integer coordinate.

This is more economical in supernatural order than a generic `R^e` ladder containing several primes, because `R^e` unnecessarily drives every prime dividing R to infinite depth.

## 6. FIBER corollary

For nonzero integer observation O, the quotient controlling exact state agreement is the nonzero free group

`im(O)`.

There is no finite torsion requirement, so the minimal complete precision profiles reduce to

`p^infinity`, one for each prime p.

Therefore every single p-adic ladder

`p,p^2,p^3,...`

is a minimal complete precision axis for exact state-output equality, while the all-primes breadth profile is complete but nonminimal.

For O=0, the requirement is trivial and the least precision is 1.

## 7. Multi-task corollary

For several IMAGE/FIBER tasks, first take the coordinatewise join of their finite torsion requirements and the OR of their free-separation requirements.

If the joined free flag is false, the joint least precision is the finite lcm of the torsion exponents.

If the joined free flag is true and the joined torsion exponent is E, the joint minimal complete profiles are exactly

`E*p^infinity`, one for every prime p.

So combining tasks does not force several independent unbounded directions: one arbitrary infinite prime direction can serve the entire joined free-separation requirement.

Supernatural divisibility and primary decomposition are standard prior mathematics. The project value is the exact least/minimal precision geometry and the distinction between a canonical least finite precision and nonunique minimal unbounded precision directions.