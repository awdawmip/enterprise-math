# R037 Independent Algorithm/Data Replication Audit

Researcher-ID: `EM-R037-A7C2D1`

Task: `RS-R037-R033-R034-INDEPENDENT-ALGORITHM-DATA-REPLICATION-AUDIT`

Source base: `092c8ced3b3a5808d8669946a830db73b129a126`

Frozen audit targets:

- R033: `c2aa1758c6cf8f194d8b4493b90c903a2dfcd048`
- R034: `674fb8717d753cd36fd83b061c869d79e8875b31`

State: `DONE / RETURNED / SEMANTIC_CHECKPOINT / CI_NOT_REQUIRED_FOR_RESEARCH`

## 1. Final verdict

R037 found **no theorem-critical mismatch** in the audited R033/R034 core after independently rebuilding the graph, distance, boundary, topology, propagation, moment, and spectral calculations.

The audit therefore finds no error that currently requires reversing the next research direction toward discrete exact worlds and continuum/readout semantics. The important boundary is semantic rather than numerical: the post-hoc constants `5/2` and `21/8` are calibration-dependent Euclidean-form readouts of the FCC/HCP graph-radius laws. They are not microscopic inputs and are not claims that classical `pi` equals either value.

R037 also upgrades one frozen R034 theorem candidate: under the stated bi-infinite legal Barlow-stacking hypotheses, nearest-neighbor **root return probabilities and root local spectral measures are exactly stacking-universal** by an explicit basal-Fourier layer-gauge proof. The periodic IDS consequence follows exactly. Arbitrary nonperiodic IDS existence and physical-coordinate pointwise heat-kernel universality remain separate open/theorem-candidate questions.

## 2. Independence and validation boundary

R037 did not use R033/R034 executable research scripts as a derivation engine. The independent path used:

- new FCC/HCP integer graph representations;
- a BFS reference path and separate closed/structural distance formulas;
- independent local symmetry-mask quotients;
- exact-rational Voronoi halfspace reconstruction and face gluing;
- integer path-count dynamic programming, with probability only as post-division;
- exact rational/algebraic moment recurrences;
- independent FCC Fourier and HCP Bloch derivations;
- direct rational/asymptotic macro evaluation from replicated closed forms.

Frozen generated outputs were opened only after the corresponding independent result existed, then used as diff targets.

The final local runner was executed with `full_topology=True`. It passed all FCC and HCP boundary-complex cases for every `r=0..20` (42 exact topology cases total), together with distance/BFS, growth, path-count, and radial-moment assertions. The local environment could not resolve GitHub DNS, so repository source reads/publication used the GitHub connector. This was a transport limitation, not a mathematical failure. Per research policy, CI was not queried.

## 3. R033 — exact graph/growth replication

### FCC

The independently rebuilt FCC world is the even-parity `D3` lattice with the twelve signed coordinate permutations of `(1,1,0)`. Its exact graph distance is

`d(x,y,z)=max(max(|x|,|y|,|z|), (|x|+|y|+|z|)/2)`.

Independent BFS through radius 20 has zero mismatches with this oracle. The replicated laws are

- `A_0=1`, `A_r=10r^2+2` for `r>=1`;
- `V_r=(10r^3+15r^2+11r+3)/3`;
- shell-induced edges `24r^2`.

The unused radius-100 holdout gives `A_100=100002`, `V_100=3383701`.

### HCP

The independent HCP model uses integer triangular-layer coordinates `(m,n,l)`, AB parity, six same-layer neighbors, and three neighbors in each adjacent layer. The map

`(m,n,l) -> (-m,-n,1-l)`

is an explicit A/B rooted graph equivalence.

With `T(m,n)=max(|m|,|n|,|m+n|)`, `L=|l|`, and `q=floor(L/2)`, an independently derived distance oracle is

- even `L`: `rem=T(m,n)`;
- odd `L`: `rem=min_s T((m,n)-s)` for `s in {(0,0),(-1,0),(0,-1)}`;
- `d=L+max(0,rem-q)`.

It has zero BFS mismatches through radius 20. The replicated growth laws are

