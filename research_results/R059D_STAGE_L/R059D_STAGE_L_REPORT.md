# R059D Stage L — Equal-L Aligned-Endpoint Branch-Count Collapse

Researcher-ID: `EM-R059D-9C6B2A`  
Taskbook source: `f1b8cacc607373ea38322853fd1a4c9aff986d12`  
Frozen Stage-K head: `fc8abf73f67a5793334905b9863cb5f7d2030d94`  
Owner branch: `research/r059d-stage-l-brc6-endpoint-branch-count-collapse`

## Primary dispositions

`BRC6_EQUAL_L_ENDPOINT_BRANCH_COUNT_COLLAPSE_ESTABLISHED`

`BRC6_ENDPOINT_COUNT_TRUE_STATE_DYNAMICS_ESTABLISHED`

Semantic strength:

`CANONICAL_WITHIN_FROZEN_ENDPOINT_BRANCH_COUNT_COLLAPSE_AXIOMS`

Not promoted:

`BRC6_NATIVE_CANONICALITY = NOT_ESTABLISHED`.

## Equal-L endpoint convention

Every candidate keeps the frozen aligned segment cell count

`L(d)=4`.

The inherited affine continuation coordinates are indexed by continuation cell:

`C_0, C_1, C_2, C_3`.

A four-cell segment has zero-based cell indices `0,1,2,3`; therefore the next aligned endpoint is the fourth cell, index `L-1=3`. Hence there is no off-by-one ambiguity:

`B_d = C_(L-1)^d = C_3^d`.

With

`A_d = O_x[d] + M_x[i,d]`

and

`C_n^d = A_d + n I_x[d]`,

the Stage-L endpoint branch multiplicity is

`B_d = A_d + 3 I_x[d]`.

L is only the common endpoint-evaluation boundary. It never enters candidate comparison.

## Collapse rule

`BRC6_COUNT_MODE(sigma)=d`

iff

`B_d > B_e` for every `e != d`.

If the maximum is tied:

`BRC6_UNRESOLVED_BY_ENDPOINT_BRANCH_COUNT`.

This is evaluator status only, not a seventh channel output.

The rule satisfies exact C6 covariance, common-background invariance, shared strictly-increasing representation invariance, exact tie preservation and winner-increase branch-count monotonicity.

## Stage-K reconciliation

Endpoint vectors and count-mode results:

- `W_ASYM_BASE`: `B=(8,11,14,17,6,20)`, count-mode `5`. Stage-K F1 gave `4`; reverse-lex and endpoint-max give `5`. Historical F2 `theta=(-2,-2,-2,1), MAX` gives `0`.
- `W_CONSENSUS_DOMINANT2`: `B=(8,8,25,8,8,8)`, count-mode `2`; F1/reverse-lex/endpoint-max also `2`.
- `W_FULLY_SYMMETRIC`: `B=(8,8,8,8,8,8)`, exact endpoint tie, unresolved.
- `W_S1_TIE_S2_RESOLVE`: `B=(9,12,15,18,6,21)`, count-mode `5`.
- `W_SIGNATURE_INSUFFICIENT_PAIRS`: `B=(8,8,12,12,7,7)`, maximal tie on channels `2,3`, unresolved.

Thus Stage L intentionally disagrees with F1 on `W_ASYM_BASE`. This is not a failure: the Stage-L positive semantics freezes aligned-endpoint sufficiency and discards arbitrary intermediate-spectrum priority.

## Six-outcome coverage

`W_ASYM_BASE` has unique endpoint-count winner `5`.

Six cyclic relabelings therefore yield

`5,0,1,2,3,4`,

covering all of C6 without six absolute-label cases.

## Hard controls

The Stage-J/Stage-K lexicographic and weighted-spectrum selectors remain historical/negative controls only.

Endpoint MIN is rejected from the positive count-mode orientation. On `W_ASYM_BASE`, endpoint MIN gives channel `4` while endpoint count-mode gives `5`.

Boundary contamination is explicitly detectable. A frozen negative witness with

`A=(10,0,0,0,0,0)`

and

`I=(0,4,0,0,0,0)`

has truncated `C_2=(10,8,0,0,0,0)` with winner `0`, but the correct four-cell endpoint is `C_3=(10,12,0,0,0,0)` with winner `1`. Omitting the fourth cell is therefore `BOUNDARY_CONTAMINATED_ENDPOINT_COUNT`.

