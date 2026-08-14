# R026 Prior-Art Rooting

Status: `ROOTING COMPLETE / RESEARCH ARTIFACT / NOT CANONICAL`

Researcher-ID: `EM-R026-D19F1B`

R026 deliberately treats a successful mapping to a solved method as `ROOTING_SUCCESS`, not as algorithmic novelty.

| R026 language | Rooted classical method / source | R026 novelty judgment |
|---|---|---|
| Euclidean residual descent | Euclidean algorithm / extended GCD; GNU MP documents exact gcd and Bezout cofactors: https://gmplib.org/manual/Extended-GCD | `EQUIVALENT_TO_KNOWN_METHOD`; useful as a generic residual-descent exemplar, not a new GCD algorithm. |
| DOWN / UP / NEAREST finite precision | Directed rounding and round-to-nearest are standard floating/fixed-point concepts; ADC/finite resolution is established measurement engineering. NIST: https://www.nist.gov/publications/uncertainty-due-finite-resolution-measurements | Standard policy specializations; no Enterprise novelty. |
| Distance-weighted stochastic endpoint choice | Unbiased stochastic rounding literature; Xia et al., *Improved stochastic rounding*, arXiv:2006.00489: https://arxiv.org/abs/2006.00489 | `EQUIVALENT_TO_KNOWN_METHOD`; R026 uses it as a calibration point for expectation vs variance. |
| Residual/error-feedback quantization | Error-feedback / noise-shaping pattern; NIST data-acquisition work explicitly treats quantization as a measurement/digitization error source: https://www.nist.gov/publications/simulated-sinewave-testing-dataacquisition-systems-using-sinefitting-and-discrete | Known engineering pattern; Enterprise residue is the cross-domain state contract, not the feedback rule. |
| Compensated summation | Kahan-style compensated summation is established prior art; Netlib Kahan bibliography: https://www.netlib.org/bibnet/authors/k/kahan-william-m.html | `EQUIVALENT_TO_KNOWN_METHOD`; demonstrates anchor+residual/error-carry bookkeeping. |
| Linear iterative refinement | LAPACK `xGERFSX` performs extra-precise iterative refinement and provides backward-error/error estimates: https://www.netlib.org/lapack/explore-html/dc/df6/group__la__gerfsx__extended.html | `EQUIVALENT_TO_KNOWN_METHOD`; R026 contribution is the explicit residual-precision kill test. |
| Multigrid residual correction | PETSc PCMG requires coarse solver, smoothers, restriction/interpolation, and residual calculation: https://petsc.org/release/manual/ksp/ | `EQUIVALENT_TO_KNOWN_METHOD`; strongly rejects “coarsen state without residual equation”. |
| Convex nearest projection / alternating projection | SIAM *Alternating Projection Methods*, including closest-point projection onto intersections of convex sets: https://epubs.siam.org/doi/book/10.1137/9781611971941 | `EQUIVALENT_TO_KNOWN_METHOD`; displacement residual is a classical correction vector. |
| Harmonic-oscillator phase/energy diagnostics | Long-time phase/energy error of symplectic integrators is classical; Scuro & Chin study the 1D oscillator: https://arxiv.org/abs/math-ph/0411086 | R026 is only a finite-precision policy stress test. Error-feedback is not a replacement for structure-preserving integration. |
| Collision field coordinates | Center-of-mass and relative-velocity coordinates plus exact elastic-collision conservation are textbook classical mechanics. | `EQUIVALENT_TO_KNOWN_METHOD`; no new mechanics. |
| Integer raster residual/phase accumulator | J. E. Bresenham, “Algorithm for computer control of a digital plotter”, IBM Systems Journal 4(1), 1965, DOI 10.1147/sj.41.0025: https://doi.org/10.1147/sj.41.0025 | `EQUIVALENT_TO_KNOWN_METHOD`; exact integer error accumulator is prior art. |
| BRC_SUPPORT | R021/R023 frozen Enterprise Boolean/result-support semantics; R026 did not find a scalar numerical benchmark where support-union semantics yields a new resource win. | Enterprise semantic specialization remains real but **observable-specific**; no new external numerical algorithm claimed. |

## Rooting conclusion

Most successful component behaviors in R026 are already-known algorithms or engineering patterns. That is a successful calibration result. The surviving Enterprise-specific residue is the *uniform semantic compiler layer*: type checking which collapse semantics are valid for which observables, factorization testing for residual sufficiency, anchor-necessity witnesses, and honest state/resource accounting.
