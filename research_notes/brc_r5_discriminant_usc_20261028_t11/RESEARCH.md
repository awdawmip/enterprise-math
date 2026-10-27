# R5 — Algebraic collision discriminant and one-sided stability of likelihood-ratio compression

Date: **2026-10-28, Asia/Shanghai**. Scientific status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED**. Scope: finite, strictly positive double-measure statistical observation trees, not native Heartbeat X6 evolution.

**Frozen input snapshots.** Account knowledge: **awdawmip/chatgpt-global-knowledge main@6247c9e5fffde5003b055b144d81565a99099cda** (both normative entry files, ACTIVE worldview and the applicable mathematical, BRC and code policies). Enterprise Math baseline: **main@7c27302dad89480a0c204fef6736c0db78c50e78** (project router, P000, Heartbeat X6/time, observer preservation, and portable research). Immediate predecessor: research_notes/brc_r5_collision_strata_20261028_t11/RESEARCH.md. That predecessor established a specific six-leaf collision discontinuity; the present note proves statements for **arbitrary finite positive-leaf observation trees**.

## Model and readout

Fix a finite rooted observation tree with at most N observation periods and m terminal leaves. At each time t, the eligible raw histories H_t index disjoint nonempty prefix cylinders C(h). Each terminal leaf j has P_j>0 and Q_j>0, and both distributions sum to 1. For any eligible prefix h define P(h)=sum of P_j in C(h), Q(h)=sum of Q_j in C(h) and R(h)=P(h)/Q(h).

A full-history behavioral decision rule conditions on h. A **seedless likelihood-ratio (LR) rule** conditions only on (t,R(h)); it does not retain a persistent common random seed across information sets. At each t a run visits at most one information set. Decisions are stop/continue and, on stopping, a P/Q declaration.

The declared four-dimensional observer is O=(e_P,e_Q,T_P,T_Q)=(P[declare Q],Q[declare P],E_P[tau],E_Q[tau]). For any signed real lambda in R^4, define V_full(theta,lambda) and V_LR(theta,lambda) as the maximum lambda·O over the respective behavioral strategy classes, theta=(P,Q), and define the nonnegative support gap Delta_lambda=V_full−V_LR.

## Theorem 1 — exact collision discriminant; generic losslessness

For distinct eligible histories h,g at the same t set

  d_hg(P,Q)=P(h)Q(g)−P(g)Q(h).

Define the **finite collision discriminant**

  D(P,Q)= PRODUCT over t=1,...,N and unordered distinct {h,g} in H_t of d_hg(P,Q)^2.

An empty product is 1. Every factor is a rational-coefficient polynomial of leaf masses. Under strict positivity:

1. D=0 **if and only if** some same-time distinct histories have identical LR signatures.
2. If D≠0, the LR signature uniquely identifies the complete history at every time. Thus **the actual strategy-outcome image sets are equal**, O_full(P,Q)=O_LR(P,Q), even for arbitrary real behavioral randomization. Indeed the action-path distributions under both P and Q can be matched, not merely four observations or their convex hulls.
3. The set D≠0 is open and dense, and has full relative Lebesgue measure, in the product of the two strictly positive normalized leaf-probability simplices. Its complement is a finite union of proper rational-algebraic hypersurface sections.

**Proof.** Q(h)>0 for every prefix, hence equality of two ratios is exactly d_hg=0. With all same-time ratios distinct, relabel the complete rule's action kernel at h as the LR action kernel at its unique signature (t,R(h)). This reproduces every path's conditional actions and joint outcomes under both measures. LR rules are already complete-history rules, proving equality.

For each distinct h,g at one time, their nonempty prefix cylinders are disjoint. Fix positive Q, move a small P mass from one leaf of C(g) to a leaf of C(h), and keep normalization and positivity. The determinant varies nontrivially, so it is not the zero polynomial on the affine simplex. The finite product is likewise nonzero as a polynomial on that simplex. The zero locus of a nonzero real polynomial has empty interior and Lebesgue measure zero. Continuity makes D≠0 open, hence it is also dense and full measure. QED.