## True O/M/I state dynamics

The Stage-K event update is used exactly:

`O_x[d] += 1`

`M_x[i,d] += 1`

`y=T_NODE(x,d)`

`j=T_INGRESS(x,d)`

`I_y[j] += 1`.

Then all six endpoint counts are recomputed from the accumulated exact state.

Starting from frozen `W_ASYM_BASE`:

### Carrier A

48 resolved decisions:

`5,1,3,5,1,3,...`

with relative label difference `2` throughout the frozen window.

Final state digest:

`6e3d78b6d572f1b7bb21ae00a82fa323e7d59d67e25701c9766eac92aead5ed5`.

### Carrier B

48 resolved decisions:

`5,2,5,2,...`

with relative label difference `3`.

Final state digest:

`80975a0fd718ee6ad8db08cb900281655dc54ed6105266a136349e286ea4bdaa`.

### Carrier C

The selector returns channel `5` for 12 resolved decisions, then at decision epoch 12 the endpoint maximum ties and the deterministic trajectory stops unresolved.

Final state digest:

`f9e46004404e95ed3952b5e3840b3ebce6ce276684eb5b50a3255357bea2c64b`.

Repeated channel-label words are not full-state cycles. At each resolved decision:

`TOTAL_O(e)=TOTAL_O(0)+e`.

## Perturbation dynamics

Frozen 96-decision tests use three exact perturbation classes.

First-decision output tables on `W_ASYM_BASE`:

- launch/count token: `[5,5,5,5,5,5]`;
- incidence `I[j]+=1`: `[5,5,5,UNRESOLVED,5,5]`;
- real tagged launch-contribution transfer `j -> j+1`: `[5,5,5,5,5,5]`.

On carriers A/B many count-token and tagged-adjacency perturbations leave the channel projection unchanged through 96 decisions even though the exact full state remains different. Thus identical BRC6 output sequence does not imply identical state.

Carrier C is more sensitive: perturbations can advance or delay the endpoint-count tie epoch.

Exact full-state recoalescence at the same epoch is impossible for the count-token class because `TOTAL_O` has a permanent +1 offset, and impossible for the incidence class because `TOTAL_I` has a permanent +1 offset. For tagged-adjacency perturbations no exact recoalescence occurs in the frozen 96-decision window; no global impossibility theorem is claimed.

Endpoint ties can be created and removed exactly:

- `W_S1_TIE_S2_RESOLVE` with `I[3]+=1` changes the endpoint vector to `(9,12,15,21,6,21)`, creating an exact maximal tie between channels 3 and 5.
- From `W_FULLY_SYMMETRIC`, one count token or one incidence increment can resolve to any of the six labels; a one-step tagged launch-contribution transfer produces outputs `1,2,3,4,5,0`.

## Large-N

The frozen registry contains `N=10^36` and neighboring exact integers.

For a replicated common background:

`A_d(N)=N+A_d(0)`,

so

`B_d(N)=N+B_d(0)`.

The common N cancels exactly from every strict comparison and tie. No huge carrier/history enumeration is performed and no length threshold is searched.

## Interpretation boundary

The endpoint-count collapse rule is canonical only after the Stage-L semantic axiom that the next aligned endpoint branch multiplicity is the sufficient collapse observable.

This does not prove that nature/native BRC6 must use that observable.

Continue:

`BRC6_NATIVE_CANONICALITY = NOT_ESTABLISHED`

`PHYSICAL_DIRECTION_CALIBRATION = NOT_ESTABLISHED`

`PHYSICAL_PROBABILITY_FROM_BRC_COUNTS = NOT_ESTABLISHED`

`PHYSICAL_RIGIDITY_INTERPRETATION = NOT_ESTABLISHED`

`PHYSICAL_ELASTICITY_INTERPRETATION = NOT_ESTABLISHED`

`QUANTUM_BRIDGE = NOT_ESTABLISHED`

## Validation

Deterministic checker:

`30091 / 30091 PASS`

Digest:

`4639b4ac4b5d93a62426a59d493a1dd9787c332ea832f2ded7868ce2467832f0`

Large-N evaluation is symbolic; true-state and perturbation regressions are exact finite integer computations.

`STOP_FOR_DRIVER_REVIEW`.
