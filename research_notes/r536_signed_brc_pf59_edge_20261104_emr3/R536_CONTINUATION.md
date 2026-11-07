# R536 — s=3, m=59 signed BRC Toeplitz continuation

2026-11-04. Frozen scientific input R462: `18783e01e3646c72b7aab3b16d3f565e83e6446f`. Predecessor R535: `cc77a93a0fab4849092efb98ee13e56b77ee7852`.

Mother objective: exact sign classification of signed BRC Toeplitz minors across odd r, plus structural cross-order explanation. R536 author-side conditional result: D59(k)>0 for 1..10 and k>=51; D59(k)<0 for 11..50. This is a 355-point exact polynomial identity under R452/R462 fixed-t lemma P, plus 118 strictly positive Newton tail coefficients at k=51; no positive-integer roots. R535 D58 and R536 D59 have opposite sign at k=5,6,11..13, and all k>=51.

Evidence: R536_VERIFY.js, R536_EVIDENCE.json, R536_INDEPENDENT.py, R536_INDEPENDENT_EVIDENCE.json and R536_PROOF.zh-CN.md. BigInt crosschecks 20 raw determinants and 21300 H/B coefficient pairs; independent Python crosschecks 12 determinants including both boundaries, 540 H/B and all 118 tail coefficients. Source and evidence kept on Draft PR #1708 (not formally admitted).

Next independently executable science: m=60 (deg<=360, 120 Newton coefficients, 361 identity points), and/or derive a uniform cross-order sign mechanism via the rational generating denominator and dominant poles for k=10,11,50,51. Keep branch/cancellation data; separate polynomial premise from verified certificate. Native owner, execution CLAIM, independent Driver acceptance remain governed by current control authority. P000/ACTIVE worldview unchanged.
