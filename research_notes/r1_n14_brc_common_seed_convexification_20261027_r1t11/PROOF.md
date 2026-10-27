# R1/N14 — Common persistent lottery convexifies two-law observer outcomes

Date: 2026-10-27 Asia/Shanghai. Status: AUTHOR_PROOF + EXACT_RATIONAL_CERTIFICATE. This is a derivation in a finite external path-probability model, not an independently accepted or native P000/X6 theorem.

Frozen verified inputs: GLOBAL_KNOWLEDGE_V1 main@07b8d313fe59948fcb976b9cdd7f6035656279f6; Enterprise Math main@55531a03bbe5b3b1d0dc8c5bd3c9c94901e89d02. Read global normative bootstrap/manual, ACTIVE worldview, project P000, source P000 V5, HEARTBEAT_WORLD_NATIVE_X6_TIME, joint observer-preservation, portable research protocol and current BRC research usage policy. GitHub identity: awdawmip. Native task-control query returned CONTROL_QUOTA; native session start denied STATIC_READONLY_SCOPE_DENIED with operation_sent=false. This author note is not a CLAIM, native Result or Driver decision.

Predecessors: research_notes/r1_n14_brc_two_law_fresh_coin_nonconvex_n2_20261027_r1t11/PROOF.md and research_notes/r1_n14_brc_observer_only_n2_sharp_20261027_r1/PROOF.md. This work adds an exact criterion for a distinct, explicitly strengthened strategy class and a finite lottery-support bound; it does not settle uniqueness of observer-only fresh-coin quotients.

## 1. Exact model

Let H_t be a finite ordered history set, t=0,...,N, with one initial root and strictly positive path-cylinder laws P,Q. At history h and time t<N a policy takes one action CONTINUE, STOP(0), STOP(1); at terminal t=N it must STOP(0) or STOP(1). One shared policy governs both laws. The next-symbol kernel is law dependent; random decisions are state-history dependent but otherwise are private choices, independent of nature.

Let z_t(h) be a finite time-typed deterministic quotient updated by z_{t+1}(ha)=rho_t(z_t(h),a). The output is Y=(T,o_t(z_t(H_T)),D), with a fixed finite readout o_t. The observer-only case is o_t constant and Y=(T,D).

A fresh-coin z-policy uses only (t,z_t) and new random coins, with no hidden persistent selector. A common-seed z-policy samples K once at the initial root independently of P/Q, remembers K, then executes a deterministic complete state-action table f_K(t,z). The weights of K must be exactly the same under both laws.

Let G_H and G_z be the finite sets of paired terminal-law vectors v=(Law_P Y,Law_Q Y) produced by deterministic complete-history and deterministic z-tables. Let F_H denote all full-history randomized-policy vectors, and F_z^fresh and F_z^seed the two quotient classes.

## 2. Main theorem and proof

**Theorem (finite all-horizon common-seed criterion):**

~~~
F_H = conv G_H;
F_z^seed = conv G_z;
F_z^fresh subset F_z^seed subset F_H;
all full-history policies admit matching common-seed z-policies
        if and only if conv G_z = conv G_H.
~~~

For every full-history behavioral policy, sample independently in advance the action at every complete possible history using that history's policy kernel. Because a realized history is visited at most once, the resulting random deterministic full table produces precisely the same action-and-path distribution under either law. This proves F_H subset conv G_H.

Conversely suppose a common initial lottery chooses deterministic complete-history table f_k with weight w_k. For a history h let s_k(h) equal 1 precisely when table f_k continues at every strict ancestor of h, and zero otherwise. Conditional on reaching h under R=P or Q, the posterior of K is

~~~
Pr(K=k | h reached, law R) =
     R(h) w_k s_k(h) / sum_l R(h) w_l s_l(h)
   = w_k s_k(h) / sum_l w_l s_l(h).
~~~

The second expression is law independent. If the denominator is zero h is unreachable under the mixture and its local action is arbitrary. Otherwise the behavioral full policy uses this posterior to mix the actions prescribed by the f_k at h. Induction over the tree reproduces the complete joint path/action law under BOTH R=P,Q, and thus conv G_H subset F_H. This is an explicit perfect-recall behavioral/mixed equivalence; no claim of novelty over Kuhn's theorem is made.

For a fresh-coin z-policy, independently sample in advance the action at each time-tagged state (t,z). A realized path visits each such state at most once because t strictly increases. Hence this random deterministic z-table exactly reproduces the fresh-coin outcomes under P,Q. Thus F_z^fresh subset conv G_z. Every convex combination of deterministic z-tables is implemented by the common persistent selector K, giving F_z^seed = conv G_z. Each deterministic z-table lifts to a full deterministic history table h->f(t,z_t(h)), whence G_z subset G_H. Combining these facts proves the theorem.

Two further equivalent finite certificates follow:

**Support criterion.** The two compact polytopes are equal iff, for every vector c of observer-coordinate coefficients,

~~~
max_{g in G_z} (c dot g) = max_{g in G_H} (c dot g).
~~~

If unequal, there is a strict rational linear separator whenever P and Q have rational cylinder masses. It eliminates ALL common-seed z-policies, not just fresh-coin policies.

**Exact LP criterion.** For each g in G_H, solve the linear feasibility problem

~~~
lambda_f >= 0; sum_{f in G_z} lambda_f = 1;
sum_{f in G_z} lambda_f f = g.
~~~

All g must be feasible; checking only vertices of conv G_H also suffices. For rational P,Q the data are rational and exact arithmetic decides the finite test. Computational cost can be exponential; no efficient algorithm is claimed.

