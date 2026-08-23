# CBRC F3R — Source and Target-Leak Audit

Researcher-ID: `EM-CBRC-F3R-AA5925`

Task: `RS-CBRC-F3R-BALANCED-MIXING-SURVIVOR-FAMILY-COMPLETION`

Verdict:

`TARGET_LEAK_AUDIT_PASS`

## 1. Mathematical whitelist actually used

Only the F3R-authorized mathematical/specification inputs were opened:

1. F3R taskbook:
   `research_tasks/COHERENT_BRC_F3R_BALANCED_MIXING_SURVIVOR_FAMILY_COMPLETION_20260823.md`
   at `0bb4fcc0bfad506d4b3891c6d139ae03faa40390`.
2. Original F3 taskbook:
   `research_tasks/COHERENT_BRC_F3_BALANCED_REVERSIBLE_MIXING_CONSERVATION_FORWARD_CLASSIFICATION_20260823.md`
   at `bbdc0ad66c5bde1c712f2fbd80308929cd6159e6`.
3. F3 blind packet:
   `research_inputs/CBRC_F3_BLIND_BALANCED_MIXING_PACKET_20260823.md`
   at `19ed5cfdba021cf67be0f059d8e26be1fb5af3b2`.
4. Frozen F3 owner packet at `ce10996ca7995279770cb7c51b21cc7812f358d4`:
   - `research_reports/CBRC_F3_BALANCED_REVERSIBLE_MIXING_CONSERVATION_RETURN_20260823.md`
   - `research_reports/CBRC_F3_SOURCE_AND_TARGET_LEAK_AUDIT_20260823.md`
   - `research_reports/CBRC_F3_ABLATION_AND_COUNTERMODEL_PACKET_20260823.md`
   - `scripts/cbrc_f3_validate_balanced_mixing_forward.py`
   - `evidence/cbrc_f3_balanced_mixing_manifest.json`
5. Driver review:
   `driver_reviews/CBRC_F3_BALANCED_REVERSIBLE_MIXING_CONSERVATION_DRIVER_REVIEW_20260823.md`
   at `bdcee332462d52dbd3642bb3f05b2cafecaebe31`.

## 2. Governance-only reads

Account execution governance was read only for connector-first repository procedure:

- `awdawmip/chatgpt-global-knowledge/00_BOOTSTRAP.md`
- `awdawmip/chatgpt-global-knowledge/OPERATING_MANUAL.md`

No mathematical carrier, matrix, scalar, target law, or downstream comparison was taken from those files.

Repository/branch metadata was used only for branch creation and committed-artifact operations.

## 3. Explicit forbidden-source status

Not opened and not used:

- R063 mathematics;
- R064 mathematics;
- R065 mathematics;
- FQ mathematics;
- F1 torsion-free counterfactual as a target route;
- downstream coherent-BRC free research;
- downstream wave free research;
- external quantum mechanics;
- quantum walks;
- Hilbert spaces;
- Born rules;
- path integrals;
- gauge theory;
- wave equations;
- external continuum wave theory.

No web search was used for mathematics.

## 4. Forbidden-selector status

Not used as premise, ranking criterion, or survivor selector:

- complex numbers;
- quadratic integer carriers;
- square norms;
- inner products;
- named finite phase groups;
- Hadamard/Fourier/splitter matrices;
- continuum wave laws.

The prime-pair support scalar emerged solely from the already accepted six-periodic F3 scalar:

`[0,1,1/2,1/2,1/2,1] = 1/2*(support mod 2 + support mod 3)`.

It was then generalized algebraically to arbitrary distinct primes to test whether the frozen axioms themselves select `(2,3)`. They do not.

This is an underdetermination/countermodel construction, not downstream matching.

## 5. Provenance of new F3R results

The new results use only:

- elementary integer divisibility;
- finite-field support counting;
- the fact that a support-count-preserving invertible 2x2 matrix over a field is monomial;
- Bezout completion of a primitive integer column;
- CRT for two coprime moduli;
- finite physical-equivalence orbits under accepted unary signs, marker swap, and inverse;
- exact finite enumeration only after `(B,D)` was reduced to `81*48` possibilities;
- the frozen carrier and `R,J,S`.

The deterministic checker uses only Python standard-library exact arithmetic.

## 6. Kill-condition checklist

`READ_FORBIDDEN_R063_R064_R065_FQ = false`

`READ_DOWNSTREAM_COHERENT_WAVE = false`

`USED_EXTERNAL_QUANTUM_OR_WAVE_PREMISE = false`

`PRESELECTED_COMPLEX_OR_QUADRATIC_CARRIER = false`

`ASSUMED_SQUARE_NORM_OR_INNER_PRODUCT = false`

`SELECTED_SURVIVOR_BY_HADAMARD_OR_FOURIER_RESEMBLANCE = false`

`USED_DOWNSTREAM_TARGET_TO_CHOOSE_PRIME_PAIR = false`

`TARGET_LEAK_AUDIT_PASS = true`

## 7. Audit verdict

`TARGET_LEAK_AUDIT_PASS`

F3R is frozen as an internal additive/congruence/positive-cone classification and strict-underdetermination result. No downstream comparison is authorized or opened here.
