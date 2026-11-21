# X6 R84 — 四阶正权 BRC 在 4–10 Port 的全域最小充分核心

Date: 2026-11-21 (Asia/Shanghai).
Scientific status: FINITE_EXHAUSTIVE_EXACT_INTEGER_CERTIFICATE / AUTHOR_CHECKED / NOT_INDEPENDENTLY_REVIEWED.
Frozen scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json.
Predecessors: R72–R83; the present proof uses no R72 finite-atlas completeness assumption.

## Model and theorem

We use the conditional positive-count degree-four BRC star-histogram observer with four moment readouts, one unknown common additive bias, arbitrary positive real weights w=(A,B,C,D), and an integer histogram difference a=(x,y,z). The source state remains native P000 V5 HEARTBEAT_WORLD X6; this readout does not identify or discard its Cell/Link/named Port/whole-triadic-event/time-process information.

Set

\[
q(a)=\max\left(\sum_{k=1}^3(a_k)^+,\sum_{k=1}^3(-a_k)^+\right),
\quad v(a)=(0,2x+6y+12z,6x+24y+60z,14x+78y+252z),
\]
\[
g_{ij}(a)=|v_i-v_j|/2,\quad F(a;w)=\max_{i<j}g_{ij}(a)/(w_i+w_j),
\quad \eta^*(p,w)=\min_{a\ne0,\ q(a)\le p}F(a;w).
\]

Theorem. For each integer p from 4 through 10 and every positive real w, the optimum equals the minimum of F(s;w) over the following fixed candidate family S_p, and the displayed family has the smallest possible cardinality even among arbitrary feasible integer-difference directions modulo ±:

| Port p | Exact S_p by ID | Minimum cardinality |
|---:|---|---:|
| 4 | u1,u3,u4m,s4,t4 | 5 |
| 5 | u1,u3,s4,t4,u5,s5,t5 | 7 |
| 6 | u1,u3,s4,t4,u5,s5,t5,s6,t6 | 9 |
| 7 | u1,s4,t4,s5,t5,s6,t6,s7m,s7,t7 | 10 |
| 8 | u1,s4,t4,s5,t5,s6,t6,s7m,s7,t7 | 10 |
| 9 | u1,s4,t4,s5,t5,s6,t6,s7m,s7,t7,s9 | 11 |
| 10 | u1,s4,t4,s5,t5,s6,t6,s7m,s7,t7,s9,s10 | 12 |

The fifteen exact directions and their six gaps (12,13,14,23,24,34) are:

| ID | a=(x,y,z) | q | Six-gap vector |
|---|---|---:|---|
| u1 | (1,0,0) | 1 | (1,3,7,2,6,4) |
| u3 | (3,-1,0) | 3 | (0,3,18,3,18,15) |
| u4m | (1,3,-1) | 4 | (4,9,2,5,6,11) |
| s4 | (3,-4,1) | 4 | (3,9,9,6,6,0) |
| t4 | (4,-1,0) | 4 | (1,0,11,1,12,11) |
| u5 | (3,2,-1) | 5 | (3,3,27,0,30,30) |
| s5 | (4,-4,1) | 5 | (2,6,2,4,0,4) |
| t5 | (5,-1,0) | 5 | (2,3,4,1,6,7) |
| s6 | (5,-4,1) | 6 | (1,3,5,2,6,8) |
| t6 | (6,-1,0) | 6 | (3,6,3,3,0,3) |
| s7m | (3,-7,2) | 7 | (6,15,0,9,6,15) |
| s7 | (6,-4,1) | 7 | (0,0,12,0,12,12) |
| t7 | (7,-1,0) | 7 | (4,9,10,5,6,1) |
| s9 | (7,2,-1) | 9 | (7,15,1,8,6,14) |
| s10 | (9,-5,1) | 10 | (0,3,6,3,6,3) |

