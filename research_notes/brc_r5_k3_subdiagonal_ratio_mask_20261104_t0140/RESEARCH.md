# R5 K3 — Two exact clock-hull obstructions: ratio dispersion and upstream mask

Date: 2026-11-04 Asia/Shanghai.
Evidence level: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
Mother objective: a common-terminal-label finite P/Q experiment with equal four-observer FULL and seedless-LR convex hulls but unequal actual real-policy observation sets.

## Source and type

Scientific inputs remain frozen at GLOBAL_KNOWLEDGE_V1@a01383f825ef9d43b4b754254303298c64041568 and enterprise-math@86149263e38c22292c9def1e0f69092efa1be77e. Direct predecessor is immutable enterprise-math commit f7584614dee2ae7440dc7994cb4af66da7219cc0, research_notes/brc_r5_k3_nonproportional_clock_hull_20261104_t0040. The governing current normative context was read separately. P000 and ACTIVE X6 worldview were not changed; this is an auxiliary finite P/Q observer experiment, not a proved native X6 physical embedding.

Four labeled strictly positive BRC masses C,I,BJ,IJ have capacities c=(1/8,1/6,1/16,3/32). FULL upstream variables are 0<=x,y<=1 and 0<=i<=1-x; LR requires i=(1-x)y and shares a single K3 stage. Let w=(1/8,(1-x)/6,y/16,3i/32), d=y/16+3i/32, M_s=w_s z_s, S_s=(2/3)M_s t_s and U_s=S_s u_s. Stage corners are 0=(0,0,0), 1=(1,0,0), 2=(1,1,0), 3=(1,1,1). For each s, p_s,q_s,r_s,v_s in (0,1), the four observers are

eP = 107/128 -21x/128 + d/4 - sum(S)/2 + sum(p_s S_s/8)
eQ = 13/64 +3x/64 - d/2 + sum(S)/8 + sum(q_s S_s/32)
TP = 3 + sum(M) +3sum(S)/2 + sum(r_s U_s)
TQ = 3 + sum(M)/2 +3sum(S)/8 + sum(v_s U_s/4).

For a linear support direction, the available deterministic extreme configurations number 6*4^4=1536 FULL and 4*4=16 LR. Their convex hulls capture all real randomized behavioral policies by the stage-wise multilinear extreme reduction and the upstream triangle-times-segment / LR unit-square extremality. The following analytic arguments independently establish the claimed all-real formulas. BRC reuse: REUSE_APPLIED, retaining separate positive source mass, source mask, and residual clock output (no new shared tool claim).

## Theorem A — universal subdiagonal clock-ratio dispersion formula

Suppose 0<v_s<r_s<1 at ALL four sources; p_s and q_s are arbitrary in (0,1). For 0<t<1/4 set n_t=(0,0,-t,1). Then the exact FULL minus LR support gap is

(A1) Delta(t) = min { sum_s c_s (v_s-4r_s t)_+, sum_s c_s (4r_s t-v_s)_+ } / 6.

Define R_c=sum_s c_s r_s, V_c=sum_s c_s v_s, kappa=V_c/R_c, and t_*=kappa/4. It lies strictly inside (0,1/4) and maximizes the exact wedge gap:

(A2) Delta(t_*) = (1/12) sum_s c_s |v_s-kappa r_s|.

If the four source ratios v_s/r_s differ, the maximum is strictly positive and the maximizing t_* within the wedge is unique. Thus equality of FULL/LR two-clock hulls (and hence four-observer hulls) on the strict subdiagonal chamber REQUIRES v_s=kappa r_s for all four sources; the necessary ratio equality is not sufficient, as Theorem B proves.

Proof. Subtract the shared (3,3) time baseline. Per unit available source mass the four stage clock vectors are P0=(0,0), P1=(1,1/2), P2=(2,3/4), P3_s=(2+2r_s/3,3/4+v_s/6). Their (-t,1)-scores are 0, 1/2-t, 3/4-2t, and 3/4-2t+(v_s-4r_s t)/6. For 0<t<1/4 and 0<v_s<r_s<1, stage 2 beats stage 1, stages 2 and 3 are strictly positive (stage 3 >1/12), and stage 0 cannot maximize. Every source mass w_s is <=c_s; all four capacities can be reached together by the feasible upstream (x,y,i)=(0,1,1). FULL therefore has support 3(1-t)+sum_s c_s max(score2,score3_s). In LR, the stage must be common, and either stage 2 or 3 with the LR upstream (x,y)=(0,1) attains every capacity; so LR support is 3(1-t)+max{sum_s c_s score2, sum_s c_s score3_s}. Their exact difference is (A1).

The positive-part sum in (A1) decreases in t, and the negative-part sum increases in t. Their difference is the linear residual sum_s c_s(v_s-4r_s t); they meet at t_*. That intersection maximizes their minimum, proving (A2). If the source ratios are nonconstant, both signs occur at t_* and monotonicity on active terms makes this maximum strict and unique. If constant, A1 is identically zero in the wedge. QED.

Constructive separation: at (x,y,i)=(0,1,1), choose source stage 3 when v_s>kappa r_s and stage 2 otherwise. This actual FULL observation W attains its signed support, hence

(A3) dist_infinity(W,conv O(LR)) >= [sum_s c_s |v_s-kappa r_s|]/[12(1+kappa/4)].

