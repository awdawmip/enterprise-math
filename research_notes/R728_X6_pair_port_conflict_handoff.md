# R728 — portable research handoff

Parent task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142; frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389. Previous published author candidate R727: Draft PR #2107 at f0e617a61af11ab9e2861c1b19747ab1f05f6249. P000 remains locked.

Completed exact mathematics: for any partition of n native axis *labels* into conflict blocks B_s, with 3m distinguishable sources, allowing triples drawn from three different blocks, decomposition exists iff each block population b_s<=m. General allowed-triple graph E has provenance-preserving BRC count L_E(a)=(prod a_i!/m!)[x^a](sum_(T in E)prod_(i in T)x_i)^m. The numeric count for a complete block-hypergraph depends on aggregate b_s, although original source IDs and axis families remain distinct.

Explicit conditional six-axis port model: blocks {0,1},{2},{3},{4},{5}; candidate E excludes 012,013,014,015 from the 20 R727 eligibility triples. In six-source models a=(1,1,1,1,1,1) and a'=(2,0,1,1,1,1) have identical block vector b=(2,1,1,1,1) and restricted BRC source count 6; after hypothetical removal of port conflict their full counts become 10 versus 6. This exact collision shows future-unsafe coarse-graining. Witness (2,1,1,1,1,0) has full count 6 but restricted count 0.

Reproduce: python3 research_notes/R728_X6_pair_port_conflict_verify.py. Exact finite enumeration of all 8708 six-family occupation vectors for m=1..4, coefficient expansion versus independent source-ID pivot recursion; all 720 axis permutations preserve the transported excluded-pair hypergraph. PASS marker R728_PORT_CONFLICT_EXACT_PASS; see adjacent evidence JSON and proof.

Smallest unanswered unit: obtain actual lawful Cell/Link/Port event with V29 PASS/TRANSFER or V39 flow j from immutable pinned source or true dependency, including TRIADIC_CLOSURE_E certificates. Extract E(c,t), compare with this conditional pair-port exclusion, and test whether real event updates preserve the block observer or require the axis-source repair. A candidate port hypothesis is not native law, and no native simulation was run.

This research note is author-side persistence only. No inherited previous Researcher-ID, CLAIM, task checkpoint, accepted Result, independent Driver review or protected P000 promotion is implied. Preserve original sources and evidence and report actual control receipts separately.