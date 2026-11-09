# PREFIX-645-R6 — All-order Poisson-to-native cumulant transfer and an exact negative-skewness witness

Date: 2026-11-10 (Asia/Shanghai). Research mode: independent TASK_RESEARCH; no formal shared-task CLAIM. Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Status: \`AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED\`.

## Exact question and scope

The preceding PREFIX-622/631/639–644 signed two-informative-direction BRC first-stop *statistical observer* has a Poissonized informative stopping time \`Y\` and native discrete action count \`T_q\`, with native sampling slots \`q=12\` and \`q=24\`. The established relation \`Var(T_q)=q² Var(Y)-q E[Y]\` uses only the first two cumulants. Determine the exact higher-order relation; calculate at least one nontrivial signed-cumulant witness on the frozen 189-layer observer without rerunning the original 96-port native dynamics.

The informative marked action stream has a total embedding Poisson intensity \`q\`; action marks determine the stopping index \`T_q\`, independent of the exponential interarrival times. Each informative direction in the Poissonization has unit rate. Consequently, conditional on the marked discrete path and on \`T_q=m\`, \`Y\` is a sum of \`m\` independent \`Exp(rate=q)\` waiting times. All q below are real parameters for which the frozen marked-action probability law exists (\`q>=12\` suffices). The 189 informative-arrival stopping cap and positive informative mark probabilities ensure exponential moments near zero.

## Theorem 645.1 — Exact transform for every cumulant order

Let \`K_X(t)=log E[e^(tX)]\` and \`κ_r(X)=K_X^(r)(0)\` for an integer \`r>=1\`. Then, in a neighborhood of zero,

\`K_Y(s)=K_(T_q)(-log(1-s/q))\`, and equivalently

\`K_(T_q)(t)=K_Y(q(1-e^(-t)))\`.

Writing \`S(r,j)\` for Stirling numbers of the second kind and \`c(r,j)\` for the unsigned Stirling numbers of the first kind gives the exact inverse pair

\`κ_r(T_q)=sum_(j=1)^r (-1)^(r-j) S(r,j) q^j κ_j(Y)\`;

\`q^r κ_r(Y)=sum_(j=1)^r c(r,j) κ_j(T_q)\`.

In particular:

- \`κ_1(T_q)=q μ\`;
- \`κ_2(T_q)=q² W-q μ\`;
- \`κ_3(T_q)=q³ C3-3q² W+q μ\`;
- \`κ_4(T_q)=q⁴ C4-6q³ C3+7q² W-q μ\`,

where \`μ=E Y\`, \`W=Var Y\`, and \`C_r=κ_r(Y)\`. The r=2 identity recovers the existing PREFIX-622 variance relation; orders 3 and 4 and the all-order invertible transform add distributional information without requiring a new native graph computation.

**Proof.** Condition on \`T_q=m\`. Independence of interarrival times and marks gives \`E[e^(sY)|T_q=m]=(q/(q-s))^m\`, hence the first cumulant-generating identity. Substitute \`s=q(1-e^(-t))\` to invert it. Expanding \`K_Y(s)=sum_(j>=1) κ_j(Y)s^j/j!\` and using \`(1-e^(-t))^j=j!sum_(r>=j)(-1)^(r-j) S(r,j)t^r/r!\` yields the first all-order formula. Standard inverse Stirling transform, or substitution \`K_Y(s)=K_T(-log(1-s/q))\`, yields the inverse. These identities hold as analytic germs about zero; no global MGF-domain extension is asserted. QED.

## Lemma 645.2 — Third and fourth cumulants from the original 189 layers

Let \`n,m=0,...,188\`, \`s_n(u)=sum_k row[n,k]u^k(1-u)^(n-k)\` be the frozen survivor polynomials, \`w_nm=binom(n+m,n)/2^(n+m+1)\`, and \`a_j(n,m)=(n+m+1)_(j-1)/2^(j-1)\`, where the parenthesized product is rising and \`a_1=1\`. For \`j=1,...,4\` define the tail-moment coefficient

\`R_j = sum_n (n+1)...(n+j-1) [s_n(p)+s_n(z)] - sum_nm w_nm a_j(n,m) s_n(p)s_m(z)\`.

An empty product equals one. The independent unit-rate Poisson informative clocks have survivor expansions \`e^(-t)sum_n s_n t^n/n!\`; the survival of their maximum is the sum of the two survivals minus their product. Integrating \`t^(j-1)\` gives the exact identity \`E[Y^j]=j R_j\`. Thus \`μ=R_1\`, \`H=R_2\`, \`J=R_3\`, \`L=R_4\`, with

\`W=2H-μ²\`,

\`C3=3J-6μH+2μ³\`,

\`C4=4L-12μJ-12H²+24μ²H-6μ⁴\`.

These formulas are finite rational sums on the frozen 189-layer state and retain the signed branch survivor coefficients. They need neither numerical integration nor classical trigonometric arithmetic. QED.

## Exact finite witness at p=1/6, z=19/128

The companion executable, using only standard-library exact integers and Fraction, regenerates all dyadic-width survivors: first stop at n=25, \`sum row[24]=2^24\`, \`sum row[25]=2^25-2\`, and complete extinction after n=189. At this point it evaluates the four finite raw moments and the two cumulant transforms. Strict rational brackets:

\`108 < μ < 109\`, \`336 < W < 337\`, \`-1210 < C3 < -1209\`, \`50374 < C4 < 50375\`;

\`-2234220 < κ_3(T_12) < -2234219\`, \`1057438820 < κ_4(T_12) < 1057438821\`;

\`-17299552 < κ_3(T_24) < -17299551\`, \`16814644408 < κ_4(T_24) < 16814644409\`.

Thus native stopping counts for **both actual slots exhibit strictly negative third cumulant** at this pinned parameter point, while the fourth cumulant is positive. Since \`C3<-1209\`, \`W>336\`, \`μ<109\`, the polynomial \`κ_3(T_q)/q=q² C3-3q W+μ\` is negative for **every real q>=12** for which the marked statistical observer is defined. Likewise \`κ_4(T_q)>0\` for q>=12 using \`C4>50374\`, \`-C3>1209\`, \`W>336\` and \`μ<109\`. These are exact special-case distributional results, not assertions of uniform skewness over all \`(p,z)\`.

An independent toy-model sanity certificate uses two equally rare marked types, each probability \`1/q\` per action, stopping when both appear once. The Poissonized maximum is \`Exp(2)+Exp(1)\`, so \`κ_r(Y)=(r-1)![1+2^(-r)]\`. The discrete action count is independently \`Geom(2/q)+Geom(1/q)\`. All four cumulant orders match the Stirling transform exactly for q=12 and q=24.

Execution: \`python PREFIX645_R6_CUMULANT_TRANSFER_CERTIFICATE.py\` produced \`ALL_CHECKS_PASS 190 layers 2 q slots four cumulant orders\`, including exact sign brackets and inverse transform. Rational six-decimal containing intervals and display values are in \`PREFIX645_R6_RESULTS.json\`. This remains author verification, not independent review.

## BRC interface, status and next problem

BRC carrier: pinned two signed informative-direction prefix-count rows; retained observations: per-direction survivor probabilities, exact arrival-time maximum and native-action stopping index; future operations here: marked thinning, cumulants and their generating-function composition. This **does not** identify these signed statistical moments with full native phase-cancellation or physical residuals. The frozen 96-port model has not been rerun.

The mother target remains the **global two-parameter sampling-variance maximum**. The next discriminating question is whether the third-cumulant polynomial has a parameter-uniform sign on the certified local valley strip, or an exact sign-change witness, using bounded bivariate Bernstein/interval evaluation. In parallel, continue the PREFIX-644 bivariate convexity extension; neither route's absence of global completion negates this finite-point theorem.

Sources: frozen PIN above; PREFIX-631 \`cab564fd9a112feed4a5a1fac0ee5556ebe7d7b6\`; PREFIX-639 \`6acbf4f472a48d846859a71a31af243808961cff\`; PREFIX-644 \`5344b1fcfca30449e5fc154b1c1deb7a118833b3\`. Formal CLAIM/Result/Review: not created.
