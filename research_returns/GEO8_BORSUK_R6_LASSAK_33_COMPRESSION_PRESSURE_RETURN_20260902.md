# GEO8 Borsuk R6 Lassak-33 constructive compression pressure — Research Return

Task: `RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE`  
Publication: `TP2-D425335E9566A3F6A54C`  
Researcher-ID: `EM-GEO8-4BBDEB`  
Claim: `CLM-3CEADA27494A571470B7`  
Execution branch: `research/geo8-borsuk-r6-lassak-33-compression-pressure-em-geo8-4bbdeb`

## Terminal verdict

`SUCCESS / FROZEN_LASSAK_COMPRESSION_TEMPLATE_CANNOT_BEAT_33`

Hard target:

`BORSUK_R6_LASSAK_33_BOUND_STRICTLY_IMPROVED_OR_TEMPLATE_OBSTRUCTION_EXACTLY_CLASSIFIED`

Disposition:

`MET AT EXPLICIT FROZEN-TEMPLATE LEVEL / NO UNIVERSAL B6 IMPROVEMENT CLAIMED`

The strongest exact conclusion reached is:

> In the six-dimensional Lassak construction, freeze the one cap atom and the 32 sign-sector atoms, allow any legal cap parameter and any horizontal `O(5)` rotation, and allow only coarsening by unions of whole atoms. Then the incompatibility graph of the 33 atoms is exactly `K_33`. Consequently no two atoms can be merged while retaining strict diameter `<1`, and every member of this frozen coarsening template requires all 33 pieces.

This is **not** a theorem that `b(6)>=33`. It does not exclude a 32-part construction that splits an old atom, redraws the walls, truncates the lens differently, moves the cone apex, or introduces a genuinely new R6 geometric ingredient. The retained external status therefore remains

`7 <= b(6) <= 33`.

## 1. Source-faithful reconstruction of the Lassak construction

The official Institute of Mathematics PAS record verifies Lassak's 1982 published article and its bibliographic data, but marks the remote digital full text as restricted. An author-uploaded full-text page is publicly discoverable, but its PDF bytes were not retrievable through the available research tools. I therefore do not claim to have read an inaccessible primary PDF.

For the proof details I used Béla Bollobás's published treatment, which explicitly identifies its proof of the Lassak bound as Lassak's proof, and cross-checked the construction type against Tolmachev–Voronov 2026, whose Theorem 4 restates Lassak's universal two-ball cover in general dimension. The source and access boundary is frozen in the source manifest.

Let `K subset R^n` have diameter 1. Jung's theorem gives an enclosing ball of radius

`r = sqrt(n/(2n+2))`.

Choose coordinates so a point `c` of `K` on the enclosing `r`-ball is the north pole

`c=(0,...,0,r)`.

Since every point of `K` is at distance at most 1 from `c`, one has

`K subset L := B_r(0) intersect B_1(c)`.

Thus it is enough to partition the universal lens `L`.

Fix `0<delta<r` and set

`h = sqrt(r^2-delta^2/4)`,

`ell = 1/(2r)-r >0`.

Cut off the top cap

`D0 = L intersect {x_n>h}`.

Its diameter is at most

`2 sqrt(r^2-h^2)=delta<1`.

Cut the remainder by the first `n-1` coordinate hyperplanes. This gives `2^(n-1)` sign sectors. In a fixed sector all products `a_i b_i` for `i<n` are nonnegative. For `a,b` in that sector, there are two cases.

If `min(a_n,b_n)>=-ell`, then `a_n b_n>=-ell h`, hence

`|a-b|^2 <= 2r^2+2ell h`.

If, say, `a_n<-ell`, the condition `a in B_1(c)` implies

`|a|^2 <= 1+2r a_n-r^2`.

Using the nonnegative horizontal inner product and `b_n<=h`,

`|a-b|^2 <= 1+2a_n(r-b_n) < 1-2ell(r-h)`.

The identity

`-2ell r = 2r^2-1`

turns the last expression into

`2r^2+2ell h`.

Because `h<r`,

`2r^2+2ell h < 2r^2+2ell r = 1`.

Therefore the cap and all sign sectors have strict diameter below 1, proving

`b(n) <= 2^(n-1)+1`.

