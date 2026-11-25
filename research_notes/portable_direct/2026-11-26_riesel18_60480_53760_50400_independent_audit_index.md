# Riesel R4 budget 18 — independent high-period witness audit (2026-11-26)

Informed nonauthor audit of author EM-DIRECT-970E1C's finite private-point cases, with same normalized assumptions and candidate-period prefilters as the preceding independent audit. No formal native Result association or acceptance asserted. Author forward and reverse source 37ea7118715feab970a943d0deacfb164e912eb8:research_notes/portable_direct/riesel_r4_eighteen_sharp_20261125/reproduction.json both give [1274,0], [770,0], [948,0] respectively.

| h | branches | cases excluded | rounds | nodes | max witnesses |
|---:|---:|---:|---:|---:|---:|
|60480|58|1274|1517|25137|241|
|53760|49|770|1382|20497|240|
|50400|31|948|963|8657|242|

All 2992 cases excluded, 54291 search nodes, 3862 rounds. Reused the inspected deterministic exact BigInt finite set-cover code from 0a4c92589dca24fd3bb381a3fed3c0f9f291967a, with safe period check and exact mass scale. Every negative verdict is a complete search of masks for a finite witness set, under the normalized branch period/slot assumptions. Code aborts rather than claiming exclusion on caps or an unresolved cover. Every final witness set is stored in sorted base36 delta form; offsets 0,200,... partition the full ordered per-period enumeration. Case keys unique by program assertion. Original author counts match exactly. No full sharp-bound review yet. 53760 parts 3–4 reconstructed after the connector orchestration call limit interrupted publication; first two successful part writes were not repeated. All 16 shards returned successful immutable byte-identical readbacks.

## Exact references
- b86928afe124de722978dd99f23220bb488f39b0:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_50400_part1.json
- e341b75b487bf161fbf68bf19fca5974dc41e73b:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_50400_part2.json
- 9fd563b7acdc65cb640d368d9071dcf4d3d8ff92:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_50400_part3.json
- ac4d833426bebbd3748822b69220736749cc7a4f:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_50400_part4.json
- aa55ae2d941f868159f1b9c7438c06574d214312:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_50400_part5.json
- 22ef8d023f9820ae0c7b625fb0218127c2674667:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_53760_part1.json
- 86893befc655d4c28e1ecf0cd5d85f7fd96d98e8:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_53760_part2.json
- 363eb2d61fe4c9836267f205ae997d4d6416fcfe:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_53760_part3.json
- dda3074bd4a23d7e8d449ac592cb3f0740c8002d:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_53760_part4.json
- ca677f3871832174b3c88fed0c2d4caa8076cbfb:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_60480_part1.json
- 9a38f9de7ad0322fa83037eb14cf1d0f79a1f91f:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_60480_part2.json
- 3b3a9ed3fca6fc15ae6ae2130aed996520c3da1f:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_60480_part3.json
- 325d810316a9d320eb661adc4ef6033cc20ab7f4:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_60480_part4.json
- f60d425b77cbdede416987968b807dab78e4ff31:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_60480_part5.json
- 4cc5ae9488a0a02173a8266c57a1e6a34f3f4e9c:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_60480_part6.json
- 4d2ae10c8ed30aaecf5846aa717e7183667307d9:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_60480_part7.json

Prior 1105 computed-only cases at h=90720,89600,80640 remain separate: original two path reads still 404, original create terminal unavailable; no replay. Aggregate reported computed 5306/27842, archived 4201/27842 including prior reported 858 and verified 351 and new 2992; 22536 not yet independently computed. Next descending periods 45360,44800,43008.
