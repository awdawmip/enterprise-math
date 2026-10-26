# R4-EC42: Time-of-information obstruction and exact finite-horizon BRC stopping certificate

**Scientific status:** author-side mathematical proof and finite exact program checks; no native Result, independent Driver review, Working Truth or Foundation acceptance.

## Fixed source and BRC model

The GLOBAL_KNOWLEDGE_V1 reading snapshot is awdawmip/chatgpt-global-knowledge main@26a5b1b309aee44516bb5ee17ae76620521fe9de (00_BOOTSTRAP, OPERATING_MANUAL, P000_STARTUP, P000_REALITY_FOUNDATION, ACTIVE worldview). The project reading snapshot is awdawmip/enterprise-math main@2fc58c45f2d48259be0e236f01ff0a44dfea51ef (docs/PORTABLE_RESEARCH_PROTOCOL.md, research_delivery_policy and weighted BRC). The direct mathematical predecessor is EC41 at commit e54910d752959f73b541282bdc6dc7042ce310f4, which characterized two-stage Bayes-gain profiles.

This is a strictly positive *two-measure, labelled-source BRC decision-tree model*. There is a compulsory finite first observation h with identical strictly positive P and Q probabilities w_h, summing to one. At h the decision maker stops and declares P or Q, or continues through finitely many additional positive-rational, fully labelled source kernels, with stopping/decision at each later stage and a fixed finite terminal depth N. The full policy can use h; the compressed policy can use only T(h) at the *first decision*. Crucially, after continuation the full ordered history (h,z1,...,zt) becomes available again, as in EC41. Randomization is allowed. Observe the **entire attainable region** of (e_P,e_Q,t_P,t_Q), with e_P=P(declare Q), e_Q=Q(declare P), t_P,t_Q the expected decision depths.

All labels and multiplicities are kept until the exact observer comparison. Time here is a decision index, not native Heartbeat time. No X6 or three-dimensional slice embedding is asserted.

## Theorem EC42.1: exact four-region support gap and if-and-only-if test

For any *real* normal lambda=(alpha,beta,gamma,delta), let

$$L_\lambda(v)=\alpha e_P+\beta e_Q+\gamma t_P+\delta t_Q,\qquad s_\lambda=\min(\alpha,\beta)+\gamma+\delta.$$

Let Pi_h^+ be the finite set of deterministic full-history future policies *compelled to continue immediately after h*. Write v_h(pi) for the four conditional observables given h, and

$$C_h(\lambda)=\min_{\pi\in\Pi_h^+}L_\lambda(v_h(\pi)),\qquad G_h(\lambda)=s_\lambda-C_h(\lambda).$$

For each fiber x of T put w_x=sum_{T(h)=x}w_h and bar G_x=sum_{T(h)=x} w_h G_h/w_x. Then the full and compressed attainable-region support minima obey, **at every finite horizon**,

$$\boxed{V_{\rm full}=s_\lambda-\sum_h w_h[G_h]_+},\qquad
\boxed{V_T=s_\lambda-\sum_x w_x[\bar G_x]_+},$$

$$\boxed{V_T-V_{\rm full}
=\sum_x\left(\sum_{T(h)=x}w_h[G_h]_+-w_x[\bar G_x]_+\right)\ge0.}\tag{EC42.1}$$

Their **complete four-observer convex polytopes are equal if and only if** no fiber x contains an ordered pair h,k and any lambda in R^4 with

$$\boxed{G_h(\lambda)>0>G_k(\lambda).}\tag{EC42.2}$$

All polarities/orderings are tested. Zeros do not create a gap by themselves.

### Proof

At first observation h, immediate decisions cost beta+gamma+delta or alpha+gamma+delta. Because the first observation has equal P and Q masses, the minimum initial stop cost s_lambda is common across h. The forced continuation cost is C_h, so the unrestricted minimum is sum_h w_h min(s_lambda,C_h), exactly the first formula. For T(h)=x, the initial stop/continue choice must be common to the fiber, while later choices can again depend on the *full* h. Thus its minimum is min(w_x s_lambda, sum_{h in x}w_h C_h), the second formula. External randomization cannot improve a linear minimum. Convexity of u -> [u]_+ yields the gap.

With every w_h>0, the positive-part Jensen inequality is strict precisely when some G_h within a fiber is strictly positive and another strictly negative. At finite depth there are finitely many deterministic decision trees, and allowing randomization yields compact convex occupation polytopes. Equality of all real linear support minima is equivalent to equality of these polytopes by separation. Therefore EC42.2 is necessary and sufficient. QED.

**Scope:** This is not a theorem for irrevocably deleting h at *every* future decision. In particular, one-time four-observer sufficiency is weaker than all-label provenance equivalence.

## Corollary EC42.2: finite exact rational feasibility test

For rational positive kernels every conditional policy vector v_h(pi) is rational, and C_h is the minimum of finitely many rational linear forms. The uncountable normal test EC42.2 therefore has a **finite exact decision procedure**. For each fiber, ordered pair h,k, and each choice b=alpha (with alpha<=beta) or b=beta (with beta<=alpha), enumerate each pi in Pi_h^+ and solve the following *rational linear feasibility system* in lambda:

$$L_\lambda(v_h(\pi))\le b+\gamma+\delta-1,$$

$$L_\lambda(v_k(\rho))\ge b+\gamma+\delta+1
\quad\text{for every }\rho\in\Pi_k^+.$$

The branch condition b<=the other initial error coefficient is included. **Any feasible system** is an explicit exact unsafe-compression certificate. **If all systems are infeasible**, the complete four-observer polytopes are equal.

### Proof

Feasibility implies C_h<s_lambda<C_k and hence G_h>0>G_k. Conversely, if those strict inequalities hold, choose a minimizing forced-continuation policy pi for h. All forced-continuation policies rho at k have cost strictly greater than s_lambda. The finitely many strict rational linear inequalities are homogeneous in lambda before margin normalization. Scaling lambda by a sufficiently large positive constant makes both margins at least 1 while retaining the stop-minimum branch. This supplies a feasible system. Rational linear feasibility has rational witnesses whenever feasible, so exact rational LP suffices. The algorithm is finite because the depth and alphabets are finite. QED.

This is a proved algorithm, **not** a claim that a general LP solver was executed in this run.

## EC42.3: strictly positive three-stage timing counterexample

Let H={a,b} with P(h)=Q(h)=1/2 each, first seen at decision depth 1. After continuing the observer receives binary z1 (depth 2) and z2 (depth 3). Terminal positive integer source counts out of 8, in ordered (z1,z2) order 00,01,10,11, are:

| First history | Hypothesis | 00 | 01 | 10 | 11 |
|---|---|---:|---:|---:|---:|
| a | P | 3 | 3 | 1 | 1 |
| a | Q | 1 | 1 | 3 | 3 |
| b | P | 3 | 1 | 3 | 1 |
| b | Q | 1 | 3 | 1 | 3 |

For a, z1 conveys all discrimination and z2 is independent fair noise. For b, z1 is fair noise and discrimination occurs at z2. Each full-terminal experiment has two source-label pairs (p,q)=(3/8,1/8) and two (1/8,3/8); the multisets are identical. Therefore for **every r>=0** the EC41-style terminal Bayes-gain profiles

$$g_h^{term}(1,r)=\min(1,r)-\sum_{z1,z2}\min\{p_h(z1,z2),r q_h(z1,z2)\}$$

are exactly equal, with rational breakpoints among 0,1/3,1,3. Terminal Bayes-profile matching alone would therefore incorrectly identify a and b as safe to merge at the first decision.

Take lambda=(1,1,1/6,1/6), so the normal objective is error sum plus one-sixth of both expected decision times. First-stage stopping has s=4/3. At a, the best forced continuation stops after informative z1, with total error 1/2 and t_P=t_Q=2; hence C_a=1/2+4/6=7/6, G_a=+1/6. At b, z1 is uninformative; the best forced continuation waits for informative z2 and stops at depth 3, with error sum 1/2; hence C_b=1/2+6/6=3/2, G_b=-1/6. Thus the gains have opposite signs while their weighted mean is 0.

The exact support gap is

$$\boxed{V_{\rm full}=5/4,\qquad V_T=4/3,\qquad V_T-V_{\rm full}=1/12.}$$

One optimal full policy continues after a, declares P at z1=0 and Q at z1=1, and declares P immediately after b. Its observer vector is

$$\boxed{(e_P,e_Q,t_P,t_Q)=(1/8,5/8,3/2,3/2).}$$

Every policy compressing a,b into the same initial action has strictly larger normal value. This proves **a strict four-region failure at the smallest horizon beyond EC41**, with no missing source branch and no hidden sign cancellation.

## Execution and validation

The companion EC42_verify.js constructs and directly scores all deterministic decision trees using integer source counts. At one first history there are 2 immediate-stop decisions and 6 possibilities at each of the two intermediate z1 labels, giving 38 policies. There are 38^2=1444 full policy pairs and 2+36^2=1298 pairs with the initial T-decision shared. Every conditional (e_P,e_Q,t_P,t_Q) component is an integer numerator divided by 8, and global mixtures divide by 16.

The program independently enumerates the support minima and compares them with EC42.1 for all **625 normals in {-2,-1,0,1,2}^4**; it also checks positive branch weights, terminal multiset equality, sign criterion and exact witness normal (6,6,1,1), whose support costs are 120/96 and 128/96. A second Python-Fraction implementation was locally run independently over the same 625 normals. Finite tests check the example and program; **the infinite-parameter theorem is supported by the written proof, not by a finite search**.

## Status and next unit

Native owner-list read gave CONTROL_QUOTA; native own-session start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. The authenticated GitHub actor is awdawmip and is permitted to write the repository. No native Task CLAIM, Result, Research Activity Guard pass or Driver review is inferred from author-side publication.

**Next EC43 question:** develop exact finite occupation-flow certificates for statistics enforced at *every* stage (later h may never reappear), preserving all four observer coordinates under successive stop/decision/composition. Determine whether a recursive feasible polytope can replace exponentially many whole decision trees. The distinct native physical bridge remains pending: P000 has fixed_heartbeat_program=null, with no justified native labelled X6 update, three-dimensional slice third-coordinate semantics or independent native-time mapping.
