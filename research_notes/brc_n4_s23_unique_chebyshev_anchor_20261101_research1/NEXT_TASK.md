# Next scientific unit

**Parent objective:** Exact ten-label full-behavior S23 minimax on k=4/6, interval currently [1/2,2/3], and validated observer-faithful transfer to P000 separately.

**Completed and do not repeat:** For the existing six-source observer model, the full 11D *single-policy-anchor* max-prepared-TV radius is exactly 3/4 and the unique centre is (1/4,1/4,1/3,1/3,1/3;1/2^6); coordinate midpoint has radius 7/8. A two-control AU/U face has unique optimum 2/3 at (s,t)=(1/3,1/2), midpoint radius 3/4. The exact vertex evaluation from previous local-box theorem is reused; proof and integer checker attached.

**Smallest next open question:** For general rational 11D subboxes Q, can one compute or rigorously bound \`min_{z in Q} rho_Q(z)\` more sharply than the midpoint and the geometric diameter using a finite **piecewise-multiaffine** cell/LP construction, preserving cross-source shared controls? Prove a correct local algorithm/certificate with full real-parameter guarantee; identify counterexamples to naive midpoint or Delta(Q)/2 heuristics. Then use it as one bound inside an actual multi-label branch-and-bound with at least two jointly redesigned decoders. Do not identify anchor-radius optimization with the ten-label optimal risk.

**Verification:** Execute \`node VERIFY.js\` and compare JSON content to \`RUN_EVIDENCE.json\`; program does exact integers and explicitly tests only specified anchors and corners. Any broader numeric search must declare its arithmetic, complete covering theorem, and model scope. Further native Result/owner path requires independent current authorization and admission.
