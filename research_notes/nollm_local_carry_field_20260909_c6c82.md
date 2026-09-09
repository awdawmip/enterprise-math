# Nollm local carry field: a bounded residue rule with solid hex checkpoints

Status: RESEARCH_NOTE / DERIVATIONS_AND_FINITE_CHECKS / NOT_PROMOTED
Progress-Event-ID: NOLLM-LOCAL-CARRY-20260909-C6C82
Researcher-ID: EM-DIRECT-C6C82
Research-Activity-ID: RA-nollm-hecke-views-20260909-c6c82
Mode: TASK_RESEARCH / direct user continuation / no Task-ID or CLAIM
Date: 2026-09-09
Source snapshot: enterprise-math@fa34f1334d522201701210db932f75a916bdc148
Parent: research_notes/nollm_layer_observer_measure_audit_20260909_c6c82.md
Code: experiments/nollm_local_carry_field_20260909_c6c82.py
Code commit: 3f00fa9f849424077f483415c7b0f02f3ee06fb1
Code blob: 10fa5a7a1bd905b685a17e6be169eeeacdd2692d
Code SHA256: 5c80fdf987e9c212cf1491a199cc9db298eefe843dd153fc545e90803693fa99

## Scope

The model is an ordinary rank-two integer lattice viewed through the hex basis
E=[[1,1/2],[0,sqrt(3)/2]]. Its norm is Q(q,r)=q^2+qr+r^2. This is a mathematical
slice/comparison model, not a modification of P000 or Nollm runtime architecture.

Two experiments must remain distinct. The first keeps the previous eight matrices
frozen. The second deliberately replaces that research schedule by a nested two-phase
index-5 chain and position-dependent residue choices. It does not claim to achieve the
new results merely by rotating the camera or changing the old eight digit sets.

Locality below means at most two hex rings in the CURRENT LATTICE coordinates.
Physical displacements in the finest lattice grow with scale. Nollm's 22.5-degree
physical layer schedule and beta=2^(1/4) were not modified or implemented here.

## 1. Frozen-matrix diagnostics

The unchanged prior experiment is imported only after checking SHA256
ab10be88cd4d827a90976aa8a32963a690abdd6b151c46e4c5ba915273637a7e.
Its exact residue, covariance-objective and hull functions are executed unchanged.

With two legal nearest-neighbor symmetric digit sets per step:
- choosing the most isotropic CURRENT covariance greedily gives endpoint axis ratio
  3.165707003405;
- first pulling covariance back through the cumulative matrix, and greedily comparing
  P_k^(-1) C_k P_k^(-T), gives 1.726374382772, matching the previous restricted
  256-choice optimum on this example. No general greedy-optimality theorem is claimed.

A frozen radius-2 digit witness gives axis ratio 1.105223841305 but convex-hull
occupied fraction only 390625/835861=0.467332487100, below the prior compact value
390625/628663=0.621358343023. All endpoint residues remain distinct. The witness is
reproduced in the code, not claimed to be a global optimum. Rounder is not necessarily
less holey. Scalar second moments cannot replace the full spatial observer.

## 2. Alternative two-phase chain

Set
A=[[2,-1],[1,2]], B=[[1,-1],[2,3]], R=[[0,-1],[1,1]].
Then det(A)=det(B)=5 and AB=5R. R is the exact 60-degree hex rotation.
Both elementary maps have Euclidean singular-value ratio 5/3, attaining the earlier
minimum determinant-5 conformal defect Delta=1. Use RIGHT prefixes:

P_(2t)=5^t R^t,
P_(2t+1)=5^t R^t A.

Thus L_k=P_k Z^2 is genuinely nested, [L_k:L_(k+1)]=5, and det(P_k)=5^k.
This resolves the previous left-prefix/non-nested-path ambiguity for this new model.
There are two base shapes and an orientation clock modulo six; no random angles.

Let S_k select the minimum-Q integer representative of every class of Z^2/L_k,
with the exact boundary convention below. Consequently |S_k|=5^k.
These are representatives, not normalized probability clouds.

## 3. Explicit integer membership tests

Write N=5^t. For even k=2t, the closed Voronoi hexagon is

|2q+r|<=N, |q+2r|<=N, |q-r|<=N.

