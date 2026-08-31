# Prime Coordinate Factor-Blind Benchmark Suite — Research Return

Status: `FROZEN / AWAITING DRIVER REVIEW`

Task-ID: `RS-PRIME-COORD-FACTOR-BLIND-BENCHMARK-SUITE`  
Publication-ID: `TP2-FDEB9BE4503CD9C60E59`  
Researcher-ID: `EM-PCF2-4B7C91`  
Claim-ID: `chatgpt-pcf2-20260827-1954`  
Execution record: `ER-97B97A7AE289CE4C53E9`  
Claim base: `c2288fb4976d0ca9cddb28b28edada816f8ca4ff`

## 1. Frozen verdict

`BENCHMARK_FROZEN_AND_SEALED`

Hard target `NBLIND_FACTORIZATION_BENCHMARK_SUITE_FROZEN` is met at task-local benchmark/control-surface strength.

This return freezes a deterministic dual-compartment factorization benchmark in which candidate execution receives only

\[
\operatorname{Run}(N,s,\theta_{\mathrm{public}})
\]

with `N`, an independent public seed, a predeclared candidate identifier and parameters frozen before the hidden factorization is exposed. Hidden factors are retained only by the private corpus/verifier compartment.

A run is counted as a successful split only when the verifier checks exactly

\[
1<d<N,\qquad d\mid N.
\]

No coordinate concentration, factor classification after factors are known, or whole-modulus gcd `d=N` counts as success.

This result freezes the benchmark. It does **not** establish or rank mathematical truth, prove a factorization theorem, or claim a factorization speedup.

## 2. PCF1 constructor boundary consumed

The accepted PCF1 information-leakage audit is the constructor authority for this task.

Candidate-side permitted inputs are only:

- the public composite `N`;
- an independent public seed;
- a fixed algorithm identifier;
- public parameters frozen independently of the hidden factorization.

The following are rejected as constructor inputs unless separately reconstructed from `N` by an admitted algorithm:

- hidden factors `p,q`;
- factor-labelled coordinates;
- factor-derived phases;
- CRT idempotents;
- prime-labelled `M_{p,q}` objects;
- postselected roots or factor-conditioned channel data;
- answer-dependent/adaptive tuning fields.

The suite intentionally keeps the private factor ledger in the parent verifier and executes Enterprise candidates in a separate worker process whose request schema has exactly five fields:

`schema, candidate_id, n, seed, public_parameters`.

## 3. Deterministic corpus

The frozen corpus contains `89` distinct composite cases spanning all eight required adversarial families:

1. `balanced_semiprime`;
2. `unbalanced_semiprime`;
3. `near_twin_semiprime`;
4. `prime_power`;
5. `multi_prime`;
6. `carmichael`;
7. `strong_pseudoprime_base2`;
8. `coordinate_collision`.

The public cases span three bit-length bands:

- `B05_12`;
- `B13_16`;
- `B17_20`.

The public corpus contains only:

`case_id, n, family, bit_length, band`.

The private factor ledger is separately hashed and is never serialized into a candidate request.

Frozen public-corpus SHA-256:

`fa4c6278e31660a1e1159e37e575f2c603d28934796466a730ca0e1bf725626b`.

Frozen private-verifier-ledger SHA-256:

`f1a0096305101fafb1269b861470220dac40cd502ef4c4987b640b9efa1bd54a`.

## 4. Enterprise candidates

PCF1 admitted two public-seed Prime Fusion gcd-probe families as N-blind enumerative extraction baselines. PCF2 freezes them without modifying their formulas or tuning them to this corpus.

### 4.1 Public quadratic probes

For public `x=s mod N`, evaluate

\[
\gcd(N,x^2+1),\qquad
\gcd(N,x^2+x+1).
\]

With the precommitted public seed set `s=0,...,63`:

- cases: `89`;
- exact nontrivial splits: `74`;
- failures: `15`;
- exact failure class: `NO_NONTRIVIAL_GCD_IN_PUBLIC_SEED_BUDGET`;
- failure families:
  - balanced semiprime: `2`;
  - near-twin semiprime: `3`;
  - prime power: `2`;
  - unbalanced semiprime: `8`;
- candidate-local operation proxy: `17,088`;
- gcd calls: `11,392`;
- successful seed-amplification aggregate: `861 / 74`.

Thus the fixed 64-seed quadratic probe is genuinely extractive on many bounded cases, but it is not a universal extractor even on this finite corpus.

### 4.2 Public sixth-power probes

For public `x=s mod N`, evaluate

\[
\gcd(N,x^6-1),\qquad
\gcd(N,x^6+1).
\]

Under the same fixed 64-seed budget:

- cases: `89`;
- exact nontrivial splits: `84`;
- failures: `5`;
- exact failure class: `SYNCHRONIZED_OR_TRIVIAL_ONLY`;
- failure families:
  - balanced semiprime: `2`;
  - near-twin semiprime: `3`;
- candidate-local operation proxy: `17,088`;
- gcd calls: `11,392`;
- successful seed-amplification aggregate: `927 / 84`.

The sixth-power family is materially stronger on this finite corpus than the quadratic public probe, but the five exact synchronization/triviality failures prevent any universal claim.

## 5. Classical baselines

All baseline parameters are frozen before corpus execution.

### Trial division

- exact splits: `89 / 89`;
- operation proxy: `4,445`;
- no benchmark failures.

### Fermat-style search

Frozen step budget: `4,096`.

- exact splits: `83 / 89`;
- failures: `6`;
- all six failures occur in `unbalanced_semiprime`;
- exact failure class: `STEP_BUDGET_EXHAUSTED`;
- operation proxy: `30,659`.

### Pollard rho

