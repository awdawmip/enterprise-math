# R633 research handoff — full-jet collision and exact background-reference repair

Date 2026-11-08. Author-side / unreviewed. Prior R632 a9dbf2905918c97935cefbaa184d03e0b146c0b9; frozen R462 18783e01e3646c72b7aab3b16d3f565e83e6446f; original K blob 7fa7a762f758b30c6090468ac43487daa34abad8.

Theorem A: Factor P_j=t^(2j−2)U_j and M_j=t^(2j−1)V_j. Select per-axis gains A+=t^a V_j, A−=t^(a−1)U_j and constant H=−t^(a+2j−2)U_jV_j. Both complete response polynomials equal zero, for all 720 direction permutations, any a≥1 and h≥0. All gain leading coefficients mod 5 nonzero. No t-jet extension or repeat with the same sign-dependent gains restores unified orientation observability.

Theorem B: Add one exact matched-background reference R_x=H_x(k0) per axis. Then Yplus−R=Aplus P_j has modular t-order a+2j−2, so d=a+8 yields all 720 permutations; this precision is uniform sharp for the augmented protocol. Second gain may vary arbitrarily.

Verification: python R633_VERIFY.py generates R633_EVIDENCE.json; marker R633_FULL_JET_GAIN_DROP_COLLAPSE_AND_REFERENCE_REPAIR_PASS. 26,616 finite exact instance checks; analytic identities supply universal scope. No original X6 field operation, heartbeat dynamics or mathematical admission is asserted.

Next research: inspect Source's native X6 joint-field operators for same-background reference, simultaneous probe or source-coordinate discrimination; find an operation-level admissible witness or rule excluding this exact obstruction. Preserve provenance, branch-grade, path, multiplicity, joint state and time typing.