# CBRC F3 — Balanced Reversible Mixing and Scalar Conservation — Driver Review

Status: `REWORK_REQUIRED / EXISTENCE_CHECKPOINT_ACCEPTED / HARD_TARGET_NOT_CLOSED`
Date: `2026-08-23`
Driver-ID: `EM-DVR-CBRC-F0-7C3A21`
Task-ID: `RS-CBRC-F3-BALANCED-REVERSIBLE-MIXING-CONSERVATION-FORWARD-CLASSIFICATION`
Accepted raw owner head for review: `ce10996ca7995279770cb7c51b21cc7812f358d4`
Taskbook source: `bbdc0ad66c5bde1c712f2fbd80308929cd6159e6`
Blind input source: `19ed5cfdba021cf67be0f059d8e26be1fb5af3b2`
Researcher-ID: `EM-CBRC-F3-7B31A9`

## 0. Driver verdict

The F3 raw packet contains a valid and high-value existence result, but it does **not** satisfy the issued F3 complete-classification obligations.

Primary Driver verdict:

`F3_REWORK_REQUIRED`.

Accepted checkpoint:

`CURRENT_CARRIER_BALANCED_MIXING_EXISTENCE_ESTABLISHED`.

Not accepted as closed:

`BALANCED_REVERSIBLE_MIXING_SCALAR_CONSERVATION_MINIMAL_EXTENSION_CLASSIFIED`.

No downstream comparison stage is authorized yet.

## 1. Accepted mathematical results

The Driver accepts the following at the raw owner head.

### 1.1 Exact automorphism normal form

For the current two-slot carrier, every additive endomorphism has the block form

`(n,t) -> (A n, B(n mod 3) + D t)`

with `A in M_2(Z)`, `B in M_2(F3)`, `D in M_2(F3)`, and it is an automorphism iff `A in GL_2(Z)` and `D in GL_2(F3)`.

This correctly exposes the free/torsion/cross degrees of freedom without importing a target algebra.

### 1.2 Literal marker-commutation no-go

If a free block commutes literally with marker swap, then

`A=[[u,v],[v,u]]`

and unimodularity forces a signed monomial matrix. This cannot give a strict positive two-output balanced split of `(e,0)` under M1/M2/M5/M6.

Therefore representative equality `MP=PM` is too strong for a genuine survivor.

### 1.3 Exact current-carrier survivor

The packet gives the exact free block

`A=[[2,3],[3,4]]`, `det A=-1`,

with `B=0`, `D=I`, and therefore an additive bijection on the current carrier.

The elementary input is split nontrivially:

`M(e,0)=(2e,3e)`.

The exact marker relation

`PMP = K_L M^{-1} K_R`

is verified using already accepted unary transports.

Thus the current carrier **does admit** at least one genuine additive balanced reversible mixing class satisfying the issued operational conditions.

Consequently, no carrier enlargement is required merely for F3 existence.

### 1.4 Exact scalar family for the canonical survivor

For the selected representative, the free scalar restriction is exactly six-periodic after M1/M2/M5/M6, with

`f(0)=0`, `f(±1)=1`, `f(±2)=1/2`, `f(3)=1/2` modulo six.

The packet further derives

`q_delta(n,a)=f(n)+delta * 1_{3|n and a!=0}`, `delta>=0`,

and supplies inequivalent exact choices such as `delta=0` and `delta=1`.

Thus even after genuine balanced reversible mixing plus exact marked conservation, the scalar law is not uniquely selected for this survivor.

In particular, F3 does not derive a homogeneous degree, positive form, polarization, norm, or Born-type law.

### 1.5 Relative recoalescence discriminator survives

The raw packet preserves

`e+Je=0`

and

`e+JRe=-tau != 0`.

For the two marked states `v0=(e,Je)` and `v1=(e,JRe)`, the same mixing law preserves equal marked branch scalar data while the unmarked additive aggregates remain distinct by torsion.

This is accepted as an exact two-path discriminator, not as a quantitative wave/intensity law.

### 1.6 Multiplication boundary

The derived operator relation

`M^2 - 6M - I = 0`

is accepted as an endomorphism relation on the marked two-slot module. It does not force an internal coefficient multiplication on the one-slot carrier.

### 1.7 Blindness / target leak

`TARGET_LEAK_AUDIT_PASS` is accepted. The survivor and scalar recurrence were derived without using the forbidden downstream amplitude/wave targets.

## 2. Why the F3 hard target is not closed

The issued taskbook required more than a current-carrier existence witness.

### Gap G1 — Q1 survivor classification is incomplete

F3-Q1 required:

> classify every additive automorphism of `C1⊕C1` relevant to M3–M8 up to the declared relabeling equivalence.

The return classifies the ambient automorphism group structurally, but does **not** classify the subset of free matrices `A in GL_2(Z)` (and their `(B,D)` lifts) for which some nonnegative scalar `q` satisfies M1/M2/M4/M5/M6.

