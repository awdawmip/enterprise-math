# Correlated inverse-pair transport: actual interfaces and geometry boundary

Status: SHARED_CONTEXT_SOURCE_AUDIT_AND_SYMBOLIC_INTERFACE; no scientific execution in this review; not admission. This note audits current source at Enterprise Math `2e81851d62c869a20b47ae083a24dde1a4c0420c`. The separate finite `conic_transport/` execution is reviewed separately. Classical inversion symmetry and a unit conic are REUSE; preserving their correlation through the existing BRC histogram interface is a domain composition/EXTENSION, not a new Foundation or a newly discovered classical trace identity.

## 1. One useful interface, with an actual saving to measure

For an integer N >= 2, keep a live **internal arithmetic state** `(u,v)` with certified `uv = 1 mod N`, rather than repeatedly recovering `v` from `u`. It contains no more mathematical information than the unit u. It deliberately stores redundant information so that inversion becomes the exact exchange

`J(u,v) = (v,u)`.

Given a certified multiplier pair `(c,d)` with `cd = 1 mod N`, the two updates are

`F+(u,v) = (cu,dv)`, `F-(u,v) = (du,cv)` modulo N.

The products are performed by the existing actual typed modular-column interface. Both preserve the unit-conic relation. Moreover `J^2 = I` and `J F+ J = F-`, over every residue ring, including prime powers and rings with zero divisors. Only u, v, c, d must be units; primality, order and factors are not inputs.

This gives a concrete small interface candidate:

```
prepare_step(N, c, typed_factory) -> StepCertificate
    bind actual source, N, c, d and the typed cd=1 receipt;
    retain both modular-table setup records, without hiding an inverse-table setup.

transport(pair_certificate, step_certificate, sign) -> PairCertificate
    two actual modular columns, parent/step references, actual output pair;
    sign in {+, -}; negative action is the exchanged correlated action.

fold(pair_certificate) -> CanonicalPairCertificate
    actual typed compare; retain either (u,v) or (v,u), plus orientation bit;
    no call to inverse_certificate(u).

observe_first_factor(pair_certificate, depth) -> LIVE or FACTOR(g, depth)
    existing typed modsubtract/gcd and proper-factor division receipt;
    an absorbed factor carries the identity histogram [1] thereafter.
```

This is a proposed reusable certificate boundary, not an already implemented import name. The actual finite runner currently performs these steps inline. A reusable importer must reject malformed/source-mismatched certificates or replay them; the invariant cannot be accepted merely because an input field says `conic=true`.

The specific eliminated work is per-visited-state extended Euclid for inversion folding. It is replaced by transporting the inverse coordinate and a paid comparison. It adds a second modular product to each nonidentity branch and a second residue field. Thus it can lose against a nonfolded one-coordinate route, or against another implementation already maintaining inverses. No bound on the number of reachable states, no order-finding shortcut, and no total-speed advantage follows.

The existing `LazyModularColumns(N,c)` constructor itself pays an inverse/permutation certificate. A separate table for d normally pays its own setup too. The current finite execution correctly charges both: “zero standalone state inverses” is accurate; “only one Euclidean computation in the whole layer” is not an accurate description of that implementation.

## 2. Why the stopped histogram law is preserved

Let `[w]` denote one microscopic branch of weight w. At each live pair use

`2[1/4] I + [1/4] F+ + [1/4] F-`.

The two identity branches are retained as multiplicity two, not replaced by one `[1/2]` branch. Exchange fixes the identity branches and interchanges the two equally weighted nonidentity actions. Hence pushing the complete outgoing weight histogram to exchange orbits gives the same row from either representative.

The observer is `g(u)=gcd(u-1,N)`. Since `v-1 = -v(u-1) mod N` and v is a unit, `g(u)=g(v)` as the actual divisor, not just as a success flag. The post-step observer and first-hit depth therefore factor through the orbit map. On a proper factor the process moves to `(FACTOR,g,depth)` and remains there with atom `[1]`. The finite first-hit histogram theorem in `WITNESS_QUOTIENT_CANDIDATE.md` now applies by induction, preserving every retained LIVE orbit and named factor/first-hit-depth histogram.

