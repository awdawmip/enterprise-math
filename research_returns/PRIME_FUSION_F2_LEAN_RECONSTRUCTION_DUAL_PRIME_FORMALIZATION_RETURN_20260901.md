# Prime Fusion F2 Lean Reconstruction / Dual-Prime Formalization — Research Return

- Task: `RS-PRIME-FUSION-F2-LEAN-RECONSTRUCTION-DUAL-PRIME-FORMALIZATION`
- Publication: `TP2-7C31E9A4D5B6082F14CE`
- Researcher-ID: `EM-PFF2-B259BF`
- Claim: `chatgpt-pff2-20260901-2007-da69b9`
- Execution record: `ER-FD6539CCDE438A77D748`
- Execution branch: `formalization/prime-fusion-f2-em-pff2-b259bf`
- PR: `#1056`
- Task hard target: `PRIME_FUSION_T7_T8_ACCEPTED_MATHEMATICS_LEAN_FORMALIZED_NO_SORRY_WITH_PINNED_BUILD_PASS`
- Research verdict: **FORMALIZED / HARD TARGET MET**

## 1. Scope discipline

This execution formalized only the Driver-accepted Prime Fusion T7/T8 mathematics. It did not discover or promote new mathematics, weaken accepted statements, or absorb T9/T12–T15. The proof layer reuses the integrated F1 kernel (`Channels`, `ArithmeticSplit`, `PointedQuotient`, `PointedRecovery`) and preserves the fixed Gaussian/Eisenstein channel attachment.

## 2. F2-L01 — universal idempotent split

Implemented in `EnterpriseMath/PrimeFusion/Reconstruction.lean`:

- `idempotent_universal_channel_split`
  - from `(H : ℤ) ∣ e*(e-1)` obtains
    `gcd(e,H) * gcd(e-1,H) = H` and coprimality of the two gcd factors;
  - directly packages the already-proved F1 `idempotent_gcd_partition` theorem.
- `channels_isCoprime_implies_primitive`
  - uses the exact F1 channel gcd identity
    `gcd(N(a,b),C(a,b)) = gcd(a,b)^2`;
  - therefore channel coprimality forces `gcd(a,b)=1`, so primitivity is derived rather than postulated.

## 3. F2-L02 — exact positive / primitive reconstruction

Implemented:

- `positive_cell_channel_orientation`
  - proves the exact positive-cell orientation `C(a,b) < N(a,b)` from `a>0,b>0`.
- `reconstruction_square_gate_necessary`
  - exposes the necessary diagonal square identities
    `U² = 3N-2C`, `V² = 2C-N` using the existing diagonal coordinates `u,v`.
- Negative controls:
  - `no_reconstruction_if_U_not_square`;
  - `no_positive_reconstruction_if_not_oriented`.
- `reconstruct_positive_cell_of_diagonal_roots`
  - hypotheses: `C<N`, integral roots `U²=3N-2C`, `V²=2C-N`, `U>0`, `V≥0`;
  - derives `U²+V²=2N`;
  - **derives root parity automatically** via `Int.even_add` and `Int.even_pow'`; parity is not an extra reconstruction assumption;
  - constructs the half-sum / half-difference coordinates and proves positivity plus exact recovery of `N` and `C`.
- `reconstruct_positive_primitive_cell_of_diagonal_roots`
  - adds only channel coprimality and derives a primitive reconstructed cell through the exact channel-gcd theorem.
- `reconstructed_strict_interior_gate`
  - isolates the strict ordering gate exactly as `0 < v(a,b) ↔ b<a`; the positive diagonal `V=0` is therefore not silently excluded from the non-strict positive reconstruction theorem.

This closes the T7 reconstruction direction without adding a parity axiom and without assuming cell primitivity independently of the channel data.

## 4. F2-L03 — dual-prime iff square-free semiprime

Implemented in `EnterpriseMath/PrimeFusion/DualPrime.lean`:

- `SquarefreeSemiprime h := ∃ p q, p.Prime ∧ q.Prime ∧ p≠q ∧ h=p*q`.
- `dualPrime_iff_squarefreeSemiprime_mul`
  - for fixed nontrivial distinct factors `n,c`, proves
    `(n.Prime ∧ c.Prime) ↔ SquarefreeSemiprime (n*c)`;
  - the reverse direction is proved exactly using prime divisibility of a product plus cancellation; no extra coprimality assumption is inserted.
