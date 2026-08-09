# Enterprise Math agent operating rules

These are execution rules, not a research roadmap.

Before substantive mathematical or engineering research:

1. read `docs/RESEARCH_COMMON_SURFACE.en.md` (or the Chinese semantic pair);
2. read `docs/RESEARCH_SCHEDULING_PROTOCOL.en.md`;
3. read `docs/PROBLEM_STATUS.en.md` and the relevant canonical theorem/result documents;
4. read the latest relevant entries in Research Relay Issue #82;
5. inspect overlapping executable specs/tests/Lean modules before inventing a parallel tool or theorem family.

Scheduling rules:

- research on L1/L2/L3 is parallel by default;
- `defer`, `consume from`, `owner moved`, `audit against`, or `replay after` are routing instructions, not stop conditions;
- only a complete explicit `HARD_BLOCK` may stop a route;
- `no_new_mathematics_during_replay=true` on an owner branch constrains only the identified replay slice; only L4 integration is globally `NO NEW MATHEMATICS`;
- moving `main` does not restart research; require one final current-main combination gate before canonical merge unless a genuine semantic conflict appears.

Knowledge propagation:

- reusable proved results and counterexamples must be relayed across affected routes with source commit, weakest assumptions, relation class, owner, and one action class: `INFORM`, `CONSUME`, `TEST`, or `HARD_DEPENDENCY`;
- canonical theorem families and reusable executable tool families must remain discoverable through the common research surface;
- do not duplicate a mother theorem merely to make a program branch self-contained;
- distinguish `CANONICAL_MAIN`, `PROVED_WIP_RELAY`, `EXECUTABLE_CHECKED`, and conjectural claims.

If `hard_block = NONE`, continue the route's best available mathematical frontier rather than waiting for another branch, conversation, review, or integration replay.