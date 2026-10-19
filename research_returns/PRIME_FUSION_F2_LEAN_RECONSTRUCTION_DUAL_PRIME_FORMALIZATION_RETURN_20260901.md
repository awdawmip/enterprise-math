# Prime Fusion F2 — Lean Reconstruction and Dual-Prime Formalization Return

- Task: `RS-PRIME-FUSION-F2-LEAN-RECONSTRUCTION-DUAL-PRIME-FORMALIZATION`
- Publication: `TP2-7C31E9A4D5B6082F14CE`
- Researcher-ID: `EM-PFF2-2F7C91`
- Claim: `chatgpt-pff2-20260901-1015-2f7c91`
- Execution branch: `research/prime-fusion-f2-lean-t7-t8-em-pff2-2f7c91`
- Proof-bearing head: `55a74d3f29c12fa2793a4f3d26b12f06a3b73963`
- Pull request: `#1043`
- Terminal verdict: `FORMALIZED`
- Hard target: `PRIME_FUSION_T7_T8_ACCEPTED_MATHEMATICS_LEAN_FORMALIZED_NO_SORRY_WITH_PINNED_BUILD_PASS`

## Result

The Driver-accepted Prime Fusion T7/T8 mathematics has been formalized in the pinned Lean/mathlib environment without theorem weakening, `sorry`, `admit`, custom axioms, or hidden expansion into T9/T12-T15.

The implementation reuses the merged F1 proof kernel and adds only two narrow modules plus the aggregate import/axiom audit:

- `EnterpriseMath/PrimeFusion/Reconstruction.lean`
- `EnterpriseMath/PrimeFusion/DualPrime.lean`
- `EnterpriseMath/PrimeFusion.lean`

## Declaration map

### F2-L01 — T7 universal idempotent split

`idempotent_channel_split` is a source-facing wrapper over the existing F1 `idempotent_gcd_partition`. For an integral representative `e` with `H | e(e-1)`, it returns both:

- `gcd(e,H) * gcd(e-1,H) = H`;
- the two gcd factors are coprime.

No prime-power splitting framework was reproved.

### F2-L02 — T7 exact reconstruction gate

The reconstruction layer is split so theorem-critical hypotheses remain visible.

- `reconstruct_positive_channels` reconstructs positive integer coordinates from ordered channel data `c < n`, nonnegative square roots of `3n-2c` and `2c-n`, and the exact parity/divisibility gates.
- `primitive_of_reconstructed_coprime_channels` derives coordinate primitivity from coprime reconstructed channels via the existing exact `channel_gcd_exact`; primitivity is not added as an independent reconstruction assumption.
- `reconstruct_positive_primitive_channels` combines the preceding two interfaces.
- `strict_interior_gate_iff` isolates strict interiority as exactly `sv > 0 <-> n < 2c` once `sv^2 = 2c-n` and `sv >= 0`.
- `reconstruction_square_gate_necessary` and `positive_channel_orientation_necessary` retain exact theorem-level negative controls.

This leaves the diagonal positive case allowed and adds strict interiority only through the extra `V>0` gate, matching the accepted T7 boundary.

### F2-L03 — T8 dual-prime arithmetic equivalence

`DualPrimeChannels` keeps the Gaussian channel `N` first and Eisenstein channel `C` second and requires both moduli prime and distinct.

Two semiprime notions are deliberately separated:

- `SquarefreeSemiprime H`: unordered product of two distinct primes;
- `ChannelledSquarefreeSemiprime n c H`: the same arithmetic data with ordered channel labels preserved.

`dualPrime_iff_channelled_squarefree_semiprime` gives the exact channel-labelled equivalence using the existing `Hmodulus_eq_mul`, while `channelled_squarefree_semiprime_forget` exposes the unordered consequence.

`unordered_semiprime_has_both_channel_orders` is the exact label-loss negative control: the bare product admits both factor orders and therefore cannot recover the Gaussian/Eisenstein attachment.

### F2-L04 — fixed quotient / prime-field characterization

`FixedChannelPrimeFieldCertificate` records the distinct prime status of the fixed `N` and `C` channel moduli together with the fused order identity. `dualPrime_iff_fixed_channel_prime_field_certificate` supplies both directions at the fixed channel attachment.

`dualPrime_fixed_zmod_fields` materializes the canonical `Field (ZMod N)` and `Field (ZMod C)` structures from those prime channel proofs.

`dualPrime_pointedCRT_prime_field_orders` returns, together in one theorem:

- the two prime-field structures;
- the existing fixed `pointedCRT` equivalence
  `ZMod H ≃+* ZMod N × ZMod C`;
- exact carrier orders `N` and `C`.

The converse is represented by the fixed-channel certificate rather than by a bare abstract product isomorphism. This is intentional: an unordered abstract product alone does not encode which factor is the Gaussian channel and which is the Eisenstein channel.

## Pinned build and axiom audit

The exact required command passed on the PR merge ref:

`lake build --wfail -KCI EnterpriseMath`

Evidence:

- workflow run: `33462543141` (`lean` run #915);
- job: `99715572859`;
- tested merge ref: `301e59acd2a35935517cd6a35b0717c568190967`;
- base main head: `e3d15d0540a1eff65deb3334479e12c2925396f8`;
- Lean: `4.33.0-rc2` (`d8b18978322de05a8f3dba51ef03cf5461676c17`);
- mathlib: `87adeaebd370a3b6a41ac4f044fddd4bf81803ad`;
- result: `Build completed successfully (8733 jobs)`.

The aggregate module prints axioms for the new load-bearing declarations. The observed dependency set is confined to the standard repository-accepted axioms:

- `propext`
- `Classical.choice`
- `Quot.sound`

No `sorryAx` or custom axiom appeared.

A previous CI attempt failed only because two local `letI` declarations triggered a warnings-fatal style linter. They were replaced by explicit `ZMod.instField` terms; no mathematical statement was weakened or changed to obtain the successful build.

## Finite regression and negative controls

The bounded checker independently validates the algebraic interfaces on positive cells `1..64`:

- 4096 positive cells checked;
- 64 diagonal cells;
- 4032 strict-interior cells;
- 2519 cells with coprime channels, each confirming primitive coordinates;
- 228 distinct dual-prime cells in the `0..64` scan.

It also locks exact finite witnesses for:

- square-gate necessity (`n=3,c=2` gives nonsquare `U=5`);
- orientation necessity (`n=c=1` meets square/parity data but reconstructs boundary `b=0`);
- diagonal versus strict interior (`a=b=7` gives `V=0`);
- unordered-factor channel-label loss.

These computations are regression evidence only and are not used as proofs of the unbounded Lean theorems.

## Scope and residue

No T9, T12-T15, publication claim, distribution claim, performance claim, or new Prime Fusion mathematics was absorbed.

Unresolved mathematical residue within the assigned F2 T7/T8 scope: `NONE`.

Control-plane residue: Driver review and any main-branch integration remain external to this researcher execution. No Working Truth, Foundation, or canonical-promotion authority is claimed.

## Recommended next control step

Driver review should audit PR #1043 against the accepted T7/T8 source review, with particular attention to the explicit channel-labelled versus unordered T8 split. If accepted, integrate the F2 Lean layer without extending the review disposition to T9/T12-T15.