This is a **histogram-kernel** quotient. Separately named F+ and F- generally do not descend through exchange: the group interchanges their names. An asymmetric future kernel or an observer retaining which signed branch was chosen can invalidate the quotient. It also does not preserve the original two-endpoint path provenance. These are declared observer limits, not discarded hidden data within the stated histogram law.

Canonical ordering of u and v uses the declared residue representation and an actual typed comparison. It is a representation convention, not a symmetry-invariant choice from an unlabeled two-element torsor. Preserve the orientation bit if any later interface needs a signed branch name. At a fixed point u=v, the orbit has size one; branch multiplicities still remain in the histogram and must not be divided by two.

## 3. What T0, T6 and T7 actually provide

All source links below are immutable at the audited commit.

| Existing interface | Actual usable contribution | Boundary |
|---|---|---|
| [T0 WeightHistogram](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/brc_histogram.py), blob `9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1` | Existing `histogram_serial`, `histogram_recoalesce` retain microscopic weights and multiplicities in the finite runner. | Positive histogram law, not signed Shor amplitudes or complete labeled-path identity. |
| [T7 finite_symmetry.py](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/finite_symmetry.py), blob `ae96a32cb6b6fdd974bd9f44fb28a1b643c9b8a2` | `validate_finite_group_action`, `orbit_partition`, `is_equivariant_map` can audit the declared two-orientation action, or an explicitly supplied bounded carrier. The conjugacy proof above supplies the general algebraic bridge. | These APIs require complete finite permutations. Enumerating all units/orbits is not a free implementation of the general proof. They are not called by the present conic runner. |
| [T6 operation_quotient.py](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/operation_quotient.py), blob `758a65de02a434446936cd7e37b2ae604eade863` | Explicit finite deterministic descent/refinement for declared named maps. Reusable as a bounded counterexample or audit mechanism. | It checks every named action, a stronger/different contract than the symmetric histogram kernel above. It cannot certify exchange folding by silently forgetting action names. |
| [T6 predictive_quotient.py](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/predictive_quotient.py), blob `f27d9ddf908f5b07051acfaf0c69f359d499b98b` | Finite-horizon or stable refinement once a complete finite system and observer are supplied. | Explicit state enumeration and named-action observation are charged inputs, not an unknown-order solver. |
| [ControlPacket](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/brc_control_port.py), blob `44def6b8ac787e798d3cc2c6be16f873f91b9db8` | Nonspatial finite control ports, exact joint affine-effect histograms, chronology-aware serial composition, and `certify_control_partition`. Useful for an explicitly affine lift/port audit. | Modular multiplication/reduction is not an affine map over Q. Its partition certificate compares exact effect-valued rows, not rows equal only after a modular readout. Do not feed modular F+/- as ordinary rational Affine actions. |

The registry describes T6 as observer/operation-language relative and T7 as standard finite group-action machinery, not Enterprise-specific target lookup. The current proposal uses these principles without claiming a new global tool family. The genuine work saving arises from maintaining the correlated inverse witness through actual T0/typed arithmetic, not from invoking a new name for the conic.

## 4. Exact coordinate-address preservation boundary

The current [coordinate_address_contract.json](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/coordinate_address_contract.json), blob `186895a2545b9c5f31de6dc0944aef157f4b35d1`, makes an address-only change. Raw X6 retains signed coordinates. The final nonnegative six-field interface is only the image of a registered lossless codec, not all of N^6. At this snapshot the registered codec is the fixed two-generator slice `three_region_slice_v1`; a general full-X6 codec is not registered.

Actual APIs are [cell_address.py](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/cell_address.py), blob `fc77f374ed8b7948dac2d5a0bfcad87ee828e97b`, and [_cell_slice_codec.py](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/_cell_slice_codec.py), blob `2aa70d8f8509dc31d73f6891b97f9fdf7377df2a`. `encode_raw_slice`, `decode_raw_slice`, and the four directed `step_cell` moves have a precise fixed-slice meaning. For positive integer representatives (u,v), the legal encoded address is `(u,v,0,0,0,0)`. This fact alone proves only an injective address representation.

In particular:

