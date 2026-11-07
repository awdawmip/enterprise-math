# R5 — Frozen likelihood-ratio keys with genuine stochastic splitting

Date: 2026-10-30 (Asia/Shanghai). Evidence status: **AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**.

Author-side scientific continuation from the static-origin absorbing stopping theorem at enterprise-math commit `db5f207ba5e5768039835139005835cca8731cc6`. Fixed canonical input snapshots: GLOBAL_KNOWLEDGE_V1 `main@f9bc230e04ba3d082a862bc7f18ae58ba535c36e`; Enterprise Math `main@c69bb3d08f7d258f118891e01f9bf8aec610d054`. This note treats a finite auxiliary two-law stochastic stopping model. It does not assert a native X6 realization, a P000 modification, independent review or a formally accepted Source Result. The provenance-preserving BRC method is reused at the level of **positive labeled source and path masses**, not as unverified native-heartbeat numerical arithmetic.

## 1. Research question and model

Fix a finite rooted nature tree with strictly positive P/Q probabilities on every possible observation prefix. Initially the FULL controller observes a source S=s, with positive masses P_s,Q_s summing to one under each law. At times j=1,...,m, it chooses stop/continue; at m stop is forced. Continuing generates the next nature signal according to the declared law-specific transition kernel. Stopping draws a terminal Bernoulli error with P-rate p_j(h) and Q-rate q_j(h), both strictly between 0 and 1, at the complete currently observed history h. Future nature randomness is not generated following absorption. The controller sees its full remembered history; a seedless LR controller sees only (j,L(h)), where the preterminal likelihood ratio is L(h)=P(h)/Q(h). Both laws use the same behavioral policy probabilities, including all real boundary values 0 and 1.

The exact original four observers are O=(e_P,e_Q,T_P,T_Q): law-specific terminal-error probabilities and law-specific expected stopping times.

**Frozen-key hypothesis:** for every initial source s and every positive nature prefix h extending s, L(h)=r_s=P_s/Q_s. Hence within the class g of sources of equal initial ratio, the LR strategy receives no further distinguishing LR-key value after postinitial stochastic branching. This happens, for example, when P and Q have the same conditional continue-nature kernels given the complete history, even though initial source weights and terminal-error kernels differ. Arbitrary source-dependent stochastic splits and reconvergences of nature histories remain allowed.

## 2. Theorem A — all-real hull-to-image rigidity

**Statement.** Under the preceding finite model and frozen-key hypothesis, the *actual real behavioral* observer sets O_FULL and O_LR are both convex polytopes. For every such model,

```text
conv(O_FULL) = conv(O_LR)    if and only if    O_FULL = O_LR.
```

The assertion holds for all real stop probabilities [0,1], zero-reach branches and all finite horizons. It does **not** assert equality for all models; it says convex-hull equality is already strong enough to imply actual-image equality throughout this class.

