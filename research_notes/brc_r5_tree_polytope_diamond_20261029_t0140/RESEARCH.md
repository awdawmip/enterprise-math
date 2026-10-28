# R5 — BRC observation-tree polytope theorem and rank-two diamond detector

Research date: 2026-10-29 (Asia/Shanghai).
Author-side portable derivation. Status: AUTHOR_PROVED / EXACT_RATIONAL_REGRESSION / UNREVIEWED / NOT_ADMITTED.
Frozen global input: GLOBAL_KNOWLEDGE_V1 main@444be71e21172c9e5ca4e443f488f1c96d493775.
Frozen project input: enterprise-math main@acacf784d6fc5357316f4217e6fb0354760aed21.
Preceding R5 input: research_notes/brc_r5_four_signature_rank_two_convex_rate_20261029_t0045/RESEARCH.md at 7a33f26b90a1bc9c8183f87c37076bfa8eeee42b.
P000, ACTIVE residual-faithful worldview and portable research protocol apply. No native X6 transfer is claimed.

## Exact finite model

There are finitely many source/origin histories i with nonnegative Q masses a_i, identifiable by a full-history policy but compressed by a seedless likelihood-ratio (LR) policy. Each observed history ends in a positive LR s, so its P mass is s times its Q mass. The P and Q laws are normalized. At each nonterminal LR decision state v=(time,s), the policy stops or continues through a fixed, source-dependent, finite observation kernel; a continue action does not itself change that kernel. Its child P transition probability is (s_child/s_parent) times its Q probability.

The LR policy uses fresh behavioral coins depending only on the current (time,s) and on no persistent random seed. The full-history policy may use its actual source and complete history. A terminal randomized declaration produces the four coordinates
O=(e_P,e_Q,T_P,T_Q)=(P(declare Q), Q(declare P), E_P[tau], E_Q[tau]).

**Single-entry decision-tree hypothesis.** After the initial permitted collapse of several origins at the root, every nonroot nonterminal LR state has exactly one predecessor among nonterminal LR states. Different post-root observable decision paths never recombine at a common nonterminal state; terminal observations may be aggregated freely at the same (time,s). Every path transition probability for a fixed source is independent of the chosen local continuation probabilities. There are finitely many nodes and a forced finite stop time. Strictly positive rational kernels are permitted but not required for the general theorem.

## Theorem R5-TREE (all real behavioral strategies)

Under these assumptions the real seedless LR four-observation image and the full-history four-observation image are **compact convex polytopes**. In particular,

    conv(O_full) = conv(O_LR)  if and only if  O_full = O_LR.

Thus this entire tree class, irrespective of kernel equality, signed information-rate equality, convex domination, source count, signature count or branch count, cannot solve the mother question (equal four-dimensional convex hulls, unequal actual images). A genuine **post-root merging of two distinct LR-observable decision paths**, or a departure from the specified finite fixed-kernel model, is necessary for such a witness.

### Full constructive proof

Fix an LR nonterminal node v. Let kappa_i(v) be the product of its unique-path Q transition probabilities from the root for source i, with kappa_i(root)=1. By uniqueness of the post-root path, these factors are constants independent of the strategy. Introduce prefix survival factors x_v and continuation factors u_v subject to the linear constraints

    x_root = 1;
    0 <= u_v <= x_v;
    x_w = u_v for each nonterminal child w of v.

Origin-i Q arrival mass at node v is a_i*kappa_i(v)*x_v; Q continue mass there is a_i*kappa_i(v)*u_v; stopping mass is a_i*kappa_i(v)*(x_v-u_v). Every terminal child from a continued node contributes a_i*kappa_i(v)*u_v*mu_i,v(s) to its (time,s) cell. Any forced-stop flow is a fixed additive constant. Consequently every aggregate terminal Q cell mass W_(t,s) is an affine expression in (x,u).

Conversely, every feasible assignment (x,u) is implemented by a real seedless LR behavioral policy: set alpha_v=u_v/x_v if x_v>0, and alpha_v=0 if x_v=0. Induction down the decision tree gives exactly the specified prefix survival factors. No external or persistent random seed enters the construction.

