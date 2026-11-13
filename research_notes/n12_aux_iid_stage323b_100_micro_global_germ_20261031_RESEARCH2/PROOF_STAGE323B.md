# Stage323-B — exact 100-micro eight-rate Pareto germ

**Research state:** TASK_RESEARCH portable author proof, \`UNREVIEWED / NOT_ADMITTED\`. This is not a Source-native CLAIM, frozen Result, independent review or a P000-X6 physical realization. Date: 2026-10-31 (Asia/Shanghai).

**Frozen global startup:** \`awdawmip/chatgpt-global-knowledge@e5bebac1166355c7161a96ec58dddac4224a8c11\` (canonical main), including \`00_BOOTSTRAP.md\`, \`OPERATING_MANUAL.md\`, P000 projection and original, ACTIVE worldview, mathematics/BRC rules and research routing. **Project control:** \`awdawmip/enterprise-math@65dc54f38e9821efead22da100db2e6c40cfc4ef\` (canonical main), P000 V5, native X6 and \`docs/PORTABLE_RESEARCH_PROTOCOL.md\`. Scientific predecessor: Stage322-B, \`749c5739e2594139d98925146c6c7497e4d6daca\`, PR #1736, still author-only. Earlier named dependencies at their original author-only proof status: Stage307-B.2 (unique algebraic public minimizer and root brackets), Stage315-B (central-rate MAP reset), Stage316-B (two-source block infimal convolution). No stronger independent-admission claim is made.

## Exact model

Two positive hidden sources and eight locked Bernoulli ports, with three future independent Bernoulli accesses. The public observer is \`(W,Y)\`; the source-tagged observer is \`(S,J,W,Y)\`. For \`k=0,1,2,3\` let

\`B_k(z)=z^k(1-z)^(3-k)\`, \`p=(61,21,9,9)/160\`,
\`r_k(x,y)=(4/5)B_k(x)+(1/5)B_k(y)-p_k\`,
\`d(x,y)=(1/2)sum_k binom(3,k)|r_k(x,y)|\`,
\`b(x,y)=(5/16)d(x,y)\`, and

\`c(x,y)=[63 D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)]/256\`.

Here \`D_3(a,t)\` is the total variation distance of three-trial Bernoulli word laws with probabilities \`a\` and \`t\`. Under the named earlier source theorems, the complete eight-parameter objective reduces *exactly* to
\`P_3=b(x,y)+b(x',y')\`, \`T_3=33/1024+c(x,y)+c(x',y')\` with four central MAP-reset rates. The unique public minimizer \`(x_*,y_*)\` has \`r_0=r_1=0\`, \`r_2>0\`, \`r_3<0\`, and strict rational brackets

\`231083940855521/10^15 < x_* < 231083940855522/10^15\`,
\`555508857277/10^12 < y_* < 555508857278/10^12\`.

Set \`beta_*=b(x_*,y_*)\`, \`P_min=2 beta_*\`, and \`C_3(s)=min_{b(x,y)<=s} c(x,y)\`.

## Theorem 323B: doubled nonzero global Pareto interval

For **every real** \`0<=epsilon<=delta=1/10000\`, the complete eight-parameter constrained optimum is

\`F_3(P_min+epsilon)=33/1024+c(x_*,y_*)+c(x_epsilon,y_epsilon)\`,

where \`(x_epsilon,y_epsilon)\` is the unique rightward \`r_1=0\` kink point with \`b=beta_*+epsilon\`. When \`epsilon>0\`, there are exactly two full eight-rate optimizers, corresponding to the two assignments of all added public budget to one external source block. At \`epsilon=0\`, the tagged optimum is unique. In the complete interval, the single-source envelope obeys the strict continuum curvature bound

\`-46 < C_3''(s) < -34\` for \`beta_*<s<beta_*+delta\`.

For all \`0<theta<epsilon<=delta\`, the cost penalty for dividing the public-error budget is strictly bounded by

\`34 theta(epsilon-theta) < C_3(beta_*+theta)+C_3(beta_*+epsilon-theta)-C_3(beta_*)-C_3(beta_*+epsilon) < 46 theta(epsilon-theta)\`.

This doubles Stage322-B's \`delta=1/20000\`. The interval endpoint is **only a rigorously certified radius**, not a proved first global branch-switch location.

## Lemma 1: new exact global exterior certificate

Use the rational rectangle

\`R=[57/250,469/2000] x [109/200,567/1000]=[0.228,0.2345] x [0.545,0.567]\`.

Let \`w=(231083940855/10^12,555508857277/10^12)\`, \`U=d(w)\`. Since \`(x_*,y_*)\` is the global minimizer, \`U>=d(x_*,y_*)\`.

The four closed rational exterior strips
\`[0,57/250]x[0,1]\`,
\`[469/2000,1]x[0,1]\`,
\`[57/250,469/2000]x[0,109/200]\`,
\`[57/250,469/2000]x[567/1000,1]\`
cover the complement of the open interior of \`R\` in the real unit square.

For any rational rectangle \`A=[a,b]x[c,e]\`, enclose each cubic \`B_k\` exactly using values at interval endpoints and, when included, the unique internal critical point \`k/3\` for \`k=1,2\`. This yields rational residual bounds \`[ell_k,u_k]\`. Define the rigorous lower enclosure

\`L(A)=(1/2) sum_k binom(3,k) max(0,ell_k,-u_k) <= inf_A d\`.

Repeatedly bisect the longer side until \`L(A)-U>(16/5)delta=1/3125\`. The attached Python \`Fraction\` checker exhaustively certifies, by exterior strip, \`(visited nodes, accepted leaves)\` equal to

\`(239,120), (79,40), (37,19), (221,111)\`.

Thus there are **290 accepted closed rational leaves**. The smallest accepted exact lower-gap value is

\`403455758784686813453557268618433 / 1250000000000000000000000000000000000\`,

which exceeds \`1/3125\` by the positive rational

\`3455758784686813453557268618433 / 1250000000000000000000000000000000000\`.

Consequently \`d(x,y)-d(x_*,y_*)>1/3125\` outside the interior of \`R\`, and thus \`b(x,y)-beta_*>delta\`. Every feasible individual block with budget at most \`beta_*+delta\` lies strictly inside \`R\`.

## Lemma 2: rigorous local branch geometry on all of R

Partition \`R\` into a closed **32 x 32 grid** of **1024** rational tiles. For each tile, compute interval extensions with endpoints in \`Q\`, retaining sign-sensitive powers, reciprocal sign checks, and the exact polynomial gradients.

The executable certificate establishes for *every real point in R*:

1. \`r_2>0\`, \`r_3<0\`. The zero-sum residual identity gives \`d=3r_2+[r_0]_+ + 3[r_1]_+\` and four complete smooth sign chambers.
2. All 16 Bernoulli TV sign comparisons are strict across R, permitting exact \`c_x=-(1-x)(189-183x)/256<0\` and \`c_y=3y(1-y)/64>0\`, without hidden TV kinks.
3. In the four smooth chambers, \`det(grad b,grad c)\` is strictly positive only for \`(e0,e1)=(0,0)\` and strictly negative in the remaining three. Therefore no smooth interior constrained minimum occurs on a regular public-error contour.
4. On the kink curves \`r_0=0\` and \`r_1=0\`, \`r_{j,y}<0\`, \`|dy/dx|<14\`, and the other residual crosses strictly monotonically. Thus the two kinks meet only at the already unique root within R.
5. Along all four oriented kink arms, \`|db/dx|>4/25\` when measured away from the root. The slope \`dc/db\` lies in disjoint rational open intervals:
   \`r_1/right=(-5/4,-11/10)\`;
   \`r_0/right=(-1,-4/5)\`;
   \`r_1/left=(17/10,19/10)\`;
   \`r_0/left=(27/10,7/2)\`.
   The rightward \`r_1=0\` branch is uniquely cheapest at every matching positive budget.
6. Implicitly differentiate \`r_1(x,y(x))=0\`: \`v=y'=-r_{1x}/r_{1y}\`, \`w=y''=-(r_{1xx}+r_{1yy}v^2)/r_{1y}\`. With \`B=b(x,y(x))\` and \`E=c(x,y(x))\`, \`d^2E/dB^2=(E'' B'-E' B'')/(B')^3\`. The checker bounds this strictly in \`(-46,-34)\` on every tile.

Each numerical bound is rational interval enclosure over a whole tile, not a finite grid evaluation. The only finite search is the exhaustive cover; its soundness follows from inclusion monotonicity and the elementary cubic extremum rule.

## Global minimization and exact budget allocation

The prior root brackets place \`(x_*,y_*)\` in the interior of R. Let \`h=7/10000\`. The checker certifies \`h\` is smaller than each x-margin and \`14h\` smaller than each y-margin to the rectangle boundary. Therefore all four kink arms exist to \`x_* +/- h\` without leaving R. The strict error derivative gives an achieved public-error rise greater than \`(4/25)h=7/62500 > delta\` along each outward arm.

No feasible positive-budget minimizer can leave R by Lemma 1. No minimizer can leave budget unused because \`c_x<0\` locally and R is open at every feasible point. No smooth chamber boundary minimizer exists by the nonzero determinant; hence only kink arms remain. Their strict slope ordering from their common root makes rightward \`r_1=0\` the unique minimizer at each single-block budget. Its strict negative curvature makes \`C_3\` strictly concave, so the two-block exact infimal convolution has only endpoint allocations (all slack in exactly one block). Integrating the curvature bounds twice gives the displayed strict \`34/46\` quantitative allocation penalty. The unique central MAP reset and source-block interchange finish the eight-rate statement, **conditional on the specifically cited Stage307/315/316 mathematical dependencies**.

## Verification, interpretation and remaining obligations

\`REPRO_STAGE323B.py\` executes with standard Python 3 and exact \`fractions.Fraction\` arithmetic. Its complete executed stdout is in \`REPRO_STAGE323B_EXECUTED_STDOUT.txt\`, with final marker \`STAGE323B_100_MICRO_GLOBAL_GERM_EXACT_PASS\`. New checks: 290 exterior leaves, 1024 full interval tiles, 16 TV signs, four determinant/slope chambers, negative curvature and kink reach. Independent exact reruns can check the complete script. This run does not re-prove Stage307-B.2, Stage315-B, Stage316-B, nor constitute Lean verification or an independent mathematical review.

The external probability-model observers and Bernoulli ports do not supply a native realization of P000's six-axis X6 signed path algebra, selected three-dimensional slice including the third coordinate, triadic closure, separately typed time, or six-field lossless Cell-address map. Every such observer-preserving native bridge remains explicitly open.

**Next scientific question:** Stage324-B should either extend the rational exterior-and-tile method to a rigorously larger \`delta\` or produce a strict full-law competitor identifying genuine optimizer change. Distinguish the true switch from the exhaustion of this particular local certificate. Do not repeat Stage323's already verified 290-leaf/1024-tile calculation as a new theorem.
