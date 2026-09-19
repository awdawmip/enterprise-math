# Heartbeat World: residue-guarded BRC research

Status: executable research candidate, not Foundation or production.

Read `research/RESIDUE_RESEARCH_NOTE.md` for the exact laws and boundaries.
Run in this directory:

```sh
python tests/verify_residue_gates.py
```

In an Enterprise Math checkout the test uses the existing `src/enterprise_math`
modules and the earlier `heartbeat_world_algebra_20260919_AD0416/research`
helpers. In the standalone bundle it uses the byte-identical `vendor/` and
`research/` copies. Its small prime-valuation dependency is the explicitly
labeled excerpt carried from the previous bundle, not a full holonomy module.

New code:
- `research/brc_residue_transport.py`: ResidueControl, GuardedKernel,
  GuardedMoments; matched control/time ports and exact conditional moments.
- `research/heartbeat_residue_gates.py`: local dyadic gates, ordered/shuffled
  sweeps, and actual material heartbeat-plus-gate examples.
- `tests/verify_residue_gates.py`: 14 exact check groups and independent
  finite path enumeration, with fixed random seed.

Checkpoint `files_sha256` uses standalone-package relative names. In this
repository `CHECKPOINT.json` is the same content as bundle
`RESIDUE_CHECKPOINT.json`; bundle `METHOD_ADDENDUM.json` is published at
`research_method_inventory_addenda/20260920_heartbeat_residue_transport.json`.
All other listed paths are relative to this research directory.

World coordinates, P000, final Cell codecs and production Nollm are unchanged.
The finite-control moment lease is not occupancy/full-provenance recovery,
arbitrary scale-switching closure, constant bit memory, or a physical law.