**Implication for the mother problem.** Any strictly positive finite-tree model with conv(O_full)=conv(O_LR) but O_full≠O_LR **must lie on the algebraic singular locus D=0**. Generic unrestricted parameter perturbation cannot preserve a candidate's collision mechanism.

## Theorem 2 — explicit rational collision removal by changing P alone

Let P,Q have strictly positive rational leaf masses. There exists a strictly positive rational P* with the **same fixed Q** and D(P*,Q)≠0. In fact, for all sufficiently small positive rational s, P_s=(1−s)P+sP* remains normalized and strictly positive, and D(P_s,Q)≠0.

**Constructive proof.** Order the m leaves j=0,...,m−1. Choose an integer B≥2 and define Z(B)=sum_j Q_j B^j, P*_j(B)=Q_j B^j/Z(B). For any distinct same-time h,g, the numerator of d_hg(P*(B),Q) is

  Q(g) sum_{j in C(h)} Q_j B^j − Q(h) sum_{j in C(g)} Q_j B^j.

The largest leaf index in the disjoint union belongs to precisely one prefix, making its leading coefficient nonzero. Each pair therefore forbids at most finitely many integer B; finitely many pairs forbid only finitely many. Search B=2,3,... until all determinants are nonzero. This terminates and constructs rational P*.

Along P_s, each cross determinant is affine in s:

  d_hg(P_s,Q)=(1−s)d_hg(P,Q)+s d_hg(P*,Q).

When its initial value vanishes, only s=0 can be a zero on this line; when its initial value is nonzero, it remains nonzero for all sufficiently small s>0. Finitely many pairs admit a shared rational positive radius, proving the claim. QED.

## Theorem 3 — upper-semicontinuity and a one-sided stability certificate

For any fixed signed lambda, the support gap Delta_lambda(theta) is **upper semicontinuous** across the entire strictly positive finite-tree parameter space. This is a useful directional result: a collision-dependent gap can disappear abruptly when signatures split, whereas the limit superior of gaps at nearby inputs cannot exceed the gap at the limiting input.

More precisely, fix theta_0=(P_0,Q_0) and a sufficiently close theta'=(P',Q') for which histories with *distinct* base signatures remain distinct (base collision classes may split). Put

  eta_P=||P'−P_0||_1, eta_Q=||Q'−Q_0||_1,
  L=(|lambda_1|+N|lambda_3|) eta_P + (|lambda_2|+N|lambda_4|) eta_Q.

