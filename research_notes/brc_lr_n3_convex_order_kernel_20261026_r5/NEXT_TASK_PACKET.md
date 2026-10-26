# NEXT TASK: N=3 root masking beyond terminal-kernel convex order

Predecessor: PROOF_CONVEX_ORDER.md (author-level exact algebra; native Driver unreviewed), source project baseline 3f0aae162f514595f4b2e5f0ccd04a91fac3abdb. The finite three-time positive P/Q model has time-1 histories a,b at LR=1, Q rows on R=(1/2,1,3/2): q_a=(1/4,1/2,1/4), q_b=(1/3,1/3,1/3); terminal Q kernel mu_r with E[Y|r]=r, conditional P(y|r)=y*mu_r(y)/r.

THEOREM COMPLETED: mu_1 <=cx (mu_(1/2)+mu_(3/2))/2 iff every signed linear-cost Bellman downstream phi is midpoint-concave at R. This implies but is NOT proved necessary for full four-scalar root masking. Explicit strictly positive LR-dependent two-endpoint kernel Y in {1/4,2} gives all-real policy-by-policy four-observer preservation despite time-1 nonlumpability. Fraction checker and executed stdout are stored in this directory.

NEXT EXACT QUESTION: Is the convex-order kernel criterion necessary for root masking, or does the root-stop option mask a violation? Find a strictly positive rational kernel violating it and a root-active separating signed Bellman support, or prove a weaker exact envelope criterion.

FIRST FINITE SEARCH: enumerate small rational mu_r on a shared terminal Y grid satisfying mean r and strict positivity, check call prices at their exact finite knots, then calculate full and LR Bellman envelopes using exact rational arithmetic. Produce an exact separation or a fully enumerated bounded no-go table with completeness proof. Do not extrapolate cost grids to a general theorem.

Keep terminal Y collisions, Q/P occupancy-flow weights, hidden history residual, signed costs, contribution provenance, and native Owner/CLAIM/review uncertainty explicit. No P000/X6/Heartbeat or physical-dynamics promotion.
