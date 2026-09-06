# Conjecture historical backfill audit — generation 2

Status: `GOVERNANCE BACKFILL / NO THEOREM PROMOTION`
Date: `2026-09-06`
Registry generation: `BACKFILL-20260906-G2`
Registry: `conjecture_registry.json`
Policy: `docs/CONJECTURE_ASSET_GOVERNANCE.md`

## Purpose

Continue the high-confidence historical scan after generation 1, with special attention to records labelled or written as `frontier`, `TESTING`, `empirical`, `main bridge conjecture`, or `smallest unresolved unit`.

The classification rule remains strict: an unfinished route is not automatically a conjecture. A registry entry requires a precise falsifiable assertion whose proof/soundness scope is genuinely unresolved.

## Generation-2 sources inspected

- `knowledge/projects/enterprise-math/pde-fcc-shell2-second-variation-frontier-20260906.md`;
- `knowledge/projects/enterprise-math/pde-opposite-edge-90deg-multipath-resonance-frontier-20260906.md`;
- `knowledge/projects/enterprise-math/pde-tetrahedral-strain-graph-tree-frontier-20260906.md`;
- `knowledge/projects/enterprise-math/pde-critical-helicity-double-null-20260906.md`;
- `knowledge/projects/enterprise-math/nt-rh-threshold-block-ablation-stability-20260906.md`;
- `knowledge/projects/enterprise-math/nt-rh-log3-branch-sine-arb-positivity-20260906.md`;
- `knowledge/projects/enterprise-math/nt-rh-log3-full-window-negative-index-20260906.md`;
- `knowledge/projects/enterprise-math/poincare-brc-normal-surface-arithmetic-observer-20260905.md`.

## New registered conjectures

### `CJ-TH-20260906-004`

**Navier-Stokes 90-degree opposite-edge resonance admits a four-STAR checkerboard native lift.**

The source explicitly labels the mechanism `Main bridge conjecture / open target` and already proves the carrier-side ingredients: the 90-degree resonance locus, the three K4 opposite-edge classes, four shortest STAR-mediated paths, gauge-robust checkerboard signs and their zero sum, and the identification of the same 2D checkerboard sector with the extensional strain gaps.

The unresolved assertion is narrower and now frozen: the actual classical resonant NS quadratic coefficient is represented by that native four-path effective sum with symmetry-matched leading weights, so the constant leading resonance cancels and only a mixed-second-difference/path-imbalance defect survives.

No scale-critical estimate or regularity conclusion is bundled into the conjecture.

### `CJ-TH-20260906-005`

**H_log3 N=8 interior threshold inertia is stable under regular archimedean-tail ablation.**

This is the intended bounded-conjecture use case. The source reports floating equality of full and principal-block threshold-inertia counts at

- `eta=0.9 -> 8`;
- `eta=0.99 -> 6`;
- `eta=0.999 -> 5`;

and explicitly keeps the observation at `TESTING` pending interval/ball matrix evaluation and certified interval `LDL*`.

The registry freezes only this 32-dimensional finite section and these three interior thresholds. `eta=1` is deliberately excluded because the floating margin is too small to use as sign evidence.

Because this conjecture is explicitly finite, a complete rigorous interval/certificate verification can promote exactly this bounded claim directly to `PROVED` without implying full-window positivity or RH.

## Deliberate non-registrations in generation 2

The following were scanned and classified but not turned into conjectures:

- FCC shell-2 second-variation frontier: exact first/second variation identities are proved; the desired viscous-absorption estimate is not yet a frozen quantitative law.
- Tetrahedral strain graph/tree frontier: exact K4/tree/Betchov identities are proved; the `theta<1` closure form is a target with an unspecified remainder class.
- Critical-helicity double-null frontier: exact/conditional identities and criteria are established; the unconditional aggregate cancellation bound is only a next target.
- `H_log3` branch-sine Arb positivity: `V_2` and `V_8` positivity are already rigorously certified; the Galerkin-complement closure is open.
- `H_log3` full-window negative index: `n_- <= 80` is already certified; weighted Birman-Schwinger/Slepian routes are improvement ideas, not asserted truths.
- Poincare/BRC arithmetic observer: the sound pruning mathematics is derived; empirical speedup/implementation payoff/novelty are exploratory rather than mathematical conjectures.

## Current registry totals after G2

- conjectural theorems: `5`;
- conjectural tools: `1`;
- total conjecture assets: `6`;
- deliberately classified non-conjecture historical candidates: `11`.

## Proof / falsification queue update

The immediate queue should distinguish leverage from proof cost.

1. `CJ-TH-20260906-005` is the best short closure target: finite, already numerically stable at three interior thresholds, and designed for interval `LDL*` certification.
2. `CJ-TH-20260906-004` is the highest-value new PDE bridge: prove or kill the exact dynamic four-path coefficient correspondence before spending effort on downstream critical estimates.
3. `CJ-TH-20260906-002` remains the major RH asymptotic structural target.
4. `CJ-TH-20260906-003` remains the major PDE aggregation target.
5. `CJ-TL-20260906-001` remains conditional on `CJ-TH-20260906-002`.
6. `CJ-TH-20260906-001` remains restricted and lower priority because its carrier is already known to be non-optimal.

High priority still means urgent to prove or falsify, not more likely true.

## Scan status

Generation 2 materially expands the historical inventory but does not claim that every old research file has been exhausted. The canonical rule is now to continue backfill in audited generations and to scan conjecture candidates at each substantial research closeout, so new unproved assets do not accumulate invisibly again.
