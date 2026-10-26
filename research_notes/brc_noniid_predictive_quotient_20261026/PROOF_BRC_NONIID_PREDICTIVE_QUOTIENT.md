# Finite non-iid BRC predictive quotients: exact Markovization, coarsest strong refinement, and rational obstructions

**Status:** AUTHOR mathematical proof and finite exact rational author checks. No Research Driver review, native CLAIM/Result, Lean check or native P000/Heartbeat correspondence. This is a separate independent auxiliary model, not an adoption of any active N14 owner.
**Frozen input:** GLOBAL_KNOWLEDGE_V1 main@9da1905975542838d289c9ef625bd01a4223f665; Enterprise Math source main@81784ac0d749311b87b7974884230541becf6ad1; original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc.
**Predecessor:** research_notes/brc_iid_lr_markovization_20261026/PROOF_LR_MARKOVIZATION.md and NEXT_PROBLEM.md. GitHub actor: awdawmip; native task list returned CONTROL_QUOTA, own native session_start rejected STATIC_READONLY_SCOPE_DENIED with operation_sent=false.

## 1. External model and typed observer

A finite rooted history tree has horizon N. For every admissible edge h to hy, the conditional probabilities p_h(y), q_h(y) are strictly positive rational numbers under P and Q, both rows sum to 1, and the tree has identical support under both hypotheses. The full-prefix likelihood ratio is lambda_n(h)=Q(h)/P(h). A common behavioral policy chooses actions D_P, D_Q or continue (the latter absent at horizon N); its history-conditional action probabilities are independent of which hypothesis is true. Its observer is (e_P,e_Q,t_P,t_Q)=(P[decide Q],Q[decide P],E_P tau,E_Q tau).

Let T_n map depth-n ordered histories into finite classes X_n. This is an observer-scoped quotient: ordered identities and future hidden-history interventions are not claimed preserved. Define K^P_h(x')=sum_{y:T_(n+1)(hy)=x'} p_h(y).

Two sufficient conditions are:
(LR) lambda_n(h)=ell_n(T_n(h)) at ALL depths, including N.
(PL) K^P_h(x')=k_n(T_n(h),x') for all h, n<N and successor classes x'. This is strong P-lumpability, independent of the policy.

### Lemma 1: P-lumpability already implies Q-lumpability under (LR)

