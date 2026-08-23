# Prime Fusion — Blind Independent Replication Packet

Status: `DRAFT REPLICATION INPUT / PENDING DRIVER INTAKE / NOT DISPATCHABLE TASKBOOK`
Date: `2026-08-23`
Origin: direct user request to begin theorem packaging plus independent replication after a free-research discovery run.
Hard target: `PRIME_FUSION_CORE_INDEPENDENTLY_RECONSTRUCTED_OR_REFUTED`

## 1. Independence boundary

This packet is designed for a **new, context-clean researcher conversation**. The current conversation that produced the source discovery is not independent evidence and must not execute this packet as the replicator.

A receiving researcher may claim `BLINDNESS_STATUS=CLEAN` only if, before beginning the derivation, it has not read or been told the theorem-package results, formulas, checker outputs, journal summaries, or current conversation conclusions.

Before freezing its return, the replicator MUST NOT read:

- branch `research/prime-fusion-theorem-package`;
- any file whose name contains `PRIME_FUSION_THEOREM_PACKAGE`;
- GLOBAL_KNOWLEDGE journal entries authored by `EM-FREE-P7K4N2` about prime-plane / prime-fusion research;
- commit messages, PR descriptions, issues, search results, or external notes that reveal the source run's formulas or theorem list;
- external literature chosen because it matches a suspected answer.

Do not use repository code search for `prime fusion`, `dual-prime`, `phase lock`, `cyclotomic corridor`, or similar source-run vocabulary before return freeze.

After the independent return is frozen, a Driver may open the withheld theorem package for comparison.

## 2. Frozen source substrate

Use only the following source snapshot for the mathematical substrate:

`SOURCE_SNAPSHOT_REF = 88d86e2146c01cbe7a62432e9488b2b4621ec9fa`

Spatial primitive definition:

`definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`

The replication concerns a single native sector `S_12` with positive integer cell coordinates `(a,b)`; do not infer unprovided cross-sector seam rules.

Define two integer readouts on an interior cell:

`A(a,b) = a^2+b^2`,

`B(a,b) = a^2-ab+b^2`.

The first is the current sector-local native squared-length readout. The second is a classical carrier-side quadratic readout supplied here explicitly as part of the replication object. Do not assume any further relationship between them.

A cell is called **simultaneously prime** when both readouts are ordinary prime integers.

## 3. Permitted background

Before return freeze, the replicator may use:

- elementary integer algebra;
- gcd/divisibility;
- modular arithmetic and finite fields;
- elementary quadratic-residue facts and quadratic reciprocity if independently triggered;
- polynomial algebra and the Chinese remainder theorem if independently triggered;
- deterministic finite computation written by the replicator.

Do not import any current Enterprise Math prime theorem/tool package merely because it exists.

## 4. Required independent classifications

The replicator must attack the following questions from the supplied object itself. No answer is implied by the wording.

### R1 — Exact relation and recoverability

Classify all exact identities between `(a,b)` and the pair `(A,B)` that are relevant to:

- common divisors;
- loss of information under the map `(a,b)->(A,B)`;
- recovery of unordered or ordered coordinates from the two readouts, if possible.

State necessary and sufficient conditions wherever possible.

### R2 — Unified finite carrier question

Determine whether the pair of readouts admits a natural single finite algebraic carrier or quotient attached to a primitive cell.

If yes:

- construct it without importing the withheld source result;
- identify what data are preserved or lost by scalarizing it;
- determine the minimum additional finite marking needed for reconstruction, if any.

If no such natural construction survives scrutiny, prove the obstruction.

### R3 — Local prime obstructions

For a prime modulus `l`, classify the residue classes/directions on which either readout vanishes.

Determine:

- which prime congruence classes can divide each channel of a primitive cell;
- whether a natural combined modulus or splitting pattern emerges;
- exact root counts for the one-parameter slice `(a,b)=(t+k,t)`.

Do not assume an answer involving any particular modulus.

### R4 — Simultaneous-prime residue relations

For cells for which both readouts are primes greater than the small ramified cases, derive every forced congruence or reciprocity relation between the two primes that can be proved elementarily.

Separate exact theorem from heuristic/statistical observation.

### R5 — Sector-local adjacency

Using only the carrier-neighbor steps visible inside one `S_12` chart, classify the induced nearest-neighbor graph of simultaneously-prime cells.

Determine whether connected components have a uniform finite bound. If a bound exists, prove it and handle finite small-prime exceptions explicitly.

Do not make a global three-sector seam claim without an explicit current chart-transition definition.

### R6 — Finite dimensional reduction

Investigate whether averaging exact finite modular survivor data over one family of one-dimensional slices recovers the full two-dimensional modular survivor data.

If a precise finite identity exists, prove it. Do not promote it into an asymptotic prime theorem.

## 5. Mandatory negative tests

Actively search for counterexamples to every proposed structural theorem. At minimum test:

- non-primitive cells;
- axis/boundary degeneracies;
- small primes `2` and `3`;
- coordinate swap `(a,b)<->(b,a)`;
- different primitive cells with the same scalar product `A*B`;
- any claimed global-neighbor statement at sector seams.

## 6. Executable evidence

Write an independently authored deterministic checker using exact integer arithmetic only.

The checker must not copy code from the withheld theorem branch.

It should test at least:

- all positive coordinate pairs in a nontrivial box;
- modular classifications over multiple primes in every surviving congruence class;
- any proposed finite quotient/reconstruction mechanism;
- adjacency classification;
- counterexample/degeneracy handling.

Finite tests are audit evidence and do not replace general proofs.

## 7. Return format

Freeze one return before any comparison with the source theorem package.

Recommended return path on the replicator's own owner branch:

`research_returns/PRIME_FUSION_INDEPENDENT_REPLICATION_RETURN_20260823.md`

Required sections:

1. `BLINDNESS_STATUS` and exact files read;
2. independently derived definitions;
3. theorem statements with proofs;
4. failed conjectures/counterexamples;
5. executable checker path and finite ranges;
6. unresolved claims;
7. final classification:
   - `FULL_STRUCTURAL_REPLICATION`,
   - `PARTIAL_REPLICATION`,
   - `MATERIAL_COUNTEREXAMPLE`, or
   - `NO_RECONSTRUCTION`.

The return must not self-compare against the withheld source package. Comparison is a later Driver function.

## 8. Governance status

This is an input packet, not an approved research taskbook and not a dispatch envelope.

A Driver must perform current taskbook/intake review before converting it into an official dispatch. Runtime Researcher-ID is intentionally absent.
