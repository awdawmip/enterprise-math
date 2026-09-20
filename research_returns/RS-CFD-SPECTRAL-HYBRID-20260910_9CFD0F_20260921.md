# CFD: exact carrier certificate, empty-support repair and cold-cost obstruction

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-DIRECT-9CFD0F`  
Claim: `CLM-CFD-9CFD0F-20260921`, Issue 240 comment `5753372709`  
Activity: `RA-RESEARCH-20260921-9CFD0F09`  
State: `CONTINUATION_REQUIRED / ORIGINAL_HOST_NOT_RUN / NO_SELF_ACCEPTANCE`

## Inherited scope

Continue the static-carrier frontier at `3fb575716647b3f618bbd1483b7a4439ccca2601:research_returns/RS-CFD-SPECTRAL-HYBRID-20260910_292BCE_20260917.md`. The original pinned spectralDNS/shenfun/FFTW serial-host execution remains outstanding. This return does not replace that host requirement with another surrogate pass.

The source adapter blob is `1436c730189ba1b4f8d84359ff24a39f3ddc2f82`; the source checker blob is `ce3de7ea13abae2235afd47260d5faf58989308d`. The existing detector, padded-FFT reference and pair-kernel mathematics were reused as named function extracts, not claimed to be byte-identical copies of complete upstream files. Current-environment imports found spectralDNS, shenfun, mpi4py and mpi4py-fft absent. Actual pip and direct-download attempts did not obtain the required host. No research computation was delegated to GitHub Actions.

## Exact axis-generator certificate

Let S be exact signed support, closed under negation, inside B_K=[-K,K]^3 intersect Z^3. For nonempty S let d_j be the gcd of the absolute j-th coordinates. Require the witness that each nonzero axis generator d_j e_j actually occurs in S. A coordinate with d_j=0 is fixed at zero.

Then the least negation/retained-addition closure is exactly

    C = product_j {m d_j : |m d_j| <= K},
    |C| = product_{j:d_j>0} (2 floor(K/d_j)+1),

with factor {0} for d_j=0. Empty S has empty closure.

Proof: divisibility and zero-coordinate constraints are preserved by negation and retained sums, so closure is contained in C. Conversely S generates zero and contains each signed axis generator. Repeated axial additions generate every admissible axial multiple without leaving the box. Summing these axial points coordinate by coordinate stays inside the box and generates every member of C. Thus both inclusions hold. S={0} is handled separately by the same nonempty argument.

This permits direct construction and direct over-cap dense fallback without pair enumeration or a quadratic pairwise re-verification. It does not assume constant-time arbitrary-size integer arithmetic. It is a proof candidate requiring independent review, not an external-novelty or Foundation claim.

The witness is essential. At K=7 the diagonal seed ±(1,1,0) closes to 15 labels, not the Cartesian 225. The diagonal parity seed ±(1,1,0), ±(1,-1,0) closes to 113, not 225. The implementation declines the shortcut and reuses the original detector in both cases. BRC resolution is `EXTEND_EXISTING_TOOL / REUSE_EXECUTED`: exact Boolean signed labels are used only for routing; complex vector amplitudes, phases, conjugacy and pair multiplicity are retained. No pruning is introduced.

## Empty-support defect and repair

The published gather constructs an empty label array of shape `(0,)`. Together with the published Numba kernel's two-index label accesses, an initially zero field raises `TypingError`. The minimal repair is `.reshape(-1,3)` on the label array, yielding `(0,3)`. The repaired zero trajectory stayed exactly zero for all 12 steps. This is a failure of the specific published gather/kernel combination, not every possible callback.

## Tests and cost evidence

All 8,192 symmetric seeds on the nonzero K=1 cube were compared against the existing closure detector: 1,040 fast certificates, 7,152 correct general-detector declines. There were also 477 larger cap-boundary checks across 120 families, two independence counterexamples and six invalid-input rejections. All passed.

Seven new held-out trajectories freeze n=16, retained K=7, physical padded grid 24^3, complex128, viscosity 0.01, dt=0.002, 12 RK4 steps, cap 384, one FFT worker and no pruning. Validation compares all 48 RK-stage right-hand sides and 12 endpoints per case. New and old static arrays are bitwise identical; all FFT comparisons pass tolerance 2e-13 + 2e-12 maxabs(reference), with maximum absolute discrepancy 2.637977740025101e-18. Nonzero dense-reference off-carrier roundoff is recorded rather than erased. Dense fallback's complement diagnostic is not applicable.

Six cases explicitly have nonzero projected nonlinear response. The mean-zero collinear case is labeled a linear control: incompressibility makes its advective nonlinearity vanish. Its unprojected rotational term need not vanish; the implementation preserves downstream pressure projection and does not substitute zero for that term.

Warm repeated-trial median total milliseconds, including setup, detector, certificate verification, allocation and integration but excluding the separately recorded first JIT warmup:

| Case | FFT | Old static | New static |
|---|---:|---:|---:|
| xy225 nonlinear active | 55.441 | 57.509 | 18.554 |
| xy35 nonlinear active | 56.098 | 5.654 | 4.541 |
| yz35 nonlinear active | 59.845 | 6.264 | 4.960 |
| parity113 general detector | 59.182 | 17.223 | 17.496 |
| oblique15 linear control | 56.873 | 4.514 | 4.468 |
| xyz3375 dense fallback | 56.478 | 57.065 | 58.352 |
| random48 dense fallback | 55.726 | 57.088 | 57.796 |

Seven interleaved repeats yield 147 raw rows. For xy225, old detection and verification cost about 18.48 ms and 20.54 ms; new detection about 0.152 ms. Pair-kernel time remains about 13.6–13.7 ms. The approximately 3.10x old/new warm gain is removal of certificate setup cost, not a different physical equation. General-detector and dense-fallback cases do not demonstrate a gain.

A separate 18-row experiment uses three fresh processes per evaluator and case; its timer starts after imports and includes first JIT compilation:

| Case | FFT cold, ms | Old static cold, ms | New static cold, ms |
|---|---:|---:|---:|
| xy225 | 61.925 | 571.182 | 537.957 |
| xy35 | 61.820 | 515.463 | 496.300 |

The sparse route therefore LOSES these one-shot cold trajectories, by approximately 8.0–8.7x versus FFT. Warm ratios must not be advertised as one-shot speedups. A compiled persistent session or an explicitly tested reuse horizon is necessary. These are local finite-Galerkin results, not spectralDNS host, industrial, universal-speedup, continuous-PDE or native-P000 conclusions. The small repeat counts establish neither hardware-independent ratios nor confidence intervals.

## Durable output and precise remaining unit

This branch contains `research_artifacts/CFD_HOST_9CFD0F_20260921/fast_carrier.py`, `checkpoint.json`, and the verified 18-row `cold_raw_trials.csv.gz`, plus this proof/return. The complete user-delivered `CFD_9CFD0F_research.bundle` includes all reproduction scripts, both original-function extracts, all 165 warm/cold timing rows, summaries, full report and SHA-256 manifest. Its SHA-256 is `7ff5b7369cb052f42820da987d0559e202834dd8d841784168c29810d73465bb`; its embedded local commit is `2f745578ab0d4c4f3f5ea51753adf79e4e689081`. The complete bundle and 147 warm raw rows have NOT been mirrored into GitHub in this checkpoint; preserve that explicit archival debt rather than treating the GitHub branch as the entire reproduction package.

Reproduce from the delivered bundle with `git clone CFD_9CFD0F_research.bundle cfd-check`, then run `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python check_research.py` and `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python check_cold.py` in that clone. NumPy, SciPy and Numba are required. The second script uses bounded local subprocesses to measure first-JIT cost.

Continuation: preserve/mirror the full user-delivered reproduction bundle; apply the axis-witness selector and empty-label repair to the existing pinned native adapter; run the actual original serial host on the nonlinear-active held-out set, retaining native dense callback, pressure/diffusion and RK4. Charge setup, certificate verification, allocation and compilation under a declared reuse horizon. Retain dense fallback for losing cases. Independent `RS-CFD-TRAJECTORY-VERIFY-20260910` review is still required. No DONE, canonical promotion or mathematical acceptance is granted here.
