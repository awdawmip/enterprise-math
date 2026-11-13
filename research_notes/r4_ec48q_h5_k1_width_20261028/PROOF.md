# EC48Q — Sharp H=5 BRC memory capacity with one stage-two history and l stage-three histories

2026-10-28 (Asia/Shanghai) — TASK_RESEARCH author-side evidence, EM-R004-EC48Q-20261028-LOCAL. Status: **AUTHOR_PROVED / EXACT_COMPUTATION_PASS / UNREVIEWED / NOT_ADMITTED**. No service-issued CLAIM, native Result or independent Driver admission.

**Sources.** Current frozen read: GLOBAL_KNOWLEDGE_V1 main@5f1ec8305245b6cc03fdbf4378006861c660691b, Enterprise Math main@5bdf5d604e128408d2c103d2262fb2a7dd333f42. Scientific parent EC48P PR #1581, commit a569913b3cc267ab571db7f552e63878eb3c6895 (NEXT_TASK.md and PROOF.md); dependency EC48O PR #1578 commit 20eb4f35105908f403d631608657d7973bd604ee. Both are unreviewed author proofs. The present fixed-width RAW-region theorem is an extension, not independent replication of EC48O.

## Problem and exact claim

A finite strictly positive two-source (P,Q) observation tree has stopping decisions at stages 1–4 and forced accept/reject at t=5. Stages 1 and 2 have **one observable history each** (deterministic source-neutral prefixes); stage 3 has exactly l **global histories** h, not l LR fibers or fanout per parent. Stage 4 has any finite conditional signals j, and stage 5 terminal signals y. Full observer remembers history. An m-state controller updates its register **before** each action from the old register, current signal, time and *joint-prefix* likelihood ratio; its terminal accept decision can read current joint ratio. Random kernels are source-independent, with no public shared seed or hidden path read.

Four observations are O=(alpha,beta,tau_P,tau_Q)=(P accept,Q accept,E_P T,E_Q T); S_F and S_m are their **raw** attainable regions, not only their convex hulls.

**Theorem.** The least register cardinality guaranteeing S_m=S_F for **all** such trees is

    M*(H=5, stage2 width=1, stage3 global width=l)=max(l,2)    for every l>=1.

For l>=2 an explicit strictly positive rational family has, for every real 0<c<=1/32 and J_c=alpha-beta-c(tau_P+tau_Q),

    V_F(c)-V_(l-1)(c)=c/(2*l*ceil(log_2 l)) > 0.

For l=1 a separate strictly positive three-leaf example requires two states.

## Upper bound: constructive equality of raw four-coordinate regions

Fix an arbitrary full-history randomized behavioral policy. Because stages 1 and 2 have only a single source-neutral prefix, copy their stopping/acceptance/continuation kernels exactly; the probability z of reaching stage 3 is the same under P and Q. At t=3, encode the current history h injectively into l register values, copying its stop/accept/continue kernel. Let t_h be full continuation probability at h. At stage 4, old register h and current signal j identify (h,j) for the update. Let u_hj be full stage-4 continuation probability, b_hj its *unconditional on stage-4 action* stopped-and-accepted probability; 0<=b_hj<=1-u_hj.

Update register to **1 with probability u_hj**, otherwise **0**, and continue iff the new state is 1. This uses only two register states at this stage. For a fiber r=p_hj/q_hj (joint prefix likelihood ratio), define

    D_r=sum_(hj: r) q_hj t_h (1-u_hj),
    A_r=sum_(hj: r) q_hj t_h b_hj,
    eta_r=A_r/D_r when D_r>0, arbitrary otherwise.

In state 0, stop and accept with probability eta_r. The Q stopped-acceptance mass is exactly z A_r; P stopped acceptance is z*r*A_r because p_hj=r*q_hj termwise. Stage-3 accepts were directly replicated. At terminal stage 5 every survivor has state 1. For final joint ratio s=p_hjy/q_hjy, let full terminal acceptance be z_hjy and set

    E_s=sum_(hjy: s) q_hjy t_h u_hj,
    C_s=sum_(hjy: s) q_hjy t_h u_hj z_hjy,
    theta_s=C_s/E_s when E_s>0 (arbitrary otherwise).

Accept with theta_s. This preserves simultaneous P and Q terminal acceptance for every fiber. The continuation masses at stages 1,2,3,4 also agree separately under P and Q, so both stopping-time expectations agree. Thus for every full-history policy a max(l,2)-state controller reproduces its **exact four-vector**. The full observer can simulate any register controller, so S_max(l,2)=S_F, with no convexification assumption.

## Lower l>=2: inherited exact rational witness and clipping-controlled neutral prefixes

