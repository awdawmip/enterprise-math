# R5: Exact equality of FULL_HIST and seedless LR on the entire stopping-time boundary

Date: 2026-11-06 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Scope and frozen scientific inputs

R5 asks for a strictly positive finite rational P/Q stopping tree with equal four-observer FULL_HIST and seedless LR convex hulls but different *actual* real-behavior observation images. This theorem is for the inherited delta=1/4 four-stage auxiliary BRC likelihood-ratio model, not native Heartbeat X6 dynamics. Scientific pins unchanged: GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Exact model and J scalar gate: EM 57f7d654e5dd002567e0b0d333937e6e38f3b4cb. Exact time octagon: EM d648610de1a56f155d3a0d3caef37cd2ce0ca415. Complementary prior common-image tube: EM b1c446234454563d587dd61e090f08106ba4deb6. The earlier four-observer hull equality certificate is inherited author-side and was not independently rerun.

Let W=(e_P,e_Q,T_P,T_Q), g=root continuation, u_i=g*a_i (i=0,1), V_j=(q3[0,j]*u_0+q3[1,j]*u_1)/2, 0<=X_j<=V_j (j=0,1,2), with q3[0]=(13/20,1/5,3/20) and q3[1]=(1/40,9/20,21/40). The six-flow occupancy polytope D has 0<=g<=1, 0<=u_i<=g, 0<=X_j<=V_j, with affine projection

T_Q=1+g+(u_0+u_1)/2+X_0+X_1+X_2,
T_P=1+g+(3u_0+5u_1)/8+X_0/2+X_1+3X_2/2.

The history-sensitive central terminal coefficient J satisfies
J_lo=max(alpha*X_1,beta*X_1-d*A), J_hi=min(beta*X_1,alpha*X_1+d*B),
where A=u_0/10, B=9u_1/40, alpha=47/180, beta=67/162 and d=beta-alpha=247/1620. The common LR continuation must satisfy F=(A+B)*J-X_1*(alpha*A+beta*B)=0. The two models have identical aggregated stop-ratio masses, and therefore identical attainable binary-declaration errors, whenever they share (g,u_0,u_1,X_0,X_1,X_2,J).

## Theorem — full real-image equality on all time-boundary fibers

Let H_T be the common convex octagon of time pairs from the predecessor. For **every** (t_P,t_Q) in its topological boundary partial H_T,

{(e_P,e_Q):(e_P,e_Q,t_P,t_Q) in O4(FULL_HIST)}
= {(e_P,e_Q):(e_P,e_Q,t_P,t_Q) in O4(seedless LR)}.

More strongly, on each time-boundary point the six occupation flows are uniquely determined by (t_P,t_Q), and the FULL_HIST admissible J interval is a singleton equal to the seedless LR J. Hence a real-image separation witness for this fixed model must have (T_P,T_Q) in the **strict interior** of H_T. Previous results independently require e_P+e_Q != 1 and place it outside the guaranteed common-image tube.

## Proof

1. **Exact finite flow reduction.** D is the convex hull of the 64 deterministic six-key timing occupancy vectors indexed by (g,a0,a1,z0,z1,z2) in {0,1}^6. This follows from successive conditional action splitting on the finite acyclic tree and linearity of occupation mass under mixture. Conversely, any feasible D is realized by g,u_i/g,X_j/V_j, with arbitrary legal actions at zero-mass keys. FULL_HIST can pool its history-dependent flows to D without changing its time pair, so the same D describes all FULL time projections.

2. **Eight time facets and exact enumeration.** The H_T halfspaces, written a*T_P+b*T_Q>=c, are:
(-282,323,41),(-160,160,-41),(-216,188,-139),(-2,1,-4),(2,-3,-4),(236,-274,-179),(80,-80,-23),(146,-123,23).
The eight counterclockwise time vertices and their *unique* six-flows (g,u0,u1,X0,X1,X2) are

v0=(1,1): (0,0,0,0,0,0);
v1=(483/160,221/80): (1,0,1,0,0,21/80);
v2=(519/160,239/80): (1,0,1,0,9/40,21/80);
v3=(613/160,293/80): (1,1,1,0,13/40,27/80);
v4=(4,4): (1,1,1,27/80,13/40,27/80);
v5=(559/160,293/80): (1,1,1,27/80,13/40,0);
v6=(211/80,117/40): (1,1,0,13/40,1/10,0);
v7=(203/80,113/40): (1,1,0,13/40,0,0).

Exact enumeration of the 64 deterministic timing vectors gives 26 distinct time images. Every vector satisfies all eight inequalities; each facet is saturated by *exactly two distinct occupation-flow vectors*, those belonging to its adjacent vertices. Facets 1 and 8 have 33 nominal policies due to choices at unreachable nodes, but still only two distinct flows. VERIFY.py checks each exact rational equality and inequality.

3. **Unique boundary flow.** If t is on a facet, any convex decomposition of its six-flow into deterministic occupancy vectors must only use facet-tight vectors, because every term is on the same side of the inequality. By step 2, these are exactly its two endpoint vectors. Their distinct time coordinates uniquely determine the interpolation coefficient, hence uniquely determine the six-flow at t. This also covers vertices.

4. **The J interval collapses.** On facets 1 through 8 respectively, the following affine identities hold at both endpoint flows and therefore throughout the whole interpolating segment:
X1=0; A=0; X1=A+B; X1=A+B; X1=A+B; X1=A+B; B=0; X1=0.
If X1=0 then J=0; if X1=A+B then J=alpha*A+beta*B; if A=0 then J=beta*X1; and if B=0 then J=alpha*X1. The four FULL inequalities defining J_lo,J_hi each collapse to the same unique value in the indicated cases, and in every case F=0 exactly (including A+B=0). Thus every FULL time-boundary flow has the same terminal stop-ratio histogram as a valid seedless LR flow.

5. **Exact declaration reconstruction.** For each ratio r in {1/10,1/2,3/4,1,5/4,3/2,19/10}, let M_r be the shared stopped Q mass and ell_r in [0,M_r] the FULL Q mass declaring P. Use in LR the common ratio declaration t_r=ell_r/M_r when M_r>0, arbitrary otherwise. This gives e_Q=sum ell_r and e_P=1-sum r*ell_r exactly, with unchanged time coordinates. The LR image is always contained in FULL. Therefore the two time-boundary fibers coincide. QED.

## Exact verification, relevance, next unit

VERIFY.py uses only Python stdlib Fraction. Exhaustively checks 64 deterministic timing policies, 26 distinct time points, eight exact facet inequalities, all exact facet-tight policies and endpoint degeneracies; checks single-valued J and F=0 at six rational interpolants per facet (the all-real claim follows from affine identities, not sample testing). Actual output is EXACT_OUTPUT.txt and ends PASS_EXACT_R5_ALL_TIME_BOUNDARY_FIBERS_EQUAL.

The result eliminates the *entire time boundary* (not just the eight vertices) from the current model's counterexample search, independently of the earlier balanced slice. Next test rational W in the full four-dimensional hull whose time coordinates satisfy all eight inequalities **strictly** and whose error sum lies outside the guaranteed nonbalanced LR tube. For each, form the complete seven-variable K(W) and globally determine min/max of the one quadratic F with exact algebraic certificates. Status: author proof plus exact finite enumeration, no independent Driver admission or formal R5 CLAIM.
