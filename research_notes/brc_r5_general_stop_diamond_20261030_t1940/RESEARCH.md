# R5: General strict-stop diamond rigidity (arbitrary positive P/Q weights)

**Date:** 2026-10-30 Asia/Shanghai. **Evidence:** AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

**Source pin:** GLOBAL_KNOWLEDGE_V1 `main@02f68f0343d66634b546d7fc27bb274271f17e0c`; Enterprise Math `main@84f57a009f46602fd19c3438e8b3fa51b875b4aa`. Predecessor: `b3fd519adbe71007d8a86542b67197501187d2ea`, `research_notes/brc_r5_stop_late_collision_rigidity_20261030_t1844/RESEARCH.md`. This note extends the predecessor's fixed-weight/four-parameter classification to arbitrary legal strictly positive weights, arbitrary early and late error baselines, and arbitrary source-specific late affine error coefficients.

## Model, exact domain, and observations

Nature first reveals source X in {0,1}. At time 2 the controller genuinely STOPs (absorption at time 2) or CONTINUEs to a natural U in {0,1}. At time 3 the controller genuinely STOPs or CONTINUEs to mandatory absorption at time 4. There is no nonterminal route and no persistent randomized seed.

Let `q_xu>0`, `p_xu>0`, with each law's four masses summing to one. Assume at time 3 that `p_0u/q_0u=p_1u/q_1u=r_u>0` and `r_0 != r_1`. Assume the time-2 source ratios `P_0/Q_0 != P_1/Q_1`, where `P_x=sum_u p_xu`, `Q_x=sum_u q_xu`. These are genuine likelihood-ratio information restrictions. FULL has behavior probabilities `s_x` for early continuation and `y_xu` for stopping at 3; seedless LR can use the distinct early ratios and hence also `s_x`, but must use one shared `y_u` across source x at time 3.

Early terminal Bernoulli error has probability `k_x`. At time 3 STOP the error probability is `beta_xu+c_xu`; at time 4 it is `beta_xu`. Assume all `k_x`, `beta_xu`, `beta_xu+c_xu` strictly in (0,1). The conditional terminal-error experiment is **common under both P and Q**, and behavioral mixing yields the expected late error `beta_xu+c_xu*y_xu`.

For `L=P,Q` and weights `w^L=p,q` define:

~~~
e_L = sum_xu w^L_xu[(1-s_x)k_x + s_x(beta_xu+c_xu*y_xu)]
T_L = sum_xu w^L_xu[2(1-s_x) + s_x(4-y_xu)]
O = (e_P,e_Q,T_P,T_Q).
~~~

The source-labeled positive rational branch family is retained before applying the LR information quotient. This uses the typed positive-weight/provenance semantics of `definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json` (REUSE_APPLIED, not a dedicated BRC engine run). The theorem concerns this external finite stochastic model, not an X6 native spatial or dynamical assertion.

## Theorem (complete all-real classification)

For **every** real admissible choice of the masses and error probabilities above:

**1.** If for some u, `c_0u != c_1u`, then `conv(O_FULL) != conv(O_LR)`. There is an explicit linear functional with strictly positive support gap, given below.

**2.** If both equalities `c_00=c_10=kappa_0` and `c_01=c_11=kappa_1` hold, then the **actual real behavioral images** satisfy `O_FULL=O_LR`, with a constructive genuine seedless LR policy for every FULL policy. This common set is a compact convex polytope.

Thus convex hull equality holds **if and only if** both late source slopes agree, and whenever the convex hulls agree the actual real observation images agree as well. The original four-observer hull-equal/image-unequal mother target cannot occur in this whole class, including full-affine-rank members.

**3.** At the equality locus set

~~~
E_x = (sum_u p_xu(beta_xu-k_x),
       sum_u q_xu(beta_xu-k_x), 2P_x, 2Q_x)^T,
F_u = (kappa_u*r_u, kappa_u, -r_u, -1)^T,
M = [E_0 | E_1 | F_0 | F_1].
~~~

The common real image has affine dimension **exactly rank(M)**, and therefore is four-dimensional if and only if `det(M) != 0`. No numerical rank threshold is assumed.

## Proof: strictly positive separation when a source slope differs

Choose a collision u with unequal slopes, and let v=1-u. Choose `sigma` in {-1,+1} so that `h=max(sigma*c_0u,sigma*c_1u)>0`, with `l=min(sigma*c_0u,sigma*c_1u)<h`. This choice exists because the two real slopes differ. Choose `theta` strictly between `max(0,l)` and `h`; the specific midpoint works.

Choose a positive number `K` satisfying for x=0,1:

~~~
K*q_xv > P_x,
K + theta*r_u > r_v*sigma*c_xv.
~~~

Such K always exists by strict positivity of q. An explicit choice is
`K=1+max_x(P_x/q_xv)+r_v*max_x|c_xv|+theta*r_u`.

Define `A=K/(r_v-r_u)` and `B=-A*r_u+theta*r_u`, and take the signed observer functional

~~~
H(e_P,e_Q,T_P,T_Q) = sigma*e_P + A*T_P + B*T_Q.
~~~

The time coefficient on each path `(x,j)` is `(A*r_j+B)*q_xj`: it is `theta*p_xu>0` at the selected collision u and `(K+theta*r_u)*q_xv>0` at the other collision v.

For any fixed real late behavior, switching an early action from STOP (time 2) to CONTINUE changes H by

~~~
D_x = sum_j (2-y_xj)(A*p_xj+B*q_xj)
      + sigma*sum_j p_xj(beta_xj+c_xj*y_xj-k_x).
