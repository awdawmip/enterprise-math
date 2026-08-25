# CBRC F7 Blind Input — Rank-Two Balanced Mixing Existence Gate

Status: `DRIVER_FROZEN_BLIND_INPUT`
Date: `2026-08-25`
Driver-ID: `EM-DVR-CBRC-F0-7C3A21`

This packet opens the first two-slot mixing stage on the accepted minimal rank-two Coherent-BRC working extension. It is an additive-automorphism / scalar-conservation existence and selector-status problem. It is not a ring, norm, square-law, transform, or wave task.

## 1. Epistemic boundary

The following are accepted **working-extension** facts, not native Foundation truths.

### 1.1 Elementary branch projection nondegeneracy A0

For an authorized elementary two-branch refinement of one embedded old occurrence, if both outputs are declared active old-refining branches, then both have nonzero old signed projection.

### 1.2 Free-projection zero separation

For the canonical old signed retraction `pi:C->Z e`,

`pi(z)!=0 => q(z)>0`.

### 1.3 Rank-two lower bound

Together with balanced reversible marked-scalar conservation, the preceding working axioms close torsion-free rank one at the issued scope.

No statement here promotes them to canonical Foundation truth.

## 2. Accepted F6 minimal carrier/unary class

Accepted F6 owner head:

`research/cbrc-f6-minimal-rank-two-conservative-carrier@b8887cb6059d05243bd1270dce5143c160cc534b`.

Accepted Driver review:

`driver_reviews/CBRC_F6_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_DRIVER_REVIEW_20260825.md@a36bfc4cbeab82704c3ebb17b8e93af0b7e2e4b7`.

Fix the unique least F6 additive carrier/unary class:

`C2 = Z e ⊕ Z f ⊕ <tau | 3 tau=0>`.

Old projection:

`pi(ne+mf+a tau)=n e`.

Inherited unary maps:

`R(e)=e+tau`, `R(tau)=tau`, `R(f)=f`;

`J(e)=-e`, `J(tau)=-tau`, `J(f)=f`;

`S(e)=e`, `S(tau)=-tau`, `S(f)=f`.

Relations:

`R^3=id`, `J^2=id`, `S^2=id`, `JR=RJ`, `SRS^-1=R^-1`.

Upstream relative witness remains

`e+Je=0`, while `e+JRe=-tau!=0`.

No multiplication, norm, inner product, square law, or named rank-two number system is part of `C2`.

## 3. Marked two-slot states

A pre-erasure two-alternative state is an ordered pair `(x,y) in C2 ⊕ C2`.

Marker names are presentation labels. Slot swap `P(x,y)=(y,x)` is an allowed presentation relabeling.

Orientation reversal of a reversible local operation identifies an operation with its inverse at physical-class level unless a theorem proves extra oriented data are unavoidable.

Carrier gauge is restricted to typed automorphisms of the accepted least F6 unary class. Using a complement chosen fixed by `R,J,S`, the remaining complement presentation freedom is `f->-f`; do not use torsion shifts that change the chosen unary-trivial representative as if they were invisible without proving the corresponding conjugacy.

## 4. Scalar semantics available at F7 entry

Use one fixed marked scalar `q:C2->R_nonnegative` with:

- `q(0)=0`;
- `q(e)=1`;
- unary invariance `q(Rz)=q(Jz)=q(Sz)=q(z)`;
- free-projection zero separation `pi(z)!=0 => q(z)>0`.

For a marked pair define `Q(x,y)=q(x)+q(y)`.

No homogeneity, power law, norm, polarization, inner product, convexity, monotonicity, or multiplication is assumed.

## 5. New F7 operation

F7 may introduce an additive automorphism `M in Aut(C2 ⊕ C2)` representing a reversible local two-slot mixing/refinement.

The new operational requirements are exactly:

1. **global marked conservation**: `Q(M(x,y))=Q(x,y)` for every marked pair in the declared operation domain;
2. **elementary balance**: if `M(e,0)=(u,v)`, then `q(u)=q(v)=1/2`;
3. **elementary A0**: `pi(u)!=0` and `pi(v)!=0`;
4. **genuine two-slot mixing**: the elementary input has nonzero outputs in both marked slots, and `M` is not physically equivalent to a product of independent unary slot automorphisms or such a product composed only with marker swap;
5. **reversibility**: exact inverse exists because `M` is an additive automorphism.

Do not silently impose `MP=PM`, a Hadamard relation, orthogonality, a chosen matrix shape, or commutation with every inherited unary map. If any additional covariance relation is claimed necessary, derive it from the declared semantics and state it separately.

