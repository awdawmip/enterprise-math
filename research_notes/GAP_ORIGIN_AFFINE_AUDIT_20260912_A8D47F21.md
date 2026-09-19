# Gap-origin affine audit

Date: 2026-09-12
Status: DIRECT-USER RESEARCH NOTE; proved conditional derivations and supplementary exact checks; not Foundation promotion or a canonical-definition change.
Research-Activity-ID: RA-20260912-gap-origin-a8d47f21
Researcher-ID: EM-CHAT-A8D47F21 (locally allocated research handle)
Session: local-chat-gap-origin-a8d47f21 (local key, not a platform-authenticated session ID)
Question: put the plotted vertical axis and spatial coordinate origin between Cell centers; determine algebraic and proof/test consequences.

## Verified inputs and scope

Source snapshot: awdawmip/enterprise-math@0e208043eabd73da6aa27fbcc5b3c81d6deb0ce2.
Read definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md and definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md.
X6 is a Z^6 torsor with no distinguished global ontic origin. A chosen Cell anchor gives an integer chart. A selected centered slice is Z^3. Its classical FCC STAR carrier projection has unit vectors u_a+u_b+u_c=0, kernel Z(1,1,1), and radius-1/sqrt(3) circular footprints at nearest-center spacing 1. Native norm is the signed component sum of squares, not the carrier Euclidean norm.
All fractional positions below belong to an auxiliary rational/real affine chart, not new fractional native Cells. No assumption about physical empty volume is introduced. This is a dependency audit of these two definitions, not a repository-wide proof/test audit.

## 1. Exact gap and axes construction

Rotate the classical carrier drawing so u_b=(0,1), u_a=(sqrt(3)/2,-1/2), u_c=-u_a-u_b. Carrier centers are m*u_a+n*u_b for integers m,n. The elementary triangle with centers 0,u_a,u_a+u_b has circumcenter q=(2*u_a+u_b)/3=(sqrt(3)/3,0). Its distance to all three centers is 1/sqrt(3).
The vertical line through q has horizontal coordinate sqrt(3)/3. A center on this line would require m=2/3, impossible. In axial (u_a,u_b) coordinates, q=(2/3,1/3); the three native-direction-parallel lines require respectively n=1/3, m=2/3, or m-n=1/3. Thus all three complete carrier axes avoid every carrier center.
A compatible raw slice affine lift is delta=(2/3,1/3,0). Each line delta+t*e_i avoids Z^3 because at least one of its fixed other components is nonintegral. The full X6 example appends three zero coordinates. This lift is an explicit convention, not uniquely determined by the planar picture: delta+t*(1,1,1) has the same carrier readout. Omitted X6 coordinates also need explicit retention.
The naive alternative delta=(1/2,1/2,1/2) projects to 0, a carrier center, NOT the desired carrier gap.
Avoiding centers does not mean avoiding footprints: their union covers the whole carrier plane. Moreover the closest center-to-vertical-line perpendicular distance is sqrt(3)/6, less than the current footprint radius sqrt(3)/3. The axis crosses footprint interiors. An axis lying entirely in uncovered space is incompatible with this carrier cover and would require changing the model, not just its origin.

## 2. Translation theorem and BRC reuse

Let Lambda=Z^d, d=3 or 6, and T_delta(x)=x-delta. Cell coordinate image C_delta=Lambda-delta is a Lambda-torsor, even when 0 is not in it. For all Cell endpoints P,Q, T_delta(Q)-T_delta(P)=Q-P. Consequently signed adjacency, native point-to-point squared distance, minimum primitive step count, support size and shortest-path counts are unchanged.
Precise existing BRC interface REUSE_APPLIED: for integer displacement v, N=sum_i |v_i| and B=N!/product_i |v_i|!. Map a path (x_0,...,x_N) to (x_0-delta,...,x_N-delta); the entire ordered signed-step word is identical. This is a bijection of path fibers, preserving branch identity and multiplicity, not a quotient. Weighted fibers are preserved only with the corresponding transported weights and state/port data.
For displacement (3,4,0), both charts give squared length 25, N=7, B=35; signed reversal also preserves them. The squared-25 displacement shell remains 30 endpoints and 846 shortest paths.
A fixed spatial rechart does not change path ordering or transition counts. A state update F must be represented as T_delta F T_delta^{-1}. No physical clock calibration or full time-evolution theorem is established by this audit.

## 3. Algebraic typing and integer implementation

For nonintegral delta, C_delta is not closed under ordinary coordinate addition: (-delta)+(-delta)=-2delta is outside C_delta. Points are not canonically additive group elements. Point-minus-point is in Lambda; vector-plus-point is in C_delta; zero displacement fixes every point and need not be an occupied point at geometric coordinate 0.
If one transports an anchor-dependent old coordinate addition, the new law is y op z=y+z+delta, whose identity is -delta, not the gap 0. Prefer the origin-free torsor action rather than pretending ordinary point addition still applies.
For delta=(2/3,1/3,0), integer-only storage is possible: Y=3x-(2,1,0), with Cell addresses Y congruent to (1,2,0) modulo 3. Unit native steps change Y by +/-3e_i. This is a scale/encoding choice, not Cell subdivision or changed physical spacing.

