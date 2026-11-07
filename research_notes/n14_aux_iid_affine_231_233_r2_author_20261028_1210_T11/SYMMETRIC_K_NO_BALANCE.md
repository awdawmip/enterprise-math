# Exact negative certificate: symmetric K=562392/8039 is not a primal-effective minimax face

At the Stage231 right endpoint, scalar symmetric penalty K=562392/8039 yields 680 exact finite Bellman states and 1238 strictly positive nonminimum-action gaps (minimum 11225/868212). Bellman ties only at (9,1,0) with P/continue and terminal (14,0,0) with P/Q. The four complete deterministic tied-action corner policies have:

| bits | eP-eQ |
|:--:|--:|
| 00 | -1213677595/6879707136 |
| 01 | -103520966755/5015306502144 |
| 10 | -116454914635/743008370688 |
| 11 | -19282695145/20061226008576 |

All differences are STRICTLY NEGATIVE. By the finite ordered-history-to-Markov occupancy lemma and convex-hull representation of Bellman-tight policies, every dual-optimal policy has eP<eQ. In particular eP=eQ is impossible, so the candidate cannot attain the balanced-error minimax dual bound at any alpha. Do NOT create a positive-width Stage for this scalar symmetric K. This is an exact finite negative result for the external N14 ternary IID auxiliary model, not native X6 or formal Driver acceptance.

Run `python3 CHECK_SYMMETRIC_GAP.py` to reproduce the full enumeration and four rational error differences. This code was actually executed locally and returned `SYMMETRIC_K_NO_BALANCED_OPTIMAL_FACE_PASS`; GitHub source is checked by Git blob identity and readable byte-for-byte. Independent review still pending.
