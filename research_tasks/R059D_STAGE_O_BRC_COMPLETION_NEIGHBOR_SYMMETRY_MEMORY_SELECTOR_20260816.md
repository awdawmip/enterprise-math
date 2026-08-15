# R059D Stage O — BRC Completion-Neighbor Gate / Symmetry No-Go / Minimal Context Selector

Task-ID: `RS-R059D-STAGE-O-BRC-COMPLETION-NEIGHBOR-SYMMETRY-MEMORY`
Generation: `R059D`
Date: `2026-08-16`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Researcher-ID: `EM-R059D-9C6B2A`
Owner branch: `research/r059d-stage-o-brc-completion-neighbor-symmetry-memory`
Frozen parent: `cacbd211a9811e96f361606d56e66bffdf83bf53`

## 0. Frozen input

Stage N is accepted and immutable.

Consume only its frozen algebraic conclusions:

- `C(n;b)=L+(U-L)b`, `b^2=b`;
- signed collapse residue;
- affine sheet `x+y+z=K`;
- symmetric pre-collapse `(-1/2,+1,-1/2)` only under transverse exchange symmetry;
- coupled bit constraint `b_x+b_z=1` once adjacent completed transverse states are `{-1,0}`;
- exact Boolean constraint-solution-set algebra;
- exact post-credit finite differences;
- straightness toy: after an initial branch is fixed, rank-one continuation requires branch consistency, but the first branch is not identified.

Do not consume Stage-N path-language superseded work.

Project mode: `REFOUND, NOT REJECT`.

## 1. Core problem

Stage N proved that sheet conservation plus integrality alone gives infinitely many transverse decompositions:

`(dx,dy,dz)=(t,1,-1-t)`, `t in Z`.

Exactly two branches arose only after restricting each transverse coordinate to the adjacent completed states `{-1,0}` (or an equivalent single-unit minimality gate).

However the scalar BRC primitive is itself defined between adjacent completed states `L<n<U`.

Stage O must decide whether `{-1,0}` is therefore a direct consequence of the declared completion layer rather than a new ad hoc minimality axiom.

The second core problem is selector identifiability: at the symmetric half-state, can any stateless deterministic local law select one complementary branch without breaking exchange symmetry? If not, identify the minimum explicit context required.

## 2. Stage O-A — Completion-layer algebra

Define an ordered discrete completion set `C` and, for every non-completed `q`, exact neighboring completed states

`PREV_C(q) < q < NEXT_C(q)`

with no completed element strictly between them.

Define the generic completion-neighbor collapse carrier

`COLL_C(q;b)=PREV_C(q)+(NEXT_C(q)-PREV_C(q))*b`, `b^2=b`.

Prove basic translation/scaling/sign covariances only where the completion set transforms accordingly.

Specialize separately:

1. integer completion layer `C=Z`;
2. perfect-square completion layer `C={k^2}` on a declared nonnegative domain;
3. at least one scaled/translated discrete completion layer as a covariance control.

Show exactly:

- for `q=-1/2`, `PREV_Z=-1`, `NEXT_Z=0`;
- for `q=5` in the square completion layer, neighboring completed states are `4,9`.

Do NOT infer a common selector law from this shared binary form.

Required classification:

`ADJACENT_COMPLETED_STATE_GATE_IS_DEFINITIONAL_GIVEN_COMPLETION_LAYER`

or

`ADJACENT_COMPLETED_STATE_GATE_REQUIRES_EXTRA_AXIOM`.

State precisely which.

## 3. Stage O-B — Coordinate completion typing

For the three-axis affine carrier, determine what makes transverse coordinate completion states integer-valued.

Do not use UNIT_PACKET as a coordinate-weight argument.

Allowed sources include the already declared integer coordinate module / vector carrier and an explicitly frozen precision/completion layer.

Test whether `C=Z` for coordinate completion is:

- already inherited from the current integer vector carrier;
- a new but natural precision-layer declaration;
- or not derivable from the existing foundation.

No hidden assumption.

## 4. Stage O-C — Re-derive two branches and D6

Assume only those premises that survived O-A/O-B plus:

- affine conservation `x+y+z=K`;
- one declared elementary recipient coordinate event `dy=+1` (and its coordinate permutations/sign reversals).

Re-derive the transverse completed outputs.

If O-A proves adjacency is definitional, do not retain a separate `minimality` axiom.

Determine whether the exact local transfer set is then

`{e_i-e_j : i!=j}`

with cardinality six.

Classify one of:

- `D6_EMERGES_FROM_AFFINE_PLUS_COMPLETION_NEIGHBOR_PRIMITIVE`;
- `D6_STILL_REQUIRES_EXTRA_LOCAL_MINIMALITY`;
- `D6_NOT_IDENTIFIED`.

Do not hard-code D6 into the derivation.

## 5. Stage O-D — Stateless symmetry no-go theorem

Let `tau` exchange the two transverse coordinates around a recipient axis.

At the symmetric pre-collapse state, the local algebraic input is fixed by `tau`, while the two complementary outputs are exchanged:

`b -> 1-b`.

