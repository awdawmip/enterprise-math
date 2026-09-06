# R037 — R033/R034 Independent Algorithm and Data Replication Audit — Return

- Task: `RS-R037-R033-R034-INDEPENDENT-ALGORITHM-DATA-REPLICATION-AUDIT`
- Researcher-ID: `EM-R037-204389`
- Mode: `TASK_RESEARCH`
- Execution branch: `research/r037-independent-replication-em-r037-204389`
- Source base: `main@c884ff0d83ac6e6455665bfd6e9366dd8107f2c1`
- Frozen R033 owner head audited: `c2aa1758c6cf8f194d8b4493b90c903a2dfcd048`
- Frozen R034 owner head audited: `674fb8717d753cd36fd83b061c869d79e8875b31`
- Return status: `DONE / RETURNED_WITH_PROVENANCE_CAVEAT / AWAITING_DRIVER_REVIEW`

## 1. Direct verdict

The theorem-critical R033/R034 numerical data, exact formulas and finite certificates audited here are reproducible.  No `FAILED_OR_MISMATCH` mathematical claim was found, and no error was found that changes the current downstream direction distinguishing an exact discrete FCC/HCP/Barlow world from later Euclidean/continuum readouts.

The evidence grades are not all the same:

- exact graph growth, distance, stable boundary populations, stable limit shapes, local moments, exact radial moment recurrences and local spectral expansions are `REPRODUCED_EXACT`;
- the exposed-face topology statement is independently reproduced as a **finite exact certificate** through `r=20`, not an all-radius theorem;
- the `10^36..10^38` intrinsic-scalar and diffusive small-k claims are retained as asymptotic certificates with explicit scope;
- all-radius boundary `S^2` and pointwise nonperiodic heat-kernel/local-CLT strength remain theorem candidates;
- the frozen Barlow return/local-DOS gauge claim is **upgraded** from theorem candidate to `REPRODUCED_EXACT` in the precise ideal bi-infinite uniform-NN Barlow scope.

There is one process limitation: a setup lookup of the R034 frozen owner head unexpectedly displayed a partial frozen experiment patch before the independent R034 implementation was complete.  That script was never executed/imported and was not used as the derivation engine, but strict zero-exposure provenance was lost.  The mathematical matrix below remains valid as a replication result; the run must not be advertised as provenance-clean blind replication.  Driver may accept this caveat or reissue only R034 in a fresh clean context if the clean label is required.

## 2. R033 growth / graph-ball audit

### FCC

Using the D3 parity lattice with the twelve `(±1,±1,0)` permutations as moves, an independent constructive distance argument gives

`d_F(x,y,z)=max(max(|x|,|y|,|z|), (|x|+|y|+|z|)/2)`.

The two lower bounds are immediate because one step changes at most one unit in each coordinate and exactly two coordinate units in `L1`; sign routing/cancellation attains the maximum.  Independent BFS agrees through radius 20.

Consequently

- `A_0=1`, `A_r=10r^2+2` for `r>=1`;
- `V_r=(10r^3+15r^2+11r+3)/3`;
- shell-induced edges `=24r^2`.

At the unused holdout `r=100`: `A=100002`, `V=3383701`, shell edges `240000`.

### HCP

Use triangular-layer axial coordinates `(i,j,k)` with `H(i,j)=max(|i|,|j|,|i+j|)`.  Pairing two vertical steps shows that each vertical pair can correct one unit of hex norm.  This gives

- even `|k|`: `d=max(|k|, |k|/2+H(i,j))`;
- odd `|k|`: `d=|k|+max(0,min(H(i,j),H(i+1,j),H(i,j+1))-(|k|-1)/2)`.

This is algebraically equivalent to the frozen odd-layer formula but was derived independently.  BFS agrees through radius 20.

Thus

- even `r`: `A_r=(21r^2+4)/2`, `V_r=(14r^3+21r^2+14r+4)/4`;
- odd `r`: `A_r=(21r^2+3)/2`, `V_r=(14r^3+21r^2+14r+3)/4`;
- shell edges are `27r^2` for even `r`, `27r^2-3` for odd `r`.

At `r=100`: `A=105002`, `V=3552851`, shell edges `270000`.

The rooted shell graphs first differ already at `r=1`: both have twelve shell vertices, but `trace(A_shell^4)` is `384` for FCC and `408` for HCP (equivalently, 6 versus 9 shell four-cycles).  Shell cardinality first differs at `r=2`: `42` versus `44`.  Both leading shell and bulk coefficient ratios are exactly `21/20`.

