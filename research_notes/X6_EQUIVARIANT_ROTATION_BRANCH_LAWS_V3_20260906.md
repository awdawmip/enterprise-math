# X6 equivariant rotation branch laws V3: two memoryless sections and exact phase-memory cost

Status: `FREE_RESEARCH / EXACT LAW-CLASSIFICATION / NOT_FOUNDATION`
Date: `2026-09-06`
Task: `RS-X6-NATIVE-ROTATION-DYNAMICS`
Consumes:
- triadic signed-C6 generator `Q_S`;
- concrete shortest INNER/OUTER branch fiber;
- atomic triadic `III` law;
- current Viète faithful OUTER law;
- path-jet/BRC observer hierarchy.

## 1. Question

For one `Q_S` signed-C6 macro rotation every phase edge has exactly two shortest native Cell realizations, INNER and OUTER.

Which deterministic branch patterns are possible if the law itself carries no extra phase label, hidden field or memory and is required to respect the native frame symmetry?

## 2. Fixed-triad Q-equivariance forces a constant branch

Fix an oriented selected triad `S` and write its six macro edges as

`E_r: a_r -> a_{r+1}`, `r in C6`,

with `a_{r+1}=Q_S a_r`.

A deterministic shortest branch law is a function

`b:C6 -> {I,O}`.

The linear frame action of `Q_S` maps

- `INNER_r` to `INNER_{r+1}` because the pivot Cell maps to itself in relative coordinates;
- `OUTER_r` to `OUTER_{r+1}` because `a_r+a_{r+1}` maps to `a_{r+1}+a_{r+2}`.

Therefore a memoryless Q-equivariant law must satisfy

`b(r+1)=b(r)`

for every `r`.

Hence `b` is constant.

There are exactly two such deterministic sections:

- `I^6`;
- `O^6`.

## 3. Full native axis-frame equivariance leaves the same two laws globally

The positive-axis permutation group `S6` is transitive on three-axis selections. Relabeling an entire shortest macro context preserves the semantic branch type INNER versus OUTER.

Therefore a universal deterministic shortest-path law which is

- memoryless;
- Q-equivariant within each selected triad;
- S6-equivariant between selected triads

must make the same constant choice on every triad.

Thus the exact global classification is still

`{ALL_INNER, ALL_OUTER}`.

This does not claim that every physical rotation is shortest or memoryless. It classifies that restricted law class completely.

## 4. Current two exact physical/research sections occupy the two extrema

Two independently typed current laws select the two allowed extrema.

### Atomic triadic force closure

The common-Cell atomic-node condition forces all three force tokens to use INNER simultaneously. At the one-token level the underlying shortest section is INNER.

### Faithful Viète root/phase refinement

On its declared single-phase trajectory interface, the current Q-equivariant faithful nonzero intermediate root law selects OUTER.

Thus the two already-derived laws are not arbitrary members of a large symmetric memoryless family: they occupy the only two deterministic fully equivariant shortest sections, selected by different consuming relations.

This is not a claim that force dynamics and Viète phase dynamics are the same physical process.

## 5. Nonconstant branch patterns require phase memory

Let `b in {I,O}^6` be an arbitrary periodic branch pattern on one Q cycle.

Let

`H_b={k in C6 : b(r+k)=b(r) for all r}`

be its shift stabilizer.

The number of distinct phase-shifted versions of the law is

`m(b)=6/|H_b|`.

A deterministic implementation that must know which shifted version is active needs at least `m(b)` distinguishable phase/memory states if no other variable already carries that information.

This bound is exact: the quotient phase state

`C6/H_b`

is sufficient to choose the correct branch.

Examples:

- constant `IIIIII` or `OOOOOO`: `m=1`, no phase memory required;
- alternating `IOIOIO`: `m=2`, exact `C2` repair;
- repeated block `IIOIIO`: `m=3`, exact `C3` repair;
- generic aperiodic six-bit pattern: `m=6`, exact `C6` repair.

Therefore a mixed branch cycle is direct evidence of additional phase/internal state rather than a memoryless frame law.

## 6. Token-symmetric joint triadic laws

At one atomic triad macrostep, before the closure relation is imposed, the joint shortest branch space is

`{I,O}^3`.

Let `S3_token` permute the three force-token labels. A deterministic branch tuple fixed by every token permutation must have all three entries equal.

Hence the only token-symmetric deterministic joint sections are

- `III`;
- `OOO`.

The atomic common-Cell law selects `III`; `OOO` does not have a common midpoint Cell and therefore is not a primitive atomic closure under the present realization.

Thus P000 atomic stability plus the common-node realization removes the second symmetric option in the primitive force sector.

## 7. Symmetric stochastic memoryless law

A token-exchangeable stochastic joint law on `{I,O}^3` is classified by four total weights

`p_k`, `k=0,1,2,3`,

where `k` is the number of OUTER branches and

`sum_k p_k=1`, `p_k>=0`.

Conditional on `k`, exchangeability assigns equal weight to the `C(3,k)` token patterns unless additional token state breaks the symmetry.

Q-equivariance requires the same four weights at every C6 phase if there is no phase memory.

For a primitive atomic closure event the common-midpoint condition forces

`p_0=1`.

So stochastic branch uncertainty is not compatible with the restricted atomic closure law unless the law/state model is enlarged beyond that realization.

## 8. One-token stochastic law and path-area observer

For one generic rotation token, an equivariant memoryless stochastic shortest law is classified by one scalar

`p = Prob(OUTER)`.

No independence across macrosteps is implied by this marginal parameter.

The current second-order path-jet theorem gives local antisymmetric area

`A(I)=-a wedge b`,

`A(O)=+a wedge b`.

Therefore at one edge

`E[A]=(2p-1) a wedge b`.

Over one full Q cycle, the second-order area is affine-linear in the six branch bits. If all six phases have the same OUTER marginal `p`, then

`E[A_cycle]=p * A(ALL_OUTER)`

because `A(ALL_INNER)=0` and expectation is linear. Correlations between branch bits are invisible to this mean second-order observable and require higher/path-joint observers.

Thus path jets provide a direct measurable/readout bridge from a weighted branch law to finite tensor observables without replacing the underlying BRC distribution.

## 9. Law selection versus provenance retention

The classification yields an exact routing rule.

### Law known and deterministic

If a consuming relation proves one of the unique sections, the next branch witness is derived rather than stored independently for Markov prediction.

### Law contains finite phase pattern

Retain the exact quotient phase memory `C6/H_b` or another variable proved to carry the same information.

### Generic/weighted/history-sensitive rotation

Retain the BRC/path distribution or a scope-proved sufficient observer such as a finite tensor jet. Do not collapse to one frame element.

## 10. Current rotation frontier

Closed in the shortest memoryless sector:

- exactly two Q- and S6-equivariant deterministic single-token sections: all-INNER and all-OUTER;
- exact phase-memory cost for every mixed 6-bit pattern;
- exactly two token-symmetric deterministic joint triad sections: III and OOO;
- primitive atomic common-node law uniquely selects III;
- exchangeable stochastic joint law reduces to four OUTER-count weights, with atomic closure forcing the deterministic endpoint `p_0=1`;
- one-token stochastic law has one OUTER marginal, with an exact second-order path-area readout.

Still open:

1. non-shortest rotation laws;
2. state-dependent laws driven by fields/channel/internal variables;
3. interactions between branch law and duration/energy calibration;
4. whether a larger native rotation generator set beyond the current triadic frame group is physically admitted;
5. external calibration of path-jet observables.

No Foundation promotion is made.
