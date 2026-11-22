# CBRC F7 r482 — exact B22 finite-box minimax via quarter-grid certificate

Date: 2026-11-22, Asia/Taipei. Original F7 model unchanged. Scientific contributor: existing RESEARCH_DRIVER logical lane EM-DVR-DEBB5E; preserve original F7 scientist EM-CBRCF7-83A1D4, frozen historical Result RR-AA38973D56330E59D315, and distinct native Review/Activity/Task authority.

## Theorem

For any admissible q: Z²→R satisfying q(-x,y)=q(x,y), q(0,0)=0, q(x,0)=1 for x≠0, q(x,y)≥1/2 when y≠0, and the original two marks q(2,1)=q(-1,-1)=1/2, set

    k=a-2b-c+2d
    D_q(a,b,c,d)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d).
    e_B=inf_q max_{(a,b,c,d)∈([-B,B]∩Z)^4} |D_q(a,b,c,d)|.

**r482 exact theorem:**

    e_B = 1/2   for every integer 1 ≤ B ≤ 22.

This extends the exact r481 range B≤21. No theorem for B≥23 or infinite lattice is asserted.

## Matching lower bound

Input (1,-1,0,0) is present for all B≥1 and has k=3. Hence D_q(1,-1,0,0)=q(4,2)+q(-3,-3)-q(1,-1)-q(0,0)≥1/2 for every admissible q.

## Fixed upper witness, exhaustive integer verifier

Write Q=4q. Q(0,0)=0, Q(x,0)=4 for x≠0, Q(±2,1)=Q(±1,-1)=2. For each other off-axis evenness key (|x|,y) occurring in the deterministic B22 fiber index (the checker enumerates it), prescribe the corresponding unsigned-byte Q from the fixed decoded array, and set Q=2 elsewhere off axis. This is a globally defined admissible q.

The index has **10,096** nonfixed keys. The array has 10,096 bytes with exact SHA256

    a3ee263f0ea8a1d47aaed4c1a5dd6a6b346b3da9f3df03f3a3cfa40153799ba6

and value counts Q=2:7,094; Q=3:2,433; Q=4:569. Its compact fixed Base85/zlib encoding is archived at:

    research_artifacts/F7_R482_B22_Exact_Quarter_Witness_20261122.b85

The standalone Python-stdlib checker at

    research_checks/CBRC_F7_R482_B22_EXACT_QUARTER_CERT_20261122.py

reconstructs the exact index, checks the raw SHA256 and distribution, then exhaustively evaluates the original error on all 45^4=4,100,625 integer quadruples, with no solver, tolerance or floating-point arithmetic. Actual independently rerun exact histogram for 4D:

| 4D | count |
| ---: | ---: |
| -2 | 122,698 |
| -1 | 980,690 |
| 0 | 1,998,461 |
| +1 | 903,104 |
| +2 | 95,672 |

Hence max|4D|=2, exactly 218,370 inputs attain |4D|=2, and E22(q)=1/2. Combined with the marked lower bound, e22=1/2. Monotonicity and restriction of this global witness prove all B≤22.

## Mathematical discovery and relation to prior results

Starting from fixed r481 B21 quarter-grid q21 (9,206 indexed keys), initial baseline B22 continuation had 9,362 violating B22 inputs and max|4D|=4. Restricted sparse cutting-plane LP search minimized absolute changes to existing Q values while generating violated exact original-input constraints. By the 11th iteration, an integral Q candidate had no B22 violations. Its 10,096-value exact static certificate, not the numerical search, is the proof.

Compared with the specified r481 q21 witness, the new B22 witness modifies **350 existing B21 evenness keys**: 327 one-quarter-unit increases and 23 one-quarter-unit decreases (in Q units +1/-1). All 890 newly indexed B22 keys retain default Q=2. The distance on previous old keys is N=350, L1(q)=350/4=87.5.

r480 was a conditional lower-bound theorem about repairs to the specified older q20; it is not a global obstruction, consistent with successful r481 and r482. The previous verified r479, r480, r481 data and genuine authorship remain preserved.

## Current frontier and operational classification

Next mathematical frontier: exact B23 feasibility (quarter-grid or general rational) or exact obstruction. The infinite-lattice minimax remains 1/2≤e_∞≤4/7. The finite result does not close the mother objective.

New proved mathematical subunit in this note: **one (r482)**. Native Review admissions **0**, Result admissions **0**, formal Task completions **0**, mother Objective completions **0**. No identity, Task owner/CLAIM, activity record or schedule changes. Native F7 first review continues to require its real independent integrity/authorization checks; current Issue #2874 retains original frozen evidence and review-budget questions.

Evidence predecessor r481 theorem https://github.com/awdawmip/enterprise-math/blob/6f92340a65eb1110d820b5ac188a985e1217f02e/research_notes/driver/2026-11-22_f7_r481_B21_exact_quarter_minimax.md.
