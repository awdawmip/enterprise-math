# R5 — Exact time-only hull equivalence can hide first-kernel differences

2026-11-05. TASK_RESEARCH author-side portable checkpoint. AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: GLOBAL a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Scientific predecessor: commit 706d2a90558c927a3ed03bbf9e9fa2df3cb5583b, research_notes/brc_r5_universal_late_kernel_separation_20261105_t1242/RESEARCH.md. Current normative rules separately refreshed.

## Exact finite statistical BRC

At t=1 the current likelihood ratio is 1. Hidden sources h=A,B have common P/Q prior weights w_A=w_B=1/2. At t=1 each FULL policy may stop and freely declare P/Q or continue. A continued path has t=2 ratio r_j from a common finite R, drawn under Q from strictly positive source-dependent K_h(j), satisfying sum K_h=1 and sum r_j K_h=1. At t=2, a policy may stop and declare or continue to t=3 with strictly positive conditional terminal Q kernel M_h,j(l) on shared S, sum M_h,j=1 and sum s_l M_h,j(l)=r_j; it then declares freely. The corresponding P probabilities are Q masses times the likelihood ratio. FULL observes h and (time,ratio); seedless LR observes only (time,ratio). Real-valued randomization is unrestricted. Observer O4=(e_P,e_Q,T_P,T_Q), with e_P=P(declare Q), e_Q=Q(declare P), and T the respective expected stopping times. This is a typed statistical BRC auxiliary observer, not a native X6 dynamics calculation.

For n=(a,b,g,d), L(r)=max(a*r,b), c(r)=-(g*r+d). Let A_h=sum_j K_h(j)L(r_j)-L(1), B_hj=sum_l M_hj(l)L(s_l)-L(r_j), X_h=A_h-c(1)+sum_j K_h(j)[B_hj-c(r_j)]_+, with [z]_+=max(z,0). For source-independent late kernels M_j, the late Jensen residual eta=0, giving h_FULL(n)=L(1)-c(1)+sum_h w_h[X_h]_+ and h_LR(n)=L(1)-c(1)+[sum_h w_h X_h]_+. These expressions are supports of the complete four-dimensional convex hulls; backward induction proves them for all real normal directions.

## Lemma: two critical strikes characterize all time-only supports

Assume finite positive R with min R<1<max R and all K_h positive, mean one. Define f_h^-(t)=t-1+sum_j K_h(j)(t-r_j)_+ and f_h^+(t)=1-t+sum_j K_h(j)(r_j-t)_+. Each f_h^- is continuous, strictly increasing, negative at min R and positive at 1, hence has one root rho_h^- in (min R,1). Each f_h^+ is strictly decreasing, positive at 1 and negative at max R, hence has one root rho_h^+ in (1,max R). For time-only n=(0,0,g,d), all terminal classification payoffs and B_hj equal zero, whatever the late kernel. Setting c(r)=alpha(r-t), alpha>0, gives X_h=alpha f_h^-(t); setting c(r)=alpha(t-r) gives X_h=alpha f_h^+(t). Constant c makes all X_h identical. Since the Jensen gap sum_h w_h[X_h]_+ - [sum_h w_h X_h]_+ equals zero exactly when all X_h have the same weak sign, FULL and LR support functions coincide at EVERY real time-only normal iff all positive-weight sources have the same rho^- AND the same rho^+. If the roots differ, choose t between two of them; the Jensen gap is strictly positive. QED.

For a three-ratio common alphabet r1<r2<r3 with r1<1<r3, every nonzero difference delta K with zero total mass and zero ratio moment equals lambda(r3-r2,r1-r3,r2-r1). For t in (r1,1), the lower hinge difference sum_j delta K_j(t-r_j)_+ equals lambda(r3-r2)(t-r1) when t<=r2 and lambda(r2-r1)(r3-t) when t>r2; it never vanishes. The two rho^- roots differ, hence K_A!=K_B yields strict time-only hull separation, independent of all late kernels. With two ratio nodes the normalization and mean already uniquely fix K.

## Exact five-node construction