**Seed support bound.** If the paired output vector has m scalar coordinates, the two probability blocks each sum to 1, giving affine dimension <=m-2. By Caratheodory, any common-seed outcome uses <=m-1 deterministic z-tables. For binary D, times 0,...,N, constant o, m=4(N+1), so <=4N+3 lottery entries suffice (upper bound; not sharpness).

## 3. Exact separation of fresh coin vs persistent common lottery

Take N=2, alphabet {0,1}, two strictly positive IID laws P=(3/4,1/4) and Q=(1/4,3/4). State z_1 retains the first letter i; z_2=* forgets all history; readout (T,D). The root always continues.

Deterministic strategy A stops (T=1,D=0) for i=1, and for i=0 continues to t=2 and sets D=1. Strategy B stops (T=1,D=0) for i=0, and for i=1 continues to t=2 and sets D=0. Their shared 50–50 initial lottery yields:

| Event | P | Q |
|---|---:|---:|
| T=1,D=0 | 1/2 | 1/2 |
| T=2,D=0 | 1/8 | 3/8 |
| T=2,D=1 | 3/8 | 1/8 |

Every fresh-coin policy has one terminal D=1 probability d at z_2=*, common to both laws. Therefore every such policy satisfies

~~~
P(T2,D1) Q(T2,D0) - Q(T2,D1) P(T2,D0) = 0.
~~~

For the lottery target the left side equals 3/8*3/8 - 1/8*1/8 = 1/8. Hence this target lies in F_z^seed but not F_z^fresh. At least two persistent selector values are needed for this specific target, and two suffice. This repairs a nonconvexity obstruction, not a proof of universal sufficiency of this z.

## 4. A linear loss gap persists even with arbitrary common initial memory

Reuse the predecessor strict-positive ternary non-IID N=2 model. At t=1 I is uniform on {0,1,2} under both laws. P(J=j|I=i), ordered j=0,1,2, has rows:

~~~
i=0: (1/4,  1/4, 1/2)
i=1: (1/12, 3/4, 1/6)
i=2: (1/6,  1/2, 1/3).
~~~

Define Q(J=j|I=i)=r_j P(J=j|I=i), with r=(2,1,1/2). All entries are positive and all Q rows sum to 1. Quotient z_1=* erases I, and terminal z_2=j keeps only J; observer Y=(T,D). The full-history witness continues after i=0 only and sets D=1 at t=2 exactly for j=0. Thus P(T2)=Q(T2)=1/3, P(T2,D1)=1/12 and Q(T2,D1)=1/6.

For a vector v define the linear functional

~~~
L(v) = Q(T2,D1) - P(T2,D1) - (1/6) P(T2).
~~~

A deterministic z-policy stopping at z_1 has L=0. If it continues, the unconditional j marginals satisfy barQ-barP=(1/6,0,-1/6). For any terminal binary decisions, Q(T2,D1)-P(T2,D1) <=1/6=P(T2)/6; hence L<=0. All common-seed mixtures also have L<=0 by linearity, and the same holds for all fresh-coin policies. But the full witness yields

~~~
L(full) = 1/6 - 1/12 - 1/18 = 1/36 > 0.
~~~

The exact gap 1/36 certifies failure of the polytope criterion even with arbitrary common initial persistent selector. No finite grid search is used in the proof.

## 5. Exact verification, BRC interpretation and prior art

VERIFY.py uses Python Fraction for exact rational arithmetic and RESULT.json records its actual execution. It computes the binary lottery midpoint and 1/8 determinant; validates the 13 full ordered prefixes and both probability normalizations of the ternary model; computes the full-history 1/36 gap; and exhaustively checks 24 deterministic z-tables (three t=1 actions times 2^3 terminal decision rules), finding max L=0. The universal theorem is mathematical, whereas these computational tests cover the declared N=2 examples.

The BRC carrier is ordered positive two-law branch mass (P(h),Q(h)), provenance and stop/continue decisions. Convexification remembers the branch-independent selector K as a distinct residual state. The 1/8 determinant diagnoses information that a fresh-coin observer drops, while the 1/36 linear gap diagnoses future-relevant branch information that even an initial selector cannot reconstruct. This finite probability model is an external auxiliary calculation. Native Heartbeat/X6 translation requires a declared X6 state/slice embedding, branch mapping and future-operation preservation certificate.

Prior art (bibliographic verification on 2026-10-27):
- H. W. Kuhn (1953), Extensive Games and the Problem of Information, Contributions to the Theory of Games II, Annals of Mathematics Studies 28, pp. 193–216. https://cir.nii.ac.jp/crid/1571135650130603904 ; collected chapter https://doi.org/10.1515/9781400829156-011 .
- B. von Stengel (1996), Efficient Computation of Behavior Strategies, Games and Economic Behavior 14(2), 220–246. https://doi.org/10.1006/game.1996.0050 .

Research contribution here is the precise two-law observer/policy-class criterion, memory-size bound, and exact application of the predecessor BRC witness. General perfect-recall mixed/behavior equivalence is classical.

**Next unsolved exact question:** for N>=3, fresh-coin observer-only policies, find two incomparable maximally coarse universally sufficient deterministic right congruences, or prove uniqueness under exact additional hypotheses. First screen candidates by the rational support criterion; passing that necessary seeded test does not prove fresh-coin all-policy preservation. See NEXT_TASK.md.

Status: AUTHOR_PROOF_COMPLETE / FRACTION_CHECK_PASS / NATIVE_OWNER_AND_CLAIM_UNVERIFIED / INDEPENDENT_REVIEW_PENDING.
