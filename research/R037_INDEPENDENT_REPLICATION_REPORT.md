# R037 Independent Algorithm/Data Replication Audit

Researcher-ID: `EM-R037-A7C2D1`

Task: `RS-R037-R033-R034-INDEPENDENT-ALGORITHM-DATA-REPLICATION-AUDIT`

Source base: `092c8ced3b3a5808d8669946a830db73b129a126`

Frozen audit targets:

- R033: `c2aa1758c6cf8f194d8b4493b90c903a2dfcd048`
- R034: `674fb8717d753cd36fd83b061c869d79e8875b31`

State: `HANDOFF_READY / SEMANTIC_CHECKPOINT / CI_NOT_REQUIRED_FOR_RESEARCH`

## 1. Audit discipline

R037 rebuilt FCC and HCP from the declared microscopic definitions. It did not import or execute R033/R034 research scripts as a derivation engine. The independent path used a new integer graph model, new BFS and closed distance oracles, new symmetry-mask canonicalization, new exact-rational Voronoi gluing, new integer path-count dynamic programming, new moment recurrences, and new Fourier/Bloch derivations. Frozen generated outputs were opened only after the corresponding independent result existed, and were then used as the diff target.

The local checkout could not reach GitHub because the execution environment failed DNS resolution. Under the repository's research hot-path policy this was treated as a soft transport limitation, not a mathematical hard block; source reads and checkpoint publication therefore used the GitHub connector while all calculations were independently rerun in the local Python environment.

## 2. R033 graph and growth replication

### FCC

The independent model is the even-parity `D3` lattice with the twelve signed coordinate permutations of `(1,1,0)`. The exact word distance is

`d(x,y,z)=max(max(|x|,|y|,|z|), (|x|+|y|+|z|)/2)`.

Independent BFS through radius 20 produced zero distance-oracle mismatches. The shell and bulk laws are

- `A_0=1`, `A_r=10 r^2+2` for `r>=1`;
- `V_r=(10 r^3+15 r^2+11 r+3)/3`;
- shell-induced edges `24 r^2`.

The radius-100 closed-form holdout is `A_100=100002`, `V_100=3383701`.

### HCP

The independent model uses integer triangular-layer coordinates `(m,n,l)`, AB layer parity, six in-layer neighbors, and three neighbors in each adjacent layer. An explicit A/B graph automorphism is

`(m,n,l) -> (-m,-n,1-l)`.

Let `T(m,n)=max(|m|,|n|,|m+n|)`, `L=|l|`, and `q=floor(L/2)`. An independently derived distance oracle is

- if `L` is even, `rem=T(m,n)`;
- if `L` is odd, `rem=min_s T((m,n)-s)` for `s in {(0,0),(-1,0),(0,-1)}`;
- `d=L+max(0,rem-q)`.

It agrees with BFS at every enumerated vertex through radius 20. The exact growth laws are

- `A_0=1`, `A_r=floor(21 r^2/2)+2` for `r>=1`;
- even `r`: `V_r=(14r^3+21r^2+14r+4)/4`;
- odd `r`: `V_r=(14r^3+21r^2+14r+3)/4`;
- shell-induced edges `27r^2` for even `r`, `27r^2-3` for odd `r`.

The radius-100 holdout is `A_100=105002`, `V_100=3552851`.

The leading shell and bulk coefficient ratio is exactly `21/20`.

## 3. First irreducible FCC/HCP differences

The rooted radius-one induced balls already differ although both contain 13 vertices and the shell contains 12 vertices. A clean independently generated witness is the number of 4-cycles in the nearest-neighbor shell:

- FCC: 6;
- HCP: 9.

Thus the first rooted graph difference is at `r=1`. Shell cardinality first differs at `r=2`: FCC has 42, HCP has 44.

## 4. Boundary spectra and exposed faces

Independent directional masks were quotiented by independently constructed local symmetry groups: the 48 signed coordinate permutations for FCC and the 12 automorphisms of the exact HCP local Gram star. The resulting stable orbit populations agree with the frozen formulas after label relabeling.

For FCC the four stable populations are

- outside degree 7: `12`;
- outside degree 5: `24(r-1)`;
- outside degree 4: `6(r-1)^2`;
- outside degree 3: `4(r-1)(r-2)`.

For HCP ten stable populations are recovered with the same parity quasi-polynomials recorded in `R037_R033_REPLICATION_ATLAS.json`.

In both worlds the independently weighted outside-degree populations give the same exposed-face count

`F_r = 12(3r^2+3r+1)`.

Directional exposure also reproduces the frozen exact proportions: FCC has six unoriented classes, each `1/6`; HCP has three basal unoriented classes, each `1/6`, and six interlayer unoriented classes, each `1/12`.

