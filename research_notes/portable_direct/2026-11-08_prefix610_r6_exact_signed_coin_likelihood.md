# PREFIX-610-R6 — Exact signed-coin likelihood and full-parameter Fisher theory for native BRC critical fibers

Date: 2026-11-08 Asia/Shanghai.
Research status: AUTHOR_PROVED / EXACT_SYMBOLIC_CHECKED / UNREVIEWED / NOT_ADMITTED.
Science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Original native graph: PREFIX565_positive_marginal_certificate.py; Git blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41.
Dependency: PREFIX-609 exact twelve-block source/terminal factorization; PREFIX-605 native null basis. All nine original allowed roots use the same phase/slot kernel. Independent author path, no formal CLAIM or review.

## Exact model

Use the positive-weight 12-incidence native BRC graph and any k simultaneously critical paired incidences, 4*t_e*t_f=1. Each critical pair gives two source contrast vectors h_l, with two +1 and two -1 source coefficients on disjoint phase supports. For active l=1,...,2k let pi_theta=uniform_48+sum_l theta_l h_l with |theta_l|<1/48. Every trial independently draws a source phase from this law, takes one native weighted action and observes the terminal phase together with one Boolean slot tag [slot=j], j=0,1,2. We consider N independent trials, not one length-N trajectory.

## Theorem — exact signed-coin reduction

For each active four-phase terminal block Q_l, each tagged/untagged terminal outcome atom Y has baseline probability p0(Y)>0 and derivative d_l(Y) satisfying

    d_l(Y)/p0(Y) in {+48,-48,0}.

Write its type as s_l(Y)=+1, -1 or 0 accordingly. The total baseline probability of informative atoms (s_l !=0) equals

    m_0=1/12 for slot0; m_1=m_2=1/24 for slot1/2.

Each sign separately has mass m_j/2; noninformative atoms in that group have baseline mass 1/12-m_j and their probabilities are theta-independent. Every outcome in a different terminal block has derivative zero with respect to theta_l. Consequently, for every theta in the open cube,

    Pr_theta(s_l(Y)=+1) = (m_j/2)*(1+48*theta_l),
    Pr_theta(s_l(Y)=-1) = (m_j/2)*(1-48*theta_l),
    Pr_theta(s_l(Y)=0) = 1-m_j.

The sign zero combines all uninformative and outside-fiber outcomes. Conditional on being informative in fiber l, s_l is a Bernoulli coin with

    Pr_theta(+1 | informative in l) = (1+48*theta_l)/2.

Across N draws, M_l (the informative sample count in fiber l) has marginal Binomial(N,m_j) distribution, independent of theta_l; the vector of group counts is multinomial rather than independent. Conditional on these counts, signs across fibers follow the specified independent biased-coin experiments.

## Corollary — exact Fisher information over the entire parameter cube

The per-observation Fisher matrix is diagonal, for every theta satisfying |theta_l|<1/48:

    I_j(theta) = diag_l [ c_j / (1-2304*theta_l^2) ],
    c_0=192,  c_1=c_2=96.

Thus slot0 contains **twice** the Fisher information of either other singleton-slot Boolean tag at every theta (not only at the uniform baseline). Each diagonal element is at least its baseline value. This statement concerns the original native terminal-phase+tag probability experiment and the declared 2k-dimensional phase-contrast family.

Proof. PREFIX-609 gives disjoint four-state terminal fibers. For one fiber and tag, the original graph equations show d_l(Y) is either 0, +48*p0(Y) or -48*p0(Y); the exact native rational identities sum the corresponding positive and negative baseline masses to m_j/2 each. The companion certificate verifies these identities for all six pairs, two signed blocks and three tags, with six independent positive symbolic weights x_0,...,x_5 and t_f=1/(4x). Every atom therefore has probability p_theta(Y)=p0(Y)*(1+48*s_l(Y)*theta_l) if |s_l|=1, and p0(Y) otherwise. The score on a positive/negative atom is 48*s_l/(1+48*s_l*theta_l). Its Fisher expectation is

    (m_j/2)*2304*[1/(1+48*theta_l)+1/(1-48*theta_l)]
    = 2304*m_j/(1-2304*theta_l^2) = c_j/(1-2304*theta_l^2).

Disjoint terminal supports give all off-diagonal zeros. QED.

## Exact finite-sample estimation

If M_l>0 and K_l^+ of the informative observations have positive sign, the conditional proportion estimator

    theta_tilde_l = (2*K_l^+/M_l-1)/48

is conditionally unbiased and has exact conditional variance

    Var(theta_tilde_l | M_l) = (1-2304*theta_l^2)/(2304*M_l).

There is probability (1-m_j)^N of observing M_l=0, which must be handled as a specified missing-data event rather than silently substituting a fictitious estimate.

An unconditional unbiased estimator, defined for every N>=1 and all theta in the cube, uses the baseline score S_l(Y)=48*s_l(Y):

    theta_hat_l = (1/(N*c_j))*sum_(a=1)^N S_l(Y_a).

Since E_theta S_l=c_j*theta_l and E_theta S_l^2=c_j, its exact full-cube covariance is

    Cov_theta(theta_hat)
      = [diag_l(1/c_j) - theta*theta^T]/N.

At theta=0 this equals (N*I_j(0))^-1 and attains the vector Cramer-Rao bound. For nonzero theta, the conditional-coin and unconditional-score estimators have distinct variances; select the estimator according to the requested target and missing-count handling.

## Verification, reuse, and future work

The companion Python certificate imports the exact PREFIX-609 source and frozen original graph, checks all twelve endpoint groups and three native Boolean tags in SymPy Q(x_0,...,x_5), checks 240 nonzero observation atoms and 144 symbolic sign-mass identities, and returns ALL_CHECKS_PASS (SymPy 1.14.0). PREFIX-609 supplies the 576 zero-direction checks and 36 baseline Fisher checks. Reuse: REUSE_EXECUTED native original BRC graph, PREFIX-605 and PREFIX-609 exact observer construction; REUSE_APPLIED PREFIX-608 information values. No hidden branch or phase collapse occurs; the signed-coin summary is valid only for this declared likelihood and estimand.

Next: develop exact confidence-region/sample-size bounds incorporating the zero-count event and study unknown-baseline/full 48-phase estimation. Evaluate the cost of observing terminal phase plus a Boolean native action tag in an operational implementation.
