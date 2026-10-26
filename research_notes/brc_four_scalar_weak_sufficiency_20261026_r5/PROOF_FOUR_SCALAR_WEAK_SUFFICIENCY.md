# Exact four-observer compression without strong P-lumpability

Date: 2026-10-26. Classification: author-level mathematical theorem and counterexample in an external finite positive-rational non-iid tree, not a native P000/X6/Heartbeat theorem or a formal Research Driver accepted Result.

Frozen account snapshot: GLOBAL_KNOWLEDGE_V1 main@f92f32e5d65551909fb6826bbbc875ec84deb781 (bootstrap, operating manual, P000 projection and ACTIVE worldview); the projection's original P000 blob is 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Project input snapshot: enterprise-math main@d6d0d2c623691df7c323f6609339bcf5dc8d3cbe (docs/PORTABLE_RESEARCH_PROTOCOL.md, research_notes/brc_noniid_predictive_quotient_20261026/PROOF_BRC_NONIID_PREDICTIVE_QUOTIENT.md, and NEXT_TASK_PACKET.md). User explicitly requests a latest-frontier anchored continuation: this is not blind FREE discovery.

Actual GitHub actor: awdawmip, with repository push permission. Native control tasks returned CONTROL_QUOTA; native session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Current native owner, session, CLAIM, Result, and review remain unverified. This is a separate author-source note and does not adopt another owner's task.

## Question and exact quantifiers

Given a finite horizon N=2, two strictly positive measures P and Q on the same ordered history tree, and a time-dependent statistic T, when can the feasible four-observer set under all complete-history stopping policies be preserved by T-adapted randomized policies without strong P-lumpability?

The four observers for a common history-dependent behavioral policy pi are
O(pi)=(P_pi[decide Q], Q_pi[decide P], E_P^pi tau, E_Q^pi tau).
Stopping and decisions can occur at the root (time zero) or at depth one. At time two, only P or Q decisions are permitted. Policy randomization is the same under both hypotheses.

The target quantifiers are FOR ALL full-history randomized pi, THERE EXISTS a time-and-T-only randomized beta with O(beta)=O(pi). Fine-state incoming occupancy, future interventions on hidden histories and path distributions are not asserted preserved.

## Strictly positive rational non-iid tree

At depth one the observations are a,b with P(a)=P(b)=Q(a)=Q(b)=1/2. At depth two observe (e,z), e in {+,-}, z in {0,1}, with the following conditional rows:

| first history | law | (+,0) | (+,1) | (-,0) | (-,1) |
|---|---|---:|---:|---:|---:|
| a | P | 3/8 | 1/8 | 3/8 | 1/8 |
| b | P | 1/8 | 3/8 | 1/8 | 3/8 |
| a | Q | 9/16 | 3/16 | 3/16 | 1/16 |
| b | Q | 3/16 | 9/16 | 1/16 | 3/16 |

Every entry is strictly positive; every row sums to one. P differs from Q: P(e=+)=1/2 whereas Q(e=+)=3/4. The nuisance observation z at time two has a conditional distribution depending on the hidden a/b prefix, so the tree is non-iid.

Define T_0=root, T_1(a)=T_1(b)=x, and T_2(h,e,z)=(e,z), h in {a,b}. Prefix likelihood ratios lambda=Q(h)/P(h) are 1 at times 0 and 1; at time 2 lambda(+ ,z)=3/2 and lambda(- ,z)=1/2. Thus likelihood ratio is T-measurable at all levels.

Yet strong P-lumpability of T FAILS: P[T_2=(+,0)|a]=3/8 and P[T_2=(+,0)|b]=1/8, an exact positive difference of 1/4. The coarsest LR-compatible *strong* refinement of T must split the two depth-one histories.

## Proposition (observer-factor criterion)

On any finite positive two-measure history tree, suppose there is a time-indexed coarsening S_n=g_n(T_n) that has (i) LR constancy on all S fibers and (ii) strong P-lumpability of the S successor transitions. Then every randomized full-history stopping/decision policy pi admits an S-only randomized policy beta preserving all four observers. In particular beta is also T-only, whether or not T itself is strongly P-lumpable.

