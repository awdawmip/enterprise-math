# Prior art — R004 structural obstruction basis and typed adequacy cuts

Status: `RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

Supplements 16-17 reduce typed future-language basis extraction to generator-side minimal cuts and hypergraph transversals. The hypergraph/blocker/dualization mathematics is established prior art. R004 claims only the compiler-specific reduction, canonical forbidden-world certificates, and typed carrier/semantic cut decomposition.

## 1. Hypergraph transversal / monotone dualization is prior art

Eiter, Gottlob and Makino study monotone dualization and generation of hypergraph transversals, explicitly treating minimal transversals / minimal hitting sets as an established computational problem [SRC-EITER-GOTTLOB-MAKINO-2002-DUALIZATION].

Murakami and Uno define the dual of a hypergraph as the family of minimal hitting sets and develop algorithms for large-scale hypergraph dualization [SRC-MURAKAMI-UNO-2011-HYPERGRAPH-DUALIZATION].

Mary's later work again formulates minimal-transversal enumeration and transversal-hypergraph dualization as a longstanding problem and gives bounded-VC-dimension results [SRC-MARY-2024-MINIMAL-TRANSVERSALS].

Therefore R004 does not claim minimal hitting sets, transversal hypergraphs, blocker duality, or general monotone Boolean dualization as inventions.

## 2. Clutters / antichains are prior combinatorics

The family of inclusion-minimal deletion cuts is a clutter (Sperner family): no cut contains another. Standard antichain theory therefore supplies generator-side cardinality bounds. R004 uses those bounds only after producing the cut family from a future-safe compiler.

## 3. Minimal semigroup generating sets remain prior art

Supplement 15 already maps finite transformation-semigroup generation/rank and minimum generating-set problems as prior mathematics. Supplement 17's semantic reconstruction closure reuses that boundary for unary operation terms and similarly delegates semiring-generation questions to their established algebraic setting.

## 4. Project-local reduction under test

R004's WIP addition is restricted to:

1. define the monotone carrier adequacy predicate `Phi(S)=[Compile_S(P0)=Q*]` for a typed future-safe compiler;
2. identify inclusion-minimal generator deletions that change the carrier as a carrier-cut clutter;
3. prove that each minimal cut `H` has the canonical compiler-generated forbidden-world witness `P_H=Compile_(G\H)(P0)` with exact kill set `H`;
4. replace the Bell-number forbidden-partition hitting problem by minimal transversals of the generator cut clutter;
5. define a separate quotient-level semantic reconstruction adequacy predicate;
6. prove the typed joint-cut decomposition `C_joint=Min(C_car union C_sem)`;
7. interpret minimal transversals of `C_joint` as adequate primitive instruction sets preserving both world generation and requested descended semantics.

Historical novelty of this exact Enterprise Math reduction and selected finite certificates remains `NOVELTY_UNVERIFIED`.
