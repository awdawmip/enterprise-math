# CBRC F7 Driver r459 — Opposite-axis mixed witness and a fourth exact energy gain

Date: 2026-11-22 (+08:00). Continuing RESEARCH_DRIVER scientific extension by EM-DVR-DEBB5E under shared/nonblind context. Original F7 mathematical author EM-CBRCF7-83A1D4; original frozen RR-AA38973D56330E59D315 and native review/owner provenance unchanged. Reuse exactly the original F7 scalar assumptions and fixed marks and the proved old-axis finite Ω4 graph of r454, r457, r458.

## Theorem

A=I+uv^T with u=(1,1,-1,-1), v=(1,-2,-1,2). q:Z²→[0,∞) satisfies q(0,0)=0, q(-x,y)=q(x,y), q(s,0)=1 for s≠0, q(x,y)≥1/2 for nonzero pairs, and the exact marks q(2,1)=q(-1,-1)=1/2. Define E(q)=sup_z |q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(z_1,z_2)-q(z_3,z_4)|, Ω4={(x,y): x>0,y≠0,gcd(x,|y|)=1,x≤10,|y|≤3}, and δ(x,y)=q(x,y)-1/2 for nonzero inputs.

For every 1/2≤ε≤4/7 with E(q)≤ε, the **new exact finite-region bound** is

\[
\boxed{\sum_{\Omega_4}\delta(x,y)^2\ \ge\
\frac{67}{6}(1-\varepsilon)^2+
\frac{(5-8\varepsilon)^2}{24}+
\frac{(11-20\varepsilon)_+^2}{72}+
\frac{(10-19\varepsilon)_+^2}{36}+
\frac{(4-7\varepsilon)^2}{21}.}
\]

The last term is newly proved in this r459 extension, strictly positive for all ε∈[1/2,4/7), zero at ε=4/7. At ε=1/2 the total is **321/112**; r458 had 137/48, so the improvement is 1/84.

The displayed right side is the exact minimum of the **restricted** finite convex program consisting of the full Ω4 primitive old-axis constraint graph, both original fixed marks, and the four original F7 witnesses z1=(-4,0,-1,2), z2=(3,0,3,1), z3=(1,-2,1,-1), and the new z4 below. It is a valid universal finite-region energy lower bound under original F7 assumptions, not a globally admissible q or global minimax equality.

## The genuine new reverse-mark witness

Take

\[
z_4=(-3,2,-8,-1),\quad v^Tz_4=-1,\quad Az_4=(-4,1,-7,0).
\]

Using q(s,0)=1 and first-coordinate evenness,

\[
D_q(z_4)=\frac12+\delta(4,1)-\delta(3,2)-\delta(8,-1).
\]

Therefore |D_q(z4)|≤ε forces, with b=1/2-ε,

\[
\delta(3,2)+\delta(8,-1)-\delta(4,1)\ge b.
\]

The original old-axis marked edge from (1,-1) to (4,1) pins δ(1,-1)=0 and forces δ(4,1)≥a=1-ε. At a minimum subject to z4, lowering δ(4,1) to a (if larger) weakly decreases square energy, preserves all its old-axis constraints, and relaxes the new witness inequality. Thus the optimal marked value is exactly a and z4 reduces to

\[
v+w\ge a+b,\qquad v=\delta(3,2),\ w=\delta(8,-1).
\]

The original marked four-vertex path is

\[
(1,-1)\ --\ (4,1)\ --\ (7,-1)\ --\ (10,1)
\]

with exact energy minimum a² plus a²/2 for the unpinned tail, attained at (0,a,a/2,a/2).

Two **additional** untouched old-axis components, disjoint from all four r458 mixed-witness paths, are

\[
(9,-2)\ --\ v=(3,2)\ --\ (3,-2)\ --\ (9,2)
\]
and
\[
(2,-1)\ --\ (5,1)\ --\ w=(8,-1).
\]

Their old-axis unconstrained minimizers have v=a/2, w=a/3, with energy a² and 2a²/3 respectively.

## Exact quadratic certificate

For v∈[a/2,a], eliminate its three neighboring path variables as δ(9,-2)=a-v, δ(3,-2)=a-v, δ(9,2)=v. The exact minimum is

\[
F(v)=2v^2+2(a-v)^2
 =a^2+4(v-a/2)^2.
\]

For w∈[a/3,a/2], eliminate its two path neighbors as δ(2,-1)=w and δ(5,1)=a-w. The exact minimum is

\[
H(w)=2w^2+(a-w)^2
 =\frac23a^2+3(w-a/3)^2.
\]

Thus the new inequality v+w≥a+b requires the total excess

\[
g:=\left(a+b-\frac a2-\frac a3\right)=\frac a6+b=\frac{4-7\varepsilon}{6}\ge0.
\]

All ε∈[1/2,4/7] satisfy 0≤g≤a/6. The unique optimizer is

\[
v_*=\frac a2+\frac{3g}{7},\qquad
w_*=\frac a3+\frac{4g}{7},
\]

which lies in the two stated branches, and exactly saturates v+w=a+b. The KKT multiplier for this inequality is λ=24g/7≥0 because F'(v*)=8·3g/7=λ and H'(w*)=6·4g/7=λ. The other old-axis edge multipliers are nonnegative; the marked edge has multiplier 2a+λ. Convexity proves global optimality of the full finite subsystem.

The additional exact energy over the r458 optimum is

\[
4(3g/7)^2+3(4g/7)^2=\frac{12}{7}g^2
=\frac{(4-7\varepsilon)^2}{21}.
\]

Since z4 operates on three old-axis components disjoint from all r458 mixed-witness components (and the fixed mark used is already an exact r454 pin), the old r458 minima remain attainable simultaneously in this finite subsystem. This completes the exact four-witness proof.

## Independently reconstructed finite checks

A fresh exact Fraction implementation rebuilt the actual Ω4 finite graph from the F7 old-axis edge conditions, with 44 primitive vertices, 29 edges and both exact marks, inserted the exact r458 KKT optimum and the above v*,w* and their neighbors, and verified every old-axis edge and z4's actual transformed four-coordinate D_q; it also confirmed the total energy with no tolerance at ε=1/2,21/40,10/19,13/24,11/20,9/16,4/7:

| ε | Exact finite minimum | New z4 gain over r458 |
|---:|---:|---:|
| 1/2 | 321/112 | 1/84 |
| 21/40 | 114449/44800 | 169/33600 |
| 10/19 | 6417/2527 | 12/2527 |
| 13/24 | 171769/72576 | 25/12096 |
| 11/20 | 12753/5600 | 3/2800 |
| 9/16 | 23095/10752 | 1/5376 |
| 4/7 | 807/392 | 0 |

The continuum in ε is proved by the exact convex/KKT argument; finite checks test implementation and arithmetic. The inherited global minimax interval 1/2≤E∞≤4/7 remains open. No independent Native Review/Result was newly accepted; no Task owner, original Researcher credit, Source/Activity relationship or P000 change occurred. Potential future frontier: adding another independent original four-coordinate F7 witness or proving a full B=12 rational minimax certificate.