Proof: Write mu_pi(h)=P(h)*s_pi(h) for pre-action live P mass. For each n, S class s and action d, let u(n,s,d)=sum_{S_n(h)=s} mu_pi(h) pi_d(h), and m(n,s)=sum_d u(n,s,d). On positive-mass classes take beta_d(n,s)=u(n,s,d)/m(n,s); define arbitrary legal actions on unreachable classes. By strong P-lumpability, induction from root shows equality of per-class P live/action masses between pi and beta. LR constancy then gives equality of the Q masses, multiplying by the single class LR. The four observers are the sums of P D_Q action mass, Q D_P action mass, P continuation mass at n<N, and Q continuation mass at n<N. They therefore agree exactly. Since S_n=g_n(T_n), the constructed beta uses no information beyond T. QED.

Apply this to the displayed tree with S_0=root, S_1=x and S_2(h,e,z)=e. The P successor distribution of e after either a or b is (1/2,1/2), while Q has (3/4,1/4), so LR constancy and strong P-lumpability hold for S. Therefore the universal four-observer claim holds even though T fails strong P-lumpability.

For direct verification, retain pi's root action probabilities. Conditional on root continuation, replace its depth-one actions by the arithmetic average of the a and b action vectors. Let c be the resulting depth-one continuation probability and r the root continuation probability. The full policy's P live mass in terminal class e equals r*c/2 and its Q live mass equals r*c times 3/4 for + and r*c times 1/4 for -. Let theta_e be the P-live-weighted full-policy probability of deciding Q at e (arbitrary if unreachable); use theta_e as the terminal Q-decision probability, independent of z. The common LR within e ensures that the Q terminal decision masses agree as well. Early decision masses and time costs agree, with t_P=t_Q=r*(1+c). This directly handles all randomized policies, including root stopping.

## Sharp distinction: four scalars match even with nonzero fine-T incoming defect

Take this deterministic full-history policy: root continue; after a continue; after b immediately decide P; at time two decide Q if e=+ and P if e=-. The exact observer tuple is
O(pi)=(1/4,5/8,3/2,3/2).

The canonical P-live averaged T-policy at depth one stops and decides P with probability 1/2 and continues with probability 1/2; at the terminal classes it decides using e alone. Its four observers are identical. However the original P live mass minus this T-policy's P live mass at the four fine terminal classes is

D(+,0)=+1/16, D(+,1)=-1/16,
D(-,0)=+1/16, D(-,1)=-1/16.

D is an exact signed DIFFERENCE OF TWO POSITIVE MASS FLOWS, not a signed BRC amplitude. The defects cancel only after summing over z within each e. The corresponding Q flow differences are lambda(e)*D(e,z) and also cancel within e. Thus preservation of four observers does not require vanishing of every fine-T incoming defect. The prior policy-specific zero-defect test is sufficient for stronger occupancy equivalence but not necessary for this scalar objective.

The model has nontrivial discrimination: sampling to time two and deciding Q for + / P for - yields (1/2,1/4,2,2), with error sum 3/4 instead of the uninformed value 1.

## Evidence, reuse and boundary

VERIFY_PORTABLE.py was executed with exact fractions and covers positive row normalization, LR constancy, nonlumpability of T, lumpability of S, the deterministic nonzero-defect witness and ALL 6912 deterministic full-history decision assignments (3 root options * 3^2 depth-one choices * 2^8 terminal decisions). Its output reports 117 distinct observer tuples, each reproduced by the constructed S-policy. An exhaustive deterministic experiment alone does NOT establish the quantifier over randomized policies; the algebraic proposition and direct construction above do.

BRC method: labeled ordered positive-rational branch masses and P/Q likelihood transport before the observer quotient. Reuse status REUSE_APPLIED: definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json and the predecessor two-measure non-iid Markovization theorem (same model scope). No new general-purpose BRC tool family is claimed. We preserve the distinction between LR observer sufficiency and future hidden-history/port semantics.

Review/admission: AUTHOR_PROVED and local exact checks; DRIVER_UNREVIEWED, NATIVE_CLAIM_UNVERIFIED, FOUNDATION_NOT_PROMOTED. The theorem has no declared map to native P000, X6, three-dimensional slice or Heartbeat dynamics. No evidence of novelty relative to world literature is claimed.

## Smallest remaining mathematical question

Impose that terminal T classes are LR-minimal (no redundant T-label split within an LR level), and ask whether universal preservation of all four scalar observers implies strong P-lumpability under an explicit policy-separation / nondegeneracy condition, or provide a second positive-rational counterexample. An alternative is a complete characterization of the feasible action-weighted nullspace of signed incoming occupancy defects. Keep exact policy quantifiers and root stopping.