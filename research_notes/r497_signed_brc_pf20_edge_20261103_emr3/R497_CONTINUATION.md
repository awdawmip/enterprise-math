# R497 Research Continuation — 2026-11-03

Mother objective: classify signed BRC auxiliary Toeplitz/PF necessary minors under the frozen R462 model; explain rank-dependent sign transitions with a reproducible algebraic mechanism.

Scientific pin: `18783e01e3646c72b7aab3b16d3f565e83e6446f`. Predecessor: verified author-side R496@ `d685e0ffee05bef48e31d93c47e0a85dcd7e519e`. The R496 exact signed BRC/Hessenberg method was reused.

New author-side exact result R497: `r=2k+1`, `s=3`, `D20(k)>0` for `1<=k<=5` and `k>=119`, `D20(k)<0` for `6<=k<=118`; all `k` are positive integers. Integer factor `P20` has degree 39 and 40 strictly positive coefficients upon shifting to `k=119+u`; each of the 118 earlier integer points was exactly evaluated. For all `k>=119`, R496 gives `D19(k)<0<D20(k)`.

Full deliverables: `R497_PROOF.zh-CN.md`, `R497_VERIFY.py` (reproducible exact standard-library program), `R497_EVIDENCE.json` (complete exact polynomial, 40 translated coefficients, 118 boundary values and 31 independent 20x20 direct determinant samples). Author-side local exact run `R497_EXACT_PASS` and a second byte-identical run: 121 factorization coefficients, 840 raw signed BRC convolution crosschecks, 31 Bareiss determinants and 20 k=2 rank recurrence crosschecks. SHA-256 of local raw output: `d90f353e2f665e5db61f9b7b2bbd390560efcdf2596e1ec660cd4e3efe89efd5`.

Authority checked 2026-11-03: GitHub authenticated as awdawmip with admin permission. Native session creation was denied `STATIC_READONLY_SCOPE_DENIED` (`operation_sent=false`); live control task inventory returned `CONTROL_QUOTA`. Thus active owner not confirmed; no native CLAIM, Result or independent Driver admission. Project files are an author-side immutable frontier on existing Draft PR, not canonical accepted science. Preserve P000, ACTIVE worldview, frozen scientific source.

Next science: rank `m=21` at `s=3`, then characteristic-root/pole analysis of fixed-k rational rank-generating functions to explain order-dependent transitions (ranks 17: k38; 18: k11; 19: k7; 20: negative k6..118).
