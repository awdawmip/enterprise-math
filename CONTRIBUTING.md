# Contributing to Enterprise Math

Thank you for helping test the project.

[Chinese version](CONTRIBUTING.zh-CN.md)

## You do not need to agree with the theory

The most valuable contribution may be a proof that a proposed rule fails.

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

Run:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
python tools/check_bilingual_pairs.py
```

## Pull requests

Prefer one conceptual change per pull request.

A good pull request explains:

- the exact claim or definition changed;
- whether it is proof, counterexample, computation, or interpretation;
- tests or proof evidence;
- nearby prior work when relevant;
- which open-problem ID it addresses.

## Credit

Preserve provenance.

When a theorem, counterexample, definition, or implementation idea originates in an issue or pull request, later canonical documentation should retain a reference to that contribution when practical.

The project does not require copyright assignment. Accepted contributions are distributed under the repository MIT License.

## Conduct

Critique claims aggressively; treat contributors respectfully.

See `CODE_OF_CONDUCT.md`.
