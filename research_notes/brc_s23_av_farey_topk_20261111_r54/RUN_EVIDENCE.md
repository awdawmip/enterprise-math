# R54 executed exact validation — 2026-11-11

Scientific pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Previous frontier: R53 PR #2022, source `077fee86b0c3dded88d1c6e844e609bea5b8ff34`.

## Exact runs

Executed locally in Python with built-in arbitrary-precision integers only. The published standalone verifier at `VERIFY_R54_PUBLISHED.py` was executed before remote publication and produced:

```text
S23 352 352 Farey (43, 164, 59, 225) quotient_blocks 7 top [225, 61, 286, 122, 347, 183, 19, 244, 80, 305, 141, 202]
S23 100000 10 Farey (3749, 14298, 25389, 96829) quotient_blocks 13 top [96829, 82531, 68233, 53935, 39637, 25339, 11041, 93572, 79274, 64976]
S23 1000000 12 Farey (124904, 476361, 165289, 630382) quotient_blocks 15 top [630382, 154021, 784403, 308042, 938424, 462063, 616084, 139723, 770105, 293744, 924126, 447765]
PASS_R54_EXACT 12620 exhaustive rational instances, 300 random, 8 interval-certified families
```

Exhaustive rational domain: every reduced p/q for integers 3<=q<=40 and 1<=p<q; every 1<=K<q. All complete K-element outputs matched independent residue sorting implemented as an exact k-best heap with k=K. The 300 seeded q=1000003 inputs had 12<=K<800 and independent exact full-list checks. The five theta=sqrt(2)-1 tests use the exact isqrt-based interval of width 1/10^30 and K in (12,20,50,352,1000), with strict Farey containment checked at both endpoints. The three frozen S23 tests use the original 1/10^24 enclosure with strict containment at both endpoints; K=352 is checked completely, K=100000 (first 10) and K=1000000 (first 12) are checked by scanning every s from 1 to K and maintaining an exact k-best heap.

The separately executed `VERIFY_R54_SWEEP_PUBLISHED.py` produced:

```text
PASS_R54_S23_352_CUT_SWEEP moves 28800 changes 290 gaps {'u': 188, 'v': 127, 'u+v': 37} farey [43, 164, 59, 225]
```

The sweep reconstructs all 225 source-age interval ownership assignments for each of 352 cells against both endpoints and the midpoint; it uses the original 128 historical labels. Its 28,800 moves include the final cyclic return; R53's 28,672 counted only transitions to the last cell.

Local executed code SHA256: `VERIFY_R54_PUBLISHED.py=aa8824554593be49598f4ba6c4414b009477a8c0be88a9f0d90f71047f37df3c`, `VERIFY_R54_SWEEP_PUBLISHED.py=a0dc387561cbef02c3eeaab6c686e86aade28c54654ed16fdba80b2c01c40663`. Complete local extended certificate SHA256: `b30a547170b7f06d580d8d49916b45e497582cefad06b751e63555d2f7698a52`. Full sweep certificate SHA256: `b01eee50e000fe9e95e1aa715706e4758e8312091fc98b7ed7110cb707fc064e`.

This is author-side finite checking of a hand-proved proposition; independent mathematical peer review, formal theorem admission, and frozen full 298-run risk recomputation have not been performed in R54.

## New output

Certified top-k generation needs one strict Farey bracket and k index updates, so it replaces a per-k Floor Sum rank search in the frozen phase-cut subproblem. The user-visible and future observer-relevant original history labels are preserved in the source sweep. Overall bit complexity and integration with the full Farey risk compiler remain the concrete next work.
