# Parent Objective gate standalone entry point

Mode: `CONTROL_PLANE_MAINTENANCE`
Base: `91ae447e514959c70691cf97b446d60fc1a673f4`
Global-Knowledge-Sync: main@990d7c1 / GLOBAL_KNOWLEDGE_V1

Original reference step 27 failed with `No module named 'tools'`: executing the
file directly did not add the repository root to the import path. A fresh
`python -m control_plane.research_parent_objective_dispatch_gate` reached the
imports, then exposed a second entry-point omission: it read the raw publication
selector and failed on the existing `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`
fork. Installing the existing canonical bootstrap before the same audit returned
an empty error list.

The entry point now adds its repository root using the neighboring CLI pattern
and installs the existing bootstrap inside `__main__`. Importing the module does
not bootstrap the runtime. `apply_parent_objective_gate`, `install`, and `audit`
retain their original code. OPEN, PARKED and CLOSED handling, provenance,
authority validation, quarantine registries, and the workflow command are
unchanged.

The existing parent gate test gains one fresh-process regression covering the
original script command and ordinary `-m`, with inherited `PYTHONPATH` removed.
Together with the existing Objective-record and parent-closure modules,
**21 tests passed in 20.522 seconds, exit 0**. The original OPEN/PARKED/CLOSED
tests remain in that run.

Evidence is in `TEMP/em-step27-entry-3s1r_goc`: the original two failure signatures
are retained in `before-entry-comparison.json`, the unchanged audit after
canonical initialization in `canonical-before.log`, and the actual test run in
`focused-tests.log`. A subsequent reference continuation uses the immutable base
plus explicitly frozen files and is recorded separately in TEMP; it must not be
reported as a test of an already committed SHA or a complete CI run.
