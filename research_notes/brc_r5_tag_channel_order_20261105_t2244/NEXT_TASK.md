# R5 next executable discriminating unit

Retain GLOBAL frozen pin `a01383f825ef9d43b4b754254303298c64041568` and EM frozen pin `86149263e38c22292c9def1e0f69092efa1be77e`. Mother objective: determine whether strict positive finite P/Q FULL_HIST and seedless LR can have the same complete four-observer convex hull but different actual behavioral images.

1. Fix a four-stage positive-rational P/Q tree with two or more distinct histories merging at a nonterminal node and with distinct valid future kernels; preserve full histories, P/Q likelihood-ratio and stop/declaration observations.
2. Compute Bellman coefficients `A_i(n),u_i(n)` from the **actual** four-observer stop/declaration alternatives, including tie/boundary faces, and enumerate their exact rational sign cones.
3. Use the predecessor's finite-history min-cut (EM `126745428ba15d75358743e88952144389dc06a6`) at representative rational cone rays; apply the present channel garbling monotonicity and exact TV stability to prioritize discriminating channels. Verify global support equality only after covering every cone and boundary; any positive min-cut yields a valid separating direction.
4. For a globally hull-equal candidate, independently test real-behavior image nonconvexity via explicit pair and rigorous midpoint nonmembership.

Proof scope in this handoff: conditional finite Bellman one-gate theorem, four items proved; exact 300-instance Fraction implementation check. Full P/Q tree/whole-direction test is open. Avoid claiming that arbitrary Bellman coefficients are all realizable by one chosen physical P/Q model.
