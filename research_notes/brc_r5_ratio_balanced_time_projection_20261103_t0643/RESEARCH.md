# R5 — Exact two-law stopping-time convex-hull classification

Date: 2026-11-03 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Objective, provenance and fixed scientific input

The mother problem asks for a finite two-law stop experiment with conv O(FULL)=conv O(seedless LR) for the true four-observer O=(e_P,e_Q,T_P,T_Q), but O(FULL) != O(LR) as actual real-behaviour image sets. This result completely classifies equality of the TWO STOPPING-TIME COORDINATE convex hulls for the independent post-K2-delay family.

Scientific predecessor: enterprise-math at immutable commit fbeb40d310d5dbdb2766d4e1994293d74bf830c2, research_notes/brc_r5_delay_ratio_rigidity_20261103_t0542/RESEARCH.md. That note proves the ratio-rigidity lemma and the exact four-observer FULL signed support oracle. The physical P/Q path realization was proved earlier at 0592311ad484d47c449563167d2ae6521ccf4234. The frozen scientific pins remain Global Knowledge a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Current normative rules are separately refreshed. Protected P000 and ACTIVE worldview remain unchanged.

The positive-mass BRC source identities are s=(C,I,BJ,IJ). The first serial P-success kernel is alpha=(1/2,2/3,1/2,3/4), its Q version alpha/2; the second P-success factor is c=2/3, its Q version c/2. The original seedless LR collisions at J=(2,1), K1=(3,1), K2=(4,2) (time, likelihood-ratio) are unchanged. At post-K2 success, under P, source s has probability a_s of stopping at time 6 rather than time 5; under Q the probability is b_s. All a_s,b_s,p_s,q_s are independently in (0,1), with p_s,q_s terminal answer kernel probabilities. This is an auxiliary physically valid two-law finite tree, with no native X6 calibration asserted.

For FULL, set 0<=x,y<=1, 0<=i<=1-x; w=(1/4,(1-x)/4,y/8,i/8). Independently choose 0<=z_s,t_s<=1, Q_s=w_s alpha_s z_s and S_s=c Q_s t_s. LR sets i=(1-x)y and z_s=z,t_s=t for all sources. The actual stopping time observations are

    T_P=3+sum_s Q_s+sum_s (1+a_s)S_s,
    T_Q=3+(sum_s Q_s)/2+(sum_s (1+b_s)S_s)/4.       (1)

Source labels are retained until this specified readout; no unproved provenance erasure is used.

## Theorem: complete time-projection convex-hull classification

Define rho_s=(1+b_s)/(1+a_s) and pi_T O=(T_P,T_Q). For every admissible real kernel (a,b,p,q) in (0,1)^16 and ALL real behavioural FULL and seedless LR strategies, the following are equivalent:

(A) conv pi_T O(FULL) = conv pi_T O(LR).

(B) rho_C=rho_I=rho_BJ=rho_IJ=:rho, AND

    a_C >= max(a_I,a_BJ),   a_IJ=min(a_I,a_BJ).         (2)

This is an exact universal continuous-parameter classification of the projected convex hulls, independent of the eight answer parameters. It admits nonuniform strictly positive kernels, for example a=b=(3/4,1/2,1/4,1/4).

## Proof, step 1: ratio rigidity

If m=min_s rho_s < M=max_s rho_s, choose u in (m,M) sufficiently close to m; since every rho_s is in (1/2,2), h=2-u>0 and h+c min(0,k_s)>0 for all sources, where k_s=(1+b_s)-u(1+a_s). In the pure time normal (n_P,n_Q)=(-u,4), FULL maximizes all source first-stage masses separately and takes second-stage controls t_s according to k_s>0. LR maximizes those first-stage masses but must share one t. With W=(1/8,1/6,1/16,3/32), Kplus=sum_s W_s max(k_s,0), Kminus=sum_s W_s max(-k_s,0), both are positive, and the exact support gap is

    h_FULL(-u,4)-h_LR(-u,4)=c min(Kplus,Kminus)>0.     (3)

The cited predecessor supplies this same all-real support calculation, including a constructive u. Hence (A) requires constant rho.

## Proof, step 2: every signed time support with common rho

Assume b_s=rho(1+a_s)-1; strict probability conditions imply 1/2<rho<2. For an arbitrary real pure-time normal (n_P,n_Q) define

    B=3(n_P+n_Q),  h=n_P+n_Q/2,  f=n_P+rho n_Q/4,
    A_s=h+c(1+a_s) f,  W=(1/8,1/6,1/16,3/32).

Equation (1) gives the exact linear score B+sum_s Q_s[h+c(1+a_s)f t_s]. When f<=0, the optimal second-stage action is t_s=0 for FULL and t=0 for LR, yielding the same support B+(43/96)max(0,h).

