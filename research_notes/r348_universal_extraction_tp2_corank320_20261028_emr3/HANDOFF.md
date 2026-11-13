# R348 portable BRC Newton research handoff

## Author-side science (not formal Source Result)

1. From the **original complete signed 12-term K/J recurrence**, a full formal-series argument establishes, for every integer r,u≥0, \`D_(r+u,u)=5^u H_r(u)\` where \`H_r\` is rational polynomial of degree at most r. Proof uses the general \`[z^q]P(y,z)\` y-degree≤2q lemma, universal \`deg(g_r)≤2r\` recurrence, exact coefficient extraction, and explicit treatment of the q<m boundary. See **R348_PROOF.zh-CN.md** sections A1–A5. R330's previous universal dependence is thus discharged **at author-side mathematical-proof level only**; independent review/Lean and native acceptance remain pending.
2. Original signed K/J arithmetic rebuilt B[0..965], H[300..321]. New 10 coranks r311..320 have precisely **6320/6320 strictly positive complete Newton coefficients**, digest **aa2bb5fbef46dc15aa766df196077f95fd5d4e4165d78fca7cab42db26b521d0**. Previous r301 digest (603 coefficients) and r302..310 digest (5517 coefficients) both exactly match immutable R346–R347. Also passed 40 raw D-minor comparisons, 10 Catalan top differences and 54 independent small SymPy comparisons.
3. Consequently, using inherited r1..310 positive certificates, \`M_(q,k)>0\` for every \`k>=1, 1<=q-k<=320\` in **auxiliary BRC model**. The two indices do not both range freely; no claim of global interior TP2, boundary TN2, TP3 or native X6 dynamical theorem.

## Source, provenance and verification

Original authorship: existing R330 at Git commit \`7c73f56263c3f0515aa28e55ced2d4c703b8e086\`; R346 \`37516cc5bb8d72098ce25f2d64881ec5da4279cd\`; R347 \`e66e12f57be134a2b0ec3350c88499a26433bad5\`. This author's fixed global snapshot: \`b074f7c2e17dce72232272df935e71823a0dff15\` / \`GLOBAL_KNOWLEDGE_V1\`. Project main read \`b2ae357431fef548a065950ac2362310459bf4c7\`.

Both posted GitHub executables \`R348_verify.py\` (Python integers/Fraction) and \`R348_kernel_audit.py\` (SymPy exact) were actually executed locally; the four remote blobs (two sources and two JSON result files) were checked against the original local **Git blob SHA**. Run \`python R348_verify.py\`, then \`python R348_kernel_audit.py\`, in a writable folder with SymPy. Program regenerates exact \`R348_NEW_COEFFICIENTS.txt\` (7.86MB) and validates its SHA256; the complete original plaintext was additionally packaged in \`EnterpriseMath_R348_Universal_Extraction_TP2_Corank320.zip\` as a user-visible attachment rather than inflating a GitHub code review by multi-megabyte decimal data. GitHub retains all source, math proof, row digests and machine-evidence JSON.

P000 + ACTIVE world assumptions untouched. Observation: this is signed auxiliary combinatorics with retained branches, not a native X6 observer-safe quotient. No author/reviewer independence claimed. Native status \`research_authority_granted=false\`; native queue saturated, active owner not verified. GitHub activity is author-side representation only, not an authenticated CLAIM/Source Result or Driver judgment.

## Exact next question

Prioritize independent proof audit of R348 theorem A (all r,u), especially polynomial y-degree cutoff and q<m case; then search a **joint (r,k) positivity cone** or true negative adjacent interior minor. A bounded fallback next computation is r321's complete 643 Newton coefficients. Do not repeat the 6320 new or 5517 inherited checks merely for reassurance; reuse committed exact-digest evidence.
