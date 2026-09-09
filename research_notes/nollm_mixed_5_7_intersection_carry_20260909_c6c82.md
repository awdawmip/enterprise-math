# Mixed 5/7 intersection carry: a finite-state coprime refinement field

Status: RESEARCH_NOTE / DERIVATIONS_AND_FINITE_CHECKS / NOT_PROMOTED
Progress-Event-ID: NOLLM-MIXED57-INTERSECTION-20260909-C6C82
Researcher-ID: EM-DIRECT-C6C82
Research-Activity-ID: RA-nollm-hecke-views-20260909-c6c82
Session: local-chat-nollm-hecke-20260909-c6c82 (local key, not a server ID)
Mode: TASK_RESEARCH / user-selected continuation / no formal Task-ID or CLAIM
Date: 2026-09-09
Source read snapshot: c5c8c2153c67e04bf1d057b0eb8d19707dfbba85
Parent: research_notes/nollm_local_carry_field_20260909_c6c82.md at fa10d35c280e284c90acc4ac5e84b71771e73472

## Recovery and scope

The source activity already binds the local-carry checkpoint ef72a8f9b72c3e99f5f77ac0575f8fd4c52fe037. The preceding chat's statement that no related source was published is not current authority. That source is reused, not copied or restarted. The separate local left-prefix/carry boundary-count experiment is not identical to the source's right-prefix nested chain; its imported provenance is kept separate.

All mathematics below concerns the ordinary axial integer lattice with Q(q,r)=q^2+qr+r^2, an external/research slice. No P000 or Nollm runtime change. Index multiplication and reversible quotient addresses are not a claim that a planar label address satisfies address(uv)=address(u)address(v).

## 1. The fixed-matrix obstruction is real

Put M=[[2,-1],[1,2]], B=[[1,-1],[2,3]], W=[[0,-1],[1,1]], G=[[1,-2],[2,3]]. Then det M=det B=5, det G=7, MB=5W, and MG-GM=[[0,-2],[-2,0]].

This cannot be removed by choosing a different fixed determinant-5 integer matrix commuting with this G. Since G=I+2W, commutation with G is equivalent to commutation with W. Its integer centralizer consists of [[u,-v],[v,u+v]], with determinant u^2+uv+v^2. Modulo 3 this is 0 or 1, never 5 modulo 3. Thus no determinant-5 integer matrix commutes with G.

## 2. Replace a fixed product by two compatible quotient directions

Reuse the parent's nested chain P5_(2t)=5^t W^t and P5_(2t+1)=5^t W^t M. Let L5_a=P5_a Z^2 and L7_b=G^b Z^2. Define

L_(a,b)=L5_a intersect L7_b.

Their indices are coprime, so L5_a+L7_b=Z^2 and the elementary lattice Chinese remainder map is an isomorphism

Z^2/L_(a,b) -> (Z^2/L5_a) x (Z^2/L7_b).

For example, Bezout coefficients for indices 5^a and 7^b construct a representative of any pair of cosets. Consequently the index is exactly 5^a 7^b. Increasing a splits each quotient class into five; increasing b splits it into seven. The two quotient projections commute. A final class and its canonical representative do not depend on the order of the refinements. Local digit RANKS generally undergo a nontrivial 35-element permutation when the order is exchanged; retaining the same rank word is not asserted.

## 3. Six intermediate shapes suffice

Describe a mod-5 line by slope r/q, including infinity. The image of M is slope 3. Successive G^(-1) actions give

3 -> 4 -> 2 -> 0 -> 1 -> infinity -> 3.

G^6=[[37,360],[-360,-323]] is 2I modulo 5 and no earlier positive power through five is scalar. Choose determinant-5 representatives for these six lines:

H0=[[2,-1],[1,2]]
H1=[[-2,1],[-3,-1]]
H2=[[-2,-1],[1,-2]]
H3=[[-1,2],[0,-5]]
H4=[[-3,-1],[2,-1]]
H5=[[-5,0],[2,-1]].

