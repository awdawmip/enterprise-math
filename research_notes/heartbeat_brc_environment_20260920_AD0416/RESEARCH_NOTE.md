# Heartbeat World BRC: environment control ports and the 64 -> 13 -> 64 boundary

Status: `RESEARCH_CONSTRUCTION / EXECUTED_FINITE_CERTIFICATE / NOT_FOUNDATION`
Date: `2026-09-20`
World: `HEARTBEAT_WORLD`.

## Question and typing

The previous residue-port tool describes information internal to a spatial coordinate fiber. This experiment asks a different question: what if a future heartbeat interaction depends on a finite local environment state? Environment state must not be smuggled into the six spatial coordinates. We therefore extend T0 BRC with a finite typed control port carrying ordinary six-axis EffectHistogram branches. T6 predictive quotient remains the minimization oracle.

For the finite witness, let `e=(e0,...,e5) in {0,1}^6` be a six-channel availability/occupancy mask indexed by the ordered positive native axes in one chosen heartbeat frame. This is deliberately NOT the complete twelve signed-neighbor environment. `R` cyclically relabels the six channels. `J` reverses the cyclic frame as a coordinate comparison; it is not physical time reversal.

Define the orientation-blind observation

`O(e) = (N(e), A(e), P(e))`,

where `N` is occupied-channel count, `A=sum e_i e_(i+1)` counts adjacent occupied pairs on the six-cycle, and `P=sum_{i=0}^2 e_i e_(i+3)` counts opposite occupied pairs.

## Exact 13-class symmetry result

Burnside's lemma gives 13 binary dihedral orbits. Rotation fixed-set counts are `64,2,4,8,4,2`; the three vertex-axis reflections fix 16 masks each and the three edge-axis reflections fix 8 each. Thus `(84+72)/12=13`.

The thirteen canonical orbit representatives have distinct `(N,A,P)` signatures:

| representative | (N,A,P) | orbit size |
|---|---:|---:|
| 000000 | (0,0,0) | 1 |
| 000001 | (1,0,0) | 6 |
| 000011 | (2,1,0) | 6 |
| 000101 | (2,0,0) | 6 |
| 001001 | (2,0,1) | 3 |
| 000111 | (3,2,0) | 6 |
| 001011 | (3,1,1) | 12 |
| 010101 | (3,0,0) | 2 |
| 001111 | (4,3,1) | 6 |
| 010111 | (4,2,1) | 6 |
| 011011 | (4,2,2) | 3 |
| 011111 | (5,4,2) | 6 |
| 111111 | (6,6,3) | 1 |

Therefore this observer is exactly the D6 orbit quotient, not merely a coarse fit. The 64 raw masks reduce to 13 observer classes.

Executing the existing T6 predictive compiler with future actions `{R,J}` gives block profile `(13,13,13,13,13)` and stable block count 13 at depth 0. The reason is structural: both actions remain inside a D6 orbit, so every finite symmetry word preserves the orbit observation.

## Phase-addressed operation restores all 64 distinctions

Add `S0`, which forces the channel in heartbeat slot 0 to occupied. This deliberately names an orientation. T6 then returns block counts

`(13, 32, 52, 63, 64, 64)`

for horizons 0 through 5 and stabilizes at all 64 raw masks at depth 4. Thus the orientation-free quotient is exact only while the allowed future language is symmetry-safe. Once a future operation addresses the heartbeat phase, orbit orientation becomes an active residual.

The same boundary appears in effect-valued BRC. `brc_control_port.py` carries finite control state plus an EffectHistogram. Rotation/reflection packets whose spatial translation depends only on the invariant occupied count parity certify the 13-class partition. A phase-addressed packet whose translation depends on `e0` rejects the 13-class certificate; exact refinement over the packet family returns 64 classes.

## Quotient plus repair coordinate

Every raw mask can be represented as `(orbit, orientation coset)` under D6. The orbit sizes are `1,2,3,6,12`; the repair coordinate is a coset modulo the mask stabilizer, not always a unique group element. This is an exact orbit-stabilizer decomposition. If all declared future operations are D6-invariant, only the orbit class is required by the declared observer. If phase-addressed operations may later occur, the orientation residual must be retained somewhere; it cannot be recreated after erasure.

For a uniform raw mask, the conditional orientation entropy is about 2.548 bits and the orbit-label entropy about 3.452 bits, summing to the original 6 bits. These Shannon values are an information accounting identity for the uniform finite model, not a fixed storage implementation or compression guarantee.

## Reuse resolution and limits

- `predictive_quotient.py`: `REUSE_EXECUTED` for the 64-state finite predictive partitions.
- existing `EffectHistogram`/affine BRC: `REUSE_EXECUTED` inside the control packets.
- residue-port BRC: `REUSE_APPLIED` conceptually but insufficiently typed for non-spatial environment state.
- `brc_control_port.py`: `EXTEND_EXISTING_TOOL`, not a new top-level family.

Local tests pass. The result does not identify physical Cell occupancy dynamics, does not model all twelve signed neighbors, and does not show semantic memory improvement. It establishes a finite exact information boundary: symmetry permits a 64-to-13 environment quotient, while a phase-addressed future can make every one of the 64 states distinguishable again.
