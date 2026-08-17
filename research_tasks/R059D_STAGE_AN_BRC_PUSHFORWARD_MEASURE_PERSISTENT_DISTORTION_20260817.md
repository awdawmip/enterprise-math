# R059D Stage AN — BRC Pushforward Measure and Persistent Metric Distortion

Task-ID: `RS-R059D-STAGE-AN-BRC-PUSHFORWARD-MEASURE-PERSISTENT-DISTORTION`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

Identity policy: `AUTO_RESOLVE_OR_ALLOCATE`

## Frozen inputs

Read-only accepted inputs:

1. Stage AL: unique canonical Enterprise native circle in final `ADM_E`;
2. Stage AK: canonical fixed-length local-turn orbit and exact minimal period `T_r=C_E(r)`;
3. Stage AI/AJ: `kappa_E^2=12`, `kappa_E>0`, including resolver/readout robustness;
4. Stage AM: canonical radial-incidence BRC closed-fiber relation from the orthogonal continuous source circle to canonical target elementary turns;
5. Stage AM local theorem: source arc metric does not descend to a constant one-turn target metric; first exact unequal-fiber witness occurs at `r=3`.

Do not modify prior-stage result files.

## Driver working truth

Treat the following as the theorem route to prove:

> The AM non-isometry is not a small-radius accident. The canonical BRC pushes the source arc measure to a nonuniform weight field on the target turn cycle. Target native circumference is counting measure on the same cycle. The weight field remains genuinely nonconstant under radial refinement, while its global mean converges to the source/target circumference-constant ratio.

Direction confidence = maximal; audit rigor = maximal.

## Hard target

Prove a theorem package strong enough for:

`CANONICAL_BRC_PUSHFORWARD_MEASURE_DECOMPOSITION_PROVED__COUNTING_MEASURE_NONPROPORTIONAL__PERSISTENT_DISTORTION_ESTABLISHED`.

At minimum establish all of:

1. an exact source pushforward measure on target elementary turns;
2. exact source circumference as a weighted target-turn sum;
3. target circumference as the unweighted target-turn count;
4. nonproportionality of those two measures for every `r>=3` or an exact sharp radius classification;
5. a refinement theorem showing the nonuniformity does not disappear merely because `r->infinity`;
6. the global mean source weight per target turn converges to `kappa_perp/kappa_E`, with `kappa_perp` remaining source typed.

Do not infer persistent distortion solely from one fixed `r=3` witness.

## Stage 0 — measure semantics freeze

Let the canonical target cycle have elementary turns

`E_r={e_0,...,e_(T_r-1)}`

and let the AM closed source fibers be `F_(r,k)`.

Freeze two measures on the same finite target edge set:

### Native counting measure

`nu_r(e_k)=1`.

Hence

`nu_r(E_r)=T_r=C_E(r)`.

### Source-arc pushforward measure

Preferred dimensionful form:

`mu_r(e_k)=Arc_perp(F_(r,k))`.

Because neighboring closed fibers overlap only on zero-arc-measure boundary rays, prove

`mu_r(E_r)=Circ_perp(r)`.

Also define the radius-normalized local weight

`w_(r,k)=mu_r(e_k)`

when source radius is represented in primitive length units, or explicitly use

`w_(r,k)=r*Delta_(r,k)`

where `Delta_(r,k)` is the source angular fiber width. Be completely explicit about units and normalization; do not silently divide by a target metric.

Required output:

`R059D_STAGE_AN_MEASURE_SEMANTICS.json`.

## Stage A — exact weighted circumference decomposition

Prove exactly:

`Circ_perp(r)=sum_k mu_r(e_k)`

and

`C_E(r)=sum_k 1=T_r`.

This is the central decomposition:

`same target cycle + two different measures`.

Define the global mean source weight per target turn

`bar_w_r = Circ_perp(r)/T_r`.

Using typed constants only, prove

`bar_w_r -> kappa_perp/kappa_E`

