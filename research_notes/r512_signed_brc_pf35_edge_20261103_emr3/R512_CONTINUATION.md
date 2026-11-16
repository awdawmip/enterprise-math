# R512 continuation

Date: 2026-11-03. Frozen scientific input R462@18783e01e3646c72b7aab3b16d3f565e83e6446f; predecessor R511@f855deb3516f86e9e9d1923e97926dc9878d07f6.

Proved under existing R452/R462 polynomial premise for signed BRC auxiliary scalar, integer k>=1: D_35(k)>0 for 1..5; <0 for 6..11; >0 for all k>=12. Used 70 Newton coefficients, 211-point degree<=210 identity, 70 strictly positive k=12 tail Newton differences; BigInt exact check and independent Berkowitz raw-matrix spot checks.

Reproduce: `node R512_VERIFY.js > R512_EVIDENCE.json` and `python R512_INDEPENDENT.py`. Verify JSON status, all 211 identity matches, 20 direct Bareiss matches and 700 raw BRC/ballot-Catalan checks. Six files are source, raw integer certificate, independent code/results, proof and this handoff.

Mother question: classify signed BRC Toeplitz right-edge minors and determine structural mechanisms of sign variation across degree/order. Next exact independent unit: s=3,m=36, 72-term Newton difference +217 exact-point identity; separately compute rational order generating-function pole phases k=5,6,11,12. Reuse original signed-branch carrier; do not collapse cancellation.

Authority: GitHub-connected account login awdawmip (repo admin). Native em_control_tasks returned CONTROL_QUOTA; em_session_start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Therefore canonical owner, Researcher-ID, CLAIM, Result, Driver review unconfirmed. Author-side Draft PR branch source only. P000, worldview, frozen scientific pin unchanged.