- `fixed_channels_dualPrime_iff_squarefreeSemiprime`
  - specializes the characterization to the fixed Prime Fusion channel moduli using `Hmodulus_eq_mul`.

## 5. F2-L04 — fixed channel-labelled finite-field / quotient characterization

Implemented:

- `FixedChannelPrimeFieldPair a b`
  - explicitly retains the labels `Nmodulus` = Gaussian channel and `Cmodulus` = Eisenstein channel and requires them to be distinct primes.
- `gaussianChannelField`, `eisensteinChannelField`
  - canonical prime-field structures on the two fixed `ZMod` carriers; declarations are marked `@[instance_reducible]` to remain warnings-fatal clean.
- `fixed_channel_prime_fields_and_orders`
  - proves existence of both fixed field structures and their exact cardinalities.
- `fixed_channel_prime_field_product`
  - for a primitive cell, combines the fixed prime-field carriers with the pre-existing labelled `pointedCRT` equivalence:
    `ZMod H ≃+* ZMod N × ZMod C`;
  - this is deliberately stronger than an abstract unordered product statement because the Gaussian/Eisenstein attachment is preserved in the codomain order.
- `fixedChannelPrimeFieldPair_iff_dualPrime`
  - records the exact converse bridge between the labelled prime-field predicate and dual primality once channel distinctness is fixed.

## 6. F2-L05 — integration, negative controls, no proof escapes

Integration:

- `EnterpriseMath/PrimeFusion.lean` now imports `Reconstruction` and `DualPrime`.
- It extends the explicit `#print axioms` surface to the principal F2 theorems.
- Deterministic static guard added at:
  `research_checks/PRIME_FUSION_F2_LEAN_RECONSTRUCTION_DUAL_PRIME_FORMALIZATION_CHECK_20260901.py`.
  It verifies the expected theorem surface and rejects `sorry`, `admit`, explicit `axiom`, or `unsafe` declarations in the two new F2 Lean modules.

## 7. Pinned machine-check evidence

Authoritative successful build:

- GitHub Actions workflow: `lean`
- Run: `33507904681`
- Job: `99856269515`
- Tested execution head: `a7b70104091029cc20149f05c886893f000d1ba2`
- PR merge ref: `8ac16f53c62f4789ad836fac363035ce182e83ac`
- Integrated base in that merge ref: `665ab87c4b5215e0af83d419da391d5f9a2810e5`
- Toolchain: `leanprover/lean4:v4.33.0-rc2`
- Lean commit reported by runner: `d8b18978322de05a8f3dba51ef03cf5461676c17`
- mathlib revision: `87adeaebd370a3b6a41ac4f044fddd4bf81803ad`
- Command: `lake build --wfail -KCI EnterpriseMath`
- Result: **PASS — `Build completed successfully (8733 jobs).`**

The warnings-fatal build compiled both new modules:

- `EnterpriseMath.PrimeFusion.Reconstruction` — PASS
- `EnterpriseMath.PrimeFusion.DualPrime` — PASS
- top-level `EnterpriseMath` — PASS

The explicit F2 `#print axioms` output contains only the repository-accepted standard Lean axioms among `propext`, `Classical.choice`, and `Quot.sound`; no custom axiom appears. Because the build is warnings-fatal, a `sorry`/`admit` proof escape would also fail the target build rather than pass silently.

## 8. Non-task CI failures isolated

The PR's repository-wide `reference-integrity` / `quality` failures are upstream control-plane failures unrelated to the F2 Lean changes. Two observed examples were:

1. existing P000 result/review binding and method/status integrity drift in the merged base; and
2. a later control bootstrap failure for
   `RS-DECORATED-CARRIER-MINIMAL-AUGMENTATION-ATOM-TRANSPORT`, where the quarantine expected active publication head `TP2-DCE2A9D900EF145F0E77` but the merged base exposed `TP2-1C9E7635984115B9DEF1`.

These failures occur before F2-specific Python testing and do not invalidate the task's explicit pinned Lean hard gate, which passed on the PR merge ref against the contemporaneous `main` base.

## 9. Residue and next control-plane action

Mathematical / formalization residue for this task: **NONE**.

The task is ready for Driver review. Driver should verify statement fidelity and fixed-channel attachment on PR #1056, then either accept the frozen result or return a concrete theorem-level correction. No further researcher execution is required unless Driver explicitly reopens the task.
