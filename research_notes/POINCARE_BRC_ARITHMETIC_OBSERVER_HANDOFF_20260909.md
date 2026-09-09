# Poincaré / 3-sphere recognition — BRC arithmetic-observer durable handoff

Status: `RESEARCH FRONTIER / PROVED SUBLEMMA + OPEN ALGORITHMIC ROUTE`
Researcher provenance: `EM-FREE-P3K7Q2 / FREE_AXIOM_DISCOVERY`
Prepared for successor researchers: `2026-09-09`

## 1. Mother route

Revisit the Poincaré / 3-sphere-recognition problem using Enterprise Math / Progress Number Theory without merely renaming Ricci flow. The productive interface found in the originating research is exact normal-surface integer coordinates plus BRC branch/observer discipline.

The core route is:

`triangulation -> normal/almost-normal integer coordinates -> quadrilateral/octagon branch tree -> integer-lattice target obstruction -> finite mod p^k character certificate -> exact subtree pruning`.

A complementary non-abelian route is:

`integer homology sphere -> pi_1 presentation -> irreducible SL(2,C) representation when non-spherical -> finite-field representation / witness-prime certificate`.

## 2. Exact durable source from the originating run

Primary source record:

`awdawmip/chatgpt-global-knowledge@c63167f2f911e2425b8a70b0aabcc90574425235:knowledge/projects/enterprise-math/poincare-brc-normal-surface-arithmetic-observer-20260905.md`

That record contains the full derivation, literature audit boundary, BRC typing, and status labels. Successors must read it before claiming novelty or changing theorem strength.

Relevant reusable Enterprise/global findings recorded before this route:

- `SMITH_LOCAL_SUPPORT`
- `MODULAR_EXACT_LINEAR_ALGEBRA`
- `FINITE_OBSERVER_COMPLETENESS`
- `GROEBNER_CERTIFICATE_BRIDGE`
- `EFFECTIVE_CHEBOTAREV_BOUNDED_WITNESS`
- account-wide BRC contract `knowledge/procedures/BRC_RESEARCH_PRIORITY_AND_USAGE_20260905.md`

## 3. Proved derivation: branch-cokernel necessary obstruction

For a triangulation `T` with `n` tetrahedra, standard normal coordinates are nonnegative integers satisfying integer matching equations and the quadrilateral constraint. Fix a quadrilateral-type branch `sigma` by retaining at most one quadrilateral type per tetrahedron. Let `A_sigma` be the resulting integer matching matrix.

Euler characteristic is linear in standard normal coordinates. After clearing denominators by an integer `D>0`, use an integral row `ell_sigma` with

`ell_sigma(x)=D*chi(x)`.

For the target `chi=2`, define

`M_sigma = [A_sigma; ell_sigma^T]`,

`b = (0,...,0,2D)^T`.

Every normal 2-sphere in branch `sigma` yields a nonnegative integer solution of

`M_sigma x = b`.

Hence

`omega_sigma(T) := [b] in coker(M_sigma : Z^{d_sigma} -> Z^{m+1})`

is an exact necessary obstruction. If `omega_sigma(T) != 0`, the whole branch contains no target normal sphere.

Boundary: `omega_sigma=0` is not an existence theorem; nonnegativity, actual admissibility, connectedness/nontriviality, and the remaining topological recognition conditions still matter.

## 4. Proved derivation: finite congruence separator

For any integer matrix `M` and target `b`, if `b notin im_Z(M)`, finite generation of the cokernel gives a finite cyclic quotient separating `[b]`. Therefore there exist a prime power `q=p^k` and a row vector/character `y` such that

`y^T M = 0 (mod q)`

while

`y^T b != 0 (mod q)`.

So every lattice-infeasible branch has a finite modular certificate. Smith normal form gives a canonical route to the relevant prime-power support; modular verification is cheap and exact.

## 5. Proved derivation: partial-branch monotone pruning

For a partial quadrilateral assignment `beta`, delete only columns forbidden by decisions already made and leave all choices available in undecided tetrahedra, giving the relaxed matrix `M_beta`.

Every descendant `gamma` deletes more columns, so

