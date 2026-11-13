# R5 — P/Q post-K2 delay-ratio rigidity and exact all-signed Bellman support

Date: 2026-11-03 Asia/Shanghai. Scientific status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Provenance and scientific scope

Mother objective: construct a finite two-law stopped experiment with conv O(FULL)=conv O(seedless LR), but different actual real-behavior four-observer images O=(e_P,e_Q,T_P,T_Q).

Verified author-side predecessor: enterprise-math@af370f5455f018e447b652f27f687fcaba925101:research_notes/brc_r5_independent_delay_face_global_gap_20261103_t0438/RESEARCH.md, together with its VERIFY.py and EXACT_OUTPUT.txt. Earlier P/Q stopping-path embedding: enterprise-math@0592311ad484d47c449563167d2ae6521ccf4234. Immutable science source pins: GLOBAL_KNOWLEDGE_V1@a01383f825ef9d43b4b754254303298c64041568; Enterprise Math@86149263e38c22292c9def1e0f69092efa1be77e. Current normative rules are applied separately, and P000/ACTIVE worldview are unchanged. This is an auxiliary positive-mass BRC source-flow model with physical P/Q stopping observations, not a native X6 physical calibration.

Four hidden sources s=(C,I,BJ,IJ) have first-stage P-success factors alpha=(1/2,2/3,1/2,3/4), Q-success factors alpha/2, and serial second-stage P-success c=2/3, Q-success c/2. LR's collision keys remain J=(2,1), K1=(3,1), K2=(4,2), stated as (time, likelihood ratio). Terminal answer parameters p_s,q_s and time-6 delay parameters a_s,b_s are independent real numbers in (0,1), with the other post-K2 terminal time being 5.

For FULL upstream real controls 0<=x,b<=1 and 0<=i<=1-x, put

    w_s=(1/4,(1-x)/4,b/8,i/8), d=b/16+3i/32,
    Q_s=w_s alpha_s z_s,  S_s=c Q_s t_s,  0<=z_s,t_s<=1.

LR sets b=y, i=(1-x)y, z_s=z and t_s=t, where x,y,z,t range over [0,1]. Exact physical path sums established by the predecessor give

    e_P=107/128 - 21x/128 + d/4 - sum_s p_s S_s,
    e_Q=13/64 + 3x/64 - d/2 + sum_s q_s S_s/4,
    T_P=3 + sum_s Q_s + sum_s (1+a_s) S_s,
    T_Q=3 + (sum_s Q_s)/2 + sum_s (1+b_s) S_s/4.       (1)

The source labels are preserved before taking this observer readout.

## Theorem 1: universal delay-ratio rigidity (all real kernels and strategies)

Let the four positive maximal source weights be

    W_s=(1/8,1/6,1/16,3/32),  W=sum_s W_s=43/96,
    rho_s=(1+b_s)/(1+a_s),  m=min_s rho_s,  M=max_s rho_s.

For EVERY admissible real kernel with m<M there is an explicit pure-time normal n=(0,0,-u,4) satisfying h_FULL(n)>h_LR(n). Thus equality of the entire four-dimensional observer convex hulls requires equality of all four ratios rho_s. This necessary condition is independent of the eight answer parameters p_s,q_s, and separation already occurs in the time-only projection (T_P,T_Q).

Construct

    epsilon=min((M-m)/2, 3*(2-m)/14), u=m+epsilon,
    h=2-u, k_s=(1+b_s)-u*(1+a_s),
    Kplus=sum_s W_s max(k_s,0),
    Kminus=sum_s W_s max(-k_s,0).

Since all rho_s lie in (1/2,2), m<u<M<2, and k_s=(1+a_s)(rho_s-u)>-2epsilon. Therefore

    h+c min(0,k_s)>(2-m)-(1+2c)*epsilon >= (2-m)/2>0

for all sources. Both Kplus and Kminus are strictly positive.

The EXACT all-real support values and positive gap are

    h_FULL(n)=12-3u + h*W + c*Kplus,
    h_LR(n)  =12-3u + h*W + c*max(Kplus-Kminus,0),
    DELTA(n) =c*min(Kplus,Kminus)>0,  c=2/3.              (2)

PROOF. From (1),

    n dot O = 12-3u + sum_s Q_s (h + c*t_s*k_s).

