# EC49FPF — Exact fixed-four sensing for two complete original BRC domains

**2026-11-15 · AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**

## Frozen source and definitions

Scientific input: immutable commit `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Frozen original 94-family, 178,850-word, 38,169-configuration input SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; complete original EC49FPD 104,104-entry rooted byte-prefix Trie cost table SHA256 `2e07ad0d935efd9824729feec6349c2af162e152cd9c8a2a93848fd4343eea93`. This is the original signed/named, provenance-preserving root operator, using roots 03, 05, 06 and 07 and exact integer costs.

Each complete legal allocation q sends every optional demand label to one permitted named root; mandatory labels stay at their unique root. P_K(r,S) is the minimum original root Trie cost with mandatory labels and optional subset S; the exact terminal observation is T_K(q)=sum_r P_K(r,S_r(q)). A *fixed* design chooses all queries before receiving any response. Within one **entire** 24-label legal-root-domain class, the unknown ranges over distinct complete rooted P profiles (repeated original source configurations giving identical profiles are identified for this discrimination task only).

## Theorem

For each of the complete named legal-root-domain classes represented by original configuration **16864** and **16988**, there are **77 original configurations**, **39 distinct rooted P profiles** and **1,296 legal complete allocations**. The minimum number of fixed scalar terminal observations needed to distinguish all 39 P profiles is exactly **4**.

The prior exact adaptive worst-case depth from [EC49FPD, PR #2463](https://github.com/awdawmip/enterprise-math/pull/2463) is **3** for each. The exact adaptivity gap is therefore one terminal query, **4 fixed versus 3 adaptive**. Together with [EC49FPE, PR #2466](https://github.com/awdawmip/enterprise-math/pull/2466), the complete four-class comparison is:

| Representative | Distinct P profiles | Optimal fixed queries | Optimal adaptive depth |
|---|---:|---:|---:|
| 16860 | 31 | 5 | 4 |
| **16864** | **39** | **4** | **3** |
| **16988** | **39** | **4** | **3** |
| 17022 | 31 | 5 | 4 |

## Explicit four-query upper bounds

Zero-based allocation indices use optional demand labels in ascending order, each permitted named-root choice in ascending order 03,05,06,07.

| Class | Fixed allocation indices | Distinct response four-tuples |
|---|---|---:|
| 16864 | `79,887,920,1212` | 39/39 |
| 16988 | `122,502,609,847` | 39/39 |

The executable certificate constructs all 39 profiles and all 1,296 legal terminal responses per profile, then checks that the selected four responses are pairwise distinct for all 39 profiles. The accompanying machine JSON gives the original configuration IDs and exact assignments.

## Four mutually exclusive witness pairs: exact lower bounds

**Exclusive-pair lemma.** If m different unordered pairs of states have the property that *every allowed query separates at most one of the m pairs*, then any fixed query set distinguishing every state requires at least m queries. A collection of k<m queries separates at most k of the witness pairs; some pair remains indistinguishable. Witness pairs may share endpoints.

Class **16864**, four witness pairs of distinct P-profile source representatives:

- `(16864,17249)`, `(17249,26174)`, `(17249,26250)`, `(19743,26250)`.

Class **16988**:

- `(17373,20051)`, `(17373,20659)`, `(17373,32442)`, `(20051,32434)`.

For **every one** of the 1,296 complete legal allocation actions, evaluate the original integer T response on all eight pair endpoints. In *each* class, exactly **1,104** actions distinguish none of the four pairs, **192** distinguish exactly one, and **0** distinguish two or more. The per-pair separating-action counts are respectively `[144,4,20,24]` and `[20,144,4,24]`. Therefore at least four queries are necessary; the explicit four-query injections provide the matching upper bounds. No LP/MILP status is load-bearing.

## Validation and scope

The standalone Python verifier reconstructs all **38,169** configuration signatures, the **625** complete legal-root domains, exact 77-member source ID sets for both studied classes, all **39** P-profile identities per class, and **101,088** integer terminal responses (39 × 1,296 × 2). It exhaustively checks the witness-pair histograms and 4-query injection signatures. The original C++17 root byte-Trie extractor was independently rebuilt with `-O2` and rerun on the frozen input for all **308** configurations covered by EC49FPD; its **104,104** integer rooted-cost records are byte-for-byte identical to the earlier table and its SHA256 above. The independent original adaptive tree decoder was rerun, confirming all 39 leaves in the two depth-3 classes (and the 31-leaf depth-4 trees in the other two classes).

This is an exact finite **complete-allocation terminal observer** theorem on the stated classes, preserving the richer named-root/source/provenance state for future operations. It neither alters P000/Heartbeat X6 nor establishes physical heartbeat timing. The prior original 625-domain classification remains **563 completed, 62 remaining**: these two classes were already fully classified, and this theorem closes their fixed-sensing optimization.

Reproduce with `python VERIFY_EC49FPF_FIXED_FOUR.py <evidence-directory>`, given the pinned original `frozen_original_master.txt`, `EC49FPD_PROFILE.csv`, `EC49FPD_CLASSES.json`. Complete standalone evidence archive: `EC49FPF_FIXED4_EXACT_EVIDENCE_20261115.tar.xz` with source, root-cost CSV, C++17 extractor, prior adaptive proof certificates, verifier, full result signatures, logs and checksums. Original source: EC49FPD [PR #2463](https://github.com/awdawmip/enterprise-math/pull/2463)@ `08fdc1cdf2cff01f23b2ffcbc84340c87ccf66b2`; previous fixed-five [PR #2466](https://github.com/awdawmip/enterprise-math/pull/2466)@ `d42bb4b1b4f0412aef0d821495c73423fe74e9a5`.

**Next:** classify remaining original legal-root classes; search higher-order, demand-subset-dependent cross-root terminal-invisible cost gauges; extend exclusive-pair lower bounds to other complete classes and examine observer-scoped named-root interventions without erasing branch identity.

Independent portable research, pending mathematical review. Formal immutable Task/CLAIM/Result/Review requires a separate current authorized publication and identity.
