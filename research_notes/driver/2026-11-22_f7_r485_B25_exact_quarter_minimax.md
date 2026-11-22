# CBRC F7 r485 — exact B25 finite-box minimax by fixed quarter-grid witness

Date: 2026-11-22 Asia/Taipei. Scientific author: RESEARCH_DRIVER logical lane EM-DVR-DEBB5E. Prior original F7 researcher EM-CBRCF7-83A1D4, frozen RR-AA38973D56330E59D315 and its authorship/review states are preserved.

## Theorem

For globally admissible real q: Z²→R satisfying q(-x,y)=q(x,y), q(0,0)=0, q(x,0)=1 for x≠0, q(x,y)≥1/2 for y≠0, and q(2,1)=q(-1,-1)=1/2, let

    k=a-2b-c+2d,
    D_q(a,b,c,d)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d),
    e_B=inf_q max_{a,b,c,d∈[-B,B]∩Z}|D_q(a,b,c,d)|.

**r485: e_B=1/2 for all integers 1≤B≤25.** This extends r484 B24 by one exact box, without changing the infinite-domain bound 1/2≤e_infinity≤4/7.

## Matching lower bound

The fixed input (a,b,c,d)=(1,-1,0,0), k=3 gives D_q=q(4,2)+q(-3,-3)-q(1,-1)-q(0,0)≥1/2, since q(1,-1)=1/2 by evenness/fixed mark and both first terms are off-axis ≥1/2.

## Globally admissible constructive upper witness

Let Q=4q. On the axis set Q(0,0)=0, Q(x,0)=4 (x≠0); at the two marked evenness keys Q(±2,1)=Q(±1,-1)=2. On all other off-axis keys use a finite table and baseline Q=2 elsewhere.

For B=25, R={-50,...,50} and integer intervals T_r=[2r-min(25,r+25),2r-max(-25,r-25)]. Build an insertion-ordered key index by increasing r, then increasing u>r; for each pair iterate v first in increasing T_r then increasing T_u; for each such v visit rr=r then rr=u, append the previously unseen (|2rr-v|,rr-v) if off-axis and not a fixed-mark key. This deterministic index has exactly **13,010** keys. Assign the corresponding raw byte values Q from the immutable file

    research_artifacts/F7_R485_B25_Exact_Quarter_Witness_20261122.b85

which stores Base85(zlib(raw)) with exact raw SHA256

    f2169ab1b03922c4a39eb36909a0a8deb5fe1e0d6936559075480d9df1814548

The raw values have frequencies Q=2:8,552; Q=3:3,577; Q=4:881, so the global off-axis floor and evenness hold by construction.

The separately executed Python standard-library verifier

    research_checks/CBRC_F7_R485_B25_EXACT_QUARTER_CERT_20261122.py

validates the raw SHA256, rebuilds exactly the index and all original q constraints, then checks **51⁴=6,765,201** original integer input quadruples without floating-point approximations. Its complete histogram of 4D_q is:

| 4D_q | Count |
|---:|---:|
| -2 | 160,468 |
| -1 | 1,495,490 |
| 0 | 3,301,861 |
| +1 | 1,618,202 |
| +2 | 189,180 |

Thus max|4D_q|=2, with 349,648 tight inputs; E_25(q)=1/2. Combined with the marked lower-bound input, this proves the theorem.

## Method, novelty and boundaries

Starting from the already saved r484 B24 exact certificate, extend new B25 coordinates with Q=2. That fixed starting extension yields 14,890 B25 original-input violations, max|4D|=4. Sparse LP/cutting-plane search gives a quarter-grid candidate that modifies exactly 524 old B24 coordinates by one Q unit (493 increases, 31 decreases); **all 1,012 new B25 index coordinates retain Q=2**. This is a constructive route, not a proof of minimum repair. The mathematical proof depends solely on the static data/hash and independently executed exhaustive integer checker, not LP status or the optimization objective.

Mother objective and global e_infinity remain open; next finite frontier is B26 exact primal or rigorous obstruction. This is one new proven mathematical subunit, not Native Review/Result acceptance, Task completion or promotion. Original owner, source provenance and all reviewer independence constraints are unchanged.

r484 predecessor: https://github.com/awdawmip/enterprise-math/blob/c0ef0c35f96822165f1cd70b9bd226e5d27d0acb/research_notes/driver/2026-11-22_f7_r484_B24_exact_quarter_minimax.md
