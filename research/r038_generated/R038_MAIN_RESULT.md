# R038 Semantic Checkpoint — Discrete Exact World, π, and Readout Semantics

Researcher-ID: `EM-R038-6A7D21`

Task: `RS-R038-DISCRETE-EXACT-WORLD-CONTINUUM-CONSTANTS-PI-READOUT-SEMANTICS`

Source main at claim: `092c8ced3b3a5808d8669946a830db73b129a126`

Frozen inputs consumed:

- R033 owner head `c2aa1758c6cf8f194d8b4493b90c903a2dfcd048`
- R034 owner head `674fb8717d753cd36fd83b061c869d79e8875b31`
- R037 remains a parallel audit dependency; this checkpoint does not wait for it, and any later confirmed mismatch must be absorbed.

Status: `SEMANTIC_CHECKPOINT / NOT_CANONICAL`

## 1. Executive result

The taskbook's strongest useful answer is not “π is fake” and not “π is microscopic”.

It is the following layer theorem/counterexample split.

1. **Finite FCC/HCP cellular algebra is π-free under an explicit algebraic operator discipline.** Coordinates, finite path counts, rational transition probabilities, finite moments, graph balls, polyhedral volumes and finitely many algebraic constructions remain algebraic.
2. **A nontrivial finite native FCC/HCP cellular object cannot have exact full continuous rotational symmetry.** Thus an exact Euclidean circle/sphere is not a native finite cell object in the fixed locally finite embedding.
3. **The graph-radius shell/bulk Euclidean-form readouts are exact and convention-specific:** FCC tends to `5/2`, HCP tends to `21/8`. These are not claims about classical π.
4. **There is no unique native scalar `pi_eff` without readout semantics.** The same FCC/HCP ball gives different exact constants under shell count, broken-bond count, physical volume, inradius, second-moment radius, or equal-volume Euclidean calibration.
5. **H7 is killed.** A purely discrete infinite lattice sum already gives a known transcendental:
   \[
   \sum_{m\in\mathbb Z\setminus\{0\}}\frac1{m^2}=\frac{\pi^2}{3}.
   \]
   Every finite partial sum is rational; the L2 infinite completion is where the transcendental enters. No continuum geometry is present in the definition.
6. A deeper square-lattice example independently supports the same boundary: the spanning-tree constant is defined by finite graph counts plus a thermodynamic limit and has exact expression `4G/pi` (Catalan `G`). Its own irrationality/transcendence is not established, so it is evidence for exact special-constant entry at L2, not a theorem that this particular constant is transcendental.
7. In diffusion, the exact microscopic covariance is `I/3` for both FCC and ideal HCP. Classical π enters a common continuum **density/readout** through Gaussian/Lebesgue normalization, but the Gaussian limit can also be specified by a characteristic function without writing π. Thus π is structural for some L3 representations, not logically required by the finite transition rule.

Ontology verdict:

> `pi` is not forced as an element of the finite microscopic FCC/HCP state algebra.  
> Purely discrete infinite completion can nevertheless generate exact transcendental/special constants before any continuum geometric approximation.  
> Classical `pi` is also a structural constant of Euclidean/Gaussian readouts.  
> Therefore “the finite native cellular world has no exact continuous circle” survives; “transcendentals only appear after continuum approximation” is false.

## 2. Four-layer observable taxonomy

### L0 — finite exact cellular state

Finite vertex/cell sets, adjacency, finite graph balls/shells, finite paths, transition counts, boundary edge counts.

Arithmetic type: integers plus exact coordinates from the declared embedding field.

### L1 — finite exact derived observable

Allowed task discipline:

- finite `+,-,*,/` with nonzero denominators;
- finite sums/products;
- determinants, inverses and polynomial equations over the current algebraic field;
- finitely many explicitly declared algebraic extensions.

For normalized nearest-neighbor embeddings:

- FCC coordinates lie in `Q(sqrt(2))`;
- ideal HCP coordinates lie in `Q(sqrt(2),sqrt(3)) = Q(sqrt(2),sqrt(3),sqrt(6))`;
- finite path probabilities are rational with denominator `12^n`;
- finite coordinate moments lie in the corresponding algebraic field.

