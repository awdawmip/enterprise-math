# R033 FCC/HCP Intrinsic Sphere Composition Atlas

Status: `RESEARCH CHECKPOINT / NOT CANONICAL`  
Researcher-ID: `EM-R033-3742D0`  
Task: `RS-R033-FCC-HCP-INTRINSIC-SPHERE-COMPOSITION-ATLAS`  
Taskbook source: `e6ddf1f4c7caec26d0d64d8ef9b7d8f5b95c1b46`  
CI: `CI_NOT_REQUIRED_FOR_RESEARCH`

## Executive result

The intrinsic nearest-neighbor graph ball is a coherent native sphere object, but it does **not** approach a Euclidean ball. The compact macroscopic descriptor found is

\[
\boxed{\text{local cell alphabet}+\text{exact growth law}+\text{stable boundary spectrum}+\text{residue data}+\text{stable polyhedral norm ball}.}
\]

FCC and HCP are not macroscopically universal. Stacking memory survives in leading shell/bulk coefficients, boundary frequencies, orientation proportions, the dimensionless constant `K=A^3/V^2`, and the limit shape.

Supported return classes:

`INTRINSIC_SPHERE_COMPOSITION_LAW_FOUND`  
`POLYNOMIAL_OR_QUASIPOLYNOMIAL_GROWTH_PROVED_OR_CERTIFIED`  
`FCC_HCP_BOUNDARY_MEMORY_SURVIVES`  
`ANISOTROPIC_LIMIT_SHAPE_FOUND`  
`BOUNDARY_TYPE_SPECTRUM_STABILIZES`  
`TOPOLOGICAL_SPHERE_CONFIRMED` for the exact `r=0..20` topology atlas  
`MACRO_SCALE_10E36_SUFFICIENT`

Killed: `EUCLIDEAN_SPHERE_EMERGES`, `FCC_HCP_MACROSCOPIC_UNIVERSALITY_FOUND`.

## 1. First-principles models and exact distances

### FCC

Use `D3={(x,y,z) in Z^3 : x+y+z even}` with the twelve generators given by permutations of `(±1,±1,0)`. The independently recovered exact graph distance is

\[
d_F(x,y,z)=\max\left(|x|,|y|,|z|,{|x|+|y|+|z|\over2}\right).
\]

Hence

\[
B_r^F=D_3\cap\{\|x\|_\infty\le r,\ \|x\|_1\le2r\}.
\]

### HCP

Use integer states `(i,j,k)`, even `k` = A layer, odd `k` = B layer. Same-layer triangular directions are `(±1,0),(0,±1),(1,-1),(-1,1)`. For even `k`, the three neighbors in each adjacent layer use planar shifts `(0,0),(-1,0),(0,-1)`; for odd `k` use `(0,0),(1,0),(0,1)`. Degree is 12 and adjacency is symmetric. A/B origins are graph-equivalent under `(i,j,k)->(-i,-j,k+1)`.

Let

\[
T(i,j)=\max(|i|,|j|,|i+j|),
\]
\[
Q(i,j)=\max(i,j,i+j,-i-1,-j-1,-i-j-1).
\]

Then

\[
d_H(i,j,k)=\begin{cases}
\max(|k|,|k|/2+T(i,j)),&k\text{ even},\\
\max(|k|,(|k|+1)/2+Q(i,j)),&k\text{ odd}.
\end{cases}
\]

BFS and these formulas agree through `r=40`; the committed reference range is `r=0..20`, with a direct shell holdout at `r=100`.

## 2. Exact growth laws

For FCC, for `r>=1`,

\[
\boxed{A_r^F=10r^2+2},\qquad
\boxed{V_r^F={10r^3+15r^2+11r+3\over3}}.
\]

For HCP, for `r>=1`,

\[
\boxed{A_r^H=\begin{cases}(21r^2+4)/2,&r\text{ even},\\(21r^2+3)/2,&r\text{ odd},\end{cases}}
\]

and

\[
\boxed{V_r^H=\begin{cases}(14r^3+21r^2+14r+4)/4,&r\text{ even},\\(14r^3+21r^2+14r+3)/4,&r\text{ odd}.\end{cases}}
\]

HCP's period is exactly 2. Its layer-sum certificate uses centered triangular-lattice hexagons on even layers, with `1+3q(q+1)` sites, and shifted hexagons on odd layers, with `3(q+1)^2` sites. Thus the quasi-polynomial is not a regression artifact.

At `r=100`, exact direct-shell holdout gives FCC `A=100002` and HCP `A=105002`.

The leading shell and volume coefficient ratio is permanently

\[
\boxed{21/20}.
\]

