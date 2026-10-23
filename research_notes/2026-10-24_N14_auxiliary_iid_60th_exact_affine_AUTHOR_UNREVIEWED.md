# N=14 auxiliary iid BRC sequential testing — exact 60th affine segment

**2026-10-24 | AUTHOR PROOF; EXACT FINITE-MODEL CHECKS PASS; DRIVER UNREVIEWED.** This concerns only the auxiliary iid model. No native BRC/X6/Heartbeat correspondence or external experimental assertion follows.

## Model, provenance and theorem

This step inherits the author-verified 59th stopping tree, exact code and source at research_notes/2026-10-24_N14_auxiliary_iid_59th_exact_affine_AUTHOR_UNREVIEWED.md (Git blob ffeb98c74adec022d7e2098b763e7d200b166c95). Global knowledge was read at main@779a23bbf80a705993a4be5ca3cabfa9bdb3a2fe. P000 projection and canonical original match blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, unchanged.

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=14. Every ordered-history-dependent randomized decision/stop policy terminating by 14 is admissible. Put eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and

\[
V_{14}(\alpha)=\inf\{\max(t_P,t_Q):e_P,e_Q\leq\alpha\}.
\]

The inherited author endpoint and balancing mixing probability are
\[
\alpha_{59}={1292959874081248715\over3725075438477770752},\quad
V_{59}={24710104251021106757\over1862537719238885376},\quad
s_{59}={6488639185595039\over10444800000000000}.
\]

At the new dual crossing set
\[
A_{60}=(11,6,5),\quad B=(12,0,1),\quad
K_{60}={1259712\over139},\quad
\lambda_Q=K_{60},\quad \lambda_P=72+{8\over9}K_{60}={1129752\over139},\quad
\Gamma_{60}=\lambda_P+\lambda_Q={2389464\over139},
\quad\eta_{60}={2641\over551863027922632704}>0.
\]

**Exact theorem for every real delta between 0 and eta60 inclusive:**
\[
\boxed{V_{14}(\alpha_{59}+\delta)=V_{59}-\Gamma_{60}\delta.}
\]
Consequently
\[
\boxed{\alpha_{60}={5171839496325066167\over14900301753911083008}},\qquad
\boxed{V_{14}(\alpha_{60})={12355052125433941189\over931268859619442688}}.
\]

This supporting line ceases to attain the value function strictly to the right of alpha60. The value function itself does not terminate there.

## 1. Exact dual against all full-history strategies

For any history with count state (n,a,b), the likelihood ratio is L=Q(h)/P(h)=2^(a+b)/3^a. In P units the exact finite Bellman minimum is
\[
D(n,a,b)=\min\{\lambda_QL,\ \lambda_P,\ 1+\sum_{i=0}^{2}P_iD(\mathrm{child}_i(n,a,b))\},
\]
without the continuation option at n=14. Because future symbols are iid, this is a valid dual lower bound for policies depending on the entire ordered past; no primal Markov assumption has been introduced. Every strategy satisfies
\[
D(0,0,0)\leq t_P+\lambda_Pe_P+\lambda_Qe_Q
\leq\max(t_P,t_Q)+\Gamma_{60}\alpha.
\]
The exact rational sweep checks all 680 states and 1240 alternative-action comparisons against the inherited deterministic stop policy (with A59 now fixed to Q). It finds 1238 strictly positive gaps (minimum positive gap 201720865/3320414208), no negative gap, and precisely two zero gaps: at A60 and B, both continue versus immediate Q. The exact dual root is
\[
D(0,0,0)={91069131810101786682859\over15228984880835592192}
=V_{59}+\Gamma_{60}\alpha_{59}.
\]
This supplies the claimed universal affine lower bound.

## 2. Real ordered first arrivals, not multinomial overcounts

