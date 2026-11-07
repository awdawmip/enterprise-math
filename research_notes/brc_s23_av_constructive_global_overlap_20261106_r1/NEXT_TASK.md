# Next research question: close the logarithmic overlap-rate gap

Known local frontier for the conditional tagged-AV S23 auxiliary experiment:

- An earlier all-n multi-hypothesis lower bound for minimax deficiency gives `1-delta_n = O(sqrt(log(n)/n))` (n>=1000 version previously published in Draft PR #1777).
- The current explicit global reconstruction kernel proves `1-delta_n >= (336/18755)exp(-789/125)/sqrt(n)` for all `n>=1`.

**Next discriminating question:** Can the lower bound on reconstruction overlap be strengthened to `Omega(sqrt(log(n)/n))` by a parameter-independent kernel with a sharper hidden-q mixing density and an empirical-z conditional proposal? Conversely, can a stronger multi-hypothesis lower bound prove `1-delta_n=O(n^{-1/2})`? Specify whether a candidate concerns one fixed fiber or the complete lawful parameter box, and retain n-wise uniformity.

A concrete first experiment: on the constant-z=1/4 fiber, compare the exact n-word overlap with (i) a uniform q-mixture and (ii) a Fisher-coordinate q-mixture; calculate the infimum over q including endpoints for n=45,100,1000. Explicitly separate exploratory numerical optimization from exact finite certificates. The original ten-label `R_beh(k,10)` transfer remains a parallel lawful bridge task.
