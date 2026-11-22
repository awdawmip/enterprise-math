# EC49FWT supplemental exact counterexample — paired Farey spectra still lose a bit

**Date:** 2026-11-22. **Frozen input:** BRC16943. **Parent:** EC49FWT actual-anchor realization and two-sided mirror theorem, same PR. **Status:** AUTHOR_PROVED / EXACT_110_SITE_CERTIFICATE / NOT_REVIEWED.

The complete *indexed* left and right reflection-defect spectra for an unknown reduced anchor do **not** jointly determine the two normalized membership traces. This obstruction already occurs for these two genuine rational anchors:

| Anchor | left normalized (U, excluded mod-11 residue) | right normalized (U, excluded residue) |
|---|---|---|
| 7/11 | (789,1) | (327,0) |
| 9/17 | (327,1) | (789,0) |

For each sign, the corresponding two ten-bit masks have the same indexed autocorrelation and the same support mass (the left is the swapped pair 789/327 with common factor excluding 1; right is the swapped pair 327/789 with common factor excluding 0). The CRT defect formula
[
D_{U\times V}(c_{10},c_{11})
=2\left(|U||V|-K_U(c_{10})K_V(c_{11})\right)
]
therefore gives **identical complete indexed 110-period reflection-defect spectra on both sides simultaneously**. Yet the original paired traces differ: for example, the **left** Boolean observation at physical parameter `t=44` (CRT residues `4 mod 10, 0 mod 11`) is **1** for anchor 7/11 and **0** for anchor 9/17. This verifies a genuine two-sided observer-fiber collision and a one-bit separating witness.

The companion Python verifier uses the exact Euclidean/lexicographic normalization and frozen P10 predicate from `EC49FWT_TWO_SIDED_ANCHOR_REALIZATION_VERIFY.py`, checks both 110-site CRT traces directly from integer coordinates, compares all 110 indexed defect values on each side, and asserts this one-bit distinction. Local result: `ALL PASS`.

**Scope:** two unknown anchors, both signed branches, complete indexed defect spectra plus one additional membership bit. The counterexample rules out *zero* added bits for the corresponding joint observer; the *optimal worst-case joint layout* for all genuine anchor states remains open. It does not make claims about the scenario in which the anchor and affine origin are already given.

**Next:** enumerate the actual paired state population and the joint defect fibers with a fixed normalization, then solve an exact minimum distance / fixed-site hitting problem on the coupled pairs rather than multiplying two independent observers. This preserves shared anchor provenance and signed chronology.