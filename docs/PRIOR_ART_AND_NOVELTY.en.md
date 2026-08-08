# Prior Art, Lineage, and Provisional Novelty Map

## 1. Purpose

Enterprise Math must make it possible to reconstruct where every major idea came from.

For each important component we distinguish:

- what is established prior work;
- what definition or theorem we directly adopt;
- what we use only as a structural neighbor or contrast;
- how Enterprise Math combines or reinterprets those pieces;
- what part is a project-specific hypothesis;
- whether any novelty claim has actually been established.

The governing rule is conservative: **similarity to prior work is presumed important; historical priority is never presumed in our favor.**

Machine-readable provenance lives in `sources.json` and `lineage.json`. The stable source identifiers used below are canonical.

## 2. Relation vocabulary

We use six relation labels.

- `ADOPT` — the mathematical definition or result is reused substantially as established.
- `EXTEND` — the project adds a mathematically stronger construction while preserving the cited core.
- `REINTERPRET` — the same formal object receives a different foundational or physical interpretation.
- `COMBINE` — separately established ideas are assembled into one construction.
- `CONTRAST` — the cited work is a competing or deliberately different route.
- `INSPIRE` — the cited work motivated a direction without being logically required by the definition.

These relation labels are about intellectual lineage, not copyright.

## 3. Arithmetic lineage

### 3.1 Integer roots

The greatest-integer characterization of integer square root is established and appears in current Python documentation: the integer square root is the greatest integer \(a\) with \(a^2\le n\). [SRC-PYTHON-ISQRT]

Mathlib also already provides the general natural-number `Nat.nthRoot` formalization and proves the order characterization `a ≤ Nat.nthRoot p b ↔ a^p ≤ b` for positive exponents, together with exact recovery on perfect powers and related lemmas. [SRC-MATHLIB-NTHROOT] Enterprise Math therefore reuses `Nat.nthRoot` as its Lean primitive rather than creating a parallel formal root implementation.

Enterprise Math **adopts the inequality definition**, but changes the foundational reading. In ordinary numerical documentation the same operation may be described as flooring an exact real square root. Enterprise Math does not require that hidden real root as a primitive object.

Therefore:

- **prior work:** integer square root, general natural-number integer roots, and their formal order characterization;
- **our combination:** use the order-defined integer operation as the root primitive of the state space;
- **not our invention:** the algorithms, greatest-integer definition, `Nat.nthRoot`, or its established order-theoretic lemmas;
- **project-specific addition:** the claim that the integer result is exact in the chosen foundational semantics rather than an approximation to a more real underlying value.

### 3.2 Floor division and order adjoints

Mathlib formalizes flooring division as the greatest state \(c\) satisfying an inequality such as \(a c\le b\), and explicitly identifies it as a right adjoint in a Galois connection. [SRC-MATHLIB-FLOORDIV]

This is a strong mathematical precedent for the general Enterprise Math pattern

\[
F^\downarrow(n)=\max\{k:F(k)\le n\}.
\]

We therefore reuse the order-adjoint viewpoint instead of inventing a new name for it.

### 3.3 Scaled integers and fixed-point arithmetic

Representing values by integers plus a scale is established. NIST documented exact addition, subtraction, and multiplication after converting prescribed decimal inputs to integer representations. [SRC-NIST-INTEGER-DECIMAL] Modern block-floating/scaled-fixed-point work similarly performs substantial numerical kernels with integer arithmetic and explicit shared exponents. [SRC-KOHL-BFP]

Exact-real arithmetic has also been implemented with scaled integers whose implicit denominator is refined to provide real-number semantics. [SRC-BRIGGS-EXACT-REAL]

Enterprise Math therefore does **not** claim integer-plus-scale representation as new. The distinction is foundational:

- fixed-point, block-floating, and exact-real systems generally retain an external numerical target or accuracy semantics;
- Enterprise Math investigates whether integer state plus finite scale can be primary without an infinitely completed real value being the hidden target.

### 3.4 Exact symbolic algebra as a contrast