~~~

The second sum is strictly greater than `-P_x`, since all terminal error probabilities are between 0 and 1; the first sum is at least `K*q_xv`. Hence `D_x>K*q_xv-P_x>0` for FULL and LR, uniformly over all late policies. Therefore **all** H-maximizers have `s_0=s_1=1`.

At full survival the gain from switching late CONTINUE to late STOP at path `(x,j)` is

~~~
g_xj = sigma*p_xj*c_xj - (A*p_xj+B*q_xj).
~~~

At j=v both gains are strictly negative by the K choice. At j=u the gain is
`g_xu=p_xu(sigma*c_xu-theta)`. Exactly one source has positive gain `Gplus=p_hi,u*(h-theta)>0`; the other has negative gain `-Gminus=-p_lo,u*(theta-l)<0`.

FULL can STOP at epoch 3 on the positive source only, gaining Gplus. The source-blind LR controller must use the same late probability for both sources and gains at most `max(0,Gplus-Gminus)`. Thus the **exact all-real support gap** is

~~~
Delta_u = sup_FULL H - sup_LR H
        = min(Gplus,Gminus)
        = min(p_hi,u*(h-theta),p_lo,u*(theta-l)) > 0.
~~~

A deterministic FULL witness has `s_0=s_1=1` and stops at time 3 only on `(hi,u)`. Every real LR observation obeys the strictly separating inequality `H <= sup_LR H`, with

~~~
distance_infinity(Ostar,O_LR) >= Delta_u/(1+abs(A)+abs(B)) > 0.
~~~

The support proof uses exact algebra and optimization of affine real behavioral variables, not a parameter grid. It also separates convex hulls because H is linear.

## Proof: observer-safe descent and full rank when late slopes agree

If `c_xu=kappa_u` for both x at each u, take any FULL real behavioral policy and retain its early survival probabilities s. Define

~~~
Q_u(s)=sum_x q_xu*s_x,
Y_u=(sum_x q_xu*s_x*y_xu)/Q_u(s) if Q_u(s)>0; else Y_u=0.
~~~

Each `Y_u` is a **single local real LR behavior probability** in [0,1], not a random mixture of complete LR strategies. Since `p_xu=r_u*q_xu`, for each u it gives the same P- and Q-weighted late stopping mass as FULL. Early probabilities, early errors and late baselines remain fixed; equal late coefficients `kappa_u` make late errors agree too. Hence all four observations are identical. The reverse inclusion LR⊆FULL is trivial.

Set `z_u=sum_x q_xu*s_x*y_xu`. The exact feasible flow set is

~~~
0 <= s_x <= 1,     0 <= z_u <= sum_x q_xu*s_x.
~~~

Any feasible `(s,z)` has a real seedless LR implementation via `Y_u=z_u/Q_u(s)` or 0 if the denominator vanishes. This is a compact convex polytope with nonempty interior in R4: take `0<s_x<1` and `0<z_u<Q_u(s)`. Direct substitution gives the affine observer map

~~~
O = O_0 + s_0*E_0+s_1*E_1+z_0*F_0+z_1*F_1,
O_0 = (sum_x P_x*k_x,sum_x Q_x*k_x,2,2).
~~~

Its image affine dimension equals the rank of the explicitly defined four-column matrix M. This proves the theorem, the sufficiency and necessity of its full-four-dimensional determinant, and the exact observer-limited status of the descent. The provenance and other future observables are not assumed recoverable from O. QED.

## Exact finite tests and scope

`VERIFY.py` is a runnable Python standard-library Fraction checker; stdout is `EXACT_OUTPUT.txt`. It independently enumerates 64 FULL and 16 LR deterministic policies in each of four legal exact rational instances, checks law normalization/strict positivity/actual ratios/terminal probability legality, and matches each strict support gap to the analytic formula. At the two equal-slope instances it checks 729 exact policy conversions each and the four-dimensional determinant.

Exact certificates include: baseline weights with unequal slopes at u=0 `Delta=3/320`, `distance_infinity>=1/719`, and at u=1 `Delta=9/400`, `distance_infinity>=18/11135`; independent perturbed weights with unequal u=1 slopes `Delta=2/65`, `distance_infinity>=216/309535`. The equal-slope determinant certificates are `117/640000` for original weights and `-11091/5796700` for perturbed weights. The actual program terminates with `PASS_EXACT_GENERAL_STOP_DIAMOND_ALL_WEIGHTS_SHARED_ERROR_SLOPES`.

The **all-real proof is the analytic argument above**. The computer tests cover their four stated rational instances and do not establish universality by sampling. No Lean/formal checker, independent review, Source Result, mathematical admission, physical calibration, or new theorem-priority claim was performed.

## Subsequent question

The classified family strictly contains the fixed-weight/four-error family of the predecessor, so the suggested path-weight or common-kernel perturbation alone cannot produce the mother counterexample in this two-source/two-merger topology. The next useful investigation is a **third genuine stop/continue epoch with interacting likelihood-ratio mergers**, a consistent P/Q-specific terminal error observation, or more than two interacting source/ratio classes. Preserve positive path masses and genuine absorption. For any candidate first certify four-dimensional hull equality via exact rational convex decompositions (at most five LR deterministic observations per FULL vertex) or publish a strict signed Farkas separator, and only then test actual behavioral image membership using an exact semialgebraic certificate. P000, the ACTIVE six-axis worldview and the native time/slice distinctions remain unchanged.
