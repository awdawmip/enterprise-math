# EC48O — Sharp memory cardinality for three-stage positive BRC observers

**Status:** AUTHOR_PROVED / EXACT_COMPUTATION_PASS / UNREVIEWED / NOT_ADMITTED. Author-side portable research; no active native CLAIM or Driver approval is represented. Read pins: GLOBAL_KNOWLEDGE_V1 main@ba55fc1478539fb270388d003f1b01d7de36b026; Enterprise Math main@f47d92f62dcaf33ecb385805379b450a40fa5534. Native task-owner query returned CONTROL_QUOTA; GitHub researcher login awdawmip. This is an auxiliary two-source finite positive BRC theorem, not an X6 native dynamics claim.

## Exact model and theorem

At time 1 observe one of k>=1 histories h; if continuing, at time 2 observe x; if continuing again, at time 3 observe terminal y and accept/reject. Finite P,Q leaf masses p(h,x,y),q(h,x,y) are strictly positive and each source mass sums to one. The recorded vector is O=(alpha,beta,tau_P,tau_Q), where alpha=P(accept), beta=Q(accept), tau_P=E_P(T), tau_Q=E_Q(T).

The memory observer has m persistent register **states**. At time 1 the encoder sees h and writes its register before the action. At time 2 the encoder sees old register, x, and current joint likelihood ratio p(h,x)/q(h,x), and rewrites before the action. Each action sees only (time, current joint likelihood ratio, current register), and terminal accept/reject likewise uses the joint LR and register. Private source-independent behavioral randomness is allowed; there is no persistent public/common seed and no hidden access to discarded h. Write S_m and S_F for raw achievable O sets, and C_3(k)=min{m>=1: S_m(P,Q)=S_F(P,Q) for every such k-history tree}.

**Theorem (EC48O):** for all integers k>=1, C_3(k)=max(k,2). In fact the lower-bound examples separate support functions and therefore convex hulls.

## Upper bound — full raw four-vector reconstruction

Let t_h=P(continue at t1|h) (strategy probability, common to sources), a_h=P(stop and accept at t1|h), u_hx=P(continue at t2|h,x), b_hx=P(stop and accept at t2|h,x), and z_hxy=P(accept at t3|h,x,y). The constraints are 0<=a_h<=1-t_h, 0<=b_hx<=1-u_hx and 0<=z_hxy<=1. With prefix source masses p_h,p_hx and analogously q:

alpha = sum_h p_h a_h + sum_hx p_hx t_h b_hx + sum_hxy p_hxy t_h u_hx z_hxy;
beta is the same expression replacing p by q.
tau_P = 1 + sum_h p_h t_h + sum_hx p_hx t_h u_hx, and likewise tau_Q.

For m>=max(k,2), encode each h injectively at time 1 and reproduce its t1 decision/stop acceptance. At t2, before the action, rewrite the register to flag 1 (continue) with probability u_hx, otherwise 0 (stop). All t2 histories reaching a stop with joint LR r=p_hx/q_hx share the acceptance probability

eta_r = [sum_{hx:LR=r} q_hx t_h b_hx] / [sum_{hx:LR=r} q_hx t_h(1-u_hx)]

when denominator>0, and 0 otherwise. Since numerator<=denominator, eta_r is admissible, and fiber identity p_hx=r q_hx preserves *both* P and Q stop-accept masses. At t3, accept at ratio s=p_hxy/q_hxy with

theta_s = [sum_{hxy:LR=s} q_hxy t_h u_hx z_hxy] / [sum_{hxy:LR=s} q_hxy t_h u_hx]

(or zero when denominator zero). Again the ratio fiber identity preserves both accept masses. Both continuation masses at t1 and t2 already match, so tau_P,tau_Q match. Thus S_F subset S_m, and reverse inclusion is simulation by the full observer. This is **raw** region equality, not merely convex hull equality. The two-state flag is needed to implement an arbitrary t2 stop/continue decision.

## Uniform k>=2 lower bound by distinct branch signatures

Put n=ceil(log2 k); choose distinct subsets T_h of X={0,...,n-1}, h=0,...,k-1, using binary masks 0,...,k-1. Exactly one T_0 is empty. Every (h,x) has P=Q prefix mass 1/(kn). If x not in T_h, use one terminal leaf with p=q=1/(kn). If x in T_h, use two terminal leaves +/- with (p+,q+,p-,q-)=(3,1,1,3)/(4kn). All existing masses are strictly positive, and both P and Q sums equal 1; every joint LR at t1 and t2 is exactly 1. Terminal ratios are 3,1/3,1.

