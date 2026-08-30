# PCF2 sealed factor-blind benchmark — Result integrity re-freeze V3 return

Status: `FROZEN / AWAITING DRIVER REVIEW`

- Task-ID: `RS-PRIME-COORD-FACTOR-BLIND-BENCHMARK-SUITE`
- Publication-ID: `TP2-B7E4C1295A8D63F021CE`
- Researcher-ID: `EM-PCF2R3-6FA55B`
- Claim-ID: `chatgpt-pcf2r3-20260831-0021-8f2c61`
- Execution record: `ER-094BC1B3B7B33E82CBCF`
- Claim base: `7a6b80db39529874edc913253cff151948d91607`
- Frozen source branch: `research/prime-coord-factor-blind-benchmark-suite-em-pcf2-4b7c91@dce4a309f8d799030081ed82e310c26a92d8f465`

## 1. Terminal verdict

`PASS / PCF2_SEALED_FACTOR_BLIND_BENCHMARK_REFROZEN_WITH_COMPLETE_DIGEST_CHAIN_AND_ZERO_SCORE_DRIFT`

This revision performs integrity recovery only. It makes no mathematical, corpus, parameter, candidate, baseline, budget, score, or asymptotic-strength change.

Exact delta disposition:

- `NO_CORPUS_DELTA`
- `NO_PARAMETER_DELTA`
- `NO_SCORE_DELTA`
- `NO_CANDIDATE_DELTA`
- `NO_BASELINE_DELTA`
- `NO_LEAKAGE_BOUNDARY_DELTA`

The generation-2 Result `RR-03A546B894E6AF3840CA` was mathematically sufficient for the sealed benchmark but its output manifest bound only the return. Generation 3 therefore replays the exact frozen benchmark and binds every load-bearing frozen output under the current Result contract.

## 2. Byte-identical source recovery

The following frozen generation-2 files were restored by their original Git blob identities, not rewritten:

| Output | Git blob SHA-1 | SHA-256 |
| --- | --- | --- |
| `research_artifacts/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE/README.md` | `d20487587d49360ad8748f79fdb965185d0a8867` | `5d02d9f802b91ce3aff13f76dab7a1a2ca9e00cabace63034c5a4d17d524b4e9` |
| `research_artifacts/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE/benchmark_result_summary.json` | `d1e54c13de87824e09b0d9febad5982cff058623` | `608dacf519fbbd75c7d3d8405899e727ba950deca4286fb7698c395ec1251cbd` |
| `research_artifacts/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE/parameter_manifest.json` | `6ab07576499899bc48935a612952101e1e9e5d0e` | `deba73a337e9bb65d0771679961d9ee8ceb3f1aa2825280abc0d156c01032211` |
| `research_artifacts/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE/replay_schema.json` | `b8d25bc3bd89c834c8a37f0146fa0ab231450b9a` | `3fab00f962592a134c2c7172b9128f3ac1774a6af6e87299114fdfd9e0885bb8` |
| `scripts/check_prime_coord_factor_blind_benchmark_suite.py` | `72eb1bab61bc57e9815f2cac7276a88a1d1c9ff4` | `741e8c4c95e6a01bdd6d053d8ecf9088b23244088ee56cbae1ad434f495909f6` |
| `scripts/check_prime_coord_factor_blind_benchmark_suite_independent.py` | `746077e8dcf4499593ad32e5b9434e2d471e86b0` | `393bfa792f0c39b719c53e8827b1defd6291bf94e6b3fed3e990bb298636c54c` |
| `research_execution_records/RS-PRIME-COORD-FACTOR-BLIND-BENCHMARK-SUITE/ER-094BC1B3B7B33E82CBCF.json` | `176d910a1621cfd9613235eaa715fd2c1935de87` | `a21fbbd0009c033617afab38d5f32068fc0615f28450608624e609b640b48747` |

