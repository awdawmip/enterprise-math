# R5: All-signed K3 Bellman oracle and a rank-two source gate fiber
2026-11-03 Asia/Shanghai. AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Provenance and scope
Mother objective: find a finite genuine P/Q stopping experiment with equal FULL-history and seedless LR four-observer convex hulls but different actual real-behavior observer sets. This note advances the physical third LR collision K3 of Enterprise Math commit 9bcdb1337dbe9d7b05e99010e0a2a55edce59524, RESEARCH.md in research_notes/brc_r5_k3_extra_collision_gate_20261103_t0943/. Scientific pins retained: global a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. P000, active native X6+time worldview unchanged. This is a positive-mass BRC source-flow auxiliary; physical X6 calibration is not asserted.

## Exact four-observer
Let sources s=(C,I,BJ,IJ), controls x,y,i real in [0,1], i<=1-x for FULL, i=(1-x)y for LR; further FULL controls z_s,t_s,u_s in [0,1] sourcewise, whereas LR imposes common z,t,u. Let
 w=(1/4,(1-x)/4,y/8,i/8), alpha=(1/2,2/3,1/2,3/4), c0=2/3,
 d0=y/16+3i/32, M_s=w_s alpha_s z_s, S_s=c0 M_s t_s, U_s=S_s u_s.
K3 is the physical likelihood-ratio-four collision at time 5. Strictly positive Bernoulli extension probabilities r_s,v_s in (0,1) give P-clock increment r_s U_s, Q-clock increment v_s U_s/4, with the complementary outcomes normalized. The predecessor observer is:
 eP=107/128-21x/128+d0/4-sum(S)/2;
 eQ=13/64+3x/64-d0/2+sum(S)/8;
 TP=3+sum(M)+3sum(S)/2+sum(r_s U_s);
 TQ=3+sum(M)/2+3sum(S)/8+sum(v_s U_s)/4.
The source-positive carrier preserves s, w_s, M_s, S_s, U_s. Signed coefficients occur only in the observer.

## Theorem 1 (all real, all signed directions)
For arbitrary n=(A,B,C,D) in R^4, define
 K=C+D/2; H=-A/2+B/8+3C/2+3D/8; J_s=C r_s+D v_s/4;
 B_n(x,y,i)=A(107/128-21x/128+d0/4)+B(13/64+3x/64-d0/2)+3(C+D);
 F_s=max(0,K,K+c0 H,K+c0(H+J_s)).
Let VF={(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0)}.
Then, for every r_s,v_s in (0,1),
 h_FULL(n)=max_{(x,y,i) in VF} [B_n(x,y,i)+sum_s w_s alpha_s F_s].
For LR put i=(1-x)y, T=sum_s w_s alpha_s, Jtot=sum_s w_s alpha_s J_s. Then
 h_LR(n)=max_{(x,y) in {(0,0),(0,1),(1,0),(1,1)}} [
  B_n(x,y,(1-x)y)+max(0,K T,(K+c0 H)T,(K+c0 H)T+c0 Jtot)].
This exact oracle evaluates six FULL upstream source envelopes and four LR upstream four-option envelopes, rather than enumerating 24,576 FULL deterministic policies per kernel.

Proof. Substitution gives exactly
 n·O=B_n+sum_s w_s alpha_s z_s [K+c0 t_s(H+u_s J_s)].
FULL may optimize each source triple independently. Its extreme alternatives z=0; z=1,t=0; z=t=1,u=0; z=t=u=1 give F_s. Since w_s>=0 and w_s and B_n are affine in x,y,i, the resulting upstream maximum is at a vertex of the triangular prism {x,i>=0,x+i<=1,0<=y<=1}; these are exactly VF. For LR, one common (z,t,u) yields the four aggregate alternatives shown. For any such alternative i=(1-x)y makes the remaining objective bilinear in (x,y), so maximizing consecutively over x and y places a maximum at a rectangle corner. Taking the max over all four alternatives proves the formula for ALL real behavioral policies, including interior mixtures. QED.

## Theorem 2 (conditional fiber rank and eliminability)
Fix a legal pre-K3 FULL policy and its source flows S_s. Changing only the source-conditioned K3 gates produces the exact (TP,TQ) increment zonotope
 Z_FULL=sum_s [0,S_s(r_s,v_s/4)].
With the same fixed pre-K3 flow but one common LR gate, the increment set is
 Z_LR=[0,sum_s S_s(r_s,v_s/4)].
If two sources with S_s>0 have different ratios v_s/r_s, Z_FULL has nonempty two-dimensional interior and Z_LR is a segment. If all active ratios agree, the two CONDITIONAL increment sets coincide.
Proof: these are linear images of the independent source cube and of a single common scalar. The rank of the 2-by-4 source-vector matrix is the affine dimension of the FULL zonotope. With r_s,S_s>0, rank one means all generators are collinear on the same positive ray, and their Minkowski sum is the aggregate segment. QED. This conditional statement alone does not decide global convex-hull equality after upstream retuning.

## Rational instance: a zero-gap earlier direction, a new positive gap
Let r=(1/2,1/2,1/2,1/2), v=(1/4,1/2,3/4,1/2). All Bernoulli outcomes and complements are positive. For n0=(0,0,-1/2,4), all v_s-r_s/2>=0, so h_FULL(n0)-h_LR(n0)=0. For n1=(0,0,-1,4), K=1,H=0,J=v-r=(-1/4,0,1/4,0), and the all-signed formula yields:
 h_FULL(n1)=227/24, h_LR(n1)=907/96; gap=1/96.
A true FULL maximizer x=0,y=i=1, all z_s=t_s=1, u=(0,0,1,0) has
 W=(209/288,187/1152,47/12,107/32).
A true LR maximizer x=0,y=1, common z=t=1,u=0 has
 V=(209/288,187/1152,187/48,427/128).
Since ||n1||_1=5, dist_infty(W,conv O(LR))>=1/480.
For that fixed FULL pre-gate flow S=(1/12,1/9,1/24,1/16), the C-only and BJ-only gate increment vectors are (1/24,1/192) and (1/48,1/128), whose determinant equals 1/4608>0.

## Verification
The accompanying independent standard-library Fraction verifier was executed. Its exhaustive test enumerates 24,576 FULL and 32 LR deterministic observer vectors for EACH of two distinct positive rational P/Q K3 kernels, and verifies ten signed directions per kernel against BOTH oracle supports, plus the explicit witness, exact gap, two-dimensional fiber determinant and Linfinity bound. All 59 explicit Fraction assertions passed. These tests independently confirm the finite configurations; universal real assertions follow from the proof, not from sampling the normal space.

## Next question
Apply the exact support oracle and rational convex combinations of at most five LR vertices per FULL deterministic vector to find all-signed hull equality or a rational Farkas separator for source-heterogeneous K3 kernels. Investigate constant v_s/r_s with nonconstant positive r_s. Only after hull equality should actual real behavior-image nonmembership be tested semialgebraically. Preserve scientific pins, source roles and independent Driver review requirement.