- `A_0=1`, `A_r=floor(21r^2/2)+2` for `r>=1`;
- even `r`: `V_r=(14r^3+21r^2+14r+4)/4`;
- odd `r`: `V_r=(14r^3+21r^2+14r+3)/4`;
- shell-induced edges `27r^2` for even `r`, `27r^2-3` for odd `r`.

The radius-100 holdout gives `A_100=105002`, `V_100=3552851`.

The HCP/FCC leading shell and bulk coefficient ratio is exactly `21/20`.

## 4. First irreducible FCC/HCP differences

The rooted radius-one induced balls already differ although both have a 12-point nearest-neighbor shell. A new independent witness is the number of simple 4-cycles in that shell:

- FCC: `6`;
- HCP: `9`.

Thus the first rooted induced-graph difference is at `r=1`. Shell cardinality first differs at `r=2`: FCC `42`, HCP `44`.

## 5. Boundary, exposed faces, and finite topology

Independent directional masks, quotiented by independently constructed local symmetry groups, recover the frozen stable boundary populations after orbit relabeling.

For FCC the four stable populations are

- outside degree 7: `12`;
- outside degree 5: `24(r-1)`;
- outside degree 4: `6(r-1)^2`;
- outside degree 3: `4(r-1)(r-2)`.

For HCP the independent exact Gram-star quotient has ten stable orbit classes with the same period-2 population quasi-polynomials recorded in `R037_R033_REPLICATION_ATLAS.json`.

Both worlds independently give the exposed-face count

`F_r=12(3r^2+3r+1)`.

The orientation proportions also reproduce exactly:

- FCC: six unoriented nearest-neighbor classes, each `1/6`;
- HCP: three basal classes, each `1/6`, and six interlayer classes, each `1/12`.

The exact-rational Voronoi boundary-complex reconstruction certifies, for **every** `r=0..20` in both FCC and HCP,

- `F=12(3r^2+3r+1)`;
- `E=2F`;
- `V=F+2`;
- `chi=2`;
- one connected component;
- exactly two incident faces at every boundary edge;
- one cycle in every vertex link.

Hence every boundary in the frozen finite reference range is a topological `S^2`.

R037 deliberately does **not** promote this to an all-radius theorem. The all-`r` shelling/induction remains `THEOREM_CANDIDATE_ONLY`.

## 6. Stable-norm limit shapes

FCC follows directly from the distance inequalities: its scaled graph ball is the cuboctahedral norm ball, with 12 vertices, 14 facets, circumradius 1, inradius `1/sqrt(2)`, anisotropy ratio `sqrt(2)`, and zero scaled convex-hull support remainder.

For HCP, the independent periodic-quotient cycle-velocity hull has 18 vertices and 14 facets. Its circumradius is 1, inradius `sqrt(24/41)`, and anisotropy ratio `sqrt(41/24)`.

In the parity-corrected coordinates `u=m+p/3`, `v=n+p/3`, `p=l mod 2`, every limit-facet inequality has unscaled finite-radius overshoot at most `1/6`, hence normalized support error at most `1/(6r)`. All 18 limit vertices are exactly reachable at even radius.

## 7. Macro scalar and Euclidean-form readout

For `K_r=A_r^3/V_r^2`, the independent closed forms give

- FCC: `K_r -> 90`, with `K_r=90-270/r+927/(2r^2)-540/r^3+O(r^-4)`;
- HCP: `K_r -> 189/2`, with leading correction `-567/(2r)` in both parity classes.

The corresponding exact rational bounds reproduce

- `0 < 90-K_F(r) < 270/r`;
- `0 < 189/2-K_H(r) < 567/(2r)`.

Thus the reported `10^36`, `10^37`, and `10^38` macro error orders are independently reproduced without large-scale enumeration.

If the replicated leading laws are only **post hoc** written as

`A~4*pi_eff*r^2`, `V~(4/3)*pi_eff*r^3`,

the native graph-radius calibration gives

- FCC `pi_eff=5/2`;
- HCP `pi_eff=21/8`.

Under a different radius calibration `R=alpha r`, the area readout scales as `alpha^-2` and the volume readout as `alpha^-3`. Therefore these are `EUCLIDEAN_FORM_READOUT_CONSTANTS`, not microscopic constants and not a statement about classical `pi`.