For a boundary equality belonging to oriented lattice vector b, retain x only when
cross(b,x)>0, where b has the sign of that equality. Equivalently the three equality
tests are (2q+r)*r>0, (q+2r)*(-q)>0, (q-r)*(q+r)>0 respectively.
Since N is odd and not divisible by 3, no integer point lies at an edge midpoint
or a Voronoi vertex. Every tied class therefore has exactly two representatives;
translation to the opposite facet reverses the cross-product sign. Exactly one is
retained. This convention is invariant under R and under negation.

For odd k=2t+1, first rotate x by R^(-t). Its exact half-open tests are

-7N <= 5q+4r < 7N,
-N < r <= N,
-7N <= 5q+r < 7N.

They select the lexicographically smaller shortest representative, including at
multiple ties. The three relevant lattice vectors of A Z^2 are (2,1), (-1,2),
and (3,-1), of squared lengths 7,3,7. These vectors form the three pairs associated
with an obtuse superbase. Their perpendicular bisectors give precisely the tests.
The closed polygon has vertices obtained by negating
(3N/5,N), (-8N/5,N), (7N/5,0), all at norm radius 7N/5.
Its inradius is sqrt(3)N/2 and its area is five fundamental hex-lattice areas.

## 4. The local 19-candidate / five-child rule

For x in S_k, consider

y=x+P_k v,  v in V={v in Z^2: Q(v)<=4}.

V has exactly 19 points, the origin plus two hex rings. Keep exactly those candidates
y satisfying the membership test for S_(k+1). No global search, matching, relaxation,
vacancy loop or Monte Carlo step is involved.

### Why all five children are inside this bounded stencil

The quotient projection Z^2/L_(k+1) -> Z^2/L_k has fibers of size five, so x has
exactly five canonical children if the full lattice of carries is considered.
It remains to bound their carry vectors, rather than assume locality.

The covering radii of the base Voronoi cells are rho_I=1/sqrt(3) and rho_A=7/5.
Also ||(E A E^(-1))^(-1)||=1/sqrt(3). Rotations preserve these bounds.
For an even-to-odd step,

||E v|| <= 7/5+1/sqrt(3) < 2.

For an odd-to-even step,

||E v|| <= (5/sqrt(3)+7/5)/sqrt(3)
          =5/3+7/(5sqrt(3)) < sqrt(7).

The integer norm Q cannot equal 5 or 6: modulo 3 it is (q-r)^2, excluding 5;
if 3 divides Q, write q=r+3s, giving Q/3=r^2+3rs+3s^2, which cannot be 2 modulo 3,
excluding 6. Therefore in both phases Q(v)<=4. The 19-candidate list is complete
at EVERY depth, not only at the eight enumerated depths. In even-to-odd steps only
the 13 points with Q<=3 can actually be needed.

Distinct parents cannot collide because reduction modulo L_k recovers their parent.
Each child has one parent, each parent has five children, and index/capacity multiplies
by five exactly. This is a proved elementary derivation within the declared model;
it has not been submitted as an accepted or formalized EM theorem.

## 5. No lattice holes and exact even-depth second-moment isotropy

Every interior integer point of the closed Voronoi polygon is retained. At odd depth,
excluded boundary facets are strict linear inequalities, so their integer points cannot
enter the convex hull of retained points. At even depth, retained points of each tied
facet occupy only its positive-tangent half; the omitted negative-tangent points cannot
be convex combinations of retained points on that supporting line. Outside-polygon
points cannot lie in the convex hull either. Hence

S_k = conv(S_k) intersect Z^2

for every k. The convex hull contains no unoccupied lattice sites. This statement
concerns lattice occupancy, not the absence of continuum space between lattice points.

At every even depth S_(2t) is exactly R-invariant. It is centrally symmetric, has mean
zero, and its Euclidean covariance commutes with a 60-degree rotation, so it is a scalar
multiple of the identity (t>=1). Thus its standard-deviation axis ratio is exactly one.
Sixfold symmetry does not imply continuous rotational symmetry or Poisson statistics.

## 6. Stable labels for all positive integers

The cells are strictly nested in radius: rho_I < inradius(A Z^2), and
rho_A < inradius(5 Z^2). Thus S_k is contained in S_(k+1), and zero carry is always
a legal child. Order zero carry first, then the remaining legal carries in a fixed
lexicographic order. Assign child digit j the label offset j*5^k.

