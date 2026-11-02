# Stage384-B — Independent continuous-domain audit of Stage378→379 cusp-strip exclusions

Research2 / portable author-side mathematical audit · 2026-11-02 (Asia/Shanghai). This is an **independent reconstruction of two earlier signed-support certificates** from their raw CSV leaves; it does not invoke the previous generation/replay programs. It is a conditional link in the global-localization proof, not an independently admitted global theorem.

## Source and hypothesis scope

The scientific freeze is unchanged: GLOBAL `main@bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math `main@2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Applicable behavioral context was separately read in this run at GLOBAL main `687acac8f5b397055b2a97434bb1498733eace32` and EM main `49771cae2ad2742dbce64eea865a202ddc7b1ef0`. The incremental parents are Stage378 `c139cf4af6f3f5a954434139468127a3521ce85f` and Stage379 `3dd97cbe4ff6eb293a10d937b59bb976acdb7cdb` in Draft PR #1736. Stage383 `52994e593adc86a19c457e7bedd70edfc8f82146` had audited the *later* Stage380 local Pareto lemma.

The original auxiliary problem has `B_k(z)=z^k(1-z)^(3-k)`, weights `w=(1,3,3,1)`, target `(m_k)=(61,21,9,9)`, and four distinct residuals

\[r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160}.\]

Let `D(a,z)=1/2 sum_k w_k |B_k(a)-B_k(z)|`, `b(x,y)=5/32 sum_k w_k|r_k(x,y)|`, and `c(x,y)=[63D(1/4,x)+D(3/4,x)+9D(1/4,y)+7D(3/4,y)]/256`. The full objective is `33/1024+c(P)+c(Q)` subject to `b(P)+b(Q) <= B*=2 beta*+11/5000`. **No audited term or residual is removed.**

The inherited **Stage377 hypothesis** is that every global minimizer can be swapped into `P∈(.2308,.2345)×(.55,.56)`, `Q∈(.2365,.239]×(.5756,.576)`. This run independently certifies the later two incremental refinements; Stage377 and its earlier global exclusion chain remain an open independent verification obligation.

## Proposition — exact two-stage conditional exclusion

Every feasible point in either of the following stage-specific closed Q strips, with P in the closed common P rectangle, has strictly higher cost than an explicit original-model feasible rational reference configuration:

* Stage378 with `lambda=97/80`: `Q_LO=[.2365,.239]×[.5756,.57565]`, `Q_HI=[.2365,.239]×[.57575,.576]`.
* Stage379 with `lambda=483/400`: `Q_LO=[.2365,.239]×[.57565,.57566]`, `Q_HI=[.2365,.239]×[.57574,.57575]`.

For both, `P=[.2308,.2345]×[.55,.56]`. Therefore, conditional on Stage377's global containment, every global minimizer satisfies `Q_y∈(.57566,.57574)`, with both new endpoints excluded.

## Exact certificate proof

Let `L_lambda=c+lambda*b`, with positive rational lambda. For every term separately, choose a midpoint sign `s∈{-1,0,1}` and use `|u|>=s u`, valid on the **entire** closed leaf regardless of any sign crossing. This yields an exact separable cubic support:

\[L_\lambda(x,y)\ge K+\sum_{k=0}^3 A_k B_k(x)+\sum_{k=0}^3 H_k B_k(y),\]

with `A_k=w_k[lambda*s_r/8-(63*s_xa+s_xb)/512]`, `H_k=w_k[lambda*s_r/32-(9*s_ya+7*s_yb)/512]`, and `K=sum_k w_k[((63*s_xa+9*s_ya)*B_k(1/4)+(s_xb+7*s_yb)*B_k(3/4))/512-lambda*m_k*s_r/1024]`. The present checker derives these coefficients **independently in the ordinary power basis** using only the raw original formulas and signs; it does not import the preceding `coeff`, `lower` or `setup` routines.

