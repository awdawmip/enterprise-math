# Split-prime boundary extension: 5/7/13/19 and a finite collision spectrum

Status: RESEARCH_NOTE / DERIVATIONS_AND_EXACT_FINITE_CHECKS / NOT_PROMOTED
Progress-Event-ID: NOLLM-SPLIT-EXTENSION-20260909-C6C82
Researcher-ID: EM-DIRECT-C6C82
Research-Activity-ID: RA-nollm-hecke-views-20260909-c6c82
Session: local-chat-nollm-hecke-20260909-c6c82 (local key, not a server ID)
Mode: TASK_RESEARCH / direct continuation / no formal Task-ID or CLAIM
Date: 2026-09-09
Source snapshot: enterprise-math@e9f7310b192a07431ccc15597afdfd2c6091113d
Parent note: research_notes/nollm_mixed57_boundary_compatible_selector_20260909_c6c82.md at 052dee375c2875b9e36119280be4f48115337978
Parent code: experiments/nollm_mixed57_boundary_repair_20260909_c6c82.py at 1069515fcb70c38e55cbf84dd317accabd897477
Parent code SHA256: fced7c21cc5fdd597381094531454e5b5d37711cd514b64c79b02989ced205fa
Executable: experiments/nollm_split_prime_extension_20260909_c6c82.py at b8c099329b1949becf544599e86fcf32045ccebc

## 1. Scope and correction record

Reuse the parent's four recorded activity checkpoints and six-shape coprime quotient field. Geometry below is ordinary rank-two integer lattice mathematics with Q(q,r)=q^2+qr+r^2, a comparison/research slice, not a P000 or Nollm runtime change. Index multiplication is not ordinary scalar-label multiplication in the plane.

Adding 13 needs no change to the old anchors. Adding 19 exposes an exact failure; three anchors are then changed. Future address stability applies within the new convention, not to migration from every old boundary address.

Readback correction: the first draft accidentally printed factors 3 and 4 in the two mod-5 matrix equalities. The correct equalities are G13=G7^3 and G19=G7^2 modulo 5, with scalar factor 1 in both cases. The phase shifts and experiments were already correct. The executable now explicitly asserts both equalities. This note replaces the displayed algebra error without changing the research scope or prior events.

## 2. New similarities, unchanged six-state atlas

Reuse W=[[0,-1],[1,1]], G7=[[1,-2],[2,3]], and the parent's determinant-5 bases:

H0=[[2,-1],[1,2]], H1=[[-2,1],[-3,-1]], H2=[[-2,-1],[1,-2]],
H3=[[-1,2],[0,-5]], H4=[[-3,-1],[2,-1]], H5=[[-5,0],[2,-1]].

Put G13=[[1,-3],[3,4]], G19=[[2,-3],[3,5]]. They are commuting Eisenstein similarities of determinants 13 and 19, satisfying Q(Gp x)=p Q(x).

Their inverse actions on the six projective lines modulo 5 shift j by 3 and 2 respectively; G7 shifts by 1. Indeed

G13 mod 5 = G7^3 mod 5 = [[1,2],[3,4]],
G19 mod 5 = G7^2 mod 5 = [[2,2],[3,0]].

For exponents a,b,c,d of 5,7,13,19 set a=2t+epsilon,

j=b+3c+2d mod 6, U=G7^b G13^c G19^d,
P(a,b,c,d)=5^t W^t U H_j^epsilon.

This is a basis for the intersection of the four component prime-power lattices. Containment in each component and the product index 5^a7^b13^c19^d prove equality. Coprime lattice CRT gives the quotient identity. Right transitions P(s)^(-1)P(s+e_p) are integral of determinant p; their products around squares telescope to the same endpoint. Local digit ranks may permute when the order changes.

The six-valued shape phase is not the full state: retain exponents, Euclidean similarity, lattice basis and quotient residue separately.

## 3. Compatible 13 and an exact old-selector failure for 19

