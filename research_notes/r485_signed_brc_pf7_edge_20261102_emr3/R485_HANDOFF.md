# R485 portable research handoff — 2026-11-02

Frozen R462 scientific pin: 18783e01e3646c72b7aab3b16d3f565e83e6446f. R484→R485 advances the signed BRC auxiliary scalar, right edge s=3, Toeplitz rank m=7. P000, ACTIVE worldview and X6 untouched.

Exact author-side theorem: for every integer k>=1, D7(2k+1,2k-2)>0 for k=1..5 and D7<0 for all k>=6. This follows from the fully verified 43-coefficient Q[k] identity and the 14 strictly positive coefficients of P7(6+u), plus the five finite boundary signs. The first negative at r=13 matches R484 rank-six threshold. This is a scalar PF7 obstruction, not a native spatial theorem.

Artifacts: R485_PROOF.zh-CN.md (full derivation), R485_VERIFY.py (locally executed standard-library verifier), R485_EVIDENCE.json (matching captured computation). Run: python R485_VERIFY.py > R485_EVIDENCE.json. Exact verification covers 800 original convolution inputs, 28 direct 7x7 determinants, four 5040-permutation checks; no floating point.

Status: AUTHOR_SIDE_EXACT_SYMBOLIC / DRIVER_UNREVIEWED / NOT_ADMITTED. Authenticated GitHub account awdawmip has repository write permission. Native research session is denied STATIC_READONLY_SCOPE_DENIED; canonical owner query returned CONTROL_QUOTA, so no CLAIM/Result/Driver authority asserted. Publication to this draft PR is Source persistence.

Next discriminating research unit: s=3,m=8, classify exact first-negative k using Hessenberg recurrence, and compare the m=5,6,7,8 thresholds. Alternate: s>=65,m=4 Newton coefficients.