### First irreducible difference

The full rooted induced balls already differ at `r=1`: the induced 12-shell adjacency matrices have the isomorphism-invariant values

\[
\operatorname{tr}(A^4)_F=384,\qquad \operatorname{tr}(A^4)_H=408.
\]

Shell cardinality first differs at `r=2`: FCC `42`, HCP `44`.

## 3. Boundary symmetry spectrum

For each shell cell, retain the twelve-slot outside-neighbor mask and quotient by the appropriate graph/point symmetry.

### FCC

From `r=3`, four orbit types are present:

- outside 7: `12`;
- outside 5: `24(r-1)`;
- outside 4: `6(r-1)^2`;
- outside 3: `4(r-1)(r-2)`.

The limiting frequencies are `0,0,3/5,2/5`, and

\[
\boxed{D_{TV}^F(r)={24r-12\over10r^2+2}\le {12\over5r}}.
\]

### HCP

From `r=4`, ten orbit masks stabilize: `69,228,229,448,453,458,469,581,1764,1765`. All exact period-2 population formulas are stored in `R033_BOUNDARY_TYPE_ATLAS.json`.

Only three retain positive limiting mass:

\[
p_{69}\to3/7,\qquad p_{228}\to3/7,\qquad p_{448}\to1/7.
\]

The other seven total exactly `24r-12`, hence

\[
\boxed{D_{TV}^H(r)={24r-12\over A_r^H}\le {16\over7r}}.
\]

Orientation memory also survives: FCC has six unoriented exposed-face normal classes at exactly `1/6` each. HCP has three same-layer classes at `1/6` each and six interlayer classes at `1/12` each.

## 4. Shell, exposed cells, exposed faces, topology

For these balls, the exposed-cell boundary is exactly `S_r`, but the exposed-face complex is different because one shell cell can expose several faces.

Shell-induced edges are

\[
E_S^F=24r^2,
\]

and

\[
E_S^H=\begin{cases}27r^2,&r\text{ even},\\27r^2-3,&r\text{ odd}.\end{cases}
\]

The number of ball-to-outside adjacencies, equivalently exposed Voronoi faces, is unexpectedly the same in both worlds:

\[
\boxed{F_\partial(r)=12(3r^2+3r+1)}.
\]

Exact rational Voronoi halfspaces were used to construct the union boundary complex. For every `r=0..20`, in both FCC and HCP,

\[
\boxed{F=12(3r^2+3r+1),\quad E=2F,\quad V=F+2,\quad \chi=2}.
\]

The checker also verifies one connected component, edge incidence exactly 2, and every vertex link a single cycle. Therefore every certified complex is a closed connected 2-manifold with Euler characteristic 2, hence topological `S^2`.

This is a finite exact topology certificate through the full taskbook reference range. The nested layer structure gives an all-radius shelling proof route, but that induction is not yet formalized as a repository theorem.

## 5. Limit shapes

### FCC

The exact distance formula implies for every integer `r`

\[
\operatorname{conv}(B_r^F)=rP_F,
\]

where `P_F` is the cuboctahedron

\[
\max(|x|,|y|,|z|)\le1,\qquad |x|+|y|+|z|\le2.
\]

After nearest-neighbor normalization,

\[
R_{out}=1,\qquad R_{in}=1/\sqrt2,\qquad R_{out}/R_{in}=\boxed{\sqrt2}.
\]

Thus FCC anisotropy is exact at every scale.

### HCP

In ideal-HCP coefficient coordinates `(u,v,z)` with physical Gram matrix

\[
G=\begin{pmatrix}1&1/2&0\\1/2&1&0\\0&0&2/3\end{pmatrix},
\]

the stable velocity polytope is

\[
P_H=\operatorname{conv}\{(h,0),(h/2,1),(h/2,-1):h\in H\},
\]

where `H={(±1,0),(0,±1),(1,-1),(-1,1)}`. Equivalently,

\[
|z|\le1,
\]
\[
|u|+|z|/2\le1,\quad |v|+|z|/2\le1,\quad |u+v|+|z|/2\le1.
\]

It has 18 vertices. Its physical anisotropy ratio is

\[
\boxed{\sqrt{41/24}}.
\]

The exact layer description yields normalized facet-support error at most

\[
\boxed{1/(6r)}.
\]

For even `r`, all 18 limiting vertices are exactly reachable. Thus HCP converges to this 18-vertex polytope, not to the FCC cuboctahedron and not to a Euclidean sphere.

## 6. Intrinsic dimensionless constant and remainder certificate

Define

\[
K_r={A_r^3\over V_r^2}.
\]

Then

