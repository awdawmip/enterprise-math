# R487 portable research handoff — 2026-11-02

Frozen science: R462@`18783e01e3646c72b7aab3b16d3f565e83e6446f`; direct source input is the original signed BRC scalar `H(r,t)`. This is author-side auxiliary-scalar research, following R486@`7aacf3dce98af2147263a8b7d0f59e498ae3ef4b`. P000 and ACTIVE worldview remain unchanged.

**New full-domain theorem:** for every integer `k≥1`, the nine-by-nine adjacent right-edge Toeplitz determinant `D9(2k+1,2k-2)>0` at displacement `s=3`. Let `F9=D9/C_k^9`. The exact degree-54 polynomial factorization is `F9=k^9(k+1)^9(k+2)(2k+1)^9(2k+3)^9 P9(k)/120989018964005127936000000000`; `P9` is degree17. All 18 coefficients of `P9(4+u)` are strictly positive and the three cases `k=1,2,3` are explicitly positive. This contrasts with the rank-eight negative window `k=6..8` established in R486. All statements are for this fixed local determinant, not automatic whole-PF9 classification.

Files: `R487_PROOF.zh-CN.md` (theorem, exact P9, proof and dependencies), `R487_VERIFY.py` (executed stdlib verifier), `R487_EVIDENCE.json` (exact coefficients, shifted certificate and test record). Reproduce with `python R487_VERIFY.py > R487_EVIDENCE.json`. The actual run returned `R487_EXACT_PASS`; 55 polynomial coefficients, 18 shifted coefficients, 1000 raw signed-convolution inputs, 27 raw 9x9 determinants, one 362880-term permutation expansion, and 3 rank-eight controls. Arithmetic is exact.

Status: `AUTHOR_SIDE_EXACT_SYMBOLIC / DRIVER_UNREVIEWED / NOT_ADMITTED`; no native CLAIM, Result or independent Driver admission is implied. Current service `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED`, and owner listing returned `CONTROL_QUOTA` in this research run. GitHub authenticated user `awdawmip` has project repository admin/write capability; source PR persistence is separate from native task authority.

**Next smallest unit:** compute and factor the `s=3,m=10` polynomial using the existing Hessenberg recursion, obtain a shifted sign certificate or a precise sign counterexample, then compare ranks 7–10. Preserve frozen scientific model and the unmerged author-side PR branch.
