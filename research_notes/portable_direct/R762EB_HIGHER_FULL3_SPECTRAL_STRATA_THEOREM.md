# R762EB — Higher cyclotomic strata of full-three-coordinate six-branch BRC

Date: 2026-11-18 (Asia/Shanghai). Task RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Author lineage EM-X6-3050F6, original SID MCP-4b2d70a97f594366a7c94a0f8b45df38 and CLAIM MCP-d6d2c143cc4d2df4dea1c00c. Status: author-side exact finite proof and independently reproducible integer code; independent review NOT_REVIEWED.

## Scope and frozen inputs

P000 V5 at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json, taskbook @e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. Reuse R762EA second-stratum theorem at @1f668adba36a05c9aa474f501c2f651b39806e64:research_notes/portable_direct/R762EA_SECOND_SPECTRAL_STRATUM_THEOREM.md.

Original six named positive paths: 000,100,001,110,011,111. Their terminal BRC polynomial is

\[
P(X,Y,Z)=1+X+Z+XY+YZ+XYZ.
\]

This is a restricted terminal observer within X6, not native signed TRIADIC_CLOSURE_E or an independent native three-dimensional space. Full path provenance, temporal order, hidden state and signed-force typing are not quotientable without a further future-operation certificate.

## Theorem (all a >= 3; extra refinement for a >= 4)

Fix Q=3^a, d=3^(a-1), a>=3, a primitive Qth root zeta in the 3-adic cyclotomic field K and pi=zeta-1. Normalize v_pi(pi)=1, v_pi(0)=infinity, so v_pi(3)=2d. Let lambda_ijk=P(zeta^i,zeta^j,zeta^k) for i,j,k modulo Q.

**For every a>=3** the exact counts of valuations are:

| v_pi(lambda), exact except last row | Count | Fraction of Q^3 |
|---|---:|---:|
| 2 | 13122 (Q/27)^3 | 2/3 |
| 4 | 3888 (Q/27)^3 | 16/81 |
| **6** | **1782 (Q/27)^3** | **22/243** |
| **10** | **432 (Q/27)^3** | **16/729** |
| **12** | **144 (Q/27)^3** | **16/2187** |
| >=18 or infinity | 315 (Q/27)^3 | 35/2187 |

Thus valuations 8, 14 and 16 never occur. Every finite v_pi is even by the palindromic real-subfield theorem from R762EA.

**For every a>=4**, the last row splits exactly into:

\[
\#\{v_\pi(\lambda)=18\}=210(Q/27)^3=(70/6561)Q^3,
\]
\[
\#\{v_\pi(\lambda)\ge28\text{ or }\infty\}
=105(Q/27)^3=(35/6561)Q^3.
\]

The finite proof produces >=27 for the last group; R762EA parity sharpens >=27 to >=28. For a=3 the ramification threshold v_pi(3)=18 prevents classification of that last group using only coefficients modulo 3. The a=2 case is outside the new theorem, since v_pi(3)=6.

## Proof (finite Lucas certificate lifted to all Q)

Write B={(0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1)}. For each branch b and character (i,j,k), choose the integer exponent e_b in 0,...,Q-1 representing b_1 i+b_2 j+b_3 k modulo Q. The exact binomial expansion in the 3-adic integer ring is

\[
\lambda_{ijk}=\sum_{b\in B}(1+\pi)^{e_b}
=\sum_{m\ge0} A_m(i,j,k)\pi^m,\qquad
A_m=\sum_{b\in B}\binom{e_b}{m}.
\]

For m<27, write m=m_0+3m_1+9m_2. Lucas's congruence gives

\[
\binom{e_b}{m}\equiv\prod_{h=0}^2
\binom{(e_b)_h}{m_h}\pmod3.
\]

Therefore A_m modulo 3 depends only on the triple (i,j,k) modulo 27, because 27 divides Q. The finite coefficient table is the explicit integer formula

\[
T_m(r,s,t)=\sum_{b\in B}
\binom{(b_1r+b_2s+b_3t)\bmod27}{m}\pmod3,
\quad(r,s,t)\in\{0,\ldots,26\}^3.
\]

If its first nonzero value occurs at m<v_pi(3), the preceding A_h are all divisible by 3 (hence have valuations >=v_pi(3)), and the later powers pi^h have valuations >m. Thus v_pi(lambda)=m exactly. If all table entries T_0,...,T_(M-1) are zero and M<=v_pi(3), then v_pi(lambda)>=M.

The accompanying executable R762EB_VERIFY.py enumerates **all 19683 triples** and **all degrees 0 through 26**, using exact Lucas products. Every table entry is independently compared with Python's direct integer binomial sum, with assertions for complete coverage and the resulting counts. The finite certificate reports:

| First nonzero T_m or terminal threshold | Counts for 27^3 triples |
|---|---|
| 2, 4, 6, 10, 12, >=18 | 13122, 3888, 1782, 432, 144, 315 |
| 2, 4, 6, 10, 12, 18, >=27 | 13122, 3888, 1782, 432, 144, 210, 105 |

An independently inspectable subdivision: among the 9^3 mod-9 prefixes, the first nonzero degree is 2 on 486, 4 on 144, 6 on 66, and >=9 on 33. Of those 33 deep prefixes, exactly 24 have 18 of their 27 third-digit lifts with T_10 nonzero; the remaining nine have zero such lifts. Consequently 24*18=432 first-degree-10 triples. Both checks, the remaining classifications, and the two full-table SHA256 hashes appear in the JSON evidence.

Each mod-27 triple occurs (Q/27)^3 times modulo Q. For a>=3, v_pi(3)=2d>=18, so all classifications with first nonzero m<18 are exact and the final group has v_pi>=18. For a>=4, v_pi(3)>=54, so the same proof works through degree 26, giving exact m=18 and remaining >=27. R762EA's parity lemma yields >=28. QED.

## Verification, interpretation, next problem

Run: python3 R762EB_VERIFY.py > R762EB_EVIDENCE.json. Standard-library integer arithmetic only, no numerical roots or floating-point approximations. The evidence reports PASS, two histograms, witness triples, intermediate mod-9 subdivision and reproducible SHA256 hashes. The all-a result uses a proved Lucas reduction, so the 27^3 enumeration is a complete finite lemma, not an extrapolation from small q. Independent mathematical review remains NOT_REVIEWED.

This result concerns only the candidate positive terminal-three-residual BRC **character spectrum**; it is not a full coefficient-content/gcd proof and does not establish native signed Cell/Link/Port admissibility or lossless future-state compression. The original six-dimensional X6 carrier, three-force closure, PERP_E 120-degree typing and path provenance remain unchanged.

Open work: (1) classify the >=18 characters at a=3 using integral cyclotomic carries; (2) at a>=4, refine the >=28 group with base-81 digits; (3) obtain a sharp coefficient nondivisibility witness for R762DN's all-horizon content conjecture; (4) obtain actual signed TRIADIC_CLOSURE_E and V17/V29/V39 event transport before any native promotion.
