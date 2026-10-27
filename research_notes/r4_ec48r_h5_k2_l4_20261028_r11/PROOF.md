# EC48R — General finite-horizon RAW memory bound and sharp H5 k=2,l=4 example

**Research date:** 2026-10-28 Asia/Shanghai. **Author-side identity:** EM-R004-EC48R-20261028-LOCAL / TASK_RESEARCH. This local identifier is not a native service-issued session or CLAIM. **Scientific status:** AUTHOR_PROVED / EXACT_COMPUTATION_PASS / UNREVIEWED / NOT_ADMITTED.

**Frozen source reading:** GLOBAL_KNOWLEDGE_V1 canonical main e86c22eb04c62c816c15041d2e4cabdec833c1c4; Enterprise Math canonical main f86ad9db1a4e3c8d7899ef4b2f43f3e46bbc77ea; previous EC48Q PR #1584 at c592bd5272ba75b42ef6ac001f915a4e39e384e5. EC48O/EC48P predecessor claims remain independent-review pending; neither is required for the two new proofs here. A current owner-inventory query returned CONTROL_QUOTA, so this is an independent author-side mathematical handoff.

## Definitions and scope

Fix H>=2. At each time t=1,...,H, a finite strictly positive two-source (P,Q) experiment has **global prefix histories** g in G_t with unconditional masses p_t(g),q_t(g)>0. These are normalized under each source. Joint-prefix likelihood ratio r_t(g)=p_t(g)/q_t(g) is observable; the originating source is not observable. The agent may stop/accept, stop/reject or continue until forced terminal accept/reject at t=H. Random behavioral kernels are **source-independent**, with no external public seed or hidden post-compression history. The full observer remembers the complete prefix. An m-state observer updates its register before acting using old register, current signal, time and current joint ratio. The terminal can read the ratio.

The declared four readouts are O=(alpha,beta,tau_P,tau_Q)=(Paccept,Qaccept,E_PT,E_QT); S_F and S_m are the **raw** attainable regions over all randomized policies. Preserving these four readouts is weaker than preserving the hidden labeled branch law or arbitrary operations after horizon H.

**BRC method:** use exact positive Q-prefix masses and aggregate only over fibers of the joint P/Q ratio. This is REUSE_APPLIED of the weighted-positive BRC algebra represented in definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json; it is not a claim to have executed the native heartbeat/BRC-Shor arithmetic pipeline. P000, ACTIVE six native discrete X6 space axes plus separately typed time, and the joint observer/provenance retention constraints remain unchanged. A transfer to native X6 dynamics requires a distinct typed embedding, readout and future-operation preservation proof.

## Theorem A: universal finite-horizon prefix-width RAW upper bound

For every declared finite experiment, let

    M_H = max(2, |G_1|, ..., |G_(H-2)|).

Then, **for every full-history randomized policy**, an M_H-state source-independent controller produces precisely its four-vector. Hence

    S_(M_H) = S_F.

For H=5, a single stage-1 root, stage-2 width k=|G_2| and stage-3 **global** width l=|G_3|>=k, it specializes to

    S_(max(l,2)) = S_F.

**Proof.** For a full-history behavioral policy, write t_t(g) for continuation probability on arrival at g, b_t(g) for **unconditional stopped-and-accepted probability given arrival**, 0<=b_t(g)<=1-t_t(g), and z_H(g) for terminal acceptance probability. Let R_t(g) be the product of ancestral continuation probabilities. Since policy kernels are source-independent, R_t(g) is the same function of g under P and Q.

At each t<=H-2 injectively code the current global history G_t in M_H states. The previous code reconstructs the previous global prefix; adding the new signal reconstructs g, so the update-before-action controller can copy t_t(g),b_t(g) exactly and overwrite with g's new code. Both P and Q survival masses and stopped-acceptance masses agree at these stages.

