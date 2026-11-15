# Exact 3/5 on two complete real BRC S23 strategy edges

2026-11-02 · Frozen science source `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. The lower-bound certificate was first persisted in PR #1765 commit `08f897bd61fc6e387bdb9afeb0be1433a7e43834` at `research_notes/brc_n4_s23_s18_j_edge_h_quarter_fifth_sharp_three_fifths_20261102_research1/PROOF.md` and `VERIFY.js`.

## New continuous-domain theorem

In the original BRC N=4 S23 six tagged positive source model with the same M20/20 mixing, single shared causal parameter `b_U`, one decoder common across six preparations, seven fixed decoders `D1,D2,D3,D4,D6,D7,D8`, and **three arbitrary real stochastic** four-by-four free decoders, put

`J(t)=(1,t,0,0,0;0,0,0,0,1,0)`, `H(s)=(s,1,0,0,0;1,0,0,0,0,0)` with all real `s,t in [0,1]`.

For the complete union `S18 ∪ J([0,1]) ∪ H([0,1])`, the exact radius is

`inf_{K1,K2,K3} sup_{z in S18 ∪ J([0,1]) ∪ H([0,1])} min_{D in {D1,D2,D3,D4,D6,D7,D8,K1,K2,K3}} max_{i=1..6}TV(P_i(z),Q_i(D)) = 3/5.`

This is a strengthening of the preceding result (which added just two H-edge points), with **every real H(s) included**. It also closes the preceding NEXT_TASK.md open unit.

## Exact new upper construction

Retain K2 and K3 from the previous theorem, and replace K1 with the following row-stochastic 4x4 matrix (row labels AU, AV, BU, BV; columns stop atoms 1,2,3,4):

`K1 = [ (2/5,0,3/5,0), (2/5,2/5,0,1/5), (2/5,0,0,3/5), (3/5,2/5,0,0) ]`.

The original six-source mixing maps four group rows to six sources via `(AU,AU,AV,BU,BU,BV)` before the shared M20/20. `VERIFY.js` recomputes **all eighteen** original S18 risks and checks their maximum is at most `3/5` (it also checks H(1/4) and H(1/5)).

For the full J-edge, exact endpoint calculations give:

`L_K2(J(0)) = L_K2(J(2/5)) = 1/2`, and `L_K1(J(2/5)) = L_K1(J(1)) = 3/5`.

Hence K2 covers `J([0,2/5])` and K1 covers `J([2/5,1])` at radius `<=3/5`.

For the full H-edge, use fixed decoder D4 for `H([0,1/5])` and K1 for `H([1/5,1])`. The exact endpoint risks are:

`L_D4(H(0))=1/2`, `L_D4(H(1/5))=3/5`, `L_K1(H(1/5))=L_K1(H(1))=3/5`.

For **each of the original six separately labeled source rows**, the policy preparation `P_i(J(t))` is affine in `t` and `P_i(H(s))` is affine in `s`, by direct substitution into the shared causal `F(a,b,c)` law and fixed positive mixing. For any fixed decoder Q, `L_Q` is the maximum of six convex total variation functions. Applying convexity on each of the four stated intervals therefore supplies an exact upper bound `3/5` for **both full real continua**.

## Reused exact lower certificate

The previously preserved ten legal witnesses `W,X,Y,Z,T5,U,V,H(1/5),J(1),J(1/5)` are all members of the enlarged population. Their seven-fixed-decoder minima are `(1,1,1,1,1,1,1,3/5,1,3/5)`. For any hypothetical radius strictly below `3/5`, all ten must be assigned to three free kernels. The original six-source TV event inequality forbids 84 of 120 policy triples from sharing a label; exact enumeration of all `3^10=59049` labeled assignments finds a monochromatic forbidden triple in each. That argument applies to every real stochastic decoder kernel, so the enlarged population has lower bound `3/5`. The upper construction meets it.

## Reproducibility and scope

The new self-contained `VERIFY.js` independently reruns the ten-witness integer lower certificate, all original six-source risk calculations, new K1 stochastic rows, and the eight exact endpoints for real J/H interval coverage. Actual V8 output is `RUN_EVIDENCE.json`. Scale is 50400, TV denominator 100800; affine/convex continuation supplies the universal real-parameter proof. Author-side proof and exact execution are not independent project review or native Result admission. The unrestricted ten-label eleven-real-coordinate problem retains the previously recorded global bounds `[1/2,2/3]` for `k=4,6`.

Next: extend from two one-parameter edges to a **two-parameter face**, e.g. `(s,t,0,0,0;1,0,0,0,0,0)`, using the same event inequality and region-covering constructions; test whether a genuine two-parameter obstruction lifts the fixed-seven/free-three minimax above 3/5.
