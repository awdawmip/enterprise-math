# R5 — Independent P/Q post-K2 delays: exact time gap and compensated face with global separation

Date: 2026-11-03 Asia/Shanghai. Scientific status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Provenance and precise question

Mother objective: construct a finite two-law stopped experiment for which conv O(FULL)=conv O(seedless LR), but O(FULL) and O(LR) differ as real-behavior images, where the physical four-observer vector is O=(e_P,e_Q,T_P,T_Q).

Immutable predecessor: enterprise-math@0592311ad484d47c449563167d2ae6521ccf4234:research_notes/brc_r5_postk2_law_coupled_split_20261103_t0340/RESEARCH.md. Scientific input pins remain GLOBAL_KNOWLEDGE_V1@a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math@86149263e38c22292c9def1e0f69092efa1be77e. Current canonical normative rules were read separately. P000 and ACTIVE world axioms are not changed. The model is a typed positive-mass BRC source-flow experiment, not a native-X6 physical calibration.

## 1. Independent two-law terminal time kernels

Use the predecessor finite tree X -> J -> K1 -> K2. Four hidden sources s=(C,I,BJ,IJ) have parent masses (1/4,1/4,1/8,1/8). K1 success probabilities are alpha=(1/2,2/3,1/2,3/4) under P and alpha/2 under Q. K2 success probability is c=2/3 under P, c/2 under Q. Seedless LR keys remain (time, likelihood ratio) J=(2,1), K1=(3,1), K2=(4,2). There are no decisions after K2.

After K2 success, the conditional P and Q probabilities of reaching time 6 rather than time 5 are independently a_s,b_s in (0,1), with terminal Q-answer probabilities p_s,q_s in (0,1). Thus all non-decision natural transitions have positive probability. Neither the pre-K2 keys nor their likelihood-ratio collisions change.

For FULL root/source controls 0<=x,b<=1, 0<=i<=1-x and independently chosen z_s,t_s in [0,1], put

    w=(1/4,(1-x)/4,b/8,i/8), d=b/16+3*i/32,
    Q_s=w_s*alpha_s*z_s, S_s=c*Q_s*t_s,
    R1=sum Q_s, R2=sum S_s.

LR enforces b=y, i=(1-x)y, z_s=z and t_s=t. Direct two-law terminal-path addition gives

    e_P=107/128-21*x/128+d/4-sum_s p_s*S_s,
    e_Q=13/64+3*x/64-d/2+sum_s q_s*S_s/4,
    T_P=3+R1+R2+sum_s a_s*S_s,
    T_Q=3+R1/2+R2/4+sum_s b_s*S_s/4.       (1)

Equations (1) are the predecessor physical-path identities extended by independent post-K2 terminal delays. This note's exact verifier checks their resulting full/LR observer values and signed supports, not a new independent enumeration of raw P/Q terminal probabilities.

## 2. Theorem A: a universal time-only support formula

Let v=(0,0,-1,4), w*=(1/8,1/6,1/16,3/32), A*=43/96 and delta_s=b_s-a_s. For EVERY real admissible 16-parameter kernel and EVERY real behavioral policy,

    h_FULL(v)=9+A*+c*sum_s w*_s max(delta_s,0),
    h_LR(v)  =9+A*+c*max(sum_s w*_s delta_s,0),
    Delta(v)=c*min(Pplus,Pminus),                         (2)
    Pplus=sum_s w*_s max(delta_s,0),
    Pminus=sum_s w*_s max(-delta_s,0).

Thus the full and LR convex hulls are strictly separated in this normal iff the sign of b_s-a_s is positive for at least one source and negative for at least one other source.

Proof: From (1),

    v dot O=9+R1+sum_s delta_s*S_s
            =9+sum_s Q_s*(1+c*t_s*delta_s).

Because -1<delta_s<1 and c=2/3, every coefficient is strictly greater than 1/3. FULL's maximum therefore takes x=0,b=i=1,z_s=1 and independently selects each t_s to maximize its signed delta. LR's maximum takes x=0,y=z=1 and chooses the single t according to the sign of sum_s w*_s delta_s. Positive/negative weighted parts give (2). These optimizations include all nonbinary real controls.

Exact strict-positive example: p_s=q_s=1/2, a=(3/8,5/8,3/8,5/8), b=(5/8,3/8,5/8,3/8). Then Delta(v)=1/32. Since ||v||_1=5, the maximizing FULL point has L_infinity distance at least 1/160 from conv O(LR).

## 3. Theorem B: equal entire exposed face, still globally unequal convex hulls