Introduce aggregate joint Q declaration masses m_(t,s) with

    0 <= m_(t,s) <= W_(t,s)(x,u).

They are implemented by a single terminal LR coin theta_(t,s)=m_(t,s)/W_(t,s) when W_(t,s)>0 and zero otherwise. Each history with observed LR s contributes P mass s times Q mass, so the exact observables are LINEAR:

    e_P = 1 - sum_(t,s) s*m_(t,s);
    e_Q = sum_(t,s) m_(t,s);
    T_P = sum_(t,s) t*s*W_(t,s);
    T_Q = sum_(t,s) t*W_(t,s).

The prefix constraints and declaration bounds define a bounded closed polyhedron. Its linear projection is exactly O_LR; hence O_LR is a compact convex polytope.

For the full-history class, duplicate (x_v,u_v) by the source i and each distinct full-history decision node, retaining the same path-flow constraints. A real full-history behavioral policy is recovered by the same local ratio u/x. Full terminal declaration probabilities may differ by source/history, but their aggregated m_(t,s) always lies between zero and W_(t,s). Conversely EVERY aggregate m in this interval is implemented by the source-independent declaration coin theta=m/W, which the full-history class also permits. Thus O_full is also a linear projection of a bounded polyhedron.

The seedless LR class is contained in the full-history class. For any convex set A contained in B, conv(A)=conv(B) implies B is contained in conv(B)=A, whence A=B. Apply with A=O_LR, B=O_full. QED.

The theorem is observer-scoped to the four declared expected quantities. It does not show equality of source-resolved terminal laws, nonadditive path statistics, full trajectory distributions, physical Heartbeat dynamics, or native X6 spatial transfer.

## Exact four-signature positive rational branching witness

Let S=(1/2,1,3/2,5/2), root LR r=3/2, two different time-2 nonterminal children left=1 and right=3/2, with all time-3 outcomes terminal. Initial Q masses are a_A=a_B=1/4 at the root plus 1/2 forced terminal at LR=1/2; initial P masses are 3/8,3/8,1/4.

In S order, the root Q kernels are

    mu_A=(7/50,11/75,1/2,16/75),
    mu_B=(17/200,23/150,3/5,97/600).

The time-2 kernels at left (mean 1) are

    nu_A,left=(1/2,1/6,1/4,1/12),
    nu_B,left=(5/12,1/3,1/6,1/12).

At right (mean 3/2) they are

    nu_A,right=(17/100,23/75,1/5,97/300),
    nu_B,right=(31/120,5/18,1/15,143/360).

Every kernel is strictly positive, sums to one, and has the displayed parent LR as its mean. Its induced P kernel is strictly positive and normalized.

Any seedless LR stopping policy with local continuations (a_root,a_left,a_right) is represented by exactly three prefix flows (a_root,a_root*a_left,a_root*a_right), satisfying 0<=u_left,u_right<=u_root<=1. This is a convex linear region despite the multiplicative behavioral presentation.

Take L1=(1/2,1/4,3/4), L2=(3/4,3/5,1/5). Their weight-2/5 mixture has prefix flows (13/20,8/25,6/25), implemented by the genuine single LR policy Lmix=(13/20,32/65,24/65). Let L1 declare P at terminal (time t, signature index j=1..4) with probability (t+j)/12 and L2 declare with probability (2t+j)/13. The mixed terminal joint declaration mass is m_mix=(2/5) W1 theta1+(3/5) W2 theta2, and a single seedless terminal coin theta_mix=m_mix/Wmix implements it at every terminal cell. Exact calculations yield

    O1=(905869/1382400,839/3072,197/128,109/80),
    O2=(113169/208000,7699/20800,2653/1600,29/20),
    Omix=(132214997/224640000,827003/2496000,3221/2000,283/200).

Each coordinate of Omix is (2/5)O1+(3/5)O2. Attached VERIFY.py and EXACT_OUTPUT.txt check all P/Q normalizations and positive kernels, all terminal joint declaration bounds, the explicit mixed behavioral coin, and 600 additional exact-rational stopping policies against a five-vertex flow decomposition. These tests verify arithmetic, while the universal conclusion is given by the proof above.

