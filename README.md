# Enterprise Math

Enterprise Math is an open research program for finite-resolution, integer-first mathematics and intrinsically forward state evolution.

[Chinese version](README.zh-CN.md)

## The one-minute idea

The project does **not** begin with a hidden real continuum and then approximate it with integers. It asks what mathematics emerges if integer states and explicit scale are primitive.

For the v0.1 core,

\[
R_p(n)=\max\{k\in\mathbb N:k^p\le n\}
\]

is an exact integer root operation. Therefore,

\[
R_2(2)=1,\qquad R_2(200)=14,\qquad R_2(20000)=141.
\]

The associated collapse operator is

\[
C_p(n)=R_p(n)^p.
\]

Hence

\[
C_2(20000)=19881.
\]

Every integer from 19881 through 20163 has the same square-collapse image 19881. The missing difference is not assumed to survive as a hidden remainder in the ontology being investigated.

## What is actually claimed

Enterprise Math currently makes three different kinds of statements, and they must not be confused:

1. **Definitions** — chosen mathematical rules such as integer root and collapse.
2. **Mathematical results** — consequences proved from those definitions.
3. **Physical hypotheses** — stronger proposals about finite resolution, irreversibility, time, and entropy that remain open to external evidence.

The repository is designed so that a mathematical result can remain useful even if a physical interpretation later fails.

## Research Beta v0.1

The current beta freezes a deliberately small core:

- natural-number states;
- integer \(p\)-th root;
- perfect-power collapse;
- discrete scale refinement and projection;
- forward composition of many-to-one maps;
- integer preimage multiplicity as a first irreversibility observable.

The beta does **not** yet freeze a complete geometry, calculus, physics, or thermodynamics.

Read:

- [v0.1 specification](docs/SPEC_v0.1.en.md)
- [proved propositions](docs/THEOREMS.en.md)
- [counterexamples](docs/COUNTEREXAMPLES.en.md)
- [open problems](docs/OPEN_PROBLEMS.en.md)
- [roadmap](docs/ROADMAP.en.md)
- [prior work](docs/REFERENCES.en.md)

## Start contributing in five minutes

You do not need to accept the project's physical interpretation.

Useful contributions include:

- prove one numbered conjecture;
- break one proposed identity with a counterexample;
- sharpen a definition;
- connect a construction to prior mathematics;
- expand the integer-only reference implementation;
- formalize a stable statement in Lean;
- translate a canonical document pair;
- propose an experiment that could falsify a physical hypothesis.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Reference implementation

The repository includes a deliberately small Python reference model under `src/enterprise_math/`.

Its rules are strict:

- no floating-point constants;
- no true division;
- integer inputs and outputs only in the core;
- tests exhaustively check small finite domains for the v0.1 invariants.

Run:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The implementation is an executable specification and counterexample finder, not a substitute for proof.

## Bilingual rule

Every canonical prose document is maintained as a pure-English / pure-Chinese semantic pair. Neither language is secondary. Canonical prose changes must update both versions in the same change set.

See [bilingual policy](docs/BILINGUAL_POLICY.en.md).

## License

Code and repository documentation are released under the MIT License. The root `LICENSE` file is the sole legal license text.

See [licensing note](docs/LICENSING.en.md).

## Status

This is an early research project. Claims are intentionally exposed to proof, counterexample, prior-art comparison, formalization, and physical falsification.

The fastest way to help is not to agree with the project. It is to find exactly where it is right, wrong, incomplete, or already known.
