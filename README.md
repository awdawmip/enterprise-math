# Enterprise Math

Enterprise Math is an early-stage mathematical research program built around finite resolution, integer-closed operations, and intrinsically irreversible state collapse.

[Chinese version](README.zh-CN.md)

## Core idea

The project does **not** start from a hidden real continuum and then approximate it with integers. It starts from integer states themselves.

At the current stage, the working direction is:

1. Integers are primitive numerical states.
2. Resolution and scale are explicit parts of a numerical description.
3. An operation should return a valid state of the same discrete system instead of manufacturing a hidden fractional or irrational value.
4. Integer square root is treated as an exact operation in the system:

   \[
   R_2(n)=\max\{k\in\mathbb N:k^2\le n\}.
   \]

   Therefore, inside this system,

   \[
   R_2(2)=1,\qquad R_2(200)=14,\qquad R_2(20000)=141.
   \]

5. The associated square-collapse operator is

   \[
   C_2(n)=R_2(n)^2.
   \]

   Hence

   \[
   20000\rightarrow19881.
   \]

   In fact, every state from 19881 through 20163 collapses to 19881 under \(C_2\).
6. The missing difference is not assumed to survive as a hidden remainder. The transition itself is many-to-one.
7. Time, irreversibility, and entropy are therefore investigated from the forward composition and preimage structure of non-invertible maps, rather than from a presumed reversible microscopic substrate.

## What this project is not

Enterprise Math is not currently presented as an established physical theory. It is a research program for constructing definitions, proving consequences, finding contradictions, comparing with prior mathematics, and testing whether a coherent discrete foundation can be built without silently restoring the real continuum.

Classical real analysis, exact algebraic arithmetic, floating-point arithmetic, coarse-graining, and reversible microscopic dynamics remain important comparison frameworks. They are not assumed as the ontology of this project.

## Repository structure

- `docs/FOUNDATIONS.en.md` — current definitions and axioms under test.
- `docs/ORIGIN.en.md` — distilled origin of the research direction and key corrections.
- `docs/ROADMAP.en.md` — proof, counterexample, implementation, and physics-comparison roadmap.
- `docs/REFERENCES.en.md` — neighboring prior work and terminology.
- `docs/BILINGUAL_POLICY.en.md` — mandatory Chinese/English synchronization rule.

Every formal prose document has a pure-English and a pure-Chinese counterpart. Neither language is secondary; the semantic pair is canonical.

## Current research questions

- Which arithmetic operations can be defined as exact integer-closed maps?
- How should scale composition work without reintroducing decimals as hidden primitives?
- Which classical algebraic identities survive, weaken, or fail?
- Which collapse operators are monotone, idempotent, order-adjoint, or composable?
- Can a purely forward many-to-one dynamics produce a natural monotone measure of historical merging?
- How should geometry be rebuilt when Euclidean distance is no longer assumed to take values in a complete real continuum?
- Can thermodynamic time and entropy be connected to collapse multiplicity without assuming hidden erased information?

## Research discipline

New claims should be separated into definitions, proved theorems, computational observations, conjectures, and physical interpretations. Nearby established mathematics should be searched before new terminology is frozen. A resemblance to prior work is evidence of a useful connection, not proof of the project's physical interpretation.
