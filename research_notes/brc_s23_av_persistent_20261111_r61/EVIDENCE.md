# R61 execution record — 2026-11-11

Author-side local run: `python CHECK_R61.py`, Python integer modular arithmetic, no floats. The version in this directory outputs the machine certificate to stdout. The run's local script also saved `R61_CERTIFICATE.json` and its raw stdout `R61_LOG.txt`; the remote machine certificate is the exact generated numerical result.

- 225 rational parameter cases (m=1,2,3,5,8; H=1,2,4,8,17; 9 seeded tests per pair).
- 3,375 persistent roots, 3,150 insert/delete updates including branches from older roots, 6,300 paired current/root oracle comparisons, 1,575 retrospective root comparisons, 900 immutable AVL height/size/order/max checks.
- S23/AV: each exact frozen rational endpoint, m=128,H=225, 21 version roots, 20 edits, 126 three-label queries against an independent direct scan; node visits 5574 and 5539 respectively; final tree height 9.
- Exact finite interval order certificate: 353 anchored indices, 704 distinct nonzero differences, least strict integer slack 1538749354821431426740.
- Two parameter values inside one frozen interval produce different history labels at source age 10^24. Also 99 exact time-translation invariance checks including offsets of size 10^80.

The independently computed source oracle scans every source timestamp and classifies it from raw phase, without calling the AVL query. These finite tests support the implementation's tested scope. The O(log n) theorem follows from persistent AVL path copying and augmented range-query arguments; no formal Lean or independent reviewer certification was performed.

Scientific input is frozen at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. The periodic rational endpoint tests are separate from the exact interval certificate and the arbitrary-long-age counterexample. Output verification and project review retain their own authority.