**Proof for FULL.** For each complete preterminal nature history h, define Q-occupancy x_h, Q-stop mass u_h and Q-continue mass v_h. Initially x_s=Q_s. At each node x_h=u_h+v_h; for each continue-nature child h' of h the occupancy satisfies x_h'=K_Q(h'|h)*v_h; at final nodes v_h=0. Require all masses nonnegative. This finite bounded system consists only of linear equalities and inequalities, hence forms a polytope F_Q.

Conversely, any solution of F_Q gives a legal FULL real behavioral policy by choosing stop probability u_h/x_h whenever x_h>0, with arbitrary choice on x_h=0. Along a realized full history h, law-independent action probabilities multiply the P and Q nature-path probabilities by the *same* reach factor. Therefore the P-stop mass is exactly L(h)*u_h, even when P and Q continuation kernels differ. The four observers are the following linear functionals of the Q flows:

```text
e_P = sum_h L(h)*u_h*p_j(h)       e_Q = sum_h u_h*q_j(h)
T_P = sum_h j*L(h)*u_h           T_Q = sum_h j*u_h
```

(The j inside each summand is the time of h.) Thus O_FULL is a linear image of F_Q, a convex polytope. Notably this FULL argument does not require frozen LR keys.

**Proof for LR.** Group initial sources by their identical frozen ratio r_g. A seedless LR hazard depends only on (j,r_g); consequently its time-to-stop distribution d_g=(d_g1,...,d_gm) is common to every origin and nature path in the group, under both laws. Every d_g in the simplex Delta_m is achievable by hazards

```text
alpha_gj = d_gj / (d_gj + d_g,j+1 + ... + d_gm)
```

where the denominator is positive; choose an arbitrary hazard after zero survival. Let pbar_sj and qbar_sj be the P/Q expectations of the terminal-error kernels at time j under the hypothetical always-continue path conditional on S=s. The exact LR observers are affine in the group time distributions:

```text
e_P = sum_g sum_j d_gj * sum_(s in g) P_s*pbar_sj
e_Q = sum_g sum_j d_gj * sum_(s in g) Q_s*qbar_sj
T_P = sum_g P_g * sum_j j*d_gj
T_Q = sum_g Q_g * sum_j j*d_gj
```

The actual O_LR is therefore the affine image of the product of finitely many simplexes, a convex polytope. Since every LR policy is a FULL policy, equality of the two convex hulls is equivalent to equality of the actual observer sets. QED.

**Research consequence:** after-initial genuine nature stochasticity, extra hidden source/path information, path-dependent terminal responses and any number of time decisions do **not** by themselves create the mother target if exact LR information remains frozen. A successful candidate needs a structural mechanism beyond this class, such as a genuinely changing LR key later colliding with another history. Source and path provenance is retained; the theorem certifies only the declared finite stopping observers and horizon.

## 3. Theorem B — exact BRC joint-observer covariance residual

Let H be the *potential* full nature path up to the forced stopping horizon under an always-continue coupling. For each class g, frozen likelihood ratios guarantee the same conditional nature-path measure mu_g under P and Q: P(H|g)=Q(H|g)=mu_g. For a particular FULL behavioral policy, define d_j(H) to be the conditional probability that it would first stop at time j along that potential path (the product of all previous continue hazards and the time-j stop hazard). The nonanticipating policy satisfies sum_j d_j(H)=1 on every H.

Set d_gj=E_mu_g[d_j(H)]. These group distributions define a legal seedless LR schedule, which preserves T_P and T_Q exactly. The two residual terminal-error differences for **this time-flow-matched LR schedule** are

```text
e_P(FULL)-e_P(LR(d)) = sum_g P_g * sum_j Cov_mu_g(d_j(H),p_j(H))
e_Q(FULL)-e_Q(LR(d)) = sum_g Q_g * sum_j Cov_mu_g(d_j(H),q_j(H))
T_P(FULL)=T_P(LR(d));   T_Q(FULL)=T_Q(LR(d)).
```

Indeed E[d_j*p_j]=E[d_j]*E[p_j]+Cov(d_j,p_j), with the same mu_g across the two laws. No signed flow is introduced: positive source/path masses remain the carrier, while covariance is a signed *observer residual*. A nonzero residual for a matched schedule is **not alone** a proof of nonmembership in the entire LR observer image. This is an exact, finite-horizon, declared-observer calculation; it does not authorize deleting joint branch information for later operations.

## 4. Strictly positive rational example with real postinitial branching

Initial source probabilities and first postinitial signal Y:

| Source | P_s | Q_s | r_s | P(Y=1|s)=Q(Y=1|s) |
| --- | ---: | ---: | ---: | ---: |
| A | 1/8 | 1/4 | 1/2 | 3/4 |
| B | 1/8 | 1/4 | 1/2 | 1/4 |
| C | 3/4 | 1/2 | 3/2 | 1/2 |

After continuation at time 1 a binary Y is drawn. After continuation at time 2 a second binary Z is drawn with P(Z=1|Y=1)=Q(Z=1|Y=1)=2/3 and P(Z=1|Y=0)=Q(Z=1|Y=0)=1/3. All nature transitions are strictly positive. On reaching time 3, distinct positive-probability (s,Y) histories have reconverged at an identical observed (time,r_s,Z) key, including distinct sources A and B. FULL retains the earlier source and Y. Three LR stop decisions (times 1,2,3) precede forced stop at time 4.

The four baseline terminal Bernoulli rates for times 1,2,3,4 are:

| Source | p baseline | q baseline |
| --- | --- | --- |
| A | (1/5,3/10,1/5,1/2) | (1/5,1/5,3/10,2/5) |
| B | (1/4,7/20,1/4,11/20) | (1/4,1/4,7/20,9/20) |
| C | (1/4,1/4,1/2,1/3) | (1/4,1/2,1/4,2/3) |

Define a_s=E[Y|s] and b_s=(1+a_s)/3=E[Z|s]. For terminal error on a given complete nature path use:

```text
p_1(s)=p_s1,                 q_1(s)=q_s1
p_2(s,Y)=p_s2+(Y-a_s)/4,     q_2(s,Y)=q_s2+(Y-a_s)/8
p_3(s,Y,Z)=p_s3,             q_3(s,Y,Z)=q_s3+(Z-b_s)/8
p_4(s,Y,Z)=p_s4,             q_4(s,Y,Z)=q_s4.
```

All listed terminal Bernoulli rates are strictly inside (0,1). Both offset expectations vanish conditional on each source, so LR deterministic observer vectors are computed from the baseline table. There are exactly 4*4=16 deterministic LR stop schedules (AB and C each select one time). They have exact minimum P-terminal-error probability

```text
min_LR e_P = min(9/160,13/160,9/160,21/160)
           + min(3/16,3/16,3/8,1/4)
           = 39/160.
```

The deterministic LR displacement columns from choosing time 1 for both classes to changing AB to time 2/3 and C to time 2/3 are:

```text
(1/40,0,1/4,1/2), (0,1/20,1/2,1),
(0,1/8,3/4,1/2), (3/16,0,3/2,1).
```

Their exact 4-by-4 determinant is 1/1280, so O_LR has a genuine full-dimensional interior in R^4, despite frozen LR information and real hidden stochastic paths.

An explicit FULL witness: A continues at time 1 and stops at time 2 when Y=0, otherwise stops at time 3; B and C stop at time 1. Its exact observer is

```text
O_witness = (617/2560,323/1280,39/32,23/16).
```

Since every real LR policy has e_P>=39/160=624/2560, this witness violates that inequality by 7/2560 and lies at L-infinity distance **at least** 7/2560 from the LR image. This is a witness-based *lower bound* on the signed support gap, not the exact optimum.

For the **exact** P-error support difference, solve the FULL Bellman recursion by backward induction: at time 3 the best P-error is min(p_s3,p_s4); at time 2 after Y=y it is min(p_2(s,y),p_s3,p_s4); at time 1 compare p_s1 with the Y-expectation of that future minimum. The resulting sourcewise optimal P errors are

```text
A: 57/320       B: 1/4       C: 11/48.
min_FULL e_P = (1/8)*(57/320)+(1/8)*(1/4)+(3/4)*(11/48)
             = 577/2560.
EXACT_SUPPORT_GAP = min_LR e_P - min_FULL e_P = 47/2560.
```

The optimum is realized by the same A behavior as above, B stopping immediately, and C continuing at time 1, stopping at time 2 if Y=0, otherwise continuing through time 3 to forced time 4. Its full observer vector is

```text
O_opt = (577/2560,1549/3840,87/32,39/16).
```

Thus every real LR observer is at L-infinity distance at least 47/2560 from O_opt. The model has **strictly unequal FULL/LR convex hulls** and is a precisely quantified rejected mother candidate, not a hull-equal solution.

Finally, the LR policy that matches the *earlier O_witness* stopping-time flows has classwise time distributions

```text
d_AB=(1/2,1/8,3/8,0),   d_C=(1,0,0,0).
O_LRmatched=(79/320,41/160,39/32,23/16).
(e_P,e_Q)_FULL-(e_P,e_Q)_LRmatched=(-3/512,-1/256).
```

These exact signed error residuals coexist with exact matching of both time observers, proving that the BRC source/path distinction matters to the declared terminal readouts.

## 5. Verification boundary, authority and continuation

The actually executed `VERIFY.mjs` uses arbitrary-precision BigInt rational arithmetic with normalized numerator/denominator and positive-denominator comparisons. It checks initial P/Q normalization; all 12 potential nature leaves with positive kernels; each of 48 P/Q terminal-error probability pairs strictly between 0 and 1; ratio freezing; sourcewise centered terminal kernels; all 16 deterministic LR schedules; full witness and matched LR observers; sourcewise Bellman minima; full Bellman-optimal observer; exact support gap 47/2560; covariance residuals; and affine determinant 1/1280. Raw actual output is saved as `EXACT_OUTPUT.txt`. Finite arithmetic independently checks this *example*, while Theorems A/B for **all real policies and all finite trees** are proved by the flow, simplex and covariance arguments above. No Lean checker, prior-art priority finding, native X6 dynamical bridge, Source Result, independent review or P000 revision is asserted.

Native capability check during this run returned `research_authority_granted=false`, active job quota 5/5, and `CONTROL_QUOTA` on the live-owner inventory. Therefore these GitHub documents are portable author evidence, with native task admission and activity registration pending.

**Next exact discriminator:** construct a positive two-law stop tree with a *non-unit* LR update at some nature transition and a later exact collision at the same (time,LR) key, retaining genuine source-sensitive transitions and at least three consequential LR stop decisions. Then obtain, for **every** FULL deterministic four-observer vector, a rational LR convex representation of size <=5, or an explicit rational signed Farkas separator. Only if every representation exists should an all-real behavior-image nonmembership certificate be attempted. Preserve all zero-reach/behavior-boundary cases, provenance and frozen model assumptions. See `NEXT_TASK.md`.
