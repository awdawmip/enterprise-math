# EC48O — Sharp three-stage BRC memory capacity for every first-stage history count

2026-10-27; independent author-side portable research. **AUTHOR_PROVED / EXACT_COMPUTATION_PASS / UNREVIEWED / NOT_ADMITTED.** Native ownership/CLAIM not obtained (owner query: CONTROL_QUOTA). No foundation, X6 dynamics, or physical calibration claim.

Source read snapshot: GLOBAL_KNOWLEDGE_V1 main@e4a50e129afcb9385b416dc05f9ebd52a11ef6df; Enterprise Math main@9ea3a32edc6d8b286518e19a44316ac08256cbeb. Exact applicable sources include the account bootstrap/manual, project AGENTS, P000, ACTIVE X6 and joint-relation observer contracts, and docs/PORTABLE_RESEARCH_PROTOCOL.md. Predecessor EC48N is author-side unreviewed, not a native Result. BRC use: positive rational labeled branches, exact joint likelihood-ratio fibers; no signed-amplitude cancellation.

## Theorem and typed semantics

A strictly positive finite two-source experiment has k>=1 first-stage histories h, stage-two symbols x, terminal symbols y, all *existing* leaf masses p_hxy,q_hxy>0 with separate totals one. Stop/accept/reject at stages 1,2; forced accept/reject at stage 3. Time is a separately typed finite decision index. The observer outputs O=(alpha,beta,tau_P,tau_Q)=(P(accept),Q(accept),E_P T,E_Q T). The full observer sees (h,x,y); an m-state observer may encode h into a register at stage 1, update its register BEFORE the stage-two action from only (old register,x,current JOINT prefix likelihood ratio), and decide from (time,updated register,current joint likelihood ratio). Terminal decoder sees register and final joint likelihood ratio. All kernels may use source-independent private randomization; no persistent shared seed or discarded-history access. S_m,S_F are original attainable four-coordinate sets, not just convex hulls.

**For every integer k>=1, the least m guaranteeing S_m=S_F for all experiments in this class is M*(k)=max(k,2).** For k>=2 an explicit positive rational model satisfies, for every real 0<c<1/10 and J_c=alpha-beta-c(tau_P+tau_Q),

V_F - V_(k-1) = c/[2k ceil(log2 k)] > 0.

A separate positive three-leaf k=1 model requires two states. Thus the worst-case minimum conventional binary memory is ceil(log2(max(k,2))) bits. The support gap separates even convex hulls and therefore also raw sets; the upper result is genuinely about entire raw sets.

## Upper bound, including the nonconvex original region

Fix any full-history randomized behavioral policy. Write t_h=Pr(continue at 1|h), a_h=Pr(stop and accept at 1|h), u_hx=Pr(continue at 2|h,x), b_hx=Pr(stop and accept at 2|h,x), z_hxy=Pr(accept at terminal|h,x,y), with 0<=a_h<=1-t_h and 0<=b_hx<=1-u_hx. Exactly:

alpha=SUM_h p_h a_h+SUM_hx p_hx t_h b_hx+SUM_hxy p_hxy t_h u_hx z_hxy;
beta=identical expression with q;
tau_P=1+SUM_h p_h t_h+SUM_hx p_hx t_h u_hx;
tau_Q=1+SUM_h q_h t_h+SUM_hx q_hx t_h u_hx.

With m=max(k,2) encode h injectively at stage 1 and reproduce its first decision. Stage two recovers (h,x), writes register 1 with probability u_hx and 0 otherwise, continuing iff 1. For each current JOINT ratio r=p_hx/q_hx define D_r=SUM_(hx:ratio=r) q_hx t_h(1-u_hx), A_r=SUM_(hx:ratio=r) q_hx t_h b_hx and eta_r=A_r/D_r when D_r>0, zero otherwise. On register=0 stop and accept with probability eta_r. As 0<=A_r<=D_r, this is legal. It exactly matches the stage-two Q acceptance mass A_r; on the same fiber p_hx=r q_hx, so it also matches P acceptance mass r A_r.

At the terminal for each JOINT ratio s=p_hxy/q_hxy define E_s=SUM_(hxy:ratio=s)q_hxy t_h u_hx and B_s=SUM_(hxy:ratio=s)q_hxy t_h u_hx z_hxy. Accept with theta_s=B_s/E_s for positive E_s, zero otherwise. Q mass B_s and P mass s B_s are exact. Per-prefix continuation t_h and u_hx also preserve both stop-time expectations. Therefore every O in S_F belongs to S_m; converse holds by full-history simulation of the stochastic register. This is policy-by-policy four-observable fiber preservation, not pathwise equivalence, X6 quotient safety or an assertion about other future operations.

## Exact rational lower-bound family for all k>=2

Put s=ceil(log2 k). Choose k distinct binary strings w_h of length s including 0^s and e_1 (one in position 1). Let mu=1/(4ks). At time 1, P(h)=Q(h)=1/k. Stage-two symbol set is {1,...,s,+,-}, shared across all histories. For each h and each j:

- Set joint p_hj=q_hj=mu.
- If w_h[j]=0, use ONE terminal neutral leaf (p,q)=(mu,mu).
- If w_h[j]=1, use two leaves up/down: (p_up,q_up)=(3mu/4,mu/4), (p_down,q_down)=(mu/4,3mu/4).