There are no shared facet normals between H_j and G13 H_(j+3), for any j; regular even sections share none with their 13-successors either. Therefore the old 5/7 selector extends to 13 without new boundary comparisons.

For 19, j=1,3,5 respectively retain the facet pairs

+/- (2,3), +/- (3,-5), +/- (5,-2), all of norm 19.

At s=(5,1,0,0), the old rule selects x=(121,39) but rejects it after one 19-refinement. The competitor is y=(-104,-61):

Q(x)=Q(y)=20881, x-y=(225,100).

Old source secondary/tertiary keys: x=(9646875,765625), y=(37975000,12250000), so x wins. Successor keys: x=(276390625,6909765625), y=(-276390625,6909765625), so y wins. Negation supplies the second lost point. Small-scale tests can miss the problem because short shared facets need not initially contain the relevant integer points.

This falsifies the old selector, not all possible 19 extensions.

## 4. Three anchor changes repair the four-prime field

Retain the parent's odd-section key, compared lexicographically:

(Q(x), -d_u(x)c_u(x), d_u(x)^2),
where d_u(x)=2<u,x>_hex and c_u(x)=det(u,x).

Use normalized anchors

u0=(-3,1), u1=(-1,3), u2=(-1,-2),
u3=(-3,2), u4=(-2,3), u5=(-2,-1).

Only u1,u3,u5 change; all six have norm 7. On an odd section the physical anchor is 5^t W^t U u_j. On even sections retain the parent's positive-chirality regular-hex boundary rule.

For normal v define A(u,v)=d_u(v)^2-3c_u(v)^2. On the facet d_v(x)=Q(v), exact expansion gives

[-d_u(x-v)c_u(x-v)]-[-d_u(x)c_u(x)]
= A(u,v)c_v(x)/(2Q(v)).

Thus A(u,v)>0 agrees with the even chiral choice. At j=1, new u=(-1,3) gives A=4 on the unit normal (-1,1) and A=46 on the outgoing 19 normal (2,3). The old unit anchor gave A=-66 on that 19 normal. The other elongated states have the same positive margins after rotation. All 48 phase/prime cases, including transformed child anchors, have consistent retained comparisons.

Uniqueness and convexity reuse the parent's proofs. The identity d_u(x)^2+3c_u(x)^2=4Q(u)Q(x) makes equal three-term keys determine x up to sign. An odd-order quotient cannot have distinct antipodes among shortest representatives of one class. Differences of each quadratic comparison are affine, and the lexicographic comparison cone is convex; hence odd sections contain every integer point in their convex hull. Even sections retain the regular-hex contiguous-half-side proof. No integer side midpoint or regular Voronoi corner occurs, since the similarity index is coprime to 6.

For nested lattices a shortest parent remains shortest for the child. Only retained co-nearest facet comparisons require agreement; the exact finite certificate supplies it at all scales. Thus each section has one representative per class, central symmetry, no missing convex-hull lattice sites, and C6 symmetry at even a. Every selected point remains selected under future refinement in any of the four directions. The new rule selects y rather than x already at the source of the witness; this is a boundary migration, not preservation of all old-version addresses. Odd bulk anisotropy remains.

## 5. Finite exceptional-prime criterion

All facet-relevant vectors of I,H0,...,H5 have squared norms in exactly

{1,3,7,19}.

If an integral hex similarity E of prime determinant ell creates a shared facet normal v between H_i and E H_j, then v=Ew for a child facet normal and

Q(v)=ell Q(w).

Since Q(w) is a positive integer, ell divides one of 1,3,7,19. Among split primes ell=1 modulo 3, only 7 and 19 qualify. Hence 13 and every split prime greater than 19 introduce no new shared-facet decisions in THIS finite-shape family. This is an all-prime exclusion argument, not numerical extrapolation.

Consequently the repaired selector extends to any finite collection of distinct split primes: retain 1+2omega for the 7 direction and 2+3omega for 19 when present; choose one norm-ell Eisenstein generator for each other split prime. The norm-prime representation is classical; equivalently read the statement conditional on supplying these integral similarities. Keep the given 5-chain as the only inert-prime direction.

