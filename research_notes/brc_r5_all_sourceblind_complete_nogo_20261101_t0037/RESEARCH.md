# R5 complete all-real source-blind terminal-response exclusion theorem

Date: 2026-11-01 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is a theorem in an auxiliary finite two-measure stopping model, NOT a native X6 or three-dimensional-slice theorem.

Frozen input: GLOBAL_KNOWLEDGE_V1 main@581bf324a7e1d2a4c4c11bb468b2b04e1d2362b3; Enterprise Math main@42da097851a02b96f8ff2018f5c28096eec13866. Read canonical bootstrap/manual, project bootstrap, P000 V4, ACTIVE worldview, current portable and mathematical protocols. P000 and worldview unchanged. Earlier immutable author results: 1dcf7491cefa861c00468a4985812e73d1965849 (3-response result), 9dda1142caa6f4e167b9ca2c4b62a1fb7a05d332 (terminal interpolation necessity). Independent derivations of both branches are supplied below.

The native gateway reported research_authority_granted=false and executor_binding_configured=false, code status CODE_REVIEW_REQUIRED. Owner listing returned CONTROL_QUOTA; native session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. No formal CLAIM/Result/Driver acceptance is asserted.

## Exact finite model and statement

Two hidden origins each have P=Q initial weight 1/2. Their parameters are (alpha0,kappa0)=(1/4,3/4) and (alpha1,kappa1)=(1/5,1/6), and theta_i=[1+kappa_i(1-2alpha_i)]/alpha_i=11/2=theta. At common observable A (time 1, likelihood ratio 1), choose STOP at A, or CONTINUE to D,C,Y at time 2 with Q fractions (alpha_i,1-2alpha_i,alpha_i) and likelihood ratios (1/2,1,3/2). At D STOP at D or CONTINUE to DH (Q 2/3, time 3, likelihood ratio 1/4) and L (Q 1/3, time 3, ratio 1). At Y STOP at Y or CONTINUE to YH (Q 1/2, time 3, ratio 2) and L (Q 1/2, time 3, ratio 1). At C nature STOPs at C (fraction 1-kappa_i, time 2, ratio 1) or enters L (fraction kappa_i). At L STOP at time 3 or CONTINUE to L4 at time 4, both ratio 1. P mass of each terminal leaf is its Q mass multiplied by its stated ratio; P=Q=1 globally. All natural transitions are strictly positive.

FULL has separate (A,D,Y,LD,LY,LC) binary actions for each source, 4096 deterministic policies. Seedless LR has common (A,D,Y,L) binary actions, 16 deterministic policies, with no persistent random seed. Every information key is visited at most once; each real behavioral-policy linear score is multi-affine, so a support maximum occurs at a deterministic vertex.

Let r=(r_A,r_D,r_Y,r_C,r_DH,r_YH,r_L,r_L4) be ANY source/route-independent legal real terminal error probability vector in [0,1]^8, shared across P and Q. Define O=(e_P,e_Q,T_P,T_Q), where e_S=E_S[r], T_S=E_S[terminal time].

THEOREM: for every such r, EITHER conv(O_FULL) != conv(O_LR), OR the affine rank of conv(O_LR) is at most 3. Thus the original mother target requiring simultaneously equal FULL/LR 4-observer hulls and rank-four LR observations is impossible for the ENTIRE legal eight-dimensional source-blind response cube on this fixed compensated topology. We do not claim that singular lower-rank images necessarily have unequal hulls.

## 1. Positive carrier flow and its real residual

Retain origin/route labels in positive Q terminal flows. Define x=Q(DH), y=Q(L4), u=Q(YH), t=T_Q, and B=sum_i (1/2)alpha_i a_i where a_i is source-i probability of continuing at A. Direct mass and time conservation gives, for every deterministic, real behavioral and mixed policy,

Q(D)=B-3x/2; Q(Y)=B-2u;
t=1+theta*B+3x/2+2u+y;
B=[t-1-y-3x/2-2u]/theta.

Let b_i=(1-2alpha_i)(1-kappa_i)=2-(theta+2)alpha_i. Then Q(C)+2Q(A)=2-(theta+2)B. Also T_P-T_Q=u-3x/4, by time reference 3, the two normalizations, and the D,Y terminal likelihoods.

Consequently fixing (x,y,u,t) fixes D,Y,DH,YH,L4 and C+2A. The only possible terminal-mass fiber is supported at (A,C,L) with difference (h,-2h,h); all three have likelihood ratio 1, so this fiber preserves P and Q normalization and both stopping times. It is a genuine source/history residual, not an observer or implementation error.

In particular, FULL has terminal-mass affine rank 5, LR has rank 4; the four-coordinate carrier itself has LR rank 4. The LR controls 0000,1000,1001,1010,1100 give a four-dimensional difference minor exactly -50787/10240000. To exhibit the fifth FULL direction, take D,Y STOP everywhere and compare two legal real FULL policies: X continues at source0 A with probability 4/5 and source1 A with probability 0; Y continues at source0 A with probability 0 and source1 A with probability 1. Both give (x,y,u,t)=(0,0,0,31/20), but Q_X(C)=1/20 and Q_Y(C)=1/4. Their only terminal-flow differences (A,C,L) are (1/10,-1/5,1/10).

