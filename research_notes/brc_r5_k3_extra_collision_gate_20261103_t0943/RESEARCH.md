# R5 — Third LR collision: exact post-K2 gate-residual theorem

2026-11-03 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Mother objective, source, model scope

Mother problem: construct a finite genuine P/Q stopped experiment such that FULL-history and seedless likelihood-ratio (LR) four-observer convex hulls coincide, while the actual real-behavior images differ. This independent unit changes the previous X→J→K1→K2 tree by introducing a genuine new decision K3. It proves a parameterized exact support gap, thus gives a discriminating obstruction rather than a hull-equal example.

Frozen scientific pins: global a01383f825ef9d43b4b754254303298c64041568; enterprise-math 86149263e38c22292c9def1e0f69092efa1be77e. Scientific predecessor and source of the physically realized base tree: enterprise-math@3537509f780d1aa45772b5cb3e149c8a266e7c25:research_notes/brc_r5_complete_16_parameter_classification_20261103_t0841/RESEARCH.md, and the underlying physical realization at commit 0592311ad484d47c449563167d2ae6521ccf4234. Current P000 and ACTIVE worldview are kept distinct and unchanged. This is an auxiliary positive-mass BRC probability-flow calculation; native six-axis calibration is not asserted.

## Physical construction, exact observer

Source labels s=(C,I,BJ,IJ), upstream FULL controls x,y,i in [0,1] with i<=1-x. LR imposes i=(1-x)y. Let

    w=(1/4,(1-x)/4,y/8,i/8), d=y/16+3i/32,
    alpha=(1/2,2/3,1/2,3/4), c=2/3,
    M_s=w_s*alpha_s*z_s, S_s=c*M_s*t_s, U_s=S_s*u_s.

The preexisting likelihood-ratio collision keys are J=(2,1), K1=(3,1), K2=(4,2). Introduce K3 at time 5 immediately upon K2 success, before either terminal delay coin has been tossed. Source s arrives with P mass S_s and Q mass S_s/4; all positive sources have the same key K3=(5,4). FULL may select u_s independently per source; LR must use common u. On selecting the gate, one additional terminal time tick occurs with Bernoulli probability r_s under P and v_s under Q, both in (0,1). The baseline terminal time delay is a separate independent Bernoulli(1/2) under both measures. Their sum gives possible stop times 5,6,7, with no further control. Q-answer terminal probabilities remain p_s=q_s=1/2. At each gate outcome, probabilities under P and Q normalize to the same input mass under the respective law. Thus the new K3 control is a real physical stop-time decision and a third genuine cross-source seedless LR collision.

For all admissible real behavior policies the exact P/Q error and mean stop-time observer is

    eP=107/128 -21*x/128 +d/4 -(1/2)*sum_s S_s,
    eQ=13/64 +3*x/64 -d/2 +(1/8)*sum_s S_s,
    TP=3+sum_s M_s+(3/2)*sum_s S_s+sum_s r_s*U_s,
    TQ=3+(1/2)*sum_s M_s+(3/8)*sum_s S_s+(1/4)*sum_s v_s*U_s.    (1)

The added P clock increment is r_s U_s; its Q increment is (v_s/4) U_s. The extra delay coin does not change terminal answer readouts. BRC source identity and positive P/Q masses are preserved; signed observer costs are applied only at the readout stage.

## All-real parametric theorem

For arbitrary real r_s,v_s in (0,1), put g_s=v_s-r_s/2 and w*=(1/8,1/6,1/16,3/32). Define Gplus=sum_s w*_s max(g_s,0) and Gminus=sum_s w*_s max(-g_s,0). For the signed four-normal n=(0,0,-1/2,4), the exact support functions of ALL legal real FULL and LR behavior policies satisfy

    h_FULL(n)=21/2 + 2*(43/96) + (2/3)*Gplus,
    h_LR(n)  =21/2 + 2*(43/96) + (2/3)*max(0,Gplus-Gminus),
    h_FULL(n)-h_LR(n)=(2/3)*min(Gplus,Gminus).             (2)

In particular, a source-positive and source-negative g pattern yields a strict separation for this entire continuum of physical probability kernels.

Proof: applying n to (1) gives exactly

    n·O=21/2+sum_s M_s*[3/2+c*t_s*(3/4+u_s*g_s)].

Since r_s,v_s in (0,1), we have -1/2<g_s<1 and 3/4+u_s*g_s>1/4>0 for all legal u_s. FULL thus maximizes each branch by z_s=t_s=1 and u_s=1 when g_s>0, 0 when g_s<0. Every source coefficient stays strictly positive; upstream x=0,y=i=1 then simultaneously maximizes all four nonnegative source masses. For LR the common z=t=1 likewise wins for each u, and x=0,y=1,i=1 simultaneously maximizes all masses. The remaining common gate payoff is c*u*sum_s w*_s*g_s, whose maximum over [0,1] is c*max(0,Gplus-Gminus). For FULL it is c*Gplus. Subtraction proves (2); no finite-sampling inference is used. QED.

## Positive rational example and separation certificate

Take r_s=3/4 for all sources and v=(1/4,3/4,1/4,3/4). Then g=(-1/8,3/8,-1/8,3/8), Gplus=25/256, Gminus=3/128, signed sum=19/256. Exact supports:

    h_FULL(n)=1467/128, h_LR(n)=1465/128, gap=1/64.

The FULL maximizer x=0,y=i=1, z_s=t_s=1 and u=(0,1,0,1) has actual observer

    W=(209/288,187/1152,773/192,2587/768).

The maximizing LR policy x=0,y=1, common z=t=u=1 gives

    V=(209/288,187/1152,791/192,2593/768).

Hence W-V=(0,0,-3/32,-1/128), n·(W−V)=1/64. Since ||n||_1=9/2, every point in conv O(LR) satisfies n·o <= h_LR, yielding

    dist_infty(W,conv O(LR)) >= (1/64)/(9/2)=1/288.

## Actual verification, evidence and next

The adjoining standalone Python standard-library Fraction source VERIFY.py was executed, and its actual output is preserved verbatim as EXACT_OUTPUT.txt: PASS_EXACT_R5_NEW_K3_COLLISION_GATE, 135 explicit rational assertions; exhaustive 24,576 FULL and 32 LR deterministic control configurations for the displayed instance; 40 additional nonbinary exact physical gate-flow checks. The continuum/all-real claim is proven above by positive-coefficient optimization, independently of these finite tests. The underlying predecessor physical path realization is an author-side cited dependency pending independent review.

Next: extend the third collision to independent source-conditioned answer and time signatures; derive the full four-signed Bellman support and seek an exact all-direction hull-equal candidate with rational FULL-vertex LR-combination certificates or a rational Farkas separator. Study when the K3 stage is observationally eliminable. Preserve the mother goal, frozen inputs, project worldview and native-authority boundaries.