An exact basis of the intersection lattice is

P_(a,b)=5^t W^t G^b H_(b mod 6)^epsilon, a=2t+epsilon,

where exponent epsilon means I at epsilon=0 and the listed H at epsilon=1. Inclusion in both component lattices and the product index prove equality with their intersection.

The state-dependent RIGHT transition matrices are:

X5(even,j)=Hj;
X5(odd,j)=adj(Hj) W;
X7(even,j)=G;
X7(odd,j)=Hj^(-1) G H_(j+1).

All are integer with determinant 5 or 7 respectively. The last integrality follows because G maps the next mod-5 line into the present one. They obey the exact diamond identity

X5(a,b) X7(a+1,b) = X7(a,b) X5(a,b+1).

This is state-dependent refinement consistency, not a pair of globally fixed commuting planar matrices.

## 4. An arithmetic tight/elongated alternation

For j even, the listed H have Delta=1 and Euclidean singular-value ratio 5/3; for j odd, Delta=12 and ratio 5. These are minimum defects for their respective lattice classes, not only values from a bounded matrix search.

For the three tighter classes, there is no norm-1 vector and a norm-3 vector exists. Inertness excludes Delta=0 and the listed Delta=1 bases attain the lower bound. The three elongated classes contain a unit vector. For any integer basis C of such a lattice, write the unit as Cv with nonzero integer v and norm(v)>=1; hence sigma_min(C)<=1. Since det C=5, its singular ratio is at least 5, equivalent to Delta>=12. The listed bases attain it.

The mechanism is visible modulo 5. Q is anisotropic there. Its quadratic character is well-defined on projective lines, since scaling a representative multiplies Q by a square. Multiplication by G multiplies Q by 7, a quadratic NONresidue modulo 5. It therefore flips the character and exchanges the two sets of three lines at every step. This is an exact mod-5 statement. Generalization to other primes must distinguish the general character identity from this specific geometry/cost classification.

Full finite point clouds at a=1, b=0..6 have standard-deviation axis ratios approximately

1.666667, 4.455822, 1.518401, 4.338961, 1.498748, 4.345057, 1.499421.

These numerical covariance readouts are not the singular-value ratios of the basis matrices.

## 5. One global canonical order gives stable addresses and even-layer C6

For z=q+r*omega, omega=exp(i*pi/3), write z^6=u+v*omega and order lattice points lexicographically by

(Q(z), 2u+v, v, q, r).

Choose the least point in each quotient class under this SAME order for every (a,b). A minimum exists. Call the resulting section S_(a,b). Nested lattices immediately imply S_parent is contained in S_child: the competitors for the finer class form a subset. Thus the zero-carry child retains the old point. This stability would not follow from independently changing tie conventions between layers.

When a is even, P_(a,b) is a hex similarity and its index is coprime to 6. A co-minimal coset cannot contain two distinct points in one W-orbit: W^k-I is invertible on the quotient for k=1..5 (its relevant norms involve only 2 and 3). The z^6 tie key is orbit-invariant, so the section is exactly W-invariant. Its nontrivial covariance is exactly isotropic.

For even a, no Voronoi vertex or side midpoint is an integer point. On each regular-hex side, comparing the sixth powers of the two equal-distance representatives selects precisely one open half-side: writing the points as exp(i phi)(ell/2 +/- i t), the difference is proportional to sin(6 arctan(2t/ell)), which has the sign of t in the open side. Therefore the convex hull has no missing lattice sites, as in the parent's handed-boundary argument.

Odd layers cannot have C6 symmetry because 5^a 7^b=5 modulo 6. The new global tie rule DOES introduce some odd-layer boundary holes: at a=3, b=0..3, exactly five hull sites are omitted; at a=5, b=0..2, exactly 25 are omitted. These are full finite checks, not a universal count formula. Strict-interior Voronoi sites are always included. The source parent's all-layer hole-free claim must not be transferred to this new global selector. The omitted boundary fraction is bounded by a constant times inverse linear scale, since only a bounded-shape perimeter is involved. Bulk elongation is a different phenomenon and does not vanish with this boundary fraction.