At the penultimate stage H-1, the previous code plus current signal reconstructs the full current prefix g even if many current histories share a likelihood ratio. Write register state 1 with probability t_(H-1)(g), otherwise state 0; continue iff state 1. For each fiber F_r={g: p_(H-1)(g)/q_(H-1)(g)=r}, set

    D_r=sum_(g in F_r) q_(H-1)(g) R_(H-1)(g) (1-t_(H-1)(g)),
    A_r=sum_(g in F_r) q_(H-1)(g) R_(H-1)(g) b_(H-1)(g).

At state 0 accept with eta_r=A_r/D_r when D_r>0, arbitrary in [0,1] otherwise. Because b_t<=1-t_t, eta_r is a legal probability. Q stopped-accept mass is A_r exactly; P stopped-accept mass equals r*A_r because p=r*q at every prefix in the fiber. The source-dependent reach probabilities are accounted for by p_t,q_t, while R_t is source-neutral.

All terminal survivors have state 1. For terminal fiber F_s^H={g: p_H(g)/q_H(g)=s}, define

    E_s=sum_(g in F_s^H)q_H(g)R_H(g),
    C_s=sum_(g in F_s^H)q_H(g)R_H(g)z_H(g).

Accept at terminal with theta_s=C_s/E_s when E_s>0 (arbitrary otherwise). Then both Q and P terminal acceptance totals agree by fiber-constant s. Earlier acceptance was copied. Expected time obeys E_PT=1+sum_(t=2..H)P(T>=t), and likewise Q. Every stage survival mass agrees (early kernels copied, last continuation encoded in bit 1), proving tau_P and tau_Q equality. Thus S_F is contained in S_(M_H). Conversely the full observer can simulate the registered machine's source-neutral random updates, proving reverse inclusion. The result is **raw region equality**, without mixing over full policies. QED.

## Theorem B: exact k=2,l=4 four-state sharpness

There is a twenty-terminal-leaf **strictly positive rational** H5 tree, genuinely branching at both stage 2 and 3, such that for every **real** 0<c<=1/32, with

    J_c = alpha-beta-c(tau_P+tau_Q),

the full-history and all three-state registered support optima satisfy

    V_F(c) = 5/16-(33/4)c,
    V_3(c) = 5/16-(133/16)c,
    V_F(c)-V_3(c) = c/16 > 0.

Combining with Theorem A proves the worst-case necessary register **cardinality is 4**, not merely an upper estimate. The three-state raw region and even its convex hull differ from the full region.

**Exact tree.** Stage 1 is one source-neutral root. Stage 2 yields A or B, each P=Q=1/2. Stage 3 yields local 0 or 1 conditionally P=Q=1/2 under either group. Four *global* histories h=A0,A1,B0,B1 each have P=Q=1/4. Associate binary codewords respectively 00,01,10,11.

Let mu=1/32. At stage 4, from every h the same observable signal names appear: private +, private -, common j=0, common j=1. Their **unconditional joint prefix** P/Q mass pairs per h are

    private + : (1/8,1/16), ratio 2;
    private - : (1/16,1/8), ratio 1/2;
    common j=0: (mu,mu), ratio 1;
    common j=1: (mu,mu), ratio 1.

They sum to (1/4,1/4) per h. At t=5 a private signal has one deterministic terminal symbol. For common j with w_h[j]=0 there is one neutral terminal symbol of pair mass (mu,mu). For w_h[j]=1 there are up and down terminals of pair masses up=(3mu/4,mu/4), down=(mu/4,3mu/4), with terminal joint ratios 3 and 1/3. There are 8 private leaves, 8 common base leaves and 4 extra positive splits = **20 leaves**, and each source's total is 1. Every stated probability is strictly positive. The word h is hidden after register compression; the stage-4 current signal name j and joint ratio 1 do not reveal it.

**Full optimum and witness.** At joint ratio 1 immediate acceptance has zero alpha-beta gain. Stage-4 private + optimally stops/accepts, private - stops/rejects: continuing to the deterministic terminal would add positive cost and no information. For a common j whose code bit is 1, continuing gains mu/2 in alpha-beta contrast and costs 2c*mu in sum of stopping times. For a zero bit it gains zero but costs 2c*mu. With c<=1/32 the full policy continues precisely the four one-bits. Stage-2 groups and stage-3 types all continue (their strict optimality is shown next). Direct mass accounting gives

    O_F=(19/32,9/32,33/8,33/8),
    V_F=5/16-(33/4)c.

