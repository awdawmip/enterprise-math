# R329 portable research handoff — exact 17-diagonal cone

Model: R325 **ordered-six positive-weight BRC auxiliary** recurrence, preserving all signed out-of-domain tails. This is not a native six-dimensional physics assertion.

Frozen references: GLOBAL_KNOWLEDGE_V1 main@d62b45cb24cc0a302a9e5a9651790a819fd0b151; original EM main@9dadf646d94c88a688a223388a1747ac00ff4867; mathematical R325 2c62f1502e640d1aed2db6f72956abc6a22ca2d5, R326 e5478b005efd75971c31ea8468d725d4c50ea26f, R327 8332494a0aea16df27beb9828edfb41b3f234e09, R328 271b843173aac0830792d3df4ecb0537eb022ee2.

**Author-side verified mathematical result**: all integers q>=r and 0<=r<=16 satisfy D_(q,q-r)>0. This adds r=5..16 (12 full infinite diagonals) to R328. Explicit positive coefficient polynomials H_r(u) satisfy D_(r+u,u)=5^u H_r(u); all finite differences Delta^j H_r(u)>0 for j<=r. The main note explains coefficient formula (★), its boundary handling, and proof; independent formal Driver review is outstanding.

Reproduce the actual completed run:
- python r329_symbolic.py --max-r 16 --json R329_SYMBOLIC_EVIDENCE.json
- python r329_independent_integer.py --q 48 --symbolic R329_SYMBOLIC_EVIDENCE.json --json R329_INTEGER_EVIDENCE.json

Observed: 17 exact symbolic rows PASS; arbitrary-precision signed-tail B0..B96: 4753 triangle positivity checks, 1225 D positivity checks, 697 diagonal equality checks PASS; 2004 negative signed tail entries retained. Compact digest/coverage receipt: R329_EXACT_EVIDENCE.json. The full raw symbolic and integer output were generated locally in the research environment and have SHA256 pins in that receipt; reproducible with these exact scripts. Reuse R327 q<=640 historical verification rather than rerun it for startup.

Current open task: derive **uniform-in-r** positivity for r≈alpha*q using H_r(q-r) from (★), or find r>=17 where shifted monomial positivity fails. Failure of a sufficient D cone is not automatically a negative B_s coefficient. Current uncovered Newton triangle remains s>=1281, 641<=q<=s. Defect fiber linear positivity and N_peak=81 remain open.

Identity: GitHub awdawmip with observed repository admin/push; logical researcher EM-DIRECT-R329-1225, stable locally assigned key em-direct-r329-20261027-1225, activity RA-EMR3-20261027-R329-DIAG-1225. These are NOT backend-issued session/CLAIM. Canonical task query returned CONTROL_QUOTA; Sites gateway static read-only; active owner, native Result and independent review pending. P000 / ACTIVE worldview unchanged.