## 8. R034 — exact local propagation and n-step second moment

With nearest-neighbor physical length normalized to 1, direct exact vector sums reproduce, for FCC and HCP-A/B,

`E[Delta X]=0`, `E[Delta X Delta X^T]=I/3`.

The same local tensor result holds for every legal ideal Barlow environment. The six basal vectors contribute `diag(3,3,0)` to the unnormalized outer-product sum; the two interlayer triangles together contribute `diag(1,1,4)`. Hence all twelve directions contribute `4I_3` and zero total drift.

The walk is therefore a martingale with deterministic predictable quadratic variation, so for all `n`

`E[X_n X_n^T]=nI/3`, `E|X_n|^2=n`.

## 9. Finite-time distributions and memory orders

Independent integer path-count DP gives at `n=2`

- FCC support `55`, histogram `{1:12,2:24,4:18,12:1}`;
- HCP support `57`, histogram `{1:18,2:18,3:2,4:18,12:1}`.

Thus the finite distributions differ despite exact second-moment universality. Return counts agree for every independently enumerated `n=0..12`.

The first rooted local tensor memory is order 3:

- FCC cubic contraction: `0`;
- HCP-A: `sqrt(3)*y*(3x^2-y^2)/72`;
- HCP-B: the negative.

The full fourth tensors also differ, while the scalar radial fourth moment remains exactly common:

`E|X_n|^4=(5n^2-2n)/3`.

The scalar radial sixth moments are

- FCC: `n(35n^2-42n+16)/9`;
- HCP: `(210n^3-252n^2+95n+1)/54` for `n>=1`;
- difference: `-(n-1)/54`.

This sixth formula is not a fit. For the signed HCP cubic harmonic `f_s`, the exact transition operator gives `P f_s=-1/432`. The conditional sixth-power recursion therefore acquires an extra `8(-1/432)=-1/54` on each step after the first.

The first same-Euclidean-radius probability nonuniformity appears at HCP `n=4`, `r^2=35/3`, with path counts `6` and `8`; FCC first shows it at `n=5`, `r^2=9`, with counts `370` and `405`.

## 10. Spectral replication

The independently derived FCC transition symbol is

`lambda_F=(cos(x/sqrt(2))cos(y/sqrt(2))+cos(x/sqrt(2))cos(z/sqrt(2))+cos(y/sqrt(2))cos(z/sqrt(2)))/3`.

Its principal log expansion starts with `-|k|^2/6`.

For HCP, set

- `C=cos(x)+2cos(x/2)cos(sqrt(3)y/2)`;
- `S=2cos(x/2)exp(i sqrt(3)y/6)+exp(-i sqrt(3)y/3)`;
- `h=sqrt(2/3)`.

The independent AB Bloch fiber is

`[[C/6,cos(hz)S/6],[cos(hz)conj(S)/6,C/6]]`.

Its principal log band has the same quadratic term `-|k|^2/6`. Hence leading diffusive geometry is exactly isotropic and FCC/HCP-universal at second order.

After explicitly aligning FCC `[111]` with the HCP stacking axis and a FCC close-packed direction with HCP x, the quartic difference is

`log4_FCC-log4_HCP=-sqrt(2)*y*z*(3x^2-y^2)/432`.

Therefore principal spectral stacking memory first appears at order 4. Under `k=xi/sqrt(n)`, it contributes `O(1/n)` to `n log lambda`. The `10^36` conclusion is consequently a **small-k diffusive** correction statement, not a global uniform pointwise heat-kernel theorem.

## 11. New exact theorem — Barlow return/root-local spectral universality

R034 froze the Barlow gauge statement as a theorem candidate. R037 closes the operator argument under the stated legal bi-infinite Barlow hypotheses.

After basal Fourier transform, the remaining layer coordinate is `j in Z`, and the fiber has the form

`(P_k psi)_j=C(k)/6 psi_j+t_j(k)psi_{j+1}+conj(t_{j-1}(k))psi_{j-1}`.

Legal stacking changes only the orientation of the interlayer structure factor. Both orientations have common modulus because the corresponding structure factors are conjugate up to the fixed orientation convention, with

