# Viète G0 bridge correction: the native T11 line-path torsor is not a fixed-radius rotation torsor

Status: `FREE_RESEARCH / EXACT LAYER-AND-RADIUS NO-GO + MINIMAL ORIENTATION-DATUM NARROWING / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Depends on:
- `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`
- `driver_reviews/R059D_STAGE_AT4_S1_DISCRETE_CELL_STATE_CORRECTION_20260817.md`
- `research_notes/VIETE_NATIVE_T11_TORSOR_NO_EUCLIDEAN_BISECTOR_20260903.md`
- `research_notes/VIETE_T11_CHIRALITY_GAUGE_AUTOMORPHISM_OBSTRUCTION_20260903.md`

## 1. Why this correction is necessary

The preceding #1158 notes proved that the realization fiber of the equal-component native line trace

\[
T_{1,1}^{(ij)}
\]

has exactly two representatives

\[
p=\Sigma_O^{(ij)};X_iX_j,
\qquad
q=\Sigma_O^{(ij)};X_jX_i,
\]

and therefore forms a free `C2` torsor under order swap. The quarter-turn root pair is also a free `C2` torsor. This gives an exact **structural** two-branch match.

It is tempting to strengthen that structural match and identify `p,q` themselves with the two physical/native rotation-chirality sheets.

That strengthening is false under the current layer semantics.

## 2. Fixed-radius rotation and line-path realization are different dynamics

Current discrete-rotation semantics requires a rotating fixed-length segment to have one native Cell as its instantaneous state at each trajectory step, with fixed algebraic radius `rho` throughout that rotation trajectory.

The current theory-level ordering is:

`ALGEBRAIC VECTOR LENGTH -> DISCRETE CELL ROTATION TRAJECTORY -> REVERSE/LINE PATH REALIZATION`.

A line/path representative is therefore not automatically a fixed-radius rotation trajectory.

For `T_{1,1}`, the native endpoint length is

\[
L_E(T_{1,1})=\sqrt2.
\]

But the two path representatives have intermediate states after their first primitive letter:

\[
p:\quad C_{ij}(0,0)\to C_{ij}(1,0)\to C_{ij}(1,1),
\]

\[
q:\quad C_{ij}(0,0)\to C_{ij}(0,1)\to C_{ij}(1,1).
\]

The intermediate component lengths are

\[
L_E(1,0)=L_E(0,1)=1,
\]

while the terminal length is

\[
L_E(1,1)=\sqrt2.
\]

Thus neither `p` nor `q` remains on the fixed shell `rho=sqrt(2)`.

Therefore

\[
\boxed{
\{X_iX_j,X_jX_i\}\text{ is a line-realization torsor, not a fixed-}\rho\text{ rotation-trajectory torsor.}
}
\]

## 3. Exact no-go for identifying path order with physical rotation chirality

Suppose one claims that the two concrete native line-path representatives `p,q` are themselves the two opposite-sweep realizations of a rotating segment of fixed radius `sqrt(2)`.

A fixed-radius rotating trajectory must preserve `rho=sqrt(2)` at every instantaneous Cell state by the current rotation typing.

But `p` and `q` each contain an intermediate state of native length `1`.

Contradiction.

Hence

\[
\boxed{
\text{T11 path order cannot be identified with physical fixed-radius rotation chirality as a trajectory identity.}
}
\]

This is stronger than saying that the physical interpretation is merely unproved. The direct trajectory identification is ruled out by the current radius/layer semantics.

## 4. What survives from the T11 torsor result

The previous torsor theorem remains useful, but only at its correct strength.

What survives exactly:

1. the scalar normalized first half-angle is anchored by the trace identity `T_11`;
2. the realization fiber contains exactly two native path representatives;
3. order swap is a free `C2` action on that path fiber;
4. the quarter-root pair is another free `C2` torsor;
5. the two torsors are abstractly equivariantly isomorphic in exactly two ways, differing by global sign gauge.

What is now killed:

`T11_PATH_ORDER = PHYSICAL_ROTATION_CHIRALITY_TRAJECTORY`.

The path-fiber torsor is therefore a **structural branch analogue**, not the native rotation sheet itself.

## 5. Current native rotation semantics already requires an independent orientation datum

The accepted discrete Cell-state correction states that a rotating segment carries sweep/orientation information and that the local state must include enough data to distinguish opposite directed traversals.

Its minimum candidate state is

\[
\boxed{S=(\rho,C,\epsilon)}
\]

where `epsilon` is one of the two local rotation orientations.

It further requires reversal to invert the deterministic transition when such a transition law is claimed:

\[
T_{-\epsilon}=T_\epsilon^{-1}.
\]

Thus #1158 does **not** need to manufacture its odd/oriented datum from radial line-path order. The current rotation layer already says that an orientation/sweep datum is mandatory.

The correct remaining question is how that native `epsilon` maps to the G1 turn-sense involution `S`, not whether the line-path order can replace `epsilon`.

Freeze:

`ROTATION_EPSILON != LINE_PATH_ORDER` unless a separate typed theorem proves a derived relation.

## 6. Absolute sign remains gauge unless extra native structure fixes it

The current rotation correction requires a two-valued local orientation state, but it does not by itself select a globally absolute naming `epsilon=+` versus `epsilon=-` independently of frame convention.

Therefore the previous chirality-gauge theorem remains compatible:

- a relative two-state orientation torsor is necessary;
- global sign naming can remain a `C2` gauge;
- scalar Viète observers are insensitive to this gauge;
- an oriented signed lift requires either a gauge choice or later native odd structure fixing one.

The new no-go only changes **where the torsor lives**:

- not in the radial `T_11` line-path fiber as physical rotation trajectories;
- instead in the dedicated rotation orientation state `epsilon` (or a later proven refinement of it).

## 7. Minimal state versus minimal transition memory

For generic local rotation away from multi-edge/vertex ambiguities, the currently declared minimum candidate is

\[
(\rho,C,\epsilon).
\]

However the same correction explicitly leaves open whether previous-cell or incoming-edge memory is necessary at vertex/multi-edge events.

Therefore #1158 can presently conclude:

### Necessary for any oriented rotation quotient

- fixed radius `rho`;
- current Cell `C`;
- a two-state orientation/sweep torsor `epsilon`.

### Not yet proved sufficient for a deterministic all-event transition/refinement law

At exceptional Cell-boundary events, one may additionally require incoming-edge or previous-Cell memory.

Hence

\[
\boxed{
(\rho,C,\epsilon)\text{ is the current minimum typed orientation state, but not yet a proved globally sufficient transition state.}
}
\]

## 8. Consequence for the Viète half-angle bridge

The native-to-G1 bridge should now be factored as

```text
native fixed-radius rotating state (rho, C, epsilon, optional minimal event memory)
    -> finite relative orientation quotient / torsor
    -> G1 normalized equal-resultant root B
    -> S-even scalar shell (r_n,h_n)
    -> Pi_n
    -> target-free Pi_rot
    -> classical compatibility Pi_rot = pi
