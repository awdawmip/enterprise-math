# R5 next unit: internal time-fiber LR separation test

Frozen sources: Global a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Current frontier: this asymmetric time-gap support theorem following 0a9e9066ee947a6410ed4b4601cdc9d419d0c90b.

Proven for every FULL_HIST and seedless LR policy:
|eP+eQ-1| <= (TQ-1)/8 - max(TP-TQ,0)/200 - (14/125)*max(TQ-TP,0).
Both penalties are sharp by exact LR witnesses.

Choose rational time fibers strictly inside the original stopping-time octagon with TP != TQ. Compute the exact FULL_HIST occupancy-flow image (retaining both x_01,x_11 hidden-history coordinates) to find candidate rational points **inside** this new necessary support. Then test each point against the entire LR seven-variable polytope K(W) with the exact quadratic residual F=(A+B)J-X1(alpha*A+beta*B), respecting the original model's definitions of A,B and X1. Prove a strict all-real sign using an exact certificate, or construct a witness seedless LR strategy if F reaches zero. Exiting a known two-stage hexagon or local LR cube alone is not global separation.

Save exact fractions, proof/certificate, reproducible code and actual output. Preserve frozen science sources, owner/CLAIM checks and independent admission roles.
