# BRC N=4 / S23: exact sharp 4/7 on S18 plus the full real J-edge

2026-11-02. **AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.** Scientific source frozen at `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Predecessors on PR #1765: S18 exact theorem `41b1b8defffdf1e7909a5ff26ea8087bc8d53604`; hidden edge counterexample for an older particular bank `f1a0487521b1b22557f92b66884e17e6955894a4`.

## Sharp theorem

Let S18 denote the legal eleven-parameter strategies W,J,A,B,C,X,Y,Z,T1,...,T8,U,V exactly reproduced in VERIFY.js. Let `J(t)=(1,t,0,0,0;0,0,0,0,1,0)` for **every real** `0<=t<=1`, in coordinate order `(a_A,a_B,b_U,b_AV,b_BV;c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV)`. Fix the original seven common four-stop stochastic decoding kernels D1,D2,D3,D4,D6,D7,D8. Optimize three other common 4×4 row-stochastic kernels over **arbitrary real entries**. Set `L_D(z)=max_{six prepared source labels i} TV(P_i(z),Q_i(D))`. Then

```
inf_{K1,K2,K3} sup_{z in S18 union {J(t): t real, 0<=t<=1}}
     min_{D in {D1,D2,D3,D4,D6,D7,D8,K1,K2,K3}} L_D(z) = 4/7.
```

## Original typed BRC observer, source and lower certificate

The unmixed common causal law remains `F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c))`. The *same* b_U parameter is shared among its original designated sources. Prepare six source rows AU0,AU1,AV,BU0,BU1,BV using positive mixing matrix M20/20 with rows `(10,10,0,0,0,0)`, `(9,11,0,0,0,0)`, `(0,0,20,0,0,0)`, `(0,0,0,10,10,0)`, `(0,0,0,2,18,0)`, `(0,0,0,0,0,20)`. The common decoder's group rows AU,AV,BU,BV are assigned to the six sources via `(AU,AU,AV,BU,BU,BV)` **before the same M20 mixing**. Each total-variation risk is taken on these original six prepared rows, without separating their common kernel.

The original S18 subset has exact lower bound 4/7 with the same fixed seven plus three arbitrary real kernels. VERIFY.js independently reproduces the source-event proof on the eleven essential witnesses W,J,A,B,C,X,Y,Z,T5,U,V: all must use a free label at any radius below 4/7; a same-labeled triple x,y,z has disjoint stopping events yielding `3r >= sum_atom max(P_i(x)[atom],P_i(y)[atom],P_i(z)[atom]) - 1` in each original source row i. Exactly **111 of C(11,3)=165 triples** have a prepared row with right side >=12/7. Each of the **3^11=177147** free-label colorings contains a monochromatic such triple. Thus all real three-kernel choices have worst error >=4/7 on S18, and therefore on the larger S18-plus-edge population.

## Three explicit rational kernels and all-real upper certificate

With group row order AU,AV,BU,BV and atom columns 1,2,3,4, take

```
K1 = 4/7 3/7 0 0; 4/7 3/7 0 0; 0 32/63 3/7 4/63; 1/7 0 3/7 3/7
K2 = 1 0 0 0; 1 0 0 0; 4/7 0 0 3/7; 0 4/7 3/7 0
K3 = 4/7 0 3/7 0; 4/7 3/7 0 0; 3/7 0 1/7 3/7; 4/7 0 0 3/7
```

All twelve rows are probability vectors. On all 18 original strategies the exact min-bank risks, in order W,J,A,B,C,X,Y,Z,T1,T2,T3,T4,T5,T6,T7,T8,U,V, are

```
(4/7,16/35,4/7,4/7,4/7,4/7,4/7,4/7,
 1/2,1/2,1/2,1/2,4/7,1/2,1/2,1/2,4/7,4/7).
```

For J(t), the six **unmixed** target rows are `e1,e1,e1,t e1+(1-t)e4,t e1+(1-t)e3,t e1+(1-t)e4`. The six prepared mixtures are affine in t, hence for any fixed decoder D the function `L_D(J(t))` is convex (maximum of six total-variation norms of affine vectors). Exact event-by-event endpoint risks are

```
L_K1(J(0))=4/7; L_K1(J(17/63))=4/7;
L_K3(J(17/63))=18/35; L_K3(J(1))=4/7.
```

Convexity yields K1 radius <=4/7 for all real `t in [0,17/63]`, and K3 radius <=4/7 for all real `t in [17/63,1]`. Consequently every point on the entire continuous J-edge is covered and the sharp theorem follows.

## Independent finite coverage and a new off-edge witness

The exact verifier scans all 2048 binary policies (maximum 4/7, 832 maximizers), all 177147 ternary policies (maximum 4/7, 40041 maximizers) and all 78848 policies with exactly one coordinate in the interior eighth grid and the other ten binary (maximum 5/8; 288 policies exceed 4/7). One explicit lawful policy `H=(1/4,1,0,0,0;1,0,0,0,0,0)` has the ten individual bank risks `(1,1,1,5/8,1,53/80,5/8,1,1,3/4)`, hence worst-bank error exactly **5/8**. This H is a next exact optimization witness. The theorem here solves the stated S18-plus-full-J-edge population; the unrestricted 11-dimensional mother minimax continues to have the previously established interval `[1/2,2/3]` (k=4,6).

## Reproducibility and scope

Run `node VERIFY.js`: exact safe integer scale 50400, total-variation denominator 100800, original six source mixtures and common stochastic decoding groups. It checks all 18 risks, 111 triple-event certificates, 177147 free-label assignments, exact endpoint events, and three complete finite grids. Analytic convexity—not finite sampling—supplies continuous edge coverage. The attached RUN_EVIDENCE.json is the output of the exact code saved here. Author-side draft is not native CLAIM/Result or independent review.