## 5. Exact-rational topology audit

R037 rebuilt local Voronoi cells from the twelve bisector halfspaces using rational arithmetic in an encoded physical coordinate system. Boundary faces were glued with global rational vertex keys. For every `r=0..20`, in both FCC and HCP, the result is

- `F=12(3r^2+3r+1)`;
- `E=2F`;
- `V=F+2`;
- `chi=2`;
- one connected component;
- exactly two incident faces at every boundary edge;
- one cycle in every vertex link.

Therefore every certified boundary in the finite reference range is a closed connected 2-manifold with Euler characteristic 2 and hence topological `S^2`.

R037 does **not** promote this to an all-radius theorem. The all-`r` shelling/induction remains `THEOREM_CANDIDATE_ONLY` unless separately proved.

## 6. Limit-shape audit

The FCC distance inequalities directly give the cuboctahedral stable norm ball, with 12 vertices, 14 facets, NN-normalized circumradius 1, inradius `1/sqrt(2)`, anisotropy ratio `sqrt(2)`, and zero finite-radius support remainder after scaling the convex hull.

For HCP, the periodic quotient cycle-velocity construction gives six basal one-step vertices and twelve upper/lower two-step mean-velocity vertices, hence an 18-vertex, 14-facet polytope. Its circumradius is 1, inradius `sqrt(24/41)`, and anisotropy ratio `sqrt(41/24)`.

Using the encoded coordinates `u=m+p/3`, `v=n+p/3`, `p=l mod 2`, the finite HCP ball satisfies the limit-facet inequalities with at most `1/6` unscaled overshoot. Thus the normalized support remainder is at most `1/(6r)`; for even radius all 18 limit vertices are exactly reachable.

## 7. Macro shape functional and readout audit

For `K_r=A_r^3/V_r^2`, R037 independently obtains

- FCC: `K_r -> 90`, with `K_r=90-270/r+927/(2r^2)-540/r^3+O(r^-4)`;
- HCP: `K_r -> 189/2`, with leading correction `-567/(2r)` in both parity classes.

The exact rational forms imply the frozen bounds `|K_F-90|<270/r` and `|K_H-189/2|<567/(2r)` for positive integer radius. At `10^36`, `10^37`, and `10^38` the correction is therefore already macroscopically negligible under this observable.

If the discrete leading shell/bulk laws are **post hoc** written in Euclidean forms `A~4*pi_eff*r^2` and `V~(4/3)*pi_eff*r^3`, the native graph-radius calibration gives `pi_eff=5/2` for FCC and `21/8` for HCP. These are readout constants, not microscopic inputs and not claims about classical pi. Under `R=alpha r`, the area and volume readouts scale differently (`alpha^-2` versus `alpha^-3`), making the calibration dependence explicit.

## 8. R034 local propagation audit

Using NN physical length 1, direct exact vector sums give, for FCC and for both HCP local classes,

`E[Delta X]=0`, `E[Delta X Delta X^T]=I/3`.

The same result holds for every legal Barlow local environment: the six basal vectors contribute `diag(3,3,0)` to the unnormalized outer-product sum; each interlayer triangle contributes `(1/2)I_2` in-plane and z-square sum 2; above plus below contributes `diag(1,1,4)`; all twelve vectors therefore sum to `4I_3` and have zero total drift.

Consequently the walk is a martingale with deterministic predictable quadratic variation, and

`E[X_n X_n^T]=n I/3`, `E|X_n|^2=n`

exactly.

## 9. Higher-order memory and finite path counts

Independent integer path-count dynamic programming through `n=12` reproduces the first distribution witness at `n=2`:

- FCC support 55, count histogram `{1:12,2:24,4:18,12:1}`;
- HCP support 57, count histogram `{1:18,2:18,3:2,4:18,12:1}`.

Return counts nevertheless agree through all sampled times `n=0..12`.

The rooted local cubic contraction is zero for FCC, while HCP gives

`sqrt(3)*y*(3x^2-y^2)/72`

on A and the negative on B. Thus the first rooted physical tensor memory is order 3. The fourth tensors also differ, but the scalar fourth radial moment remains universal:

`E|X_n|^4=(5n^2-2n)/3`.

The scalar sixth moments are

- FCC: `n(35n^2-42n+16)/9`;
- HCP: `(210n^3-252n^2+95n+1)/54`, `n>=1`;
- difference: `-(n-1)/54`.

R037 also supplies an exact recurrence explanation rather than an interpolation: for the signed HCP cubic harmonic `f_s`, the transition operator sends `f_s` to the constant `-1/432`; the sixth-radial recursion therefore receives an extra `8(-1/432)=-1/54` per step after the first.

