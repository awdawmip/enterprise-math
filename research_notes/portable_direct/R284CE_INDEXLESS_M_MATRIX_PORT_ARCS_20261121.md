# R284CE — Indexless monotone M-matrix arcs for the fixed 34-bit Port observer

Date: 2026-11-21 Asia/Shanghai. Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**.
Portable continuation of immutable R284CD @1495f91f2b63ffe160960759f8b6bcae3009f813. Its scientific input pins are unchanged.

## Model and theorem

For a 4×4 matrix C with all entries in {1,2}, retain the frozen R284BZ observer

F(C) = det M(C) mod p,
M(C) = diag(1120832,6,13,1651128) - C - 390139 E_01 - 394465 E_02 - 1497639 E_03,
p=17179869143.

The 12 lower coordinates in row order are L=(u1,a11,x,y,u2,w,a22,z,u3,g,h,r). Fix the six coordinates S=(u1,a11,x,u2,w,a22), allowing the other six lower entries and all four first-row entries to vary. This partitions 65536 binary matrices into 64 groups of 1024.

**Theorem.** For every fixed group key g, let C_minus have the ten unselected entries all equal to 2; let C_plus have the same ten entries all equal to 1. Their selected entries stay fixed. Let l_g=det M(C_minus), h_g=det M(C_plus) be **unreduced integers**, a_g=l_g mod p and w_g=h_g-l_g. Then:

1. For every C in the group, l_g <= det M(C) <= h_g. The group's 1024 modular codewords all lie on the closed circular arc (a_g,w_g).
2. Across the 64 groups, min w_g=307592214 and max w_g=450181375, both strictly below p/2=8589934571.5. The two extremizers are codewords and the outside empty gap p-w_g is uniquely largest; hence the arc (a_g,w_g) is the **unique shortest single covering circular arc**.
3. These are **exactly the 64 stored arcs** of R284CD. A decoder may compute each group arc using only two exact determinant evaluations—**zero persisted per-group arc records**—or obtain the same arcs from **13 coefficient pairs** rather than 64 start/width pairs.
4. The R284CD maximal closed-radius-59/2 arc overlap remains 4, preserving a 256 lower-state worst-case reconstruction bound, the R284CB top-row greedy inverse, minimum codeword distance 59 and ±29 integer-noise recovery. This is a storage/arithmetic tradeoff, not a measured speedup.

## Proof of monotonicity

Write M=D-B, where D is positive diagonal and B nonnegative. Uniformly for every real C in the entire entry cube [1,2]^16, the vector v=(10,12,5,1)^T satisfies the *entrywise strict inequalities*

M(C)v >= (3056632,16,9,1651072)^T > 0.

For example, the first component at worst C=2 is
(1120832-2)*10-(390139+2)*12-(394465+2)*5-(1497639+2)=3056632.
All offdiagonal entries of M are strictly negative. Thus M is an irreducible nonsingular M-matrix: the strict positive-vector inequality yields spectral radius rho(D^-1 B)<1, the Neumann series gives M^-1>0, and det M>0. Jacobi's formula now yields
∂det(M)/∂C_ij = -det(M)*(M^-1)_ji < 0
throughout the complete real cube. The integer determinant is therefore strictly decreasing in every free matrix entry. The designated all-2 and all-1 matrices attain its extrema. Their width is independent of p and the exhaustive 64 endpoint computations establish w_g<p/2. All internal gaps between codewords are <=w_g while the external complement gap is >p/2. This proves (1)–(3). Exact doubled-integer circle-event sweeping reestablishes (4).

## Polynomial index: 13 monomials

Represent the six selected coordinate bits (C_entry-1) as a 6-bit integer g in the order (u1,a11,x,u2,w,a22), with u1 as most-significant bit. Define I_m(g)=1 iff (g&m)==m. There are exactly 13 possibly nonzero coefficients, with mask set

T={0,1,2,4,8,10,12,16,17,20,32,33,34}.

Then a_g = (sum_m alpha_m I_m(g)) mod p,
and w_g = sum_m beta_m I_m(g).
The exact integer alpha values below are canonical representatives modulo p:

| mask | alpha (start mod p) | beta (width) |
|---:|---:|---:|
|0|10327531074|390497532|
|1|15332501228|-28639536|
|2|6308559268|3030594|
|4|16246662240|16517160|
|8|13451347648|3021942|
|10|4797308146|-4269599|
|12|8660083386|2758628|
|16|4516839201|-58535381|
|17|12382560997|4269599|
|20|15662556833|-2754302|
|32|2359080780|35870816|
|33|8519785757|-2758628|
|34|1517312310|2754302|

Why degree ≤2: the six selected entries occur in only rows 1 and 2 (three each); determinant is linear in each complete row. Products of two entries from the same row vanish; products occupying the same column also vanish. Of the nine cross-row products, exactly six use distinct columns. Therefore the only possible terms are the constant, six linear terms and six permitted bilinear terms. The 13 coefficient pairs are binary Möbius transforms of the 64 exact determinant endpoint values; direct evaluation matches every key. This is a structural sparse formula, not an interpolation-only guess.

## Exact validation and mathematical boundaries

The companion standalone Python standard-library program verifies all 65536 original codewords, 128 independent Leibniz determinant extremizer crosschecks, all group inclusions, the unique largest gap in all 64 groups, the sparse coefficients on all 64 keys, minimum circular distance 59 and continuous-position closed arc overlap 4. Source-codeword SHA-256 in the original R284CD order is b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4. Arc-pair digest, with group-key ascending ASCII lines "start:width\n", is 62696d9968f22d9ccfb1886a2d053731090f62eaac195948eb531ede3d0e1dcb.

This is a fixed **auxiliary Port-observer** theorem. Coarse arcs are overapproximations used only for pruning; exact lower-state and top-row distinctions are retained for the subsequent decoder. It does not identify the Port matrix with native P000/X6 geometry or perform BRC-native operations. Neither dynamic determinant query latency nor end-to-end CPU, program bytes or polynomial-vs-array performance has been benchmarked. Independent mathematical review is NOT_REVIEWED.

**Next scientific unit:** benchmark full decoding (static bytes + preprocess + arithmetic + verification) for 64 stored arc pairs, 13 coefficient pairs and zero-index determinant recomputation; use the monotone endpoint formula to investigate direct group inversion rather than a 64-key scan. The 33-bit gap-59 encoding objective remains open.

Related frozen source: [R284CD](https://github.com/awdawmip/enterprise-math/blob/1495f91f2b63ffe160960759f8b6bcae3009f813/research_notes/portable_direct/R284CD_EXHAUSTIVE_COORDINATE_ARC_FRONTIER_20261120.md). Publication is portable scientific evidence; not a formal CLAIM, Result or independent Review.
