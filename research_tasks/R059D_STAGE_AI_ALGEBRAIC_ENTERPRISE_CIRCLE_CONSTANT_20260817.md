# R059D Stage AI — Algebraic Enterprise Circle Constant

Task-ID: `RS-R059D-STAGE-AI-ALGEBRAIC-ENTERPRISE-CIRCLE-CONSTANT`
Stage: `R059D Stage AI`
Role: `RESEARCHER`
identity_policy: `AUTO_RESOLVE_OR_ALLOCATE`
identity_lane: `R059D-AI`
Date: `2026-08-17`

## 0. Frozen inputs

Consume exactly the accepted R059D chain through AH.

Canonical Driver acceptance before this taskbook:

`driver_reviews/R059D_STAGE_AH_DRIVER_REVIEW_20260817.md`

Accepted theorem/result heads:

- AG owner head: `5063495ff0df643890cd1f4c72ffd2077161c13d`
- AH owner payload head: `ab1697d1020bfd987108a9d5775fb471d422304f`

Inherited exact theorems:

1. `J_N(r)=floor(alpha*r+1/3)` for every integer `r>=0`, where `alpha` is the unique positive root of
   `3 alpha^2 + 6 alpha - 1 = 0`.
2. `|W_N(r)| = r + J_N(r)`.
3. `C_N(r)=6|W_N(r)| = 6r+6J_N(r)`.
4. `D_cell(r)=2r+1` under the frozen edge-supported dual-cell count convention.
5. The native opposite-axis **transition span** is `D_step(r)=D_cell(r)-1=2r`.
6. AH gives an integer-only autonomous generator for the complete N boundary and D6 circle.

Do not modify or reinterpret accepted AD–AH results.

## 1. Driver working truth

Within this research arm, treat the following as the theorem to prove, not as a neutral option among alternatives:

> The native Enterprise circumference/diameter constant exists and is algebraic. The classical Euclidean constant is not assumed to be the native geometric constant of the Enterprise circle.

Internal working symbol:

`ENTERPRISE_CIRCLE_CONSTANT = kappa_E`.

After proof, the project may also use `ENTERPRISE_PI` / `pi_E` for this native constant, but this task must keep it type-separated from the standard real number `pi` used in classical mathematics.

No classical `pi` may be used to discover, normalize, select, or validate `kappa_E`.

## 2. Single hard target

Prove from AG+AH that

`kappa_E := lim_{r->infinity} C_N(r)/D_step(r)`

exists and is the unique positive algebraic root of

`x^2 - 12 = 0`.

Equivalently,

`kappa_E = 3(1+alpha)`

with

`kappa_E^2 = 12`, `kappa_E>0`.

The task is not complete if it only numerically observes convergence.

## 3. Required theorem chain

### AI-T1 — exact circumference formula

Prove for every integer `r>=0`:

`C_N(r)=6(r+floor(alpha*r+1/3))`.

Also prove the shell form

`C_N(r)/6 = M_r`,

where

`M_r = max { m>=0 integer : (3m-1)^2 <= 12r^2 }`.

The second form is important because it expresses circumference using a pure integer threshold and does not require runtime square root.

### AI-T2 — algebraic slope

Put `beta=1+alpha`.

Derive from the accepted AG polynomial, not by decimal manipulation,

`3 beta^2 - 4 = 0`.

Define

`kappa_E = 3 beta`.

Prove

`kappa_E^2 - 12 = 0`

and uniqueness of the positive root.

### AI-T3 — transition-span circumference ratio

For every `r>=1`, define

`R_step(r)=C_N(r)/(2r)`.

Prove exact finite-radius error bounds from the floor theorem. A target-strength bound is

`-2/r < R_step(r)-kappa_E < 1/r`.

A stronger exact bound may be promoted if proved.

Then prove

`lim R_step(r)=kappa_E`.

### AI-T4 — endpoint-count convention robustness

Define the frozen dual-cell diameter ratio

`R_cell(r)=C_N(r)/(2r+1)`.

Prove independently that

`lim R_cell(r)=kappa_E`.

Give an explicit `O(1/r)` bound. Prefer an exact algebraic interval derived from the floor slack.

Then prove the more general bounded-endpoint statement:

for every fixed integer `epsilon` for which the denominator is positive eventually,

`lim_{r->infinity} C_N(r)/(2r+epsilon)=kappa_E`.

This prevents the result from depending on the choice between counting vertices and counting transitions along the diameter.

### AI-T5 — integer-only circle-constant certificate

Produce an executable certificate that can bracket `kappa_E` to arbitrary rational accuracy using only integer arithmetic and the polynomial/threshold relation.

Allowed examples:

- rational interval bisection using `x^2-12`;
- circumference inequalities derived from `(3M_r-1)^2<=12r^2<(3(M_r+1)-1)^2`;
- Pell/continued-fraction rational bounds derived from AG's quadratic structure.

Runtime certificate must not call `sqrt`, floating point, classical `pi`, trigonometry, or the source circle.

