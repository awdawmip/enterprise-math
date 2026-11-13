# R486 portable handoff — 2026-11-02

Frozen science: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f. Continuation of R485 (s=3,m=7) using its exact Catalan polynomial representation and Hessenberg recurrence. Project P000, ACTIVE worldview, native X6 and source pin unchanged.

**New exact author-side result:** for every integer k≥1, s=3,m=8 right-edge Toeplitz determinant D8(2k+1,2k-2) is strictly positive for k=1..5 or k≥9, strictly negative for k=6,7,8. It is positive again from r=19 onward, whereas the same-position rank-seven determinant is negative for all k≥6 (R485). The 49-coefficient polynomial identity and all 16 positive coefficients of P8(9+u), plus integer boundary checks, prove the claimed entire domain.

Files: R486_PROOF.zh-CN.md (full statement, factors, dependence), R486_VERIFY.py (executed exact stdlib verifier), R486_EVIDENCE.json (captured checks and all sign certificates). Reproduce: `python R486_VERIFY.py`. Verification scope: 900 original convolution inputs, 28 raw 8x8 determinants, two full 40320-permutation crosschecks; no floating point.

Status: AUTHOR_SIDE_EXACT_SYMBOLIC / DRIVER_UNREVIEWED / NOT_ADMITTED; GitHub publication is Source persistence only. Native identity/CLAIM unavailable at this research stage if service continues to report STATIC_READONLY_SCOPE_DENIED / CONTROL_QUOTA; no native Result or Driver authority inferred.

Next discrimination: compute m=9 with p_2,...,p_11, determine exact sign intervals and shifted coefficient certificate, compare whether finite vs infinite negative tails alternate with rank. Keep exact source model; use native X6 bridge only with separately proved observer correspondence.
