# PREFIX-1051 — Critical-radius polynomial tail and complete upper spectral band

Date: 2026-11-24 Asia/Shanghai. Parent PREFIX-1050. Classification: AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_CHECKED / NOT_REVIEWED.

## Scope and result

Inherit frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json, Stage46 W=J12−6I12, incoming −e1, bidirectional exclusion on Link {0,e1}, exactly one outgoing negative step, and native X6 Cell, terminal port, grade, signed branch order, multiplicity and provenance. The proof concerns the inherited auxiliary six-phase scalar observer only; NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION. No new native trajectory, classical comparison, phase or pi calculation. Exact integer/rational arithmetic below checks an analytic certificate of that inherited model.

Primary immutable sources:
- PREFIX-1050 c8cec7e6f23cbfb1b1ab8730f95ae5bb3f02a552:research_notes/portable_direct/2026-11-24_r6_prefix1050_shifted_companion_near_critical_band.md (recurrence, contrast, branch match and [16.1,36) positivity).
- PREFIX-1050 b20f0626de7a289010eccdc89f34adb8633fc5d0:research_notes/portable_direct/PREFIX1050_R6_SHIFTED_COMPANION_FIXED_POINT_CHECK.py (P and V).
- PREFIX-1040 5211ee897e8e26fede70cde758df683e8f294aad:research_notes/portable_direct/2026-11-23_r6_prefix1040_narrow_band_modulus_positivity.md (continuity and |y−16|<=10^-9 implies g(y)>49/50).
All previous scalar premises remain in force.

Theorem: for the inherited positive edge coefficient c and x=36−y,
    16 <= y < 36 => g(y)>251 c (36−y)^(5/2)>0.
Combining the prior local critical certificate also gives strict positivity throughout [16−10^-9,36). The upper regular interval (16,36) is now entirely certified, with no omitted gap. g(36)=0.

## 1. Polynomial rather than geometric tail at the exact singular radius

With the same b_0=1 and b_i=0 for i<0, set r=20, c_n=20^n b_n, v_n=(c_n,c_{n−1},...,c_{n−4})^T. Use the inherited exact recurrence v_n=E(n)v_{n−1}/D(n), D(n)=−P_0(n+3/2), E first row (20^k P_k(n+3/2−k)) for k=1,...,5 and subdiagonal D(n). All six P polynomials and the exact rational V are printed in the attached checker. As in PREFIX-1050 define S=diag((20/16)^4,...,1) V diag(1,1/8,1/64,1,1) and B(n)=S^{-1}E(n)S. The dominant limiting eigenvalue equals 1, so a uniform geometric contraction cannot hold at r=20.

New bound, valid for every real n>=3000:
    ||B(n)/D(n)||_infty <= 1−9/(4n).

Proof: substitute n=3000+z. The checker verifies positivity of all coefficients of D and of (4n−9)D, and each of the 35 exact inequalities
    [z^k] (4n−9)D(n) >= sum_j |[z^k] 4n B_ij(n)|,
    i=1,...,5, k=0,...,6.
The polynomial triangle inequality at z>=0 gives the norm bound after division by 4n D(n)>0. This covers the unbounded index domain. It exploits the first-order decay missed by a constant geometric majorant. The dominant diagonal entry of the transformed first-order coefficient is −5/2, consistent with the chosen exponent 9/4; that observation is explanatory, not needed in the certificate.

Let J=2999. Convexity of t^(9/4) on [0,1] gives 1−9/(4n) <= ((n−1)/n)^(9/4), hence
    ||S^{-1}v_n||_infty <= (J/n)^(9/4)||S^{-1}v_J||_infty, n>J.
In particular, H=||row_1(S)||_1 times any upper bound for ||S^{-1}v_J||_infty gives |c_n|<=H(J/n)^(9/4). Unlike the prior geometric estimate at r<20, this implies absolute uniform convergence of BOTH the scaled series and its first derivative on [0,20]. For sums over integers n>J, comparison with integrals of decreasing powers yields
    sum |c_n| <= (4/5) H J,
    sum n|c_n| <= 4 H J^2.
This remains valid at the singular radius without claiming analytic continuation across it.

## 2. Fixed-point residual bound with terminal transformed state

Compute a_n=floor(sum_{k=1}^5 E_{1k}(n)a_{n−k}/D(n)), a_0=M=10^800 and a_i=0 for negative i. Write w_n=(a_n,...,a_{n−4})^T. The error vector Mv_n−w_n satisfies the exact companion recurrence with first-component additive residual in [0,1). Thus transformed error norm <= e_n, with e_0=0 and
    e_n=ceil(||B(n)/D(n)||_infty e_{n−1})+ceil(||S^{-1}||_infty).
