# R184 — Exact minimum subset-query catalog and optimal adaptive recovery

Date: 2026-11-15. Status: **AUTHOR_PROVED / EXACT_CHECKED / NOT_REVIEWED**.
Frozen scientific input: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.
Verified dependency: R182–R183 at immutable Enterprise Math commit \`5557fb3748bbe9e831e2f35716607dacffc0c6d4\`.

## Population and observation

Fix \`k>=1\` distinct selected source IDs T. Histories consist of *whole* X6 native atoms \`(branch_id,source_id,ordered_signed_X6_path)\`, concatenated chronologically; the present observer reads only selected source IDs and their last-occurrence order. Other path, branch, weight, multiplicity and provenance information stays on the uncompressed native carrier when required. Let S_k be the lists of pairwise distinct elements of T, oldest last occurrence first. The product is \`a⋆b=(a with all elements of b deleted) followed by b\` (R182). For each nonempty U⊆T, \`q_U(s)\` returns the rightmost member of s in U, or NONE.

A fixed catalog C supplies q_U for U∈C; the evaluator may prepend/append arbitrary complete histories before querying, and adapt future choices to answers. Sufficiency means separating every distinct pair in S_k. An unrestricted adaptive evaluator may instead construct a new subset U at every query; one query returns one source or NONE.

## Theorem A: exact minimum fixed query catalog, including future contexts

The **unique inclusion-minimal sufficient catalog** is

\[
\mathcal B_k=\{\{i\}:i\in T\}\cup\{\{i,j\}: i,j\in T,\ i\ne j\},
\quad |\mathcal B_k|=k+\binom k2=\frac{k(k+1)}2.
\]

This is a global lower bound on the number of available subset-query *types*, not merely on R183's reset-coordinate representation.

**Sufficiency.** Singleton answers reveal the support. For equal supports, distinct linear orders disagree on the relative order of some pair i,j; q_{\{i,j\}} separates them. Therefore B_k separates all S_k.

**Necessity.** For U={i}, take R listing T\{i} and compare u=iR with v=R. Every q_V with V≠{i} agrees: either i∉V, or V includes a member of the common suffix R whose last occurrence masks i. The singleton q_{\{i\}} distinguishes.

For U={i,j}, take R listing T\{i,j} and compare u=ijR with v=jiR. Any V meeting R is masked by the common suffix. Among nonempty V⊆{i,j}, only V={i,j} distinguishes the reversed order. Hence every member of B_k has a witness invisible to *all* other nonempty queries.

For each V, q_V maps concatenation into the right-zero-with-identity monoid V∪{NONE}:
\[
q_V(xy)=q_V(x)\odot q_V(y),\qquad a\odot b=
\begin{cases}b,&b\ne\mathrm{NONE}\\a,&b=\mathrm{NONE}.\end{cases}
\]
Equality of q_V(u),q_V(v) survives arbitrary left and right complete-history contexts. Thus contextual and adaptive use of a fixed catalog cannot evade these witnesses. QED.

## Theorem B: optimal unrestricted adaptive query complexity

Let an evaluator choose any nonempty U⊆T at each step, dependent on previous outcomes. Then the exact deterministic worst-case number of q_U calls required to recover arbitrary s∈S_k is **k**.

**Upper bound.** Query U=T to obtain the most recent source i. Remove i from U and repeat, collecting the returned sources most-recent first; reverse the collected sequence. Stop on NONE or when U is empty. With r<k present sources this makes r+1 calls; with r=k it makes k calls; in every case at most k.

**Lower bound.** Fix any full-support s (a permutation of all k targets). For a query returning j, removing from s any other source i≠j leaves the answer unchanged. If fewer than k queries have been made, some i has never appeared as an answer; deleting i preserves the *entire adaptive transcript*, including every next query chosen from prior answers. The evaluator cannot distinguish s from this deletion, so correctness on all S_k forces at least k distinct returned sources and therefore k calls. QED.

## Distinct representation costs and BRC scope

The full semantic quotient has \(\sum_{r=0}^k k!/(k-r)!=\lfloor e\,k!\rfloor\) states and fixed-length storage bound \(\lceil\log_2\lfloor e\,k!\rfloor\rceil\) bits. This is distinct from \(\frac{k(k+1)}2\) indispensable publicly callable fixed subset selectors and k worst-case adaptive subset queries. R183's diagonal reset affine realization matches the fixed catalog cardinality, while unrestricted faithful affine dimension is still open. The k-query recovery method requires a changing subset oracle; a packet previously collapsed to only one q_U cannot answer arbitrary future U without more information. For an explicit ordered-list state of length ≤k, naïve q_U scanning costs O(k) per call, O(k²) total for recovery, plus the source-ID mapping and upstream atom storage.

This is a precise scope-typed source-observer quotient within the ACTIVE P000 Heartbeat World X6 environment. Original signed paths, branch identity, provenance, positive rational BRC weights and multiplicity remain available in the full carrier wherever later operations may read them.

## Exact checks and next scientific problem

\`R184_latest_source_query_basis_check.py\` is an integer-only exhaustive checker, \`R184_verification.json\` its result: k=1..6 (2,371 states total); 56 unique indispensable-catalog witnesses; 61,910 explicit context/witness comparisons; 65,246 subset composition checks; 242,850 deletion checks; every state recovered in at most k queries. These finite tests corroborate the all-k symbolic proofs. Actual installed \`enterprise_math.brc_transport\` integration remains unexecuted; the present theorem concerns the exact source selector, not a claim of completed native package testing.

Historical Researcher-ID \`EM-DIRECT-BF4AD7\`, SID \`MCP-46f202db13e64ad6b4c8860e06908245\`, Activity \`RA-7A118452894D2600AE7DE5A2\`. This is independent portable research with no asserted formal CLAIM, Result, Review or Foundation promotion. The Activity checkpoint remains a separate pending Source association.

Next: determine unrestricted minimal faithful rational affine dimension of the free right regular band S_k, implement and execute genuine project-native BRC source-selector tests, and compare compressed vs full branch/ordered-path costs under exact port-specific future operations.
