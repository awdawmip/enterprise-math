# Exact 91/145 obstruction on a continuous B-side-release edge (BRC N=4 S23)

Date: 2026-11-02. Author-side analytic proof and exact V8 integer execution; UNREVIEWED / NOT_ADMITTED. Scientific input remains frozen at enterprise-math commit 43ec6098b1330ae86d0a7863be336c5d97f6ef34. The concrete ten-decoder bank is unchanged from research commit 57a6db1d81068504cca2b3a6ea809a63555473d6.

## Statement and quantifiers

There are six separately labeled positive-weight source preparations and one shared four-state causal encoder. Seven original decoding kernels D1,D2,D3,D4,D6,D7,D8 are fixed; this calculation also fixes the three explicitly previously constructed kernels K1_old,K2_old,K3_repair. Let B denote that particular ten-decoder bank. For a legal eleven-parameter policy z define

\[
L_D(z)=\max_{0\le i<6}\frac12\sum_{j=0}^3|P_{ij}(z)-Q_{ij}(D)|,\qquad
m_B(z)=\min_{D\in B}L_D(z).
\]

Release the second B-side causal coordinate through the legal real continuum

\[
Z(s)=(s,1/3,9/20,0,0;\ 1,1,0,0,0,0), \quad 0\le s\le1.
\]

This lies in the six-parameter family F6(s,t,u,v,w,h)=(s,t,u,v,w;1,h,0,0,0,0), with t=1/3,u=9/20,v=w=0,h=1. Then the exact result for THIS FIXED BANK is

\[
\boxed{\max_{s\in[0,1]}m_B(Z(s))=\frac{91}{145},
\qquad \operatorname{argmax}_{[0,1]}m_B(Z(s))=\{5/29\}.}
\]

This strictly exceeds the prior concrete bank's worst-case 3/5 on F5 by 4/145.

## Exact preservation of the causal and provenance map

Using zero-based indices z[0]..z[10], the six raw source rows are defined by A=(0,0,0,1,1,1), Bidx=(2,2,3,2,2,4), C=(5,6,7,8,9,10). For each source i put x=z[A_i], b=z[Bidx_i], c=z[C_i], and

\[
R_i(z)=\bigl(x,(1-x)b,(1-x)(1-b)c,(1-x)(1-b)(1-c)\bigr).
\]

The six prepared observation rows are P=(M/20)R, where

\[
M=\begin{pmatrix}
10&10&0&0&0&0\\9&11&0&0&0&0\\0&0&20&0&0&0\\
0&0&0&10&10&0\\0&0&0&2&18&0\\0&0&0&0&0&20
\end{pmatrix}.
\]

Decoder observations use the original decoder-row source map G=(0,0,1,2,2,3) and the same M/20. The decoder rows and all source constraints are reproduced in VERIFY.js. No source labeling, joint causal parameter or nonuniform mixing coefficient is projected away.

With the other ten parameters fixed, every P_i(Z(s)) is affine in s. For a fixed decoder D, TV(P_i(Z(s)),Q_i(D)) is convex in s; the maximum over six sources, L_D, is convex too.

## Three endpoint measurements give an all-real upper bound

The V8 verifier checks all six rows with exact integers and obtains

| s | L_D8(Z(s)) | L_K1_old(Z(s)) |
| --- | --- | --- |
| 0 | 11/20 | 4/5 |
| 1/4 | 53/80 | 11/20 |
| 1 | 1 | 3/5 |

For 0<=s<=1/4, the two upper chord bounds from convexity are

\[
L_{D8}(Z(s))\le 11/20+9s/20,\qquad
L_{K1}(Z(s))\le 4/5-s.
\]

Hence m_B(Z(s)) is at most the smaller of these two lines. They intersect exactly at s=5/29, and the smaller line has a UNIQUE maximum there, equal to 91/145.

For 1/4<=s<=1, the K1 chord from its endpoint risks 11/20 and 3/5 stays at most 3/5, which is strictly below 91/145. Together these bounds prove the upper bound and uniqueness on the entire real interval, including irrational values.

## Exact lower certificate at the rational maximizer

At s*=5/29, the ten risks in the declared order

D1,D2,D3,D4,D6,D7,D8,K1_old,K2_old,K3_repair

are EXACTLY

\[
\left(19/30,\ 1,\ 1,\ 2/3,\ 24/29,\ 2/3,\
91/145,\ 91/145,\ 19/30,\ 24/29\right).
\]

All ten are at least 91/145 and D8 and K1 attain it. Thus m_B(Z(s*))=91/145. This closes the all-real fixed-bank theorem.

## Interaction with the previous result, and open question

Reuse the prior immutable 100000-cell F5 common-decoder certificate and the discrete S18/J certificates from commit 57a6db1d81068504cca2b3a6ea809a63555473d6. For the SAME BANK, the exact worst radius over S18 union J([0,1]) union F5([0,1]^5) union Z([0,1]) becomes 91/145.

When the three free stochastic kernels are REOPTIMIZED, the previously certified arbitrary-real lower bound and this explicit bank give the conditional author-side interval [3/5,91/145]. A new universal lower bound of 91/145 has NOT been established for reoptimized kernels. Next work jointly optimizes those three kernels at Z(5/29) and tests a full B-side continuum. The full eleven-parameter ten-label mother problem remains a distinct open optimization.

## Reproducible exact computation

Run Node.js: node VERIFY.js > RUN_EVIDENCE.recomputed.json. The saved VERIFY.js is the exact source executed by the author, and RUN_EVIDENCE.json is its captured result. The code recreates all ten stochastic decoders, the 6x6 mixture and shared causal preparation map; verifies probability normalization, all ten witness risks, exact chord endpoints, rational line intersection, and an affine midpoint identity. It uses safe integer probability denominator N=487200 and total-variation denominator 2N=974400. The continuum conclusion follows from the proof above, not grid sampling. Native Owner/CLAIM, Result and independent review have not been obtained.
