# PREFIX-400 exact verification and ownership record — 2026-11-01

Research input: Global main@9ced971d8b4a0352707cfb25bcb17977a494feb4, EM main@993a408982a302265cb3c31f93e69e4751299500. Scope: exact first four readings I1,I2,Cu,I3=k; arbitrary rational interval bands I4,I5,Cv. Author-side, not independently reviewed or native-admitted.

Original Python 3.13 Fraction run:
PASS_PREFIX400_EXACT_CIRCLE_LINE_BOUNDARY_FEASIBILITY 8_CASES
PASS_PREFIX400_UNIFORM_NOISY_SINGULAR_TWO_BRANCH_CV_SEPARATION

Independent original complex A SymPy check:
PASS_PREFIX400_INDEPENDENT_ORIGINAL_A_MATRIX_CIRCLE_AND_CV_IDENTITIES

Exact analytic margin with xi4=xi5=1/10, eta_v<=1:
T maximum displacement=63/160
per branch Cv displacement bound=1654443/551630360
between-branch true Cv separation >662821077/275815180
between-branch noisy observed separation >111190717/275815180.

GitHub subject: awdawmip, repository ordinary push=true. Native DIRECTED_RESEARCH authority_granted=false, complete_task_packet=false. Native em_control_tasks(owner inventory) returned CONTROL_QUOTA; own em_session_start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false (read-only connector identity), so no source-native registration/CLAIM/Result was performed. Portable research_notes only.

The main checker in GitHub has immutable Git blob SHA 95b5bfe15c5d127f6e67423f91dd227936d4d1a2 and the independent checker has cebfcf493b134a29e861b1d99b4c8a9fd07fa4b0. Both SHA values EXACTLY match the locally executed Python files (computed from Git blob framing and file bytes). Therefore local run results apply to identical remote source bytes. The complete 8-case machine-output sign table and logs are also present in the local evidence package.

Selected exhaustive NO certificate: for joint-noise midpoint case k=2, T lies in [19457/160,19583/160] and Z lies in [-7687,67467]. All nine candidates fail at least one of the four constraints (T>=L,T<=U,Z>=A,Z<=B):
- circle anchor: (-1,+1,+1,+1).
- T lower intersections: (0,+1,+1,-1), (0,+1,-1,+1).
- T upper intersections: (+1,0,+1,-1), (+1,0,-1,+1).
- Z lower intersections: (-1,+1,0,+1), (+1,-1,0,+1).
- Z upper intersections: (-1,+1,+1,0), (+1,-1,+1,0).
Every sign is exact in rational-square-root arithmetic. The general NO-certificate completeness is provided by the circle-boundary lemma. The formula proof does not rely on software fingerprint matching.

Next: extend to noisy I3, then generic five Port intensities and Cu; preserve both signs of sigma.
