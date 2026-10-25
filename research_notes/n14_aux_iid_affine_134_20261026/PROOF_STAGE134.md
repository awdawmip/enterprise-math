# Stage134 | N=14 ternary iid exact optimal affine interval

Status: AUTHOR_EXACT_FINITE_MODEL_PROOF; two independent-in-implementation AUTHOR checkers executed locally; UNREVIEWED / NOT_NATIVE_CLAIM / NOT_ADMITTED. This is an **external auxiliary iid** statistic, not a P000/Heartbeat/X6 result.

## Exact theorem

For iid symbols 0,1,2 under P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=14, let every possibly randomized sequential policy observe the entire literal ordered history, stop by N and declare P or Q. Put eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=inf max(tP,tQ) subject to both errors <= alpha.

Consume the author-verified Stage133 endpoint
alpha133=36703010861169506695/105616844785075617792,
V133=656403116242184147227/52808422392537808896.

For **every real** 0<=delta<=eta134=71274875/1273351234387968,

$$
\boxed{V_{14}(\alpha_{133}+\delta)=V_{133}-\frac{93320536}{81457}\,\delta.}
$$

The right endpoint and its exact value are

$$
\boxed{\alpha_{134}=\frac{36703016772992738695}{105616844785075617792}},\qquad
\boxed{V_{134}=\frac{656399729826573779227}{52808422392537808896}}.
$$

The supporting line is right-sharp: at larger alpha the same line is strictly below the true optimum; feasibility itself is not asserted to fail.

## Universal dual proof

At count state s=(n,a,b), n<=14, the Q/P likelihood ratio is r=2^(a+b)/3^a, identical for all literal ordered prefixes with that count. Set K=48012912/81457, L=45307624/81457, and compute exactly in P units

$$
H(s)=\min\{Kr_s,\;L,\;1+\tfrac18H(n+1,a+1,b)+\tfrac1{24}H(n+1,a,b+1)+\tfrac56H(n+1,a,b)\},
$$

omitting continuation at n=14. An exhaustive exact Fraction backward induction checks 680 reachable count states, 1238 strictly positive nonchosen-action gaps, zero negative gaps, minimum positive gap 129758627/4504246272. Only the following two states have action ties:

B=(11,0,1): declare Q versus continue;
G=(9,3,3): declare Q versus continue.

The exact root value is H(0,0,0)=2442656918158809916870213/5949675882197721022464. By backward induction on **each literal ordered prefix** (not a restriction to count-based policies), for any randomized strategy

$$
H(0,0,0)\le t_P+Le_P+Ke_Q\le\max(t_P,t_Q)+(K+L)\alpha.
$$

Every positive-gap action has strict excess dual cost at each positively visited prefix and cannot appear in an equality policy.

## Exact BRC provenance and two-tie family

Use the positive-rational weighted BRC carrier of literal sample histories, keeping full order, branch identity, stopping depth and separate P/Q mass until evaluation of the four observers M=(eP,eQ,tP,tQ). This is only the declared *external iid* carrier, not signed cancellation and not a native X6 quotient.

An independently structured integer-product DFS enumerates actual literal first-hit words along strict Bellman choices, using P symbol numerators (3,1,20) over 24 and Q numerators (1,1,10) over 12:

B=(11,0,1): 11 first-hit words, P mass 107421875/1451188224, Q mass 107421875/725594112.

G=(9,3,3): 756 first-hit words, P mass 875/14155776, Q mass 875/5971968.

The two actual history cones are disjoint: at depth9 G has three zeros, so it cannot reach depth11 B with zero zeros; B cannot precede G because it is deeper. Let w be the probability of declaring Q at B and z the probability of declaring Q at G, each otherwise continuing. Since a history never encounters both, the **full-real** four-observer identity is exactly M(w,z)=M00+w*dB+z*dG, with no wz term, for all 0<=w,z<=1.

Exact vectors obtained independently from bottom-up Fraction and literal integer DFS at all four deterministic corners:

M00 =
(2431513653068080769/7011906707722862592,
 447002527473041/1283918464548864,
 10923564086046461711/876488338465357824,
 1276450324742933/106993205379072).

dB =
(4619140625/2229025112064,
 -751953125/417942208512,
 -25673828125/278628139008,
 -17939453125/104485552128).

dG =
(193375/347892350976,
 -93625/247669456896,
 -11265625/130459631616,
 -1255625/6879707136).

Direct comparison yields M11-M10-M01+M00=(0,0,0,0). The literal DFS visits respectively 736690,704938,736558,704806 prefixes at (w,z)=(0,0),(0,1),(1,0),(1,1), and 491127,469959,491039,469871 distinct terminal words. These are exhaustive deterministic integer enumerations, not Monte Carlo observations.

## Full real primal saturation

Solving eP=eQ in the above exact affine vector equation yields

$$
\boxed{w(z)=\frac{29148450914061437}{81438720000000000}
-\frac{4650723}{19280000000}z,\qquad0\le z\le1.}
$$

Both w(0)=29148450914061437/81438720000000000 and w(1)=29128806260109437/81438720000000000 lie strictly in (0,1). Hence this is a legal policy for every real z in the full closed interval. Exact substitution gives

$$
e_P(z)=e_Q(z)=\alpha_{133}+\frac{71274875}{1273351234387968}z,
$$

$$
t_P(z)=V_{133}-\frac{10206933625}{159168904298496}z.
$$

The exact positive endpoint margins tP-tQ are

z=0: 88899829683689096807/158425267177613426688;
z=1: 88912023540183944807/158425267177613426688.

Affinity preserves tP>tQ throughout the interval. Every chosen action is a Bellman minimizer, so the dual root inequality is an equality along the family:

$$
t_P+Le_P+Ke_Q=H(0,0,0).
$$

Since K+L=93320536/81457, the universal dual lower bound and this saturating primal family prove the stated optimum for every real delta in the interval.

## Sharpness for arbitrary full-history coins

The finite-horizon behavioral-policy space is compact and its four observers continuous, so a minimizing policy exists. If any alpha>alpha134 attained the *same* supporting line, equality in both dual inequalities would force eP=eQ=alpha and Bellman-minimizing actions everywhere on visited prefixes. Exactly 1238 strict gaps rule out all flexible actions except B and G. Although tie coins may depend on ordered first-hit prefixes, each prefix with a given tie count has identical likelihood ratio and conditional iid continuation. For the four declared observers, its coins collapse exactly to a P-first-hit-mass-weighted average in [0,1]. The B/G cones are disjoint, so this generates precisely the two-coin moment family above.

Error balancing therefore enforces w(z) and alpha=alpha133+eta134*z<=alpha134 for z∈[0,1], a contradiction. The affine supporting line is right-sharp over **unrestricted literal ordered-history randomized** strategies.

## Evidence, authority and next work

Actually executed locally: exact 680-state Fraction bottom-up Bellman/dual/four-corner checker and an independently coded recursive-optimum + complete literal integer DFS checker. Both passed, including four-corner vectors, first-hit masses, exact endpoints, time margin and dual identities. Author-side exact finite proof is not independent Driver review. No native Source CLAIM, Result freeze, native P000 physical inference or Working Truth/Foundation acceptance is claimed.

Source read: GLOBAL_KNOWLEDGE_V1 main@0640165130b1a9268805f3ee02e8fb88ecfe368e (same frozen bootstrap/manual/P000/ACTIVE); EM canonical input main@56f75ca89dc8a07824e0c02200dcc41fff6a9133, with prior Stage133 proof/authority preserved. Native dispatch attempt returned CONTROL_QUOTA, so active Owner and current native CLAIM were not verified. This file is noncanonical author research evidence only.

Next Stage135: at z=1 G always declares Q, while B remains mixed. Recompute the next exact Bellman dual ray and first new tie, retaining same source/role constraints, then derive the next four-observer interval and exact right sharpness. Do not infer Stage135 from a dual gap alone.
