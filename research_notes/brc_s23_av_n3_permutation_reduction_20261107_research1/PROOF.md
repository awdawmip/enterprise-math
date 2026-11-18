# S23 n=3: exact worst-case error preserved by permutation symmetrization

Date: 2026-11-07. Status: author-side exact proof and executed integer/Fraction certificate; independent review pending. Frozen science: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Source 8×27 kernel: `research_notes/brc_s23_av_n3_uniform_quarter_upper_20261107_research1/KERNEL.json` (Git blob `564acd9574876059c505fd8a40d14f2f6e0e3736`). Exact continuous global maximum of the unsymmetrized kernel: previous proof at commit `f60c2cc3e1cb983a8e58413a9a26691153a36666` in `research_notes/brc_s23_av_n3_fixed_kernel_exact_continuum_max_20261107_research1/PROOF.md`.

## New theorem

For real a,c∈[1/2,7/8], put z=(1−a)c, p=(a,z,(1−a)(1−c)), b=(z,1−z). The original law on ordered ternary triples is p^⊗3, while the compressed law on ordered binary triples is b^⊗3. Let K be the pinned row-stochastic 8×27 reconstruction matrix. Simultaneously permuting the coordinates of both input and output, set

K_sym(y,x) = (1/6) Σ_{π∈S3} K(πy,πx).

(i) K_sym is an exact rational stochastic matrix with common denominator 6,000,000 and 92 nonzero numerator entries.
(ii) Every lawful parameter satisfies TV(p^⊗3,b^⊗3 K_sym) ≤ TV(p^⊗3,b^⊗3 K).
(iii) On the whole critical rectangle R=[17/25,73/100]×[17/20,7/8], equality holds pointwise.
(iv) Consequently its exact continuous worst-case error equals the already-proven fixed-K maximum

sup TV(p^⊗3,b^⊗3 K_sym) = f(α) = 0.237838693711015430…,

where f(t)=(-821105487t³+611013165t²+365908179t−152165297)/512000000 and α is the unique root in [17/25,73/100] of −2463316461t²+1222026330t+365908179=0.

More generally, searching the global n=3 minimax TV reconstruction error over all stochastic kernels loses no optimum when restricted to S3-equivariant kernels. Equivariant kernels admit **56 nonnegative output-orbit masses with 4 row-sum equations: 52 affine degrees of freedom**, compared with 208 for arbitrary 8×27 stochastic kernels.

## Proof

For an output x, exchangeability of p^⊗3 and b^⊗3 implies that the signed reconstruction residual of K_sym at x equals the average of K's residuals at πx. The triangle inequality and invariance of the L1 norm under permutations give (ii); averaging six permuted stochastic kernels gives (i).

The prior exact Bernstein certificate establishes, on R, the fixed signs of all 27 residuals (one identically zero), with sign vector

(+,+,−,+,+,−,−,−,−,+,+,−,+,0,−,−,−,−,−,−,−,−,−,−,−,−,−).

Its minimum nonzero *signed* tensor-Bernstein coefficient is exactly 2999060771571/1600000000 for residuals scaled by 1,000,000. The 27 output indices in lexicographic ternary order have the **same sign within each S3 permutation orbit**, which the new exact verifier checks. Thus averaging orbit residuals creates no cancellation on R; the L1 inequality is an equality everywhere on R. The previous theorem locates K's global maximizer at (α,7/8)∈R; equality at that witness and (ii) establish (iii) and (iv).

For the dimension count, represent each binary-input orbit by Hamming weight t=0,1,2,3; its stabilizer in S3 is respectively S3,S2,S2,S3. These stabilizers have 10,18,18,10 orbits on ternary output triples: 10=binomial(5,3) for the unordered three-label multiset, and 18=3×binomial(4,2) for one distinguished output and an unordered pair. One nonnegative **orbit mass**, distributed equally over its orbit, specifies each equivariant probability row. The four representative row normalizations are independent, giving 56−4=52 degrees. Any kernel can be symmetrized at no increase of the worst-case error; equivariant kernels are a subset of all kernels. Hence the minimax infima agree.

## Computation and evidence scope

The accompanying `VERIFY.py` is an executed Python standard-library exact-int/Fraction program, with captured output in `RUN_EVIDENCE.txt`. It reconstructs the 6-permutation symmetrized matrix directly from the pinned original K, verifies its row sums, nonnegativity, equivariance, 92 nonzero entries, 56 stabilizer output orbits, recomputes the 26 residual-sign Bernstein coefficient lower bound, and checks equality at four rational points of R. The all-real-parameter equality follows from the Bernstein polynomial sign certificate. The global maximum of the original K is inherited from the pinned previous proof; its grid maximum is not re-executed here.

Observer: stop3 is distinguished from the merged stop1/stop4 branch at compression, while the full ternary ordered joint output and signed residuals are retained through TV evaluation. This is an exact symmetry reduction in the conditional AV auxiliary statistical experiment. The independent ten-label S23 mother bridge R_beh(k,10) for k=4,6 and an optimal primal-dual minimax certificate remain research targets.

Next: optimize the 52-dimensional equivariant primal and seek an exact rational least-favorable prior/dual certificate.