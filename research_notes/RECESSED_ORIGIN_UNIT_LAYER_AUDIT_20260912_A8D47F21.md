# Recessed external origin and unit first layer

Progress-Event-ID: recessed-origin-unit-layer-20260912-a8d47f21
Research-Activity-ID: RA-20260912-gap-origin-a8d47f21
Researcher-ID: EM-CHAT-A8D47F21
Session: local-chat-gap-origin-a8d47f21 (locally assigned, not a platform ID)
Status: CONDITIONAL_EXACT_DERIVATIONS_AND_FINITE_CHECKS; NOT_FOUNDATION; NOT_WORKING_TRUTH
Source snapshot: awdawmip/enterprise-math@d63e2915f3b54a3e6271f8050245d499153a6446.
Exact inputs: definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md and definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md.
Continuation of research_notes/GAP_ORIGIN_AFFINE_AUDIT_20260912_A8D47F21.md at 726b887cd0a71bb6fe17740478598856f8c8ea8b; prior work is consumed, not restarted.
User question: recess the origin slightly outside the dimensions and define all first-layer Cells as 1. This is a hypothetical model audit, not authorization to replace native definitions.

## 1. Three meanings of 1

Layer label w=1, radial metric distance d(O,P)=1, and one primitive transition from O are different declarations. A common scalar observer must not identify different Cells or erase directions, addresses, common depth, ports, or path provenance. Unit layer is not the multiplicative unit element of an algebra.

## 2. Affine homogenization without a new physical axis

For native integer addresses x in Z^d (d=6, or a raw selected d=3 slice), a fixed rational gap offset delta and h>0, use the auxiliary embedding J_h(x)=(x-delta,h), with ambient zero O=(0,0). The represented Cells lie in the affine hyperplane t=h, outside O. Its normalized auxiliary coordinate w=t/h is 1 for every represented Cell, even for a small drawing recess h. The embedding is injective and

J_h(y)-J_h(x)=(y-x,0).

Consequently the native component metric on Cell differences, signed adjacency, and every ordered primitive path are preserved if no new transitions through O are admitted. Native common depth remains part of x, not the extra coordinate. This is not a seventh native spatial axis, not physical time, not the removal of the original chart-zero Cell. O is an auxiliary ambient zero, not an intrinsic point/origin of the Cell hyperplane. The all-zero vector does not define a projective point.

For an affine map y -> My+b in the normalized coordinates, its homogeneous linear lift is H(M,b)=[[M,b],[0,1]]. Direct multiplication gives H(M,b)H(N,c)=H(MN,Mc+b). All such matrices fix the ambient zero. They need not preserve the ambient Euclidean norm; this does not prove that the gap is an intrinsic isometric rotation center. For the previous origin change b=(M-I)delta.

## 3. Extrinsic equal-distance theorem

Assume explicitly an auxiliary positive-definite Euclidean/component metric extension. For base centers (p_i,0) and external O=(q,-h),

D_i^2=||p_i-q||^2+h^2.

Therefore D_i^2-D_j^2=||p_i-q||^2-||p_j-q||^2, independent of h. A perpendicular recess cannot equalize previously unequal distances. All D_i equal a fixed length ell iff the base centers are cospherical around q with common radius R and h^2=ell^2-R^2. A strictly external solution requires R<ell. If the common radial distance is merely renamed 1 by changing units, the old primitive unit also changes unless the distances already coincide.

In the established triangular CARRIER ONLY, generators have Gram matrix [[1,-1/2],[-1/2,1]], centers are (0,0),(1,0),(1,1), and q=(2/3,1/3). The three base squared radii are 1/3. Keeping carrier neighbor spacing 1, h^2=2/3 gives three unit radial distances, a regular tetrahedron realization. The depth is approximately 0.8165, not arbitrarily slight relative to the fixed spacing. This is not a native X6 distance theorem. For the raw native lifts 0,e1,e1+e2 and delta=(2/3,1/3,0), the native squared radii are 5/9,2/9,5/9; the same perpendicular recess does not make these three equal.

More generally any set whose points all have distance ell from one added point must have diameter at most 2 ell by the triangle inequality. Thus an unbounded first layer cannot all be at finite common distance while its original metric is retained, regardless of the number of auxiliary dimensions.

## 4. BRC reuse and graph-extension obstruction

REUSE_APPLIED: the exact current native theorem has N_min(z)=sum |z_i| and B_min(z)=N_min(z)!/product |z_i|!. Under J_h each ordered path word has the identical labeled realization; the bijection preserves these quantities and any carried weights without compression. The layer-only observer w=1 is not adequate for future displacements or path composition, so x and branch identities are retained.

If an undirected unit-edge apex O is added to every vertex in a nonempty first-layer set S, then

d_new(u,v)=min(d_old(u,v), d_old(u,S)+2+d_old(v,S)).

Proof: a shortest positive-edge path either avoids O or visits O exactly once; independently minimize its entry and exit legs. In particular distances within S become min(d_old,2). Even unchanged distances do not guarantee unchanged BRC multiplicity: on the native chain 0--e1--2e1, adding O adjacent to both endpoints leaves distance 2 but increases shortest path count from 1 to 2. For endpoints 0 and 3e1, distance changes from 3 to 2. A one-way source avoids return shortcuts but defines a distinct directed initialization model, not an unchanged symmetric native path space.

## 5. Verification and disposition

Exact rational local regression PASS: 27 lifted Cells; 729 ordered displacement pairs; 27 affine cyclic-action tests; 2916 normal-distance-difference tests; the carrier 1/3 and 2/3 identities; native projection-confusion witness; both graph distance/count witnesses. The ambient block action also fixes zero. Finite regressions supplement the displayed general proofs; they are not full repository tests or Lean validation.

Recommendation: retain an external-reference / unit-layer homogeneous representation as an auxiliary candidate. Admit equal radial unit distance only for an explicitly fixed cospherical first-shell population and metric/unit convention. Adding a real spatial dimension, changing the native Cell set, or introducing origin-to-Cell transitions requires a separately specified model and new affected proofs. No worldview, P000, native origin, adjacency, time calibration, Foundation or Working Truth changes are made.

Next unresolved modeling choice: the exact first-layer population and whether 1 is a label, a metric unit, or a transition count. The conditional calculation is complete without assuming that choice.

## External references

Standard affine point/vector typing: https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Torsor/Defs.html
Homogeneous point/vector coordinates and affine matrix representation: https://jcsites.juniata.edu/faculty/rhodes/graphics/represent.htm
These references support the standard representation, not the project's physical interpretation.
