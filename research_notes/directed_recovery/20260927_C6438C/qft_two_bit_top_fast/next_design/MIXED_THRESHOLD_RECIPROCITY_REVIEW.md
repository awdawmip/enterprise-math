# Shared-context review of mixed threshold reciprocity

Status: PASS — symbolic, shared-context review; no scientific execution, host numerical test, independent admission, or novelty claim.

The complete reviewed source is `../MIXED_THRESHOLD_RECIPROCITY.md`, SHA256 `2f2f90d23324c3a672aec67e8ff7783ebfcb511fef6cdfae774e06a106a0949a`. This review binds that version. Its previously read dependencies are the period-extension proof `97d2011a41a2f0a8416151955daa4b08f448ab38336b9214e29d8a5208bbd3b6`, top-bit proof `880fb9d90f9258e0b96f6f47281bd711b11bd2ec515bddb6a6212cf45266ee89`, and degree-five proof `1453444f21c113c0d1819328b731031d0fe296e25756caac7e94d9cf628047b6`. No material mathematical defect was found.

## Threshold identity

Equation (3) correctly uses the endpoint value minus the weighted prefix before each jump. The restricted thresholds lie in `(b,D]`, hence their ceiling indices lie in `1..n-1`; for `n=1` both ranges are empty. At a coincident threshold (`zeta=0`), coarse-before-fine gives the old fine value `B_k^-` and the new coarse value `A_y`. Their two increments sum to the exact product increment. The replacement of the half-integer shift by the displayed integer shift in `A_y` is valid. These choices also cover a sample exactly on a threshold, exponent zero, and the convention `0^0=1` for the polynomial constant.

The coarse correction has total single-floor degree at most `u+a+c<=5`. The fine correction has the precise unit-slope mixed interface (4); replacing it by an already available ordinary-floor call would be unjustified. Rational polynomial expansions must combine their numerator before an exact division, as the source states.

## Spline identity and boundaries

The two pieces of (5) agree at the half-period and period junctions. Stretching gives knot values `(-1)^z V B(z)`. Directly subtracting adjacent slopes gives (7), initial slope `4H-1-2C`, and the coarse second difference (8). Since `m` is even, the coarse knot has positive `(-1)^(lm)`, explaining the **positive** coarse correction in (11). No endpoint slope jump is inserted.

The three ranges for `G(theta)` are necessary. Equation (10) applies only to `b<theta<=D`; at `theta=D` its value is zero. The prefix formula covers `theta=b`, and thresholds beyond `D` contribute zero. Thus the finite hinge rearrangement (11) is correct without scanning either long knot range as part of the claimed algorithm.

Expanding (5) verifies (12). On `z=2y+nu`, the two coarse floors become exactly the two offsets in (13), because `m` is even. Eliminating the indicator products through neighboring floor powers needs at most degree three in the coarse floor. Multiplication by the prefix linear kernel gives degree at most four; the active quadratic kernel gives total degree at most five. The four count refers to parameter families per original progression, not four arithmetic operations or four implemented mixed tables. Both modular orientations and their multiplicities remain required.

## Cost and continuation boundary

The normalization preserves degree but does not prove that recursive states decrease or have polynomial aggregate count. A subsequent transpose can restore the earlier denominator scales; a bounded number of children and memoization alone do not resolve this. The source correctly reports a remaining interface, without asserting hardness, independence of all moments, or impossibility of a different cancellation.

The degree-five single-floor extension is a distinct implementable subproblem. Its source was statically reviewed separately, but no such execution is certified by this note. Supplied order/address information remains paid; scalar identities do not themselves evaluate chronological matrix correlations or close full Shor sampling. The next useful step is a strict typed implementation of the ordinary degree-five contract, followed separately by a terminating mixed recurrence or an elimination of the particular combination.

Global-Knowledge-Sync: main@9f0e65b / GLOBAL_KNOWLEDGE_V1. This is the reviewer-read canonical snapshot; later coordinator journal-only refreshes are not represented as new policy reads here.