For `n=6` this is exactly one cap plus 32 sectors, hence `b(6)<=33`.

## 2. Exact R6 constants and the lens intersection sphere

From `n=6`,

`r^2 = 3/7`.

The parameter

`ell=1/(2r)-r`

satisfies

`ell^2=1/84`,

`2r ell=1/7`,

and therefore

`2r^2+2r ell=1`.

The two sphere boundaries

`|x|=r`,

`|x-c|=1`

intersect in the horizontal hyperplane

`x_6=-ell`.

If `rho` is the horizontal radius of that intersection sphere, then

`rho^2=r^2-ell^2=5/12`.

This codimension-one sphere supplies exact incompatibility witnesses between the frozen Lassak atoms.

## 3. Frozen Lassak atom-coarsening template

Freeze the following construction class.

For arbitrary `0<delta<r`, let `h=sqrt(r^2-delta^2/4)`. Choose any orthonormal horizontal frame, equivalently any `O(5)` rotation fixing `e_6`.

The atoms are:

- one cap atom `D0=L intersect {x_6>h}`;
- for each sign vector `sigma in {+-1}^5`, one sector atom
  `D_sigma=L intersect {x_6<=h} intersect {sigma_i x_i>=0, i=1,...,5}`,
  with any deterministic boundary tie-breaking.

Allowed new parts are unions of whole atoms. Splitting an atom or redrawing a wall leaves the frozen template.

Every individual atom has diameter `<1` by the Lassak proof above.

## 4. Cap-versus-sector incompatibility

Fix a sign vector `sigma`. Put

`u_sigma = sigma/sqrt(5)`

in the horizontal five-space and define

`a_sigma = rho u_sigma - ell e_6`.

All horizontal coordinates of `a_sigma` have the strict signs prescribed by `sigma`, and `x_6=-ell<h`, so it lies in the interior of the sector relative to the cut halfspaces.

The north pole

`c=r e_6`

lies in the cap because `h<r`.

Since `a_sigma` is on the two-sphere intersection,

`|a_sigma-c|^2`

`= rho^2+(r+ell)^2`

`= (r^2-ell^2)+(r^2+ell^2+2r ell)`

`=2r^2+2r ell`

`=1`.

Thus the union of the cap with any complete sector has diameter at least 1. No cap-sector pair can be merged.

## 5. Sector-versus-sector incompatibility

Let `sigma != tau` be two sign vectors. Choose an index `j` with `sigma_j=-tau_j`.

Define horizontal unit vectors by

`u_j=3 sigma_j/sqrt(13)`, `u_i=sigma_i/sqrt(13)` for `i!=j`,

and analogously

`v_j=3 tau_j/sqrt(13)`, `v_i=tau_i/sqrt(13)`.

Every coordinate is nonzero, so these are strict-interior directions of their respective sign orthants.

Their inner product is

`u dot v = (-9 + sum_{i!=j} sigma_i tau_i)/13 <= (-9+4)/13=-5/13`.

Place both directions on the lens intersection sphere:

`a=rho u-ell e_6`,

`b=rho v-ell e_6`.

Then `a` and `b` lie in the corresponding sector interiors and

`|a-b|^2 = 2 rho^2 (1-u dot v)`

`>= 2*(5/12)*(1+5/13)`

`=15/13`

`>1`.

Hence no two distinct sectors can be merged.

## 6. Complete incompatibility theorem

There are 33 atoms. The previous two sections give:

- 32 cap-sector incompatibilities;
- `C(32,2)=496` sector-sector incompatibilities.

The total is

`32+496=528=C(33,2)`.

Therefore the atom incompatibility graph is exactly

`K_33`.

### Theorem — frozen Lassak coarsening rigidity in R6

For every legal cap parameter `0<delta<r`, every horizontal `O(5)` rotation, and every boundary tie-breaking convention, a strict-diameter partition obtained solely by unions of the 33 whole Lassak atoms has at least 33 parts.

Since the original 33 atoms already form a valid strict-diameter partition, the minimum inside this frozen template is exactly 33.

This proves the valid terminal outcome

`FROZEN_LASSAK_COMPRESSION_TEMPLATE_CANNOT_BEAT_33`.