The two checker files were independently reconstructed from the frozen Git contents before execution and verified locally with `git hash-object`; both reconstructed blob IDs exactly matched the pinned source blobs above.

## 3. Authoring replay

The exact frozen main checker was run against the exact frozen independent worker/verifier.

Fresh replay result:

- schema: `PCF2_SEALED_BENCHMARK_V1`
- verdict: `BENCHMARK_FROZEN_AND_SEALED`
- corpus cases: `89`
- adversarial families: `8`
- bit bands: `3` (`B05_12`, `B13_16`, `B17_20`)
- benchmark rows: `534`
- successful exact splits across all rows: `458`
- deliberate leakage/adaptive attacks rejected: `6/6`
- private factors serialized to candidate worker: `false`

The freshly generated full report is exactly `271,966` bytes and has

`sha256:d5cde066e23c42838e080d4cdcd05ce1d0ea8a336c85870bf17ca5ecc21793c4`.

That byte count and SHA-256 exactly equal the frozen generation-2 compact summary pin. This is a byte-level replay equality for the full generated report, not merely an aggregate-score comparison.

## 4. Score-by-score zero-drift check

Fresh exact successes:

- Prime Fusion public quadratic gcd probes: `74/89`; failures `15` = `NO_NONTRIVIAL_GCD_IN_PUBLIC_SEED_BUDGET`; total ops `17,088`.
- Prime Fusion public sixth-power gcd probes: `84/89`; failures `5` = `SYNCHRONIZED_OR_TRIVIAL_ONLY`; total ops `17,088`.
- trial division: `89/89`; total ops `4,445`.
- Fermat with frozen `4096` step budget: `83/89`; failures `6` = `STEP_BUDGET_EXHAUSTED`; total ops `30,659`.
- fixed-schedule Pollard rho: `89/89`; total ops `1,584`.
- Pollard p-1 with frozen `B1=256`: `39/89`; failures `50` = `B1_BASE_BUDGET_EXHAUSTED`; total ops `77,520`.

Every value above equals the frozen generation-2 benchmark summary. No retuning or postselection occurred.

## 5. Independent verifier replay

The exact frozen independent verifier was run on the freshly generated full report and returned `PCF2_INDEPENDENT_REPORT_VERIFY_V1 / PASS`.

It independently recounted all six algorithms and verified every one of the `458` successful rows satisfies

`1 < d < N` and `N % d == 0`.

It also rechecked:

- exact algorithm set;
- all eight required adversarial families;
- all three frozen bit bands;
- no private-factor fields in public corpus rows;
- failed rows carry no factor;
- all aggregate success, operation, preprocessing and seed-amplification values;
- leakage rejection completeness;
- deterministic worker replay.

## 6. Evidence boundary preserved

This recovery does not promote finite benchmark evidence into a factorization theorem or speedup result.

The operation counters remain algorithm-local exact proxies. They are not interchangeable wall-clock units. The 89-case corpus remains a regression/falsification surface only.

Candidate execution remains factor-blind: the worker receives exactly `N`, independent public seed, candidate id and precommitted public parameters. Hidden factors remain private verifier state.

Future N-only extractors may consume this benchmark only through a separately authorized benchmark generation; this generation must not be edited or retuned to admit them.

## 7. Hard-target disposition

Hard target:

`PCF2_SEALED_FACTOR_BLIND_BENCHMARK_REFROZEN_WITH_COMPLETE_DIGEST_CHAIN_AND_ZERO_SCORE_DRIFT`

Disposition:

`ACHIEVED`

There is no unresolved mathematical or benchmark-content residue inside this integrity-recovery task. The only remaining control-plane action is Driver review of the new immutable Result and its complete output manifest.

Recommended Driver disposition:

`ACCEPTED / TASK-TERMINAL / BENCHMARK_CONTROL_SURFACE`

No Foundation mutation, Working Truth grant, theorem promotion, factoring-speedup claim, corpus extension, or score change follows from this Result.
