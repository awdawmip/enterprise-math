# P018 Ternary Carry Threshold-to-Cardinality — Final Research Return

Status: `FINAL_FROZEN / EXACT_TERNARY_THRESHOLD_TO_CARDINALITY_PROVED_AND_LEAN_CHECKED / HARD_TARGET_ACHIEVED`

Date: `2026-08-27`

Researcher-ID: `EM-P018TC-E9AA2D`

Task: `RS-P018-TERNARY-CARRY`

Publication: `TP2-674C46ECF01DD1D3E6F4`

Claim: `chatgpt-p018tc-20260827-1131`

Execution record: `ER-21C68CC5C36A48DA17A9`

Execution branch: `research/p018-ternary-carry-replay-em-p018tc-e9aa2d`

Execution base: `9b5ec8d1190bf14f00309df421e51734c36b2f24`

Stacked review PR: `#690` over `research/p018-ternary-atlas-cardinality`

## 1. Final verdict

Freeze:

`PRIMARY_VERDICT = EXACT_TERNARY_THRESHOLD_TO_CARDINALITY_PROVED_AND_LEAN_CHECKED`.

`HARD_TARGET_DISPOSITION = ACHIEVED`.

`P018_TERNARY_THRESHOLD_TO_CARDINALITY_EXACT_AND_LEAN_CHECKED_NO_SORRY = true`.

`UNRESOLVED_RESIDUE = NONE`.

The legacy P018 HANDOFF has been migrated into the current immutable-publication runtime and closed at the exact finite-atlas/cardinality level. The difficult local quotient-root arithmetic already present on Draft PR #328 now composes into a finite-set decomposition and then into the existing ternary carry theorem without adding a new arithmetic hypothesis.

## 2. Exact finite atlas

For `s,n : Nat`, define the positive quotient-root atlas

`quotientRootStates s n`

as the image of physical denominators `d=1,...,n`:

`{ root (s+1) (n/d) : 1 <= d <= n }`.

In Lean this is represented by the zero-based denominator index:

```lean
def quotientRootStates (s n : ℕ) : Finset ℕ :=
  (Finset.range n).image (fun i : ℕ => root (s + 1) (n / (i + 1)))
```

Let

`H = root (s+2) ((s+1)*n - 1)`

and

`D = n / (H+1)^(s+1)`.

The completed atlas split is:

1. the high-denominator image from `d=1,...,D`;
2. every positive low root `1,...,H-1`;
3. the horizon root `H` exactly when the carry threshold
   `(D+1)*H^(s+1) <= n`
   holds.

For positive `H`, the high image and low chart are disjoint.

## 3. Exact high branch

The current #328 arithmetic layer proves:

- every `1 <= d <= D` produces a quotient-root strictly above `H`;
- two distinct denominators in that interval cannot collide.

Therefore the finite high image has exactly

`D`

states.

The formal theorem is:

`root_state_high_states_card`.

## 4. Exact low branch

For every positive `t < H`, an explicit nonempty denominator fiber is produced. The stable proof route uses the pure natural-number tangent/floor-gap kernel harvested from the independent historical P018 binary-atlas branch:

`floor_quotient_strict_gap_of_tangent`.

With

`A=t^(s+1)`,
`B=(t+1)^(s+1)`,
`u=t^s`,

the Bernoulli/tangent lower bound and the horizon inequality imply

`n/B < n/A`.

Hence

`d=n/B+1`

lies in the exact quotient-root fiber of `t`.

The horizon state is separately characterized exactly:

`H` is realized by some `1 <= d <= n`

iff

`0 < H` and `(D+1)*H^(s+1) <= n`.

Thus the low chart has

`H-1 + kappa`

states, where

`kappa = 1` if the horizon threshold holds and `0` otherwise.

## 5. Exact binary cardinality

The disjoint high/low decomposition gives the exact subtraction-free binary count

`|quotientRootStates(s,n)| + 1 = D + H + kappa`,

with

`kappa = if (D+1)*H^(s+1) <= n then 1 else 0`.