FLINT represents algebraic numbers exactly by integer minimal-polynomial data plus isolating intervals. [SRC-FLINT-QQBAR] Sage represents quadratic-number-field elements internally by integer triples for expressions of the form \((a+b\sqrt D)/c\). [SRC-SAGE-QUADRATIC]

These are important counterexamples to the simplistic statement that an irrational number requires storing infinitely many decimal digits. Enterprise Math accepts that lesson.

The project then asks a different question: whether exact finite symbolic representation still needs the traditional infinitely precise algebraic-real object as the underlying ontology.

## 4. Finite-information and discrete-physics lineage

### 4.1 Finite-information critiques of real-number ontology

Gisin argued that ordinary real numbers contain infinite information and proposed finite-information numbers as a physically more appropriate alternative. [SRC-GISIN-2018] Del Santo and Gisin later named the tacit assumption of fully predetermined infinite digits the `principle of infinite precision` and developed finite-information quantities as an alternative classical interpretation. [SRC-DEL-SANTO-GISIN-2019]

This is direct intellectual prior art for the Enterprise Math rejection of physically instantiated infinite precision.

Enterprise Math does not claim that critique as original. Its different step is to explore an integer-closed, scale-explicit arithmetic and collapse dynamics rather than the finite-information-number formalism used in those papers.

### 4.2 Discrete spacetime

Snyder exhibited a Lorentz-invariant discrete spacetime in 1947. [SRC-SNYDER-1947] Causal-set theory later proposed locally finite partially ordered sets as microscopic spacetime structure, with continuum spacetime appearing as an approximation in suitable regimes. [SRC-CAUSALSET-1987]

These works establish that discreteness, local finiteness, causal order, and scale-dependent continuum approximation are not new ideas.

Enterprise Math currently uses them as **physical neighbors and stress tests**, not as definitions of its arithmetic or spacetime model.

## 5. Irreversibility lineage

### 5.1 Logical irreversibility and reversible computation

Landauer analyzed logical functions without a single-valued inverse and connected logical irreversibility to physical dissipation. [SRC-LANDAUER-1961] Bennett showed that computation can instead preserve intermediate results and be made logically reversible. [SRC-BENNETT-1973]

These works are essential because they expose the exact fork in our hypothesis.

Enterprise Math is **not** claiming that ordinary information erasure was newly discovered. It tests the stronger possibility that natural state evolution itself may be many-to-one, without requiring a hidden reversible completion analogous to Bennett's saved history.

### 5.2 Projection and coarse-graining

Zwanzig derived irreversible macroscopic transport equations with memory from a projection formalism. [SRC-ZWANZIG-1961] Mori developed the related projection-operator framework for transport, collective motion, and Brownian motion. [SRC-MORI-1965]

This is a major contrast class:

\[
\text{finer dynamics}\rightarrow\text{projected macrodynamics}.
\]

Enterprise Math deliberately tests a stronger alternative:

\[
\text{fundamental state}\rightarrow\text{fundamental many-to-one state}.
\]

That stronger ontology is a hypothesis, not something established by the Mori-Zwanzig literature.

### 5.3 Preimage and folding entropy

There is an established program for quantifying non-invertibility using preimage structure. [SRC-NITECKI-PRZYTYCKI-1999] [SRC-CHENG-NEWHOUSE-2005] Ruelle connected folding-type entropy to nonequilibrium entropy production. [SRC-RUELLE-1996] Later work explicitly studies how non-invertibility contributes to entropy and relates preimage and folding entropy under stated conditions. [SRC-WU-ZHU-2021]

Enterprise Math therefore does not claim the idea “many preimages relate to entropy” as new.

Its current design choice is narrower and more foundational: begin with the integer multiplicity

\[
M_t(x)=|[x]_t|
\]

and other integer-valued observables before choosing logarithms, measures, or real-valued entropy as primitives.

### 5.4 Forward semigroups in physics

Forward dynamical semigroups are already standard in open-system quantum theory. The 1976 Gorini-Kossakowski-Sudarshan and Lindblad papers characterize important classes of completely positive quantum dynamical semigroups. [SRC-GKSL-1976] [SRC-LINDBLAD-1976]

Enterprise Math uses semigroup language only as a structural neighbor for time composition when inverse maps need not exist. It does not identify its collapse dynamics with the GKSL/Lindblad model.

