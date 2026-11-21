# X6 native time — Unit236: exact bidirectional 36-state BRC/Cell time carrier

Date: 2026-11-21 (Asia/Hong_Kong)
Task: `RS-X6-NATIVE-TIME-DYNAMICS` / `TP2-91D4A7C2F63805BE21A3`
Author: existing Research lane `chatgpt-research-onhour-enterprise-math-20260923`, researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`
Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED**. No new P000 axiom, physical branch-selection, fiber time law, or independent review.

## Source lease and new question

Preserve frozen scientific pin `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`:
- `p000_reality_foundation.json` (signed X6 Cell torsor, time orders relational change);
- `research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md` (exact two shortest primitive native paths between adjacent selected C6 shell Cells; all-OUTER local C12 lift);
- `research_notes/VIETE_NATIVE_HALF_TURN_PRINCIPAL_ROOT_BUNDLE_20260905.md` (oriented OUTER half-turn sweeps select static root addresses ±3; C6 aliases sign and C12 resolves it).

Consume existing Unit234 (18-state *fixed forward chirality* two-branch model) and Unit235 (12-phase abstract clock). The new native-time question is whether **both possible sweep chiralities** can be represented by a *single* observer-safe Markov state, with reverse primitive steps, BRC branch history and the source principal-root interpretation correctly typed.

All paths here are the two-shortest-path **native possibility population**. INNER admissibility under a future physical rotation/triadic selection law remains unknown. `R063` belongs to the separate `RS-X6-LEGACY-PLANE-RECONCILIATION` original native benchmark and is not executed or substituted.

## Exact oriented native Cell graph

Choose a real pivot Cell as chart anchor in a centered three-axis slice of the full signed six-axis torsor. With zero-valued *omitted coordinates only for this declared slice*, let

```
a_0=e_1, a_1=e_2, a_2=e_3,
a_3=-e_1, a_4=-e_2, a_5=-e_3.
```

Take `r∈Z/6Z`, sweep chirality `ε∈{−1,+1}`, and `b=a_(r+ε)`. The two exact shortest native microtraces from `a_r` to `b` are:

- **INNER:** `a_r → 0 → b`;
- **OUTER:** `a_r → a_r+b → b`.

Every displayed arrow has exactly one signed X6 unit-axis component; the reverse sweep uses the reverse ordered Cell path, not an independently assumed reverse physics. Introduce decorated states `S(r,ε), I(r,ε), O(r,ε)`, with outputs `c(S)=a_r`, `c(I)=0`, `c(O)=a_r+a_(r+ε)`; transitions

```
S(r,ε) -> I(r,ε) or O(r,ε)
I(r,ε), O(r,ε) -> S(r+ε,ε).
```

**Theorem 1 (sharp live Cell observer).** This source-possible oriented time graph has 36 live states, 48 primitive arrows and precisely 13 distinct native spatial Cell outputs. For the observer that reads current and *all allowed subsequent native Cells* (including alternatives), **36 is the minimal exact Markov-state count**, or **6 fixed-length bits**. More sharply, length-at-most-two future Cell word sets distinguish every pair of states; the successive partition counts at horizons 0,1,2 are **13,30,36**.

Proof: each of the 36 states is sufficient because the shown transition function and Cell output determine the complete future branch trace set. For necessity, distinct shell Cells have norm-square 1; OUTER gates have norm-square 2; INNER pivot is 0. Opposite-sweep shells at the same Cell reach opposite neighboring shell Cells after two steps. Equal OUTER gate Cells from reverse uses of one edge have different forced next shell Cells. INNER states have equal current pivot, but their next shell Cell `a_(r+ε)` separates all except the opposite-chirality pair leading to that same shell; those two have distinct future OUTER gate options at the following event. Thus every two decorated states have unequal future Cell trace sets at horizon ≤2. The exact finite checker independently enumerates all 36 pairs and all transitions. The result is scoped to the displayed possibility graph, not a statement that an actual full-X6 dynamical law activates all 36 states.

**Theorem 2 (time and sweep clock).** Define the orientation-relative *event-phase* map

```
Φ(S(r,ε)) = [2εr]_12
Φ(I(r,ε)) = Φ(O(r,ε)) = [2εr+1]_12.
```

Every primitive transition increments `Φ` by 1 modulo 12, because `ε²=1`. For each fixed chirality, even-phase fibers have one source state and odd-phase fibers have two; keeping `(Φ,ε)` yields **24** abstract time/chirality states (5 bits). The 24-state quotient preserves the event-phase and orientation label, **not** all physical Cell observations or BRC provenance. Erasing the chirality label gives the 12-state time-only clock (4 bits). On the source-proved **all-OUTER** two-direction subpopulation, 24 oriented live states suffice for the Cell and sweep interface; its two oriented traversals share the same 12 spatial Cell positions.

**Theorem 3 (static principal-root readout).** On a *source-qualified all-OUTER oriented half-turn arc*, `Σ(A(r,ε))=3ε∈P_rot` is an invariant of the sweep direction. After six native microsteps it ends at `a_(r+3)=-a_r`; after twelve it returns to the starting Cell. The two directions have indistinguishable root readouts `[±3]_6=[3]_6`, but differ already at `C12`: `[3]_12 ≠ [-3]_12=[9]_12`. This map **selects an existing root/precision lineage and does not assert that the precision fiber advances with elapsed microsteps**. For mixed INNER paths the variable `ε` remains an ordered-sweep/BRC tag; applying the frozen geometric principal-root section to INNER paths would exceed its source lease.

**Theorem 4 (exact oriented BRC multiplicity).** Starting from `a_0`, choose a fixed sweep sign and `W≥1` full six-edge C6 circuits. At `12W` primitive events, `6W` independent INNER/OUTER branch choices create exactly `2^(6W)` different complete ordered Cell histories, each with the same starting/ending shell and even-step shell sequence. Combining both possible sweep signs gives exactly `2^(6W+1)` different ordered histories with the same initial/final Cell and same event count. The orientation is distinguished by the shell order; distinct branch words are distinguished at the first unequal intermediate Cell. For each fixed orientation, the exact number with `j` pivot visits is `binom(6W,j)`. The history observer therefore needs **6W+1 bits** on the joint two-direction population; the current/future state quotient does not retain past BRC word labels. This is a cardinality lower bound for this stated source-possible population, not a physical stochastic probability or unbounded-time finite-state memory assertion.

## Executed exact certificate and original objective

The self-contained JavaScript checker at `experiments/x6_time_bidirectional_36state_20261121/check_36state.js` evaluates the six signed axes as full six-component integers, exactly checks all 48 primitive arrows, the phase semiconjugacy, length-2 Cell trace partitions, the 12-step OUTER orbits and half-turns for both chiralities, and the complete `W=1,2` BRC populations: 128 and 8,192 distinct full two-direction histories. Exact arithmetic only, no floating point. Its result is `experiments/x6_time_bidirectional_36state_20261121/results.json`. Symbolic proofs cover all `W≥1`; finite checks only claim their declared finite domains.

This combines the existing native BRC two-path realization and frozen Viète sweep-root selector to give the parent objective an exact **bidirectional time/Cell/phase/root typing and an observer-minimality certificate**. It leaves separate the primitive event count, periodic phase, current/future Cell, elapsed BRC history, and static precision/root lineage.

## Remaining exact scientific and evidence debt

The source does not yet supply a global **physical** Cell/Link/Port transition selecting INNER/OUTER or defining internal/precision-fiber time motion; the 36-state population therefore remains possible rather than physically admitted. Look for a frozen native rotation or triadic Port rule that restricts this graph, and recompute reachable states and observer-safe minimal quotients. A physically independent C12/C24 same-Cell closed-loop fiber readout is not present in these pins. Independent Driver review and Result admission are pending.

Original R063 six-file native regression is a distinct task/issue `#2416`, with unassigned runner support; this Unit does not substitute for its native 1..512 regression or original 17 gates. Preserve all prior native and Activity requests as their own journal events.
