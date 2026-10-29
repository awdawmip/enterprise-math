# BRC N=4 BU source-bit: complete b-axis exact minimax, a=49/50

Date 2026-10-29. Status: AUTHOR ANALYTIC PROOF / EXACT SYMBOLIC + 16-LEAF CHECKED / UNREVIEWED / NOT_ADMITTED. This is a finite positive P/Q stopping-tree result, not a P000 native X6 physical theorem.

## Fixed model and independently checked predecessors

For target F=(a,b,1,0), fix a=49/50 and all real 0<b<=1. Q masses for AU,AV,BU,BV are 1/6,1/3,1/4,1/4; respective P/Q ratios are 1,1/4,1,2. AU descendants have ratios 9/10,11/10; BU descendants 1/5,9/5; each is again split equally at stage 4, giving 16 strictly positive leaves. Observation is (T,Decision,Z_BU), with BU origin bit set only upon stage-3 arrival. AU and BU share every lawful common instantaneous decision.

The actual-causal observation-preserving S2/S23 reduction, and nonnegative event duals L0,L3,R, come from the immutable predecessor enterprise-math@01959291d98e6d666cf6b769889bcca623caf12c, research_notes/brc_n4_bu_expanded_rectangle_zero_wedge_20261029_r1t11/PROOF.md, Git blob 8dfee379b45b88dfe26f07375e076fa071c19843. The high-b exact result 3/50<=b<=1 is enterprise-math@2f9fd05d81744d01fa8cbd84921b57e70bb98bef, research_notes/brc_n4_bu_gamma_true_switch_20261029_r1t11/PROOF.md, blob 5ecf1a094d91fc65d6e7f53f4218699448c927b8. Both are author-side mathematical evidence awaiting independent review.

The complete lawful competitor variables satisfy 0<=A,B,c<=1, 0<=U<=A, 0<=V<=B. Define s=(A-a+B-b)/2, t=(A-a+3(B-b))/4, H=Bc/4, rQ=a/6-Ac/6-U/3-V/4, rP=a/6-Ac/6-U/12-V/2. The observed four-atom signed target-minus-competitor vectors are DeltaQ=(s,H-s-rQ,rQ,-H), DeltaP=(t,H-t-rP,rP,-H); the error e=max(TV_Q,TV_P). Each signed observable event has absolute mass <=e. The causal reduction justifies d2=d23, and it is not a relaxed occupancy optimization.

## Complete new author theorem

Let BETA=(146-sqrt(10921))/1050=0.039520391947491502612..., GAMMA=(sqrt(38494)-83)/750=0.15093183825600634856..., and c_low(b) the unique positive zero of
(a+3b)c^2+(3a+8b)c+14b-4a=0.
Let c_cap(b)=(7-a-21b)/(4a+12b+2) and c_alt(b)=(2a-7b)/(2a+4b).

Then for every real lawful causal random S2 or S23 competitor with a=49/50 and 0<b<=1, the exact common minimax is

  d2=d23=b*c_low/(4+c_low)                     for 0<b<=BETA;
        =(a+3b-1)*(7-a-21b)/(12*(4a+12b+2)) for BETA<=b<=GAMMA;
        =b*(2a-7b)/(8*(a+2b))                for GAMMA<=b<=7/25;
        =0                                    for 7/25<=b<=1.

The upper three high-b regions from b=3/50 onward are inherited from the above immutable high-b theorem. New in this release: the algebraic root phase 0<b<=BETA (including all b<1/150 where the old capacity strategy is infeasible) and proof of the bridging capacity optimum BETA<=b<=3/50. Boundaries are continuous: at BETA both first formulas equal 1/150, and the earlier source establishes continuity at GAMMA and 7/25.

## NEW complete-event convex dual: K(c)

Set Q1=s, Q7=H (Q atoms 1+2+3), and P6=H-t (P atoms 2+3). The three nonnegative weights w1=c/(4+c), w2=(4-2c)/(4+c), w3=2c/(4+c), valid on every 0<=c<=1, sum exactly to 1. For every competitor,

 w1*Q1+w2*Q7+w3*P6
   =c*(s-2t)/(4+c)+4H/(4+c)
   =c*(b-B)/(4+c)+Bc/(4+c)
   =b*c/(4+c)=K(c).

Hence e>=K(c), uniformly over all lawful real strategies. This uses actual observable events including the BU bit and is valid without assuming A=1 or V=B.

The exact old event duals are
 L0(c)=[4a-14b-3ac-(a+3b)c^2]/[2(23-2c)]<=e, 0<=c<=3/7;
 L3(c)=c[a-(a+3b)c]/[2(7-2c)]<=e, 0<=c<=1;
 R(c)=c(a+3b-1)/12<=e, 0<=c<=1.

Their load-bearing event certificates can be checked directly. Put Q2=H-s-rQ, Q3=H-rQ, Q7=H, P4=rP, P5=t+rP, and H-s=Q2+(third Q atom). For L0, convex weights on Q2,H-s,P4,P5 are (c+4,3-7c,2(1+4c-c^2),2(c^2-2c+7))/(23-2c). The weighted event sum plus 7(c+4)(V-B)/[4(23-2c)] is exactly L0, and V-B<=0. For L3, convex weights on Q3,Q7,P4,P5 are (c,7(1-c),2c(2-c),2c^2)/(7-2c); weighted event sum plus 7c(V-B)/[4(7-2c)] is exactly L3. All weights are nonnegative in their declared intervals. Exact VERIFY_RELEASE.py checks the identities. L0 decreases on [0,3/7]. L3 has no interior minimum on any [u,v] subset of [0,1], because its derivative sign polynomial D=7a-14(a+3b)c+2(a+3b)c^2 has D'=(a+3b)(4c-14)<0.

