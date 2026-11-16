# X6 Unit64 — 最小三切片相容图册、整数 holonomy 与无损恢复

Date 2026-11-16 Asia/Hong_Kong. Parent TASK_RESEARCH `RS-X6-LEGACY-PLANE-RECONCILIATION` / publication `TP2-B4A441B23DA3159232C2`; research conversation `chatgpt-research-onhour-enterprise-math-20260923`; Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`. Science pins: signed X6 P000 V5 `59538f585d037d09ef687b28715c4bc1a3f9fe03`, historical `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Classification: **AUTHOR-EXACT / FINITE EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Scope and relation to established theorem

Previously verified `research_notes/X6_20_SLICE_INVERSE_LIMIT_RECONSTRUCTION_V10_20260905.md` (current blob `d956ad7eb2f181557242dca30d483c4b60952596`; original frozen blob `35e98cee4268cff11284c44020baec9e68139f8b`) proves that all 20 compatible three-axis min-zero local observations recover the **relative** quotient `G6_D = Z^6 / Z(1,1,1,1,1,1)`, and exhibits a sufficient family of **four** local charts. This unit proves **three is the exact minimum**, classifies all full-covering three-chart families, and derives the missing integral cycle-gluing obstruction. The triples are derived observations of a six-dimensional native Cell, not primitive two-dimensional planes or a replacement for the four specifically realized FCC carrier charts.

## Theorem A: integer graph-potential gluing

Fix a set of local 3-subsets `S_a` of the six **named** axes. On each triple supply `r_a in Z^3/Z(1,1,1)`, represented by its unique nonnegative min-zero triple. Every observed ordered pair `(i,j) in S_a` supplies `d^a_ij = r_a(i)-r_a(j)`. Let `Gamma` have all six vertices and the union of the observed pairs as edges.

There exists a global signed six-axis raw displacement `z in Z^6` whose restrictions have all prescribed classes **iff** (i) every repeated pair has equal declared `d_ij`, and (ii) every oriented cycle of `Gamma` has zero sum of `d_ij` along its edges. When `Gamma` is connected the resulting global relative class `[z] in G6_D` is unique. If `Gamma` has `c` components the remaining relative choice is a free `Z^(c-1)` family of intercomponent offsets.

**Proof:** Necessity telescopes `d_ij=z_i-z_j`. Conversely choose one root per component and integrate edge differences along a path; the cycle condition makes the integer potential path independent, reconstructing each local chart up to a scalar diagonal offset. Two solutions differ by a constant on each component. This proves the result for all integer chart values, with no numerical approximation.

This exact relative reconstruction still forgets one native diagonal `h` when connected. The native raw chart lift is `z=can6(z)+h(1,...,1)`, `h=min_i z_i`. Native public address codec and ordered BRC path provenance remain distinct additional types.

## Theorem B: exact minimum and complete 3-chart family classification

Two triples fail as a complete connected relative atlas over all six axes: if their union covers all six, they are disjoint and disconnected; if they overlap, at least one axis is uncovered. Three suffice, e.g.
`S1={1,2,3}, S2={1,2,4}, S3={3,5,6}`;
their graph is connected and the single repeated edge `{1,2}` must have matching integer differences.

Among all `C(20,3)=1140` unordered distinct three-triple families, exactly **480** cover all six axes. Every full-covering family has connected observed-pair graph. Exhaustive classification:

| Sorted pairwise intersection sizes | Triple intersection size | Number of full covers | Additional compatibility |
|---|---:|---:|---|
| `(0,1,2)` | 0 | **180** | equality of repeated two-axis pair difference |
| `(1,1,2)` | 1 | **180** | equality of repeated two-axis pair difference |
| `(1,1,1)` | 0 | **120** | one nontrivial integral cycle-holonomy equation |

This follows from inclusion/exclusion `6=9-(|A∩B|+|B∩C|+|C∩A|)+|A∩B∩C|` together with distinctness. A separate complete enumeration of all 1140 candidates gives the counts 180+180+120=480 with zero omissions. Therefore **three** is the minimal local-chart count for the relative `G6_D` observer. This does not supersede the already-proved sufficient four-chart specific FCC cover.

## Theorem C: the one-cycle integer obstruction and exact repair metric

