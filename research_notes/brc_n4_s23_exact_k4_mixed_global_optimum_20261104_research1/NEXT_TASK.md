# Follow-up: certify the small-budget optimizer map

Mother objective: source-aware BRC N=4 S23 integer-budget T/B Chernoff design, in the wider still-open ten-label decoder minimax line `[1/2,2/3]`.

Verified author frontier at `s=1/2,v=1/21`: no optimum with both observation types at K<=3; **unique** global optimum K=4 is `(m,n)=(2,1)`; exact advantage over four B samples exceeds `1/5000000`. A fully exact rational interval certificate and analytic data processing proof are in `PROOF.md`, `VERIFY.py`, `RUN_EVIDENCE.txt`. Do not replay earlier large-K arguments to establish this fact.

Next independent unit: classify optimal integer pairs for K=5..100 at fixed s=1/2. Monotonicity permits `n=floor(K-(3/2)m)` for each m; each candidate requires **one shared Chernoff exponent** `max_t(m f_T(t)+n f_B(t))`. Derive certified interval/derivative bounds for comparisons, determine if optimizers can require n>1 and identify count transitions. Then vary rational s above/below the efficiency crossover with exact bounds. Record tie status and exact finite cover, not only floating-point scanning.

Actual Source-native task CLAIM/Result and independent Driver review remain outstanding.