`|S_sigma(k)|^2=3+2C(k)`.

Thus all interlayer hopping magnitudes are equal and stacking enters only through edge phases. The layer graph `Z` has no cycle flux. Fix `u_0=1` and recursively choose unit phases so that

`conj(u_j)t_j u_{j+1}=|t_j|`.

At a zero hopping the phase is arbitrary because the edge vanishes. The resulting diagonal unitary fixes the root vector and transforms every legal stacking fiber into the same real constant-magnitude Jacobi fiber. A measurable phase selection yields the direct-integral unitary.

Exact consequences are:

1. all legal bi-infinite Barlow stacks have the same root return probability for every `n`;
2. all have the same root local spectral measure;
3. the infinite operators are spectrally unitarily equivalent in this representation;
4. periodic Barlow stacks therefore have the same standard integrated DOS.

For arbitrary nonperiodic stacking, equality of the IDS value is asserted only conditional on existence of the relevant trace-per-volume/IDS limit. Existence itself is not proved. The gauge is `k`-dependent and is not a physical-coordinate vertex permutation, so it does not erase rooted cubic/quartic physical angular memory and does not imply pointwise physical-coordinate heat-kernel equality.

## 12. Evidence-grade disposition

### `REPRODUCED_EXACT`

The exact class includes the core FCC/HCP graph models, distances, growth laws, A/B equivalence, first structural/count differences, exposed-face count and orientation law, stable-norm limit shapes and anisotropy, exact K limits/readout algebra, local drift/covariance, generic Barlow local tensor, n-step second moment, rooted cubic and full fourth memory, scalar fourth/sixth closed forms, FCC/HCP spectral symbols and principal quadratic/quartic terms, Barlow root return/root-local spectral universality, and the periodic IDS consequence.

### `REPRODUCED_FINITE_CERTIFICATE`

The exact-rational boundary topology is independently certified for every frozen radius `r=0..20`; the finite path-distribution summaries and same-radius nonuniformity witnesses are independently reproduced on their stated finite domains.

### `REPRODUCED_ASYMPTOTIC_CERTIFICATE`

The stable boundary-orbit population/TV laws, macro `O(1/r)` remainder bounds, and diffusive quartic `O(1/n)` small-k correction are reproduced with their asymptotic domains kept explicit.

### `THEOREM_CANDIDATE_ONLY`

Three important statements remain deliberately unpromoted:

1. all-radius exposed-face boundary `S^2`;
2. unconditional existence of an arbitrary-nonperiodic Barlow IDS;
3. arbitrary-nonperiodic physical-coordinate pointwise heat-kernel/local-CLT universality.

There are no `FAILED_OR_MISMATCH` rows in the final full replication matrix.

## 13. Required checkpoint artifacts

The completed task-scoped delivery consists of ten files:

1. `research/r037_independent_replication.py`
2. `tests/test_r037_independent_replication.py`
3. `research/r037_generated/R037_R033_REPLICATION_ATLAS.json`
4. `research/r037_generated/R037_R034_REPLICATION_ATLAS.json`
5. `research/r037_generated/R037_SPECTRAL_MOMENT_CERTIFICATE.json`
6. `research/r037_generated/R037_MACRO_READOUT_AUDIT.json`
7. `research/r037_generated/R037_EVIDENCE_MATRIX.json`
8. `research/r037_generated/R037_FULL_REPLICATION_MATRIX.json`
9. `research/r037_generated/R037_MISMATCH_REPORT.json`
10. `research/R037_INDEPENDENT_REPLICATION_REPORT.md`

`R037_FULL_REPLICATION_MATRIX.json` is the taskbook-complete claim matrix and records `claim_id`, frozen claim, independent method, exact/holdout domains, result, evidence grade, minimal counterexample, and provenance boundary for every audited row.

## 14. Return decision

R037 is complete at the requested independent-replication gate. The audited R033/R034 core is reproducible under independent representations and algorithms, with no mismatch presently requiring a change of direction. Downstream work may consume these replicated results, provided it preserves the evidence boundaries above—especially the distinction between exact discrete structure and any later continuum/Euclidean readout.

Draft PR remains a research checkpoint. No CI query is made at this stage.
