# Stage372-B — exact cross-source x-straddle theorem (2026-11-02)

Research2 portable author-side result. Frozen scientific pins: GLOBAL_KNOWLEDGE_V1 main@bf84bd7c61a2444b59b1da96be57df0e9ae47e53, enterprise-math main@2af3fc484eb11060b69e0afc1b562bcaf5ad1419. Current behavioral rules independently read at global main@e0e8ce5065badbb3d8842d5a7d436d579dadeabb and EM main@959673dd0922494276789b0f041ccbec7b9cfbcc. P000 V5 and ACTIVE worldview remain as original premise.

## Statement and exact model

For k=0,1,2,3 set w=(1,3,3,1), m=(61,21,9,9), B_k(z)=z^k(1-z)^(3-k) and
r_k(x,y)=(4 B_k(x)+B_k(y))/5-m_k/160.
Define
b(x,y)=(5/32) sum_k w_k |r_k(x,y)|,
D_3(a,z)=(1/2) sum_k w_k |B_k(a)-B_k(z)|,
c(x,y)=[63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)]/256.
The four separate ports, including all sixteen distinct outcome-label comparisons, are retained.

For P,Q in [0,1]^2, minimize T(P,Q)=33/1024+c(P)+c(Q) subject to
b(P)+b(Q) <= 2 beta_* + E, E=11/5000, beta_*=b(q_*), and q_* the common root r_0=r_1=0.

Previously verified Stage369-B/370-B universal results ensure that each *global minimizer source* lies in the open/closed core
C=(577/2500,239/1000] × (27/50,59/100).
They also establish, for the exact rational feasible reference
P0=(231138/10^6,555681/10^6), Q0=(237807/10^6,575694/10^6),
2 beta_*+E<61/6250, b(P0)+b(Q0)<2 beta_*+E, and
c(P0)+c(Q0)<6319/100000. The present checker independently repeats the algebraic bracket, feasible-reference and cost inequalities.

**New theorem.** In the full four-real-parameter optimization problem, every global minimizer can be source-relabelled to satisfy

    x_P < 469/2000 < x_Q .

More quantitatively, on the closed rational rectangles R_-=[577/2500,469/2000]×[27/50,59/100] and R_+=[469/2000,239/1000]×[27/50,59/100], respectively,

    L(x,y):=c(x,y)+(6/5)b(x,y) > 1873/50000      on R_-  (L)
    b(x,y) > 49/10000                               on R_+  (R)

for **every real point**, including all rectangle boundaries.

If P,Q are feasible and both in R_-, then
c(P)+c(Q) = L(P)+L(Q)-(6/5)(b(P)+b(Q)
> 2*(1873/50000)-(6/5)*(61/6250)
= 6319/100000+9/500000
> c(P0)+c(Q0)+9/500000.
Thus they cannot be global minimizers. If both in R_+, then
b(P)+b(Q)>2*(49/10000)=49/5000
and 49/5000-61/6250=1/25000>0; hence they violate the budget by >1/25000.
Every actual global minimizer lies within C by the earlier universal results.
The two closed-side exclusions also cover equality x=469/2000, so the remaining necessary structure is the **strict** straddle. Compactness of the original feasible domain and the exhibited feasible rational reference give existence.

## Continuous-domain exact certificate for (L),(R)

The self-contained REPRO_STAGE372B.py calculates Fraction-only exact interval lower bounds. For each 1D rational interval [u,v], each cubic B_k has extrema at endpoints or k/3 (when inside). Hence a closed 2D box has exact containing ranges for all residuals and all sixteen *port-specific* label differences. Applying gap(t,[a,b]) = 0 for t in [a,b], otherwise min(|t-a|,|t-b|), to every label separately yields b_lower and c_lower with
b(x,y)>=b_lower and c(x,y)>=c_lower for every real point in the box.
The lower bound c_lower+(6/5)b_lower certifies L. Every subdivision retains both closed halves, bisecting x when 5*width_x>=width_y, otherwise y. Every accepted leaf must satisfy the relevant strict rational threshold; the program rejects any unclosed depth-40 box. It verifies total rational leaf area equals the parent region area.

R_- certificate: 4199 bisections, 4200 strictly accepted leaves, max depth 20.
R_+ certificate: 50 bisections, 51 strictly accepted leaves, max depth 14.
Total: 4251 leaves, zero unresolved boxes; exact arithmetic only.

The deterministic complete CSV produced by the code (with --emit and a target file name) is 782383 UTF-8 bytes and has SHA256:
5608a0843c3105eafa75c65b7496050391e3781919c337acb4c861d2303c6323
The checker was actually executed twice, with byte-identical stdout. REPRO_STAGE372B_EXECUTED_STDOUT.txt preserves the actual execution result. All required rational reference checks are assertions in the published program.

## Provenance, scope, next problem

This is a new *source-heterogeneity necessary condition*: in the frozen two-real-parameter per-source Bernoulli/BRC auxiliary observer, all full four-parameter global optimal pairs strictly straddle x=0.2345. It combines with Stage371-B's condition that at least one y-coordinate belongs to (0.56,0.58). The mother global optimality question stays open; next compute a coupled four-parameter y-band exclusion or an exact rational strictly cheaper competitor on the ordered domain x_P<469/2000<x_Q. This portable result is author-side / exact Fraction executed / independently unreviewed / native not admitted. It changes no P000 X6, six-axis, three-dimensional slice, time, Cell-address or joint-provenance semantics; native observer-preserving transfer remains separate.
