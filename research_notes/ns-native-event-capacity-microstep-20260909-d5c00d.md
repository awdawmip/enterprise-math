# Exact current-state microsteps and the complete read-dependency contract

Companion to `ns-native-event-capacity-20260909-d5c00d.md`, event `NS-NATIVE-EVENT-CAPACITY-20260909-D5C00D-13`. Status remains TESTING; no physical-force assertion.

## 1. Precise concurrent-rewrite hypothesis

In the main note's Section1, “read conditions” must cover **all data read to determine both eligibility and output**, not merely an unchanged Boolean guard. The sufficient contract is: write sets are disjoint; executing one rewrite leaves the other rewrite's full read data unchanged; each rewrite depends only on those declared read data. Under these hypotheses the two rewrites produce the same values on their disjoint output sets, and leave every other coordinate unchanged, so they commute.

The weaker guard-only assertion is false. On (a,b), let U(a,b)=(b,b) and V(a,b)=(a,1-b). Their guards are always true and their writes are disjoint, but U(V(0,0))=(1,1) while V(U(0,0))=(0,1). This counterexample is executed. It prevents applying the main note's concurrency statement under an inadequate read contract. None of the capacity, parity, 24-frame, or recurrence proofs uses the weaker assertion.

## 2. An actual microstep function, not only a list of endpoints

`experiments/ns_native_event_tick_d5c00d.py` defines a frozen Router configuration (anchor and incidence template) and a State containing ordered frame, current phase, and the current native position of each token. Its `step` reads only this state. At phase0 it moves each active token to its two-axis intermediate Cell. At phase1 it identifies that token by its current buffer position and retained frame, moves it to the next resource Cell, and rotates the frame. The original start positions or a desired terminal trajectory are not additional inputs.

The executor validates the declared six-distinct-token state family. A changed external configuration is a different system; the same system does not receive a fresh selector each tick. The intermediate buffer positions and inactive resource positions are distinct. The first- and second-phase maps are bijections on their six slots. Thus the phase-tagged executor is an autonomous bijection, and its two-step restriction is exactly the main checker's macro-step.

The 24 frames and 720 token assignments give17,280 boundary states and equally many in-flight states. All34,560 microstates were exercised once, with207,360 individual particle-edge checks. Each particle either waits or takes exactly one signed native unit step. For all24 frame representatives the current-state executor was iterated40 ticks and returned for the first time at tick40, agreeing with the ordinary period proof. The independent macro implementation and microstep executor agree on every boundary token/frame state.

## 3. A scoped observer-loss witness

Two boundary states with identical labelled particle positions but frames (A,B,C,D) and (B,A,C,D) have identical spatial count observations. After one microstep their spatial count L1 difference is10. At the next event boundary both again have the original count pattern. Hence event-boundary stationarity is not microstep stationarity, and boundary spatial counts alone cannot determine intermediate dynamics. This is hidden-state dependence under the declared observation, not an amplification claim for initially identical complete states.

No force, mechanical energy or compensating reservoir is defined from the midpoint's change in position sum. There is still no proof that these path events implement TRIADIC_CLOSURE_E, viscosity, physical f=0, or an NS solution. The added executor closes the software/state-transition obligation for the stated routing example, not the physical constitutive gap.
