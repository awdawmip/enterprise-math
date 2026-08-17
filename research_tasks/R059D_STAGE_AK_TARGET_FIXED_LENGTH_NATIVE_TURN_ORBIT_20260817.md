# R059D Stage AK — Target Fixed-Length Native Turn-Orbit Certification

Task-ID: `RS-R059D-STAGE-AK-TARGET-FIXED-LENGTH-NATIVE-TURN-ORBIT`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

Identity policy: `AUTO_RESOLVE_OR_ALLOCATE`

## Frozen inputs

Read-only accepted inputs:

1. Stage AG all-radius N Beatty/Sturmian jump theorem;
2. Stage AH all-radius autonomous N Motzkin-word / D6 circle generator;
3. Stage AI algebraic Enterprise circle constant theorem `kappa_E^2=12`, `kappa_E>0`;
4. Stage AJ uniform N/C_s one-layer phase theorem and resolver-robust `kappa_E`;
5. canonical Enterprise circle semantics already frozen at project level:

> circle = complete closed turning orbit of the free endpoint of a fixed-length segment with the other endpoint fixed.

Do not modify any prior-stage result file.

## Driver working truth

Treat the following as the theorem to prove, not as a neutral possibility:

> The autonomous integer N-circle obtained in AH is already the target-side realization of the Enterprise primitive circle. The missing work is semantic/formal: expose the hidden segment state and one-step legal turn operator, prove the radius/length class is preserved by every turn, and prove that the complete endpoint orbit is exactly the accepted D6 boundary.

The target-side notion of equal length is **not** Euclidean equal-distance. It is an Enterprise segment-state equivalence preserved by legal translation and legal turn transport.

Stage AK must upgrade the old status

`SOURCE_LENGTH_COMPATIBLE`

to

`TARGET_FIXED_LENGTH_PROVED`

for the accepted autonomous N orbit.

## Hard target

Prove:

`TARGET_FIXED_LENGTH_NATIVE_TURN_ORBIT_THEOREM_PROVED`.

At minimum construct a target-side state space `SEG_E`, an integer local turn operator `tau`, and a length-class map/equivalence such that for every integer `r>=1` and center `O`:

1. an anchor segment state `S_r(O)` has fixed endpoint `O` and free endpoint `O+(r,0)`;
2. `tau` advances by one legal Enterprise boundary move using constant-size integer state;
3. `L_E(tau(S))=L_E(S)=r` for every state in the orbit;
4. the free endpoint orbit is exactly the AH N D6 boundary;
5. the orbit closes after exactly `C_N(r)` turns and has no smaller positive period;
6. translation of both endpoints commutes with `tau`;
7. D6 rotation/sign transport conjugates the same turn law rather than creating six unrelated rules;
8. the runtime and target definitions use no source-circle query, Euclidean distance/equidistance, source `Q`, pi, sqrt, floating point, trigonometry, occupancy table, word table or radius-specific tuning.

If a single radius-uniform one-step state machine cannot be produced from the accepted AH state, exhibit the precise obstruction before weakening the theorem.

## Stage 0 — target semantic freeze

Before coding or replay, define the target segment state explicitly.

Preferred shape:

`S=(O, r, sector, local_state, turn_phase)`

where `local_state` contains only the constant number of integers needed to advance the AH boundary locally, e.g. coordinates/residual/branch phase derived from `(a,b,rho)`.

The endpoint projection

`endpoint : SEG_E -> Enterprise coordinate state`

must be explicit.

Freeze three distinct notions:

- `SEGMENT_STATE`: the full target state;
- `ENDPOINT_STATE`: its coordinate projection;
- `ENTERPRISE_LENGTH_CLASS`: the invariant carried by the segment state.

Do not require endpoint coordinates alone to recover the entire segment state unless that is actually proved.

Required output:

`R059D_STAGE_AK_TARGET_SEGMENT_SEMANTICS.json`.

## Stage A — derive a one-step turn machine

AH generates the full first-sector word using a constant-size residual state and reflection. AK must expose this as a true one-step dynamics.

Construct a radius-uniform local operator

`tau : SEG_E -> SEG_E`

such that one application emits exactly one legal boundary edge.

The machine must handle:

- left-half AH residual evolution;
- the possible center symbol;
- reflected right-half evolution without storing the whole left-half word;
- sector transition;
- six-sector D6 completion;
- return to the canonical anchor state.

