# BRC Feedback Circuit Atoms and Interaction Girth

Status: `RESEARCH CANDIDATE / EXACT SUPPORT+RATIONAL / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCFB-93C7D1`
Parent: PR #1146 / merge `69ca04e285d717f015295e149f03cbfd31836ba4`

## 1. Purpose

PR #1146 decomposed stable feedback loop surplus into nonnegative Möbius interaction factors

\[
J_T\ge1
\]

indexed by nonempty inserted-event subsets `T`, with `J_T>1` exactly when there exists a positive closed event walk using precisely the events in `T`.

This note identifies the **minimal nontrivial interaction supports** and the first nonzero interaction order.

The generic facts about directed cycles, girth, induced cycles and geometric-series closure are classical. No generic graph-theory novelty is claimed. The project-specific synthesis is the exact BRC atom:

```text
minimal recurrent event support
-> induced directed circuit
-> rational cycle holonomy Q_T
-> exact interaction factor 1/(1-Q_T)
-> LN readout -ln(1-Q_T)
```

## 2. Möbius-primitive interaction support

Call a nonempty event set `T` **Möbius-primitive** when

\[
J_T>1
\]

but

\[
J_U=1
\qquad
\text{for every nonempty }U\subsetneq T.
\]

Equivalently, the induced feedback-event support on `T` admits a positive closed walk visiting all events of `T`, while no proper induced event subset admits any positive closed walk covering that subset.

## 3. Primitive supports are induced directed circuits

### Candidate BRC-CA1

Let `T` be Möbius-primitive.

If `|T|=1`, the unique event has a positive self-return and is a one-event circuit atom.

If `|T|>=2`, the induced positive-support digraph on `T` is exactly a directed simple cycle.

**Proof.** Since `J_T>1`, there exists a positive closed walk whose event support is `T`. Every finite directed closed walk contains a directed simple cycle. Let `U` be the vertex/event set of such a simple cycle. Then `J_U>1`. Möbius-primitivity forces `U=T`, so a directed Hamiltonian cycle on `T` exists.

Fix that cycle. If the induced support contained any additional directed edge `i->j` not equal to the Hamiltonian successor edge, combining it with the directed cycle segment from `j` back to `i` would produce a directed cycle on a proper subset of `T`, contradicting primitivity. Hence no additional support edge exists.

Thus the induced support is precisely one directed simple circuit.

This is a **support theorem**: positive magnitudes do not affect which event sets are primitive as long as support is unchanged and the full system remains in the stable positive phase.

## 4. Exact atom holonomy and closure

Let a primitive circuit atom `T` have directed event-kernel edges

\[
t_1\to t_2\to\cdots\to t_r\to t_1
\]

with positive rational kernel masses

\[
f_1,\ldots,f_r.
\]

Define its circuit holonomy/product

\[
\boxed{Q_T=\prod_{j=1}^r f_j.}
\]

Every proper principal subkernel is acyclic, so its zeta factor is 1. The whole circuit determinant is

\[
\det(I-F_T)=1-Q_T.
\]

Stable recurrence forces `0<Q_T<1`. Therefore the primitive Möbius factor is

\[
\boxed{
J_T=\frac1{1-Q_T}
}
\]

and the additive interaction surplus is

\[
\boxed{
\Phi_T=-\ln(1-Q_T).
}
\]

This is exactly the one-state recurrent closure law, but with the scalar one-step mass replaced by the full circuit holonomy.

No logarithm is required in the exact layer: `Q_T` and `J_T` are positive rationals, and `Phi_T` is materialized only via the canonical BRC `LN` facade.

## 5. Interaction girth

Define the first nonzero interaction order

\[
\boxed{
g_{\rm int}(F)
=\min\{|T|:J_T>1\},
}
\]

with `g_int=infinity` when every interaction factor is 1.

Let `g_dir(F)` be the directed girth of the positive-support feedback-event digraph, counting a self-loop as a directed cycle of length 1, and `infinity` for a DAG.

### Candidate BRC-CA2

\[
\boxed{
g_{\rm int}(F)=g_{\rm dir}(F).}
\]

**Proof.** Any directed simple cycle with vertex set `T` gives a positive closed event walk supported on `T`, hence `J_T>1`; therefore `g_int<=g_dir`.

Conversely any `J_T>1` yields a closed walk supported on `T`, which contains a directed simple cycle on some `U subseteq T`, hence `g_dir<=|U|<=|T|`. Taking the minimum gives the reverse inequality.

Thus the order at which the Möbius hierarchy first becomes nontrivial is purely the minimum number of declared feedback events needed to close a recurrent directed circuit.

## 6. Atom topology versus atom intensity

A primitive circuit atom separates cleanly into:

- **topological order** `r=|T|` — how many inserted feedback events are minimally required;
- **rational holonomy** `Q_T` — the positive multiplicative strength around that circuit;
- **zeta multiplier** `J_T=1/(1-Q_T)` — exact recurrent amplification;
- **log surplus** `Phi_T=-ln(1-Q_T)` — derived additive readout.

The support/topological order is unchanged under positive weight rescaling that does not remove an edge. `Q_T` changes with actual branch weights but is invariant under the original vertex-gauge similarity because gauge factors telescope around the circuit.

Thus the circuit atom has a natural `support + rational holonomy` typing before logarithmic readout.

## 7. Prime-valuation coordinates of a circuit atom

Because `Q_T` is a positive rational gauge invariant,

\[
Q_T=\prod_p p^{\nu_{p,T}}
\]

with finitely many nonzero integer valuations

