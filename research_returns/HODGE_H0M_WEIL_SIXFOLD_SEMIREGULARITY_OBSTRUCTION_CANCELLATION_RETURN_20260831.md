# HODGE H0M — Weil sixfold frontier return

Task: `RS-HODGE-H0M-WEIL-SIXFOLD-SEMIREGULARITY-OBSTRUCTION-CANCELLATION`  
Publication: `TP2-4D8C1A7E2B609F35C614`  
Researcher-ID: `EM-DIRECT-6A4F21`  
Claim: `chatgpt-20260917-A-6A4F21-h0m-02`

## Frozen result

**Classification:** `EXACT_HARD_BLOCK_WITH_MISSING_OBJECT_AND_UNBLOCK_CONDITION`.

This run does not prove algebraicity of the selected open Weil class and does not assert a new case of the Hodge conjecture. It establishes prerequisite A on a fixed open-frontier model, proves an exact discriminant-transport no-go for the audited carrier-preserving operations, and identifies the first missing algebraic object needed before an obstruction-cancellation mechanism can even be instantiated.

## 1. Current frontier and model

The literature gate was rerun from primary arXiv sources through 2026-09-17. Markman's `arXiv:2502.03415` proves the sixfold theorem at discriminant `-1`; Mostaed `arXiv:2603.20268` states that outside this locus the sixfold Weil-class Hodge conjecture remains open and isolates absent K-secant structure and uncontrolled discriminant as independent obstructions. Markman's broader `arXiv:2509.23079` remains conditional on semiregularity, and the July 2026 `arXiv:2607.18341` concerns abelian fourfolds. The bounded fresh search found no later primary arXiv result closing the model selected below.

Freeze:
- `K = Q(i)`.
- `V = K^6`, `Lambda = Z[i]^6`.
- Hermitian form `H = diag(1,1,1,-1,-1,-3)`, signature `(3,3)`.
- Discriminant `det H = -3` in `Q^*/N(K^*)`.
- Frontier abelian sixfold `A_eta` is the geometric-generic member of the level-3 PEL unitary component attached to this datum, fixed before cycle search.

The ratio between target and Markman solved discriminants is `3`. It is not a norm from `Q(i)`: every rational norm has even valuation at primes `p == 3 (mod 4)`, whereas `v_3(3)=1`. Hence `[-3] != [-1]`.

## 2. Exact rational Hodge carrier

Let `W_K(A_eta) = wedge_K^6 H^1(A_eta,Q)`.

1. `H^1(A_eta,Q)` has K-rank 6.
2. Its sixth K-exterior power has K-rank 1.
3. Since `[K:Q]=2`, `dim_Q W_K(A_eta)=2`.
4. After tensoring with C, the two K-embedding determinant lines each contain three `(1,0)` and three `(0,1)` factors by the Weil signature `(3,3)`. Both lines therefore have type `(3,3)`.

Thus prerequisite A is established at the exact carrier level. The generic model has cyclic Neron-Severi group; the exceptional 2-dimensional Weil carrier is not replaced by the single divisor-generated `theta^3` line.

## 3. BRC audit

Resolution: `REUSE_APPLIED`.

The relevant BRC use is provenance/observer discipline, not positive-mass obstruction cancellation. The branch state retains `(M1–M4 mechanism, source provenance, discriminant class, carrier map)` and observes exact discriminant, source-object existence, defined obstruction status, and exact `W_K` class equality. No branch is compressed to a Boolean success/failure before its defect is recorded.

The Foundation signed boundary is decisive: positive Weighted-BRC does not represent signed/complex Ext obstruction cancellation. Consequently no artificial positive branching model is introduced for `Ext^2` cancellation.

## 4. M1 defect

The known secant-sheaf source geometry produces the solved discriminant-`-1` Weil datum. On the fixed `[-3]` component there is no audited frontier sheaf/object `E` whose characteristic class has a certified nonzero `W_K` component. Without such an object, `Ext^1(E,E)`, `Ext^2(E,E)`, and semiregularity maps are not available objects to compute.

The missing object is therefore explicit, not a slogan:
`frontier E or codimension-3 Z with a certified nonzero/spanning W_K(A_eta) class`.

## 5. M2 obstruction-cancellation

Status: `BLOCKED_BEFORE_EXT2`.

No obstruction matrix or cancellation table is fabricated. Standard semiregularity remains in the source baseline; even a successful standard semiregularity calculation would not by itself earn Enterprise attribution.

Smallest unblock step: construct a frontier `E` (or `Z`) first, then calculate its `Ext^2` carrier and semiregularity/trace map.

## 6. M3 exact transport no-go

For a K-linear change of basis/similitude,
`det(g^* H g) = N(det g) det(H)`.
For rational scaling in K-rank 6,
`det(cH)=c^6 det(H)=N(c^3) det(H)`.
For duality,
`det(H^{-1})=det(H)^{-1}`, and the inverse is the same class in `Q^*/N(K^*)` because every rational square is a K-norm.

Therefore:
- K-linear polarized isogenies/similitudes preserve the discriminant class;
- Hecke moves inside the fixed unitary datum preserve it;
- deformation inside the fixed PEL component preserves it;
- duality preserves its quotient class;
- a K-equivariant Fourier–Mukai route that genuinely identifies the H^1 Weil carrier is subject to the same similitude invariant.

Since `[-1] != [-3]`, these audited carrier-preserving operations cannot transport the solved source to the target. A general Fourier–Mukai equivalence lacking a certified K-linear H^1 identification is rejected at the carrier-identification gate rather than treated as a hidden jump.

This is `DISCRIMINANT_TRANSPORT_NO_GO_WITHIN_AUDITED_CARRIER_PRESERVING_OPERATIONS`, not a claim about every conceivable algebraic correspondence.

## 7. M4 class-first lift

No codimension-3 frontier cycle was constructed. No solved-locus cycle constants were imported. Hodge/absolute-Hodge/Mumford-Tate status was not promoted to algebraicity.

Rational scaling is verified only conditionally: if cycles `Z1,Z2` with classes forming a Q-basis of `W_K` were constructed, any negative or denominator-bearing rational input would lift by the Q-cycle `a Z1+b Z2`. The basis itself remains missing.

## 8. Controls

- C1 solved `[-1]`: used only as a positive mechanism control.
- C2 divisor algebra: generic rank-one divisor algebra cannot replace the exceptional two-dimensional Weil carrier.
- C3 transport: exact discriminant transformation laws above give the no-go.
- C4 semiregularity null: without a frontier `E`, the semiregularity channel is undefined, not automatically cancelled.
- C5 rational scaling: conditional linearity recorded; no false cycle basis asserted.

## 9. Verification and unresolved residue

The deterministic checker validates:
- exact model freeze and `det H=-3`;
- norm-class separation `[-3] != [-1]`;
- `dim_Q W_K=2`;
- `(3,3)` typing from the `(3,3)` Weil signature;
- the algebraic discriminant formulas used in M3;
- absence of a claimed frontier cycle;
- BRC signed-boundary handling and the hard-block classification.

No `sorry`, `admit`, custom axiom, or unproved algebraicity assertion is used.

**Unresolved residue:** construct an algebraic/derived object on the fixed `[-3]` frontier model with an exact nonzero `W_K` characteristic/cycle class, or construct a carrier-preserving algebraic correspondence that actually changes the norm-class discriminant. Until then M2 cannot begin and M4 cannot pass.
