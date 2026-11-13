# R42 complete 298-interval integration evidence

2026-11-10. The portable R42 suffix selector was substituted into the existing R41 compiler and run on the frozen S23/AV input. Both R42-recurrence and forced R40-endpoint source preparation produced the same complete 298 affine-risk TSV bytes as R32 reference.

Run: python VERIFY_R42_INTEGRATION.py

Dependencies: R41's frozen local bundle copies src/VERIFY_R32.py, src/VERIFY_R33.py, src/VERIFY_R36.py and src/AFFINE_RUNS_R32.tsv placed in src/ adjacent to this script. The R42 branch also contains VERIFY_R42.py and REFERENCE_R41.py.

Actual output:
R42_FULL_298 RECURRENCE 3 initial stages 298 runs (-4017401528447, 15321634290944) 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6 source scan 259
R42_FULL_298 ENDPOINT_ONLY 3 initial stages 298 runs (-4017401528447, 15321634290944) 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6 source scan 0
PASS_R42_298_AFFINE_RUNS_WITH_RECURRENCE_AND_R40_FORCED_ENDPOINT

Both routes evaluated 3 initial Farey stages, 4 initial increment blocks, 78 total stages, 28 quotient-jump decisions and 148 long positive blocks; all 298 final affine runs matched the pinned R32 reference byte-for-byte. Endpoint-only is independent for source preparation but shares the downstream frozen compiler. Independent mathematical review remains a separate step.

This addendum supersedes the earlier pending-integration text in PROOF.md §6. Next R43 addresses consecutive-J streaming and enclosure refinement.
