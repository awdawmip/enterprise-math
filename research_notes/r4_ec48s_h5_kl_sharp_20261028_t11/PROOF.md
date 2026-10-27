# EC48S — Sharp five-stage BRC memory capacity for every intermediate width pair

2026-10-28 Asia/Shanghai. Research identity: EM-R004-EC48S-20261028-PORTABLE, independent portable TASK_RESEARCH (local author-side label, not a Source session or CLAIM). Math status: AUTHOR_PROVED / EXACT_COMPUTATION_PASS / UNREVIEWED / NOT_ADMITTED.

Frozen GLOBAL_KNOWLEDGE_V1 main@2d20804f76d412bcba30cde6485f866709504af3; Enterprise Math main@8391f12306c8cfb0064d7f4aa9f08e7b118420b4. Prior EC48R proof: PR #1589, commit 655892439b52c3aa8eb0b6d63ebfd1ecbe0e1d26. Native owner listing in this turn returned CONTROL_QUOTA, so this is not a canonical CLAIM, Research-Activity, Result or Driver admission.

## Exact model, theorem and formula

A finite strictly positive two-source P/Q *stopped* observation tree has a single stage-1 root, exactly k global histories at stage 2, exactly l global histories at stage 3 (2<=k<=l), stage-4 signals, and forced accept/reject at stage 5. Every extant edge has positive P and Q conditional mass. Single-child deterministic edges are allowed. Current signal, stage and joint-prefix P/Q likelihood ratio are visible; a controller may update an m-state register *before acting* from those observations and its previous register. It cannot secretly use earlier discarded history or a shared seed encoding that history. Random behavioral updates are source independent. Readout O=(Paccept,Qaccept,E_PT,E_QT); S_m is the original RAW attainable four-vector set.

**Theorem.** For every integer 2<=k<=l, the worst-case minimum register size sufficient to preserve the entire original RAW region is exactly

M*(H=5;k,l)=l.

Let s=ceil(log_2 l), mu=1/(4ls) and B=sum_{h=0}^{l-1} popcount_s(h). For *every* positive composition l=n_0+...+n_(k-1), there is a strictly positive rational experiment with those stage-3 counts below the respective stage-2 groups for which J_c=alpha-beta-c(tau_P+tau_Q) has optima, for **all real** 0<c<=1/(32l),

V_full = 1/4+B*mu/2-c(8+2*B*mu),
V_(l-1) = V_full-2c*mu,
V_full - V_(l-1) = c/(2ls) > 0.

Thus (l-1) states cannot even preserve the convex hull of RAW observables for these witnesses. The theorem allows stage-3 deterministic descendants when k=l. If every stage-2 group must genuinely split into at least two stage-3 histories, necessarily l>=2k and the same construction works with every n_g>=2.

## Exact positive rational BRC tree

At stage 2 group g has unconditional P=Q=n_g/l. Each of its n_g stage-3 descendants h has unconditional P=Q=1/l, with likelihood ratio 1 at every prefix through stage 3. Give the l distinct histories the binary words w_h representing integers 0,...,l-1 with s bits, leading zeroes.

From each h, the same stage-4 *signal names* occur:
private '+' has (P,Q)=(1/(2l),1/(4l)), current joint ratio 2;
private '-' has (1/(4l),1/(2l)), ratio 1/2;
each shared j in 0,...,s-1 has (mu,mu), ratio 1.

Total for each h under either source is 3/(4l)+s*mu=1/l. At t=5 each private branch has one deterministic child. Shared j with w_h[j]=0 has one neutral child of mass (mu,mu); if w_h[j]=1 it splits into up=(3mu/4,mu/4) and down=(mu/4,3mu/4), terminal joint ratios 3 and 1/3. All extant masses are positive rationals; terminal P and Q masses each sum to one; leaf count is 2l+ls+B. A collided register cannot distinguish h at a shared stage-4 signal j because both its name and current joint ratio are identical.

BRC application is the exact positive-rational branch carrier and P/Q-ratio fiber aggregation from definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json: REUSE_APPLIED, not an assertion of native heartbeat or BRC-Shor executable integration.

## Universal l-state RAW preservation (self-contained upper bound)

Fix any full-history randomized policy. Denote its nonterminal continuation probability at prefix g by t(g), its stopped-and-accepted conditional probability by b(g) with 0<=b(g)<=1-t(g), and product of ancestor continuation probabilities by R(g), source neutral as a *function of full history*. Store an injective code of every prefix at times 1,2,3 (there are at most l). The previous register plus the current signal reconstructs the present prefix; early decisions and survival probabilities are copied exactly.

At time 4 reconstruct full g, write register 1 with probability t(g) and 0 otherwise; continue exactly when state=1. On each stage-4 joint-likelihood fiber F_r where P(g)=rQ(g), define D_r=sum_{F_r}Q(g)R(g)(1-t(g)) and A_r=sum_{F_r}Q(g)R(g)b(g). If state=0 and ratio r, accept with probability A_r/D_r for D_r>0, arbitrary otherwise. It is in [0,1] and preserves Q stopped acceptance A_r and P stopped acceptance r*A_r. Both sources' continued mass is unchanged.

All survivors at stage 5 have register 1. On each terminal joint-likelihood fiber F_z, set accept probability [sum_{F_z} Q(g)R(g)a_full(g)]/[sum_{F_z}Q(g)R(g)], arbitrary for zero denominator. This simultaneously preserves P and Q terminal accepted mass by fiber constancy. Stage-by-stage survival masses match separately, so E T=sum_{t=1}^5 Pr(T>=t) matches under each source. Hence **each** full-history raw four-vector is reproducible with l states. Full history can simulate every register policy, yielding S_l=S_full.

