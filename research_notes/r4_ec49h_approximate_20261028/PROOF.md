# EC49H — Approximate causal likelihood-ratio quotient: a two-sided raw-region bound

Date: 2026-10-28. **Author-side proved proposition and exact finite test; independent Driver review / native Result admission pending.** Continues EC49G, PR #1635, immutable commit c066b607682b89fd0bdb956b4d26e06cef2b0840. Domain: finite **positive-rational two-source auxiliary BRC probability observation tree**; not native signed BRC, X6 dynamics, or physical time. P000 and ACTIVE worldview remain unchanged.

## 1. Exact problem and assumptions

A finite horizon t=0,...,H-1 controls a fine observation-history tree. At each t, a fine history h maps to an observable, causally updateable compressed class s=s_t(h). The class includes stage and remaining action budget; each history in a class permits the same source-independent legal action set and incurs the same rational auxiliary clock cost c_t(s,a) in [0,M_t]. Accept/reject terminal labels are included as absorbing states (later clock cost zero). Positive source measures P and Q govern passive observations; one behavioral controller must use identical randomization under both sources. Its **raw** output is O=(alpha,beta,C_P,C_Q)=(P(accept),Q(accept),E_P T,E_Q T), where T is the sum of acquired-clock increments.

Write K_theta(h,a,s') for the conditional successor coarse-class distribution at a fine prefix h under source theta=P or Q. Choose a valid source-specific Markov reference model on compressed classes, with kernels barK_theta(s,a,s'), **the same** initial coarse distribution, legal actions, clock increments and terminal readouts. Let TV be one half of the sum of absolute mass differences. For each legal action and every fine h mapped to s, require:

  TV(K_theta(h,a,.), barK_theta(s,a,.)) <= epsilon_theta,t(s,a).

Set epsilon_theta,t to the supremum over s,a (zero for wholly absorbing stages). Initially impose **exact classwise prefix likelihood ratio**:

  P(h)/Q(h) = r_t(s)>0

for every fine passive observation/action history h in class s (strategy selection probabilities cancel in P/Q). This ensures that P and Q induce the **same** conditional action distribution on each coarse s even when the full policy depends on hidden fine history. A controller cannot infer exact r by merely preserving a sensor's marginal LR histogram (cf. EC49G).

## 2. Theorem EC49H-1 — quantitative raw-set conservation

Let S_full and S_ref be the full and compressed-reference sets of achievable original four-vectors, including every real source-independent behavioral randomized policy. Define

  B_theta = sum_{j=0}^{H-1} epsilon_theta,j,
  D_theta = sum_{t=0}^{H-1} M_t [sum_{j=0}^{t-1} epsilon_theta,j].

**For each** O in S_full there is O' in S_ref, and conversely **for each** O' in S_ref there is O in S_full, such that, in either direction,

  |alpha-alpha'| <= B_P,       |beta-beta'| <= B_Q,
  |C_P-C'_P| <= D_P,           |C_Q-C'_Q| <= D_Q.

Therefore the ordinary two-sided directed-Hausdorff maximum in unscaled L-infinity is no more than max(B_P,B_Q,D_P,D_Q). The explicit four budgets remain meaningful when probability and clock units differ. For **every** real coefficient vector lambda, the difference between optimal linear support values on the two raw regions is bounded by

  |lambda_1| B_P + |lambda_2| B_Q + |lambda_3| D_P + |lambda_4| D_Q.

This is not an equality claim at epsilon>0 and does not only control a single support functional.

**Forward proof.** Fix an arbitrary full-history strategy, and write d_theta,t(s) for the complete active/absorbing coarse-stage mass and x_theta,t(s,a) for its state-action mass. Because the source-independent action law cancels in each likelihood ratio and r is constant across fine histories in s,

  d_P,t(s)=r_t(s)d_Q,t(s),    x_P,t(s,a)=r_t(s)x_Q,t(s,a)

for reachable active classes. Define a legal **source-neutral** compressed policy pi_t(a|s)=x_Q,t(s,a)/d_Q,t(s), with arbitrary legal choice on zero-mass classes. Exact r makes this equal to x_P/d_P. The original source-theta outgoing class distribution, conditional on (s,a), is a mixture of the fine K_theta(h,a,.), so its TV distance from barK_theta(s,a,.) is bounded by epsilon_theta,t(s,a). Let bar_d_theta,t be the reference distribution under this same pi, and delta_theta,t=TV(d_theta,t,bar_d_theta,t). Markov-kernel contraction and convexity imply

  delta_theta,t+1 <= delta_theta,t
     + sum_{s,a} x_theta,t(s,a) epsilon_theta,t(s,a)
  <= delta_theta,t + epsilon_theta,t.