Then the certified one-sided bound is

  **0 ≤ Delta_lambda(theta') ≤ Delta_lambda(theta_0)+2L.**

If both inputs have the **same exact time-LR partition**, the two-sided bound |Delta_lambda(theta')−Delta_lambda(theta_0)|≤2L also holds. The constant 2L is a valid universal bound, not asserted optimal.

**Proof.** Fix any raw-history deterministic policy. Its lambda·O is linear in the P/Q terminal masses. Each P-leaf coefficient is bounded in absolute value by |lambda_1|+N|lambda_3|, and each Q-leaf coefficient by |lambda_2|+N|lambda_4|. Therefore any fixed policy value changes by at most L. Taking the maximum over finitely many complete-history deterministic policies, V_full(theta',lambda)≤V_full(theta_0,lambda)+L.

Distinct base ratios remain distinct in a small neighborhood because there are finitely many positive ratio separations. Thus the LR partition at theta' refines the base partition. Take an optimal LR action rule at theta_0 and assign its action law to each new signature contained in the corresponding old information class. It remains legal and its score changes by at most L. Hence V_LR(theta',lambda)≥V_LR(theta_0,lambda)−L. Subtraction gives the one-sided bound and upper-semicontinuity. Under an unchanged partition, transfer works both ways, giving the two-sided bound.

For completeness, strategy objectives are **multi-affine** in the independent local behavioral action probabilities: every realized path visits a given time-indexed signature at most once. Each signed linear objective therefore attains its extrema at deterministic strategy tables. All deterministic maxima used here also cover all real behavioral randomization, not a probability grid. QED.

**Exact no-new-merge radius.** Let q_* be the smallest Q_0-prefix mass and m_* the smallest positive separation |R_0(h)−R_0(g)| among same-time distinct base signatures (m_*=infinity if no such pair exists). With eta_Q<q_*, every prefix satisfies

  |R'(h)−R_0(h)| ≤ B := eta_P/(q_*−eta_Q) + eta_Q/[q_*(q_*−eta_Q)].

If 2B<m_*, distinct base signatures cannot merge. This rational inequality gives a directly checkable neighborhood for the one-sided stability certificate.

## Exact six-leaf P-only transverse check

The preceding R5 six-leaf model has (leaf: P0,Q0):

| Leaf | P0 | Q0 |
| --- | ---: | ---: |
| A,C,low | 1/24 | 1/12 |
| A,C,high | 1/8 | 1/12 |
| A,L | 1/12 | 1/3 |
| B,C,low | 1/32 | 1/8 |
| B,C,high | 7/32 | 1/8 |
| B,H | 1/2 | 1/4 |

The within-time prefix levels have sizes (2,4,4), hence exactly 13 unordered pairs. At the original weights, D=0 due to the sole pair (AC,BC) sharing ratio 1.

Transfer epsilon of **P mass only** from A,L to A,C,low, keeping every Q mass fixed. For every 0<epsilon<1/100, time-1 ratios remain (1/2,3/2); at time 2 the ratios (AC,BC,AL,BH) become (1+6epsilon,1,1/4−3epsilon,2); at time 3 (ACl,ACh,BCl,BCh) become (1/2+12epsilon,3/2,1/4,7/4). All signatures are distinct within each time. Therefore D>0 and O_full=O_LR as **true sets** for every such real epsilon>0.

At epsilon=1/10000, the exact smallest within-time signature gap is 3/5000; the squared discriminant is nonzero (numerator 157 bits, denominator 316 bits). For signed lambda=(912,456,128,−194), the original instance has (V_full,V_LR)=(868,857), Delta=11, while the P-only perturbed instance has **both supports 542557/625=868+912/10000 and Delta=0**. Thus the gap falls from 11 at the collision point to zero along an arbitrarily close P-only rational path. This is consistent with, and concretely demonstrates, the proved upper-semicontinuity.

The actual Python 3 standard-library Fraction verifier at VERIFY.py enumerates all 5,184 complete-history deterministic tables and 1,728 original collision-constrained LR tables; their original distinct outcome counts are 196 and 124. At the perturbed input, 5,184 complete tables correspond bijectively to 5,184 legal seedless LR tables because signatures are injective. The 1,728-table equal-C subset at the perturbed input is *not* its LR class, and is printed only as an audit. EXACT_OUTPUT.txt contains observed execution output ending with ALL EXACT DISCRIMINANT AND SUPPORT CHECKS PASSED.

## BRC/X6 bridge, literature and validation boundary

P000 fixes native six-axis discrete Heartbeat X6 Cell space with separately typed time, not a native plane. The finite histories here are typed statistical observer labels that may be injected into distinct chart-relative Cell identities; this is an **observer-label bridge**, not an asserted native X6 propagation law. Branch identity, ordered prefixes, P/Q positive rational masses, and sampling times are retained until the declared quotient is certified. The exact branch weights are a typed positive BRC carrier; cross determinants and signed support coefficients are **derived signed comparisons**, not positive branch masses.

Related external background, not a source for this proof, includes Blackwell experiment comparison (Khan, Yu and Zhang, Economics Letters 247, article 112146, 2025; DOI 10.1016/j.econlet.2024.112146) and Kuhn's behavioral/mixed strategy theorem (1953). Independent mathematical review, novelty checking, canonical Result and Driver admission remain separate.

## Next bounded research question

Parameterize a **fixed exact collision stratum D=0** of a new strictly positive rational tree with at least two independently controlled upstream signatures. Construct an exhaustive exact rational Bellman cone/facet certificate for **all** signed four-dimensional supports. Only after proving complete/full convex-hull equality should one exhibit a convex-hull point not realizable by **any real** seedless LR behavioral strategy. An exact rational separating direction eliminates the candidate instead of solving the mother question. Respect native owner/CLAIM, source identity and independent review before formal task promotion.
