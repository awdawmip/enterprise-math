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

`MET AT AN EXPLICIT QUANTIFIED TEMPLATE / NO UNIVERSAL B6 IMPROVEMENT CLAIMED`

The exact terminal theorem is:

> In `R^6`, freeze Lassak's one cap plus 32 sign-sector atoms. Allow every legal cap parameter, every horizontal `O(5)` rotation fixing the lens axis, and arbitrary deterministic boundary tie-breaking, but allow only coarsening by unions of whole atoms. Then the atom incompatibility graph is `K_33`. Hence no strict-diameter coarsening has fewer than 33 parts.

This is a template obstruction, **not** a lower bound `b(6)>=33`. The retained Euclidean status remains

`7 <= b(6) <= 33`.

A 32-part construction can escape the theorem only by leaving the frozen atom-coarsening class, e.g. by splitting an old atom, redrawing walls, truncating the lens, moving an apex, or introducing another R6 geometric ingredient.

## 1. Source and reconstruction boundary

The official Institute of Mathematics PAS record verifies Marek Lassak's 1982 journal article *An estimate concerning Borsuk partition problem*, volume 30, issue 9-10, pages 449-451, but marks remote digital access as restricted. A public ResearchGate page identifies an author-uploaded full text, but its PDF bytes were not retrievable through the available tools. No claim is made that an inaccessible primary PDF was read.

The proof details below are reconstructed from Béla Bollobás's published treatment of the Borsuk problem, where he explicitly states that the proof he gives for this bound is Lassak's proof, and are cross-checked against Tolmachev–Voronov 2026, whose Theorem 4 restates Lassak's universal two-ball cover in general dimension.

This access/provenance boundary is frozen in:

`research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/source_manifest_20260902.json`.

## 2. Exact reconstruction of Lassak's `2^(n-1)+1` construction

Let `K subset R^n` have diameter 1. Jung's theorem gives the radius

`r = sqrt(n/(2n+2))`.

In the Lassak/Bollobás normalization, choose an enclosing radius-`r` ball and a point `c in K` at its north pole,

`c=(0,...,0,r)`.

Because `diam(K)=1`, every point of `K` lies in the unit ball centered at `c`, so

`K subset L := B_r(0) intersect B_1(c)`.

Fix `0<delta<r`, put

`h=sqrt(r^2-delta^2/4)`

and

`ell=1/(2r)-r>0`.

Cut off the top cap

`D0=L intersect {x_n>h}`.

Its diameter is at most

`2 sqrt(r^2-h^2)=delta<1`.

Cut the remainder by the coordinate hyperplanes

`x_1=0,...,x_(n-1)=0`.

This creates `2^(n-1)` sign sectors. In one sector, for `a,b` all horizontal products `a_i b_i` are nonnegative.

If `min(a_n,b_n)>=-ell`, then `a_n b_n>=-ell h`, hence

`|a-b|^2 <= 2r^2+2ell h`.

If, say, `a_n<-ell`, the constraint `a in B_1(c)` gives

`|a|^2 <= 1+2r a_n-r^2`.

Using the nonnegative horizontal inner product and `b_n<=h`,

`|a-b|^2 <= 1+2a_n(r-b_n) < 1-2ell(r-h)`.

Since

`-2ell r = 2r^2-1`,

the right side equals

`2r^2+2ell h`.

Finally `h<r`, so

`2r^2+2ell h < 2r^2+2ell r = 1`.

Thus every sector has strict diameter below 1, as does the cap. Therefore

`b(n) <= 2^(n-1)+1`.

For `n=6`, Lassak's construction is exactly

`1 cap + 32 sign sectors = 33 parts`.

## 3. Exact R6 lens constants

For `n=6`,

`r^2=3/7`.

With

`ell=1/(2r)-r`,

one gets

`ell^2=1/84`

and, since `r,ell>0`,

`2r ell=1/7`.

Hence

`2r^2+2r ell=1`.

The two sphere boundaries

`|x|=r`, `|x-c|=1`

meet in the horizontal hyperplane

`x_6=-ell`.

If `rho` is the horizontal radius of this intersection sphere, then

`rho^2=r^2-ell^2=5/12`.

This sphere supplies exact witnesses for the new obstruction.

## 4. Frozen atom-coarsening template

For arbitrary `0<delta<r`, let `h=sqrt(r^2-delta^2/4)`. Choose any horizontal orthonormal frame, equivalently any `O(5)` rotation fixing `e_6`.

Freeze 33 atoms:

- `D0=L intersect {x_6>h}`;
- for every `sigma in {+-1}^5`,
  `D_sigma=L intersect {x_6<=h} intersect {sigma_i x_i>=0, i=1,...,5}`,
  with any deterministic boundary tie-breaking.

Allowed new partition pieces are unions of complete atoms only.

Each atom individually has diameter `<1` by Lassak's argument.

## 5. Cap-sector incompatibility

For a sign vector `sigma`, let

`u_sigma=sigma/sqrt(5)`

in the horizontal five-space, and set

`a_sigma=rho u_sigma-ell e_6`.

All five horizontal coordinates have strict signs `sigma`, and

