# Exact semialgebraic fidelity of four-observable BRC history quotients

**2026-10-27 — author-level mathematical note.** This document states and proves an exact finite decision method for an external positive-rational two-measure observation tree. It is not a native P000/X6/Heartbeat theorem, a formal Source Result, an authorized Task CLAIM, a completed CAD/QE run, or an independent mathematical review.

## Frozen scope and predecessor

GLOBAL_KNOWLEDGE_V1 input: awdawmip/chatgpt-global-knowledge@fcf778e263a2de22711ca308108f912f91d7b2e9. Enterprise Math input: awdawmip/enterprise-math@107a893ec5886ade2ca4966b554c723adf215cdd, including docs/PORTABLE_RESEARCH_PROTOCOL.md. Predecessor: research_notes/brc_n4_hidden_kernel_second_residual_20261026_r5/PROOF.md and NEXT_TASK.md. Its 32-leaf separation 1/96 is previous evidence, **not rerun or newly claimed here**. Current active native owner could not be resolved (CONTROL_QUOTA), and native session creation was rejected (STATIC_READONLY_SCOPE_DENIED, operation_sent=false). This is independently authored, non-admitted research material.

## 1. Precise policy semantics

Fix a finite rooted tree of ordered histories H_t for 0<=t<=N, including root e. Give every history positive rational masses p_h=P(h), q_h=Q(h), with p_e=q_e=1 and exact child-sum conservation. Define exact likelihood ratio L(h)=p_h/q_h. A history-dependent policy at depth t<N chooses action SP (stop, decide P), SQ (stop, decide Q), or C (continue); at depth N it must choose SP/SQ.

Fix any time-indexed state readout s_t(h), for instance (t,L(h),residual). A **behavioral compressed policy** assigns a probability distribution over available actions to each current state (t,s). It uses a fresh conditional action distribution when that state is encountered and retains no additional hidden initial random seed. A **mixed compressed policy** chooses a deterministic state-policy table using an initial random seed and remembers the chosen table; this latter global memory is a distinct policy class. The distinction is essential in history quotients with imperfect recall.

Let z_{h,a} denote full behavioral action probabilities, or z_{h,a}=y_{t,s_t(h),a} for compressed behavioral probabilities. Define the survival factor

    w_h(z) = product_{g strict prefix of h} z_{g,C}, with w_e=1.

Exactly, with H the union of all H_t,

    O_1(z) = sum_{h in H} p_h w_h(z) z_{h,SQ}
    O_2(z) = sum_{h in H} q_h w_h(z) z_{h,SP}
    O_3(z) = sum_{t=0}^{N-1} sum_{h in H_t} p_h w_h(z) z_{h,C}
    O_4(z) = sum_{t=0}^{N-1} sum_{h in H_t} q_h w_h(z) z_{h,C}.

These correspond respectively to P(decide Q), Q(decide P), E_P[tau], E_Q[tau]. The third and fourth identities use E[tau]=sum_{t=0}^{N-1}Prob(tau>t); root stopping is included. Since the branch masses and action-simplex equations are rational, each O_i is a polynomial over Q of degree <=N+1. No sampling-cost sign assumption occurs.

Let X be the finite Cartesian product of all full-history action simplexes and Y the product of all compressed-state action simplexes. Let F:X→R^4 and G:Y→R^4 be the above polynomial maps. All maps are continuous, and X,Y are compact. Every compressed behavioral policy is a particular full policy by copying its state action distribution to all member histories. Therefore G(Y)⊆F(X).

## 2. Theorem A — exact necessary-and-sufficient decision procedure

**Statement.** Universal behavioral four-vector preservation for the chosen quotient is equivalent to truth of the following rational first-order sentence over the reals:

    for all x:
      [ x in X  =>  exists y:
           (y in Y and F_1(x)=G_1(y) and F_2(x)=G_2(y)
                    and F_3(x)=G_3(y) and F_4(x)=G_4(y)) ].

