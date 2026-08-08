# P019 — Causal Role / Direction Bridge, Supplement 09

Status: `ACTIVE RESEARCH NOTE / STRUCTURAL BRIDGE`
Depends on: P019 causal boundary, phase/magnitude correction, Directional Focusing Supplement 08
Discipline: causal phase-transition roles are not geometric tangent/normal directions and direction orbits are not physical shear modes without further derivation.

## 1. Purpose

Stage 08 showed that intrinsic directions can be represented by outgoing-incidence orbits of automorphisms preserving the justified marked causal structure. The next question is whether the already-existing phase/boundary layer actually supplies useful marks rather than merely promising that it might.

The answer is yes, with an important distinction:

- causal phase transitions define **coarse causal roles**;
- marked automorphism orbits define **intrinsic direction classes**;
- one causal role may contain multiple direction classes.

Thus role and direction must not be collapsed into one concept.

## 2. Exact causal phase role

For a directed primitive incidence `e=(u,v)` and phase field

`phi:V->{-1,0,+1}`,

define

`role_phi(e)=(phi(u),phi(v))`.

This gives at most nine exact transition roles. Examples include

- `(+,+)` phase-preserving positive incidence;
- `(-,-)` phase-preserving negative incidence;
- `(+,-)` or `(-,+)` opposite-phase crossing incidence;
- roles involving `0`, which touch the exact zero-phase boundary state.

No radius, Euclidean normal vector, coordinate chart, or angle is required.

## 3. P019-ROLE-T01 — Phase-preserving automorphism orbits refine causal roles

Status: `PROVED`.

Let the direction orbits be computed using graph automorphisms that preserve the phase marks. If two incidences lie in the same orbit, their sources have equal phase and their targets have equal phase. Therefore every marked direction orbit lies entirely inside one exact causal role.

Symbolically, the orbit partition refines the phase-role partition.

This is useful because it proves that causal phase is a legitimate source of direction refinement without importing an external axis.

## 4. P019-ROLE-N01 — Causal role is not a complete direction invariant

Status: `COUNTEREXAMPLE / NECESSITY RESULT`.

Take the five-vertex graph

`a->x, b->y, a->z, b->z`

with current section `{a,b}` and assign phase `0` to every vertex. Every outgoing incidence therefore has the same causal role `(0,0)`.

Nevertheless the section-preserving graph automorphism structure yields two incidence orbits:

- private-future orbit `{a->x,b->y}`;
- common-future orbit `{a->z,b->z}`.

Hence

`same causal role != same intrinsic direction orbit`.

Causal role is therefore a coarse mark, not a substitute for automorphism-resolved direction.

## 5. P019-ROLE-T02 — Phase marks can break an otherwise transitive direction orbit

Status: `PROVED BY FINITE EXAMPLE`.

For the unmarked graph

`a->x, b->y`

with section `{a,b}`, the two incidences form one orbit because the graph admits the swap `a<->b, x<->y`.

Now give the sources phase `0`, but assign

`phi(x)=+1`, `phi(y)=-1`.

Any phase-preserving automorphism can no longer exchange `x` and `y`, so the single unmarked orbit splits into two marked direction orbits with causal roles `(0,+1)` and `(0,-1)`.

Thus the existing causal phase field can create genuine intrinsic directional resolution.

## 6. What may and may not be called horizon crossing

An incidence with endpoint phases `(+,-)` or `(-,+)` is an exact opposite-phase transition in the discrete phase field. It is safe to call this an **opposite-phase crossing role**.

It is not yet safe to call every other role “tangent to the horizon.” Tangency requires additional local geometry or boundary-incidence structure. A same-phase edge can be far from the boundary, and a `0->0` incidence can lie within a zero-phase substructure without defining a continuum tangent direction.

Therefore Stage 09 deliberately stops at causal roles.

## 7. Combined hierarchy after Stage 09

The compact hierarchy is now

`marked primitive causal graph`

`-> phase/boundary complex`

`-> causal phase-transition roles`

`-> marked automorphism direction orbits`

`-> per-orbit C and J_k + cross-orbit overlap`

`-> anisotropy diagnostics`.

The role partition is coarser than or equal to the direction-orbit partition whenever the automorphism group preserves phase marks.

## 8. Consequence for the shear comparison gate

Stage 09 removes one ambiguity but does not complete a shear theory.

What is now justified:

- phase/boundary data can supply intrinsic marks;
- those marks can refine graph-symmetry direction classes;
- resolved direction classes can carry the existing integer focusing spectrum.

What is still missing:

- a derivation identifying any direction class as physical transverse/tangent direction;
- an evolution law for directional anisotropy comparable to continuum shear;
- a physical calibration of graph steps/sections to a spacetime congruence.

Therefore the next useful theorem should concern **stability of the marked direction partition under one-step causal evolution**, not another static scalar.

Executable reference:

- `src/enterprise_math/directional_focusing.py`
- `tests/test_directional_focusing.py`
