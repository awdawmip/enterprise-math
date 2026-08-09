# A3 Guard-Image Lattice Supplement 02 — Exact Rank-Two Hidden-Guard Reachability

Status: `RESEARCH WIP / EXACT RANK-TWO INTEGER FEASIBILITY SOLVER + COMPLEXITY BOUND`

## 1. Goal

Supplement 01 solved

\[
\operatorname{rank}L_G=1,
\qquad
L_G=W(K_A)\subseteq\mathbb Z^r,
\]

where the hidden guard-score set in one coarse fiber is an integer arithmetic line.

This supplement solves the next layer:

\[
\boxed{\operatorname{rank}L_G=2.}
\]

The number of guards `r` need not equal three. The result applies to any finite guard family whose hidden image lattice has rank two.

Given base scores

\[
g\in\mathbb Z^r
\]

for one coarse fiber and a threshold pattern

\[
\sigma\in\{\mathrm{False},\mathrm{True}\}^r,
\]

we decide exactly whether some

\[
x\in g+L_G
\]

realizes that pattern.

No floating-point computation, continuous optimization, or finite fine-state box is used as the correctness criterion.

## 2. A3-G07 — Exact integer basis of a rank-two lattice

Let

\[
v_1,\ldots,v_m\in\mathbb Z^r,
\qquad
\operatorname{rank}_{\mathbb Q}\langle v_i\rangle=2.
\]

Choose the lexicographically first pair of guard coordinates `(p,q)` whose projection preserves rational rank two. This projection is injective on the rank-two rational span, so a basis of the projected `Z^2` subgroup lifts uniquely to the full lattice.

The construction uses two Bezout/gcd stages:

1. take the gcd `a` of all projected `p` coordinates and construct a Bezout combination realizing it;
2. eliminate the `p` coordinate from all generators and take the gcd `c` of the residual `q` coordinates;
3. construct the second basis vector with projected form `(0,c)`;
4. reduce the first vector by an integer multiple of the second so the projection is

\[
\boxed{(a,b),(0,c),\qquad a,c>0,\ 0\le b<c.}
\]

This yields an exact basis

\[
\boxed{L_G=\mathbb Z h_1+\mathbb Z h_2.}
\]

It is not enough to pick two independent original generators: redundant generators can decrease the lattice index, so the generated subgroup itself must be reduced.

The implementation also provides exact integer membership coordinates in this basis.

## 3. Threshold patterns become 2D integer halfplanes

Every guard-score vector in the fiber is uniquely

\[
\boxed{x=g+s h_1+t h_2,\qquad s,t\in\mathbb Z.}
\]

For guard `j`:

- `True` requires
  \[
  h_{1j}s+h_{2j}t\ge -g_j;
  \]
- `False` means the integer condition `x_j<0`, equivalently `x_j\le-1`, so
  \[
  -h_{1j}s-h_{2j}t\ge g_j+1.
  \]

Hence every branch pattern is exactly a finite two-variable integer halfplane system

\[
\boxed{a_i s+b_i t\ge c_i.}
\]

The infinite fine-state problem has been reduced to two integer parameters.

## 4. A3-G08 — Three exact certificate regimes

Let the homogeneous recession cone be

\[
C=\{(u,v):a_i u+b_i v\ge0\ \forall i\}.
\]

In two dimensions there are only three essential regimes.

### 4.1 Strict recession

If an integer direction `d` satisfies

\[
\boxed{a_i d_1+b_i d_2>0\quad\forall i,}
\]

then for a sufficiently large integer `N`, the point `Nd` satisfies every constant right-hand side `c_i`.

The implementation constructs a strict interior integer direction from exact recession boundary rays/normals and returns the required integer multiplier. No search is needed.

### 4.2 Recession ray or line

If the recession cone is nonzero but has no 2D interior, it is a rational ray or line.

Choose its primitive integer direction

\[
d=(d_1,d_2)
\]

and primitive perpendicular normal

\[
n=(-d_2,d_1).
\]

Bezout gives an integer section `p` with `n·p=1`. Every integer point can then be written as

\[
q p+t d.
\]

Constraints with zero growth along `d` give one-dimensional integer bounds on `q`; after solving that interval, a sufficiently large integer `t` handles all positive-growth constraints.

Again, no 2D enumeration is required.

### 4.3 Bounded polygon

If the recession cone is `{0}`, any nonempty real feasible set is a bounded polygon, segment, or point.

All coordinate extrema occur at pairwise line intersections. The implementation stores each exact rational intersection only as integer numerators plus a positive denominator and compares fractions by cross multiplication.

