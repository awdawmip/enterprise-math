# R5 K3 — Exact terminal-answer threshold gaps in two four-parameter slices

Date: 2026-11-03 (Asia/Shanghai). Scientific state: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Input and scope

Predecessor: awdawmip/enterprise-math@9b03284f766c53ac8843a81d2b2c8e1f793bf571, research_notes/brc_r5_k3_independent_two_law_20261103_t1240/RESEARCH.md; inherited all-signed K3 support oracle at 2c47ed2096e2cbdc1b5bbd88291dc8583d9f72de. Scientific pins remain Global Knowledge a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Current normative context was read separately on 2026-11-03. P000 and ACTIVE worldview are unchanged.

This is a fully specified algebraic **finite two-law auxiliary** that extends the K3 four-observer map by assigning source-sensitive Bernoulli terminal answer labels to a tagged fraction of positive K3-delayed mass. The exact semantic embedding of the new auxiliary error label into the original stopping experiment's existing error event is not claimed and is the next specified task. No physical/native X6 interpretation is asserted.

## Definition

Sources s=(C,I,BJ,IJ), alpha=(1/2,2/3,1/2,3/4). FULL upstream x,y,i in [0,1], x+i<=1; seedless LR upstream i=(1-x)y. Positive source masses w=(1/4,(1-x)/4,y/8,i/8), d=y/16+3i/32. Sourcewise FULL controls z_s,t_s,u_s in [0,1]; LR uses the same common z,t,u for each source. Write M_s=w_s alpha_s z_s, S_s=(2/3)M_s t_s, U_s=S_s u_s. Fix all original P/Q K3 delay probabilities to r_s=v_s=3/4. Attach a positive answer Bernoulli fraction theta=1/8 of U_s under P and U_s/4 under Q with source probabilities p_s and q_s in (0,1).

Define actual auxiliary four-observer vector by
\[
\begin{aligned}
e_P &=107/128-21x/128+d/4-\sum_s S_s/2+\sum_s p_s U_s/8,\\
e_Q &=13/64+3x/64-d/2+\sum_s S_s/8+\sum_s q_s U_s/32,\\
T_P &=3+\sum_s M_s+3\sum_s S_s/2+3\sum_s U_s/4,\\
T_Q &=3+\sum_s M_s/2+3\sum_s S_s/8+3\sum_s U_s/16.
\end{aligned}
\]
No signed source masses are used. All original positive gate-to-source provenance is retained. With 0<=d<=5/32 and 0<=sum U<=sum S<=43/144, conservative bounds valid for all real controls are 301/576<=eP<=1051/1152<1 and 1/8<=eQ<=1/4+215/4608<1.

At FULL upstream corner (x,y,i)=(0,1,1), c_s=w_s alpha_s=(1/8,1/6,1/16,3/32), sum c_s=43/96.

## Two continuous all-real classification theorems

**Slice P:** q_s=1/2 for all four sources; p_s vary independently over (0,1). Then conv O(FULL)=conv O(LR) if and only if p_s is source-constant. In the equality case also O(FULL)=O(LR).

**Slice Q:** p_s=1/2 for all four sources; q_s vary independently over (0,1). Then conv O(FULL)=conv O(LR) if and only if q_s is source-constant. In the equality case also O(FULL)=O(LR).

More strongly, for every real tau in (0,1), let
\[
n_P(\tau)=(-8,\tfrac{64}{9}(\tau-13),4,0),\qquad
n_Q(\tau)=(\tfrac{16}{7}(5-\tau),-32,4,0).
\]
For an arbitrary vector a of the varying source probabilities put P_a=sum_s c_s (tau-a_s)_+, N_a=sum_s c_s(a_s-tau)_+. In the respective slices the following are **exact support gaps over every real behavior policy**:
\[
h_F(n_P)-h_{LR}(n_P)=\frac23\min(P_p,N_p),\qquad
h_F(n_Q)-h_{LR}(n_Q)=\frac23\min(P_q,N_q).
\]
The resulting rational normals are all-real dual separation certificates whenever min(a)<tau<max(a).

## Proof

The preceding signed K3 Bellman result applied to normal n=(A,B,C,D) gives an upstream baseline B0=constant+Ux+Vd, U=(-21A+6B)/128, V=(A-2B)/4. The **new** answer channel adds (A/8)p_s+(B/32)q_s to the source delay term; explicitly,
\[
K=C+D/2,\quad H=-A/2+B/8+3C/2+3D/8,\quad
J_s=3C/4+3D/16+(A/8)p_s+(B/32)q_s.
\]
The four exhaustive nested deterministic local gate possibilities z=0, (z,t)=(1,0), (z,t,u)=(1,1,0), (z,t,u)=(1,1,1) give
\[
F_s=\max(0,K,K+\tfrac23 H,K+\tfrac23(H+J_s)).
\]
Multi-affinity extends this Bellman optimization from local vertices to all real local gate probabilities.

