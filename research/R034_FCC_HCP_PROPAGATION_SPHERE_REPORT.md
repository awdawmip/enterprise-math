# R034 FCC/HCP Propagation-Sphere Semantics

Status: `RESEARCH CHECKPOINT / NOT CANONICAL`  
Researcher-ID: `EM-R034-422B8C`  
Task: `RS-R034-FCC-HCP-PROPAGATION-SPHERE-SEMANTICS`  
Taskbook source: `9fa57d7ac25659ca947bb9d3c9d1a1e33a41da3a`  
Frozen R033 input: owner head `c2aa1758c6cf8f194d8b4493b90c903a2dfcd048`  
CI: `CI_NOT_REQUIRED_FOR_RESEARCH`

## Executive result

R034 separates two intrinsic propagation geometries on the same close-packed cell worlds.

R033's nearest-neighbor shortest-path radius produces stable anisotropic polyhedral balls: the FCC cuboctahedral norm ball and the distinct HCP 18-vertex velocity polytope. R034 finds that the uniform 12-neighbor random walk on the same exact embedded graphs instead has the exact local covariance

\[
\boxed{\Sigma_F=\Sigma_{H,A}=\Sigma_{H,B}=\frac13 I}
\]

when physical nearest-neighbor length is normalized to one. Hence, for every time `n`,

\[
\boxed{E[X_n]=0,\qquad E[X_nX_n^T]=\frac n3 I,\qquad E|X_n|^2=n.}
\]

The common quadratic form is not a fit to a continuum sphere; it is derived from the twelve discrete step vectors. Under diffusive scaling `X_n/sqrt(n)`, FCC and HCP have the same leading Gaussian/Brownian covariance `I/3`. Thus the same microscopic world naturally carries both a polyhedral ballistic sphere and a Euclidean-leading diffusive sphere.

The leading diffusive universality does not erase stacking information. The first stacking-sensitive order depends on the observable:

- rooted local physical one-step tensor: order 3;
- A/B-averaged or principal low-frequency band: order 4;
- scalar radial even moments: order 6;
- full finite-time propagation distribution: physically distinguishable at `n=1`; even as unlabeled path-count multisets, distinguishable at `n=2`;
- return probability/root local spectral measure: a Barlow layer-gauge argument removes stacking for all times for the nearest-neighbor model.

Supported return classes:

`DIFFUSIVE_ISOTROPY_FOUND`  
`FCC_HCP_SECOND_MOMENT_UNIVERSALITY_FOUND`  
`FCC_HCP_DIFFUSIVE_LEADING_UNIVERSALITY_FOUND`  
`BALLISTIC_DIFFUSIVE_GEOMETRY_SPLIT_FOUND`  
`HIGHER_ORDER_STACKING_MEMORY_FOUND`  
`FIRST_MEMORY_ORDER_CLASSIFIED`  
`HEAT_BALL_EUCLIDEAN_LIMIT_FOUND` for periodic FCC/HCP  
`BARLOW_SECOND_MOMENT_UNIVERSALITY_FOUND`  
`BARLOW_DIFFUSION_UNIVERSALITY_FOUND` at the leading functional-CLT level  
`PROPAGATION_RELATIVE_SPHERE_PRINCIPLE_FOUND`  
`OBSERVABLE_MEMORY_HIERARCHY_FOUND`  
`NO_PI_INPUT_BUT_CONTINUUM_ISOTROPY_EMERGES`.

## 1. Frozen microscopic input

No R033 graph-ball law was re-opened. R034 consumes only the frozen microscopic graphs and exact embeddings.

### FCC

The graph is `D3` with twelve generators given by signed permutations of `(1,1,0)`. To normalize the physical nearest-neighbor length to one, use physical vectors

\[
\frac1{\sqrt2}(\pm1,\pm1,0)
\]

and coordinate permutations.

### HCP

The graph uses states `(i,j,k)`, even `k` for A layers and odd `k` for B layers. The exact coefficient embedding uses the layer shift `(1/3,1/3)` on odd layers and physical Gram matrix

\[
G_H=\begin{pmatrix}
1&1/2&0\\
1/2&1&0\\
0&0&2/3
\end{pmatrix}.
\]