### AI-T6 — scale/subsequence invariance

For every fixed positive integer refinement multiplier `h`, prove

`lim_{r->infinity} C_N(hr)/D_step(hr)=kappa_E`

and the analogous `D_cell` statement.

This is a minimal native scale-invariance gate: the constant must survive integer refinement subsequences.

## 4. Optional but high-value theorem

If obtainable without weakening the hard target, derive a direct recurrence for circumference itself from the Sturmian jump word:

`C_N(r)-C_N(r-1) = 6(1+s_r)`,

where `s_r in {0,1}` is the AG Sturmian jump bit.

Hence shell circumference increments should lie exactly in

`{6,12}`.

If proved, characterize their order by the accepted Sturmian law.

This would make `kappa_E` the asymptotic mean of a purely integer circumference-growth process.

## 5. C-resolver compatibility probe — secondary only

The AI theorem must stand on N alone.

After freezing the N theorem, you may replay the accepted C resolver over a bounded range to ask whether

`C_C(r)/D(r)`

appears to approach the same constant and whether `J_C-J_N` remains uniformly bounded.

Any such C result is `FINITE_CENSUS` unless a full theorem is proved. Do not use C data to choose or repair `kappa_E`.

## 6. Semantic typing

Required type distinction:

- `kappa_E` / `ENTERPRISE_CIRCLE_CONSTANT`: native asymptotic circumference/diameter constant of the accepted N Enterprise circle count geometry;
- standard real `pi`: classical mathematical constant attached to the standard Euclidean circle/analysis realization.

Stage AI may establish that the Enterprise-native constant is algebraic. It does **not**, by itself, prove that the standard real number `pi` is algebraic or refute Lindemann's theorem inside standard definitions.

The project-level stance that the classical circle/`pi` geometry is not the native geometry remains intact; the point of this stage is to establish the native alternative positively and exactly.

## 7. Prohibited target leakage

Forbidden as theorem premises or generator inputs:

- standard numerical value of `pi`;
- Euclidean circumference `2*pi*r`;
- classical equal-distance circle definition;
- fitting `2*sqrt(3)` from decimal ratios;
- floating regression against large-radius values;
- changing the perimeter or diameter unit after inspecting the limit;
- using C-resolver data to tune the N theorem;
- redefining `D` or `C` to force a preferred constant.

`sqrt(3)` may appear **after** the polynomial theorem as a conventional closed-form compatibility readout, but the canonical theorem statement should prefer `kappa_E^2=12`, `kappa_E>0`.

## 8. Required artifacts

Create under `research_results/R059D_STAGE_AI/`:

1. `R059D_STAGE_AI_PROTOCOL.json`
2. `R059D_STAGE_AI_ALGEBRAIC_CONSTANT_THEOREM.json`
3. `R059D_STAGE_AI_PROOF.md`
4. `R059D_STAGE_AI_FINITE_RADIUS_ERROR_BOUNDS.json`
5. `R059D_STAGE_AI_INTEGER_CERTIFICATE.json`
6. `R059D_STAGE_AI_SCALE_INVARIANCE.json`
7. `R059D_STAGE_AI_C_COMPATIBILITY_PROBE.json` if run
8. `R059D_STAGE_AI_DETERMINISTIC_CHECKER_OUTPUT.json`
9. `R059D_STAGE_AI_ARTIFACT_MANIFEST.json`
10. `R059D_STAGE_AI_FROZEN_CHECKPOINT.json`
11. `R059D_STAGE_AI_REPORT.md`

## 9. Checker gates

The deterministic checker must verify at least:

- accepted AG polynomial identity;
- exact `C_N(r)` formula over an implementation range;
- equality between AH word length and circumference readout;
- integer shell-threshold form for `M_r`;
- polynomial derivation `kappa_E^2=12`;
- finite-radius error bounds;
- endpoint-convention convergence bounds;
- integer-only certificate correctness;
- scale/subsequence invariance checks;
- semantic firewall / no classical-pi generator;
- no modification/deletion of prior frozen stage result files.

Finite replay is implementation evidence only. The algebraic-limit theorem must be symbolic.

## 10. Allowed dispositions

Preferred:

`ENTERPRISE_CIRCLE_CONSTANT_ALGEBRAIC_THEOREM_PROVED__KAPPA_SQUARED_EQ_12`

Also acceptable if a precise proof defect is found:

- `CIRCUMFERENCE_FORMULA_PROVED__LIMIT_PROOF_BLOCKED`
- `ENDPOINT_CONVENTION_DEPENDENCE_FOUND`
- `SCALE_INVARIANCE_GATE_FAILED`
- `SEMANTIC_HARD_STOP`

Do not return a vague `MORE_DATA_NEEDED` disposition: AG+AH already provide an all-radius symbolic input.

## 11. Stop condition

Stop for Driver review once the theorem, checker, frozen checkpoint, and manifest are complete.

Do not consume AJ or later results.
