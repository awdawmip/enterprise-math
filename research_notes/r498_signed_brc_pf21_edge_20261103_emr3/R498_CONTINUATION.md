# R498 Research Continuation — 2026-11-03

Mother question: frozen R462 signed BRC auxiliary scalar's Toeplitz/PF necessary-minor sign structure and rank-dependent oscillation. Exact source pin `18783e01e3646c72b7aab3b16d3f565e83e6446f`. Previous author-side R497@ `ec05cfbbc19768102aca749164236b10dbaf18c0`.

R498 proves `D_21(k)>0` for `1<=k<=5` and `k>=15`; `D_21(k)<0` for `6<=k<=14`. Here `r=2k+1`, `s=3`; the negative odd-r range is `13,15,...,29`. A degree-41 integer polynomial `P_21` controls the sign, with `P_21(15+u)` having 42 strictly positive integer coefficients. All 14 earlier integer values are exactly checked. At `15<=k<=118`, R497 also gives `D_20(k)<0<D_21(k)`.

Author-side exact execution: `R498_EXACT_PASS`, 127 rational coefficient identities, 440 raw signed-convolution checks, 20 independent original 21x21 Bareiss determinants, 21 k=2 rank recurrence checks. Evidence `R498_EVIDENCE.json` preserves all 42 original coefficients, 42 shifted coefficients and 14 boundary values; reproducible generator `R498_VERIFY.py`. Full local execution JSON SHA-256: `24bd14130ff2e8395089cc6e1d7249b6607a9df1d70e8342389f2ecfb3c1ca20`. Mathematical proof: `R498_PROOF.zh-CN.md`.

Native research session start failed `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. Live control task inventory returned `CONTROL_QUOTA`. GitHub authenticated `awdawmip` with admin permission. Accordingly active owner unconfirmed; no native CLAIM, Result, independent Driver acceptance. Draft PR artifact is an author-side checkpoint only; P000, ACTIVE worldview, source pin unchanged.

Next: classify `s=3,m=22`; study denominator poles of the fixed-k rational rank-generating function for a structural explanation of positive/negative regimes. Reconcile owner/claim before any native state-machine write.
