# R5 K3 — Non-proportional equal two-clock hulls and a four-observer residual

Date: 2026-11-04 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Sources, scope and frozen science
Predecessor: immutable enterprise-math commit 1a20faa45098c3d69e45430c42eb516e56c4a8e9, research_notes/brc_r5_k3_asymmetric_clock_face_fiber_20261103_t2340/RESEARCH.md, PR #1663.
Frozen science pins: GLOBAL_KNOWLEDGE_V1@a01383f825ef9d43b4b754254303298c64041568 and enterprise-math@86149263e38c22292c9def1e0f69092efa1be77e. Current behavior rules read separately. P000 and ACTIVE worldviews remain unchanged. This is a two-law finite common-terminal-label auxiliary experiment, not an asserted native X6 embedding.

The mother target is equality of FULL and seedless LR **four-observer convex hulls** with unequal actual real-behavior images. Here we classify a new time-plane equality family and identify its distinct error-observer fiber.

Four positive-provenance BRC sources C,I,BJ,IJ have capacity c=(1/8,1/6,1/16,3/32). FULL controls 0<=x,y<=1, 0<=i<=1-x, and four independent continuation stages. LR has i=(1-x)y and one common stage. Set w=(1/4,(1-x)/4,y/8,i/8), alpha=(1/2,2/3,1/2,3/4), d=y/16+3i/32, M_s=w_s alpha_s z_s, S_s=(2/3)M_s t_s, U_s=S_s u_s. All behavior variables are in [0,1]. For independent p_s,q_s,r_s,v_s in (0,1), the readouts are

eP=107/128-21x/128+d/4-sum(S)/2+sum(p_s S_s/8)
eQ=13/64+3x/64-d/2+sum(S)/8+sum(q_s S_s/32)
TP=3+sum(M)+3sum(S)/2+sum(r_s U_s)
TQ=3+sum(M)/2+3sum(S)/8+sum(v_s U_s/4).

BRC reuse state: REUSE_APPLIED — preserve source identity, positive mass and the d residual while examining information lost by the two-clock projection. No novelty claim for a shared general tool.

## Theorem 1 (complete signed clock-plane support equality, continuous non-proportional family)
Let 0<L<R<1 and take real lambda>1. Define
V=(lambda(3+2R)-3)/2, W=(lambda(3+2L)-3)/2,
r=(R,R,L,L), v=(V,V,W,W).
Assume R<V<min(1,3R/2) and L<W<min(1,3L/2). For each pair 0<L<R<1 these inequalities hold for lambda>1 sufficiently close to 1. For all p,q in (0,1)^4 and for every real behavior policy,

conv{(TP,TQ):FULL} = conv{(TP,TQ):LR}.

The clock kernels are genuinely non-proportional: V/R=lambda+3(lambda-1)/(2R) differs from W/L=lambda+3(lambda-1)/(2L).

**Proof.** For signed clock normal (a,b), the source-level four deterministic vectors after subtracting the baseline (3,3) are
P0=(0,0), P1=(1,1/2), P2=(2,3/4), P3(r,v)=(2+2r/3,3/4+v/6).
For r<v<3r/2, P2 is strictly inside the triangle conv{P0,P1,P3}. The barycentric weights at P1,P3,P0 respectively are
beta=(6r-4v)/(3+4r-2v), gamma=3/(3+4r-2v), delta=2(v-r)/(3+4r-2v);
all are positive and sum to one. Hence stage 2 is never needed for support optimization.

Define h_r,v(a,b)=max(0,a+b/2,(2+2r/3)a+(3/4+v/6)b).
The stage-3-minus-stage-1 score factors as
(1+2r/3)(a+lambda*b/4);
its sign is common to the R/V and L/W groups. Let
mu(r,v)=(9+2v)/(8(3+r))=[6+lambda(3+2r)]/[8(3+r)].
Then d mu/dr=3(lambda-2)/[8(3+r)^2]. The inequalities v<3r/2 imply lambda<2 and mu<3/8; therefore mu_R<mu_L<3/8.

