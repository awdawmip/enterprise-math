# R059D Stage AO — Macroscopic BRC Density Profile and Limiting Measure Separation

Task-ID: `RS-R059D-STAGE-AO-MACROSCOPIC-BRC-DENSITY-PROFILE-LIMIT`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

Identity policy: `AUTO_RESOLVE_OR_ALLOCATE`

## Frozen inputs

Read-only accepted inputs:

1. Stage AL canonical Enterprise native circle / unique final-`ADM_E` resolver;
2. Stage AK native fixed-length local turn orbit and exact period;
3. Stage AM canonical radial-incidence BRC fibers and source-arc metric nondescend;
4. Stage AN exact pushforward measure decomposition, sharp `r in {1,2}` proportionality classification, and persistent axis/mid two-limit distortion;
5. Stage AG/AI exact asymptotics `M_N(r)/r -> beta`, `3 beta^2=4`, and `kappa_E^2=12`, `kappa_E>0`.

Do not modify prior-stage result files.

## Driver working truth

Treat the following as the theorem to expose, not as a neutral possibility:

> AN's two distinguished local limits are samples of a full nonconstant macroscopic distortion field. Under radial refinement the canonical Enterprise turn cycle acquires a deterministic D6-periodic turn-density profile in the orthogonal source compatibility angle. The source-arc pushforward measure and native turn-counting measure converge to two distinct continuum measures whose Radon–Nikodym ratio is nonconstant.

The intended first-sector limiting turn density is

`g(theta)=2/sqrt(3)*cos(theta)` for `0<=theta<=pi_source/6`,

and its reflected continuation on the second half-sector,

`g(theta)=2/sqrt(3)*cos(pi_source/3-theta)` for `pi_source/6<=theta<=pi_source/3`,

with D6 periodic continuation.

This formula is a **research target to prove**. If exact derivation yields another profile, freeze the true profile rather than tuning definitions.

Here `theta` and any trigonometric display are source-compatibility coordinates only; they must never enter the target generator or canonicality definition.

## Hard target

Prove the strongest form:

`FULL_MACROSCOPIC_BRC_DENSITY_PROFILE_PROVED__NONCONSTANT_RADON_NIKODYM_LIMIT__POSITIVE_LIMITING_VARIANCE`.

At minimum establish a full-circle weak-limit theorem for normalized native turn counting and normalized source-arc pushforward measures, and prove their limiting local density ratio is nonconstant on a set of positive measure.

Two-point subsequence separation alone is insufficient for Stage AO.

## Stage 0 — common continuum carrier

Create a rigorous comparison carrier for varying-radius target cycles.

For every canonical target edge `e_(r,k)=(p_(r,k),p_(r,k+1))`, assign a source-compatibility angular location using only the already-frozen AM radial-incidence chart, preferably the midpoint of its source fiber.

Define:

- `theta_(r,k)` — source-compatibility angular location;
- `N_r(theta)` — cumulative number of canonical target turns from the sector axis to angle `theta`;
- normalized target counting probability `hat_nu_r`;
- normalized source pushforward probability `hat_mu_r`.

Boundary-ray tie choices must be shown irrelevant in the weak limit.

Required output:

`R059D_STAGE_AO_CONTINUUM_CARRIER_SEMANTICS.json`.

## Stage A — scaled canonical frontier theorem

Use AL's primitive-support carrier, not source selection, to prove the canonical target boundary has a uniform radial scaling limit in the source compatibility chart.

A sufficient theorem is:

`Q_E(a,b)=r^2+O(r)` uniformly on canonical radius-r frontier vertices,

with an explicit constant, hence the source-compatible radial magnitude divided by `r` tends uniformly to 1.

This is a comparison theorem after target canonicality; it must not be used to redefine the target circle.

Derive the limiting first-sector coordinate functions from the source compatibility angle:

`B(theta)=2/sqrt(3)*sin(theta)`,

`A(theta)=cos(theta)-sin(theta)/sqrt(3)`,

or exact equivalent source-typed formulas.

Required output:

`R059D_STAGE_AO_SCALED_FRONTIER_THEOREM.json`.

## Stage B — exact cumulative turn-count identities

Exploit the already-proved target monotone turn structure.

