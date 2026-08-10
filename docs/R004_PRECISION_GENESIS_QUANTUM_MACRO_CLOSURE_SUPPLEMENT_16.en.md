# R004 precision genesis — Supplement 16: structural obstruction clutter and carrier-basis duality

Status: `PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_REDUCTION + P023_BOUNDARY`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_15.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 15 reduced carrier-minimal generator selection to hitting every forbidden coarse partition. The open problem was whether the Bell-number family of forbidden partitions can itself be replaced by a smaller complete obstruction object. This supplement answers that question exactly on the generator side.

The generic hypergraph-transversal/blocker theory used below is prior art. R004's contribution is the reduction from a typed future-safe compiler to a minimal deletion-cut clutter equipped with canonical forbidden-world witnesses.

## 1. Setup

Let `G` be a finite set of typed future-language generators, `P0` an initial observation partition, and

`Q* = Compile_G(P0)`

the unique coarsest jointly safe refinement under the declared compiler semantics.

For a retained generator set `S subseteq G`, write

`Q_S = Compile_S(P0)`.

Because every `S`-safe condition is contained in the full `G` condition, `Q*` refines every `Q_S`. Therefore the Boolean carrier-adequacy predicate

`Phi(S)=1 iff Q_S=Q*`

is monotone under generator inclusion:

`S subseteq T and Phi(S)=1 => Phi(T)=1`.

## 2. R004-COMP-T24 — minimal carrier cuts

A deletion set `H subseteq G` is **carrier-breaking** when

`Compile_(G\H)(P0) != Q*`.

Let

`C_G(Q*) = Min_subseteq { H subseteq G : H is carrier-breaking }`.

Because this family is inclusion-minimal, `C_G(Q*)` is a clutter/antichain on the generator set.

Its elements are the **minimal carrier cuts**: every generator in a cut is jointly necessary for that particular failure mode, but no proper sub-deletion already causes that failure.

## 3. R004-COMP-T25 — canonical forbidden-world witness theorem

For each minimal cut `H in C_G(Q*)`, define

`P_H = Compile_(G\H)(P0)`.

Then `P_H` is a forbidden coarse world (`P_H != Q*`) and its full-language kill set is exactly

`K(P_H)=H`,

where

`K(P)={g in G : g is unstable/illegal on P}`.

Proof. `P_H` is stable for every generator outside `H`, so `K(P_H) subseteq H`. If some `h in H` were also stable on `P_H`, then `P_H` would be stable for `G\(H\{h})`. But minimality of `H` says deleting the proper subset `H\{h}` must preserve `Q*`, so no strictly coarser forbidden stable refinement can exist. Contradiction. Hence every `h in H` kills `P_H`.

Thus each generator cut has a canonical coarse-state certificate produced by the compiler itself; no external search over partitions is needed to construct the witness once the cut is known.

## 4. R004-COMP-T26 — minimal kill sets are exactly minimal cuts

Conversely, let `P` be any forbidden partition between `P0` and `Q*`, and suppose its kill set `K(P)` is inclusion-minimal among all forbidden-world kill sets.

Because `P` is stable under `G\K(P)`, deleting `K(P)` is carrier-breaking. If a proper subset of `K(P)` were already carrier-breaking, its canonical failed compiler output would have a strictly smaller forbidden kill set, contradicting minimality. Therefore

`K(P) in C_G(Q*)`.

So the two finite objects coincide exactly:

`minimal forbidden kill sets = minimal carrier deletion cuts`.

Many forbidden partitions may share the same kill set; `P_H` gives one canonical coarsest witness for the cut type.

## 5. R004-COMP-T27 — Structural Obstruction Basis

Define

`O* = { P_H : H in C_G(Q*) }`.

Then a retained set `S subseteq G` preserves the full carrier `Q*` iff it kills every canonical obstruction world in `O*`, equivalently iff

`S cap H != empty`

for every `H in C_G(Q*)`.

Therefore the inclusion-minimal Carrier Bases are exactly the minimal transversals of the carrier-cut clutter:

`B_C = Tr(C_G(Q*))`.

This is the exact replacement for Supplement 15's Bell-number forbidden-partition universe.

The earlier pairwise-merge no-go remains important: `O*` cannot generally be replaced by pair distinctions or immediate coarsenings of `Q*`. A generator may kill every one-pair merger and still allow a larger multi-block merger. Structural obstruction types live on generator cuts, not on state pairs.

## 6. Blocker duality

Since `C_G(Q*)` is a clutter, standard hypergraph blocker duality gives

`Tr(Tr(C_G(Q*))) = C_G(Q*)`.

Hence minimal sufficient Carrier Bases and minimal carrier-breaking cuts determine one another:

`B_C = Tr(C_G)`,

`C_G = Tr(B_C)`.

This is prior hypergraph duality, not a new theorem of R004. The project-level result is that the Representation Compiler produces a concrete monotone Boolean function whose minimal true sets and maximal-failure complements instantiate that duality.

## 7. Generator-side complexity bound

If `m=|G|`, every minimal cut is an incomparable subset of `G`. By the classical antichain bound,

`|C_G(Q*)| <= binom(m, floor(m/2))`.

The same bound applies to the family of inclusion-minimal Carrier Bases.

This can still be exponential in `m`; no polynomial algorithm is claimed. But the obstruction universe is now generator-side and independent of the Bell number of the exact-state carrier.

The relevant computational problem is monotone Boolean / hypergraph dualization over the generator bits, with the compiler used as a membership oracle for `Phi(S)`.

## 8. Integer optimality certificates revisited

Supplement 15's disjoint-forbidden-world lower bound is now the ordinary matching lower bound in the carrier-cut clutter.

If `D subseteq C_G` is a pairwise generator-disjoint cut family, every carrier basis must contain at least one different generator for each cut:

`|S| >= |D|`.

If a candidate basis `S` has `|S|=|D|`, cardinality optimality follows with an entirely finite/integer certificate.

Likewise, an inclusion-minimal basis has the standard private-cut property: for every retained generator `g`, some cut edge intersects the basis only in `g`.

## 9. Validation

Independent exhaustive validation used the unified mixed typed compiler from Supplement 14.

On the complete 3-state family containing:

- one total unary generator;
- one partial unary generator (disabled or one of three target states at each source state);
- one loopless COUNT-relation generator;
- every initial set partition;

there are **552,960** full language instances.

For every instance, exact subset enumeration verified simultaneously:

1. minimal carrier deletion cuts equal inclusion-minimal forbidden-world kill sets;
2. each canonical witness `P_H=Compile_(G\H)(P0)` has `K(P_H)=H`;
3. inclusion-minimal Carrier Bases equal the minimal transversals of the cut clutter.

No violations were found.

The executable reference is `src/enterprise_math/precision_structural_obstruction_basis.py` with direct regressions in `tests/test_precision_structural_obstruction_basis.py`.

No fresh full-repository CI or canonical-main theorem status is claimed.

## 10. Prior-art boundary

Established mathematics includes hypergraph transversals/minimal hitting sets, clutter blockers, monotone Boolean dualization, Sperner antichain bounds and minimal-cut/minimal-transversal algorithms. Source mapping is recorded in `docs/PRIOR_ART_R004_STRUCTURAL_OBSTRUCTION_BASIS.*` and `sources_r004_structural_obstruction_basis.json`.

R004 claims only the typed-compiler reduction:

`future-safe compiler -> monotone generator adequacy -> minimal carrier cuts -> canonical forbidden worlds -> minimal carrier bases`.

Historical novelty of this exact Enterprise Math reduction/certificate package remains `NOVELTY_UNVERIFIED`.

## 11. Next

Carrier preservation is only half of a primitive instruction set. Supplement 17 adds quotient-level semantic reconstruction and shows that carrier cuts and semantic cuts combine into one typed adequacy clutter whose minimal transversals are the minimal adequate primitive instruction sets.
