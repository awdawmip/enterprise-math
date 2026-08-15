# R059D Stage J REISSUE — BRC6 Next-Channel Selection Algebra

Researcher-ID: `EM-R059D-4C7E21`  
Taskbook source: `3ca99589c5c3ade32c9cc164cdc3b3c4f6e15b7b`  
Frozen provenance parent: `03650b38df5950b86cb2636db9e43094683b1bc8`  
Owner branch: `research/r059d-stage-j-brc6-next-channel-selection`

## Disposition

`BRC6_PARTIAL_SELECTOR_WITH_EXACT_SYMMETRY_UNRESOLVED_STATES`

A single exact, cyclic-label-equivariant six-channel selector is established on the resolved asymmetric signature domain. Exact states whose entire controller-visible signature retains a nontrivial cyclic stabilizer remain evaluator-unresolved; no seventh BRC output is introduced.

## Semantic correction

`BRC` is retained only as the user-selected symbol. No acronym expansion is introduced.

`C6={0,1,2,3,4,5}` is a set of relational channel labels only.

The frozen segment readout is

`ALIGNED_SEGMENT_CELL_COUNT=L`

with `L=4` on the positive Stage-J registries. Every one of the six candidate aligned segments has the same L. L is absent from every candidate signature, score, comparator, perturbation decision and huge-N selector calculation.

Thus Stage J algebraizes next-channel selection, not length.

## Exact channel signatures

For candidate `d`, the frozen base incidence state supplies exact integers

`I[d], O[d], M[i,d]`.

Define the candidate launch count

`A_d = O[d] + M[i,d]`.

The J-S2 continuation quotient has two exact count states U,V:

`u_0=A_d`
`v_0=I[d]`
`u_(n+1)=u_n+v_n`
`v_(n+1)=v_n`.

Therefore

`C_n^d=u_n=A_d+n I[d]`

for the frozen horizon `n=0,1,2,3`.

The same recurrence is applied to every channel label.

J-S3 records exact visit/support diagnostics; J-S4 records only `RECOALESCENCE COUNT` diagnostics. In the current frozen registry S3/S4 do not add new unique-winner power beyond S2.

## Preferred selector F1

Freeze

`Z_d=(C_0^d,C_1^d,C_2^d,C_3^d)`.

F1 returns the exact unique lexicographic maximum of the six Z_d tuples, in the pre-frozen horizon order.

If there is no unique maximum, the evaluator returns

`BRC6_UNRESOLVED_BY_CURRENT_SIGNATURE`.

That verdict is not in C6.

For the asymmetric base witness:

`A=(5,5,5,5,6,5)`
`I=(1,2,3,4,0,5)`,

so the six spectra are

- 0: `(5,6,7,8)`
- 1: `(5,7,9,11)`
- 2: `(5,8,11,14)`
- 3: `(5,9,13,17)`
- 4: `(6,6,6,6)`
- 5: `(5,10,15,20)`.

Hence

`BRC6(W_ASYM_BASE)=4`.

A second witness has all `C_0=6`; F0 is unresolved there, but F1 resolves it exactly to channel 5 from later continuation counts. Thus the continuation spectrum adds genuine selector information.

A separate witness selects relative class 0, proving same-channel output is legal. Another selects relative class 3; no geometric meaning is assigned to that class.

## Selector-family audit

F0: exact on unique primitive C0 extrema, but partial on ties.

F1: preferred coefficient-free selector.

F2:

`P_theta(Z_d)=sum_{n=0}^3 theta_n C_n^d`

with the pre-frozen integer box `theta_n in {-2,-1,0,1,2}`, excluding the all-zero vector.

All `5^4-1=624` coefficients were exhaustively evaluated.

On the base witness under max polarity:

- unique channel 4: 258 coefficients;
- unique channel 5: 290 coefficients;
- unique channel 0: 22 coefficients;
- remaining coefficients produce exact ties.

The min-polarity distribution has the corresponding exact same count structure under sign reversal.

Therefore F2 demonstrates exact algebraic selectors but no coefficient choice is promoted as uniquely natural.

F3 is the exact pairwise tournament induced by the same F1 lex comparator. On strict tuple orderings it is equivalent to F1; exact ties remain unresolved.

## Cyclic covariance

Let `tau(d)=d+1 mod6` and relabel ingress plus every channel-indexed incidence/count component simultaneously.

