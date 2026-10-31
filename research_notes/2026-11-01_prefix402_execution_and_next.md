# PREFIX-402 | Actual execution, exact certificate, provenance, and next research unit

Observed 2026-11-01 (Asia/Shanghai). Author-side mathematical status: EXACT_SYMBOLIC_AND_RATIONAL_VERIFIED / UNREVIEWED / NOT_ADMITTED. All facts here refer to the external auxiliary static complex three-amplitude/five-Port inverse model, with I1 exactly 1.

## Source pins (held fixed for this research)

- GLOBAL_KNOWLEDGE_V1 canonical main: c93fe73d7cc7391e8c27c5c51e0552ecfd611b2a. Verified original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc against startup projection, read ACTIVE worldview and relevant math/BRC/code policies.
- Enterprise Math source main: ace20a3785eb79ba4f7f4fa7299871fffc07a96e; exact PREFIX-401 antecedent at research_notes/2026-11-01_prefix401_four_annuli_72_candidate_feasibility.md, blob 6fce4f484aec84724eea9600dbadb11ba96c49f7.
- GitHub connected user login: awdawmip; ordinary repository write permission present. Research identity is not inferred from that login.

## Real program execution

Python 3.13.5; SymPy 1.14.0. Executed (local files saved in complete research evidence archive):

    python verify_prefix402.py > exact_output.json
    python independent_fraction_check.py > independent_output.log

Results:
    PASS_PREFIX402_TWO_NOISY_U_OBSERVERS_SHARP_SQRT_AND_BRANCH_SEPARATION
    PASS_PREFIX402_INDEPENDENT_PURE_FRACTION_ORIGINAL_PORT_WITNESS_AND_GAP
    PASS_PREFIX402_FALSE_NEGATIVE_WITNESS_WITHIN_ALL_ERROR_LIMITS

The first program derives B=A*A3^-1 from the original five complex rows; checks both nominal four-annulus identities, both distinct nominal complex sources, the coherent observer, all decisive rational bounds and the frozen-u false-negative witness. The second uses only Fraction and independent rational complex-pair arithmetic. The third directly confirms the constructed witness's I4/I5 shifts are within 1/10.

Exact output, no floating comparison in load-bearing inequalities:

    epsilon_I2_Cu=1/100000000, rho_u=1/5000
    additional_I4<1/40, additional_I5<1/50
    DT=4347/640
    S_squared_lower=51693638631/409600 (>355²)
    DS=3776031769/296140800
    H_Cv_true=690021310849/3709360947200
    nominal_Cv_gap=90528/37577
    joint_observed_branch_separation=68790132351/1854680473600 (>0)
    frozen_u_h=1/10000
    frozen_u_I4_actual=110122857795101/793800000000
    I4_actual_minus_I4(u0,1+i)=720029/200000000
    I4_actual_minus_I4(u0,1-i)=-262384879391/4200000000
    I5_actual_minus_I5(u0,1+i)=14720709/6400000000

Local executed source SHA-256:
    verify_prefix402.py = ffec3684ef03d1d74a00eeb1b1f4088159593439a4f1bcf944f156af82ba5196
    independent_fraction_check.py = 5c4d03c321a788e43a7cde95d0ba62a0e1465f8967e8ed683b021a35f06c112d

The exact local package contains long Chinese proof, both executed checkers, JSON result, execution log. Archive SHA-256: ae07b6dbd655ae08e208f362a6fe23415fbc6995cbf3109889f579868b471cb5. Complete archive bytes are a local artifact, not claimed as uploaded to GitHub or Google Drive.

## Owner/authority and submission semantics

Native Enterprise Math MCP v0.6.11 status read: research_authority_granted=false; source control state CODE_REVIEW_REQUIRED, error UPSTREAM_CODE_REVIEW_REQUIRED; active job quota 5/5. Read-only control owner/task listing returned CONTROL_QUOTA. Therefore no live owner list was successfully obtained and no new CLAIM, native activity/Result, Review or mathematical admission was obtained. Direct GitHub research_notes publication is source material preservation only. Source publication must be read back at the actual commit before it can be reported complete.

## Immediate scientific continuation

PREFIX-403: Build an actual executable **two-way** feasibility algorithm for the parametric annulus family: u lies in the intersection of I2/Cu annuli and v lies in four u-dependent annuli. Return an algebraic (u,v) witness for YES and an exact real-closed-field exclusion certificate for NO; preserve both conjugate-u possibilities, sign(S) and phase provenance. Check tangent/singular fibers and the algorithm's finite complexity. The earlier PREFIX-401 72-candidate result works only with u fixed; PREFIX-402 exhibits a strict false-negative if that hypothesis is dropped.
