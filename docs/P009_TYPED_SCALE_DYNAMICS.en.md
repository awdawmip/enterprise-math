# P009 Supplement — Typed scale dynamics and termination

Status: `PROVED STRUCTURAL COMPLETION`  
Parent: `P009`  
Dependency: `P005`

## 1. Why raw integer scale maps create a false semigroup

P005 defines total scale factors \(d\in\mathbb N_{>0}\) and canonical projection

\[
\pi_{e\to d}(m)=m\operatorname{//}(e/d)
\qquad(d\mid e).
\]

The carrier of the root coordinate at every scale can be written using the same symbol \(\mathbb N\). But the semantic types are different:

\[
m\in X_e
\quad\longrightarrow\quad
\pi_{e\to d}(m)\in X_d.
\]

Erasing the scale tags turns this typed map into an apparent endomap \(\mathbb N\to\mathbb N\). Repeating that erased map would produce artificial dynamics such as repeated division toward zero.

That is a **type-erasure artifact**. After one projection from scale \(e\) to scale \(d\), the result is no longer a state at scale \(e\), so the same typed arrow cannot simply be applied again.

P009 therefore must classify scale dynamics on tagged states, not on an untyped integer carrier.

## 2. Tagged scale state

Use the state form

\[
(d,m),
\]

where

- \(d\in\mathbb N_{>0}\) is the explicit scale factor;
- \(m\in\mathbb N\) is the integer coordinate represented at that scale.

For a finite allowed scale set

\[
D\subset\mathbb N_{>0},
\]

the tagged state space is

\[
\mathcal X_D=\bigsqcup_{d\in D}\{d\}\times X_d.
\]

The disjoint-union notation is semantic: two identical integers at different scales are different tagged states.

## 3. Canonical transition types

### A. Scale coarsening

If

\[
d\mid e,
\qquad d<e,
\]

define

\[
\Pi_{e\to d}(e,m)
=
\left(d,m\operatorname{//}(e/d)\right).
\]

This changes the scale tag.

### B. Same-scale collapse

For a positive exponent \(p\), define

\[
\mathcal C_p(d,m)
=
(d,C_p(m)).
\]

This keeps the scale tag and applies perfect-power collapse to the integer coordinate.

Both are canonical many-to-one operations already justified by earlier project mathematics.

## 4. P009-S01 — Lexicographic rank decreases on every strict canonical transition

Status: `PROVED`

Order tagged states lexicographically by

\[
\operatorname{rank}(d,m)=(d,m)
\]

with the ordinary order on natural numbers and the scale coordinate first.

Then every non-identity canonical transition strictly decreases this rank.

### Strict scale coarsening

If

\[
(e,m)\to(d,m')
\]

with \(d<e\), the first coordinate strictly decreases, so

\[
(d,m')<(e,m)
\]

lexicographically regardless of \(m'\).

### Strict collapse

If

\[
(d,m)\to(d,C_p(m))
\]

and the state changes, then

\[
C_p(m)<m
\]

because collapse is reductive and non-fixed states collapse strictly downward. The first coordinate is unchanged and the second decreases.

Hence every strict canonical step decreases \((d,m)\). ∎

## 5. P009-S02 — No nontrivial directed cycles

Status: `PROVED`

The canonical collapse+coarsening transition system has no directed cycle containing a strict state change.

### Proof

A directed cycle would return to its starting tagged state. But every strict edge decreases the lexicographic natural-number rank, while identity edges preserve it. A finite sequence containing a strict decrease cannot return to the original rank. ∎

Therefore every directed cycle consists entirely of identity transitions.

This extends the collapse-only no-cycle result to the properly typed canonical scale system.

## 6. P009-S03 — Every strict trajectory terminates

Status: `PROVED`

Suppose \(D\) is finite and consider a trajectory in which identity/no-op transitions are omitted.

Then the trajectory is finite.

### Proof

Strict scale changes can occur only finitely many times because each one decreases the positive integer scale tag inside finite \(D\).

Between scale changes, every strict collapse decreases \(m\in\mathbb N\), which can also happen only finitely many times.

Equivalently, the lexicographic order on \(\mathbb N_{>0}\times\mathbb N\) is well-founded for strictly descending finite-state trajectories. ∎

Thus the canonical system is terminating as a rewrite/reduction system.

A scheduler can of course apply an identity transition forever. Such stuttering is not a nontrivial dynamical cycle.

## 7. Terminal scale states and sinks

Let \(D\) carry the allowed strict projection arrows. Call \(d\in D\) terminal when there is no allowed strict coarsening

\[
d\to d'<d.
\]

Suppose the same-scale allowed collapse exponents at terminal scale \(d\) are

\[
P_d=\{p_1,\ldots,p_r\}.
\]

A tagged state \((d,m)\) is a sink exactly when:

1. \(d\) is terminal for scale coarsening; and
2. \(m\) is fixed by every allowed collapse \(C_{p_i}\).

By the fixed-point result from P004, if the exponents are positive and

\[
L_d=\operatorname{lcm}(p_1,\ldots,p_r),
\]

then condition 2 is equivalent to

\[
m\text{ being a perfect }L_d\text{-th power}.
\]

Therefore the sink set at terminal scale \(d\) is

\[
\boxed{
\{(d,k^{L_d}):k\in\mathbb N\}.
}
\]

If no collapse map is required at that scale, every tagged integer state there is a sink with respect to the specified transition family.

## 8. Unique versus multiple terminal scales

The canonical transition system need not have a unique sink for each starting state.

If the allowed scale graph has several incomparable terminal scales, different legitimate coarsening choices can end at different scale tags.

This is not contradiction. It means the transition specification itself is nondeterministic at the level of which projection is chosen.

If a unique normal form is desired, the model must provide an additional rule, for example:

- a unique chosen coarsest scale;
- a deterministic scheduling policy;
- or a confluence theorem showing different reduction paths rejoin.

P005's projection diamond proves path independence when two projection paths have the **same target scale**. It does not say that different terminal target scales are identical states.

## 9. Same-target scale path independence

If

\[
d\mid e\mid f,
\]

P005 gives

\[
\Pi_{e\to d}\circ\Pi_{f\to e}
=
\Pi_{f\to d}.
\]

Thus the integer coordinate at a fixed target scale is independent of how the projection chain is factorized.

This remains true inside the tagged system:

\[
(f,m)
\to(e,\cdot)
\to(d,\cdot)
\]

and

\[
(f,m)\to(d,\cdot)
\]

end at the same tagged state.

So scale projection itself has a strong confluence property.

## 10. Collapse/projection interleaving need not be order independent

Path independence of pure scale projection does not imply that arbitrary collapse and projection operations commute.

A collapse changes the integer coordinate before a later projection. A projection changes the coordinate before a later collapse. Unless a separate interchange theorem applies to the particular operations, different interleavings may produce different transient tagged states.

P009 should therefore distinguish:

- **termination / absence of cycles**, which follows from the rank argument;
- **confluence / unique normal form**, which is an additional theorem and may require stronger compatibility assumptions.

This mirrors the distinction already found in P003/P004: different collapse words can have the same fixed-point set without being equal as one-pass operators.

## 11. Why canonical refinement is absent

P005 proves that a coarse root state does not determine a unique finer root state.

Therefore there is no canonical state-only arrow

\[
X_d\to X_e
\qquad(d<e)
\]

that inverts \(\Pi_{e\to d}\).

A model that wants refinement has two options.

### A. Retain the underlying source state

If the underlying \(n\) is still explicitly represented, a finer view can be recomputed:

\[
(n,d)\mapsto(n,e),
\]

with the scale-dependent root derived again from \(n\).

This is a change of represented view with retained information, not an inverse of a many-to-one root-state projection.

### B. Add a noncanonical lifting rule

A rule may choose one compatible fine state from the projection fiber. But that is extra model structure. Different lifting conventions can create different cycles or path dependencies and must be studied separately.

Such a lift is not part of the minimal canonical scale algebra.

## 12. P009-S04 — Type erasure creates spurious zero-attractor dynamics

Status: `COUNTEREXAMPLE / DESIGN WARNING`

Erase scale tags and treat a fixed projection ratio \(r>1\) as the endomap

\[
Q_r(m)=m//r
\]

on one copy of \(\mathbb N\).

Repeated iteration gives

\[
Q_r^t(m)=m//r^t,
\]

which eventually reaches zero.

It would therefore be tempting to conclude that “repeated scale projection drives every state to zero.”

But after the first typed projection

\[
(e,m)\to(d,m//r),
\]

the state belongs to scale \(d\), not scale \(e\). Reapplying the same \(e\to d\) arrow is ill-typed.

Hence the apparent universal zero attractor is an artifact of forgetting the scale coordinate.

## 13. Revised P009 classification

The P009 dynamics now separates into two mathematically clean layers.

### Collapse-only endomorphism layer

For a fixed collapse word, the previous P009 result shows finite stabilization, no nontrivial cycles, and exact convergence to the appropriate lcm-collapse state.

### Typed collapse+scale layer

For canonical strict scale coarsenings plus same-scale collapses:

- every strict step lowers lexicographic rank \((d,m)\);
- no nontrivial cycle exists;
- every strict trajectory terminates;
- sinks occur only at terminal scale tags and collapse-fixed integer states;
- pure projection paths to the same target scale are path independent;
- unique normal forms across different target scales or arbitrary collapse/projection interleavings require additional confluence assumptions;
- state-only refinement is not canonical.

This removes the earlier ambiguity in the phrase “semigroup generated by collapse and scale maps.” The canonical scale structure is a **typed directed system/category of projections**, not merely a set of endomorphisms of one untagged integer carrier.

## 14. P009 status after P005

With the P005 typing correction, the canonical finite collapse+coarsening dynamics is structurally classified at the level of termination, cycles and sink states.

What remains open is not the existence of mysterious scale cycles. The remaining research concerns optional additional structures:

- noncanonical inverse lifts;
- deterministic refinement policies with retained source state;
- confluence of mixed collapse/projection rewrite systems;
- normal-form classification for particular finite scale graphs.

These should be separated from the minimal canonical P009 result.

## 15. Prior-art discipline

Typed transition systems, well-founded rewrite orders, projective systems and divisibility-poset maps are established mathematics. P005 already treats inverse/projective-system language as prior structural vocabulary.

The project-specific correction here is semantic and architectural: the scale tag is part of the state type, so erasing it creates fake endomorphism dynamics. No historical-priority claim is made for well-founded rewriting or typed categories.
