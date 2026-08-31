# RERUN_LOG

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`  
Driver: `EM-DVR-7Q4K2C`

## Run sequence

1. Resolved Enterprise-Math researcher identity: `RHR-9Q6M2K`.
2. Locked GLOBAL_KNOWLEDGE snapshot and Enterprise-Math operating rules.
3. Searched first-hand provenance for “Claude proved RH”.
4. Locked Coleman/Claude V6 as strongest exact Claude-specific RH object.
5. Verified its actual status is RH OPEN / no proof claimed.
6. Locked frozen KakeyaLogic source commit `6f12f0fd58e147d04eb2c5feefa4797a9fa0a852`.
7. Built candidate matrix rather than selecting a convenient fallback.
8. Reconstructed Candidate A operator lane.
9. Independently reproved Hilbert–Schmidt threshold `sigma>1/2`.
10. Independently reproved bounded-coupling eigenvalue counting `N_H(Lambda)~Lambda^(1/4)`.
11. Compared to intended squared-zero count `~sqrt(Lambda) log Lambda` and closed direct spectral bijection.
12. Locked Gershon Preprints.org v1 as a full RH claim with Claude Opus 4.6 assistance.
13. Converted its TP∞ route into load-bearing DAG.
14. Marked Lemma 8 uniform curvature inheritance as unproved.
15. Found Lemma 10 Taylor-coefficient spectral expansion.
16. Refuted Lemma 10 by Cauchy–Hadamard root growth for entire functions.
17. Added finite polynomial stress counterexample to the generic Hadamard→Taylor-coefficient inference.
18. Audited Lemma 11 / Remark 19 for hidden critical-line zero exhaustiveness.
19. Locked Yamaguchi v3 spectral-determinant fallback at commit `ccbc3cfcf61518a0fc64a63705900e50a472d5b1`.
20. Located circular Hadamard factorization parameterizing all `xi(1/2+iz)` zeros as real `±gamma_k`.
21. Locked CIPHER/RTSG adversarially failed proof as negative control.
22. Verified our checker independently rejects its tautological functional bridge.
23. Ran numerical finite-matrix checks for Candidate A (`EVIDENCE_ONLY`).
24. Ran Riemann–von Mangoldt scale comparison (`EVIDENCE_ONLY`).
25. Translated the load-bearing boundaries into Enterprise-Math finite-resolution / future-language terms.
26. Lean decision: no Lean file created; the decisive Candidate B bridge is false and Candidate C bridge circular, so axiom/sorry formalization would add no proof evidence.
27. Prepared semantic-checkpoint research artifacts.

## Numerical observations

Representative `sigma=1`, bounded coupling, diagonal `n^4-0.15n^2`:

- N=20: `lambda_max/N^4 = 0.9996250000001766`
- N=40: `0.9999062500000003`
- N=80: `0.9999765625000003`
- N=120: `0.9999895833333333`

Leading RvM target counts in squared spectral variable:

- Lambda=1e4: target/base-count ratio ≈ 2.90
- Lambda=1e8: ≈ 101.43
- Lambda=1e12: ≈ 1747.15
- Lambda=1e16: ≈ 24800.80

These numbers are explicitly **not** used to prove the infinite asymptotic claim.

## Formalization status

`EnterpriseMath/RH/`: not created.

Reason:
- false lemma should be refuted, not axiomatised;
- the Cauchy–Hadamard contradiction is a standard analytic fact and a direct written certificate already closes the candidate bridge;
- no `sorry`, no axioms, no fake `LEAN_CHECKED` status were introduced.

Strongest formal status produced in this run:
- written exact theorem-level counterargument: `CHECKED_CLASSICALLY`;
- executable finite stress checks: `EXECUTABLE_CHECKED_LOCAL`;
- Lean: `NOT_CREATED_BY_DESIGN`.

## CI

`CI_NOT_REQUIRED_FOR_RESEARCH`.
