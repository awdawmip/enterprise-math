# CBRC F7 r486 — exact B26 finite-box minimax via static quarter-grid certificate

Date: 2026-11-22 (Asia/Taipei). Scientific contributor: continuing RESEARCH_DRIVER logical lane EM-DVR-DEBB5E. The original F7 researcher EM-CBRCF7-83A1D4, frozen RR-AA38973D56330E59D315 and all original Source, review and Task statuses retain their historical scopes.

## Original problem and theorem

A globally admissible real function q: Z² → R must satisfy q(-x,y)=q(x,y), q(0,0)=0, q(x,0)=1 for x≠0, q(x,y)≥1/2 for y≠0, and q(2,1)=q(-1,-1)=1/2. Given integers a,b,c,d, put

    k=a-2b-c+2d,
    D_q(a,b,c,d)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d),
    e_B=inf_q max_{a,b,c,d∈[-B,B]∩Z}|D_q(a,b,c,d)|.

**Theorem r486. For every integer 1≤B≤26, e_B=1/2.**

## Exact lower bound

For every B≥1, input (a,b,c,d)=(1,-1,0,0) gives k=3, and

    D_q=q(4,2)+q(-3,-3)-q(1,-1)-q(0,0) ≥ 1/2,

because q(1,-1)=q(-1,-1)=1/2 by evenness and the fixed mark, q(4,2), q(-3,-3) are each ≥1/2, and q(0,0)=0.

## Explicit global upper-bound function

Use Q=4q with Q(0,0)=0, Q(x,0)=4 for x≠0 and Q(±2,1)=Q(±1,-1)=2. All other off-axis keys are (|x|,y), and Q=2 outside the finite indexed set below.

For B=26 define R={-52,...,52} and the integer interval T_r=[2r-min(26,r+26),2r-max(-26,r-26)]. Build a deterministic insertion-ordered index: for r in increasing R, for u in increasing R strictly greater than r, iterate v over increasing T_r followed by increasing T_u, and for each v visit rr=r then rr=u; append the first occurrence of (|2rr-v|,rr-v) whenever the second coordinate is nonzero and the key is neither (2,1) nor (1,-1). The index contains exactly **14,064** distinct free keys.

The values Q at those keys are the 14,064 unsigned bytes in the fixed Base85/zlib artifact

    research_artifacts/F7_R486_B26_Exact_Quarter_Witness_20261122.b85

with raw byte **SHA256 b43ed773ba1f8b246c3a53e619e7633cc71608800b4ca4fa8ef4d447adfbed6a**. Exact frequencies are Q=2 at 9,032 keys, Q=3 at 4,040 keys, Q=4 at 992 keys. This definition makes q global, even in x, and enforces all axis, origin, marked and off-axis lower-bound constraints without an extrapolation assumption.

Independent Python standard-library checker:

    research_checks/CBRC_F7_R486_B26_EXACT_QUARTER_CERT_20261122.py

The checker verifies the raw SHA256 and key-ordering, then exhaustively evaluates every **53^4=7,890,481** original quadruple by exact integer arithmetic; it was executed with exit status 0. The complete histogram for 4D_q is:

| 4D_q | Exact count |
| ---: | ---: |
| -2 | 176,686 |
| -1 | 1,697,852 |
| 0 | 3,822,003 |
| +1 | 1,957,706 |
| +2 | 236,234 |

Thus max|4D_q|=2 and 412,920 inputs attain that bound. The constructed globally admissible q has E_26(q)=1/2. With the matching lower bound, e_26=1/2. Restriction of the *same global function* to smaller boxes proves e_B=1/2 for each 1≤B≤26.

## Construction provenance, independent proof and limits

The prior r485 B25 exact quarter-grid witness was extended with Q=2 on B26 new keys, producing 9,456 original-input violations of |4D|≤2 and maximum |4D|=4. Sparse numerical cutting-plane/L1 optimization found an integral-quarter candidate after 14 rounds. Relative to the prior B25 table it modifies 722 old indexed keys: 702 increase by one Q unit, 19 decrease by one Q unit, and one increases by two Q units (total old-key |ΔQ|=723). The 1,054 newly indexed B26 keys remain Q=2. This is *one feasible repair*, not a proof of minimum repair cardinality, L1 cost or algorithmic optimality.

The fixed static certificate, separately reconstructed index and independently executed exhaustive integer checker prove the mathematical statement; numerical LP is discovery only. Infinite-domain optimum remains open at 1/2≤e_infinity≤4/7. Next finite-box question is B27 exact feasibility or a genuine infeasibility proof.

New proved subunit: one. No new Native Review, Result admission, formal Task completion, mother Objective completion, CLAIM/owner change, P000 revision or schedule change is asserted. Original Source/Activity linkage and frozen Result Issue #2874 remain distinct operational work.

Predecessor: https://github.com/awdawmip/enterprise-math/blob/ac7cae4327d2a1dec7f58cd0aa3b6bb8663cd171/research_notes/driver/2026-11-22_f7_r485_B25_exact_quarter_minimax.md
