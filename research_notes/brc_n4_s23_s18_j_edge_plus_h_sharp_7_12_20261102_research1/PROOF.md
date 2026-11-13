# BRC N=4, S23: sharp 7/12 on S18, an entire real J-edge, and H(1/4)

**2026-11-02 · author proof and exact computation · UNREVIEWED / NOT_ADMITTED.**
Scientific input remains frozen at `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Continue the original S18 + full real J-edge theorem at author commit `0075a2ad5a49aa433ad8be6df05cded243f39075`.

## Exact theorem

Let `S18={W,J,A,B,C,X,Y,Z,T1,...,T8,U,V}` be the eighteen legal eleven-parameter policies specified by the frozen BRC model and reproduced in `VERIFY.js`. Set
[
J(t)=(1,t,0,0,0;0,0,0,0,1,0), qquad 0le tle1,
]
and `H=(1/4,1,0,0,0;1,0,0,0,0,0)`. All eleven coordinates are probabilities. For seven original, fixed common decoders `D1,D2,D3,D4,D6,D7,D8` and three freely chosen arbitrary **real** row-stochastic four-by-four common kernels, define `L_D(z)=max_i TV(P_i(z),Q_i(D))` on the six original prepared source labels. Then
[
oxed{inf_{K_1,K_2,K_3} sup_{zin S18cup J([0,1])cup{H}}
   min_{Din{D1,D2,D3,D4,D6,D7,D8,K_1,K_2,K_3}}L_D(z)=rac7{12}.}
]
The previous S18 + J-edge value was `4/7`. Adding H increases the optimum by exactly `1/84`.

## Typed original observer and causal law

Use the six separately labeled sources `AU0,AU1,AV,BU0,BU1,BV` and the same shared causal coordinate `b_U`. An unmixed source with parameters a,b,c has the four-stop distribution
[
F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)).
]
The positive source mixing is the six-by-six matrix `M20/20` with rows
`(10,10,0,0,0,0)`, `(9,11,0,0,0,0)`, `(0,0,20,0,0,0)`, `(0,0,0,10,10,0)`, `(0,0,0,2,18,0)`, `(0,0,0,0,0,20)`. The four common decoder group rows `AU,AV,BU,BV` induce the six source rows as `(AU,AU,AV,BU,BU,BV)` before the same M20 mixing. No source identity, joint coupling, or common-kernel constraint is dropped.

## Lower bound: ten-point exact source-event certificate

The following **ten legal witness policies** lie in the theorem's population:
`W, B, Y, Z, T5, U, V, H, J(1), J(1/6)`.
All seven fixed decoders have minimum risks on these ten policies, respectively:
[
(1,1,1,1,1,1,1,5/8,1,7/12).
]
For a claimed common radius `r<7/12`, each witness must consequently use one of the **three free kernels**.

For any three witnesses a,b,c using the same free kernel and any original prepared source i, select for each stop atom the largest of `P_i^a,P_i^b,P_i^c`. Summing positive deviations from the one common decoder distribution gives
[
3r ge sum_{j=1}^{4}max(P_i^a(j),P_i^b(j),P_i^c(j))-1.
]
Thus a triple is forbidden to share a free label whenever its best source makes the right-hand side at least `3*(7/12)=7/4`.

Using exact original six-source fractions, **87 of all 120 triples** satisfy this condition. The self-contained verifier exhausts all `3^{10}=59049` assignments of the ten witnesses to three labeled free kernels. **Each assignment contains at least one monochromatic forbidden triple** (minimum hit count 1). This is an exhaustive finite combinatorial fact, computed with exact integers and checked independently in the author-side Python Fraction reconstruction. Hence no three real stochastic kernels can attain radius strictly less than `7/12`.

## Upper bound: three explicit common stochastic kernels

In row order `AU,AV,BU,BV`, stop-atom column order `1,2,3,4`, take
```text
K1 = 5/12 0 7/12 0; 5/12 5/12 0 1/6; 5/12 0 1/6 5/12; 5/12 55/126 0 37/252
K2 = 1/2 1/2 0 0; 1/2 0 0 1/2; 0 0 1/2 1/2; 0 0 1/2 1/2
K3 = 0 1/2 1/2 0; 0 1 0 0; 0 1 0 0; 0 0 1/2 1/2
```
All rows are nonnegative and sum to 1. `VERIFY.js` evaluates the original six prepared source mixtures for every policy in S18 plus H; all nineteen min-bank risks are at most `7/12`, with equality for W, Z and H.

For the entire real continuum J(t), all six prepared source rows are **affine in t**. Therefore the maximum of their six total-variation distances to any one fixed decoder is convex in t. Exact endpoint values:
[
L_{K2}(J(0))=L_{K2}(J(1/3))=1/2,
]
[
L_{K1}(J(1/3))=L_{K1}(J(1))=7/12.
]
Thus K2 covers the whole real interval `[0,1/3]` at radius at most `1/2`, and K1 covers `[1/3,1]` at radius at most `7/12`. This proves the continuum upper bound and closes the exact theorem.

## New next-step counterexample for this particular bank

The legal strategy `H(1/5)=(1/5,1,0,0,0;1,0,0,0,0,0)` lies on the neighboring real H-edge. The **specific ten-decoder bank above** has individual exact risks
`(1,1,1,3/5,1,16/25,3/5,19/30,1,1)`, giving min-bank risk exactly `3/5`, larger than `7/12` by `1/60`. The next optimization adds H(1/5), optionally the full H-edge, and constructs a new bank or a stronger lower-bound certificate.

## Execution, evidence and scope

Run `node VERIFY.js`. The source is the exact function executed in the connected V8 runtime during this research turn. It uses integer probability scale `50400`, total-variation denominator `100800`, checks all divisions, all 19 finite risks, four real-edge endpoints, 87 source-event certificates, all 59049 labeled colorings, stochastic row normalization, and the H(1/5) counterexample. See `RUN_EVIDENCE.json` for the complete execution record. The continuum result follows from the analytic convexity argument above; the finite execution verifies its stated exact certificates. This is an author-side mathematical artifact, not an accepted native Result or independent review.

The unrestricted ten-label eleven-real-parameter mother minimax retains its earlier documented bounds `[1/2,2/3]` for `k=4,6`; this theorem gives an exact value on the named fixed-seven/free-three witness population.
