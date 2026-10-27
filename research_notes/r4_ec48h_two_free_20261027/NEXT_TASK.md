# EC48I — Exact encoder-component certificate beyond two-free switching

Verified author-side frontier EC48H (2026-10-27): finite, strictly positive, two-stage BRC source model. For every critical likelihood-ratio face, define the non-tied forced decoder rows C, the tied lower/upper endpoint words b and a, and the bipartite outside-to-outside graph E. If E is a matching, has a common Boolean pivot (OR of incident lower words <= AND of incident upper words), or has at most two incident words on each side, the complete face is attainable with K_hull memory states and only private stochastic history encoding. If this holds on all faces then K_seed=K_hull. In particular K_hull<=2 unconditionally implies K_seed=K_hull for this auxiliary model. The full proof and exact Fraction verification are in EC48H_TWO_FREE_SWITCHING_THEOREM.md, EC48H_VERIFY.py and EC48H_REPORT.json at the same research branch/immutable source commit.

**Exact unresolved target:** Either exhibit a strictly positive rational p,q with K_seed>K_hull, or prove a further universal graph reconfiguration principle. A strict-gap model needs K_hull>=3 and K_hull<|H|. At some critical ratio r its outside-to-outside graph must have at least three available free decoder rows, not be a matching, lack a common Boolean pivot and have at least three distinct incident words on at least one side. Failure of an EC48H sufficient condition alone establishes no failure of ROC preservation.

**Small fully specified candidate to analyze first:**

P_raw = [[2,2,5],[4,6,7],[2,3,6],[6,2,6]]
Q_raw = [[1,2,5],[3,3,4],[1,4,1],[1,5,3]].

Normalize each matrix by its own total. Here H=4, Y=3, exact chamber count K_hull=3. At r=22/17, C is empty, t=3, and E has four distinct edges:

000 -> 010; 000 -> 100; 001 -> 101; 100 -> 101.

There are three distinct incident sources and three distinct incident targets; the graph has no common Boolean pivot and is not a matching. This is an obstruction **candidate**, not a proved gap. Use EC48C's exact optimal encoder-component interval criterion: enumerate optimal deterministic encoders, connect the allowed single-coordinate transitions, compute the precise closed tied-mass interval of every connected component, and test whether the union covers the full [0,Q_r]. Independently verify each component and the certificate against a direct encoder-decoder factorization.

If some rational subinterval is uncovered, publish the matrices, exact normalization, critical r, complete enumerated component intervals and rigorous uncovered rational interval. Check other faces when claiming K_seed>K_hull for the full model. If the interval union is complete, exhibit an explicit graph reconfiguration, classify the mechanism and extend the general sufficient criterion.

Preserve EC48A–H definitions and exact source provenance; study only the finite positive-weight two-stage terminal ROC observer. Any X6, three-dimensional slice or heartbeat dynamical transfer requires an independently typed embedding/readout proof under P000. Native control last returned CONTROL_QUOTA and STATIC_READONLY_SCOPE_DENIED (operation_sent=false), so active task ownership remains to be verified by legitimate control. Do not conflate independent author-side progress with a native CLAIM/Result/Driver review.

Research activity: RA-EMR4-20261027-1138-EC48H-MATCH. Frozen GLOBAL_KNOWLEDGE_V1 main@2b67737ee24d9cdb3c2c7ee176e86c1bbf83df39; original Enterprise Math source main@03a7ce964fcc3993fd0736dafc69f16858a8d6d3; predecessor EC48G commit fd08c300cde18245565ce3b27d7ced523d35b627.
