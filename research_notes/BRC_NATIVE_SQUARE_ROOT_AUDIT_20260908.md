# Exact native square-root preparation

Researcher: `EM-HME-0CE4FD / TASK_RESEARCH`  
Global read snapshot: `b2d9ceff961c70ecb356721aafcb03d31396daeb`  
Project parent: `0ba74daea4992becd19b9cc5aaed08854eae729d`  
Status: tested implementation change and fixed-input arithmetic audit; no new public factor.

## Change and reason

Square-root preparation was still routed through the general integer_nth_root binary search. Its Python doubling/search loops dominated the preceding complete-cost observations. The library already uses math.isqrt for testing prepared square gaps.

The change imports math.isqrt in src/enterprise_math/core.py and dispatches p==2 to it after the existing argument validation and trivial cases. This is five added source lines. Existing signatures, ValueError guards, n=0/1 behavior, the p=1 identity and the p>2 algorithm are retained.

The optimization reuses an exact integer primitive. It does not introduce floating-point approximation, a multiplier order, a new factor-search route or a new mathematical factoring result. Python >=3.11 is already the project's declared requirement.

Source identities:
- Baseline core Git blob: cdb8ace10e4cc8bba13b70f4da306313efb24819.
- Candidate core Git blob: 2b7ab070868ef4a2b6d8b33f5e3bc69dbac62c07.
- Baseline normalized SHA-256: d2814d1d31eb195905f05136f250fcac2232b8cfc7dc6c9797000733ddebe636.
- Candidate normalized SHA-256: 4cffb67323365690e1029678a6fe1bff74566d8fb5b50203880ba642f332c9ed.

Both the project parent and current main had the baseline core blob when inspected. The candidate was prepared in a separate local worktree. The old execution checkout remains available for the paired baseline.

Reuse resolution: EXTEND_EXISTING_TOOL. The square-gap and ordering API source files are unchanged; the common square-root dependency is the changed implementation.

## Mathematical and input contracts

integer_nth_root(n,2) specifies the unique integer k satisfying

    k^2 <= n < (k+1)^2.

That is the exact integer-square-root contract used by isqrt. Replacing the computation preserves k, hence also its collapse k^2, scaled-root projections, and derived BRC state coordinates. Nonnegative integer validation is performed before the new branch, so bool, float, string, negative and missing-type values are not newly accepted through the standard-library function.

The two added tests cover 20 exact square-basin boundary cases, using roots through 4096 bits and targets through 8192 bits. They test k^2-1, k^2, k^2+2k and (k+1)^2 directly against k-1,k,k,k+1. Additional cases preserve the wrapper's ValueError behavior for six invalid n values and seven invalid p values.

The existing characterization, exact powers, monotonicity, collapse idempotence, scale compatibility and source-level no-float/no-true-division checks remain in force. The existing p=1 through p=5 tests also exercise the unchanged other-exponent path.

## Reused public state evidence

The audit consumes the original three public mathematical puzzle integers, the 60-position frozen-prefix certificate and the six later root-projected positions. No new public position or square-witness query is added.

Input Git blobs:
- brc_public_rsa_fixed_predicates_20260908.json: e56cfc8457e2398b5de3c90182c2b37824580ef3.
- brc_public_frozen_prefix_20260908.json: c4b201e608167cfff96c5a141bd9e26b575dad69.
- brc_materialized_gap_order_20260908.json: 9a866dd4a923fa046768346c3ce0f1f49f4dc73c.

Each variant reconstructs the same 22 saved states per public input through the unchanged ceiling_completion_cost API. The timer includes target multiplication, root calculation, ceiling/gap formation and the caller's fixed list construction. The exact saved gap, floor/ceiling bounds, derived remainder and original D/U label are checked outside the timer. Full state digests agree across both variants and every round.

| Public mathematical input | Saved states | Baseline median, ms | Candidate median, ms | Baseline / candidate | Candidate faster |
|---|---:|---:|---:|---:|---:|
| RSA-270 | 22 | 8.2885 | 0.0967 | 85.71x | 7/7 |
| RSA-896 | 22 | 8.3888 | 0.0827 | 101.44x | 7/7 |
| RSA-2048 | 22 | 44.1573 | 0.1845 | 239.33x | 7/7 |

