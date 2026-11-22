# CBRC F7 r480 — exact 55-witness B21 repair obstruction for the specified B20 optimum

Date: 2026-11-22 (Asia/Taipei). Scientific contribution: the existing RESEARCH_DRIVER lane EM-DVR-DEBB5E. Preserve original F7 researcher EM-CBRCF7-83A1D4, original frozen Result RR-AA38973D56330E59D315, and every independent Review/Activity/Task authority.

## Original unchanged problem

An admissible q: Z² -> R satisfies q(-x,y)=q(x,y), q(0,0)=0, q(x,0)=1 for x!=0, q(x,y)>=1/2 for y!=0, and q(2,1)=q(-1,-1)=1/2. Set

    k=a-2b-c+2d
    D_q(a,b,c,d)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d)
    E_B(q)=max_{a,b,c,d in [-B,B]∩Z}|D_q(a,b,c,d)|.

Let q20 be the *specific* globally defined rational quarter-grid function of r479, the fixed 8,358-byte B20 certificate, equal to the off-axis baseline q=1/2 outside its finite support. The r479 independent checker establishes E20(q20)=1/2.

Let S20 be the 8,358 nonfixed off-axis evenness classes (|x|,y) in the original B20 fiber index, with coordinates q20 supplied by its fixed vector. An admissible q' has a difference on S20 measured by

    N20(q',q20)=#{p in S20:q'(p)!=q20(p)}
    L20(q',q20)=sum_{p in S20}|q'(p)-q20(p)|.

## Theorem r480 (exact conditional necessity)

**For every real-valued admissible q' with E21(q') <= 1/2:**

    N20(q',q20) >= 55
    L20(q',q20) >= 57/4 = 14.25.

The conclusion is independent of q' values at newly introduced B21 coordinates and does not assume that q' has quarter-grid values. Hence no B21 half-error extension can keep all the r479 B20 indexed values fixed. This is a repair theorem for a *specified B20 optimizer*, not an infeasibility proof for the freely reoptimized B21 problem.

## Exact finite certificate

Write Q20=4q20 and Q'=4q'. Fifty-five fixed quadruples (a,b,c,d) in [-21,21]^4 are encoded as UTF-8 CSV and compressed with zlib/Base85 in the standalone verifier:

    research_checks/CBRC_F7_R480_B21_FROZEN_B20_DISJOINT_REPAIR_20261122.py

Their uncompressed 585-byte CSV SHA256 is:

    91296dd050299efa9237ae671e5e9e3dd5be129717bee840dcc5129fb143c466

Independent exact-integer checks on the fixed r479 q20 show:

- 53 selected inputs have D_Q20=-3 and two inputs have D_Q20=-4, so all 55 violate |D_Q|<=2.
- Every coordinate occurring in these 55 inequalities is either a fixed axis/mark or an existing S20 coordinate; **no new B21 coordinate participates**.
- After combining repeated coordinates and enforcing x-evenness, each witness's mutable-coordinate coefficient is 0, +1, or -1; every witness has at least one nonzero mutable coordinate.
- The 55 mutable supports are **pairwise disjoint**, using 124 distinct S20 keys in total.

These are all finite exact statements, verified by the checker against the original r479 SHA256-bound witness. Example witness (-21,0,-8,0) has D_Q20=-3; the full 55-quadruple certificate is embedded in the checker (fixed compressed bytes with a separate exact CSV digest).

## Proof

For one witness w, write D_{Q'}(w)-D_{Q20}(w) as an integer-coefficient linear combination of the old mutable differences Q'(p)-Q20(p). Because no new coordinate occurs, fixed axis/mark values cancel and every effective coefficient has absolute value <=1. The half-error requirement |D_{Q'}(w)|<=2 therefore gives, by the reverse triangle inequality,

    sum_{p in supp(w)}|Q'(p)-Q20(p)| >= |D_Q20(w)| - 2.

Since each witness's right side is positive, at least one mutable old key in that support must change. The 55 supports are disjoint, proving N20>=55. Summing the same inequalities over disjoint supports yields

    4 L20(q',q20) >= 53*(3-2) + 2*(4-2) = 57,

or L20>=57/4. QED.

## Execution evidence and frontier

The exact checker was executed locally with the original r479 compressed certificate and printed:

    CERTIFIED: 55 disjoint B21 violations on old B20 variables;
    old keys: 124; sum quarter gaps: 57;
    minimum old-coordinate changes: 55;
    minimum old L1(q): 57/4 = 14.25

The certificate checker is independently re-runnable in a normal checkout of awdawmip/enterprise-math with the original r479 witness file. It uses only Python 3 standard library and exact integer arithmetic.

A separate exploratory exhaustive B21 diagnostic of the baseline extension of q20 examined all 43^4=3,418,801 inputs and found 4,994 half-error violations, with |4D| maximum 4. The theorem above relies only on the explicitly fixed 55-witness certificate.

**Remaining frontier:** Find an exact B21 half-error primal with freely modified old/new coordinates or an exact obstruction for every such q. Preserve the finite B20 theorem e_B=1/2 for 1<=B<=20 and the global 1/2<=e_infty<=4/7 bounds. A fixed B20-witness repair cost is not a general B21 lower bound above 1/2.

## Scientific and control classification

New proved scientific subunit: r480 (one). Native Review admitted: 0. Native Result admitted: 0. Formal Task completed: 0. Mother Objective completed: 0. Original F7 authorship, historical Result/Review, current Task owner/CLAIM, contribution exposure and scheduled cadence remain untouched.

Predecessor r479 theorem: research_notes/driver/2026-11-22_f7_r479_B20_exact_quarter_minimax.md @ 557f9b056776d92f6732868b37ee98dd3c5867de.
Original r479 witness: research_artifacts/F7_R479_B20_Exact_Quarter_Witness_20261122.b85 @ 87e442f08f2a48701db179a8ab2066a182ac5aab.