At p=5 u4m leaves the core and u5,s5,t5 enter. At p=7 u3,u5 leave, and s7m,s7,t7 enter. The core is unchanged from p=7 to p=8. Thus its evolution includes replacement, not just adding new elements.

## Exact proof of sufficiency

For q(a)<=p, each of x,y,z lies in the complete finite cube [-p,p]^3. Enumerate every nonzero integer difference, identify a and -a by choosing the first nonzero coordinate positive, and compute all six gaps by integer arithmetic.

For every enumerated a, the verifier checks that some s in the displayed S_p satisfies g_ij(s)<=g_ij(a) in all six coordinates. This gives F(s;w)<=F(a;w) simultaneously for EVERY positive real weight vector: all w_i+w_j are strictly positive. Every s lies in q(s)<=p. Hence the optimum over the full integer domain equals the minimum over S_p.

| Port | Unoriented domain size | First available six-gap domination witness allocations in the order of S_p |
|---:|---:|---|
| 4 | 154 | (143,5,1,1,4) |
| 5 | 280 | (263,6,1,5,1,3,1) |
| 6 | 461 | (434,10,2,7,2,3,1,1,1) |
| 7 | 707 | (671,4,9,4,1,1,1,1,14,1) |
| 8 | 1028 | (979,6,13,6,1,1,1,1,19,1) |
| 9 | 1434 | (1372,6,19,7,1,1,1,1,24,1,1) |
| 10 | 1935 | (1857,6,22,13,1,1,1,1,30,1,1,1) |

Each row sums exactly to its complete domain size, including all possible feasible integer directions. The finite exhaustion proves the pointwise coverage, not merely agreement at sampled weights.

## Exact proof of global minimum cardinality

Each candidate has its own positive integer weight profile under which it is the UNIQUE optimum (modulo sign) among ALL feasible integer directions for every p at which that candidate occurs in S_p. The verifier separately tests every pairwise rational comparison by BigInt cross-product and records the strictly greater second-best cost.

| ID | Strict unique winner weight w=(A,B,C,D) |
|---|---|
| u1 | (2,1,1,4) |
| u3 | (1,1,9,38) |
| u4m | (1,1,3,1) |
| s4 | (7,7,1,1) |
| t4 | (1,7,1,7) |
| u5 | (26,1,1,61) |
| s5 | (1,1,4,1) |
| t5 | (1,2,2,2) |
| s6 | (2,1,4,10) |
| t6 | (3,1,1,1) |
| s7m | (1,7,19,1) |
| s7 | (1,1,4,24) |
| t7 | (20,9,1,2) |
| s9 | (2,22,21,1) |
| s10 | (1,1,1,2) |

Fix p. Any universally sufficient fixed candidate collection, even if using entirely different integer vectors, must contain the unique global minimizing direction at each of these displayed weight profiles. Thus every member of S_p is necessary. The finite domination proof supplies a collection of exactly that cardinality. This establishes absolute minimality, QED.

## Validation, source and next questions

Reproduction:
node research_notes/portable_direct/x6_r84_ports4_10_exact_verify.js

The JavaScript verifier needs no packages or floating-point approximations, computes integer gaps and exact rational maxima with BigInt, checks all seven finite domains, and asserts unique full-domain winners. Persisted certificate: research_notes/portable_direct/x6_r84_ports4_10_results.json. Independent preparatory Python integer enumeration reproduced the seven domain sizes and the gap-allocation vectors. Verification is author-checked and not independently peer-reviewed.

Next, combine this exact 4–10 minimum-cardinality result with R80–R83 for 11–124, preserving R82's narrower internal-indispensability claim for 23–38; then independently audit the R72/R79 p>=125 cone-cover certificate. The native X6 observer-fiber and future-operations preservation obligation for named Port, whole triadic events and heartbeat histories remains separate from this conditional histogram theorem.

Contributor provenance: R84 independent portable source continuation; prior R72–R83 contributors retain their own attribution. GitHub research publication is not formal Task CLAIM/PROGRESS, Activity association, Result review or Foundation admission.