Because each source max h>=0, FULL's exact clock support is
3(a+b)+(7/24)h_R,V(a,b)+(5/32)h_L,W(a,b).
To realize it within LR: for b>0, either stage 0 is jointly optimal or a common stage 1 or 3 maximizes both groups. Indeed stage 3 positive implies stage 1 positive (mu<3/8<1/2), and the stage-1/stage-3 comparison has the same sign. Use upstream (x,y,i)=(0,1,1). For b<0, any positive source score is maximized at stage 3: stage 3 positive means a/(-b)>mu>lambda/4, hence stage 3 dominates stage 1. If the L group is positive, so is R since mu_R<mu_L; use upstream (0,1,1) and common stage 3. If only R is positive, choose upstream (0,0,0) to keep C/I while masking BJ/IJ, common stage 3. If neither group positive choose stage 0. For b=0, choose stage 3 when a>0, else 0. Thus every real signed clock support direction agrees. LR is included in FULL and the compact convex hulls coincide by separation. QED.

## Theorem 2 (the complete four-observer hulls separate throughout this family)
For the same parameters mu_R<mu_L<3/8. Choose any m in (mu_R,mu_L) and let
A_R=2m-3/4+(4mR-V)/6>0,
A_L=2m-3/4+(4mL-W)/6<0,
g=min{A_R/6, -A_L/16-3A_L/32}>0,
eps=g/2.

The clock normal (0,0,m,-1) has the unique LR maximizing observation H from upstream (0,0,0), common stage 3. FULL may take upstream (0,1,1) and source stages (3,3,0,0), producing W, with
W-H=(5/128,-5/64,0,0).
The original clock-face lemma at the predecessor immutable commit proves (and direct comparison of the 16 LR deterministic vertices confirms) that each other LR vertex loses at least g in clock support. As every LR eP value is in (0,1), the perturbed normal n=(eps,0,m,-1) still uniquely maximizes H in LR, and
n.W-h_LR(n)=5eps/128>0.
Consequently the FULL/LR four-observer convex hulls differ, for **every p,q in (0,1)^4**, and
dist_infinity(W,conv O(LR)) >= (5eps/128)/(1+m+eps)>0.
The projection has erased a genuine BRC upstream d-fiber, rather than established four-dimensional equality. QED.

## Executed exact rational example
R=3/5, L=1/4, lambda=36/35, V=33/50, W=3/10, p=q=(1/2,1/2,1/2,1/2).
Non-proportional ratios: V/R=11/10, W/L=6/5.
The common exact CCW two-clock convex hull consists of
(3,3), (37/10,3901/1200), (3877/960,4051/1200), (331/96,619/192).

Take m=11/30, mu_R=43/120, mu_L=24/65, A_R=1/50, A_L=-1/180,
g=1/1152, eps=1/2304.
FULL witness W=(455/576,39/256,37/10,3901/1200).
LR clock-exposed H=(865/1152,59/256,37/10,3901/1200).
Normal n=(1/2304,0,11/30,-1) gives
h_FULL=-62832529/33177600, h_LR=-125666183/66355200,
support gap=5/294912, infinity-distance lower bound=25/2015872.

Actual Python standard-library fractions.Fraction program VERIFY.py executed and generated EXACT_OUTPUT.txt. It exhaustively generated 1,536 FULL and 16 LR deterministic observations, exactly built both time-plane convex polygons, checked each of the 1,552 deterministic time vectors against the opposite polygon, and verified the strict four-dimensional signed separator and exposed face. 1,573 exact assertions passed. Finite enumeration proves the rational finite-instance hull equality under the established multi-affine deterministic-hull reduction; the all-real continuous theorem is the analytical argument above.

Native Site status observed 2026-11-04 00:38 Asia/Shanghai: static_machine_readonly, research_authority_granted=false; bounded owner query returned CONTROL_QUOTA. Hence active owner/CLAIM/Result/independent Driver review are unconfirmed; this PR research note is author-side preservation, not Source task admission.

Next discriminating unit: outside mu_R<mu_L<3/8, construct clock-equihull examples with matching non-singleton LR/FULL error fibers; use exact rational 4D convex-combination or Farkas certificates before attempting real observer-image nonmembership.