because

`Circ_perp(r)=2*kappa_perp*r`

on the accepted orthogonal source realization and

`T_r/(2r)->kappa_E`.

`kappa_perp` remains source typed. Do not identify it with `kappa_E`.

Required output:

`R059D_STAGE_AN_WEIGHTED_CIRCUMFERENCE_THEOREM.json`.

## Stage B — exact local weight formula

Starting from AM, retain the exact source-side formula for consecutive target rays

`p=(a,b), q=(c,d)`:

`tan(Delta)=sqrt(3)*(ad-bc)/(2ac+2bd+ad+bc)`.

Derive exact integer/algebraic certificates for the local normalized weight wherever possible.

The proof may use source-side analytic facts after typing them explicitly as source compatibility geometry. They must not enter the target generator or target canonicality proof.

Required output:

`R059D_STAGE_AN_LOCAL_WEIGHT_FORMULA.json`.

## Stage C — nonproportionality classification

AM proves nonproportionality at `r=3`. Strengthen this.

Determine and prove the sharp all-radius statement, preferably:

`mu_r is proportional to nu_r iff r in {1,2}`,

and therefore

`mu_r not proportional to nu_r for every r>=3`.

If that exact classification is false, produce the complete exact exceptional set or the strongest proved theorem.

A finite census is not a proof of the all-radius statement.

Preferred proof tools:

- axis-edge exact weight;
- reflection/bisector edge exact weight;
- canonical Motzkin word structure;
- AL primitive-support frontier inequalities;
- monotonicity of source angular increments.

Required output:

`R059D_STAGE_AN_NONPROPORTIONALITY_THEOREM.json`.

## Stage D — persistent distortion under refinement

This is the hard new stage.

Define the local source weight on a target turn as

`w_(r,k)=r*Delta_(r,k)`

if `Delta` is angular width.

Prove that the local weight field does not converge uniformly to one constant as `r->infinity`.

Preferred strongest route: construct two canonical macroscopic-position turn sequences with distinct exact limits.

### Axis sequence

For the first canonical edge

`(r,0)->(r-1,1)`, derive exactly

`tan(Delta_axis(r))=sqrt(3)/(2r-1)`

and prove

`r*Delta_axis(r) -> sqrt(3)/2`.

### Bisector/interior sequence

Select a canonical turn whose location approaches the sector bisector and prove its scaled coordinates and local symbol are controlled strongly enough to obtain a second limit, preferably

`r*Delta_mid(r) -> 1`.

Then freeze

`PERSISTENT_LOCAL_DISTORTION` because the two limits differ.

If the bisector limit is not exactly 1, derive the correct second limit. Do not tune the sequence to a desired constant.

Alternative admissible route if the direct bisector proof is blocked: compare the exact axis limit with the global mean limit `kappa_perp/kappa_E` and prove they differ using a source-side exact inequality, clearly typed as source mathematics. This is weaker than two local subsequential limits and should be used only if necessary.

Required output:

`R059D_STAGE_AN_PERSISTENT_DISTORTION_THEOREM.json`.

## Stage E — defect field and optional limiting profile

Define

`d_(r,k)=w_(r,k)-bar_w_r`.

Then exactly

`sum_k d_(r,k)=0`

when `bar_w_r` uses the same local-weight normalization.

Audit:

- max positive/negative defect;
- D6 symmetry of the defect field;
- reflection symmetry;
- whether a nonzero limiting defect profile exists as a function of macroscopic sector position;
- whether the empirical variance has a positive limiting lower bound.

Preferred stronger theorem:

`liminf_r (1/T_r) sum_k d_(r,k)^2 > 0`.

This variance theorem is optional and must not block the hard target if persistent nonuniformity has already been proved by distinct local limits.

Required output:

`R059D_STAGE_AN_DEFECT_PROFILE_AUDIT.json`.

## Stage F — no hidden metric renormalization

