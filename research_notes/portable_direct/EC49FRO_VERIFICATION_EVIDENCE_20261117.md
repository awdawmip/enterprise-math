# EC49FRO — Provenance, verification and remaining obligations

Date: 2026-11-17. Original scientific input commit/pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Scientific result and dependency

The companion `EC49FRO_UNRESTRICTED_DETERMINISTIC_MINIMAX_20261117.md` proves that for the original 141 named BRC profiles and all 228 physical observations, with root-to-terminal price ratio `x>=1` and all real prior mixtures `lambda in [0,1]`, the unrestricted prior-blind **deterministic** minimax expected regret equals `(5-x)/141` for `1<=x<=3`, or `2/141` for `x>=3`. The optimizer is native complete tree C or E, respectively. There is no candidate-tree restriction in the lower-bound proof.

New load-bearing argument: two hard terminal-observer fibers force four root observations at weight one; when uniform root mass equals four the multiplicity root mass also equals four. Combined with integer-supporting inequalities derived from *six exact unrestricted finite Bellman anchors* at x=1,3 and lambda=0,620/3299,1, this excludes every putative better native tree through exhaustive integer cases. Continuous price and prior ranges are handled symbolically, not by price-grid sampling.

## Original frozen evidence and exact scope

- Original Bellman anchor index: EC49FRI exact check result and six corresponding raw native Bellman JSONs, pinned by SHA256 in the inherited EC49FRI release, PR #2621, https://github.com/awdawmip/enterprise-math/pull/2621.
- Original terminal observation fibers: {8,139} and {46,140}, each state of multiplicity 1; original native reconstruction / fiber certificate in EC49FRJ, PR #2624, https://github.com/awdawmip/enterprise-math/pull/2624.
- Original complete named trees A–E and their full-state path replay: EC49FRL, PR #2630, https://github.com/awdawmip/enterprise-math/pull/2630. Feasible coefficients C=(5,295,5,685), E=(4,298,4,688).
- Predecessor randomized minimax theorem: EC49FRM–FRN, PR #2633, https://github.com/awdawmip/enterprise-math/pull/2633. Combining results produces exact ratio randomized/deterministic = 2679/3299 over all x>=1.

Frozen original source master SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.
Original BRC profile CSV SHA256: `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.
Original five-tree certificate SHA256: `2164b2a374c46bad29d5b669573fcafe87218f946e1bdd42e78dc78642ba0dfb`.

## Executed verification

1. `python EC49FRO_DETERMINISTIC_MINIMAX_VERIFY_20261117.py --evidence-root /mnt/data/em_r4_current` (local source archive extracted) **PASSED**.
2. Reconstructed original 141x228 response system and original 310 multiplicities; found exactly the two expected nontrivial terminal-observation fibers, checked four unit-multiplicity mandatory states and root query 148 discrimination.
3. Compared each of the six raw unrestricted Bellman certificates against its SHA256 in the inherited EC49FRI index; checked their exact optimal rational values. This reuses previously computed exhaustive Bellman minima; no new Bellman DP was run in this turn.
4. Replayed inherited complete original tree vectors A–E and matched their exact four cost coefficients.
5. Checked rational/symbolic case inequalities at full interval boundaries and representative interior points. Universal quantifiers follow from the written integer-case proof plus affine/concavity lemmas.
6. Self-contained local evidence archive `EC49FRO_DETERMINISTIC_MINIMAX_COMPLETE_EVIDENCE_20261117.tar.xz`: SHA256 `9e1944a6280b81f69faf2485c8873ee593717375774499f6a5048856ef6a7495`; 22 files listed in a signed-size-independent SHA256 manifest, all read/checked again after archive creation. It includes full proof, executable verifiers, frozen original data, six raw Bellman anchor JSONs, original full tree JSONs, archived native reconstruction and execution logs. This archive is a local ChatGPT downloadable companion, not a claim that its binary bytes are attached to GitHub.

Console:
```
PASS: exact full-real-domain deterministic minimax proof arithmetic
formula: R_det=(5-x)/141 [1,3]; R_det=2/141 [3,infinity)
randomized/deterministic ratio: 2679/3299
PASS: original frozen 141x228 reconstruction, four hard states, six hash-matched Bellman anchors, five feasible tree vectors
```

## Truth and control state

Status: `AUTHOR_PROVED / EXACT_FINITE_CHECKED_REUSING_ARCHIVED_NATIVE_ANCHORS / NOT_REVIEWED`. Review of the original six native Bellman minima and new all-tree integer/fiber derivation remains independent-review work. No Lean/formal verification was attempted.

As of 2026-11-17T08:34:46.070592Z, native exact-task lookup request `r4-ec49fro-20261117-1631-current-task-read-01` resolved `SUCCEEDED` but returned `NO_CANONICAL_PUBLICATION_DIRECTORY` for `RS-EC49AS` at Source `92d3c62e14a45481e02bbf220b7cab9655d7e390`. This is a scoped directory observation, not a current full owner projection. Native researcher execution authority remains unconfirmed; no formal Task CLAIM, Result, Review or Activity checkpoint is asserted. Independent portable publication only.

## Next question

For a *proper* prior interval [a,b] within [0,1], characterize the unrestricted deterministic minimax policy over all native trees and exact integer Pareto facets. Also investigate multidimensional priors with observer-provenance-preserving randomized support bounds.
