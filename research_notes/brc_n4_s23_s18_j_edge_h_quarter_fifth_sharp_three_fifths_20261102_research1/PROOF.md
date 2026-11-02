# BRC S23: exact 3/5 for S18, the full J-edge and two H witnesses

2026-11-02. Frozen scientific input `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Continuation of the exact 7/12 author theorem at `awdawmip/enterprise-math@3f1643710eec93c297b4ccf1c3275dd986d19b10`, PR #1765.

## Exact claim and scope

Use the original six separately labeled positive observation sources `AU0,AU1,AV,BU0,BU1,BV`, the original `M20/20` mixing, shared causal parameter `b_U`, one common decoder for each label, and fixed decoders `D1,D2,D3,D4,D6,D7,D8`. The other three common four-row stochastic decoders are arbitrary **real** kernels. For eleven-parameter legal policies, let `J(t)=(1,t,0,0,0;0,0,0,0,1,0)` and `H(s)=(s,1,0,0,0;1,0,0,0,0,0)`. Let `S18` be the previously frozen set of eighteen legal policies. With `L_D(z)=max_{i=1..6} TV(P_i(z),Q_i(D))` and `S=S18 ∪ J([0,1]) ∪ {H(1/4),H(1/5)}`, the following value is exact:

`inf_{K1,K2,K3} sup_{z in S} min_{D in {D1,D2,D3,D4,D6,D7,D8,K1,K2,K3}} L_D(z) = 3/5.`

It increases the previous `S18 ∪ J([0,1]) ∪ {H(1/4)}` optimum `7/12` by precisely `1/60`.

## Six-source model and constructive upper bound

Unmixed law: `F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c))`; source selectors `A=[0,0,0,1,1,1]`, `B=[2,2,3,2,2,4]`, `C=[5,6,7,8,9,10]`. Mix with `M20` rows `(10,10,0,0,0,0);(9,11,0,0,0,0);(0,0,20,0,0,0);(0,0,0,10,10,0);(0,0,0,2,18,0);(0,0,0,0,0,20)`, divided by 20. Four decoder rows expand to source groups `(AU,AU,AV,BU,BU,BV)` before mixing. These parameters are reproduced exactly in the checker.

Reuse the same explicit rational free decoders from the 7/12 theorem, copied into `VERIFY.js` as `K1,K2,K3`. For all twenty policies `S18+H(1/4)+H(1/5)`, the greatest minimum bank risk is `3/5`; the first nineteen still have greatest minimum risk `7/12`, while `H(1/5)` has minimum bank risk exactly `3/5`. For the full continuous `J(t)` family, the exact endpoints are `L_K2(J(0))=L_K2(J(1/3))=1/2` and `L_K1(J(1/3))=L_K1(J(1))=7/12`. All original prepared source rows for `J(t)` are affine in `t`; total variation and a maximum of source total variations are convex for a fixed decoder. Therefore `K2` covers **every real** `0<=t<=1/3`, and `K1` covers **every real** `1/3<=t<=1`. This proves upper bound 3/5.

## Exact lower bound: ten source-event witnesses

Choose the following ten legal policies in S: `W,X,Y,Z,T5,U,V,H(1/5),J(1),J(1/5)`. The minima over the seven **fixed** decoders, respectively, are `(1,1,1,1,1,1,1,3/5,1,3/5)`. For any hypothetical radius `r<3/5`, every one must therefore use one of the **three** free decoder labels.

Suppose policies `a,b,c` share a free decoder. For any one of the six original preparations `i`, the three errors obey

`TV(P_i^a,Q_i)+TV(P_i^b,Q_i)+TV(P_i^c,Q_i) >= [sum_{j=1}^4 max(P_i^a(j),P_i^b(j),P_i^c(j))]-1.`

This follows by summing the positive parts `(P_i^a(j)-Q_i(j))_+`, etc.; at each stop atom their sum dominates `max(P_i^a(j),P_i^b(j),P_i^c(j))-Q_i(j)`. Consequently, under common radius r, `3r` is at least the maximum of the right-hand side over **all six separately labeled preparations**.

Exact rational calculation on those ten policies gives **84 of 120 possible triples** for which this source-event quantity is `>=9/5=3*(3/5)`. At `r<3/5`, no such triple can be monochromatic. Exhausting **all `3^10=59049` assignments** of the ten witnesses to the three labeled free decoders, every assignment has at least one monochromatic forbidden triple; the minimum hit count is exactly 1. Thus `r<3/5` is impossible for **all real stochastic decoder kernels**. The upper and lower bounds meet at 3/5. The fixed risk equality at r=3/5 is legitimate: the obstruction is formulated strictly below the optimum.

## Exact evidence and status

Run `node VERIFY.js`. It checks six original sources, the shared parameter, stochastic rows, the twenty finite risks, J-edge convex endpoints/affinity, ten fixed minima, 84 triple certificates and all 59049 labeled assignments using scale 50400 integer probabilities, total variation denominator 100800. `RUN_EVIDENCE.json` is actual V8 execution of the same verifier body. The continuum statement uses the analytic convexity proof; integer execution verifies the exact finite certificates. Independent author-side Python `fractions.Fraction` analysis separately reconstructed the 10-witness hypergraph and value. Mathematical status: author exact proof/compute, no independent review or native Result acceptance.

The unrestricted eleven-real-coordinate ten-label mother minimax retains previous `[1/2,2/3]` bounds for `k=4,6`. Next study the entire continuous `H([0,1])` edge rather than only two sampled points.