## 3. R033 boundary / topology / limit shapes

Independent outside-neighbor mask classification modulo independently generated world symmetries reproduces:

- FCC stable four-orbit boundary alphabet from `r=3`, with counts `12`, `24(r-1)`, `6(r-1)^2`, `4(r-1)(r-2)` by the corresponding outside-degree types; positive limiting masses `3/5,2/5`; `TV=(24r-12)/(10r^2+2)<=12/(5r)`.
- HCP stable ten-orbit, period-two alphabet from `r=4`, with the same ten population formulas recorded in the R033 replication atlas; positive limiting masses `3/7,3/7,1/7`; zero-mass total `24r-12`; `TV<=(16)/(7r)`.

The exposed-face crossing count simplifies in both worlds to

`F_boundary(r)=12(3r^2+3r+1)`.

Orientation counts also reproduce: FCC has six unoriented classes each `1/6`; HCP has three same-layer classes each `1/6` and six interlayer classes each `1/12`.

A separately built exact-rational Voronoi halfspace/gluing checker reproduces the boundary complex for every `r=0..20`: it is connected, every boundary edge has incidence two, every vertex link is one cycle, and

`F=12(3r^2+3r+1)`, `E=2F`, `V=F+2`, `chi=2`.

At `r=20`, `(V,E,F)=(15134,30264,15132)`.  This is graded `REPRODUCED_FINITE_CERTIFICATE`.  No all-radius shelling/induction was completed here, so the all-`r` `S^2` claim remains `THEOREM_CANDIDATE_ONLY`.

The stable norm analysis independently yields the FCC cuboctahedron with NN-normalized anisotropy `sqrt(2)` and zero finite-radius support error.  HCP yields the 18-vertex polytope

`|z|<=1`, `|u|+|z|/2<=1`, `|v|+|z|/2<=1`, `|u+v|+|z|/2<=1`,

with physical Gram matrix `[[1,1/2,0],[1/2,1,0],[0,0,2/3]]`, circumradius `1`, inradius `sqrt(24/41)`, anisotropy `sqrt(41/24)`, and facet support overshoot at most `1/(6r)`.  For even `r` all 18 limiting vertices are exactly reachable.

## 4. R033 intrinsic scalar / macro / readout

For `K_r=A_r^3/V_r^2`, direct algebra gives

- FCC `K_inf=90`;
- HCP `K_inf=189/2`;
- the frozen `O(1/r)` bounds at `10^36`, `10^37`, `10^38` are independently recovered.

If graph radius is **temporarily** inserted into Euclidean forms `A=4*pi_eff*r^2`, `V=(4/3)*pi_eff*r^3`, both leading channels give

- FCC `pi_eff -> 5/2`;
- HCP `pi_eff -> 21/8`.

These are `EUCLIDEAN_FORM_READOUT_CONSTANTS`, not identities for classical pi.  If the readout radius is changed to `R=alpha*r`, the shell channel scales as `alpha^-2` and the bulk channel as `alpha^-3`; therefore the numerical readout is calibration-dependent.

## 5. R034 finite propagation / moment audit

Fresh integer path-count DP through `n=12` reproduces all reference return counts.  At `n=2`:

- FCC support `55`, count histogram `{1:12,2:24,4:18,12:1}`;
- HCP support `57`, count histogram `{1:18,2:18,3:2,4:18,12:1}`.

The return sequence shared by both through `n=12` is

`1,0,12,48,540,4320,42240,403200,4038300,40958400,423550512,4434978240,46982827584`.

Exact local vector sums give zero conditional drift and covariance `I/3`.  FCC has zero cubic tensor.  HCP-A has cubic harmonic

`sqrt(3)/72 * y*(3*x^2-y^2)`

and HCP-B has the opposite sign, so rooted local memory starts at order three.  Exact fourth contractions differ between FCC and HCP.

The radial recurrences independently prove, for all applicable `n`,

- `E|X_n|^2=n`;
- `E|X_n|^4=(5n^2-2n)/3` in both worlds;
- FCC `E|X_n|^6=n(35n^2-42n+16)/9`;
- HCP `E|X_n|^6=(210n^3-252n^2+95n+1)/54` for `n>=1`;
- HCP minus FCC `=-(n-1)/54`.

The sixth-order recurrence is closed by an independent signed-cubic calculation: the HCP conditional cubic observable satisfies `E[C_next(X+V)|current]=-1/432`.  Hence scalar radial memory first appears at order six.  Enumeration through `n=12` is a second check, not the derivation.

