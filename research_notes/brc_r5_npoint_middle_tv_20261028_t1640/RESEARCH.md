# R5 — Sharp middle-order TV ratio for any number of next likelihood ratios

Date: 2026-10-28 (Asia/Shanghai). Author-side local role: LOCAL_EM_R5_20261028_1640_NPOINT_TV / TASK_RESEARCH. This local label does not confer a native session, CLAIM, Source Result or review authority. Mathematical status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED.

Frozen global input: awdawmip/chatgpt-global-knowledge main@6e5b93c07e83298ff051acfbf1ed032ebbb155b2. Canonical P000 original Git blob: 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, matching the startup projection. Frozen Enterprise Math scientific input: main@c318a8ad19cffc14d2911ffc4ccb8ca24b991506. ACTIVE worldview, current TASK_RESEARCH route, portable research and BRC priority were used.

Predecessor: research_notes/brc_r5_occupation_weighted_tv_20261028_t1440/RESEARCH.md established the three-next-signature exact identity and occupation-weighted compression bounds. research_notes/brc_r5_two_level_signed_support_phase_20261028_t1540/RESEARCH.md excluded the exact 22-history tree from the mother-problem search by a strict signed-support gap. This note extends the first identity from three to arbitrary finitely many successor ratios. It does not redo the 22-history search.

## Exact setting

Two hidden sources a and b have the same parent likelihood ratio r=P(h)/Q(h)>0. Their conditional next-step likelihood-ratio signatures belong to a common ordered finite list 0<s1<...<sn. Under Q the two conditional probability kernels are q^a and q^b. Under P their kernels are p_i^c=(s_i/r)q_i^c, c=a,b. By conditional normalization, each q^c satisfies sum_i q_i^c=1 and sum_i s_i q_i^c=r. A missing signature under one source may be padded by zero; the sharpness constructions below use strictly positive masses at every signature.

Set v_i=q_i^a-q_i^b, d_Q=TV(q^a,q^b)=sum|v_i|/2, and d_P=TV(p^a,p^b)=sum s_i|v_i|/(2r). The TV distances are between *next-signature probability kernels*, not spatial lengths, signed BRC amplitudes or native X6 dynamics.

## Theorem 1 — exact second-extreme interval, with positive attainability

For n<=2 the two kernels coincide (d_Q=d_P=0). For n>=3 and d_Q>0,

    (s2/r)*d_Q <= d_P <= (s(n-1)/r)*d_Q.                  (1)

Both coefficients are optimal for every fixed strictly increasing signature list and any fixed r strictly between s1 and sn: each endpoint is attained by a pair of *strictly positive* P/Q conditional kernels. If n=3 the formula collapses to the equality d_P/d_Q=s2/r. If n>=4 every real value in [s2/r,s(n-1)/r] is attained; whenever the signature data, r and desired ratio are rational, all kernel probabilities can be rational.

### Proof over all real kernels

The two normalization laws yield sum v_i=0 and sum s_i v_i=0. For n<=2 the two independent linear equations force v=0.

For d_Q>0 let v_i^+=max(v_i,0), v_i^-=max(-v_i,0). The positive and negative parts each have total mass M=d_Q, and equal first s-moment, so their shared mean is

    m=sum(s_i*v_i^+)/M=sum(s_i*v_i^-)/M
     =sum(s_i*|v_i|)/(2M).

The identity d_P/d_Q=m/r follows directly from the definition of d_P.

Suppose m<s2. All signatures except s1 are at least s2; for *each* of the positive and negative parts to have mean below s2, both must place positive mass at index 1. This contradicts v_1^+ v_1^-=0. Hence m>=s2. The symmetric argument at the last index shows m<=s(n-1). Thus (1) holds for every real-valued conditional kernel without a grid or limiting argument.

For attainability at any interior index j=2,...,n-1, define a signed vector u^(j) supported on indices 1,j,n by

    u_1=(sn-sj)/(sn-s1),  u_j=-1,
    u_n=(sj-s1)/(sn-s1),  all other u_i=0.

It has sum u_i=sum s_i u_i=0; sum|u_i|/2=1; and its positive/negative s-means are both sj. A strictly positive baseline q0 with sum q0=1 and sum s_i q0_i=r exists: give every interior index a sufficiently small positive mass and adjust the two endpoint masses, possible since s1<r<sn. For small epsilon>0, q^a=q0+epsilon*u^(j) and q^b=q0-epsilon*u^(j) are strictly positive Q kernels of mean r; multiplying by s_i/r gives strictly positive normalized P kernels. Their TV ratio equals sj/r. Thus j=2 and j=n-1 attain both endpoints.

