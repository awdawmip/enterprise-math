# EC49FSC — a three-price native BRC cross-section: exact sampled bounds, open phase reconstruction

**Date:** 2026-11-18 (Asia/Shanghai). **Status:** EXACT_FINITE_BELLMAN_CHECKED / PHASE_CLASSIFICATION_OPEN / NOT_REVIEWED. **Freeze:** \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`.

Continue EC49FSA–FSB with the original **228 physically named native observations**, 141 named profiles and uniform profile prior, all complete adaptive trees. Set q32 and q34 prices each to \(t/2\), q140 price to \((1-z)t\), and all remaining prices to \(t\), with \(z\in[0,1]\). As before \(F(z)=141V(z)/t\).

Two differently implemented exact rational Bellman solvers, each using a separately decoded 94-family frozen raw source, agree at the following anchors:

| q140 discount z | exact global Bellman F(z) | representative optimal root |
|---|---|---|
| 0 | 215 | q32 |
| 1/2 | 201 | q34 |
| 1 | 263/2 | q140 |

Main-path DP state counts for the three observations, respectively: 9,884, 9,486, 6,441; exact replay of the retrieved witnesses identifies all 141 profiles. The q140 use counts of these representatives are 0, 51 and 141, respectively.

**Scientific significance:** at this three-price slice, a single affine formula is impossible: the slopes of the exhibited tree types are \(0,-51,-141\). The two outer affine witness lines based on these specific trees do not determine the unrestricted optimum throughout the interval; intermediate original-native policies already strictly improve their naive lower envelope. This is a finite exact observation, not a claimed complete phase theorem.

A rational adaptive Bellman supporting-line exploration was also attempted. It produced several further candidate lines and exact finite checkpoints, but did **not** reach complete breakpoint certification in this run; do not promote its provisional walls as a theorem. The correct continuation is to resume from the saved exact anchor triples above, use the cost-line witness \((A=U-(N_{32}+N_{34})/2,\ K=N_{140})\) as the affine Pareto coordinate, and prove all-real segments only after their exact Bellman endpoint lower bounds and complete tree witnesses are verified. The overall three-parameter q32/q34/q140 phase complex remains open.

Reproduce the three anchors from the associated \`EC49FSA_FSB_RECOMPUTE_20261118.py\` by giving the original frozen archive and applying the same integer Bellman recurrence with discounts \`{32:1/2,34:1/2,140:z}\`. The local uncompleted exploration is retained with the run's evidence, not presented as a globally certified diagram.

Control scope: portable research only, independent of any formally claimed Task or owner.
