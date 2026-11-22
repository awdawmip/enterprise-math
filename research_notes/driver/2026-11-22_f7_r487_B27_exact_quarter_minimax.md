# CBRC F7 r487 — exact B27 finite-box minimax via fixed quarter-grid witness

Date: 2026-11-22 (Asia/Taipei). Contributor: established RESEARCH_DRIVER logical lane EM-DVR-DEBB5E. Original F7 researcher EM-CBRCF7-83A1D4, frozen Result RR-AA38973D56330E59D315, original Source evidence and task ownership retain their scope.

## Exact statement

Let q:Z²→R be a globally defined function with q(-x,y)=q(x,y), q(0,0)=0, q(x,0)=1 for all nonzero x, q(x,y)≥1/2 whenever y≠0, and q(2,1)=q(-1,-1)=1/2. For integers a,b,c,d define

    k=a-2b-c+2d,
    D_q(a,b,c,d)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d),
    e_B=inf_q max_{a,b,c,d∈[-B,B]∩Z}|D_q(a,b,c,d)|.

**Theorem r487: e_B=1/2 for every integer 1≤B≤27.** Previous frontier was B≤26.

## Exact lower bound

The original fixed quadruple (a,b,c,d)=(1,-1,0,0), with k=3, gives

    D_q=q(4,2)+q(-3,-3)-q(1,-1)-q(0,0)≥1/2

for every admissible q, because q(1,-1)=q(-1,-1)=1/2 and the other two off-axis terms are each at least 1/2.

## Global explicit upper-bound witness

Define Q=4q, Q(0,0)=0, Q(x,0)=4 for x≠0, and Q(±2,1)=Q(±1,-1)=2. For other off-axis keys (|x|,y), take Q from the fixed table below when indexed and Q=2 otherwise.

With B=27, let R={-54,...,54} and integer intervals

    T_r=[2r-min(27,r+27),2r-max(-27,r-27)].

Construct an insertion-ordered index of off-axis keys by increasing r∈R; for each r increasing u>r in R; increasing v in T_r followed by increasing v in T_u; for each v visit rr=r then rr=u; insert the first occurrence of (|2rr-v|,rr-v) whose second coordinate is nonzero and key is not one of the two fixed marked keys. This gives exactly **15,158** free keys. Their Q values are the corresponding raw bytes in

    research_artifacts/F7_R487_B27_Exact_Quarter_Witness_20261122.b85

Base85/zlib encoding of 15,158 raw Q bytes, SHA256

    95543262a02565ba87b8f88c44d4824683db4e99ffbe7b121759dc5624e71fd9

Their exact value counts are Q=2: 9,541; Q=3: 4,439; Q=4: 1,178. In particular the constructed function is globally admissible, even in x, and satisfies the marks, axis data and off-axis floor.

The independent Python standard-library checker

    research_checks/CBRC_F7_R487_B27_EXACT_QUARTER_CERT_20261122.py

reconstructs the index, verifies raw SHA256/frequencies and exhaustively computes every original integer-input tuple with a,b,c,d∈[-27,27]. It was separately executed and returned status 0. For the **55⁴=9,150,625** original inputs the *complete exact histogram* of 4D_q is:

| 4D_q | Count |
| ---: | ---: |
| -2 | 199,494 |
| -1 | 1,938,934 |
| 0 | 4,413,859 |
| +1 | 2,315,628 |
| +2 | 282,710 |

Thus max|4D_q|=2 with 482,204 tight inputs. Hence E_27(q)=1/2 and the universal lower bound yields e_27=1/2; the same global witness establishes all B≤27 by restriction.

## Mathematical discovery and evidence scope

Extend the immutable r486 B26 table with Q=2 on 1,094 new B27 keys; the extension produces 17,346 original-input violations (maximum |4D|=4). Constraint-generation LP exploration reaches fractional candidates whose naive integer rounding still violates the original inequalities. Rechecking exact quarter-unit residuals and adding the missing full-input constraints eventually produces an *integral quarter-grid* LP feasible solution. The final candidate modifies exactly **823 old B26 indexed keys**, 797 Q values increased by one and 26 decreased by one, and all 1,094 newly indexed keys stay at Q=2. The operation is not proven to minimize changes or total repair cost. Its static fixed bytes plus the independently executed original-input all-integer checker, not numerical solver status or rounding, certify the theorem.

The infinite-domain minimax remains open with 1/2≤e_infinity≤4/7; next finite-box frontier is B28 exact feasibility or a rigorous obstruction. r487 is one new proved bounded mathematical subunit. Original F7 RR has no new Native Review/Result admission, no formal Task/mother Objective completion, and no owner/CLAIM/P000/schedule change. See original integrity/first-review budget Issue https://github.com/awdawmip/enterprise-math/issues/2874.

Predecessor r486: https://github.com/awdawmip/enterprise-math/blob/ab1e4e33edb3b56296613be1f93bd3056f91be14/research_notes/driver/2026-11-22_f7_r486_B26_exact_quarter_minimax.md
