# EC49FPC — Eight complete native BRC root-domain classes and exact adaptive terminal query depths

Scientific status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.
Date: 2026-11-15.
Frozen science pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Original frozen corpus SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.

## Definitions and scope

The original dataset has 94 signed-prefix key families, 178,850 original codewords, 38,169 seven-key configurations, labeled demands 0..23, and four **named** roots 03,05,06,07. For a configuration K, let E_l(K) be the exact union of legal roots at label l from its selected keys. The full 24-tuple (E_l(K)) defines a legal-root class; the frozen original dataset contains exactly 625 classes.

Write P_K(r,S) for the original integer byte-prefix Trie minimum-coverage cost at root r for an attainable labeled subset S. Its native implementation is the original EC49FOR extractor. For a complete legal assignment a, let T_K(a)=sum_r P_K(r,S_r(a)). All comparisons below keep root names, labels and complete allocation indices fixed within the same legal-root class.

## Theorem 1 — Eight exhaustive new finite equivalence certificates

The eight disjoint classes with representatives 14316,14320,16777,16781,16987,16989,17017,17027 each contain exactly 74 configurations. For all A,B *within any one of these classes*,

```
  (forall legal complete a, T_A(a)=T_B(a))
       iff
  (forall named r and attainable S, P_A(r,S)=P_B(r,S)).
```

P-equality implies T-equality algebraically. The converse is an exact, finite, complete-vector enumeration over all configurations, attainable root subsets and complete legal assignments in the eight declared classes.

| Class rep | Configs | Complete allocations/config | Reachable root entries total | P/T equivalence classes | Equal P/T configuration pairs |
|---:|---:|---:|---:|---:|---:|
| 14316 | 74 | 864 | 24,568 | 29 | 991 |
| 14320 | 74 | 864 | 24,568 | 29 | 991 |
| 16777 | 74 | 432 | 12,136 | 34 | 781 |
| 16781 | 74 | 432 | 11,840 | 40 | 562 |
| 16987 | 74 | 432 | 11,840 | 40 | 562 |
| 16989 | 74 | 864 | 24,568 | 36 | 668 |
| 17017 | 74 | 432 | 12,136 | 34 | 781 |
| 17027 | 74 | 864 | 24,568 | 36 | 668 |

**Exact totals:** eight complete classes, 592 configurations, 146,224 rooted cost entries, 383,616 complete-assignment total costs, 21,608 unordered within-class pairs, exactly 6,004 equal-P pairs and 6,004 equal-T pairs, and **zero** terminal-equal/root-unequal pairs.

## Theorem 2 — Eight exact optimal adaptive terminal observation depths

An unknown *distinct named-root cost profile* belongs to one of the eight complete classes. At each step the observer selects any complete legal assignment a and receives the exact integer T(a). Subsequent choices may depend on previous answers. The optimal worst-case depth of a deterministic decision tree is:

| Class | Distinct profiles | Candidate queries | Optimal adaptive depth | Constructive first query, zero-based |
|---:|---:|---:|---:|---:|
| 14316 | 29 | 864 | **2** | 11 |
| 14320 | 29 | 864 | **2** | 20 |
| 16777 | 34 | 432 | **2** | 132 |
| 16781 | 40 | 432 | **3** | 0 |
| 16987 | 40 | 432 | **3** | 0 |
| 16989 | 36 | 864 | **3** | 2 |
| 17017 | 34 | 432 | **2** | 254 |
| 17027 | 36 | 864 | **3** | 2 |

Proof of lower bounds: for each class, every single allocation has a collision among distinct profiles. For the depth-three classes, enumerate all 432/864 possible first queries. For each first query, there is an answer fiber for which no candidate second query is injective. Thus every possible adaptive two-query policy fails in worst case. Proof of upper bounds: explicit complete decision trees were constructed and each resulting leaf was exhaustively checked to contain exactly one distinct rooted-cost profile. Four trees have depth two, four have depth three.

The cost-vector calculation uses exact integers. Query indices use the Cartesian product in ascending optional-label order with choices in named root order 03,05,06,07. The exact branch-by-answer second/third query maps are preserved in the machine-readable decision-tree certificate of the evidence archive.

## Validation and reproducibility

- The immutable frozen input passed its SHA256 and shape checks; all 625 legal-root signatures were recomputed, and membership of each complete 74-member class was checked.
- C++17 original byte-prefix Trie and minimum-cover DP enumerated all 146,224 root costs for the 592 configurations. Under `-O2` and `-O3`, the complete original CSVs were **byte-identical**, with SHA256 `3f8d43c2234e80d9699157352bfe9f7f87166985310fd4fe66e1c78f851e252c`.
- The independent Python byte-prefix Trie implementation recomputed **the complete rooted cost table** for 16 original configurations (the first and last member of each class), matching every entry.
- The independent Python exact-vector verifier regenerated all 383,616 complete-assignment costs and both 21,608-pair equivalence partitions. Adaptive checker used integer collision-pair bitsets, all candidate first/second-query alternatives and full leaf verification.

Full portable evidence archive: `EC49FPC_EIGHT_CLASSES_ADAPTIVE_EVIDENCE_20261115.tar.xz`, SHA256 `6509d7d4600d0ea3088334f54df35ed0ae745d2dad73640fd775bde4148c7d97`. It includes the original frozen input, the original native C++ extractor, all 146,224 generated CSV rows, complete 592-member index manifest, exact checks, independent Python byte-Trie, full adaptive decision trees, logs, and a verified SHA256 manifest. Executable scripts `EC49FPC/VERIFY_EC49FPC.py` and `EC49FPC/ADAPTIVE_EXACT.py` run from the extracted package root. The portable evidence archive was created and verified locally; it is a separate conversation artifact, not claimed to reside inside this GitHub branch.

## Continuation and evidence boundaries

Existing exact complete-class coverage through EC49FOZ was 551 / 625. The eight newly completed and disjoint classes increase it to **559 / 625**, leaving **66**. Prior quartic subset-dependent original gauges (EC49FOT PR #2433) remain valid outside these eight domains. Next: classify remaining classes (especially paired size-77, size-87 and size-101 domains); test for degree at least five or mixed-root gauges and compare adaptive/augmented rooted observation costs.

Related source frontiers: [EC49FOT PR #2433](https://github.com/awdawmip/enterprise-math/pull/2433), [EC49FOW PR #2442](https://github.com/awdawmip/enterprise-math/pull/2442), [EC49FOZ PR #2454](https://github.com/awdawmip/enterprise-math/pull/2454). The research result is a finite BRC observation statement; no new P000 axiom is proposed.

Control: exact read of `research_task_records/RS-EC49AS` returned `NO_CANONICAL_PUBLICATION_DIRECTORY` at 2026-11-15T00:05:18Z, Source `1668ed1b7830dfd9892d4790563e47567792fdfb`. No formal CLAIM, Result or review is asserted by this independent portable research publication.