Audit possible attempts to rescue isometry by rescaling one target turn by a radius-dependent global factor.

The factor

`lambda_r = Circ_perp(r)/T_r = bar_w_r`

matches total circumference by construction, but prove that for `r>=3` it fails locally:

there exists at least one `e_k` with

`mu_r(e_k) != lambda_r`.

Under the persistent-distortion theorem, prove that global renormalization also fails to become locally exact uniformly as `r->infinity`.

Freeze the distinction:

- `GLOBAL_MEAN_CONVERSION_FACTOR` is allowed as a summary statistic;
- `LOCAL_METRIC_ISOMETRY` is false.

Required output:

`R059D_STAGE_AN_GLOBAL_RENORMALIZATION_NO_GO.json`.

## Stage G — deterministic replay

Only after theorem statements are frozen, validate implementation.

Minimum:

- all `r=1..1024` where practical;
- checkpoints `2048,4096,8192`;
- exact weighted-sum coverage;
- `r=1,2` equal-weight controls;
- all `r>=3` nonproportionality over the replay range;
- exact axis formula;
- chosen interior/bisector sequence;
- D6/reflection defect symmetry;
- no source geometry used to alter target orbit.

Finite replay is implementation evidence only.

## Required artifacts

- `R059D_STAGE_AN_MEASURE_SEMANTICS.json`
- `R059D_STAGE_AN_WEIGHTED_CIRCUMFERENCE_THEOREM.json`
- `R059D_STAGE_AN_LOCAL_WEIGHT_FORMULA.json`
- `R059D_STAGE_AN_NONPROPORTIONALITY_THEOREM.json`
- `R059D_STAGE_AN_PERSISTENT_DISTORTION_THEOREM.json`
- `R059D_STAGE_AN_DEFECT_PROFILE_AUDIT.json`
- `R059D_STAGE_AN_GLOBAL_RENORMALIZATION_NO_GO.json`
- `R059D_STAGE_AN_PROOF.md`
- `R059D_STAGE_AN_DETERMINISTIC_CHECKER_OUTPUT.json`
- `R059D_STAGE_AN_FROZEN_CHECKPOINT.json`
- `R059D_STAGE_AN_REPORT.md`

## Mandatory semantic firewalls

- source arc measure is source typed;
- target turn counting measure is target native;
- source-side `sqrt(3)`, angles and standard circle integration may be used only in the source compatibility layer;
- no source quantity may select, tune or redefine the AL canonical target orbit;
- do not identify `kappa_perp` with `kappa_E`;
- do not claim a new theorem about the standard real number pi unless a later task explicitly asks for a source-side theorem;
- do not replace the relational BRC fibers with a bijective point map.

## Dispositions

Use the strongest justified terminal status:

1. `BRC_PUSHFORWARD_MEASURE_DECOMPOSITION_PROVED__NONPROPORTIONAL_FOR_ALL_R_GE_3__PERSISTENT_DISTORTION_PROFILE_ESTABLISHED`
2. `BRC_PUSHFORWARD_MEASURE_DECOMPOSITION_PROVED__PERSISTENT_TWO_LIMIT_DISTORTION_ESTABLISHED`
3. `BRC_PUSHFORWARD_MEASURE_DECOMPOSITION_PROVED__NONPROPORTIONAL_ALL_RADIUS__ASYMPTOTIC_PROFILE_OPEN`
4. `BRC_PUSHFORWARD_MEASURE_DECOMPOSITION_PROVED__FINITE_RADIUS_NONISOMETRY_ONLY`
5. `PERSISTENT_DISTORTION_WORKING_TRUTH_FALSIFIED__EXACT_COUNTERTHEOREM`
6. `FINITE_REPLAY_ONLY__NO_MEASURE_THEOREM`

Do not stop at a weaker disposition while a stronger route remains untested.

`STOP_FOR_DRIVER_REVIEW` only after the strongest reachable measure/distortion theorem and all semantic firewalls are frozen.