### L2 — infinite discrete observable

Limits/sums/products/spectral or thermodynamic completions of exact discrete objects. This layer is **not algebraically closed under “finite-stage algebraicity”**.

Minimal counterexample:
\[
S_N=\sum_{0<|m|\le N}m^{-2}\in\mathbb Q,\qquad
\lim_{N\to\infty}S_N=\pi^2/3.
\]

### L3 — continuum/coarse/Euclidean readout

Diffusive rescaling, Gaussian density with respect to Lebesgue measure, Fourier inversion conventions, Euclidean area/volume calibration, effective radius, equal-volume sphere and other observer-selected coarse equivalences.

The “first transcendental layer” is therefore **observable-family dependent**, not globally fixed.

## 3. Finite algebraicity theorem and operator kill test

### Theorem R038-A — finite algebraic closure

Let `K/Q` be an algebraic extension containing all finite input labels/coordinates. Let an observable be represented by a finite expression tree whose leaves are elements of `K` and whose internal nodes are field operations plus finitely many algebraic root selections. Then the output is algebraic over `K`, hence algebraic over `Q`. If only field operations are used, the output remains in `K`.

Proof: induction over the finite expression tree. Field operations preserve `K`. A selected root of a nonzero polynomial with coefficients algebraic over `Q` is algebraic over `Q`; finitely many such adjunctions remain algebraic.

### Necessary scope restriction

The unrestricted statement “finite discrete observables are always algebraic” is false if the observable language itself imports analytic primitives. Example: allowing `exp(1)` at L1 produces `e`, a transcendental number. Thus the theorem is about **finite algebraic observables**, not about the word “finite” alone.

Disposition: H1 `CONFIRMED_WITH_OPERATOR_SCOPE`.

## 4. Finite native continuous-circle no-go

### Theorem R038-B — locally finite orbit no-go

Let `L` be a locally finite subset of Euclidean space and let `S subset L` contain a point `x` at nonzero radius from a chosen center `o`. If `S` were invariant under every rotation about `o`, then it would contain the full continuous rotation orbit of `x`. That orbit is an infinite compact circle/sphere. Local finiteness implies `L` has only finitely many points in that compact set, contradiction.

Therefore no nontrivial finite FCC/HCP center set has full `SO(2)`/`SO(3)` symmetry.

For a finite union of native Voronoi/polyhedral cells, the same conclusion follows from the finite nonzero vertex set: continuous rotational invariance would force an infinite orbit of a nonzero vertex.

### Equidistance locus

For fixed `R`, `{x in L: |x-o|=R}` is finite because the Euclidean sphere is compact and `L` is locally finite. It may have a large finite point-group orbit, but it is not a continuous circle/sphere.

This proves only the native-cell statement. It does **not** deny:

- exact circles in continuum mathematics;
- topological spheres;
- graph-distance spheres;
- rotationally invariant probability laws;
- rotationally invariant continuum limits.

Disposition: H2 `CONFIRMED_AT_FINITE_NATIVE_CELLULAR_SCALE`.

## 5. Exact FCC/HCP graph-radius readout

Use graph radius `r>=1`, shell count `A_r`, and ball count `V_r` as the first count-based readout:
\[
\pi_A^{graph}(r)=\frac{A_r}{4r^2},\qquad
\pi_V^{graph}(r)=\frac{3V_r}{4r^3}.
\]

### FCC

Frozen R033 formulas, independently re-enumerated in `experiments/r038_discrete_pi_readout.py`:

\[
A_r=10r^2+2,
\]
\[
V_r=\frac{10r^3+15r^2+11r+3}{3}.
\]

Hence
\[
\boxed{\pi_A^{FCC}(r)=\frac52+\frac{1}{2r^2}}
\]
and
\[
\boxed{\pi_V^{FCC}(r)=
\frac52+\frac{15}{4r}+\frac{11}{4r^2}+\frac{3}{4r^3}}.
\]

