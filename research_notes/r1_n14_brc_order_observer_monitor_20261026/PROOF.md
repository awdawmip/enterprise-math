# R1/N14 auxiliary IID: observer-fiber no-go and finite-monitor exact rescue

**Claim level:** author's complete finite-horizon mathematical derivation, independently unreviewed. **Scope:** strictly positive finite-alphabet IID sequential tests; external auxiliary model only, no native X6/P000 result, no native CLAIM/Result or promotion. Date: 2026-10-26.

## Frozen inputs and provenance

- Global `GLOBAL_KNOWLEDGE_V1` canonical main snapshot `468fd2fb5d79232c1fa1f8f34d1e0519e6f5bbd2`; entrypoints `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`; P000 startup projection agrees with original `P000_REALITY_FOUNDATION.json` blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`. ACTIVE worldview and the mandatory joint-observer/structural-residual constraints read.
- Enterprise Math source initial main `7ce2f8cebef341c08cbde799d67e93bb974655b6`; `AGENTS.md`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`.
- Parent author's result: `research_notes/r1_n14_brc_observer_safe_markovization_20261026/PROOF.md` (count-only Markovization of the joint terminal time/count/decision law under P,Q). This note answers its explicitly open ordered-observer extension. Other claimed Stage171 primal execution/ownership is not reused or taken over.
- Native `em_control_tasks` query returned `CONTROL_QUOTA`; native `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`. Current canonical owner/CLAIM cannot be verified; the GitHub author record is local activity metadata, not native authority.

## Theorem A — an exact terminal-observer factorization boundary

Fix finite alphabet \\(\\mathcal A\\)\\, finite horizon \\(N\\), and strictly positive IID laws \\(P,Q\\). A policy may randomize based on the entire ordered observation history and on its private coins; the coins are independent of the unknown law. It must stop by \\(N\\), deciding P or Q.

