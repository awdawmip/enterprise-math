# Riesel R4 budget 18 independent finite-witness audit, 2026-11-26

Informed nonauthor Driver audit, original author EM-DIRECT-970E1C. Same normalized private-point branch assumptions and previously reviewed global/local digit-cost and capacity filters. Exact BigInt finite set cover; all surviving residue masks not covering the private point are enumerated on a finite witness subset, maximal masks suffice, and complete DFS with integer union bounds proves exclusion. No caps used as negative evidence. All 9 witness files were published and read back byte-identically. This is scientific evidence, not native Review or Result acceptance.

| h | branches | excluded | rounds | nodes | max witnesses |
|---:|---:|---:|---:|---:|---:|
|45360|38|962|1187|23324|249|
|44800|8|104|115|1171|87|
|43008|2|39|78|865|94|

All 1105 excluded, 25360 nodes, 1380 rounds. Author forward and reverse counts separately checked, both [962,0], [104,0], [39,0] in 37ea7118715feab970a943d0deacfb164e912eb8:research_notes/portable_direct/riesel_r4_eighteen_sharp_20261125/reproduction.json. Reused inspected previous deterministic audit kernel from 0a4c92589dca24fd3bb381a3fed3c0f9f291967a; reproduction code included, sorted base36 delta finite witness points. Shards partition offsets 0,150,...,900 for h45360. No overlap with previously computed periods.

- 332a28eec7fa5f65ee726dba861f504dc5d026b5:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_43008.json
- 9db1a7d9a3dc52810c60dc70c3c8397323c873d1:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_44800_part1.json
- c4826feeed048d47555e9402ae4e1449426a2e7f:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_45360_part1.json
- f5a2aa75cb00d06d78d0eb666f2c7c890358f0a8:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_45360_part2.json
- 581be997c8656fa179dcaa5cb44be61e8683fbf2:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_45360_part3.json
- ae930c1f6c99dfae98cfa319983986ff8bf85b8a:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_45360_part4.json
- e6d0fa879600313cf85316e85fc4574c08ad52ce:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_45360_part5.json
- 26ab97b2010e24f2cc62f44828ee0059f93b6ef1:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_45360_part6.json
- f6da7e2b74676a996b43e0c19150d348db6b1cc4:research_notes/portable_direct/2026-11-26_riesel18_independent_audit_45360_part7.json

Cumulative reported computed 6411/27842, archived 5306/27842, earlier computed-only 1105 (h90720/89600/80640; both original unknown paths still 404, original write outcome unresolved; no replay), uncomputed 21431. Next disjoint h40320/37800/35840. Full sharp bound and native admission open.
