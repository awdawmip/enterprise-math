# R5 K3 — Complete signed clock plane and a nonuniform clock-hull equality family

Date: 2026-11-03 Asia/Shanghai.
Scope/status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Scientific inputs and original experiment

Immediate immutable scientific predecessor: Enterprise Math commit edc14f20b97725f855886aba1d12fb635b6d20be, research_notes/brc_r5_k3_dual_clock_normal_20261103_t2042/RESEARCH.md (PR #1663). Frozen task science pins: Global Knowledge a01383f825ef9d43b4b754254303298c64041568, Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Current norms are independently re-read; protected P000 and ACTIVE worldview unchanged.

We retain the strict common terminal label P/Q finite experiment and four hidden source labels C,I,BJ,IJ. Source carrier maxima c=(1/8,1/6,1/16,3/32), alpha=(1/2,2/3,1/2,3/4), and w=(1/4,(1-x)/4,y/8,i/8). FULL has real x,y in [0,1], i in [0,1-x], and sourcewise z_s,t_s,u_s in [0,1]. Seedless LR has i=(1-x)y and shared z,t,u. Put M_s=w_s alpha_s z_s, S_s=(2/3)M_s t_s, U_s=S_s u_s, d=y/16+3i/32. All p_s,q_s,r_s,v_s are strictly between 0 and 1. The four observer coordinates are:

    eP=107/128-21x/128+d/4-(sum S)/2+sum_s p_s S_s/8
    eQ=13/64+3x/64-d/2+(sum S)/8+sum_s q_s S_s/32
    TP=3+sum M+(3/2)sum S+sum_s r_s U_s
    TQ=3+(sum M)/2+(3/8)sum S+sum_s v_s U_s/4

These are exact readouts for the already constructed modified common-label finite probability experiment. Native X6 physical realization is a separate unresolved correspondence question.

## Theorem 1: exact complete signed clock plane, all real parameters

For an arbitrary real signed normal n=(0,0,a,b), define four source-stage scores per unit carrier:

    V0=0
    V1=a+b/2
    V2=2a+3b/4
    V3_s=2a+3b/4+(2/3)a r_s+(1/6)b v_s.

Let H be the four LR carrier vectors obtained from (x,y,i)=(0,0,0),(0,1,1),(1,0,0),(1,1,0). Then, for ALL eight real time-kernel parameters (r,v) in (0,1)^8 and all (a,b) in R^2,

    h_FULL(n)=3(a+b)+sum_s c_s max(0,V1,V2,V3_s)
    h_LR(n)=3(a+b)+max_{h in H, j=0,1,2,3} sum_s h_s Vj_s.

Proof: At each source, the behavioral objective is multi-affine in nested z_s,t_s,u_s; deterministic scores collapse to the stages 000,100,110,111. For FULL, the nonnegative optimum beta_s=max_j Vj_s is weighted by w_s alpha_s<=c_s. Simultaneous carrier equality is attained at the feasible FULL corner x=0,y=1,i=1, so this corner maximizes the complete clock support. For LR, deterministic stage choice j is common to all sources. For a fixed stage, the upstream objective is bilinear in x and y under i=(1-x)y, so its maximum occurs at one of four listed corners. Multi-affine convex decomposition proves the formulas over all REAL behavioral strategies, not merely binary samples.

Complete fixed-rational-kernel criterion: each support is a maximum of finitely many linear forms in (a,b). Conic chamber boundaries lie among normals perpendicular to source-stage point differences and LR stage/corner point differences; add coordinate axes. Checking equality on both signed ray directions for all these boundaries is sufficient for equality on EVERY real signed clock direction, since both supports are linear inside each chamber and positively homogeneous. For the rational example below this produces 104 exact rays, not an angle grid.

## Theorem 2: continuous family of equal clock-projection convex hulls with nonuniform sources

For arbitrary REAL parameters 0<L<=R<1 and 0<k<=1 with kR<1, take

    r=(R,R,L,L),  v=k*r,

ordered C,I,BJ,IJ. For EVERY signed real (a,b),

    h_FULL(0,0,a,b)=h_LR(0,0,a,b).

Hence the two-dimensional convex hulls of the (TP,TQ) projections are EXACTLY equal, even when R>L and the sources have genuinely different clock kernels.

Proof. If a,b are both nonnegative, stage 3 at full-carrier LR corner attains FULL; if both nonpositive, stage 0 does. On a<0,b>0 set b=1, m=-a/b. Stage values are V1=1/2-m, V2=3/4-2m, V3_s=V2+r_s(k-4m)/6. Since 0<k<=1, a single common stage maximizes ALL sources: stage 3 for m<=k/4, stage 2 for k/4<=m<=1/4, stage 1 for 1/4<=m<=1/2, stage 0 for m>=1/2. Every common stage is realizable at x=0,y=1,i=1.

On a>0,b<0 set -b=1, m=a/(-b). Values are V1=m-1/2, V2=2m-3/4, V3_s=V2+r_s(4m-k)/6. For m<=k/4, stages 1,2,3 are nonpositive and stage 0 works. For m>=3/8, stage 3 is maximal for all sources and the full-carrier corner works. In k/4<m<3/8, stages 1 and 2 are negative. Since 4m-k>0 and R>=L, V3(R)>=V3(L). The positive stage-3 source set is therefore one of NONE, exactly {C,I}, or ALL. Each mask is attainable by an LR policy: common stage 0; stage 3 at upstream (0,0,0), giving precisely carriers (c_C,c_I,0,0); or stage 3 at (0,1,1), giving all c_s. Thus LR attains the FULL componentwise optimum in every direction. Axis boundaries are covered by the same stage choices. QED.

The particular source grouping C/I is load-bearing: the actual LR upstream mask can suppress BJ and IJ together. Arbitrary permutations of r need not share this equality.

## Exact example: all time-only directions agree, mixed 4D observers separate

Use positive rational parameters

    r=(4/5,4/5,1/5,1/5),  v=(2/5,2/5,1/10,1/10),
    p=(1/4,1/2,3/4,1/2), q=(3/4,1/2,1/4,1/2).

The clock hull is the same 5-vertex polygon under FULL and LR, counterclockwise:

    (3,3)
    (673/180,4663/1440)
    (733/180,9671/2880)
    (187/48,427/128)
    (331/96,619/192)

The SAME actual FULL policy x=0,y=1,i=1, source stages (3,3,1,1), produces four-dimensional observer

    W=(907/1152,235/1536,5609/1440,9551/2880).

Two distinct mixed error/clock normals give exact signed strict hull separation:

    nP=(8,0,28/9,-56/9):
       h_FULL=-1597/720, h_LR=-821/360, gap=1/16, nP.W=h_FULL.
    nQ=(0,-32,4,-8):
       h_FULL=-3803/240, h_LR=-3823/240, gap=1/12, nQ.W=h_FULL.

Hölder duality gives distance_infinity(W, conv O(LR)) >= max((1/16)/(52/3),(1/12)/44)=3/832. Hence an entire two-dimensional all-signed clock-hull equality can coexist with strict FOUR-dimensional hull inequality in the same finite P/Q experiment. This is a scoped counterexample to using clock-plane support equality as a sufficient full-hull test, not a solution to the mother target (which requires equal full 4D convex hulls but different actual 4D images).

## Verification scope, reuse and limitations

The accompanying independently executed standard-library Fraction VERIFY.py performed 2,886 exact assertions, last line PASS_EXACT_R5_K3_FULL_CLOCK_PLANE_EQUAL_NONUNIFORM_FAMILY. It enumerates 1,536 FULL and 16 LR deterministic time points, proves their equal 5-vertex exact convex polygons for the rational kernel and checks every FULL point against the LR polygon; checks all 104 normal-fan rays and 5 additional rational family kernels (484 rays); independently checks the formula against complete finite enumeration for 3 clock kernels; and enumerates complete 1,536 FULL / 16 LR four-observer choices for both mixed witness normals. Analytical proofs above establish the ALL-REAL statements; finite assertions crosscheck the specified rational data and the exhaustive fixed-kernel fan only.

No literature novelty, native physical proof, independent Driver acceptance, formal Source CLAIM or Result is asserted. Authenticated GitHub user awdawmip has admin/push permissions. The Enterprise Math Site as observed 2026-11-03T13:49Z is static_machine_readonly with research_authority_granted=false, and bounded current owner query returned CONTROL_QUOTA. This PR branch is portable author evidence, not native admission.

Next unit: vary p,q and the nonuniform R,L,k family and perform all-signed FOUR-dimensional convex hull containment, requiring a rational <=5-LR-vertices mixture for every FULL deterministic observer or an exact rational Farkas separator. Only if 4D hull equality survives should actual real-image nonmembership be tested. See NEXT_TASK.md.
