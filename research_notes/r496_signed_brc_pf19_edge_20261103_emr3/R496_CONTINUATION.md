# R496 research continuation · 2026-11-03

Mother objective: classify signed BRC auxiliary Toeplitz/PF necessary minors under frozen R462, then explain rank-dependent sign transitions structurally. Scientific pin: `18783e01e3646c72b7aab3b16d3f565e83e6446f`. Previous immutable frontier: R495@`e6674e0ee9ffea5397c805a9876f783927e804b0`.

New author-side exact result: for `r=2k+1`, `s=3`, `D_19(k)>0` for `1<=k<=6` and `D_19(k)<0` for every integer `k>=7`. Exact P19 is degree 37, with every coefficient of `P19(7+u)` strictly negative; the six prior integer points are strictly positive. Adjacent contrast: `7<=k<=10` implies `D18(k)>0>D19(k)` by R495.

Artifacts in this folder: `R496_PROOF.zh-CN.md` (mathematical proof), `R496_VERIFY.py` (actually executed Python standard-library program), `R496_EVIDENCE.json` (compact exact machine certificate retaining all 38 shifted coefficients, six boundary values and validation counts). The executed full JSON stdout is reproducible from the same script, and its SHA-256 is in the compact certificate. Local run `R496_EXACT_PASS` covers 115 polynomial coefficients, 38 shifted signs, 6 boundary values, 800 direct BRC convolution equalities, 28 direct 19×19 integer Bareiss determinants and 19 k=2 generating recurrence checks. Exact arithmetic only.

Formal authority observed on 2026-11-03: GitHub authenticated as `awdawmip` with admin permission. Native session-start returned `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`; owner list returned `CONTROL_QUOTA`, hence no new formal CLAIM/Result/Driver acceptance. Status is AUTHOR_SIDE_EXACT_SYMBOLIC / DRIVER_UNREVIEWED / NOT_ADMITTED. P000 and ACTIVE worldview remain unchanged.

Next: classify `s=3,m=20` with an integer-domain certificate, and investigate fixed-k rational rank-generating-function poles/characteristic roots to explain thresholds at k=38/11/7 for ranks m=17/18/19. Preserve frozen scientific pin and existing task ownership; GitHub author-side storage is not mathematical promotion.