## New small-b interval: all 0<b<=BETA

Define f_b(c)=(a+3b)c^2+(3a+8b)c+14b-4a. For b<=1/25, f_b is strictly increasing on c>=0, f_b(4/5)=6(2325b-98)/625<0, f_b(1)=25b>0. Thus c_low lies in (4/5,1). Identity
 L3(c)-K(c)= -c*f_b(c)/[2(7-2c)(4+c)]
gives L3(c_low)=K(c_low)=:e_low. At a=49/50 and b<=1/25,
 L0(3/7)-b/4=(196-2025b)/3500 >=115/3500>0,
 L3(3/7)-b/4=(588-8875b)/30100 >=233/30100>0.
Since e_low<=b/4, both dual endpoint values exceed e_low.

Partition every competitor c into [0,3/7], [3/7,c_low], [c_low,1]. Decreasing L0 gives e>=L0(3/7)>e_low on the first; no-interior-minimum L3 gives e>=min(L3(3/7),L3(c_low))=e_low on the second; increasing K gives e>=K(c_low)=e_low on the third. The lower bound thus covers all real c, not a search grid.

Construct the actual lawful causal matching policy with c=c_low:
 B=4b/(4+c), H=bc/(4+c), A=a+3H, U=B(1+c), V=B.
Direct substitution and f_b(c)=0 give s=H,t=0,rQ=0,rP=H, so DeltaQ=(H,0,0,-H), DeltaP=(0,0,H,-H), and both TVs equal e_low. Furthermore B<=b, V=B, U<=2b<a<=A. To prove capacity A<=1, parameterize the positive root by
 b(c)=a(1-c)(4+c)/(3c^2+8c+14),
 H(c)=ac(1-c)/(3c^2+8c+14).
Their derivatives in c are respectively a(c^2-52c-74)/D^2 and -a(11c^2+28c-14)/D^2, D=3c^2+8c+14; both are strictly negative on [4/5,1]. Hence H rises with b. A<=1 iff H<=1/150; equality solves 150c^2-139c+14=0 at c=(139+sqrt(10921))/300 and precisely b=BETA. Thus the matching lawful witness exists for all 0<b<=BETA, proving the first exact phase.

## New bridge: BETA<=b<=3/50

For this entire interval use A=1, B=(a+3b-1)/3=b-1/150, c=c_cap(b), U=B(1+c), V=B. B>0; c_cap decreases from (139+sqrt(10921))/300<1 to 119/166>3/7; and U<=2b<=3/25<1. This is a real lawful policy. Its signed observations are
 DeltaQ=(1/150,e_cap-1/150,0,-e_cap),
 DeltaP=(0,0,e_cap,-e_cap),
 e_cap=c_cap(a+3b-1)/12.

Set G=5a^2+8ab-21b^2-2b-5. Exact factorization
 G=-21(b-BETA)(b-(146+sqrt(10921))/1050)
shows G>=0 on this interval; and 3e_cap-(1-a)=3G/[8(2a+6b+1)] guarantees e_cap>=1/150. Therefore both actual TV errors are e_cap.

For all competitor c, use L0,L3,R duals. The exact identity L3(c_cap)=R(c_cap)=e_cap holds; 3/7<c_cap<1, R increases since a+3b-1>0. For b<=3/50,
 L0(3/7)>=127/3500>1/75>=e_cap,
 L3(3/7)>=507/30100>1/75>=e_cap
because c_cap<=1 and a+3b-1<=4/25. Partition [0,1] into [0,3/7], [3/7,c_cap], [c_cap,1]; L0, L3, R respectively prove e>=e_cap throughout. This exactly matches the feasible witness. At BETA, c_low=c_cap and both e equal 1/150; at 3/50, the previously proved continuous high-b phase begins. This closes 0<b<=1 at author-proof level.

## Verification and boundary

The locally executed full VERIFY.py checked 29 exact symbolic identities, witness divisibility by f_b, exact capacity radicals, 16 positive P/Q leaves and five algebraic low-b points (b=1/1000,1/150,1/100,1/50,1/30). Released VERIFY_RELEASE.py executes the core exact dual and witness identities. Finite checks confirm algebra and implementation, while the above event certificate proves the continuous theorem.

Source snapshots checked this turn: GLOBAL_KNOWLEDGE_V1 main@1ed9afe8dc2ca7e9b833fdde51048253b678fa6b, enterprise-math initial main@4d641868367e435cb350b7dbaa46b02f48f976d3. Site gateway research_authority_granted=false, owner/task read returned CONTROL_QUOTA: this is author-side portable research, not a canonical CLAIM/Result/review. The native P000 X6, three-dimensional slice and independent time embedding remain separate obligations.

Next precise unit: free a near 49/50, extend the new K-L3 algebraic phase to a nonempty open 2D parameter set with all causal capacities, and decide whether its capacity boundary remains a true minimax switch.