The report explicitly states that the full infinite feasibility family of free matrices was not classified because one exact witness already decided the carrier-enlargement question. That is sufficient for existence, but not for the issued classification target.

### Gap G2 — Q2 is only solved for one representative

F3-Q2 required the marked scalar conservation family to be classified for **every Q1 survivor**.

The exact `q_delta` theorem is proved only for the canonical `(A=[[2,3],[3,4]], B=0, D=I)` representative and partially for its lifts.

There is no theorem showing that every other admissible physical mixing class is equivalent to this representative, nor a classification of the scalar families for inequivalent survivors.

Therefore:

`CURRENT_CARRIER_MARKED_SCALAR_CONSERVATION_CLASSIFIED`

is not yet established at the issued scope.

### Gap G3 — Q4 global scalar-law classification is incomplete

F3-Q4 required all scalar laws for every least surviving `(C,M)` family.

The current carrier is indeed the least successful carrier once one survivor exists, but `(C,M)` includes the mixing class. Since the complete minimal mixing family is not classified, the global scalar-law classification cannot yet be declared complete.

The accepted conclusion is narrower:

`BALANCED_MIXING_DOES_NOT_FORCE_UNIQUE_SCALAR_ON_AT_LEAST_ONE_EXACT_SURVIVOR`.

The stronger statement

`BALANCED_MIXING_SCALAR_LAW_CLASSIFIED`

remains open.

### Gap G4 — M4 physical-equivalence relation needs completion

The packet proves one valid noncommuting marker-choice relation for the canonical survivor and proves literal commuting is impossible for genuine balance.

But the taskbook requested classification of all target-independent choice-independence possibilities actually surviving. It is not yet proved that every admissible survivor must fall into the same inverse/conjugate pattern, nor is the full equivalence group on survivor matrices classified.

### Gap G5 — checker validates the chosen family, not the missing infinite classification

The deterministic checker is strong evidence for the canonical survivor, its scalar family, torsion lifts, composition, and ablations. Its zero mismatch count does not close G1–G4 because the missing claims are infinite/global classification statements outside the enumerated family.

## 3. Scope disposition

Accepted:

- `CURRENT_CARRIER_BALANCED_MIXING_EXISTENCE = YES`;
- `CURRENT_CARRIER_ENLARGEMENT_NEEDED_FOR_EXISTENCE = NO`;
- `LITERAL_SWAP_COMMUTATION_GENUINE_BALANCE = NO_GO`;
- `CANONICAL_BALANCED_SURVIVOR = VALID`;
- `CANONICAL_SURVIVOR_SCALAR_FAMILY = EXACT_AND_NONUNIQUE`;
- `BALANCED_MIXING_RELATIVE_RECOALESCENCE_DISCRIMINATOR = VALID_FOR_CANONICAL_SURVIVOR`;
- `TARGET_LEAK_AUDIT_PASS`.

Not accepted as closed:

- `CURRENT_OBSERVABLE_CARRIER_BALANCED_MIXING_CAPABILITY_CLASSIFIED` at full family scope;
- `CURRENT_CARRIER_MARKED_SCALAR_CONSERVATION_CLASSIFIED` at full family scope;
- `BALANCED_MIXING_SCALAR_LAW_CLASSIFIED` at full family scope;
- original F3 hard target.

## 4. Important scientific boundary

The current exact survivor is deliberately pathological from a stronger positivity/homogeneity viewpoint: for example the derived free scalar has `q(6e)=0` although `6e != 0`.

This is **not** a defect relative to the issued F3 axioms, because global strict positivity was intentionally not assumed. The Driver will not reject the survivor for failing an unstated downstream preference.

However, this pathology is a reason not to interpret the survivor as a wave intensity or positive geometry. The correct F3 checkpoint is still operational/algebraic.

## 5. Rework route

A narrow F3 completion task is required before any F4/downstream comparison.

The rework must not search for a preferred familiar target. It must complete the survivor-family classification or prove exact underdetermination/intractable infinitude under the present axioms.

The acceptable closure outcomes include:

1. all survivors are one physical equivalence family and the canonical representative is universal;
2. finitely many inequivalent families survive, each with classified scalar laws;
3. an infinite parameterized family survives and can be classified by exact invariants;
4. the current axioms are too weak to admit an honest complete minimum/mixing classification, yielding a formal underdetermination verdict.

Any of these is preferable to selecting a downstream-looking matrix.

## 6. Driver final verdict

`F3_REWORK_REQUIRED`.

`EXISTENCE_CHECKPOINT_ACCEPTED = true`.

`ORIGINAL_F3_HARD_TARGET_CLOSED = false`.

`DOWNSTREAM_COMPARISON_AUTHORIZED = false`.