Before the sector bisector, every elementary turn increases `b` by exactly one. Therefore prove an exact cumulative identity of the form

`N_r(p)=b`

for canonical vertices on the left half.

After the bisector, every elementary turn decreases `a` by exactly one. Derive the corresponding exact right-half identity, preferably

`N_r(p)=M_N(r)-a`

with the precise convention at the center turn frozen.

These are target combinatorial identities. Do not derive them from source arc lengths.

Required output:

`R059D_STAGE_AO_CUMULATIVE_TURN_COUNT_THEOREM.json`.

## Stage C — macroscopic turn-density profile

Combine Stages A and B to prove uniform convergence of the scaled cumulative turn count:

`N_r(theta)/r -> G(theta)`

on each closed half-sector, with explicit `G` and controlled center/axis conventions.

Preferred first-sector formula:

- `G(theta)=2/sqrt(3)*sin(theta)` on the left half;
- `G(theta)=beta-A(theta)` on the right half, where `beta=2/sqrt(3)` is only a conventional source-side display after the algebraic relation `3 beta^2=4` is established.

Then prove the limiting turn-density exists almost everywhere / piecewise continuously:

`g(theta)=G'(theta)`.

Preferred formula:

- left: `g(theta)=2/sqrt(3)*cos(theta)`;
- right: `g(theta)=2/sqrt(3)*cos(pi_source/3-theta)`.

Prove positivity, D6 periodicity, reflection symmetry, and correct total mass:

`integral_full g(theta) dtheta = lim T_r/r = 2*kappa_E`.

Do not use standard decimal pi.

Required output:

`R059D_STAGE_AO_TURN_DENSITY_PROFILE_THEOREM.json`.

## Stage D — full local BRC weight profile

AN defines source local weight

`w_(r,k)=r*Delta_(r,k)`.

Prove that for any macroscopic angular location away from a finite set of sector-boundary convention points, canonical local weights converge to

`w_infty(theta)=1/g(theta)`

in the correct local/Young-measure sense required by the discrete symbol mixing.

Important: if individual edge weights fail to converge pointwise at generic angles because the Sturmian/local symbol microstructure alternates, do **not** force pointwise convergence. Instead freeze the strongest correct object:

- local block average;
- two-scale/Young measure;
- Cesaro density;
- or weak Radon–Nikodym profile.

The profile theorem must recover AN's exact distinguished limits:

`w_axis -> sqrt(3)/2`,

`w_mid -> 1`.

Required output:

`R059D_STAGE_AO_LOCAL_WEIGHT_PROFILE_THEOREM.json`.

## Stage E — weak limits of the two normalized measures

Define

`hat_nu_r = (1/T_r) sum_k delta_(theta_(r,k))`

and the normalized source pushforward measure induced by AM fibers

`hat_mu_r = mu_r / Circ_perp(r)`

on the common angular carrier.

Prove weak convergence against a sufficiently rich test class, ideally all continuous periodic test functions.

Preferred target-counting limit:

`d hat_nu_infty = [g(theta)/(2*kappa_E)] dtheta`.

Preferred source-pushforward limit:

`d hat_mu_infty = [1/(2*kappa_perp)] dtheta`.

Hence prove mutual absolute continuity and a nonconstant limiting Radon–Nikodym derivative

`d hat_mu_infty / d hat_nu_infty = kappa_E/(kappa_perp*g(theta))`.

This is a source/target comparison density only. It is not a target native metric.

Required output:

`R059D_STAGE_AO_LIMIT_MEASURE_THEOREM.json`.

## Stage F — positive limiting variance / defect profile

AN deliberately left positive limiting variance open. AO must now resolve it from the full profile.

Let the source-weight mean be

`bar_w_infty=kappa_perp/kappa_E`.

Using the limiting turn-count measure, prove

`Var_infty = integral (w_infty(theta)-bar_w_infty)^2 d hat_nu_infty(theta) > 0`

or the exact equivalent if Stage D requires a two-scale local law.

If a closed form is naturally derivable without unsafe source/target type collapse, record it. A candidate identity worth testing is

`E_(hat_nu)[w_infty^2] = (3/4)*log(3)`

under the conventional source analytic chart, hence

`Var_infty=(3/4)*log(3)-(kappa_perp/kappa_E)^2`.

