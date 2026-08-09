# Change type

- [ ] Definition
- [ ] Proof
- [ ] Counterexample
- [ ] Computation
- [ ] Formalization
- [ ] Prior art
- [ ] Physical hypothesis
- [ ] Documentation

## Exact change

Describe the smallest claim, definition, or implementation change in this pull request.

## Evidence

Provide proof, counterexample, test output, or primary-source references as appropriate.

## Claim status

State the status before and after this change.

## Shared theorem/tool surface

For a canonical promotion, state the shared-surface delta for reusable theorems, formalizations, executable families, negative boundaries, or active interface alerts.

- [ ] `docs/RESEARCH_COMMON_SURFACE.*` and `research_common_surface.json` are updated where the promoted result/tool is reusable, **or** the PR explains why the shared-surface delta is `N/A`.
- [ ] Any change to root imports in `EnterpriseMath.lean` is mirrored in the exact root-Lean indexes in the human/machine shared surface.
- [ ] Any added/removed `tools/*.py` file is mirrored in the exact repository-tool indexes in the human/machine shared surface.

## Bilingual parity

- [ ] Every changed canonical prose file has its paired language version changed in the same pull request.
- [ ] The two versions make the same material claims.

## Validation

List commands or checks run, including `python tools/check_research_common_surface.py` when the shared surface, root Lean imports, or repository tools change.
