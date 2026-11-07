# EC49Y — Exact maximal-discrimination acceptance face and sensing rigidity

Date: 2026-10-29. Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED**.

Parent scientific evidence: EC49X draft PR #1674, immutable commit 46a6784db65680d774e23a23b34a597298b6b60f. Frozen rules: GLOBAL_KNOWLEDGE_V1 main@f08728bcfe2bab9f89c0aac9f9d4af5b52160c72; Enterprise Math main@3fb7fc8138eca68cf5473b9da31511b017be62cb. Native directed context returned authority_granted=false; canonical owner query returned CONTROL_QUOTA. This is author-side portable research, without canonical CLAIM, Result or independent Driver acceptance. P000 and ACTIVE worldview unchanged.

## 1. Model and theorem

The auxiliary positive-probability BRC readout has histories and terminal symbols \(w,z\in\{0,1,2\}\), first sensor \(u\in\{0,1\}\), and source laws
\[
Q(w,z)=1/9,\quad P(w,z)=\begin{cases}1/6&z=w\\1/12&z\ne w,\end{cases}
\quad t_w(u)=1/2+(2u-1)(1/200)\sigma_w,\quad \sigma=(1,0,-1).
\]
Each source has 18 strictly positive rational joint leaves \(R(w,u,z)=R(w,z)t_w(u)\), and \(P(w,u)=Q(w,u)\).

At history \(w\) the observer chooses STOP or paid code \(c\in\{A0,A1,B0,B1\}\). Codes A cost 1, codes B cost 2; the suffix is the retained one-bit memory. The original \(w\) is then erased. After seeing \(u\), the observer may buy S at cost 1 to observe \(z\). Terminal acceptance uses \(w\) at STOP, \((c,u)\) without S or \((c,u,z)\) after S. All randomized actions are source blind and use independent fresh behavioral coins, without a persistent ex-ante common seed.

The two source-equal expected costs are fixed at \(C_1=43/48,\ C_2=7/8\). Write \(\alpha=P(\mathrm{accept})\), \(\beta=Q(\mathrm{accept})\). EC49X proved the sharp universal maximum \(\delta_*=\max(\alpha-\beta)=59/576\).

**EC49Y theorem.** Every real, legal independent-coin behavioral policy attaining \(\alpha-\beta=\delta_*\) purchases S on every paid information state of positive probability. The entire maximizing acceptance-pair face is exactly
\[
\boxed{\{(\alpha,\beta):\alpha-\beta=\delta_*, C_1=43/48,C_2=7/8\}
=\left\{\left(\frac{109}{192}+\frac r8,\frac{67}{144}+\frac r8\right):r\in[0,1]\right\}.}
\]
Every rational point of this face is implemented by rational independent behavioral probabilities. The theorem concerns this **one exposed face** of the fixed-cost pair image, not the full two-dimensional image.

## 2. Exact prefix reduction

Let \(x_{wc}\ge0\) be the probability of buying first-stage code c at history w; \(\sum_c x_{wc}\le1\). Let \(s_{cu}\in[0,1]\) be the subsequent S-purchase probability after \((c,u)\). The causal joint probability is \(x_{wc}s_{cu}\): freely convexified occupation variables would change the model.

Define B-code prefix mass \(b=\sum_{w,c\in B}x_{wc}\), and the expected *unsensed paid* prefix mass
\[
m=\sum_{w,c,u}x_{wc}t_w(u)(1-s_{cu})\ge0.
\]
Direct source-equal cost accounting gives
\[
3(C_1-C_2)=b+m=1/16,\qquad 0\le b\le B:=1/16.
\]
Set \(h_w=1-\sum_cx_{wc}\) and \(b_w=x_{w,B0}+x_{w,B1}\). Then
\[
\sum_wh_w=5/16+b=:H,\quad \sum_wb_w=b,\quad \sum_w(h_w+b_w)=5/16+2b\le7/16<1.
\]
Thus row-capacity constraints are automatically satisfied for every pair of nonnegative allocations of H and b across three histories.

