# R5: exact family-optimal four-dimensional seedless-LR cube
Date: 2026-11-06 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Frozen input and statement

The mother problem compares actual four-observer FULL_HIST and seedless LR images for a strictly positive finite P/Q likelihood-ratio stopping tree at delta=1/4, with equal convex hulls. This is an auxiliary BRC observer, not a claim about native X6 heartbeat dynamics. Scientific pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568, EM 86149263e38c22292c9def1e0f69092efa1be77e. Continue EM research_notes/brc_r5_sharper_lr_cube_20261106_t1035/RESEARCH.md at ba30a09979a06e9e82f2caf6a7fb4f7b3ce700ca; use the exact stopping-ratio lift from research_notes/brc_r5_scalar_nonlumpability_gate_20261106_t0343/RESEARCH.md at 57f7d654e5dd002567e0b0d333937e6e38f3b4cb.

Let W=(e_P,e_Q,T_P,T_Q), with e_P=P(declare Q), e_Q=Q(declare P). All appearances of each stopped likelihood-ratio key use a single shared declaration probability.

**Theorem A (closed four-cube, all real points).** Let W*=(1/2,1/2,15/8,15/8), h=10395/788344, approximately 0.013185868098190638. Every real W satisfying max_i |W_i-W*_i|<=h is exactly achieved by a valid randomized seedless LR policy, hence by FULL_HIST. Compared with the predecessor radius 11283/1291520, the radius improves by factor 559389600/370620223, about 1.5093337203 (+50.93%).

**Theorem B (sharp within the declared inverse-section family).** Consider the family with u0=u1=u fixed; baseline central X0=X2=x and X1=y fixed; time deviations adjusted only by g=g0+3b-2a and X2=x+2(a-b); declarations fixed at 1/2 except the shared stopped ratio keys 1/10 and 1, whose inverse probabilities are set by the 2x2 linear observation equations. For any center parameters u,x,y,g0 satisfying T_P=T_Q=15/8, the largest uniformly feasible closed four-cube radius in this family is at most h; our section attains equality. This optimality is conditional on this specified family.

## Inverse policy

For target deviations a=T_P-15/8, b=T_Q-15/8, c=e_P-1/2, d=e_Q-1/2, all in [-h,h], set
    u=30800/98543, x=10395/197086=4h,
    y=30933/394172, g0=298375/788344=7/8-u-2x-y;
    g=g0+3b-2a, u0=u1=u,
    X0=x, X1=y, X2=x+2(a-b).

At time 1 the continuation probability is g; at the two time-2 histories it is u/g; at the time-3 ratio keys j=0,1,2 it is X_j/V_j, with
    V=(27u/80,13u/40,27u/80).
The stochastic Q kernels at time 3 are (13/20,1/5,3/20) and (1/40,9/20,21/40), with time-2 ratios 3/4 and 5/4; the time-3 ratios are (1/2,1,3/2). At the time-4 ratio keys (1/10,1,19/10), the first and third row are (509,382,9)/900 and (9,382,509)/900 for either time-2 history, and the central rows are (47/180,43/90,47/180) and (67/162,14/81,67/162), respectively. P kernels are likelihood-ratio weightings of these strictly positive Q kernels.

Let M_r denote the total stopped Q mass over every history and time for ratio r in {1/10,1/2,3/4,1,5/4,3/2,19/10}. For the given flow,
    M_(1/10)=m0+(a-b)/50, m0=233079/3941720,
    M_1=m1+(2+191/225)a-(3+191/225)b,
    m1=2799887/3941720.
Set shared P-declaration probabilities
    t_(1/10)=1/2+10(c+d)/(9*M_(1/10)),
    t_1=1/2-(10c+d)/(9*M_1),
    t_r=1/2 for all other ratio keys.
These are the only two declaration probabilities that vary from the common half-half baseline.

## Proof of Theorem A

The inherited stopping-time formulas are
    T_P=1+g+(3u0+5u1)/8+X0/2+X1+3X2/2,
    T_Q=1+g+(u0+u1)/2+X0+X1+X2.
Direct substitution gives T_P=15/8+a and T_Q=15/8+b.

The exact rational facts x=4h, V2-x=4h, g0-u=5h, 0<y<V1 and g0+5h<1 show 0<=X2<=V2 and u<=g<=1 for every |a|,|b|<=h, including all corners. The remaining continuation masses X0 and X1 are within their capacities. Therefore all stopping probabilities are legal. Positivity, normalization and first likelihood-ratio moments of the inherited rows give nonnegative M_r with sum_r M_r=sum_r r M_r=1.

At the baseline t_r=1/2, the two error coordinates equal (1/2,1/2). Write s=t_(1/10)-1/2, v=t_1-1/2. The exact changes are
    c=-(M_(1/10)/10)s-M_1 v,
    d=M_(1/10)s+M_1 v.
The displayed inverse probabilities solve these equations exactly. Their denominators and limits obey
    M_(1/10)>=m0-h/25=5775/98543>0,
    |s|<=20h/[9(m0-h/25)]=1/2,
    M_1>=m1-(1507/225)h=245177/394172>0,
    |v|<=11h/[9(m1-(1507/225)h)]=12705/490354<1/2.
Thus all seven shared declaration probabilities are in [0,1], proving the entire real closed cube is actually attained. QED.

## Proof of Theorem B: exact necessary upper bound

For any member of the stated affine inverse family realizing all time corners of radius H, let the centered fixed flows be u,x,y and g0=7/8-u-2x-y. Capacity and root constraints necessarily give
    x>=4H,  27u/80-x>=4H,  g0-u>=5H.
Hence u>=(80/27)(x+4H) and
    y<=7/8-(214/27)x-(775/27)H.
The centered stopped ratio-1/10 mass is m0=(259/450)x+(11/30)y. At corner (a,b,c,d)=(-H,H,H,H), that ratio's mass is m0-H/25. The declaration at ratio 1/10 is legal only if
    m0 >= (1009/225)H.
On the other hand, using the preceding upper bound on y, the coefficient of x is strictly negative, so x>=4H gives
    m0 <= (259/450)*4H+(11/30)*(7/8-(214/27)*4H-(775/27)H)
       = 77/240 - (7*91864/32400)H.
Combining these necessary inequalities gives H<=10395/788344. Our explicit parameters attain this exact radius; at the sharp corner t_(1/10)=1. QED.

## Verification, comparison and next question

Standard-library Python Fraction verifier VERIFY.py executes all 625 rational points on the 5^4 grid (including all 16 corners) under the all-real inverse formulas, validates all seven aggregated stopped ratio masses, the strict positive kernel moments, exact errors and times, and the sharp rational bound. Actual stdout is in EXACT_OUTPUT.txt with PASS_EXACT_R5_OPTIMAL_AFFINE_SECTION_CUBE. The analytic inequalities above, not finite sampling, justify the all-real claim.

This proves a larger definite subset of both images; the global R5 mother difference/equality remains open. The next discriminating unit is a rational FULL_HIST-feasible W outside this cube with stopping times strictly inside the known octagon, and a global sign calculation of the single quadratic F over the entire seven-variable polytope K(W). A strict sign proves real LR nonreachability; sign crossing reconstructs a legal LR policy. Formal Source CLAIM, Result, independent review and admission remain to be established.