This sentence is algorithmically decidable by real-closed-field quantifier elimination, for **every fixed finite positive rational tree, arbitrary fixed time-indexed readout, randomized stopping/decision policy, signed supporting coefficient choice, and root stopping**.

**Proof.** The action-simplex inequalities and equalities and the four equations are polynomial constraints with rational coefficients by Section 1. The sentence says exactly that F(X) is a subset of G(Y). The reverse inclusion was established above. Quantifier elimination for the first-order theory of real closed fields decides the truth of every such sentence. The assertion is effective decidability, not a claim of practical polynomial complexity; no CAD/QE computation has yet been executed in this research unit. QED.

**Theorem B — rational unsafe-policy witness.** If the quotient is unsafe under this criterion, there exists a rational full-history behavioral policy x* such that F(x*) is not achievable by any real compressed behavioral policy.

**Proof.** G(Y) is compact, hence closed. For any failing real x0, the distance from F(x0) to the compact G(Y) is positive. Continuity of F gives a relative-open neighborhood of x0 in X whose F-images remain outside G(Y). Rational points are dense in each finite simplex and hence in X. Choose rational x* in that neighborhood. QED.

This rationality conclusion concerns a full-policy counterexample, **not** rational matching coarse policies: rational polynomial equations can have only irrational real solutions.

## 3. Theorem C — what Bellman support and linear programs actually certify

Write D_F and D_S for the finite sets of four-vectors from full and compressed **deterministic** policy tables.

(1) F(X)=conv(D_F). Sampling independently an action at every full-history node realizes every full behavioral policy as a distribution over deterministic tables. Conversely, for an arbitrary distribution over full deterministic tables, condition the table distribution on reaching each observed history without earlier stopping. This yields a behavioral action distribution indexed by the full history. The conditioning uses the prior action choices only: its weights are the same for P and Q, because the history chance factor p_h or q_h cancels in the posterior over the random table. Thus the mixture's full stopping/decision law under both measures is recovered. This is the finite-tree perfect-recall construction.

(2) G(Y)⊆conv(D_S) and conv(G(Y))=conv(D_S). Pre-sampling action choices independently for each coarse time/state proves the first inclusion. Every deterministic table is itself a behavioral policy, proving the opposite convex-hull inclusion.

(3) Consequently, **convexified coarse fidelity** is exactly the rational polytope inclusion

    D_F subseteq conv(D_S).

This is decidable by a finite collection of rational LP membership problems, one for each full deterministic table. A failed LP produces a rational separating signed linear objective

    J(O)=A O_1+B O_2+C O_3+D O_4

with a strict rational gap. Conversely, success proves the mixed/convexified coarse policy class can match every full-policy four-vector if the initial persistent seed is permitted.

(4) **Caution for behavioral-only claims:** LP inclusion, equivalently equality of all signed Bellman support minima, establishes only equality with conv(G(Y)), not automatically equality with G(Y). Without a proof that G(Y) is convex, it is a logical error to replace the original for-all/there-exists sentence by the support test. Theorem A remains valid unconditionally. This is a necessary audit of the reduction step, **not** an allegation that any particular prior project theorem has already been disproved.

**Strong-lumpability sufficient case.** Suppose each state fiber has a fixed exact likelihood ratio and for each possible next state the Q-conditional transition probability is the same for all histories in the current fiber. Aggregate the Q-weighted history occupancy of any full strategy at every (time,state,action). Its incoming and outgoing mass obeys linear conservation with the common state transition kernel. Define a coarse behavioral action probability as the aggregated action mass divided by the aggregated state mass (choose arbitrary probabilities at zero-mass states). The induced Q occupancy and action masses agree by induction. Since the current L is constant in a fiber, the P masses there are L times the Q masses, and all four observables are preserved. Thus strong Q-lumpability supplies a genuine convex, linear occupation-flow model and makes the LP criterion valid for behavioral fidelity. This sufficient condition is not claimed necessary in general.

