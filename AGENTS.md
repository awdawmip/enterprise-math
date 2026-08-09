# Enterprise Math agent operating rules

These are execution rules, not a research roadmap.

Before substantive mathematical or engineering research:

1. read `docs/RESEARCH_COMMON_SURFACE.en.md` (or the Chinese semantic pair);
2. read `docs/RESEARCH_SCHEDULING_PROTOCOL.en.md`;
3. read `docs/RESEARCH_OWNER_ISOLATION.en.md`;
4. read `docs/PROBLEM_STATUS.en.md` and the relevant canonical theorem/result documents;
5. read the latest relevant entries in Research Relay Issue #82;
6. inspect overlapping executable specs/tests/Lean modules before inventing a parallel tool or theorem family;
7. when the work touches foundational language, notation, formulas, theorem/tool interfaces, or a flagged contradiction, read `docs/FOUNDATION_STEWARD_PROTOCOL.en.md` and relevant entries in Foundation Problem Set Issue #164.

Scheduling rules:

- research on L1/L2/L3 is parallel by default;
- `defer`, `consume from`, `owner moved`, `audit against`, or `replay after` are routing instructions, not stop conditions;
- only a complete explicit `HARD_BLOCK` may stop a route;
- `no_new_mathematics_during_replay=true` on an owner branch constrains only the identified replay slice; only L4 integration is globally `NO NEW MATHEMATICS`;
- moving `main` does not restart research;
- L1/L2/L3 owner branches may legitimately be behind `main` and MUST NOT merge/rebase/copy the whole moving `main` merely to stay current;
- canonical promotion freezes the owner payload and uses a fresh L4 branch from then-current `main`, replaying only owner-owned assets and required registration/provenance changes;
- if an owner or integration branch acquires unrelated theorem-home files through synchronization, treat that as `SCOPE_DRIFT`: preserve the history, restore the current tree to its declared scope, and route off-owner assets back to their real owner/source;
- require one final current-main combination gate before canonical merge unless a genuine semantic conflict appears.

Knowledge propagation:

- reusable proved results and counterexamples must be relayed across affected routes with source commit, weakest assumptions, relation class, owner, and one action class: `INFORM`, `CONSUME`, `TEST`, or `HARD_DEPENDENCY`;
- canonical theorem families and reusable executable tool families must remain discoverable through the common research surface;
- do not duplicate a mother theorem merely to make a program branch self-contained;
- distinguish `CANONICAL_MAIN`, `PROVED_WIP_RELAY`, `EXECUTABLE_CHECKED`, and conjectural claims.

Foundation stewardship:

- the foundation steward maintains and verifies shared mathematical language/notation, formula integrity, theorem statements/status/interfaces, and reusable tool routing;
- mechanical or already-determined maintenance is fixed directly;
- a genuine unresolved contradiction, mathematical choice, missing hypothesis, cross-route incompatibility, high-value new structure, prior-art uncertainty, or tool/theorem sufficiency question is **not** solved by the steward;
- after minimum verification, such findings are posted to Issue #164 with a stable `FQ-*` ID for other researchers to claim;
- researchers answering an `FQ-*` item supply proof/counterexample/tool evidence and scope; the steward verifies before canonicalization.

If `hard_block = NONE`, continue the route's best available mathematical frontier rather than waiting for another branch, conversation, review, or integration replay.