**Complete three-state support argument.** In a finite acyclic stopping tree, fixing all other kernels makes the linear objective affine in any one time/input policy or register-update row: no such row is visited twice on a single path. Successive simplex maximization yields a deterministic optimal controller. Global private random mixtures cannot improve that linear maximum. Three states can represent A versus B distinctly at stage 2; this is a weak refinement of any collapsed group encoding and preserves all later choices, so assume distinct stage-2 encodings. Every stage-3 h now either stops or continues with one of 3 register messages. Every (message,j) row at stage 4 stops or continues. Private +/- and terminal acceptance follow the optimal joint-ratio rule.

For c<=1/32, early stopping cannot be optimal. If one h currently stops at stage 3, continue it using any available state while retaining other rows. The private + adds 1/16 acceptance contrast; additional stage-4 reach costs c/2 and at most two common stage-5 reaches cost 4mu*c=c/8. Any informative up acceptance gained is nonnegative. Net improvement is at least

    1/16 - (5/8)c > 0.

If one entire A/B group stops at stage 2, instead continue both of its types with any register messages, leaving the other group unchanged. The two private + branches add 1/8 acceptance contrast; stage-3 and stage-4 reach costs sum to 2c, and at most four common terminal continuations cost 8mu*c=c/4. Net improvement is at least

    1/8 - (9/4)c > 0.

Stopping at the root yields -2c, whereas the constructed three-state policy below has strictly positive J for every c<=1/32. Thus all four global types continue to stage 4 in every optimal deterministic three-state support policy.

For each register message m and shared signal coordinate j, let n_1(m,j) and n_0(m,j) be numbers of encoded words having 1 or 0 at j. Continuing that row rather than stopping changes support by exactly

    G_(m,j) = mu*(n_1(m,j)/2 - 2c*(n_1(m,j)+n_0(m,j))).

For n_1=0 it is negative; for n_1>=1 and at most four words, c<=1/32 implies G>=mu*(1/2-8c)>=mu/4>0. Hence the optimal compressed row continues **iff at least one of its codewords has bit 1**.

Map four distinct 2-bit words into only three messages. By pigeonhole two different words collide; they differ in some coordinate j. That row contains 0 and 1, so must continue and unnecessarily advance at least one zero-bit branch. Its exact extra total time is 2mu, losing 2c*mu=c/16. Conversely merge adjacent 10 and 11, encode 00 and 01 separately, continue rows containing any 1. This creates exactly one unnecessary zero continuation and loses no accepted information. Therefore

    O_3=(19/32,9/32,133/32,133/32),
    V_3=V_F-c/16

for **all real** 0<c<=1/32. At c=1/32 the exact values are V_F=7/128 and V_3=27/512, gap=1/512. QED.

**Verification and limits.** VERIFY.js is an actually executed exact integer enumerator of the justified deterministic support normal forms. It checks 65,536 three-state policies (4 group stop masks * 4^4 type stop-or-message choices * 2^6 shared-signal rows), 16,384 full policies (4 group masks * 2^4 type continuations * 2^8 shared rows), and 20 strictly positive terminal masses summing to 128/128 under P and Q. For c=1/128,1/64,1/32 all exact maxima match the formulas; EXACT_REPORT.json preserves the actual numerical outputs. The real interval and universal raw upper are proved algebraically, not inferred from these three samples. An independent larger Python Fraction checker also produced 513 exact raw four-coordinate reconstruction equalities for a *different* strictly positive 2->4 model with nonidentical tau_P and tau_Q; that local cross-check is supplementary and not required for the remote support certificate. Formal proof assistant verification, native Source publication/CLAIM and independent Driver scientific admission are future gates. No native X6 dynamics is inferred.

**Next:** EC48S in NEXT_TASK.md investigates general sharp capacity at arbitrary global intermediate widths k,l, controlling partially revealed stage-2 information.