## 4. Theorem D — exact minimum deterministic residual search

Fix a typed baseline readout b_t(h), e.g. (t,L(h)). Enumerate the finitely many partitions refining the fibers of b at every time. For each candidate partition run the Theorem A decision procedure. The singleton-history partition is safe, so the passing set is nonempty. Minimize any explicitly computable partition cost: for example maximum per-time residual bit width

    max_t ceil(log2 max_b(number of quotient blocks inside baseline fiber b)),

or sum of state blocks. This is a finite exact algorithm, albeit potentially astronomical (partition enumeration plus quantifier elimination).

**Online implementation qualification.** A partition that can be read directly at a history is not automatically computable from past compressed state and newly observed symbol. To insist on a deterministic online update U_t(s,z), require right congruence: whenever two histories h,k have the same retained state and the same next symbol z is enabled from both, the extended histories hz,kz have the same next retained state. Check enabled-symbol interfaces for unequal alphabets. Restrict partition enumeration to such refinements. This condition is finite-checkable; singleton full-history states remain feasible. Abstract readout-minimality and online-residual-minimality must not be conflated.

## 5. Exact rational validation: seven-prefix N=2 toy

This is a regression for the method, not a replay of the predecessor's 32-leaf N=4 instance. Let P(a)=Q(a)=P(b)=Q(b)=1/2, and after a or b let Q(x)=Q(y)=1/2. For P let (x,y)|a=(3/4,1/4), while (x,y)|b=(1/2,1/2). Thus L_1(a)=L_1(b)=1 but the future L distributions differ. The quotient is (time,exact LR), and root stopping is allowed.

Take J=eP+eQ+(E_P tau+E_Q tau)/32. At t=1 the Q-normalized optimal stopping loss is H(1)=1; the best terminal expected losses on a and b are 3/4 and 1. A continuation from L=1 incurs cost 1/16. Thus

    V_full(a)=min(1,1/16+3/4)=13/16,
    V_full(b)=1,
    V_full(root)=min(1,1/16+(13/16+1)/2)=31/32.

A coarse policy must take one action at a and b. Its conditional terminal average is 7/8, hence

    V_coarse(t1)=min(1,1/16+7/8)=15/16,
    V_coarse(root)=min(1,1/16+15/16)=1.

The separation is exactly 1/32. The explicit full-history policy continues at root and a, stops deciding P at b, decides P after ax and Q after ay. It gives

    O_full = (1/8, 3/4, 3/2, 3/2),
    J(O_full)=31/32,

unachievable by ANY coarse real behavioral policy (its optimal J is 1). The local Python Fraction checker enumerated **all 432** full deterministic tables and **all 72** compressed deterministic tables, cross-checking independent Bellman values. All tests passed. These finite tests validate the toy, not Theorem A's general CAD implementation.

## 6. Background, limits, next work

External mathematical ingredients are **classical**, not claimed as first discoveries in the research literature: quantifier elimination in real closed fields (Tarski–Seidenberg; see https://logic.kastel.kit.edu/ap/course/dcd/13-arithmetic.pdf) and perfect-recall mixed/behavioral equivalence (Kuhn theorem; see https://plato.stanford.edu/archives/sum2018/entries/epistemic-game/index.html and https://arxiv.org/abs/2104.05249). The Enterprise Math research increment is the full quantifier-correct four-observable criterion, rational failure witness, mixed-vs-behavioral separation, and finite update-consistent residual optimization in the exact positive branch-mass semantics.

**Still open:** Run actual CAD/QE on a small positive rational N=3/N=4 hidden-kernel tree. Determine whether there is a time/LR-respecting four-observable example where the convexified LP test passes but the behavioral inclusion fails; if found, give a rational full policy and exact polynomial infeasibility certificate. Otherwise prove an additional structural convexity lemma. Compare minimal abstract readout and online update state counts. Native owner, formal CLAIM/Result, independent Driver review, and native dynamical transfer all remain **unverified/not done**.

