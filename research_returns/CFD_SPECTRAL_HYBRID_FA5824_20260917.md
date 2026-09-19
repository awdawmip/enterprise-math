# Research return — exact closed-support gate for spectral hybrid CFD

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-CFD-FA5824`  
Claim: `claim-CFD-autoA-20260917-0704-FA5824`

## Verdict at researcher strength

`SUCCESS_AT_BOUNDED_PRIMARY_RESEARCH_UNIT / EXACT_SUPPORT_GATE_PROVED / LOCAL_CHECKS_PASS / HOST_REINTEGRATION_AND_INDEPENDENT_REVIEW_PENDING`

This return consumes rather than repeats the immutable spectralDNS host checkpoint at `20255478397fc475ec0584da0cf4311dd17bcc82`. That checkpoint already establishes that the original host was actually run and that general Taylor--Green/random supports rapidly force FFT fallback. The remaining primary-research question selected by current dispatch was exact closed-support recognition and its applicability/cost.

## New result

For a signed retained seed `S` in `B_K=[-K,K]^3`, iterating negation plus all retained pair sums reaches the least finite carrier `C*` containing `S` and closed under both operations. This gives two exact routing outcomes for a sparse threshold `L`:

1. if the fixed point satisfies `|C*| <= L`, convolution, diagonal Fourier multipliers, retained truncation, and RK linear combinations stay inside `C*` under the frozen host's alias-free retained-cube setting, so a static sparse carrier is support-safe;
2. if any monotone intermediate carrier exceeds `L`, then every valid closed carrier exceeds `L`, so dense FFT fallback is sound immediately.

The carrier is Boolean routing information only. Exact integer wavevectors and full complex vector amplitudes, phase/cancellation, conjugacy and multiplicity remain in the evaluator; no amplitude pruning is introduced.

## Reproducible evidence

- Checker: `research_checks/CFD_SPECTRAL_HYBRID_FA5824_20260917.py`
- Raw result JSON: `research_artifacts/CFD_SPECTRAL_HYBRID_FA5824_20260917/closed_support_detector_results.json`
- Derivation and BRC audit: `research_notes/cfd_hybrid_fa5824_20260917/CLOSED_SUPPORT_CARRIER.md`
- `python -m py_compile` passed.
- Deterministic checker passed 25-repeat cases at `K=7,15` with `L=384`.
- Frozen two-generator lattice: exact carrier sizes `33` (`K=7`) and `139` (`K=15`); `K=7` exactly matches direct enumeration of the frozen hyperplane `kx-7ky+6kz=0`.
- Shear exact carrier sizes: `15` and `31`.
- Taylor--Green and held-out random 16-pair / 128-pair seeds cross the exact lower bound `>384` and therefore select early FFT fallback on both grids.
- Local detector medians are sub-millisecond for all fallback cases and the certified shear cases; the `K=15` two-generator carrier takes about `5.96 ms`. These are detector-only local timings, not host speedup evidence.

## Boundary of claim

This is a finite Fourier-label/support theorem and executable routing certificate. It is not a continuous-PDE theorem, not a strict trajectory-error certificate, not a novelty claim, and not a universal turbulence speedup result. This run did not rerun the already verified author host matrix and does not claim independent acceptance of it. The separate verification/certification/prior-art tasks retain their own authority.

## Next unresolved unit

Wire this static-carrier detector into the existing spectralDNS-compatible adapter as an optional pre-trajectory routing mode, retain the unchanged FFT fallback, and measure detection + full-trajectory total host cost on new held-out cases only. Independent Driver/trajectory verification is still required before any acceptance or broader performance statement.