Consider the continuous two-level diagonal-delay subfamily

    0<rminus<rplus<1,
    a=b=(rminus,rplus,rminus,rplus),
    p_s=kappa*(1+a_s), q_s=lambda*(1+a_s),

where kappa,lambda>0 are small enough that every terminal answer parameter is strictly below 1; kappa=lambda=1/4 works throughout.

Define

    rbar=(18*rminus+25*rplus)/43,
    k=c*(1+rbar), n=(0,0,2+k,-4*(1+k)).

The entire FULL maximizing physical-observer face for v=(0,0,-1,4) is EXACTLY the LR maximizing face, yet

    h_FULL(n)-h_LR(n)=(25/344)*(rplus-rminus)>0.       (3)

Proof of face equality: Here a_s=b_s, hence v dot O=9+R1. The maximizing first-stage policy sets x=0,b=i=1,z_s=1 (LR: x=0,y=z=1), and all four t_s remain free. The physical K2 source response vectors are

    u_s=(-p_s,q_s/4,1+a_s,(1+b_s)/4)
        =(1+a_s)*(-kappa,lambda/4,1,1/4).

The FULL exposed face O_base+sum_s c*w*_s*[0,1]*u_s is a line segment equal to the LR face O_base+[0,1]*sum_s c*w*_s*u_s. Every real FULL face point is matched by the LR t equal to sum_s w*_s(1+a_s)t_s / sum_s w*_s(1+a_s). This is equality of the WHOLE exposed face, not merely its support value.

Proof of global gap: Put G=sum_s(1+a_s)*S_s. From (1),

    T_P-3=R1+G, T_Q-3=R1/2+G/4,
    n dot O=G-k*R1-(6+9*k).

For an arbitrary LR real strategy with upstream y, group K1 source masses into

    U=1/8+y/16  (C and BJ),
    V=(1-x)*(1/6+3*y/32)  (I and IJ).

Then 18*V<=18*(1/6+3*y/32)<=25*(1/8+y/16)=25*U, with the latter difference equal to (1-y)/8. Consequently

    B=(1+rminus)*U+(1+rplus)*V
     <=(1+rbar)*(U+V),
    R1=z*(U+V), G=c*z*t*B<=k*R1.

Thus h_LR(n)=-(6+9*k), reached by z=0.

For FULL the contribution from each Q_s is c*(1+a_s)*t_s-k, negative for every low source and maximally c*(rplus-rbar)=c*(18/43)*(rplus-rminus)>0 for each high source. Maximizing sets z_I=z_IJ=t_I=t_IJ=1, low-source z=0, x=0,i=1, giving high-source Q mass 1/6+3/32=25/96. Its maximum G-k*R1 is c*(18/43)*(25/96)*(rplus-rminus)=(25/344)*(rplus-rminus). This proves (3) for every real behavior.

Rational instance: rminus=1/4, rplus=1/2, kappa=lambda=1/4, so p=q=(5/16,3/8,5/16,3/8) and a=b=(1/4,1/2,1/4,1/2). The first normal's maximizing faces coincide, but k=40/43, n=(0,0,126/43,-332/43), and the EXACT full/LR support gap is 25/1376. A FULL maximizing witness is

    W=(311/384,217/1536,169/48,409/128).

Since ||n||_1=458/43, the exact L_infinity distance lower bound is 25/14656.

## 4. Verification, reuse and next open unit

VERIFY.py is the executed Python standard-library Fraction regression. It enumerates 2048 raw FULL and 16 LR deterministic assignments per rational kernel, checks equations (2) and (3), three rational two-level cases, 16 FULL-to-LR exposed-face control matches for each selected case, the exact witness/distance, the LR inequality, and 120 nonbinary face-policy identities. Its actual output is EXACT_OUTPUT.txt (294 exact assertions; PASS_EXACT_R5_INDEPENDENT_DELAY_EXPOSED_FACE_AND_GLOBAL_GAP). Analytic proofs are all-real; enumeration is independent exact-rational corroboration of the observer optimization in the declared model, not a replacement for either proof.

Scientific lesson: full equality of ONE exposed observer face can coexist with a strict signed gap elsewhere; local compensation of a source zonotope does not automatically extend to global convex-hull equality. This is an observer-specific BRC residual and supplies an exact adversarial regression for future candidate selection.

Next: classify support normals beyond v in the 16-parameter independent delay tree, then obtain ALL-signed finite vertex containment certificates (at most five LR vertices per FULL deterministic observer) or an exact rational Farkas separator. Only after verified convex-hull equality attempt actual real-image nonmembership. The mother objective remains open. No native Source CLAIM, accepted Result or independent review is asserted.
