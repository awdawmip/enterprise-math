# R5 finite positive BRC: LR-key lumpability implies exact behavioral image equality

Date: 2026-11-05 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Scientific scope and frozen frontier

Continue the author-side R5 lawful two-gate model in \`research_notes/brc_r5_two_gate_roc_jensen_collision_20261105_t0040/RESEARCH.md\` at immutable EM commit \`aba424a063ec4bbaca016d26272e483baa4445ea\`. The prior model has a strict support gap 1/32 - 3 lambda/8 on [1/24,1/12). This unit identifies a complementary **exact equality mechanism**, rather than retrying that separation calculation.

Frozen scientific-source pins (unchanged): GLOBAL \`a01383f825ef9d43b4b754254303298c64041568\`; Enterprise Math \`86149263e38c22292c9def1e0f69092efa1be77e\`. Current behavioral policy was read separately at 2026-11-05: global canonical main \`262c14ea545284945656d843fa11662c2d029de8\`, EM control main \`db5f524f22ac71d6627e1b76a2a50dbc041ef68a\`. The finite BRC model is an auxiliary positive-rational stochastic/path observer, not a claim of a complete native X6 physical realization.

## Theorem: Q-lumpable likelihood-ratio keys are a future-safe quotient

Let the finite-horizon, finitely branching **history tree** have strictly positive conditional P and Q transition probabilities. At every nonterminal history h at discrete time t, the permitted actions are STOP_P, STOP_Q and CONTINUE; at terminal time T, STOP_P or STOP_Q. A behavioral strategy uses independent fresh randomization conditional on its information. FULL may condition on complete h, while seedless LR may condition only on k(h)=(t,r(h)), with r(h)=P(h)/Q(h)>0 for the unconditional all-continue path measures. The stopped observation is

\[
O_4(\pi)=(P_\pi[\mathrm{declare}\ Q],\,Q_\pi[\mathrm{declare}\ P],\,E_{P,\pi}[\tau],\,E_{Q,\pi}[\tau]).
\]

Assume **Q-key lumpability**: for each nonterminal key k=(t,r), the pushforward under k(h') of the conditional Q successor kernel on CONTINUE is the same probability distribution K_k for **all histories h with k(h)=k**. The continuation kernels are policy-independent. The initial distribution also has a well-defined key pushforward. Then, for **every real behavioral FULL strategy** pi, there is an explicitly constructible real behavioral seedless LR strategy bar(pi) with exactly the same four coordinates. Consequently,

\[
\boxed{O_4(\mathrm{FULL})=O_4(\mathrm{seedless\ LR})=\operatorname{conv} O_4(\mathrm{FULL})=\operatorname{conv} O_4(\mathrm{seedless\ LR}).}
\]

The same construction preserves any finite collection of P- or Q-expectations of additive stopped-history observables whose per-stop contribution is a function of (t,r,declared label). It does not require that FULL's hidden-history action probabilities agree at merged keys.

### Proof (occupation-flow disintegration; all real parameters)

For a FULL strategy pi let q_pi(h) be the unconditional-Q path mass reaching the live history h (including the pi continuation factors on the preceding histories). Let m_pi(k)=sum_{h:k(h)=k}q_pi(h), and

\[
s_\pi(k,a)=\sum_{h:k(h)=k}q_\pi(h)\pi(a\mid h),\qquad a\in\{\mathrm{STOP_P},\mathrm{STOP_Q},\mathrm{CONTINUE}\}.
\]

At terminal keys omit CONTINUE. Define bar(pi)(a|k)=s_pi(k,a)/m_pi(k) for m_pi(k)>0, choosing an arbitrary legal distribution when m_pi(k)=0. This is a valid real seedless LR behavioral policy.

Under pi, the Q mass arriving at a next-time key k' is

\[
m_\pi(k')=\sum_{k:\,\mathrm{time}(k)=t} s_\pi(k,\mathrm{CONTINUE})K_k(k').
\]

The same recursion holds under bar(pi) because the Q-pushforward transition K_k depends only on the key. Their initial key masses coincide. Induction in t proves equality of all live m(k), and hence of all action occupancies s(k,a).

Each history h reaching a given k has P-to-Q density r, since decision randomization is measure-independent and the same continuation factors multiply the two path masses. Therefore P live/action mass at k is exactly r times Q mass, even when the individual hidden-history mixtures differ. The four observations are the following linear functionals of s:

\[
e_P=\sum_{t,r}r\,s((t,r),\mathrm{STOP_Q}),\quad
e_Q=\sum_{t,r}s((t,r),\mathrm{STOP_P}),
\]
\[
T_P=\sum_{t,r}t\,r\,\bigl[s((t,r),\mathrm{STOP_P})+s((t,r),\mathrm{STOP_Q})\bigr],
\quad
T_Q=\sum_{t,r}t\,\bigl[s((t,r),\mathrm{STOP_P})+s((t,r),\mathrm{STOP_Q})\bigr].
\]

They match exactly. Inclusion of LR strategies in FULL gives set equality. On a finite history tree the reachable FULL occupation-flow set is a bounded polytope (nonnegative flows and linear conservation constraints); every feasible flow is attained by normalization into behavioral probabilities. Its linear O4 image is a polytope, hence convex, completing the displayed equality. QED.

**Structural corollary for R5**: every finite lawful model realizing the R5 sought phenomenon (equal O4 convex hulls but unequal actual behavior images) must have a reachable LR key at which this Q-lumpability condition fails. This is a necessary screening criterion within the stated finite-tree model, not a claim that every failure yields a gap.

## Exact strictly positive two-gate compensation construction

Take hidden sources h=A,B, initial P(h)=Q(h)=1/2, merging at t=1, LR=1. CONTINUE produces a t=2 signal s=0,1 with Q(s|h)=(1/2,1/2) and P(s|h)=(1/4,3/4); thus t=2 keys are r=1/2 and 3/2, regardless of h. All stop/continue/P/Q declaration actions remain free at t=1,2.

Modify only the CONTINUE experiment from t=2 to the terminal time t=3. Independently draw c=0,1 with P(c|h,s)=Q(c|h,s)=1/2, and then j=0,1 with Q(j|h,s,c)=1/2. For A,c=0 and B,c=1 use likelihood multipliers (3/4,5/4) for j=0,1. For A,c=1 and B,c=0 use (1/2,3/2). Set P(j|h,s,c)=u(h,c,j)/2. These are normalized strictly positive probabilities because the mean multiplier in either experiment is one.

The **Q law of the next key** under CONTINUE, conditional on each t=2 key r, is the same for A and B: the four t=3 ratios

\[
r(3/4),\ r(5/4),\ r(1/2),\ r(3/2)
\]

each have Q probability 1/4. The t=1 transition is already Q-key lumpable. Terminal keys have no continuation. Thus the theorem gives **actual** O4(FULL)=O4(LR), for all real randomized actions, with full freedom of terminal P/Q declaration and positive conditional P/Q kernels.

The full terminal ratio-key union is {1/4,3/8,5/8,3/4,9/8,15/8,9/4}. The ratio 3/4 receives paths from both t=2 keys; the quotient is still valid because only the future key law, not unique path identity, is needed for these declared stopping observations.

A deterministic FULL test policy continues at t=1; at t=2 it stops P on (A,s=1), stops Q on (B,s=0), and continues otherwise. At t=3 it declares P for A and Q for B. This history-sensitive FULL strategy yields

\[
W=(1/2,1/2,5/2,5/2).
\]

Occupancy disintegration reconstructs an LR policy with the identical W. Its terminal P-declaration probability at the colliding ratio 3/4 is **1/2**, demonstrating genuinely mixed reconstruction at a merged key.

## Validation and provenance

The accompanying Python stdlib Fraction script evaluates the complete strictly positive joint P/Q path laws and exact behavioral occupancy. It checks the explicit witness and 512 seeded rational FULL behavioral policies, with exact reconstructed O4 equality and probability normalization. It also checks seven terminal LR keys and both balanced-multiplier normalizations. This finite arithmetic check corroborates the specified model; the theorem for arbitrary real policies and finite Q-lumpable trees follows from the induction above.

Applied BRC carrier: finite nonnegative rational P/Q branch weights with history/path identity retained through the proof; observer is (time, LR, declared action, stopped P/Q errors and times). Reuse: \`REUSE_APPLIED\` for positive-weight BRC provenance and prior R5 likelihood-ratio tree, plus standard occupation-measure Markovization proof technique. Neither mathematical novelty over general MDP occupancy theory nor independent admission is asserted. For external precedent, Romain Laroche and Remi Tachet Des Combes, "On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs", ICML 2023, PMLR 202:18548-18562, https://proceedings.mlr.press/v202/laroche23a.html. A separate 2026 semi-algebraic-value-set comparison is Ryan A. Anderson and Guido Montufar, ICML 2026, PMLR 306:2677-2715, https://proceedings.mlr.press/v306/anderson26a.html.

R5 mother task remains open: find a lawful model where hulls equal but actual images differ. The next exact unit must break key-lumpability in a reachable branch while looking for full four-dimensional hull equality; the prior positive-gap Jensen construction remains a valuable discriminatory baseline.
