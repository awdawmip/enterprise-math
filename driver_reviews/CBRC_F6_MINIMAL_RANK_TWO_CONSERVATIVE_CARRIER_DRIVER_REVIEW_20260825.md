# CBRC F6 — Minimal Rank-Two Conservative Carrier Driver Review

Status: `ACCEPTED_WITH_SCOPE_NARROWING`
Date: `2026-08-25`
Driver-ID: `EM-DVR-CBRC-F0-7C3A21`
Task-ID: `RS-CBRC-F6-MINIMAL-RANK-TWO-CONSERVATIVE-CARRIER-CLASSIFICATION`
Taskbook source: `e5d3c761e291b3193ccbbd85a4a2b05c70338141`
Accepted owner branch: `research/cbrc-f6-minimal-rank-two-conservative-carrier`
Accepted owner head: `b8887cb6059d05243bd1270dce5143c160cc534b`
Researcher-ID: `EM-CBRCF6-D694C8`

## 0. Driver verdict

`F6_ACCEPTED_WITH_SCOPE_NARROWING`.

Accepted primary verdict:

`F6_UNIQUE_MINIMAL_RANK_TWO_CARRIER_AND_UNARY_CLASS`.

Hard target:

`MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_AND_UNARY_TRANSPORT_CLASSIFIED = ACCEPTED`.

The uniqueness claim is accepted only under the target-independent lexicographic minimality order frozen in the F6 blind packet. It is not a claim that rank-two additive groups or unary lifts are globally unique without that order.

All conclusions remain in the explicit Coherent-BRC working extension; no native Foundation promotion is authorized.

## 1. Publication-liveness / firewall

PASS.

The required execution stamp was committed before mathematics and records `phase=STARTED_BEFORE_MATH`, `carrier_verdict=null`, and `math_source_read_before_stamp=false`. The owner branch was remotely verified at the stamp before the blind packet was opened.

Before raw freeze, the only mathematical source used was the frozen F6 blind packet. The source/target-leak audit excludes historical F1 counterfactuals, R063/R064/R065/FQ, downstream coherent-wave work, external quantum/wave formalisms, complex/quadratic carriers, rings, multiplication, norms, inner products, square laws, and known splitter targets.

`TARGET_LEAK_AUDIT_PASS = ACCEPTED`.

## 2. Additive carrier normal form

With the typed retraction `pi:C->Z e`, the old free summand splits:

`C = Z e ⊕ ker(pi)`.

At torsion-free rank exactly two, `ker(pi)` has free rank one, hence

`C ~= Z e ⊕ Z f ⊕ T`

with finite abelian torsion `T`. The embedded upstream order-three element `tau` lies in `T` and must retain exact order three.

Conversely every pointed finite abelian group `(T,tau)` with `ord(tau)=3` gives an allowed additive carrier. Typed isomorphism classes are exactly pointed-torsion isomorphism classes.

Under the issued order, the least torsion choice is uniquely

`T=<tau> ~= Z/3`.

Therefore the unique least additive carrier is

`C_min = Z e ⊕ Z f ⊕ <tau | 3 tau=0>`.

The explicit primitive-old-generator condition is redundant once the integer retraction `pi(e)=e` is typed.

Accepted label:

`F6_RANK_TWO_ADDITIVE_CARRIER_NORMAL_FORM_CLASSIFIED`.

## 3. Conservative-extension notions

The report correctly separates embedding only, old-signed retraction `pi:C->Z e`, and full upstream retract `r:C->C1`.

A full additive retract exists exactly when the distinguished order-three class satisfies `tau notin 3T`; equivalently there is `phi:T->Z/3` with `phi(tau)=1`. At the least carrier `T=Z/3`, a full retract exists automatically, but choosing one is extra data and is not required for the least class.

Accepted label:

`F6_CONSERVATIVE_EXTENSION_NOTIONS_CLASSIFIED`.

## 4. Inherited unary lift classification

On `C_min`, projection covariance and the frozen upstream restrictions force every lift to have

`R(f)=f+r tau`,
`J(f)=delta f+j tau`,
`S(f)=sigma f+s tau`,

