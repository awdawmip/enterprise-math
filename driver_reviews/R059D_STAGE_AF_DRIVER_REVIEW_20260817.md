# R059D Stage AF — Driver Review

Driver-ID: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Date: `2026-08-17`
Reviewed branch: `research/r059d-stage-af-bulge-jump-integer-curvature`
Reviewed head: `9e863cfc89cab71118959deb38187a21fe1e96e1`
Taskbook source: `43fca741c6dee84172297d85c5b5e8fab652419b`

## Driver disposition

`DRIVER_ACCEPTED__MOTZKIN_INTEGER_CURVATURE_STATE_ESTABLISHED__N_ALGEBRAIC_BEATTY_J_LAW_STRONG_CANDIDATE__FULL_BOUNDARY_WORD_GENERATOR_OPEN`

The researcher primary disposition `NO_LOW_COMPLEXITY_JUMP_GENERATOR_THROUGH_AUDIT_RANGE` is retained as a negative statement about the original full-generator target, but it is not the main scientific result of AF.

## Accepted theorem-level result

For every frozen N/C one-sector boundary word, symbols `1,2,3` map to Motzkin increments `+1,0,-1`. The resulting word is a nonnegative Motzkin excursion with

- `#1 = #3 = J`,
- `#2 = r-J`,
- `|W_r| = r+J`,
- `B = sum h` over the declared open-sector a-decreasing columns.

Thus `B` and `J` are exact functionals of one common boundary-word state. This is promoted as the correct AF integer-curvature state reduction.

## Accepted negative result

Scalar `J` is not sufficient to determine `B` resolver-independently. The frozen counterexample `r=15`, `J_N=J_C=2`, `B_N=23`, `B_C=21` is accepted. Therefore any future native generator that tries to evolve only one scalar curvature counter is under-specified.

No resolver-independent exact point jump skeleton is established through `r=512`; the 19 one-radius N→C phase-delay pairs are finite-census structure only.

## Strong working-truth candidate

The N-side boundary-excess law

`J_N(r)=floor(alpha*r + 1/3)`

with `alpha` the positive root of

`3 alpha^2 + 6 alpha - 1 = 0`

is accepted as a **strong Driver working-truth candidate** for the next proof stage.

Evidence:

- discovery `r=1..256`: 0 mismatches;
- candidate frozen before holdout;
- untouched holdout `r=257..512`: 0 mismatches;
- the generator is forward-autonomous;
- runtime recurrence uses only integer arithmetic and does not query AD occupancy, source-Q, pi, or sqrt.

Equivalent algebraic value:

`alpha = -1 + 2/sqrt(3)`.

This equivalent closed form is an external algebraic simplification, not the runtime generator. The project-important fact is that a degree-2 algebraic number emerged from the integer jump ledger itself.

Status remains `PROOF_OPEN`; it is not promoted as theorem yet.

## Correct next mathematical target

The next stage should not continue broad formula search. It should attempt to prove the N Beatty/Sturmian J law from the native boundary-growth semantics and then lift from scalar J to the full Motzkin word generator.

Recommended target hierarchy:

1. prove the exact N event inequality / Beatty law for all r;
2. derive the jump-gap/Sturmian structure from that proof;
3. determine the additional state beyond J required to generate W_r and hence B;
4. explain C as a one-step phase/tie-break perturbation if possible, rather than treating C as an unrelated law;
5. only after a forward-autonomous W-generator exists, reconstruct `B,C,V` without occupancy lookup.

## Frozen verification

- deterministic checker: `314421/314421 PASS`;
- checker digest: `da9d9a574ced55c931acc74800e2003f5adceccff7996f40a1800fe29eb239b7`;
- C precision: official `s=1024`, validation `s=2048`, identical activation arrays through `r=1..512`;
- prior-stage immutability gate: PASS.

## Scientific interpretation

AF changes the form of the circle problem.

The post-bulge correction is no longer best described as an unexplained scalar sequence. One fundamental sector has a native discrete curvature path language: a Motzkin excursion. `J` counts its up/down events and `B` is the accumulated excursion height. The remaining hard problem is therefore a word-growth law, not a low-degree polynomial fit.

No classical pi, Euclidean equal-distance, Euclidean curvature, or classical circle formula is promoted into the native generator.