## 2. Gamma=0: universal 4D factorization and separation

Define gamma=2r_C-r_A-r_L. If gamma=0, then r_A-r_L=2(r_C-r_L), so both e_P and e_Q annihilate (h,-2h,h). Put d=B-3x/2, qY=B-2u, S=r_L+(r_C-r_L)[2-(theta+2)B]. Exact leaf summation gives

e_Q=S+(r_D-r_L)d+(r_Y-r_L)qY+(r_DH-r_L)x+(r_YH-r_L)u+(r_L4-r_L)y,
e_P=S+(r_D-r_L)d/2+(r_Y-r_L)3qY/2+(r_DH-r_L)x/4+2(r_YH-r_L)u+(r_L4-r_L)y,
T_P=t+u-3x/4, T_Q=t.

Thus O=M_r(x,y,u,t) for a real affine map M_r:R4->R4. If its linear rank is <4, LR observed affine rank is <=3. Otherwise M_r is invertible, since LR carrier rank is exactly 4. Define F(x,y,u,t)=985x/8+70y-130u-23t. Exhaustion of the 16 LR deterministic vertices gives max_LR F=-23; eight A-STOP policies attain it and the other eight are strictly lower. The legal FULL policy with source0 actions (1,1,0,1,0,1), source1 all STOP has (x,y,u,t)=(1/12,11/48,0,49/24) and F=-661/32. Its exact gap to LR support is 75/32 >0. Multi-affinity extends the LR maximum to all real behavioral policies. When M_r is invertible, the signed affine functional F composed with M_r inverse separates FULL from the entire LR four-observer convex hull, with the same gap 75/32. This gap is NOT a uniform normalized observed-space distance when M_r approaches singularity.

## 3. Gamma!=0: universal explicit signed Bellman separation

For H=(p,q,h_P,h_Q), let a terminal key j have Q-weighted score w_j=(p lambda_j+q)r_j+(h_P lambda_j+h_Q)time_j. Define L*=max(w_L,w_L4), D*=max(w_D,(2w_DH+L*)/3), Y*=max(w_Y,(w_YH+L*)/2). Origin-specific continuation gain at A is G_i=alpha_i(D*+Y*)+b_i w_C+c_i L*-w_A, where b_i=2-(theta+2)alpha_i and c_i=theta alpha_i-1. FULL optimizes A separately by source; LR uses common A. All downstream optimal decisions are shared because their conditional kernels are source-independent. Therefore the exact support gap is Delta(H)=(|G_0|+|G_1|-|G_0+G_1|)/4.

Choose the SAME rational s=1/16 for EVERY legal response. Put abar=alpha0+alpha1=9/20,
xi=r_D+r_YH/2-3r_L/2-(theta+2)(r_C-r_L),
tau=theta-s(xi+2gamma/abar),
H_r=(0,s,2(tau+1),-(2tau+3)).

For 0<=r_j<=1, |xi|<=theta+2=15/2 and |gamma|<=2. Hence tau>=1289/288>1. At H_r the L optimum is uniquely STOP, the D optimum uniquely STOP and the Y optimum uniquely CONTINUE: time scores dominate bounded s error increments. Direct substitution yields
G_i=alpha_i(tau-theta)+s(gamma+alpha_i xi);
G_0=-s gamma/9=-G_1.
So the exact support gap at the explicit legal direction H_r is
Delta(H_r)=|gamma|/288>0 for EVERY response with gamma!=0.

Combining the exhaustive gamma=0 versus gamma!=0 cases proves the theorem for every real r in [0,1]^8. QED.

## Verification, BRC typing, and open objective

The actually executed standalone Python Fraction verifier in VERIFY.py and stdout in EXACT_OUTPUT.txt check P/Q normalization and all identities for all 4096 FULL +16 LR deterministic policies, LR four-carrier minor, FULL5/LR4 terminal mass ranks, exact behavioral hidden-fiber pair, four independent rational gamma=0 response configurations (factorization on 4112 policies each), original carrier separator and three gamma!=0 rational exact Bellman support cases. The all-real result follows from symbolic conservation identities and universal bounds, NOT finite sampling. The positive source/route-labelled flow carrier and dual signed separating functional are mathematically separate; no conversion of signed score into negative branch probability is allowed. Native BRC arithmetic, X6 embedding, third slice coordinate, physical clocks, novelty or independent admission are NOT claimed.

Next: stop adding source-blind error coordinates on this compensated topology. Study a route-sensitive response at shared L (D/Y/C ingress distinguished in the observation law while the seedless LR policy still cannot distinguish it), or change the positive transition topology. Calculate augmented carrier dimensions and exact observer kernels; require <=5-vertex rational LR decompositions for all FULL vertices to certify 4D hull equality, otherwise produce rational Farkas separation. Only after full hull equality should actual real LR-image nonmembership be attempted. Original mother question remains open.