For x=T_n(h) and any successor x', every corresponding edge satisfies

 q_h(y) = [ell_(n+1)(x')/ell_n(x)] p_h(y).

Indeed Q(hy)/Q(h)=[lambda_(n+1)(hy)/lambda_n(h)] P(hy)/P(h). Summing gives

 K^Q_h(x')=[ell_(n+1)(x')/ell_n(x)] k_n(x,x').

Thus Q has an x-dependent transition kernel automatically; a second, separately assumed Q-lumpability hypothesis would be redundant. Summing over x' gives the required Q row normalization.

### Theorem 2: exact two-measure Markovization

Assume (LR) and (PL). Every full-history randomized stopping/decision policy pi has a policy beta depending only on (n,T_n) with exactly the same four observer values AND the same per-time/per-T-class live and action P/Q masses.

Proof: Let s_pi(h) denote survival probability after seeing prefix h, integrated over previous internal policy randomization. Put mu(h)=P(h)s_pi(h), m_n(x)=sum_{T_n(h)=x} mu(h), and u_(n,x,a)=sum_{T_n(h)=x} mu(h) pi_a(h). Since lambda is constant on each fiber, the corresponding Q live/action masses are ell_n(x)m_n(x), ell_n(x)u_(n,x,a). Define beta_a(n,x)=u_(n,x,a)/m_n(x) on positive-mass classes and any legal action probabilities on unreachable classes.

At depth zero both policies have the same mass. If the live P masses agree at depth n, the per-class P action masses agree by beta's definition and the Q masses by (LR). The P mass entering x' in the original policy is

 sum_x sum_{h:T_n(h)=x} mu(h) pi_C(h) K^P_h(x') = sum_x u_(n,x,C) k_n(x,x'),

exactly the expression for the quotient policy, using (PL). Thus P live masses agree at n+1; Q masses agree because lambda_(n+1) is constant within x'. Induction proves the claim. The four observer formulas are

 e_P=sum_(n,x) u_(n,x,D_Q),  e_Q=sum_(n,x) ell_n(x)u_(n,x,D_P),
 t_P=sum_(n<N,x) u_(n,x,C),  t_Q=sum_(n<N,x) ell_n(x)u_(n,x,C).

All four therefore agree exactly. QED.

Corollary: the nonnegative P-action-flow LP with m_0(root)=1, m_n(x)=sum_a u_(n,x,a), m_(n+1)(x')=sum_x u_(n,x,C)k_n(x,x'), no C at N, and the four linear observer forms above gives EXACTLY the feasible observer set over all full-history policies. Conversely every feasible flow induces a T-policy u/m on positive classes. This is not an LP relaxation.

## 2. The coarsest strong predictive repair

Starting with arbitrary declared T, recursively construct partitions E_n backwards. At terminal depth N, h and k are equivalent iff their pairs (T_N,lambda_N) match. At n<N, h and k are equivalent iff their (T_n,lambda_n) agree AND their P transition probability vectors over the already constructed E_(n+1) classes agree componentwise.

**Theorem 3.** E satisfies (LR) and (PL). It is the coarsest layerwise refinement of T that does so for all depths: every other T-refining statistic R whose own state fibers are LR-constant and P-strongly-lumpable must refine E.

Proof: E has the two properties directly by construction. For coarseness use backward induction. Every valid R_N refines the (T_N,lambda_N) terminal partition E_N. If R_(n+1) refines E_(n+1), an R_n-equivalent pair must agree in T_n and lambda_n. Its equal P transition masses into each finer R_(n+1) class also sum equally into every union constituting an E_(n+1) class; it is therefore E_n-equivalent. Hence R_n refines E_n. QED.

This is coarsest within the *strong predictive LR-compatible refinement class*. It does NOT assert minimal state dimension for preserving only four scalar observers, which could admit weaker policy-specific quotients. Its signatures use exact positive rational sums and retain the branch/transition residual required by this particular future-operation lease.

## 3. A carefully scoped policy-specific weakening

For a FIXED full-history policy pi, form its P-live-fiber averaged beta as in Theorem 2 even if (PL) fails. Define, for each next class x' and depth n, the exact signed incoming defect

 D_(n+1)(x') = sum_{h in H_n} [P(h)s_pi(h)pi_C(h) - P(h)s_beta(h)beta_C(T_n(h))] K^P_h(x').

Under (LR), vanishing of every such defect is necessary and sufficient for equality of the entire per-depth T-class P live occupation profiles for this specific canonical beta. Necessity is the forward conservation equation; sufficiency follows inductively from equal incoming masses, beta's P-action averages and fiberwise LR equality, which also yields Q equality. This is a sufficient, but not necessary, test for equality of *only the four scalars*. The quantifiers are: FIX pi; CONSTRUCT beta; CHECK its actual defect. Do not replace this by an unconditional claim that ALL full-history policies can be compressed without (PL). The beta-induced hidden-history distribution need not equal the original policy's within-fiber distribution.

## 4. Exact non-iid rational counterexample: LR alone is insufficient

Take N=2, P(a)=Q(a)=P(b)=Q(b)=1/2 at depth one. Conditional second symbols 0,1 are:

 Prefix a: P=(9/10,1/10); Q=(1/10,9/10).
 Prefix b: P=Q=(1/2,1/2).

Let T_0=root, T_1(a)=T_1(b)=x, and T_2 retain the entire terminal ordered history. (LR) holds at all depths because lambda_1(a)=lambda_1(b)=1 and terminal classes are singletons. (PL) fails. A full-history policy first observes a/b; after a continues and decides P on 0, Q on 1; after b stops with a fair P/Q choice. Its exact observer tuple is

 (e_P,e_Q,t_P,t_Q) = (3/10,3/10,3/2,3/2).

No T-only policy reproduces it. To include root stopping, let r be the probability it observes the first symbol and s the probability it continues at the unique depth-one class. Then t_P=t_Q=r(1+s). Matching 3/2 implies 3/4<=r<=1 and rs=3/2-r<=3/4. No P/Q information exists at the root, after the collapsed first symbol or in the b subtree. Only a->(0/1) can improve the sum of two errors below one; conditional total variation there is |9/10-1/10|=4/5, and the probability of sampling that a subtree is rs/2. Thus every randomized T-only strategy with this expected sample cost satisfies

 e_P+e_Q >= 1-(4/5)(rs/2) >= 1-(4/5)(3/8) = 7/10 > 3/5.

This is a continuum-wide exact impossibility bound, not a finite numerical search. Horizon two is the first depth at which failed continuation lumpability after a merged intermediate fiber can matter; no global minimal-alphabet claim is made.

**Opposite failure (PL without LR).** For N=1, P(a,b)=(3/4,1/4), Q(a,b)=(1/4,3/4); merge the two terminal symbols into one T class. P-lumpability at the root is automatic but terminal LR constancy fails. Observe once; decide Q after a, P after b. The full policy has (3/4,3/4,1,1), while every T-only policy has e_P+e_Q=1, not 3/2. Hence neither condition can be discarded by itself.

## 5. Positive genuinely history-dependent witness and exact checks

Again P(a)=Q(a)=P(b)=Q(b)=1/2 at depth one. At depth two the symbols are 0A,0B,1A,1B, with P rows

 a: (1/2,1/10,1/10,3/10);  b: (1/5,2/5,1/5,1/5).

For each history multiply the P probability of either 0* symbol by 4/3 to get Q and either 1* symbol by 1/2 to get Q; Q rows still sum to one. T_1 merges a,b into x; T_2 retains only the leading 0 or 1. The original P conditional law varies with the hidden first symbol and is not iid, but P pushforwards to T_2 are (3/5,2/5) in both cases. Q pushforwards are (4/5,1/5). LR values are ell_1(x)=1, ell_2(0)=4/3 and ell_2(1)=1/2. Theorem 2 applies.

A fully specified history-dependent rational policy encoded in VERIFY_PORTABLE.py has exact observer tuple (341/600,10489/25200,3/2,3/2). Its P-fiber averaged beta has at depth one (D_P,D_Q,C)=(5/24,7/24,1/2), at terminal T_2=0 P-decision probability 97/252, at terminal T_2=1 P-decision probability 151/280. Exact tree enumeration returns the identical tuple before and after compression. Bottom-up strong predictive class counts by depth are (1,1,2) for this positive witness versus (1,2,4) for the nonlumpable counterexample.

## 6. Evidence, typed reuse and limitation

Author executed Python standard-library Fraction verifier (VERIFY_PORTABLE.py) and a separately expanded author cross-check (local research package), retaining exact rational weights, tree histories and action flow; stdout is in EXACT_CHECK_OUTPUT.md. These finite checks confirm the two displayed witnesses and partition counts; general mathematical claims rely on the proofs above, not finite experiments. BRC reuse is **REUSE_APPLIED** to definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json: ordered positive-rational branch mass and provenance are kept prior to the observer-scoped quotient; there is no signed-amplitude cancellation and no new generic BRC tool family.

No claim is made about full ordered-history observables, interventional ports, arbitrary hidden operations, asymptotic bounds, native six-dimensional X6, three-dimensional slice, P000, or Heartbeat dynamics. This work needs independent Research Driver scrutiny before project admission.

**Next question:** Can the four-scalar feasible set be preserved by a T statistic that is strictly coarser than the strong predictive partition, even when (PL) fails? Find a rational example with quantifier forall full-history policies exists T-policy, or derive an extra policy-separating condition under which strong lumpability becomes necessary. Investigate observer error bounds from the exact signed incoming defects while retaining provenance.
