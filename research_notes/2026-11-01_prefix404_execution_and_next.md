# PREFIX-404｜Verification, source pin, permissions and continuation

Date: 2026-11-01. Status: **AUTHOR_SIDE_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING**.

**Pinned input (one control phase):** GLOBAL_KNOWLEDGE_V1 main@75711f73714b2cebf8a177ec4ec53912e23acffc; Enterprise Math main@ac48238d40c28c9ad139faa5b0e11cb7defdd8f9. Canonical bootstrap/manual, P000, ACTIVE worldview, joint-observer preservation and Portable Research protocol were read. Parent is PREFIX-403 (author-side, not independently admitted). BRC: REUSE_APPLIED for source-fiber fidelity, no typed BRC execution.

**Exact matrix:** five original Ports A, normalized W=(1,u,v); I1=1 exact. The dual-slice theorem requires **I2 and Cu exact rational**; the four other readings are rational finite closed intervals. The full-noisy theorem is a two-real-parameter conditional finite-fiber reduction, not a completed all-noisy numeric solver.

**Execution environment:** Python 3.13.5; SymPy 1.14.0; independent check uses Python standard-library Fraction only. Both scripts were executed locally, not merely parsed.

Primary solver output:
    PASS dual rational/noisy YES 4 candidates 7 circles
    PASS dual rational/noisy NO 28 candidates 6 circles
    PASS dual two-u-branches YES 1 candidates 4 circles
    PASS dual two-u-branches NO 22 candidates 4 circles
    PASS_PREFIX404_DUAL_144_CANDIDATES_EXACT_U_NOISY_V

Independent original A matrix and nonzero-width six-band check:
    matrix_identity_basis_checked = 3
    u = 1/2000 + i/2000; v = 1/2500 - i/4000
    I2 = 1/2000000
    Cu = 2002001/2000000
    I3 = 89/400000000
    Cv = 400320089/400000000
    I4 = 2653691681/100000000
    I5 = 554863033/50000000
    all-noisy YES bands = (I2,I3 in [0,1/1000000], Cu,Cv in [99/100,101/100], I4 in [26,27], I5 in [10,12])
    all-noisy NO with I4 in [0,1] and same five other bands:
        reverse-triangle strict amplitude lower > 624/125 > 1
    PASS_PREFIX404_INDEPENDENT_FRACTION_ALL_NOISY_YES_NO_AND_ORIGINAL_MATRIX

Local sha256 of actually executed dual solver:
    50604f6e63ba7568d980b35edab9dbb2bfe6e879b9c5284049cef35ef548c8cc
Local sha256 of actually executed independent checker:
    c3fcf97fe82888d55b7d112a28629c2b53bc15f698cd068647e37919daf7471b

**Limits:** Universal finite candidate completeness is proven in the research note, not inferred from finite tests. The SymPy runtime raises if it cannot resolve an exact algebraic sign, rather than returning NO. Universal real-algebraic comparator exists as mathematical specification; not all possible input expressions have been operationally tested. No all-noisy two-parameter CAD was executed. Author-side checks are not independent scientific review or formal verification.

**Authority:** GitHub authenticated as awdawmip with repository push access; native Enterprise Math status version 0.6.11 reports research_authority_granted=false, executor_binding_configured=false and 5/5 active-job quota. A scoped owner/task inventory attempt returned CONTROL_QUOTA. The active Task owner was not verified; no Source-native CLAIM, run, freeze, Result or review was created by this work. Ordinary GitHub research-note publication is only durable author-side material.

**Next PREFIX-405:** construct a complete executable two-real-parameter sign decomposition (e.g. CAD or certified algebraic cell decomposition) for all parameterized 72 candidates, handling coincident/tangent/zero-radius circles, and replayable YES/NO certificates; do not silently collapse distinct source fibers or claim native X6 mapping.
