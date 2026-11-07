# EC49AN — parameterized sharp BRC support beyond the first eta transition

2026-10-29. Author-side analytical proof with an executed exact-rational certificate. Status: PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## The exact claim

In the exact 18+18 strictly positive leaf auxiliary BRC observer inherited from EC49AM, set C1=43/48, k=177/172, alpha=P(accept), beta=Q(accept), H=alpha-k*beta. For **every real** eta in [41/1106, 1/20], every feasible second-stage purchase cost C2 and every lawful causal behavioral policy (fresh local random coins, hidden w erased after paid labeling),

    H <= B(eta) + lambda(eta) C2,
    lambda(eta) = (553/946) eta - 152/473 < 0,
    B(eta) = 22625/60544 - (13825/30272) eta.

The line is sharp, achieved by legitimate policies at C2=25/32 and C2=43/48 for every eta in the interval. Yet for **each** eta in the interval and every C2 strictly between these two costs, the fixed-C2 maximum is **strictly below** the line. In particular, a line that supports two attainable cost endpoints does not fill the intervening causal observation boundary.

The line agrees with EC49AM's support at eta=41/1106. The new eta-dependent slope and strict nonattainment of its interior are this increment. No formula for the exact fixed-C2 maximum in the open interval is asserted.

## Model, carriers, and causal scope

The hidden source label w is in {0,1,2}, u in {0,1}, z in {0,1,2}. Put t_eta(w,u)=1/2+(2u-1)(1-w)eta, and

    P(w,u,z)=t_eta(w,u)*(1/6 if z=w else 1/12),
    Q(w,u,z)=t_eta(w,u)/9.

Each distribution has 18 positive leaves and sums to 1 throughout the stated eta interval. At hidden w a policy chooses c in {A0,A1,B0,B1,STOP} with probability x[w,c]; independent local choices have costs (1,1,2,2,0), row sums 1 and sum_{w,c} cost(c)*x[w,c]=43/16. A paid label exposes only (c,u), not w or its seed; fresh purchase coin r(c,u) reveals z, and terminal acceptance is conditioned only on the actual observation. Exact C2 is sum_{paid(c,u)}r(c,u)T(c,u), where

    q_w(c,u)=x[w,c]*t_eta(w,u)/3, T=sum_w q_w,
    V(q)=sum_{z=0}^2 [43 q_z -16T]_+.

Here [a]_+=max(a,0). Purchased fibers have exact observed masses P_z=(T+q_z)/4, Q_z=T/3 and optimal H-contribution V(q)/172. STOP and no-sensor terminal fibers have equal P,Q masses; their best H contribution is zero (reject). This is positive-rational **auxiliary** BRC, not signed/phase cancellation or native X6/heartbeat dynamics.

## All-real support via two exact endpoints

For lambda=lambda(eta)<0, an arbitrary lawful strategy satisfies

    H-lambda*C2
      <= sum_{paid(c,u)} r(c,u)*(V(q)/172-lambda*T)
      <= D(x,eta) := sum_{paid(c,u)}(V(q)/172-lambda*T).

The second inequality is valid because the parenthesized term is nonnegative; it is strictly positive whenever T>0. For fixed eta, D is convex in x because every q is affine and V is a sum of positive parts of affine functions. The feasible x-polytope is a 3-fold 5-action simplex product sliced by the single cost hyperplane. It has no deterministic product vertices on this noninteger cost plane. Each vertex is an intersection of that hyperplane with an edge changing just one w row; exact enumeration produces 168 **distinct** vertices.

For fixed x, each q(c,u) is affine in eta, V is convex in eta, and sum_u T(c,u)=sum_w x[w,c]/3 is eta-independent. Consequently D(x,eta)=sum V/172-lambda(eta)*Cpaid(x) is convex in eta, where Cpaid(x) is eta-independent. B(eta) is affine. Therefore, checking D(v,eta)<=B(eta) for all 168 vertices at just the two eta endpoints suffices for **all real** eta in the entire interval and all real lawful x. The executed Fraction verifier checks 168*2=336 vertex inequalities (2688 paid observation fibers). It finds:

    eta=41/1106: max_v D=675/1892=B, 24 tight vertices;
    eta=1/20: max_v D=42485/121088=B, 16 tight vertices.