The minimal structural escape is immediate: any construction with at most 32 parts must split/repartition at least one original Lassak atom or otherwise alter the geometric decomposition.

## 7. R4 truncation/UCS transfer audit

Tolmachev–Voronov do not obtain `8` in R4 by simply merging two of Lassak's 9 old parts. They first replace the single lens by a small universal covering system of truncated lens variants and then repartition each variant by cone-like pieces. This is exactly the kind of new freedom required by the K33 obstruction above.

The transfer classification is:

| R4 ingredient | R6 classification | Exact reason |
|---|---|---|
| general Lassak two-ball lens | `EXACTLY_TRANSFERABLE_TO_R6` | stated in general dimension |
| splitting a UCS by parallel hyperplanes one unit apart | `EXACTLY_TRANSFERABLE_TO_R6` | dimension-independent set argument |
| centered orthogonal width-one slab selection | `EXACTLY_TRANSFERABLE_TO_R6` | admits the all-dimensional lemma below |
| rhombic-dodecahedron normal completion and four-orbit reduction | `DIMENSION_4_SPECIFIC` | uses the 3D projection geometry of R4 |
| hypercube vertex rays / facet cones | `EXACTLY_TRANSFERABLE_TO_R6` combinatorially | becomes 64 directions and 12 facets |
| strict `<1` diameter for all optimized truncated cone pieces | `TRANSFERABLE_WITH_NEW_R6_LEMMA` | the simplest R6 port is exactly false |
| outer polyhedral validation machinery | `TRANSFERABLE_WITH_NEW_R6_LEMMA` | code is dimension-parameterized, but an R6 cover and global certificate are still missing |

### General centered-strip lemma

Let `A subset R^m` be bounded with diameter at most 1 and `0 in A`. Then there exist `m-1` pairwise orthonormal unit vectors `u_1,...,u_{m-1}` such that

`|<u_i,x>|<=1/2`

for every `x in A` and every `i`.

Proof: in any subspace `W` of dimension at least 2, define

`a(u)=sup_{x in A}<u,x>`,

`b(u)=sup_{x in A}<-u,x>`.

Both are continuous and nonnegative on the unit sphere of `W`, and diameter at most 1 gives `a(u)+b(u)<=1`. The continuous function `a-b` is odd. Since the unit sphere of `W` is connected, it vanishes at some `u`; then `a(u)=b(u)<=1/2`. Pass to `u^perp intersect W` and iterate until one dimension remains.

For the five-dimensional projection relevant to R6, this gives four mutually orthogonal centered unit-width slabs. Thus the first slab-selection step is not the R6 obstruction.

The genuinely missing geometry is a five-dimensional replacement for the R4 rhombic-dodecahedron completion/orbit reduction together with a strict R6 diameter certificate after the ensuing repartition.

## 8. Exact no-go for the naive center-fixed R6 cube-facet port

A second exact obstruction isolates another tempting but insufficient transfer.

Keep the untruncated R6 Lassak lens and put the cone apex at the center `0` of the radius-`r` ball. Take any `Q in O(6)` and the 64 normalized cube-vertex directions

`d_v=Qv/sqrt(6)`, `v in {+-1}^6`.

The 12 cube facets define 12 cones.

Let

`z=Q^T e_6`

and choose an index `j` for which `|z_j|` is maximal, say `M`.

For the other five coordinates choose signs so their signed sum `S` satisfies `|S|<=M`. This follows by the elementary greedy sign-balancing lemma: starting from zero, when adding a number of magnitude at most `M`, choose its sign to reduce the current absolute value; the partial sum remains of magnitude at most `M`.

Choose a cube vertex `v` whose `j` coordinate has the sign of `z_j` and whose other signs realize `S`. Let `w` keep the same `j` sign and reverse all other five signs. Then `v,w` lie in the same cube facet and

`<d_v,d_w>=(1-5)/6=-2/3`.

Their axial components are

`(M+S)/sqrt(6)>=0`,

`(M-S)/sqrt(6)>=0`.

Hence along both rays the small sphere `|x|=r` is reached at `r d_v` and `r d_w` while those points still lie inside the unit ball centered at `c`. Therefore both are lens boundary points in the same facet cone.

Their squared distance is

`2r^2(1+2/3)`

`=2*(3/7)*(5/3)`

