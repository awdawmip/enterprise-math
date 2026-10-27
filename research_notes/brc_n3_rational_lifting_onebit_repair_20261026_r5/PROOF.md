# N=3 BRC: constructive rational four-observer lifting and minimal one-bit repair

2026-10-26. **AUTHOR-LEVEL research, not independent Driver review or native Result.**
Pinned GLOBAL_KNOWLEDGE_V1: awdawmip/chatgpt-global-knowledge@67ddeba77aec9bff05039175463bda1af1397f73 (BOOTSTRAP, OPERATING_MANUAL, TASK role, P000 and ACTIVE worldview).
Pinned Enterprise Math read: awdawmip/enterprise-math@e8992339dbbb511df56bf9a22f5095fd6ea1e123 (PORTABLE_RESEARCH_PROTOCOL, current BRC/P000 sources, sharp universal region theorem).

## Precise model and reused premise

Time 1 has histories a,b with P=Q probability 1/2 and LR=1. At time 2 LR r in (1/2,1,3/2) has Q row q_a=(alpha,1-2alpha,alpha) after a, q_b=(beta,1-2beta,beta) after b; P row is r times the Q row. At time 3 finite strictly positive Q kernel mu_r(y) (dependent only on r) has sum_y y mu_r(y)=r and P kernel y mu_r(y)/r. A randomized policy may stop and decide P/Q at times 0,1,2; at 3 it must decide. Exactly four observers:
 O=(P(decide Q),Q(decide P),E_P tau,E_Q tau).

The already **author-proved, not Driver-admitted** sharp theorem in research_notes/brc_lr_n3_sharp_universal_region_20261026_r5/PROOF_SHARP_REGION.md states: for 0<alpha<=beta<1/2, every full-history randomized strategy has an equal-O time/LR-only strategy for *every* coherent terminal kernel iff beta<=3alpha and 3beta-alpha<=1. That theorem is an explicit antecedent here, not reproved or silently promoted.

## Theorem A. Rational constructive lifting in the safe region

For rational alpha,beta, terminal kernels and original policy probabilities satisfying the safe region, an equal-O LR-only policy with **rational** action probabilities is obtainable by finite rational Gaussian elimination and subset enumeration. Let m be the size of the union of terminal Y supports. Define BRC Q action flows z[t,s,a]>=0: 3 actions (stop P, stop Q, continue C) at t0 root and t1 LR=1, 3 actions at each of the three t2 values r, and 2 terminal actions at each distinct y. There are n=15+2m variables. Put qbar_r=(q_a(r)+q_b(r))/2.

Exact conservation:
 sum_a z[0,root,a]=1;
 sum_a z[1,1,a]=z[0,root,C];
 for each r: sum_a z[2,r,a]=qbar_r z[1,1,C];
 for each y: z[3,y,P]+z[3,y,Q]=sum_r mu_r(y) z[2,r,C].
Here z[t,s,P] means stopping and declaring P, etc. Together with four exact equations
 e_P=z[0,root,Q]+z[1,1,Q]+sum_r r z[2,r,Q]+sum_y y z[3,y,Q],
 e_Q=z[0,root,P]+z[1,1,P]+sum_r z[2,r,P]+sum_y z[3,y,P],
 E_P tau=z[0,root,C]+z[1,1,C]+sum_r r z[2,r,C],
 E_Q tau=z[0,root,C]+z[1,1,C]+sum_r z[2,r,C],
we obtain a rational nonnegative system A z=b with 9+m equations. The RHS b uses the *exact* four-vector of the history policy.

By the reused sharp safe-region theorem, this system is feasible over the reals. In a nonnegative orthant a nonempty finite polytope has a basic feasible solution; thus it has a rational solution with <=rank(A)<=9+m positive Q-action masses. Construct it without floating point: rational row-reduce A and b, enumerate invertible rank(A)-column subsets in a fixed order, solve each basis rationally, set other variables to zero, and retain the first nonnegative solution satisfying ALL original rows. Existence follows from the basic-feasible-solution argument. At a reachable node divide its action masses by their Q arrival sum; at zero-mass nodes choose arbitrary actions. Since each node's P arrival mass equals its LR times the Q arrival, the resulting rational policy reproduces all four observers.

A coarse certificate bit bound: after clearing denominators row-by-row let every integer matrix/RHS entry have absolute value <=M and rank k. Each basic-coordinate numerator and denominator is an order-k integer determinant bounded by k^(k/2) M^k (Hadamard); hence each needs <=1+ceil(k log2(M)+(k/2)log2(k)) bits. If the original rationals have at most B bits per numerator/denominator, rowwise products give log2 M=O((n+1)B), thus bit size O(k(nB+log k)) per coefficient. Enumeration may take exponentially many bases: no polynomial runtime is claimed.

