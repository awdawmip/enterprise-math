# R5 continuation — piecewise Bellman pair-cone coverage

Frozen GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Parent: strict-positive finite P/Q stopping BRC with equal FULL_HIST/LR *complete O4 convex hulls* and different real behavior images.

1. Keep complete time/ratio/path identity and alternative STOP_Q, STOP_P, CONTINUE. Choose an exact small positive four-stage merger with history-sensitive future kernels; reuse model S for negative controls.
2. Derive Bellman sign cells from exact four-dimensional observation vectors; represent every boundary/tie, not only sample rays. For each cell, compute correct linear gate coefficients or explicitly mark where one-gate independence fails.
3. For each ordered pair of opposite gate histories within a globally valid cell, test the combined cell inequalities and `M_ij n>0`. A positive rational solution is a strict FULL/LR hull separation. For all infeasible cells, retain exact nonnegative Gordan/Farkas duals, including cell constraints.
4. Only after certifying all cells with zero support gap for a candidate, test actual LR-image nonconvexity through an exact midpoint nonmembership certificate with fully real policy probabilities.

This note's completed new unit: all-directions pairwise criterion for a global one-gate reduction, exact model-S coefficients and full-tree support checks in direction n0, plus a guaranteed 1/6400-radius neighborhood with gap >=1/800. No full fan or mother-target closure is claimed.
