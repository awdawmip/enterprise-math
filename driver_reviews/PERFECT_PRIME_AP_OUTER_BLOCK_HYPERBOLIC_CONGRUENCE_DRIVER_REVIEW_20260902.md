# Driver Review — Perfect Prime AP outer block-hyperbolic congruence

Driver-ID: `EM-DVR-P8H4Q2`
Review-ID: `DR-4B27C9136E5A08D1F624`
Task: `RS-PERFECT-PRIME-AP-OUTER-BLOCK-HYPERBOLIC-CONGRUENCE`
Publication: `TP2-E2EE65A96658AD50D37C`
Result: `RR-19DB7617DE41BD10CCF7`
Execution: `ER-F7285D4C9DB27860AEF4`

## Disposition

`ACCEPTED / EXACT_NEGATIVE_BOUNDARY / FOLLOWUP_TASK`.

The Result is accepted at its exact declared strength. It does not prove or refute `det S_m(t) != 0` for all `m>=2`, `0<t<=1`. It closes two specific block-factorization readings: one fixed `t`-independent simultaneous congruence with blocks of size at most two, and the unstructured existential claim that some adaptive nonsingular `1x1/2x2` symmetric block-LDL decomposition exists.

## Envelope audit

The immutable Result record is bound by Git blob `c66d05a707eed54e3540eaf40fee6afc8a306024` and independent SHA-256 `fdc9fd8b958e494be715a55a4b59f523ac9a7209dc184508f5363eb18eef435e`. Its output manifest is complete and all four frozen paths resolve to the declared Git blobs:

- Return: `84a4d48828bfeef104938b4bff58303b70a7866c`;
- checker: `e23e69062fa99a2cbebd7f45f85b194f9906ce10`;
- exact static-block certificate: `e51eda899b88eebe6352ae1bc39b7150ddcff3f6`;
- execution record: `0f9772ae8678ed68b2013f6b1272467694be788d`.

The taskbook binding is the published blob `df991fb3079a934097a1b034784a9c358b188fac`. Finite exact arithmetic is used only for the stated `m=4` obstruction and the accepted `m=15` regression; the adaptive block-LDL equivalence is symbolic.

## Accepted symbolic boundary — adaptive block existence is circular

For a finite real symmetric matrix `A`, the Result proves:

`A is nonsingular`

if and only if, after symmetric permutations and Schur-complement elimination, there exists a block-LDL congruence with nonsingular diagonal blocks of size `1` or `2`.

The forward direction is a complete dimension induction. If a diagonal entry is nonzero, pivot on a `1x1` block. If all diagonal entries vanish, nonsingularity forces a nonzero off-diagonal entry, giving a nonsingular block `[[0,a],[a,0]]`. In either case determinant factorization makes the remaining symmetric Schur complement nonsingular, so induction continues.

Therefore the bare assertion

`there exists some adaptive nonsingular 1x1/2x2 block LDL for S_m(t)`

is exactly equivalent to the parent target `det S_m(t) != 0`. It is not an independent invariant and cannot be used to prove the target without circularity.

## Accepted exact static obstruction

At `m=4`, take

`A=S_4(1/3)`, `B=S_4(2/3)`, `C=S_4(1)`.

All three are nonsingular in exact arithmetic. If one fixed real congruence and one fixed `1+2` partition simultaneously block-diagonalized all three, the one-dimensional block would be a common real invariant/eigenline for

`T_B=A^(-1)B`, `T_C=A^(-1)C`.

The exact commutator `K=[T_B,T_C]` has rank `2`, so its kernel is one-dimensional. The certificate gives a primitive generator of that line and verifies that `T_B v wedge v` has all three coordinates nonzero. Hence the unique commutator-kernel line is not `T_B`-invariant, so there is no common eigenline. Thus no fixed `t`-independent simultaneous congruence with blocks of size at most two can work uniformly, already for these three exact parameter values.

The accepted `m=15` regression is preserved: the canonical `Delta_12` has signs `+,-,+` at `t=3/4,4/5,1`, so simply pairing adjacent canonical scalar pivots cannot make all paired blocks nonsingular throughout the interval.

## Exact route closure

Freeze as closed:

- `FIXED_T_INDEPENDENT_SIMULTANEOUS_BLOCK_BASIS_LE_2`;
- `BARE_ADAPTIVE_BLOCK_LDL_EXISTENCE_AS_PROOF_INVARIANT`;
- `CANONICAL_ADJACENT_PAIRING_AS_UNIFORM_REPAIR`.

Do **not** infer that every structured `t`-dependent block rule is impossible. Such a rule would still need an independently derived pivot/block law and independent nonvanishing formulas. However, the block lane has now passed through the canonical one-by-one flag obstruction and this stronger static/adaptive block audit without producing an independent all-`m` invariant.

## Successor decision

The parent objective remains open, so mathematical continuation is required. Closure is invalid. A third generic block-search task would risk repackaging the same circularity; the already-frozen residual Bernstein/Mobius interface is genuinely different and has exact positive finite evidence through `m<=10`. Therefore the next single continuation should switch route rather than continue unstructured block exploration.

Publish P0/HIGH `RS-PERFECT-PRIME-AP-RESIDUAL-BERNSTEIN-MOBIUS-ALL-M-POSITIVITY`, targeting an all-`m` proof or exact obstruction for the double-endpoint residual polynomial coefficients.

## Gate decisions

- `MATHEMATICAL_CONTINUATION = REQUIRED`.
- `LEAN_FORMALIZATION = NOT_REQUIRED` — the load-bearing all-`m` theorem remains open.
- `EXTERNAL_PRIOR_ART_DUPLICATION = SATISFIED_BY_EXISTING_REVIEWED_BOUNDARY`.
- `INDEPENDENT_REPLICATION = NOT_REQUIRED_AT_THIS_CHECKPOINT`.
- `ADVERSARIAL_AUDIT = BUILT_INTO_SUCCESSOR` — bounded coefficient positivity remains regression only and no closed block/flag mechanism may be silently reintroduced.

No Working Truth, Foundation authority, L4 status, novelty, canonical promotion, or parent-objective closure is granted.