Use EC48O's positive three-stage k=l history construction: s=ceil(log_2 l), mu=1/(4*l*s), l distinct binary words w_h including 0^s and e_1; let B=sum_(h,j)w_h[j]. At stage 1, p_h=q_h=1/l. Each shared stage-2 signal j has P=Q=mu; a bit-0 j has one neutral leaf (mu,mu), while bit-1 j has terminal up=(3mu/4,mu/4), down=(mu/4,3mu/4). Each h has private stage-2 + with (P,Q)=(1/(2l),1/(4l)) and - with (1/(4l),1/(2l)). Strictly positive P/Q leaf masses each sum to 1; shared signal joint ratio=1, private +/- ratios 2,1/2. EC48O's exact support formula for 0<c<1/10 is

    V_F^E=1/4-4c+B*mu*(1/2-2c),
    V_(l-1)^E=V_F^E-d,   d=c/(2*l*s).

Prepend TWO single-signal deterministic source-neutral roots; original first history h becomes stage 3. The exact linear-support transformation of prepending ONE such root is Phi_c(v)=-2c+max(0,v): stop at the root yields -2c, continuation incurs one extra P and Q time unit and yields v-2c. Root private randomness only convexly mixes feasible old controllers and cannot improve their linear optimum.

To prevent root stopping from clipping the separation, note d<=c/4 (l>=2) and B*mu*(1/2-2c)>=0; hence for 0<c<=1/32,

    V_(l-1)^E >= 1/4-4c-d >= 1/4-17c/4 > 2c.

Both support values survive two neutral roots, each losing 4c with no clipping. Therefore the H=5 difference stays exactly d>0 for ALL REAL 0<c<=1/32. In particular S_(l-1) and S_F even have different convex hulls; l states are necessary. This also proves positivity: only deterministic roots were prepended; original existing leaves remain positive.

## Lower l=1: three-leaf witness

Two source-neutral roots lead to one stage-three history. Stage-four signals a,b have P=Q=1/2 and identical joint ratio 1. Signal a has one neutral terminal leaf (1/2,1/2), while b has up=(3/8,1/8), down=(1/8,3/8). At c=1/32, the full observer stops on a, continues b and accepts up, giving

    O_F=(3/8,1/8,9/2,9/2), V_F=-1/32.

With one register state, a and b are indistinguishable at stage 4. Exhaustive deterministic support-optimal choices (including earlier stopping) give max[-2c,-4c,-6c,-8c,1/4-10c]=-1/16. Source-independent behavioral randomization cannot increase the maximum of this finite multiaffine linear support over its deterministic vertex values. Thus a strict gap 1/32 persists, while the upper factorization shows 2 states suffice.

## Explicit l=3 14-leaf verification

Select codewords 00,01,10, s=2, mu=1/24, B=2, c=1/32. For each h the private + and - leaves have masses (1/6,1/12) and (1/12,1/6). Each j=0,1 has neutral joint mass (1/24,1/24); code bit 1 splits into terminal up=(1/32,1/96), down=(1/96,1/32), while code bit 0 has one neutral leaf. There are exactly 14 positive leaves, P sum=Q sum=1.

Full continuation through both roots and all h, accepting private +, and continuing only bit-1 shared signals to accept terminal up, has

    O_F=(9/16,13/48,49/12,49/12),    V_F=7/192.

Merge the 00 and 01 words into one register message and retain 10 separately. Continuing the merged pair on their unique conflicting shared signal forces one extra neutral stage-4 continuation, giving a two-state policy with

    O_2=(9/16,13/48,33/8,33/8),    V_2=13/384,

so the strict optimum gap is 1/384. For this l=3 family, the full exact parameter interval can be extended to 0<c<=7/150, with V_F=7/24-(49/6)c and V_2=7/24-(33/4)c.

The accompanying VERIFY.py runs exact Python Fraction arithmetic, 432=3^3*2^4 stage-3/stage-4 deterministic two-state normal-form controllers and 125=5^3 full controller normal forms at each of four rational costs, plus exact early-root, mass and observation checks. The normal form is complete for linear support: stage-3 action is stop or continue with bit 0/1; each bit/shared-j row stops or continues. Private +/- have no informative descendants and therefore optimal support always stops there; terminal decisions optimize alpha-beta by their current LR. Each stage-indexed random kernel row occurs at most once per path, so the support is multiaffine in rows and attains a deterministic extreme point. These computations verify finite instances; the real interval and arbitrary l theorem follow from the algebra and inherited EC48O lemma, not sample extrapolation.

## Evidence level and boundaries

This proves only preservation of the declared four raw observations and only for the stated auxiliary finite positive two-source experiment. It does **not** establish identity of hidden paths, all future tasks, raw joint-path structures, or physical native-X6 dynamics. Internal project P000's six discrete spatial axes and separately typed time are unchanged; no original X6 state/readout/future-operation preserving bridge is supplied. EC48O/EC48P dependence and the assumptions about deterministic extreme policies and joint-ratio fibers must receive independent mathematical review before admission. Native Owner/CLAIM could not be established at the read-only control gateway (CONTROL_QUOTA).

**Next discriminating question EC48R:** H5 with stage-two width k>=2 and stage-three global history width l>=k. Determine whether max(k,l,2) memory states preserve all raw four-vectors, or give an exact positive rational counterexample. Do not conflate per-parent branch fanout, global history width and LR-fiber count.
