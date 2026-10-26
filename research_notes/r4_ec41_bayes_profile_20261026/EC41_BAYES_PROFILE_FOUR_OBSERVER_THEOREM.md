# R4-EC41 — Exact horizon-two BRC four-observer compression through Bayes-gain profiles

**Status:** Author mathematical proof + exact finite cross-check, **not** a native Task CLAIM, frozen Result, Driver review, Working Truth, Foundation result or Heartbeat/X6 theorem.

## Fixed source pins and research question

- GLOBAL_KNOWLEDGE_V1 **main@11c141acc178d3b6cd5f478ee97751535d61108e**; 00_BOOTSTRAP, OPERATING_MANUAL, P000_STARTUP and original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview.
- Enterprise Math reading snapshot **main@cd3472e6448ae4b62e6b64b9b3bbedc38f7c3cc9**, including docs/PORTABLE_RESEARCH_PROTOCOL.md, research_delivery_policy and positive-weight BRC constraints. Direct mathematical parent: EC40 immutable proof [R4-EC40](https://github.com/awdawmip/enterprise-math/blob/6ee9ae31c3b58eee5d38d7f6dfd88af3087fb3a9/research_notes/r4_ec40_noniid_brc_markovization_20261026/EC40_NONIID_BRC_MARKOVIZATION.md).
- This is independent author-side work; authenticated GitHub login awdawmip has write permission. The native task/owner list reported CONTROL_QUOTA. No active formal Owner, CLAIM or native research session was verified.
- Specific EC40 open question: characterize when reducing the observed history preserves **all four** two-measure stop/decision observables even when history-to-next-statistic lumpability fails.

## Exact typed BRC model and observer

There is a compulsory first positive-branch observation h in a finite set H. Both strictly positive hypotheses have *the same* initial ordered-source mass w_h=P(h)=Q(h)>0, sum_h w_h=1. At stage 1, the common behavioral policy observing h chooses: stop and decide P; stop and decide Q; or continue. When continuing, a finite terminal label z is sampled from strictly positive conditional laws p_h(z)=P(z|h) and q_h(z)=Q(z|h); each sums to 1. Terminal observation exposes the **entire ordered (h,z) provenance** and the policy decides P or Q. The coarse stage-one statistic T:H→X may erase h; no coarse terminal ambiguity is assumed. Time is decision depth 1 or 2, not physical heartbeat time.

An unrestricted history policy uses h at stage 1. A T-policy uses only x=T(h) at stage 1; both may use full (h,z) at stage 2. Policies may randomize. Let e_P=P(decide Q), e_Q=Q(decide P), and t_P,t_Q the mean decision depth. Define C=P(continue)=Q(continue); then t_P=t_Q=1+C. We compare **the entire attainable sets** of (e_P,e_Q,t_P,t_Q), not merely minimum total Bayes error.

All branches carry explicit nonnegative P- and Q-counts and retain ordered source identity; this is a two-measure positive labelled BRC observer, **not** complex/signed amplitude or native physical dynamics.

## Theorem EC41.1 (necessary and sufficient four-observer criterion)

For α,β≥0 define the conditional *Bayes gain*

\[
g_h(\alpha,\beta)=\min(\alpha,\beta)
  -\sum_z\min\{\alpha p_h(z),\beta q_h(z)\}\ge0.
\]

The unrestricted-history and T-statistic policies have **identical complete attainable four-observer regions** if and only if

\[
\boxed{\forall x\in X,\ \forall h,k\in T^{-1}(x),\
  \forall r\ge0:\ g_h(1,r)=g_k(1,r).}
\tag{EC41.1}
\]

In particular, the partition of H by the *entire* function r↦g_h(1,r) is the unique coarsest **deterministic stage-one partition** preserving the complete four-observer region. This is a two-stage result with first-layer likelihood ratio 1 and a fully revealing terminal readout. It does not assert a general finite-horizon or general-hidden-state characterization.

### Proof

Fix arbitrary real α,β,θ. Minimize the linear functional
\[
L=\alpha e_P+\beta e_Q+\theta C.
\]
Stopping at a first-stage h has minimum local weighted error b=min(α,β). Continuing incurs θ and the optimal terminal weighted error
\(R_h=\sum_z\min(\alpha p_h(z),\beta q_h(z))\), because a terminal decision is independently available for each (h,z). Set g_h=b-R_h, and \(u_+=\max(u,0)\). Optimizing each h separately gives the exact unrestricted support minimum
\[
\boxed{V_{\rm full}(\alpha,\beta,\theta)
=b-\sum_h w_h\bigl(g_h(\alpha,\beta)-\theta\bigr)_+.}
\tag{EC41.2}
\]
A T-policy must select a common first-stage continuation probability inside each fiber x. Terminal decisions still depend on (h,z). Put \(w_x=\sum_{T(h)=x}w_h\) and \(\bar g_x=w_x^{-1}\sum_{T(h)=x}w_h g_h\). Optimizing each fiber gives
\[
\boxed{V_T(\alpha,\beta,\theta)
=b-\sum_x w_x\bigl(\bar g_x(\alpha,\beta)-\theta\bigr)_+.}
\tag{EC41.3}
\]
Consequently
\[
\boxed{V_T-V_{\rm full}
=\sum_x\left[\sum_{h:T(h)=x}w_h(g_h-\theta)_+
  -w_x(\bar g_x-\theta)_+\right]\ge0.}
\tag{EC41.4}
\]
Each term is nonnegative by convexity of the positive-part function. This is an **exact** support-function loss, not merely an upper bound.

Both attainable regions are compact convex polytopes. For clarity, encode a T-policy using first-stage nonnegative probabilities \(s_{x,P},s_{x,Q},c_x\) summing to 1, and terminal decision-flow variables \(v_{hz}=c_{T(h)}d_{hz}\), where \(0\le v_{hz}\le c_{T(h)}\). Error probabilities and C are affine in these variables. Conversely, any such feasible flows realize a behavioral T-policy (divide v by c when c>0). The full-history class has the same representation with h-dependent first-stage variables. Thus equality of all real linear support minima is equivalent to equality of the attainable regions.

If gains are constant inside each x for every real α,β, equation EC41.4 vanishes for every θ, giving equality of polytopes. Conversely, if g_h≠g_k in one positive-weight fiber for some α,β, select θ strictly between two distinct values. Strict Jensen inequality for positive part in that fiber yields \(V_T>V_{\rm full}\); hence the polytopes differ.

It remains to reduce all real α,β to the stated one-parameter nonnegative profile. For α,β≥0 and α>0, positive homogeneity yields \(g_h(\alpha,\beta)=\alpha g_h(1,\beta/\alpha)\); if α=0 or β=0 the gain is 0. For mixed signs the same deterministic decision is optimal both before and after continuing, so g_h=0. For α,β≤0, elementary identities \(\max(u,v)=u+v-\min(u,v)\) and \(\sum_zp_h(z)=\sum_zq_h(z)=1\) show \(g_h(\alpha,\beta)=g_h(-\alpha,-\beta)\). Therefore profile constancy for r≥0 implies constancy for every real normal, proving the forward implication. Strict failure at a positive-normal r yields a separating functional, proving necessity. QED.

**Scope of coarseness:** Unique coarsest partition among deterministic summaries of h with terminal full-path readout; no assertion about arbitrary stochastic encodings, strong future source-label equivalence, or native X6 transformations.

## Corollary EC41.2 (finite exact rational certificate)

Suppose all conditional p_h(z),q_h(z) are positive rationals. Form the **finite rational breakpoint set**
\[
\mathcal B=\{0,1\}\cup
  \{p_h(z)/q_h(z):h\in H,\ z\}.
\]
Every function \(r\mapsto g_h(1,r)\) is continuous piecewise-linear with possible breakpoints only in \(\mathcal B\), and vanishes for r above the largest breakpoint. It follows that EC41.1 is equivalent to comparing the rational values \(g_h(1,r)\) for **only the finitely many r∈\mathcal B** inside each T-fiber. This is an exact finite criterion for an arbitrary finite rational input, not an enumeration-based proof of the general theorem.

A simple **certificate for failure** is a pair h,k in one T-fiber, a rational r∈\mathcal B with gains different, and \(\theta=(g_h(1,r)+g_k(1,r))/2\) for the two-history equal-weight case. Its exact four-region support gap is \(|g_h(1,r)-g_k(1,r)|/4\). For more histories choose any θ strictly between discrepant gains; EC41.4 supplies the gap.

## Exact witnesses and relation to EC40

**Recover EC40 counterexample.** Give a,b equal first-hypothesis masses 1/2. Let a have conditional binary P=(3/4,1/4), Q=(1/4,3/4); let b have P=Q=(1/2,1/2). Merge a,b at stage 1 and reveal the terminal ordered pair. With α=β=1, gains are g_a=1/2, g_b=0. At θ=1/4, support gap is 1/8. Fixing C=1/2, the full-policy minimum e_P+e_Q is 3/4, but the T-policy minimum is 7/8, exactly the EC40 witness.

**Nonlumpable yet four-observer-safe.** Give a,b identical initial masses, with a using P=(3/4,1/4),Q=(1/4,3/4), and b using P=(1/4,3/4),Q=(3/4,1/4). The two conditional experiments are related by a *terminal-label permutation*. Their gains match for every ratio r, so merging a and b preserves all four-observer attainable vectors even though the full-terminal-history next-statistic distributions are different at a and b. This exhibits a concrete relaxation of EC40's P-LUMP sufficient condition.

**Equal conditional TV is still insufficient.** For a let P=(15/20,5/20), Q=(5/20,15/20); for b let P=(12/20,8/20), Q=(2/20,18/20). Both conditional total-variation distances are exactly 1/2, so g_a(1,1)=g_b(1,1). But for α=1,β=2, \(g_a=5/20\), \(g_b=8/20\). Taking θ=13/40 gives exact support gap \(3/80>0\). Therefore matching the symmetric Bayes-risk curve alone does **not** guarantee the complete two-error/four-observer region.

## Actual computation, reuse and limits

The accompanying EC41_verify.js explicitly enumerates all positive binary P/Q branch-count pairs with denominator 4: 9 conditional experiments and 81 ordered two-history pairs. For each pair it checks the complete finite breakpoint signature and **independently enumerates all 144 deterministic full-history decisions and 48 deterministic T-decisions** for each breakpoint. Exact integer costs (scaled by 4M) agree with the Jensen support-gap formula. The JSON report stores counts, three witness inputs and exact rational gaps. This finite computation checks the implementation and example constants; the theorem and finite breakpoint test are proved algebraically above.

**BRC reuse:** REUSE_APPLIED to EC40's positive two-measure branch/stop-decision occupation model, to definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json for provenance/multiplicity, and to the EC40 policy-evaluation formulas. Here the new mathematical object is the *whole Bayes-gain function* as a minimal sufficient observable for this narrowly declared four-scalar decision problem, not a universal replacement for source history.

**Next exact question (EC42 candidate):** For N≥3 and arbitrary non-iid positive histories, characterize which history statistics preserve the **complete** two-measure error-and-stopping-time region. Does a family of history-indexed Bayes continuation value profiles suffice, or must joint occupation-flow coupling/history information be retained? Construct the smallest depth-three counterexample to naive one-stage profile iteration. Keep native X6/three-dimensional-slice/third-coordinate/time bridge pending until the project supplies an actual fixed heartbeat update (P000 fixed_heartbeat_program=null).

**Verification classes:** authored proof; finite exact code execution PASS; remote source readback to be recorded separately; formal native Guard, independent Driver review, canonical mathematical admission **not performed**.
