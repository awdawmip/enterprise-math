# Stage256 — Exact asymmetric support beyond the N=12 TV region

Date 2026-10-29. Status: AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. External ternary IID sequential decision model, not native P000-X6 dynamics. Parent: Stage255 proof commit 6c399579c9e744aa9be5eb519aa059d2ffbd1618; previous support Stage254 a538e30f5a6e5c2d83bdf88f56a2837aeea17842 and prior global TV result Stage247 c2dbf682c021327dee18f57e2c6864feb6a09a39.

## 1. Model and exact target

Observation laws P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), alphabet {0,1,2}, maximum sample count N=12. Every fully ordered-history policy, including randomized stopping and randomized terminal declarations, is admissible. Let eP=Pr_P(declare Q), eQ=Pr_Q(declare P), tP=E_P(tau), tQ=E_Q(tau). For caps eP<=a, eQ<=b, V12(a,b) minimizes max(tP,tQ).

For the exact outside-TV cap pair

    a=6788660051/34828517376,
    b=572868317/967458816,

we prove the GLOBAL optimum

    V12(a,b)=3625356966401597/645573577789440
            ≈5.615714600364332.

The pair satisfies a+b<1, a+b> C=(3+(5/6)^12)/4=6774487633/8707129344, but 2a+b-1=-313968931/17414258688<0, so it lies strictly outside the maximal affine TV-support region established in Stage247/Stage255. Its exact positive gap above the TV lower bound is

    V12-24(1-a-b)=5868351353787331/11620324400209920>0.

## 2. Globally valid exact Bellman dual

Take time multipliers thetaP=0, thetaQ=1 and nonnegative error multipliers

    Kp=644972544/8007455,
    Kq=418575732/8007455.

At ordered history h with counts s=(i,j,k), the Q-to-P likelihood ratio is L(s)=(2/3)^i*2^j. Define H(s) backwards by

    H(s) = min { Kq*L(s)                 [declare P],
                 Kp                      [declare Q],
                 L(s)+sum_z P_z*H(s+e_z) [continue, if |s|<12] }.

At depth 12, continuation is unavailable. This is the P-normalized conditional cost of tQ+Kp*eP+Kq*eQ. At arbitrary ordered histories the future is still IID and the ratio depends only on the counts, so backward induction at histories proves a lower bound for EVERY history-dependent policy, not just those whose actions use counts.

Two load-bearing exact action equalities are

    At A=(0,0,8), P-stop equals continuation:
        -1 - Kp/24 + Kq/12 = 0;

    At B=(0,1,2), Q-stop equals continuation:
        -4648223/1679616 + (5429473/53747712)*Kp
         - (2070241/20155392)*Kq = 0.

They solve to the rational Kp,Kq above. The complete Python Fraction program STAGE256_ASYMMETRIC_EXACT.py independently constructs the backwards recurrence and checks all 455 count states (sum(s)<=12), with precisely 11 two-action ties: (0,0,k) for k=2,3,...,11 (P/C), plus (0,1,2) (Q/C). It establishes exactly 808 strictly positive alternative-action gaps, and root value

    H(0,0,0)=30134718329/576536760.

Every full-history randomized policy thus satisfies

    max(tP,tQ)>=tQ>=H(0,0,0)-Kp*eP-Kq*eQ
                  >=H(0,0,0)-Kp*a-Kq*b.

The last inequality follows from Kp,Kq>0, preserving separate error caps.

## 3. Constructing an attaining two-coin policy

Take two arbitrary legal coins x,y in [0,1]. Along any all-symbol-2 prefix continue, except at A=(0,0,8), where continue with probability x and otherwise declare P. Along all 12 twos declare P. At B=(0,1,2), continue with probability y and otherwise declare Q. Elsewhere choose the unique Bellman-minimizing action. All actual actions are exact dual minimizers.

A and B are incomparable under prefix ancestry: A has depth 8 and contains only symbol-2, whereas B has depth 3 and contains symbol-1. Thus the four-observer vector is affine without an x*y interaction term:

    (eP,eQ,tP,tQ)=W+x*U+y*D,

    W=(2798826503/15479341056,
       3640889785/5804752896,
       3085480967/644972544,
       2378853959/483729408),

    U=(262109375/8707129344,
       -262109375/4353564672,
       262109375/362797056,
       262109375/362797056),

    D=(-135736825/15479341056,
       51756025/5804752896,
       88211975/644972544,
       116205575/483729408).

