# R288 handoff — 2026-10-25

Status: AUTHOR_SIDE_PROOF_AND_LOCAL_INTEGER_CHECK / NATIVE_OWNER_UNVERIFIED / DRIVER_UNREVIEWED / NOT_ADMITTED.

New: Exact cancellation (1-u²)/sqrt(D)=u/x converts both R287 gap families into w=u/x polynomials divided by 1+y. For every fixed legal m it yields explicit asymptotic gap constants and exhaustive ultimate sign classification: ε=+: m≤3 eventually negative, m≥4 eventually positive; ε=−: m=2 eventually negative, m≥3 eventually positive.

Proof dependencies: exact R283 Green kernel and clean six-edge source semantics. No native X6 Cell transfer. The classification is fixed-m; no uniform-in-m bound or effective integer threshold N_m has been proved.

Actual local execution: Python unbounded integer six-edge DP 0..320; direct algebraic series to y^168; 6,021 coefficient comparisons and 169 radical cancellation coefficient checks; PASS; see EXACT_EVIDENCE.json. R287's four all-length positivity obligations remain undischarged.

Control read: Global Knowledge main@773662089f9db565f6e81977489c182f24933001; EM source read main@0b10176535779ebabd2d3420e7a94929518e6513. GitHub connected identity awdawmip may push author-side artifacts. Native em_control_tasks CONTROL_QUOTA; em_session_start STATIC_READONLY_SCOPE_DENIED; operation_sent=false. No authenticated owner/CLAIM/Result/Driver.

Next exact unit: explicit effective coefficient positivity cutoff for G^+_13, G^+_14, G^-_11, G^-_12 plus exhaustive finite validation; only then remove the R287 28-candidate reduction condition.
