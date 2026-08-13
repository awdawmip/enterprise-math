# R053 Foundation Packet — Triangular-Packing Pi-Supervised Boundary Collapse

Status: `FROZEN PROBLEM PACKET / NEW MOTHER QUESTION / NOT CANONICAL`

## Core hypothesis

This task intentionally uses the traditional Euclidean constant `π` as a **teacher / supervision signal**.

The goal is not to derive classical π without seeing it. The goal is to discover a compact local collapse algebra on a two-dimensional densest crystal packing whose macroscopic perimeter readout reproduces classical circular circumference as closely and as stably as possible across scale and lattice phase.

The intended causal direction is:

`classical circular success -> credit assignment over local crystal-boundary collapses -> frozen local collapse algebra -> native circumference/tangent readout on new crystal clusters`.

This is calibration/inverse reconstruction, not foundational proof of π.

## Teacher / student separation

### Teacher surface

The teacher is the ordinary Euclidean plane. It may use:

- Euclidean point coordinates;
- Euclidean circle, center, radius and diameter;
- the classical symbolic constant `π`;
- classical circumference target `2πR`;
- Euclidean tangent direction for **post-policy validation**.

Traditional π is therefore explicitly allowed and expected in the training loss.

### Student surface

The student is a fixed two-dimensional densest equal-cell packing.

Use the triangular lattice of crystal centers

`Λ = {a e1 + b e2 : a,b in Z}`

with

`e1=(1,0)`, `e2=(1/2, sqrt(3)/2)`

in normalized center-spacing units. Equivalently use Eisenstein/axial integer coordinates. Exact squared norm is

`Q(a,b)=a^2 + ab + b^2`.

The crystal package attached to each lattice center is its regular hexagonal Voronoi cell. Nearest-neighbor center spacing is one normalized cell scale; the physical scale may later be restored by a symbolic factor `ell_0`.

The student inference rule, once frozen, must use only:

- local crystal/cell adjacency;
- exposed boundary edges;
- a finite local microcluster neighborhood;
- the frozen collapse grammar/policy;
- exact algebraic geometry of local lattice anchors.

After freeze, student inference must not call `π`, circle center, teacher radius, or a radius-specific parameter.

## Discrete teacher-circle realization

For a teacher circle of center phase `c` and normalized radius `R`, define the primary crystal cluster by center inclusion:

`C(R,c) = union of Voronoi cells H_lambda with ||lambda-c|| <= R`.

Ties are included by `<=`.

The exposed hex-cell boundary of `C(R,c)` is the raw crystal boundary. It is a cyclic word in six lattice edge directions, together with the adjacent boundary-cell patch.

Center phase matters. `c` must be varied over a deterministic finite set in a fundamental lattice cell so that the collapse law is not fitted only to a specially centered circle.

## What is a microcluster collapse?

A boundary microcluster is a bounded local patch around consecutive exposed boundary edges/cells. A candidate collapse mode replaces that local patch by one exact effective segment or short effective chain determined from local algebraic anchor points.

Allowed local anchors may include, when declared and frozen:

- exposed hex-boundary vertices;
- exposed-edge midpoints;
- boundary-cell centers;
- cell-contact points;
- other finite affine/algebraic anchors definable solely from the local crystal patch.

A collapse mode must return at least:

- exact effective segment vector(s);
- exact/algebraic effective length;
- an effective unoriented or oriented tangent-direction class;
- its consumed raw boundary support;
- composability/non-overlap conditions.

A collapse output may live in an exact algebraic number field such as `Q(sqrt(3), sqrt(q1),...)`; it may not contain a free real parameter chosen to equal π or a multiple of π.

Different collapse modes of the same local patch are intentionally allowed. Classical π will assign credit among them.

## Credit assignment principle

Let a frozen local collapse policy `kappa` parse the whole raw boundary into non-overlapping local collapses and produce a perimeter

`P_kappa(R,c)`.

The primary supervised target is

`P_teacher(R)=2πR`.

The primary scale-normalized loss is based on

`pi_kappa(R,c)=P_kappa(R,c)/(2R)`

and its deviation from classical `π`.

The exact loss aggregation and construction/holdout split must be frozen before candidate policy fitting.

Credit is local but judged globally: a local collapse mode receives positive or negative credit according to its reproducible marginal contribution to reducing the global circumference/π residual across many teacher circles, scales and center phases.

No direct classical tangent label is required during training. The tangent direction should be inferred from the winning local collapse geometry. Classical tangent comparison is a post-freeze validation surface.

## Required invariances of a serious learned rule

A serious rule should be tested for:

- translation equivariance;
- 60-degree lattice rotation equivariance;
- reflection behavior, if orientation is not part of the student state;
- cyclic-start invariance of a closed boundary parse;
- no overlap/double counting;
- radius independence;
- center-phase generalization;
- scale transfer;
- deterministic inference after freeze.

If these fail, preserve the failure rather than hiding it.

## Circumference after training

If a policy is frozen, define the Enterprise-Math crystal circumference readout by

`Per_EM(C) := total effective length produced by the frozen collapse policy on the exposed crystal boundary of C`.

For teacher circles this gives the scale-dependent readout

`pi_EM(R,c) := Per_EM(C(R,c))/(2R)`.

Finite-scale values are not required to equal one another. A major downstream object is the scale/phase oscillation envelope around classical π.

## Tangent after training

For every accepted local collapse, its exact effective segment vector defines an effective local tangent direction. Assemble these into a boundary tangent field.

Only after the policy is frozen, compare this inferred field against the classical Euclidean circle tangent field. This validation asks whether a collapse rule trained only by global circumference/π credit also recovers the local ideal tangency direction.

## Scale and precision horizon

Keep the physical cell scale symbolic:

`R_physical = R * ell_0`.

Do not assume a currently known minimum universe-cell size.

For the frozen policy study the finite-scale residual

`epsilon(R,c)=pi_EM(R,c)-π`

and suitable phase envelopes. Separate:

- exact theorems;
- bounded exhaustive computation;
- empirical asymptotic fits/conjectures.

A precision horizon may be reported only with its scope explicit: theorem-level if proven, otherwise bounded-computation/empirical.

## Non-goals

This task is not:

- a proof that the universe is a triangular lattice;
- a proof that a minimum physical cell size is known;
- a blind derivation of π;
- a requirement that finite-radius π values be identical;
- permission to hard-code π into the frozen inference rule;
- permission to fit one independent rule per radius or per center phase;
- permission to define circumference as `2πR` on the student side after training.

## Desired research outcome

The desired success is a compact algebraic statement of the form:

`local crystal boundary type -> credited collapse mode -> effective length + effective tangent direction`

such that one fixed frozen policy:

1. approximates `2πR` well over construction circles;
2. transfers to held-out radii and held-out center phases without refitting;
3. defines a standalone student-side circumference readout;
4. yields a local tangent field that can be compared with the classical ideal tangent only after freeze;
5. exposes how `pi_EM(R,c)` oscillates and stabilizes with increasing `R/ell_0`.