## 4. Observer transport and an exact failure witness

The old lossless min-zero chart is h=min(x), r=x-h*(1,1,1). In the gap chart recover x=y+delta before computing r,h. For x=0, y=(-2/3,-1/3,0), naive can3(y)=(0,1/3,2/3), which is not the required integer min-zero address. The correct old residual is (0,0,0), depth 0.
The new carrier readout is pi_gap(x)=pi(x)-q, an affine map, not a group homomorphism. Its equal-value fibers and difference kernel remain those of pi; its zero fiber is empty when q is not a carrier-lattice point. Do not describe the old kernel as the new zero fiber. Common depth and omitted coordinates remain necessary; H=(1,1,1) remains nonzero native displacement despite zero carrier difference.

## 5. Rotation conjugation and a no-go statement

An old anchor-fixed action x -> Mx becomes y -> My+(M-I)delta. Conjugation preserves all group relations. Omitting the constant generally changes the actual rotation center.
For an integer lattice automorphism M, the new origin-centered linear map y -> My preserves C_delta iff (I-M)delta belongs to Lambda. This follows by evaluating it on x-delta and translating back.
All coordinate permutations preserve C_delta in this uncorrected linear form iff delta_i-delta_j are integers for every i,j: necessity follows from each transposition; sufficiency is immediate. Thus delta=t*(1,...,1)+n with n integral. On any established triangular STAR carrier, such a shift projects to an existing carrier center. Therefore a true carrier-gap origin cannot simultaneously retain all native axis permutations as uncorrected linear origin-fixed actions. Keep their affine conjugates instead, or explicitly change/restrict the symmetry action.
For delta=(2/3,1/3,0), the native cycle M(x_a,x_b,x_c)=(x_c,x_a,x_b) has (M-I)delta=(-2/3,1/3,1/3), nonintegral; the naive gap-centered cycle fails Cell closure. In the 2D carrier, however, the 120-degree matrix [[0,-1],[1,-1]] obeys (I-M)q=(1,0), so that separate carrier symmetry is valid. Carrier symmetry does not automatically lift to the native Cell action. Also 2q is not a carrier-lattice vector, so this interstice is not an inversion center.

## 6. Changing an observable is not merely changing coordinates

The same physical shell about the old Cell anchor has equation ||y+delta||^2=25 and still 30 endpoints. A newly defined shell about the gap, using the auxiliary extension of the component metric, instead requires ||n-delta||^2=25. Multiplication by 9 gives (3n_a-2)^2+(3n_b-1)^2+(3n_c)^2=225, impossible modulo 3 (left 2, right 0). That new shell has zero Cell endpoints. This does not invalidate the original native metric; a different center and an auxiliary gap-to-Cell metric have been selected.
Consequently origin-centered shells, potentials, boundary locations, sources and initial data need audit when their physical reference point is changed. Distances between unchanged Cells do not.

## 7. Supplementary exact checks actually executed

A Python Fraction/integer certificate checked 15,625 ordered pairs of Cells from {-2,-1,0,1,2}^3; 125 lossless observer reconstructions; 750 affine permutation identities; and 3,721 carrier centers against all three gap axes. All final assertions passed. It also independently enumerated the squared-25 displacement shell (30,846), checked the (3,4,0) witness, and exhibited failed naive addition, min-zero and native-cycle rules. These finite checks supplement the general proofs above; no full project test suite or Lean proof compilation was run.

## Recommendation and remaining work

Permit the chosen gap as the primary geometric/display origin and keep Cell identity, displacement zero, and geometric origin separately typed. The current torsor need not privilege any ontic Cell center. Do not delete the old zero-labelled Cell or reintroduce a special gap-to-first-Cell primitive transition. Preserve native signed displacement/BRC inputs, explicit affine frame offsets, hidden depth and axis labels. Keep fixed old physical operations by conjugation. Reprove new gap-centered symmetries and observables only when they are intentionally different operations.
Implementation follow-up: one exact frame/Cell address API and dependency-directed regression for zero-is-Cell assumptions, min-zero observers, rotation encodings, origin-centered shells, boundary/source initialization and plotted-axis incidence. No canonical Foundation file was modified by this audit.

External alignment: mathlib4 Mathlib.Algebra.Torsor.Defs and Mathlib.LinearAlgebra.AffineSpace.Defs distinguish points, displacement actions and point differences; IUCr educational material on matrices/mappings/crystallographic symmetry treats origin shifts as coordinate transformations. These support the standard affine framework, not the project's physical worldview.
