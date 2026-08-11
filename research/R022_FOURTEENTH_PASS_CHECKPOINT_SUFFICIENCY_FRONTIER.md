# R022 Fourteenth-Pass Deepening — Information-Sufficient Causal Rewind and Checkpoint Pareto

**Researcher-ID:** `EM-R022-HC7B4A`  
**Task:** `RS-R022-HASHCLASH-BRC-TOOL-MINING`  
**Taskbook base:** `89fb6c99fa2a00e42f58c1fc11ea016b7421f3be`  
**Owner PR:** `#497`  
**Status:** `FOURTEENTH_PASS / RESEARCH ADDENDUM / NOT CANONICAL`

## Executive result

Earlier R022 passes separated causal rewind depth from future precision debt. Pass 14 combines them into an exact checkpoint sufficiency criterion and a storage/rewind Pareto frontier.

A checkpoint is not useful merely because it is earlier. Its complete retained encoding must contain enough information to determine the stronger target semantic token.

For an arbitrary existing partition `E` and target partition `F`, define

`M(E=>F) = max_{C in X/E} number of F-classes intersecting C`.

This generalizes pass 9, which assumed `F` refined `E`.

### General Side-Information Theorem

The minimum cardinality of a shared side-label alphabet `A` such that

`(E-token(x), side(x))`

determines the `F` token for every state is exactly `M(E=>F)`.

Thus fixed-width side cost is

`B(E=>F)=ceil(log2 M(E=>F))`.

Zero bits are needed iff `E` already determines `F`, equivalently `E subseteq F` as relations.

For a nested sequence of progressively forgetful checkpoints, the latest checkpoint whose retained encoding determines `F` is the exact minimal no-extra-metadata rewind point. Adding side metadata can move that recovery point forward. This creates an explicit Pareto frontier between checkpoint metadata bits and rewind depth.

Recommended classification:

`BRC_INFORMATION_SUFFICIENT_REWIND_FOUND / GENERAL_SIDE_INFORMATION_BOUND_EXACT / CHECKPOINT_SUFFICIENCY_CRITERION_FOUND / STORAGE_REWIND_PARETO_FOUND / CAUSAL_REWIND_SHARPENED / NOT_CANONICAL`.

---

## 1. Generalizing future precision debt

Pass 9 considered a refinement `F subseteq E`: every new `F` class lay completely inside an old `E` class.

A replay checkpoint may instead carry an encoding that is finer in some directions and coarser in others. To determine a target token from an existing token, only the number of possible target classes compatible with each existing class matters.

For each `E` class `C`, define

`r_{E=>F}(C) = |{D in X/F : C intersect D != empty}|`.

Then

`M(E=>F)=max_C r(C)`.

When `F subseteq E`, this reduces exactly to pass 9's number of refined subclasses inside `C`.

## 2. General Side-Information Theorem

Suppose runtime retains the `E` class identifier plus one side label from a global finite alphabet `A`.

### Lower bound

Inside an `E` class touching `M` different target `F` classes, those target cases require distinct side labels. Otherwise one `(E-token, side-label)` value would decode to two different `F` classes.

Thus `|A|>=M`.

### Upper bound

Inside each `E` class, locally enumerate the target `F` classes that intersect it by labels `0,...,r(C)-1`. The same alphabet can be reused independently in every `E` class.

Hence `|A|=M` suffices.

So the bound is exact.

## 3. Checkpoint sufficiency criterion

A checkpoint encoding `E` can determine the target `F` with **no extra side metadata** iff

`M(E=>F)=1`.

This is equivalent to every `E` class lying inside one `F` class, i.e.

`E subseteq F`.

Thus the exact checkpoint question is:

> does the complete retained checkpoint equivalence refine the target equivalence?

If not, NO_RESURRECTION prevents exact recovery from that checkpoint token alone.

## 4. Latest sufficient checkpoint theorem

Consider checkpoints

`E_0 subseteq E_1 subseteq ... subseteq E_k`

on the same semantic state space, where later checkpoints are progressively more forgetful/coarse.

Fix target `F`.

The sufficient indices

`{i : E_i subseteq F}`

form a prefix. If nonempty, let

`j*=max{i : E_i subseteq F}`.

Then:

- checkpoint `j*` is sufficient to determine the target;
- every later checkpoint is insufficient without extra retained information;
- therefore minimal no-extra-metadata rewind depth from current `k` is

`k-j*`.

This is the exact same-domain causal-rewind theorem.

## 5. Storage can buy shallower rewind

