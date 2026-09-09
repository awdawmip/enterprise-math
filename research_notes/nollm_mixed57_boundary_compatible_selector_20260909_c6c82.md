# Mixed 5/7 boundary-compatible selectors: solid sections without a common global order

Status: RESEARCH_NOTE / DERIVATIONS_AND_EXACT_FINITE_CHECKS / NOT_PROMOTED
Progress-Event-ID: NOLLM-MIXED57-BOUNDARY-REPAIR-20260909-C6C82
Researcher-ID: EM-DIRECT-C6C82
Research-Activity-ID: RA-nollm-hecke-views-20260909-c6c82
Session: local-chat-nollm-hecke-20260909-c6c82 (locally assigned key, not a server ID)
Mode: TASK_RESEARCH / direct continuation / no Task-ID or CLAIM
Date: 2026-09-09
Source snapshot: enterprise-math@108ac80d4af9a1ebe19cc613aaccb7402564100e
Parent: research_notes/nollm_mixed_5_7_intersection_carry_20260909_c6c82.md at adc999842597c0d4d3458e1d3a9b79378d207640
Executable: experiments/nollm_mixed57_boundary_repair_20260909_c6c82.py at 1069515fcb70c38e55cbf84dd317accabd897477

## 1. Exact scope and recovered frontier

The parent already supplies the mixed coprime intersection lattice family, six intermediate shapes, an exact commuting refinement square, and complete phasewise stencils of at most 19 candidates. Its global sixth-power tie order can leave boundary holes on odd sections. This turn changes only the section selector. The lattice family, matrices, quotient identity and stencil geometry are unchanged.

This is ordinary rank-two integer lattice mathematics, viewed through the hex metric Q(q,r)=q^2+qr+r^2. It is a comparison/research slice, not a change to P000 or Nollm runtime. Index/refinement multiplication is NOT scalar multiplication of ordinary integer labels. No Foundation, Working Truth or mathematical acceptance is claimed by persistence.

## 2. Parent geometry and the six anchors

Let W=[[0,-1],[1,1]], G=[[1,-2],[2,3]], and write a=2t+epsilon, j=b mod 6. Reuse

P(a,b)=5^t W^t G^b H_j^epsilon,
L(a,b)=P(a,b) Z^2,
[Z^2:L(a,b)]=5^a 7^b.

Here H_j^0 means I, and the determinant-5 matrices H_j are

H0=[[2,-1],[1,2]], H1=[[-2,1],[-3,-1]],
H2=[[-2,-1],[1,-2]], H3=[[-1,2],[0,-5]],
H4=[[-3,-1],[2,-1]], H5=[[-5,0],[2,-1]].

Use these anchor vectors in the normalized frame:

j:    0       1        2        3       4        5
u_j: (-3,1)  (-1,1)  (-1,-2)  (-1,0) (-2,3)  (0,-1).

For even j, +/-u_j are precisely the facet normals shared by V(H_j) and V(G H_(j+1)); Q(u_j)=7 and G u_(j+1)=+/-u_j. For odd j, +/-u_j are the normals shared by V(I) and V(H_j); Q(u_j)=1. V(P) denotes the Euclidean Voronoi polygon of P Z^2, expressed in axial coordinates.

The physical anchor on an odd section is u=5^t W^t G^b u_j. Its sign is irrelevant to the quadratic score below.

## 3. New selector: minimum distance, then a boundary-compatible quadratic comparison

For axial vectors u,x, define

d_u(x)=2<u,x>_hex=2u_q x_q+u_q x_r+u_r x_q+2u_r x_r,
c_u(x)=u_q x_r-u_r x_q.

On every odd section choose the minimum representative in each coset using

K_u(x)=(Q(x), -d_u(x)c_u(x), d_u(x)^2),

in lexicographic order. Only equal-distance choices are affected. No random phase, relaxation, optimizer or whole-section lookup is needed at runtime.

