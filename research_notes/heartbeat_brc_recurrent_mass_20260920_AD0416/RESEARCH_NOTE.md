# Heartbeat World BRC: control-mass quotient and recurrent transport

Status: RESEARCH_CONSTRUCTION / LOCAL_EXACT_CHECK / NOT_FOUNDATION
Date: 2026-09-20
Parent tools: T0 BRC finite control ports + finite recurrent positive-mass calculus.

## Question

The existing control-port certificate preserves the complete positive weight–affine-effect rows. That is stronger than needed when the declared observer asks only for total positive branch mass through arbitrary recurrence depth. This note isolates the weaker exact quotient.

Let W be the finite nonnegative rational mass matrix obtained by forgetting affine effects from a ControlPacket. Let P be the raw-state-to-retained-class membership matrix. A partition is mass-lumpable when, for any two raw source states in the same class A and every target class B, the total outgoing mass into B is identical.

Then a quotient Q is well defined and

    W P = P Q.

Induction gives W^k P=P Q^k for every k. In particular, since the all-ones raw vector is P times the all-ones class vector, every finite-depth total walk mass is exactly reproduced by Q. When the positive all-depth series is finite, summing the identities gives W*P=P Q*. Conversely the same finite-depth identity shows full and quotient total-mass stability agree under the existing finite recurrent-mass criterion.

This is observer-scoped: the full affine effects inside a target class may differ.

## Strictness witness

Two control states each have a self branch of weight 1/2. One translates +e1 and the other -e1. The one-class mass quotient is Q=(1/2) and is exact for every recurrent mass depth. The effect-valued control certificate correctly rejects the same merge. Thus MASS_EQUIVALENCE is strictly weaker than EFFECT_EQUIVALENCE.

## Phase-weight obstruction

Keep identity spatial effects, but assign two otherwise merged control states self weights 1/2 and 3/2. The mass certificate rejects the merge. The first all-depth self mass is 2; the second diverges. Hence a symmetry quotient that is valid for geometry can fail for weighted recurrence solely because erased phase/environment changes branch mass.

## 64-mask D6 witness

On the existing six-channel environment masks, use a D6-equivariant positive kernel: self weight 1/5; flipping an empty bit has weight 1/80; flipping an occupied bit has weight 1/120. D6 equivariance makes target-orbit mass sums constant on every source orbit, so the 64-state kernel lumps exactly to the existing 13 D6 environment classes. Exact local computation checked W^k P=P Q^k for depths 0..8. Both raw and quotient witnesses have strict row sums below 1, giving simple stable certificates; the general stability equivalence is the theorem above, not a claim derived from these finite depth checks.

## Tool extraction

`src/enterprise_math/brc_control_mass.py` supplies:
- `control_mass_matrix`
- `certify_control_mass_partition`
- `quotient_control_mass_matrix`
- `ControlMassQuotient`

It composes existing ControlPacket semantics with the existing recurrent mass tool. No new top-level BRC family is introduced.

## Boundaries

Positive total mass only. No signed/amplitude cancellation, affine-effect equivalence, exact path provenance, within-class target identity, infinite-state recurrence or physical instability interpretation.