`=10/7`

`>1`.

Thus **for every cube orientation**, at least one center-fixed untruncated R6 facet cone fails the strict-diameter test.

This does not refute the full R4-style strategy: truncation, movable apex, new cone directions, multiple UCS representatives, and atom splitting remain available.

## 9. Deterministic exact checker

The checker uses only Python integer/rational arithmetic for all finite symbolic subcertificates. It verifies:

- `r^2=3/7`, `ell^2=1/84`, `rho^2=5/12`;
- `2r ell=1/7` through the positive squared identity;
- exact cap-sector distance squared `1`;
- all 496 sector pairs and the uniform lower bound `15/13`;
- all 32 cap-sector incompatibilities;
- complete incompatibility count `528=C(33,2)`;
- the center-fixed cube-facet lower bound `10/7`.

Expected summary:

`PASS GEO8 exact Lassak R6 obstruction: atoms=33 incompatibility_edges=528 sector_pair_lb2=15/13 center_fixed_facet_lb2=10/7`

Checker:

`research_checks/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE_CHECK_20260902.py`

The checker does not pretend to replace the continuous `O(5)` invariance or arbitrary-`O(6)` sign-balancing proofs; those are proved analytically above.

## 10. Frozen artifacts

- exact obstruction certificate:
  `research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/lassak_r6_exact_obstruction_20260902.json`
- R4-to-R6 transfer audit:
  `research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/r4_to_r6_transfer_audit_20260902.json`
- theorem dependency graph:
  `research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/theorem_dependency_graph_20260902.json`
- source manifest:
  `research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/source_manifest_20260902.json`
- adversarial audit:
  `research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/adversarial_audit_20260902.json`

## 11. Adversarial scope audit

The following possible overclaims were explicitly killed.

1. **Boundary convention:** sector witnesses have no zero horizontal coordinates, so orthant tie-breaking cannot remove them.
2. **Cap parameter:** the intersection sphere stays at `x_6=-ell<0<h` for every legal `delta`, while `c` stays strictly above the cap cut.
3. **Horizontal rotation:** the lens is invariant under `O(5)` fixing its axis, so rotating the explicit witness family preserves the theorem.
4. **Borsuk lower bound:** no statement `b(6)>=33` is made.
5. **Full R4 transfer:** the `10/7` no-go is restricted to center-fixed, untruncated cube-facet cones.
6. **Numerical universality:** no finite sample, Monte Carlo search, or floating-point optimizer is used to prove a universal R6 bound.
7. **Source access:** the inaccessible primary Lassak PDF is not represented as read.

Adversarial verdict:

`PASS_FOR_RESTRICTED_TEMPLATE_TERMINAL_OUTCOME`.

## 12. Residue and Driver handoff

The world-class Euclidean gap is not closed:

`7 <= b(6) <= 33` remains the retained status.

What is now closed is a precise route:

`MERGE_EXISTING_LASSAK_ATOMS -> CANNOT_REDUCE_33_TO_32`.

A genuine upper-bound improvement must introduce at least one of:

- splitting/repartitioning an original Lassak atom;
- a new five-dimensional truncation/UCS normal system;
- movable or multiple cone apices;
- non-hypercubic directions;
- another continuous R6 covering lemma not contained in the frozen coarsening class.

The R4 method remains relevant because it does exactly the first kind of structural escape, but its three-dimensional rhombic-dodecahedron orbit reduction has no proved five-dimensional replacement in this Result.

Driver recommendation:

Accept this Result at exactly the strength

`LASSAK_R6_33_ATOM_COARSENING_INCOMPATIBILITY_GRAPH_IS_K33_AND_NAIVE_CENTER_FIXED_R6_CUBE_FACET_PORT_HAS_UNIFORM_10_OVER_7_OBSTRUCTION`.

Do not interpret it as `b(6)=33`, as a global impossibility of `b(6)<=32`, or as a proof that the full Tolmachev–Voronov truncation strategy cannot be generalized.

Method harvest:

`RESULT_ONLY / EXACT_TEMPLATE_OBSTRUCTION_AND_R4_TO_R6_TRANSFER_AUDIT`.

No Working Truth, Foundation authority, P000 transfer, canonical native-geometry promotion, or historical novelty claim is requested.
