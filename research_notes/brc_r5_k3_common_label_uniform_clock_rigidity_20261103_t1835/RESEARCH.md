# R5 K3 — strict common label: complete source-uniform-clock joint answer classification

2026-11-03 Asia/Shanghai. AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Scope and source pins

Mother objective: a genuine two-law finite stopped experiment with equal FULL / seedless likelihood-ratio (LR) four-observer convex hulls, but different actual real-behaviour observer images. This note classifies a **ten-real-parameter** common-label K3 subfamily. Frozen science pins: Global Knowledge a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Direct physical predecessor is research_notes/brc_r5_k3_single_common_label_20261103_t1740/RESEARCH.md at 0d74ec81ef571623da677f49cdad29926b9c5a3f. Current normative rules were read separately on 2026-11-03. P000, ACTIVE X6/Heartbeat worldview and source/BRC provenance are unchanged. This is a finite two-law observer theorem, not a native X6 physical realization.

## Model and theorem

Four sources are C,I,BJ,IJ, with alpha=(1/2,2/3,1/2,3/4). FULL uses 0<=x,y<=1, 0<=i<=1-x and sourcewise z_s,t_s,u_s in [0,1]; LR uses i=(1-x)y and common z,t,u. Put

    w=(1/4,(1-x)/4,y/8,i/8), d=y/16+3*i/32,
    M_s=w_s alpha_s z_s, S_s=(2/3)M_s t_s, U_s=S_s u_s.

The physical shared terminal-label experiment gives

    eP=107/128-21*x/128+d/4-sum(S)/2+sum_s(p_s*S_s/8)
    eQ=13/64+3*x/64-d/2+sum(S)/8+sum_s(q_s*S_s/32)
    TP=3+sum(M)+(3/2)*sum(S)+sum_s(r_s*U_s)
    TQ=3+sum(M)/2+(3/8)*sum(S)+sum_s(v_s*U_s/4).

All parameters are in (0,1); here the four p_s and four q_s vary independently, while r_s=r and v_s=v are each source-constant, and r,v vary freely. These are 10 real parameters.

**Theorem.** Within this entire family, conv O(FULL)=conv O(LR) iff all four p_s are equal and all four q_s are equal. Under these conditions the actual real images also agree: O(FULL)=O(LR).

Let c=(1/8,1/6,1/16,3/32), P_a(tau)=sum c_s(a_s-tau)_+, N_a(tau)=sum c_s(tau-a_s)_+ for tau in (0,1). Define eta=3/2+2r-v>1/2 and kappa=eta for 2r>=v, otherwise kappa=3/2. The two explicit, independent signed normals are

    nP(tau)=(8,0,2*(4-tau)/kappa,-4*(4-tau)/kappa)
    nQ(tau)=(0,-32,2*(4+tau)/kappa,-4*(4+tau)/kappa).

For ALL real behavioural policies the exact support differences are

    hFULL(nP)-hLR(nP)=(2/3)min(P_p(tau),N_p(tau))
    hFULL(nQ)-hLR(nQ)=(2/3)min(P_q(tau),N_q(tau)).

The P gap is independent of q; the Q gap is independent of p, including when both parameter vectors vary. Any nonconstant vector is strictly separated by a threshold between its least and greatest entries.

## Proof of the all-real support identities

Use the proven all-signed Bellman reduction at the immediate physical predecessor: for direction (A,B,C,D), at carrier c_s(x,y,i)=w_s alpha_s, the four nested local stage values are

    0, K, K+(2/3)(L+H_s), K+(2/3)(L+H_s+T)
    K=C+D/2, L=-A/2+B/8+3C/2+3D/8
    H_s=A*p_s/8+B*q_s/32, T=C*r+D*v/4.

The signed baseline is b=A*(107/128-21x/128+d/4)+B*(13/64+3x/64-d/2)+3*(C+D). FULL maximizes each source stage independently, LR must use one stage for all sources. The maxima over real upstream policies reduce exactly to six FULL corners (0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0) and four LR corners (0,0,0),(0,1,1),(1,0,0),(1,1,0), by upstream affinity and LR bilinearity.