## Theorem B. One-bit time-1 residual repairs *all* alpha,beta

For every 0<alpha,beta<1/2, independent of the sharp inequalities, and every r-only terminal kernel, a policy on the following compressed states exactly reproduces any full-history random policy's four observers:
 t0: root; t1: **h in {a,b}** (one branch bit);
 t2: only r (the bit is forgotten);
 t3: only y (the bit remains forgotten).

Proof (BRC two-measure disintegration). For each compressed fiber (t,s) and action u, sum original live Q path mass taking u to g[t,s,u]. Every history in a fiber shares an *exact* LR l(t,s) (1 for h at t1, r at t2, y at t3), so its corresponding P action-flow mass is exactly l(t,s) g[t,s,u]. Define compressed action probabilities g[t,s,u]/sum_v g[t,s,v] at reached fibers. Induct on time: t1's retained h determines q_h(r); t2's current r determines mu_r(y) independently of the forgotten h; t3 has no successor. Thus all Q and P action flows at every compressed state, and therefore the two error totals and both survival-time sums, agree. Rational data give rational g and policies. Ordered full path flows are **not** claimed identical.

Worst-case minimality for deterministic state quotients: merging a and b at t1, while allowing only exact r at t2 and y at t3, is exactly the LR-only state compression. Outside the sharp region the published rational witnesses establish O sets differ. Hence any deterministic universally adequate time-1 quotient must distinguish at least two states. The single a/b bit is sufficient. This is only a lower bound for the declared horizon, policy architecture and four observers, not for arbitrary future operations, soft random encodings or native BRC spatial states.

## New exact rational lifting certificate

Take alpha=1/4, beta=1/3 (safe). Terminal alphabet Y=(1/4,1,2):
 mu_(1/2)=(5/7,1/4,1/28);
 mu_1=(3/7,1/4,9/28);
 mu_(3/2)=(1/7,1/4,17/28).
All Q and induced P probabilities are strictly positive and normalized with conditional LR mean r.

A rational full-history strategy randomizing differently at a,b and then depending jointly on h,r,y is specified in LOCAL_AUTHOR_REPRODUCTION.md, with its full source in local author research bundle. Direct ordered-history Fraction summation yields
 O_full=(429887/806400,378989/806400,13733/9600,20519/14400).
The compressed feasibility system has 21 nonnegative variables, 12 exact equations and rank 12. An exploratory floating-point LP located a 12-column support; exact rational solving then produced these **verified Q action masses** (all unlisted entries zero):
 z[0,root,P]=50293/1612800; z[0,root,C]=1562507/1612800;
 z[1,1,Q]=422459/806400; z[1,1,C]=717589/1612800;
 z[2,1/2,P]=717589/5529600; z[2,1,P]=717589/3870720;
 z[2,3/2,P]=4352659/38707200; z[2,3/2,Q]=619/100800; z[2,3/2,C]=161/14400;
 z[3,1/4,P]=23/14400; z[3,1,P]=161/57600; z[3,2,P]=391/57600.
The portable VERIFY_CERT.py checks every conservation equation, all four fractions and nonnegativity using Fraction only, without needing the exploratory solver. The full independent author script also recomputed the compressed randomized policy stage-by-stage: both exact approaches passed. At time 1 the compressed policy declares Q with probability 844918/1562507 and continues with probability 717589/1562507.

## Reused exact unsafe gap and minimal repair witness

From the predecessor's sharp theorem, alpha=1/12, beta=1/3, A=B=2,C=0,D=5/48 and Q terminal leaves r±1/100 (equal weights) give V_full=191/96 and V_LR=2, gap 1/96. One explicit one-bit policy continues at root; at time 1 stops/declares P after a but continues after b; at time 2 stops/declares Q for r=1/2 and P for r=1,3/2. Its exact four-vector is (1/12,5/6,3/2,3/2), and J=191/96. This supplies an exact necessity/repair witness. Its Bellman optimality is **reused** from the predecessor, not a new independent review.

## Limits, sources and next research question

Proof A's all-policy premise relies on the prior author-level sharp theorem; its new constructive rational algorithm is proved conditionally on that theorem. Finite verification checks one rational instance, not universal coverage. Proof B is a direct flow-disintegration argument. The results concern strictly specified external finite Bayesian positive-mass BRC carriers and four observers, not a proof of P000/X6/Heartbeat dynamics. Typed path/provenance can be erased only for this horizon/future-operation contract. No native active Owner, CLAIM, frozen Result, independent Driver review, Lean proof or original-literature priority is claimed.

Next: sharpen bit-complexity and rational synthesis algorithms near region boundaries; investigate N>=4 hidden-history-dependent terminal kernels and the minimal time-2 residual; seek a separately certified X6 observer-preserving bridge before native promotion.
