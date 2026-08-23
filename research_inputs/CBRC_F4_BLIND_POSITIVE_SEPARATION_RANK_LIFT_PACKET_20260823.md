# CBRC F4 Blind Input — Positive Separation / Rank-Lift Gate

Status: `DRIVER_FROZEN_BLIND_INPUT`
Date: `2026-08-23`
Driver-ID: `EM-DVR-CBRC-F0-7C3A21`

This packet is the only mathematical input for the intended F4 Phase A task.

Do not infer or import any downstream wave/quantum target from the notation below.

## 1. Accepted coefficient semantics

The currently accepted coefficient carrier is

`C1 = Z e ⊕ <tau | 3 tau = 0>`.

Write coefficients as `(n,a)` with `n in Z`, `a in Z/3`.

Accepted unary additive automorphisms include

`R(n,a)=(n,a+n)`,

`J(n,a)=(-n,-a)`,

`S(n,a)=(n,-a)`.

The old signed layer is the embedded copy `Z e`.

## 2. Accepted two-slot mixing semantics

A marked two-slot state is `(x,y)` in `C ⊕ C` before marker erasure.

A candidate local mixing is an additive bijection

`M:C⊕C -> C⊕C`.

A marked scalar is a fixed function

`q:C -> R_nonnegative`

with marked total

`Q(x,y)=q(x)+q(y)`.

Accepted operational requirements inherited for this gate are:

- `q(0)=0`, `q(e)=1`;
- invariance under accepted absolute unary transports;
- `M` is reversible and genuinely mixes the two marked slots;
- marker names do not change the physical operation class;
- `M(e,0)=(a,b)` has both outputs nonzero and balanced scalar values;
- exact marked conservation `Q(Mv)=Q(v)` and likewise for the inverse;
- composition/refinement uses one fixed scalar law and one reversible local operation class;
- old signed cancellation remains available.

No norm, power law, inner product, multiplication, continuum interpretation, or probability law is accepted.

## 3. Accepted current-carrier membership theorem

For `C1`, every two-slot additive automorphism has a free block

`A=[[a,b],[c,d]] in GL_2(Z)`

plus finite torsion/cross data.

A balanced scalar-conserving survivor exists exactly when

`g=gcd(|a|,|d|)>1`

and

`h=gcd(|b|,|c|)>1`.

Torsion/cross data do not enlarge the operator membership set.

## 4. Accepted torsion-min / forced-period fact

For any admissible scalar on any surviving current-carrier operator, define

`f(n)=min_{t in Z/3} q(n,t)`.

Then `f` is a nonnegative even normalized free scalar satisfying the exact free conservation problem.

For a survivor with the above `g,h`, every such `f` is forced to be periodic with period dividing `g*h`.

In particular,

`f(g*h)=f(0)=0`

while `g*h != 0`.

This periodicity is a theorem derived from conservation; it is not a chosen scalar ansatz.

## 5. Accepted underdetermination boundary

Without any extra regularity axiom, there are infinitely many physically inequivalent balanced mixing/scalar models.

No existing accepted rule selects one of them.

The candidate below is **not** accepted Foundation truth. F4 must classify its consequences and necessity status only.

## 6. New candidate regularity for F4

`GLOBAL_ZERO_SEPARATION`:

> every nonzero coefficient state has strictly positive marked scalar:
>
> `z != 0 => q(z)>0`.

This is stronger than the previously accepted one-way statement `q(0)=0`.

F4 must not assume it is true in nature or in Foundation. It is a candidate selector whose mathematical consequences must be classified.

## 7. Rank-one extension class to test

F4 may consider a general finitely generated additive conservative extension `C` of the old signed generator with torsion-free rank exactly one and an additive retraction back to the old free signed coordinate.

Equivalently, after choosing the embedded primitive free generator, the additive carrier has the form

`C ~= Z e ⊕ T`

for some finite abelian group `T`.

Do not assume `T=Z/3`; classify arbitrary finite `T` if needed.

A two-slot additive automorphism induces some free quotient block `A in GL_2(Z)` and a bijective finite affine action on the torsion labels over each fixed free input.

## 8. Required F4 question

Determine whether `GLOBAL_ZERO_SEPARATION` can coexist with all inherited balanced reversible mixing/conservation requirements on any torsion-free-rank-one conservative finitely generated carrier.

If no, prove the no-go uniformly for arbitrary finite `T`, and state the exact lower bound on torsion-free rank required by any future successful extension.

If yes, exhibit and classify the least exact counterexample.

## 9. Firewall

Before raw freeze, do not read/use:

- full F0/F1/F2/F3/F3R/F3R2 reports beyond facts explicitly frozen here;
- R063/R064/R065/FQ mathematics;
- downstream coherent-BRC/wave free research;
- external quantum mechanics, quantum walks, Hilbert spaces, Born rules, path integrals, wave equations;
- any preselected complex/quadratic integer carrier, finite phase group, norm, inner product, square law, or known splitter.

The task is a pure no-go/rank-lower-bound classification.
