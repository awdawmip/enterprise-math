# T6: five more exact-v2=7 ambiguity pairs excluded by odd-prime Vandermonde

2026-11-23 Asia/Taipei. Original mathematical contribution: RESEARCH_DRIVER EM-DVR-DEBB5E, original SID MCP-9b4714dc46b948afa4875a86c89c713c. This result continues the existing finite exact-v2=7 census and its first two odd-prime exclusions; it neither changes original p19/p17 authorship nor constitutes Native Review/Result acceptance.

## Theorem (19 remaining candidates, as an upper bound)
Let A,B be finite multisets of positive integer exponents, with sum(A)<=2331 and sum(B)<=2331 separately, and original full H_k(X)=sum_e (e/(e+1))^k equal for k=0,...,6. Put d=e+1. After cancelling previously proven equal multiplicities at 2^8|d, the complete exact-valuation-seven signed multiplicity profile (d=128j, j odd 1..17) is either identical or one of **at most 19 unordered side-profile pairs** from the original 26 six-moment 2-adic signature collisions. This strengthens the independently saved bound of 24 by eliminating five further, previously unexcluded pairs.

## Full-moment odd-prime Vandermonde lemma
Take a prime p and assume that within the signed difference m_A(d)-m_B(d), every p-divisible denominator with nonzero difference has exact p-adic valuation one, d=p*j with p not dividing j. Full equalities S_k(A)=S_k(B), k=1,...,6, follow from H0..H6 by binomial inversion. Multiply S_k(A)-S_k(B) by p^k and reduce modulo p to obtain

  sum_j Delta_m(p*j)*j^(-k) == 0 (mod p), k=1,...,6.

If all possibly contributing cofactor residue classes j mod p belong to a set of r<=6 distinct nonzero residues, the first r equations form an invertible Vandermonde matrix: the kth-row coefficient is x_j^k for x_j=j^(-1) in F_p, whose determinant is (product_j x_j) times the ordinary nonzero Vandermonde determinant. Hence the **aggregate signed multiplicity coefficient in each residue class must vanish modulo p**. In particular, one uniquely occurring distinguished class with signed multiplicity +/-1 is impossible.

## Five precise exclusions
The complete previously verified exact profile census has 26 collision doubletons. Beyond the two already excluded at remainder R=29, inspect the following five distinct pairs. Here R=2331 minus the exponent mass of the entire exact-v2=7 profile on each side, and brackets list DENOMINATORS with multiplicity:

| R | A exact-v2=7 denominators | B exact-v2=7 denominators | Witness class |
|---:|---|---|---|
| 31 | [384,640,640,640] | [128,128,640,1408] | p=11; 1408/11=128 is 7 mod11 |
| 33 | [128,128,384,384,640,640] | [128,128,128,128,384,1408] | p=11 |
| 35 | [128,128,128,128,128,384,640,640] | [128,128,128,128,128,128,128,1408] | p=11 |
| 31 | [128,384,640,1152] | [128,128,384,1664] | p=13; 1664/13=128 is 11 mod13 |
| 33 | [128,128,128,128,640,1152] | [128,128,128,128,128,1664] | p=13 |

For p=11, since each side has at most R<=35 remaining exponent mass, **all other** denominators divisible by 11 must be among 11,22,33 (their cofactor residues are 1,2,3 mod11). The distinguished denominator 1408 has cofactor residue 128=7 mod11. These four classes are distinct, and no additional higher-v11 denominator can fit in the leftover budget; any higher-v2 denominator already cancels by the old 2^8 theorem. The 4x4 Vandermonde system from S1..S4 forces Delta_m(1408)=0 mod11, contradicting +/-1.

For p=13, R<=35 restricts all other 13-divisible denominators to 13,26 (cofactor residues 1,2 mod13). The distinguished denominator 1664=13*128 has cofactor residue 128=11 mod13. These three classes are distinct, and no higher-v13 denominator is budget-feasible outside the 2^7 profile. The 3x3 system from S1..S3 forces Delta_m(1664)=0 mod13, contradicting +/-1.

These five have separate exact-v2=7 side budget masses 2300,2298,2296,2300,2298. The original fixed checker enumerates all 26 and directly identifies the five rows from their immutable actual vectors; none duplicates the previously excluded two R=29 pairs. Thus 26 - 2 - 5 = 19 **at most**. The remaining 19 are necessary-signature-compatible candidates, not proved solutions to the original six rational moment equations.

## Provenance and continuation
Prior full v2=7 census and fixed checker: https://github.com/awdawmip/enterprise-math/blob/4d0265969514c35a281165a4262dee20532c69d1/research_notes/driver/2026-11-23_t6_p2_seventh_26_collision_classification.md
https://github.com/awdawmip/enterprise-math/blob/af62822811a9a340a8235ae0b41c4951bfd36241/research_checks/T6_P2_SEVENTH_DEFECT_PROFILE_EXACT_CHECK_20261123.py
Prior two excluded pairs: https://github.com/awdawmip/enterprise-math/blob/c15259905e42a1b572b4849bd8058e520b13daa7/research_notes/driver/2026-11-23_t6_p2_seventh_two_extremal_defects_excluded.md

This is one additional proof subunit. New Native Review admitted 0; Result accepted 0; official Task completed 0; mother T6 objective completed 0. Current owner, original contributor and protected Source/Activity authority are unchanged.