When f>0, active second-stage controls optimally equal 1. FULL can select source first-stage continuation z_s independently. All remaining source terms are nonnegative after selecting z_s=1 iff A_s>0, so x=0,y=i=1 maximizes the available source weights. Thus

    h_FULL(n_P,n_Q) = B + sum_s W_s max(0,A_s).        (4)

For LR, z=0 yields B; at z=t=1 the upstream multilinear corners (x,y)=(1,0),(0,0),(1,1),(0,1) respectively expose source subsets

    {C}, {C,I}, {C,BJ}, {C,I,BJ,IJ}.

As all (1+a_s)f are positive, t=1 is optimal whenever z=1. The LR support is therefore EXACTLY

    h_LR = B + max_{S in F} sum_{s in S} W_s A_s,
    F={empty,{C},{C,I},{C,BJ},{C,I,BJ,IJ}}.          (5)

By strict positivity of all W_s, (4)=(5) for a fixed direction if and only if some S in F contains every positive A_s and excludes every negative A_s. Zero-value labels can be assigned freely.

Since det((n_P,n_Q)->(h,f))=(rho-2)/4 !=0, f>0 directions can realize every threshold tau via h=-c(1+tau)f. Then A_s=cf(a_s-tau), so the positive set is exactly the strict superlevel set U_tau={s:a_s>tau}. Therefore (4)=(5) for ALL time normals exactly when every U_tau, for tau strictly between distinct a_s levels, is in F.

The allowed subsets yield a complete elementary order classification. If some non-C a_s exceeds a_C, choose tau between them: U_tau is nonempty without C and is not in F. If a_IJ>min(a_I,a_BJ), a threshold between them gives IJ without I or BJ, also impossible. If a_IJ<min(a_I,a_BJ), a threshold between them gives {C,I,BJ} without IJ, also impossible. Conversely, a_C>=max(a_I,a_BJ) and a_IJ=min(a_I,a_BJ) ensure U_tau runs only through empty, {C}, then either {C,I} or {C,BJ}, and finally all four; all belong to F. At ties, zero terms do not affect the optimum. Conditions (2) are thus precisely necessary and sufficient for equal supports in all time directions. Compactness of the finite-horizon behavioural images and standard support-function uniqueness for compact convex sets prove (A) iff (B). QED.

## New exact positive-probability witness

Set a=b=(1/4,1/2,1/4,1/4), p=q=(1/2,1/2,1/2,1/2). Here EVERY rho_s=1 but a_C<a_I, so the ratio test alone has no gap. Choose tau=3/8, f=1 and h=-c(1+tau)=-11/12, corresponding to actual two-time normal (35/12,-23/3). Then

    A_C=A_BJ=A_IJ=-1/12,  A_I=1/12,
    h_FULL=-1025/72, h_LR=-4103/288, DELTA=1/96.

The actual FULL strategy x=y=i=0, z_I=t_I=1 with all other downstream controls zero produces the TRUE P/Q four-observer

    W=(899/1152, 125/576, 10/3, 25/8).

W attains the FULL support in the four-normal (0,0,35/12,-23/3). Its l1 norm is 127/12; hence for every real LR behavioural strategy and its convex hull,

    dist_infinity(W,conv O(LR)) >= (1/96)/(127/12) = 1/1016.

The second independent order condition is necessary as well: a=b=(3/4,1/2,1/2,1/4) has C maximal but violates a_IJ=min(...); tau=3/8 gives exact positive time-support gap 1/192.

## Exact checking, scope and next question

VERIFY.py is the standalone executed Python Fraction verifier; EXACT_OUTPUT.txt records its real output. Seven admissible strict-positive rational parameter tuples were tested (rho=1,4/5,6/5). For each, all 2048 raw FULL binary configurations and 16 LR binary controls were enumerated. Their physical observers and the analytic supports (4),(5) were compared at 48 distinct signed time normals; all non-tied threshold intervals were checked. The actual four-observer witness and distance inequality were separately checked. Final output: PASS_EXACT_R5_RATIO_BALANCED_TIME_PROJECTION_CLASSIFICATION; 369 exact assertions. The universal claim is established by the analytic proof, not by finite tests.

The original four-observer convex-hull equality and actual behavioural image inequivalence remain the parent research target. This time-only classification is a lossless prefilter for its necessary time-projection constraint; other four-observer directions can still separate. The selected next unit studies source-dependent answer kernels on the nonuniform admissible delay skeleton. Native source owner/CLAIM/Result and independent Driver acceptance have not been confirmed: current Site gateway is static_machine_readonly and current bounded owner inventory returned CONTROL_QUOTA.
