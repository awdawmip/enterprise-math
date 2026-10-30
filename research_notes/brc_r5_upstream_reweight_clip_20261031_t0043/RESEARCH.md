# R5: All-real clipping criterion for upstream-reweighted three-class STOP trees

**2026-10-31 Asia/Shanghai.** Author-side PROVED with exact Fraction regression; **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This is portable derivation, not a native CLAIM, Result or independent review. An attempted bounded live owner read via em_control_tasks returned CONTROL_QUOTA. No native ownership asserted.

## Pinned inputs and source scope

GLOBAL_KNOWLEDGE_V1 canonical main: 7c3130bc1a11f50266cfef83d123c939fdf3917d. Enterprise Math canonical main: d6784e1dad20bf11d02962ba8f199ea95051218a. Consumed global bootstrap/manual, P000 full current project contract, ACTIVE worldview and Heartbeat companion, observer-preservation constraint, applicable portable research/control rules. Global P000 startup projection's canonical blob differs from the live project P000 blob; the complete current project P000 controls this derivation. The locked worldview is unchanged.

Immediate scientific source: research_notes/brc_r5_threeclass_affine_time_hull_rigidity_20261030_t2342/RESEARCH.md at d3ea995feff73faa65f2a537da9f5feaf2692ff1, Draft PR #1663. It proved a time-hull obstruction at fixed Q(X,U); here both upstream source weights are freed and the chosen direction's exact clipping behavior is characterized.

## Exact positive model

For real 0<A,B<1/2, A!=B and 0<t0,t1<1/4, set Q(0,0)=A, Q(1,0)=1/2-A, Q(0,1)=B, Q(1,1)=1/2-B. Write a_x=Q(x,0), b_x=Q(x,1). The time-3 P/Q likelihood ratios are r_0=3/4 and r_1=5/4; the time-4 ratios are R=(1/2,1,3/2). Given source X=x and middle U=u, the Q transition to V=0,1,2 is

    K_(x,0)=(1/2+t_x,1/2-2t_x,t_x);
    K_(x,1)=(t_x,1/2-2t_x,1/2+t_x);
    q_xuv=Q(x,u) K_(x,u)(v), p_xuv=R_v q_xuv.

All twelve P/Q path masses are strictly positive, both measures sum to 1 and sum_v K_(x,u)(v)R_v=r_u. Time-2 source likelihood ratios are (3A+5B)/(4(A+B)) and [3(1/2-A)+5(1/2-B)]/[4(1-A-B)], distinct iff A!=B. Hence LR sees X at time 2, sees U at time 3 and V at time 4, but no longer knows X at time 3 or 4. FULL sees history. Decisions at times 2,3,4 are actual STOP/CONTINUE (STOP absorbs at once); time 4 CONTINUE terminates at time 5. LR uses independent real behavioral controls at time-plus-ratio keys and has no persistent random seed.

## Theorem A: exact all-real support clipping

Define ell(t)=(5-2t)/(6-4t), w_x=a_x(3/2-t_x), and lambda=(w_0 ell(t0)+w_1 ell(t1))/(w_0+w_1), lying strictly in (5/6,9/10). Let H=T_P-lambda T_Q and [z]_+=max(0,z). Define

    G_x0=(3/2-t_x)(ell(t_x)-lambda);
    G_x1=5/2-2lambda+t_x(lambda-1/2);
    g_x=a_x G_x0;
    D_x=a_x(3/4-lambda)+b_x(5/4-lambda+G_x1).

For **all real behavioral policies**, the signed-support extrema are exactly

    sup_FULL H = 2(1-lambda)+sum_x [D_x+[g_x]_+]_+;
    sup_LR H = 2(1-lambda)+max(sum_x [D_x]_+,
                                 sum_x [D_x+g_x]_+).

The weights enforce g_0+g_1=0. When t0!=t1 they have opposite strict signs. At **this specific lambda**, strict support separation occurs precisely when

    g0>0: D0+g0>0 AND D1>0;
    g1>0: D1+g1>0 AND D0>0.

A zero for this chosen H is NOT a certificate that the complete time hulls agree.

**Proof.** A trajectory visits each control key at most once, including shared LR time-ratio keys, so every expected signed time payoff is multiaffine in the policy cube and achieves its maximum at a deterministic vertex. Continuing at time 4 adds R_v-lambda per unit Q mass; maximize to L_v=[R_v-lambda]_+=(0,1-lambda,3/2-lambda). At time 3 the continue-over-stop gain per Q(x,u) is r_u-lambda+sum_v K_(x,u)(v)L_v, directly giving the two G formulas. G_x1>0 for all admissible parameters. Thus U=1 CONTINUE is optimal whenever reached. Let h in {0,1} specify the shared LR U=0 decision. Its source-x time-2 continue gain is D_x+h g_x, while STOP gains zero. FULL independently selects h_x, giving sum_x[D_x+[g_x]_+]_+; LR must share h, giving max_h sum_x[D_x+h g_x]_+. Baseline time 2 contributes 2(1-lambda). Since lambda is the w-weighted average of ell(t_x), g0+g1=0; ell'(t)=2/(3-2t)^2>0. If g0=g>0, g1=-g, FULL's variable part is [D0+g]_++[D1]_+, LR's candidates are [D0]_++[D1]_+ and [D0+g]_++[D1-g]_+. The FULL value exceeds both exactly if D0+g>0 and D1>0. Interchange x for the other sign. QED.

