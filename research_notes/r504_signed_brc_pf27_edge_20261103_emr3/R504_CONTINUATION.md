# R504 signed-BRC continuation

Date 2026-11-03; scientific pin R462 `18783e01e3646c72b7aab3b16d3f565e83e6446f`; predecessor R503 `47cf593fc85017e1b80fe33fbf10bc8d1983b901`.

Theorem for s=3, rank 27, k≥1 (r=2k+1): D_27(k)>0 for 1≤k≤5; D_27(k)<0 for 6≤k≤25; D_27(k)>0 for k≥26. Last permanent sign transition occurs at r=53.

Executable exact source: `R504_VERIFY.js` (Node BigInt, 163 polynomial identities at degree bound 162, 54 positive Newton differences at origin k=26, first 25 exact integer signs, 20 independent Bareiss determinant checks and 560 kernel comparisons). `R504_EVIDENCE.json` contains full 54 + 54 coefficients, 25 finite values, L, and counters; status R504_EXACT_JS_PASS. `R504_INDEPENDENT.py` computes 10 finite parameters via SymPy exact matrix determinant; status R504_INDEPENDENT_PASS. Proof: `R504_PROOF.zh-CN.md`.

Generic structural lemma: fixed-k rank-generating function is 1/(1 - sum_{ell=1}^{2k-1}(-1)^{ell-1}p_{ell+2}p_2^{ell-1} z^ell). Next: m=28 (56 Newton coefficients, 169-point degree bound 168) and dominant poles at k=6,7,10,25,26.

Github author-side artifact only; no authenticated native CLAIM/Result/Driver. Native research session request returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false), active owner list CONTROL_QUOTA. Source evidence remains distinct from native accepted result; freeze pinned R462 input, P000 and ACTIVE worldview unchanged.