## Rank-two diamond merge: an exact source-flow obstruction

Keep the same kernels, but allow the time-3 LR=3/2 reached from EITHER time-2 child to be nonterminal. At that merged state, a seedless LR policy must use ONE shared continuation probability gamma. The final time-4 Q terminal kernel may be any fixed strictly positive mean-3/2 kernel, e.g. eta=(1/8,1/4,3/8,1/4).

With root continuation one and independently selected time-2 continuation flows p,q in [0,1], the two incoming source-resolved Q contribution vectors are

    v=(a_A mu_A(1) nu_A,left(3/2), a_B mu_B(1) nu_B,left(3/2))
     =(11/1200,23/3600),
    w=(a_A mu_A(3/2) nu_A,right(3/2), a_B mu_B(3/2) nu_B,right(3/2))
     =(1/40,1/100).

Their exact determinant is det(v,w)=-49/720000. The incoming origin vector x=p*v+q*w and outgoing origin vector y=gamma*x must satisfy the polynomial equation

    y_A*x_B - y_B*x_A = 0.

Policies (p,q,gamma)=(1,0,1) and (0,1,0) give the feasible pairs (x,y)=(v,v) and (w,0). The midpoint would have x=(v+w)/2, y=v/2, violating the required equation by exactly -49/2880000. Therefore the SOURCE-RESOLVED joint input/output flow set of this genuine diamond is nonconvex.

**Local lemma.** Given nonnegative fixed origin-vectors v_j, independent p_j in [0,1], and one common gamma in [0,1], the set {(x,y): x=sum p_j v_j, y=gamma*x} is convex iff the nonzero v_j span dimension at most one. Proof: in rank one, x and y share a fixed nonnegative ray and the two scalar coefficients obey linear bounds 0<=y<=x<=sum_j |v_j|/|v|; all are attainable. In rank at least two, choose independent v,w and mix feasible (v,v) with (w,0); the midpoint is not collinear and so is infeasible. QED.

This rank-two obstruction is a statement about **origin-resolved flows**, not yet an impossibility certificate for the projected four-observation set. Projection and terminal declaration randomization may erase it. The mother question remains open; its smallest plausible candidate should contain a real post-root diamond and survive all signed support tests.

## Source context, BRC reuse and next discriminating action

BRC reuse resolution: REUSE_APPLIED — preserve distinct source/branch origins, positive rational Q and P masses, LR mean normalization, prefix occupancy, and verify the exact four-coordinate observer quotient before discarding provenance. This finite statistical proof does not assert a native Heartbeat/BRC–Shor simulation, triadic force balance, six-axis placement, or a three-dimensional slice theorem. No working-truth/Foundation or mathematical admission is claimed.

Relevant external context inspected 2026-10-29, without claiming external novelty: Laroche & Tachet des Combes, ICML/PMLR 202 (2023), https://proceedings.mlr.press/v202/laroche23a.html ; Cohen & Parmentier, Future memories are not needed for large classes of POMDPs (2023), https://www.research-collection.ethz.ch/entities/publication/9e7ebef3-5bd6-4103-8cc8-531794e68e0f ; Piunovskiy & Zhang, Extreme Occupation Measures in Markov Decision Processes with an Absorbing State, SIAM J. Control Optim. 62 (2024), https://doi.org/10.1137/23M1572398 . These works concern related but nonidentical assumptions.

Next: with the exact rank-two diamond above, derive projected (e_P,e_Q,T_P,T_Q) feasibility with shared gamma, preserving the rank-two source vectors, and determine whether a rational midpoint remains outside every real seedless LR strategy after terminal randomized declarations. Test ALL signed Bellman support directions before claiming convex-hull equality; if a support gap exists, exclude the candidate. Do not confuse source-flow nonconvexity with the required four-observer nonconvexity.

Actual control boundary for this run: GitHub account awdawmip has repository push access; native gateway task inventory returned CONTROL_QUOTA; native session start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. No active Source Owner/CLAIM could be established, so the present record is author-side research evidence, not a canonical native Result/Review.
