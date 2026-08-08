# P019 — Directed Causal Expansion, Supplement 03: Future Sections, Branching, and Merging

Status: `ACTIVE RESEARCH NOTE`  
Depends on: P010/P011 forward merging, P012 primitive graph geometry, P019 Causal Boundary Supplement 02  
Scope: generate integer expansion directly from directed one-step reachability instead of supplying `xi` by hand  
Discipline: this is a finite-graph candidate null-cross-section calculus, not a discrete derivation of the Einstein or Raychaudhuri equations.

## 1. From point phases to future-section cardinality

Let

\[
G=(V,E^+)
\]

be a finite directed primitive graph.

For a nonempty finite cross-section

\[
A\subseteq V,
\]

define its one-step future reachable set

\[
\boxed{
F(A)
=
\{w\in V:\exists v\in A,(v,w)\in E^+\}.
}
\]

`F(A)` keeps only **distinct future states**. Multiple edges that reach the same `w` still contribute one future state.

Define the integer future-section expansion

\[
\boxed{
\Xi(A)=|F(A)|-|A|.
}
\]

Thus:

- `Xi(A)>0`: the next cross-section has more distinguishable future states;
- `Xi(A)=0`: marginal cardinality;
- `Xi(A)<0`: the future cross-section contracts.

This gives a first candidate source for the manually supplied `xi` field in Supplement 02: treat the **cross-section itself** as the state and `Xi(A)` as its expansion field.

## 2. P019-D-T01 — Future preserves unions

Status: `PROVED`

For any two cross-sections `A,B`,

\[
\boxed{F(A\cup B)=F(A)\cup F(B).}
\]

This follows directly from existential one-step reachability. ∎

## 3. P019-D-T02 — Exact overlap defect for expansion

Status: `PROVED`

Finite inclusion-exclusion gives

\[
|F(A\cup B)|
=|F(A)|+|F(B)|-|F(A)\cap F(B)|,
\]

\[
|A\cup B|
=|A|+|B|-|A\cap B|.
\]

Therefore

\[
\boxed{
\Xi(A\cup B)
=
\Xi(A)+\Xi(B)
+|A\cap B|
-|F(A)\cap F(B)|.
}
\]

If

\[
A\cap B=\varnothing,
\]

then

\[
\boxed{
\Xi(A\cup B)
=
\Xi(A)+\Xi(B)
-|F(A)\cap F(B)|.
}
\]

When initially disjoint sections begin to share future states, their future overlap therefore subtracts **exactly** from total expansion.

This is the first formula in this line that writes focusing/merging directly into a cross-section change without primitive continuum curvature.

## 4. P019-D-T03 — Exact branching–collision decomposition

Status: `PROVED`

Define the number of directed edge incidences leaving `A` by

\[
E_A
=
|\{(v,w)\in E^+:v\in A\}|.
\]

Define the **branching surplus**

\[
\boxed{
B(A)=E_A-|A|.
}
\]

For each future state `w`, define its incoming multiplicity from `A`:

\[
m_A(w)
=
|\{v\in A:(v,w)\in E^+\}|.
\]

Define the **collision/focusing excess**

\[
\boxed{
C(A)
=
\sum_{w\in F(A)}(m_A(w)-1).
}
\]

Since

\[
\sum_{w\in F(A)}m_A(w)=E_A,
\]

we have

\[
C(A)=E_A-|F(A)|.
\]

Thus

\[
\Xi(A)
=|F(A)|-|A|
\]

becomes

\[
\boxed{
\Xi(A)=B(A)-C(A).
}
\]

This is the central formula of this stage:

\[
\boxed{
\text{future expansion}
=
\text{branching surplus}
-
\text{collision/focusing excess}.
}
\]

In this candidate model, causal-space convergence no longer needs a mysterious continuous compression variable. It first means that multipath coalescence consumes more distinguishable future states than outgoing branching creates.

## 5. P019-D-T04 — A marginal boundary is exact integer balance between branching and collision

Status: `PROVED`

By T03,

\[
\Xi(A)=0
\iff
B(A)=C(A).
\]

A candidate marginal cross-section therefore obeys

\[
\boxed{
\text{new future branching}
=
\text{future collision/focusing}.
}
\]

Likewise,

\[
\Xi(A)>0
\iff
B(A)>C(A),
\]

\[
\Xi(A)<0
\iff
B(A)<C(A).
\]

The expansion–horizon–contraction phases now share one discrete mechanism rather than being only three labels.

## 6. P019-D-T05 — Exact interface with the P011 local collision spectrum

Status: `PROVED FINITE-MAP INTERFACE`

Collect all outgoing edge incidences from `A` into the finite set

\[
I_A
=
\{(v,w)\in E^+:v\in A\}.
\]

Define the target map

\[
\tau_A:I_A\to F(A),
\qquad
\tau_A(v,w)=w.
\]

This is a genuine finite function whose fiber size is exactly

\[
m_A(w).
\]

The P011 collision spectrum therefore applies directly:

\[
\boxed{
J_k^{\mathrm{out}}(A)
=
\sum_{w\in F(A)}\binom{m_A(w)}k.
}
\]

