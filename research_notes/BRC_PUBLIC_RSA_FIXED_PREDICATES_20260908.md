# Fixed public RSA puzzle observations under the existing shortcut contracts

Researcher: `EM-HME-0CE4FD / TASK_RESEARCH`  
Status: completed fixed mathematical observations; no factor recovered.  
Global snapshot: `e76fdc883f9f4a3a93c1284340e38c55aeba0a6a`.  
Parent project frontier: `e0b6dcdf746a93b652c32d23db913c6e9f9dbf86`.

## Current user instruction and scope

The user explicitly added: use published RSA challenges as test targets, only verifying shortcut algorithms. This checkpoint performs that requested transition from constructed small integers to three fixed public mathematical challenge integers. It tests the existing identities once each, with no parameter expansion after the result.

The sources are author-attributed RSA Inc challenge PDFs hosted by MysteryTwister. Their introduction records RSA Inc's permission to host the challenges. Only the published integers are used; no key material, service endpoint, ciphertext or external system is involved.

| Literal fixture | Decimal digits | Measured bits | Exact source, page 3 |
|---|---:|---:|---|
| RSA-270 | 270 | 895 | [RSA-270 challenge](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-09-en.pdf) |
| RSA-896 | 270 | 896 | [RSA-896 challenge](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-10-en.pdf) |
| RSA-2048 | 617 | 2048 | [RSA-2048 challenge](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-38-en.pdf) |

The PDFs were read on 2026-09-08. Decimal blocks preserve their source line boundaries; the certificate stores the concatenated integer and its ASCII decimal SHA-256. RSA-270 and RSA-896 are distinct integers despite having the same decimal length. This experiment does not make a current global claim about which challenge numbers remain unfactored.

## Frozen reuse and observation budget

The existing sources are executed unchanged, with their exact local SHA-256 checked before use:

- `brc_multiplier_basin.point_cost_state`: separate `(J,R,A)` annotation;
- `brc_square_gap_prefilter.ceiling_completion_square_witness(N,1)`: one immediate-completion call;
- `brc_neighbor_square_lift_shortcut.neighbor_square_parameters`: the same fixed `a=8` parameter identity, reachable only if `N mod 64` is 1 or 63.

The parameter identity is first checked on its previously certified positive construction `17473`; the immediate-completion API is checked on `299=13*23`. These controls warm imports/caches and confirm the interfaces before the public observations. The neighbor helper is not invoked on a public fixture when its prerequisite gate fails.

Each public integer receives exactly one ceiling position and one fixed low-bit gate. A qualifying neighbor gate would receive at most one sign and one exact parameter-square test. The executable has no external-integer argument, multiplier sweep, advancing ceiling, adaptive retry or factor-search fallback. It performs no timing repetitions.

The existing bounded lookup keeps its `A<=510` contract. The fixed-residual recurrence keeps its complete-interval reuse contract. One public integer can be viewed as a singleton indexed interval after computing J and R; that gives the same immediate-completion predicate and supplies no multi-position reuse benefit.

## Observed outcomes, with directions kept separate

As before, D means `R<=J` and U means `R>J`; the canonical collapse is downward in both cases.

| Public fixture | Initial cost direction | Direct completion | N mod 64 | Fixed a=8 observation |
|---|---|---|---:|---|
| RSA-270 | U | No witness at this ceiling | 55 | Gate not met |
| RSA-896 | U | No witness at this ceiling | 15 | Gate not met |
| RSA-2048 | D | No witness at this ceiling | 37 | Gate not met |

The independent native square check agrees with every direct API output. All three neighbor gates terminate before the lifted parameter-square test. All three completion gaps exceed the bounded lookup's range. No factor was recovered or submitted.

These outcomes describe these six fixed observations. They do not refute a general route, change the retained positive constructions or justify expanding parameters without a separately declared cost. The prior 406-input coverage remains its own population, as do the indexed-fiber success and timing results.

## Recorded single-observation costs

The host uses CPython 3.14.6 on Windows. These are single measurements on a warmed imported runtime, not a stable benchmark or end-to-end factorization speedup.

| Public fixture | Separate state annotation, ms | Direct API call, ms | Fixed a=8 gate record, microseconds |
|---|---:|---:|---:|
| RSA-270 | 0.4005 | 0.3750 | 1.3 |
| RSA-896 | 0.3779 | 0.3883 | 1.0 |
| RSA-2048 | 2.0236 | 1.9996 | 0.9 |

The three direct calls and three gate records total about 2.7661 ms in this run. Direction annotation is a separate measured cost, about 2.8020 ms total, and is not a prerequisite of the low-bit gate. The direct timer covers the unchanged API; the independent audit is outside it. The gate timer includes creation of its small result record. Source acquisition, imports, positive controls and serialization are outside these timers. The complete command finished in about 0.95 seconds on this host.

## Reproduction and next boundary

```powershell
python experiments/brc_public_rsa_fixed_predicates_20260908.py --enterprise-root . --output-dir experiments
```

The companion JSON contains the literal public inputs, exact source URLs/hashes, positive controls, D/U metadata, outcomes, operation budgets and timing scopes. A subsequent wording-only clarification describes the singleton fiber correctly; it does not alter the observed calculations or rerun them.

Retain the low-cost fixed observations and the positive families already established. This is an actual public-puzzle validation of the selected shortcut conditions, with no success on these three instances. It is not a test of every method in the larger library and does not establish RSA factorization effectiveness. The updated research goal remains active. Further work should preserve explicit input prerequisites and measured costs; no larger scan was launched from these outcomes.