At an insufficient checkpoint `E_i`, store a side label of minimum alphabet `M(E_i=>F)`.

The augmented encoding `(E_i,side)` now determines `F`, so recovery can start at checkpoint `i` instead of rewinding farther.

This produces a storage/rewind tradeoff:

`(fixed side bits B(E_i=>F), rewind depth k-i)`.

A compiler can take the Pareto-minimal checkpoints under the chosen cost model.

## 6. Eight-state witness

Take progressively coarser checkpoints:

- `E0`: 8 singleton states;
- `E1`: four pairs;
- `E2`: two quartets;
- `E3`: one 8-state block (current checkpoint).

Target `F=E1`.

Then:

- E0: 0 side bits, rewind depth 3;
- E1: 0 bits, depth 2;
- E2: 1 bit, depth 1;
- E3: 2 bits, depth 0.

E0 is dominated by E1. Pareto frontier:

`(0 bits, depth 2)`,

`(1 bit, depth 1)`,

`(2 bits, depth 0)`.

This is a literal storage-versus-recomputation-depth Pareto generated by future precision debt.

## 7. Exhaustive finite evidence

Artifact:

`experiments/r022_checkpoint_sufficiency_frontier.py`.

On five states:

- all 52 partitions;
- all `52^2=2704` ordered existing/target partition pairs;
- constructive local side-label upper bound checked for every pair;
- zero-bit iff existing partition determines target checked throughout;
- side-alphabet distribution:
  - M=1: 358 pairs;
  - M=2: 1825;
  - M=3: 485;
  - M=4: 35;
  - M=5: 1;
- counterexamples: 0.

Focused pass-14 tests: **4/4 PASS** in the research execution environment.

## 8. Relation to HashClash rollback

HashClash's script uses a fixed timeout-driven one-stage rollback. R022 still does not reinterpret that heuristic as an information-minimal rewind algorithm.

The new generic controller would instead ask, for the stronger residual requirement now needed:

1. what target semantic partition/interface must be recovered?;
2. which retained checkpoint is the latest whose complete encoding determines it?;
3. if later checkpoints stored side metadata, which one becomes sufficient after charging that metadata?;
4. what recomputation depth/work follows from choosing that checkpoint?

Thus the source remains motivation; the information-sufficient rewind theorem is a generic finite compiler primitive.

## 9. Relationship to CRD

Pass 4's Certificate Reuse Depth and pass 14's information-sufficient rewind solve different problems.

- **CRD:** after a context change, which existing proof certificates remain valid without recomputation?
- **checkpoint sufficiency:** after semantic/future strengthening, which retained execution state still contains enough information to reconstruct the newly required token?

Both can affect rewind, but proof validity and state information sufficiency must remain separate axes.

## 10. Tool delta

### `checkpoint_sufficiency`

Given existing checkpoint encoding and target semantic equivalence, test whether the former refines the latter.

### `checkpoint_side_debt`

Compute `M(E=>F)` and fixed-width bit lower bound for making a checkpoint target-sufficient by side metadata.

### `rewind_frontier`

Across retained checkpoints, output Pareto points involving:

- metadata bits/storage;
- rewind depth;
- expected replay work;
- checkpoint size;
- target language/semantic version.

## 11. Prior-art/rooting boundary

Partition refinement, sufficient statistics, checkpointing and storage/recomputation tradeoffs are established ideas. R022 claims no generic novelty for them.

The Enterprise Math residue is the exact placement of the partition-side-information lower bound inside BRC's no-resurrection/replay controller and the resulting checkpoint storage/rewind Pareto.

## 12. R021 feedback

Recommended additions:

1. Generalize pass-9 debt to arbitrary existing/target partitions using intersection counts.
2. Define checkpoint sufficiency as `E subseteq F`, not as “checkpoint is old enough.”
3. Define latest sufficient checkpoint and exact no-extra-metadata rewind depth for nested forgetting sequences.
4. Add checkpoint side-debt bits and storage/rewind Pareto.
5. Keep CRD certificate validity separate from checkpoint semantic sufficiency.
6. Require replay contracts to name both target precision and checkpoint information level.

No correction is requested to R023.

## 13. Fourteenth-pass classification

`BRC_INFORMATION_SUFFICIENT_CAUSAL_REWIND_FOUND / GENERAL_CHECKPOINT_SIDE_DEBT_EXACT / STORAGE_REWIND_PARETO_FOUND / CRD_VS_STATE_SUFFICIENCY_SEPARATED / R021_FEEDBACK_READY / NOT_CANONICAL`.