Prove or refute the following exact no-go statement:

> No deterministic stateless selector from the fully exchange-symmetric local input to a unique Boolean branch can be equivariant under transverse exchange.

In algebraic form, if input `s=tau(s)` and equivariance requires

`f(tau(s)) = 1-f(s)`,

then a Boolean fixed output would require `b=1-b`, impossible.

Audit loopholes carefully:

- set-valued output `{0,1}`;
- randomized/probabilistic output (record only as a separate non-native possibility; do not use as positive solution);
- hidden label ordering;
- coordinate naming bias;
- external/history context.

If proved, freeze:

`STATELESS_EXCHANGE_EQUIVARIANT_UNIQUE_BRC_SELECTOR_IMPOSSIBLE_AT_SYMMETRIC_STATE`.

## 6. Stage O-E — Minimal symmetry-breaking context

Do not invent arbitrary scores.

Introduce candidate context variables one at a time and determine the minimum information needed to make a unique selector possible while retaining covariance.

Priority candidates:

- previous complementary branch bit `h`;
- previous donor/recipient relation;
- ingress/orientation state already available in the frozen relational carrier;
- an exact upstream collapse constraint.

For each candidate, state whether it is sufficient, necessary, redundant, or overpowered for the tested law family.

The preferred first test is one-bit memory only.

## 7. Stage O-F — Straightness as downstream post-credit

Use only the already agreed algebraic straightness criterion:

positions are straight when their displacement vectors generate a rank-one integer submodule.

For repeated fixed-recipient elementary transfers, derive exactly whether straightness requires

`b_{k+1}=b_k`.

If so, interpret this only as downstream credit on continuation:

- it identifies branch persistence;
- it does NOT identify the initial bit.

Test whether one-bit memory `h=b_k` with recurrence

`b_{k+1}=h`

is sufficient and minimal for straight continuation.

Also test coordinate permutation and global inversion covariance.

Do not use Euclidean distance, angle, norm, trig, shortest path, or visual straightness.

## 8. Stage O-G — Selector-family constraint solving

Construct a small symbolic family of context-dependent Boolean selectors

`b_{next}=F(local algebraic signature, context bits)`

without arbitrary real weights.

Impose exact constraints from:

- transverse exchange covariance;
- coordinate permutation covariance;
- sign/global inversion covariance where applicable;
- straightness continuation credit;
- completion-neighbor legality;
- idempotent Boolean typing.

Solve symbolically for the admissible selector family or prove non-identifiability.

Do not brute-force a huge truth table as the theorem mechanism. Tiny truth-table enumeration is allowed only as an oracle against the symbolic derivation.

Required output classification:

- `UNIQUE_CONTEXTUAL_SELECTOR_FAMILY`;
- `FINITE_SELECTOR_EQUIVALENCE_CLASS`;
- `SELECTOR_STILL_NONIDENTIFIED`.

## 9. Stage O-H — Scalar/vector bridge

Return to `5 -> 4 or 9`.

Use the abstract completion-neighbor algebra to separate:

- the completion set that determines the two legal endpoints;
- the selector/context that determines which endpoint is realized;
- coupling constraints that may correlate multiple collapse bits.

Show explicitly what the three-axis result teaches about the scalar case and what it does NOT teach.

Do not claim the scalar selector for 5 has been solved unless independently derived.

## 10. Stage O-I — Large background and precision covariance

Check symbolic backgrounds near `10^36` and at least two completion scales.

Large background is system/coordinate scale only; not length, norm, probability, or selector strength.

## 11. Required artifacts

At minimum freeze:

1. `R059D_STAGE_O_COMPLETION_LAYER_PROTOCOL.json`
2. `R059D_STAGE_O_COORDINATE_COMPLETION_TYPING.json`
3. `R059D_STAGE_O_TWO_BRANCH_D6_REDERIVATION.json`
4. `R059D_STAGE_O_STATELESS_SYMMETRY_NOGO.json`
5. `R059D_STAGE_O_CONTEXT_NECESSITY_LEDGER.json`
6. `R059D_STAGE_O_STRAIGHTNESS_MEMORY_CREDIT.json`
7. `R059D_STAGE_O_CONTEXTUAL_SELECTOR_FAMILY.json`
8. `R059D_STAGE_O_SCALAR_VECTOR_BRIDGE.json`
9. `R059D_STAGE_O_LARGE_BACKGROUND_COVARIANCE.json`
10. `R059D_STAGE_O_TRIVIALITY_LEAKAGE_LEDGER.json`
11. deterministic checker source/output
12. report
13. manifest
14. frozen checkpoint

## 12. Hard negative-result discipline

Do not force a unique selector.

If symmetry proves that unique stateless selection is impossible, preserve the theorem.

If one-bit memory only determines continuation but not initiation, preserve that boundary.

If completion adjacency still needs a new axiom, say so explicitly.

No nearest rounding, endpoint-count argmax, arbitrary reward weights, ML fitting, path-language selection, or physical probability interpretation.

## 13. Stop

After all artifacts and checker are frozen:

`STOP_FOR_DRIVER_REVIEW`.
