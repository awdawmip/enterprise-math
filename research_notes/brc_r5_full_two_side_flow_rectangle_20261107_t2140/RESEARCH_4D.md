# R5: complete maximal-early-flow four-parameter Blackwell lift

Date: 2026-11-07 Asia/Shanghai. Exact rational author-side theorem, independent mathematical review pending. Frozen scientific pins GLOBAL a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e remain unchanged.

## Theorem: one entire four-real-parameter legal FULL_HIST face

In the frozen four-stage, seven likelihood-key P/Q-BRC observer with
r=(1/10,1/2,3/4,1,5/4,3/2,19/10), for EVERY real
  0 <= u <= 27/80,
  0 <= w <= 27/80,
  0 <= z <= 1/10,
  0 <= q <= 9/40,
the FULL_HIST flow
  x=(g,a,b,u,v,w,z)=(1,1,1,u,z+q,w,z)
is legal. For EVERY real seven-key declaration d in [0,1]^7 there exists
a single legal seedless LR flow y(u,w,z,q) and one row-stochastic calibrated
declaration kernel K(u,w,z,q), independent of d, such that with d'=Kd,
  (e_P,e_Q,T_P,T_Q)(x,d)=(e_P,e_Q,T_P,T_Q)(y,d').

Both signed history residual regimes and zero are covered:
  R(x)=9*b*z-4*a*(v-z)=9z-4q in [-9/10,+9/10].
The two source stopping times are
  T_P(x)=3+u/2+z+q+3w/2,
  T_Q(x)=3+u+z+q+w.

The result is FULL-HIST -> SEEDLESS pointwise Blackwell lifting for the
COMPLETE legal face g=a=b=1 of the frozen flow parameterization,
simultaneously for the entire real declaration cube.

## Sixteen explicit corner certificates, grouped in four blocks

Set D=27/80, Z=1/10, V=9/40. Each corner has
u in {0,D}, w in {0,D}, z in {0,Z}, q in {0,V}.
Every target seedless flow lies on the SAME AFFINE SEEDLESS FACE
  z_target=a_target/10,
  v_target=a_target/10 + (9/40)*b_target.
This linear face identically satisfies 9*b*z=4*a*(v-z) and is convex.

The four z=0,q=V corner targets and 7x7 transports are exactly given
in RESEARCH.md and VERIFY.py of this folder. They were checked anew.

The four z=0,q=0 targets and transported matrices follow. Rows correspond to
seedless likelihood keys; columns to FULL_HIST source keys. All omitted entries
are zero. Their full data is also in VERIFY_3D.py.

z=0,q=0, (u,w)=(0,0):
  y=(4/5,4/5,4/5,7/100,13/50,7/100,2/25)
  Q: (0,1)=197/1875; (0,5)=11/360; (1,1)=1/5;
     (3,1)=169/45000; (3,3)=13/40; (5,5)=1/5;
     (6,1)=2581/90000; (6,5)=77/720.

z=0,q=0, (u,w)=(D,0):
  y=(1,1,2/3,61/240,1/4,0,1/10)
  Q: (0,0)=1527/8000; (0,3)=9/560; (0,5)=943/37800;
     (1,3)=19/240; (3,3)=2179/12000; (4,3)=1/6;
     (5,3)=13/525; (5,5)=473/2100; (6,5)=943/10800;
     (6,6)=27/8000.

z=0,q=0, (u,w)=(0,D):
  y=(1,1/2,1,1/20,11/40,21/80,1/20)
  Q: (0,0)=27/8000; (0,1)=17/144; (0,3)=187/12000;
     (1,1)=1/8; (2,3)=1/4; (3,1)=17/180;
     (3,3)=727/7200; (5,3)=3/80;
     (6,3)=2311/36000; (6,6)=1527/8000.

z=0,q=0, (u,w)=(D,D):
  y=(1,1,1,7/40,13/40,7/40,1/10)
  Q: (0,0)=777/4000; (0,3)=923/36000;
     (1,3)=13/80; (3,3)=2117/9000;
     (5,3)=13/80; (6,3)=923/36000; (6,6)=777/4000.

The four z=Z,q=0 positive-residual corner certificates:

z=Z,q=0, (u,w)=(0,0):
  y=(127/130,73/130,73/130,1971/10400,73/400,1971/10400,73/1300)
  Q: (0,0)=47/1800; (0,1)=27/208;
     (0,3)=93959/10764000; (0,5)=93959/8280000;
     (2,1)=27/130; (3,3)=181447/780000;
     (4,3)=93959/2990000; (4,5)=527041/2990000;
     (6,5)=701459/4680000; (6,6)=47/1800.

z=Z,q=0, (u,w)=(0,D):
  y=(1,11/20,1,63/800,7/25,243/800,11/200)
  Q: (0,0)=2123/72000; (0,1)=22591/180000;
     (1,1)=10067/900000; (1,3)=91183/900000;
     (2,1)=22591/112500; (2,3)=5443/225000;
     (3,3)=13651/60000; (6,3)=11341/180000;
     (6,6)=15623/72000.

z=Z,q=0, (u,w)=(D,0):
  y=(1,1,11/20,531/1600,179/800,171/1600,1/10)
  Q: (0,0)=15623/72000; (0,3)=35329/720000;
     (3,3)=685133/3600000; (3,5)=234277/3600000;
     (4,3)=35329/200000; (4,5)=9671/200000;
     (5,5)=9/80; (6,5)=80329/720000; (6,6)=2123/72000.

z=Z,q=0, (u,w)=(D,D):
  y=(37/40,37/40,37/40,999/3200,481/1600,999/3200,37/400)
  Q: (0,0)=7933/36000; (0,3)=100151/1440000;
     (3,3)=100843/240000; (6,3)=100151/1440000;
     (6,6)=7933/36000.

The remaining four z=Z,q=V corners already satisfy the seedless face
as x=(1,1,1,u,13/40,w,1/10). For them choose y=x and
Q[i,j]=M_i(x) when i=j and zero otherwise (identity experiment).

## Exact four-dimensional all-real proof

For each scalar coordinate, write its normalized parameter in [0,1]:
  s=u/D, t=w/D, p=z/Z, h=q/V.
Assign to each of the 16 corners c=(i,j,k,l) the NONNEGATIVE weight
  omega_c=(s if i=1 else 1-s)
         *(t if j=1 else 1-t)
         *(p if k=1 else 1-p)
         *(h if l=1 else 1-h).
Their sum is exactly one, and x=SUM_c omega_c * x_c because the source flow
is affine in the four scalars.

Define the explicit mixed target and transported mass:
  y=SUM_c omega_c * y_c,
  Q=SUM_c omega_c * Q_c.

All 16 targets are LEGAL and satisfy the SAME LINEAR seedless-face equations
z=a/10 and v=a/10+9b/40. Therefore their arbitrary real convex combination
is legal and seedless, even though the general seedless condition is bilinear.
All seven Q stopping masses M and both times are AFFINE in the seven flow
coordinates. At each of the sixteen corners, the exact rational data satisfy
  Q_c>=0;
  SUM_j Q_c[i,j] = M_i(y_c);
  SUM_i Q_c[i,j] = M_j(x_c);
  SUM_i r_i Q_c[i,j] = r_j M_j(x_c);
  T_P(y_c)=T_P(x_c), T_Q(y_c)=T_Q(x_c).
The four equalities remain valid on taking the indicated convex mixture.

For each y row with M_i(y)>0 let K[i,j]=Q[i,j]/M_i(y).
A zero-mass row of a nonnegative Q must vanish; choose the identity kernel
row there. Hence K is row stochastic and d'=Kd belongs to [0,1]^7.
The two calibrated column equalities give simultaneously
  SUM_i M_i(y) d'_i = SUM_j M_j(x) d_j,
  SUM_i r_i M_i(y) d'_i = SUM_j r_j M_j(x) d_j.
These are e_Q and (1-e_P). Both stopping times are preserved.
Every algebraic step holds for ALL REAL inputs and edge cases. QED.

## Verification, scope, source and next

The published code is chained to avoid duplicating the frozen seven-mass
definition: VERIFY.py holds the exact 2D corner data and mass/time formulae,
VERIFY_3D.py adds four lower-q corners, and VERIFY_4D.py adds the four
positive-residual corners plus four identity transports. Exact Fraction
checks establish every corner flow bound, zero seedless residual, both times,
all seven nonnegative row equations and both types of seven column equations,
and likelihood/stop normalization. Executed the expanded local scripts:
2D: 49 rational (s,t) sample pairs; 3D: 125 rational (s,t,h) triples;
4D: 81 rational quadruples with 128 binary declarations for each checked case.
EXACT_OUTPUT_4D.txt records the executed chained output. The analytic
multilinear proof is the source of the all-real theorem.

This is an exact *special-face theorem* internal to the frozen P/Q-BRC model.
It establishes pointwise lifting for the whole g=a=b=1 full-history face,
including both history-residual signs. The full-image R5 mother question still
includes g,a,b below 1 and other earlier parameter regimes.

Next: retain this calibrated-transport method and seek an explicit adjacent
early-flow face with g<1 or a<g or b<g, first with rational vertex tests,
then prove a common affine seedless interpolation if possible. Do not mistake
a failed candidate transport for a global non-liftability proof.
Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
