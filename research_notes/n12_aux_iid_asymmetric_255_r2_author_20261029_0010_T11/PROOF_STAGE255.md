# Stage255 — Exact TV-face transition at the Stage254 equal-time boundary

**2026-10-29. AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED.** External ternary IID sequential stopping/classification, not native P000-X6. Exact parents: Stage254 proof commit a538e30f5a6e5c2d83bdf88f56a2837aeea17842 and Stage247 global sharpness theorem c2dbf682c021327dee18f57e2c6864feb6a09a39. This scientific increment applies the previously proved Stage247 TV theorem to the previously open Stage254 exterior point, supplies a new matched Bellman/ordered-history certificate, and identifies their precise adjacent support faces; it does not claim that the general Stage247 theorem was discovered anew.

## Model and new exact result

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6) on alphabet {0,1,2}. A randomized policy based on arbitrary full ordered histories may stop, declare P or Q, after at most N=12 observations. Define eP=Pr_P(declare Q), eQ=Pr_Q(declare P), tP=E_P tau, tQ=E_Q tau and V12(a,b)=minimum max(tP,tQ) with eP<=a,eQ<=b, or +infinity if infeasible.

The Stage254 unsolved feasible exterior caps are:

    a = 15492478957579/55725627801600
    b = 580533802651/1160950579200.

Their **exact global optimum** is

    V12(a,b) = 12367526316773/2321901158400
             = 24(1-a-b)
             ≈ 5.326465457855814.

The globally valid rational dual uses time weights thetaP=thetaQ=1/2 and error multipliers lambdaP=lambdaQ=24, with root dual value H=24. Both error caps are tight and tP=tQ in the exact primal strategy constructed below. This **already-proved sequential-TV support** is the next face past Stage254's equal-time boundary, rather than a new asymmetric-multiplier support.

## Exact dual and full-history proof

For any ordered history h with counts s=(i,j,k), its positive Q/P likelihood ratio equals L(s)=(2/3)^i 2^j. Every conditional future distribution remains IID. The P-normalized Bellman action costs for the stated time/error dual are

    declare P : 24 L(s)
    declare Q : 24
    continue  : (1+L(s))/2 + sum_{z=0}^2 P_z H(s+e_z), if |s|<12.

At depth 12 continuation is unavailable. Backward induction yields the **exact value at every state**

    H(s)=24 min(1,L(s)).

Indeed, if the child values satisfy the formula, the continuation cost minus 24 min(1,L), for L>0, is exactly

    L<=1/2       : (1+L)/2
    1/2<=L<=1   : 3(1-L)/2
    1<=L<=3/2   : 5(L-1)/2
    L>=3/2      : (1+L)/2.

These four scalar expressions are nonnegative, and zero only at L=1. Thus the lower-cost terminal action is strictly optimal whenever L≠1. Unique factorization gives L(s)=1 iff i=j=0 for nonnegative count states, so Bellman ties are exactly the all-symbol-2 prefixes: before depth12 P/Q/continue all tie, and at depth12 P/Q tie. This induction holds at each **ordered history**; no assumption that arbitrary policies were count-only is made. Consequently every full-history randomized policy satisfies

    (tP+tQ)/2 + 24(eP+eQ) >= H(0,0,0)=24
    max(tP,tQ) >= 24(1-eP-eQ) >= 24(1-a-b).

An executed Python Fraction checker independently confirms all 455 Bellman states, 13 exact tie states, 794 strictly positive alternative-action gaps, and the exact root value. The general proof comes from the induction, not numerical fitting.

## Exact primal witness

Put r=(5/6)^12 and smax=1-r. For the stated caps let

    s = 4(1-a-b) = 12367526316773/13931406950400
    z = 2a+b-1 = 1562476320403/27862813900800
    w = s/smax = 12367526316773/12368906950400
    q = z/(1-s) = 1562476320403/3127761267254.

All four numbers lie in [0,1], and 0<=z<=1-s. At time zero activate observation with probability w. Otherwise stop immediately, guessing Q with probability q and P otherwise. If activated, continue while every observation is 2; on the first 0 declare P, on the first 1 declare Q. If twelve 2s occur, stop and guess Q with probability q, P otherwise.

Under both P and Q the chance of the first non-2 before the horizon on an activated trajectory is smax, and the hazard per active sample is 1/6. The unconditional signal probability is s, and unconditional Q decision probability on no-signal branches is z. Exact four-observer summation gives

    eP=s/4+z=a;
    eQ=1-s/2-z=b;
    tP=tQ=6s=12367526316773/2321901158400.

