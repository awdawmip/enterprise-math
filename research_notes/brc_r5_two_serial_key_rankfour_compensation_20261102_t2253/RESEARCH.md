# R5 — Two serial continuation gates: full-rank equal images and an exact source perturbation separator

Date: 2026-11-02 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Provenance and scope

Direct scientific predecessor: awdawmip/enterprise-math commit 1853681d7f517559269eda5532544bec04334535, research_notes/brc_r5_postdecision_j_reward_rank_barrier_20261102_t2206/RESEARCH.md and NEXT_TASK.md. Preserve frozen scientific source pins: global a01383f825ef9d43b4b754254303298c64041568 and enterprise-math 86149263e38c22292c9def1e0f69092efa1be77e. Current behavioral control was separately read on global main 37fc58c1e0eee8d1211f034946bff2d3cae2458c and enterprise-math main e6f675caf4a340766d117d16c859c1f9c06b2512.

The predecessor established a full-rank separation for four affine aggregates with one continuation statistic. This new auxiliary BRC model has two *serial, interacting* continuation decisions and four raw observers. Its results concern this precise model: correspondence to the physical two-law (eP,eQ,TP,TQ) stop model, its likelihood-ratio/time partitions, and native X6 remain separate questions. P000, ACTIVE worldview and scientific admission remain unchanged.

## Source-labelled BRC model and legitimate natural probabilities

The first three FULL controls x,jB,jI are in [0,1]. Put b=1-jB and i=(1-x)(1-jI). Source masses for C,I,BJ,IJ are w=(1/4,(1-x)/4,b/8,i/8). Let alpha=(a0,aI,betaB,betaI) belong to (0,1)^4, and c belong to (0,1). At first downstream decision K1, FULL may choose independent z_s in [0,1]; after nature success with probability alpha_s, a second downstream decision K2 chooses independent t_s in [0,1]. The natural K2 success probability is gamma_s/alpha_s: gamma_s=c alpha_s for all sources except gamma_BJ=c betaB+epsilon. Require 0<=epsilon<betaB(1-c), so every natural probability at both stages is strictly in (0,1).

Define d=(betaB*b+betaI*i)/8, H(x)=a0/4+aI(1-x)/4, A=H(x)+d, r1=sum_s w_s alpha_s z_s, r2=sum_s w_s gamma_s z_s t_s. The declared four-score auxiliary observer is O=(x,d,r1,r2). Its branch provenance is retained in the model even when these four coordinates are read out. The LR-like restricted class shares J control y and downstream controls z,t across all source labels: b=y, i=(1-x)y, r1=Az, r2=zt(cA+epsilon*y/8). The two downstream controls are distinct and serial; K2 decisions occur only after K1 continuation. In this declared information quotient the controls collide across sources. A legal two-law/time-likelihood-ratio realization is not assumed here.

## Theorem 1: complete real-policy image equality at proportional source kernels

For every real a0,aI,betaB,betaI,c in the stated strict domain, epsilon=0 implies

    O(FULL)=O(LR), and therefore conv O(FULL)=conv O(LR).

Proof. From a FULL policy, take y=(betaB*b+betaI*i)/(betaB+betaI(1-x)). Since 0<=b<=1 and 0<=i<=1-x, 0<=y<=1. The LR policy then has the same x,d,A. In FULL, 0<=r1<=A and 0<=r2<=c*r1. Since A>=a0/4>0, set z=r1/A, t=r2/(c*r1) if r1>0 and t=0 otherwise. These are valid LR controls, preserving x,d,r1,r2 exactly. Any LR policy embeds in FULL by assigning the shared controls to all labelled sources, proving both inclusions.

Moreover, for fixed (x,b,i), the FULL attainable (r1,r2) fiber is *exactly* the triangle 0<=r1<=A, 0<=r2<=c*r1. Sufficiency is obtained by taking all z_s=r1/A and all t_s=r2/(c*r1) for r1>0. Thus the proportional-kernel reduction is safe for these declared observers, not an assertion that source distinctions disappear for every future operation.

