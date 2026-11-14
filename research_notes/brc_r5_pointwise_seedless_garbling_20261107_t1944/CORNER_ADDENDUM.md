# R5 addendum — exact one-process seedless garbling for all eight FULL-only flow corners

Date: 2026-11-07. Author-side extension of RESEARCH.md at commit 695dd608b3b8b6a9aac5d5b6482ea3b714b031e7. Scientific pins unchanged (Global a01383f825ef9d43b4b754254303298c64041568, EM 86149263e38c22292c9def1e0f69092efa1be77e). Mathematical status: exact author certificate, independent review outstanding.

## New finite complete corner lemma

The predecessor enumerated exactly 34 distinct deterministic FULL_HIST flow corners, 26 seedless-LR corners and eight FULL-only corners. All eight nonseedless corners have g=a=b=1, u,w∈{0,27/80}, with either (v,z)=(9/40,0) (negative residual) or (v,z)=(1/10,1/10) (positive residual).

RESEARCH.md already gives an explicit universal two-measure transport for **every** legal flow with R=9*b*z−4*a*(v−z)>=0, covering all four positive-residual corners. It also handles the negative-residual (u,w)=(0,0) corner and the entire real two-parameter face g=a=b=1,u=w=0. This addendum gives **three rational 7×7 mass-transport certificates** covering precisely the remaining negative-residual corners.

For each of the following full source flows x, the stated single seedless y has equal stop times T_P,T_Q. All source joint transport entries J_ij are explicitly supplied as nonnegative exact rationals in THREE_CORNERS_VERIFY.py; that verifier checks every exact equation

- row sums sum_j J_ij = M_i(y);
- Q column sums sum_i J_ij = M_j(x);
- P column sums sum_i r_i*J_ij = r_j*M_j(x);
- seedless identity 9*b*z=4*a*(v−z), legality and stop times.

Consequently for ANY real source declaration d∈[0,1]^7, d'_i=(sum_j J_ij*d_j)/M_i(y) (zero if denominator zero) is one legal seedless LR terminal declaration preserving both error coordinates **and** both time coordinates. This establishes pointwise four-observer seedless lifts for each of the eight FULL-only flow corners and all their declarations, without a cross-run seedless mixture.

The new three exact pairs (x,y) are:

1. U_ONLY:
   x=(1,1,1,27/80,9/40,0,0);
   y=(1,1,9/10,5/16,3/10,0,12/121);
   T_P=543/160, T_Q=57/16. J has ten nonzero entries.
2. W_ONLY:
   x=(1,1,1,0,9/40,27/80,0);
   y=(1,9/10,1,0,3/10,5/16,3/35);
   T_P=597/160, T_Q=57/16. J has ten nonzero entries.
3. BOTH:
   x=(1,1,1,27/80,9/40,27/80,0);
   y=(1,19/20,19/20,513/1600,247/800,513/1600,19/200);
   T_P=T_Q=39/10. J has seven nonzero entries.

### Proof certificate for each pair

Each matrix J is encoded sparsely with (source row i, target column j)→exact rational mass in THREE_CORNERS_VERIFY.py. This file is the entire finite proof certificate, not a numeric approximation. It executes the prior (same directory) VERIFY.py exact rational mass/observer checker and additionally checks all three J's. To reconstruct a single lifting for any declaration vector, take its weighted row-average d' exactly as above.

The transport supports were *discovered* with float LP and then solved using rational linear algebra; the saved certificates are exact rationals verified without scipy or sympy. The all-real declaration claim is direct linear algebra after those exact identities, not an inference from a rational grid.

## Impact on parent question

This closes the eight special nonseedless **deterministic flow corners** (and entire nonnegative-residual domain plus one negative-residual continuous face) at the stronger single-strategy observation level. However, an arbitrary FULL_HIST interior flow is not generally an extreme corner: interpolation of distinct seedless processes may violate the seedless bilinear relation and is not automatically a single seedless process. The global nonconvex equality K_FULL=K_L remains open. Concrete next action: construct a parameterized J(x,y(x)) for all negative residual interior flows, or find a complete global infeasibility certificate for one four-observer point. This work concerns the frozen P/Q-BRC finite observer; it does not claim native X6 dynamics equivalence.

## Evidence and status

Run from this directory: `python3 THREE_CORNERS_VERIFY.py`. The executed stdout is in THREE_CORNERS_EXACT_OUTPUT.txt. The verifier imports the colocated exact base `VERIFY.py`, which is itself already published with original independent checks. Original source: research_notes/brc_r5_four_observer_convex_hull_20261107/RESEARCH.md at predecessor f20b9a0bdc8c1fc8f69a2abeb7c231181d1a0d27.

Native service owner/claim inspection returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false`; this is author-side portable evidence, not Source acceptance. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