Explicit same-radius nonuniformity also reproduces: FCC at `n=5,r^2=9` has path counts `370` and `405` on two states; HCP at `n=4,r^2=35/3` has counts `6` and `8`.  Equal covariance therefore does not imply a finite-time spherical law.

## 6. R034 spectral audit

Direct Fourier/Bloch derivation gives the common quadratic log term `-|k|^2/6` and reproduces both frozen quartic terms.  FCC's quartic unit-direction range is `[-1/144,-1/216]`, HCP's is `[-1/168,-1/216]`.  Under diffusive scaling `k=q/sqrt(n)` the angular exponent corrections are respectively

- FCC `q^4/(432n)+O(n^-2)`;
- HCP `q^4/(756n)+O(n^-2)`.

Thus principal spectral memory starts at order four.  In stacking-aligned coordinates,

`log4_FCC-log4_HCP=-sqrt(2)*y*z*(3*x^2-y^2)/432`.

The `10^36` values are only small-k certificates; no global uniform heat-kernel bound is inferred.

## 7. Barlow return/local-DOS theorem upgrade

For any legal bi-infinite Barlow registry sequence, basal Fourier transform reduces the NN transition operator to a Jacobi operator on the layer line.  The two possible interlayer structure factors are conjugates and have the same magnitude

`beta(q)=|1+exp(-ia)+exp(-ib)|/12`.

Stacking therefore changes only edge phases.  Since the layer graph is `Z`, there is no gauge-invariant cycle flux.  Fix `u_0=1` and recursively choose the layer phases `u_n` so every hopping becomes positive `beta(q)`; if `beta=0`, there is nothing to gauge.  Every fiber is unitarily equivalent to

`J_q=alpha(q)I+beta(q)(S+S*)`,

where `alpha(q)=[cos(a)+cos(b)+cos(a-b)]/6`.

The root layer is preserved, so all legal ideal bi-infinite Barlow stacks have the same all-time return probability and root local spectral measure.  Four unrelated legal stacking sequences were independently enumerated through `n=12` and all reproduce the common return sequence above.

**Grade:** `REPRODUCED_EXACT` within the stated ideal NN scope.

Boundary: the gauge is `q`-dependent and is not a physical-coordinate vertex permutation.  It does not remove physical angular heat-kernel information.  A pointwise nonperiodic local CLT remains open.  A finite-volume IDS wording should state its exhaustion/boundary convention; the infinite-operator and root-local spectral equivalence do not require periodicity.

## 8. Evidence summary

Machine-readable full matrix:

`research_artifacts/R037_R033_R034_INDEPENDENT_REPLICATION/EVIDENCE_MATRIX.json`

Summary:

- `FAILED_OR_MISMATCH`: 0 mathematical claims;
- retained theorem candidates: 2 scoped items (all-radius boundary `S^2`; pointwise nonperiodic heat-kernel/local-CLT strength);
- evidence upgrade: 1 (`R034-BARLOW-RETURN-GAUGE` -> exact);
- direction-changing error: **none found**;
- strict provenance-clean label: **no**, due the documented R034 partial-patch exposure.

## 9. Returned artifacts

- `scripts/check_r037_independent_replication.py`
- `tests/test_r037_independent_replication.py`
- `research_artifacts/R037_R033_R034_INDEPENDENT_REPLICATION/R033_REPLICATION_ATLAS.json`
- `research_artifacts/R037_R033_R034_INDEPENDENT_REPLICATION/R034_REPLICATION_ATLAS.json`
- `research_artifacts/R037_R033_R034_INDEPENDENT_REPLICATION/SPECTRAL_MOMENT_DERIVATION_CERTIFICATE.md`
- `research_artifacts/R037_R033_R034_INDEPENDENT_REPLICATION/MACRO_READOUT_AUDIT.json`
- `research_artifacts/R037_R033_R034_INDEPENDENT_REPLICATION/EVIDENCE_MATRIX.json`
- `research_artifacts/R037_R033_R034_INDEPENDENT_REPLICATION/MISMATCH_REPORT.md`
- this return.

## 10. Driver action

Review the mathematical evidence and the R034 provenance caveat separately.  If mathematical replication is the gate, accept the exact/finite/asymptotic grades above and consider promoting the Barlow return/local-spectral statement at its precise ideal-NN scope.  If the program requires the literal label **provenance-clean blind independent replication**, reissue only the R034 portion into a fresh clean executor because the early partial-patch exposure cannot be undone in this conversation.