Take R=(1/4,1/2,1,3/2,7/4), K0=(1/8,1/4,1/4,1/4,1/8), and D=(15,-26,22,-26,15). Let
K_A=K0+D/512=(79/512,51/256,75/256,51/256,79/512),
K_B=K0-D/512=(49/512,77/256,53/256,77/256,49/512).
Both are positive unit-mass Q kernels with mean ratio 1. At rho^-=37/44 and rho^+=51/44, the exact signed hinge moments of D vanish:
15*(26/44)-26*(15/44)=0,
-26*(15/44)+15*(26/44)=0.
K0 itself has those two roots, so both KA and KB share both roots. The lemma proves equality of their entire two-time-coordinate convex hulls, for every (g,d), despite KA!=KB.

Now impose common M_j on S=(1/8,1/2,1,3/2,15/8). Put epsilon=1/16, m(r)=(r-epsilon)/(1-epsilon), q(r)=(m(r)-1/8)/(15/8-1/8) and
M_j(l)=epsilon/5+(1-epsilon)*((1-q(r_j))*1_{l=1}+q(r_j)*1_{l=5}).
Every M_j(l) is positive (at least 1/80), its sum is one, and its S moment is exactly r_j. Thus all P and Q transitions are legitimate strictly positive rational probabilities.

Choose n=(-1,-1,0,-13/50), so L(r)=max(-r,-1) and c(r)=13/50. Direct fractions give the shared late classification gains
B_j=(67,227,547,227,67)/1280.
Only node r=1 strictly continues at t=2 (all others stop). The early classification gains are A_A=441/2048, A_B=455/2048, and the early continuation advantages satisfy
X_A=A_A-13/50+K_A(r=1)*(547/1280-13/50)=7141/1638400>0,
X_B=A_B-13/50+K_B(r=1)*(547/1280-13/50)=-5221/1638400<0.
By backward induction,
h_FULL(n)=-4121627/3276800,
h_LR(n)=-32241/25600,
h_FULL-h_LR=5221/3276800>0.

An attaining FULL strategy stops on source B at t=1 and declares P; source A continues, stops at t=2 outside r=1 declaring Q when r<=1 and P when r>1; at central node r=1 it continues to t=3 and declares Q when s<=1 and P when s>1. Its exact observation vector is W=(10571/131072,12273/16384,843/512,843/512), satisfying n·W=h_FULL(n). Since ||n||_1=113/50, the distance from W to the seedless-LR four-dimensional convex hull in infinity norm is at least 5221/7405568.

This proves that equality of the complete time-only projected convex hulls does not imply complete O4 convex-hull equality, even when all terminal kernels are source-independent. It filters this concrete five-node model out of the equal-hull R5 candidate pool; it does not close the broader R5 objective.

## Verification, scope, provenance, continuation

An actually executed Python 3 standard-library Fraction script verified all first/late Q and P probability normalizations, shared roots, classification gains, signs, explicit witness, four-dimensional supports, distance lower bound, and exhaustively evaluated 3*3^5*2^5=23,328 deterministic seedless-LR strategies. No floating-point tolerance was used; complete support over real randomization follows from finite multilinear policy optimization/backward induction. The script run ended PASS_EXACT_R5_TIME_FACE_CLASSIFICATION_SEPARATION. The analytic lemmas above are independent of the one finite enumeration.

The source/branch carrier is retained, with any loss of provenance through LR projection checked relative to downstream declaration and stopping. P000, ACTIVE worldview and frozen input pins remain unchanged. GitHub publication is author provenance only; it grants no mathematical admission, Result/Review, or task CLAIM. Contextual literature only: Blackwell, *Equivalent Comparisons of Experiments* (1953), DOI 10.1214/aoms/1177729032; Laroche & Tachet des Combes (2023), PMLR 202 https://proceedings.mlr.press/v202/laroche23a.html; these do not establish the novel lemma.

Next: partition classification and late-gate sign cones exactly, derive constraints on first K differences compatible with zero Jensen gap for ALL four-dimensional normals, then search a strictly positive nonzero K direction satisfying them. For a certified hull-equality candidate, test actual real-behavior image nonmembership semialgebraically. If a bounded finite family admits no candidate, record its exact scoped separation certificate and explore alternative architectures. Mother objective remains open.
