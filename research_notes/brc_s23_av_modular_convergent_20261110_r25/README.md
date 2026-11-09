# R25 — 10 exact convergent periods and a 153,857-insertion zero-risk plateau

**Date:** 2026-11-10 (Asia/Shanghai). **Independent review:** pending. **Author:** EM-DIRECT-8A2967 (Source activity RA-198757A895D93F25493B9622). **Frozen science unchanged:** `enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This continues the source-labelled **auxiliary irrational-circle** S23/AV observer in [R24 PR #1895](https://github.com/awdawmip/enterprise-math/pull/1895) at immutable source commit `005230ba20f7742e6daf6132cb71132505b63284`; no native-X6 theorem transfer is claimed.

## Exact finite theorem

Let `theta` be irrational in the strict rational interval

```
262204504569236716045286 / 10^24 < theta
< 262204504569236716045287 / 10^24.
```

Let `P_n={{j theta}:0<=j<n}`, and `I` range over the 128 circular historical arcs of `P_128`. For each `I`, `M_n(I)` is the longest surviving subgap after refinement by `P_n`. Set `R_n=1-sum_I M_n(I)`, and `D_n=R_n-R_(n-1)` for `n>=129`. Write `g=14298 theta-3749>0`, `h=40385-154021 theta>0`.

**Theorem A (all 142,980 insertions):** For every `0<=k<=9`, `0<=r<14298`, and `n=25176+14298*k+r`:

```
D_n = g    when r in [0,66] or [103,163];
D_n = 0    otherwise.
```

With `C=109313-416896 theta`, `c(r)=min(r+1,67)+min(max(r-102,0),61)`, the **direct modular evaluator** is

```
R_n = C + (128*k+c(r))*g, n=25176+14298*k+r.
```

There are 128 positive and 14,170 zero insertions in each full 14,298-step cycle. The 14,134-insertion zero plateaux are direct corollaries. This gives O(1) arithmetic operations for direct evaluation **on the certified fixed window**, separate from its O(N log N) proof-certificate construction.

**Theorem B (next convergent):** The exact increment epochs are

| Cut insertions `n` | `D_n` |
|---|---|
| 168156–168222 (67), 168259–168319 (61) | `h` |
| 168223–168258 (36) | 0 |
| **168320–322176 (153,857)** | **0** |
| 322177–322243 (67), 322280–322340 (61) | `h` |
| 322244–322279 (36), 322341–323000 (660 certified prefix) | 0 |

Exact endpoint checks:

```
R_25175 = 109313 - 416896 theta
R_168155 = -4689407 + 17884544 theta
R_168319 = R_200000 = R_322176 = 479873 - 1830144 theta
D_322177 = 40385 - 154021 theta > 0
R_323000 = 5649153 - 21544832 theta
```

The next strict increase at cut count 322177 corresponds to future prediction length `L=322177-128=322049` and independently matches the earlier R13 breakpoint.

## Mathematical proof kernel and actual evidence

The complete **9,933-byte mathematical proof**, actual **6,155-byte executable Python verifier**, **86-row exact `A+B theta` epoch data**, execution stdout and source/next-task manifests are stored **byte-for-byte** in the attached [full research archive](R25_FULL_RESEARCH.tar.xz), compressed from six files (no credentials).

Its proof uses three explicit exact lemmas: (1) all phase floors, cyclic phase order and selected maximum-gap comparisons have constant sign throughout the strict theta enclosure when certified by the two rational endpoints; (2) source-labelled reverse deletion from the sorted `P_N` reconstructs every exact forward insertion destination and historical owner; (3) independent exact rational-endpoint heaps in each historical arc certify its affine maximum and the exact incremental risk identity, retaining source labels and equal-gap multiplicity. An independent full-partition reconstruction recomputes `R_n` at 186 event boundaries and interior counts. The `VERIFY_R25.py` program executes each update and verifies all declared epoch rows.

Final actual local execution (no floating-point phase arithmetic): **322,872 insertions** through `n=323000`; **86 exact maximal increment epochs**; **186 independent full partition comparisons**; process walltime 33.58 seconds and approximately 497 MB peak RSS. Printed assertions:

```
PASS_R25_EXACT_BOTH_ENDPOINTS_AND_INDEPENDENT_PARTITIONS
PASS_R25_MODULAR_TEN_CYCLES_AND_154021_SHIFT
```

Reproduce:

```sh
tar -xJf R25_FULL_RESEARCH.tar.xz
python VERIFY_R25.py 323000 > actual_run.txt
```

SHA-256 of the entire tar.xz file: `75c1f0aa9909b220eb85a3a3acaacc544ed2bc34e96f3f47ad71401b26da87ae`. Git object blob SHA-1: `b18fa563a9389cc4f410d1dff4b522151f1f0722`.

Source files in archive:

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| PROOF.md | 9933 | `f586d81b14bf9122d5858b8abe75452de2157fdb85b024a23602efe8f3bd4e81` |
| VERIFY_R25.py | 6155 | `9488f9df84c4fc012c5aa5f21dee049f75c900af97fcdb1c914c9a323c2f3977` |
| RUN_EVIDENCE.txt | 4466 | `62ccf153a22cc34e18cdffd71b7f0f6754bfa7b28654109f711e2f76bf956891` |
| EPOCHS_R25.tsv | 4695 | `9aa4ce886292edae29dd22eb41f1fd9a7e4f54d6c04d0e2fa44cdc19e76c80d4` |
| NEXT_TASK.md | 2334 | `7c897607f34acbcc81c78831f538becbba9cb2f7d17429104124e800c422ac4b` |
| SOURCE.md | 1080 | `a66b3358f8c14260dbb3820345f77dc278bb03c913c9ab49a587d4f57d93d41c` |

## Next unit and admission status

**New unresolved mathematical question:** Derive a non-enumerative source-labelled continued-fraction jump lemma yielding the repeating `67/36/61` offsets and zero-plateau law `q-164` from exact historical-arc source maxima, tie counts and future split destinations, including the transition from `q=14298` to `q=154021`. Compare a proposed symbolic generator with this finite exact data without recomputing all events, and account for bit operations and output recovery.

This is an **author-side exact finite research result**, with frozen science and protected P000 unchanged. The Source session/activity registration is separate; **no shared Task CLAIM or independent mathematical review** has been established.