At A60=(11,6,5), there are binom(11,6)=462 nominal prefixes with six symbol-0 and five symbol-1 observations. Applying the prior earliest-stopping rule to each ordered prefix excludes 291 prefixes. Their *first* earlier stops are:
P at (6,6,0): 1 word; Q at (10,5,5): 89; Q at (9,4,5): 34; Q at (7,3,4): 76; Q at (6,2,4): 45; Q at (5,1,4): 18; Q at (3,0,3): 28. Exactly 171 prefixes genuinely first reach A60. The resulting P/Q masses are
\[
p_A={19\over231928233984},\qquad q_A={19\over82556485632}.
\]
At B=(12,0,1), all 12 prefixes first arrive, with
\[
p_B={48828125\over725594112},\qquad q_B={48828125\over362797056}.
\]
Exact conditional suffix-risk quadruples (eP,eQ,tP,tQ) under continuation are
\[
c_A=(511/512,\ 1/1728,\ 73/64,\ 157/144),\qquad
c_B=(63/64,\ 1/144,\ 9/8,\ 13/12).
\]
A and B first-arrival cylinders are disjoint because observation counts cannot decrease, so a history first reaching A60 (a=6,b=5) cannot later reach B (a=0,b=1), nor vice versa. The previous special P stop (12,7,2) also cannot be reached after A60 since b cannot decrease. Every remaining suffix is already covered by exact backward risk recursion.

## 3. Balancing and attaining the dual on a continuum

At A60 immediately decide Q with probability u, otherwise continue. At B immediately decide Q with probability s, otherwise continue. Relative to the 59th policy, with the inherited s59, first-arrival disjointness gives exactly
\[
e_P-\alpha_{59}=Xu+E(s-s_{59}),\quad
e_Q-\alpha_{59}=-Yu-H(s-s_{59}),
\]
where
\[
X=p_A(1-c_A.e_P)={19\over118747255799808},\quad
Y=q_Ac_A.e_Q={19\over142657607172096},
\]
\[
E=p_B(1-c_B.e_P)={48828125\over46438023168},\quad
H=q_Bc_B.e_Q={48828125\over52242776064}.
\]
The balancing relation is
\[
s(u)=s_{59}-h_{60}u,\qquad
h_{60}={X+Y\over E+H}={2055819\over13926400000000000},\qquad
\eta_{60}=X-Eh_{60}=-Y+Hh_{60}>0.
\]
Its endpoint is s(1)=25954556736212699/41779200000000000, strictly between 0 and 1. Therefore s(u) is an admissible probability for every real u in [0,1], and
\[
e_P=e_Q=\alpha_{59}+\eta_{60}u.
\]
Since each chosen or randomized action minimizes the Bellman dual, we have exact complementary slackness, yielding tP(u)=V59-Gamma60*eta60*u. Exact backward and forward recurrences show
\[
t_P(0)-t_Q(0)={328510182739260281\over620845906412961792}>0,
\qquad
t_P(1)-t_Q(1)={657020365661213713\over1241691812825923584}>0.
\]
All risks are affine in (u,s): the exact four-corner mixed term is zero because the tied first-arrival cylinders are disjoint. Hence tP>=tQ throughout every real u in [0,1]. Taking u=delta/eta60 yields primal attainment of the universal lower bound, proving the entire real interval theorem.

## 4. Sharp right endpoint

The finite-horizon history-dependent randomized-policy occupancy region is compact and polyhedral. If the same dual supporting line attained equality for alpha>alpha60, both positive multipliers would force eP=eQ=alpha, and any reached action with a strictly positive Bellman gap would be impossible. The exhaustive gaps leave decisions only at A60 and B. For arbitrary order-dependent mixtures within each count state, the iid likelihood ratio and conditional continuation suffix risks are constant across surviving prefixes, hence one may aggregate them to effective u,s in [0,1] without changing risk. Balancing forces s=s59-h60*u, so alpha=alpha59+eta60*u<=alpha60, contradiction. This proves sharpness without restricting the primal strategy class.

## Reproduction, status and next target

The supplied portable Python 3 standard-library Fraction checker tests all 680 states and 1240 gaps, ordered first-hit masses, conditional suffix risks, seven rational mixtures, root equality and candidate next crossing. The second author checker directly enumerates all 462 nominal A60 ordered words and their earliest stop states, independently minimizes all Bellman actions, and uses four-corner backward risk recurrences; the 12 B words and a later stop are also checked. **Both programs actually passed local execution**, but share explicitly inherited stop sets and are not an external independent Research Driver review, Lean certificate, or native BRC transfer.

After changing A60 to immediate Q the next *unproved* dual candidate is
\[
\boxed{K_{61}={18824330664\over2180893},\quad A_{61}=(7,5,0)}
\]
with continue/immediate-P tie. Next compute genuine first hits, propagated changes to later stop paths, compensation, the complete 61st real affine interval and sharpness. The native owner query returned CONTROL_QUOTA; no formal owner/CLAIM/Result/independent admission is asserted.