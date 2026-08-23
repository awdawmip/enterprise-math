<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-NATIVE-FILAMENT-SHARP-BOUND-INDEPENDENT-REPLICATION",
  "title": "Native Prime Filament — Sharp-Bound Independent Replication",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "NATIVE_PRIME_FILAMENT_SHARP_BOUND_INDEPENDENTLY_RECONSTRUCTED_OR_REFUTED",
  "next_action": "Using only the blind carrier packet, independently derive the maximal-flower classification, rolling-overlap dynamics, global filament-length result, and an exact witness or counterexample; freeze proof and checker evidence before any source comparison.",
  "dependencies": [
    "research_inputs/PRIME_NATIVE_FILAMENT_BLIND_REPLICATION_PACKET_20260823.md@123cfecb25b30fe2ff9d4fddf900b6e3f2569a7a"
  ],
  "source_refs": [
    "research_inputs/PRIME_NATIVE_FILAMENT_BLIND_REPLICATION_PACKET_20260823.md@123cfecb25b30fe2ff9d4fddf900b6e3f2569a7a"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "prime",
    "native-trisector",
    "maximal-flower",
    "filament",
    "independent-replication",
    "modular-obstruction"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PNFREP",
  "origin_kind": "REPLAY_OR_INTEGRATION",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Native Prime Filament — Sharp-Bound Independent Replication

Task-ID: `RS-PRIME-NATIVE-FILAMENT-SHARP-BOUND-INDEPENDENT-REPLICATION`

Intended owner branch:

`research/prime-native-filament-sharp-bound-replication`

Hard target:

`NATIVE_PRIME_FILAMENT_SHARP_BOUND_INDEPENDENTLY_RECONSTRUCTED_OR_REFUTED`

## Context

A free-research branch reports a sharp global statement about rolling overlaps of maximal local prime flowers in the frozen native tri-sector integer allocation. That report is not canonical evidence and is deliberately withheld.

This task is a clean independent replay. The result may confirm the source claim, produce a narrower theorem with explicit exceptional cases, or refute it.

The research value lies in a complete local-to-global proof: carrier adjacency, prime-eligible neighbor structure, overlap dynamics, modular capacity, and an independently certified extremal witness must all agree.

## Parent-Chain Identity

Lineage is `REPLAY`, not continuation of a prior taskbook.

The parent chain is:

`USER PRIME-RESEARCH DIRECTION -> ENTERPRISE MATH PRIME BATCH DRIVER -> THIS INDEPENDENT REPLAY`.

No worker identity from the free-research source is inherited. Runtime Researcher-ID allocation is external to this taskbook.

## Locked Source Package

Read and execute only:

`research_inputs/PRIME_NATIVE_FILAMENT_BLIND_REPLICATION_PACKET_20260823.md@123cfecb25b30fe2ff9d4fddf900b6e3f2569a7a`.

Before the independent report is frozen, do not inspect any file or branch whose name suggests native maximal prime flowers, prime filaments, sharp length, transverse classes, explicit witnesses, or source checkers.

Ordinary exact mathematics and independently written computation are allowed. The source theorem statement, claimed numerical bound, source residue table, and source witness are intentionally not inputs.

## Previous Outputs

No prior taskbook output is accepted as evidence for this replay.

The existence of a free-research branch is motivation only. It supplies neither a lemma nor a trusted computation.

## Input Artifact Provenance

The locked packet was authored by the Prime batch Driver from the primitive tri-sector allocation and neighbor formulas, while withholding all source proof steps and outcome-bearing data.

Its carrier formulas are the only inherited mathematical data. Every prime-specific classification must be reconstructed.

## Exact Research Question

Determine the exact global behavior of rolling overlap filaments of maximal prime flowers defined in the packet.

The report must give one of these mutually exclusive terminal outcomes:

1. `SHARP_FINITE_BOUND_PROVED_AND_ATTAINED`;
2. `FINITE_BOUND_PROVED_BUT_SHARPNESS_OPEN`;
3. `SOURCE_SCOPE_REQUIRES_NARROWING`;
4. `UNBOUNDED_OR_ARBITRARILY_LONG_FAMILY_PROVED`;
5. `MATERIAL_COUNTEREXAMPLE`;
6. `OPEN_AFTER_CERTIFIED_PARTIAL_PROGRESS`.

A successful finite-bound result must include:

- a complete proof that no longer nonexceptional filament exists;
- a precise list of small-prime and boundary exceptions;
- a witness attaining the claimed bound;
- a complete classification of every surviving extremal residue/presentation channel.

The unique hard target is met only when the sharp-bound question is independently settled or materially refuted.

## Scope Guard

### In scope

- derivation of prime-eligible neighbor patterns from exact residues;
- center-slot and shell-parity classification;
- sorted and unsorted five-prime packet identities;
- overlap transition laws on consecutive shells;
- derivation or refutation of a conserved transverse coordinate;
- modular covering/capacity arguments for arbitrary filament length;
- exact primality certification of every extremal witness value;
- cyclic-sector and orientation-reversal ablations;
- comparison with classical admissible prime tuples only after the internal theorem is frozen.

### Out of scope

- any assertion that the underlying prime tuple is historically new;
- infinitude claims not proved by this task;
- changing the integer allocation or nearest-neighbor graph to rescue a claim;
- treating a finite census as a global proof;
- using source scripts, source witness values, or source residue tables before freeze;
- promoting the carrier to Foundation or calling presentation-dependent coordinates intrinsic.

Kill condition:

If the claimed global obstruction fails for one exact admissible residue state or one certified longer filament, preserve the smallest counterexample and classify the source claim as refuted or narrowed. Do not repair the definition post hoc.

## Required Outputs

Produce all of the following:

1. Full report:
   `research_output/PRIME_NATIVE_FILAMENT_SHARP_BOUND_INDEPENDENT_REPLICATION_20260823.md`
2. Reducer result:
   `research_output/reducer_results/PRIME_NATIVE_FILAMENT_SHARP_BOUND_INDEPENDENT_REPLICATION_REDUCER_20260823.md`
3. Independent exact checker:
   `experiments/prime_native_filament_sharp_bound_independent_checker.py`
4. Machine-readable residue/channel table:
   `research_output/PRIME_NATIVE_FILAMENT_RESIDUE_CHANNELS_20260823.csv`
5. Evidence event stream:
   `research_output/evidence/PRIME_NATIVE_FILAMENT_SHARP_BOUND_INDEPENDENT_REPLICATION_20260823.jsonl`

The full report must contain the exact definitions used, proof lemmas in dependency order, all exceptional cases, witness certificates, checker invocation, finite ranges, output digest, and final terminal label.

## Validation Standard

The mathematical validation must include:

- complete enumeration of all local residue states needed by the proof, not sampling;
- symbolic verification of every transition and prime gap formula used globally;
- an obstruction proof whose modulus and coverage are explicit;
- independent witness primality checks separate from the bulk sieve;
- two implementations of at least one critical component, such as direct graph construction versus closed formulas;
- negative controls specified by the packet;
- exact agreement under cyclic relabeling and the correct equivariance statement under orientation reversal.

For any claimed extremal witness, record coordinates, all center and neighbor labels, sorted prime packets, overlap sets, primality method, and a reproducible digest.

A result that merely finds no longer chain up to a large shell fails validation.

## Evidence Policy

Proof evidence, exhaustive finite-state evidence, witness evidence, and source-comparison evidence must remain separately typed.

Every JSONL event must identify the predicate tested and the artifact containing the evidence. Events obtained after opening withheld source material must be marked comparison evidence and may not retroactively strengthen the independent-replication classification.

## Reporting Requirements

Use these report sections in order:

1. Executive Summary
2. Certified Claims
3. Reproducible Evidence
4. Failed Attempts and Null Results
5. Conjectures and Open Problems
6. Next Steps

Also include:

- `Sources Read Before Freeze`;
- `Outcome-Blindness Statement`;
- `Local-State Classification`;
- `Global Obstruction or Counterexample`;
- `Ablation Matrix`;
- `Final Classification`.

When the full report and artifacts are frozen, stop. Do not open the withheld source branch or perform source reconciliation.

## Repository Closure Protocol

Use the inherited repository closure protocol with no task-specific deviation. Closure is not complete until the full report, reducer, checker, tables, and evidence stream are promoted together and this active taskbook is archived by the responsible Driver.
