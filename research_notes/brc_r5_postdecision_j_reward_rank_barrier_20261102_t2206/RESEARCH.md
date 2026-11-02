# R5 — Affine source-flow rank barrier and exact source-conditioned J-time compensation

Date: 2026-11-02 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Source, frozen scientific scope and mother target

Predecessor: awdawmip/enterprise-math@4a491075bc9815e4c355bcdfdf448322d7cce507:research_notes/brc_r5_compensated_family_full_classification_20261102_t2036/RESEARCH.md and NEXT_TASK.md. Preserve original scientific input pins: global main a01383f825ef9d43b4b754254303298c64041568 and enterprise-math main 86149263e38c22292c9def1e0f69092efa1be77e. These are scientific provenance, not current behavioral rules. Current normative snapshots read separately: global main d62616e2b3334c66663f4f92883f4ba137125c10 and Enterprise Math main 0f235fef24035ecb0378da1d1ae6cfcf615a9735.

Mother target: a strictly positive finite-horizon two-law stopping model whose FULL-history and seedless likelihood-ratio (LR) policy classes have the same convex hull of four observers, but different actual real-behaviour observer images, ideally of full affine rank four. The present result is a finite auxiliary positive-rational source-flow/BRC theorem, not an X6 physical realization. P000, ACTIVE worldview and formal scientific admission are unaffected.

## Model: source-labelled flows and postdecision J-time rewards

The I→J→K policy uses FULL variables x,j_B,j_I,k_C,k_I,k_BJ,k_IJ in [0,1]. Define

    b=1-j_B; i=(1-x)(1-j_I);
    D_B=b/8; D_I=i/8;
    w=(1/4,(1-x)/4,b/8,i/8);
    alpha=(alpha_C,alpha_I,beta_B,beta_I), with all four entries >0;
    r=sum_s alpha_s*w_s*(1-k_s);
    H(x)=alpha_C/4+alpha_I*(1-x)/4;
    rmax(x,b,i)=H(x)+(beta_B*b+beta_I*i)/8.

LR shares J hazard y and K hazard z, so b=t=1-y, i=(1-x)t, r=(1-z)rmax. Prior compensated-law kernels may additionally be imposed by alpha_s=1+p_s with p_s in (1/8,1), q_s=(8p_s-1)/9, K answer probabilities U_s=kappa*alpha_s, V_s=lambda*alpha_s in (0,1). All three examples below meet these stricter requirements.

Modify the observable terminal clock by adding source-conditioned nonnegative J→K *postdecision* rewards u_B,u_I,v_B,v_I. They are recorded only after decisions, so they do not split the K likelihood-ratio collision key. Put

    B=5/2-3*x/4+(b+i)/4;
    eP=1-(aB*b+aI*i)/8-kappa*r;
    eQ=  (cB*b+cI*i)/8+lambda*r;
    TP=B+r+(uB*b+uI*i)/8;
    TQ=B+(8/9)*r+(vB*b+vI*i)/8;
    O=(eP,eQ,TP,TQ).

Here aB,aI,cB,cI are in (0,1), uB,uI,vB,vI >=0. The new observer is affine in four sufficient aggregates: O=O0+M*(x,b,i,r), with O0=(1,0,5/2,5/2), and columns

    Mx=(0,0,-3/4,-3/4);
    Mb=(-aB,cB,2+uB,2+vB)/8;
    Mi=(-aI,cI,2+uI,2+vI)/8;
    Mr=(-kappa,lambda,1,8/9).

Genuinely *predecision* visible delay would change the LR information partition, and is a different model not covered by the theorem.

## Main theorem — universal rank-four and rank-three classification

For every real strictly positive alpha_C,alpha_I,beta_B,beta_I under the source-flow topology above, let O=O0+M*(x,b,i,r) be ANY real affine map into R^4, with columns Mx,Mb,Mi,Mr.

(1) If rank(M)=4, the full and LR four-observer convex hulls differ. With ell=(-1,1,-1,0) and normal n=M^(-T)ell, their signed support-function difference is exactly

    h_FULL(n)-h_LR(n)=1,

