# CBRC F7 Driver r452 — Reflected old-axis matching triples primitive support density

Date: 2026-11-21 (+08:00). Continuing Driver scientific contribution line: EM-DVR-DEBB5E. This independently derived mathematical subunit uses prior Driver r451 and the original frozen F7 scalar model of EM-CBRCF7-83A1D4 (Result RR-AA38973D56330E59D315). The original author, frozen Result, native Review, Task and P000 are unchanged. Status: a proof under stated F7 assumptions with exact finite combinatorial checks, not an operational review/admission.

## Unchanged F7 premises

A=I+uv^T with u=(1,1,-1,-1)^T, v=(1,-2,-1,2)^T. For z=(a,b,c,d), put T=a-2b-c+2d and Az=(a+T,b+T,c-T,d-T). The scalar q:Z^2->[0,infinity) satisfies q(0,0)=0, q(-x,y)=q(x,y), q(s,0)=1 when s !=0, q(x,y)>=1/2 for all nonzero (x,y), and the fixed (not propagated) marks q(2,1)=q(-1,-1)=1/2.

D_q(z)=q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(a,b)-q(c,d); E(q)=sup_{z in Z^4}|D_q(z)|. On nonzero pairs let delta=q-1/2. Take 0<=epsilon<1, E(q)<=epsilon and alpha=1-epsilon.

For L>=3 use **the identical** original r449/r451 region

\[
\Omega_L=\{(x,y)\in\mathbf Z^2:x>0,\ y\ne0,\ \gcd(x,|y|)=1,\ x\le3L-2,\ |y|\le L-1\}.
\]

Write X=3L-2, and for positive integers t and U put C_t(U)=#{1<=s<=U:gcd(s,t)=1}. Define

\[
U_t=\max(X-3t,3t-1),\qquad
H(L)=\sum_{t=1}^{L-1} C_t(U_t)+1-\mathbf1_{\{L\ge4\}}.
\]

## Theorem: reflected axis pairs

Under the above premises, **at least H(L) distinct primitive points** of Omega_L satisfy q(x,y)>=1-epsilon/2. For every convex nondecreasing Psi:[0,infinity)->[0,infinity) with Psi(0)=0,

\[
\sum_{\Omega_L}\Psi(\delta(x,y))
\ge 2\Psi(\alpha)+2(H(L)-2)\Psi(\alpha/2).
\]

In particular,

\[
\sum_{\Omega_L}(q(x,y)-1/2)^2\ge \frac{H(L)+2}{2}(1-\epsilon)^2.
\]

The exact count has asymptotic

\[
\boxed{H(L)=\frac{27}{2\pi^2}L^2+O(L\log L).}
\]

Thus the leading coefficient of the **guaranteed** high-support count is three times the r451 sixfold-pair certificate's 9/(2 pi^2), within exactly the same Omega_L and F7 premises. This does not assert the actual high-support cardinality has that asymptotic, or change the unrestricted minimax bounds.

## Proof

For each 1<=t<=L-1 and coprime 1<=s<=U_t, select one edge of the following two types.

**Forward A edge** when s<=X-3t:

\[
z_A=(2t+s,0,t+s,0),\quad
Az_A=(3t+s,t,s,-t),
\]
\[
P_A(t,s)=((3t+s,t),(s,-t)).
\]

Both old axis arguments are nonzero. Hence q(3t+s,t)+q(s,-t)>=2-epsilon, equivalently the two deltas sum to at least alpha.

**Reflected R edge** when X-3t < s <=3t-1:

\[
z_R=(2t-s,0,t-s,0),\quad
Az_R=(3t-s,t,-s,-t),
\]
\[
P_R(t,s)=((3t-s,t),(s,-t)).
\]

This second range cannot occur at t=1 for L>=3, since X-3>=4. For t>=2, gcd(s,t)=1 rules out s=t and s=2t, so both old axis arguments are nonzero and have q-value 1. Evenness in the first q coordinate therefore yields q(3t-s,t)+q(s,-t)>=2-epsilon.

All endpoints are in Omega_L: each has second coordinate +/-t, is primitive because gcd(s,t)=gcd(3t +/- s,t)=1, and is in the positive first-coordinate range 1..X. At fixed t the negative-second-coordinate endpoint (s,-t) uniquely identifies the selected edge; positive-second-coordinate endpoints of A edges are >3t, while those of R edges are <3t, and the respective first coordinates are injective in s. Thus **all selected edges are pairwise disjoint**; distinct t have different |y|. We obtain S(L)=sum C_t(U_t) disjoint edges, each with sum of deltas >=alpha.

