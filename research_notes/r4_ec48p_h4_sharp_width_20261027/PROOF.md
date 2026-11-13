# EC48P — Sharp horizon-four BRC memory width theorem

2026-10-27 · TASK_RESEARCH independent author-side mathematics. Status: AUTHOR_PROVED / EXACT_COMPUTATION_PASS / UNREVIEWED / NOT_ADMITTED. No native Result, CLAIM, independent review, or X6 physical assertion.

Verified source pins for this derivation: GLOBAL_KNOWLEDGE_V1 main@5757eed6a2acb37dffe2f53363bcb27e2c40a3bb; Enterprise Math main@88d3f0f6f1bface54cf6bef9eba6177c8326afab. P000 and ACTIVE native X6 worldview preserved. Scientific predecessor: EC48O, commit 20eb4f35105908f403d631608657d7973bd604ee, PR #1578 (unreviewed author-side theorem). BRC reuse: positive rational branch labels, joint-likelihood-ratio fiber aggregation and the exact EC48O construction. Auxiliary source-conditional probability experiments are not native spatial X6 states.

## Definitions and precise new theorem

Finite two-source strictly positive P/Q stopping tree. Times t=1,2,3 allow stop/accept/reject; terminal t=4 forces accept/reject. First stage has a SINGLE uninformative root, stage two exactly k>=1 possible observable signals h, stage three signals j and terminal signals y arbitrary finite. Full observer remembers (h,j,y). An m-state observer updates its register BEFORE each action, using only old register, current signal, time and CURRENT JOINT PREFIX likelihood ratio P(prefix)/Q(prefix). Terminal acceptance sees the register and terminal joint likelihood ratio. Private randomization is source-independent; no public common seed, hidden path access, or a priori guarantee that likelihood ratio uniquely identifies path.

For O=(alpha,beta,tau_P,tau_Q)=(P accept,Q accept,E_PT,E_QT) let S_F and S_m denote RAW four-coordinate sets, with V(c)=max[alpha-beta-c(tau_P+tau_Q)].

**Theorem EC48P.** The sharp worst-case memory state count for all such horizon-four experiments with stage-two width k is

    M*(4,k) = max(k,2)   (every integer k>=1).

The upper equality is S_{max(k,2)}=S_F as RAW sets, not only convex hulls. For every k>=2 there is a positive rational model attaining this cardinality lower bound. Put s=ceil(log_2(k)), mu=1/(4ks), choose distinct s-bit words w_h including 0^s and e_1, and B=sum_{h,j}w_h[j]. For ALL REAL 0<c<=1/16 its exact support values satisfy

    V_F = 1/4 - 6c + B*mu*(1/2-2c),
    V_(k-1) = V_F - c/(2ks);
    strict gap = c/(2ks) > 0.

Thus with unrestricted intermediate branching, no uniform finite memory budget works at horizon four even with one stage-one history. Every individual model remains finite; the unboundedness is over the family.

## Proof A — neutral-prefix support identity (including early stopping)

Take ANY horizon-three P/Q experiment E with its original first-stage history set. Prepend one deterministic common source-neutral root, then shift the old stages to t=2,3,4. At the root, stopping has alpha-beta=0 and tau_P=tau_Q=1, yielding -2c. Continuing makes both stopping times exactly one unit longer while preserving alpha-beta, giving V_m^E(c)-2c. The root's private randomized initial register cannot improve a linear-support optimum because its outcome is source independent and can be conditioned into a feasible old m-state policy. Therefore for each m>=1 (and also F):

    V_m^lift(c) = -2c + max(0, V_m^E(c)).

This identity is SUPPORT-only. It is not used to assert raw-set equality.

## Proof B — every full policy admits max(k,2)-state RAW reproduction

Fix any full randomized policy. Reproduce the common root stop/accept/continue kernel exactly. Conditional on continuing, at t=2 observe h and write it injectively into a register with k available states; reproduce h's stop/accept/continue probabilities. Write t_h=Pr(continue at t=2 | h). At t=3, on each reached (h,j) write binary register 1 with full conditional continuation probability u_hj, else 0 (STOP), and select action from this written state. This uses only old register h and current j and its joint likelihood ratio; m>=2 suffices for the binary rewrite.

