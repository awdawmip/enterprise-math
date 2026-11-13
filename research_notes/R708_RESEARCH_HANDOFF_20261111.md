# R708 concise handoff — saturation criterion and BRC triad source kernel

Task RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142; frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389. Original R707 proof in immutable author commit 877562f8f1affc12016fbd5c35f623d8a27f467b.

Proven in the R707 candidate equal-q Cell-local model for all m: a covering of 3m individually labeled force tokens on six axes by m distinct-axis triples exists iff max n_i<=m. Greedy take the three largest remaining axes per round. For fixed labeled visible pair axes i,j, third-axis positive BRC branch count W_ij,k=n_k D(n-e_i-e_j-e_k), supported iff n_k>0 and all saturated axes n_a=m belong to {i,j,k}. If two distinct axes saturate, D(n)=(m!)² and conditional third-axis probability is n_k/m. Exact observer counterexample: nA=(3,3,3,0,0,0), nB=(3,3,1,1,1,0) both have D=36, but third axis of a fixed (0,1) token pair has support {2} vs {2,3,4}; in nB a (2,3) pair cannot occur together.

Verifier marker R708_X6_TRIADIC_SATURATION_BRC_EXACT_PASS; 1366 profiles checked (0<=n_i<=3), 1135 feasible, 10755 pair tests, 390 two-saturated profiles. Proof has all-m scope, test has finite scope. BRC reuse: R707 labeled partition recurrence and positive source multiplicity; preserve token sign, port and provenance for future source-addressed operations.

Native control snapshot checked 2026-11-10T23:23:28Z: task was CLAIMED by EM-X6-42F854 / session MCP-e778de4655a24997b8e0880a0937bd26; last activity 23:17:28Z; lease through 2026-11-11T01:17:28Z; this author-side branch makes no task CLAIM, Result, or Driver review. Recheck active Source before any native mutation.

Next exact unit: actual frozen X6 Cell/Link/Port, V29 PASS/TRANSFER and V39 j-flow event permit or forbid candidate nA/nB; construct one conservation ledger and resulting axis-addressed BRC source prediction.