`-ell<h`,

so `a_sigma` lies strictly inside the corresponding sector relative to the cut hyperplanes.

The north pole

`c=r e_6`

lies strictly in the cap because `h<r`.

Since `a_sigma` lies on the two-sphere intersection,

`|a_sigma-c|^2`

`=rho^2+(r+ell)^2`

`=(r^2-ell^2)+(r^2+ell^2+2r ell)`

`=2r^2+2r ell`

`=1`.

Therefore the cap cannot be merged with any complete sector.

## 6. Sector-sector incompatibility

Let `sigma != tau`. Pick `j` with `sigma_j=-tau_j`.

Define horizontal unit vectors

`u_j=3 sigma_j/sqrt(13)`, `u_i=sigma_i/sqrt(13)` for `i!=j`,

and analogously

`v_j=3 tau_j/sqrt(13)`, `v_i=tau_i/sqrt(13)`.

Every coordinate is nonzero, so both directions are strict interior directions of their respective sign orthants.

Their inner product satisfies

`u dot v`

`=(-9 + sum_(i!=j) sigma_i tau_i)/13`

`<=(-9+4)/13`

`=-5/13`.

Now put

`a=rho u-ell e_6`, `b=rho v-ell e_6`.

Both points lie on the lens intersection sphere and in the corresponding sector interiors. Hence

`|a-b|^2`

`=2rho^2(1-u dot v)`

`>=2*(5/12)*(1+5/13)`

`=15/13`

`>1`.

Thus no two distinct sectors can be merged.

## 7. `K_33` incompatibility theorem

There are

`32`

cap-sector pairs and

`C(32,2)=496`

sector-sector pairs. Their sum is

`528=C(33,2)`.

Every unordered pair of distinct atoms is incompatible, so the incompatibility graph is exactly

`K_33`.

### Theorem

For every legal `delta`, every horizontal `O(5)` rotation, and every boundary tie-breaking convention, any strict-diameter partition obtained only by coarsening the 33 whole Lassak atoms uses at least 33 parts.

The original 33 atoms already form a strict-diameter partition, so the minimum inside this frozen template is exactly 33.

This proves the task-valid terminal outcome

`FROZEN_LASSAK_COMPRESSION_TEMPLATE_CANNOT_BEAT_33`.

The smallest necessary escape is structural: at least one original atom must be split/repartitioned or some other geometric boundary of the template must change.

## 8. R4-to-R6 transfer audit

Tolmachev–Voronov's R4 method does not obtain 8 parts by simply merging two of Lassak's 9 original atoms. It changes the geometry: unit-distance truncations create a universal covering system of lens variants, and each variant is repartitioned by cone-like pieces. This is exactly the sort of escape not covered by the `K_33` theorem.

The exact transfer classification is:

| R4 ingredient | R6 classification | Reason |
|---|---|---|
| general Lassak two-ball lens | `EXACTLY_TRANSFERABLE_TO_R6` | stated in general dimension |
| UCS split by parallel hyperplanes one unit apart | `EXACTLY_TRANSFERABLE_TO_R6` | dimension-independent |
| centered orthogonal unit-width slabs | `EXACTLY_TRANSFERABLE_TO_R6` | all-dimensional lemma below |
| rhombic-dodecahedron normal completion and four-orbit reduction | `DIMENSION_4_SPECIFIC` | uses the three-dimensional projection geometry of R4 |
| hypercube vertex rays / facet cones | `EXACTLY_TRANSFERABLE_TO_R6` combinatorially | R6 gives 64 directions and 12 facets |
| strict `<1` diameter for every optimized truncated cone piece | `TRANSFERABLE_WITH_NEW_R6_LEMMA` | the naive center-fixed R6 port is exactly false |
| circumscribed-polyhedron outer validation machinery | `TRANSFERABLE_WITH_NEW_R6_LEMMA` | code is dimension-parameterized, but an R6 UCS and global certificate are missing |

The complete machine-readable audit is:

`research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/r4_to_r6_transfer_audit_20260902.json`.

## 9. General centered-strip lemma

Let `A subset R^m` be bounded with `diam(A)<=1` and `0 in A`.

Then there exist `m-1` pairwise orthonormal unit vectors `u_1,...,u_(m-1)` such that

`|<u_i,x>|<=1/2`

for every `x in A`.

Proof. In any subspace `W` of dimension at least 2 define

`a(u)=sup_(x in A)<u,x>`

and

`b(u)=sup_(x in A)<-u,x>`.

Because `A` is bounded these support functions are continuous; because `0 in A` they are nonnegative. The diameter bound gives

`a(u)+b(u)<=1`.

The continuous function `a-b` on the connected unit sphere of `W` is odd, so it has a zero. At such a direction,

`a(u)=b(u)<=1/2`.

Choose that direction, restrict to its orthogonal complement in `W`, and iterate until one dimension remains.

For the five-dimensional projection relevant to R6, four mutually orthogonal centered unit-width slabs therefore exist. The initial slab-selection mechanism itself is not the R6 bottleneck.

The missing step is a five-dimensional analogue of the R4 normal-completion/orbit geometry plus a strict R6 diameter certificate after repartitioning.

