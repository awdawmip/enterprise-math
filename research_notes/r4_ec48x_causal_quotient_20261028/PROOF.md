# EC48X — Causal likelihood-fiber simulation; a non-necessary predictive-kernel criterion

**2026-10-28. Author-side TASK_RESEARCH, UNREVIEWED / NOT_ADMITTED.** Direct continuation of EC48W, PR #1605, immutable commit 6d395c8d1460942ef155ae7b3e0019da02e2543c. This is a finite positive-rational two-source weighted-branch stopping experiment, not signed/amplitude BRC, native BRC–Shor, an X6 heartbeat dynamics theorem, a native CLAIM, or accepted Foundation material.

## Definitions

For finite decision epochs t=1,...,d, let H_t be the *live full controlled observable histories* and let two strictly positive underlying source kernels be P and Q. A full observer can condition source-neutral behavioral actions on all observations and previous actions. A compressed observer can condition on a register r in a set of size at most m, current sensor o, exact **fine-history** joint likelihood ratio L_t(h), and t. Its update is a causal source-neutral operation on previous register/action and newly observed sensor/full-LR data; no hidden seed or inaccessible fine history is an allowed extra memory channel. Stop/reject, stop/accept and continue are available. Define the raw set S of (alpha,beta,E_P T,E_Q T), where alpha=P(accept) and beta=Q(accept). Raw set equality is stronger than equality of support functions in general.

## Theorem X1 — A sufficient criterion for exact raw-region preservation

Assume at each live history h there is a quotient y=q_t(h)=(r_t(h),o_t(h),L_t(h)), with r_t in {1,...,m}. Require:

1. **Causality:** initial r is computed from permitted initial observation. Subsequent r_{t+1}=u_t(r_t,a_t,o_{t+1},L_{t+1}) is implementable by one common source-independent register updater.
2. **Action-indexed dual-source lumpability:** For each source s in {P,Q}, each continuing action a, all h,k with q_t(h)=q_t(k)=y, and each next quotient state y', the pushforward probabilities agree: sum over descendants h' with q_{t+1}(h')=y' of K_s(h'|h,a) equals the corresponding sum for k. Call the common value Kbar_s(y'|y,a). The next readout includes the **full fine-history LR**, not merely the compressed posterior LR. Extend to all other nonterminal actions if present.
3. **Observer factorization:** accept/reject/stop rewards and stopping epoch depend only on the quotient state, current action and time. In particular, no untracked joint-relation/future-operation observable is silently discarded.

Then **S_m = S_full**, including original nonconvex regions under the specified behavioral randomization class.

**Proof.** Fix any full history-dependent source-neutral policy pi. Let mu_s^pi(h) be its live fine-history mass. Policy factors are identical under P and Q, so wherever nonzero they cancel in the likelihood ratio: mu_P^pi(h)=L_t(h) mu_Q^pi(h). On every quotient fiber, L_t is constant. Therefore the conditional fine-history distribution given y is the same under P and Q, even if the unconditional fiber masses differ. Define a *single* source-neutral quotient policy

pi'_t(a|y) = [sum_{h:q_t(h)=y} mu_Q^pi(h) pi_t(a|h)] / mu_Q^pi(y),

arbitrary on unreachable fibers. The same expression with P in place of Q is equal because the fiber LR is fixed. At the first decision both policies have the same pushed-forward live y masses. Inductively, equal live (y,source) masses and the common action distribution imply equal (y,a,source) masses. Every stop/accept outcome matches by factorization; every continuation next-y mass matches by the declared action-indexed Kbar_s independently of the erased micro-history. Thus, at every time, acceptance increments and survival masses match under **both** sources. Summing survival masses computes E_s T exactly. By the causal update, pi' is implementable with at most m registers; hence S_full is contained in S_m. The reverse inclusion holds because the full observer can emulate any compressed policy. QED.

This is a *sufficient*, scope-typed controlled-lumping criterion; its proof needs the **common source-neutral conditional action disintegration**. Two independently chosen P/Q simulators would not establish the result. A latent-state relabeling lacking causal update is also insufficient. We claim no general novelty over classical Markov/POMDP sufficient-statistic results.

## Theorem X2 — Dual-source predictive-kernel lumpability is not necessary

At a preliminary readout t=0, H∈{0,1} is observed with P(H=h)=Q(H=h)=1/2. There is **no action at t=0**. Before the t=1 stop/accept/reject/continue decision, the one-register observer has forgotten H and sees a constant sensor and full LR=1, while the full observer remembers H. If continuing, at t=2 observe W,Z and full LR, then choose accept/reject.

The exact joint terminal mass is rho(h) K_h(w) nu_s(z), where rho(0)=rho(1)=1/2, K_0(W=1)=3/4, K_1(W=1)=1/4, nu_P(Z=1)=3/4, nu_Q(Z=1)=1/4. W is source-neutral conditional on H, and Z is independent of H,W for each source. All eight P/Q leaves are strictly positive. Full LR at t=2 is 3 when Z=1 and 1/3 when Z=0. The action-indexed observable W kernel **fails lumpability** on the erased H fiber: 3/4 ≠ 1/4, although the terminal Z remains genuinely source-informative.

Nevertheless, for this declared four-observer language, **S_1=S_full**, with the exact parameterization

S = { (A+N_0/4+3N_1/4, A+3N_0/4+N_1/4, 1+C, 1+C):
       A≥0, C≥0, A+C≤1, 0≤N_0≤C, 0≤N_1≤C }.

**Proof.** Given arbitrary full behavioral policy, write a_h for the probability of stop/accept and c_h for the probability of continue after H=h. Let d_{h,w,z}∈[0,1] be its t=2 conditional accept probability. Define A=(a_0+a_1)/2, C=(c_0+c_1)/2 and N_z=sum_{h,w}(c_h/2) K_h(w)d_{h,w,z}. Source-neutrality and Z independence give alpha=A+nu_P(0)N_0+nu_P(1)N_1; beta=A+nu_Q(0)N_0+nu_Q(1)N_1; and E_P T=E_Q T=1+C. Since 0≤N_z≤C, a single-register policy can stop/accept with probability A, stop/reject with 1-A-C, continue with C, then accept at t=2 given Z=z with probability N_z/C (arbitrary if C=0). This reproduces the **four coordinates exactly** under both sources. Conversely each tuple satisfying the inequalities can be achieved by this same one-register policy, which the full observer can emulate. QED. In particular |alpha-beta|≤C/2 at expected time 1+C.

### The erased history still matters for an expanded observer

Fine policy: continue at t=1 iff H=0, and at t=2 accept iff W=1 (ignore Z). It produces (alpha,beta,E_PT,E_QT)=(3/8,3/8,3/2,3/2). Add a fifth coordinate R_s=E_s[1_{T=2,W=1,accept}]. Fine gives R_P=R_Q=3/8. Any one-register policy with E_s T=3/2 must continue with probability C=1/2 independently of H; hence its total continuing W=1 mass is at most C*P(W=1)=1/4. It has R_s≤1/4; exact gap **1/8** for this extended observable. The four-coordinate raw equivalence does NOT preserve this future joint relation.

Without the full LR readout, an even smaller informative-source boundary is P(H=1)=3/4, Q(H=1)=1/4 with an initially seen but forgotten H: fine policy accept iff H=1 attains (3/4,1/4), but one register with no other sensor can only attain (r,r). With the oracle full LR, H becomes distinguishable and this boundary example no longer applies.

## Validation, scope and next dependency

VERIFY.py uses Python Fraction (exact rational branch masses); it tests all 3^2*2^8=**2304** full deterministic controllers for X2, checks the exact simulator under P and Q for all four coordinates, and separately checks 512 seeded rational randomized fine policies. Its output EXACT_REPORT.json records eight strictly positive P/Q leaves, 115 distinct deterministic raw vectors, source normalization, LR fibers, the nonlumpable W kernels, and the 1/8 fifth-coordinate obstruction. The all-behavioral result and X1 are analytical proofs rather than consequences of these finite tests.

The operation is **auxiliary positive-weighted BRC branch arithmetic only**: no native 6D X6 heartbeats, signed phase/amplitude cancellation, BRC–Shor evolution or physics residual was computed. Native transfer requires typed X6 carrier and relation/observer/future-operation bridge with actual lawful BRC kernel. P000 and ACTIVE worldview remain intact. No formal mathematical review/admission has been performed.

Owner inventory returned CONTROL_QUOTA, service research_authority_granted=false: no native own session, RA, CLAIM, Result or Driver review is asserted. This research-note GitHub handoff is not a retry of an earlier separately platform-denied Research-Activity write.

**Next: EC48Y** — find an observer-relative necessary/sufficient dual-source causal *policy-lifting* certificate weaker than action-indexed kernel equality, distinguishing fixed-policy feasibility from full raw-region equality and preserving finite-register realization. See NEXT_TASK.md and SOURCES.md.
