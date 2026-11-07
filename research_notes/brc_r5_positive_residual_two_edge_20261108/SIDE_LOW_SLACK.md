# R5: exact low-slack negative-residual witness outside the known convex join

Date 2026-11-08, frozen P/Q-BRC scientific pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568, EM 86149263e38c22292c9def1e0f69092efa1be77e.
This is a second independent author-side result in the same four-stage seven-key model. It answers the explicit first open unit in NEXT_UNIT.md (as first published) for one concrete negative-residual source.

## Theorem (one point and a continuous segment)

Take the exact legal FULL_HIST source

x=(1,1,1/2,0,9/80,0,0),  R(x)=-9/20,  (T_P,T_Q)=(14/5,229/80).

The old six-edge negative-residual g-shift requires delta=-R/(9b)=1/10, whereas g-max(a,b)=0. The source also lies OUTSIDE the previously proved conv(C union F union H_slack), as shown below.

The following legal seedless LR target matches both stopping times:

y=(39/40,19/20,9/20,0,3/16,0,57/628),  R(y)=0.

There exists ONE exact nonnegative Q-mass Blackwell transport from y to x for EVERY real seven-key declaration d in [0,1]^7. A rational 7x7 certificate is supplied below. Therefore the four observations (e_P,e_Q,T_P,T_Q) of every source declaration are reproduced by one transformed seedless declaration.

More strongly, for EVERY real 0<=t<=1, the legal flow x_t=(1-t)x+t*y has the same two stop times as y and is dominated by the SAME seedless flow y via
Q_t=(1-t)Q+t*diag(M(y)).
The row sums stay M(y), columns become M(x_t) and P-weighted columns become r_j M_j(x_t), by affine linearity of M. Hence the entire real segment has exact four-observer Blackwell lifts.

Along that segment,
R(x_t)=-9(t-1)(307t-3140)/62800 <0 for 0<=t<1,
with R(x_1)=0. Thus this gives a genuine continuous new negative-residual family, with an explicit rational kernel and algebraic interpolation.

## Exact seven-by-seven transport

Rows are y's likelihood keys r=(1/10,1/2,3/4,1,5/4,3/2,19/10). Columns are x's same keys.
All entries are rational; zero entries are shown as 0:

Q0=[67/1440, 27113/4044320, 0, 28949/5199840, 0, 971/197820, 0]
Q1=[0, 503/1600, 0, 0, 0, 0, 0]
Q2=[0, 43271/4333200, 0, 0, 5447/2166600, 0, 0]
Q3=[0, 0, 0, 35357/376800, 0, 0, 0]
Q4=[0, 0, 0, 28949/1444400, 175103/722200, 0, 0]
Q5=[0, 22459/121329600, 0, 0, 5447/1083300, 32383/175840, 0]
Q6=[0, 0, 0, 0, 0, 971/56520, 67/1440]

Source Q masses:
M(x)=(67/1440,53/160,0,43/360,1/4,33/160,67/1440).
Seedless Q masses:
M(y)=(4801/75360,503/1600,1/80,35357/376800,21/80,303/1600,4801/75360).

The exact checker VERIFY_SIDE.py proves via Fraction arithmetic:
Q>=0; sum_j Q[i,j]=M_i(y); sum_i Q[i,j]=M_j(x);
sum_i r_i Q[i,j]=r_j M_j(x) for all rows/columns; both measures have normalized Q mass and unit P likelihood moment; both times coincide.
Use K[i,j]=Q[i,j]/M_i(y) for each nonzero-mass row to obtain the stochastic declaration map. All M_i(y)>0 in this example. The interpolation gives the full real segment without sampling any irrational t.

## Strictly beyond the former convex join

The previous faces are C (a=b), F (z=a/10), and H_slack (v-z=9b/40 and g+z>=max(a,b)+a/10). The source x has a=g=1 and z=0. In ANY convex decomposition into legal flows, 0<=a<=g<=1 forces every positively weighted component to have a=g=1; nonnegative z forces every such component to have z=0. Such a component cannot belong to F (there a=0), cannot belong to H_slack (it would require 1>=1+1/10), and if it belongs to C it has b=1. Every mixture would then have b=1, contradicting b(x)=1/2. This proves x is outside conv(C union F union H_slack), not merely outside a particular shift formula.

## Verification and remaining question

VERIFY_SIDE.py is the actually executed independent standard-library Fraction checker; EXACT_SIDE_OUTPUT.txt is captured stdout. The proof is the rational calibrated kernel plus affine interpolation, so it covers all real t and all declarations.
Remaining mother question: full pointwise equality between ALL FULL_HIST four-observer values and seedless LR values. Next seek a second low-slack source with u,w>0 and a!=b outside all proved regions; try to construct a rational kernel or a precise infeasibility certificate. No formal Source CLAIM or independent review is asserted.
