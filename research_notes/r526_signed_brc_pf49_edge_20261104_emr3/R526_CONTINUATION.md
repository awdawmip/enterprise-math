# R526 signed BRC s=3,m=49 continuation

Date: 2026-11-04. Frozen scientific pin: R462@`18783e01e3646c72b7aab3b16d3f565e83e6446f`. Predecessor: R525@`c15deb1b4256bd2eb8be351fcfbbd5c399bf3ef3`. Mother objective: classify signed BRC Toeplitz minors in integer k and derive across-order sign mechanism.

Conditional author-side result: D49 positive for k=1..5 and 10..95; negative for k=6..9 and all k>=96. In r=2k+1, permanent negative starts r=193. Adjacent D48<0<D49 at k=10..13 and D48>0>D49 for all k>=96. Fixed-t polynomial prerequisite frozen at R452/R462; exact definition in R526_PROOF.zh-CN.md.

Reproduce: `node R526_VERIFY.js > R526_EVIDENCE.json` (295 exact polynomial identities, 98 initial and shifted differences, 20 direct Bareiss determinants, 980 signed/ballot comparisons); `python R526_INDEPENDENT.py > R526_INDEPENDENT_EVIDENCE.json` (18 direct SymPy Berkowitz 49x49 determinants, 882 signed/ballot comparisons). Checks performed 2026-11-04, exact integers. Independent code is author-side cross-implementation, not a native independent Driver review.

Control read: `CONTROL_QUOTA`. Native `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`; Site configuration is static read-only, no research execution grant. GitHub identity awdawmip has admin permission to publish author-side source to Draft PR #1708. No native Researcher-ID/CLAIM/Result/Driver acceptance obtained. P000, ACTIVE worldview and frozen R462 science unchanged.

Next: `s=3,m=50` (degree<=300, 100 Newton coefficients, 301 exact evaluation points), or the alternative fixed-k pole mechanism for k=5,6,9,10,95,96. Avoid turning relative numerical evidence into an algebraic root theorem without a separate certificate.
