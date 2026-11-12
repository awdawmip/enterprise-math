# EC49FMZ — Exact BRC seven-cache-key radius-three scan, indices 15400–16299

Date: 2026-11-13. Scientific status: **author-side exact finite computation** for independent review. Frozen scientific input: \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\` (unchanged). Predecessor: [EC49FMY PR #2212](https://github.com/awdawmip/enterprise-math/pull/2212), commit \`05784066cd0519cac7e595976fd649d391373520\`.

## Domain and theorem

Let W denote the **178,850 lawful operation words** under the frozen nine-state BRC transition system. Preserve the original ordered signed native-X6 microsteps, the complete raw cache-key identity, and the 24 distinct observation labels; there are 94 distinct full keys. The frozen radius-three seven-key enumeration has 38,169 configurations K_i, i=0,...,38168. Let C(K_i) be the minimum number of *distinct nonempty full ordered native-X6 prefixes* necessary for a selection of legal words using keys in K_i to cover every one of the 24 observation labels. Equal endpoint or signed net displacement is not equality of prefix histories.

The original exact C++ prefix-trie/subset integer dynamic program completed **900 consecutive rows**, exactly indices **15400 through 16299 inclusive**:

\[
\min_{15400\le i\le16299} C(K_i)=\boxed{104},\quad
\operatorname{argmin}_{15400\le i\le16299} C(K_i)=\{15740\}.
\]

The maximum is **202**, reached exactly at indices **15604, 16047**. An independent Python trie/subset DP agreed with the C++ values for **15400=150, 15740=104, 16299=178**. The 900-element exact cost vector and constructive certificate are supplied in \`EXACT_CERTIFICATE_EC49FMZ.json\` in this branch. That JSON contains lossless zlib/base64 encodings and integrity hashes, not a rounded or sampled summary.

## Upper-bound certificate for 15740

Seven full cache key indices: \`[0,4,5,19,22,34,49]\`. The certificate contains 24 *actual lawful operation words*, one for each demand label. Their nonempty signed native-X6 prefixes have the root partition:
\[
45\quad(\text{root }05)\;+\;39\quad(\text{root }06)\;+\;20\quad(\text{root }07)
=\boxed{104}.
\]
This gives the constructive upper bound C(K_15740)≤104. The exact global trie/subset recurrence computes 104 as the lower bound for precisely that restricted key set, so C(K_15740)=104.

## Why the optimization is exact

For each node v of each first-native-step trie, a subset-mask dynamic-programming table stores the minimum size of a nonempty selected prefix subtree meeting the specified demand-label subset. A terminal legal word contributes its labels without extra prefix nodes beyond the selected terminal. Child alternatives combine by bitmask union and additive nonoverlapping child-subtree cost, with cost 1 for selecting the current nonempty node. Induction on subtree height verifies optimality. Different first-native-step roots contain disjoint nonempty prefix strings; optimize demand allocation among roots, using each root's exact table. This enumerates all legal demand-covering selections and gives an exact finite integer minimum, with no floating approximation.

## Cross-configuration finding

Previous exact case 14750 used \`[0,4,5,6,22,34,49]\`, attained optimum 104 with root costs \`(39,45,20)\`. New case 15740 changes cache key 6→19 and attains optimum 104 with root costs \`(45,39,20)\`. The first root reallocates from 8 to 12 covered labels; the second reallocates from 12 to 8; the third retains four labels with changed selection. These are two distinct certified equal-cost configurations and an experimentally precise candidate for identifying a condition on cost-preserving key substitution.

## Verification, scope and continuation

The exact vector and witness are preserved in \`EXACT_CERTIFICATE_EC49FMZ.json\`, with SHA-256 of the original uncompressed JSON and exact vector. The local full evidence archive additionally contains the **900 original C++ output rows**, original frozen generator, complete 38,169 case key list, 9.3MB master input, C++ solver, Python independent checker, 24 fully reconstructed original words, and a standalone deep-check program. Its \`VERIFY_EC49FMZ.py --deep\` completed successfully: all 900 rows, SHA-256 matching frozen master input \`cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e\`, 178,850 legal words, 94 keys, witness membership and independent three-case Python DP.

Cumulative author-side radius-three coverage is **16,300 / 38,169 cases (42.7%)**, minimum so far **102**. Separate unrestricted seven-key BRC mother objective preserves an earlier valid 84-prefix construction, \`C_min(7)≤84\`. The next radius-three case is **16300**, with 21,869 remaining. Scientific next questions: search the next finite window; develop a cross-configuration lower-bound certificate; determine a sufficient (or discriminating failure) condition for 104-cost-preserving key replacement; explore unrestricted ≤83-prefix constructions.

Formal task \`RS-EC49AS\` was queried under request \`emr4-20261113-0725-task-rs-ec49as\`, but the last observed backend receipt was \`QUEUED\`. Researcher session registration request \`emr4-20261113-0725-session-direct\` was also \`QUEUED\`. Accordingly no canonical CLAIM, Result, Activity checkpoint or independent Driver mathematical admission is represented by this document. The reported computation and construction are author-side evidence from the immutable frozen scientific pin.
