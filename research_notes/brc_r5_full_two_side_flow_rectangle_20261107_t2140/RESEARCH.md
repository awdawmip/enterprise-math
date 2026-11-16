# R5: complete two-side-flow Blackwell rectangle (exact, all real)

Date: 2026-11-07 Asia/Shanghai. Status: author-proved, exact Fraction checker executed, independent review and formal Source admission pending.
Frozen scientific inputs unchanged: GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e.
Predecessor: research_notes/brc_r5_symmetric_high_v_blackwell_slab_20261107_t2042/ at 8231237c0863b6fb9d4c394f753e3f6480dc156f.

## Statement

In the frozen four-stage P/Q-BRC observer let the seven likelihood ratios be
r=(1/10,1/2,3/4,1,5/4,3/2,19/10). Let M(x) be the seven Q stopping masses.
Given real stopping declaration d in [0,1]^7, define e_Q=sum M_j(x)d_j
and 1-e_P=sum r_j M_j(x)d_j, with the two frozen stopping-time observers T_P,T_Q.

THEOREM. For every real (u,w) with 0<=u,w<=27/80 and every real d in [0,1]^7,
the legal FULL_HIST source
  x=(g,a,b,u,v,w,z)=(1,1,1,u,9/40,w,0)
has one legal seedless LR target y(u,w), independent of d, and one row-stochastic
seven-by-seven declaration channel K(u,w), also independent of d, such that
with d'=Kd the complete four-vector (e_P,e_Q,T_P,T_Q) is exactly the same.

The source times and frozen history residual are
  T_P(x)=129/40 + u/2 + 3w/2,
  T_Q(x)=129/40 + u + w,
  R(x)=9*b*z-4*a*(v-z)=-9/10.
Thus the family covers the whole legal u,w rectangle at fixed remaining coordinates,
including both strictly positive side flows and all real boundaries.

## Explicit four-corner certificates

Put D=27/80 and x_ij=x(iD,jD). The target coordinates are ordered
(g,a,b,u,v,w,z). Q_ij[row,col] denotes Q mass transported from seedless
likelihood row to source likelihood column. Cells not listed are exactly zero.

CORNER (0,0):
y00=(15/16,15/16,15/16,29/1280,39/128,29/1280,3/32).
Q00:
  (0,0)=67/720; (0,1)=1/32; (0,5)=29/64000;
  (1,1)=47/160; (3,3)=5/36; (3,5)=771/32000;
  (5,1)=1/80; (5,5)=9/32; (6,5)=2029/64000; (6,6)=67/720.

CORNER (1,0):
y10=(686/705,686/705,659/705,1233/3760,347/1128,0,343/3525).
Q10 (the previously proved nonzero-u corner, independently rechecked):
  (0,0)=20443/72000; (0,3)=9977/1184400; (0,5)=16277/2961000;
  (3,3)=421271/1692000; (4,3)=9/470;
  (5,3)=3677/658000; (5,5)=102899/329000;
  (6,5)=16277/846000; (6,6)=6943/72000.

CORNER (0,1):
y01=(1,4/5,1,7/200,61/200,129/400,2/25).
Q01:
  (0,0)=6943/72000; (0,1)=76/1875;
  (1,1)=34817/150000; (1,3)=101/18750;
  (2,1)=608/9375; (2,3)=659/18750;
  (3,3)=4577/20000; (6,3)=287/22500; (6,6)=20443/72000.

CORNER (1,1):
y11=(29/30,29/30,29/30,261/800,377/1200,261/800,29/300).
Q11:
  (0,0)=10343/36000; (0,3)=5639/360000;
  (3,3)=70931/180000;
  (6,3)=5639/360000; (6,6)=10343/36000.

At each corner, exact rational equalities (checked by VERIFY.py) are:
  y is legal and lies in z=a/10, v=a/10+9*b/40, hence R(y)=0;
  (T_P,T_Q)(y)=(T_P,T_Q)(x);
  Q_ij>=0;
  sum_col Q_ij[row,col] = M_row(y);
  sum_row Q_ij[row,col] = M_col(x);
  sum_row r_row Q_ij[row,col] = r_col M_col(x).
Normalization sum M=1 and likelihood calibration sum r*M=1 hold on both sides.

## Proof for arbitrary real parameters (not a finite-grid extrapolation)

Let s=u/D and t=w/D, both in [0,1], and define four weights:
  h00=(1-s)(1-t), h10=s(1-t), h01=(1-s)t, h11=s*t.
These are nonnegative and sum to one. Set
  y = h00*y00+h10*y10+h01*y01+h11*y11,
  Q = h00*Q00+h10*Q10+h01*Q01+h11*Q11.
The source itself satisfies x=h00*x00+h10*x10+h01*x01+h11*x11.
Legality is a convex system of linear bounds on (g,a,b,u,v,w,z).
Crucially ALL FOUR y_ij lie in the same AFFINE SEEDLESS FACE
  z=a/10, v=a/10+9*b/40.
Every real convex combination remains legal, in the same face; that face
identically satisfies the otherwise bilinear seedless constraint
  9*b*z=4*a*(v-z).
Stopping times and stopping masses are affine in the seven coordinates.
Hence, by weighted summation of the four exact corner identities,
Q is nonnegative, both times agree, and its rows/columns satisfy
  sum_j Q[i,j]=M_i(y),
  sum_i Q[i,j]=M_j(x),
  sum_i r_i*Q[i,j]=r_j*M_j(x).

For every row i with M_i(y)>0, define K[i,j]=Q[i,j]/M_i(y).
For a zero-mass row, nonnegativity and its row-mass equality force Q's
row to vanish; choose the identity row for K there.
Thus K is row stochastic even on the boundary. For arbitrary real
d_j in [0,1], d'_i=sum_j K[i,j]d_j is also in [0,1].
The last two Q column equalities give
  sum_i M_i(y)d'_i=sum_j M_j(x)d_j,
  sum_i r_i*M_i(y)d'_i=sum_j r_j*M_j(x)d_j.
Therefore e_Q, e_P and both times are exactly preserved. QED.

## Evidence / scope / next

The explicit certificates are exact rational and fully encoded in VERIFY.py.
The executed local checker used Python stdlib Fraction with no floating point
and checked each corner, 49 rational pairs of (s,t), and 128 binary declaration
vectors for each check. EXACT_OUTPUT.txt records actual run output.
The ALL-REAL theorem is justified by the affine-face proof and the exact
corner identities, not by sampling. A preliminary LP search found candidates,
but the published proof and checker require no LP package.

Research scope: frozen seven-key four-observer P/Q-BRC model; the R5 mother
question is full set equality of FULL_HIST and seedless LR four-observer images.
Continue from this square by varying v-z or z while keeping a,b,g fixed, and
seek either another common-affine-face lift or a certified non-liftable point.
This theorem does not assert the entire model's image equality or X6 dynamics.
