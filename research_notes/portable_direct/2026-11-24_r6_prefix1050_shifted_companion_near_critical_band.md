# PREFIX-1050 — Shifted companion norm and fixed-point residual certificate near the upper critical point

Date 2026-11-24 Asia/Shanghai. Parent PREFIX-1049. Status AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_CHECKED / NOT_REVIEWED.

## Scope and result

Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Inherit the Stage46 W=J12−6I12, incoming −e1, both directions excluded on Link {0,e1}, exactly one outgoing negative step. Retain native X6 Cell, terminal port, grade, signed branch order, multiplicity and provenance. This certificate concerns only the existing auxiliary scalar observer: NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION. No new native trajectory, classical reference computation, phase evaluation or pi computation. Rational operations verify inequalities of the inherited analytic certificate only.

Primary immutable source f3fa48009350bf4441eeeec05c2c8b137f128396:research_notes/portable_direct/2026-11-24_r6_prefix1049_weighted_companion_bernstein_upper_band.md, including the frozen ODE, contrast identity, and the branch identification from PREFIX-1048. Use the same positive edge coefficient c and x=36−y. The new theorem is

    161/10 <= y < 36  =>  g(y) > 578 c (36−y)^(5/2) > 0.

At y=36 the density contrast vanishes. The interval length grows from 16 to 199/10. The remaining gap to y=16 is 1/10 before using the prior narrow critical neighborhood.

## 1. Exact shifted polynomial norm certificate

Use the same P_0,...,P_5, D(n)=−P_0(n+3/2), and b_0=1 as in PREFIX-1049, and replace the scaling radius 16 by r=199/10. Let c_n=r^n b_n, with c_n=0 for negative n. Define v_n=(c_n,c_{n−1},...,c_{n−4})^T. Then v_n=E(n)v_{n−1}/D(n) for every integer n>=1, where the first row of E is (r^k P_k(n+3/2−k))_{k=1}^5 and its subdiagonal equals D(n). This includes n<5 by the negative-index convention. D(n) is nonzero at every positive integer.

Let V be the exact rational Jordan-chain matrix in PREFIX-1049 §1 and put
S=diag((r/16)^4,(r/16)^3,(r/16)^2,r/16,1) V diag(1,1/8,1/64,1,1).
Let B(n)=S^{-1}E(n)S. The scaling changes the limiting eigenvalues by r/16; the largest becomes 199/200. Rather than sum separate global matrix norms, shift the polynomial variable: n=5000+z, z>=0. Write
D(5000+z)=sum d_k z^k, B(5000+z)=sum B_k z^k.
The checker verifies d_k>0 and for each row i and each k=0,...,5

    sum_j |(B_k)_{ij}| <= (199/200)d_k.

Consequently for every real n>=5000, the row triangle inequality at z>=0 and division by D(n) prove

    ||S^{-1}E(n)S/D(n)||_infty <= 199/200 = q.

This is an all-index bound, not a finite sample of norms. The checker also verifies ||S||_infty<=3 and ||S^{-1}||_infty<68000.

## 2. Fixed-point residual propagation

Directly storing exact fractions for thousands of coefficients can inflate numerator/denominator length. Here M=10^1500 is a fixed integer scaling, not a claim of native measurement resolution. Compute integers a_n by floor rounding of the exact recurrence for the scaled a values, initialized by a_0=M and a_n=0 for n<0. Let w_n=(a_n,...,a_{n−4})^T. The scaled vector M v_n−w_n obeys the exact companion recurrence with a first-component residual in [0,1), all other components zero. Therefore in the S coordinates its norm is bounded by an integer sequence e_n, initialized at zero, with

    e_n = ceil( ||B(n)||_infty / |D(n)| * e_{n−1} ) + 68000.

For each computed n, ||M v_n−w_n||_infty <= 3e_n, giving |c_n−a_n/M| <= 3e_n/M. No cancellation is assumed in bounding the rounding error: it is propagated under the actual signed joint transition. For n=1,...,4999 the checker uses exact rational row norms and exact integer floor/ceiling. It verifies max 3e_n < 10^1400. The floating outputs are diagnostic displays only, not used in any acceptance inequality.