The signature construction obeys

`Z_(tau d)(tau sigma)=Z_d(sigma)`.

Because F1 applies one shared label-blind comparator, a unique maximizer d maps to unique maximizer tau(d). Therefore

`BRC6(tau sigma)=tau(BRC6(sigma))`.

No absolute channel number appears in the selector.

## Exact symmetry obstruction

For any equivariant deterministic selector f and any automorphism pi in the stabilizer of sigma,

`f(sigma)=f(pi sigma)=pi f(sigma)`.

Thus the selected channel must be fixed by every stabilizer element.

For any nonzero cyclic translation `tau^t`, `t=1,...,5`, no channel label is fixed.

The symmetric witness has

`I[d]=1`
`O[d]=2`
`M[i,d]=3`

for all six d, giving the same spectrum `(5,6,7,8)` for every candidate.

Therefore it cannot have a unique deterministic equivariant BRC6 value.

Freeze:

`BRC6_UNRESOLVED_BY_CURRENT_SIGNATURE`.

## Six-outcome coverage

The asymmetric base witness has output 4.

Applying `tau^t`, `t=0,...,5`, produces outputs

`4,5,0,1,2,3`,

which is exactly C6.

Freeze:

`BRC6_SIX_OUTCOME_SURJECTIVITY_ON_FROZEN_REGISTRY`.

This coverage follows from one witness plus covariance, not six absolute-label lookup cases.

## Huge-N symbolic test

The large-system family freezes

`A_d(N)=N+a_d`

with

`a=(5,5,5,5,6,5)`

and the same

`I=(1,2,3,4,0,5)`.

Therefore

`C_n^d(N)=N+a_d+n I[d]`.

The exact common N term occurs in every candidate coordinate and cancels from every lexicographic comparison.

Hence for every integer N, and in particular for all 15 frozen probes around `10^36`, the relative output remains 4. All six cyclic relabelings remain covariant.

N is system/tag/packet scale only. L remains 4 for every candidate. No length threshold exists or was searched.

The symmetric huge-N control remains unresolved.

No huge object/history enumeration is used.

## Repeated channel-label dynamics

For the frozen diagnostic update in which the selected channel becomes the next ingress and the normalized signature profile is reused:

Base profile:

`d_(k+1)=d_k+4 mod6`

from `d_0=0` gives

`0,4,2,0,4,2,...`

with minimal period 3 and

`r_k=4`.

Same-channel profile:

`d_(k+1)=d_k`

has period 1.

The S2 tie-resolved profile has relative output 5, giving a six-label cycle.

The fully symmetric profile has no first BRC6 output and iteration stops as unresolved.

These are relational channel-label dynamics only.

## Exact perturbation response

Baseline output is 4.

A single admissible launch-count token `A_j += 1` gives after-outputs

`[0,1,2,3,4,5]`

for relative perturbation classes `j=0,...,5`.

A single local incidence increment `I_j += 1` gives

`[4,4,4,4,4,4]`.

A single tagged adjacency perturbation transferring one launch-count contribution

`j -> j+1 mod6`

gives

`[1,2,3,4,5,0]`.

Thus the perturbation registry contains exact six-way channel response without altering L.

`DELTA_BRC6` means only selected-label change/no-change.

## Boundary and padding

The selector horizon is K=3.

Padding depths 4, 8 and 16 are outside the signature dependency depth and reproduce the identical base spectrum/output 4.

A negative control that injects an extra candidate history inside the decision horizon is classified

`BOUNDARY_CONTAMINATED_BRC6`

and excluded from structural evidence.

## Final interpretation boundary

The Stage-J result is an exact relational/count selector on its resolved signature domain.

It does not establish physical directions or direction probabilities.

Freeze:

`PHYSICAL_DIRECTION_CALIBRATION = NOT_ESTABLISHED`

`PHYSICAL_PROBABILITY_FROM_BRC_COUNTS = NOT_ESTABLISHED`

`PHYSICAL_RIGIDITY_INTERPRETATION = NOT_ESTABLISHED`

`PHYSICAL_ELASTICITY_INTERPRETATION = NOT_ESTABLISHED`

`QUANTUM_BRIDGE = NOT_ESTABLISHED`

`STOP_FOR_DRIVER_REVIEW`