For fixed b, every feasible prefix is a convex combination of 144 labelled vertices indexed by STOP history i (three choices), B history j (three choices), three independent A labels \(a_w\in\{A0,A1\}\) (eight choices), and B label \(q\in\{B0,B1\}\) (two choices):
\[
h_w=H\mathbf1_{w=i},\quad b_w=b\mathbf1_{w=j},\quad
v_{w,a_w}(b)=1-h_w-b_w,\quad v_{j,q}(b)\mathrel{+}=b.
\]
For completeness: choose i with weights \(h_i/H\); choose j with weights \(b_j/b\) when \(b>0\), arbitrary when \(b=0\); conditional on the row allocate each A label by its prescribed A share and each B label at j by its B share. Expectations recover every entry of x. The vertex formula is affine in b:
\[
v(b)=(1-b/B)v(0)+(b/B)v(B).
\]
Hence *all* allowed prefixes with \(0\le b\le B\) lie in the convex hull of 288 endpoint vertices: 144 at b=0 and 144 at b=B. Duplicated labelled vertices are intentionally retained.

## 3. Equality forces sensing every occupied code-signal state

Define
\[
d_{cuz}(x)=\sum_w x_{wc}(P(w,z)-Q(w,z))t_w(u),\quad
g_{cu}(x)=\sum_z[d_{cuz}(x)]_+,\quad D(x)=\sum_{c,u}g_{cu}(x).
\]
Because \(P(w,u)=Q(w,u)\), both initial STOP and post-u omission of S yield zero source contrast. Consequently
\[
\alpha-\beta\le\sum_{c,u}s_{cu}g_{cu}(x)\le D(x).
\tag{1}
\]
Each \(g_{cu}\) is convex in x.

The executed Python Fraction certificate in VERIFY.py and ENDPOINT_CENSUS.csv checks all 288 justified endpoints and establishes:
(a) \(D(v)\le59/576\) for each;
(b) 72 maximum-labelled vertices at b=0 and 48 at b=B;
(c) **every** maximizing endpoint has positive \(g_{cu}(v)\) at each occupied \((c,u)\), where occupied means \(\pi_{cu}(v):=\sum_wv_{wc}t_w(u)>0\). Across all such endpoint states the minimum positive gain is \(11/6400\). The last assertion was checked on every c and u at all 120 maximizing labelled endpoints, not sampled.

If an actual policy attains \(\delta_*\), write its prefix as \(x=\sum_v\lambda_vv\) with endpoint vertices. Convexity gives
\[
\delta_*\le D(x)\le\sum_v\lambda_vD(v)\le\delta_*.
\]
Thus every vertex with \(\lambda_v>0\) is maximizing, and equality in the sum of convex functions implies for each c,u
\[
g_{cu}(x)=\sum_v\lambda_vg_{cu}(v).
\tag{2}
\]
At any occupied \((c,u)\), some used endpoint is occupied. The finite strict-gain assertion and (2) show \(g_{cu}(x)>0\). Equality in (1) forces \(s_{cu}=1\) on all such states. Therefore \(m=0\), so the exact cost identity forces \(b=B=1/16\).

This proves **equality rigidity** over all real causal random policies: an arbitrary permitted post-u decision to omit S cannot occur with positive probability at the maximum.

## 4. Exhaustive two-coordinate maximum face

At \(b=B\), the prefix is a convex combination of 144 B-endpoint vertices. Equality in the previous bound implies every used endpoint is one of 48 maximizing B-endpoint vertices. For **each** of these 48 endpoints the executed exact checker computes the same optimal terminal acceptance masses:
\[
P(\mathrm{positive\ contrast\ paid\ cells})=109/192,\quad
Q(\mathrm{positive\ contrast\ paid\ cells})=67/144.
\]
There is zero positive mass in paid cells with exactly zero source contrast; the STOP mass is \(1/8\). Any optimal terminal rule accepts positive cells, rejects negative cells, and can accept STOP with arbitrary probability. Hence each maximum endpoint attains only
\[
109/192\le\alpha\le133/192,\qquad \beta=\alpha-59/576.
\tag{3}
\]

