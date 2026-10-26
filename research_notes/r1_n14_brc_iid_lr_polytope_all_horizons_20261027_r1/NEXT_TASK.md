# R1 portable successor — minimal predictive repair for non-IID LR-fiber compressions

## Consumed frontier (do not re-prove)

`PROOF.md` in this research unit gives the all-finite-horizon theorem: strictly positive IID two-law histories, recursively updatable time-typed `x`, and constant Q/P likelihood ratio on every `x` fiber imply universal common-kernel Markovization and an *exact rational linear occupancy polytope* for both laws and any terminal observer factoring through `x`. Thus the question of an IID LR-fiber nonconvex example at N>=3 is **closed negatively under exactly those hypotheses**. The prior N=3 non-IID example remains nonconvex and is not refuted. Exact finite program checks all 121 paths at N=4 and both law distributions for two policy-pairs; it does not substitute for the theorem proof. Independent native review and Lean are pending.

## Hard next question

Given positive **non-IID** P,Q on a finite history tree and a time-typed deterministic recursive compression x that may have unequal conditional next-symbol laws on its fibers, construct a canonical **coarsest stable refinement** z=(x,repair) that preserves both the likelihood ratio of histories and the P/Q compressed successor kernels. Precisely specify the meaning of coarsest: among time-typed right congruences refining x and satisfying both-law LR and SL. Prove existence/uniqueness up to state renaming or give a minimal counterexample if arbitrary common refinements need not admit a meet. Check the exact N=3 non-IID witness from `research_notes/r1_n14_brc_lr_fiber_nonconvex_n3_20261027_r1/PROOF.md` and report its minimal state count/time profile.

## First finite exact unit

Start with all full prefixes as distinct terminal-labeled nodes. Construct backwards equivalence classes with the same current x and LR, and compare per-law future transition probability mass to each already-refined next-level class (not merely to x). Since finite, test a repeated-fiber split to a fixed point. Prove that the procedure is minimal for the stipulated observer/future operation semantics, and verify its output with integer/rational arithmetic on the 40-prefix N=3 counterexample. Distinguish the full-history right congruence from the quotient transition *mass* congruence.

## Evidence / return contract

Provide theorem or explicit obstruction to coarsest existence; complete proof of quantifier scope; input kernels; exact partition certificates and counts; executable checker if needed; source pins; a specified subsequent question. Extend an existing BRC observer/predictive-state method instead of inventing a top-level tool. Registration/provenance is not CLAIM or Result acceptance. Maintain review, P000 six-dimensional world, and SOURCE-native/published evidence distinctions.