For each h, the private '+' stage-two branch has one leaf (p,q)=(1/(2k),1/(4k)); private '-' has one leaf (p,q)=(1/(4k),1/(2k)). Per history both P and Q total s mu+3/(4k)=1/k; every existing leaf mass is strictly positive rational. All first-stage and shared-stage-two joint ratios equal 1. Terminal informative ratios are 3 and 1/3, neutral ratio 1; private stage-two ratios 2 and 1/2.

For 0<c<1/10, a full-history Bellman optimum continues ALL first histories, stops/accepts on '+', stops/rejects on '-', and at shared j continues precisely for bits w_h[j]=1, accepting terminal up only. Express gains relative to compulsory baseline -2c:

G0=(1/4-2c)/k is the guaranteed per-history gain from first-stage continuation/private '+', even with no informative j;
G1=mu(1/2-2c) is the positive gain on an informative shared j when continuing to the terminal;
d=2c mu=c/(2ks) is the loss from unnecessarily continuing a neutral shared j.

Here G1>d because mu(1/2-4c)>0 for c<1/8, and G0>d because (1/4-2c-c/(2s))/k>0 for c<1/10 and s>=1. Put B=SUM_h SUM_j w_h[j] (the number of informative incidences). Exact full support is

V_F=-2c+kG0+B G1=1/4-4c+B mu(1/2-2c).

For a deterministic (k-1)-state controller, either some h stops at t=1 (losing >=G0>d against its full independent optimum), or all k continue and pigeonhole forces two distinct binary words to share a register message. These words differ at some shared j; both have the same observed j, joint ratio 1 and old register, hence the stage-two update/action must be identical. Stopping loses G1 on the informative history; continuing loses d on the neutral history. Both losses >=d. No terminal decoder can beat full-history likelihood-ratio-optimal terminal acceptance. Thus every deterministic controller loses >=d.

The same bound covers arbitrary allowed private randomization. With finite horizon and stage-indexed independent stochastic kernel rows, the fixed *linear objective* is separately affine in every row: each trajectory invokes each row at most once. Fixing all other rows and selecting a simplex vertex never lowers the objective; sequentially doing so produces a deterministic optimum. This proves an extreme-point reduction for SUPPORT maximization only, not raw-set convexity or availability of a common random seed.

Merge only the adjacent histories 0^s and e_1 into one message, keep all other h separate, continue all at time 1 and choose full-optimal actions thereafter except that at shared j=1 the merged message continues for both, unnecessarily continuing just one neutral branch 0^s. Exact loss is d, establishing

V_(k-1)=V_F-d,   V_F-V_(k-1)=c/(2ks),   0<c<1/10.

For all k>=2, fewer than k register states cannot preserve even the support functional; the upper construction proves k suffice for the *entire raw region*.

## k=1 needs two states

With one first-stage history and two stage-two symbols x=0,1 having joint masses P=Q=1/2 each, set x=0 to a single neutral terminal leaf (1/2,1/2), while x=1 has terminal up=(3/8,1/8), down=(1/8,3/8). All three leaves positive and stage-two ratios both 1. For c=1/32 the full controller continues at time 1, stops on neutral x=0, continues on informative x=1 and accepts up, with V_F=1/4-5c=3/32. A ONE-state controller cannot transmit x; its complete deterministic options yield

V_1=max(-2c, -4c, 1/4-6c)=1/16.

So gap=1/32; 2 states suffice by the earlier upper factorization. Therefore M*(1)=2 and M*(k)=max(k,2) is sharp for all k>=1.

## Explicit k=4 witness and checker scope

For k=4, s=2, codes A=00,B=01,C=10,D=11 and mu=1/32. All masses use denominator 128. For each h the private terminal '+' and '-' leaves have respectively (P,Q) numerators (16,8) and (8,16). Each shared label x=0,1 has a single neutral (4,4) leaf when its bit is 0, or terminal up (3,1) and down (1,3) when bit is 1. There are exactly 20 strictly positive leaves, with P(h)=Q(h)=1/4. At c=1/16,

O_full=(19/32,9/32,17/8,17/8),    V_full=3/64=12/256,
O_3=(19/32,9/32,69/32,69/32),    V_3=11/256,
gap=1/256.

The three-state witness merges A and B, continuing both at shared x=1; it incurs exactly one unnecessary neutral time-three continuation. The executable exact-Fraction verifier examines ALL 16,384 three-state deterministic normal forms (for each of c=1/32, 1/16, 1/10; total 49,152). Normal-form completeness follows because stage-one ratio 1 makes stop acceptance indifferent for J, the private x=2/3 leaves have no terminal information and optimally stop accept/reject, and shared LR=1 makes stage-two stop acceptance indifferent; at terminal, accepting iff final joint ratio>1 is optimal. Its output includes the exact four-coordinate witness, P/Q normalization, and constructive checks for k=2..32 and the k=1 three-leaf model. The real-c and all-k theorem rests on the analytic argument above, not extrapolation.

## Boundaries, evidence and continuation

This theorem concerns only the stated auxiliary finite positive BRC observer, its four readouts and time-three horizon. State counts encode historical control profiles and are not added native spatial dimensions. The fixed P000 ontology remains a six-axis discrete X6 Cell space plus separately typed time; no native-state/finite-experiment map preserving jointly observed relations and allowed X6 updates is established. Finite support separation cannot alone establish an empirical physical law or automatically generalize to extra readouts/horizons. Independent mathematical review and external prior-art check are outstanding; native Activity/Result/Driver admission require actual authorization.

Next unit EC48P: determine sharp memory needed for the FOUR-STAGE original region with k=1 and the same update/readout semantics; construct a positive rational support separation for two states or prove an original-region factorization; then audit the native X6 bridge explicitly.