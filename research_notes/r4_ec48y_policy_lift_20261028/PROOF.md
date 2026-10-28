# EC48Y: exact dual-source occupancy certificates for finite-register observation

Date: 2026-10-28 Asia/Shanghai. Author-side TASK_RESEARCH, local identity R4-EC48Y-20261028-LOCAL. Scientific status AUTHOR_PROVED / EXACT_FINITE_CHECK_PASS / UNREVIEWED / NOT_ADMITTED. Directly continues EC48X PR #1607, commit 6eabe0500d921c52e534a665e25f445eceb7a5d3. The exact previous prompt is its NEXT_TASK.md.

## Mathematical model and source boundary

This note studies an AUXILIARY finite, strictly positive, rational, dual-source P/Q probability-branch stopping model. It is not a signed-amplitude BRC/Shor computation or a native X6 heartbeat experiment. P000 and the ACTIVE six-dimensional spatial Cell plus separately typed time worldview remain unchanged. Transfer requires an explicit typed native-state/readout/path/future-operation homomorphism, not analogy.

At decision times t=1,...,d let H_t be the finite set of full controlled observable histories, including earlier actions. Source-neutral behavioral controls have actions acc (stop and accept), rej (stop and reject), and cont (continue, unavailable at d). No hidden persistent random seed exists outside the stated register. Each fine P/Q branch is strictly positive and rational. At any history h, define full joint LR L_t(h)=P(h)/Q(h)>0 before adding the source-neutral policy action factors. Hence every allowed fine continuation h->h' satisfies K_P(h'|h,cont)=L_{t+1}(h') K_Q(h'|h,cont)/L_t(h). The compressed controller has register r in R, fixed deterministic and source-neutral causal updater u(r,a,new sensor,new full LR), and reads y_t=(t,r,current sensor,L_t(h)); L is the fine-history LR oracle, not quotient-only LR. Initial register is implementable from the initial permitted sensor. A full observer can condition on h. Define O=(alpha,beta,E_PT,E_QT), alpha=P(acc), beta=Q(acc).

## Theorem Y1. Exact necessary-and-sufficient polynomial occupancy test for one fixed updater

A vector O is achievable by a single source-neutral compressed behavioral policy if and only if there exist real nonnegative Q-live masses x_t(h,r) and Q-action masses z_t(h,r,a) satisfying ALL of these finite rational polynomial constraints:

(1) x_1(h,r)=Q(H_1=h) times the indicator of the authorized initial register; sum_a z_t(h,r,a)=x_t(h,r), with z>=0.

(2) For continuation to t+1,
x_{t+1}(h',r')=sum_{h,r} z_t(h,r,cont) K_Q(h'|h,cont) 1{u(r,cont,o(h'),L(h'))=r'}.
Here h' ranges over extensions of the recorded controlled h and zero otherwise.

