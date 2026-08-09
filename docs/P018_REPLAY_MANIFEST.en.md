# P018 v2 — Semantic Replay Manifest

Status: `ACTIVE REPLAY MANIFEST / NO NEW MATHEMATICS`  
Target branch: `program/p018-precision-v2`  
Baseline: `main@c8aae69491fe50b107ca98b5777b9653be9f9aaf`  
Primary historical source: `agent/p018-critical-grid@ee6d69fc2bb9894a47a3d5c6273d50d286047ca8` / PR #68  
Other sources: `research/p018-graded-precision`, `research/p018-proof-certificates`, `research/p018-factor-precision`, `research/p018-centered-prime-radius`

## 1. Purpose

This branch is neither a rebase of #68 nor a mechanical copy of Supplements 12–26.

Its purpose is to compress historical P018 work into a sustainable **precision-specific program owner**, while handing general future-compatible quotient / operation-language mathematics to A2/P023.

Hard rule:

> Replay work performs ownership audit, semantic transport, canonical numbering, implementation replay, and validation. It creates no new mathematics.

If audit exposes a genuinely new theorem, replay stops and the theorem returns to the appropriate owner.

---

## 2. Five target layers

### P18-L1 — Precision State / Pair / Kernel

P018 keeps:

- typed interpretation of finite precision states;
- State Pair as a subtraction-free comparison primitive;
- kernel/diagonal interpretation for precision observations;
- optional signed difference as coordinates on Pair rather than a primitive substrate;
- precision-specific critical-square / holonomy readings.

Primary source assets:

- `state_pair.py`
- `critical_grid.py`
- `EnterpriseMath/State/CriticalGrid.lean`
- precision-specific statements from old #68 T110–T128.

Classification: `KEEP_P018`.

### P18-L2 — Time / Coalescence / Spectrum Interface

P018 keeps:

- interface between precision observations and P010/P011 history merging;
- labelled kernel-time filtration;
- merge-time matrix as a precision/history observation coordinate;
- boundaries for how precision coarsening affects P011 spectra.

Primary source assets:

- `coalescence_time.py`
- `collision_increment.py`
- `merge_time_complex.py`
- `EnterpriseMath/State/Coalescence.lean`
- precision-facing corollaries from old #68 T129–T156.

Generic deterministic coalescence belongs to A1/P010/P011/P020; P018 keeps only the precision interface.

Classification: `KEEP_P018_COROLLARY` / `DEFER_A1_MOTHER`.

### P18-L3 — Observation Closure / Context Separation

P018 keeps:

- the precision interpretation of whether a raw observation carries the declared future language;
- context-separation depth as a finite certificate explaining why detail must be retained;
- positive/negative boundaries for closed versus non-closed precision observations.

The following general results move to A2/P023:

- finite operation-family congruence criterion;
- largest compatible equivalence inside an observation kernel;
- generic predictive/contextual closure;
- generic minimum reusable interface.

Primary source assets:

- `observation_kernel.py`
- `predictive_closure.py`
- `contextual_closure.py`
- `context_separation.py`
- `EnterpriseMath/State/ObservationClosure.lean`
- `EnterpriseMath/State/OperationCongruence.lean`
- `EnterpriseMath/State/ContextSeparation.lean`

Classification:

- precision interpretation/counterexamples → `KEEP_P018`;
- generic theorem implementation / Lean mother statements → `DEFER_A2_P023`.

### P18-L4 — Precision Transport

P018 keeps:

- defect/response/carry as operation-specific transport of a precision projection;
- interpretation of one-shot transport branching under a concrete precision observation;
- separation between persistent detail and transient correction token;
- radix addition/multiplication and other integer instances;
- carry/remainder structured composition.

Generic finite communication/interface theorems move to A2/P023 or a future transport core rather than being duplicated in P018.

Primary source assets:

- `transport_branching.py`
- `transport_fusion.py`
- `reusable_interface.py`
- `EnterpriseMath/State/TransportProtocol.lean`
- `EnterpriseMath/State/ReusableInterface.lean`
- existing `EnterpriseMath/Precision/Carry.lean`

