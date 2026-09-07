# Shared tool ownership repair

Date: 2026-09-07. Status: `REPAIR_COMPLETE / CHECKS_PASS / SOURCE_NOT_PUBLISHED_BY_HELPER`. Classification: `NO_NEW_MATHEMATICS_CONTROL_PLANE_ONLY`.
Role: owner-directed ANCHOR_EXPOSED internal helper; no official research/review identity.

## Reproduced defect and exact scope

At control checkout HEAD `d49ffdb0441b374a2b6ae10900ad31c8bca7dfd0`, canonical bootstrap followed by `tools.check_research_common_surface.check()` failed with:

```text
registered shared paths do not exist: ['tools/research_scheduler.py']
```

`research_common_surface.json` still assigned this deleted legacy module to Common Surface. Both human Common Surface indexes had instead listed `tools/research_runtime_reducer.py` in that position, but `research_runtime_state_machine.json` already owns the reducer. Replacing the stale JSON path with the reducer would create duplicate Common/Runtime ownership.

The existing checker requires all actual `tools/*.py` files to be the exact pairwise-disjoint union of Common Surface, Toolbox and Runtime indexes. Current control authority separately names `research_control_dispatch.py` as the recovery-aware live entrypoint, `tools/research_dispatch.py` as the fresh task selector, and `tools/research_runtime_reducer.py` as the event reducer. Registration of internal files is not a change to those public entrypoints.

The authorized repair removes the stale scheduler registration and synchronizes the bilingual Common Surface lists with their actual Common ownership. Both documents explicitly point to the existing Runtime and Toolbox owner indexes. The Toolbox document's shared-ownership paragraph is also corrected from two surfaces to three; its two owned tools and all mathematical-family sections are preserved.

## Further exact-coverage findings

After the stale path was removed, the same checker exposed three previously unindexed files:

- `tools/check_exact_arithmetic_policy.py`: a static checker for explicitly supplied changed research-calculation files; it grants no mathematical status. It is registered with the other Common Surface policy/checking tools and listed in both Common Surface documents.
- `tools/research_dispatch_core.py`: the existing implementation behind the current dispatch facade. It belongs with Runtime implementation files and is not a replacement live entrypoint.
- `tools/research_driver_queue.py`: the existing read-only queue over immutable Result/review/follow-up state. It creates no CLAIM, review, publication or mathematical authority; it belongs to Runtime.

The Toolbox JSON's `common_surface_bridge.ownership_rule` also retained the older two-surface description. That description was corrected to the existing three-surface partition; the Toolbox's two owned paths and all mathematical-family data remain unchanged.

At the intermediate checkpoint, actual tool count was 22; Common owned 7, Toolbox 2 and Runtime 11, with zero duplicates or stale paths but two unindexed Runtime files. The initial scope expressly excluded Runtime-index changes. After root authorized the precise expansion, the two existing files were added only to `research_runtime_state_machine.json`'s ownership index and the Runtime document's discovery list. Live entrypoints, selectors, invariants, execution logic and admission conditions were not changed. Final ownership is **7 Common + 2 Toolbox + 13 Runtime = 22 actual tools**, with no missing, stale or duplicate ownership.

## Final validation and preservation

The intermediate Common Surface unit test correctly failed at the newly exposed exact-coverage gap; that failure is preserved here rather than described as a passing check. After the authorized registration repair, all required checks passed:

```text
research common surface: OK (19 Lean root imports, 22 repo tools [7 common + 2 toolbox + 13 runtime], 2 active foundation questions, 0 active FQ canonical-dispatch links)
test_research_common_surface.py: 1 test, OK
PASS: 65 sources and 30 lineage components across 12 source registry file(s) and 18 lineage registry file(s).
PASS: 124 bilingual document pairs are synchronized structurally.
```

Commands: canonical bootstrap followed by `tools.check_research_common_surface.check()`; `python -m unittest discover -s tests -p test_research_common_surface.py -v`; `python tools/check_references.py`; `python tools/check_bilingual_pairs.py`. `git diff --check` also passed. The existing regression was reused; no checker or test criterion was modified.

Against exact baseline `d49ffdb0441b374a2b6ae10900ad31c8bca7dfd0`, structural comparisons established that the only JSON changes are the Common tool-list removal/addition, the two Runtime ownership-list additions, and the Toolbox ownership-description string. A separate byte comparison reconstructed each final JSON using only these exact byte substitutions in the baseline: all three reconstructed files equalled their final bytes, proving non-target bytes identical. All seven existing files retain their original trailing-newline state, including no EOF newline for the Toolbox JSON and both Common Surface documents. The seven tracked files have a total diff of 16 inserted and 8 deleted lines; the only additional owned file is this repair note.

No legacy module, source implementation, checker, task publication, taskbook, theorem status, claim event or remote ref was changed. The untracked `OWNER_X6_TASKBOOK_REPAIR_PROPOSAL_20260907.md` and its corresponding audit belong to separate owner work and were left untouched. No commit or push was performed by this helper.

## Frozen file hashes

SHA-256 for the seven repaired registration/document files:

| Path | SHA-256 |
| --- | --- |
| research_common_surface.json | 3a2e9da23c98ab0e7daf7292bc8da8a78bcb237221dbf01d40ad377454e7f74e |
| research_runtime_state_machine.json | 6352597a5838d54191f23333d5872524cb676be830d59fdb872c43fcbeb71748 |
| enterprise_toolbox_registry.json | d8a0a7e6e2090def201175d9f42da1b1c2a56e80fe5a5220ab5c6c8e12da10e6 |
| docs/RESEARCH_COMMON_SURFACE.en.md | c27a61db61b3a759e235ff65e422ec6d96069e9dab1da8809de278eb7f97e7c8 |
| docs/RESEARCH_COMMON_SURFACE.zh-CN.md | b8e1301321235b233dec83583aed341e95d10d47cbb5f530847e4eabe03d3a96 |
| docs/ENTERPRISE_TOOLBOX_REGISTRY.md | 1a94e1728586d6a0add42bbb5fb9788281f0c057b132c93cfe5b174fde8c15e9 |
| docs/RESEARCH_RUNTIME_STATE_MACHINE.md | f5f38e8e23ffd1acf93c5908049c599b108bc148645d797d4a0a5d25dad7fc7a |

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
