# R53 execution evidence — 2026-11-11

- Frozen scientific input: `enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
- Predecessor R52: `PR #2018@032d035bd320af17022bc36023e36567d3bc14c6`.
- Full locally executed standard-library verifier: `VERIFY_R53.py` (included in R53 full downloadable handoff); exact JSON certificate: `EXACT_CERTIFICATE.json` (same handoff).
- Main method independently reconstructs each age-owner map at *both rational-envelope endpoints*, checks entire cut ordering for all `s<=K`, reconstructs the labelled youngest-source vector and recursively checks that the indexed treap stores every age **exactly once**.
- Six cases: **486 phase cells, 29,945 source moves**. S23 `m=128,H=225,K=352`: **352 cells, 28,672 moves, 290 changing youngest vectors, 225 live indexed nodes**. Quadratic full atlases: `(m,H)=(5,8),(8,17),(16,25),(23,31)`. Quadratic `m=8,H=99993` lazy five-cell suffix: **32 moves after full 99,993-age initialization**, no lost ages.
- Exact counterexample: for `sqrt(2)-1, K=12`, top 7 upper phases `12,7,2,9,4,11,6`; `9` is not a convergent/semiconvergent denominator.
- GitHub `VERIFY_R53_COMPACT.py` reproduces the six exact families with the same fixed-index treap algorithm. It uses exact integer enclosure endpoint checks, no floating-point mathematical comparisons.
- Algorithmic conclusion: `O(H+m)` fixed member storage and complete label/provenance preservation. Treap updates are **expected** `O(log H)` under independent random priorities. The full phase oracle, initial classification, precision and output are separately counted.
- Status: author-side derivation and exact finite evidence; independent review and formal shared Result/Review are pending.