Every parenthesized coefficient remains positive for every real t_s in [0,1]. Hence the FULL maximum takes x=0, b=i=1, z_s=1, and separately takes t_s=1 where k_s>0, otherwise 0. The LR maximum likewise takes x=0, y=z=1, after which a single shared t maximizes t*sum_s W_s k_s. The two optimizations yield (2), for all real history-adaptive policies. The choice m<u<M makes positive and negative k_s both occur, so DELTA>0. QED.

The predecessor normal v=(0,0,-1,4) detects the mixed-sign structure of b_s-a_s. The tilted ratio normal in (2) can detect nonconstant but entirely one-sided delay changes that v misses.

## Theorem 2: universal all-signed FULL support oracle

For any real four-normal n=(n0,n1,n2,n3) and arbitrary admissible real kernels let

    B = 107n0/128 + 13n1/64 + 3(n2+n3),
    hx=-21n0/128 + 3n1/64,  hd=n0/4 - n1/2,
    h=n2+n3/2,
    k_s=-n0*p_s+n1*q_s/4+n2*(1+a_s)+n3*(1+b_s)/4,
    L_s=max(0,h+c*max(0,k_s)).

Then the exact support over ALL FULL real behavioral strategies is

    h_FULL(n)=B + L_C/8 + max(0,(hd+L_BJ)/16)
                 + max(hx, L_I/6 + max(0,3*(hd+L_IJ)/32)). (3)

PROOF. Optimize each source-dependent downstream K2 control t_s and then K1 control z_s, producing the coefficient L_s. The remaining upstream objective is the affine expression

    B + L_C/8 + hx*x + (L_I/6)*(1-x)
      + ((hd+L_BJ)/16)*b + (3*(hd+L_IJ)/32)*i.

Optimize b∈[0,1], i∈[0,1-x], then x∈[0,1], yielding (3). LR's observer map is multi-affine in its four shared controls (x,y,z,t), so its support is the maximum of exactly 16 deterministic LR corner values. Equation (3) and those 16 values supply an exact all-signed support-gap oracle for any rational kernel and rational normal; the formula itself holds for real kernels and normals. QED.

## New exact one-sided rational witness

Take p_s=q_s=1/2, all a_s=1/4, and b=(1/4,1/4,1/2,1/4). Then b_s-a_s>=0 for all s and the predecessor time normal v=(0,0,-1,4) has support gap zero.

Here rho=(1,1,6/5,1) and the constructive normal is n=(0,0,-11/10,4). Precisely

    h=9/10; k=(-1/8,-1/8,+1/8,-1/8),
    Kplus=1/128; Kminus=37/768;
    h_FULL(n)=1093/120; h_LR(n)=2913/320; DELTA=1/192.

The FULL policy x=0,b=i=1,z_s=1, t_BJ=1, t_C=t_I=t_IJ=0 yields the ACTUAL four-observer witness

    W=(41/48,25/192,7/2,311/96), n dot W=1093/120.

Since ||n||_1=51/10, the valid exact distance lower bound is

    dist_infinity(W,conv O(LR)) >= (1/192)/(51/10)=5/4896.

Every non-decision natural transition remains strictly positive, and the three original LR collision keys are unchanged.

## Verification, open scope and continuation

VERIFY.py is the executed standalone Python Fraction verifier; EXACT_OUTPUT.txt is its actual output. Five strictly positive rational kernels were tested. Each uses all 2048 FULL raw deterministic assignments and 16 LR corners; four or five exact signed normals per kernel are checked against (3), and the constructive time-ratio gap (2) is checked when m<M. The rational witness, vanishing predecessor normal, and exact support/distance values are separately asserted. The output records 85 explicit exact equalities (enumeration sizes are stated separately). Analytic proofs support the universal real-parameter claims; finite computations crosscheck them in the declared rational cases.

Next: restrict the next route to ratio-balanced kernels b_s=rho(1+a_s)-1 and analyze remaining signed normals with (3) and the 16 LR corners. The diagonal-delay predecessor has constant rho yet another global gap; thus ratio-balance is necessary, and the remaining convex-hull classification is open. For any candidate, provide exact LR convex combinations for ALL FULL vertices or a rational Farkas normal. Actual real-image nonmembership remains a subsequent independent issue. This record establishes no native CLAIM, Result, review, or canonical mathematical admission.
