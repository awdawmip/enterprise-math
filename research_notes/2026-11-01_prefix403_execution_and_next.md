# PREFIX-403 execution, authority, and next exact unit

2026-11-01. Author-side precise computation; UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING. Global snapshot main@1a1e0968079c9ab3e91279990e164d38f31838a5; project initial main@f8cc8141ca4c92b793ec694de7bfff9ad5e3bba6.

Actual Python 3.13.5 / SymPy 1.14.0 execution:
- PASS precise-variable-u repair: YES checked 13 circles 6 v=1+I.
- PASS nominal-u impossible: NO checked 38 circles 4.
- PASS quadratic-v-source: YES checked 1 circles 4.
- PASS quadratic-v-conflict: NO checked 14 circles 4.
- PASS_PREFIX403_144_CANDIDATES_NOISY_U_EXACT_I3_CV.
- ORIGINAL_A_DET=-32+32i.
- ACTUAL_I4=110122857795101/793800000000.
- ACTUAL_I5=1766982026494021/25401600000000.
- I4_FROZEN_BRANCH_DIFFERENCES=720029/200000000, -262384879391/4200000000.
- PASS_PREFIX403_INDEPENDENT_ORIGINAL_A_NOISY_U_AND_TWO_V_BRANCHES.

Main checker supplies finite exact-candidate enumeration with a fail-closed symbolic sign procedure. For an input whose symbolic ordering SymPy cannot resolve, it raises rather than returns an unsupported YES/NO. Mathematical generality is from the 144-candidate proof and standard exact real-algebraic comparison, while actual program checks cover the four displayed cases. These tests do not constitute formal checker verification or independent mathematical review.

BRC REUSE_APPLIED only to source-fiber, full complex u/v, port and observer provenance; no native typed BRC run. Native service v0.6.11 reports research_authority_granted=false / UPSTREAM_CODE_REVIEW_REQUIRED; current owner/control-tasks request returns CONTROL_QUOTA. Connected GitHub user awdawmip has repository push permission, which allows evidence storage but does not grant a CLAIM/Result or mathematical admission. No service session key is saved.

Next PREFIX-404: when I3 and Cv also have positive rational interval widths, replace the discrete v branch by its two-annulus feasible set and implement a general necessary-and-sufficient exact four-real-variable solver, preserving degenerate/tangent fibers, algebraic witnessing and NO certificates. Prefix402's robust sign separation remains a case-specific necessary check, not complete feasibility.
