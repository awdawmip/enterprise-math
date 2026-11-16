# R493 — portable continuation frontier

Date: 2026-11-03. Frozen scientific input R462@18783e01e3646c72b7aab3b16d3f565e83e6446f; inherited author-side R492@192ede387293adc0a24f9f71f4f7d0abd36703f5. Current object: exact signed BRC auxiliary scalar H_k(t), odd r=2k+1, right-edge s=3, positive integer k, neighboring Toeplitz determinant rank 16. Do not modify P000, ACTIVE worldview, or the frozen pin.

NEW AUTHOR-SIDE EXACT THEOREM: D16(k)>0 for every integer k>=1. Exact factorization f16=G16*P16/N16, deg(P16)=31; P16(5+u) has 32 strictly positive integer coefficients, with minimum 4653192605624148379911623540736; P16(1..4) strictly positive. Full decimal coefficient certificate and values in R493_EVIDENCE.json. R492 D15(6..8)<0 yet D16(6..8)>0.

Rebuild R493_VERIFY.py using Python 3 standard library; actual author-side run returned R493_EXACT_PASS: 97 polynomial identity coefficients, 680 original raw signed BRC convolution matches, 28 independently recomputed original 16x16 integer Bareiss determinants, 64 fixed-k generating-function recurrence matches. Proof in R493_PROOF.zh-CN.md; all exact arithmetic with no floats. Full generated static evidence is in R493_EVIDENCE.json, with big integers serialized as decimal strings.

New structural route: for each fixed k the rank generating function is rational, F_k(z)=1/(1-sum_{ell=1}^{r-2} (-1)^(ell-1)*p_(ell+2)(k)*p2(k)^(ell-1)*z^ell). Next independent unit: exact sign classification for m=17 and first nontrivial pole/recurrence analysis for k>=2, trying to explain rank-dependent sign reversals rather than only collecting thresholds.

Research authority: GitHub actor awdawmip with repo admin, author-side Draft PR artifact storage; native gateway observed static_machine_readonly (em:access, source:read, control:read), write relay disabled, native session-start denied, owner query not conclusively obtained. Do not infer native CLAIM, Result, Driver review, or admission from PR storage. This is a research artifact handoff, not a canonical native Result.
