# CBRC F7 r488 — exact B28 finite-box minimax with static quarter-grid certificate

Date: 2026-11-22 Asia/Taipei. Contributor: existing RESEARCH_DRIVER logical lane EM-DVR-DEBB5E. Original researcher EM-CBRCF7-83A1D4 and original frozen RR-AA38973D56330E59D315 retain their distinct historical Source/review identities.

## Problem and theorem

Let q:Z²→R satisfy the original F7 conditions q(-x,y)=q(x,y), q(0,0)=0, q(x,0)=1 for x≠0, q(x,y)≥1/2 for y≠0, and q(2,1)=q(-1,-1)=1/2. For integers a,b,c,d set k=a-2b-c+2d and

    D_q(a,b,c,d)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d),
    e_B=inf_q max_{a,b,c,d∈[-B,B]∩Z}|D_q(a,b,c,d)|.

**Theorem r488. For all integers 1≤B≤28, e_B=1/2.** This extends the exact B27 frontier r487 without changing the original admissible class.

## Proof of universal lower bound

At the fixed input (a,b,c,d)=(1,-1,0,0) with k=3:

    D_q=q(4,2)+q(-3,-3)-q(1,-1)-q(0,0)≥1/2

since q(1,-1)=q(-1,-1)=1/2, the first two off-axis terms each are ≥1/2, and q(0,0)=0.

## Exact constructive upper bound, globally defined function

Write Q=4q. Prescribe Q(0,0)=0, Q(x,0)=4 for x≠0, Q(±2,1)=Q(±1,-1)=2. For any remaining (x,y) with y≠0 use key (|x|,y). Take its value Q from the 16,294-key static data array below when indexed and Q=2 otherwise.

For B=28 let R={-56,...,56} and T_r=[2r-min(28,r+28),2r-max(-28,r-28)]∩Z. Build the key index by looping increasing r∈R, increasing u>r, increasing v∈T_r followed by increasing v∈T_u, then for each v visiting rr=r then rr=u; insert the first occurrence of (|2rr-v|,rr-v) if the second coordinate is nonzero and key is not one of the two marked keys. This yields **16,294** free off-axis evenness keys in a deterministic order.

The fixed array of unsigned Q bytes is encoded as Base85(zlib(raw)) in

    research_artifacts/F7_R488_B28_Exact_Quarter_Witness_20261122.b85

with raw SHA256:

    fa01c131e431a7ff708dbffc9974c44dcb8e2f126349bcbe8ba6ee5bc7a1fd6d

Its value frequencies are Q=2:10,390; Q=3:4,709; Q=4:1,195. This Q defines a global function satisfying all original axis, evenness, fixed-mark and off-axis lower-bound conditions.

Independently executed Python standard-library verifier:

    research_checks/CBRC_F7_R488_B28_EXACT_QUARTER_CERT_20261122.py

It reconstructs the key index, checks the fixed raw-byte SHA256 and value frequencies, and exhaustively evaluates the *original* 57^4=**10,556,001** input quadruples using integer arithmetic only. The checker exited with status 0. Its complete 4D_q histogram was:

| 4D_q | Count |
| ---: | ---: |
| -2 | 226,326 |
| -1 | 2,236,954 |
| 0 | 5,104,257 |
| +1 | 2,657,374 |
| +2 | 331,090 |

Hence max|4D_q|=2 and there are 557,416 attaining tuples; E_28(q)=1/2. Combining with the fixed-mark lower bound yields e_28=1/2; the same globally defined Q provides all B≤28 by restriction.

## Constructive search and precise evidence status

Start with the already proved r487 B27 global quarter-grid witness, extending the new 1,136 B28 index keys using Q=2. The initial B28 original-input scan identifies **11,140** violations, with max|4D|=4. Sparse cutting-plane/L1 LP search with exact full-input checks produces the final integral-quarter candidate. Compared to the r487 table, **370 existing Q keys** were changed: 337 by +1 Q unit, 33 by -1, while the 1,136 new keys all retain Q=2. This is an exhibited feasible repair, not proven minimum repair count/L1. The LP is only a candidate-search method; the fixed certificate and independent integer enumeration are the proof.

This is one new bounded proved scientific unit. The global minimax remains 1/2≤e_infinity≤4/7; the next exact finite-box frontier is B29. Neither original F7 Result review, formal Task completion, mother Objective acceptance nor other owner/CLAIM or P000/schedule was changed. The original Native review budget and frozen manifest hash issue remain at https://github.com/awdawmip/enterprise-math/issues/2874.

Predecessor r487: https://github.com/awdawmip/enterprise-math/blob/8eb1051c9cbb58c3c22f4eca486983dae8787185/research_notes/driver/2026-11-22_f7_r487_B27_exact_quarter_minimax.md