Put U=max_{4995<=i<=4999} (|a_i|+3e_i)/M and H=204000 U. For every j>=1 the uniform contraction gives |c_{4999+j}|<=H q^j, and hence tail bounds T0=Hq/(1−q), T1=H(4999q/(1−q)+q/(1−q)^2) for the absolute coefficient sum and its n-weighted sum. This proves convergence and differentiability on compact subsets of |x|<r/q=20. The inherited local Frobenius branch agrees near zero; regular ODE uniqueness identifies it on 0<x<20. No matching at the singular point x=20 is asserted here.

## 3. Whole-interval Bernstein certificate

Inherit the exact contrast identity of PREFIX-1049 §3:

    G(x)=5g(36−x)/(c x^(5/2))=sum c_n (x/r)^n F_n(x),
    F_n(x)=(36−x)(538−12x)−4(36−x)^2 n
            −12(47−x)(30/(n+5/2)−x/(n+7/2)).

For 0<=x<=r<20, |F_n(x)|<=30000+5200n, by 36*538+12*47*(12+20*2/7)<30000 and 4*36^2<5200. All termwise operations on this closed interval are justified by the bound in §2.

Use K=400 and the polynomial Q(t)=sum_{n=0}^K (a_n/M) t^n F_n(rt). Write Q(t)=sum_{j=0}^{402} p_j t^j. The code explicitly constructs the three coefficients of F_n(rt) and then the 403 Bernstein coefficients
beta_k=sum_{j=0}^k p_j binom(k,j)/binom(402,j).
For every k the checker proves beta_k>2956, so Q(t)>2956 on [0,1].

The error from replacing the first K+1 exact coefficients is bounded by
Rerr=sum_{n=0}^K (30000+5200n) 3e_n/M <1.
The remaining series has absolute bound
T=sum_{n=K+1}^{4999} (30000+5200n)(|a_n|+3e_n)/M +30000T0+5200T1 <64.
Both comparisons are exact. Thus G(x)>2956−64−1=2891 for all x in [0,r] (at zero use the normalized extension). For 0<x<=r, g(36−x)>(2891/5)c x^(5/2)>578 c x^(5/2). This yields the claimed interval.

## 4. Reproduction, evidence and status

Complete executed checker at b20f0626de7a289010eccdc89f34adb8633fc5d0:research_notes/portable_direct/PREFIX1050_R6_SHIFTED_COMPANION_FIXED_POINT_CHECK.py, Git blob 3ac854816e0a0a7ebfbbbf55ca5baee7892ffff8. Remote readback matched the complete submitted source and its blob matched the executed local file. Python with SymPy; all exact assertions passed. Observed diagnostics: 5000 shifted-bound threshold with ratio .995; max integer error-bound length 526 digits; terminal U approximately 4.3339e−20; K=400 tail approximately 63.4152; smallest Bernstein coefficient approximately 2956.6875; final certified lower bound exceeds 2891. Actual terminal output PREFIX1050_CERTIFICATE_PASSED. The earlier r=19 trial also passed a weaker certificate; no need to repeat it. The checker comment "x=19t" is a stale comment only: actual executable coefficients use F(r) with r=199/10.

Science pin unchanged. Current canonical entry files and project protocols read, prior registration receipt r6-20261123-2358-session-start-own-v1 SUCCEEDED, historical EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322. Current logical-session binding not attested. Previous LEASED observation r6-20261124-0752-leased-observe-v1 SUCCEEDED with empty filtered list as of 2026-11-23T23:52:22Z; latest original r6-20261124-0851-leased-observe-v1 RUNNING / error=null at last read. No protected CLAIM, PROGRESS, Result or Activity mutation in this independent portable note.

## Next

Do not repeat the established x<=19.9 band. Close the remaining gap using a critical-point expansion with explicit remainder or a local continuation certificate, then address (4,16) and (0,4). The auxiliary spectral sign theorem and native signed BRC correspondence remain separate. Mother B_fix,odd(32) in {19,20} remains open.