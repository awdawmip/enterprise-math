# R5 next: certify an exact real-image inclusion or exclusion

Scientific freeze GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e.
Use delta=1/4 tree and 80 H facets / 82 H vertices from research_notes/brc_r5_kernel_perturbation_phase_diagram_20261106_t0047.

This note gives an exact six-variable quadratic membership iff: g,u0,u1,z0,z1,z2, two time equations, fourteen error-zonotope inequalities. Choose a rational W in H (ideally a FULL deterministic-policy midpoint) and determine exact feasibility over REAL variables, including all boundaries. An exact UNSAT certificate plus W in H establishes the missing image inequality; a universal constructive SAT policy for all H establishes image equality for delta=1/4 and redirects parameter search.

Suggested approach: fix rational stopping-time slice (T_P,T_Q), eliminate g or two z combinations linearly where possible, and use certified CAD / rational positivity certificates for remaining low-dimensional inequalities. A floating-point solver/non-exhaustive grid supplies candidates only. Keep both observer strategy definitions unchanged; independent admission is separate.
