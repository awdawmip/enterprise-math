# X6 triadic interaction V20: irreducible 5D pure-triadic field and unique symmetric multi-Cell coupling

Status: `FREE_RESEARCH / EXACT REPRESENTATION-AND-COUPLING DERIVATION / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, `RS-X6-CELL-CHANNEL-INTERNAL-STATE`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_TRIADIC_INTERACTION_DEFECT_V18_20260906.md`;
- `X6_TRIADIC_RATIONAL_PAIR_FACTORIZATION_V19_20260906.md`;
- current finite-symmetry and BRC observer discipline.
Checker: `experiments/x6_pure_triadic_field_coupling_v20_20260906/check_pure_triadic_field_coupling.py`.

## 1. Question

V18 identifies a canonical five-dimensional sector

`K=ker(P) subset Q^20`

of triad-type contrasts invisible to every pair co-occurrence observer.

V19 shows that exact rational pair factorization has an additional finite valuation torsion, but pair-factorizable laws still cannot distinguish branches related by a V18 trade.

The next question is:

> what is the smallest genuinely non-pairwise interaction law that respects full six-axis relabeling symmetry?

The answer separates context-free and relational laws sharply.

## 2. S6 action on the pure-triadic sector

`S6` acts on the 20 triad coordinates by relabeling the six axes.

The pair-shadow map P is equivariant under simultaneous relabeling of triads and pairs, hence

`K=ker(P)`

is an S6-stable five-dimensional rational representation.

Use the saturated integer kernel basis B already frozen in the V18 checker. Its five pivot triad coordinates are an identity block, so every axis permutation induces an exact `5x5` integer matrix on K.

## 3. Exact irreducibility theorem

Take the five adjacent positive-axis transpositions

`(12),(23),(34),(45),(56)`,

which generate S6, and let their induced matrices on K be `R_1,...,R_5`.

Solve for a rational `5x5` matrix X satisfying

`X R_a = R_a X`

for all five generators.

This is a homogeneous rational linear system in 25 unknown matrix entries. Exact elimination gives rank 24.

Therefore

`End_{S6}(K)=Q * I`.

Because representations of a finite group over Q are semisimple, a nontrivial decomposition of K would produce a non-scalar equivariant projection. Hence none exists:

`K is irreducible over Q`.

This is a direct exact commutant certificate; no character table or external representation classification is required.

## 4. No context-free linear pure-triadic bias

The fixed-vector equations

`R_a h=h`

for all generators have only the zero solution.

Thus K contains no trivial S6 subrepresentation.

Equivalently, no nonzero pure-triadic linear functional/field can be frozen as one globally preferred axis-symmetric direction without supplying extra relational context.

At the full 20-triad level, a fixed S6-invariant linear triad-type weight is constant on all 20 types; its V18 pure projection is zero. So a globally symmetric **fixed linear type bias** cannot select one member of a pair-shadow trade over another.

## 5. Unique invariant bilinear form up to scale

Let the ordinary coefficient dot product on `Q^20` restrict to K. In the V18 integer basis its Gram matrix is

`G=B^T B`,

which is positive definite and S6 invariant.

For any other S6-invariant bilinear form `b` on K, write

`b(x,y)=<A x,y>_G`

using the nondegenerate G pairing.

Invariance forces A to commute with every S6 action matrix. By the commutant theorem,

`A=c I`.

Hence every invariant bilinear form is a scalar multiple of G.

Therefore the symmetric quadratic magnitude on the pure-triadic sector is unique up to normalization.

V18's projector

`Pi_tri=F/24`,

with

`F=sum_M v_M v_M^T`,

uses exactly this canonical invariant geometry.

## 6. Canonical integer multi-Cell coupling

For any two triad-population/context vectors `n,m in Z^20`, define

`C3(n,m)=n^T F m`.

Using the V18 tight-frame identity:

`C3(n,m)=sum_M (v_M dot n)(v_M dot m)`

and

`C3(n,m)=24 <Pi_tri n, Pi_tri m>`.

Properties:

- integer-valued on integer inputs;
- symmetric;
- S6 invariant under simultaneous axis relabeling;
- depends only on the pure-triadic components;
- vanishes if either input has zero V18 pure-triadic projection.

By the invariant-bilinear theorem, after restriction to K this coupling is the **unique S6-invariant bilinear pure-triadic coupling up to one scalar coefficient**.

This is an algebraic interaction observable, not automatically a physical energy.

## 7. Exact positive-rational non-pairwise weight family

Let `rho in Q_{>0}`.

Define a context-dependent branch weight

