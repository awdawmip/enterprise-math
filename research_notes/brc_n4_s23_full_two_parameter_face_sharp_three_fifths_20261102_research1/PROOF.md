# BRC S23 exact 3/5: full two-parameter real strategy face

Date 2026-11-02. Frozen scientific input `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Reuses exact lower source-event certificate and rational bank from PR #1765, previously at `6b7d90cb199a14983c492124730706c1289bc985`.

## Theorem: an entire real square

Preserve the original six separately labeled positive sources `AU0,AU1,AV,BU0,BU1,BV`, shared causal b_U and M20/20 mixing, seven fixed common decoders D1,D2,D3,D4,D6,D7,D8, and three arbitrary real row-stochastic free common decoders K1,K2,K3. Let `S18` be the existing 18 legal strategies and `J(t)=(1,t,0,0,0;0,0,0,0,1,0)` for each real t in [0,1]. Define a legal two-dimensional real face

`H(s,t)=(s,t,0,0,0;1,0,0,0,0,0)`, all real `s,t in [0,1]`.

With `L_D(z)=max_{i=1..6} TV(P_i(z),Q_i(D))`, the fixed-seven/free-three exact minimax is:

`inf_{K1,K2,K3} sup_{z in S18 ∪ J([0,1]) ∪ H([0,1]^2)} min_{D in {D1,D2,D3,D4,D6,D7,D8,K1,K2,K3}} L_D(z) = 3/5.`

The H(s,1) boundary is the previous entire H(s) real edge; this theorem covers every interior real (s,t) point too. It is a model-internal author analytical proof, with exact finite verification, not an accepted native Result.

## Original observer and two-coordinate exact dependence

For the original unmixed four-stop law `F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c))`, use source selectors `A=[0,0,0,1,1,1]`, `B=[2,2,3,2,2,4]`, `C=[5,6,7,8,9,10]` and M20 rows `(10,10,0,0,0,0)`, `(9,11,0,0,0,0)`, `(0,0,20,0,0,0)`, `(0,0,0,10,10,0)`, `(0,0,0,2,18,0)`, `(0,0,0,0,0,20)`, divided by 20. The common decoder group rows AU,AV,BU,BV expand to AU,AU,AV,BU,BU,BV before mixing.

For the H(s,t) face, the six original **unmixed** source distributions are exactly

`(s,0,1-s,0); (s,0,0,1-s); (s,0,0,1-s); (t,0,0,1-t); (t,0,0,1-t); (t,0,0,1-t)`.

Applying the unchanged positive source mixing, the six **observed** distributions are affine jointly in (s,t). More generally, for any rectangle `[s0,s1]×[t0,t1]`, every prepared row at interior (s,t) is a **convex combination of its four corner rows**, with bilinear weights `(1-u)(1-v),u(1-v),(1-u)v,uv`, `u=(s-s0)/(s1-s0)`, `v=(t-t0)/(t1-t0)`. For any fixed decoder D, the maximum over six sources of the TV distance is convex in the prepared distributions. Consequently, if one decoder D has `L_D<=3/5` at all four corners of a rectangle, that **same D covers the entire real rectangle** at radius <=3/5.

## Rational upper construction: 25 exact rectangles

The fixed decoders are retained from the frozen bank. The three free kernels are exactly those in the preceding theorem's VERIFY.js (also reproduced in the new self-contained verifier):

`K1 = [(2/5,0,3/5,0),(2/5,2/5,0,1/5),(2/5,0,0,3/5),(3/5,2/5,0,0)]`;

`K2 = [(1/2,1/2,0,0),(1/2,0,0,1/2),(0,0,1/2,1/2),(0,0,1/2,1/2)]`;

`K3 = [(0,1/2,1/2,0),(0,1,0,0),(0,1,0,0),(0,0,1/2,1/2)]`.

Each row is a stochastic stop-atom distribution. The old exact result shows all S18 and J([0,1]) covered at radius <=3/5: K2 for J[0,2/5], K1 for J[2/5,1]. For the whole 2D face, partition the unit square into `5×5=25` rectangles `[a/5,(a+1)/5]×[b/5,(b+1)/5]`, `a,b in {0,1,2,3,4}`. The finite certificate below lists **one common decoder** whose maximum six-source risk across the four exact corners is at most 3/5. Rows are s intervals in increasing order; columns are t intervals in increasing order.

| s-row / t-column | [0,1/5] | [1/5,2/5] | [2/5,3/5] | [3/5,4/5] | [4/5,1] |
|---|---|---|---|---|---|
| [0/5,1/5] | D1≤1/2 | D1≤1/2 | D1≤3/5 | D4≤3/5 | D4≤3/5 |
| [1/5,2/5] | D1≤1/2 | D1≤1/2 | D1≤3/5 | K1≤3/5 | K1≤3/5 |
| [2/5,3/5] | D1≤3/5 | D1≤3/5 | D1≤3/5 | K1≤21/50 | K1≤3/5 |
| [3/5,4/5] | K2≤1/2 | K2≤1/2 | K1≤3/5 | K1≤51/100 | K1≤3/5 |
| [4/5,5/5] | K2≤1/2 | K2≤1/2 | K1≤3/5 | K1≤3/5 | K1≤3/5 |

The only covering decoders needed for these 25 squares are D1, D4, K1 and K2. The listed fractions are exact corner maxima, not rounded measurements. The rectangle convex-combination argument proves the upper bound for **all real pairs** without an unresolved mesh gap.

## Exact real-kernel lower bound

The preceding ten legal strategies `W,X,Y,Z,T5,U,V,H(1/5),J(1),J(1/5)` remain in the new population, because `H(1/5)=H(1/5,1)`. Their minima against the seven fixed decoders are `(1,1,1,1,1,1,1,3/5,1,3/5)`. For any r<3/5, all ten must use one of three free kernels. The original source-event inequality

`3r >= max_{i=1..6} [sum_{j=1..4} max(P_i^a(j),P_i^b(j),P_i^c(j)) - 1]`

for three strategies sharing a decoder yields 84 forbidden monochromatic triples out of 120. An exhaustive integer check of all `3^10=59049` labeled assignments gives at least one forbidden monochromatic triple in every assignment. Thus r<3/5 is impossible for arbitrary real kernels. Combining with the explicit rational upper construction gives exact value 3/5.

## Reproducibility and next scientific question

`VERIFY.js` runs in V8 with exact safe integers, common base probability scale 50400 and total variation denominator 100800. It independently checks the 6×6 vertex source distributions, all 25 complete rectangle certificates, 36 two-coordinate bilinear reconstruction identities, S18 and J upper, the ten witness lower and every one of the 59049 three-label colorings. The actual execution record is `RUN_EVIDENCE.json`. The universal real-parameter conclusion is the analytic convexity argument on these exact vertex certificates. Proof/authorship is not an independent project review or native mathematical acceptance.

This exact fixed-seven/free-three subproblem remains distinct from the full eleven-real-coordinate ten-label mother problem, whose previous bounds remain `[1/2,2/3]` for k=4 and 6.

Next: examine genuinely larger two-parameter faces with **nonconstant causal b** or nonzero third stop parameter so that source dependence is multi-affine or includes interactions; test exact square/triangle covers and extract new lower witnesses where a fixed common decoder cannot cover the branch interactions.