Thus both tend to `5/2`.

### HCP

The frozen R033 formulas are period-2, and the independent BFS reconstruction agrees:

\[
A_r=
\begin{cases}
(21r^2+4)/2,&r\ even,\\
(21r^2+3)/2,&r\ odd,
\end{cases}
\]

\[
V_r=
\begin{cases}
(14r^3+21r^2+14r+4)/4,&r\ even,\\
(14r^3+21r^2+14r+3)/4,&r\ odd.
\end{cases}
\]

Therefore
\[
\boxed{\pi_A^{HCP}(r)=
\begin{cases}
21/8+1/(2r^2),&r\ even,\\
21/8+3/(8r^2),&r\ odd,
\end{cases}}
\]

\[
\boxed{\pi_V^{HCP}(r)=
21/8+\frac{63}{16r}+\frac{21}{8r^2}
+\begin{cases}
3/(4r^3),&r\ even,\\
9/(16r^3),&r\ odd.
\end{cases}}
\]

Thus both tend to `21/8`.

### Local R037-style audit note

An earlier non-source summary contained a different HCP finite shell remainder. Independent HCP BFS produced `12,44,96,170,...`, which exactly matches the frozen R033 growth atlas:
`A_even=(21r^2+4)/2`, `A_odd=(21r^2+3)/2`.
No mismatch with frozen R033 was found in this local audit.

Disposition: H3 `CONFIRMED_EXACTLY`.

## 6. Readout-dependence atlas

### Channel G — shell/bulk count units

Limits:

| crystal | shell-count `pi_A` | bulk-count `pi_V` |
|---|---:|---:|
| FCC | `5/2` | `5/2` |
| HCP | `21/8` | `21/8` |

These are dimensionless count calibrations.

### Channel B — broken-nearest-neighbor boundary count

R033 gives an exact common exposed-edge count:
\[
E_\partial(r)=12(3r^2+3r+1)
\]
for both FCC and HCP.

With one unit of “area” per exposed bond:
\[
\pi_A^{bond}(r)=\frac{E_\partial(r)}{4r^2}
=9+\frac9r+\frac3{r^2}\to 9.
\]

This is a second exact readout on the **same objects**, already incompatible with `5/2` and `21/8`.

For FCC, weighting each exposed NN bond by the exact shared Voronoi-facet area `sqrt(2)/4` gives a genuine polyhedral boundary-area channel:
\[
\pi_A^{FCC,VoroBond}(r)
=\frac{\sqrt2\,E_\partial(r)}{16r^2}
\to \frac{9\sqrt2}{4}.
\]

The facet weight follows from the FCC rhombic-dodecahedral Voronoi cell: site volume `1/sqrt(2)`, inradius `1/2`, total area `3sqrt(2)`, divided among 12 congruent NN facets.

### Channel P — physical per-site volume with center circumradius

Both close packings have per-site volume
\[
v_0=1/\sqrt2
\]
when NN distance is one.

Every graph-ball center lies at Euclidean radius at most `r` by the triangle inequality, and a straight basal/NN ray reaches radius exactly `r`; hence the center circumradius is exactly `R_c=r` for both models.

Define `V_phys=v_0 V_r`. Then
\[
\pi_{V,phys}^{FCC}(r)=\pi_V^{FCC}(r)/\sqrt2
\to \frac{5\sqrt2}{4},
\]
\[
\pi_{V,phys}^{HCP}(r)=\pi_V^{HCP}(r)/\sqrt2
\to \frac{21\sqrt2}{16}.
\]

Already, merely replacing “one vertex = one volume unit” by the physical primitive-cell volume changes the asymptotic constant.

### Channel C — actual FCC convex-hull geometry

The FCC graph-ball center hull is an exact cuboctahedron for every `r`. In NN-normalized coordinates its circumradius and edge length are both `r`.

Its Euclidean surface area is
\[
A_{cub}=(6+2\sqrt3)r^2
\]
and volume is
\[
V_{cub}=(5\sqrt2/3)r^3.
\]

