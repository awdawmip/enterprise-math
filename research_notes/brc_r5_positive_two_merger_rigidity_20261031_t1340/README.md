# R5 — Exact source rigidity of a strictly positive two-law serial-merger stopping model

**Date:** 2026-10-31 (Asia/Shanghai).  
**State:** `AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING`.  
**Archive:** [EM_R5_20261031_1340_evidence.tar.gz](EM_R5_20261031_1340_evidence.tar.gz) (9,702 bytes; SHA256 `c57ee98ffcad258665e21e4506be83a8c2e41ef74398e388b9f16ccd42abd001`). This contains **unabridged** `RESEARCH.md` (the full proof), `VERIFY.py` (the exact, actually executed Python Fraction checker), `EXACT_OUTPUT.txt` (literal stdout), and `NEXT_TASK.md` (precise continuation). None are placeholders.

## Exact new result

A real finite two-law STOP/CONTINUE process is specified on positive, origin-labelled P/Q branches with two serial LR-information collisions. Two hidden origins of mass 1/2 share likelihood ratio 1 at stage 1. Given origin `i`, stage-2 Q probabilities of three LR classes `(1/2,1,3/2)` are `(alpha_i,1-2alpha_i,alpha_i)` with P probabilities `(alpha_i/2,1-2alpha_i,3alpha_i/2)`, for arbitrary real `0<alpha_i<1/2`. The two optional stage-2 routes lead with strictly positive likelihood-ratio-correct transition probabilities to a **shared** stage-3 LR=1 decision node, then STOP or CONTINUE to stage 4. Full branch table, action-specific error labels and normalization proof are in the archive's `RESEARCH.md`.

For the complete four-vector observer `(error_P,error_Q,stop_time_P,stop_time_Q)`, and REAL seedless-LR behavioral policies, put `s=(alpha_0+alpha_1)/2`. An explicit LR affine-rank minor is
```
det = s^3 (s+4) / 16 > 0.
```
For the signed support direction `H=(3/4+1/(2s)) error_Q - stop_time_Q`, exact finite-horizon Bellman calculation proves
```
max_FULL H - max_LR H = |alpha_0-alpha_1|/(4s)
                        = TV(Q_0,Q_1)/(8s).
```
Consequently FULL and LR **four-dimensional convex hulls are equal iff alpha_0=alpha_1**. If equal, predictive likelihood-ratio flow Markovization proves their **actual real behavioral images** coincide and are the same convex polytope. Hence the entire precisely defined positive stochastic model family cannot solve the mother target. This classification follows from an all-real analytic proof; finite rational tests are independent regressions, not justification for the universal quantifier.

With `alpha_0=1/4,alpha_1=1/8`, the exact integer direction `J=41 error_Q-12 stop_time_Q` has FULL maximum `-10`, LR maximum `-12` and gap `2`. A legitimate FULL witness `(1/4,1/4,7/4,27/16)` is at `L_infinity` distance **at least 2/53 from the entire LR convex hull**. The rank minor is `1809/1048576`.

## Reproduce from complete saved evidence

```sh
tar -xzf EM_R5_20261031_1340_evidence.tar.gz
python VERIFY.py
```

The Python standard-library `Fraction` checker **was executed**. For seven rational parameter pairs it exhaustively computed 1,024 FULL and 16 LR deterministic strategies per pair, checked exact P/Q normalization, positive natural paths, supports and rank. For three equal-source instances it checked 46 distinct FULL deterministic vectors each against exact nonnegative combinations of no more than five LR vertices. Final stdout marker:

`PASS_EXACT_R5_POSITIVE_TWO_MERGER_SOURCE_RIGIDITY`.

Full source file SHA256 digests:
- `RESEARCH.md`: `f29ba48cfb2091bdfe2a54aff8b2f07e6f306654d40a7b786fbc01ee86094725`.
- `VERIFY.py`: `2ac424599ebd1154afe0d46e090b0a5210bb702a80c597fd158ddd8168a2c519`.
- `EXACT_OUTPUT.txt`: `f1ea7ba1921d88aed3f92ba61e62c3c4b93d9b8612a4ee06e90f0d1fe0673c19`.
- `NEXT_TASK.md`: `c0c0e2b1cdc1295848b9f80715f27a289277011fdd127823d78063d0b33ac6c6`.

## Frozen inputs, permissions, next question

Input pins: GLOBAL_KNOWLEDGE_V1 `main@d171cc0e7df8db282f5eb9c40c67e55ce341488b`; Enterprise Math `main@7a46ed70b59ca823805468daab0122ac0b230a20`. Scientific predecessor `a7764f6d1e2b4f4f423c6dc0813e26f568fe60f4` (abstract independent fifth bypass no-go) was used, not replayed. P000 and protected ACTIVE worldview remain unchanged. The origin/route-labelled positive-flow BRC carrier is retained; signed functional is applied only after the readout. **No native X6 correspondence, novel physical law, SOURCE CLAIM/Result, owner adoption, or independent Driver acceptance is claimed.** Native status had `research_authority_granted=false`, `executor_binding_configured=false`, `CODE_REVIEW_REQUIRED`, active jobs quota 5/5, so canonical owner was not authenticated.

**Next exact unit:** make the post-merger L terminal response genuinely path/source-dependent, while keeping strictly positive normalized P/Q flows and true LR collisions. Test all-signed four-hull equality by exact rational ≤5-LR-vertex primal certificates for each FULL deterministic observation, or publish a Farkas separator. Only if hull equality and rank four pass, certify exclusion from the actual real LR image. See unabridged `NEXT_TASK.md` in archive.

**Archive storage on this unmerged PR branch is author-side durable evidence, not mathematical or source-control-plane admission.**