In a full cover of the third class the three pairwise intersections are **different singleton axes**: denote `a=A∩B`, `b=B∩C`, `c=C∩A`. Define the chart-gauge invariant integer residue

`H = [r_A(c)-r_A(a)] + [r_B(a)-r_B(b)] + [r_C(b)-r_C(c)].`

Then a common signed `Z^6` lift exists **iff `H=0`**. Each local representative's diagonal shift cancels in its pair differences, so `H` is well defined. There is exactly one interchart cycle; the graph-potential theorem makes its single vanishing condition sufficient.

Exact counterexample in **1-based** named axes:
`A=(1,2,3), B=(1,4,5), C=(2,4,6)`; choose local ordered min-zero triples `r_A=(0,0,0), r_B=(0,0,0), r_C=(0,1,0)`. Pairwise overlaps are all singleton, hence pairwise agreement is vacuous; nevertheless `H=1`, so no six-axis signed raw displacement generates these observations simultaneously.

For the explicitly declared **local raw-chart L1 edit metric**, every unit-coordinate edit changes H by at most its absolute magnitude. Therefore any repair of `H≠0` has cost at least `|H|`. Changing a shared-axis coordinate of the third chart by `-H` and re-min-zero-normalizing attains cost exactly `|H|`. This is a mathematical data-repair cost on chart inputs, not a claim about a native physical transition or energy.

## Executed exact verification

The author ran `research_checks/X6_THREE_SLICE_MINIMAL_HOLONOMY_UNIT64_20261116.py` in ordinary CPython and `python -O`; both exited successfully and yielded byte-identical JSON. The exact finite checks include:

- all **1,140** three-slice subsets of 20, with all **480** full-axis covers and 180/180/120 classification;
- **20,577** independent local chart triples across representative intersection types (19 min-zero triples with entries 0..2, so `3*19^3`), comparing a BFS integral-potential gluing solver to the explicit overlap/holonomy formulas;
- **2,187** signed six-axis raw Cell lifts (`3*3^6`) checking exact recovery modulo a common diagonal;
- explicit `H=1` non-gluing example and minimal raw-chart repair cost 1.

Finite computations independently corroborate the graph-theoretic **all-integer proof**, rather than replacing it. The immutable checker and full certificate are saved as:

- [Exact source/checker](https://github.com/awdawmip/enterprise-math/blob/9eb87f549606a5d6cd3e14d02007ae40bf50fa37/research_checks/X6_THREE_SLICE_MINIMAL_HOLONOMY_UNIT64_20261116.py), Git blob `4ab314a0b200c8c231b7a15152381add72d268a7`.
- [Exact integer JSON certificate](https://github.com/awdawmip/enterprise-math/blob/6e498d2d1c528ea33187a9e32b6f1619ec242fc9/research_checks/X6_THREE_SLICE_MINIMAL_HOLONOMY_UNIT64_RESULTS_20261116.json), blob `63699cb16e8610ccbc5ede1bb509ded3222048a8`.

## Source and consumer disposition

This is a new strengthening of previously verified 20-slice inverse-limit and depth-fiber results, relevant to **LP003/LP005/LP022/LP026** relative-coordinate consumers. Retain the native signed raw `Z^6` Cell identity, positive BRC multiplicity and independent ordered path history; the `H` residue is a **chart compatibility** predicate. No wrong current consumer was established or patched by this study.

The original 28-claim ledger at `a0bfa8eace20b061f5b228c733acdc46221388d7:research_artifacts/X6_LEGACY_PLANE_RECONCILIATION/claim_ledger.json` (blob `5881055c0801ca5bb0970756d500daa0114d36b0`) only retrospectively states alleged LP011 wrong signed-axis singleton argmax and LP019 positive N-BRC cancellation. Their exact wrong historical **callsite** remains `UNRESOLVED_PROVENANCE`; the inspected correct modules do not become culprits by association.

**Next precise action:** identify an actual consumer of partially compatible 3-axis charts and its operation; preserve H and h or demonstrate a safe quotient. Continue remaining 28-LP downstream calls, original LP011/LP019 provenance and independent Driver `REQUEST_REVISION`. Reuse previous frozen original R063, Helly and signed BRC +4 producer executions; do not repeat them.

Status: AUTHOR-EXACT / FINITE-EXECUTED / UNREVIEWED / NOT_ADMITTED.
