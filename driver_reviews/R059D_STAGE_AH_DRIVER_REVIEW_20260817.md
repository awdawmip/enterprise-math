# R059D Stage AH — Driver Review

Driver-ID: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Date: `2026-08-17`
Reviewed owner branch: `research/r059d-stage-ah-n-motzkin-word-autonomous-growth`
Reviewed owner head: `ab1697d1020bfd987108a9d5775fb471d422304f`
Taskbook source: `134eec2e1482c8edeb2fbe03a4ab6e012d1f9fd1`

## Driver disposition

`DRIVER_ACCEPTED__FULL_N_MOTZKIN_WORD_FORWARD_GENERATOR_PROVED`

Stage AH is accepted.

The decisive theorem is that the canonical N first-sector boundary word `W_N(r)` is generated for every integer `r>=0` by a constant-size integer residual state `(a,b,rho)` with initial `rho=-4` and exact local update rules. Runtime uses no source occupancy query, source `Q`, floating point, square root, trigonometry, pi, word table, jump table, or radius-specific tuning.

The proof closes the chain

`r -> W_N(r) -> (B_N,J_N) -> (D_N,C_N,V_N) -> full D6 boundary`.

Accepted inherited exact results:

- `J_N(r)=floor(alpha*r+1/3)` for all integer `r>=0`, where `3alpha^2+6alpha-1=0` and alpha is the unique positive root;
- `#1=#3=J_N(r)`, `#2=r-J_N(r)`, `|W_N(r)|=r+J_N(r)`;
- `B_N` is the AF Motzkin-height functional of `W_N`;
- `D_N=2r+1`;
- `C_N=6r+6J_N=6|W_N|`;
- `V_N=1+3r(r+1)+6B_N`;
- D6 completion gives one closed adjacent boundary cycle.

Checker: `146779/146779 PASS`.
Digest: `a63fa7ac7bf014ef1c91a0c27613ecef9bab8d360c7379224637a2b11c981c48`.

## Interpretation

AH is the first stage that closes a complete integer-only N-circle generator after source-side discovery. The runtime generator is now autonomous.

This does **not** yet establish:

- N/C resolver-independence;
- uniqueness/canonicity of N as the only Enterprise circle realization;
- the C word-growth theorem;
- information-theoretic minimality of `(a,b,rho)`;
- any theorem about the standard real number pi.

## Next route decision

The next stage is not another N-generator search. AG+AH already imply an exact circumference formula, hence an algebraic large-radius circumference/diameter constant. The next route will prove that constant, freeze exact finite-radius error bounds, and audit its invariance under the admissible native counting conventions before any classical compatibility interpretation.

`AH_ACCEPTED_AND_CLOSED_FOR_DRIVER_REVIEW = true`
