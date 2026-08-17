# R059D Stage AG — Driver Review

Driver-ID: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Date: `2026-08-17`
Stage: `R059D Stage AG`
Task-ID: `RS-R059D-STAGE-AG-N-BEATTY-PROOF-STURMIAN-JUMP-LAW`
Researcher-ID: `EM-R059D-AG-8C2E47`
Owner branch: `research/r059d-stage-ag-n-beatty-proof-sturmian-jump-law`
Frozen owner head: `5063495ff0df643890cd1f4c72ffd2077161c13d`
Accepted AF owner head: `9e863cfc89cab71118959deb38187a21fe1e96e1`

## Driver disposition

`DRIVER_ACCEPTED__N_BEATTY_STURMIAN_JUMP_LAW_PROVED`

Stage AG is accepted.

The principal theorem is promoted inside the R059D research line as a proved N-resolver theorem:

`J_N(r)=floor(alpha*r+1/3)` for every integer `r>=0`,

where `alpha` is the unique positive root of

`3 alpha^2 + 6 alpha - 1 = 0`.

The associated exact jump position and gap laws are also accepted:

`r_m = ceil((m-1/3)/alpha)`

and

`r_(m+1)-r_m in {6,7}`.

The binary jump word is accepted as the lower mechanical/Sturmian word of slope `alpha` and intercept `1/3`.

## Why AG passes

The proof does not promote finite replay into theorem status. It derives the result symbolically from the frozen N-resolver semantics:

1. exact edge-supported dual-cell support criterion;
2. shell/height reduction;
3. exact integer shell threshold
   `(3m-1)^2 <= 12r^2`;
4. maximal-shell formula;
5. Beatty floor theorem;
6. exact integer-only forward recurrence.

Finite validation through `r=16384` is implementation validation only.

The deterministic checker passes `60536/60536`, digest
`54b53af610a6f8c7a805397275d7146f29da371b0c9debc1a52eab70697f68f0`.

History immutability gate passes.

## Frozen results

- `N_BEATTY_THEOREM = PROVED`
- `INTEGER_ONLY_FORWARD_GENERATOR = PROVED`
- `N_JUMP_WORD = STURMIAN`
- `N_JUMP_GAP_ALPHABET = {6,7}`
- `alpha=[0;overline{6,2}]`
- `#1=#3=J_N(r)`
- `#2=r-J_N(r)`
- `|W_r|=r+J_N(r)`

## Boundaries that remain binding

AG does **not** establish:

- a forward-autonomous generator for the full Motzkin boundary word `W_r`;
- a generator for `B(r)` from `r,J` alone;
- a C-resolver phase theorem;
- resolver-independent circle uniqueness.

AF's exact counterexample showing `J` alone does not determine `B` remains binding.

## Driver interpretation

The R059D circle problem has now moved from scalar counting to symbolic boundary dynamics.

The proved jump skeleton gives the exact number of up/down events and their radial event schedule. The remaining mathematical object is the **internal placement of flat/up/down events inside the Motzkin excursion**.

Therefore the next stage must target the full word-growth law:

`r -> W_N(r) -> (B_N(r), J_N(r)) -> (C_N(r), V_N(r))`.

A valid next-stage generator must not query AD occupancy, source-circle lookup tables, classical pi, floating-point square roots, or a precomputed boundary-word table at runtime.

---

Driver freeze:

`AG_ACCEPTED = true`

`NEXT_HARD_TARGET = FULL_N_MOTZKIN_WORD_FORWARD_GENERATOR`
