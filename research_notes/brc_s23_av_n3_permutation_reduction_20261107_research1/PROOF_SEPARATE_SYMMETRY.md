# S23 n=3: stronger separate-input/output symmetrization reduces minimax search to 36 variables

Date: 2026-11-07. Status: author-side exact proof and exact computation; independent review pending. Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This extends the simultaneous-permutation 52-variable theorem in this directory and improves the **parameterization**, not the already established numerical error bound.

## Theorem

For p=(a,(1−a)c,(1−a)(1−c)), b=((1−a)c,1−(1−a)c), a,c∈[1/2,7/8], and any 8×27 row-stochastic kernel K, define the independent input/output twirl

K_sep(y,x) = (1/36) Σ_{π∈S3, σ∈S3} K(πy, σx),

where π acts on three binary input positions and σ on three ternary output positions independently. Then K_sep is a stochastic kernel, invariant under independent permutations, and

TV(p^⊗3,b^⊗3 K_sep) ≤ TV(p^⊗3,b^⊗3 K)

at every legal a,c. Hence the global minimax infimum over all K equals the infimum over independently permutation-invariant kernels. Such kernels are parametrized by **4×10=40 nonnegative output-orbit masses**, with four independent row normalization equations, giving **36 affine variables** (versus 208 for arbitrary K or 52 for simultaneous-equivariant K).

For the pinned previous 8×27 kernel K with row denominator 1,000,000, K_sep has exact row denominator 36,000,000, 104 nonzero entries, and **the same global continuous maximum**

sup_{a,c} TV(p^⊗3,b^⊗3 K_sep) = f(α) = 0.237838693711015430…

where f(t)=(-821105487t³+611013165t²+365908179t−152165297)/512000000 and α∈[17/25,73/100] uniquely solves −2463316461t²+1222026330t+365908179=0.

## Proof

Each input law b^⊗3 is invariant under permutations π. Thus averaging K(πy,x) over π does **not change the marginal reconstructed output distribution** b^⊗3K at all (the input probabilities are exchangeable). Averaging output positions σ subsequently symmetrizes the reconstructed output distribution. Since p^⊗3 is itself invariant under σ, convexity of the total-variation norm shows that output symmetrization weakly decreases the discrepancy. This gives the pointwise assertion for all K, and the minimax infima coincide because the invariant kernels are themselves feasible kernels.

There are four binary input orbits characterized by the number of ones, 0,1,2,3. There are ten ternary output orbits characterized by the histogram (n0,n1,n2), n0+n1+n2=3, namely binomial(5,3)=10. An independently invariant kernel can allocate one nonnegative total mass to each output orbit for each input orbit; divide by the orbit size to obtain probabilities of individual ordered output triples. Row-normalization imposes one independent sum-to-one equation per input orbit. Conversely, every such 4×10 mass array determines a valid independently invariant kernel, proving the exact 36-variable parametrization.

For the pinned K, its exact Bernstein sign certificate on R=[17/25,73/100]×[17/20,7/8] has a fixed sign on each output-permutation orbit (min signed Bernstein coefficient 2999060771571/1600000000 after scaling residuals by 1,000,000). Therefore output symmetrization causes no signed cancellation on R and yields **exact pointwise equality** with the old discrepancy there. The previous proven global maximizer (α,7/8) lies in R. Consequently K_sep attains the same exact global maximum f(α).

## Reproducibility and boundaries

The executed standard-library `VERIFY_36.py` imports the independently executed source certificate `VERIFY.py` from this directory; computes the full 8×27 separated twirl by exact integer sums; checks positivity, row sums, invariance under all 36 pairs of permutations, exactly 104 nonzero entries, four/ten input/output histogram classes, and exact equality at four rational critical-rectangle points plus a strict improvement outside. Captured output is `RUN_EVIDENCE_36.txt`. Reuse the previous exact Bernstein and continuous-maximum proofs; they are not re-run as 8192-grid scans.

The observer/output is the **unconditional ternary three-label marginal**, compared in TV with p^⊗3. This distinct-input/output twirl applies to the currently declared auxiliary minimax deficiency loss; preserving an external *joint (Y,X)* readout would require its own preservation certificate. The frozen six-source/ten-label S23 mother observation map remains a separate step.

Next: formulate a 4×10 stochastic optimization over rational a,c witnesses, then seek an exact uniform upper certificate and finite-support dual lower certificate.