```

The exact first scalar half-angle may still be calibrated by the normalized trace `T_11`, but the **orientation sheet** must come from the rotation layer, not from the radial path realization of `T_11`.

This cleanly separates two independent uses of current native line theory:

1. `T_11` trace supplies the scalar `sqrt(2)` normalization anchor;
2. it does not supply physical fixed-radius chirality dynamics.

## 9. Stronger residual frontier

The remaining G0 problem for #1158 has now narrowed to two precise subquestions:

1. **orientation intertwiner** — does the native `epsilon` torsor admit an operation-safe map into the G1 turn-sense torsor such that `epsilon` reversal corresponds to `S`?
2. **refinement sufficiency** — is `(rho,C,epsilon)` sufficient to generate the branchwise normalized equal-resultant refinement, or do exceptional Cell events force one additional incoming-edge/previous-Cell memory field?

A negative answer to (1) would kill the proposed native oriented lift while leaving the scalar G1/G2 Viète reconstruction intact.

A positive answer to (1) but negative answer to (2) would identify the exact minimal extra event-memory needed for a native refinement law.

## 10. Current verdict

This note resolves an ambiguity in the previous #1158 bridge:

\[
\boxed{
\text{T11 is an exact scalar normalization anchor, but its path fiber is not the native fixed-radius chirality carrier.}
}
\]

The odd/oriented datum must remain at the dedicated rotation-state layer already demanded by current Cell semantics.