Therefore
\[
\pi_A^{cub}=(3+\sqrt3)/2,
\qquad
\pi_V^{cub}=5\sqrt2/4.
\]

The surface readout is neither `5/2` nor the broken-bond limit.

### Channel I — inradius

R033 exact/stable-norm atlas gives:

- FCC `R_in/r = 1/sqrt(2)` exactly;
- HCP asymptotically `R_in/r -> sqrt(24/41)` with bounded support remainder.

Using the same count observables but inradius instead of circum/graph radius changes the asymptotic values. For example:

FCC shell:
\[
\pi_A^{graph,in}\to 5.
\]

FCC bulk:
\[
\pi_V^{graph,in}\to 5\sqrt2.
\]

HCP shell:
\[
\pi_A^{graph,in}\to (21/8)(41/24)=287/64.
\]

Thus radius semantics alone destroys uniqueness.

### Channel M — second-moment radius (π-free)

Define
\[
R_2(r)^2=\frac{1}{V_r}\sum_{x\in B_r}|x|^2.
\]

For FCC:
\[
M_2^{FCC}(r)=
\frac{r(r+1)(2r+1)(7r^2+7r+6)}{10}.
\]

For ideal HCP, direct layer summation yields the exact period-2 quasipolynomial
\[
\begin{aligned}
M_2^{HCP}(r)=&
\frac{721}{480}r^5+\frac{721}{192}r^4+\frac{581}{144}r^3
+\frac{147}{64}r^2+\frac{1619}{2880}r+\frac{3}{128}\\
&+(-1)^r\frac{38r^2+38r-9}{384}.
\end{aligned}
\]

The experiment reconstructs these values exactly from the HCP neighbor graph through radius 18.

Asymptotically:
\[
R_2^{FCC}/r\to\sqrt{21/50}=\sqrt{42}/10,
\]
\[
R_2^{HCP}/r\to\sqrt{721/1680}=\sqrt{1545}/60.
\]

Using physical volume `V_r/sqrt(2)` and `R_2` therefore gives yet another pair of algebraic constants:
\[
\pi_{V,R_2}^{FCC}\to\frac{625\sqrt{21}}{441}\approx6.49458,
\]
\[
\pi_{V,R_2}^{HCP}\to\frac{1260\sqrt{3090}}{10609}\approx6.60200.
\]

### Channel E — equal-volume Euclidean radius

If one defines
\[
R_{eq}=\left(\frac{3V_{phys}}{4\pi}\right)^{1/3},
\]
then
\[
3V_{phys}/(4R_{eq}^3)=\pi
\]
identically.

This is a valid L3 calibration but cannot be evidence that π was present microscopically: π was inserted into the radius definition.

Disposition: H4 `CONFIRMED_STRONGLY`; H10 `CONFIRMED`.

## 7. Finite diffusion and the π-entry point

For uniform 12-NN propagation, every length-`n` path has probability `12^{-n}`. Therefore for any endpoint `x`,
\[
P(X_n=x)=c_n(x)/12^n\in\mathbb Q.
\]

The normalized physical FCC and ideal-HCP one-step vectors independently give:
\[
E[\Delta X]=0,\qquad E[\Delta X\Delta X^T]=I/3.
\]

No π is needed.

The fourth moments already differ. One exact coordinate audit gives:

FCC:
\[
E[x^4]=E[y^4]=E[z^4]=1/6,\quad
E[x^2y^2]=E[x^2z^2]=E[y^2z^2]=1/12.
\]

HCP A-site step law:
\[
E[x^4]=E[y^4]=5/24,\quad E[z^4]=2/9,
\]
\[
E[x^2y^2]=5/72,\quad E[x^2z^2]=E[y^2z^2]=1/18.
\]

Thus exact finite distributions are not made identical by the common covariance.

For the diffusive scaling,
\[
X_n/\sqrt n \Rightarrow N(0,I/3).
\]