For a fixed joint likelihood-ratio fiber r=p_hj/q_hj, let b_hj be the probability of stopping/accepting at t=3 conditional on reaching (h,j), with 0<=b_hj<=1-u_hj. Define

    D_r = sum_{(h,j):p_hj/q_hj=r} q_hj*t_h*(1-u_hj),
    A_r = sum_{same fiber} q_hj*t_h*b_hj.

On state 0, stop and accept with eta_r=A_r/D_r when D_r>0 (otherwise arbitrary). Q stop acceptance agrees exactly. For P each summand is r times the corresponding Q mass, hence its stop acceptance agrees too, even after multiplying by the source-neutral root continuation probability.

For terminal ratio s=p_hjy/q_hjy, with full conditional terminal accept probability z_hjy, define

    E_s = sum_{(h,j,y):p_hjy/q_hjy=s} q_hjy*t_h*u_hj,
    C_s = sum_{same fiber} q_hjy*t_h*u_hj*z_hjy.

All terminal survivors have register 1. Accept with C_s/E_s for E_s>0. Terminal P and Q acceptance masses match separately by the fiber constancy p=s*q. Since every stage's continuation masses agree for both sources, their EXPECTED STOPPING TIMES also match. Together with reproduced root and t=2 acceptance, this constructs the exact original four-coordinate O for every full policy. Conversely full history simulates any register policy, hence S_m=S_F for m>=max(k,2). This statement is about four readouts, not complete pathwise/future-operation/native-X6 equivalence.

## Proof C — positive rational k>=2 family and exact lower bound

Use the EC48O three-stage k-history construction appended below, and prepend the neutral root of Proof A. At t=2, P(h)=Q(h)=1/k. For stage-three shared signals j=1..s, P(h,j)=Q(h,j)=mu. If word w_h[j] is 0, put a single neutral terminal leaf (P,Q)=(mu,mu); if 1, put terminal up=(3mu/4,mu/4), down=(mu/4,3mu/4). For each h, add private t=3 signals + with one leaf (1/(2k),1/(4k)), and - with one leaf (1/(4k),1/(2k)). Every existing leaf is positive rational, P/Q normalize individually: s*mu+3/(4k)=1/k. Stage-two h and all shared stage-three j have JOINT LR=1; private +/- ratios are 2 and 1/2. Terminal informative ratios are 3 and 1/3.

At an old first-stage history, optimal continuation's private +/- reward minus expected extra time is G0=(1/4-2c)/k. Informative shared j has continuation gain G1=mu*(1/2-2c); neutral shared j's unnecessary continuation costs d=2c*mu=c/(2ks). For 0<c<=1/16, G0>d and G1>d>0. Thus full history continues every h, accepts on private +, rejects private -, and continues a shared j exactly where its word bit is 1, then accepts only terminal up. Old V_F^E=1/4-4c+B*mu*(1/2-2c).

Any deterministic (k-1)-state controller either stops prematurely on some h, losing >=G0>d, or continues all and must give the same register message to two distinct code words. They differ on some shared j but have identical current j, stage-three joint LR=1 and register, so must choose the same action: stopping loses at least G1 on the informative word; continuing loses d on the neutral word. The full policy already chooses optimal terminal acceptance, so this loss cannot be restored at t=4.

The linear objective is multiaffine in the FINITELY many private kernel rows: each stage-indexed row occurs at most once along any trajectory. Extremizing each row onto a deterministic simplex vertex yields a deterministic controller at least as good as any randomized one. Therefore this lower bound covers private randomization without presuming that the raw observation set is convex.

Achievability at loss exactly d: merge only words 0^s and e_1; give all other h distinct messages. On their single conflicting j, continue both, causing exactly one neutral extra continuation. Thus V_(k-1)^E=V_F^E-d. Crucially the prefix root does not clip this separation: since B>=1,

    V_(k-1)^E=(1/4-4c)+mu[B*(1/2-2c)-2c]
                 >= mu*(1/2-4c)>0

