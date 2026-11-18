# S23/AV continuation: after exact second inversion window

Frozen scientific pin: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Prior: PR #1777 @ `aaf8ea15f257ae5af8bb14421f9dc38008397caa`.

**New mathematical frontier.** All true threshold orders for each integer `7365717<=H<=9820785` are recovered from the old lex integer key via exactly `T(H-7365717)` disjoint four-point rotations plus `T(H-4910648)-2T(H-7365717)` disjoint pair swaps. This yields O(1) correction after old exact rank/select oracle. Read `PROOF.md`, `VERIFY.py` and `RUN_EVIDENCE.txt` in this directory.

**Next concrete problem.** At `H=9820786`, add `q4=u+4w` inversion and compute the corrected ordering of the finite integer-key fibers. By `H=9821296=2|u+2w|_1`, also include the first doubled-`q2` inversion; inspect overlaps and derive new rank/select corrections, testing a small scaled unimodular model. Independently complete the full changed-gap **prefix occupancy** at `H=2455579` to decide the capacity `N(H)` question. The capacity and ordering objectives have different evidence obligations.

**Control.** This is author-side mathematical evidence only. A native research session attempt returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE` with `operation_sent=false`; native active Owner and CLAIM were not verified. Independent review remains pending. Do not copy old session credentials, invent a new native Researcher-ID or treat GitHub write rights as Task claim authority.