Four-dimensionality: in LR variables (x,y,z,t), put D=(betaB+betaI(1-x))/8>0. The determinant of the Jacobian of (x,d,r1,r2) is D*A*(c*A*z)=c D A^2 z. It is nonzero for any interior x,y,z,t with z>0. Thus both full and restricted actual images contain four-dimensional open sets. This construction passes the dimension obstruction of the prior *single*-statistic theorem while satisfying a stronger actual-image equality.

## Theorem 2: an exact full-continuum one-source perturbation separation

Set B=betaB+betaI, H0=(a0+aI)/4, and define the signed four-coordinate direction

    n_e=(c*aI/4-epsilon*betaI/(8B), -(c+epsilon/B), 0, 1).

For every real epsilon in [0,betaB(1-c)), every real behavioral policy obeys the exact support identities

    h_LR(n_e)=c*H0,
    h_FULL(n_e)=c*H0+epsilon*betaI/(8B).

In particular the exact support-function gap is epsilon*betaI/(8B), strictly positive for every epsilon>0.

Proof. With gamma_s=c alpha_s except BJ, nonnegativity of labelled flow gives r2<=c(H(x)+d)+epsilon*b/8. Substitute into the direction: direct cancellation gives

    n_e dot O <= c*H0+[epsilon*betaI/(8B)]*(b-i-x).

For FULL, b-i-x<=1, attained at x=0,b=1,i=0; all z_s=t_s=1 also attains equality in the bound. For LR, b=y and i=(1-x)y, hence b-i-x=-x(1-y)<=0, attained at x=0 with z=t=1. Both upper bounds are exact. Thus the support formula holds over all real controls, independently of finite sample coverage.

## Strictly positive rational case, distance and exact regression

Take alpha=(1/2,2/3,1/2,3/4), c=2/3, B=5/4 and H0=7/24. For epsilon=0, the exact real observer images coincide and have rank four. At x=y=z=t=1/2, D=7/64, A=101/384, and the exact positive Jacobian is 71407/28311552.

For epsilon=1/8, the BJ conditional natural K2 success probability is 11/12, and all natural kernels are strictly between zero and one. The exact separating normal and FULL witness are

    n=(293/2880,-23/30,0,1),
    W=(0,1/16,17/48,145/576).

Exact supports are h_LR=7/36=560/2880 and h_FULL=587/2880, giving gap 3/320. The L-infinity distance from W to the entire LR convex hull is at least (3/320)/(5381/2880)=27/5381.

Actual Python standard-library Fraction execution of VERIFY.py produced PASS_EXACT_R5_TWO_SERIAL_GATE_COMPENSATION_AND_PERTURBATION, with 6477 exact assertions. The verified finite domain includes all 2048 FULL deterministic policies and all 16 LR deterministic policies at epsilon=0, with an explicit *16-term rational Bernoulli convex representation* for every FULL vertex; 100 noncorner exact behavioral lifts; support enumeration at epsilon=0,1/96,1/32,1/12,1/8; exact nonzero Jacobian and a rational distance witness. Finite-horizon multi-affinity ensures that support functions attain maxima on deterministic corners, so this enumeration also checks the analytic support formula in those five parameter cases. The universal real-policy results follow from the displayed algebra. No Lean theorem, independent Driver review, physical model embedding or native research admission has been claimed.

## Current authority and next step

Authenticated connected GitHub account: awdawmip, permission admin in enterprise-math. Current native Enterprise Math DIRECTED_RESEARCH context reports authority_granted=false and the bounded owner/task query returned CONTROL_QUOTA; active Source owner was not certified. This is author-side portable research in existing R5 Draft PR #1663. No native CLAIM/Result/independent review is asserted.

Next: construct a genuinely legal finite-horizon two-law P/Q stopped-path tree with explicit (time,likelihood-ratio) keys at *both* serial gates and four physical observers (eP,eQ,TP,TQ). Prove or refute an invertible affine mapping from that four-observer vector to (x,d,r1,r2). For a strictly positive rational candidate, obtain all-signed hull certificates for every FULL deterministic vector or a rational signed separator; only then analyze actual image nonmembership. The original four-observer mother problem remains open.