The limiting characteristic function can be written
\[
\varphi(t)=\exp(-|t|^2/6),
\]
with no explicit π. If the same Gaussian is represented by its density with respect to 3D Lebesgue measure, then
\[
f(x)=\left(\frac{3}{2\pi}\right)^{3/2}\exp(-3|x|^2/2),
\]
and π appears in normalization (equivalently Fourier inversion/radial Euclidean integration).

So H6 is true as a **density/readout statement**, but “the CLT itself requires π” would be too strong.

Disposition: H5 `CONFIRMED`; H6 `CONFIRMED_WITH_REPRESENTATION_SCOPE`.

## 8. H7 kill: pure discrete infinity can generate a transcendental

Define on the one-dimensional integer lattice:
\[
S_N=\sum_{0<|m|\le N}\frac1{m^2}.
\]

Each `S_N` is rational and the definition uses only the discrete vertex labels and rational arithmetic. The L2 limit is the classical Basel value
\[
S=\sum_{m\ne0}\frac1{m^2}=\frac{\pi^2}{3}.
\]

Because classical π is transcendental, `π^2/3` is transcendental.

This kills:

`TRANSCENDENTALS_ONLY_APPEAR_AFTER_CONTINUUM_APPROXIMATION`.

It does **not** imply that every L2 observable is transcendental, or that π is a microscopic FCC/HCP state constant. It proves only that infinite completion is a separate gateway not controlled by finite algebraicity.

### Deeper lattice cross-check — square spanning-tree constant

For finite square-lattice graphs let `n_L(N)` count spanning trees. The infinite square-lattice constant is defined by
\[
\lambda=\lim_{N\to\infty}\frac{\log n_L(N)}{N}.
\]

Viswanathan (arXiv:1706.00799, Eqs. 1 and 5) records the exact square-lattice value
\[
\lambda=4G/\pi,
\]
where `G` is Catalan's constant. This definition is pure graph enumeration plus an infinite-volume limit; the Fourier integral is an evaluation tool, not part of the native graph definition.

As of the checked literature, irrationality of `G` itself remains open; therefore this example is classified as:

`L2_EXACT_SPECIAL_CONSTANT / TRANSCENDENCE_OF_THIS_VALUE_NOT_ESTABLISHED`.

It corroborates H8 but is not used as the rigorous transcendence witness. The Basel lattice sum is the rigorous witness.

Disposition: H7 `KILLED`; H8 `CONFIRMED`.

## 9. Circle/sphere as an observable-relative equivalence class

Use equality of limiting readout vectors rather than an epsilon relation, so transitivity is automatic.

For a model `X` define:

- ballistic readout `B(X)` = its stable velocity polytope;
- quadratic diffusion readout `D2(X)` = one-step/leading covariance tensor;
- quartic refinement `D4(X)` = `(D2(X), fourth-cumulant tensor)`.

Define
\[
X\sim_{\mathcal O}Y\iff \mathcal O(X)=\mathcal O(Y).
\]

Then:

- `FCC !~_B HCP`, because R033 gives different stable polytopes (FCC 12 vertices, HCP 18);
- `FCC ~_D2 HCP`, because both have covariance `I/3`;
- `FCC !~_D4 HCP`, because the exact fourth moments above differ.

Thus “sphere/circle as coarse observational class” can be made precise:

> the quadratic diffusive class is rotationally isotropic at its retained resolution, even though its finite microscopic members and ballistic geometry are not continuously rotationally symmetric.

Disposition: H9 `CONFIRMED_AS_TYPED_EQUIVALENCE`.

## 10. H1–H10 disposition

| H | disposition | reason |
|---|---|---|
| H1 | `CONFIRMED_WITH_OPERATOR_SCOPE` | finite algebraic expression trees stay algebraic; analytic primitives would break it |
| H2 | `CONFIRMED_FINITE_NATIVE_SCALE` | locally finite continuous-orbit no-go |
| H3 | `CONFIRMED_EXACT` | exact FCC/HCP shell and bulk formulas |
| H4 | `CONFIRMED_STRONGLY` | bond, physical, hull, inradius, RMS and equal-volume channels disagree |
| H5 | `CONFIRMED` | finite path counts/probabilities and moments need no π |
| H6 | `CONFIRMED_WITH_REPRESENTATION_SCOPE` | π enters Gaussian density/Fourier/Lebesgue readout, not necessarily characteristic-function description |
| H7 | `KILLED` | discrete Basel lattice sum equals `pi^2/3` |
| H8 | `CONFIRMED` | L2 infinite completion is a separate constant-generation gateway |
| H9 | `CONFIRMED` | ballistic unequal; quadratic diffusion equal; quartic refinement unequal |
| H10 | `CONFIRMED` | pi_eff requires observable, radius, geometry and readout semantics |

