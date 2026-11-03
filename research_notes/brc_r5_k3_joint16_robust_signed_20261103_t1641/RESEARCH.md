# R5 K3 — All-signed Bellman envelope and robust joint 16-parameter separation

Date: 2026-11-03 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Provenance and selected question

Mother goal: find a real finite P/Q stopped experiment with equal four-observer FULL/LR convex hulls and unequal actual real behavioural images. Predecessor physical event construction: Enterprise Math immutable commit e498befa4d647ade7eb87620127ebe20213167eb, research_notes/brc_r5_k3_physical_event_bridge_20261103_t1545/RESEARCH.md. Frozen scientific sources: Global Knowledge a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Current behavioral rules were read separately. P000 and ACTIVE worldview are untouched.

Four distinct BRC-positive latent source branches: C,I,BJ,IJ; their P/Q mass ratio at the third collision gate K3 is 4. Source identity and the future conditional operations are retained prior to the four-coordinate readout.

## Actual physical model, 16 open probability parameters

FULL controls real x,y in [0,1], i in [0,1-x], and source-specific real z_s,t_s,u_s in [0,1]. Define:

    w=(1/4,(1-x)/4,y/8,i/8)
    alpha=(1/2,2/3,1/2,3/4)
    c_s=w_s alpha_s, M_s=c_s z_s, S_s=(2/3) M_s t_s
    U_s=S_s u_s, d=y/16+3i/32.

Seedless LR imposes i=(1-x)y and common z_s=z, t_s=t, u_s=u, with x,y,z,t,u in [0,1].

For each source before K3 action draw exogenous independent binary potential variables B,D,L0,L1 with conditional P/Q laws: P(B=1)=Q(B=1)=1/2, P(D=1)=r_s, Q(D=1)=v_s, L0 symmetric under each law, P(L1=Q)=1/2+p_s/8, Q(L1=Q)=1/2-q_s/8. All p_s,q_s,r_s,v_s are in (0,1), giving strictly positive atoms of the common terminal sample space. Stop at K3 reads time 5+B and label L0; continue reads time 5+B+D and label L1. Labels and coins are revealed only after the K3 decision; the pre-action information collision is unchanged. The joint genuine binary testing observation is exactly

    eP=107/128-21*x/128+d/4-sum(S)/2+sum_s(p_s U_s)/8
    eQ=13/64+3*x/64-d/2+sum(S)/8+sum_s(q_s U_s)/32
    TP=3+sum(M)+(3/2)*sum(S)+sum_s(r_s U_s)
    TQ=3+sum(M)/2+(3/8)*sum(S)+sum_s(v_s U_s)/4.

The formulas follow for every real policy by conditioning on the disjoint source and gate events; P/Q source arrival masses are S_s and S_s/4. In this explicit topology action may choose one of two fixed potential terminal labels. A common-label readout is a distinct target topology.

## Theorem A: exact all-signed envelope for every real direction and kernel

For n=(A,B,C,D) in R^4 let

    K=C+D/2
    L=-A/2+B/8+3*C/2+3*D/8
    J_s=A*p_s/8+B*q_s/32+C*r_s+D*v_s/4
    F_s=max(0,K,K+2*L/3,K+2*(L+J_s)/3)
    b(x,y,i)=A*(107/128-21*x/128+d/4)
              +B*(13/64+3*x/64-d/2)+3*(C+D).

Define FULL upstream corners V_F={(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0)} and LR corners V_L={(0,0,0),(0,1,1),(1,0,0),(1,1,0)} where the tuple is (x,y,i). Then

    h_FULL(n) = max_{v in V_F} [b(v)+sum_s c_s(v) F_s].

For each v in V_L put T=sum_s c_s(v). Then

    h_LR(n) = max_{v in V_L} [
      b(v)+max(0,K*T,(K+2*L/3)*T,
                   (K+2*L/3)*T+(2/3)*sum_s c_s(v) J_s) ].

Proof. For one source the signed K3 contribution is c_s z_s[K+(2/3)t_s(L+u_s J_s)]. It is multi-affine in (z_s,t_s,u_s), so its maximum on their real cube occurs at one of the four distinct nested stages (0,0,0),(1,0,0),(1,1,0),(1,1,1), with exact values forming F_s. FULL optimizes stages independently by source. For any fixed stages its remaining objective is affine in (x,y,i), on the six-vertex upstream prism, yielding V_F. LR shares the stage and therefore has one aggregate maximum over the four displayed values. For each fixed common stage i=(1-x)y makes the upstream signed objective bilinear in x,y, whose maximum on the real square lies at one of its four corners V_L. These reductions hold for arbitrary signed real n and all sixteen real parameters, with no limiting or numerical approximation. QED.