This closed form is **not frozen**; prove it or reject it explicitly.

Positivity must follow structurally from nonconstancy on positive measure, not from decimal evaluation of standard pi.

Required output:

`R059D_STAGE_AO_LIMITING_VARIANCE_THEOREM.json`.

## Stage G — symbol/microstructure audit

The canonical turn word is Sturmian/Motzkin-derived and discrete. Audit whether the macroscopic density `g(theta)` hides nontrivial symbol-level microstructure.

At minimum determine:

- local limiting frequency of symbols `1/2/3` as a function of macroscopic angle;
- whether pointwise source weights have one limit or a finite local mixture;
- whether the macro density is sufficient to reconstruct the weak measure limit;
- whether the AN axis/center values are extremal values of the macro profile.

Do not let unresolved microstructure invalidate a correct weak macroscopic theorem.

Required output:

`R059D_STAGE_AO_MICROSTRUCTURE_AUDIT.json`.

## Stage H — deterministic replay

Freeze all theorem statements before replay.

Minimum:

- all radii `1..2048`;
- checkpoints `4096,8192,16384` where practical;
- exact cumulative turn identities;
- empirical distribution functions versus proved `G`;
- weak moments/test functions versus limiting formulas;
- AN axis/central witnesses;
- D6/reflection symmetry;
- variance convergence diagnostic;
- target runtime/source-selection firewall.

Finite replay is implementation validation only.

## Required artifacts

- `R059D_STAGE_AO_CONTINUUM_CARRIER_SEMANTICS.json`
- `R059D_STAGE_AO_SCALED_FRONTIER_THEOREM.json`
- `R059D_STAGE_AO_CUMULATIVE_TURN_COUNT_THEOREM.json`
- `R059D_STAGE_AO_TURN_DENSITY_PROFILE_THEOREM.json`
- `R059D_STAGE_AO_LOCAL_WEIGHT_PROFILE_THEOREM.json`
- `R059D_STAGE_AO_LIMIT_MEASURE_THEOREM.json`
- `R059D_STAGE_AO_LIMITING_VARIANCE_THEOREM.json`
- `R059D_STAGE_AO_MICROSTRUCTURE_AUDIT.json`
- `R059D_STAGE_AO_PROOF.md`
- `R059D_STAGE_AO_DETERMINISTIC_CHECKER_OUTPUT.json`
- `R059D_STAGE_AO_FROZEN_CHECKPOINT.json`
- `R059D_STAGE_AO_REPORT.md`

## Mandatory semantic firewalls

1. Source angle, trig, source arc measure, `sqrt(3)`, `log`, and `kappa_perp` are compatibility/source-side analysis only.
2. None may choose, retune, or redefine the AL canonical target orbit.
3. Target native circumference remains turn counting / minimal period.
4. Do not identify `kappa_perp` with `kappa_E`.
5. Do not claim a new theorem about standard real pi.
6. Do not replace AM's relational fibers by a bijective point map.
7. Do not assume pointwise local-weight convergence if the discrete microstructure only supports a weak/two-scale limit.

## Dispositions

Use the strongest justified terminal status:

1. `FULL_MACROSCOPIC_BRC_DENSITY_PROFILE_PROVED__NONCONSTANT_RADON_NIKODYM_LIMIT__POSITIVE_LIMITING_VARIANCE`
2. `WEAK_LIMIT_MEASURE_SEPARATION_PROVED__POSITIVE_VARIANCE__POINTWISE_PROFILE_MICROSTRUCTURE_OPEN`
3. `MACROSCOPIC_TURN_DENSITY_PROVED__FULL_SOURCE_WEIGHT_LIMIT_OPEN`
4. `TWO_SCALE_DISTORTION_LIMIT_PROVED__SINGLE_PROFILE_FALSE`
5. `PERSISTENT_TWO_LIMIT_ONLY__NO_FULL_PROFILE_THEOREM`
6. `PROPOSED_MACRO_PROFILE_FALSE__EXACT_COUNTERTHEOREM`

Do not stop at a weaker disposition while a stronger mathematically valid limit object remains untested.

`STOP_FOR_DRIVER_REVIEW` only after the strongest reachable full-profile theorem and all firewalls are frozen.