* Swapping two internal arithmetic fields is legitimate wiring. Swapping two spatial axes is not thereby proved to be a same-cell rechart or a native adjacency-preserving physical operation.
* Reduction modulo N identifies different integer lifts. The current coordinate contract does not permit that identification as a lossless native Cell rechart. A residue returning to 1 is not a native Cell returning to its initial address.
* The contract preserves native Cell population, signed operation domain, adjacency and decoded metric, common depth/omitted information, ordered edges/ports/branch IDs/weights, boundaries, initial states and time labels. The arithmetic conic quotient declares a narrower task observer and cannot claim to preserve all of those spatial data.
* A nonnegative address, zero inactive slots, a minimum-zero normalization or an axis picture is not a proof that omitted lift/depth information vanished harmlessly.

An optional **unreduced positive lift** `(X,Y)` gives an honest affine bridge: apply integer diagonal effects `diag(c,d,1,1,1,1)` and `diag(d,c,1,1,1,1)` on the raw fixed slice, and perform modulo-N observation separately. Both preserve `XY=1 mod N`; exchange conjugates them exactly. This can use the rational affine-effect container without claiming its matrices perform modular reduction. However, the two diagonal maps are mutual inverses only modulo N, not generally over Q or the unreduced integer lattice. Large diagonal macro-actions are not one primitive adjacency step. A primitive-path/time interpretation needs an additional paid realization, and this optional lift was not executed here or by the finite residue runner.

The old `definitions/enterprise_coordinate_system_and_brc_bridge.json` is superseded and is not an authority for this construction.

## 5. Why the other geometric/HBW interfaces do not close the gap

[brc_transport.py](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/brc_transport.py), blob `be1debe367263931bd5e93fd750be3ed54624fe1`, has exact rational affine effects and degree-at-most-two moments. Joint effect histograms may support the unreduced lift just described. Its moment lease does not include gcd, modular threshold/occupancy, factor extraction, or full path provenance. A degree-two relation `uv=1 mod N` does not make gcd a degree-two observer, and independent coordinate marginals lose the needed correlation.

[heartbeat_carry_peak.py](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/heartbeat_carry_peak.py), blob `44bde8bbff397adf8aec80fcb2bffa79c6e272e9`, has actual `first_passage_prefix` / `first_hit_generating_value` interfaces for a declared p-adic lattice-peak observer, with HIT/UNKNOWN accounting and an input prime. Its quotient preserves an oriented p-lattice, not arbitrary gcd observations. Supplying an unknown prime factor as p would give away the target. Its first-hit accounting pattern is reusable; its lattice observer cannot simply be replaced by “factor found.”

[heartbeat_weighted_germ_lift.py](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/heartbeat_weighted_germ_lift.py), blob `9cb12b10890a14d179ea3aa036fcde1b08728134`, retains weighted germ compatibility at a declared prime/precision. It is not a proof that a gcd-sensitive conic state is determined by those germs. No use of its mass quotient is licensed without a new observer-preservation bridge.

[brc_newton_quadratic_selector.py](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/brc_newton_quadratic_selector.py), blob `9a2bff3e8026f2fe68680994d74082883461c84b`, uses rational/real quadratic root selection. It does not select the correlated pair of modular trace successors over a ring with zero divisors. The repair is to retain the inverse-pair lift, not to invoke this selector as a modular root oracle.

## 6. Small certificate target and remaining cost

A bounded next checker can consume an existing schedule and compare this pair representation against saved inversion-folded histogram evidence, retaining all first-hit factor values/depths and LIVE classes. Charge separately: distinct c/d table setups, every queried column and cache hit, typed compare, gcd/verified factor division, schedule construction, invariant validation, histogram operations, and optional certificate replay. A one-catalog native call count cannot stand for this total work. Include a nonconic pair rejection and unequal branch-weight/named-action negative controls before making a reusable-interface claim.

The parent has now executed a bounded inline instance of this plan in `conic_transport/`; this audit makes no additional numerical execution or extrapolation. The unresolved costs remain reachable support, multiplication, gcd observation and output size. The design helps one previously measured inverse bottleneck. It does not complete a general native Shor simulator, prove efficient factoring, or turn a classical modular conic into a new native spatial axiom.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.
