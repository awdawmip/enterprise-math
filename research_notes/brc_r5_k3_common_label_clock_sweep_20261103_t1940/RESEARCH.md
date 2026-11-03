# R5 K3 — common-label sixteen-parameter clock sweep, exact all-real separation

Date: 2026-11-03 Asia/Shanghai. Classification: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Exact frozen scope

Mother goal: find a genuine finite two-law stopped experiment whose FULL and seedless likelihood-ratio four-observer convex hulls agree while their actual real-behaviour observer images differ. Here we produce a parameter-uniform necessary condition for hull equality in the existing *strict common terminal-label* K3 experiment, rather than changing that experiment.

Scientific pins carried from the 18:35 predecessor: Global Knowledge a01383f825ef9d43b4b754254303298c64041568, Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Immediate scientific source: immutable R5 common-label uniform-clock theorem at c7caa7554474a18e3e5a71398e0293317624c10c, folder research_notes/brc_r5_k3_common_label_uniform_clock_rigidity_20261103_t1835. Current *normative* routing independently read on 2026-11-03 from Global Knowledge main 5f51c8f6ba95b862bbe59a9d158141ef7f62e785 and Enterprise Math main d3cb251a258c05fdf7b510507100cd5af5bfb001.

The four source labels are C,I,BJ,IJ, with positive BRC weights c=(1/8,1/6,1/16,3/32) at the upstream source-maximizing corner. Their identities, two-law provenance and distinct sourcewise clocks are retained. Source-to-observer aggregation is performed only inside the stated four-coordinate readout.

## Full real behavioural model

Let alpha=(1/2,2/3,1/2,3/4). FULL chooses real 0<=x,y<=1, 0<=i<=1-x and source-specific z_s,t_s,u_s in [0,1]. LR imposes i=(1-x)y and common controls z,t,u. Define

    w=(1/4,(1-x)/4,y/8,i/8)
    M_s=w_s alpha_s z_s, S_s=(2/3)M_s t_s, U_s=S_s u_s
    d=y/16+3i/32.

For each source independently let p_s,q_s,r_s,v_s be arbitrary REAL numbers in (0,1), with the common terminal-label physical experiment of the predecessor. All four observables are

    eP=107/128-21x/128+d/4-(sum S)/2+sum_s p_s S_s/8
    eQ=13/64+3x/64-d/2+(sum S)/8+sum_s q_s S_s/32
    TP=3+sum M+(3/2)sum S+sum_s r_s U_s
    TQ=3+(sum M)/2+(3/8)sum S+sum_s v_s U_s/4.

This is a full 16-real-parameter kernel: all p,q,r,v are independently source-heterogeneous. No additional observer, action-dependent answer label, or modified error readout is introduced.

## New theorem: one-parameter time-only separating family

For ANY theta in (0,9/8], use the signed direction

    n(theta)=(0,0,-theta,4).

Let b(theta)=3-2theta if theta<=1, and b(theta)=2-theta if theta>=1. Set

    g_s(theta)=v_s-theta*r_s                           if theta<=1;
    g_s(theta)=v_s-theta*r_s-(3/2)(theta-1)           if theta>=1.

Put P(theta)=sum c_s max(g_s,0) and N(theta)=sum c_s max(-g_s,0). For all real behavioural policies, exactly

    h_FULL(n(theta))=3(4-theta)+b(theta)sum c_s+(2/3)P(theta);
    h_LR(n(theta))  =3(4-theta)+b(theta)sum c_s+(2/3)max(P(theta)-N(theta),0);
    Delta(theta)    =(2/3)min(P(theta),N(theta)).

Consequently a theta in (0,9/8] with min_s g_s(theta)<0<max_s g_s(theta) yields strict four-observer convex-hull separation, REGARDLESS of all eight answer probabilities p_s,q_s. Every hull-equal kernel in this strict common-label family must avoid such a sign crossing for EVERY theta in that interval. This is an explicit necessary condition, not a classification of every possible clock vector.

### All-real proof

For n(theta), both error coordinates have zero coefficient, so p and q disappear identically. The signed baseline equals 3(4-theta) for every upstream policy. At a single source with unit carrier c_s(x,y,i)=w_s alpha_s, the four nested deterministic-stage payoffs (off, z-only, z+t, z+t+u) are

    V0=0,
    V1=2-theta,
    V2=3-2theta,
    V3=3-2theta+(2/3)(v_s-theta*r_s).