These numbers measure preparation of an existing batch, not total factorization time. The 66 unique public states remain the same; their square-witness statuses are inherited from the earlier certificates. No fresh public square filter or factor recovery is performed by this benchmark.

Seven paired rounds in fresh processes give 924 reconstructions of those same 66 states. Repetition is timing and equivalence evidence, not extra candidate coverage.

## Complete-cost constructive evidence

The same three previously prescribed positive inputs are reused:

    N=t(2t+1), t odd,
    t=2^((B-2)/2)+1, B in {896,2048,8192},
    8N=(4t+1)^2-1 and gcd(N,4t)=t.

Their large factors are not asserted prime. They are structured positive controls rather than a measured public-puzzle success population.

Both versions call the identical source witness API at the same fixed positions m=1 and m=8. The first output is None and the second is (4t+1,1). Target-root preparation, the unchanged default 4032 filter, gcd extraction and exact product verification are all inside the timer. The validated factor is the same t.

| Constructed N bits | Baseline median, ms | Candidate median, ms | Baseline / candidate | Candidate faster |
|---|---:|---:|---:|---:|
| 896 | 0.7574 | 0.0234 | 32.37x | 7/7 |
| 2048 | 3.9680 | 0.0320 | 124.00x | 7/7 |
| 8192 | 131.2545 | 0.2272 | 577.70x | 7/7 |

The comparison changes only the common square-root implementation. It does not change the fixed two positions, expose t to the computation before factor verification, or substitute a cheaper unverified output.

The seven paired rounds perform 84 source witness calls on the same three constructive inputs. Fourteen small warmup calls occur separately, outside all measured paths. These repetitions are not independent new successes and are not fed into adaptive routing statistics.

The ratios are relative to this repository's former general binary-search implementation on CPython 3.14.6 / Windows. They do not establish the same gain over other optimized root libraries or a new number-theoretic shortcut.

## Verification and timing isolation

Forty-six selected tests passed:

- test_core;
- test_brc_square_gap_prefilter;
- test_brc_multiplier_basin;
- test_brc_multiplier_priority_jump;
- test_brc_opportunistic_shortcuts.

This includes the two added contract tests and the existing direct consumers. It is a targeted test run, not a full-repository CI assertion. The benchmark JSON's unit-test section records that separately performed run; the benchmark script itself does not execute those suites.

Each variant and round uses a fresh child process. The worker verifies exact core/helper/input blobs, imports from the selected checkout, and checks that the square-gap API points to that imported core function. There is no runtime monkeypatch or mixed baseline/candidate module state. Round order is shuffled by a fixed seed.

Interpreter startup, imports, source/input verification, one warmup, fixture construction, post-timer state auditing and serialization are outside the measured paths. Their exclusion does not remove root acquisition from the timed APIs. All raw per-round measurements are retained. The complete audit command took about 6.64 seconds.

Unchanged helper blobs:
- brc_square_gap_prefilter.py: 42d4e9a397b56d9d371f034780ffc736d43e6d96.
- brc_opportunistic_shortcuts.py: 1214aa09770893fb3de7f85b994d1994ff56bffe.

## Reproduction and scope

Run the listed unit suites against the candidate source, then run:

    python experiments/brc_native_square_root_audit_20260908.py --baseline-root BASELINE_CHECKOUT --candidate-root CANDIDATE_CHECKOUT --output-dir experiments

The script requires the exact core blobs above and the three pinned input JSON files beside it. Its root-path arguments choose verified source implementations; they do not accept a new mathematical target.

Local source snapshots used for this run:
- baseline: D:\em\control-h0o-frozen-result-source-20260908;
- candidate: D:\em\TEMP\brc-hidden-moment-20260908-0ce4fd\native-root-checkout.

The candidate is an isolated worktree based on local 7fc2aecb9242034b8364792f5c5010d009df1117, with the two source/test changes only. Exact relevant source equality with the project parent was checked before publication.

Earlier timing certificates remain historical measurements of their recorded source snapshots. Reproducing them against a newer core would measure a different implementation and must not be used to reinterpret those earlier results.

The useful outcome is a substantially cheaper exact arithmetic preparation step with preserved contracts and positive witnesses. State separation, fixed-budget observations and the broader unfinished research objective remain intact. No public RSA factorization is claimed.