Checker evaluates the polynomial numerators and denominator using a common exact integer denominator; the ceiling uses integer arithmetic. It establishes ||S||_infty=3 and ||S^{-1}||_infty<60000. For 0<=n<=J, |c_n−a_n/M|<=3e_n/M, max 3e_n<10^600.

Important improvement: retain S^{-1}w_J itself, not just a bound on the untransformed magnitude multiplied by a condition number. The sharper certified H is
    H=||row_1(S)||_1 (||S^{-1}w_J||_infty+e_J)/M <162/10^10.
This is observer-specific error control with all five recurrence coordinates retained. No native state compression is asserted.

## 3. Full continuous gap certificate

The inherited normalized contrast for x in (0,20) is
    G(x)=5g(36−x)/(c x^(5/2))=sum_{n>=0} c_n (x/20)^n F_n(x),
    F_n(x)=(36−x)(538−12x)−4(36−x)^2 n
       −12(47−x)(30/(n+5/2)−x/(n+7/2)).
The inherited analytic branch equality holds on 0<x<20 by PREFIX-1048/1050. On [199/10,20], the coefficient bound improves to |F_n(x)|<=30000+1040n: the constant terms are bounded as in PREFIX-1050 and 4(36−x)^2<=4(161/10)^2<1040. The bound and Section 1 justify uniform convergence up to x=20. PREFIX-1040 continuity of g near y=16 identifies the endpoint value by the one-sided limit.

Take K=400. Define Q(t)=sum_{n=0}^K (a_n/M)t^n F_n(20t), degree <=402. Its exact Bernstein coefficients beta_k=sum_{j=0}^k p_j binom(k,j)/binom(402,j), where p_j are its monomial coefficients, all exceed 2256. Therefore Q(t)>2256 throughout [0,1]. The checker verifies two bounds:
    Rerr=sum_{n=0}^K (30000+1040n)3e_n/M <1,
    T=sum_{n=K+1}^J (30000+1040n)(|a_n|+3e_n)/M
        +30000(4/5)HJ+1040(4HJ^2) <998.
Here T includes the full infinite tail, not just the computed coefficients. It follows on [199/10,20] that G(x)>2256−998−1=1257. Thus g(y)>(1257/5)c(36−y)^(5/2)>251c(36−y)^(5/2) for 16<=y<=16.1. PREFIX-1050 gives the stronger constant 578 on [16.1,36); together they prove the theorem. PREFIX-1040 separately supplies the small extension below 16.

## 4. Reproduction and evidence

Executed standalone Python checker (SymPy and standard-library Fraction), immutable source:
3e6750ea4c429cab0758e35b6292d2bcb59a1da0:research_notes/portable_direct/PREFIX1051_R6_CRITICAL_TAIL_CHECK.py
Git blob 071a2baf2ad18ad4130e9df9dc66f935dfd0a535, identical to executed local file and to full remote readback. SHA256 9a8ff2754823a4d4c4ce699c2c3e376335ac881292fab381b2be097f3e5f020f. Actual output:
    N 3000 H 1.6173221665366614e-08 tail 997.2405906753423 Bernstein min 2256.2460415370383
    PREFIX1051_CRITICAL_TAIL_CERTIFICATE_PASSED
The decimals are diagnostics only; all acceptance assertions are exact. 403 Bernstein coefficients, 3000 finite coefficients including b_0, 35 half-line inequalities plus positivity checks, exact directed rounding and infinite tail. Earlier exploratory uniform F_n bound 30000+5200n was insufficient near the critical radius; the local bound and terminal transformed state remove that obstacle. No new classical reference or physical model execution.

## 5. Control and next scientific question

Current canonical entry files, worldview, project protocols and frozen P000 V5 read. Original session registration r6-20261123-2358-session-start-own-v1 SUCCEEDED, historical EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322. Current private session possession not established by its public receipt. Previous owner read r6-20261124-0851-leased-observe-v1 SUCCEEDED: empty LEASED filter as of 2026-11-24T00:51:49.963791Z; current read r6-20261124-0950-leased-observe-v1 RUNNING / NATIVE_RUNNER at last check. No CLAIM, PROGRESS, Result, review or protected Activity mutation. This independent portable contribution leaves the Activity association pending.

Do not repeat the upper band proof. Next target (4,16): obtain left-hand critical connection data (including singular mode and smooth background, with explicit residual bounds) from the actual scalar kernel, then use a local Frobenius or interval certificate with branch matching on that interval. The upper series and its first derivative converge at x=20 but do not identify the continuation to the other side of the singularity. The native signed BRC joint-observer correspondence and mother B_fix,odd(32) in {19,20} remain open.