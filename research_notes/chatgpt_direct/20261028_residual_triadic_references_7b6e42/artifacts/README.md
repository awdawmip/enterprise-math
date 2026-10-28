# Triadic dynamic references — reproducible research packet

This packet implements one logical object with a bounded, closed table of references using only the pinned `reserve`/`release` matching kernel during production execution. The published mathematical contract is in `RESULT.md`. It is a sequential macro-boundary refinement, not an intrinsic physical-birth-preserving observer or a calibrated cell/force model.

## Run

Use Python 3.11+ and the standard library. No network access is needed.

```sh
python check_triadic_refs.py smoke --out smoke-recheck.json
python check_triadic_refs.py audit --slots 2 --out audit-r2-recheck.json
python check_triadic_refs.py cycle --rounds 1000 --out cycle-recheck.json
python check_triadic_refs.py histories --depth 5 --out histories-recheck.json
python check_triadic_refs.py faults --out faults-recheck.json
python check_more.py partitions partitions-recheck.json
python check_more.py intrinsic_identity intrinsic-recheck.json
```

The three-slot full domain is covered by two runs with `--slots 3 --start 0 --stop 313` and `--slots 3 --start 313 --stop 625`. The four-slot quotient is covered with `--slots 4 --canonical --start 0 --stop 102` and `--slots 4 --canonical --start 102 --stop 203`.

`PROGRAMS.json` contains every fixed command for 1/2/4/6 slots, the declared event library, and address layout. Production words do not use the test-only `decode`, `expected`, or the parent's runtime name table. `SUMMARY.json` distinguishes uncached physical-kernel calls from repeated uses and the separately executed logical oracle.

`parent/` contains unchanged inherited implementation files and their original source pins. Parent test mains are not run on import. Some inherited modules verify their pinned code at the input boundary. The new implementation does not modify these kernels.

Primary results are twelve different completed test modes, not two full independent repetitions. The clean extraction checks are supplementary and excluded from the primary assertion total. `PUBLICATION.json` identifies the exact source-report and journal readbacks; the remote reports are compact versions, not copies of this full runtime tree.