## 6. Free quotient bookkeeping

Modulo torsion, each slot has free coordinates `(e,f)`, so the two-slot free quotient is `Z^4`.

Write the free block of `M` as `A in GL_4(Z)` in ordered basis `(e_1,f_1,e_2,f_2)`.

For the first column, corresponding to `(e,0)`, the elementary A0 condition means the `e_1` and `e_2` output coordinates are both nonzero.

This does not assume that the new `f` coordinate must participate. F7 must decide whether successful exact models can keep the new free direction dynamically spectator, whether at least one elementary `f` component is forced, or whether both possibilities occur.

## 7. F7 questions

F7 is an **existence and selector-status stage**, not yet a complete arbitrary-lift membership classification.

### Q1 — exact existence

Determine whether at least one exact pair `(M,q)` exists on `C2` satisfying all Section 5 requirements.

If none exists, prove the no-go and identify the first inconsistent assumption.

Deliver: `F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_CLASSIFIED`.

### Q2 — role of the newly forced free direction

For every successful model class found or structurally permitted, determine whether the new free direction `f` is necessarily active, optionally active, or can remain spectator. Distinguish elementary spectator, invariant spectator sector, globally spectator, and genuinely active rank-two mixing.

Deliver: `F7_NEW_FREE_DIRECTION_PARTICIPATION_CLASSIFIED`.

### Q3 — free-block structural constraints

Derive necessary structural conditions on `A in GL_4(Z)` and on its elementary first column from additivity, invertibility, A0, balance, scalar conservation, unary invariance and free-projection positivity.

Give exact sufficient families where possible. Distinguish theorem-level constraints from bounded census observations. Do not claim exhaustive arbitrary-`GL_4(Z)` membership unless actually proved.

Deliver: `F7_RANK_TWO_FREE_BLOCK_CONSTRAINTS_CLASSIFIED`.

### Q4 — scalar feasibility and underdetermination

Classify what scalar information is actually forced. Determine existence per witness family, uniqueness/nonuniqueness, exact countermodels to uniqueness, and whether periodic/support/pathological laws remain possible despite free-projection positivity.

If strict underdetermination remains, prove it by explicit physically inequivalent exact models, not parameter counting alone.

Deliver: `F7_SCALAR_AND_MIXING_SELECTOR_STATUS_CLASSIFIED`.

### Q5 — physical equivalence / minimum representatives

Use only marker relabeling, operation orientation `M<->M^-1`, and typed carrier automorphisms preserving the accepted F6 unary class and old projection.

Classify every returned witness family under this equivalence. If a minimum-complexity representative is discussed, declare the order before use and do not treat a minimizer as physically selected unless the axioms select that order.

Deliver: `F7_MIXING_PHYSICAL_EQUIVALENCE_AND_MINIMUM_STATUS_CLASSIFIED`.

## 8. Allowed final verdicts

Choose exactly one:

- `F7_NO_BALANCED_RANK_TWO_MIXING_EXISTS`;
- `F7_BALANCED_RANK_TWO_MIXING_EXISTS_UNIQUE_CLASS`;
- `F7_BALANCED_RANK_TWO_MIXING_EXISTS_FINITE_CLASSES`;
- `F7_BALANCED_RANK_TWO_MIXING_EXISTS_STRICTLY_UNDERDETERMINED`;
- `F7_EXISTENCE_PROVED_BUT_STRUCTURAL_SELECTOR_STATUS_INCOMPLETE`;
- `F7_TARGET_LEAK_INVALID`.

## 9. Firewall

Before raw freeze do not read/use historical F3/F3R/F3R2 mixing work, R063/R064/R065/FQ, downstream coherent-wave research, external quantum mechanics, complex/quadratic carriers, rings/fields/multiplication, phase groups, norms/inner products/quadratic forms/p-norms/square laws, Hadamard/Fourier/splitter targets, or any known downstream rank-two answer.

Do not identify `e,f` with real/imaginary coordinates.

## 10. Evidence expectation

A successor taskbook requires a deterministic checker verifying exact witness automorphisms, declared equivalences, A0/balance, exact finite reductions used for conservation, unary invariance, bounded `GL_4(Z)` regression, mandatory ablations, and zero theorem/model mismatch.

---

Driver freeze:

`F6 FIXES THE LEAST ADDITIVE/UNARY RANK-TWO OBJECT. F7 MAY NOW ASK WHETHER TWO-SLOT MIXING EXISTS AND WHETHER THE NEW FREE DIRECTION IS ACTUALLY USED, WITHOUT NAMING A DOWNSTREAM NUMBER SYSTEM.`