Classification:

- radix / precision-specific transport → `KEEP_P018`;
- generic protocol/interface minimum theorem → `DEFER_A2_P023`.

### P18-L5 — Arithmetic / Proof Applications

Retain P018 applications and pressure tests without treating them as general core:

- graded precision;
- finite proof certificates;
- factor precision;
- prime-gap slack / centered-prime radius;
- square-basin quotient/root transport;
- all-power quotient transport;
- precision corollaries consumed by P017/Legendre work.

Historical sources:

- `research/p018-graded-precision`
- `research/p018-proof-certificates`
- `research/p018-factor-precision`
- `research/p018-centered-prime-radius`
- QuotientBasin assets from #68.

Classification: `APPLICATION_ONLY`, with theorem-by-theorem semantic absorption / replay audit.

---

## 3. Source asset classification

| Source asset/family | v2 classification | Target |
|---|---|---|
| State Pair / diagonal / pair coordinates | `KEEP_P018` | P18-L1 |
| Critical-grid endpoint/holonomy precision reading | `KEEP_P018` | P18-L1 |
| Generic deterministic coalescence | `DEFER_A1_MOTHER` | A1/main |
| Precision↔coalescence interface | `KEEP_P018_COROLLARY` | P18-L2 |
| Generic predictive closure | `DEFER_A2_P023` | A2/P023 |
| Generic operation congruence/descent | `DEFER_A2_P023` | A2/P023 |
| Context separation as precision certificate | `KEEP_P018` | P18-L3 |
| Generic contextual-equivalence algorithm | `DEFER_A2_P023` | A2/P023 |
| Carry/defect/radix transport | `KEEP_P018` | P18-L4 |
| Generic transport protocol minimum | `DEFER_A2_P023` | A2/P023 / future transport core |
| Generic reusable-interface theorem | `DEFER_A2_P023` | A2/P023 |
| Graded/factor/proof/prime/square applications | `APPLICATION_ONLY` | P18-L5 |
| Assets already exact on main | `ALREADY_MAIN` | consume; do not copy |
| Duplicate old numbering/prose only | `PROVENANCE_ONLY` | PR/Git history |

---

## 4. Numbering strategy

P018 v2 **does not continue the historical branch with Supplement 27+**.

Historical T identifiers remain provenance references, but long-term interfaces should prefer conceptual core documents/modules after clean replay. Only statements entering the canonical theorem ledger receive conflict-free canonical numbering.

Never overwrite an identifier or Supplement path already owned by main merely to preserve historical numeric continuity.

---

## 5. Replay batches

### Batch A — manifest + source audit

- this manifest;
- source→owner matrix;
- check main for exact/strict generalizations;
- no theorem code replay.

### Batch B — P18-L1 precision state core

Replay first:

- State Pair;
- precision-specific critical grid;
- exact interfaces to P009/P010.

### Batch C — P18-L3/L4 precision-specific context/transport

Replay precision specializations only; consume generic mother theorems from A2/P023.

### Batch D — applications

Audit graded/proof/factor/centered-prime/quotient-basin small branches one by one; do not replay material already on main.

---

## 6. Freeze contract for #68

From the creation of this manifest, PR #68 becomes a `FROZEN REPLAY SOURCE`:

- no new theorem or Supplement commits;
- provenance/migration notes remain allowed;
- every unique source asset must eventually map to exactly one of `ALREADY_MAIN / KEEP_P018 / DEFER_* / APPLICATION_ONLY / PROVENANCE_ONLY`;
- after all assets are mapped and replayed, #68 can close without deleting branch history.

---

## 7. Completion criteria

P018 v2 is compressed when:

1. the current P018 owner is based on recent main;
2. P018 no longer duplicates A2/P023 generic closure/congruence theorems;
3. precision-specific state/context/transport has a stable long-term interface;
4. historical applications have theorem-by-theorem semantic audits;
5. old #68 and small historical branches can become provenance;
6. new work no longer requires reading a 100+ commit historical tree merely to determine theorem ownership.