\[
\boxed{K_\infty^F=90},\qquad \boxed{K_\infty^H=189/2}.
\]

Direct positive-polynomial factorization gives, for every `r>=1`,

\[
0<90-K_r^F<{270\over r},
\]

and for both HCP residue classes,

\[
0<{189\over2}-K_r^H<{567\over2r}.
\]

The volume subleading/leading ratio in both worlds is exactly `3/(2r)`.

## 7. `10^36`--`10^38`

All three requested radii are even, so HCP uses its even residue class. Exact integers and exact reduced `K_r` rationals are stored in `R033_MACRO_10E36_10E38.json`; no brute-force enumeration is used.

At `r=10^36`:

- FCC `|K-90| < 2.70e-34`;
- HCP `|K-94.5| < 2.835e-34`;
- FCC boundary-spectrum TV error `<2.4e-36`;
- HCP boundary-spectrum TV error `<2.286e-36`;
- HCP normalized facet-support error `<=1.667e-37`;
- volume subleading/leading ratio `=1.5e-36`.

At `10^37` and `10^38`, every `O(1/r)` bound improves by one and two more orders of magnitude. Therefore `MACRO_SCALE_10E36_SUFFICIENT` is certified. Stability means each world is extremely close to its own macroscopic law; it does not mean FCC and HCP become equal.

## 8. Post-hoc continuous comparison

Only after freezing the intrinsic laws may one compare to a Euclidean ball. A Euclidean sphere would give the analogous `K=36*pi`. The intrinsic graph-ball limits are instead `90` and `94.5`, and both stable metric balls are polyhedral and anisotropic.

Therefore pi is neither an input nor the native emergent sphere constant of this nearest-neighbor graph metric. Euclidean scalar radius/area/volume belongs to a later calibration/coarse-readout layer.

## 9. Prior-art rooting after independent discovery

The exact enumeration and law discovery preceded prior-art checking.

- Conway & Sloane, *Low-Dimensional Lattices VII: Coordination Sequences*, Proc. R. Soc. Lond. A 453 (1997), already establish the Barlow-packing coordination-sequence extremal result with FCC minimum and HCP maximum. The shell laws are therefore prior art, not claimed as new Enterprise mathematics.
- Nakamura, Sakamoto, Mase & Nakagawa, *Coordination sequences of crystals are of quasi-polynomial type*, Acta Cryst. A77 (2021), DOI `10.1107/S2053273320016769`, give the general periodic-graph quasi-polynomial theorem.
- Tobias Fritz, *Velocity polytopes of periodic graphs and a no-go theorem for digital physics*, Discrete Mathematics 313 (2013), DOI `10.1016/j.disc.2013.02.010`, supplies the general cycle-weight velocity-polytope/stable-norm framework and periodic-graph anisotropy no-go result.

R033's project-side contribution at this checkpoint is the integrated representation and certificates: exact graph models/distances, boundary orbit spectra, exposed-face topology atlas, explicit FCC/HCP limit polytopes, and certified macro evaluation. No novelty claim is made for pieces already in prior art.

## 10. Direct answers

1. FCC shell: `A_0=1`; `A_r=10r^2+2` for `r>=1`.
2. HCP shell: `A_0=1`; `A_r=floor(21r^2/2)+2` for `r>=1`.
3. FCC bulk: `(10r^3+15r^2+11r+3)/3`. HCP bulk: period-2 formulas above.
4. First full rooted-graph difference: `r=1`; first shell-count difference: `r=2`.
5. Stable symmetry types: FCC `4`; HCP `10` from `r=4`.
6. Type proportions converge: FCC positive limits `3/5,2/5`; HCP `3/7,3/7,1/7`.
7. Exposed-face boundary is exact topological `S^2` for every certified `r=0..20`; all-radius formal induction remains future work.
8. Limit shape is anisotropic/polyhedral in both worlds; the two polytopes differ.
9. `r=10^36` is sufficient under explicit `O(1/r)` remainder bounds above.
10. Pi/continuous area/volume are not intrinsic inputs and do not emerge as the native graph-metric sphere law; they are later readout/calibration quantities.

## Final judgment

A huge FCC/HCP-world sphere can be described without enumerating its `O(r^3)` cells. The finite descriptor is: local 12-neighbor rule; radius plus HCP residue bookkeeping; exact shell/bulk laws; finite stable boundary alphabet with exact populations; orientation proportions; exposed-face topology certificate; and stable polyhedral norm ball with explicit finite-radius remainder.

At `10^36` these descriptors are already in a rigorously stable macro regime. The key negative result is equally strong: **the macro regime does not wash FCC and HCP into the same sphere; it freezes each into a different stable sphere law.**