(3) For all i=(h,r),j=(k,r') in the SAME readout y_t and each action a, impose the quadratic rank-one minors z_t(i,a)x_t(j)-z_t(j,a)x_t(i)=0.

(4) Set alpha=sum_{t,h,r} L_t(h) z_t(h,r,acc); beta=sum z_t(h,r,acc); E_PT=sum_{t,h,r} L_t(h)x_t(h,r); E_QT=sum x_t(h,r).

Proof, forward: For any compressed policy pi_t(a|y), Q occupancy obeys (1)-(2), with z=x pi. The same pi on each readout fiber makes every minor in (3) zero. Since the source-neutral policy factors cancel in fine LR, the P-live and P-action masses are L(h)x and L(h)z. Stopped acceptance gives the first two readouts. For finite integer-valued T, E_s T=sum_t Pr_s(T>=t), which equals the corresponding live-mass sum, giving (4).

Proof, reverse: Fix a solution. For each observed fiber y with any x_i>0 choose such i and define pi_t(a|y)=z_i(a)/x_i. Each pi is a probability vector. All other positive-mass cells j on this fiber have the SAME pi since z_i(a)x_j=z_j(a)x_i. If x_j=0 its row sum and positivity force all z_j(a)=0. On a fiber with no live mass choose an arbitrary valid policy. Induction through (2) proves that this single source-neutral pi realizes the entire Q fine/register occupation. Its P occupation is L(h) times Q occupation by the fine LR identity, source-neutral action/update and induction, so (4) is reproduced exactly. No inaccessible fine history is consulted by pi. QED.

Consequence: For a finite rational model, fixed updater and behavioral finite-register class, raw S_m is a projection of a rational semialgebraic set; it is semialgebraic by Tarski-Seidenberg. Membership of a specified real algebraic target O is decidable in principle by real-closed-field quantifier elimination. When allowed deterministic causal updaters form a finite collection, their union is also semialgebraic. The full-history raw region has the same finite representation with unrestricted fine-history action choices; thus raw S_full subset S_m, and equality of whole raw regions, can be formulated as finite forall/exists real polynomial sentences and decided in principle. This is a logical decidability statement: no general quantifier-elimination program was run, and no universal rational witness or practical complexity bound is claimed. Merely imposing independent P and Q linear flows or dropping (3) is insufficient.

## Theorem Y2. Exact rational LP in the controlled-Markov LR quotient subclass

Add the hypothesis that after the fixed register update the readout y is a controlled-Markov quotient under Q: each K_Q(y'|y,cont) is rational and independent of erased fine history. L_t is constant on each y. Then the exact original four-coordinate region equals the projection of the LINEAR rational occupancy system

x_1(y)=Q(Y_1=y); z_t(y,a)>=0; sum_a z_t(y,a)=x_t(y);
x_{t+1}(y')=sum_y z_t(y,cont) K_Q(y'|y,cont);
alpha=sum L_t(y)z_t(y,acc);
beta=sum z_t(y,acc);
E_PT=sum L_t(y)x_t(y);
E_QT=sum x_t(y).

Proof: Every source-neutral controller satisfies the Q flow. Conversely let a feasible x,z be given. pi_t(a|y)=z_t(y,a)/x_t(y) on positive x, arbitrary on zero x, induces exactly the Q quotient flow because transitions are controlled-Markov. The fine LR identity makes the P quotient kernel K_P(y'|y,a)=[L_{t+1}(y')/L_t(y)] K_Q(y'|y,a), hence P occupations are Lx and P action occupations Lz. Therefore pi attains all four readouts exactly. The finite LP polytope has rational coefficients and bounds; with a rational target, any feasible nonempty rational polytope contains a rational basic feasible point, and the corresponding pi is rational after normalization. Infeasibility has a rational Farkas dual certificate. QED. This specializes classical occupation-measure LP methods; no general novelty over constrained MDP theory is asserted.

### Concrete LP witness and false independent-source certificate

At t=1 only one state (P=Q=1,L=1) exists. Continuing reveals Z=0 or1 at t=2 with Q=(3/4,1/4), P=(1/4,3/4), L=(1/3,3). Choose initial (acc,rej,cont)=(1/8,3/8,1/2), and at t=2 acceptance given Z=(1/3,2/3). Exact Q occupancy:
x_1=1, z_1=(1/8,3/8,1/2), x_2=(3/8,1/8), z_2(acc)=(1/8,1/12).
The reconstructed common policy gives O=(5/12,1/3,3/2,3/2).

Every accepting leaf has P/Q <=3, hence every COMMON source-neutral policy satisfies alpha-3 beta<=0. Candidate O*=(3/4,1/8,3/2,3/2) violates by exactly 3/8. Nevertheless its P acceptance/time pair is realizable by a P-only policy with initial acc=3/8,cont=1/2 and terminal accept iff Z=1; the Q acceptance/time pair is realizable by a DIFFERENT Q-only policy with initial acc=1/8,cont=1/2 and always reject terminal. This demonstrates why separately feasible dual-source flows do NOT certify one common policy. The O* example is not asserted to be a full-history-vs-compressed raw gap.

## Y3. Four positive observation leaves certify a non-Markov rank-one obstruction

At an earlier readout H is observed, P(H=0)=P(H=1)=Q(H=0)=Q(H=1)=1/2, then a one-register controller forgets H before its t=1 choice (there is no intervening decision). At t=1 the current sensor is constant and exact full LR is 1, for both H. If it continues, at t=2 the observation is Z and full LR and it must stop. The strictly positive P,Q joint leaf masses are:
H0Z1: (3/8,1/8), L=3;
H0Z0: (1/8,3/8), L=1/3;
H1Z1: (1/4,1/4), L=1;
H1Z0: (1/4,1/4), L=1.
Each source mass sums to one.

A full observer continues iff H=0 and accepts iff Z=1, attaining O_full=(3/8,1/8,3/2,3/2). Its Q initial occupancy and continuation action masses are x(H0)=x(H1)=1/2, z(H0,cont)=1/2, z(H1,cont)=0. The ONE-register rank-one minor z(H0,cont)x(H1)-z(H1,cont)x(H0)=1/4, whereas Y1 requires zero.

For every one-register controller, the t=1 continuation probability c is identical in both H histories because neither current sensor nor fine LR distinguishes them. Its stop/accept contribution cancels in alpha-beta; from the continuing leaves, only H0Z1 has positive P-Q mass (equal to 1/4). Consequently alpha-beta<=c/4=(E_QT-1)/4, valid for ALL source-neutral behavioral controllers, regardless of terminal readout choices. At O_full, alpha-beta=1/4 while (E_QT-1)/4=1/8: the EXACT raw-region separation gap is 1/8. The full fine-history LR at t=2 cannot restore the information needed to decide continuation at t=1. Removing rank-one equations makes the forbidden fine policy satisfy linear history-flow equations.

This minimal rank-one witness is related to the EC48V/W information-value examples and is used here to certify the new mathematical occupancy formulation; it is not claimed as an externally novel information principle.

## Validation, provenance and boundary

Actual executed independent Python stdlib Fraction checks: 1125 Markov quotient grid controllers, 720 deterministic-terminal one-register grid controllers, 1215 fractional-terminal one-register grid controllers (3060 grid cases), plus positive mass normalization, four-vector witness reconstruction, LR, rank-one minor, 3/8 dual violation and 1/8 raw gap. All exact checks passed. General Y1/Y2 follows from the proofs; no general real quantifier elimination was executed.

GLOBAL_KNOWLEDGE_V1 frozen main@575b91106229454fe114ee1e2c38c548f689dfab; Enterprise Math control main@359d3ecde05f3679f909ded1703f4655ad359eac. The owner inventory returned CONTROL_QUOTA; service status reported research_authority_granted=false. No native CLAIM, RA, formal Result or independent Driver review is inferred. A previously platform-denied RA write was not repeated. The model is positive-rational auxiliary BRC only; native X6/phase/physical attribution remains a separate typed proof obligation.

Next EC48Z: determine structural conditions under which the quadratic rank-one constraints reduce exactly to an LP despite nonlumpable history; explore rational-output instances with exclusively irrational policy lifts. See NEXT_TASK.md.