In an orthonormal stacking frame, the six basal neighbors form a regular unit hexagon. The three neighbors in each adjacent layer have planar projections forming an equilateral triangle of radius `1/sqrt(3)` and vertical component `sqrt(2/3)`. The B-layer planar triangle is the negative of the A-layer triangle.

## 2. Exact local covariance audit

For FCC, opposite step pairs make the mean zero. Direct outer-product summation gives

\[
\sum_{v\in N_F} vv^T=4I,
\]

so

\[
\frac1{12}\sum_v vv^T=\frac13 I.
\]

For HCP, the six same-layer vectors satisfy

\[
\sum_{v\in N_{same}}vv^T=\operatorname{diag}(3,3,0).
\]

For either interlayer triangle, the planar outer-product sum is `(1/2)I_2`; combining the three above and three below gives

\[
\sum_{v\in N_{inter}}vv^T=\operatorname{diag}(1,1,4).
\]

Hence the total is again `4I`, independently of whether the current layer is A or B. The interlayer first moments cancel above/below, and the six basal vectors sum to zero. Therefore

\[
\boxed{E[\Delta X\mid X_t]=0,\qquad E[\Delta X\Delta X^T\mid X_t]=I/3}
\]

at every FCC and ideal-HCP cell.

This verifies H1 and H2 exactly.

## 3. Exact all-time second moments

Let `Delta_t=X_t-X_{t-1}`. Since `E[Delta_t|F_{t-1}]=0`, cross terms vanish:

\[
E[\Delta_s\Delta_t^T]=0\qquad(s\ne t).
\]

The conditional second moment is deterministically `I/3`, so

\[
E[X_nX_n^T]
=\sum_{t=1}^nE[\Delta_t\Delta_t^T]
=\frac n3I.
\]

This is exact, not merely asymptotic. FCC and HCP therefore recoalesce completely at the rank-2 covariance observable for every `n`.

The conclusion is deliberately limited: second-moment isotropy is not finite-time spherical symmetry.

## 4. First higher-order stacking memory

### 4.1 Rooted local order 3

For a test vector `(x,y,z)`, define

\[
M_m(x,y,z)=E[(x\Delta X_1+y\Delta X_2+z\Delta X_3)^m].
\]

FCC is centrally symmetric, hence all odd one-step moments vanish. For HCP-A the cubic contraction is

\[
\boxed{M_3^{H,A}=\frac{\sqrt3}{72}\,y(3x^2-y^2),}
\]

and HCP-B has the opposite sign. Therefore the first rooted local physical memory order is

\[
\boxed{m_*^{local}=3.}
\]

The A/B sign reversal explains why the principal two-layer Bloch band does not show an odd-power correction.

### 4.2 Fourth-order global tensor

FCC:

\[
E[X^4]=\frac{n(2n-1)}6,
\qquad
E[X^2Y^2]=\frac{n(4n-1)}{36},
\]

with cubic permutations.

HCP in the stacking frame:

\[
E[X^4]=E[Y^4]=\frac{n(8n-3)}{24},
\]
\[
E[Z^4]=\frac{n(3n-1)}9,
\]
\[
E[X^2Y^2]=\frac{n(8n-3)}{72},
\]
\[
E[X^2Z^2]=E[Y^2Z^2]=\frac{n(2n-1)}{18}.
\]

The leading `O(n^2)` Gaussian part agrees, while the `O(n)` correction differs. Thus standardized fourth-order anisotropy is `O(1/n)`.

### 4.3 Radial recoalescence through order 4; first radial memory at order 6

Despite the different fourth tensor,

\[
\boxed{E|X_n|^4=\frac{5n^2-2n}{3}}
\]

for both FCC and HCP. In fact this follows from unit step length plus zero drift and conditional covariance `I/3`, so it is not an FCC/HCP accident.

At sixth radial order the worlds separate:

\[
E_F|X_n|^6=\frac{n(35n^2-42n+16)}9,
\]

and, for `n>=1`,

\[
E_H|X_n|^6=\frac{210n^3-252n^2+95n+1}{54}.
\]

Therefore

\[
\boxed{E_H|X_n|^6-E_F|X_n|^6=-\frac{n-1}{54}.}
\]

The first scalar radial even-moment stacking memory is order 6.

A complementary HCP cubic harmonic persists globally. From an A origin,

\[
H(X,Y,Z)=Y(3X^2-Y^2),
\qquad
E[H(X_n)]=\frac{\sqrt3}{18}\quad(n\ge1),
\]

