# Stage302-B — Exact repair memory, source coupling, and Bayesian prediction

**2026-10-30; class: PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.** Independent Driver review and native Task/CLAIM/Result are separate future actions. This is an external finite positive-rational BRC-labelled probability model, not a P000 native dynamical or physical theorem.

## Frozen inputs and observer scope

Global: GLOBAL_KNOWLEDGE_V1 main@b86a7783db271ebadd217ac6acbd0249653336d3; global P000 startup matches V4 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Project: Enterprise Math main@bcd9709cc57f0313c734d0b53110f9f0d6f0cd1a; project P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. ACTIVE joint-relation/observer and Heartbeat World constraints, current portable protocol, weighted BRC substrate, and Stage301-B proof at immutable commit 7eaac56362f7122b02789250c531b76212cb7fc4 were read. No original-worldview content is altered.

At start, S is a fair hidden source bit; initial visible X is a separate fair bit. At each of n subsequent rounds, an examiner chooses H or F using previous visible outcomes and action labels, with optional source-independent policy coins. H generates a new independent fair bit. F generates a new Bernoulli bit of parameter p_S, p_0=1/4, p_1=3/4; innovations are mutually independent conditional on S. Let P_s^pi denote the complete visible, action-labelled path law conditional on S=s; the pooled law is M^pi=(P_0^pi+P_1^pi)/2. Positive-rational BRC branches retain (S,X,actions,outputs,order,multiplicity). Pooling erases only S, under a declared observer lease.

O_visible never reads the externally fixed S. O_source reads the **same pre-existing** S, potentially only after n rounds. O_joint also reads a private persistent J, compared to a reference J_ref=S. A synthetic S sampled retrospectively from a posterior is not the pre-existing external S unless a genuine coupling was installed. The source-blind simulator's law Q^pi cannot depend on that S. Total variation is TV(P,Q)=sum_path |P-Q|/2. Source-labelled risk is sup_pi [TV(P_0^pi,Q^pi)+TV(P_1^pi,Q^pi)]/2.

## Theorem 302.1 — Two exact pooled repairs, all finite adaptive horizons

**A. Persistent generative two-state repair.** Choose J~Bern(1/2), independent of S if only O_visible is required; emit X and every H as independent fair bits, and F as conditionally independent Bern(p_J). For every n and every visible-history-adaptive randomized examiner, the full action-labelled simulator law is exactly M^pi. The pair (J,visible paths) also matches (J_ref=S,visible paths) when the actual external S is not separately observed.

**B. Deterministic posterior repair.** Let k be the count of previous F outputs, ell the count of F successes, and d=2ell-k. Posterior odds satisfy Pr(S=1|history)/Pr(S=0|history)=3^d, hence

    b(d)=Pr(S=1|history)=3^d/(1+3^d),
    r(d)=Pr(next F=1|history)=(1+3*3^d)/(4*(1+3^d)).

An F success increments d, an F failure decrements it, while X or H leaves it unchanged. Draw a new bit with success rate r(d) for F and 1/2 for H. This causal model matches M^pi for all finite n and all such policies simultaneously, without a persistent private latent seed.

**Proof.** Condition the original and repair A on the respective fair source label j. Their complete transition kernels, including the decisions of a common policy at each visible history, are equal. Averaging over j gives equality of all path cylinders; conditioning on policy coins covers randomized policies. For B, the F likelihood ratio (S=1 versus S=0) is 3 for a success and 1/3 for a failure; X, H, and a source-blind policy selection contribute ratio 1. Bayes' rule gives b(d), and averaging p_0,p_1 with this posterior gives r(d). The two systems therefore have identical conditional next-step output laws at every positive-mass visible history, and induction proves equality of all complete paths. QED.

## Theorem 302.2 — Memory minimality depends on implementation interface

Within the restricted generative class where F outputs are conditionally IID given ONE persistent hidden label and the label fixes their success rate, at least two latent rates are required: the original two-F covariance is

    E[p_S^2]-E[p_S]^2 = ((1/4)^2+(3/4)^2)/2-(1/2)^2 = 1/16,

whereas any one-state fixed-rate IID model has zero covariance. The two-rate J construction achieves the pooled process; thus its hidden-state support size two is optimal **in this generative class**, not for arbitrary causal simulators.

Conversely, consider deterministic finite predictive summaries of observable history where the next F rate depends only on that summary (no latent seed and no retained external history). After exactly k F observations, all k+1 integer values d=-k,-k+2,...,k occur with positive probability. Since r(d) strictly increases with d, all have distinct next-F predictions. If one further F operation is allowed, at least k+1 deterministic predictive states are required, and the d statistic attains this count. Across histories with at most N previous F outcomes, d ranges over all 2N+1 integers from -N to N, so unbounded horizons cannot be supported by one fixed finite deterministic predictive-state budget. An observer retaining complete history externally is outside this state-budget assumption. The generative hidden Markov two-state implementation does not contradict this: its prediction uses an evolving posterior belief.