The first same-Euclidean-radius path-count nonuniformity appears at HCP `n=4`, `r^2=35/3`, with counts 6 and 8; FCC first shows such a witness at `n=5`, `r^2=9`, with counts 370 and 405.

## 10. Spectral audit

The independently derived FCC symbol is

`lambda_F=(cos(x/sqrt(2))cos(y/sqrt(2))+cos(x/sqrt(2))cos(z/sqrt(2))+cos(y/sqrt(2))cos(z/sqrt(2)))/3`.

Its principal log expansion begins with `-|k|^2/6`.

For HCP, with

- `C=cos(x)+2cos(x/2)cos(sqrt(3)y/2)`,
- `S=2cos(x/2)exp(i sqrt(3)y/6)+exp(-i sqrt(3)y/3)`,
- `h=sqrt(2/3)`,

the AB Bloch matrix is

`[[C/6, cos(hz)S/6], [cos(hz)conj(S)/6, C/6]]`.

The principal log band also begins with `-|k|^2/6`; hence leading diffusive geometry is isotropic and FCC/HCP-universal at quadratic order.

After physically aligning FCC `[111]` with the HCP stacking axis and a FCC close-packed direction with HCP x, the quartic log difference is exactly

`log4_FCC-log4_HCP = -sqrt(2) y z (3x^2-y^2)/432`.

Thus principal spectral stacking memory first appears at order 4. Under `k=xi/sqrt(n)`, this term contributes `O(1/n)` to `n log lambda`, so the `10^36` statement is an extremely small **small-k diffusive correction**. R037 explicitly does not upgrade this to a global pointwise heat-kernel theorem.

## 11. New upgrade: exact Barlow return/local-spectral universality

R034 froze a gauge argument as a theorem candidate. R037 closes the missing algebraic step under the stated bi-infinite Barlow hypotheses.

After basal Fourier transform the layer coordinate is a chain `j in Z`. The fiber has diagonal term `C(k)/6` and interlayer hopping

`t_j(k)=S_{sigma_j}(k)/12`,

where stacking only chooses the orientation `sigma_j`. The two orientations have the same modulus because their structure factors are conjugate up to convention, and

`|S_sigma(k)|^2=3+2C(k)`.

Therefore every layer edge has the same hopping modulus. Since the layer graph is `Z`, it has no cycle flux. Fix `u_0=1` and recursively choose unit phases so that

`conj(u_j) t_j u_{j+1}=|t_j|`.

At a zero hopping the phase is irrelevant. The resulting diagonal unitary fixes the root vector and transforms every legal stacking fiber into the same real constant-magnitude Jacobi fiber. A measurable phase selection gives the direct-integral unitary.

Hence, exactly:

1. every legal bi-infinite Barlow stacking has the same root return probability for every `n`;
2. every such stacking has the same root local spectral measure;
3. the infinite operators have the same spectrum under this direct-integral unitary.

For periodic stacks, the integrated spectrum/IDS is therefore also identical. For arbitrary nonperiodic stacks, R037 states IDS equality conditional on a standard trace-per-volume/IDS limit existing; existence itself is kept separate. The gauge is wavevector-dependent and is not a physical-coordinate vertex permutation, so it does **not** remove cubic/quartic physical angular memory or imply pointwise heat-kernel equality.

This is the one substantive R037 upgrade over the frozen evidence grades.

## 12. Disposition

No theorem-critical frozen R033/R034 numerical or algebraic claim audited here produced a mismatch. Representation differences were found only where independent coordinate conventions or orbit labels differed, and all resolved after explicit equivalence/alignment.

The strict non-upgrades are intentional:

- all-radius exposed-face `S^2`: still theorem candidate;
- arbitrary nonperiodic IDS existence: separate theorem candidate;
- arbitrary nonperiodic pointwise heat-kernel/local-CLT universality: open/theorem candidate.

The evidence matrix and mismatch report are machine-readable in `research/r037_generated/`.

## 13. Checkpoint files

- `research/r037_independent_replication.py`
- `tests/test_r037_independent_replication.py`
- `research/r037_generated/R037_R033_REPLICATION_ATLAS.json`
- `research/r037_generated/R037_R034_REPLICATION_ATLAS.json`
- `research/r037_generated/R037_SPECTRAL_MOMENT_CERTIFICATE.json`
- `research/r037_generated/R037_MACRO_READOUT_AUDIT.json`
- `research/r037_generated/R037_EVIDENCE_MATRIX.json`
- `research/r037_generated/R037_MISMATCH_REPORT.json`
- `research/R037_INDEPENDENT_REPLICATION_REPORT.md`

No CI query is made at this research checkpoint, per task policy.
