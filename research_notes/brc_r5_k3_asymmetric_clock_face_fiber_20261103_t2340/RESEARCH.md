# R5 K3 — An asymmetric eight-clock open no-go chamber via an exposed error fiber

Date: 2026-11-03 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Provenance and scope

Predecessor: Enterprise Math immutable commit c87447eb778e2935dde85855b658a1b47bb88dbd; research_notes/brc_r5_k3_exposed_clock_face_no_go_20261103_t2235/RESEARCH.md, PR #1663. Frozen *scientific* pins remain GK a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. Current behavioral rules were separately refreshed. P000 / ACTIVE X6 Heartbeat worldview is untouched. This result concerns the specified strictly positive finite P/Q single-common-terminal-label auxiliary experiment, with no claimed native X6 physical realization.

Four provenance-preserving positive BRC sources, in order C,I,BJ,IJ, have carrier maxima c=(1/8,1/6,1/16,3/32). Put w=(1/4,(1-x)/4,y/8,i/8), alpha=(1/2,2/3,1/2,3/4), d=y/16+3i/32. FULL allows 0<=x,y<=1, 0<=i<=1-x and individual z_s,t_s,u_s in [0,1]. Seedless LR imposes i=(1-x)y and common z,t,u. Put M_s=w_s alpha_s z_s, S_s=(2/3)M_s t_s, U_s=S_s u_s. For independent p_s,q_s,r_s,v_s in (0,1), all four readouts are

    eP=107/128-21x/128+d/4-sum(S)/2+sum_s p_s S_s/8
    eQ=13/64+3x/64-d/2+sum(S)/8+sum_s q_s S_s/32
    TP=3+sum(M)+(3/2)sum(S)+sum_s r_s U_s
    TQ=3+sum(M)/2+(3/8)sum(S)+sum_s v_s U_s/4.

## Theorem: strict threshold crossing excludes four-dimensional convex-hull equality

For s=C,I,BJ,IJ define mu_s=(9+2*v_s)/(8*(3+r_s)). If

    max(mu_C,mu_I) < min(mu_BJ,mu_IJ,3/8),

then for every p,q in (0,1)^4, conv O(FULL) != conv O(LR). More precisely choose any m strictly inside that interval, let

    A_s=2m-3/4+(4*m*r_s-v_s)/6,
    g=min{A_I/6,-A_BJ/16-3*A_IJ/32}>0,
    epsilon=g/2,
    n=(epsilon,0,m,-1).

There are actual deterministic FULL and LR observations W,H with

    W-H=(5/128,-5/64,0,0),
    h_LR(n)=n.H,
    n.W-h_LR(n)=5*epsilon/128>0,
    dist_infinity(W,conv O(LR))>=5*epsilon/(128*(1+m+epsilon))>0.

This holds for all *real* admissible parameters satisfying the condition, not merely rational instances. In particular, full convex-hull equality requires the strict interval above to be empty.

### Proof

For time normal n0=(0,0,m,-1), the nested source-stage scores per unit positive carrier are V0=0, V1=m-1/2, V2=2m-3/4, V3_s=2m-3/4+(4*m*r_s-v_s)/6. Since m<3/8, V1,V2<0. The sign of V3_s is that of m-mu_s (multiply by positive 8(3+r_s)), so V3_C,V3_I>0 and V3_BJ,V3_IJ<0.

FULL's optimal stages are (3,3,0,0), and source carriers C and I simultaneously reach their maxima at upstream (x,y,i)=(0,1,1). Denote this actual observation W. Its clock support is 3(m-1)+c_C A_C+c_I A_I. LR attains the same score at upstream (0,0,0), common stage 3, with carriers (c_C,c_I,0,0); call that observation H. All other LR deterministic vertices have strictly smaller clock scores. Comparing the four upstream corners at stage 3 yields the minimum clock deficit

    g=min(c_I A_I,-c_BJ A_BJ-c_IJ A_IJ)>0.

Stages 0,1,2 cannot beat H because their contributions are 0, negative, negative. Under LR, fixed-stage upstream contributions are bilinear in x,y (with i=(1-x)y), and the nested continuation controls are multi-affine. Every real behavioral observation admits the relevant deterministic convex decomposition. Thus H is the *unique LR clock-exposed observation*, and W is a FULL clock maximizer.

At W and H the x-coordinate, C/I source contributions M,S,U, and both times agree. Both policies have zero BJ/IJ contributions. Only the upstream residual d differs: d(W)=5/32, d(H)=0. Therefore W-H=(5/128,-5/64,0,0), for every choice of p,q.

For every admissible LR observation Z, 0<eP(Z)<1. Indeed sum S<=43/144, 0<=d<=5/32 and 0<p_s<1 imply

    43/64-43/288 <= eP(Z) <= 7/8+43/1152 <1.

Thus for every *other* LR deterministic vertex Z, the mixed-normal margin obeys

    n.H-n.Z >= g-epsilon*|eP(H)-eP(Z)| > g/2>0.

So H remains the unique support maximizer for the perturbed normal n. At W, n.W-n.H=5*epsilon/128. The infinity-distance bound follows by Hölder duality with ||n||_1=1+m+epsilon. QED.

## New nonproportional and fully source-distinct exact instance

Set r=(4/5,7/10,1/5,3/10), v=(2/5,1/3,1/10,1/5), and p=q=(1/2,1/2,1/2,1/2). Neither r nor v is source-uniform, and v_s/r_s is not constant. At m=1/3, thresholds are

    mu=(49/152,145/444,23/64,47/132)

and source scores are A=(1/36,1/60,-1/18,-1/20). Hence g=1/360 and epsilon=1/720. One actual FULL observation W and the sole LR clock-face observation H are

    W=(455/576,39/256,671/180,13981/4320)
    H=(865/1152,59/256,671/180,13981/4320).

For n=(1/720,0,1/3,-1), complete exact finite deterministic enumeration confirms

    h_FULL(n)=-826393/414720
    h_LR(n)=-1652831/829440
    h_FULL(n)-h_LR(n)=1/18432
    dist_infinity(W,conv O(LR))>=5/123008.

Robustness: if each of the eight clock coordinates r_s,v_s varies by strictly less than 3/70 in absolute value, all parameters remain in (0,1), and the sign of every A_s at m=1/3 remains unchanged. Indeed |delta A_s|<((4/3)+1)*(3/70)/6=1/60, no larger than the smallest original |A_s|=1/60. Thus a full open eight-clock cube, with *arbitrary* p,q in (0,1)^4, is excluded from four-dimensional convex-hull equality. This is an open 16-real-parameter family of no-go auxiliary experiments.

## Evidence and interpretation

The attached standard-library Fraction VERIFY.py actually ran on three rational configurations (1,536 FULL and 16 LR deterministic vertices each): common-label base kernel, independent p/q answer variation, and a nonproportional clock perturbation. 68 exact assertions passed, including face uniqueness, threshold signs, exact witness, signed gap, and distance certificate. The universal theorem is proved analytically; this finite run checks the enumerated instances. BRC resolution: REUSE_APPLIED (labeled positive source carrier with provenance-aware upstream masking and observer fiber). The native Enterprise Math Site at 2026-11-03T15:40Z remained static_machine_readonly, research_authority_granted=false; owner query returned CONTROL_QUOTA, so no live owner/CLAIM/Result/Driver admission is claimed. The mother objective remains open. See NEXT_TASK.md.
