# R749SL — Exact eight-lift Bayesian filter for public-history/state-local policies; one-bit hidden-provenance obstruction

Date 2026-11-13 (Asia/Shanghai). Original scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Mathematical predecessor R749SF/SI/SJ, including R749SJ @a1b658b031824e1e784949dd77f8c921c45536cc. Research-lane Activity RA-C90B76621B9191DE224257C3, Researcher EM-DIRECT-F5DC4E; no shared task CLAIM. This is an author-side result for an explicitly augmented controlled-observer kernel, not permission for a native Cell/Link/Port event.

## Statement and scope

Let the current unsigned directed support e_t be publicly observed and let X_t range over the eight legal sign lifts of e_t. Conditional on a positive-probability legal next unsigned support c, R749SF supplies the exact signed transition T_{t,c}(x,y) (forced BSC with theta=8p/(1+7p), or nonforced independent new sign). Parameter p is known. At time t the controller's policy is public as a function pi_t(c|x,h_t) of the current signed state x and the **public observation history** h_t; pi_t is nonnegative and sums to one across allowed next-support choices. This permits hidden-sign-dependent support selection, but no separate controller memory hidden from h_t and X_t. An observed later emission z has likelihood ell_t(z|y,c,h_t), again nonnegative. Every conditioning denominator below is assumed positive.

## Theorem 1 — complete recursive eight-state posterior under state-local adaptive selection

Write b_t(x)=Pr(X_t=x | h_t). After observing support choice c and emission z, the exact posterior is

b_{t+1}(y) = [
 ell_t(z|y,c,h_t) * sum_x b_t(x) pi_t(c|x,h_t) T_{t,c}(x,y)
] / [
 sum_{y',x} ell_t(z|y',c,h_t) b_t(x) pi_t(c|x,h_t) T_{t,c}(x,y')
].

The same denominator is the conditional probability of the newly observed (c,z). Thus seven independent masses suffice for *all future current-sign queries and observation predictions* under this declared policy class, given the public history, the known policy and p. In particular, allowing past publicly observed signed emissions into the policy does not by itself enlarge hidden state dimension: they can be included in h_t.

**Proof:** Conditional on X_t=x and public history h_t, the policy draws c, the signed transition draws y with T_{t,c}, and the emission draws z with ell. Their joint conditional weight is pi*T*ell. Sum over the current posterior, then divide by total observed weight. The resulting distribution on the next eight signs is sufficient to apply the same factorization inductively at every subsequent public history. The argument holds for arbitrary time horizon and arbitrary legal history-adapted state-local nonnegative kernels, including singular/zero likelihood choices wherever the observed denominator stays positive. It does not assert that all eight degrees of freedom are necessary for a restricted query family; R749SK provides the exact query-specific rank when a fixed family of posterior ratios is declared.

## Theorem 2 — loss of sufficiency from genuinely hidden historical controller memory

Let A={0,1}, B={1,2}, C={2,3} be a legal nonforced support continuation at p=1/2. Start with z=X_0(0) fixed at either +1 or -1, and take X_0(1),X_0(2) independent fair ±1. The old-only signed axis 0 is discarded at the update; the new axis 3 is independent fair. Both histories produce the **same uniform eight-lift current distribution** on signed axes {1,2,3} for edge (B,C):

Pr(X_1=x | z=+1) = Pr(X_1=x | z=-1) = 1/8 for every x in the eight-state support.

Now suppose the controller privately remembers the *discarded historical sign* Z=z, which is not measurable from public history and is not a function of current X_1, and chooses the next forced unsigned C1 completion C_f=B triangle C={1,3} with probability

Pr(C_f|Z=z)=(2+z)/4.

The complementary choice is the fixed legal nonforced C_n={3,4}. Hence the probability of publicly observing C_f is exactly 3/4 when z=+1 and 1/4 when z=-1. Two histories with identical current eight-state beliefs have different next public observations. Therefore no filter storing only b_1(x) can be predictive for this **history-memory-dependent** controller family. Retaining the one hidden sign Z along with the eight-state belief exactly repairs this two-prior example; one binary distinction is necessary because the next observed likelihoods differ and sufficient because the controller consults no other private history. This is a scope-sharp obstruction, not an impossibility theorem for all adaptive policies.

**Proof:** The nonforced transition copies axes 1 and 2 and draws axis 3 fair, yielding a uniform three-sign distribution for either fixed old z. The later controller's action likelihood depends only on Z, and both C_f and C_n are legal supports at the new edge. Its Bernoulli probabilities are (2+z)/4. The additional retained-bit repair makes all controller and transition probabilities conditionally computable. The exact failure is loss of a provenance variable that later affects a declared future operation, consistent with the global JOINT_RELATION_OBSERVER_PRESERVATION constraint.

## Exact verification

R749SL_ADAPTIVE_HIDDEN_MEMORY_CHECK.py uses standard-library Fraction arithmetic. It checks the two exact initial priors, all eight current signed lifts, a legal first nonforced transition at p=1/2, identical current sign distributions, a signed-state-local controller and post-transition emission producing identical future law, and distinct hidden-memory forced-choice probabilities of 1/4 versus 3/4. Actual checker status PASS. Algebraic Theorem 1 is all-horizon by conditional probability induction; these finite checks validate the concrete boundary witness.

## Next discriminating science

Classify the minimal hidden-controller memory for a declared finite set of future public observation laws by a predictive-equivalence quotient of histories and exact rank/fiber certificates; compare the minimal current-state Walsh carrier of R749SK with such memory coordinates. Separately, native V29/V39 three-force Cell/Link/Port event permission requires actual event guard, closure evidence and source provenance; this abstract controller model alone does not grant it.