For a cubic `f` on `[a,b]`, its four Bernstein–Bézier controls are `f(a)`, `f(a)+(b-a)f'(a)/3`, `f(b)-(b-a)f'(b)/3`, `f(b)`. Every value is a convex combination of those controls, giving an exact continuous lower bound. Summing two bounds plus K proves a lower bound for every real `(x,y)` in the leaf. All divisions are rational.

The checker reconstructs each leaf rectangle **from the binary split path** (split the wider coordinate, x first on a tie), requires exact equality to its CSV coordinates and recorded bound, verifies every bound strictly exceeds its corresponding threshold, checks uniqueness and complete prefix-tree coverage, and rechecks total exact area. Thus the result is not a floating-point mesh.

The common reference pair `P_ref=(.23113910,.55568442)`, `Q_ref=(.23780690,.57569391)` has original-model variable cost exactly

`C_ref=16174336378406867755705673/256000000000000000000000000`.

Original four-residual evaluation verifies its budget below `2 beta_lower+11/5000`. The unique simultaneous `r0=r1=0` root lies within `x∈(231083940,231083942)/10^9`, `y∈(555508852,555508864)/10^9`: `r0` decreases in both coordinates, `r1` increases in x and decreases in y; strict opposite-face tests prove existence and uniqueness by monotone intersection/Poincaré–Miranda. Since `r2>0>r3` there and `sum w_k r_k=0`, `beta*=15 r2/16`. The monotonicity of `r2` on the isolating rectangle gives `2 beta*+11/5000 < B_UP=97582683/10^10`.

For any budget-feasible `(P,Q)` in an excluded strip,

`c(P)+c(Q) = L(P)+L(Q)-lambda*(b(P)+b(Q)) > TP+TQ-lambda*B_UP > C_ref`.

The two exact strict comparison gaps `TP+TQ-[C_ref+lambda*B_UP]`, in order lower/upper, are:

- Stage378: `4149273132244294327 / 256000000000000000000000000` and `309273132244294327 / 256000000000000000000000000`.
- Stage379: `19084697132244294327 / 256000000000000000000000000` and `7564697132244294327 / 256000000000000000000000000`.

All four fractions are strictly positive. Since a feasible rational pair has cost `C_ref`, no global minimizer satisfying Stage377's necessary box can lie in these four strips.

## Actual execution and evidence

The self-contained `REPRO_STAGE384B_INDEPENDENT.py` was executed with the prior Stage378 and Stage379 raw CSVs. Return: `STAGE384B_INDEPENDENT_STAGE378_STAGE379_CHAIN_PASS`. The exact Stage378 CSV has 794 covered leaves (637+57+100) and SHA256 `1c7552cc6ae40cb133faee01b59b47329e4357691bb58e7198cabda2b5a826bc`; Stage379 has 1453 (1344+37+72), SHA256 `aa48034a214df51a493d387862e12d05eed5b18681299574f41264656262d828`. **2247 leaves checked, zero uncovered.** The expanded rational diagnostics and exact minimum margins are in the captured execution output. The scientific proof uses exact midpoint signed supports and continuous polynomial convex-hull bounds, not numerical root sampling.

These CSV sources were supplied by the prior run and are identified by immutable digests; use the already published Stage378/379 regeneration programs and their stated original digests to obtain them. This audit's checker requires those two CSV paths as arguments. The original project generators and the independent verifier use separate implementations.

## Actual research state and next discriminating question

This is a **proved conditional exact certificate / independently reconstructed two-stage local exclusion**, not a clean-independent Driver review and not a global completion proof. Stage377's entire global-exclusion chain and the inherited Stage381 uniqueness theorem need separate validation; the latter also inherits Stage379/380. The precise next unit is **Stage385-B: independently reconstruct and audit the Stage377 closed Q-low exclusion and its Stage376 predecessor**, or find an exact original-model feasible counterexample to the earliest failing inequality. Preserve all original 16 audit labels and four residual channels. The P000 X6 three-dimensional-slice embedding, third coordinate and declared future-observer preservation remain open.