For arbitrary maximizing x, fix its actual terminal acceptance probabilities and its initial history-dependent STOP acceptance probabilities. With these probabilities fixed, both \(\alpha\) and \(\beta\) are affine functions of x. In the maximizing-endpoint convex decomposition, the same terminal rule must attain discrimination \(\delta_*\) at every used endpoint: otherwise its mixture would be strictly below \(\delta_*\). Therefore each component pair satisfies (3), and so does their affine average. This establishes the global inclusion without invoking a generally false behavioral convexity principle.

For the reverse inclusion, use the single rational prefix: W0 chooses A0; W1 chooses A1; W2 chooses STOP with probability 3/8, A0 with probability 9/16, B0 with probability 1/16. Always buy S after payment. Accept precisely those \((c,u,z)\) having positive \(d_{cuz}(x)\); at STOP accept independently with arbitrary \(r\in[0,1]\). Exact source-mass accounting yields
\[
(\alpha,\beta,C_1,C_2)=\left(109/192+r/8,\ 67/144+r/8,\ 43/48,\ 7/8\right).
\]
Thus all points are achieved and the endpoints are \((109/192,67/144)\) and \((133/192,85/144)\). For rational \(\alpha\) on the face, \(r=8(\alpha-109/192)\) is rational. QED.

## 5. Complete, uneliminated polynomial membership formula

The remainder of the two-dimensional image admits an exact semialgebraic existential decision specification. Use 12 prefix variables \(x_{wc}\), 8 S probabilities \(s_{cu}\), 24 acceptance variables \(a_{cuz}\), 8 no-S acceptance variables \(a^0_{cu}\), and 3 STOP acceptance variables \(q_w\): **55 real policy variables**. Require \(x\ge0,\sum_cx_{wc}\le1\), all other variables in [0,1], and
\[
\frac13\sum_{w,c}k_cx_{wc}=43/48,\quad
\frac13\sum_{w,c,u}x_{wc}t_w(u)s_{cu}=7/8.
\]
For R=P and Q, require the respective output \(A_P=\alpha,A_Q=\beta\) satisfy
\[
A_R=\frac13\sum_w(1-\sum_cx_{wc})q_w+
\sum_{w,c,u}x_{wc}t_w(u)
\left[
(1-s_{cu})a^0_{cu}\sum_zR(w,z)
+s_{cu}\sum_zR(w,z)a_{cuz}
\right].
\]
Here R(w,z) is the *joint* source law. This is a compact rational polynomial system of degree at most three. Its coordinate projection is a compact semialgebraic set, and the factor \(x_{wc}s_{cu}\) preserves causal unseeded behavior. The formula is a **membership specification**, not yet a quantifier-free boundary.

## 6. Evidence, relation to external literature, and scope

Run locally: python VERIFY.py. The program regenerates EXACT_REPORT.json and ENDPOINT_CENSUS.csv and asserts rational normalization of all 18 leaves per source, all 288 endpoint discriminations, the 120-maximizer occupied-state gain implication, all 48 B-vertex equality-face intervals, and three rational STOP witnesses. Mathematical completeness uses the preceding convex decomposition; the finite checker is an exact arithmetic certificate rather than an independent Driver acceptance or a Lean formal proof.

Anderson–Montúfar (ICML 2026) studies semialgebraic feasible value-function sets for infinite-horizon memoryless POMDP policies; Main–Randour (LICS 2026) studies payoff sets and finite mixtures in multiobjective POMDPs. Their models are different: in particular, ex-ante shared strategy mixtures cannot be silently equated with this erased-history protocol's fresh independent behavioral coins. See SOURCES.md; no originality claim beyond this specified model is made.

These are results for auxiliary *positive* P/Q probability readouts, not primitive signed BRC amplitudes, native X6 spatial/torsor relations, the third component of the native three-dimensional slice, or the heartbeat time dynamics. Each such representation transfer needs its own typed preservation proof. P000 and protected ACTIVE worldview are unchanged. The exact remaining question EC49Z is recorded in NEXT_TASK.md.
