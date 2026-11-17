# P000 S4 扩张外部先例与48元中央非分裂例（2026-11-17）
Task: RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT
Frozen publication: TP2-2F8C6A1D9E7043B5C812
Mode: author-side scoped mathematical/literature research; no independent Driver acceptance.

## Twelve-item external-prior-art map
| V8 item | Classification | Scope |
|---|---|---|
| 1 short exact group extension | EXACT_DUPLICATE | 1→K→E→S4→1 is classical |
| 2 split section, complement, semidirect | EXACT_DUPLICATE | split iff there is a homomorphic section |
| 3 relation residues landing in K | EXACT_DUPLICATE | a lifted relator projects to identity; simultaneous removal is a stronger condition |
| 4 H² with abelian/central K | EXACT_DUPLICATE under hypotheses | fix abelian S4-module K; central case uses trivial action; class zero iff split |
| 5 nonabelian extension Schreier/Mac Lane | EXACT_DUPLICATE in abstract setting | prescribed outer action S4→Out(K), obstruction H³(S4,Z(K)), when realized classes form an H²(S4,Z(K))-torsor |
| 6 change of section/complement conjugacy | PARTIAL_ANTECEDENT | factors change with lifts; complement uniqueness/conjugacy require extra hypotheses |
| 7 natural S4 four-point and six-edge action | EXACT_DUPLICATE | induced permutation action on 2-subsets; 24-element faithful images |
| 8 minimal faithful permutation degree 4 | EXACT_DUPLICATE | n!<24 for n≤3, four-point action exists |
| 9 projective and covering analogies | ADJACENT_METHOD | only when exact kernel/action and extension hypotheses match |
| 10 automorphism-invariant canonical-choice obstruction | EXACT_DUPLICATE of general criterion | first verify symmetries preserve complete primitive P000 structure |
| 11 existence in one model vs universality | EXACT_DUPLICATE of quantifier distinction | Gen12 single-model existence supplies no ∀-model lift |
| 12 P000 opaque Cell + no quotient + typed axes + PF-10 | NO_MATERIAL_MATCH within cited finite audit | classical components exist separately; NO_MATERIAL_MATCH != NOVELTY |

## A: precise split criterion
Let E→S4 be any group extension with kernel K, possibly nonabelian. Let a=(BCD), b=(AB), so a^3=b^2=(ab)^4=1 and a,b generate S4. The spherical (3,2,4) triangle group has order 24 (independent SymPy FpGroup enumeration: 24), hence this is a complete presentation of S4. For lifts A,B in E, the three relation values A³, B², (AB)⁴ lie in K. There is a homomorphic section iff SOME pair of lifts has all three values equal to 1. This equivalence does not require K abelian. A nontrivial residue for just one arbitrary lift does not by itself prove nonsplitting.

For abelian K=A with fixed induced S4-module structure, a normalized section s produces f(g,h)=s(g)s(h)s(gh)^-1∈A satisfying a 2-cocycle equation. A change of section modifies f by a coboundary. [f]=0 iff split, by classical H²(S4,A) theory. For nonabelian K, conjugation descends canonically only to Out(K), and the factor set must be paired with its lift-dependent automorphisms.

## B: 48-element exact counterexample to universal splitting
Define E={(g,j)∈S4×Z/4 : sign(g)=j mod 2}, with componentwise multiplication. The projection to g is onto and its kernel is {(id,0),(id,2)}≅C2, central in E; |E|=48.
If E→S4 had a homomorphic section s(g)=(g,u(g)), u:S4→Z/4 would be a homomorphism with u(g) mod2=sign(g). But S4^ab=C2 forces its image inside {0,2}, making u mod2 zero. Contradiction for odd g, so the extension is nonsplit.
Choose a=(BCD), b=(AB), A=(a,0), B=(b,1). The lifted residues are A³=1, B²=(id,2)≠1, (AB)⁴=1. Either lift of b (with j=1 or3) has square (id,2), so no adjustment removes the B² residue. All assertions were exhaustively checked in the attached stdlib-only checker over 24 S4 elements and 48 E elements.
This example concerns ordinary group extensions; it is NOT a physical countermodel to root P000.

## Frozen Gen12 comparison
Gen12's exact four opaque Full-Cell common model with six K4-edge typed axes, uniform PF-10/connection and generators r_a,r_b already realizes a faithful 24-element action and all three exact relation equalities, with trivial forgetful kernels in that declared model. This is classical S4 representation structure instantiated with project-specific typed data; retain original author attribution and no-quotient Cell semantics. V7 had already classified torsor/frame/holonomy and emphasized TRIVIAL_HOLONOMY rather than generic flatness for globally synchronized frames. No re-proof of V7 is claimed.

## Authority-based source ledger
- Brian Conrad, Stanford, Extensions and H²(G,A): https://math.stanford.edu/~conrad/210BPage/handouts/Cohomology%26Extensions.pdf (abelian K, fixed module action, cocycle and split).
- S. Eilenberg, S. Mac Lane, Ann. Math. 48 (1947), 326–341, DOI 10.2307/1969174, Cohomology Theory in Abstract Groups II (nonabelian kernels, outer actions and 3-dimensional obstruction).
- Cambridge University Press, Group extensions by non-abelian kernels (chapter 7): https://www.cambridge.org/core/books/abs/lie-groups-lie-algebras-cohomology-and-some-applications-in-physics/group-extensions-by-nonabelian-kernels/F1678715693CB37557E12C060204AE93
- Stanford group-theory Geometry and Groups: https://crypto.stanford.edu/pbc/notes/group/geometry.html (24-element octahedral S4 action).
- Project frozen task and V7/Gen12 inputs pinned at enterprise-math@805a2834521bbd34855b025ad5e710fc0502b14e.

## Remaining scientific frontier
The Gen13 exact lift and actual nonabelian kernel/relations require their own pinned source study. A complete per-claim external citation crosswalk can refine borderline classes. The classification above is within the explicit external group-theory comparison; the P000 Full-Cell compound ontology is retained without a quotient or universal/canonical promotion.