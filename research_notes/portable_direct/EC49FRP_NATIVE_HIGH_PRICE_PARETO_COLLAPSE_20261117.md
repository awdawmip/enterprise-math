# EC49FRP — Exact high-price two-tree Pareto basis for original native BRC class 16943

Date: 2026-11-17. Frozen input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Predecessors: EC49FRJ/FRK/FRL and EC49FRO (PR #2636). Evidence status: AUTHOR_PROVED / EXACT_FINITE_CHECKED_TWICE / NOT_REVIEWED.

## The finite native model

Keep all 310 original configurations, 141 complete named physical-response states with positive integer multiplicities m_i (sum 310), and all 228 named physical observations (144 terminal observations priced t>0, 84 root observations priced r=xt). Every permitted deterministic tree identifies all 141 profiles without error. For any tree Q define U_R,U_T as unweighted sums of root/terminal observations on all named state paths and M_R,M_T as the same sums weighted by original multiplicities. The original real prior is p_i(lambda)=(1-lambda)/141+lambda*m_i/310 with 0<=lambda<=1.

Normalized expected cost:
C_Q(x,lambda)/t=(1-lambda)(U_T+x U_R)/141 + lambda(M_T+x M_R)/310.

Two original, fully replayed legal named decision trees are
D=(U_R,U_T,M_R,M_T)=(4,296,4,707),
E=(4,298,4,688).
These have (U_3,M_3)=(308,719) and (310,700), respectively, where U_3=U_T+3U_R and M_3=M_T+3M_R.

**Theorem.** For every legal original deterministic complete identifying tree Q, there is one T in {D,E} such that C_T(x,lambda)<=C_Q(x,lambda) **simultaneously for every real x>=3 and every real lambda in [0,1]**. In particular D,E form a complete pointwise Pareto-dominating basis among ALL original named deterministic trees. The result also reduces any prior-blind randomized mixture over arbitrary trees to a mixture of D,E without increasing any expected cost.

This is stronger than the previously established lower envelope V=min(D,E): it eliminates a possible unsupported but prior-robust intermediate tree.

## New finite native parity computation

At x=3 and beta=620/3299,
(1-beta)/141=19/3299 and beta/310=2/3299.
For each tree, the integer weighted Bellman cost is
Phi(Q)=3299*C_Q(3,beta)/t=19 U_3(Q)+2 M_3(Q).
Consequently Phi(Q) mod 2 = U_3(Q) mod 2.

For a subset S of named states define w_i=19+2m_i and W(S)=sum_{i in S}w_i. For p in {0,1}, B_p(S) minimizes the integer cost of an identifying subtree on S **subject to the parity p of the unweighted price-three path sum**. On singleton S, B_0(S)=0 and B_1(S)=infinity. For every informative original physical observation q with price c_q=1 (terminal) or 3 (root), let S_{q,y} be its nonempty response fibers within S. The exact unrestricted recurrence is

B_p(S)=min_q { c_q W(S) + min_{XOR_y p_y = p XOR (c_q |S| mod 2)} sum_y B_{p_y}(S_{q,y}) }.

Every informative action partitions S into strictly smaller child subsets; by induction the recurrence covers all legal complete original trees of arbitrary finite depth. Since every action has positive cost, an uninformative query can be deleted from an optimum. Identical partitions may be coalesced only within the same price class.

**Exact freshly computed result on all 141 profiles:**
B_0(ALL)=7290 and B_1(ALL)=7311.

Two implementations verified this result directly from the archived exact BRC original master SHA256 cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e and raw profile costs SHA256 a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f. The first reconstructs all 228 observations and quotients to 209 same-price identical partitions; the second independently re-parses the 94-family master and all raw CSV costs, retaining ALL 228 observations with no quotient. Each exact min-plus parity DP memoized 12,922 reachable nontrivial/subtree subsets, and each returned (7290,7311). Fully replayed native witness trees have, respectively,
even: (U_R,U_T,M_R,M_T)=(4,298,4,688), Phi=7290;
odd: (4,299,4,689), U_3=311, M_3=701, Phi=7311.

The second implementation additionally **recomputed**, without reusing old endpoint claims, the unrestricted minima min_Q U_3=308 and min_Q M_3=700. Full original D and E trees were replayed along all 141 named physical-response paths.

## Proof of Pareto domination

Original terminal observation signatures have exactly two distinct non-singleton fibers {8,139} and {46,140}; all four profiles have original multiplicity 1. To identify both profiles in either fiber, any complete tree must query a root observation on every member's path; consequently U_R>=4 and M_R>=4. This uses the original full response profiles, without any new state collapse.

Now fix an arbitrary legal Q. The freshly computed unrestricted exact endpoint minima imply U_3(Q)>=308 and M_3(Q)>=700. The parity DP implies 19U_3+2M_3>=7290; if U_3 is odd, it instead implies >=7311.

- U_3=308: 19*308+2M_3>=7290 forces M_3>=719, so D weakly dominates both endpoint costs.
- U_3=309: odd-parity bound 19*309+2M_3>=7311 forces M_3>=720. D=(308,719) strictly dominates both.
- U_3>=310: M_3>=700, so E=(310,700) weakly dominates both.

No other U_3 is possible. Thus D or E dominates Q at x=3 in **both** uniform and multiplicity endpoint costs. For any real x>=3, U_x(Q)=U_3(Q)+(x-3)U_R(Q)>=U_3(Q)+4(x-3), and similarly M_x(Q)>=M_3(Q)+4(x-3). D and E each have exactly four root counts in both weightings, so the previously chosen domination persists at all x>=3. An arbitrary prior's expected cost is a nonnegative affine combination of these endpoint costs, so the same D/E tree dominates for every lambda. QED.

The odd-parity fact is essential: prior scalar anchors alone allow a hypothetical intermediate vector (U_3,M_3)=(309,710), which would escape D/E pointwise domination. The new exhaustive parity certificate rules that vector and all U_3=309 with M_3<=719 out.

## Exact minimax regret on every closed prior subinterval

Let beta=620/3299 and kappa=3299/43710=2/141+19/310. D and E tie at beta for all real x>=3, with D optimal on lambda<=beta and E on lambda>=beta. Their regret curves are

C_D/t-V/t = kappa max(0,lambda-beta),
C_E/t-V/t = kappa max(0,beta-lambda).

For ANY real 0<=a<b<=1, the unrestricted deterministic prior-blind minimax regret over lambda in [a,b] is precisely

R_det(x;[a,b]) =
kappa * min(beta-a,b-beta)   if a<beta<b,
0                            otherwise.

Select D if b-beta<=beta-a, otherwise E. This is exact for every x>=3, independent of price x. For prior-blind pre-observation randomized policies, pointwise replacement reduces every mixture to D/E. Balancing the two endpoint regrets gives

R_rand(x;[a,b]) =
kappa * (beta-a)*(b-beta)/(b-a)  if a<beta<b,
0                                 otherwise,

attained with probability P(D)=(beta-a)/(b-a). On a strict crossing interval the exact ratio R_rand/R_det equals max(beta-a,b-beta)/(b-a). A symmetric interval around beta therefore yields 50% lower minimax regret with randomization. For the full prior interval [0,1], the deterministic regret is 2/141 and the prior randomized/deterministic ratio is 2679/3299, consistent with EC49FRO.

Proof: the D/E regret curves are piecewise affine and nonnegative. For a fixed tree regret is convex in lambda (tree cost affine, Bellman V concave), so its interval maximum occurs at an endpoint. Pointwise domination lets us compare only D and E and take the lesser of their worst endpoint regrets. The same replacement argument reduces randomized strategies to D/E mixtures; minimizing the maximum of two affine endpoint regrets gives the displayed balancing probability. The one-chamber intervals have zero regret because one of D or E stays Bellman-optimal everywhere. QED.

## Evidence, limitations, and continuation

The self-contained evidence archive contains the frozen original master and raw source CSV, the original native profile reconstruction module, two separately implemented unrestricted Bellman computations (including an all-228 implementation), full even and odd witness decision trees, original fully replayed D/E trees, a rational interval verifier covering 275 triples (x,a,b), execution logs, and a SHA256 file manifest. The finite experiments validate the code and numerical premises; the explicit integer argument proves the continuous-real theorem. Neither proof checker nor two runs imply independent mathematical review or formal Foundation admission.

This is an exact, original finite *typed BRC response/observer* theorem under frozen model assumptions. It does not assert full X6-state equivalence under future observers, a new spatial coordinate, or universality for unmodelled physical actions. P000 and the ACTIVE residual-fidelity worldview are unchanged.

Next question: classify analogous unsupported Pareto candidates in 1<=x<3 using appropriately lifted (price,profile-count,parity) Bellman certificates; then test higher-dimensional original prior polytopes and altered observation availability/cost classes.

Control: independent portable research. A repository commit/PR does not grant native publication, active CLAIM, Result, Review, Activity write, or mathematical admission.
