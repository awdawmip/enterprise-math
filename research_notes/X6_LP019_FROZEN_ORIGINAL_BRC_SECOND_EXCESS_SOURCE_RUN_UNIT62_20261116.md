# X6 / LP019 — frozen original signed-BRC executable source, exact first and second backtrack layers (unit 62)

Date: 2026-11-16, Asia/Hong_Kong. Parent task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Research ordinary-control lane `chatgpt-research-onhour-enterprise-math-20260923`; maintenance lane not used.

## Frozen source and execution

Directly fetched, reconstructed and executed the **exact original** `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` from science commit `59538f585d037d09ef687b28715c4bc1a3f9fe03`. Its 2,852-byte content has Git blob SHA-1 `300a96e3dc24bf6fff73743037a0347a8bc83176`; local `git hash-object` matches. P000 V5 and mandatory joint-observer preservation remain in force. No modification to original frozen source or original R063 / Helly benchmark.

Executable publication: `research_checks/X6_SIGNED_NATIVE_BRC_ORIGINAL_SOURCE_PLUS4_UNIT62_20261116.py` Git blob `f34f7ffb7cedf4d1252234255b4c6fa962ba412d`; local SHA256 `fa5cd16e2471d8be122b1bfe0efcac727a633ff7548ef0ad95384d10e45c1ec4`. Machine JSON: `research_checks/X6_SIGNED_NATIVE_BRC_ORIGINAL_SOURCE_PLUS4_UNIT62_RESULTS_20261116.json` Git blob `146446c4ecc26cb78bf25f64f39b1ccbd0a63c7c`, SHA256 `82b04f102c8cc2c43c43780b21e73370de0ac2aabb31ebe3d48eec851e66fc25`.

Both ordinary Python and Python `-O` executions returned **PASS** with identical JSON hash. Runtime checks use explicit exceptions, not optimization-removed `assert`. Independently propagated all twelve signed native axis steps through lengths `m=0,...,6`; **10,364** endpoint/layer comparisons against the original `endpoint_multiplicity(m,z)` succeeded, with the direct walk population `12^m` verified each layer. This is an original frozen producer execution, not a source-only paraphrase.

## New exact second-backtrack identity

For an arbitrary signed six-axis native displacement `z`, put `a_i=|z_i|`, `T=sum_i a_i`, and `B_T(z)=T!/prod_i a_i!`. Exactly two extra positive/negative return pairs may be (i) both placed on one named axis `i`, or (ii) placed on distinct named axes `i,j`. These disjoint cases give

```text
B_(T+4)(z) = B_T(z) * (T+1)(T+2)(T+3)(T+4)
              * [ sum_i 1/{2(a_i+1)(a_i+2)}
                  + sum_{i<j} 1/{(a_i+1)(a_j+1)} ].
```

Every term counts positive natural signed-axis words; no signed amplitude cancellation was taken. Parity forces `B_(T+1)(z)=0`. The first-extra-pair formula from unit61 is reused exactly.

## Full original-source G=25 experiment

For every one of the 7,812 signed six-axis endpoints with `G(z)=sum_i z_i^2=25`, call the **original** `shortest_path_multiplicity`, `endpoint_multiplicity`, and `spatial_norm_squared` for lengths `T,T+1,T+2,T+4`. Independently recompute the first- and second-pair formulas over exact `Fraction`s. All 7,812 endpoints agree. Exact results, grouped by endpoint `(T, support)`:

| T | support | endpoints | shortest B_T | first excess B_(T+2) | second excess B_(T+4) |
|---:|---:|---:|---:|---:|---:|
| 5 | 1 | 12 | 12 | 2,604 | 438,912 |
| 7 | 2 | 120 | 4,200 | 1,345,680 | 295,772,400 |
| 9 | 4 | 2,880 | 10,886,400 | 4,031,596,800 | 951,696,345,600 |
| 11 | 5 | 960 | 399,168,000 | 160,864,704,000 | 39,557,149,632,000 |
| 11 | 6 | 3,840 | 2,128,896,000 | 774,918,144,000 | 179,296,685,568,000 |
| **Total** | | **7,812** | **2,538,954,612** | **939,815,793,084** | **219,805,827,756,912** |

`T+2` is consumed from unit61 (confirmed independently here); `T+4` is the new exact layer. The totals use each endpoint's own `T(z)` and do not represent a single fixed global walk-time shell.

Additional original-source tests: `endpoint_multiplicity(9,(3,0,0,-4,0,0))=11214`; `return_multiplicity(4)=396`. For 32 signed endpoints, imported `endpoint_weight` passed exact sign-reversal+swapped-weight covariance with distinct integer positive/negative weights, unit-weight reduction, and forbidden-parity zero. This directly verifies typed direction/provenance behavior of the original producer.

## Consumer inference and remaining mother objective

The source API supplies exact positive natural word multiplicities, including non-geodesic detours; P022's `sc_geodesic_path_count` and L1-shell total are typed *shortest* path consumers only. A six-axis quadratic `G` observer and an endpoint-specific `T+4` observer require explicit predicate/length transfer. No incorrect historical LP011 singleton-dominant-axis or LP019 signed-subtraction callsite was established by this experiment; preserve both as `UNRESOLVED_PROVENANCE`.

The original R063 frozen six-source 17-gate/512-radius experiment was already actually executed and Source-published (unit50), and original Helly producer likewise (unit54); both are reused here. Exact Source for unit59–61 was read on 2026-11-16 from original request `onhour-20261116-1418-x6-unit59-61-saved-exact-native-progress-v1` as `SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED` with authenticated readback. This unit62 report is author-side **AUTHOR-PROVED / EXECUTED / UNREVIEWED / NOT_ADMITTED** until its own semantic PROGRESS and independent Driver disposition. Remaining: actual historical LP011/LP019 caller lines, 28-LP consumer dependency closure, Driver `REQUEST_REVISION`.

## Reproducibility and source isolation

Published checker refuses a wrong original Git blob before importing; the exact frozen source is read in place. To reproduce, run the checker from a checkout containing its path unchanged. Do not substitute a reimplementation under the same path or alter original frozen science. The new checker/JSON form author-side outputs and do not rewrite accepted historical Result or create a new Task.