`im_Z(M_gamma) subseteq im_Z(M_beta)`.

Therefore

`b notin im_Z(M_beta) -> b notin im_Z(M_gamma)`

for every descendant. One separator at depth `k` can prune the entire descendant subtree. For a ternary quadrilateral branch tree, an antichain of first-pruned nodes `P` removes search-leaf mass

`W_pruned(P)=sum_{beta in P} 3^(n-|beta|)`.

This is an algorithmic BRC statistic, not a topological invariant and not a count of distinct surfaces.

## 6. Almost-normal extension

The same equality-relaxation architecture should apply to the octagonal almost-normal stage used in Rubinstein–Thompson recognition. Fixing the exceptional octagon location/type produces an inhomogeneous integer target system suitable for the same cokernel / mod-`p^k` prefilter. This extension is structurally justified but still needs an implementation-level exact coordinate adapter and benchmark.

## 7. Hard information-loss wall

Pure homology / Smith-normal-form observers cannot solve Poincaré recognition alone. The Poincaré homology sphere has the same integral homology as `S^3` but nontrivial fundamental group (binary icosahedral group, equivalently `SL(2,F_5)`). Therefore a final acceptance/rejection architecture must retain a non-abelian observer layer or an independent topological acceptance theorem. Do not silently infer simple connectedness from homology.

This motivates the complementary `SL(2,C) -> finite-field` certificate route associated with Zentner / Heusener–Zentner / Kuperberg-type results. GRH-conditional and unconditional statements must remain separately tagged.

## 8. Pachner no-go and open extension

Because Pachner moves are reversible, no nonconstant scalar depending only on the bare triangulation can strictly decrease under every nontrivial Pachner move. Any Perelman-like discrete monotone must include an oriented simplification protocol or enlarged state, e.g. `(triangulation, branch/recognition/geometric state)`.

Open but lower-priority direction: define and test a Pachner-covariant obstruction profile carrying branch lattices, `p`-primary cokernel data, and surviving BRC search mass across local bistellar moves.

## 9. Prior-art boundary already established

Known prior art includes normal/almost-normal coordinates, quadrilateral constraints, Hilbert-basis/fundamental-surface methods, LP/tree traversal feasibility, Rubinstein–Thompson 3-sphere recognition, Burton quadrilateral–octagon coordinate optimizations, Perelman’s Ricci-flow proof, and finite-representation recognition routes.

The exact claim preserved from the originating audit is narrower: no focused source was found using the Smith/cokernel finite-character observer specifically as a partial normal-sphere branch-pruning layer. This is not a novelty proof. A successor must perform a deeper literature/code audit before claiming originality.

## 10. Recommended task decomposition

1. **Experimental/integration task:** implement incremental integer-lattice / modular-character pruning in a normal-surface branch traversal and benchmark on `S^3`, lens spaces, Poincaré homology sphere, and hyperbolic homology-sphere census inputs.
2. **Exact-certificate task:** formalize the branch-cokernel separator, incremental update rules, certificate checker, and almost-normal octagon adapter; state precise conditions under which a cached separator survives descendants.
3. **Non-abelian observer task:** build a finite-field representation certificate pipeline for integer-homology-sphere non-sphericity, reusing the existing Gröbner-certificate and effective witness-prime tools and preserving GRH tags.
4. **Lower-priority exploratory task:** test whether a Pachner-covariant obstruction profile exists; kill quickly if local moves destroy any useful comparability beyond trivial invariants.

## 11. Do not overclaim

Not established:

- a new proof of the Poincaré conjecture;
- polynomial-time 3-sphere recognition;
- a worst-case asymptotic improvement over existing exponential search;
- novelty of the pruning mechanism after a complete literature/code audit;
- sufficiency of the abelian obstruction;
- a triangulation-invariant scalar entropy.

## 12. Smallest next action

Start with the experimental task on a minimal exact adapter: given a triangulation and a partial quadrilateral assignment, construct `M_beta,b`, compute either exact Smith/cokernel nonmembership or a small prime-power separating character, and measure subtree mass pruned before the existing expensive normal/almost-normal feasibility machinery runs.
