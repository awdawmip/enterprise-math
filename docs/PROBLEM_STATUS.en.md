# Canonical Problem Status Index

Status: `CANONICAL`  
Effective: 2026-08-08

This file is the authoritative status ledger for numbered Enterprise Math research problems. `OPEN_PROBLEMS.en.md` preserves the original problem statements and may contain historical wording from the moment a problem was posed; when status wording differs, this index controls.

`RESOLVED` means that the specific numbered problem has a canonical main-branch answer at its stated scope. It does **not** mean the surrounding research area is closed.

| Problem | Status | Canonical scope/result |
|---|---|---|
| P001 | `RESOLVED` | `docs/P001_ROOT_MULTIPLICATIVITY.en.md`: integer roots are supermultiplicative, and multiplicativity holds exactly when the basin-product carry load stays below the next perfect-power threshold; the note also gives the exact carry count, downward-closed no-carry region, and a floor-division boundary. |
| P002 | `RESOLVED` | `docs/P002_COLLAPSE_GAP_BOUND.en.md`: the collapse gap has the sharp basin bound `0 <= G_p(n) <= (k+1)^p-k^p-1`, with equality exactly at the last basin state; the gap coordinate is a bijection across each basin. |
| P003 | `OPEN` | Global collapse-commutation classification remains Draft/noncanonical. |
| P004 | `OPEN` | Fixed points of arbitrary collapse words remain Draft/noncanonical. |
| P005 | `RESOLVED` | `docs/P005_SCALE_LATTICE_CORE.en.md`: total positive scale factor, divisibility projections, gcd/lcm scale lattice, path independence, and nonunique inverse refinement. |
| P006 | `RESOLVED` | `docs/P006_SIGNED_STATE_EXTENSION.en.md`: ordinary-order odd roots and signed-magnitude quantization are explicitly separated; even powers have no ordinary-order right adjoint on all signed states. |
| P007 | `RESOLVED` | `docs/P007_DISCRETE_DIVISION.en.md`: quotient, same-space multiple collapse, and reversible quotient/remainder state are distinct exact discrete semantics. |
| P008 | `RESOLVED` for the current v0.1 root/quotient/collapse family | `docs/P008_MINIMAL_ORDER_CORE.en.md` plus the Lean core: partial-order equality semantics, greatest-sublevel/right-adjoint existence, order-embedding exact recovery, and reductive idempotent collapse. Richer future operations may justify richer structure separately. |
| P009 | `RESOLVED` for the minimal typed collapse+coarsening system | `docs/P009_TYPED_SCALE_CORE.en.md`: strict trajectories terminate, no nontrivial cycles exist, pure projection is target-confluent, and mixed collapse/projection is generically nonconfluent. Noncanonical inverse lifts define a different system. |
| P010 | `RESOLVED` | `docs/P010_STRICT_HISTORY_MERGE.en.md`: exact reachable-collision criterion and exact multiplicity increment. |
| P011 | `RESOLVED` for finite deterministic maps | `docs/P011_INTEGER_IRREVERSIBILITY_SPECTRUM.en.md` and supplements: superadditive integer observables, complete collision spectrum, collision polynomial, and derived entropy comparisons. |
| P012 | `RESOLVED` at the metric-foundation scope | `docs/P012_INTRINSIC_DISCRETE_GEOMETRY.en.md`: primitive-step graph distance gives an exact integer metric; the supplement explicitly separates metric structure from inner-product/Pythagorean structure. Broader discrete geometry remains open research. |
| P013 | `RESOLVED` | T001 and T005 are Lean-checked in `EnterpriseMath/Arithmetic/IntegerRoot.lean`; the warning-fatal pinned Lean build passes in CI. |
| P014 | `RESOLVED` | T010 is Lean-checked in `EnterpriseMath/Scale/Compatibility.lean`, with `EnterpriseMath.lean` importing the module so CI actually compiles it. |
| P015 | `OPEN / CONTINUOUS` | Prior-art mapping remains an ongoing obligation as new components are added. |
| P016 | `RESOLVED` at the protocol level | `docs/P016_PHYSICAL_FALSIFICATION_CONTRACT.en.md` and `falsification.schema.json` define F1–F9 quantitative kill-test requirements. This does not validate or falsify the physical hypothesis itself. |
| P017 | `OPEN / ACTIVE RESEARCH` | The Legendre pressure test has many canonical structural lemmas but no proof of Legendre's conjecture; continue pressure-testing and counterexample-first work. |
| P018 | `OPEN / ACTIVE RESEARCH` | The finite-precision proof calculus is an expanding foundational program; current stages are canonical results but the numbered research program remains active. |

## Status discipline

A Draft PR, branch theorem, finite computation, or unmerged formalization never changes a numbered problem to `RESOLVED` here. Promotion requires a main-branch result at the stated scope and all applicable final gates.

If a resolved problem later receives a stronger extension, add a new problem or explicitly widen the scope; do not silently reinterpret the old `RESOLVED` label as a universal closure claim.
