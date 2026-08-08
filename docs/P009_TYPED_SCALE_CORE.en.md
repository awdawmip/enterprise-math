# P009 — Typed scale dynamics core

Status: `PROVED STRUCTURAL RESOLUTION`

## 1. Scale projection is not an endomap on one untyped integer set

P005 defines a typed projection

\[
\pi_{e\to d}:X_e\to X_d,
\qquad
\pi_{e\to d}(m)=m//(e/d)
\]

for `d|e`.

Although every coordinate set can be written using the symbol `N`, the semantic state includes the scale tag. After one projection from `e` to `d`, the result is a state at scale `d`; the original `e -> d` arrow cannot simply be applied again.

Erasing this tag creates a false endomorphism `m -> m//r` and therefore a spurious repeated-division dynamics.

## 2. Tagged state

Use

\[
(d,m),
\qquad d\in\mathbb N_{>0},\ m\in\mathbb N.
\]

Canonical transitions are:

### Strict scale coarsening

For `d|e`, `d<e`,

\[
(e,m)\longrightarrow
\left(d,m//(e/d)\right).
\]

### Same-scale perfect-power collapse

For positive exponent `p`,

\[
(d,m)\longrightarrow(d,C_p(m)).
\]

## 3. P009-T01 — Every strict canonical transition lowers lexicographic rank

Status: `PROVED`

Define

\[
\rho(d,m)=(d,m)
\]

with lexicographic order, scale first.

A strict coarsening lowers the first coordinate. A strict collapse leaves the first coordinate fixed and lowers the second because `C_p(m)<=m`, with strict inequality away from a fixed point.

Therefore every state-changing canonical transition satisfies

\[
\boxed{
\rho(\text{next})<\rho(\text{current}).
}
\]

## 4. P009-T02 — No nontrivial directed cycles

Status: `PROVED`

A directed cycle containing any strict transition would have to return to its original lexicographic rank after a strict decrease, which is impossible.

Hence every directed cycle in the canonical typed system consists only of identity/no-op transitions.

## 5. P009-T03 — Every strict trajectory terminates

Status: `PROVED`

On a finite allowed scale set, strict scale coarsenings can occur only finitely many times because the positive scale factor decreases.

Between scale changes, every strict collapse decreases the natural-number coordinate and therefore can also occur only finitely many times.

So every trajectory with identity stuttering removed is finite.

## 6. Sink states

At a terminal scale tag `d`, suppose the allowed positive collapse exponents are

\[
P_d=\{p_1,\ldots,p_r\}
\]

and let

\[
L_d=\operatorname{lcm}(p_1,\ldots,p_r).
\]

Using the P004 fixed-point result, a sink coordinate is exactly a perfect `L_d`-th power. Thus the sinks at terminal scale `d` are

\[
\{(d,k^{L_d}):k\in\mathbb N\}.
\]

If no collapse operation is required at that scale, every coordinate at that terminal tag is a sink relative to the specified transition family.

## 7. Projection confluence versus mixed confluence

P005 already proves that different projection chains with the same target scale agree:

\[
d\mid e\mid f
\implies
\pi_{e\to d}\pi_{f\to e}=\pi_{f\to d}.
\]

So pure scale projection is path independent to one fixed target.

This does **not** automatically imply that arbitrary collapse/projection interleavings commute. Mixed confluence requires additional interchange theorems.

Thus P009 must separate:

- termination / no cycles — already proved by rank;
- pure projection confluence — inherited from P005;
- unique normal forms for arbitrary mixed schedules — an additional question.

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

It is tempting to conclude that repeated scale projection drives every state to zero.

But the first typed step is

\[
(e,m)\to(d,m//r).
\]

The result belongs to `X_d`, so the same typed `e -> d` arrow is no longer applicable. The universal zero attractor is therefore an artifact of forgetting the scale coordinate.

## 9. Refinement is extra structure

P005 shows that a coarse root coordinate does not determine one unique finer root coordinate. Therefore no canonical state-only inverse

\[
X_d\to X_e
\]

exists for `d<e`.

A model may refine only by adding extra structure, for example:

- retaining the underlying source state and recomputing a finer view;
- choosing a noncanonical lift from the projection fiber.

Such a lift can introduce new path dependence or cycles and must be studied separately.

## 10. Revised status of P009

The canonical collapse+coarsening system is structurally classified at the level of termination and cycles:

- scale tags are part of the state;
- every strict canonical transition decreases lexicographic rank;
- no nontrivial cycle exists;
- every strict trajectory terminates;
- pure projection paths to one target are confluent;
- noncanonical inverse lifts and arbitrary mixed normal forms are additional structures, not part of the minimal system.

The earlier collapse-only asymptotic classification and this typed-scale result are complementary rather than competing descriptions.

## 11. Prior-art discipline

Typed transition systems, well-founded orders, rewriting termination, divisibility posets and projective systems are established mathematics. Enterprise Math does not claim those structures as inventions.

The project-specific correction is semantic: the scale tag is explicit state information, so erasing it creates dynamics that the typed model never contained.
