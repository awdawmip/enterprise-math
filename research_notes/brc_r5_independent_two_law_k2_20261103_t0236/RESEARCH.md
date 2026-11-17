# R5 — Independent two-law K2 answer kernels: exact eight-parameter classification

Date: 2026-11-03 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Source and scope

Research successor to immutable awdawmip/enterprise-math@6ef66b52cc827ac779be34fe483b2e556ccee7d0:research_notes/brc_r5_four_source_k2_coin_classification_20261103_t0140/RESEARCH.md. Frozen scientific pins: global a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Current operational rules refreshed independently. P000 and ACTIVE six-axis Heartbeat worldview unchanged.

Mother problem: construct a valid finite two-law stopped experiment with conv O(FULL)=conv O(LR) yet O(FULL)!=O(LR), where physical observers O=(eP,eQ,TP,TQ). Here we classify the continuous eight-parameter family of independent terminal Q-answer coins in the fixed genuine X->J->K1->K2 tree. This is an auxiliary positive-source BRC finite probability flow, not a native-X6 physical embedding.

## Main theorem (all real parameters and policies)

Maintain the fixed tree, four source labels s=(C,I,BJ,IJ), source masses (1/4,1/4,1/8,1/8) and an additional D mass 1/4. First K1 success probabilities under P are alpha=(1/2,2/3,1/2,3/4), under Q alpha/2. Second K2 successes have P probability c=2/3, Q probability c/2. J, K1, K2 LR collision keys remain (time,likelihood-ratio)=(2,1),(3,1),(4,2). The only new parameters are arbitrary Q-answer coin probabilities p_s under P and q_s under Q conditional on K2 success, with every real p_s,q_s strictly between 0 and 1.

Set w*=(1/8,1/6,1/16,3/32), A*=43/96, D*=5/32, and define

    theta_s=(2/3)p_s-(7/12)q_s=(8p_s-7q_s)/12,
    xi_s=(64/9)p_s-(8/9)q_s,
    phi_s=theta_s-xi_s/8=(-8p_s-17q_s)/36.

For kappa=0,-1/8 let f^(0)=theta, f^(-1/8)=phi, m_kappa=sum_s(w*_s f_s)/A*, and let the physical normal be

    n_kappa=(-2/3-64*kappa/9,-7/3-32*kappa/9,
             -1-2*m_kappa,4+4*m_kappa).

Then for every eight-tuple (p,q) in (0,1)^8, and all real history-adaptive behavioral policies in FULL and seedless LR, the **exact** support gap is

    h_FULL(n_kappa)-h_LR(n_kappa)
      = c * sum_s w*_s (f_s-m_kappa)_+
      = (1/3)*sum_s w*_s |f_s-m_kappa|.               (T1)

Consequently,

    conv O(FULL)=conv O(LR)
    iff p_C=p_I=p_BJ=p_IJ and q_C=q_I=q_BJ=q_IJ.     (T2)

Under these conditions the actual real policy images satisfy O(FULL)=O(LR) and the common image has full four-dimensional local rank.

## Exact P/Q source flow

Let x be the root flag probability and b,i the source-labelled J continuation masses, with 0<=b<=1 and 0<=i<=1-x. Define positive source weights, first continuation and second continuation:

    w=(1/4,(1-x)/4,b/8,i/8),
    d=b/16+3i/32,
    Q_s=w_s*alpha_s*z_s, R1=sum_s Q_s,
    S_s=c*Q_s*t_s,      R2=sum_s S_s,

where z_s,t_s are source-conditional probabilities (or effective conditional flow averages) in [0,1]. Keep each source label until its answer coin contribution is evaluated. Set SP=sum_s p_s S_s and SQ=sum_s q_s S_s. Direct full terminal path summation under the two measures yields

    eP=107/128-21x/128+d/4-SP,
    eQ=13/64+3x/64-d/2+SQ/4,
    TP=3+R1+R2, TQ=3+R1/2+R2/4.                    (1)

Recover from these physical observers the baseline affine coordinates

    vP=eP-107/128, vQ=eQ-13/64,
    X=(-vP/2-vQ/4)/(9/128),
    D=(-3vP/64-21vQ/128)/(9/128),
    U=4(TQ-3)-(TP-3),
    V=2(TP-3)-4(TQ-3).

Exactly,

    X=x+sum_s xi_s*S_s,
    D=d+sum_s theta_s*S_s,
    U=R1, V=R2.                                    (2)

This identifies two independent law-sensitive residuals in the BRC source-labelled flow.

## Complete all-real support proof

For kappa=0 or -1/8 put f_s=theta_s+kappa*xi_s and m=m_kappa. The signed physical support functional n_kappa·O differs only by a common additive constant from

    Psi_kappa=D+kappa*X+U-mV
      =d+kappa*x+sum_s Q_s*[1+c*t_s*(f_s-m)].       (3)