The exact signed determinant of the two error-plane directions is

    determinant=U_eP*D_eQ-U_eQ*D_eP
               =-52470725634765625/202170937101722320896 !=0.

Solving the two error constraints eP=a and eQ=b yields the exact lawful coins

    x=2942214371765387/4197658050781250,
    y=478956919/600559125,

with 0<x,y<1. The corresponding EXACT four-observer vector is

    eP=6788660051/34828517376,
    eQ=572868317/967458816,
    tP=62742333308848141/11620324400209920,
    tQ=3625356966401597/645573577789440.

Consequently eP=a, eQ=b and tQ-tP=313968931/1451188224>0, so the objective max(tP,tQ) equals tQ. Since every reached action minimizes Bellman cost, the exact primal-dual identity holds:

    tQ+Kp*eP+Kq*eQ=H(0,0,0).

Together with the global lower bound, this is a complete rational optimality certificate for the specified cap pair.

## 4. New all-real, positive-area support region

Let

    R256 = { (W_eP,W_eQ) + x*(U_eP,U_eQ)+y*(D_eP,D_eQ):
             0<=x<=1, 0<=y<=1 }.

It is a nonzero-area rational parallelogram of area

    52470725634765625/202170937101722320896.

For EVERY real cap pair (a',b') in R256 (irrational coins allowed), invert the nonsingular error-coordinate map to recover legal x,y. Four-observer affine equality is an exact symbolic identity for these policy kernels, not a finite empirical interpolation. Time Q dominates throughout this coin square, because

    tQ-tP = 258972935/1934917632
            + y*200186375/1934917632 > 0.

The same Bellman global lower bound and the attaining policy prove

    V12(a',b') =
       30134718329/576536760
       -(644972544/8007455)*a'
       -(418575732/8007455)*b'

for ALL real (a',b') in R256. Since the maximum of 2a'+b' over R256 is 1-258972935/23219011584<1, the entire parallelogram lies strictly OUTSIDE the Stage255 sharp-TV region. The error multipliers Kp and Kq are unequal; this is a distinct asymmetric support.

This is a rigorously certified SUBREGION. There are 11 Bellman tie states, not only the two chosen randomization sites. Other optimal tie policies may enlarge the full contact region. We do NOT claim the parallelogram is maximal or that this support face is directly adjacent to TV.

## 5. Independent ordered-history evidence and scope

The companion executed script checks 455 exact Bellman states, the complete tie/gap list, four deterministic corners of the (x,y) square and the target rational coins. A separate UNMERGED ordered-history DFS carries nonnegative rational P and Q source probabilities, terminal depth and classification for each full path, with both terminal masses normalized to precisely 1. DFS and rational memoized suffix dynamic programming agree on all four observers in all five cases: total 869 ordered-history nodes and 585 terminal decision branches. Actual stdout is in EXACT_RUN_STAGE256.txt and ends with STAGE256_ASYMMETRIC_EXACT_PASS.

This realizes BRC-compatible positive source-label preservation for the four declared finite-IID observers; it does not claim to run a native BRC heartbeat implementation, nor to preserve arbitrary future X6 relations. GLOBAL_KNOWLEDGE_V1 scientific source main@243041d5d4e2c6bc8b78be63668669b0f1d26dce, Enterprise Math control main@bc0a149e03ba2632a8ba79042361b50ad3ab471a, original P000 Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc match the ACTIVE six-native-X6 and separate time requirements. Native status v0.6.11: research_authority_granted=false, CODE_REVIEW_REQUIRED; active Owner read returned CONTROL_QUOTA. Research output remains portable author evidence without native CLAIM, Result, independent review or P000-to-IID correspondence.

## Next Stage257

Determine the maximal error contact polygon of this support by examining all 11 Bellman ties (at most 2^11=2048 deterministic choices, with exact P/Q source mass), including ancestor reachability effects. Check whether Q-time dominance holds everywhere, find exact vertices/edges, and identify genuine adjacency (or intervening support) with the Stage255 TV contact set. Preserve all four observers and do not promote unreviewed author evidence.