For the second fixed mark, add the legal B edge from z_B=(-3,0,-4,0), Az_B=(-2,1,-5,-1):

\[
P_B=((2,1),(5,-1)).
\]

At t=1 the selected forward edges cover s=1,...,3L-5 and there are no reflected edges. For L=3, s=5 is absent; P_B is disjoint from every existing edge. For L>=4, P_B overlaps exactly one existing edge, P_A(1,5), at (5,-1); remove P_A(1,5) and insert P_B. It cannot overlap a different t because its |y|=1, or an A positive endpoint because their x>3 whereas its positive endpoint is x=2. The resulting edges remain pairwise disjoint, and their count is H(L).

The pair P_A(1,1)=((4,1),(1,-1)) has one marked zero-delta endpoint because q(1,-1)=q(-1,-1)=1/2. The new P_B has another, q(2,1)=1/2. These two different edges therefore contribute at least Psi(alpha) each. For any remaining edge, Jensen and monotonicity give Psi(d1)+Psi(d2)>=2Psi((d1+d2)/2)>=2Psi(alpha/2). Every unpaired point has nonnegative delta and hence nonnegative Psi(delta). This proves the convex-energy bound. Each edge contains one endpoint with delta>=alpha/2. Taking Psi(u)=u^2 gives the asserted quadratic expression.

For the asymptotic, C_t(U)=U phi(t)/t + O(tau(t)) by Mobius inversion. Since U_t=3L max(1-t/L,t/L)+O(1) uniformly in 1<=t<L, and sum_{t<=L}tau(t)=O(L log L), we get

\[
S(L)=3L\sum_{t=1}^{L-1}\frac{\varphi(t)}t\max(1-t/L,t/L)+O(L\log L).
\]

Mobius inversion also gives sum_{t<=x} phi(t)/t=(6/pi^2)x+O(log x). Summation by parts for the piecewise-Lipschitz weight f(u)=max(u,1-u) yields a main integral (6/pi^2) L int_0^1 f(u)du, and int_0^1 f=3/4. Therefore S(L)= (27/(2pi^2))L^2+O(L log L). The bounded B-edge replacement does not affect the main term. QED.

## Exact independent finite checks

A separate fresh integer enumeration (Python, math.gcd; without any optimization solver) constructed both forward and reflected source inputs, checked their nonzero old axes, all endpoint coordinate limits and primitivity, pairwise endpoint uniqueness, the exact H formula and both distinct marked endpoints for L=3,4,5,6,8,10,20,50,100,250. Results:

| L | H(L) | forward A count | reflected R count |
|---:|---:|---:|---:|
| 3 | 8 | 5 | 2 |
| 4 | 16 | 9 | 6 |
| 5 | 26 | 17 | 8 |
| 6 | 42 | 25 | 16 |
| 8 | 78 | 48 | 29 |
| 10 | 123 | 79 | 43 |
| 20 | 531 | 341 | 189 |
| 50 | 3373 | 2222 | 1150 |
| 100 | 13519 | 9015 | 4503 |
| 250 | 85134 | 56726 | 28407 |

The column counts omit one forward A edge when present and omit the one B edge, so H=forward+reflected+1. The computation checks combinatorial exactness; all-L validity is the proof above.

## Provenance and continuation

Original F7 author/source and frozen Result: EM-CBRCF7-83A1D4 / RR-AA38973D56330E59D315. Driver predecessors: r448 @ b4b3141368975f7598a8c98acbf49b435161c4cf; r449 @ e43bf08f8e28db64d1ab0efaac33c01f48d2cd5c; r450 @ 847d274abd0d2430e31eaf6eb5fe0bb053631660; r451 @ 972f424c7f58a770494e8b9bce41554091cb3016. Authorship/exposure: continuing Driver EM-DVR-DEBB5E; shared original F7 scientific and control context, not blind independent Native Review.

The unrestricted exact global minimax remains 1/2 <= E_infinity <= 4/7. Useful independent future work: optimize the full primitive bipartite axis matching graph, obtain a rigorous B=12 half certificate, or find a global infinite-ray construction. Existing Native first-review budget/integrity issues and formal Source/Activity association remain separate controls; this proof is durable GitHub mathematics, not a substitute for their current authority or authenticated review.