For a proposed *count-only* replacement, define \\(k(h)=(\\#_i(h))_{i\\in\\mathcal A}\\), \\(t=|h|\\), and let \\(f_t(h,d)\\in\\mathbb R\\) be an additional terminal observer.

**Universal exact boundary.** A count-only Markovization can, for **every** such full-history policy, preserve simultaneously under P and Q (i) the joint terminal law of \\(T,k(T),D\\) and (ii) the additional observer's law (equivalently every bounded function of it, together with \\(T,k(T),D\\)) **if and only if** \\(f_t(h,d)\\) is constant over all ordered histories \\(h\\) with the same count vector, for every attainable \\(t,k,d\\).

*If:* the observer factors as \\(f_t(h,d)=g(t,k(h),d)\\). The previous verified count-flow Markovization already preserves the joint law of \\(T,k,D\\), so it preserves the joint law including \\(f\\).

*Only if:* suppose, for some \\(t,k,d\\), the values \\(f_t(h,d)\\) are nonconstant among the \\(M(k)=t!/\\prod_i k_i!\\) ordered words of that fiber. Pick one word \\(h_*\\) whose value differs from their arithmetic mean. Construct a policy that always continues to exactly \\(t\\), then decides \\(d\\) only on \\(h_*\\), with the other decision everywhere else; choose horizon \\(N=t\\). Strict positivity makes every word possible. Every word in the fiber has likelihood \\(\\lambda_L(k)=\\prod_i L(i)^{k_i}\\) under \\(L=P,Q\\). If a count-only policy has the same terminal \\(T,k,D\\) law, it must never stop before \\(t\\); consequently its chance of deciding \\(d\\) at \\(k\\) is forced to \\(1/M(k)\\). Its \\(f\\)-weighted terminal mass at \\(k,d\\) is therefore
\\[
\\lambda_L(k)\\frac{1}{M(k)}\\sum_{h:k(h)=k}f_t(h,d),
\\]
whereas the original policy produces \\(\\lambda_L(k)f_t(h_*,d)\\). These differ. This proves necessity. The criterion is for **universal preservation of the full terminal joint observer**, not a claim that an individual policy can never admit a coincidental compression.

The boundary captures a positive information-loss obstruction: equal IID path likelihoods do not make ordered observer values equal.

## Theorem B — exact rescue by a deterministic finite observation monitor

Let \\(S\\) be any finite monitor-state set, initial state \\(s_0\\), and deterministic letter update \\(\\rho_t:S\\times\\mathcal A\\to S\\). Define \\(s(h)\\) recursively by \\(s(\\varnothing)=s_0\\), \\(s(hi)=\\rho_{|h|}(s(h),i)\\). The monitor may encode any chosen order-sensitive finite automaton, including past occurrence of an ordered substring.

**Claim.** For every full-history randomized finite-horizon policy, there exists a randomized policy depending only on \\(x=(t,k(h),s(h))\\) which, under **both** P and Q, exactly preserves the *entire* joint terminal distribution of
\\[
(T,k(T),s(H_T),D).
\\]
Consequently it preserves four observers \\(e_P=\\Pr_P(D=Q)\\), \\(e_Q=\\Pr_Q(D=P)\\), \\(t_P=\\mathbb E_P T\\), \\(t_Q=\\mathbb E_Q T\\), and every terminal observer factoring through \\(T,k,s,D\\). No approximation or path-uniform average is used.

*Proof.* Given an ordered word \\(h\\), let \\(u_h\\) be the pre-action survival probability conditional on the word having been observed, averaged over policy-private coins. Conditional action probabilities \\(a_h,b_h,c_h\\) denote stop P, stop Q, and continue, with \\(a_h+b_h+c_h=1\\), \\(c_h=0\\) at depth \\(N\\). Coin-law independence gives \\(u_{hi}=u_hc_h\\) regardless of whether the true law is P or Q.

For \\(x=(t,k,s)\\), sum positive *unweighted* ordered-history flows
\\[
F(x)=\\sum_{h:x(h)=x}u_h,\\quad
A(x)=\\sum_{h:x(h)=x}u_ha_h,\\quad
B(x)=\\sum_{h:x(h)=x}u_hb_h,\\quad
C(x)=\\sum_{h:x(h)=x}u_hc_h.
\\]
In particular \\(F=A+B+C\\). Define the new policy, when \\(F(x)>0\\), by the triple \\((A/F,B/F,C/F)\\); choose any valid triple at unreachable states. Its initial pre-action mass is one at \\((0,0,s_0)\\). Its unweighted survival flow obeys the exact positive-branch BRC recurrence
\\[
F_{t+1}(k',s') =
\\sum_{i\\in\\mathcal A}\\ \sum_{s:\\rho_t(s,i)=s'} C_t(k'-e_i,s),
\\]
with terms with negative count entries interpreted as zero. This recurrence holds for the original full-history flow by unique ordered-prefix extension. It also holds for the compressed policy, because its continuation flow at each reachable x is \\(F'(x) C(x)/F(x)\\). Induction on t yields \\(F'=F\\), then \\(A'=A,B'=B,C'=C\\) for all states.

Under either IID law \\(L\\), every fixed ordered word in a count fiber has probability \\(\\lambda_L(k)=\\prod_i L(i)^{k_i}\\), so for \\(d=P\\), for instance,
\\[
\\Pr_L(T=t,k(T)=k,s(H_T)=s,D=P)
=\\lambda_L(k)A_t(k,s).
\\]
An identical identity holds for d=Q with B. Thus all asserted terminal joint probabilities match simultaneously under P and Q. QED.

**Scope:** monitor updates use observed letters only, not law-specific hidden variables. The proof does not preserve internal private-coin correlations, conditional future observations after stopping, path-dependent non-IID likelihoods, or native X6 dynamics without additional bridges.

## Exact N=2 no-go with all four basic observers preserved

Use \\(\\mathcal A=\\{0,1,2\\}\\), \\(P=(1/8,1/24,5/6)\\), \\(Q=(1/12,1/12,5/6)\\), \\(N=2\\). Observe exactly twice; declare P **only** if the ordered word is 01; declare Q otherwise. Then
\\[
\\Pr_P(D=P)=1/192,\\qquad \\Pr_Q(D=P)=1/144,
\\]
\\[
e_P=191/192,\\quad e_Q=1/144,\\quad t_P=t_Q=2.
\\]
The count policy that decides P with probability 1/2 at \\(k=(1,1,0)\\), and Q elsewhere, matches all four exactly: the words 01 and 10 have equal likelihood under each IID law.

Now add the fifth ordered observer \\(R_L=\\Pr_L(H_2=01,D=P)\\). The original has \\(R_P=1/192, R_Q=1/144\\), but that count policy has \\(R_P'=1/384,R_Q'=1/288\\).

This is not merely failure of one natural averaging algorithm. Suppose *any* count-only policy preserves all four original quantities and \\(R_P\\). Since \\(T\\leq2\\) but \\(\\mathbb E_PT=2\\), it must continue with probability one before depth 2 on every positive-probability prefix. Matching \\(R_P=P(01)=1/192\\) forces the common count-state action at \\(k=(1,1,0)\\) to decide P with probability one. Thus it must also decide P on word 10, yielding \\(\\Pr_P(D=P)\\ge2/192>1/192\\), contradiction. The fifth observer is genuinely incompatible with count-only preservation of the original four.

A 3-state DFA with \\(s=0\\) (no pending 0), \\(s=1\\) (last symbol 0), \\(s=2\\) (substring 01 already seen) and update \\(s=2\\to2\\), \\(s=1,i=1\\to2\\), otherwise \\(i=0\\to1\\), other transitions to 0, resolves this obstruction by Theorem B.

## Reproducible exact evidence

`VERIFY.py` performs ordered-prefix positive rational recursion with `fractions.Fraction`, independently constructs count-plus-DFA action flows, and checks the exact equality of all augmented terminal flow coefficients. It also independently compresses to counts to check the basic two-law observers, and explicitly checks the N=2 witness. `RESULT.json` stores full exact fractions for N=3,4,5, respectively 28/55/96 reached augmented states versus 20/35/56 count states. These tests are finite demonstrations; the universal statement is the preceding written induction proof. Test status: author exact computation PASS, independent Driver review and Lean formalization PENDING.

Prior-art context (not a claim of discovery of occupancy-measure Markovization): Romain Laroche and Remi Tachet des Combes, *On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs*, ICML/PMLR 202 (2023), https://proceedings.mlr.press/v202/laroche23a.html. Their general occupancy-equivalence topic is related, but it is **not cited as a proof** of this specific IID order-monitor certificate.

## BRC / Enterprise Math observer scope

The carrier is the positive weighted ordered-prefix population; alternate branches are summed only after retaining sufficient \\(k,s\\) provenance and action-flow labels. This is an **observer-scoped quotient**: it deliberately erases order distinctions beyond the selected monitor and makes no claim about full structural residual equality. `REUSE_APPLIED` from the previous R1 BRC markovization. The P000 native X6 world remains a separate conditional research substrate, not a conclusion of this external IID theorem.

## Next discriminating problem

Find a minimal observer monitor for a *declared finite family of terminal ordered readouts* while maintaining exact (P,Q) action-flow preservation. Develop a partition-refinement/automaton right-congruence certificate accounting for the future letter updates, and test whether the coarsest monitor is observer-sufficient (the naive partition by current readouts generally is not). Then characterize exactly which hypotheses of equal within-fiber likelihood and update closure fail in path-dependent/non-IID models. Keep the Stage171 primal ownership separate; secure independent Research Driver review before any project-theorem promotion.