whereas FCC gives zero.

## 5. Exact finite-time path-count atlas

The executable oracle propagates integer counts `c_n(x)` and only divides by `12^n` when a probability is required. Full state/count/radius distributions are stored for `n=0,1,2`, compact summaries through `n=12`, angular-orbit summaries through `n=4`, and heat-threshold samples at `n=4,8,12`.

Support sizes begin

| n | FCC | HCP | common return count |
|---:|---:|---:|---:|
| 1 | 12 | 12 | 0 |
| 2 | 55 | 57 | 12 |
| 3 | 147 | 153 | 48 |
| 4 | 309 | 323 | 540 |
| 5 | 561 | 587 | 4320 |
| 6 | 923 | 967 | 42240 |
| 8 | 2057 | 2157 | 4038300 |
| 12 | 6525 | 6847 | 46982827584 |

At `n=2`, the path-count multisets already differ:

\[
FCC:\ \{1:12,2:24,4:18,12:1\},
\]

\[
HCP:\ \{1:18,2:18,3:2,4:18,12:1\}.
\]

Thus the first unlabeled path-count distribution witness is

\[
\boxed{n_*=2.}
\]

The physical one-step distributions are already distinguishable at `n=1` by the cubic tensor.

The `n=2` radial path-count distributions also differ. FCC has masses at squared radii `0,1,2,3,4`; HCP additionally has `8/3` and `11/3` and different counts at `3,4`.

Finite-time probability is not a function of Euclidean radius alone. A same-radius nonuniformity witness appears in HCP at `n=4`, `r^2=35/3`, with counts 6 and 8, and in FCC at `n=5`, `r^2=9`, with counts 370 and 405.

## 6. FCC Fourier and HCP Bloch expansion

### 6.1 FCC

With nearest-neighbor length one,

\[
\lambda_F(k)=\frac13\left[
\cos\frac{x}{\sqrt2}\cos\frac{y}{\sqrt2}
+\cos\frac{x}{\sqrt2}\cos\frac{z}{\sqrt2}
+\cos\frac{y}{\sqrt2}\cos\frac{z}{\sqrt2}
\right].
\]

Near zero,

\[
\log\lambda_F(k)
=-\frac{|k|^2}{6}
-\frac{x^4+x^2y^2+x^2z^2+y^4+y^2z^2+z^4}{144}
+O(|k|^6).
\]

### 6.2 HCP

Define

\[
C=\cos x+2\cos(x/2)\cos(\sqrt3 y/2),
\]

\[
S=2\cos(x/2)e^{i\sqrt3 y/6}+e^{-i\sqrt3 y/3},
\qquad h=\sqrt{2/3}.
\]

The two-orbit transition fiber is

\[
P_H(k)=\frac16
\begin{pmatrix}
C&\cos(hz)S\\
\cos(hz)\overline S&C
\end{pmatrix}.
\]

Near zero the bands are

\[
\lambda_\pm=C/6\pm\cos(hz)\sqrt{3+2C}/6.
\]

The principal band satisfies

\[
\log\lambda_+(k)
=-\frac{|k|^2}{6}
-\frac{9x^4+18x^2y^2+24x^2z^2+9y^4+24y^2z^2+8z^4}{1728}
+O(|k|^6).
\]

The optical band has `lambda_-(0)=0`, so it does not control the long-time leading diffusion.

Therefore FCC and HCP have exactly the same quadratic low-frequency form but different quartic corrections:

\[
\boxed{a_2^F=a_2^H=-|k|^2/6,\qquad a_4^F\ne a_4^H.}
\]

In a common stacking-aligned frame, the quartic log-band difference factors as

\[
\boxed{L_4^F-L_4^H=-\frac{\sqrt2}{432}\,yz(3x^2-y^2).}
\]

Hence the first principal/even spectral stacking-memory order is

\[
\boxed{m_*^{spectral}=4.}
\]

For `k=q/sqrt(n)`,

\[
n\log\lambda(q/\sqrt n)=-\frac{|q|^2}{6}+\frac{L_4(q)}n+O(n^{-2}).
\]

The sampled unit-direction quartic spread is

\[
A_n^{FCC}=\frac{q^4}{432n}+O(n^{-2}),
\qquad
A_n^{HCP}=\frac{q^4}{756n}+O(n^{-2}).
\]