The executable address(n) reads the base-5 digits of n-1 from least significant to most
significant and chooses the corresponding child. Extra leading zeros keep the point
unchanged. It follows that the first 5^k labels fill S_k, old addresses never move,
and label_of is its inverse. Since the regions exhaust the plane, this gives a bijection
between positive integers and the entire axial lattice. It requires at most 19 candidate
checks per digit. Integer bit cost still grows with the label's bit length.

The radial order remains r(n)=Theta(sqrt(n)), although it is not the old exact equation
r(n)=C sqrt(n). A coarse bound for n>=2 is

3n/100 <= Q(address(n)) <= 49n/25.

Indeed a new label lies outside the previous cell and inside the next. For even entry
k=2t, N=5^t gives radii at least sqrt(3)N/10 and at most N/sqrt(3), with
N^2/5<n<=N^2. For odd entry, radii are at least N/2 and at most 7N/5, with
N^2<n<=5N^2. These imply the displayed uniform bounds. Label 1 is the origin.

IMPORTANT: this is a RADIX ADDRESS bijection. It does NOT prove
address(ab)=address(a)*address(b), nor implement all prime Hecke correspondences by
one planar similarity. Exactness here is quotient refinement/index multiplication and
reversible indexing. Arbitrary non-checkpoint prefixes n<5^k are not proved uniformly
distributed. The missing cross-prime multiplication/selector contract is not hidden.

## 7. Full finite check

All levels 0 through 8 were generated, not sampled for statistics. Every one of the
97,656 parents in levels 0 through 7 was checked for exactly five children. Quotient
bijections, stable old addresses, and exact integer hull occupancy were verified at
each depth; rectangular enumeration independently checked the first six levels.

| k | count | cloud axis ratio | occupied/hull lattice sites |
|---:|---:|---:|---:|
|1|5|1.666666666667|5/5|
|2|25|1|25/25|
|3|125|1.529758979427|125/125|
|4|625|1|625/625|
|5|3125|1.500578400304|3125/3125|
|6|15625|1|15625/15625|
|7|78125|1.499455577891|78125/78125|
|8|390625|1|390625/390625|

At depth 8 the hull has twice-area 780618 and 630 boundary lattice sites; Pick's
formula gives 390625 total sites exactly. Even-depth isotropy was checked by integer
covariance identities and complete R-rotated-set equality, not rounded eigenvalues.
There were 211 address/label round trips, including 100 labels below 5^40 and 100
random integer points with coordinate magnitudes below 10^12, plus 100 independent
comparisons of single-address lookup with the full depth-8 array. All checks passed.
These tests supplement the all-depth derivations; they do not substitute for them.

## 8. BRC reuse / information boundary

REUSE_EXECUTED: the exact prior experiment functions for legal residue digit sets,
integer adjugates, rational covariance scores, lattice hull counts and spectral readout.
EXTEND_EXISTING_TOOL at the task-experiment level only: position-dependent residue
membership and reversible local labels. No new global tool family or authority claimed.

REUSE_APPLIED: branch count/provenance versus scalar observers. The local carrier is
(current residue x, phase/orientation, lattice basis P_k, selected digit rank). Moment
isotropy alone is not sufficient to choose legal carries or certify holes. Preserve full
residue identity until after the next-step membership test. The new conditional digits
are not independent identically distributed copies of the old fixed digit template;
the old simple iid covariance recursion is not silently transferred to this model.
Positive mass cancellation and deterministic phase/shape closure remain distinct.

## 9. Interpretation and remaining unit

The local obstruction for determinant 5 is carried by a two-shape phase and an exact
carry, instead of a growing uncertainty cloud. Solid finite hex checkpoints can coexist
with five-way multiplicative capacity and fixed old addresses. The cost is changing the
research matrix schedule and making the residue selector depend on the parent.

Classical background: lattice quotient representatives and Voronoi cells; Lagarias and
Wang, Integral Self-Affine Tiles I (1996), DOI 10.1112/jlms/54.1.161, and Part II (1997),
DOI 10.1007/BF02647948, distinguish digit completeness and geometric tiling. This
position-dependent construction is proved directly above; their fixed-digit theorems
are not invoked as automatic proofs of this selector or as a priority claim.

Next exact question: can the same bounded carry/phase discipline support two coprime
prime refinements with path-consistent arithmetic identity, while preserving solid
finite sections and without materializing the entire Hecke correspondence? Do not
replace that question by the trivial conjugation of integer multiplication through an
arbitrary address bijection.