Here:

- `J_2` counts paired future-incidence collisions;
- higher `J_k` record higher-order focusing;
- the full spectrum reconstructs the target-fiber multiplicity multiset.

The T03 quantity

\[
C(A)=\sum_w(m_A(w)-1)
\]

is a coarser first-order focusing loss than the full collision spectrum.

P019 therefore does not need a new “black-hole merging entropy.” Existing P011 integer fiber tools can be applied directly to the causal incidence target map.

The semantics remain precise: P011 is applied here to the **local map from outgoing incidences to future targets**, not automatically to the universe-wide time evolution map.

## 7. P019-D-T06 — Single-successor dynamics cannot create positive cardinal expansion

Status: `PROVED`

If every vertex in `A` has exactly one outgoing successor, then

\[
E_A=|A|,
\]

so

\[
B(A)=0.
\]

T03 gives

\[
\boxed{
\Xi(A)=-C(A)\le0.
}
\]

Equality holds iff the successor map is injective on `A`.

Thus:

> **If bare spatial vertices evolve under a single-valued successor function, distinct future-state cardinality can only stay fixed or decrease; it cannot positively expand.**

This matches the deterministic merging structure of P010.

Representing genuinely expanding spatial light fronts therefore cannot simply identify primitive causal geometry with a state function having exactly one successor per bare spatial point. At least one of the following is needed:

- a branching reachability relation;
- richer ray/direction states;
- time-layered cells in which one spatial cross-section reaches multiple future cells.

This is an architecture constraint, not a physical conclusion.

## 8. P019-D-T07 — Expansion telescopes exactly along future-section evolution

Status: `PROVED`

Let

\[
A_{t+1}=F(A_t).
\]

Then by definition

\[
\Xi(A_t)=|A_{t+1}|-|A_t|.
\]

For every finite `T`,

\[
\boxed{
\sum_{t=0}^{T-1}\Xi(A_t)
=|A_T|-|A_0|.
}
\]

This is a fully integer cumulative expansion law.

It uses no derivative, integral, or continuous affine parameter. A later comparison can study how one-step cardinal differences relate to continuum null expansion under typed scale, but no continuum limit is required by the definition.

## 9. P019-D-C01 — Expansion is not entropy and need not be monotone

Status: `COUNTEREXAMPLE / SCOPE BOUNDARY`

A finite directed graph can produce the expansion sequence

\[
+1,-3,-1.
\]

So `Xi_t` itself is not monotone.

It is only the cardinal difference between adjacent future cross-sections.

Therefore `Xi` must not be renamed entropy or treated as an irreversibility monotone. P010/P011 monotonicity remains attached to appropriate forward-function fiber/collision observables. P019 `Xi` is a geometric/causal cross-section quantity. T03/T05 provide an interface, not an identity of meanings.

## 10. A sharper form of the original intuition

The original question was whether a black hole could be “slower time causing spatial convergence.”

After the Schwarzschild, RN, graph-boundary, and directed future-section stages, the strict candidate mechanism is now

\[
\boxed{
\text{future reachability}
\to
\text{branching}
+
\text{collision/focusing}
\to
\Xi=B-C.
}
\]

When

\[
C>B,
\]

the future cross-section contracts. When

\[
C=B,
\]

a marginal-boundary candidate appears.

It has **not** yet been proved that slower clock state causes `C` to rise. The first-stage clock observation and this graph structure now expose a precise missing interface:

\[
\boxed{
\text{clock precision state}
\stackrel{?}{\longrightarrow}
\text{allowed future-incidence structure}
\longrightarrow
B,C,\Xi.
}
\]

The next stage should attack this arrow rather than repeat another coordinate discretization.

## 11. Stage ledger

- `P019-D-T01`: future preserves unions — `PROVED`
- `P019-D-T02`: exact union-overlap expansion defect — `PROVED`
- `P019-D-T03`: `Xi=B-C` branching/collision decomposition — `PROVED`
- `P019-D-T04`: marginal iff branching equals collision — `PROVED`
- `P019-D-T05`: local outgoing collision spectrum interfaces exactly with P011 — `PROVED`
- `P019-D-T06`: single-successor maps cannot create positive distinct-state expansion — `PROVED`
- `P019-D-T07`: future-section expansion telescopes — `PROVED`
- `P019-D-C01`: `Xi` need not be monotone and is not entropy — `COUNTEREXAMPLE / BOUNDARY`

Executable checks:

- `src/enterprise_math/directed_expansion.py`
- `tests/test_directed_expansion.py`

## 12. Next stage: actually couple clock state to causal incidence

The highest-priority questions are now:

1. define an allowed future-incidence budget for each finite clock state `K` instead of specifying a graph by hand;
2. test whether slower clock states necessarily reduce branching, increase collision, or neither — counterexamples must be allowed;
3. identify the minimum extra axiom under which `K=0` produces marginal `B=C`;
4. separate observer-coordinate clock slowdown from invariant causal-incidence restriction;
5. if no natural coupling exists, reject the strong causal direction “slower time causes spatial convergence” and retain only the weaker explanation that both arise from the same deeper structure.