This is a finite all-signed hull-support oracle: six upstream corners plus four sourcewise maxima for FULL, versus sixteen aggregate upstream/stage configurations for LR.

## Theorem B: Lipschitz persistence of separation under all sixteen simultaneous perturbations

For two physical kernels theta and theta', suppose |delta p_s|<=eps_p, |delta q_s|<=eps_q, |delta r_s|<=eps_r, |delta v_s|<=eps_v, all sources. At a fixed real FULL/LR policy, the signed observer difference is exactly

    sum_s U_s (A*delta p_s/8+B*delta q_s/32+
               C*delta r_s+D*delta v_s/4).

Since U_s >=0 and

    sum_s U_s <= (2/3) sum_s c_s
              <= (2/3)*(1/8+1/6+1/16+3/32) = 43/144,

taking maxima yields, for either class X in {FULL,LR},

    |h_X(theta;n)-h_X(theta';n)|
       <= (43/144)(|A|eps_p/8+|B|eps_q/32+
                   |C|eps_r+|D|eps_v/4).

This uniform bound covers all real controls; taking a maximum does not increase a pointwise uniform error. QED.

Take base kernel

    p0=(1/4,1/2,3/4,1/2), q0=(3/4,1/2,1/4,1/2),
    r0=v0=(3/4,3/4,3/4,3/4).

From an exact complete deterministic-policy enumeration, at nP=(8,0,-8/9,88/9) and nQ=(0,-32,0,8), both signed support gaps are exactly 1/96. For any kernel in the full 16-parameter sup-norm box of radius eps around the base, the preceding theorem implies

    Delta(nP)>=1/96-(559/216)eps,
    Delta(nQ)>=1/96-(43/24)eps.

Thus for EVERY such kernel with 0<=eps<9/2236 and all parameters in (0,1), BOTH four-dimensional FULL/LR convex-hull support gaps stay strictly positive. This supplies an exact full-dimensional open region of simultaneous, source-heterogeneous clock/answer kernels excluded from the mother target. It is a continuous real-parameter theorem, not finite-sample extrapolation.

## Explicit rational 16-parameter witness

Set eta=1/1000 and signs sigma=(1,-1,1,-1). Put p=p0+eta*sigma, q=q0-eta*sigma, r=r0+eta*sigma, v=v0-eta*sigma; all sixteen conditional probabilities are in (0,1) and each kernel vector is nonconstant. Complete exact enumeration and independent Theorem A calculation give:

    nP: FULL 15322633/432000, LR 851/24,
        gap 4633/432000 > robust lower 1691/216000.
    nQ: FULL 3139519/144000, LR 523/24,
        gap 1519/144000 > robust lower 69/8000.

One FULL policy x=0,y=1,i=1; local stages C=(1,0,0) and I=BJ=IJ=(1,1,1), simultaneously attains both maxima and yields

    W=(100109/128000,714019/4608000,
       566231/144000,1926769/576000).

Hölder's inequality and the signed LR support bounds give two rational certificates:

    dist_infty(W,conv O(LR)) >= 4633/8064000,
    dist_infty(W,conv O(LR)) >= 1519/5760000.

The first is the stronger bound. Both are independently certified signed hyperplane separations.

## Reproducibility, evidence scope, BRC reuse

VERIFY.py actually executed with standard-library Fraction; EXACT_OUTPUT.txt is its stdout. The program fully enumerates 1536 distinct FULL deterministic configurations and 16 LR configurations for the base and perturbed kernels, evaluates three signed directions in each, and matches the independent closed envelopes. It checks the baseline and new gaps, exact robust lower bounds, witness distances, all positive terminal observation atoms, normalization, P/Q expected terminal times and testing errors at all four sources under both measures and both gate actions. All 89 counted verification groups pass. Universal real quantifiers are established by the above analytic arguments. No formal proof checker or independent Driver mathematical review is asserted.

Existing pinned BRC positive source-flow interface (w,alpha,M,S,U): REUSE_APPLIED. Original source identity and future gate operations are retained; the convex-hull support is a declared four-observer projection with provenance. The method here is a scoped exact support-theory extension, not a new top-level BRC theorem family or a claim of native X6 transfer.

## Next research problem

Search rational 16-parameter K3 models OUTSIDE this robust exclusion box for an all-signed hull-equality candidate using the finite Theorem A support oracle. For equality give rational convex decompositions of all 1536 FULL deterministic observation points by <=5 LR vertices each in R4; for failure give one rational Farkas separator with attainable FULL witness. Independently examine the stricter physical topology in which K3 stop/continue actions reveal the same terminal label, preserving the mother target's exact observation semantics. Only after full hull equality attempt real-policy image nonmembership. Formal owner, native CLAIM/Result and independent Driver review require separately established current authority.