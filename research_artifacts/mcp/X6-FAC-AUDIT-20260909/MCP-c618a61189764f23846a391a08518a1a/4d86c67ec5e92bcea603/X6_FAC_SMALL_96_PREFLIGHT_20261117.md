# X6-FAC independent finite preflight, 2026-11-17 (author-side, no formal review)
Task: X6-FAC-AUDIT-20260909 / publication TP2-A791A4490CC57388583C.
Sources: handoff research_handoffs/X6_FACTOR_LAYER_20260909/START_HERE.md and pinned scientific note @84ccdcba0525155be29e8a0f89a4b05885e76686, blob b5154af019d4f7d437341562e4b22b0b2d327304.

## Exact algebra checked
For any positive integer R and r|R, evaluation on the quotient ring Z/NZ[x]/(x^R-1) to Z/NZ[x]/(x^r-1) is a well-defined ring homomorphism. For a=f(x)^N mod (N,x^R-1), the quotient has coefficient j equal to sum of a_k over k ≡ j (mod r). It equals a direct exponentiation f(x)^N mod (N,x^r-1); this is universal for these rings, independent of N primality. For each divisor d|R, Phi_d(x) divides x^R-1 over Z[x], so the same polynomial reduces to each cyclotomic quotient; their degree sum is sum phi(d)=R. For gcd(N,R)=1 the full cyclotomic decomposition is an invertible coordinate change modulo N; otherwise we make no invertibility claim. These projections are declared arithmetic observers of the retained original fine-layer coefficients, not a lossless reconstruction of native X6 path provenance without further type proof.

## Predeclared finite plan
Take p in {11,13,17,19}, g in {6,12,18,24}, q the first prime >=p+g, N=pq; 16 semiprimes, R in {12,18,24}, sparse seeds f=1+x and f=1+x+x^2: 96 deterministic trials. Compute P_R using square-and-multiply cyclic convolution mod N. A factor witness is a coordinate a_j with 1<gcd(N,a_j)<N. Inspect fine coefficients, then all divisor quotients, then all monic Phi_d quotient coordinates. Each divisor quotient was asserted against an independent fresh exponentiation at r. Each cyclotomic quotient was asserted against an independent exponentiation directly modulo Phi_d; degree identities checked.

| Width, seed | fine / 16 | fine+divisor /16 | fine+divisor+cyclotomic /16 | counted modular multiplications | counted gcds |
|---|---:|---:|---:|---:|---:|
| R=12, 1+x | 10 | 12 | 14 | 20,287 | 832 |
| R=12, 1+x+x² | 12 | 15 | 15 | 24,323 | 832 |
| R=18, 1+x | 16 | 16 | 16 | 40,686 | 1,200 |
| R=18, 1+x+x² | 12 | 15 | 15 | 49,741 | 1,200 |
| R=24, 1+x | 16 | 16 | 16 | 64,995 | 1,728 |
| R=24, 1+x+x² | 12 | 15 | 15 | 81,661 | 1,728 |

The arithmetic counts include the sparse main cyclic exponentiation and coefficient-reduction operations, not the independent assertion controls or full Python runtime. Workloads are toy p<=19, chosen to check operator semantics, not a blind representative scale sample. The original large-p hit rates and R~p wall remain untested by this preflight; Pollard rho, Fermat, seeds, scale confidence intervals and full end-to-end accounting remain separate obligations.

Reproducibility: author-side Python3/sympy script x6_fac_finite_audit.py sha256 7c78efb6845655117e579e6b067cce2e67c970047b86459954d5c66ff4bc8e09; full 96-trial JSON sha256 b06c1b8615fc58d88e5802be33ce7bba03bd45d7b5fcc2bcb9ff3d8b48056a0e. Local paths /mnt/data/x6_fac_finite_audit.py and /mnt/data/x6_fac_finite_audit_results.json in execution environment. This artifact staging alone is not Source publication, CLAIM or Driver review.