## Theorem 302.3 — Reading the original S requires a real joint coupling

Allow an arbitrary joint law of the *externally fixed* S and repair seed J, and put q_s=Pr(J=1|S=s). The simulator uses F rate p_J. For just one F output, the source-conditional mean-TV risk is

    R_1 = (|p_0-E[p_J|S=0]|+|p_1-E[p_J|S=1]|)/2
        = (q_0+1-q_1)/4.

The equality follows from p_1-p_0=1/2 and 0<=q_s<=1. Thus R_1=0 if and only if q_0=0, q_1=1, i.e. **J=S almost surely** with the stated mapping of rates. The exact coupling J=S also gives equality for every finite adaptive visible policy even when the actual S or J_ref is read later. For independent fair J, q_0=q_1=1/2, and R_1=1/4. If the observer requests the joint label pair (S,J_ref=S), replacing J_ref with an independent fair J changes its law by TV=1/2. Reading J_ref alone together with visible paths, but never reading S, *is* safe for the independent-J generative simulator, as in 302.1(A). These are different observer interfaces.

## Theorem 302.4 — Exact source-blind minimax for every horizon

For each integer n>=1 let the examiner choose H/F causally during n rounds, retaining all action labels; allow an eventual read of the original S. Among all source-blind causal simulators, the simultaneous minimax source-labelled risk is

    R_n^* = TV(Bern(1/4)^{tensor n}, Bern(3/4)^{tensor n}) / 2.

If K has Binomial(n,1/4) law, then

    2 R_n^* = 1 - Pr(K=n/2) * 1_{n even} - 2 Pr(K>n/2).

Values: R_1=R_2=1/4, R_3=R_4=11/32, R_5=R_6=203/512, R_7=1759/4096.
For all n,

    (1-(sqrt(3)/2)^n)/2 <= R_n^* <= 1/2,

so R_n^* tends to 1/2 as n grows.

**Proof of lower bound.** For any particular visible examiner pi and any source-independent Q^pi, the triangle inequality implies (TV(P_0^pi,Q^pi)+TV(P_1^pi,Q^pi))/2 >= TV(P_0^pi,P_1^pi)/2. Selecting F at every round yields exactly the n-fold Bernoulli source separation, hence a universal lower bound TV_n/2.

**Proof of upper bound and simultaneous attainment.** For an arbitrary policy pi, pre-sample n F innovations for each source, n fair H innovations, the independent X and policy random coins. The construction that follows the policy and emits either pre-sampled H or F bits is a common, source-independent Markov kernel from the n source-specific F draws to the full action-labelled path. TV contracts under this kernel, so TV(P_0^pi,P_1^pi)<=TV_n. The same posterior simulator of Theorem 302.1(B) generates Q^pi=M^pi for *every* pi, where its mean source-TV equals TV(P_0^pi,P_1^pi)/2 <=TV_n/2. The lower and upper bounds coincide.

**Proof of formula and limit.** For a bit word with j ones, P_1(word)/P_0(word)=3^(2j-n). Therefore the optimal TV sign set is j>n/2 and equal-likelihood ties j=n/2 contribute nothing. Reflection of the two binomial laws gives the formula above. Also TV_n=1-sum_word min(P_0,P_1) >= 1-sum_word sqrt(P_0 P_1)=1-(sqrt(3)/2)^n. QED.

This minimax statement excludes examiner access to S **before** its source-blind action choices; it permits an S-read after observations for evaluation. Once S is revealed earlier, the allowed policy class and the simulator's information interface must be redeclared. Retrospectively sampling a synthetic label from the posterior can reproduce a synthetic joint law but cannot reproduce a separately fixed external source read without a coupling.

## Evidence, BRC reuse, and native boundary

Executable standard-library Python Fraction verifier enumerates all 64 deterministic two-round policies, 1024 strictly-positive source-conditioned action-labelled path contributions, exact binomial laws for n=1..7, posterior-path equality, two-F covariance and one-step S/J coupling errors. Its actual log ends STAGE302B_SOURCE_COUPLING_POSTERIOR_EXACT_PASS. Finite verification checks the example; the universal conclusions follow from the proofs above.

BRC reuse: **REUSE_APPLIED** to the existing positive-rational weighted branch, provenance-labelled ports, observer-lease and source-pooling law. Fraction arithmetic is an auxiliary verification tool, **not** an executed native Heartbeat/BRC kernel. No novelty claim for Bayesian filtering, likelihood ratios, data processing or general BRC machinery.

Native transfer remains a distinct obligation: no exact embedding into six signed native X6 chart coordinates, ordered one-axis path algebra, chosen three-dimensional slice with specified third coordinate, triadic closure E, separate true-time dynamics, registered six-nonnegative-field Cell codec, or commuting source/operation/observer map was established.

**Next unit Stage303-B:** optimize n-round source-tagged risk under imperfect or delayed S/J coupling; find an exact formula or a smallest rational adaptive-policy counterexample, and keep native X6/BRC transfer independent. The canonical Task, Source Result and independent Driver admission remain pending.