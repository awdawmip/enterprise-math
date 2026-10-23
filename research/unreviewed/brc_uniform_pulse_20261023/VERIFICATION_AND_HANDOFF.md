# N31 author-side verification and successor handoff

**Status:** UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CLAIM.

## Frozen inputs

Global rules: `awdawmip/chatgpt-global-knowledge@c0063368858bfea93f5bda62c8f43039d03a1f0e` (`GLOBAL_KNOWLEDGE_V1`).
Enterprise Math control source: `awdawmip/enterprise-math@af1ac6a8dc1f960a84449366b5ae9cafbae6b7d8`.
Mathematical predecessor: supplied N30 author-side exact certificate and all-position z=1 proof, not an independently reviewed canonical result.

## Scientific delta

Proof in `N31_AUTHOR_THEOREMS.md`: for all n>k>=4, all z in [0,1], fixed single-pulse word 0^(k-1)2 0^(n-k), the exact post-pulse residual increase is [Z_n(z)]_+/3^n. The historical maximum remains frozen by a uniform δ_3=2/3 and δ_t<=2/3−3^(−t) bound. In addition, Z_n has exactly one positive real root for every n>=4, by a uniform coefficient sign-separation argument. This is not a full n=31 all-word classification, nor a native Cell dynamics theorem.

N31 theta bracket checked by exact rational arithmetic:
`0.999999999999985429962090489914281751655992293 < theta_31 < 0.999999999999985429962090489914281751655992294`.

## Actual local verification

Ran the separate, more extensive local Python stdlib file `verify_uniform_pulse.py` from the accompanying conversation evidence ZIP. The run's actual stdout:

```text
COEFFICIENT_IDENTITY_AND_SINGLE_SIGN_CHANGE_PASS m=2..90 coefficients_checked= 4272
INDEPENDENT_MASK_DP_PASS trials= 960 prefix_checks= 12800 increment_checks= 4480 peak_checks= 5440 residual_increment_checks= 4480 z1_residual_checks= 120
ROOT_BRACKET n=30 (999999999999956290911979050955368443431899478/1000000000000000000000000000000000000000000000, 999999999999956290911979050955368443431899479/1000000000000000000000000000000000000000000000); endpoint_signs=PASS
ROOT_BRACKET n=31 (999999999999985429962090489914281751655992293/1000000000000000000000000000000000000000000000, 999999999999985429962090489914281751655992294/1000000000000000000000000000000000000000000000); endpoint_signs=PASS
ROOT_BRACKET n=40 (999999999999999999259727655110802983288274854/1000000000000000000000000000000000000000000000, 999999999999999999259727655110802983288274855/1000000000000000000000000000000000000000000000); endpoint_signs=PASS
RATIONAL_ROOT_GRID_BRACKETS_PASS counts=12 digits=45
OVERALL_EXACT_REGRESSION_PASS
```

Local full Chinese proof SHA-256: `16f998a6fafa22d41a3f343e935017bea8ab1c74fc829f7963ae30acfea066f9`.
Local detailed checker SHA-256: `f4d2aa2ffa7fe9bfba6a9af34133437179059cbc73b96d4bf475810e0d0908a0`.
Local execution log SHA-256: `a3fc8b6788cda7bfc126104a9f1d45493cf3e6a5c8cb88877e570998e5b52d6c`.
Full local evidence ZIP SHA-256: `63b0d4a7a432bedc92b7dcec68039a05654322882796a5d05d46d3efe42db7db`.

The adjacent GitHub `verify_uniform_pulse.py` is a *compact independently executable variant* of the local detailed checker. Its remote bytes were read back, but it was not executed from the GitHub checkout in this run. No unexecuted check is labelled a pass.

## Authorization, publishing and next task

`em_control_dispatch`: CONTROL_QUOTA; `em_control_tasks`: CONTROL_QUOTA; `em_session_start`: STATIC_READONLY_SCOPE_DENIED and operation_sent=false. No authoritative current owner confirmation, claim, native Result, review or promotion. Current branch stores provenance only.

Next scientific unit: a universal non-single-pulse sign criterion or exact counterexample using the count-vector last-increment polynomial while respecting historical order. A separate precise unit is whether theta_n increases monotonically in n; finite root samples alone do not prove monotonicity. The 4-label-to-P000-X6 faithful observer bridge remains open.