No interpolation of a finite eta grid is used: convexity supplies continuous coverage. All second-stage purchase/acceptance coins are included in the dual bound.

## Two lawful, source-verified equality witnesses

At low cost, use w0:A0, w1:A1, w2:(11/32)B0+(21/32)STOP, buy every paid sensor and accept only z=w of that pure label. The actual observation determines w for each paid label, so this terminal rule is legal. Exactly C1=43/48, C2=25/32, H=(27/172)*(25/32)=675/5504, at all eta.

At high cost, use w0:(11/16)A1+(5/16)STOP, w1:A0, w2:A1, buy each paid sensor. On A0 accept z=1; on A1,u=0 accept z=2; on A1,u=1 accept z=0 or 2. The z=0 coefficient on A1,u=0 is zero at eta=41/1106 and negative immediately beyond; the positive atoms remain as specified through eta=1/20. These choices depend only on (c,u,z), not hidden w. Exactly C1=C2=43/48, and

    H_high(eta)=1417/16512+(553/8256)*eta.

The affine line through (25/32,675/5504) and (43/48,H_high(eta)) gives exactly lambda(eta),B(eta). Row-local coins and the sensor purchase choice can be implemented independently without a retained shared seed. The verifier separately sums the original P/Q leaf masses for both witnesses.

## Stronger result: line equality is impossible at intermediate cost

With lambda<0, equality in H-lambda*C2<=D requires r=1 on every positive-mass paid fiber and optimal terminal decisions. Thus C2=Cpaid(x). If D(x,eta)=B, any convex decomposition of x into polytope vertices can involve only tight vertices. At eta=41/1106 the verifier classifies all 24 tight vertices as 12 with Cpaid=25/32 and 12 with Cpaid=43/48; at eta=1/20 the 16 tight vertices are 12 low and 4 high. Every eta strictly between the endpoints has its tight vertices drawn from the **intersection** of the two endpoint-tight sets, by convexity in eta. This intersection is precisely those 12 low and 4 high vertices.

For a low vertex v and high vertex h, let g_vh(eta)=B(eta)-D((v+h)/2,eta). The verifier enumerates all 144 low-high midpoint pairs at eta=41/1106 and all 48 at eta=1/20 and finds every gap positive, with respective minimum gaps 41/16512 and 321/110080. The 48 pairs relevant at both endpoints therefore have g_vh>0 throughout the interval: g_vh is concave in eta, since B is affine and D is convex. At the first endpoint, the 144-pair check covers the additional high vertices as well.

If x had positive weights on a low and high tight vertex, write their positive common weight into a positive multiple of their midpoint and use convexity; the strict midpoint gap forces D(x,eta)<B. Hence equality is possible only at the two endpoint paid costs. The finite-dimensional legal policy space at fixed eta,C2 is compact and H is continuous; each intermediate cost is feasible (e.g. w1:A0,w2:A1,w0:A1 with probability p, B0 with probability (11/16-p)/2, STOP otherwise, p=6(C2-25/32)). Therefore the actual fixed-cost maximum is strictly below the supporting line for every 25/32<C2<43/48.

## Verification, provenance, and scope

Executable: VERIFY.py (Python 3, stdlib Fraction). Actual output: EXACT_REPORT.json; asserts 168 vertices, 336 exact dual inequalities, 2688 observation fibers, 192 strictly positive low-high midpoint cases at the two endpoints, 18+18 leaf normalization, all source-level legal witness equations, and three interior eta spot checks. The complete real-quantifier proof uses the analytic convexity reductions above; the numerical certificate itself is finite exact arithmetic. Author-side result only: independent Driver review, formal Source registration/CLAIM/Result and mathematical admission require their real protocols. Protected P000 and ACTIVE worldview remain unchanged. Native signed BRC, X6 and heartbeat transfer require a separately typed provenance-preservation proof.
