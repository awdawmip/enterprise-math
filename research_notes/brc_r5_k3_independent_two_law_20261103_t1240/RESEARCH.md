# R5 K3 — complete independent P/Q delay-source rigidity

Date: 2026-11-03 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Exact model and scientific inputs

Science pins, unchanged: Global Knowledge a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Current normative reads: global main fdb1f9982861a4065b492bb4342edbf07932ad1f and EM main e15cb849720aaf5388cc252ad47c14eaa015cbe8. Direct scientific predecessors: K3 support oracle RESEARCH.md at commit 2c47ed2096e2cbdc1b5bbd88291dc8583d9f72de and equal-law K3 rigidity at 5decc42d923aea0c34904930078bc74cd652e7e6.

Four labelled positive BRC carriers s=(C,I,BJ,IJ), alpha=(1/2,2/3,1/2,3/4). FULL upstream: 0<=x,y,i<=1 and x+i<=1. LR upstream: i=(1-x)y. Let w=(1/4,(1-x)/4,y/8,i/8), d=y/16+3i/32; M_s=w_s alpha_s z_s, S_s=(2/3)M_s t_s, U_s=S_s u_s. FULL independently chooses sourcewise real z_s,t_s,u_s in [0,1]; seedless LR uses common z,t,u. K3 is a true LR=4 collision and its P and Q delay probabilities r_s,v_s independently range over (0,1). The four readouts are:

    eP=107/128-21x/128+d/4-sum(S)/2
    eQ=13/64+3x/64-d/2+sum(S)/8
    TP=3+sum(M)+3sum(S)/2+sum(r_s U_s)
    TQ=3+sum(M)/2+3sum(S)/8+sum(v_s U_s)/4.

This is a typed finite two-law four-observer auxiliary; no native X6 embedding or physical calibration is asserted.

## All-real eight-parameter classification theorem

For every r,v in (0,1)^4, the convex hulls of the four-observer images are equal if and only if r and v are each constant across the four sources. Under these two conditions, the full *actual real-behaviour images* also coincide.

Let c=(1/8,1/6,1/16,3/32) and tau in (0,1). Define P_a=sum c_s(a_s-tau)_+ and N_a=sum c_s(tau-a_s)_+. For normals

    n_r(tau)=(-16,-76-8tau,1,0)
    n_v(tau)=(-16,-70-4tau,0,2)

the exact support gaps, optimizing over ALL real policies, are

    h_FULL(n_r)-h_LR(n_r)=(2/3)min(P_r,N_r)
    h_FULL(n_v)-h_LR(n_v)=(1/3)min(P_v,N_v).

These directions isolate the two laws: the first gap is independent of v and the second is independent of r. Any nonconstant r or v admits a tau between its minimum and maximum, giving a strict positive gap.

## Proof of the two formulas

Use the previously proved all-signed Bellman oracle for n=(A,B,C,D). Set K=C+D/2, H=-A/2+B/8+3C/2+3D/8, J_s=C r_s+D v_s/4. Each source with positive carrier c_s=w_s alpha_s has envelope

    F_s=max(0,K,K+(2/3)H,K+(2/3)(H+J_s)).

For n_r one has (K,H,J_s)=(1,-tau,r_s). For n_v they equal (1,-tau/2,v_s/2). In either case define a=r or v and kappa=1 or 1/2. Then F_s=1+(2kappa/3)(a_s-tau)_+.

The upstream baseline is B=constant+U x+V d, with U=(-21A+6B_direction)/128 and V=(A-2B_direction)/4 (B_direction denotes the second normal coordinate). For n_r: U=-(120+48tau)/128, V=34+4tau. For n_v: U=-(84+24tau)/128, V=31+2tau. Hence U<0 and V>0. The FULL baseline and all nonnegative source envelopes attain their maximum at (x,y,i)=(0,1,1), with c_s=w_s alpha_s=(1/8,1/6,1/16,3/32).

For LR let c_s(x,y)=(1/8,(1-x)/6,y/16,3(1-x)y/32), T=sum c_s and F=sum c_s(a_s-tau). The four joint gate choices reduce exactly to

    B(x,y)+T(x,y)+max(0,(2kappa/3)F(x,y)).

Indeed T>0, and the third gate option T(1-2kappa*tau/3) is dominated by T. The two branches B+T and B+T+(2kappa/3)F both maximize at x=0,y=1. To verify, d=y(5-3x)/32 gives partial_x B<=U<=-84/128, partial_y B>=V/16>=31/16, while partial_x T<=0, partial_y T>=0 and |partial_x F|<=25/96, |partial_y F|<=5/32. Since 0<kappa<=1, each branch has partial_x<=-84/128+25/144<0 and partial_y>=31/16-5/48>0.

At that common maximizing corner, FULL support is B_*+sum c_s+(2kappa/3)P_a; LR support is B_*+sum c_s+(2kappa/3)max(0,P_a-N_a). Their difference is (2kappa/3)min(P_a,N_a), proving both identities for every real policy.

## Proof of exact real-image equality when r and v are source-constant

Given any FULL upstream (x,y,i), d=y/16+3i/32 lies in [0,(5-3x)/32]. Choose LR y'=32d/(5-3x), i'=(1-x)y'; x and d and total carrier T=1/8+(1-x)/6+d>0 are retained. Let M=sum M_s, S=sum S_s, Udelay=sum U_s and set common LR gates z=M/T, t=3S/(2M) when M>0 else 0, u=Udelay/S when S>0 else 0. From 0<=Udelay<=S<=2M/3<=2T/3, all gates lie in [0,1]. The resulting LR policy has identical x,d,M,S,Udelay. When r_s=r0 and v_s=v0 the four observers depend only on these totals and r0,v0. Thus every FULL real observer is realized by LR; the reverse containment is immediate.

## Two exact positive rational separators and verification

Take tau=1/2, spread=(1/4,1/2,3/4,1/2), constant=(1/2,1/2,1/2,1/2).

Case P-only: r=spread, v=constant, n_r=(-16,-80,1,0). hFULL=-493/24, hLR=-1973/96; gap=1/96. A realized FULL witness is (41/48,25/192,85/24,623/192), with L-infinity distance from conv O(LR) at least 1/9312.

Case Q-only: r=constant, v=spread, n_v=(-16,-72,0,2). hFULL=-1059/64, hLR=-1589/96; gap=1/192. A realized FULL witness is (41/48,25/192,113/32,1247/384), with distance at least 1/17280.

Both witnesses use upstream (0,1,1), z_s=1 for every source, and t_s=u_s=1 exactly for sources with the selected delay parameter above tau, zero otherwise. Dual norm inequality |n.(W-V)|<=||n||_1||W-V||_infty gives the distance certificates.

The executed standard-library Fraction verifier separately enumerates 1536 distinct FULL and 16 LR deterministic observer vectors per kernel/direction, 14 rational cases, including threshold sweeps and both-law variation. Its 30 explicit exact assertions passed. Finite checks are regression evidence; the analytic proof establishes the quantified all-real result. Original longer local verifier additionally passed 85 exact assertions and three nonbinary strategy Markovization checks; that local working copy is a supplementary run, not the published source.

## Open research route and authority

This closes only the fixed K3 model with independent P/Q source-dependent *time* kernels; the four-observer mother problem remains open for altered topology and terminal answer-time coupling. Follow NEXT_TASK.md. Native Site was static read-only (research_authority_granted=false), owner listing returned CONTROL_QUOTA, so this GitHub artifact is author-side evidence, not a Source CLAIM/Result or independent Driver review. Frozen pins, P000 and protected ACTIVE worldview are unchanged.