and one FULL observation has directed L-infinity distance at least 1/||n||_1 from conv O(LR).

(2) If rank(M)=3, their convex hulls are equal IF AND ONLY IF

    Mb/beta_B = Mi/beta_I   (equality of all four coordinates).

Whenever this condition holds, their ACTUAL real-behaviour images coincide: O(FULL)=O(LR). The same explicit lift proves sufficiency at lower rank if this alignment holds.

It follows that any hull-equal but actual-image-unequal candidate WITHIN this fixed affine one-scalar-K source-flow topology must have rank(M)<=2. The mother problem for other decision topologies remains open.

### Proof, A: complete FULL aggregate polytope

The exact feasible FULL aggregate set is

    PF={0<=x<=1, 0<=b<=1, 0<=i<=1-x,
        0<=r<=H(x)+(beta_B*b+beta_I*i)/8}.

Every (x,b,i) is realized by J hazards, with jI=1-i/(1-x) when x<1 (i=0 when x=1). Any r in the stated interval is realized by taking every K hazard equal to 1-r/rmax, which is in [0,1] because rmax>=alpha_C/4>0. Thus the ACTUAL FULL image O0+M PF is a convex polytope. Let PL denote the convex hull in aggregate space of actual LR tuples (x,t,(1-x)t,r).

Every PL point has b>=i and, at x=0, the exact slice is

    PL intersect {x=0} =
    {x=0, b=i=t in [0,1],
     0<=r<=H(0)+(beta_B+beta_I)*t/8}.

Indeed a convex combination yielding x=0 can use only source tuples with x=0, and their (t,r) feasible set is a convex trapezoid.

### Proof, B: full-rank exact dual separation

At every LR point, ell dot (x,b,i,r)=-x+b-i=-x*(1-t)<=0. At the FULL point E=(0,1,0,0), its value equals 1. It is never greater than 1 on PF, since b<=1, i>=0, x>=0. If M is invertible, n=M^(-T)ell transports this identity to the four-observer map, with the affine constant cancelling. Hence the exact signed support gap is 1; Holder's inequality gives the L-infinity lower bound.

### Proof, C: rank-three necessity

Assume rank(M)=3 and conv O(FULL)=conv O(LR), with ker M the line spanned by nonzero v=(vx,vb,vi,vr). FULL vertices E=(0,1,0,0) and F=(0,0,1,0) must map inside M PL. Since neither lies in PL, there exist nonzero s,t with E+s v and F+t v in PL.

If vx != 0, nonnegative x coordinates force s and t to have the same sign. The opposite b-box corners E_b=1,F_b=0 force s*vb<=0 and t*vb>=0, hence vb=0. Similarly the opposite i-box corners E_i=0,F_i=1 force vi=0. Then F+t v still has b=0,i=1, contradicting b>=i throughout PL. Thus vx=0.

Both shifted points now lie at x=0, where PL requires b=i. Consequently s*(vb-vi)=-1 and t*(vb-vi)=1, so t=-s and vb-vi != 0. Both shifted r coordinates must be nonnegative, while E_r=F_r=0; therefore s*vr>=0 and -s*vr>=0, giving vr=0.

Define theta_B=-vi/(vb-vi), theta_I=vb/(vb-vi). The two shifted lower points have common b=i equal respectively to theta_B and theta_I, so theta_B,theta_I >=0 and theta_B+theta_I=1. The kernel relation then forces

    Mb=theta_B*(Mb+Mi), Mi=theta_I*(Mb+Mi).

Now consider the two FULL upper vertices

    E+=(0,1,0,H(0)+beta_B/8),
    F+=(0,0,1,H(0)+beta_I/8).

Their images also belong to M PL; because the kernel has vx=vr=0, the corresponding PL representatives must have x=0, r unchanged, and common b=i equal theta_B or theta_I. The LR slice upper roof implies

    beta_B <= (beta_B+beta_I)*theta_B,
    beta_I <= (beta_B+beta_I)*theta_I.

These two inequalities sum to an equality. Both therefore bind, yielding theta_B=beta_B/(beta_B+beta_I), theta_I=beta_I/(beta_B+beta_I) and precisely Mb/beta_B=Mi/beta_I.

