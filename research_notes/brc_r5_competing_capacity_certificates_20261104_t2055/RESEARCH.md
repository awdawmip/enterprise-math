# R5 competing-child simplex: exact convex hull and support certificates

Date 2026-11-04. Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Scientific parent and scope

R5 asks for a strictly positive finite two-measure P/Q BRC with equal complete four-observer convex hulls but unequal actual real-behavior images for FULL and seedless LR. This note establishes a complete support and endpoint calculus for an auxiliary competing-child occupancy geometry. A physical BRC implementation with all P/Q terminal declarations is a separate open obligation.

Predecessor (independent boxes, not competing capacity): enterprise-math immutable 7103131fbb688cec6dbf49afd6ca89b28d439ee7. Frozen scientific pins: Global a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. P000 and ACTIVE worldview remain unchanged. Source/path labels are kept distinct until a future-operation-safe observer equivalence is proven.

Let k >= 1, V be any real vector space, A, B_i, C_i in V. Write Delta_k = {y_i >= 0, sum_i y_i <= 1}. Define two **actual real behavior** images:

F = {x A + sum_i(y_i B_i + z_i C_i): 0<=x<=1, y in Delta_k, z in x Delta_k};
L = {x A + sum_i y_i (B_i + x C_i): 0<=x<=1, y in Delta_k}.

Thus child occupancies compete: sum z_i <= x; seedless LR additionally ties z_i = x y_i. These are auxiliary model definitions, not assumed identities for an arbitrary stochastic BRC.

## Theorem 1: finite exact convex-hull criterion in every dimension

Set B_0=C_0=0. Let

E_L = {B_i: i=0,...,k} union {A+B_i+C_i: i=0,...,k},
E_F = {B_i: i=0,...,k} union {A+B_i+C_j: 0<=i,j<=k}.

Then F=conv(E_F), conv(L)=conv(E_L). In particular, complete convex hulls agree if and only if **every cross endpoint A+B_i+C_j belongs to conv(E_L)**. In the finite coefficient span of dimension d this is a finite exact membership problem, and any feasible cross endpoint has a certificate using at most d+1 LR endpoints (Caratheodory). For rational data relative to a rational basis, exact rational linear feasibility gives rational mixture certificates; infeasibility has a rational separating functional.

Proof. Every point (x,y,z) in the convex FULL domain, for 0<x<=1, decomposes into (1-x)(0,y,0)+x(1,y,z/x). Both y and z/x lie in Delta_k. The x=0 image is conv{B_i}, and the x=1 image is A+conv{B_i}+conv{C_j}, whose pairwise Minkowski vertex sums yield E_F. Conversely every endpoint is attainable by a FULL policy; convexity of the domain implies F=conv(E_F). For LR,

xA+sum_i y_i(B_i+xC_i)
= (1-x)sum_i y_i B_i + x(A+sum_i y_i(B_i+C_i)).

This lies in conv(E_L). Both endpoint simplices belong to L by taking x=0 or x=1; hence its convex hull is exactly conv(E_L). Since L is contained in F, inclusion of the missing cross endpoints is necessary and sufficient for hull equality. QED.

## Theorem 2: universal exact support gap and distance certificate

For any real linear functional ell on span(A,B,C), let

a=ell(A), p_i=ell(B_i), q_i=ell(C_i),
S=max(0,p_1,...,p_k), Q=max(0,q_1,...,q_k),
T=max(0,p_1+q_1,...,p_k+q_k), D=S+Q-T >= 0, U=a+Q.

Then

h_F(ell)=S+max(0,U);
h_L(ell)=S+max(0,U-D);
gap(ell)=min(D,max(0,U)).

The gap is positive precisely when D>0 and U>0. For a maximizer W of the FULL support direction in a normed finite-dimensional observer space, dist(W,conv L)>=gap(ell)/||ell||dual when ell is nonzero.

Proof. Maximizing ell over the endpoint families from Theorem 1 gives h_F=max(S,a+S+Q), h_L=max(S,a+T). Since maximization over independently chosen indices dominates maximization over the same index, D>=0. Substitute T=S+Q-D and use max(0,U)-max(0,U-D)=min(D,max(0,U)) for D>=0. The distance bound follows by the dual norm inequality for every point of conv L. QED.

**Structural distinction from the prior independent-box formula:** the competing simplex yields max over child indices, where the independent-box model yielded sum of their positive parts. The new D need not be invariant under ell -> -ell, so the earlier sign-pair rigidity argument does not extend unchanged.

## Explicit exact separator

In V=R^2 choose A=(0,0), B1=(1,0), B2=(0,1), C1=(0,1), C2=(1,0). For ell(v)=v1-v2, (S,Q,T,D,U)=(1,1,0,2,1), so (hF,hL,gap)=(2,1,1). The legal FULL parameters x=1, y=(1,0), z=(0,1), satisfying both competing simplex capacities, attain W=(2,0). The l-infinity distance from W to conv L is at least 1/2.

## Hidden gate-residual without global image difference

Embed the scalar configuration A=-2, B1=1, B2=0, C1=0, C2=1 on one coordinate axis. Both global convex hulls are [-2,1]. Because the LR parameter domain [0,1] times Delta_2 is connected and its scalar image continuous, it reaches the whole interval; therefore the actual global images also coincide. However at fixed x=1 FULL reaches 0 via y1=z2=1, while LR is confined to [-2,-1]. Thus an unobserved gate-conditioned occupancy difference can survive when the globally observed image remains identical. A candidate mother witness must preserve the complete observable O4 and the relevant future operations before discarding source/path residuals.

## Exact computation and coverage

Executed standard-library Python exact integers and Fraction verifier. For all 9^5=59,049 assignments of (A,B1,B2,C1,C2) in 2D with each vector component in {-1,0,1}, monotone-chain exact hull membership (including degenerate point/segment cases) found 5,737 equal-hull assignments and 53,312 unequal-hull assignments. Zero discrepancies between finite cross-endpoint membership and direct exact hull comparison. Both support values were independently recomputed from all deterministic endpoints on four signed coordinate axes for every tuple. The worked separator, scalar hidden-gate example and 75 rational policies passed. Exact run tag: PASS_EXACT_R5_COMPETING_SIMPLEX_FINITE_HULL_AND_SUPPORT.

All-real theorems use the preceding proofs. The finite census only exhausts the declared 59,049-case integer box. No claim of a positive finite P/Q tree or R5 mother counterexample follows from the auxiliary model.

## Scientific literature comparison and next question

Anderson & Montufar, The Value Function Semi-Algebraic Set in Partially Observable Markov Decision Processes (ICML 2026, PMLR 306, https://proceedings.mlr.press/v306/anderson26a.html), describes semialgebraic feasible memoryless policy value sets. Its scope is infinite-horizon POMDPs, not the auxiliary theorem or mother BRC; it motivates checking polynomial image nonmembership beyond convex hull support.

Next: derive a physical two-measure positive finite tree where a shared stop/declare/continue key creates a genuine competing resource; retain source/path history and all P/Q declarations, then enumerate the exact four-dimensional O4=(eP,eQ,TP,TQ) deterministic policies. Use an exact rational convex certificate (at most five LR endpoints in four dimensions) or a rational strict separator. Only after hull equality test actual real-policy nonmembership. P000, ACTIVE worldview, scientific pins, owner and independent review scope stay preserved.