for 0<c<=1/16. Apply Proof A to BOTH support optima to obtain the displayed four-stage formulas, preserving exactly gap d. This proves k necessary, while Proof B proves k sufficient for RAW set equality.

## Proof D — k=1 needs two states

Common t=1 root, one t=2 history, and at t=3 two signals a,b each of joint mass P=Q=1/2 and joint LR=1. Signal a has one neutral terminal leaf (1/2,1/2); signal b has up=(3/8,1/8), down=(1/8,3/8), all strictly positive. At c=1/32 full history stops on a, continues on b, and accepts up only:

    O_F=(3/8,1/8,7/2,7/2), V_F=1/32.

With one register state the t=3 signals are indistinguishable after LR compression, and deterministic support-optimal choices are stop at t=1,2,3, or continue all t=3 signals until t=4, with values respectively -2c,-4c,-6c,1/4-8c. At c=1/32 their maximum is 0. Multiaffinity extends this to random policies. Exact gap is 1/32, so two states are necessary; Proof B shows sufficiency.

## Exact 14-terminal-leaf rational witness

k=3, words 00,01,10; s=2, mu=1/24, B=2, c=1/16. For each h, private + (P,Q)=(1/6,1/12), -=(1/12,1/6). At each shared j with code bit 0, one leaf (1/24,1/24); with code bit 1, up=(1/32,1/96),down=(1/96,1/32). All 14 leaves have positive rational mass and each source totals one. Full optimum:

    O_F=(9/16,13/48,37/12,37/12), V_F=-3/32.

Two-state optimum (merge 00 and 01; continue both at shared j=1):

    O_2=(9/16,13/48,25/8,25/8), V_2=-19/192.

The strict gap is 1/192. Early root stopping gives only -1/8=-24/192 and is inferior, despite both continuing objectives being negative. The accompanying exact checker confirms both four-vectors and enumerates 432 full support-optimal deterministic two-state normal forms at each of three rational c values.

## Higher fixed-horizon consequence

For every H>=4 prepend H-3 neutral deterministic roots to EC48O's original k-history three-stage family. The support transformation Phi(v)=-2c+max(0,v) composes H-3 times. For any real 0<c<1/(16H), the old compressed support exceeds the threshold 2c(H-4): using d<=c/4,

    V_(k-1)^E - 2c(H-4)
       >= 1/4 - [4+1/4+2(H-4)]c > 0.

Hence no clipping occurs and the strict difference c/(2ks) survives at EVERY fixed finite H>=4. This does NOT claim infinite memory for any fixed finite experiment.

## Evidence, bounded verification, and scope

The published VERIFY.py extends the *actual preceding exact Fraction executable* without reimplementing its three-stage exhaustive engine. It reproduces old EC48O 16,384 deterministic three-state controllers for each of three cost values (49,152 exact old evaluations), and adds 432 deterministic two-state stage-2/3 controllers at each of three values for k=3 (1,296 new evaluations). It also checks P/Q positive mass, exact four-coordinate new witnesses at k=2..32 (31 families at three rational costs), k=1 and the 14-leaf instance. The three-stage parent also checks c=1/10, but for the NEW FOUR-STAGE theorem we use only 0<c<=1/16 because early root stopping can clip larger-c differences. Universal k and real-c claims are analytical; finite computations do not establish them by extrapolation.

The original six-dimensional discrete X6 Cell ontology plus separately typed time remains P000's internal research starting point. The finite BRC tree is a typed auxiliary probability model; no path/branch carrier, joint-relational observation and native-future-update preserving bridge from full X6 was established. A source file is neither a native Result nor independent mathematical admission. Next: EC48Q examines H=5 at fixed intermediate branch widths, seeking raw factorization or rational support separation with complete exact control normal form.

---

## Appendix — Exact predecessor EC48O theorem, proof, and family (verbatim, immutable commit 20eb4f35105908f403d631608657d7973bd604ee)

This appendix is included as mathematical dependency documentation and provenance. It remains an independently unreviewed three-stage author proof; the new horizon-four claims are in the self-contained sections above.

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