with `r,j,s in Z/3` and `delta,sigma in {+1,-1}`.

The exact congruence constraints are:

`(delta-1)j=0`, `(sigma-1)s=0`, `(1+delta)r=0`, `(sigma-1)(s-r)=0`.

These yield exactly `22` raw lifts. Under typed complement gauge, the `22` solutions form exactly `6` equivalence classes. Driver independently recomputed the finite parameter set and orbit count and obtained the same `22 / 6` classification.

Modulo torsion, `R` fixes the new free direction while `J` and `S` can only act by sign. Therefore no genuine order-three unary orbit on the new free quotient is derived at F6.

Accepted label:

`F6_INHERITED_UNARY_TRANSPORT_LIFTS_CLASSIFIED`.

## 5. Minimal unary class

The six unary equivalence classes are all feasible on the same least carrier. F6 uniqueness is obtained only at the next lexicographic step: minimize additional unary structure/data.

Exactly one class admits a complement generator `f0` satisfying

`R(f0)=J(f0)=S(f0)=f0`.

Every other class carries an unavoidable sign or torsion-shear invariant under the allowed typed complement changes. Hence the unary-trivial class is uniquely least under the issued order.

Freeze:

`C_min = C1 ⊕ Z f`

with the new cyclic summand unary-trivial in the unique least F6 class.

This does **not** imply that `f` is dynamically irrelevant to future two-slot mixing; it only says inherited unary structure does not force a nontrivial action on it.

Accepted label:

`F6_MINIMAL_RANK_TWO_CARRIER_UNARY_CLASSIFIED`.

## 6. Upstream structure preservation

PASS.

The embedded relations remain exact, including `e+J e=0` and `e+J R e=-tau != 0`. No new relation collapses `e` or `tau`. No multiplication is introduced.

Accepted label:

`F6_UPSTREAM_RELATIVE_STRUCTURE_PRESERVED`.

## 7. Checker / evidence

Accepted frozen checker evidence:

- checker blob: `be8f34e8d10bd934497439d8fabd231b82480020`;
- checker SHA-256: `682c3ba50ede00bf5cad9ea948e03b8542f1d8a0ded927c2aef34664bd2e9b2a`;
- deterministic stdout SHA-256: `1cf4c992156d34f12183d7b160805c332e31b146704d3f0bea96429a8e329e7e`;
- result: `PASS`;
- theorem/model mismatches: `0`;
- raw lift cases: `22`;
- typed gauge classes: `6`;
- depth-4 unary-word checks: `2662` words / `5324` upstream generator comparisons.

## 8. Scope narrowing

F6 does not derive multiplication, a ring/field, norm, inner product, quadratic form, square law, probability law, complex/quadratic-integer interpretation, two-slot mixing, a unique scalar law, or wave/continuum structure.

The new free direction being unary-trivial must not be interpreted as a preferred real/imaginary axis, phase axis, or geometric orthogonal direction.

## 9. Successor routing

F6 closes the additive-carrier/unary stage. The next load-bearing question is whether the newly forced rank-two carrier actually supports a target-independent balanced reversible two-slot mixing with the already admitted working-extension scalar rules, and whether such mixing is unique or remains underdetermined.

The successor must first classify existence and coarse selector status, not attempt a full arbitrary torsion-lift membership theorem in one step.

Authorized next stage:

`RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION`.

Two-slot mixing is now authorized only at additive/scalar-conservation scope. Multiplication, norm, inner product, square law, complex/quadratic carrier interpretation, Hadamard/Fourier targets, and downstream wave comparison remain forbidden.

Freeze:

`F6_ACCEPTED_WITH_SCOPE_NARROWING = true`.

`F6_MINIMAL_RANK_TWO_ADDITIVE_CARRIER = Z e ⊕ Z f ⊕ Z/3 tau`.

`F6_MINIMAL_INHERITED_UNARY_ACTION_ON_NEW_FREE_SUMMAND = TRIVIAL`.

`F7_TWO_SLOT_MIXING_EXISTENCE_GATE_AUTHORIZED = true`.