For the linear functional J_c=alpha-beta-c(tau_P+tau_Q), 0<c<1/[4(n+1)], the terminal optimal action accepts + only. Informative t2 continuation has net gain g=(1/2-2c)/(kn)>0; neutral continuation incurs loss d=2c/(kn)>0. Continuing h at t1 incurs cost 2c/k. Hence h=0 uniquely stops at t1, while every h>0 uniquely continues at t1 and t2 precisely for x in T_h, with positive gain R_h=|T_h|g-2c/k >= r_min=(1/2-2c(n+1))/(kn)>0. The k optimal action signatures S, C(T_1),...,C(T_{k-1}) are distinct.

Any deterministic m-state controller gives each initial state s just one fixed action signature: all histories mapped to s have equal time-1 LR=1, and at t2 for equal x they have equal LR=1 and the same (s,x) update/action kernel. Therefore m<k forces a wrong stop/continue action for at least one positive-mass history and a support loss at least

epsilon=min{2c/k, r_min, 2c/(kn), g}>0.

The bound includes stopping a useful history, continuing an empty one, over-continuing a neutral x or skipping informative x. Time-indexed behavioral stochastic kernels appear at most once on each trajectory, so expected J_c is multi-affine in the finite list of stochastic kernels; coordinatewise replacement by deterministic simplex vertices cannot decrease the linear expectation. Every randomized controller is thus dominated in J_c by a deterministic one; the strict support gap holds for all allowed private randomness, without claiming raw-set convexity. Consequently C_3(k)>=k for every k>=2.

## k=1 and the 12-leaf exact k=4 witness

For k=1, let two equally likely t2 symbols have LR=1, with informative +/- on x0 with masses (3,1,1,3)/8 and neutral x1 with p=q=1/2. At c=1/32, full observer continues at t1, continues x0 and stops x1, giving V_F=3/32. One-state register cannot transmit x and attains V_1=1/16 (enumerate its four stop/continue schedules), a gap of 1/32. Upper bound m=2 closes k=1.

For k=4 use n=2, T_A=empty,T_B={x0},T_C={x1},T_D={x0,x1}; the P,Q masses as numerators/32 are:
A x0 0:(4,4); A x1 0:(4,4);
B x0 +:(3,1), -:(1,3); B x1 0:(4,4);
C x0 0:(4,4); C x1 +:(3,1), -:(1,3);
D x0 +:(3,1), -:(1,3); D x1 +:(3,1), -:(1,3).
There are 12 strictly positive terminal leaves. For every real 0<c<1/16, full strategy stops A, continues B,C,D, and extends precisely four informative hx branches:
O_F=(3/8,1/8,9/4,9/4), V_F=1/4-9c/2.
With three states the general epsilon is c/4 on this interval, and it is attained by merging B,D (continue both x), retaining C (continue x1 only) and A (stop); B x1 incurs precisely one neutral extra continuation:
O_3=(3/8,1/8,19/8,19/8), V_3=1/4-19c/4, so V_F-V_3=c/4.
At c=1/32: V_F=7/64, V_3=13/128, gap=1/128. This is a rigorous *support* obstruction and therefore a difference of raw/convexified observation regions.

## Validation, provenance and next question

The local complete author-side verifier uses Python fractions.Fraction and exhausts 3^4*2^3*2^6=41472 k4 three-state deterministic effective controllers, 2^4*2^2*2^4=1024 two-state controllers, six rational values of c, four k1 controllers, and positive parameter constructions k=2,...,12. Assertions and repeated output checks pass. The finite enumeration checks the witness, while the universal theorem rests on the proof above. BRC reuse: two positive source-labelled path measures, branch provenance and joint-LR fibers are retained until the declared four-output, three-stage future operations admit an exact quotient. Distinct T_h histories are structural residuals that cannot be erased at less than k states. No evidence of native X6 physical embedding, heartbeat propagation, formal Lean checking or independent Driver acceptance is implied.

**EC48P**: Investigate whether at horizon 4 fixed k=1 or 2 needs more than max(k,2) states with the same pre-action register update and joint-LR observer. Prove a new lower bound with a strictly positive rational tree and exact support certificate, or prove a general raw-region compression theorem. Retain declared stage/time semantics and all source-labelled branch masses.