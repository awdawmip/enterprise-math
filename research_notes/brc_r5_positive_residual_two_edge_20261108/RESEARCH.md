# R5: Universal positive-residual two-edge Blackwell lift (all real flows)

Date: 2026-11-08 Asia/Shanghai. Author-side exact proof and Fraction regression; unreviewed and not admitted.
Frozen scientific pins: global a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e.
Direct predecessor: a5c2575f344fdf3043f26198293704daa9c1be1f, research_notes/brc_r5_residual_slack_blackwell_shift_20261107/.
This concerns only the frozen four-stage, seven-likelihood-key P/Q-BRC experiment and the four observations (e_P,e_Q,T_P,T_Q); it does not alter native X6 premises.

## Model

Let r=(1/10,1/2,3/4,1,5/4,3/2,19/10). A legal real FULL_HIST flow x=(g,a,b,u,v,w,z) obeys
0<=a,b<=g<=1; 0<=u<=13a/40+b/80; 0<=w<=3a/40+21b/80;
0<=z<=a/10; 0<=v-z<=9b/40.
The seven exact Q stopping masses M_i and both stopping times are reproduced from the predecessor in VERIFY.py.
For every declaration d in [0,1]^7: e_Q=sum_i M_i(x)d_i and 1-e_P=sum_i r_i M_i(x)d_i.
The history residual is R(x)=9bz-4a(v-z)=(4a+9b)z-4av.
The seedless LR constraint is R=0.

## Theorem: positive residual always lifts by two edges

For EVERY legal real x with R(x)>=0, there is a legal seedless LR y with identical T_P,T_Q and ONE stochastic seven-key Blackwell kernel K independent of d such that for EVERY d in [0,1]^7,
(e_P,e_Q,T_P,T_Q)(y,Kd)=(e_P,e_Q,T_P,T_Q)(x,d).

For a=0 or b=0, legality forces R=0; set y=x and K=I.
For a,b>0 set
z0=4av/(4a+9b), y=(g,a,b,u,v,w,z0), Delta=z-z0=R/(4a+9b)>=0,
h=(247/1620)Delta.
Legality gives 0<=v<=a/10+9b/40=(4a+9b)/40. Consequently
0<=z0<=a/10 and 0<=v-z0=9bv/(4a+9b)<=9b/40.
Thus y is legal and R(y)=0. The stop times depend only on (g,a,b,u,v,w), so are unchanged.

At fixed (g,a,b,u,v,w), inspect the exact seven predecessor masses.
The coefficient of z in M_0 and M_6 is 47/180-67/162=-247/1620;
in M_3 it is 43/90-14/81=247/810; and in the other four masses it is zero.
Thus M(y)-M(x)=h(1,0,0,-2,0,0,1).

Construct nonnegative Q with source rows indexed by y and destination columns indexed by x:
Q[i,i]=M_i(x) for i=0,6; Q[i,i]=M_i(y) for i=1,2,3,4,5;
Q[0,3]=Q[6,3]=h; all remaining entries zero.
Rows sum to M(y), columns to M(x). All likelihood-weighted columns are calibrated:
the only nontrivial column is j=3, where r_0 h+r_6 h=(1/10+19/10)h=2r_3h.
For each row of positive mass define K[i,j]=Q[i,j]/M_i(y); use any stochastic row if M_i(y)=0.
Then Kd belongs to [0,1]^7 and reproduces both Q and P error expressions for every real declaration.
This proves the theorem for all real parameters, including boundary points.

## Sharp sign criterion for the fixed-six-coordinate candidate

When a,b>0, y(z0) is the UNIQUE seedless flow with fixed (g,a,b,u,v,w).
It Blackwell-dominates the FULL_HIST source x for all declarations if and only if R(x)>=0.
Sufficiency is the theorem. If R(x)<0, z0>z and M_0(y)<M_0(x).
Since r_0=1/10 is strictly the smallest likelihood key, calibration plus nonnegative Q implies
all incoming mass to column 0 originates from source row 0, hence M_0(y)>=M_0(x) is necessary.
Contradiction. This criterion governs only the fixed-six-coordinate target;
other seedless targets remain available for negative residuals.

## Exact new extreme-side-flow witness

x=(1,3/4,1/2,1/4,3/40,3/16,3/40), R(x)=27/80.
Both u=13a/40+b/80=1/4 and w=3a/40+21b/80=3/16 are maximal.
y=(1,3/4,1/2,1/4,3/40,3/16,3/100) is seedless and legal.
Both stopping times equal (123/40,251/80).
The ONLY off-diagonal transport masses are Q[0,3]=Q[6,3]=247/36000.
This positive-residual g=1 instance is outside the predecessor's negative-residual shift domain.

## Verification and reusable BRC interface

VERIFY.py uses Python standard-library Fraction for coefficient identities;
800 exact rational legal positive-residual cases in a fixed 5-by-4^4 parameter family;
normalization, both likelihood moments, legality, stop times, seedless equality,
all 7 row/column/weighted-column identities, and three declarations per case;
the exact extreme-side-flow witness; and an exact negative-residual fixed-slice obstruction.
EXACT_OUTPUT.txt records actual local execution. The universal theorem is proved
by the displayed exact algebra, not inferred from 800 tests.

BRC reuse: positive seven-key branch-mass carrier, residual R, and calibrated mass transport (REUSE_APPLIED).
Observed future operation: stochastic terminal declarations and the four stated observers;
other hidden-history operations are outside the declared horizon.
Next: for low-slack negative residual outside the earlier g-shift,
vary at least one of g,a,b,u,v,w and find a calibrated seedless target or an exact infeasibility witness.
GitHub evidence publication here is author-side; active native Owner/CLAIM, independent review
and Result admission remain separate.