On even sections use the same chiral rule for every regular Voronoi facet: if d_v(x)=Q(v), retain x precisely when c_v(x)>0. Interior points are retained. Here [Z^2:L] is coprime to 6: no integer point lies at a regular Voronoi vertex or side midpoint. Thus every tied class has exactly two candidates and the opposite facet receives the complementary choice. The rule is invariant under W and negation.

### Uniqueness on odd sections

The identity

d_u(x)^2+3c_u(x)^2=4Q(u)Q(x)

shows that equal Q, equal -dc and equal d^2 determine x up to sign. Distinct antipodes cannot both be shortest representatives of one coset of an odd-index lattice. Indeed 2x in L implies x in L since multiplication by 2 is invertible on Z^2/L, and the shortest representative of that coset is zero. Therefore the three-term key determines a unique integer representative; an arbitrary final coordinate tie is unnecessary.

Because the three quantities are even functions, the section is centrally symmetric. Its exact centroid is zero at every depth.

## 4. Why every section has no missing lattice sites

For any fixed lattice vector v, compare x and x-v under the three-term quadratic key. The difference of each quadratic form at these two points is AFFINE in x. The lexicographic nonnegative cone is convex, so the set defined by the lexicographic comparison is convex. Intersect these sets over v in L. Its integer points are exactly the selected representatives. Consequently

S(a,b)=conv(S(a,b)) intersect Z^2

for odd sections. This is an elementary convexity proof, not an extrapolation from tests. The indefinite secondary quadratic is harmless: the primary positive definite Q makes each coset minimization well-defined, and affine comparison sets give the needed convexity.

For even sections all strict-interior lattice points are retained. On each supporting facet the retained boundary lattice points form one contiguous open half-side. The omitted half-side cannot enter the convex hull of the retained points on that supporting line, and there are no integer vertices or midpoints. This gives the same lattice-convexity identity.

At even depth the section is also W-invariant, so its nonzero Euclidean covariance is a scalar multiple of I. Odd sections retain central symmetry but cannot be sixfold symmetric: 5^a 7^b is 5 modulo 6, whereas a finite W-invariant planar point set has cardinality 0 or 1 modulo 6. Odd bulk tight/elongated alternation remains; filling boundary holes does not make those shapes isotropic.

## 5. The key new compatibility argument: only shared boundary decisions matter

A common global total order is SUFFICIENT for stable representatives but is NOT NECESSARY.

For nested lattices L_child subset L_parent, a shortest parent representative remains shortest for the child, because the child's competitor set is smaller. If it becomes a strict-interior point, there is no tie to resolve. If a child competitor remains co-nearest, its difference vector was also a co-nearest parent vector. Thus agreement on these retained boundary comparisons suffices for S_parent subset S_child.

All base shapes here are strict hexagons, not rectangular Voronoi cells; active co-nearest difference vectors are among the six facet-relevant vectors. After stripping the common similarity 5^t W^t G^b, there are only 24 transition types. Their shared-facet certificate is:

- 5, even->odd: none for even j; +/-u_j for odd j;
- 5, odd->even: none for every j;
- 7, even->even: none for every j;
- 7, odd->odd: +/-u_j for even j; none for odd j.

Exact rational polygon intersections verify all 24 types. Similarity scaling and rotation preserve the complete table, so it applies at every a,b.

On a shared facet with normal u, d_u(x)=Q(u) and

[-d_u(x-u)c_u(x-u)]-[-d_u(x)c_u(x)]
=2Q(u)c_u(x).

Hence the odd quadratic rule chooses the SAME side c_u(x)>0 as the even chiral rule. For the odd->odd shared case the successor anchor maps to +/- the same physical u; its quadratic comparison is identical. Side-midpoint ties are impossible on these shared normals, so no tertiary disagreement is left.

It follows for the NEW convention that

S(a,b) subset S(a+1,b),
S(a,b) subset S(a,b+1).

The two coprime quotient projections still commute, and every parent has exactly five or seven canonical children. Both orders around a square reach the same final representatives, with the same 35-element parent fibers. Local digit ranks still undergo a permutation; preserving an unchanged digit word under swapping factors is not claimed.