Both caps are saturated and max time equals the Bellman bound: exact primal/dual equality proves the claimed global optimum, including all unrestricted ordered-history randomized competitors. A separate unmerged ordered-history DFS carries both P and Q positive Fraction branch masses, verifies each total terminal mass is 1, and reproduces all four observers at 37 nodes and 28 decision branches.

Exact positive margins placing the target strictly inside the new TV contact region are

    a+b-[3+r]/4 = 460211209/18575209267200 > 0
    2a+b-1        = 1562476320403/27862813900800 > 0
    2a+3b-2       = 1565284946851/27862813900800 > 0.

## Maximal all-real TV-affine contact trapezoid

Let C=(3+r)/4=6774487633/8707129344 and

    R_TV = { (a,b) in [0,1]^2 : C<=a+b<=1, 2a+b>=1, 2a+3b>=2 }.

**For every real (a,b) in R_TV**, the policy above with s=4(1-a-b), z=2a+b-1, w=s/(1-r), q=z/(1-s) is legitimate, including irrational probabilities. Its four observers give V12(a,b)=24(1-a-b).

Conversely suppose a+b<1 and a policy attains that affine lower bound. Every inequality in the dual chain must be tight: both caps saturate, tP=tQ, and every positive-mass action must attain the exact Bellman minimum. Since the only ties occur at all-2 histories, every such policy stops at a first 0 (declare P) or first 1 (declare Q), and may stop and guess arbitrarily along the all-2 paths. Write s for the chance of observing a first non-2 before stopping and z for the probability of no-signal stop declaring Q. Necessarily 0<=s<=1-r and 0<=z<=1-s, and the exact observer identities are eP=s/4+z, eQ=1-s/2-z, tP=tQ=6s. Setting eP=a,eQ=b recovers the three inequalities defining R_TV. Thus no outside pair with a+b<1 can attain this affine support. For a+b>1 its raw value is negative, so equality with nonnegative V is impossible; at a+b=1 a time-zero decision achieves equality. R_TV is therefore the **maximal affine-contact region** in the entire cap square. The corresponding full sharpness theorem already appeared in Stage247; this derivation specializes it to the present N=12 support transition.

The four exact vertices of R_TV are (0,1), (1,0), ((1-r)/4,(1+r)/2), and ((1+3r)/4,(1-r)/2). The lower edge at a+b=C is exactly Stage254's x254=0 edge as **full four-observer vectors**, not merely a drawing: Stage254's endpoint w=(969734737/2902376448,1932641711/4353564672), its direction v=(-244140625/2176782336,+244140625/2176782336), and the two TV lower-edge vertices agree componentwise in errors; both constructions also have tP=tQ=24(1-C).

Stage254 has K254=1310563224/20009183>24 and H254=204301839860512073/3629636342682624. Exactly

    H254-K254*C = 24-24*C.

Throughout Stage254 R254, the error sum equals C - [460211209/185752092672] x254, hence is less than C in its interior. R_TV instead has error sum at least C. The two nonzero-area contact regions intersect **exactly along their shared full edge**, with disjoint interiors. At the Stage255 target the TV support beats the Stage254 support by the positive exact margin 397872607/386983526400. This explains the non-smooth transition from total-error slope -K254 to -24 at the time-equality boundary.

## Computation, observer type, authority

Complete runnable source: STAGE255_EXACT_TV_FACE.py (Python standard-library Fraction, lru_cache); actual stdout: EXACT_RUN_STAGE255.txt. The program checks all 455 Bellman states, tie/gap classification, target strategy, each of four trapezoid vertices, independent ordered P/Q mass propagation and exact Stage254 edge identities. Actual execution returned STAGE255_EXACT_TV_FACE_PASS. Finite machine checks verify those rational inputs; the all-real assertion rests on the displayed Bellman proof and elementary convex region argument.

The only BRC interface applied is finite-IID positive-rational branch mass and source/provenance preservation for the stated four observers; no native heartbeat-BRC executable was run. A likelihood-ratio/count reduction is justified only for these future IID operations through N=12, not for arbitrary native X6 events. P000 and the ACTIVE six-dimensional space plus separate time and three-dimensional-slice worldview are unaltered.

Frozen scientific source read: GLOBAL_KNOWLEDGE_V1 main@243041d5d4e2c6bc8b78be63668669b0f1d26dce, Enterprise Math main@bc0a149e03ba2632a8ba79042361b50ad3ab471a, original P000 Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc (matching global startup projection). Native em_status v0.6.11 reported research_authority_granted=false, current CODE_REVIEW_REQUIRED; owner query em_control_tasks returned CONTROL_QUOTA. This is portable AUTHOR_EXACT/UNREVIEWED/NOT_ADMITTED material, neither a Source CLAIM/Result nor an independent Driver review, and it establishes no transfer to native X6 dynamics.