## 11. Strongest theorem candidates

1. `FINITE_ALGEBRAIC_OBSERVABLE_CLOSURE_V1`.
2. `LOCALLY_FINITE_CONTINUOUS_ROTATION_ORBIT_NO_GO_V1`.
3. `FCC_HCP_GRAPH_RADIUS_PI_EFF_EXACT_FORMULAS_V1`.
4. `NO_UNIQUE_NATIVE_PI_WITHOUT_READOUT_SEMANTICS_V1`.
5. `INFINITE_DISCRETE_COMPLETION_TRANSCENDENCE_GATEWAY_V1`.
6. `OBSERVABLE_RELATIVE_SPHERICAL_EQUIVALENCE_V1`.

## 12. Minimal counterexamples

- To unrestricted finite algebraicity: allow the primitive `exp`; `exp(1)=e`.
- To H7: `sum_{m!=0} 1/m^2 = pi^2/3`.
- To unique `pi_eff`: on the same FCC graph ball, shell-count limit `5/2`, bond-count limit `9`, cuboctahedral geometric-area constant `(3+sqrt(3))/2`, physical-volume constant `5sqrt(2)/4`, and equal-volume Euclidean calibration returns π by definition.
- To “diffusive leading isotropy means exact microscopic rotational symmetry”: FCC/HCP have equal covariance but unequal fourth moments and unequal ballistic polytopes.

## 13. Prior-art roots

- J. H. Conway & N. J. A. Sloane, *Low-Dimensional Lattices VII: Coordination Sequences* (1997), as already rooted by R033.
- T. Fritz, *Velocity polytopes of periodic graphs and a no-go theorem for digital physics*, arXiv:1109.1963, as rooted by R033.
- G. M. Viswanathan, *Correspondence between spanning trees and the Ising model on a square lattice*, arXiv:1706.00799.
- S.-C. Chang & R. Shrock, *Some Exact Results for Spanning Trees on Lattices*, arXiv:cond-mat/0602574.
- Euler's Basel identity `zeta(2)=pi^2/6`, used here only as an exact L2 counterexample.

## 14. Final ontology verdict

`USER_HYPOTHESIS_PARTIALLY_KILLED_AND_REFINED`.

The strongest surviving statement is:

> In a fixed FCC/HCP/Barlow locally finite cellular model, no nontrivial finite native object is an exact Euclidean circle/sphere under full continuous rotation; finite algebraic observables do not spontaneously create classical π. Euclidean π can therefore legitimately be treated as a structural constant of selected continuum/readout semantics rather than a required finite microscopic state constant.

But the stronger statement must be rejected:

> “π/transcendentals exist only because we approximate a discrete world by a continuum.”

It fails because an exact pure-discrete infinite completion can already evaluate to a transcendental, with the Basel lattice sum providing the minimal witness.

The correct boundary is not **discrete vs continuum**. It is:

\[
\boxed{
\text{finite algebraic closure}
\quad\longrightarrow\quad
\text{infinite completion}
\quad\longrightarrow\quad
\text{continuum/readout}
}
\]

and both of the last two arrows can introduce exact constants that are absent from every finite microscopic stage.

## 15. Remaining frontier / next action

The main unresolved R038 frontier is not H7 anymore. It is to classify **which operator families** make L2 transcendental entry necessary/possible and whether any FCC/HCP-native infinite observable admits a provably transcendental exact value rather than merely a special-function expression of unknown arithmetic status. R037 should also be absorbed when its independent audit publishes.