A generator that recomputes the entire word from radius at every step is not a local turn operator and does not satisfy the hard target.

A constant number of integer registers is preferred. If extra finite-control bits are needed, type them explicitly.

Required output:

`R059D_STAGE_AK_LOCAL_TURN_MACHINE.json`.

## Stage B — Enterprise equal-length relation

Define target equal length operationally on segment states.

Preferred formulation:

Two target segment states are `ENTERPRISE_EQUAL_LENGTH` iff, after possibly translating their fixed endpoints to a common origin, they lie in the same legal-turn orbit class generated from the same radius anchor.

The scalar/class label `r` may be retained as a conserved integer invariant, but Stage AK must prove this is not an arbitrary decoration:

- translations do not change `r`;
- every legal turn preserves `r`;
- different anchor classes `r!=r'` remain disjoint as segment-state classes;
- every state generated from the radius-r anchor belongs to the same equal-length class;
- every state admitted into the radius-r target orbit is reachable by legal turns from the anchor.

Do **not** define equal length by `Q(P-O)=r^2`, Euclidean norm, classical distance to the center, or the source teacher.

Required output:

`R059D_STAGE_AK_ENTERPRISE_LENGTH_CLASS_THEOREM.json`.

## Stage C — fixed-center turn orbit theorem

For fixed center `O`, define

`C_E^N(O,r) := { endpoint(tau^k(S_r(O))) : k>=0 }`.

Prove:

- `O` remains fixed;
- every step is one legal target adjacency move;
- all segment states remain `ENTERPRISE_EQUAL_LENGTH` to `S_r(O)`;
- the endpoint sequence is connected and closed;
- the endpoint set/path equals exactly the accepted AH full D6 boundary for radius `r`;
- for `r>0`, no endpoint repeats before full closure except the final return to the anchor.

This is the semantic upgrade from a generated digital boundary to a native Enterprise circle orbit.

Required output:

`R059D_STAGE_AK_FIXED_LENGTH_TURN_ORBIT_THEOREM.json`.

## Stage D — exact period / circumference theorem

Prove the minimal positive period of the segment-state turn orbit is exactly

`T_r=C_N(r)=6*(r+J_N(r))`.

Hence circumference is not introduced by an external formula; it is the number of elementary legal turns required to close one full fixed-length orbit.

Combine with accepted AG/AI to retain:

`C_N(r)=6*(r+floor(alpha*r+1/3))`

and

`lim T_r/(2r)=kappa_E`,

`kappa_E^2=12`, `kappa_E>0`.

The theorem should explicitly distinguish:

- `TURN_PERIOD`;
- `BOUNDARY_EDGE_COUNT`;
- `CIRCUMFERENCE_COUNT`.

Prove their equality in the accepted target dynamics rather than treating it as notation.

Required output:

`R059D_STAGE_AK_PERIOD_CIRCUMFERENCE_THEOREM.json`.

## Stage E — covariance and symmetry

Prove the target dynamics is geometric rather than tied to one origin/chart.

### Translation covariance

For every Enterprise translation `t`:

`tau(t.S)=t.tau(S)`

with the fixed endpoint and free endpoint translated together.

### D6 covariance

For the accepted rotation

`R(a,b)=(-b,a+b)`,

prove the turn dynamics is conjugate under D6 transport.

The six sectors must therefore be six transported copies of one law, not six separately tuned machines.

Also audit global sign inversion/reversal compatibility.

Required output:

`R059D_STAGE_AK_TURN_COVARIANCE_AUDIT.json`.

## Stage F — state minimality diagnostic

AH proved only that a constant-size auxiliary state is sufficient and that scalar `J` alone is insufficient.

AK should test, but need not fully solve, the minimal-state question.

At minimum determine whether the one-step turn machine can be expressed with:

- radius `r`;
- current endpoint/local coordinates;
- one signed residual integer;
- finite phase/sector bits;

without storing an unbounded prefix/history.

If a smaller state is impossible, provide explicit collision/counterexample witnesses showing two geometrically different next turns share the proposed reduced state.

This stage is diagnostic only and must not block the main theorem once a constant-size local state is proved sufficient.

Required output:

`R059D_STAGE_AK_STATE_MINIMALITY_DIAGNOSTIC.json`.

## Stage G — N/C_s phase compatibility

AJ proved every `C_s` is at most one shell behind N and shares the same `kappa_E`.

