# RS-CFD-TRAJECTORY-VERIFY-20260910 — successor 23-cycle native manifest freeze 91D4E7

Status: `CONTINUATION_REQUIRED`
Researcher: `EM-CFD-VFY-MANIFEST-91D4E7`
Claim: `CLM-CFDVFY-91D4E7-20260922-0158`

## Scope

This unit consumes the immutable 4C2F19 cycle-block design and the historical 6D3A91 native-run manifest without replay. It freezes the next confirmatory native benchmark **before observing any new native timing data**. It does not alter 6D3A91, does not execute the unavailable pinned spectralDNS/shenfun/MPI/FFTW host, and does not independently accept the CFD result.

The successor machine-readable contract is `research_artifacts/RS-CFD-TRAJECTORY-VERIFY-20260910_91D4E7/cycle_block_manifest.json`.

## 1. Frozen sampling design

The successor design fixes **23 complete six-order cycles**, hence **138 A/B/C triplets and 414 arm executions**. Every cycle contains each literal order `ABC,BCA,CAB,ACB,CBA,BAC` exactly once. The within-cycle sequence is a deterministic SHA256 permutation from predeclared seed material, so there is no timing-data-dependent reordering, replacement, or optional stopping.

Across all 23 cycles, each arm occupies each execution position exactly **46** times, and each directed pairwise precedence occurs exactly **69** times. Every raw triplet magnitude, literal order and timestamp remains durable evidence; the cycle observer is derived rather than substituted for those data.

The historical physical contract is preserved: 32^3 Taylor-Green, pinned spectralDNS commit `835b01b1e820b5c56559b9a028293e57526bfbf9`, shenfun 4.3, A=dense FFT, B=guarded hybrid, C=guarded forced-fallback, the same input-identity requirements, Nyquist/pressure-diffusion/Source/RK4 ordering, route constraints, endpoint/Hermitian/divergence/Source/energy/fallback diagnostics, and full setup/allocation/compilation/RK4 cost accounting. The declared fully charged horizon is updated from 24 triplets to the frozen **138-triplet** horizon.

## 2. Exact cycle-block inference frozen into the manifest

For each gate `g in {AB,CB,AC}`, a triplet is positive only when its contrast is strictly greater than zero; exact zero and negative contrasts are non-successes. A cycle block is positive only when at least **4 of its 6** triplet contrasts are strictly positive. Ties are never deleted, replaced or resampled.

For the strictly conjunctive global target `AB directional advantage AND CB directional advantage`, the primary analysis is the 4C2F19 intersection-union test. Each component is tested at one-sided alpha `0.05`, and both must pass. With 23 independent cycle blocks, the exact minimal critical value is **16/23** because

`P[Binomial(23,1/2) >= 16] = 763/16384 ≈ 0.0465698`,

while

`P[Binomial(23,1/2) >= 15] = 440485/4194304 ≈ 0.105020`.

At the planning alternative `p_block=0.8`, the exact marginal power of the 16/23 rule is

`11068512973881344/11920928955078125 ≈ 0.928494`,

which gives a dependence-free Frechet lower bound for both AB and CB passing of

`10216096992684563/11920928955078125 ≈ 0.856988`.

If AB and CB are instead required as separately reportable simultaneous claims, the manifest preserves the non-primary Bonferroni `.025` option: **17/23**, with exact null tail `145499/8388608 ≈ 0.0173448`.

The AC negative control is no longer interpreted through the defective triplet-level 17/24 calibration. It uses the same cycle observer; **16/23 AC-positive blocks triggers an attribution veto** until explained.

## 3. Cross-cycle independence is explicitly not fabricated

A fresh solver worker is required for every cycle; solver arrays, route state, sparse caches, RNG state and mutable application context may not carry across cycle boundaries. Immutable binaries/JIT artifacts may be reused only symmetrically across A/B/C and with explicit logging. These requirements reduce operational carry-over and make the inferential block boundary concrete.

They do **not** prove statistical independence. The manifest therefore records `cross_cycle_independence_status = REQUIRED_ASSUMPTION_NOT_CERTIFIED_BY_MANIFEST`. Exact binomial confirmation is permitted only if the completed native run supplies a defensible post-run justification of independent cycle block units under the null, or if an alternative dependence law/calibration was separately predeclared. Otherwise the block-sign p-values are `DESCRIPTIVE_ONLY` and the run is barred from confirmatory performance acceptance. This is fail-closed by construction.

Within each cycle, arbitrary dependence among the six order observations remains permitted under the previously derived sufficient null condition of central sign symmetry of the six-dimensional gate-difference vector. The machine check again verifies the sign-reversal disjointness over all `3^6 = 729` positive/zero/negative sign patterns.

## 4. Machine verification

`research_checks/RS_CFD_TRAJECTORY_VERIFY_91D4E7.py` was executed successfully with stdlib exact `Fraction` arithmetic and also passed `py_compile`. It verifies:

- all 729 six-sign patterns for the central-symmetry block argument;
- the deterministic SHA256 permutation of all 23 cycles;
- 138 triplets / 414 arm executions;
- exact 46-per-arm-per-position balance and 69-per-directed-precedence balance;
- the exact 16/23 IUT tail and the failure of 15/23 at alpha .05;
- the alternate 17/23 Bonferroni tail;
- the exact `p_block=.8` marginal power and Frechet joint lower bound;
- fail-closed synthetic cases for missing independence justification, insufficient AB wins, AC attribution veto, and all-tie non-success.

The verifier output explicitly records `cross_cycle_independence_certified=false` and `native_host_run=false`.

## 5. Acceptance boundary

This unit freezes an experimental contract; it does not execute spectralDNS/shenfun/MPI/FFTW, certify cross-cycle independence, establish a native speedup, establish a nonzero material speedup magnitude, prove generic CFD/industrial acceleration, prove a continuous-PDE theorem, or grant Working Truth/Foundation/final acceptance.

## Next action

On a provisioned host matching the pinned native stack, execute the **immutable 23-cycle manifest exactly as frozen**, including all physical correctness diagnostics, raw triplet retention, route/support/guard/sparse/fallback traces, cycle-boundary reset logging, and fully charged 138-triplet horizon costs. Before any confirmatory interpretation, provide either a defensible cross-cycle-independence justification or the already-predeclared replacement dependence calibration. Return the immutable native checkpoint to this verifier task for independent review.
