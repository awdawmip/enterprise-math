# Driver Review — Native Oriented-Matroid / Circuit Tool Discovery

Driver-ID: `EM-DVR-ZX1UEJ`
Date: `2026-08-22`
Task: `RS-TD-OM-NATIVE-ORIENTED-MATROID-CIRCUIT-CALCULUS`
Owner branch: `research/tool-native-oriented-matroid-circuits`
Researcher: `EM-TDOM-BH6ND3`

## Verdict

`ACCEPT_DERIVED_TOOL_WITH_SCOPE_NARROWING`

Frozen tool classification:

`TYPED_INCIDENCE_CIRCUIT_CALCULUS_ACCEPTED`

The stronger proposed direction-level oriented-matroid refoundation is **not** accepted.

## Accepted reusable interface

For a finite component-typed incidence skeleton

`Gamma=(V,E,s,t,tau)`,

choose only a reference orientation of edges as gauge and form integer 1-chains. The accepted circuit object is the sign vector of a primitive support-minimal nonzero circulation in `ker(partial)`. For ordinary graph skeletons these are exactly signed simple cycles. Dually, cocircuits are support-minimal signed cuts/bonds.

Accepted API:

- `SIGN`;
- `CIRCUITS`;
- `ELIMINATE`;
- `SEPARATE`;
- `DUAL`;
- `REALIZATION_CHECK`;
- path-defect decomposition of same-endpoint path pairs into circuit combinations.

The report supplies signed elimination, circuit-cocircuit orthogonality, deterministic finite checks, and reuse on both native spatial/shuffle incidence and nonspatial BRC recoalescence/provenance skeletons.

## Mandatory no-go boundary

`DIRECTION_ONLY_SIGNED_CIRCUIT_NOT_DERIVED`.

The bare three positive direction types do not, at current native strength, carry a signed dependency merely because a classical/carrier realization satisfies a linear relation. In particular the carrier relation `e1+e2+e3=0` may not be imported as a native circuit dependency.

Therefore this tool begins only after a finite incidence/transition skeleton exists. Its status is:

- `N0 DERIVED` when the skeleton itself is N0-definable;
- `CONDITIONAL DERIVED` when the skeleton depends on N1/process placement semantics.

No carrier angle, Euclidean determinant, slope, metric magnitude, or Pythagorean law is part of the circuit definition.

## Tool status

- semantic level: `DERIVED_RELATIONAL / INCIDENCE TOOL`
- Foundation mutation: `NONE`
- direction-only chirotope: `NOT_DERIVED`
- circuit elimination: `PASS`
- dual/cocircuit interface: `PASS`
- cross-domain reuse: `PASS`
- provenance-preserving path-defect use: `PASS`

## Successor gate

No broader oriented-matroid Foundation stage is authorized. Future tasks may call this circuit calculus on an admitted skeleton. A stronger chirotope/oriented-matroid claim requires a genuinely new native dependency/orientation datum and separate Foundation review.
