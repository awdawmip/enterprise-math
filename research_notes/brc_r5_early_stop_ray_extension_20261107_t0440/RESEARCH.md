# R5 — Exact seedless-LR ray extension beyond the g=u0=1 ceiling

Date: 2026-11-07 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
Frozen science unchanged: GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e.
Immediate predecessor: 3fd9cc9d13429a00aeee6aa06a1508e57fa5f873, research_notes/brc_r5_target_dependent_v_single_corner_20261107_t0345/RESEARCH.md. Current normative rules were independently read from canonical main.

## Exact theorem

Fix the strictly positive four-stage P/Q likelihood-ratio tree at delta=1/4. Its four observables are W=(eP,eQ,TP,TQ), where eP=P(declare Q), eQ=Q(declare P), and T denotes expected stopping time. Write W*=(161801/180000,6499/18000,267/80,137/40).

The predecessor established an all-real sharp restriction: when g=u0=1, even with target-dependent u1 and arbitrary pooled LR continuation and declaration probabilities, the single ray W*+h(1,1,1,-1) is attainable iff 0<=h<=H=3543/3009580.

**New theorem.** Permitting general early continuation 0<=u0,u1<=g<=1, there are legitimate seedless-LR strategies realizing W*+h(1,1,1,-1) for EVERY real h in [0,9/2500]. In particular h0=9/2500 exceeds H, with h0/H=451437/147625>3 and h0-H=227859/94049375>0. This constructs an exact counterexample to extending the preceding restricted-class ray ceiling to the unrestricted class. The asserted attained set is a one-dimensional ray segment; no 4D cube or FULL_HIST-vs-LR separation is inferred.

## Frozen kernels and rational endpoint construction

At time 2 the LR keys are (3/4,5/4), each with Q mass 1/2. At time 3, LR keys (1/2,1,3/2) have Q conditional rows
    q3[0]=(13/20,1/5,3/20)
    q3[1]=(1/40,9/20,21/40).
At time 4, keys (1/10,1,19/10) have conditional rows for (i,j)=(0,0)/(1,0); (0,1); (1,1); (0,2)/(1,2):
    (509/900,382/900,9/900)
    (47/180,43/90,47/180)
    (67/162,14/81,67/162)
    (9/900,382/900,509/900).
Every row is normalized and has its parent likelihood ratio as first moment (verified with exact Fraction).

Keep the SAME early continuation for the entire ray segment:
    g=u0=u1=77/80.
Hence time-1 stopping Q mass is 3/80 at LR=1, conditional time-2 continuation is 1, and time-3 pooled Q capacities are V=(2079/6400,1001/3200,2079/6400). For each pooled LR key j, use the SHARED continuation probability z_j=X_j/V_j, independent of history i. All remaining paths stop at time 4. For every stopped LR key r, E_r is the stopped Q mass declared P; use shared declaration probability E_r/M_r where M_r>0 (zero otherwise).

An exact CENTER endpoint realizing W* has
    X(0)=(3/16,3/10,1/80)
    E_{1/10}=1297/6000; E_{1/2}=879/6400
    E_1=563/144000; E_{19/10}=349/96000
and all other E_r=0.

An exact RAY endpoint at h0=9/2500 has
    X(1)=(1723/10000,781/2500,117/10000)
    E_{1/10}=458111/2160000; E_{1/2}=24407/160000
    E_1=221/10800000; E_{3/2}=7/2400000
and all other E_r=0.

At that endpoint the complete stopped Q LR histogram M_r in order (1/10,1/2,3/4,1,5/4,3/2,19/10) equals
    (95449/450000,24407/160000,0,717541/3600000,0,50103/160000,18433/150000).

For both endpoints, exact calculations give 0<=X_j<=V_j and 0<=E_r<=M_r, sum M_r=1, sum r M_r=1. Both error observers are given by eQ=sum E_r and eP=1-sum r E_r. The exact time identities are
    TQ=1+g+(u0+u1)/2+X0+X1+X2
    TP=1+g+(3u0+5u1)/8+X0/2+X1+3X2/2.
The ray endpoint observation is EXACTLY
    W(1)=(162449/180000,32819/90000,33411/10000,17107/5000)
        = W*+(9/2500)*(1,1,1,-1).

## All-real segment proof

Fix g=u0=u1=77/80. For an arbitrary REAL s in [0,1], set X(s)=(1-s)X(0)+s X(1), and E(s)=(1-s)E(0)+s E(1). The pooled Q capacities V_j remain unchanged, and z_j(s)=X_j(s)/V_j lies in [0,1]. At fixed early continuation the complete stopped LR mass histogram M_r is affine in X, including the central terminal kernel's pooled contribution, because its history mixture ratio u1/u0 remains fixed. Therefore M_r(s)=(1-s)M_r(0)+s M_r(1); the inequalities 0<=E_r(s)<=M_r(s) follow from endpoint legality. These flows give a valid seedless-LR policy for EVERY real s, with shared declarations E_r(s)/M_r(s).

All four observation formulas are affine in (X,E) at fixed early continuation. Thus W(s)=(1-s)W*+s W(1)=W*+s*(9/2500)*(1,1,1,-1). This proves the whole real ray segment, including irrational h and both endpoints.

## Verification, meaning, next unit

Adjacent VERIFY.py is a standalone Python fractions.Fraction checker actually executed for this research step. It checks all kernel conditional LR moments, both endpoint probability and declaration bounds, seven stopped masses, both times, both errors, h0>H and five intermediate rational interpolation points. Its observed stdout is in EXACT_OUTPUT.txt, ending PASS_EXACT_R5_UNRESTRICTED_EARLY_CONTINUATION_RAY_BREACH. All-real coverage follows from the preceding affine argument, not the finite checks.

BRC carrier is the complete seven-bin stopped likelihood-ratio Q mass histogram and declaration mass flows, with central history kernel retained until valid pooling; the four-observer W is a coarsening. This result locates the previous sharp obstruction in the imposed early-stop constraint, not an unrestricted LR impossibility.

Next: optimize the unrestricted seedless-LR ray supremum with variable g,u0,u1; try a higher exact Fraction witness or prove an all-real global upper bound. The original mother R5 question FULL_HIST vs seedless LR for the unrestricted FOUR observations remains open and is studied separately using the full K(W) plus quadratic F=(A+B)J-X1*(alpha*A+beta*B) feasibility test.

Actual control attempt: GitHub authenticated awdawmip with push/admin; native Enterprise Math em_status, em_control_tasks and em_session_start returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Active owner and formal CLAIM remain unconfirmed; no native Result/Review claim was made.