## Sharp (l-1)-state separating support bound

(1) Any finite controller's linear-support maximum has a deterministic optimizer: each time/input stochastic decision/update row lies in a simplex and is visited at most once along any acyclic path. With other rows fixed, objective J is affine in that row, so successive extreme-point maximization is valid. No missing private randomness can improve the global maximum.

(2) At stage 4, regardless of register, private '+' optimally stops/accepts (ratio 2), private '-' stops/rejects (ratio 1/2). At terminal, up accepts and down rejects by visible joint ratios; neutral tie choices can reject. Continuing private signals adds time cost without useful discrimination.

(3) For 0<c<=1/(32l), stopping before stage 4 is dominated. Every stopped stage-3 type h is at ratio 1; sending it onward through any available register message gains private contrast 1/(4l), and costs at most 2c/l for reaching stage 4 plus 2c*s*mu=c/(2l) to reach stage 5 on all common signals. Net gain >=[1/4-(5/2)c]/l>0. If a controller row represents several h, switch that row together; each has the same strict bound. Once all stage-3 rows continue, reopening a stopped stage-2 group with n descendants yields gain at least n/(4l) private contrast and at most (2cn/l)+(2cn/l)+(2cns*mu)=(9/2)cn/l extra time penalty, so net n[1/4-(9/2)c]/l>0. If k=l and early group codes collide, this grouped dominance still works. Stopping at root yields -2c, but the feasible policy continuing to stage 4 and accepting only private '+' gets 1/4-8c>0. Thus any support-optimal policy continues to stage 4 for every h.

(4) Let f(h) be h's register message after stage 3. In shared row (m,j), let n1,n0 count represented words with bit 1 and 0 at j. Relative to stopping, continuing yields mu[n1/2-2c(n1+n0)]. This is negative if n1=0 and at least mu[1/2-2cl]>=mu[1/2-1/16]>0 if n1>=1. Thus a shared row continues **iff** any represented bit equals 1. Every informative 'up' reward is collected, but each shared zero bit that also advances adds 2mu to tau_P+tau_Q, losing 2c*mu.

(5) Any mapping of l **distinct** binary words into m=l-1 register messages collides at least two distinct words. They differ in some coordinate, forcing a 0 and 1 in the same shared row and at least one unnecessary neutral continuation. Even permitting an arbitrary map f (possibly relaxing earlier encoding constraints) bounds every actual m-state support value by V_full-2c*mu. Equality is *attainable*: merge words w_0=00...0 and w_1=00...1, which differ at exactly one coordinate, with all other words separately encoded. For k<l, m=l-1>=k permits distinct stage-2 parent codes and that stage-3 remapping. For k=l, all stage-3 children are deterministic; merge parent codes 0,1 at stage 2 and distinguish the rest. Stage 4 continues when a represented word has bit 1. Exactly one zero-bit history is unnecessarily continued. The gap is therefore exactly 2c*mu.

Both policies have explicit attainable RAW witnesses (taking neutral stops to reject):

O_full=(1/2+3Bmu/4, 1/4+Bmu/4, 4+Bmu, 4+Bmu)
O_(l-1)=(1/2+3Bmu/4, 1/4+Bmu/4, 4+(B+1)mu, 4+(B+1)mu).

This proves the claimed worst-case cardinality and strict support gap, not merely an empirical finite conjecture.

## Actual exact validation

VERIFY.js executes exhaustive integer normal-form support enumerations, including group early stopping and stage-3 stop/message decisions, at c=1/(32l). For (k,l)=(2,3),(3,4),(2,2),(4,4), full/compared-policy counts are respectively (2048,1728), (32768,131072), (64,32), (65536,262144). For k=l, the independent per-group early-stop choices *relax* the m<k stage-2 encoding constraint, thus the computed compressed maximum is an upper bound, which the explicit realizable merged-parent controller attains. Checks also verify P=Q terminal normalization, strictly positive leaf masses and exact RAW vector formulas for l=2,3,4,5,8,11.

At (k,l)=(2,3), s=2, mu=1/24, B=2, 14 leaves and c=1/96: V_full=119/576, V_2=79/384, gap=1/1152. At (k,l)=(3,4), s=2, mu=1/32, B=4, 20 leaves and c=1/128: V_full=127/512, V_3=507/2048, gap=1/2048. Analytic real-parameter and unbounded integer-width conclusions are proved above rather than inferred from finite enumeration.

## Scientific boundary and contextual literature

The exact positive-rational observer tree is an auxiliary typed model. It is not a replacement for locked P000 six-dimensional native X6 Cell space with separately typed time. No native joint-state/readout/future-operation preservation bridge is supplied, so the raw region result cannot be exported as an X6 dynamical law. P000 and the ACTIVE world constraints remain unchanged.

Related work: Mintae Kim, “Finite Memory Belief Approximation for Optimal Control in Partially Observable Markov Decision Processes,” arXiv:2601.03132v1, submitted 2026-01-06, https://arxiv.org/abs/2601.03132. It derives Wasserstein policy-conditional finite-memory approximation bounds; its state model and results differ from this exact finite stop-test BRC register theorem. No exhaustive novelty determination from this abstract comparison.

Next precise question: EC48T, memory capacity for bounded common-signal alphabet and the distinction between linear-support versus entire RAW-region fidelity.