## Theorem B: uniform open positive-weight obstruction

Suppose additionally b_x >= a_x/4 for x=0,1. Then, for EVERY legal real A,B,t0,t1 in that region,

    sup_FULL H - sup_LR H =
       a_0 a_1 |t1-t0| /
       [a_0(3-2t0)+a_1(3-2t1)].

It is strictly positive whenever t0!=t1. Therefore the FULL/LR two-dimensional STOP-time convex hulls differ; any four-observer hull projecting onto (T_P,T_Q) also differs for **every** terminal error reward that preserves the natural masses, STOP timing, and information structure. The strict interior b_x>a_x/4 is an open upstream-weight family, not one isolated rational instance.

**Proof.** Uniformly for 5/6<lambda<9/10,

    3/4-lambda > -3/20,
    G_x0 > -1/10,
    5/4-lambda+G_x1 =
         15/4-3lambda+t_x(lambda-1/2) >21/20.

It follows from b_x>=a_x/4 that D_x>9a_x/80>0 and D_x+g_x>a_x/80>0. Thus the time-2 gains are positive at both sources for either shared U=0 action; the clipping formulas reduce the gap to [g0]_++[g1]_+=|g0|=|g1|. Since

    ell(t1)-ell(t0) =
       2(t1-t0)/[(3-2t0)(3-2t1)],

and |g0|=[w0w1/(w0+w1)]|ell(t1)-ell(t0)|, substitution w_x=a_x(3-2t_x)/2 gives the claimed exact formula. Changing only terminal errors cannot alter this time-only support inequality. QED.

## Explicit new upstream rational certificate

A=1/4, B=1/3, t0=1/16, t1=1/8. The time-2 ratio pair is 29/28 and 19/20. The exact direction is lambda=77/90, and

    sup_FULL(T_P-77 T_Q/90)=913/1080,
    sup_LR  (T_P-77 T_Q/90)= 91/108,
    delta=1/360.

A maximizing valid FULL deterministic policy continues at time 2 for both sources, at time 3 for U=1 and for (X=1,U=0), but stops at (X=0,U=0); at time 4 it continues if V=1,2, otherwise stops. Its exact time pair is

    (T_P,T_Q)=(869/192,413/96).

Every LR real behavioral strategy satisfies 90T_P-77T_Q <=90*(91/108), whereas the FULL witness reaches 90*(913/1080): signed integer-direction support gap 1/4. Dual-norm control gives the actual-image bound d_inf>=1/668.

A clipping boundary example is A=49/100,B=1/100,t0=1/16,t1=1/8: lambda=1949/2298, the chosen direction's support gap is zero. This does not imply global time-hull equality.

## Typed reuse, verification and unfinished question

BRC resolution: REUSE_APPLIED to twelve positive source-labeled P/Q branch masses, future-operation-sensitive observer and exact residual. LR identification at time 3 drops source X while K_(0,u)-K_(1,u)=(t0-t1)(1,-2,1) has total variation 2|t0-t1|; never infer that total-mass equality licenses future-transition compression. This is auxiliary finite-probability mathematics, not Heartbeat native BRC-Shor arithmetic or an asserted X6/physics theorem.

Run the accompanying Python standard-library VERIFY.py. It checks 108 exact rational grid models (72 off-diagonal cone models), four independent exhaustive maxima with 2^18=262144 FULL and 2^7=128 LR deterministic policies per model, 12 positive masses and measure normalization, new witness, and a zero-at-lambda clipping case. All-real statements are proved analytically above, not from a grid or a floating fit. EXACT_OUTPUT.txt is genuine local stdout. Author proof and tests are not an independent mathematical admission.

**Next independent unit:** for strict-positive upstream parameters outside the cone, analyze the full Bellman normal fan and decide *all* signed time directions, not just lambda*, by exact halfspace/Farkas certificates. If a candidate has equal two-dimensional time hulls, select terminal errors and test full four-dimensional hull equality using <=5 rational LR vertices per FULL vertex or a strict rational separator, before investigating real-image nonmembership. Preserve full branch provenance and the unchanged locked P000/ACTIVE worldview. No native owner or CLAIM may be inferred from this portable PR.
