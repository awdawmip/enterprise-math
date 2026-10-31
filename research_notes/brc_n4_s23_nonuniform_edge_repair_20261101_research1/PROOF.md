# BRC N4 / S23: rational decoder edge repair and a displaced exact adversary

Date 2026-11-01. Independent author-side research and exact integer check; **UNREVIEWED / NOT_ADMITTED**. Scope: the finite BRC six-source/four-time stopping experiment, not native P000 dynamics.

## Frozen model, quantifiers and the changed label

Six positive latent BRC sources (AU0, AU1, AV, BU0, BU1, BV), with six prepared P/Q rows given by M=M20/20:
M20=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]].

Legal controls are 11 real numbers a_A,a_B,b_U,b_AV,b_BV and one c_x for each latent source, each in [0,1]. For latent x of A/B group g and second-stage information set h, the four-time distribution is
F_x=(a_g,(1-a_g)b_h,(1-a_g)(1-b_h)c_x,(1-a_g)(1-b_h)(1-c_x)).
The U information set is shared between AU and BU. Each prepared row p_i=(M F)_i.

The fixed deterministic k=4 encoder retains the AU/AV/BU/BV group. Given ten fixed four-group row-stochastic decoder kernels D_l, the policy-visible (before outcome) selection loss is
G(theta)=min_l max_i TV(p_i(theta),(M E D_l)_i).

Keep original decoder labels 1–9 from the predecessor:
1=34 24 34 24; 2=34 23 34 34; 3=34 34 34 23;
4=24 24 12 12; 5=12 12 24 34; 6=12 13 23 24;
7=23 34 12 13; 8=24 34 12 14; 9=13 12 13 13.
Each two-digit pair is uniform on those two times, in group order AU, AV, BU, BV.

Replace only label 10 (formerly 12 12 14 12) with this valid nonuniform decoder, whose four time probabilities sum to one in each group:
AU=(1/2,0,1/4,1/4), AV=(1/2,0,1/2,0),
BU=(1/2,0,0,1/2), BV=(1/2,1/2,0,0).
The six decoded prepared rows are, as numerator/160:
(80,0,40,40),(80,0,40,40),(80,0,80,0),
(80,0,0,80),(80,0,0,80),(80,80,0,0).

## Theorem A: one entire continuous counterexample edge is repaired

For any real t∈[0,1] define lawful family H(t):
a_A=t, a_B=1, all three b's zero,
(c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV)=(1,0,1,0,0,0).

The two AU prepared laws are (t,0,(1-t)/2,(1-t)/2) and
(t,0,9(1-t)/20,11(1-t)/20); AV=(t,0,1-t,0);
all B prepared laws are delta_T1.

At t=0, the AU laws each overlap the new AU decoder with exactly 1/2 total probability (both time 3 and time 4 decoder weights 1/4); AV=delta_T3 overlaps its decoder at exactly 1/2. At t=1, all A laws are delta_T1 and overlap their decoders at exactly 1/2. Every B law is always delta_T1 and has overlap 1/2 with its BU or BV decoder. As each prepared row is affine in t and TV to a fixed decoder is convex, the new label-10 loss never exceeds 1/2 for any real t, and the B rows force equality.

Every one of the remaining nine labels also has loss ≥1/2 on this family because a B row is delta_T1 and its B decoding has time-1 probability at most 1/2. Therefore the exact repaired envelope is G*(H(t))=1/2 for ALL real t∈[0,1]. In particular the old t=1/3 fixed-bank 2/3 counterexample no longer applies.

## Theorem B: another lawful edge retains exactly the old 2/3 peak

Take instead J(t): a_A=1, a_B=t, all three b's zero,
(c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV)=(0,0,0,0,1,0).
All A prepared rows are delta_T1. The three B prepared rows are
BU,Q=(t,0,(1-t)/2,(1-t)/2);
BU,P=(t,0,9(1-t)/10,(1-t)/10);
BV=(t,0,0,1-t).

Using the exact identity TV(p,q)=1−sum_s min(p_s,q_s), each label's worst six-row error on J(t) for every real t in [0,1] is:
L1=L2=L3=L4=L7=L8=1,
L5=(9+t)/10,
L6=(1+t)/2,
L9=L10=max(1-t,1/2).

Proof details: labels 1–4 and 7–8 have an A prepared row delta_T1 with a decoder pair excluding T1, hence disjoint support. Label 5's decisive BU,P row has only T4 overlap (1−t)/10 against BU decoder times 2,4, hence loss (9+t)/10; the other rows are no worse. Label 6's decisive BU,Q row overlaps only at T3 with mass (1−t)/2 against BU decoder times 2,3, hence loss (1+t)/2; other rows are no worse. Labels 9/10 have the decisive BV row (t,0,0,1−t) against a BV decoder with T1 mass 1/2 and T4 mass zero, hence loss 1−min(t,1/2); other rows are no worse. These inequalities follow by inserting the displayed rows in the overlap formula. Since L5−L6=(2/5)(1−t)≥0, the exact bank risk is

G*(J(t))=min{(1+t)/2, max(1−t,1/2)}
       =(1+t)/2 for t∈[0,1/3],
        1−t     for t∈[1/3,1/2],
        1/2     for t∈[1/2,1].

The unique maximum is 2/3, attained at t=1/3. There, the ten exact label errors are
(1,1,1,1,14/15,2/3,1,1,2/3,2/3). The t∈{0,1/2,1} scores are all 1/2. Therefore the repaired bank still has global worst-case ≥2/3, although the former H edge is now fully protected.

## Exact finite verification and scope

Executed VERIFY.js using Node.js integer arithmetic. It enumerates every 3^11=177147 lawful ternary policy with each control in {0,1/2,1}; computes all six prepared rows, all ten decoder rows and the min/max risk; exact grid risk is the integer numerator /320. The modified bank has exactly 168353 policies at TV=1/2, 8794 below 1/2, and zero above 1/2, maximum TV=1/2. The predecessor bank's corresponding counts were 169441,7706; therefore the new bank strictly improves at least 1088 finite-grid policies, while retaining the same grid-wide radius bound. Marginal counts alone do not show pointwise nonworsening of every policy.

Additionally the executed program checked the explicit H/J loss formulas on 121 rational t points per edge, including t=1/3. Both full real-continuum theorems are proved by the overlap and convexity arguments above, not inferred from a grid. All integer magnitudes are exactly representable in JavaScript (below 2^53); no floating tolerance, sampling or optimization solver is used.

This proves a constructive *bank-specific* repair and an exact displaced counterexample. The optimized ten-label minimax R_beh(k,10), k=4 or 6, retains its previously bounded interval [1/2,2/3]. S2 information-set transfer, native P000 six-axis Cell/slice and independent time correspondence, and independent mathematical review remain separate obligations. Six latent statistical sources are not P000's six native spatial axes.