Frozen public parameter schedule:

- seeds: `[2,3,5,7,11]`;
- maximum `4,096` steps per attempt.

Results:

- exact splits: `89 / 89`;
- operation proxy: `1,584`;
- gcd calls: `528`;
- successful attempt-amplification aggregate: `95 / 89`;
- no benchmark failures.

### Pollard p-1

Frozen public parameters:

- bases: `[2,3,5,7]`;
- `B1=256`.

Results:

- exact splits: `39 / 89`;
- failures: `50`;
- exact failure class: `B1_BASE_BUDGET_EXHAUSTED`;
- operation proxy: `77,520`;
- gcd calls: `304`;
- successful attempt-amplification aggregate: `104 / 39`.

The raw `ops` counters are **algorithm-local exact machine-cost proxies**. They are not asserted to be interchangeable wall-clock units across different algorithms. Accordingly this return does not infer cross-algorithm asymptotic superiority from those raw totals.

## 6. Leakage and replay gates

The sealed worker was attacked deliberately with six forbidden payload patterns:

1. top-level `factors`;
2. top-level `p`;
3. top-level `q`;
4. nested `factorization`;
5. nested factor-derived `phase_p`;
6. nested `adaptive`.

Result:

`6 / 6 REJECTED`.

The same valid worker request was also replayed twice under a minimal environment and produced byte-identical output.

The independent checker then reopens only the **public** benchmark report and separately verifies:

- all eight mandatory families are present;
- at least three bit bands are present;
- no private factor field exists in public corpus rows;
- the algorithm set is exactly the two admitted Enterprise candidates plus four required baselines;
- every claimed successful row satisfies exact nontrivial divisibility;
- failure rows do not smuggle a factor;
- aggregate success, operation, preprocessing and seed-amplification counts recompute exactly;
- leakage rejection is complete;
- deterministic replay is true.

Authoring replay:

`python scripts/check_prime_coord_factor_blind_benchmark_suite.py --out /tmp/pcf2_report.json`

Independent verification:

`python scripts/check_prime_coord_factor_blind_benchmark_suite_independent.py --verify-report /tmp/pcf2_report.json`

Final full-report authoring digest:

`sha256:d5cde066e23c42838e080d4cdcd05ce1d0ea8a336c85870bf17ca5ecc21793c4`.

Full report size:

`271,966` bytes.

The full report is reproducible from the frozen scripts/parameter manifest rather than checked in as a large duplicated artifact; the compact result summary pins its digest and all load-bearing aggregate values.

## 7. Frozen artifacts

Primary runner:

`scripts/check_prime_coord_factor_blind_benchmark_suite.py`

Independent worker/verifier:

`scripts/check_prime_coord_factor_blind_benchmark_suite_independent.py`

Versioned public parameters:

`research_artifacts/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE/parameter_manifest.json`

Replay/result schema:

`research_artifacts/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE/replay_schema.json`

Compact frozen result:

`research_artifacts/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE/benchmark_result_summary.json`

Execution provenance:

`research_execution_records/RS-PRIME-COORD-FACTOR-BLIND-BENCHMARK-SUITE/ER-97B97A7AE289CE4C53E9.json`

## 8. Source and dependency pins

Operational publication:

`TP2-FDEB9BE4503CD9C60E59`.

Generation-2 taskbook blob:

`sha1:2edc7e86dad982e3e7a4fb10d21c21ef984e290e`.

Generation-1 taskbook blob:

`sha1:042229f1401ba83813ff55e5caccc7f47b97512a`.

Accepted PCF1 result:

`RR-B8D8679EB033E990E825`.

PCF1 result-record blob:

`sha1:5962795e98743cf8b5dba3fcfc043f508bda34a4`.

PCF1 return blob:

`sha1:650a01f59534f2652b033873cc7c4dcd8038723a`.

PCF1 Driver-review blob:

`sha1:b1bef218c80e5979a5de8f8b0c95ac2317857bf4`.

Execution claim base:

`c2288fb4976d0ca9cddb28b28edada816f8ca4ff`.

## 9. Exact scope of what is closed

PCF2 closes the benchmark-construction question:

- deterministic corpus generation: complete;
- private/public compartment separation: complete;
- strict N-only candidate schema: complete;
- deliberate leakage rejection: complete;
- exact verifier: complete;
- required classical baselines: complete;
- versioned parameter manifest: complete;
- machine-readable replay/result schema: complete;
- required adversarial families and multiple bit bands: complete;
- independent verification: complete.

Therefore the strongest task-local verdict is:

\[
\boxed{\texttt{BENCHMARK_FROZEN_AND_SEALED}}.
\]

There is no unresolved blocker inside the benchmark task itself.

The exact residual questions are **external** to PCF2: whether a particular candidate has a universal theorem, whether an N-only extractor beats classical baselines asymptotically, how the hidden-factor separation spectrum should be classified, and whether newly reviewed candidates should be admitted into a later benchmark generation.

## 10. Driver recommendation

Recommended disposition:

`ACCEPT / TASK-TERMINAL / BENCHMARK_CONTROL_SURFACE`.

If accepted, downstream candidate tasks may consume this frozen runner without changing its corpus or tuning parameters inside a scored run. New candidates should be added only by a new authorized benchmark generation or an explicitly versioned parameter extension.

The exact current evidence recommends two program-level uses:

1. feed PCF3/related separation analysis with the frozen failure families rather than relying on concentration plots;
2. if the N-only valuation-wall extractor is separately Driver-accepted, benchmark it in a new authorized generation against these same baseline rules, preserving its no-speedup boundary.

No Foundation mutation, Working Truth grant, mathematical theorem promotion, or factorization-speedup claim follows from PCF2.
