# P009 — Typed scale dynamics: termination without generic confluence

Status: `PROVED STRUCTURAL RESOLUTION`

## 1. Correct the state type first

P005 defines, for `d|e`, a scale projection

\[
\pi_{e\to d}:X_e\to X_d,
\qquad
\pi_{e\to d}(m)=m//(e/d).
\]

Although every coordinate carrier can be written as `N`, the semantic state is not an untyped integer. It is a tagged state

\[
(d,m),
\qquad d\in\mathbb N_{>0},\ m\in\mathbb N.
\]

After one projection from scale `e` to scale `d`, the state lives in `X_d`; the original `e -> d` arrow cannot simply be applied again. Erasing the scale tag manufactures a false endomorphism and false repeated-division dynamics.

## 2. Canonical transitions

The minimal collapse+coarsening system has two transition families.

### Strict scale coarsening

For `d|e` and `d<e`,

\[
(e,m)\longrightarrow
\left(d,m//(e/d)\right).
\]

### Same-scale perfect-power collapse

For a positive exponent `p`,

\[
(d,m)\longrightarrow(d,C_p(m)).
\]

A collapse transition is strict only when `C_p(m)<m`.

Refinement arrows are **not** part of this minimal system, because P005 proves that a coarse root coordinate has no canonical state-only inverse lift.

## 3. P009-T01 — Every strict canonical transition lowers lexicographic rank

Status: `PROVED`

Define

\[
\rho(d,m)=(d,m)
\]

with lexicographic order, scale first.

A strict coarsening lowers the positive scale coordinate. A strict collapse leaves the scale coordinate fixed and lowers the natural-number coordinate. Therefore

\[
\boxed{\rho(\text{next})<\rho(\text{current})}
\]

for every state-changing canonical transition.

## 4. P009-T02 — No nontrivial directed cycle exists

Status: `PROVED`

A directed cycle containing a strict transition would have to return to its starting rank after a strict decrease. This is impossible.

Hence every directed cycle in the canonical typed system consists only of identity/no-op transitions.

## 5. P009-T03 — Every strict trajectory terminates

Status: `PROVED`

No finiteness assumption on a global scale universe is needed.

Starting from one finite positive scale factor `d`, strict coarsening can lower the first coordinate only finitely many times. Once the scale coordinate stops changing, every strict collapse lowers the natural-number coordinate and therefore can occur only finitely many times.

Equivalently, the lexicographic order on

\[
\mathbb N_{>0}\times\mathbb N
\]

is well founded for this downward transition system.

Thus every trajectory with identity stuttering removed is finite.

## 6. P009-T04 — Sink coordinates at a terminal scale

Status: `PROVED`

Fix a terminal scale tag `d` and a finite nonempty set of allowed positive collapse exponents

\[
P_d=\{p_1,\ldots,p_r\}.
\]

Let

\[
L_d=\operatorname{lcm}(p_1,\ldots,p_r).
\]

Then a coordinate `m` is fixed by every allowed collapse if and only if it is a perfect `L_d`-th power:

\[
\boxed{
C_{p_i}(m)=m\ \forall i
\iff
m=k^{L_d}\text{ for some }k\in\mathbb N.
}
\]

### Proof

If `m=k^{L_d}`, then every `p_i` divides `L_d`, so `m` is a perfect `p_i`-th power and is fixed by every `C_{p_i}`.

Conversely, suppose `m` is fixed by every `C_{p_i}`. By the perfect-power fixed-point characterization, `m` is a perfect `p_i`-th power for every `i`. For `m>0`, write its prime factorization. Every prime exponent is divisible by every `p_i`, hence by their least common multiple `L_d`; therefore `m` is a perfect `L_d`-th power. The states `0` and `1` satisfy the same conclusion directly. ∎

If no collapse operation is required at a terminal scale, every coordinate there is a sink relative to the specified transition family.

## 7. P009-T05 — Pure projection is confluent to a fixed target

Status: `PROVED`

P005 gives, for

\[
d\mid e\mid f,
\]

\[
\boxed{
\pi_{e\to d}\circ\pi_{f\to e}
=
\pi_{f\to d}.
}
\]

Thus every pure projection chain ending at the same target scale has the same result.

This is path independence of the typed scale subsystem.

## 8. P009-C01 — Type erasure manufactures a false zero attractor

Status: `COUNTEREXAMPLE / DESIGN WARNING`

Erase the scale tag and treat a fixed ratio `r>1` as an endomap

\[
Q_r(m)=m//r.
\]

Then

\[
Q_r^t(m)=m//r^t
\]

eventually reaches zero.

But the actual typed step is

\[
(e,m)\to(d,m//r),
\]

and the result belongs to `X_d`. Reapplying the same `e -> d` arrow is ill typed. The universal zero attractor therefore belongs to the type-erased surrogate, not to the original scale system.

## 9. P009-C02 — Collapse/coarsening is not generically confluent

Status: `COUNTEREXAMPLE`

Take the tagged state

\[
(2,3),
\]

allow square collapse `C_2`, and coarsen from scale `2` to scale `1`.

Collapse first:

\[
(2,3)\to(2,C_2(3))=(2,1)\to(1,0).
\]

Project first:

\[
(2,3)\to(1,3//2)=(1,1)\to(1,C_2(1))=(1,1).
\]

Therefore

\[
\boxed{(1,0)\ne(1,1).}
\]

Both terminal coordinates are square-collapse fixed points. Hence the canonical typed system is terminating but **not confluent under arbitrary mixed collapse/projection schedules**.

A unique mixed normal form requires an additional scheduling convention or a specific interchange theorem; it does not follow from termination alone.

## 10. Refinement remains extra structure

P005 proves that a coarse root coordinate does not uniquely determine one finer root coordinate. Therefore no canonical state-only inverse

\[
X_d\to X_e
\]

exists in general for `d<e`.

A model may add refinement only by adding extra represented information, for example by retaining an underlying source state and recomputing a finer view, or by explicitly choosing a noncanonical lift from a projection fiber.

Such added lift arrows define a different dynamical system and may introduce new cycles or path dependence. They must be analyzed separately.

## 11. Structural classification

For the minimal typed collapse+coarsening system:

- the scale tag is explicit state information;
- every strict canonical transition decreases a well-founded lexicographic rank;
- every strict trajectory terminates;
- no nontrivial directed cycle exists;
- terminal sink coordinates for a finite exponent family are exactly perfect `lcm`-power states;
- pure projections to a fixed target are confluent;
- arbitrary collapse/projection interleavings are not confluent in general;
- inverse refinement is not canonical and is outside the minimal system.

So the corrected P009 picture is not “one semigroup of untyped integer endomaps.” It is a typed directed rewriting system that is strongly normalizing but generically nonconfluent.

## 12. Prior-art discipline

Typed transition systems, well-founded orders, rewriting termination/confluence, divisibility posets, projective systems, prime factorization, and lcm fixed-point intersections are established mathematics.

Enterprise Math does not claim these structures as inventions. The project-specific correction is semantic: precision/scale tags remain explicit state data, and deleting those tags changes the dynamical system being studied.
