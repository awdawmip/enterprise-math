# R022 Fifteenth-Pass — Research-Only BRC Compiler Consolidation

**Researcher-ID:** `EM-R022-HC7B4A`  
**Task:** `RS-R022-HASHCLASH-BRC-TOOL-MINING`  
**Owner PR:** `#497`  
**Status:** `FIFTEENTH_PASS / COMPILER CONSOLIDATION / NOT CANONICAL`

## Result

After fourteen semantic/source/minimality passes, R022 now has enough separation of concerns to consolidate a small finite-state compiler core without promoting any component to the shared tool surface.

Artifact:

`experiments/r022_brc_compiler_core.py`.

The core deliberately does **not** contain MD5/SHA-1 attack code. It integrates only the generic contracts that survived source pressure tests and kill tests.

## Surviving layers

### Semantic precision

- `future_kernel` — compute the coarsest deterministic future-exact partition for explicit finite futures;
- `target_precision` — intersect required future precision with the currently retained equivalence;
- `required_distinction_pairs` — expose exactly which currently merged pairs must split.

### Proof-carrying representation checks

- `verify_future_basis`;
- `verify_feature_basis`;
- `verify_residual_join` for Boolean support;
- `verify_residual_aggregate` for declared aggregate monoids;
- `verify_boolean_interface_factor` for finite BRC-Connect factors.

### Replay / no-resurrection

- `side_alphabet` and `side_bits` — exact checkpoint metadata lower bound;
- `checkpoint_sufficient` — test whether retained encoding already determines target precision.

### Connection

- `deterministic_row_quotient` — context-complete deterministic connection classes;
- Boolean shared-atom factor verifier.

These are deliberately small semantic/verifier primitives. Hard optimizers and heuristic proposers remain outside the trusted core.

## End-to-end synthetic model

A six-state finite system starts from two three-state coarse classes. Two declared future probes jointly refine the target to six singleton classes.

The compiler computes:

- 6 required pair distinctions;
- both futures required by the chosen synthetic basis;
- both candidate raw features required;
- current coarse checkpoint not target-sufficient;
- minimum abstract side alphabet 3;
- minimum fixed side debt 2 bits.

The same test then performs:

- an exact Boolean support RJC rewrite;
- a mutation that drops necessary support and is rejected;
- an exact three-atom Boolean compatibility factor;
- a mutation dropping one interface atom and rejected with a concrete pair witness.

## Mutation suite

Five cross-layer mutations are checked:

1. remove a necessary future;
2. remove a necessary raw feature;
3. perform an unsafe support rewrite;
4. truncate an exact compatibility factor;
5. pretend an insufficient checkpoint can resurrect the target without side information.

Result:

**5/5 mutations rejected or classified correctly.**

This is important because each individual theorem family had already passed isolated tests; pass 15 verifies that their interfaces can be composed without silently changing the declared semantics.

## Compiler architecture

The resulting research architecture is:

`declare observable/aggregation`

`-> declare future language`

`-> compute required future kernel`

`-> expose distinction pairs / semantic frontier`

`-> choose static/adaptive extractors and executable branch macros`

`-> independently verify exact rewrites`

`-> execute quotient-descending operations / branch-local partial operations`

`-> connect cones through deterministic or shared-atom interfaces`

`-> reuse context/language-scoped certificates`

`-> if future strengthens, compute checkpoint debt / rewind frontier`

`-> otherwise label any unsupported pruning HEURISTIC`.

## What is not in the trusted core

The following remain proposers/optimizers or problem-specific modules:

- minimum Set Cover/RJB search;
- minimum Test Cover / raw feature basis;
- optimal adaptive decision tree;
- minimum Boolean rank/biclique cover;
- heuristic branch ranking/tunnel scoring;
- probabilistic/weighted search policies.

They may be sophisticated or approximate because exactness is guarded by independent semantic verifiers wherever feasible.

## T01–T13 closure assessment

The original taskbook requested source reconstruction, BSR, branch cones/connect, safe recoalescence, neutral operations, rewind, potential, branch-budget Pareto, synthetic experiments, generic prototypes, kill tests, prior-art rooting and R021 feedback.

All thirteen requested areas have now been substantively addressed. Several were sharpened beyond the initial hypotheses:

- generic scalar recoalescence potential was killed;
- causal rewind was restricted by exact-RCC/no-resurrection and then rebuilt as information-sufficient checkpoint selection;
- ABB was split into EXACT / REPLAY_EXACT / HEURISTIC;
- BRC-Connect gained deterministic row quotients and optional Boolean shared-atom factorization;
- branch signature gained static, distinction-cover and adaptive-acquisition layers;
- Boolean support recoalescence was explicitly gated by idempotent aggregation semantics.

## Current recommendation

Do not promote the entire compiler as one canonical theorem/tool package.

The most stable small shared candidates, after R021/R023 review, are:

1. future-kernel / refinement-trigger semantics;
2. RJC/RAC proof-carrying rewrite verification;
3. context-scoped NCC with dependency footprint;
4. checkpoint sufficiency / precision debt;
5. typed BRC-Connect interface verifier.

Hard optimization strategies should remain replaceable outer layers.

## Classification

`R022_T01_T13_SUBSTANTIVELY_COMPLETE / BRC_RESEARCH_COMPILER_CORE_CHECKED / CROSS_LAYER_MUTATIONS_5_OF_5 / GENERIC_SEARCH_NOVELTY_NEGATIVE / TRANSFERABLE_CERTIFICATE_CALCULUS_POSITIVE / R021_FEEDBACK_READY / NOT_CANONICAL`.