This gives an explicit `1/n` anisotropy-decay scale for the principal diffusive spectral correction.

## 7. Diffusive limit and heat balls

The bounded increments, zero conditional drift, and deterministic quadratic variation

\[
\langle X\rangle_n=\frac n3I
\]

put FCC and HCP in the standard martingale/periodic-crystal invariance-principle regime. Thus

\[
\boxed{X_n/\sqrt n\Longrightarrow N(0,I/3).}
\]

The leading continuum density is

\[
\left(\frac3{2\pi}\right)^{3/2}\exp\left(-\frac32|x|^2\right).
\]

`pi` is absent from the microscopic transition rule and first appears only when the limiting Gaussian is normalized/Fourier-inverted.

For an exact finite-time heat-threshold set

\[
H_{n,\theta}=\{x:c_n(x)\ge\theta c_n(0)\},
\]

the atlas shows finite-time nonradial interfaces. For example at `theta=1/10`, `n=12`, the FCC maximum included squared radius is 19 and the minimum excluded is 20; HCP gives 19 and `59/3`. These finite sets are not exact Euclidean balls. The common quadratic principal exponent and `O(1/n)` quartic term imply that periodic FCC/HCP heat-kernel level sets, after `sqrt(n)` rescaling, have a Euclidean leading limit with stacking-dependent subleading angular correction.

## 8. Barlow extension

The local covariance calculation does not use ABAB periodicity. Every legal ideal Barlow cell has six basal neighbors plus one three-neighbor triangle above and one below. The same outer-product certificate gives

\[
\boxed{E[\Delta X\mid\mathcal F_t]=0,\qquad
E[\Delta X\Delta X^T\mid\mathcal F_t]=I/3}
\]

for any legal stacking word.

Consequently any deterministic periodic or nonperiodic ideal Barlow stacking under the uniform 12-neighbor rule is a bounded-increment martingale with deterministic predictable quadratic variation `nI/3`. A standard multidimensional martingale functional CLT therefore gives the same leading Brownian covariance `I/3`.

This establishes leading Barlow diffusion universality under the declared geometry/dynamics hypotheses. It does **not** automatically establish a pointwise local central limit theorem or a full heat-kernel asymptotic for arbitrary nonperiodic stackings. That is retained as an open boundary.

Higher memory survives locally. An ABA turnback environment carries the nonzero cubic tensor; an ABC continuation cancels the cubic term but retains a quartic chirality-sensitive correction.

## 9. Return probability and the Barlow layer gauge

Exploratory exact enumeration found identical FCC/HCP origin return counts through `n=40`. A stronger structural route removes the need to regard that finite range as evidence for a late difference.

After Fourier transform in the basal plane, every close-packed nearest-neighbor stacking becomes a one-dimensional layer chain. The diagonal same-layer term is stacking-independent. The adjacent-layer three-hop amplitude has a stacking-dependent complex phase but a common magnitude. Since the layer graph is a bi-infinite line, a diagonal phase gauge can be chosen recursively to remove every hopping phase.

The resulting fiber is a stacking-independent constant-magnitude Jacobi operator. Choosing root gauge phase one preserves the root diagonal matrix element, yielding the theorem candidate:

> For the ideal uniform nearest-neighbor Barlow transition operator, the root local spectral measure and all return probabilities `P^n(o,o)` are stacking-independent; the integrated adjacency/transition density of states is likewise stacking-independent.

This does not imply physical-coordinate graph isomorphism or equality of wavevector-labelled dispersion. The gauge depends on basal momentum and changes the phase/momentum identification. Thus return probability can forget stacking exactly while angular finite-time propagation and physical Bloch dispersion retain it.

## 10. Observable memory hierarchy

R034 therefore obtains the following hierarchy.

| Observable | FCC/HCP relation | First memory |
|---|---|---|
| local rooted physical step tensor | different | order 3 |
| full physical one-step distribution | different | `n=1` |
| unlabeled finite path-count multiset | different | `n=2` |
| one-step covariance | exactly same `I/3` | forgotten |
| all-time covariance | exactly same `nI/3` | forgotten |
| fourth tensor | different in subleading terms | order 4 |
| scalar `E r^4` | exactly same | forgotten through 4 |
| scalar `E r^6` | different | order 6 |
| principal low-frequency band | same quadratic, different quartic | order 4 |
| leading CLT/heat quadratic geometry | same isotropic Gaussian | forgotten at leading order |
| return probability/local DOS | same by layer gauge | forgotten exactly in NN Barlow model |
| R033 word-metric ball | different at leading order | retained permanently |

