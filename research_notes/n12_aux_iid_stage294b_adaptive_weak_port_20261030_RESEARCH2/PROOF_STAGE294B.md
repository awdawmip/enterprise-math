# Stage294-B｜自适应动作下弱可合并的最小例与重复 Bernoulli 端口的有理精确放松缺口

Status: PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. This is an external finite controlled probability model, not an X6 native-dynamics, official CLAIM/Result, or independent review.

## Frozen sources / bridge scope
GLOBAL_KNOWLEDGE_V1 main@1da64e1589bd9a1b29ea40706df7e0189b657be5; Enterprise Math main@96da51b79be3604143e7ffd6e27eb4faa5d28083; Stage293-B parent exact commit 2ec0d172153641d3e4e7e85f84153150e336d33a (PR #1571, PROOF_STAGE293B and NEXT_TASK_PACKET_294B). Original P000 Git blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488; GLOBAL P000_STARTUP projection referenced older 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc and was not substituted for original. ACTIVE heartbeat/X6 and residual-fidelity/joint-observer contracts plus portable-research protocol were read. Weighted BRC exact finite positive-rational branch sum/product and source/history preservation are used at the level of a typed mathematical law (REUSE_APPLIED; native typed BRC implementation NOT EXECUTED). No native correspondence theorem is claimed.

Scope: the observer is the complete ordered visible word with optional action/source tags as stated; future operations may select L/R adaptively from visible history and independent outside randomization, but not hidden state. Zero-probability histories are not conditioned on.

## Theorem 294.1: a three-hidden-state, two-action fully adaptive weak/strong separation
Take states a,b,c, visible output o(a)=o(b)=0 and o(c)=1, and initial measure mu=(1/2,1/2,0). With columns a,b,c, transitions have rows:

P_L(a)=(1/2,1/4,1/4), P_L(b)=(0,1/4,3/4), P_L(c)=(0,0,1);
P_R(a)=(0,1/4,3/4), P_R(b)=(1/2,1/4,1/4), P_R(c)=(0,0,1).

For either action the submatrix on B={a,b} has both *column sums* 1/2. Whenever conditional hidden distribution given a positive-probability surviving visible/action history is (1/2,1/2), the unnormalized next-hidden masses at a and b are each (1/2)*(1/2)=1/4. Thus survival probability is 1/2 and posterior given survival is again (1/2,1/2); absorption at c has probability 1/2. By induction from mu this filtering invariant holds after every finite all-zero observation history, for every visible-history-adapted policy (randomized policies likewise by conditioning on their external randomization). Once c is reached, all later visible outputs are 1. Thus the joint law of all finite visible-output and chosen-action words agrees exactly with the two-state controlled quotient 0->0 with probability 1/2, 0->1 with probability 1/2, and 1 absorbing, with both actions sharing this same quotient kernel. This proves a TWO-LABEL EXACT WEAK QUOTIENT for the fixed initial mu.

For a strong output-preserving quotient valid independently at every original reachable state, a and b cannot merge: P_L(a,{c})=1/4 differs from P_L(b,{c})=3/4, and action R reverses the values. Hence the coarsest strong quotient has three blocks {a},{b},{c}, requiring THREE LABELS. A one-label weak quotient cannot represent both visible output values, which occur with positive mass; thus exact weak minimum is two. With at least two visible values and a same-output pair whose per-state block probabilities disagree, three hidden states are minimal. If the source a/b is subsequently observed, the weak two-label preservation no longer holds: each source’s first-step output distribution differs from the quotient by TV=1/4. This is observer- and initial-law-specific weak lumpability, not strong lumpability.

Prior art: weak lumpability is classical (Ledoux, Journal of Applied Probability, 2016, https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/geometric-invariant-in-weak-lumpability-of-finite-markov-chains/038435A194FC5FC8E946C862EF1E3704); stronger all-start laws and higher-order lumpability are distinct (Geiger/Temmel, https://arxiv.org/abs/1212.4375). No historical priority claim.

## Theorem 294.2: exact fixed-two-label unrestricted-output LP optimum

A history with port parameter p generates TWO ORDERED independent Bernoulli bits from the SAME parameter p, so B_p=( (1-p)^2, p(1-p), p(1-p), p^2 ) on words 00,01,10,11. Take six equally weighted original histories: the first five with p=0,1/4,1/2,3/4,1 have FROZEN quotient label 0, and the sixth with p=1/2 has label 1. Risk is the source-retaining conditional total variation averaged over six histories. A label may use a common output kernel Q. When unrestricted Q may be any probability distribution on four words, label1 fits perfectly as B_{1/2}. Label0 can be symmetrized with Q(01)=Q(10) without increasing risk by TV convexity and the targets' swap symmetry. Collapse the pair 01,10 into the Hamming-count vector q=(q0,q1,q2); a target becomes K_p=((1-p)^2,2p(1-p),p^2), and TV of the ordered word distribution equals TV of these vectors because both are exchangeable.

Let L_j(z)=sum_{five p}|z-K_p[j]|. At q*=(1/4,3/8,3/8), subgradient ranges of (L_0,L_1,L_2) are respectively [-1,1], [-1,3], and {1}. Hence 1 is a common subgradient of each coordinate. For any q in the simplex, sum L_j(qj) >= sum L_j(q*j)+sum(qj-q*j) = sum L_j(q*j). Direct exact evaluation gives (sum L_j(q*j))/2=2. Thus the five-history unrestricted LP optimum is EXACTLY 2, attained at ordered Q*=(1/4,3/16,3/16,3/8). The normalized six-history risk is 1/3. This is a complete exact LP dual certificate, not a solver guess.

## Theorem 294.3: the deterministic-parameter repeated-port optimum is 17/8

Suppose quotient label 0 must use one DETERMINISTIC common parameter theta for BOTH Bernoulli draws, Q=B_theta; the two labels may separately set their own parameters but cannot mix parameter values within a label. For label 0 let F(theta)=sum_{five p} TV(B_p,B_theta). The absolute-value signs of coordinates K_theta[j]-K_p[j] change only when theta=p or theta=1-p; the complete breakpoints are 0,1/4,1/2,3/4,1. The exact polynomial for F on each interval is:

[0,1/4]: theta^2 - 4theta + 25/8, interval minimum 35/16.
[1/4,1/2]: -3theta^2 + 2theta + 15/8, interval minimum 17/8.
[1/2,3/4]: -3theta^2 + 4theta + 7/8, interval minimum 17/8.
[3/4,1]: theta^2 + 2theta + 1/8, interval minimum 35/16.

The outer intervals are monotone toward their nearer inner endpoint; the two interior polynomials are concave and have their minimum at endpoints. Therefore global minimum is F(1/2)=17/8. Label 1 again fits perfectly. For this FROZEN two-label assignment, the exact deterministic shared-port gap versus the free-output LP is (17/8-2)=1/8 unnormalized, or 1/48 when weighted by six source masses. This does NOT prove a gap for relabeling all six histories freely, nor a gap for probabilistically mixed ports.

## Theorem 294.4: this deterministic gap disappears under correct port randomization

Allow label0 to draw one parameter before the two Bernoulli observations, keeping that parameter unchanged on the sample path. Choose theta=3/7 with probability 49/64 and theta=1 with probability 15/64. Exact moment calculation:

(49/64)K_{3/7} + (15/64)K_1 = (1/4,3/8,3/8) = q*.

Therefore the unrestricted LP minimum 2 is realized exactly by a TWO-ATOM GLOBAL RANDOMIZATION WITHIN LABEL. The previous strict 1/8 gap is an exact feature of the deterministic port class only, and cannot be promoted to a claim about randomized BRC strategies. If different label ports must additionally share one global parameter, or a future operation reads the latent parameter / its source correlation, a new joint-source/path certificate is required. Keeping this distinction is a scientifically material observer/future-operation requirement.

## Executed evidence, verification scope and provenance

REPRO_STAGE294B.py uses the Python standard library Fraction without numerical tolerance. It checked every probability row, conditional filter invariant and strong discrepancy, and compared the full observable distribution of all 255 action words through horizon 7 (1793 positive observation leaves) with the two-state quotient. It checked the common-subgradient LP certificate, derived each piecewise polynomial by exact sign algebra, verified its complete interval minima, and checked the rational two-atom mixture. Observed stdout is REPRO_STAGE294B_EXECUTED_STDOUT.txt with marker STAGE294B_ADAPTIVE_WEAK_AND_TYPED_PORT_EXACT_PASS. Universal all-horizon/adaptive and real-theta claims rest on the algebraic proofs above, not the finite tests.

Site read research_authority_granted=false; owner discovery returned CONTROL_QUOTA. No native source-issued session/CLAIM/Result, no independent Driver admission, no native P000/X6/heartbeat/BRC-Shor bridge. Portable author evidence only. Stage278-A N12 Bellman route remains separate.

Next Stage295-B: find a STRICT two-label LP relaxation gap after allowing legitimate joint pre-randomization and cross-label shared-parameter correlations, or prove exact feasibility for a typed finite family; separately measure minimal repair labels when the three-state weak quotient's observer is enlarged to include source or interventions. See NEXT_TASK_PACKET_295B.md.
