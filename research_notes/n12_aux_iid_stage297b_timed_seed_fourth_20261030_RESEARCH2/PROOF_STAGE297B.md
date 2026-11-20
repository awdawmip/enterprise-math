# Stage297-B — Timed parity seed and sharp fourth-moment observer hierarchy

**Author / classification:** Research2, 2026-10-30; PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. This is a mathematical statement inside a declared external finite BRC-style ordered Bernoulli model, not a native P000/X6 theorem, physical heartbeat result, authenticated Source Result or independent review.

**Fixed read inputs:** GLOBAL_KNOWLEDGE_V1 main@a8b949c4cf3a47ae30a94b8d08e8ddeeb12e1e9d; Enterprise Math main@154ab052d3f249639c7af245ed7d9899e9efd99a; current P000 original blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488; ACTIVE Heartbeat/X6, joint relation preservation, researcher/activity and portable research protocols. Prior immutable science: Stage296-B at f44220d9c7fe64e743a38ca50c124cbb393b2ab6, Draft PR #1736. This work does not replace the P000 worldview and does not change its protected source.

## 1. Timed seed-erasure theorem

In the parity-mode model, let U be an independent fair bit, and Z in {E,X} have probabilities P(E)=3/8 and P(X)=5/8. Visit A emits A=U. The next visit emits B=U in mode E and B=1-U in mode X. This completely declares the finite hidden-state law, its temporal order and its allowed emissions.

**After B is observed:** U=A and Z=E if and only if A=B. Thus Z and U can be recovered as deterministic functions of the ordered visible pair (A,B). Any later kernel whose only otherwise hidden inputs are U and Z (and which has no other dropped inputs) factors through (A,B); deleting Z and U at this *post-B cut* is pathwise and future-observer exact. A future operation reading Z does not create a loss here. A blanket statement that deleting the parity-mode label always incurs positive TV is false.

**After A but before B:** for each visible A=u there are two positive-mass original states, (u,E) and (u,X), with distinct deterministic B outputs. No one-block *statewise strong* quotient on visible A reproduces both future B kernels. One binary Z label is sufficient; within these two states it is necessary. The same conclusion follows if the future action reads Z itself. This statement is at a specific time cut; it does not bar a weak initial-mixture simulator from resampling Z.

**Exact source-state-weighted error:** For any finite hidden label Z and visible X, a future action that reports Z without noise has statewise kernel delta_z. For a compressed free probabilistic kernel Q(.|X), the mean conditional-TV risk is

    R(Q) = sum_(x,z) P(x,z) TV(delta_z,Q(.|x))
         = 1 - sum_x P(x) sum_z P(z|x)Q(z|x).

Since the last expression is linear in each probability vector Q(.|x), its exact minimum is

    R* = 1 - sum_x P(x) max_z P(z|x).

This is the Bayes classification error, not unconditional pooled TV. Here X=A, Z is independent of A, so R*=3/8. If X=(A,B), R*=0 by the explicit decoder. Conversely a source-blind choice P(B=A|A)=3/8 generates exactly the pooled pair distribution Q=(3,5,5,3)/16 in the order (00,01,10,11), giving pooled TV 0 while failing original-Z-conditioned equality. Never conflate these metrics or treat optional S (the separately tagged initial source) as automatically equal to Z.

## 2. Exact future-label ambiguity even when the present pair law agrees

Let Q(00)=Q(11)=3/16 and Q(01)=Q(10)=5/16. Define two lifts of this *same* visible-pair distribution: in lift I an additional hidden W equals A; in lift II it equals B. An allowed future operation exposes W. On diagonal pairs the lifted laws agree; on off-diagonal pairs their conditional W laws are mutually singular. Hence

    TV( P_I(A,B,W), P_II(A,B,W) )
       = Q(A != B) = 5/8.

A single common free stochastic future kernel approximating both lifts has exact minimax TV 5/16: the triangle inequality gives a lower bound half their distance, and the midpoint of the two lifted laws achieves it. The extra bit here selects **which lift** is the true system; this is not the fixed parity-mode Z of Section 1. In that original parity model Z is already recoverable from (A,B). The underdetermination concerns an *unspecified future hidden readout*, not a contradiction with its explicit parity decoder. No claim is made that native BRC admits either arbitrary hidden lift without separate typing.

## 3. Four-visit truncated Hausdorff moment interval

Draw Theta once from a probability measure mu on [0,1]. Conditional on Theta, make four Bernoulli visits independently with common success parameter Theta. Let m_k=E_mu[Theta^k], m_0=1. Freeze the strictly feasible asymmetric rational triple:

    (m_0,m_1,m_2,m_3) = (1,3/5,11/25,43/125).

The precise attainable interval is:

    m_4 in [171/625,179/625], width 8/625.

**Necessary lower bound.** The moment Hankel matrix H2=(m_(i+j))_(i,j=0,1,2) is positive semidefinite because for every quadratic p, E[p(Theta)^2]>=0. Its upper-left H1 is positive definite: m2-m1^2=2/25>0. The Schur complement yields

    m4 >= (m2^3-2*m1*m2*m3+m3^2)/(m2-m1^2) = 171/625.