## 10. Uniform no-go for the naive R6 cube-facet port

A second exact theorem blocks a particularly natural but insufficient transfer.

Keep the untruncated R6 Lassak lens and put the cone apex at `0`, the center of the radius-`r` ball. For arbitrary `Q in O(6)`, use the 64 normalized cube directions

`d_v=Qv/sqrt(6)`, `v in {+-1}^6`.

The 12 cube facets define 12 cone parts.

Let

`z=Q^T e_6`

and choose `j` with maximal `|z_j|=M`.

For the other five coordinates choose signs with signed sum `S` satisfying

`|S|<=M`.

This follows by a greedy sign-balancing lemma: if a current partial signed sum has magnitude at most `M` and the next number has magnitude at most `M`, choose its sign to reduce the absolute value; the new magnitude remains at most `M`.

Choose a cube vertex `v` whose `j` coordinate has the sign of `z_j` and whose other signs realize `S`. Let `w` keep the same `j` sign and reverse the other five signs.

Then `v,w` lie in the same cube facet and

`<d_v,d_w>=(1-5)/6=-2/3`.

Their axial components are

`(M+S)/sqrt(6)>=0`

and

`(M-S)/sqrt(6)>=0`.

Therefore along both rays the small sphere is met at `r d_v` and `r d_w`, and those points still lie in the unit ball centered at `c` because for nonnegative axial component

`|r d-c|^2=2r^2(1-<d,e_6>)<=2r^2=6/7<1`.

So both points belong to the same facet-cone part of the lens. Their squared distance is

`2r^2(1+2/3)`

`=2*(3/7)*(5/3)`

`=10/7`

`>1`.

Hence for **every** cube orientation at least one center-fixed untruncated R6 facet cone has diameter greater than 1.

This theorem does not block truncation, movable apex, non-hypercubic directions, multiple UCS representatives, or atom splitting.

## 11. Deterministic exact checker

Checker:

`research_checks/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE_CHECK_20260902.py`

It uses only integer/rational arithmetic for the finite symbolic subcertificates and verifies:

- `r^2=3/7`, `ell^2=1/84`, `rho^2=5/12`;
- `2r ell=1/7`;
- cap-sector distance squared `1`;
- all 496 sector pairs with lower bound at least `15/13`;
- all 32 cap-sector incompatibilities;
- `528=C(33,2)` total incompatibility edges;
- center-fixed cube-facet lower bound `10/7`.

Expected output:

`PASS GEO8 exact Lassak R6 obstruction: atoms=33 incompatibility_edges=528 sector_pair_lb2=15/13 center_fixed_facet_lb2=10/7`

The checker is deliberately not used as a substitute for the continuous `O(5)` invariance or arbitrary-`O(6)` sign-balancing proofs above.

## 12. Artifacts and adversarial audit

Frozen artifacts:

- `research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/lassak_r6_exact_obstruction_20260902.json`
- `research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/r4_to_r6_transfer_audit_20260902.json`
- `research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/theorem_dependency_graph_20260902.json`
- `research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/source_manifest_20260902.json`
- `research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/adversarial_audit_20260902.json`

Adversarial checks explicitly cover:

- orthant-boundary tie-breaking;
- all legal cap parameters;
- all horizontal `O(5)` rotations;
- strict-interior witness placement;
- the distinction between a template lower bound and `b(6)>=33`;
- arbitrary cube orientation in the `10/7` subtemplate no-go;
- the fact that the full R4 truncation strategy remains outside that no-go;
- the prohibition on using finite/floating-point evidence as a universal R6 theorem;
- the remote-access limitation of the Lassak primary PDF.

Audit verdict:

`PASS_FOR_RESTRICTED_TEMPLATE_TERMINAL_OUTCOME`.

## 13. Residue and Driver handoff

The Euclidean value `b(6)` remains open in the retained interval

`7 <= b(6) <= 33`.

What is closed here is the route

`MERGE_WHOLE_LASSAK_ATOMS -> CANNOT_REDUCE_33_TO_32`.

Any genuine improvement must introduce at least one new freedom, such as:

- split/repartition an original Lassak atom;
- construct a five-dimensional truncation/UCS normal system;
- move or multiply cone apices;
- use non-hypercubic directions;
- prove another continuous R6 covering lemma outside the frozen coarsening class.

Driver-review strength should be exactly:

`LASSAK_R6_33_ATOM_COARSENING_INCOMPATIBILITY_GRAPH_IS_K33_AND_NAIVE_CENTER_FIXED_R6_CUBE_FACET_PORT_HAS_UNIFORM_10_OVER_7_OBSTRUCTION`.

Do **not** promote this to `b(6)=33`, to a global impossibility of `b(6)<=32`, or to a proof that the full Tolmachev–Voronov strategy cannot extend to R6.

Method harvest:

`RESULT_ONLY / EXACT_TEMPLATE_OBSTRUCTION_AND_R4_TO_R6_TRANSFER_AUDIT`.

No Working Truth, Foundation authority, P000 transfer, canonical native-geometry promotion, or historical novelty claim is requested.