It then scans the smaller of the two exact integer coordinate spans. Once one coordinate is fixed, the other is again a one-dimensional integer interval.

Thus the bounded scan width is an explicit finite certificate rather than an arbitrary truncation box.

## 5. Real feasibility does not imply integer reachability

A bounded real halfplane intersection can be nonempty while containing no integer lattice parameter point.

The regression suite preserves such a counterexample. Therefore continuous LP feasibility followed by rounding is not a valid replacement for the integer solver.

## 6. A3-G09 — Base-independent reachability from a strict cone

If the homogeneous parameter cone of a threshold pattern contains a strict integer recession direction, then

\[
\boxed{\text{the pattern is reachable for every affine base score }g.}
\]

The base offset changes only how far one must travel along that direction.

Therefore the genuinely base/arithmetic-sensitive rank-two patterns are confined to lower-dimensional recession or bounded parameter cells.

## 7. A3-G10 — Branch-pattern complexity is at most quadratic

After choosing the exact basis `h_1,h_2`, every nonconstant guard defines one affine threshold line in the `(s,t)` plane:

\[
g_j+s h_{1j}+t h_{2j}=0.
\]

Let `q` be the number of nonconstant guard lines.

An arrangement of `q` real lines has at most

\[
\boxed{2q^2+1}
\]

total faces (regions, edges, and vertices), attained by a simple arrangement.

The binary `>=0 / <0` pattern is constant on each relative-open face. Integer lattice sampling can remove faces but cannot create additional sign patterns. Hence

\[
\boxed{
\#\{\text{reachable branch patterns in one rank-two fiber}\}
\le 2q^2+1.
}
\]

Thus fixed hidden rank two produces at most quadratic branch geometry rather than the syntactic `2^r` explosion.

This is an application of standard hyperplane-arrangement mathematics, not an A3 originality claim.

## 8. Implementation

Added:

- `src/enterprise_math/rank_two_guard_reachability.py`;
- `tests/test_rank_two_guard_reachability.py`.

Main APIs:

- `rank_two_lattice_basis`;
- `rank_two_basis_coordinates`;
- `rank_two_threshold_pattern_witness`;
- `rank_two_threshold_pattern_reachable`;
- `rank_two_threshold_pattern_face_bound`.

`RankTwoPatternWitness` returns the exact lattice basis, integer parameters, realized guard scores, certificate mode, and bounded-case scan width.

## 9. Verification

Current checks cover:

1. exact basis reconstruction from redundant rank-two generators;
2. membership recovery for original generators and many integer combinations;
3. strict recession witnesses;
4. recession-ray/line witnesses and unreachable cases;
5. bounded finite-scan witnesses;
6. a bounded real-but-no-integer counterexample;
7. closed solver versus bounded parameter enumeration on small rank-two families;
8. actual reachable pattern counts below the arrangement face bound.

Several thousand additional random small-integer rank-two lattice/base/pattern cases were pressure-tested against direct parameter enumeration without a detected conflict. That randomized check is implementation evidence, not a substitute for the integer proof.

The current execution environment still cannot clone GitHub through local DNS, so full repository pytest/CI is not claimed.

## 10. Prior-art boundary

The following are standard tools and are not claimed as A3 inventions:

- Hermite normal form and integer lattice bases;
- Bezout/Smith/Hermite subgroup reduction;
- low-dimensional integer linear feasibility;
- polyhedral recession cones;
- hyperplane arrangements and face-count bounds.

The A3-specific novelty question remains only at the synthesis/interface level

\[
W(K_A)
\to
\text{exact reachable branch patterns}
\to
\text{future-safe relation precision},
\]

and remains `NOVELTY_UNVERIFIED` pending explicit prior-art mapping.

## 11. Next

Rank 0, 1, 2, and the full-rank endpoint now have exact treatments.

The next unresolved region is

\[
\boxed{2<\operatorname{rank}L_G<r.}
\]

Priority directions:

1. lift the rank-two certificate trichotomy to fixed hidden rank `d` via rational polyhedral cones and lower-rank face recursion;
2. separate the `O(r^d)` hyperplane-arrangement pattern bound from arithmetic lattice holes;
3. determine whether Smith/Hermite plus fixed-dimension integer feasibility gives a unified solver without duplicating general Presburger/ILP theory inside A3;
4. connect rank-two reachability to piecewise coarse-effect equality for a state-dependent exact branch-erasure checker;
5. relay the result to A2/P023 as an A3 specialization and a new precision/complexity obligation.
