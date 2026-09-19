# CFD spectral hybrid: exact truncated-additive support carrier gate

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-CFD-FA5824`  
Claim: `claim-CFD-autoA-20260917-0704-FA5824`  
Status: `PROVED_FINITE_SUPPORT_ROUTING_CERTIFICATE / LOCAL_CHECKS_PASS / HOST_REINTEGRATION_PENDING / INDEPENDENT_REVIEW_PENDING`

## 1. Recovered frontier and source pins

This run did not replay the already completed full-trajectory host matrix. It consumed the immutable native-host checkpoint `research_notes/CFD9R2K7/host_20260916/REPORT.zh-CN.md@20255478397fc475ec0584da0cf4311dd17bcc82`, which records actual spectralDNS/shenfun/FFTW execution and the negative result that Taylor--Green and random data rapidly fall back to FFT, while exact special supports can remain sparse. It also inspected the exact prior sparse kernel/adapter source `research_notes/CFD-B1F673/main/hybrid.py@e40e5303234c5e8bd725528aad9bff9edf0c059d` (blob `984b0b902302394aa84105bc99aa69e7388d4185`).

The open primary-research unit from that frontier was narrower: recognize exact closed support structure without assuming arbitrary fields remain sparse, and measure the recognition cost sufficiently to decide whether an exact fallback gate is viable.

## 2. BRC applicability and observer audit

BRC is applicable only at the routing layer here. The population is the finite retained signed Fourier label cube `B_K=[-K,K]^3 ∩ Z^3`. Branch identity is the exact integer wavevector label. The observable used for routing is Boolean support membership/cardinality; future operations are retained pairwise convolution, diagonal Fourier multipliers (pressure/viscosity), retained-cube truncation, and linear combinations appearing in RK stages.

No compression from complex amplitudes to positive mass is allowed. Complex vector coefficients, phase/cancellation, conjugacy, and pair multiplicity remain inputs to the nonlinear evaluator. The support certificate is therefore a cost-routing invariant, not a replacement state and not a statement that every allowed carrier label has nonzero amplitude.

Resolution: `REUSE_APPLIED` for the existing exact wavevector/support representation and unprojected rotational kernel; the new work extends the existing hybrid family with an exact support-carrier gate rather than defining a parallel algorithm family.

## 3. Exact finite carrier theorem

For a signed seed support `S ⊆ B_K`, define

`C_0 = S ∪ (-S)` and

`C_{r+1} = C_r ∪ (-C_r) ∪ {p+q ∈ B_K : p,q ∈ C_r}`.

Because `B_K` is finite, this monotone sequence stabilizes at a fixed point `C*`.

**Theorem (least retained additive carrier).** `C*` is the unique least subset of `B_K` that contains `S`, is closed under negation, and contains every retained sum `p+q ∈ B_K` of its elements.

**Proof.** Existence follows from monotonicity on the finite powerset of `B_K`. The stabilized set satisfies the three closure conditions by construction. If `D ⊆ B_K` is any other set containing `S` and satisfying the same closures, then `C_0 ⊆ D`. Inductively, `C_r ⊆ D` implies every negation and retained pair sum added to form `C_{r+1}` also lies in `D`; hence `C_{r+1} ⊆ D`. Therefore `C* ⊆ D`. QED.

**Early fallback corollary.** During the monotone construction every intermediate `C_r ⊆ C*`. Hence, for a production sparse limit `L`, the first observation `|C_r| > L` proves `|C*| > L` and authorizes exact dense fallback without computing the rest of the closure.

**Trajectory support corollary in the frozen finite model.** Assume the host's retained-cube convolution has no alias into retained labels (the prior host checkpoint gives this for the frozen native 3/2 setting). If the Fourier state is supported in `C*`, retained nonlinear convolution is supported in `C*`; diagonal pressure/viscosity do not change labels; retained truncation only deletes labels; and RK linear combinations preserve the carrier. Thus all RK stages stay inside `C*`. A certified `|C*| <= L` permits a static sparse-routing carrier without silently discarding newly generated retained modes.

This statement is finite and support-level. It is not a continuous Navier--Stokes theorem, not an error certificate, and not a speedup theorem.

## 4. Deterministic local checks

Checker: `research_checks/CFD_SPECTRAL_HYBRID_FA5824_20260917.py`  
Raw results: `research_artifacts/CFD_SPECTRAL_HYBRID_FA5824_20260917/closed_support_detector_results.json`  
Production comparison limit: `L=384` full signed labels. Each timing is the median of 25 local repeats and is only the detector cost on this execution host.

| K | seed family | result | exact size / proved lower bound | rounds | pair tests | median detector time |
|---:|---|---|---:|---:|---:|---:|
| 7 | shear line | certified | 15 | 4 | 183 | 0.086 ms |
| 7 | frozen two-generator lattice | certified | 33 | 5 | 855 | 0.354 ms |
| 7 | Taylor--Green support | fallback | >384 | 3 | 905 | 0.504 ms |
| 7 | held-out random 16 pairs | fallback | >384 | 2 | 964 | 0.475 ms |
| 7 | held-out random 128 pairs | fallback | >384 | 1 | 392 | 0.313 ms |
| 15 | shear line | certified | 31 | 5 | 712 | 0.316 ms |
| 15 | frozen two-generator lattice | certified | 139 | 6 | 14047 | 5.962 ms |
| 15 | Taylor--Green support | fallback | >384 | 3 | 770 | 0.457 ms |
| 15 | held-out random 16 pairs | fallback | >384 | 2 | 923 | 0.541 ms |
| 15 | held-out random 128 pairs | fallback | >384 | 1 | 444 | 0.362 ms |

The checker compiles and passes all assertions. It independently enumerates the frozen hyperplane `kx-7ky+6kz=0` in the retained cube. For `K=7` the least carrier is exactly the 33 labels already reported by the native-host checkpoint, providing a deterministic non-trajectory regression. For `K=15` the same exact structural family has 139 labels, still below the current `384` sparse-routing threshold. The shear carrier is exactly the retained line `{(0,y,0):-K<=y<=K}`, with sizes 15 and 31.

For Taylor--Green and both held-out random families the algorithm proves the least support-only carrier already exceeds 384 and returns dense fallback early. This agrees qualitatively with the prior host observation of fast support filling, but this run does not re-label the prior host timing/correctness evidence as an independent verification.

## 5. What the certificate changes

The existing dynamic hybrid asks whether the current support count is below a threshold and rescans until it becomes dense. The new theorem supplies a stronger one-time decision when exact structure exists:

- if the least retained additive carrier has at most `L` labels, route the trajectory through that fixed carrier while still computing exact complex coefficients;
- if the monotone lower bound crosses `L`, switch to the unchanged FFT path immediately;
- no coefficient thresholding, pruning, or assumption of persistent observed sparsity is needed.

This also avoids an overly strict shortcut. For example, the initial shear seed itself is not closed under retained pair sums, but its least closed carrier is only `2K+1`; rejecting every non-closed seed would lose a real sparse structural case.

## 6. Limits and next smallest unit

The detector is currently a standalone verified prototype, not yet wired into the existing spectralDNS adapter. Its timings are local algorithm timings and must not be combined with the prior host's elapsed times to manufacture a cross-host speedup ratio. The independent task `RS-CFD-TRAJECTORY-VERIFY-20260910` remains responsible for independent source/pressure/cost/special-support review; this author does not perform or claim that acceptance.

Smallest unresolved implementation unit: add an optional static-carrier mode to the existing adapter/kernel, use the exact early-fallback result before a trajectory starts, and run only new held-out host cases needed to measure total host cost of detection plus trajectory evaluation. Preserve the unchanged FFT fallback and the full complex coefficient path. Any broader claim that arbitrary turbulent fields possess small exact carriers requires separate evidence and is explicitly excluded.