**Necessary upper bound.** For any real a,b, E[Theta(1-Theta)(a+b*Theta)^2]>=0. Therefore the localizing 2x2 matrix

    [[m1-m2,m2-m3],[m2-m3,m3-m4]]

is positive semidefinite. Since m1-m2=4/25>0 its Schur complement yields

    m4 <= m3-(m2-m3)^2/(m1-m2) = 179/625.

**Sufficiency for this complete fibre, with exact rational certificates.** Put

    mu_L = (1/3) delta_(1/5) + (2/3) delta_(4/5);
    mu_U = (2/15) delta_0 + (2/3) delta_(3/5) + (1/5) delta_1.

Direct rational evaluation gives exactly the same m0,m1,m2,m3 above for both, but m4(mu_L)=171/625 and m4(mu_U)=179/625. All mixing weights are nonnegative, total 1 and all nodes in [0,1]. For t in [0,1], the convex interpolation (1-t)mu_L+t mu_U preserves the three moments and gives every fourth moment in the stated interval. Thus upper/lower necessity and explicit attainment establish exactness without relying on a numerically sampled measure or an unproved general sufficiency assumption. The lower moments obey all strict interior inequalities: m2>m1^2, m1>m2, m3>m2^2/m1 and m3<m2-(m1-m2)^2/(1-m1).

## 4. General ordered-vs-success-stopping TV identity

For **every n>=1**, consider two laws of common mixed Theta as above, with identical moments m_0,...,m_(n-1). Write d=|delta m_n|. The probability of one specified ordered n-bit word containing k successes is E[Theta^k(1-Theta)^(n-k)]. Its highest-moment coefficient is (-1)^(n-k). Hence every one of the 2^n ordered words changes by absolute amount d. It follows exactly that

    TV(complete ordered n-bit laws) = 2^(n-1)*d.

For the observer reporting the first time of the **j-th success** (j=1,...,n), or a censored symbol if fewer than j successes occurred by n, all stopping-time events strictly earlier than n depend only on moments up to n-1. A hit at time n has probability

    C(n-1,j-1)*E[Theta^j(1-Theta)^(n-j)],

whose coefficient of m_n has absolute value C(n-1,j-1). The censored event changes by the opposite amount to preserve total mass, and all earlier events stay fixed. Consequently

    TV(j-th-success stopping laws) = C(n-1,j-1)*d.

These formulas require the declared *common-parameter conditional IID* mechanism and the equality of lower moments; they do not apply unchanged to retuned, history-dependent or time-varying physical ports. The proof uses binomial expansion and total-variation arithmetic, not a finite numeric grid.

For the rational n=4 fibre of Section 3, d_max=8/625. The full ordered four-bit law has sharp TV diameter 64/625. The j=1,2,3,4 success-stopping diameters are, respectively, 8/625,24/625,24/625,8/625. Corresponding exact minimax reconstruction radii among **valid common mixers** are one half of these: 32/625 for the ordered law and 4/625,12/625,12/625,4/625 for the stopped laws. Triangle inequality at the two endpoint witnesses gives the lower radius; their feasible midpoint mixing law gives the upper radius because all declared observation laws depend affinely on m4.

## 5. Exact verification, sources, limitations and next step

REPRO_STAGE297B.py was *actually executed* using Python's standard-library Fraction on this precise material: all four rational endpoints/support masses, first four common moments and Schur bounds, 16 nonzero ordered four-bit words, four censored stopping laws, elementary n=2..8 coefficient checks, parity reconstruction, statewise original-Z-conditional error and two hidden-W lifts. Saved stdout concludes STAGE297B_TIMED_SEED_FOURTH_MOMENT_EXACT_PASS. Finite checks only corroborate instances; Sections 1–4 contain the general proofs. Neither physical heartbeat/X6, native signed/phase BRC, native Result/Driver review, a formal proof assistant nor independent review was executed.

Related external work checked as of 2026-10-30: Nicholas G. Polson and Daniel Zantedeschi, “Predictive Coherence and the Moment Hierarchy: Martingale Posteriors for Exchangeable Bernoulli Sequences,” arXiv:2603.00661 (submitted 2026-02-28), https://arxiv.org/abs/2603.00661. It supports the broad moment-hierarchy/predictive-ambiguity context, **not** the exact constants derived above. Classical interval-polynomial positivity background: https://mathworld.wolfram.com/LukacsTheorem.html. No novelty claim is made for these classical principles.

**Stage298-B:** exact finite-label budget/error frontier for multiple time-adaptive actions reading discarded mode information; determine whether action-dependent future sigma-algebras admit a canonical minimal sufficient partition, and separately construct a typed X6/BRC packet/branch/time mapping with explicit future-observer descent obligations. Stage278-A Bellman N=12 remains a separate uncompleted frontier. The native Site presently does not authorize Source research publication; a GitHub author note is durable provenance, not CLAIM, Result, review or mathematical admission.