### Proof, D: sufficiency and exact real-policy lift

If Mb/beta_B=Mi/beta_I, take any actual FULL tuple (x,b,i,r), and set

    denominator=beta_B+beta_I*(1-x)>0,
    t=(beta_B*b+beta_I*i)/denominator in [0,1],
    y=1-t,
    rmax_L=H(x)+denominator*t/8>0,
    z=1-r/rmax_L in [0,1].

The new LR policy has the same x and r and the same weighted J source sum beta_B*b+beta_I*i. Due to column alignment it therefore has exactly the same four observers. Since LR is a restriction of FULL, actual images and convex hulls coincide. The constructed lift is valid for all real policies, not just deterministic corners.

## Three strictly positive rational worked cases

Rank 4: alpha=(5/4,4/3,3/2,5/3), kappa=2/5, lambda=1/3, (aB,aI)=(3/5,1/2), (cB,cI)=(7/12,1/2), (uB,uI)=(1/2,1/4), (vB,vI)=(1/3,1/3). The J-source contrasts are compensated in selected combinations eP+kappa*TP and eQ-lambda*TP because kappa*uB-aB=kappa*uI-aI=-2/5 and cB-lambda*uB=cI-lambda*uI=5/12. Nevertheless det M=1/11520, n=(90,80,220/3,-72), ||n||_1=946/3. FULL policy (x,jB,jI;kC,kI,kBJ,kIJ)=(0,0,1;1,1,1,1) gives W=(37/40,7/96,45/16,67/24), exact signed gap=1, distance lower bound 3/946.

Rank 3 aligned global compensation: alpha=(4/3,5/3,3/2,5/4), kappa=2/5, lambda=1/3, J answer pairs (aB,aI)=(3/5,1/2), (cB,cI)=(2/5,1/3), terminal-time rewards (uB,uI)=(1,1/2), (vB,vI)=(1,1/2). Then Mb/beta_B=Mi/beta_I, det M=0 and an exact 3x3 minor equals 3/800 !=0. The P and Q J answer kernels and BJ/IJ time source weights are genuinely distinct. For every FULL real behaviour the displayed formula (y,z) gives identical LR observers: entire actual images and convex hulls coincide.

Rank 3 misaligned: keep that rank-3 observation map and change beta_I from 5/4 to 4/3, preserving all strict natural probabilities. Normal n=(755/33,335/11,0,0) gives exact support gap 1/176, attained by FULL (0,1,0;0,0,0,0) with W=(137/240,25/72,179/48,1567/432). Indeed with c=17/528, n^T M=(0,-6c,-5c,1); all LR obey r-c(6b+5i)<=H(0), whereas this FULL corner exceeds the bound by 1/176.

## Verification and continuing question

Standalone attached VERIFY.py uses only Python Fraction, enumerates all 128 FULL and 8 LR deterministic policies in the rank-four and misaligned cases, checks exact dual normal identities and observer maps, and tests 288 deterministic/non-corner FULL→LR real-strategy matches in the aligned case. The actually captured EXACT_OUTPUT.txt reports 1,595 passing exact assertions. Universal real conclusions are established by the algebra above, not by finite samples. No Lean/formal proof assistant, independent Driver review, native Source Result/admission, or claimed native X6 embedding.

The key new barrier is the single scalar K continuation statistic r and an affine observer. Next test a second genuinely interacting decision key producing two independent continuation statistics, or predecision-visible J time which changes the LR collision partition. Require an exact all-signed convex-hull certificate (or rational separator) for a fully positive rational model before testing actual LR-image nonmembership. The unaligned rank<=2 family is a separate optional question.

Research preserved as portable author material on the existing R5 PR. GitHub author identity is awdawmip with repository administrator permission. Native gateway status for this run: research_authority_granted=false, executor_binding_configured=false, active owner lookup CONTROL_QUOTA; own-session attempt STATIC_READONLY_SCOPE_DENIED (operation_sent=false). No native CLAIM/Result/independent Driver review is claimed.