## 6. At most 19 candidate carries per step

For a parent x and P=P_(a,b), children have form y=x+P v. Keep candidates in the canonical child section. There are exactly five or seven because these are quotient fibers; distinct parents cannot collide.

There is a finite, depth-independent candidate certificate. The six H shapes have covering radii 7/5 (tight) and 19/(5 sqrt(3)) (elongated), and minimum singular values sqrt(3) and 1. The ordinary hex lattice has covering radius 1/sqrt(3). Combining parent and child radii gives norm(v)<6 for every transition; the largest bound is 19/(5 sqrt(3))+7 sqrt(7)/5<6.

Start with the 127 integer vectors Q(v)<=36. For each phase remove vectors outside the exact rational polygon

P_base^(-1) (Vor(child_base)-Vor(parent_base)).

The vertices are calculated by integer Gauss reduction and rational intersections of bisectors. Minkowski sums and point-in-polygon tests use Fraction, not floating tolerance. The resulting COMPLETE candidate counts are:

5, even -> odd: 11 tight / 17 elongated;
5, odd -> even: 13 tight / 15 elongated;
7, even -> even: 19;
7, odd -> odd: 17.

Thus at most 19 candidates are checked and exactly 5 or 7 survive. The union has 43 vectors with maximum Q=16, but each phase uses its own smaller table. Locality is in the current lattice basis; it is not a bound of four or fewer steps in the finest physical grid. The finite rational polygon certificate proves stencil completeness at all scales for this family.

## 7. Executed checks

The unchanged prior baseline was executed with SHA256 ab10be88cd4d827a90976aa8a32963a690abdd6b151c46e4c5ba915273637a7e for determinant, adjugate, integer hull counts and covariance readout.

- 200 exact inclusion/index checks on a 10 by 10 state grid.
- 24 complete sections, 844736 points in total across those sections, maximum individual section 588245 points.
- Three extra odd sections, bringing the total to 27 sections and 1022861 enumerated points (counts across different sections are not unique global memories).
- 29 full refinement edges, 17051 parents: broad complete stencil and compact phasewise stencils give identical sets; every parent has exactly 5 or 7 children.
- Eight complete commuting diamonds, 542 parents and 18970 two-step descendants; both orders give identical endpoint sets and exact parent fibers of size 35.
- All tested even sections are C6-invariant and have exact hull occupancy one; the stated odd boundary holes are retained as negative evidence.

The all-depth conclusions come from the quotient, shape-table, total-order and rational-stencil arguments, not extrapolation from these tests.

## 8. BRC and next unresolved unit

REUSE_EXECUTED: pinned baseline arithmetic and hull observer. COMPOSE_APPLIED: coprime quotient decomposition, branch identity retained through the 35-state digit permutation, and phase-dependent lattice transport. The retained state includes prime exponents, the six-state intermediate line, exact lattice basis and quotient residue. Counts, covariance and defect norm are observers, not replacement state. No signed/positive mass identification is used.

Resolved in this slice: two coprime refinement directions with exact path-independent quotient identity, bounded phasewise candidates, stable canonical old points and even-layer solid C6 sections.

Not resolved: ordinary scalar label multiplication as an intrinsic low-cost geometric operation; simultaneous extension to all primes with uniformly bounded state/cost; preservation of semantic Nollm neighborhoods; an odd-layer tie rule with all desired symmetry/stability/convexity properties; physical runtime integration. A trivial conjugation through an arbitrary label bijection is not counted as solving these.

Classical provenance: the lattice Chinese remainder argument is elementary; compare primary work on coprime Eisenstein/ideal-lattice array designs, Li-Gan-Ling, arXiv:1808.07505. No novelty claim is made for CRT or finite-field projective actions. The candidate contribution here is this explicit mixed refinement/selector/stencil synthesis and its measured limitations.