The initial distributions match, hence delta_theta,t <= sum_{j<t} epsilon_theta,j. Acceptance is an event on terminal coarse labels and incurs error at most delta_theta,H <= B_theta. At stage t, the common clock expectation is an expectation of the function g_t(s)=sum_a pi_t(a|s)c_t(s,a) in [0,M_t]. Its error is <=M_t delta_theta,t. Summing stages gives D_theta. No convexification or assumption of original fine-policy Markovity occurred.

**Reverse proof.** Run any reference pi_t(a|s) on the full tree, simply ignoring hidden fine-history distinctions. It is a source-neutral causal full controller. Given any active s,a, its mixture of fine conditional kernels remains within epsilon_theta,t(s,a) of barK_theta by convexity. Apply the same TV recursion, cost, and acceptance estimates source by source. This proves two-sided approximation of the *actual raw sets*. QED.

**Q-only residual certificate (exact r).** If the reference kernel is taken from a representative fine history and successor ratios r_(t+1)(s') are exact, then

  K_P(h,a,s') = [r_(t+1)(s')/r_t(s)] K_Q(h,a,s'),
  barK_P(s,a,s') = [r_(t+1)(s')/r_t(s)] barK_Q(s,a,s').

Consequently TV(K_P,barK_P) <= (max_successor r_(t+1)/r_t(s)) TV(K_Q,barK_Q). Thus a Q-kernel rational certificate plus exact source ratios gives a valid (possibly conservative) P bound; directly measured P errors may be smaller. The equality of two original raw regions follows exactly when all four budgets vanish, recovering the previous lumpability case.

## 3. Lemma EC49H-2 — LR oscillation as a separate error family

If exact r fails, suppose all positive fine prefix ratios within s lie in [l_t(s),u_t(s)] with l_t(s)>0. Then for any one source-independent fine behavioral policy, the induced conditional P and Q **action laws** on coarse s obey

  TV(pi_P(.|s),pi_Q(.|s)) <= rho_t(s)
     := min(1,(u_t(s)-l_t(s))/(2 l_t(s))).

Proof: conditioning on s, the P distribution on fine histories is obtained from Q by multiplying each fine-history probability by r(h)/E_Q[r|s]. Its TV from the Q fine-history law is (1/2)E_Q|r/E_Q[r|s]-1| <=(u-l)/(2l). Applying the common randomized action kernel contracts TV (data processing).

If both source-specific successor kernels are still within declared epsilon_P,epsilon_Q of *valid* reference P/Q kernels, compiling the original full strategy using pi_Q gains an **additional P action-law discrepancy** rho_t. A conservative forward bound is:

  B_P^osc=sum_t (epsilon_P,t+rho_t),
  D_P^osc=sum_t M_t [rho_t+sum_{j<t}(epsilon_P,j+rho_j)],

where rho_t is the sup over accessible active classes. Q retains B_Q,D_Q. In the reverse direction the lifted reference pi(s) is identical on each fine h, hence the original kernel-only estimates still apply. This is a **conditional relaxation**; an approximate LR alone does not imply P-kernel closeness from Q-kernel closeness, nor does it give exact common occupancy policies. Sharp constants and an independent positive-rational nonconstant-r stress test remain open.

## 4. Six strictly-positive rational leaves (per source), exact LR and strict loss

A freely visible source-neutral label W is 0 or 1 with probability 1/2 under each source. Full controller reads W; compressed controller forgets it. Both may immediately accept, immediately reject, or **buy one ternary sensor** Y in {u,v,z}, auxiliary clock cost 1, then accept/reject after seeing Y. No further acquisition is permitted.

The following table gives each source's Y probabilities conditional on W (multiply by 1/2 for actual labeled leaf masses):

|W|Q(u)|Q(v)|Q(z)|P(u)|P(v)|P(z)|
|--|--:|--:|--:|--:|--:|--:|
|0|22/48|15/48|11/48|11/48|15/48|22/48|
|1|26/48|9/48|13/48|13/48|9/48|26/48|

Each of the 12 source-specific entries is strictly positive. All rows sum to 1. At every W and Y the prefix LR is r(Y)=(1/2,1,2) for (u,v,z), independent of W, and r(root)=1. Forgetting W is therefore causally compatible with **exact LR at every observable stage**, even though Q and P sensor distributions vary with W. The compressed reference laws are the W mixtures:

  barQ=(1/2,1/4,1/4),   barP=(1/4,1/4,1/2).

For **each** W, TV(Q_W,barQ)=TV(P_W,barP)=1/16. An immediate stop has zero kernel error. With stage 0 purchase/stop and stage 1 terminal accept/reject, M_0=1,M_1=0 and epsilon_theta,0=1/16, epsilon_theta,1=0. The theorem bounds **both** directions by |delta alpha|,|delta beta|<=1/16 and **exactly** zero clock error.

Nonetheless define the linear support functional

  J(O)=alpha-(3/2)beta-(C_P+C_Q)/16.

The terminal optimal acceptance mask is *only* Y=z: for each outcome the conditional net accept contribution P(Y)-(3/2)Q(Y) is positive only when LR=2. Purchasing at a fixed W and accepting only z gains Q_W(z)/2-1/8. This equals -1/96 at W=0, +1/96 at W=1. Thus the W-visible optimum is to reject without purchase at W=0, and buy/accept-only-z at W=1. Its exact vector is

  O_full=(13/48,13/96,1/2,1/2),   J(O_full)=1/192.

A W-blind/coarse controller instead sees barQ(z)=1/4, so purchasing's optimal contribution is 1/8-1/8=0; rejecting yields 0; immediate accepting yields -1/2. Consequently every W-blind real-randomized strategy has J<=0, and

  sup_(S_full) J - sup_(S_ref) J = 1/192 > 0.

This proves strict raw-region non-equality (indeed the witness is outside the convex hull of the coarse region), **despite exact classwise LR and kernel TV only 1/16**. The W-blind actual observation law equals the chosen mixture reference, so this is genuine loss from forgetting W.

Q-occupation compilation of the displayed W-visible witness yields the valid W-blind randomized strategy: buy with probability 1/2, otherwise reject; on purchase accept only z. It realizes

  O_ref=(1/4,1/8,1/2,1/2).

The specific errors are |delta alpha|=1/48, |delta beta|=1/96 and clock errors=0, inside the theorem's componentwise bounds.

## 5. Verification, lineage and limits

At this PR path, run `python VERIFY.py` and compare the JSON stdout against `EXACT_REPORT.json`. The exact Fraction program verifies leaf positivity, normalization, all source LR identities, kernel TV=1/16, all **10** W-blind deterministic controllers and **100** W-visible deterministic controller pairs. It tests a Q-occupation compressed policy for every full pair and **250** reproducible rational strategy mixtures; asserts the exact separating support and witness, with maximum compiled acceptance error 1/32 under each source and zero clock error. Exhaustiveness covers the specified one-sensor finite pure-strategy set only. General theorems above are analytic; finite deterministic maxima hold for all real behavioral strategies by finite perfect-recall tree extremality.

Relation to EC49G: its *different* adaptive two-sensor example has 74 and 5476 pure-policy enumerations, clock costs (2,3/2), and support separation 1/48, and did not establish a complete exact-LR quotient after second acquisition. EC49H adds an explicit all-four-coordinate approximation bound with a new exact-LR ternary example and strict separation 1/192. No novelty claim is made for general TV simulation or approximate bisimulation methods.

BRC classification: **auxiliary positive-mass COMPOSE_APPLIED** — branch summation, conditionalization, and source-provenance-preserving quotient tests are used. No actual native signed BRC/phase cancellation, six-axis spatial carrier, rotation, address codec, or physical-heartbeat time is computed. Transferring this result to native P000/X6 requires a new typed readout and future-operation bridge. Native research authority and independent Driver acceptance remain separate.

External background, verified 2026-10-28: Bian & Abate (2017), *Bisimulation and trace equivalence in an approximate probabilistic context*, https://research.google/pubs/bisimulation-and-trace-equivalence-in-an-approximate-probabilistic-context/ (finite-horizon TV bisimulation bounds on labelled Markov chains); Torgersen (1991), *Comparison of Statistical Experiments*, https://www.cambridge.org/core/books/comparison-of-statistical-experiments/405F64D2A2FB3A4E6A1893C1C8A4A60B (deficiency/decision information comparison). Neither citation substitutes for the specific proof above.

**Status:** AUTHOR_PROVED / EXACT_FRACTION_FINITE_CHECK_PASS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. **Next:** EC49I robust occupation-weighted bounds, sharpness of LR oscillation penalty and the independently open irrational-witness problem, as specified in NEXT_TASK.md.
