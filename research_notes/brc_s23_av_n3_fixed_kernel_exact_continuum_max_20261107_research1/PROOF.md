# S23 conditional AV n=3: exact continuous supremum of the previously fixed reconstruction kernel

Date: 2026-11-07. Status: AUTHOR-SIDE EXACT PROOF / EXACT-COMPUTATION CERTIFICATE / INDEPENDENT REVIEW PENDING.
Frozen science pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Source kernel: `research_notes/brc_s23_av_n3_uniform_quarter_upper_20261107_research1/KERNEL.json` (blob `564acd9574876059c505fd8a40d14f2f6e0e3736`), unchanged, eight lexicographic binary inputs by 27 lexicographic ternary outputs, row denominator 1,000,000.
Previous lemma and bound: `research_notes/brc_s23_av_n3_bilinear_2ndorder_20261107_research1/PROOF.md` at `54c6254c49434902510c03292578071833bb5528`.
Project main control read at `91ec9d893bba99e33bb129ce079b1f5f29e971ff`. Separate formal native session/CLAIM not established (backend identity/version mismatch; operation_sent=false).

## Exact result

For all real `(a,c) in [1/2,7/8]^2`, set
`z=(1-a)c`, `p=(a,z,(1-a)(1-c))`, `b=(z,1-z)`, and
`E_K(a,c)=(1/2)||p^{tensor 3}-(b^{tensor 3})K||_1`.
The fixed rational stochastic K has **exact global continuous maximum**

```
sup_{a,c in [1/2,7/8]} E_K(a,c) = f(alpha),
f(x) = (-821105487 x^3 + 611013165 x^2 + 365908179 x - 152165297)/512000000,
alpha = the unique root in [17/25,73/100] of
        -2463316461 x^2 + 1222026330 x + 365908179 = 0.
```

The maximum occurs at `(a,c)=(alpha,7/8)`. For orientation only,
`alpha = 0.7063779901394989561293...` and `f(alpha)=0.2378386937110154301506...`.
Consequently the minimax error `delta_3=inf_K sup_{a,c} E_K(a,c)` satisfies
`5211/21952 <= delta_3 <= f(alpha)`.
This is the **exact worst-case error of this specific K**, not an assertion that K is globally minimax optimal.

## Proof

1. **Polynomials and exact sign region.** Put `G_j(a,c)=1000000*[p^{tensor3}-(b^{tensor3})K]_j`, for `j=0,...,26`; their degree in each variable is at most three. On
   `R=[17/25,73/100] x [17/20,7/8]`, the tensor-product Bernstein degree-(3,3) coefficients of all 26 nonzero signed residuals have strictly positive minimum
   `2999060771571/1600000000` (for the scaled G; divide by 1e6 for unscaled residuals).
   Here the signs at `(a,c)=(7/10,43/50)` are
   `(+,+,-,+,+,-,-,-,-,+,+,-,+,0,-,-,-,-,-,-,-,-,-,-,-,-,-)`,
   and the 14th residual, index 13, is identically zero. A Bernstein polynomial is a convex combination of its control coefficients, so these fixed signs hold everywhere on R. Accordingly `E_K=P/(2e6)` on R, with `P=sum_j sign_j G_j`.

2. **Monotonicity in c on R.** The tensor Bernstein degree-(3,2) coefficients of `dP/dc` on R have strictly positive minimum `57424508055009/32000000`. Thus `dE_K/dc>0` everywhere on R, proving
   `E_K(a,c)<=E_K(a,7/8)` for `(a,c) in R`.

3. **Maximize the boundary cubic.** Substituting `c=7/8` into `P/(2e6)` gives `f(a)` above. The exact first derivative is
   `f'(a)=(-2463316461 a^2 + 1222026330 a + 365908179)/512000000`.
   The derivative is positive at 17/25 (`17653977/156250000`) and negative at 73/100 (`-547139421669/5120000000000`).
   The affine second derivative is strictly negative at both interval endpoints, hence throughout. Therefore `f` has exactly one maximum, at the root alpha.

4. **Exclude the remainder of the full lawful square.** Divide `[1/2,7/8]^2` into `256^2` closed grid cells, with coordinates `a_i=(4N+3i)/(8N)`, `c_j=(4N+3j)/(8N)`, `N=256`. Exactly 578 cells are entirely contained in R; evaluate all remaining 64,958 cells by their four corner values. An exhaustive **integer-only** evaluation of 66,049 grid vertices and all 27 output residuals gives maximum among the corners of those outside cells
   `15172039/64000000`, attained at `(i,j)=(0,0)` (`a=c=1/2`).
   The previously proved bilinear second-derivative enclosure, applied to each cell, gives
   `max_cell E_K <= max_four_corners E_K + 3915/(8192*N^2)`.
   Thus any point in any cell not wholly contained in R obeys
   `E_K <= 1988690667683/8388608000000 = 0.23707040163075924...`.
   A single exact rational witness on the boundary, `a=35319/50000,c=7/8`, has
   `E_K=15221676396934896943367/64000000000000000000000 = 0.23783869370210778...`, strictly exceeding the outside-cell upper bound.

5. **Cover the square.** Every point lies in a grid cell. Entirely contained cells lie in R and obey steps 1–3; all remaining cells obey step 4. The value at (alpha,7/8) is feasible. Therefore it is exactly the global supremum of K. QED.

The new science is the exact boundary-maximizer theorem and algebraic value, replacing the old 8192-grid upper approximation. The independent short exact certificate re-executes a 256-grid plus Bernstein sign checks and does not rerun 8192-grid evidence.

## Computational verification and BRC scope

`VERIFY.py` is the executed Python standard-library-only certificate. It recomputes the kernel, the 27 polynomial residuals, every 2D Bernstein coefficient, the exact edge polynomial, and the 257x257 rational grid with integer numerators; `RUN_EVIDENCE.txt` holds genuine captured stdout. All comparisons are exact `int` or `Fraction`, including the global strict inequality. The decimal alpha and f(alpha) above are explanatory high-precision diagnostics and are not proof inputs.

Observer map: stop3 remains distinguished, while stop1/stop4 map to N in the compressed experiment. BRC reuse: `REUSE_APPLIED`; full three-branch output and signed residual coordinates are retained until total-variation evaluation, with explicit source/provenance and a fixed lawful observer. This claim concerns the S23 conditional AV auxiliary experiment. The mother objective remains the lawful six-source/ten-label `R_beh(k,10)` for `k=4,6`; exact lawful encoder/decoder/source transfer and the minimax dual certificate remain open.

Scientific review: author-side exact certificate completed; independent review and formal native admission pending.
