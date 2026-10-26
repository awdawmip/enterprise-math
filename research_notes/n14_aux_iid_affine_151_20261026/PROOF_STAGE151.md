# Stage151 — exact all-real N=14 auxiliary iid optimal segment

**Status:** AUTHOR exact finite computation-assisted proof, not independently reviewed, not a native Enterprise Math CLAIM/Result, and not a P000/X6/Heartbeat theorem.

## Statement and scope

Consider complete ordered-history randomized sequential policies on the ternary iid experiment, with horizon N=14,

\[
P=(1/8,1/24,5/6),\qquad Q=(1/12,1/12,5/6).
\]

Let \(e_P=P(\mathrm{decide}\ Q)\), \(e_Q=Q(\mathrm{decide}\ P)\), \(t_P=E_P[\tau]\), \(t_Q=E_Q[\tau]\), and let \(V_{14}(\alpha)\) minimize \(\max(t_P,t_Q)\) subject to both errors at most \(\alpha\).

**Exact theorem (all real parameters).** For every real

\[
0\leq\delta\leq \eta_{151}
=\frac{558936875}{141483470487552},
\]

\[
\boxed{V_{14}(\alpha_{150}+\delta)
=V_{150}-\frac{90040056}{127757}\delta,}
\]

where

\[
\alpha_{150}=\frac{18372793163552518325}{52808422392537808896},
\qquad
V_{150}=\frac{318819628004877985013}{26404211196268904448}.
\]

The new exact right endpoint is

\[
\boxed{\alpha_{151}=\frac{18373001785623238325}{52808422392537808896}},
\qquad
\boxed{V_{151}=\frac{318746112099955105013}{26404211196268904448}}.
\]

The corresponding affine dual support is **strictly below** \(V_{14}(\alpha)\) for every \(\alpha>\alpha_{151}\).

## 1. Bellman dual and all-ordered-history validity

For a count state \(s=(n,a,b)\), where a and b count the first and second symbols, each ordered prefix has likelihood ratio \(Q(\text{prefix})/P(\text{prefix})=2^{a+b}/3^a\). For positive K,L, define backward

\[
H(s)=\min\left\{K\frac{2^{a+b}}{3^a},\ L,\
1+\sum_{i=0}^2P_i H(s+e_i)\right\},
\]

omitting continuation at n=14. The three actions are decide P, decide Q and continue. Finite-horizon conditioning proves this Bellman recurrence gives the exact dual minimizer against **every** randomized policy depending on the complete ordered history: suffix laws and likelihood ratio depend only on (n,a,b), though actual paths must retain their order and multiplicity. Thus

\[
H(0,0,0)\le t_P+L e_P+K e_Q
\le\max(t_P,t_Q)+(K+L)\alpha .
\]

At

\[
K_{151}=\frac{45154992}{127757},\qquad
L_{151}=\frac{6412152}{18251}=\frac{44885064}{127757},
\]

exact arithmetic gives

\[
H_{151}(0,0,0)=
\frac{3601141501561668677150701}{13997190082164839940096}.
\]

Exhaustive exact Bellman enumeration covers all 680 count states. There are exactly two tied states:

* \(U=(9,4,1)\): decide P / continue;
* \(B=(11,0,1)\): decide Q / continue.

The other nonminimal state-action gaps number 1238, all strictly positive; their exact minimum is \(204027667/1716661610496\). There are no negative gaps. The dual-only candidate from Stage150 is thereby rechecked at its complete finite state scope.

## 2. Exact branch provenance and four observers

At B stop and decide Q with probability b; at U stop and decide P with probability u; elsewhere take the unique strict Bellman minimizer. These are coins in [0,1]. U is at depth 9 with a=4, while B is at depth 11 with a=0; U cannot reach B because a never decreases, and B cannot reach U because depth increases. Their literal ordered prefix cones are disjoint.

An independent integer-weight DFS of literal ordered prefixes (P weights (3,1,20)/24 and Q weights (1,1,10)/12) gives:

* B: 11 first-hit histories, P mass \(107421875/1451188224\), Q mass \(107421875/725594112\).
* U: 378 first-hit histories, P mass \(4375/2359296\), Q mass \(4375/5971968\).

For the observer \(M=(e_P,e_Q,t_P,t_Q)\), a Fraction-valued backward recursion, independently checked by literal-prefix integer DFS on all four deterministic corners, yields the **exact affine law**

\[
M(b,u)=M_{00}+b\,d_B+u\,d_U,
\]

with

\[
M_{00}=\left(
\frac{1212629741108379235}{3505953353861431296},
\frac{224481853556365}{641959232274432},
\frac{5331301420067770717}{438244169232678912},
\frac{70013062572629}{5944066965504}
\right),
\]

\[
d_B=\left(
\frac{4619140625}{2229025112064},
-\frac{751953125}{417942208512},
-\frac{25673828125}{278628139008},
-\frac{17939453125}{104485552128}
\right),
\]

\[
d_U=\left(
-\frac{100751875}{9393093476352},
\frac{153125}{9172942848},
-\frac{834281875}{391378894848},
-\frac{19656875}{20639121408}
\right).
\]