For n>=4 consider u(theta)=(1-theta)u^(2)+theta u^(n-1), 0<=theta<=1. Both constituent circuits are positive only at the extreme indices and negative only at interior indices. No cancellation occurs, so sum|u(theta)|/2=1 and the common signed-mass mean is (1-theta)s2+theta s(n-1). A sufficiently small positive epsilon provides strict positivity throughout. With rational input and rational theta take rational q0 and epsilon. This constructs the entire asserted range and completes the proof.

## Corollary 2 — heterogeneous hidden-source fiber

Let F be any same-(time,r) fiber, with all its hidden sources' next-signature laws supported on the ordered union s1<...<sn. Let delta_F^mu be the maximum pairwise TV distance of these laws under mu. For n>=3,

    (s2/r)*delta_F^Q <= delta_F^P <= (s(n-1)/r)*delta_F^Q.

For n<=2 both diameters vanish. Apply Theorem 1 to each pair and take maxima; the two-source construction proves sharpness.

## Corollary 3 — sharper occupation-weighted two-law budgets

In the preceding occupation-flow compression theorem, the actual continuing masses satisfy C_F^P=r_F*C_F^Q. Let epsilon_t^mu=sum_{F at stage t} C_F^mu delta_F^mu. Theorem 1 gives the exact valid envelope

    sum_F s(F,2)*C_F^Q*delta_F^Q
       <= epsilon_t^P
       <= sum_F s(F,n(F)-1)*C_F^Q*delta_F^Q,

with only fibers having >=3 successor signatures included (all others contribute zero). The upper coefficient s(F,n-1) is strictly smaller than the previously available crude maximal-next-signature coefficient s(F,n) whenever these ordered values differ. This refines an error estimate; it does not by itself establish zero information loss or equality of full and LR behavioral images.

## Exact rational sharpness example and actual execution

Take s=(1/2,1,2,3), r=3/2, q0=(1/4,1/4,3/8,1/8), epsilon=1/100, and

    u^(2)=(4/5,-1,0,1/5),
    u^(3)=(2/5,0,-1,3/5).

Let u(theta)=(1-theta)u^(2)+theta*u^(3) and q^a=q0+epsilon*u(theta), q^b=q0-epsilon*u(theta). Both laws are positive and normalized for all theta in [0,1]. In exact arithmetic, TV_Q=1/50 and TV_P=(1+theta)/75. Hence the TV ratio runs across the entire sharp interval [2/3,4/3] through the strictly positive models. These are mathematical identities, not numerical extrapolations.

The attached VERIFY.py was actually executed using Python fractions.Fraction. It checked positivity, P/Q conditional normalization and moment laws at five rational theta values; it also enumerated 3169 distinct positive-rational same-r kernel pairs with n=4,5,6, checking the exact mean identity and both inequalities. EXACT_OUTPUT.txt is the captured execution output. Finite checks validate the stated data and implementation; the all-real theorem rests on the complete proof above.

## BRC application, limitations and next question

BRC REUSE_APPLIED: positive rational Q/P branch masses, source-tag provenance, likelihood-ratio transport p=(s/r)q, the signed zero-mass/zero-first-moment residual v and its unsigned TV observer. The vanishing first two readouts do not imply equal branch distributions or future policy behavior. The 3-signature circuit is an algebraic representation, not a claim about P000's native three-force equilibrium.

External subject background only (not citations of this exact theorem or historical priority claims):
- Laroche & Tachet des Combes, On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs, PMLR 202 (2023), https://proceedings.mlr.press/v202/laroche23a.html
- Demirci, Kara & Yüksel, Computable Robustness Bounds to Transition and Measurement Kernel Perturbations and Approximations in Partially Observable Stochastic Control (2025), https://arxiv.org/abs/2508.10658

The result applies to finite external two-measure statistical kernels; native Heartbeat World X6 state embedding, full relation preservation, and physical interpretation remain independent proof obligations. Source owner/CLAIM and independent review were not verified; historical reports of CONTROL_QUOTA are not new live receipts.

Next task: use the sharpened per-fiber budget to screen interacting two-level predictive-heterogeneity models. The mother problem remains open: prove *all signed four-coordinate support directions* have equal full and seedless-LR optimal values, then find an exact rational full-image vector with a global semialgebraic nonmembership certificate for all real seedless-LR policies, retaining all terminal declarations and continuation choices.