Do not force C_s to have the identical pointwise orbit.

Instead test whether the AJ phase bit can be interpreted as a finite-precision readout delay of the same radius/length class.

Allowed successful result:

`C_s = bounded phase/readout perturbation of the same target fixed-length class`.

This is secondary. Failure does not invalidate the N target fixed-length theorem.

Do not use C_s to redefine the N turn law.

Required output:

`R059D_STAGE_AK_C_PHASE_COMPATIBILITY_AUDIT.json`.

## Stage H — deterministic checker

After theorem statements and turn-machine code are frozen, run independent deterministic replay.

Minimum mandatory checks:

- all `r=1..4096`;
- checkpoints `8192,16384`;
- exact equality of one-step endpoint orbit with AH full boundary;
- exact period `C_N(r)`;
- no early return/repeated endpoint for `r>0`;
- all steps legal adjacency moves;
- D6 closure and rotation covariance;
- translation covariance on deterministic nonzero translation vectors;
- length-class invariant never changes;
- source/runtime firewall scan.

Finite replay validates the implementation of the symbolic theorem; it is not the theorem itself.

## Required artifacts

- `R059D_STAGE_AK_TARGET_SEGMENT_SEMANTICS.json`
- `R059D_STAGE_AK_LOCAL_TURN_MACHINE.json`
- `R059D_STAGE_AK_ENTERPRISE_LENGTH_CLASS_THEOREM.json`
- `R059D_STAGE_AK_FIXED_LENGTH_TURN_ORBIT_THEOREM.json`
- `R059D_STAGE_AK_PERIOD_CIRCUMFERENCE_THEOREM.json`
- `R059D_STAGE_AK_TURN_COVARIANCE_AUDIT.json`
- `R059D_STAGE_AK_STATE_MINIMALITY_DIAGNOSTIC.json`
- `R059D_STAGE_AK_C_PHASE_COMPATIBILITY_AUDIT.json`
- `R059D_STAGE_AK_PROOF.md`
- `R059D_STAGE_AK_DETERMINISTIC_CHECKER_OUTPUT.json`
- `R059D_STAGE_AK_FROZEN_CHECKPOINT.json`
- `R059D_STAGE_AK_REPORT.md`

## Mandatory semantic firewalls

The target Enterprise circle is defined by the fixed-length segment-state turn orbit, not by classical equal-distance from a center.

Forbidden as native premises or runtime dependencies:

- `distance(P,O)=r` in a Euclidean/orthogonal metric;
- the source circle equation;
- source `Q` lookup or occupancy query;
- classical pi/circumference formula;
- trig/angle lookup;
- floating point or sqrt;
- precomputed full word/boundary tables;
- radius-specific tuning.

Accepted prior theorems may be cited to prove comparison/equality with the already frozen AH boundary, but they must not be silently reintroduced as the **definition** of the target length class or turn law.

## Research discipline

Internal working truth:

`THE_AUTONOMOUS_ENTERPRISE_CIRCLE_IS_A_FIXED_LENGTH_NATIVE_TURN_ORBIT`.

Attack the proof, not the direction. A route may be rejected only by exact counterexample, formal contradiction, frozen checker failure, or Driver/user supersession.

Do not weaken `TARGET_FIXED_LENGTH` back to `SOURCE_LENGTH_COMPATIBLE` merely because standard geometry uses a different primitive circle definition.

## Dispositions

Use the strongest justified terminal status:

1. `TARGET_FIXED_LENGTH_NATIVE_TURN_ORBIT_THEOREM_PROVED__KAPPA_NATIVE_CIRCLE_CONSTANT`
2. `TARGET_FIXED_LENGTH_TURN_ORBIT_PROVED__PERIOD_MINIMALITY_OPEN`
3. `LOCAL_TURN_ORBIT_PROVED__LENGTH_CLASS_SEPARATION_OPEN`
4. `CONSTANT_SIZE_TURN_MACHINE_PROVED__TARGET_LENGTH_SEMANTICS_OPEN`
5. `TARGET_FIXED_LENGTH_ROUTE_BLOCKED__EXACT_COUNTEREXAMPLE`
6. `FINITE_REPLAY_ONLY__NO_TARGET_THEOREM`

Do not stop at a weaker disposition while a stronger theorem route remains untested.

`STOP_FOR_DRIVER_REVIEW` only after the strongest reachable target-side theorem and all firewalls are frozen.