For both new normals, K=0 and T=(4∓tau)*(2r-v)/kappa (minus for P, plus for Q). If 2r>=v, stage3 dominates stage2 and equals g_s=(2/3)(p_s-tau) for nP or g_s=(2/3)(tau-q_s) for nQ. If 2r<v, stage2 dominates stage3 and equals the SAME g_s. Thus at each upstream corner FULL adds sum_s c_s (g_s)_+, whereas LR adds max(0,sum_s c_s*g_s).

Both upstream maxima occur at v*=(0,1,1), where c*=c. The P baseline differs from a constant by -21x/16+y/8+3i/16; the Q baseline differs by -3x/2+y+3i/2. Every carrier at v* is at least as large as at any other corner and all FULL local payoffs are nonnegative, so v* maximizes FULL. For LR, |g_s|<2/3 and all carrier differences are nonnegative. For any corner v,

    max(0,sum c_s(v)g_s)-max(0,sum c_s(v*)g_s)
    <= (2/3)sum_s(c_s(v*)-c_s(v))
    = (2/3)[x/6+(1-y)/16+3(1-i)/32].

But the baseline gain from v to v* is
    P: 21x/16+(1-y)/8+3(1-i)/16;
    Q: 3x/2+(1-y)+3(1-i)/2,
each term strictly exceeding the respective (2/3)*carrier difference away from v*. Hence v* maximizes LR as well. Subtraction there gives min(sum c_s (g_s)_+,sum c_s(-g_s)_+), exactly the two claimed gap formulas. Positive c_s and tau between min and max prove the necessary source constancy.

## Sufficiency via explicit real-policy pooling

When p_s=p0, q_s=q0 and the delay probabilities already have common r,v, any FULL policy has aggregates M=sum M_s, S=sum S_s, U=sum U_s, Tbar=sum w_s alpha_s=1/8+(1-x)/6+d. Construct an LR policy:

    y'=32d/(5-3x), i'=(1-x)y',
    z'=M/Tbar, t'=3S/(2M) if M>0 else 0,
    u'=U/S if S>0 else 0.

FULL constraints give 0<=d<=(5-3x)/32 and 0<=U<=S<=2M/3<=2Tbar/3, so the LR controls lie in [0,1]. They preserve x,d,M,S,U exactly. With common p0,q0,r,v, all four observer formulas depend only on these five retained scalars, proving each FULL real observation is attained by LR; reverse containment is immediate. Therefore actual images and convex hulls coincide.

## Exact rational example and executed verification

Take r=v=3/4, tau=1/2, p=(1/4,1/2,3/4,1/2), q=(3/4,1/2,1/4,1/2). Normals nP=(8,0,28/9,-56/9), nQ=(0,-32,4,-8) yield:

    hFULL(nP)=-223/96; hLR(nP)=-7/3; gap=1/96.
    hFULL(nQ)=-1535/96; hLR(nQ)=-16; gap=1/96.

The same FULL strategy at upstream (0,1,1), source stages (1,1,3,1), attains both maxima at W=(659/768,401/3072,85/24,1247/384). The signed-hyperplane dual norm gives dist_infinity(W,conv O(LR))>=1/1664 (from nP) and independently >=1/4224 (from nQ).

VERIFY.py, executed with Python standard-library Fraction, tests both formulas at 5 thresholds for 12 rational kernels, including 2r<v, 2r=v and 2r>v. Each of the 120 direction/kernel tests exhaustively scans 1536 FULL and 16 LR deterministic observations; 9 nonbinary real-policy FULL-to-LR pooling examples and the joint witness are also checked. All 142 exact assertions passed. The analytic argument proves the continuous real domain; finite tests check the arithmetic. No formal independent project review or native Result/CLAIM was obtained.

## Next question

For a fully source-heterogeneous sixteen-parameter common-label K3 model, determine whether clock heterogeneity can be isolated by an exact signed normal even when p_s and q_s also vary. Clock-only rigidity normals from the earlier action-selectable-label topology contain error coefficients, so their transfer to arbitrary joint p,q requires a fresh proof. Seek all-signed exact rational hull-mixture/Farkas certificates, then test actual image nonmembership only for hull-equal candidates. Preserve original terminal physical experiment, frozen pins and current owner/role semantics.