For kappa=0, f_s=theta_s in (-7/12,2/3) and c*range(f)<5/6<1. For kappa=-1/8, f_s=phi_s in (-25/36,0) and c*range(f)<25/54<1. Hence each source Q_s coefficient in (3) is positive for every t_s in [0,1].

FULL optimizes z_s=1, t_s=1 exactly where f_s>m, and then chooses x=0,b=i=1, since all source coefficients are positive and kappa<=0. With Q_s=w*_s and d=D*, the exact maximum is

    max_FULL Psi=A*+D*+c*sum_s w*_s(f_s-m)_+.       (4)

LR forces b=y, i=(1-x)*y, common z and t. Put A=sum_s w_s alpha_s. Each 0<=w_s alpha_s<=w*_s, so A<=A*, d<=D*. Since sum_s w*_s(f_s-m)=0,

    |sum_s w_s alpha_s(f_s-m)|
      =|sum_s(w*_s-w_s alpha_s)(f_s-m)|
      <=range(f)(A*-A).

For every LR real policy and either kappa,

    Psi_LR=d+kappa*x+zA+czt*sum_s(w_s alpha_s)(f_s-m)
          <=D*+zA+c range(f)(A*-A)
          <=D*+A*.

Equality is achieved at x=0,y=z=1,t=0. Subtraction proves the first expression T1. The weighted centered sum is zero, so its positive part is half its weighted absolute value, proving the second T1.

All weights w*_s are positive. Gap zero for kappa=0 forces source-constant theta, and gap zero for -1/8 forces source-constant phi. From 12theta_s=8p_s-7q_s and 36phi_s=-8p_s-17q_s, the two source-constant equalities imply -24q_s is constant, then all p_s are constant. Thus equal hulls imply T2. The converse follows by the exact aggregation below.

## Uniform kernel: actual-image equality and full rank

When p_s=p0 and q_s=q0 for every source, SP=p0 R2 and SQ=q0 R2. Thus O is a fixed affine shear of the baseline (x,d,R1,R2), with determinant -9/512. For an arbitrary FULL strategy set

    y=32d/(5-3x),
    z=R1/(1/8+(1-x)/6+d),
    t=R2/(c R1) if R1>0, otherwise 0.

Positive-flow bounds 0<=d<=(5-3x)/32, 0<=R1<=1/8+(1-x)/6+d, 0<=R2<=cR1 ensure y,z,t in [0,1]. The LR strategy then matches all four physical coordinates; the reverse inclusion is automatic. At an interior LR strategy with A=1/8+(1-x)/6+(5-3x)y/32, the auxiliary Jacobian determinant equals (5-3x)/32*c*z*A^2>0; the physical Jacobian is -9/512 times this number. The common image has nonempty four-dimensional interior.

## Strictly positive exact example: the second normal matters

Take q=(1/4,1/2,3/4,1/2) and p=(9/32,1/2,23/32,1/2). Both law probabilities are strictly positive and less than one. All theta_s=1/24, so the first normal has gap zero. But phi is not source-uniform:

    m_-1/8=-1003/3096,
    n_-1/8=(2/9,-17/9,-545/1548,2093/774),
    gap_-1/8=37/3096 > 0.

The FULL witness has x=0, J and K1 always continue, and at K2 only those sources with phi_s>m_-1/8 continue:

    W=(109/128,25/192,113/32,623/192),
    hFULL=92563/12384, hLR=30805/4128,
    distance_inf(W,conv O(LR)) >= 37/15998.

An opposite example with phi constant and theta nonconstant is included in the exact checker.

## Verification and continuation

An independently implemented finite-tree path-sum checker in standard-library Python Fraction recomputes terminal paths for P and Q; five rational kernel pairs, 2048 reduced FULL and 16 LR deterministic controls each; both signed normals and maximizing witnesses; and 160 history-adaptive nonbinary strategies, checking the source-flow/physical observer identities. It also checks explicit real strategy aggregation in the uniform case. Actual execution: 32239 exact assertions, marker PASS_EXACT_R5_INDEPENDENT_TWO_LAW_K2_TERMINAL_CLASSIFICATION. The continuous classification rests on the analytic proof above.

Next research direction: introduce a source-conditioned strictly positive post-K2 terminal time split or a third interacting decision key. Retain true P/Q likelihood-ratio collision identities, derive the new positive source-flow observer, test full rational convex-hull containment or obtain Farkas separating certificates, then test actual real-image nonmembership if hull equality holds. The four-observer mother objective is open. Author-side publication is distinct from formal native CLAIM, Result and independent Driver review.