In Slice P, substituting nP yields K=4, H=(8tau-14)/9<0, H+J_s=tau-p_s. In Slice Q, substituting nQ yields K=4, H=(8tau-26)/7<0, H+J_s=tau-q_s. Since -1<tau-a_s<1, both source envelopes become exactly F_s=4+(2/3)(tau-a_s)_+.

For FULL, U<-2, V>0 for either normal family and all tau in (0,1). All F_s>=4, so the baseline and every variable positive carrier can be simultaneously maximized at (x,y,i)=(0,1,1). Hence hF=B_*+4(43/96)+(2/3)P_a.

For LR, i=(1-x)y, d=y(5-3x)/32, carrier c_s(x,y)=(1/8,(1-x)/6,y/16,3(1-x)y/32), total T=sum c_s, and F_tau(x,y)=sum c_s(x,y)(tau-a_s). The common LR gate envelope equals
\[
4T(x,y)+\tfrac23\max(0,F_\tau(x,y)).
\]
Indeed the intermediate gate option 4T+(2/3)HT is dominated by 4T because H<0, while the zero gate is dominated since T>0.

For both affine pieces B0+4T and B0+4T+(2/3)F_tau, strictly decreasing x and increasing y hold throughout [0,1]^2: |partial_x F_tau|<=25/96, |partial_y F_tau|<=5/32, partial_x B0<=U<-2, partial_y B0>=V/16>0; also partial_x(4T)<=0, partial_y(4T)>=1/4. The only potentially adverse slopes are at most (2/3)(25/96)=25/144 for x and at least -(2/3)(5/32)=-5/48 for y, so both monotonicities are strict. The pointwise maximum of the two pieces preserves them. Thus LR, too, is maximized at (x,y)=(0,1), yielding
\[
h_{LR}=B_*+4(43/96)+\tfrac23\max(0,P_a-N_a).
\]
Subtract to obtain the stated gaps.

If a varies across sources, select tau strictly between its least and greatest entries, so P_a,N_a>0 and the convex hulls strictly differ. For the converse with source-constant p,q,r,v: for any FULL policy set y'=32d/(5-3x), i'=(1-x)y', preserving x,d and T=1/8+(1-x)/6+d>0. Set LR z=sum M/T; t=3sum S/(2sum M) if sum M>0, otherwise 0; u=sum U/sum S if sum S>0, otherwise 0. These gates are in [0,1], preserve total M,S,U and hence preserve all four readouts exactly. This produces an LR *real* policy for every FULL real observer and proves actual observer equality in both source-constant slices.

## Exact separators and executed evidence

Take tau=1/2, varying a=(1/4,1/2,3/4,1/2), opposite answer vector constant 1/2. Then P_a=1/32, N_a=1/64, gap=1/96. P-only n=(-8,-800/9,4,0): hF=-619/144, hLR=-1241/288, FULL witness W=(107/128,35/256,349/96,157/48), with Linf distance to conv O(LR)>=3/29056. Q-only n=(72/7,-32,4,0): hF=301/16, hLR=1805/96, witness W=(161/192,209/1536,349/96,157/48), distance>=7/31104. Both FULL witnesses use x=0,y=i=1; local gate stage 3 for a_s<tau and stage 1 otherwise. Distance bounds use the dual l1 norm of the normal.

Execute Python 3 standard-library Fraction VERIFY.py. The actually executed script checks 26 exact assertions: 3 thresholds x 4 probability patterns x 2 slices; enumerates for each case the 1536 distinct FULL deterministic controls (6 upstream extrema and four per source) and 16 LR deterministic controls (4 upstream extrema, 4 common gates), cross-checks support gaps and both displayed witnesses, and emits EXACT_OUTPUT.txt. The all-real theorem follows from the above algebra; the enumeration is a rational regression check.

**Open dependencies:** These are complete conditional slice classifications of the explicitly stated auxiliary, not a theorem covering general jointly varying p and q, not native X6 and not a solution of the mother observer-image target. Next: independently derive a positive P/Q path-level terminal answer event that yields these *exact* modified error readouts without changing timing/LR collisions; then study jointly varying p and q through the mixed J_s envelope and exact primal/dual all-signed hull certificates. GitHub artifact preservation does not issue a native CLAIM, Result, or independent Driver review.