# R5: Rank-four early-error lift destroys convex-hull equality despite equal STOP-time hulls

**2026-10-31 Asia/Shanghai. Author-side PROVED / exact integer-rational checked / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.** Frozen inputs: GLOBAL_KNOWLEDGE_V1 main@7c3130bc1a11f50266cfef83d123c939fdf3917d; Enterprise Math main@d6784e1dad20bf11d02962ba8f199ea95051218a. Scientific predecessor: TIME_HULL_EQUALITY_CERT.md in this folder, with its exact ten-facet proof. Native owner lookup yielded CONTROL_QUOTA. No native CLAIM or Result.

## Model and terminal-error observer

Keep the predecessor's exact 12 strictly positive normalized dual-measure path masses and real STOP/CONTINUE at times 2,3,4, forced absorption at 5. Nature Q(X,U) equals (49/100,1/100,1/100,49/100) for (00,01,10,11). Time3 likelihood ratios r=(3/4,5/4), time4 R=(1/2,1,3/2), and K_(x,0)=(1/2+t_x,1/2-2t_x,t_x), K_(x,1)=(t_x,1/2-2t_x,1/2+t_x), t0=1/16,t1=1/8. Non-lumpable source transition TV residual=1/8. FULL observes complete history; seedless LR only time and likelihood ratio.

Introduce strictly-interior terminal error probabilities epsilon(tau)=3/4 if tau=2, and 1/4 if tau=3,4,5. This legal error reward depends only on stop time (LR-local). Thus eP=1/4+P(tau=2)/2, eQ=1/4+Q(tau=2)/2. The 4D observable is (eP,eQ,TP,TQ).

## Exact theorem: rank four, strictly different four-hulls

The LR four-dimensional deterministic policy points have **affine rank 4**. However for H=TP−(1949/2298)TQ−2eQ, the exact suprema over **ALL real behavioral strategies** are

    sup_FULL H=87149/229800;
    sup_LR H=871/2298;
    Delta=49/229800 > 0.

The explicit FULL deterministic witness is (eP,eQ,TP,TQ)=(1/4,1/4,13539/3200,6323/1600). It has L-infinity distance from the entire real seedless LR four-image of at least

    Delta / (1+1949/2298+2)=49/884300.

The rank-four certificate uses LR policy indices 0,49,10,66,6, with determinant of the four difference rows (indices 49,10,66,6 minus index 0), coordinate order (eP,eQ,TP,TQ):

    det=147/2000000 != 0.

This proves four-dimensional FULL/LR hull inequality even though the EXACT SAME natural process has equal two-dimensional (TP,TQ) hulls. It is a no-go for the declared early-error reward lift, not for every possible source-dependent or time-dependent error kernel.

## Analytic proof

Take lambda=1949/2298, L_v=[R_v−lambda]_+ and G_xu=r_u−lambda+sum_v K_(x,u)(v)L_v. Exact gains are G_00=−1/2298, G_10=49/2298, G_01=1897/2298, G_11=649/766. Put a_x=Q(x,0), b_x=Q(x,1), g_x=a_x G_x0 and D_x=a_x(r_0−lambda)+b_x(r_1−lambda+G_x1). Then

    g=(-49/229800,+49/229800);
    D=(-2743/76600,140429/229800);
    Q(X=0)=Q(X=1)=1/2.

The reward term −2eQ=−1/2−Q(tau=2) penalizes time-2 STOP relative to CONTINUE. The baseline if all stop at time 2 is 2(1−lambda)−3/2. The time-2 CONTINUE gains are D_x+1/2+h_x*g_x, h_x in {0,1}. All are strictly positive for both sources and either h_x. The U=1 decision CONTINUE is strictly optimal; the U=0 decision is independent in FULL and must be shared in LR; time4 continuation optimal reward is L_v. Therefore

    sup_FULL H = 2(1−lambda)−3/2 + sum_x [D_x+1/2+[g_x]_+]_+;
    sup_LR H   = 2(1−lambda)−3/2 + max_{h in {0,1}} sum_x [D_x+1/2+h*g_x]_+.

All outer positive-part operators are inactive; g0+g1=0 and g0<0<g1, hence exact gap=49/229800. Multi-affinity in independent behavioral controls proves these deterministic maxima cover every real FULL/LR policy.

A separate exact program independently enumerates all 262144 FULL policies with integer-scaled H and the 128 LR four-observation vectors, verifies analytic extrema, checks the rank-four determinant, the explicit FULL witness and the norm bound. VERIFY_EARLY_ERROR_LIFT.py and literal executed stdout EXACT_EARLY_ERROR_LIFT_OUTPUT.txt are in this folder. No float arithmetic, formal review or native six-dimensional physical inference is claimed.

## BRC observer and next question

BRC retains all 12 positive source-labeled dual-measure masses; the LR projection loses X at stage3 and has future-kernel TV=1/8. The observer-sensitive result illustrates that a projection safe for convexified 2D stopping-time readout need not be safe after enriching the future observation by early-stop error reward, even with LR-local terminal error probabilities.

Next: select alternate terminal-error kernels on the same frozen 12-path model preserving strict positive probabilities and 4D rank, and certify 4D convex-hull equality with rational LR simplex lifts of FULL vertices (at most five LR vertices), or prove a Farkas separator. Only after full 4D hull equality investigate actual seedless LR real-image inequality. Preserve exact P000/worldview, roles, source pins and branch provenance.