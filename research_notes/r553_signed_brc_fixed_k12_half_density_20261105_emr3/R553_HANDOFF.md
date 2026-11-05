# R553 author-side handoff | fixed k=12 signed BRC

- **Mother problem:** frozen R462 signed BRC Toeplitz–Hessenberg sign classification across m and k. Retain separate s=3,m=63 full-parameter sign-classification line.
- **Immutable scientific input:** R462 `18783e01e3646c72b7aab3b16d3f565e83e6446f`; preceding R541 exact rational generating function and R551 finite-field root-ratio argument are reused at their scopes. Current behavioral rules are separately resolved from latest main.
- **Completed R553 scientific unit:** k=12 strict +/− natural densities both 1/2; nondegenerate order-23 recurrence has finitely many zero terms. Roots: 23 exact Rouché discs, unique dominant conjugate pair |λ|>14 vs others <6. Noncyclotomic: 991 complete `F_65537` gcds, `deg R=506`, `q≤512072`.
- **Evidence:** `R553_PROOF.zh-CN.md`, `R553_VERIFY.py`, `R553_MODULAR.py`, `R553_INDEPENDENT.py`, `R553_EVIDENCE.md`. Finite recurrence `m≤1024`: positive 514, negative 511, zero 0, changes 302. Independent raw determinants m=1..16 checked.
- **Current evidence level:** author-side mathematical proof with exact machine-checkable certificates; no assertion of native CLAIM, formal Result or independent Driver acceptance. No changes to P000/ACTIVE worldview.
- **One next exact question:** fixed k=13, do the 25-root rational Rouché discs still isolate a unique dominant nonreal conjugate pair, and does a single prime modular resultant exclude all root ratios of unity? If yes, deduce half-density and finitely many zeros. Independently seek a k-uniform root separation / noncyclotomic theorem.
- **Other open task:** s=3,m=63 full positive-integer parameter sign classification, without expanding the fixed-k result to it.