## 6. The 19-candidate bound survives unchanged

Every selected point still lies in the same CLOSED Voronoi polygon as before. Therefore the parent's exact rational Minkowski-difference stencil certificate applies without modification. The same per-phase candidate lists have size at most 19; precisely five or seven candidates survive the new membership predicate. This is locality in the current lattice basis, not a fixed number of finest-grid moves.

The actual shared-boundary choice is determined by six anchors and the existing phase/orientation state. The optimization solver used during exploration is not part of the executable rule.

## 7. Exact finite validation

The published executable imports the parent's mixed57.py and stencil_proof.py unchanged after SHA256 checks, and those reuse the original unchanged baseline.py.

Results from a fresh complete run:

- 29 complete sections; sum of section cardinalities 1,537,361; largest section 588,245.
- All sections have exactly 5^a 7^b distinct residues, exact central symmetry and no missing lattice points in their convex hulls.
- Every tested even section has complete set-level C6 equality and exact integer covariance isotropy.
- 32 complete refinement edges; 25,176 parents checked for exact five/seven degree.
- 12 complete commuting diamonds; 2,510 parents and 87,850 two-step descendants; zero order mismatches and every parent fiber has size 35.
- All 24 rational shared-facet types checked; every candidate table has at most 19 entries.

Example boundary-hole repairs:

(a,b)  count    old holes  new holes
(3,0)    125        5          0
(3,1)    875        5          0
(3,2)   6125        5          0
(5,0)   3125       25          0
(5,1)  21875       25          0
(5,2) 153125       25          0

Numerical odd-section covariance ratios remain approximately 1.50 versus 4.35 in the two alternating bulk shape families. These floating readouts are not symmetry acceptance tests.

## 8. Negative controls and migration boundary

A fixed linear lexicographic tie order fills holes but loses exact C6 at some even boundaries. Naively retaining the old sixth-power rule on even sections and switching odd sections to lexicographic ties breaks stability: (5,3) belongs to the old S(2,1) but is omitted by the lexicographic S(3,1). This exact witness is checked in the executable.

Blindly imposing c_v(x)>0 on every odd facet fails at three-way integer Voronoi vertices; it can lose whole cosets. The quadratic key resolves these vertex comparisons consistently instead of merely drawing smoother sides.

The new selector DOES reassign some predecessor boundary representatives. At (3,0), five old representatives are replaced; at (5,0), 29 are replaced although there were only 25 old hull holes. Even sections may switch chiral boundary convention too. Stable old addresses means stability UNDER FUTURE REFINEMENT OF THIS NEW CONVENTION. It is not a zero-movement migration from all earlier published address maps. No live Nollm data were modified.

## 9. BRC reuse and interpretation

REUSE_EXECUTED: pinned predecessor lattice arithmetic, exact Voronoi geometry, hull counts and rational stencil compiler.
EXTEND_EXISTING_TOOL: task-local selector predicate and its finite compatibility certificate, not a new global tool family.
COMPOSE_APPLIED: the observer contract may retain only the comparisons that survive at shared boundaries, while preserving full coset identity for future quotient refinements. A global scalar score was excessive state coupling, not a necessary invariant.

Retained carrier: prime exponents, lattice/phase basis, residue identity, anchor and local digit identity. Dropped assumption: all layers must use one identical total ordering. No mass/signed-amplitude cancellation or theorem promotion is invoked.

## 10. Next boundary

Resolved for this 5/7 slice: exact quotient paths, bounded local candidates, future address stability, lattice-convex sections at ALL parities, central symmetry everywhere, and C6 at even 5-depth.

Still unresolved: arbitrary-prime extension with bounded state/cost; scalar multiplication of ordinary integer labels as an intrinsic geometric operation; shape roundness on odd layers; useful semantic neighborhoods; arbitrary non-checkpoint prefix distribution and actual Nollm integration. For further primes, multiple nonparallel shared facet pairs may impose incompatible quadratic tie directions; the next meaningful question is the feasibility of those boundary constraints, not another search for a universal fixed rotation angle.