For 0<theta<=1, V2>=V1 and V2>0, so the sourcewise maximum is V2+(2/3)max(v_s-theta*r_s,0). For 1<=theta<=9/8, V1>=V2 and V1>0, so the sourcewise maximum is V1+(2/3)max(v_s-theta*r_s-(3/2)(theta-1),0). In both regimes this is b(theta)+(2/3)(g_s(theta))_+.

Crucially V1>0 and V2>0 for the entire interval; and V3>3-(8/3)theta>=0 because 0<r_s,v_s<1. Thus every individual stage payoff is nonnegative for every source. The source weights w_s alpha_s are componentwise no greater than the weights at x=0,y=1,i=1, which are c_s. Each deterministic FULL or LR policy, with all sources choosing a fixed common stage in LR, therefore has signed value at most its counterpart at this source-maximizing corner. The FULL choice of x,y,i=(0,1,1) and independent source stages attains sum c_s max_j Vj_s; the LR choice at the same corner attains max_j sum c_s Vj_s. This establishes global maxima over all real upstream behaviours without any finite sample assumption.

The continuation-control contribution is multi-affine in the probabilities z_s,t_s,u_s (or common z,t,u). Iterative maximization over the unit cube attains a deterministic stage; for FULL each source can pick its own maximizing stage, while LR selects one stage for all sources. Hence FULL adds (2/3)P, and LR adds (2/3)max(P-N,0), on the same baseline b(theta)sum c_s. The difference is (2/3)min(P,N), proving the theorem for arbitrary REAL kernel parameters and behavioural controls. Sourcewise positive weights establish strictness precisely at mixed signs.

## New separating rational witness invisible at theta=1

Choose r=(1/2,1/2,1/2,1/2), v=(13/20,9/10,13/20,9/10) and deliberately nonuniform p=(1/4,1/2,3/4,1/2), q=(3/4,1/2,1/4,1/2). At theta=1 all four v_s-r_s are positive, giving Delta(1)=0. At theta=11/10, g=(-1/20,1/5,-1/20,1/5), so

    P=5/96, N=3/320, Delta=(2/3)(3/320)=1/160.

The actual FULL policy x=0,y=1,i=1, source stage sequence (1,3,1,3) (z-only on C,BJ; z+t+u on I,IJ) gives

    W=(1841/2304,153/1024,1093/288,213/64).

Its exact signed support values are

    h_FULL(0,0,-11/10,4)=26317/2880,
    h_LR  (0,0,-11/10,4)=26299/2880.

Since ||n||_1=51/10, for EVERY actual real LR policy and every point in its convex hull,

    distance_inf(W,conv O(LR)) >= (1/160)/(51/10)=1/816.

This is a model-specific rigorous no-go witness and a reusable time-only signed screening criterion. The mother target requiring *equal* hulls stays open.

## Executed exact regression

The companion VERIFY.py uses only standard-library fractions.Fraction. It exhaustively computes all 1536 FULL (six upstream corners times 4^4 source stages) and 16 LR (four upstream corners times four common stages) deterministic observers, for three fully rational kernels and six theta values each: 18 model/direction combinations. It checks exact FULL and LR support formulae and their gap, as well as the explicit rational witness and theta=1 non-detection. All 58 assertions passed. The published EXACT_OUTPUT.txt is actual program output. The analytic theorem covers all real parameters; the finite regression independently checks its arithmetic in the stated sample.

## Authority, provenance and continuation

GitHub connected principal awdawmip had admin permission. Native Site status on 2026-11-03T11:39Z: static_machine_readonly, research_authority_granted=false; bounded owner lookup did not return a certified active owner. Hence this is author-side portable material and not an authorized CLAIM, formal Result, independent Driver review, or theorem admission. P000 / ACTIVE worldview / frozen scientific pins remain unchanged. BRC applied: explicit positive source carriers c_s and a fiber-sensitive observer comparison, without collapsing hidden origin before the FULL/LR extremization. Next step is in NEXT_TASK.md.