The mixed four-vector difference \(M(1,1)-M(1,0)-M(0,1)+M(0,0)\) is **exactly zero**. The signed observer increments are differences between positive branch masses; no signed cancellation is claimed as a BRC positive-mass operation.

The DFS visits respectively 519988, 496174, 519856 and 496042 ordered prefix nodes for the (b,u) corners (0,0), (0,1), (1,0), (1,1). All four exact observer coordinates agree with the separately structured backward recursion.

## 3. Complete real interval of primal attainment

The condition \(e_P=e_Q\) is equivalent to the exact compensation equation

\[
\boxed{b(u)=\frac{727663006224481}{740352000000000}
+\frac{300408507}{42416000000}\,u.}
\]

It is legitimate throughout every real \(0\le u\le1\): specifically

\[
0<b(0)=\frac{727663006224481}{740352000000000}
<b(1)=\frac{8061971501813291}{8143872000000000}<1.
\]

At u=0 the previous endpoint is recovered *exactly*, not assumed:
\(e_P=e_Q=\alpha_{150}\), \(t_P=V_{150}\) and

\[
t_P-t_Q=\frac{36808457207099213665}{79212633588806713344}>0.
\]

At u=1:

\[
e_P=e_Q=\alpha_{151},\quad t_P=V_{151},\quad
t_P-t_Q=\frac{36759675262851533665}{79212633588806713344}>0.
\]

The error increase is precisely \(\eta_{151}>0\), so every real alpha in the interval is reached with \(u=(\alpha-\alpha_{150})/\eta_{151}\). Both time differences are positive and affine in u; hence throughout \(t_P>t_Q\).

At both endpoints—and therefore everywhere, by affinity—

\[
t_P+L_{151}e_P+K_{151}e_Q=H_{151}(0,0,0).
\]

The Bellman lower bound is attained by these lawful randomized ordered-history policies, giving the exact value function and slope \(K_{151}+L_{151}=90040056/127757\).

## 4. Right endpoint is sharp

The finite ordered-history behavioral-policy space is compact and its observer map continuous, so an optimal policy exists. Suppose at some \(\alpha>\alpha_{151}\) it attained the same dual affine lower support. Since K,L>0, equality forces both errors to equal alpha and only Bellman-minimizing actions at all reached prefixes. All strict states have a unique action. At either tied count state, distinct first-hit ordered prefixes have a common Q/P likelihood ratio and identical conditional suffix distributions, so arbitrary history-dependent stop probabilities can be replaced by one P-mass-weighted effective coin, preserving **all four** observers. Because U and B have disjoint cones, the resulting observer lies in the above square \(M(b,u)\).

Error balance forces precisely b(u) above, and for 0<=u<=1 the common error cannot exceed \(\alpha_{151}\). Contradiction. Hence the affine dual support cannot remain optimal at any larger alpha. This sharpness argument does not determine the next segment.

## 5. Exact next dual frontier (not a primal theorem)

After u=1, hold B's Q/continue tie and take U strictly P-stop. The positive dual ray is \(dK=-1,\ dL=-112/129\). A complete rational directional-gap scan first closes at

\[
t_*=\frac{210556552344}{4643483645269},
\qquad W=(8,3,3)\ \text{(decide Q / continue)}.
\]

A fresh complete Bellman evaluation at this candidate gives

\[
K_{152}=\frac{12844717560}{36346217},\qquad
L_{152}=\frac{12768141608}{36346217},
\]

\[
H_{152}(0,0,0)=
\frac{341463027624594134301829727}{1327376472826305935572992}.
\]

The only ties are B=(11,0,1) Q/C and W=(8,3,3) Q/C, with 1238 strictly positive gaps, minimum \(204027667/1130512733568\), and zero negative gaps. **Stage152 is DUAL CANDIDATE ONLY**: no primal interval or right sharpness has been proved.

## 6. Verification, limits and immutable inputs

Three locally executed Python programs accompany this note: recursive exact Fraction Bellman/four-observer checker; independently structured iterative Bellman plus literal ordered-prefix integer DFS; and rational tangent scan. Their raw output and JSON evidence are retained. These programs establish the stated finite arithmetic if executed as supplied, with no floating-point dependence; they are two **author** methods, not an independent Research Driver review or formal proof-assistant check.

Fixed source inputs: GLOBAL_KNOWLEDGE_V1 canonical main@5a3cc94fb7e833c9f3a5a332d14ff94c1683d65f; Enterprise Math research input main@14497eb725037b01bf6ef2ec2ff5f82588f2d11d. P000 startup projection's original blob matched 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; ACTIVE worldview and current portable research protocol were read. Positive rational ordered branch provenance (BRC) is applied, with count compression limited to the declared iid observables.

Current connector GitHub principal is awdawmip. Native owner listing failed CONTROL_QUOTA. Own native Researcher session_start was refused STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Thus active Owner, formal session, CLAIM, Result and independent Driver review remain unverified. This is source-persisted AUTHOR evidence only, not a takeover of any live claim. No native X6 embedding/observer preservation proof is asserted.

Next unsolved scientific unit: compute W and B's genuine first-hit masses under Stage152 strict actions, test overlap and corner interactions, solve equal-error compensation and legal coins, and either prove the next full real interval or supply a precise obstruction.
