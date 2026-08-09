# P022 — Observation, History, Collision, and Repair Checkpoint

Status: `ACTIVE RESEARCH CHECKPOINT / PROVED WIP ROUTER`  
Owner: `program/p022-geometry-v2`  
Task branch: `research/p022-observation-history-20260809`

This file is a compact router for the current P022 research generation. It does not change canonical `PROBLEM_STATUS` and does not promote WIP results to `main`.

## 1. Current theorem groups

### Observation geometry and history

- `P022_BARLOW_LOCAL_OBSERVABILITY.*`: two consecutive coordination shells recover the current unordered absolute-drift pair; uniform state-observation depth is exactly two.
- `P022_BARLOW_COORDINATION_HISTORY_SUPPLEMENT_01.*`: full coordination history reconstructs the global shortest-path multiplicity spectrum, not merely its total.
- `P022_BARLOW_HISTORY_STRATIFICATION.*`: one terminal height-stratified shell profile is information-equivalent to the full coordination history, up to side exchange.

### Checkpoint fibers and collision statistics

- `P022_BARLOW_HIGHER_COLLISION_PRECISION.*`: generalized binomial power-sum factorization and exact higher-collision Pareto conflict.
- `P022_BARLOW_WORST_FIBER_SCHEDULING.*`: odd-balanced/pair-balanced schedule exactly minimizes the largest observation fiber.
- `P022_BARLOW_FIBER_CONVOLUTION.*`: complete selected-layer fiber profiles form a multiplicative convolution algebra and invert to the unordered checkpoint segment geometry plus hidden tail.
- `P022_BARLOW_PAIR_COLLISION_ALIAS.*`: exact fixed-`N`, fixed-`m` examples show `J_2` alone does not identify checkpoint geometry.

### Event-driven repair

- `P022_BARLOW_EXCURSION_ORIENTATION_REPAIR.*`: one orientation bit per zero-departure excursion is necessary and sufficient for one-sided signed recovery.
- `P022_BARLOW_TWO_SIDED_REPAIR.*`: two-sided exact repair is one bit per zero excursion plus one bit per diagonal side split; fiber size is `2^(E+B)`.
- `P022_BARLOW_REPAIR_POLYNOMIAL.*`: weighted chamber polynomial packages repair dimension, quotient image, microscopic domain, aggregate repair load, and P011 collision data.

## 2. High-value exact conclusions

1. Precision optimization is multi-objective. Ordinary balanced checkpoints maximize image size and minimize `J_2`, while odd-balanced pair packets minimize the maximum fiber / highest possible nonzero collision order.
2. The complete P011 collision polynomial is an exact encoding of the selected-layer checkpoint geometry **up to segment order**, including an unobserved tail; `J_2` alone has exact aliases.
3. Current hidden Barlow drift has sharp observation depth two, while richer shell-wide future queries may still require an arbitrarily long height horizon.
4. Coordination history can be re-encoded in one terminal shell stratification; retaining history can change the information order among observables.
5. Hidden state is created at specific boundary events: zero departures create orientation freedom and diagonal splits create side-label freedom.

## 3. Negative boundaries

- Do not promote ordinary balanced spacing to a universal optimum for the full collision spectrum.
- Do not infer checkpoint segment order from a complete fiber profile or collision polynomial.
- Do not infer coordinate-labelled geometry from coordination history or the global multiplicity spectrum.
- Do not generalize two-channel quadratic-history reconstruction to three or more channels; explicit successor-energy collisions exist.
- Do not identify average fiber size, maximum fiber size, `J_2`, or path total with the complete ambiguity state.

## 4. Prior-art-sensitive ingredients

Classical ingredients include central/binomial power sums, Franel-type sequences, Stirling and binomial inversion, finite Dirichlet convolution, Catalan/ballot decompositions, Weyl-chamber walks, and sum-of-two-squares arithmetic. Enterprise Math claims only the proved P022 specializations and their integration into the finite-resolution observation/repair framework. Historical novelty remains `NOVELTY_UNVERIFIED` where not separately audited.

## 5. Verification boundary

The branch contains ordinary proofs, exact formulas, executable reference modules, and many bounded exhaustive reconstructions. A repository-level CI checkpoint is still required before calling this generation implementation-clean. Executable checks support proof auditing but do not upgrade branch WIP to canonical-main theorem status.

## 6. Next frontier

After CI/consistency cleanup, continue from the strongest open questions rather than waiting for integration:

- characterize Pareto frontiers for multiple collision orders;
- determine how much ordered checkpoint placement can be recovered when labelled observations are retained;
- analyze the repair polynomial beyond its endpoint coefficients and classical `z=1` chamber count;
- abstract only those observation/history principles whose weakest hypotheses genuinely exceed the Barlow geometry specialization.
