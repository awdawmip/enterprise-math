# R47 exact execution evidence (2026-11-10)

Frozen input `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. R46 reference commit `99bff704811c7bf39eafb3717c8f1b4dbc6659eb`. All calculations use Python standard-library exact integer/rational-enclosure arithmetic, with no floating point comparisons.

```text
python R47_VERIFY.py
GAP 224 LO 7063970631381752664458 HI 7063970631381752664561 deltaLO 5525221276560321237554 deltaHI 5525221276560321237493 max_pair (60, 163)
GAP 225 LO 5525221276560321237554 HI 5525221276560321237493 deltaLO 5525221276560321237554 deltaHI 5525221276560321237493 max_pair (164, 103)
GAP 388 LO 5525221276560321237554 HI 5525221276560321237493 deltaLO 5525221276560321237554 deltaHI 5525221276560321237493 max_pair (224, 163)
GAP 389 LO 3986471921738889810650 HI 3986471921738889810425 deltaLO 5525221276560321237554 deltaHI 5525221276560321237493 max_pair (328, 103)
PASS_R47_SHARP_UNIFORM_H_225 strict389 [103, 42] [164, 103]
PASS_R47_225_SUFFIX_298_RUNS stages 78 positive 9697 sha256 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6

python VERIFY_R47_COMPACT.py
PASS_R47_SHARP_ALL_OFFSETS_225_AND_FAILURE_224
PASS_R47_225_SUFFIX_298_RUNS 298 updates 9697 sha256 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6

python AUXILIARY_R47.py
AUX_PASS 4 minimal_uniform_H 7 Hminus1_failure_J -599 Hminus1_failures_in_1201_offsets 172
AUX_PASS 7 minimal_uniform_H 17 Hminus1_failure_J -600 Hminus1_failures_in_1201_offsets 71
AUX_PASS 13 minimal_uniform_H 41 Hminus1_failure_J -536 Hminus1_failures_in_1201_offsets 15
AUX_PASS 21 minimal_uniform_H 41 Hminus1_failure_J -536 Hminus1_failures_in_1201_offsets 135
```

Exact emitted TSV comparison: `AFFINE_RUNS_R47.tsv` = frozen R46 reference and R32 oracle byte-for-byte; 15,356 bytes; SHA-256 `2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6`.

This PR contains independently executable `VERIFY_R47_COMPACT.py` (derived from published R46 code with sharp cover check). The complete author execution bundle additionally preserves `R47_VERIFY.py`, `AUXILIARY_R47.py`, `CERTIFICATE_R47.json`, regenerated `AFFINE_RUNS_R47.tsv`, full proof, this evidence and R48 continuation. Author validation is not independent mathematical review or shared Task Result publication.