\[
\nu_{p,T}=v_p(Q_T)\in\mathbb Z.
\]

Hence every primitive feedback atom has an exact prime-valuation holonomy module coordinate before any log embedding:

\[
\ln Q_T
=\sum_p \nu_{p,T}\ln p.
\]

For any `m>=2`, the previously merged skeleton/thickness decomposition applies:

\[
Q_T=s_m(Q_T)t_m(Q_T)^m.
\]

Thus a primitive circuit atom naturally carries both:

- a mod-m / parity skeleton;
- an exact rational m-th-power thickness.

The recurrent phase boundary for the isolated atom is simply

\[
Q_T<1.
\]

Parity/skeleton alone does not determine this inequality; the thickness coordinate remains essential.

## 8. Determinant-polynomial relation

At event level, the determinant polynomial of a primitive atom is

\[
P_T=1-Q_T.
\]

This is the smallest possible nontrivial directed-cycle determinant term. In the finite alternating determinant language of PR #1134, it is one simple-cycle monomial; in the positive loop-zeta language, inversion gives the full repeated-circuit geometric closure

\[
1+Q_T+Q_T^2+\cdots.
\]

Therefore a primitive Möbius atom is the exact bridge between:

```text
finite determinant cycle monomial
<-> rational circuit holonomy Q_T
<-> infinite positive recurrent closure 1/(1-Q_T)
<-> LN surplus -ln(1-Q_T).
```

## 9. Nonprimitive interactions are genuinely composite

If `J_T>1` but some proper subset `U` also has `J_U>1`, then `T` is not a circuit atom. Its induced event subgraph contains lower-order recurrent circuits.

The higher interaction `J_T` then records closed walks that use all events of `T` **in addition to** those lower-order circuits. It should not be collapsed to one simple cycle product.

Example: two overlapping recurrent cycles may generate a positive higher-order interaction even though each cycle already has its own lower-order atom.

Thus the full hierarchy is:

```text
primitive circuit atoms
-> overlapping/composite event interactions
-> total subset zeta Z(A)
-> scalar Gamma(A).
```

## 10. Pure r-th order circuit family

For every `r>=2`, consider an event kernel supported only on one directed r-cycle:

\[
1\to2\to\cdots\to r\to1
\]

with positive rational edge masses `f_1,...,f_r` and product `Q<1`.

Every proper event subset is acyclic, so

\[
J_U=1
\quad(U\subsetneq T),
\]

while

\[
\boxed{J_T=1/(1-Q)>1.}
\]

Hence pure feedback cooperation exists at arbitrary finite order: all interactions below order `r` can vanish exactly while the first nonzero recurrent interaction occurs at order `r`.

This generalizes the pure third-order example from PR #1146.

## 11. Full-graph DAG realization at arbitrary order

A pure r-event cycle kernel can be realized on a feed-forward old background with `2r` states:

- inserted event `e_i: a_i->b_i`;
- old background path/edge `b_i->a_{i+1}` for `i=1,...,r-1`;
- old background path/edge `b_r->a_1`.

Because all `a_i,b_i` are distinct and old edges alone do not chain through inserted edges, the old background is acyclic. Any proper subset of inserted events leaves the full graph acyclic. All r inserted events together create the first directed recurrent loop.

Thus arbitrary-order pure Möbius feedback is not merely an abstract event-kernel construction; it has an explicit BRC graph realization.

## 12. Boundary with pairwise risk models

If `g_int>2`, every singleton and pair interaction factor is exactly 1. Any risk model that stores only:

- per-edge return masses;
- pairwise interaction factors;
- pairwise interaction graph,

will report no recurrent coupling before the full higher-order circuit closes.

Therefore pairwise recurrent summaries are complete only under an additional structural restriction excluding directed feedback circuits of length `>=3` that have no shorter recurrent subcircuits.

No such restriction is assumed in general BRC.

## 13. Prior-art boundary

Directed girth, simple cycles, induced/chordless cycles, cycle products and geometric closure are classical graph/algebra facts.

The project-specific reusable synthesis is:

\[
\boxed{
\text{first nonzero BRC Möbius interaction order}
=
\text{directed feedback girth}
}
\]

plus the exact circuit-atom coordinate

\[
\boxed{(T,Q_T,J_T)}
\]

inside the already established Weighted-BRC / prime-valuation / zeta toolchain.

## 14. Boundaries

This candidate does not claim:

- that every nonprimitive `J_T` is a single-cycle closure;
- that pairwise interaction is complete;
- signed/amplitude circuit semantics;
- infinite event-set girth/closure;
- a new graph-theoretic notion of girth;
- external novelty for simple-cycle or determinant identities.

## 15. Validation plan

Use exact rational arithmetic and support enumeration.

1. Exhaust all `2^12=4096` loopless directed support graphs on four labeled event vertices, assign uniform edge mass `1/10` (all stable), and verify `g_int=g_dir`.
2. Enumerate every nonempty event subset; classify Möbius-primitive subsets and verify the induced support is exactly one directed simple cycle.
3. For every primitive subset verify `J_T=1/(1-Q_T)` exactly.
4. Add explicit self-loop cases to verify interaction order 1.
5. Add nonuniform rational directed cycles of lengths 2,3,4 and verify prime-valuation/gauge-invariant product `Q_T` and exact zeta closure.
6. Verify pure r-order examples for r=2,3,4 have all lower-order interactions exactly 1.
7. Realize the pure r-order kernels on explicit `2r`-state DAG backgrounds for r=2,3,4 and verify proper inserted subsets remain acyclic.

A dedicated research CI gate must pass before any Foundation backflow.