There is no need to choose between `leading universality` and `subleading memory`: both are simultaneously true for different observable resolutions.

## 11. Propagation-relative sphere principle

The task's central principle can now be stated mathematically.

Given an embedded graph `G`, a propagation semantics `S` defines its own radial object. For the same FCC/HCP microscopic graphs:

- shortest-path semantics uses the stable word norm and produces R033's anisotropic polyhedral balls;
- uniform random-walk/heat semantics uses the Hessian of the principal transition band at `k=0`, equivalently the covariance tensor, and produces the quadratic form `3|x|^2` at leading diffusive scale.

Thus

\[
\boxed{\text{cell world}+\text{propagation law}\longrightarrow\text{macroscopic geometry}}
\]

is not merely philosophical. The two macroscopic unit objects are limits in different scalings and of different observables on the same microscopic adjacency.

R033's polyhedral sphere is therefore the shortest-path/ballistic propagation sphere, not a propagation-independent proof that every intrinsic large-scale propagation geometry of the cell world must be polyhedral.

Conversely, the Euclidean diffusive sphere is not a microscopic constituent. It emerges from repeated discrete propagation because the exact local quadratic variation is scalar.

## 12. H1-H12 dispositions

- H1 `PASS`: exact local zero drift.
- H2 `PASS`: exact common covariance `I/3`.
- H3 `PASS`: exact `E[X_nX_n^T]=nI/3` for all `n`.
- H4 `PASS`: common isotropic leading Gaussian/Brownian geometry.
- H5 `PASS_REFINED`: memory local-3 / principal-even-4 / radial-6 / return-none for NN Barlow.
- H6 `PASS`: ballistic and diffusive sphere non-equivalence.
- H7 `DIRECT_LINK_KILLED`: the R033 exposed-face scalar equality and the R034 covariance equality are both coarse memory-loss observables, but no derivation of one from the other was found.
- H8 `PASS`: arbitrary legal Barlow local second-moment universality.
- H9 `PASS_LEADING_OPEN_LOCAL`: arbitrary Barlow leading martingale FCLT; nonperiodic pointwise heat-kernel/local-CLT remains open.
- H10 `PASS`: no microscopic `pi`; it appears only at continuum Gaussian normalization/inversion.
- H11 `PASS_ASYMPTOTIC`: explicit quartic `O(1/n)` spectral anisotropy.
- H12 `PASS_ASYMPTOTIC_CERTIFICATE`: for fixed `q=1`, quartic direction spread at `n=10^36` is approximately `2.31e-39` for FCC and `1.32e-39` for HCP; sixth spectral scale is `O(10^-72)`. This is an asymptotic small-`k` certificate, not a claimed global uniform remainder theorem.

## 13. Minimal counterexamples and boundaries

1. `second moment isotropic => full distribution spherical` is killed already at `n=1` physically and `n=2` by unlabeled path counts.
2. `FCC/HCP same diffusion tensor => same higher propagation statistics` is killed by the local cubic tensor and quartic Bloch term.
3. `radial fourth moment detects all stacking memory` is killed: `E r^4` is exactly universal, while `E r^6` separates.
4. `return probability distinguishes close-packed stacking` is killed for the ideal NN Barlow model by the layer gauge.
5. `leading Brownian universality => arbitrary nonperiodic pointwise heat-kernel universality` is not proved; it remains an explicit open boundary.
6. Unequal transition weights, nonideal geometry, longer-range hops, or other propagation laws need not preserve the covariance/gauge results and should be treated as new semantics rather than silently absorbed here.

## 14. Prior-art rooting boundary

The task derived its exact local tensors, path counts, and spectral expansions before rooting them externally.

Relevant established roots include:

- periodic crystal-graph random-walk transition asymptotics and twisted-operator perturbation: Kotani, Shirai, Sunada, *Asymptotic Behavior of the Transition Probability of a Random Walk on an Infinite Graph*, J. Funct. Anal. (1998);
- functional CLT and higher asymptotics for random walks on crystal lattices: Ishiwata, Kawabi, Kotani, *Long time asymptotics of non-symmetric random walks on crystal lattices*, J. Funct. Anal. 272 (2017), arXiv:1510.05102;
- HCP/FCC origin-return generating-function relations: Ishioka and Koiwa, *Random walks on diamond and hexagonal close packed lattices*, Philosophical Magazine A (1978);
- equality of close-packed nearest-neighbor density of states despite different dispersion: *Identity of the density of states of simple excitations in close-packed lattices*, J. Phys. Chem. Solids (1972), DOI `10.1016/S0022-3697(72)80448-7`;
- a modern hidden-gauge/one-dimensional-chain formulation for close-packed stacking phases: Wilson, Ganesh, Samokhin, *Transport in close-packed solids with stacking defects*, arXiv:2602.18574 (2026).

Accordingly, no novelty claim is made for the general CLT machinery, periodic-graph spectral perturbation, FCC/HCP return/DOS equality, or the existence of a close-packed phase gauge. Enterprise-specific value here is the exact propagation-semantics comparison, observable memory hierarchy, executable certificates, and task-specific theorem/counterexample packaging.

## 15. Strongest theorem candidates

### Theorem candidate A — exact close-packed covariance universality

For the ideal unit-NN uniform walk on any legal Barlow stacking, at every cell the conditional increment mean is zero and the conditional second-moment tensor is `I/3`. Hence `E[X_nX_n^T]=nI/3` exactly.

### Theorem candidate B — Barlow leading martingale invariance principle

Under any deterministic legal Barlow stacking, the rescaled position process has leading Brownian covariance `I/3`, by bounded martingale differences with deterministic quadratic variation.

### Theorem candidate C — FCC/HCP memory-order hierarchy

For the exact task embeddings and uniform NN propagation: rooted local stacking memory first appears at tensor order 3; the principal/even low-frequency band first differs at order 4; the scalar radial hierarchy first differs at order 6.

### Theorem candidate D — NN Barlow return gauge universality

The basal-Fourier fibers of all ideal Barlow NN transition operators are related by a diagonal layer gauge to the same constant-magnitude Jacobi family. Therefore root return probabilities and local spectral measures are stacking-independent.

### Theorem candidate E — propagation-relative sphere split

The same embedded FCC/HCP nearest-neighbor graph supports a word-metric stable polytope under ballistic reachability and a common isotropic quadratic leading level-set geometry under uniform diffusion. The two are distinct intrinsic limits generated by different propagation semantics.

## 16. Foundation / Lean / physical-model recommendation

Foundation/Lean priority should be narrow and theorem-driven:

1. formalize the finite-dimensional outer-product identities giving zero drift and `I/3` conditional covariance for the generic Barlow local environment;
2. formalize the elementary exact second-moment martingale recurrence;
3. retain CLT/FCLT as rooted external probability theory unless Enterprise Math needs a dedicated probability foundation;
4. formalize the finite algebraic FCC/HCP third/fourth/sixth moment identities if the observable hierarchy becomes a shared theorem surface;
5. formalize the layer-phase gauge at the operator/algebra level only after its exact hypotheses are stabilized.

For physical-model continuation, the highest-value next semantics are weighted NN transport, next-nearest-layer hopping, continuous-time heat flow, persistent/ballistic random walks, classical waves, and unitary/quantum walks. Those perturbations directly test which current universalities depend on the special uniform NN balance and which survive a richer future language.

## 17. Validation and artifacts

Focused exact tests: `7 PASS`.

The experiment engine uses integer path counts, `Fraction`, and exact `Q(sqrt(2),sqrt(3))` arithmetic for theorem-critical local moments. Generated artifacts:

- `experiments/r034_fcc_hcp_propagation_sphere.py`
- `tests/test_r034_fcc_hcp_propagation_sphere.py`
- `research/r034_generated/R034_LOCAL_MOMENT_TENSORS.json`
- `research/r034_generated/R034_FINITE_N_PROPAGATION_ATLAS.json`
- `research/r034_generated/R034_SPECTRAL_EXPANSION.json`
- `research/r034_generated/R034_PROPAGATION_SEMANTICS_MATRIX.json`
- `research/r034_generated/R034_BARLOW_EXTENSION.json`
- `research/r034_generated/R034_HYPOTHESIS_DISPOSITIONS.json`

No R033 word-metric law was modified or re-proved beyond the frozen baseline interface required for the comparison.
