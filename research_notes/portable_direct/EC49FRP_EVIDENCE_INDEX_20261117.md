# EC49FRP — evidence and continuation index (2026-11-17)

Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED_WITH_TWO_IMPLEMENTATIONS / NOT_REVIEWED.
Frozen science input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, original native BRC class 16943, 310 source configurations, 141 complete named state profiles, 228 original physical observations. Current project control/rules were read separately; science was not repinned.

## New result and relation to predecessors

Predecessor: EC49FRO GitHub PR #2636 and inherited original D/E trees. The new parity-lifted unrestricted Bellman minima at price 3 and prior beta 620/3299 are:
- even U3: exact integer Phi = 7290, witnessed by native E;
- odd U3: exact integer Phi = 7311, witnessed by an independently replayed complete original tree with (U_R,U_T,M_R,M_T)=(4,299,4,689);
- unrestricted scalar endpoints: min U3 = 308 and min M3 = 700, recomputed.

The integer parity exclusion proves that every legal full original deterministic tree is pointwise dominated by either D or E in BOTH uniform and weighted population costs at price 3. The irreducible two-pair root-observation lower bound transfers the same dominating tree to all real x>=3, all real lambda in [0,1]. This yields the exact unrestricted deterministic and prior-randomized minimax regret formulas for every closed prior subinterval. The proof file declares the hypotheses, parity recurrence, all integer cases, continuous extension and remaining limitations.

## Source and independent reproduction

Frozen sources copied in the full self-contained research archive:
- `source/frozen_original_master.txt` SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`;
- `source/EC49FPG_PROFILE.csv` SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

Full self-contained archive name `EC49FRP_HIGH_PRICE_PARETO_COLLAPSE_COMPLETE_EVIDENCE_20261117.tar.xz`, SHA256 `3a2a3422e461d2006399f6a4f7085634b5af5dc6271518b4eda3d91748b39e8b`, 16 files individually checked for size and SHA256 after reopening tar.

The archive includes frozen original raw inputs, unmodified original native model constructor, both independent parity Bellman implementations, full native even/odd witness decision trees, complete inherited D and E replayed trees, exact-rational 275-case interval validator, primary and independent execution logs, a machine certificate and 16-file manifest. Python 3 stdlib only. Independent implementation parses 94 original families from source, reconstructs 310 matching configurations, 141 named profiles, 228 full native observations, without relying on the first implementation; both yield 7290/7311 on 12,922 reachable dynamic-programming subsets. The second implementation separately recomputes 308 and 700. This finite exact computation establishes the native model prerequisites only, not general independent mathematical review.

## GitHub source files in this PR

- `EC49FRP_NATIVE_HIGH_PRICE_PARETO_COLLAPSE_20261117.md`: full mathematical statement and proof.
- `EC49FRP_PORTABLE_BELLMAN_MINIMAL_20261117.py`: original-constructor-based parity and scalar DP.
- `EC49FRP_INDEPENDENT_ALL_228_20261117.py`: independent reconstruction from frozen raw input and 228-action exact DP.
- `EC49FRP_INTERVAL_PARETO_VERIFY_20261117.py`: rational regression for 275 interval/price cases.
- This evidence index.

Python scripts are copied into the PR for inspection/reproduction. They are not standalone without the two large original frozen sources in the full 16-file archive; do not report those sources as stored as additional GitHub files. An archived local evidence bundle is not a remote repository publication of the entire bundle.

## Status, no authority promotion, and next question

Portable scientific artifacts remain independent of native immutable Task publication, winning CLAIM, Result/Review, owner projection, or Activity Source checkpoint. The exact current Source task-directory query for topic `RS-EC49AS` returned `NO_CANONICAL_PUBLICATION_DIRECTORY`; do not convert this into a claim that no other researcher has an active owner anywhere. Current native execution authority is unconfirmed. P000, ACTIVE worldview, original input and admissible observer semantics were preserved, and no new physical-model universality is claimed.

Next research: on 1<=x<3 classify whether all original deterministic trees admit a small pointwise Pareto-dominating set; test with exact multiobjective/parity Bellman, and construct explicit native counterexample if small fixed basis fails. Extend to multidimensional prior uncertainty only after this original scope is clear.
