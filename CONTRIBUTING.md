# Contributing to Enterprise Math

Thank you for helping test the project.

[Chinese version](CONTRIBUTING.zh-CN.md)

## Agent/project task entry

`AGENTS.md` contains entry routes. Use the public project route relevant to the current task and reuse still-valid loaded context. Account-global requirements are supplied through an authorized user's account entry; public contributors do not need access to a private knowledge repository.

| Current work | Public project entry |
|---|---|
| Project-native semantics outside FREE A | [P000](p000_reality_foundation.json) and its declared companion contracts; [Heartbeat World](definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json) for research |
| FREE before candidate freeze, including P000 | [Phase-A foundation package](definitions/EM_FREE_A_FOUNDATION_STARTUP.json) and [primitive-only substrate](definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md) |
| Formal task/control work | [Architecture and roles](docs/RESEARCH_ARCHITECTURE.md), [current control precedence](control_plane/current_control_authority.json), [runtime](docs/RESEARCH_RUNTIME_STATE_MACHINE.md), [V2 publication](docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md) |
| Research advancement and preservation | [Current research protocol](docs/PORTABLE_RESEARCH_PROTOCOL.md) |
| Research identity/activity | [Role identity](docs/RESEARCH_IDENTITY_PROTOCOL.md), [activity persistence](docs/RESEARCH_ACTIVITY_PROTOCOL.md) |
| BRC residual fitting | [Native X6 semantic alignment](research_notes/BRC_NATIVE_X6_SEMANTIC_ALIGNMENT_20261002_9D72AC.md) |
| Driver organization/continuation | [Line ownership](docs/CODEX_RESEARCH_ORCHESTRATION.en.md), [Source continuation](docs/RESEARCH_CONTINUATION_PROTOCOL.md) |
| Tool use/source operations | [Reuse protocol](docs/ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md), [GitHub/source-read protocol](docs/GITHUB_INTERACTION_BUDGET.md) |
| Unbound maintenance reporting | [Reporting scope](docs/CHATGPT_ORDINARY_CONTROL.en.md#final-interaction-gate) |

For a selected task, begin with the exact taskbook/current immutable publication and first required dependency; expand only from a concrete need. The prior-work catalog in “Start small” below is for ordinary targeted contributions; FREE Phase A uses its primitive-only route before freeze. Existing formal role, task and ownership bindings retain their canonical checks. Ordinary reporting and unshared derivation do not claim those authorities. Build/test commands and contribution operations remain in this guide and the linked project documents.

## You do not need to agree with the theory

The most valuable contribution may be a proof that a proposed rule fails.

Report a reproducible conflict with its assumptions, definitions, domain and the smallest failing derivation or implementation. An unresolved conflict remains open for review at that scope. Only a direct user instruction changes P000 as a project premise. A prediction derived from a physical model can still be tested against its stated observations and parameters. [Physical falsification contract](docs/P016_PHYSICAL_FALSIFICATION_CONTRACT.en.md)

Accepted contribution types include:

- proof;
- counterexample;
- definition refinement;
- prior-art identification;
- integer-only implementation;
- formalization;
- physical falsification proposal;
- documentation and translation.

## Start small

Before proposing a broad new theory, read:

1. `docs/SPEC_v0.1.en.md`
2. `docs/THEOREMS.en.md`
3. `docs/COUNTEREXAMPLES.en.md`
4. `docs/OPEN_PROBLEMS.en.md`
5. `docs/PRIOR_ART_AND_NOVELTY.en.md`

Choose one numbered item when possible.

## Claim status

Every substantive claim should be labeled as one of:

- `DEFINITION`
- `PROVED`
- `CONJECTURE`
- `COUNTEREXAMPLE`
- `COMPUTATIONAL`
- `PHYSICAL-HYPOTHESIS`

Do not present computational evidence as proof.

Do not present a mathematical analogy as physical evidence.

## Prior art and citation provenance

Finding earlier work is a first-class contribution.

If your change materially uses an external source:

1. verify the primary source when possible;
2. add or reuse its stable `SRC-*` entry in `sources.json`;
3. connect it to the relevant `EM-COMP-*` component in `lineage.json`;
4. classify the relationship as `ADOPT`, `EXTEND`, `REINTERPRET`, `COMBINE`, `CONTRAST`, or `INSPIRE`;
5. update the bilingual prior-art/novelty map when the new source changes the lineage or novelty boundary.

Do not claim historical priority merely because a search did not find a match.

Read `docs/CITATION_POLICY.en.md` before changing novelty language.

## Bilingual canonical documents

Issues and discussions may use either English or Chinese.

Canonical prose files must remain synchronized English/Chinese pairs. Contributors are not required to know both languages: a maintainer may supply the paired translation before merge.

A pull request that changes one canonical language file but not its pair is incomplete.

## Code rules

The v0.1 reference core is integer-only.

In `src/enterprise_math/core.py`:

- no floating-point constants;
- no true division;
- no hidden call to a floating root implementation;
- behavior must follow the written specification.

Run the relevant checks locally first. The routine GitHub workflows for quality, reference integrity, bilingual synchronization, and Lean are manual; ordinary research does not wait for them.

For a Python integration change that warrants the full local suite, use the repository runner, which includes both unittest and pytest-style tests:

```bash
python -m pip install pytest==8.4.2 sympy==1.14.0 jsonschema==4.25.1
PYTHONPATH=src python scripts/run_unittest_shard.py --index 0 --count 1
```

For a committed branch diff involving bilingual files, compare against the actual base. Set `BASE_REF` to the intended, locally available target branch or immutable base commit (for example, an up-to-date `origin/main`). The first command verifies that it resolves to a commit:

```bash
base=$(git rev-parse --verify "${BASE_REF:?Set BASE_REF to the locally available comparison base}^{commit}") &&
python tools/check_bilingual_pairs.py --base "$base"
```

The base-free bilingual command only checks structure. Run `python tools/check_references.py` for citation or lineage changes, and `lake build --wfail -KCI EnterpriseMath` for changes to the Lean proof layer. For narrower changes, run the affected test or proof directly.

## Pull requests

Prefer one conceptual change per pull request.

A good pull request explains:

- the exact claim or definition changed;
- whether it is proof, counterexample, computation, or interpretation;
- tests or proof evidence;
- nearby prior work when relevant;
- the `SRC-*` / `EM-COMP-*` lineage changes when external work is used;
- which open-problem ID it addresses.

## Credit

Preserve provenance.

When a theorem, counterexample, definition, or implementation idea originates in an issue or pull request, later canonical documentation should retain a reference to that contribution when practical.

The project does not require copyright assignment. Accepted contributions are distributed under the repository MIT License.

## Conduct

Critique claims aggressively; treat contributors respectfully.

See `CODE_OF_CONDUCT.md`.