Exactly the same distance bound holds for the two-clock projection, because the normal has zero error components and L1 norm 1+kappa/4.

## Theorem B — independent upstream-mask obstruction even when ratios agree

Suppose 0<k<1, v_s=k*r_s, and 1>r_C>=r_I>=r_BJ>r_IJ>0. Define
mu_s=(9+2v_s)/(8(3+r_s)),
A_s(t)=(2+2r_s/3)t-3/4-v_s/6.
Since d mu(r,kr)/dr=(6k-9)/[8(3+r)^2]<0, we have mu_C<=mu_I<=mu_BJ<mu_IJ<3/8. For EVERY real t in (mu_BJ,mu_IJ), m_t=(0,0,t,-1) has exact gap

(B1) h_FULL(m_t)-h_LR(m_t)=min{ A_BJ(t)/16, -3 A_IJ(t)/32 }>0.

Proof. At this normal, stage 1 has score t-1/2<0 and stage 2 has 2t-3/4<0, while stage 3 has A_s(t), with zero at mu_s. Since mu_BJ<t<mu_IJ, stage-3 scores satisfy A_C>=A_I>=A_BJ>0>A_IJ. For the ordering use t>mu_BJ>k/4 and dA/dr=(4t-k)/6>0.

FULL retains all capacities using (x,y,i)=(0,1,1), choosing stage 3 for C,I,BJ and stage 0 for IJ; its support above baseline equals c_C A_C+c_I A_I+c_BJ A_BJ. LR upstream masks at a common stage 3 are C+I, C+I+BJ+IJ, C, C+BJ. Since c_I A_I >= c_BJ A_BJ>0, C+BJ and C cannot beat C+I. Stage 0 contributes zero; common stages 1 and 2 contribute negatively. LR support above baseline is c_C A_C+c_I A_I+max(0,c_BJ A_BJ+c_IJ A_IJ). Subtract to obtain B1. This proves full real-policy two-clock separation for every p,q. QED.

Let a_B=c_BJ(2+2r_BJ/3), a_J=c_IJ(2+2r_IJ/3). The two branches of B1 meet at
t^diamond=(a_B mu_BJ+a_J mu_IJ)/(a_B+a_J),
with maximum over THIS exposed-mask interval
Delta^diamond=a_B*a_J*(mu_IJ-mu_BJ)/(a_B+a_J)>0.
No global optimization over every signed normal is asserted.

## Exact executed instances (Python fractions.Fraction only)

VERIFY.py executed; saved EXACT_OUTPUT.txt is its complete actual output. Three rational subdiagonal kernels each generate and score 1536 FULL and 16 LR deterministic 4D points, checking eight signed wedge directions, the closed gap expression, strict positivity and actual witness. Two additional complete signed mask enumerations check B1. 114 exact assertions passed. The analytic derivation proves the universal real-parameter statements; enumeration is rational regression.

1. Grouped nonproportional: r=(3/5,3/5,1/4,1/4), v=(3/10,3/10,1/5,1/5), with nonuniform p,q. Kappa=76/137, t*=19/137, source stages (2,2,3,3).
W=(1709/2304,515/3072,251/64,1283/384), n=(0,0,-19/137,1).
h_FULL=147157/52608, h_LR=147073/52608, exact gap 7/4384, distance >=7/4992.

2. Four ungrouped source times: r=(3/5,1/2,2/5,1/4), v=(3/10,3/10,1/5,1/5), p=q=1/2. Kappa=228/397, t*=57/397, stages (2,3,2,3), gap=59/47640, distance >=59/54480. Hence Theorem A does not require earlier two-group symmetry.

3. Equal-ratio obstruction: r=(3/5,1/2,2/5,1/4), v=r/2, p=q=1/2. At t=7/20, stage-3 scores A=(1/25,1/40,1/100,-1/80), gap=1/1600, distance >=1/2160. Actual FULL witness W=(889/1152,81/512,1379/360,9449/2880), stages (3,3,3,0). The interval-optimal t^diamond=931/2648 has gap 9/10592 and distance >=3/4772. Full enumeration confirms both. A separate grouped v=r/2 control correctly gives wedge gap zero; this is only a wedge statement, not an assertion of full-hull equality.

## Research consequence, status and next unit

Theorem A isolates positive-BRC source ratio heterogeneity; Theorem B detects a source mask that a shared LR upstream cannot realize even on the ratio-locked surface. This screens two continuous families from the four-observer mother target, without treating an exclusion of these mechanisms as a universal impossibility claim.

Next: analyze all 24 strict orderings of r_C,r_I,r_BJ,r_IJ on v_s=k r_s, 0<k<1, with boundary ties handled separately. Determine complete signed two-clock hull equality or furnish exact separating normals, then check error-observer fibers for survivors. For an all-four-observer rational equality candidate certify every FULL extreme point by a <=5-vertex rational LR convex combination; otherwise provide a rational Farkas separator. Only then test behavioral-image nonmembership.

Native status observed 2026-11-04: Site static_machine_readonly, research_authority_granted=false; active-owner lookup CONTROL_QUOTA. GitHub identity awdawmip has project write permission. Formal owner/CLAIM/Result/review and native Researcher-ID remain unconfirmed; this is author-side immutable source handoff only.