## 6. What Enterprise Math actually combines

The current synthesis has five layers.

1. **Order-defined integer operations** — integer roots and flooring-style adjoints are treated as exact state maps, not approximations to hidden continuous answers. [SRC-PYTHON-ISQRT] [SRC-MATHLIB-NTHROOT] [SRC-MATHLIB-FLOORDIV]
2. **Explicit finite scale** — integer-plus-scale engineering precedents are retained, while infinite real completion is not assumed to be physically primitive. [SRC-NIST-INTEGER-DECIMAL] [SRC-KOHL-BFP] [SRC-GISIN-2018] [SRC-DEL-SANTO-GISIN-2019]
3. **Collapse as an algebraic operator** — \(C_p(n)=R_p(n)^p\) is studied with the language of monotone/idempotent order projections. [SRC-MATHLIB-CLOSURE]
4. **Fundamental many-to-one dynamics as a hypothesis** — this is explicitly separated from reversible-computation and coarse-graining explanations. [SRC-BENNETT-1973] [SRC-ZWANZIG-1961] [SRC-MORI-1965]
5. **Preimage degeneracy before logarithmic entropy** — established preimage/folding-entropy work is used as the mathematical neighborhood, while the primitive observable is kept integer-valued first. [SRC-CHENG-NEWHOUSE-2005] [SRC-WU-ZHU-2021]

The novelty candidate is therefore **the integrated foundational package and its consequences**, not the isolated ingredients.

## 7. Provisional innovation claims

The repository currently allows the following wording.

### 7.1 Project synthesis

**EM-NOV-001.** We propose an integer-first semantics in which integer roots are exact primitive operations rather than rounded views of hidden real roots.

**EM-NOV-002.** We combine explicit scale with integer state semantics while refusing to require an infinitely precise real completion as the hidden physical value.

**EM-NOV-003.** We study perfect-power collapse operators simultaneously as order-theoretic projections and as candidates for intrinsically many-to-one natural transitions.

**EM-NOV-004.** We study integer preimage multiplicity and related integer observables before elevating logarithmic entropy to a primitive.

### 7.2 Physical hypothesis

**EM-NOV-005.** We test whether fundamental dynamics can be genuinely many-to-one rather than merely appearing irreversible after coarse-graining or information erasure.

This is a physical hypothesis, not an established result.

### 7.3 Historical novelty status

**The overall historical novelty of Enterprise Math is currently `NOVELTY_UNVERIFIED`.**

We have not performed an exhaustive-enough literature search to claim that no earlier author assembled an equivalent framework. Until that burden is met, use phrases such as:

- “we define”;
- “we propose”;
- “we combine”;
- “we investigate”;
- “we are not aware of an equivalent synthesis after the searches recorded so far”.

Do not write “first”, “unprecedented”, or “never proposed before” without a dedicated evidence review.

## 8. What we must never misattribute

Do not attribute the following to Enterprise Math as inventions:

- integer square root or general natural-number integer roots;
- Euclidean/floor division;
- Galois adjoints;
- closure/interior operators;
- fixed-point or scaled-integer arithmetic;
- finite symbolic representation of algebraic numbers;
- critiques of infinite-precision physical real numbers;
- discrete spacetime or causal sets;
- logical irreversibility or reversible computation;
- Mori-Zwanzig projection/coarse-graining;
- dynamical semigroups;
- preimage entropy or folding entropy.

Our responsibility is to cite those lines clearly and state exactly where our use changes.

## 9. Update rule

This document is living project infrastructure.

Whenever a new external source materially affects a definition, proof strategy, terminology choice, physical comparison, or novelty boundary:

1. add a stable `SRC-*` record to `sources.json`;
2. connect it to one or more `EM-COMP-*` records in `lineage.json`;
3. update this English/Chinese document pair if the source changes the human-readable lineage or novelty boundary;
4. update canonical technical documents that rely on the source;
5. keep the claim no stronger than the evidence;
6. preserve older provenance rather than deleting inconvenient prior art.

`tools/check_references.py` and the reference-integrity workflow enforce the machine-checkable part of this rule.
