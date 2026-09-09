# X6 factor-layer research handoff

Status: `CURRENT RESEARCH HANDOFF / NO FOUNDATION PROMOTION`
Parent objective: `OBJ-X6-FACTOR-LAYER-20260906`
Prepared for successor researchers: `2026-09-09`

## 1. Read this first

The complete durable synthesis is:

`research_notes/20260906T122500+0800-x6-layer-frobenius-multiresolution-progress.md`

Frozen source pin for this handoff:

- repository: `awdawmip/enterprise-math`
- commit: `84ccdcba0525155be29e8a0f89a4b05885e76686`
- Git blob: `b5154af019d4f7d437341562e4b22b0b2d327304`

The note is intentionally self-contained enough that a new researcher should not need predecessor chat history.

## 2. Current frontier

Keep these exact derivations:

1. X6 layer path multiplicity is `N!/(a_1!...a_6!)`.
2. The first two-axis divisibility defect is the classical binomial factor criterion, retyped as an X6/BRC path defect.
3. Primitive 3-axis shell counting gives the exact `4 J_2(N)` factor bridge, but exact counting is factor-equivalent on semiprimes.
4. Multinomial Lucas gives factor-scale defect sublattices inside one X6 layer.
5. If `r|R`, one fine cyclic layer modulo `x^R-1` projects exactly to the `r` layer; one expensive exponentiation therefore supplies all divisor layers.
6. The same fine state can be observed through every cyclotomic component `Phi_d`, `d|R`, with total component dimension `R`.

Keep these as finite evidence, not theorem claims:

- divisor-layer and cyclotomic observation families materially improve finite success rates over the fine layer alone;
- constant-success width in the tested balanced-semiprime ranges behaves approximately like `R~p`;
- sparse multi-term seeds can beat the simplest binomial seed in some fixed-width tests, but no stable theorem-level optimum in branch count was established.

Current generic verdict:

`GENERAL_SEMIPRIME_FACTORING_BREAKTHROUGH = REJECTED_AT_CURRENT_FRONTIER`.

The generic claim may be reopened only if a new observer breaks the scale wall or otherwise gives total work below the current `sqrt(p)` target barrier used for comparison with Pollard rho.

## 3. Do not repeat without new evidence

Do not restart these routes as if unexplored:

- Fibonacci or X6 scalar layer codes;
- whole-layer Cell counts or total path-period signatures;
- prefix-gcd compression, which collapses to LCM/factorial/product-tree structure;
- fixed `N mod r`, Legendre-symbol, or `ord_r(N)` scheduling as a recovery of the hidden factor ratio;
- arbitrary large stacks of linear changes followed by gcd, which reproduce the random-gcd opportunity baseline;
- claims that triadic or six-axis branch count alone creates a factorization advantage;
- generic fixed-width Frobenius factoring across growing factor scales.

## 4. Published successor tasks

The state-machine tasks attached to this handoff are:

1. `X6-FAC-AUDIT-20260909` — independent reconstruction and reproduction of the exact identities, finite success rates, and scale wall.
2. `X6-FAC-SPECIAL-20260909` — after audit, search special semiprime families where a natural factor relation permits `R=o(p)`.
3. `X6-FAC-OBSERVER-20260909` — after audit, search for a genuinely non-Frobenius provenance-preserving X6/BRC observer with sub-barrier total work, or prove a stronger no-go.

The second and third tasks depend on the audit task so successor work consumes one common reproducible baseline.

## 5. Prior-art boundary

The cyclic Frobenius factorization family overlaps the Agrawal–Saxena–Srivastava 2016 line. Pollard rho, Pollard-Strassen/product trees, Fermat/near-factor methods, Pollard p-1 / Lucas-order mechanisms, QS and NFS remain mandatory comparison families where structurally relevant.

No novelty claim follows merely from the Enterprise coordinate interpretation.

## 6. Return discipline

Successors should append corrections or new results rather than rewriting this handoff as if older negative results never existed. Finite experiments must remain typed as finite evidence. If an exact identity or cost bound fails, report the smallest counterexample and downstream impact.