Modulo 5 each such E is invertible and commutes with G7. G7 acts as a six-cycle on the six lines, so every commuting permutation is a power of that cycle. With s(E) its shift, j=sum e_ell s(E_ell) mod 6 still suffices for the normalized shape. There is no growing shape atlas from adding these split primes; exponent and geometric bit costs still grow. Another inert prime is outside this argument. Different associates/conjugates of the chosen 7 or 19 generators require rechecking those exceptional constraints.

## 6. Local cost: complete polygons, not an inherited cutoff

Reuse the parent's exact rational Voronoi/Minkowski polygon compiler but not its old radius<6 cutoff, which was proved only for 5/7. Enumerate all integer vectors in each exact rational polygon bounding box and retain those inside.

Maxima over the six states and both parities:

5: 17 candidates, 5 children;
7: 19 candidates, 7 children;
13: 27 candidates, 13 children;
19: 43 candidates, 19 children.

These bounds are depth-independent for each fixed prime. Uniform materialized fanout independent of ell is impossible, since a fiber has ell members. Fixed finite shape distortion implies Minkowski area ell+O(sqrt(ell))+O(1) and perimeter O(sqrt(ell))+O(1); covering boundary cells gives ell+O(sqrt(ell)) candidate count. This is not a bound on integer bit cost. No <=7 physical fanout hierarchy for 13/19 has been implemented. Locality remains in the current lattice basis rather than the finest grid.

## 7. Fresh exact finite validation

- 48 exact phase certificates for shared-facet signs and integral transitions.
- 51 fully enumerated sections; summed cardinalities 997575; maximum 415625.
- Exact residue uniqueness, central symmetry and zero convex-hull lattice holes throughout; complete C6 set equality and exact covariance identities for even a.
- 89 full refinement edges; 45175 parents checked for exact prime degree and future stability.
- 288 exact matrix commuting squares on a bounded exponent grid.
- 132 complete permutation runs: all six orders for three-prime groups and all 24 orders for four-prime groups, from multiple starting sections. There are 3187800 descendant appearances, including repeated endpoint sets; zero order mismatches.
- The explicit old-19 failure and the repaired representative are checked.
- The packaged executable was independently rerun and the core result JSON matched byte-for-byte.

Example consecutive indices: 5,35,455,8645,43225. Numerical cloud standard-deviation axis ratios: 1.73205,4.43115,1.50159,1.49936,1.00000. The last index is 5^2*7*13*19 and its C6 property is checked exactly, not inferred from the rounded ratio.

## 8. BRC reuse, interpretation and unresolved boundary

REUSE_EXECUTED: hash-pinned predecessor boundary selector, mixed57 lattice geometry, rational stencil polygons, integer hull and baseline functions. EXTEND_EXISTING_TOOL: task-local exponent adapter, selector anchors and complete polygon enumeration, not a new global toolbox family. COMPOSE_APPLIED: keep coset identity and branch provenance; compress only the finite projective shape permutation. The short-vector norm support suffices to EXCLUDE new shared-facet constraints; it is not a complete lattice or semantic-neighborhood representation.

Resolved here: compatible 13, exact 19 failure and repair, four-prime finite tests, finite exceptional-prime criterion, and the stated conditional split-prime-family extension.

Unresolved: another inert direction such as 11, 2/3 directions, ordinary integer-label multiplication as an intrinsic planar operation, arbitrary-prefix uniformity, physical fanout integration and semantic memory quality. Persistence implies no Foundation, Working Truth or theorem acceptance.

Classical comparisons: Li-Gan-Ling, Coprime Sensing via Chinese Remaindering over Quadratic Fields, Part I, arXiv:1808.07505; Natarajan-Hong-Viterbo, Lattice Index Coding, arXiv:1410.6569. CRT, ideal lattices and finite-field actions are classical. This research claims only the explicit selector compatibility, negative witness and exceptional-prime synthesis within the declared model, not novelty of those ingredients.
