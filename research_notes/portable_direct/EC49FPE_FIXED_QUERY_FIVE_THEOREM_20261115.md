# EC49FPE — Two original BRC legal-root domains require exactly five fixed terminal queries

Date: 2026-11-15. Scientific status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

## Pinned input, cost and query semantics

This continues EC49FPD (PR #2463, head \`08fdc1cdf2cff01f23b2ffcbc84340c87ccf66b2\`) and retains its immutable scientific source commit \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Frozen original corpus \`frozen_original_master.txt\` SHA256: \`cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e\`. Existing complete integer root-cost table \`EC49FPD_PROFILE.csv\` SHA256: \`2e07ad0d935efd9824729feec6349c2af162e152cd9c8a2a93848fd4343eea93\`.

The original corpus consists of 94 key families, 178,850 byte codewords, 38,169 seven-key configurations and 24 demand labels. Root identities 03,05,06,07 and signed/source-specific codeword paths remain preserved. A legal complete allocation q sends each optional demand label to exactly one of its legally permitted named roots. For configuration K, the rooted exact prefix-Trie cost P_K(r,S) covers mandatory labels at root r plus optional subset S. The scalar terminal response is

\[
T_K(q)=\sum_{r\in\{03,05,06,07\}}P_K(r,S_r(q)).
\]

A *fixed* observation design selects all its actions in advance, without adapting to earlier response values. The unknown is promised to belong to one specified entire 24-label legal-domain class; identical full rooted-cost profiles count once. Query indices are zero-based, with optional labels ascending and permitted root choices 03,05,06,07 ascending.

## Main exact finite theorem

Let C_r be the entire original legal-root domain represented by r=16860 or r=17022. Each C_r contains exactly 77 original configurations, with 31 distinct full rooted-cost profiles and 1,296 legal complete allocation actions. For each r,

\[
\boxed{\min\{|H|:\ K\mapsto (T_K(q))_{q\in H}
  \text{ is injective on the 31 rooted profiles in } C_r\}=5.}
\]

The previously verified optimal **adaptive** worst-case depth on these same two complete classes is 4 (EC49FPD). Therefore the exact fixed-versus-adaptive difference is one query, 5 versus 4.

## Upper-bound certificates: five fixed queries distinguish all 31 profiles

| Whole domain | Five zero-based action indices | Distinct five-value signatures |
|---|---|---:|
| 16860 | 62, 331, 732, 868, 992 | 31 / 31 |
| 17022 | 114, 271, 776, 798, 1126 | 31 / 31 |

For each row, recompute all 1,296 complete terminal responses for each of the 31 distinct rooted profiles from the original legal domains and full named-root cost table. Direct integer comparison shows all 31 five-tuples are pairwise different. The accompanying Python verifier recomputes the original domains and these signatures, including every optional-label to root assignment.

## Lower-bound certificates: five exclusive pairs

**Lemma (exclusive-pair sensing lower bound).** Let e_1,...,e_m be distinct unordered pairs of different profiles. If every allowed query distinguishes at most one e_i, any fixed set of fewer than m queries leaves at least one e_i indistinguishable. Proof: a set of k queries can distinguish at most k of these m pairs; for k<m, one pair yields equal answers at every chosen query. The pairs need not be vertex-disjoint.

Exact five-pair certificates, written as the original configuration IDs of distinct rooted profiles:

| Whole domain | Five exclusive witness pairs |
|---|---|
| 16860 | (16860,18514); (16860,19727); (16860,21230); (16860,25850); (19727,25949) |
| 17022 | (17022,25612); (17022,33870); (17022,34409); (17022,34418); (20175,34418) |

For **every one of the 1,296 legal actions**, compare exact integer responses at the ten pair endpoints. In **each** class exactly 1,038 actions distinguish zero listed pairs and 258 distinguish one; **none distinguishes two or more**. Thus the lemma yields a lower bound of 5. Unlike a solver status or a search through all four-query subsets, this is a compact, independently executable finite obstruction witness. Combined with the five-query injections, it proves equality.

## Independent evidence and scope

- Reconstructed legal root-domain signatures of **all 38,169 configurations** from the frozen input, confirming 625 full domains and exact 77-member membership for both selected classes.
- Reconstructed 31 distinct P-profiles and all 1,296 terminal response values per profile, 40,176 integer responses in each class, from 104,104 existing exact rooted cost records across all four EC49FPD classes.
- Fresh C++17 -O2 recompilation and rerun of the original byte-prefix Trie on the frozen corpus reproduced all **104,104** rooted records byte-for-byte, identical to the prior complete table SHA256 above.
- Re-ran the prior independent EC49FPD adaptive decision-tree decoder; both depth-four trees were confirmed to have 31 correctly labelled profile leaves. The earlier *exhaustive depth ≤3 obstruction proof* for the adaptive interface is reused at its stated finite scope.
- The local complete evidence archive \`EC49FPE_FIXED_FIVE_COMPLETE_EVIDENCE_20261115.tar.xz\` contains frozen source, full cost table, source extractor, independent verifier, full profile-signature machine certificate, logs and SHA256 manifest. SHA256 of archive: \`a32dd4c7fed5627665be7e9fe0636fefdd08b15d40edb3bea00186f40c5a1fa6\`. The archive is a conversation attachment; this GitHub PR publishes the research report, standalone verifier and compact certificate.

The theorem is an **exact finite observer result** under the declared complete-allocation scalar terminal query interface. Named-root source/provenance remains part of the richer P state; no claim of safe elimination under untested future operations or of native physical time measurement is made. P000's six native spatial axes and separately typed time are unchanged.

## Reproduction

Provide the two original files \`frozen_original_master.txt\` and \`EC49FPD_PROFILE.csv\` plus \`EC49FPD_CLASSES.json\` (all in the EC49FPD/EC49FPE complete evidence archive) in one directory, then execute the published \`VERIFY_EC49FPE_FIXED_FIVE.py <directory>\`. Expected terminal line: \`EC49FPE_CERTIFICATE_PASS\`. To reproduce the raw rooted-cost table, compile \`EC49FPD_ORIGINAL_EXTRACTOR.cpp\` as C++17 -O2 and run with \`EC49FPD_IDS.txt\` and pinned original input on stdin; byte-compare stdout to the original CSV.

Next scientific questions: evaluate exclusive-pair witnesses in other completed domains, classify the remaining 62 original legal-root domains, investigate higher-order subset-dependent terminal-invisible cross-root gauges, and compare fixed/adaptive observation with a declared, provenance-preserving named-root intervention interface.

This artifact is independent portable research. The exact topic RS-EC49AS had no canonical immutable task publication directory in its 2026-11-15 control read; this report does not create CLAIM, formal Result, Review or mathematical acceptance.