The formal theorem is:

`quotientRootStates_binary_cardinality`.

This is the threshold-to-cardinality bridge that the legacy P018 HANDOFF had not yet frozen in its current #328 lineage.

## 6. Exact ternary threshold theorem

Define

`q = H/(s+1)`,
`X = (H+1)^(s+1)`,
`Y = H^(s+1)`,

and

`A = max(q*X, (q+1)*Y)`,
`B = (q+1)*X`.

Let

`tau = 0` if `n < A`,
`tau = 1` if `A <= n < B`,
`tau = 2` if `B <= n`.

The already-proved denominator three-point band and forced lower/upper carry lemmas supply the hypotheses of `ternary_count_from_binary_carry`. Feeding the exact binary atlas count into that theorem yields

`|quotientRootStates(s,n)| + 1 = H + q + tau`.

The formal theorem is:

`quotientRootStates_ternary_cardinality`.

No new analytic, asymptotic, prime, geometric, or physical premise occurs in this specialization.

## 7. Internal method harvest provenance

During the replay, an independent same-task historical proof asset was found on:

`research/p018-binary-root-atlas-lean@9fa0a84b4fff7f5140bc6cf96779a774c891ebcb`

(Draft PR #246).

That branch had already discovered the correct finite-atlas proof architecture: high-image injectivity, forced low interval, optional horizon state, disjoint union, and binary cardinality. It was never treated as canonical truth. The current execution harvested the architecture and re-established it on top of the stronger current #328 lemma layer.

Provenance classification:

`INTERNAL_PRIOR_RESEARCH_METHOD_HARVEST / SAME_TASK_LINEAGE / NONBLIND_DISCLOSED`.

The exact load-bearing arithmetic hypotheses in the final theorem come from the current execution lineage, not from assuming the historical branch conclusion.

## 8. Lean validation

Final warning-fatal validation:

- workflow: `lean`
- run number: `888`
- run id: `33038025114`
- job id: `98405044303`
- command: `lake build --wfail -KCI EnterpriseMath`
- Lean: `4.33.0-rc2`
- mathlib revision: `87adeaebd370a3b6a41ac4f044fddd4bf81803ad`
- compiled theorem file blob: `e46d6037257d4f330d6cd46459beb0bc1a11ba5d`
- compiled execution commit: `5ab06db341bc4e579a8e86ca5d14f39c3a1f5e2a`
- conclusion: `SUCCESS`.

The preceding warning-fatal run exposed proof-plumbing errors and one linter warning; these were repaired without weakening the theorem. The final run completed the warning-fatal compile successfully.

PR patch audit found no occurrences of:

- `sorry`;
- `admit`;
- custom `axiom`.

Therefore the hard formalization condition is satisfied.

## 9. Finite regression

The exact regression script

`scripts/check_p018_ternary_carry.py`

checks both

`|S|+1 = D+H+kappa`

and

`D+H+kappa = H+q+tau`

for

- `s = 0,...,7`;
- `n = 1,...,2499`.

Total exact cases:

`19,992`.

Failures:

`0`.

This is explicitly `FINITE_REGRESSION_ONLY_NOT_A_PROOF`; the general proof is the Lean theorem above.

## 10. Anti-overclaim boundary

This result closes the P018 quotient-root threshold-to-cardinality layer only.

It does not:

- claim that the old legacy scheduler state was itself current canonical control state;
- promote the historical PR #246 branch;
- introduce new Foundation semantics;
- claim a prime theorem or asymptotic statement;
- grant automatic integration into `main`.

The immutable research result is returned for separate Driver review.

## 11. Recommended control-plane disposition

Driver should review the exact formal closure. If accepted:

1. integrate this replay result into the P018 owner lineage, preserving the historical-method provenance;
2. resolve the older Draft PR #328 / legacy HANDOFF as superseded by the immutable current result or merge-equivalent evidence;
3. mark the P018 ternary threshold-to-cardinality frontier closed;
4. open no successor merely to extend finite scans.

No theorem-critical mathematical residue remains in the authorized task scope.