`W_rho(n | m)=rho^(C3(n,m))`.

Because `C3(n,m)` is an integer, this is always a positive rational even when the exponent is negative.

It is S6 invariant under simultaneous relabeling of n and m.

Unlike pair-factorized laws, it can distinguish pair-shadow-equivalent decomposition branches whenever the context m has a nonzero pairing with their pure-triadic difference.

This provides a concrete exact Weighted-BRC family realizing the type of non-factorized interaction left open in V18/V19.

No claim is made that nature uses an exponential/power-law weighting or any particular rho.

## 8. Minimal 4<->4 trade is selected by a neighboring pure-triadic context

Let `n_+` and `n_-` be the two four-triad branches of one perfect-matching trade and

`v=n_+-n_-=v_M`.

They have identical macro axis demand and identical pair shadow.

For any context m,

`C3(n_+,m)-C3(n_-,m)`

`=v^T F m`

`=24 v dot m`,

because `F v=24v`.

Therefore:

- if `v dot m=0`, this coupling leaves the trade unresolved;
- if `v dot m!=0`, the context gives an exact route preference for any `rho!=1`.

Taking `m=n_+` gives the exact values

`C3(n_+,n_+)=48`,

`C3(n_-,n_+)=-48`,

so

`W_rho(n_+|n_+) / W_rho(n_-|n_+) = rho^96`.

Thus the five-dimensional pure-triadic context can resolve the first pair-shadow collision with an exact rational ratio.

## 9. Context-free S6-invariant scalar cannot orient a minimal trade

For each perfect matching M, swapping the two endpoints inside any one matching pair maps the even-transversal four-triad branch to the odd-transversal branch.

Hence `n_+` and `n_-` lie in the same S6 orbit.

Therefore **every context-free S6-invariant scalar function**, linear or nonlinear, must assign them the same value.

This is stronger than the absence of a linear fixed vector: the minimal pair-shadow ambiguity cannot be resolved at all by a scalar law depending only on one isolated decomposition while preserving full S6 relabeling symmetry.

A route preference requires some additional relational datum that transforms with the system, e.g.:

- a neighboring Cell's pure-triadic field;
- active-triad/event history;
- internal/channel state;
- an external/calibrated symmetry-breaking field.

The context can preserve global covariance even though a particular state is not itself S6 fixed.

## 10. Minimal covariant field interpretation

Define the pure-triadic field coordinate of a local triad population by

`h(n)=Pi_tri n in K_R`.

For exact integer-only work one may instead carry

`H(n)=F n=24 h(n) in Z^20`.

Under axis relabeling `g in S6`:

`h(gn)=g h(n)`,

`H(gn)=g H(n)`.

The field therefore has exactly five independent rational degrees and transforms irreducibly.

A neighboring field h supplies the minimal linear covariant context. Up to scale, the only S6-invariant bilinear response is the canonical pairing already encoded by `C3`.

So the first non-pairwise symmetric interaction is not “five unrelated coefficients”; it is one five-component transforming field plus one overall bilinear coupling scale.

## 11. Multi-Cell network and time dependency

For a graph/network of interacting Cells with local triadic contexts `n_x`, an exact algebraic interaction score may be assembled from edges

`sum_{x~y} kappa_xy C3(n_x,n_y)`

or, in positive-rational Weighted-BRC form,

`product_{x~y} rho_xy^(C3(n_x,n_y))`.

If an update at x changes the context used by y or vice versa, the events are not certified independent and the native-time dependency poset must retain the corresponding order relation.

Thus V20 gives a concrete bridge between:

`pure triadic BRC defect`

and

`multi-Cell relational dependency`.

It does not yet derive a specific update schedule or show that this coupling produces the V17 holonomy/Ori6 trigger; that is the next dynamical question.

## 12. Current frontier

Closed:

- irreducibility of the 5D pure-triadic sector over Q;
- absence of a nonzero S6-fixed pure-triadic field;
- uniqueness of S6-invariant bilinear coupling up to scale;
- canonical integer coupling `C3=n^T Fm`;
- exact positive-rational non-pairwise weight family;
- context-free S6-invariant route-selection no-go on minimal 4<->4 trades;
- neighboring pure-triadic context as a minimal covariant repair.

Next high-leverage target:

construct the smallest coupled two-/multi-Cell update law in which the local pure-triadic field changes active triad context and determine whether its dependency/history holonomy can generate the V17/V15 Ori6 control bit without an externally supplied trigger.

No Foundation promotion, physical-energy interpretation or external novelty claim is made.
