# R5 — three-parameter negative-residual low-slack Blackwell family

**Date**: 2026-11-08. **Science**: same frozen pins and seven likelihood keys as RESEARCH.md and SIDE_LOW_SLACK.md. Author-side all-real proof, independently checkable exact rational matrix; no formal project admission.

## Theorem

Let 0 <= u <= 503/1600, 0 <= w <= 32383/175840, 0 <= t <= 1 be arbitrary real numbers. Define

x(u,w)=(1,1,1/2,u,9/80,w,0)
y(u,w)=(39/40,19/20,9/20,u,3/16,w,57/628)
x_t(u,w)=(1-t)*x(u,w)+t*y(u,w).

For every triple (u,w,t) in this box and every real declaration d in [0,1]^7, there is a stochastic declaration map from the single legal seedless LR target y(u,w) reproducing all four observations (e_P,e_Q,T_P,T_Q) of (x_t(u,w),d).

The residual along the full box is independent of u,w:
R(x_t)=-9*(t-1)*(307*t-3140)/62800 <0 when 0<=t<1; at t=1 it is zero.

Both source and target have the same stopping times at each (u,w) (base times (14/5,229/80) plus (u/2+3w/2,u+w)).

## Calibrated kernel and proof

Reuse the exact rational matrix Q0 published in SIDE_LOW_SLACK.md, originally transporting y(0,0) to x(0,0). At fixed other coordinates, the seven stopping masses depend on (u,w) affinely, with common increment

D(u,w)=(509u/900+w/100, -u, 0, 191(u+w)/450,
        0, -w, u/100+509w/900).

Thus M(x(u,w))=M(x(0,0))+D(u,w) and M(y(u,w))=M(y(0,0))+D(u,w). Define the seven-by-seven Q-mass kernel

Q(u,w)=Q0+diag(D(u,w)).

All off-diagonal entries remain those of nonnegative Q0. The only negative diagonal increments are D_1=-u and D_5=-w; corresponding base diagonal entries are exactly Q0[1,1]=503/1600 and Q0[5,5]=32383/175840. Therefore the parameter bounds guarantee Q(u,w)>=0. All other diagonal increments are nonnegative. The source's physical capacities are u<=53/160, w<=33/160, and the target capacities are u<=503/1600, w<=303/1600; the chosen rectangle fits both. The seedless condition is independent of u,w and continues to hold for y.

Adding a diagonal increment affects each corresponding P and Q column by exactly (r_j D_j,D_j). Therefore:
sum_j Q(u,w)[i,j] = M_i(y(u,w));
sum_i Q(u,w)[i,j] = M_j(x(u,w));
sum_i r_i Q(u,w)[i,j] = r_j M_j(x(u,w)).

For real t in [0,1], set Q_t(u,w)=(1-t)*Q(u,w)+t*diag(M(y(u,w))).

Nonnegativity follows by convexity; its row masses stay M(y(u,w)), and its calibrated column-mass identities become those of x_t(u,w) by the affine mass laws. Both stop times interpolate identical endpoints. On positive-mass target rows divide by M_i(y(u,w)) to produce a stochastic declaration kernel; arbitrary stochastic rows at zero target mass are harmless. This is a parameter-uniform all-real proof independent of finite sampling.

At t=0, all flows in this u,w rectangle have a=g=1,z=0,b=1/2, so the same boundary argument in SIDE_LOW_SLACK.md proves they lie outside the earlier conv(C union F union H_slack). Both side flows can be simultaneously positive, including their displayed parameter maxima. Their negative residual and zero g slack exclude the predecessor's simple six-edge shift.

## Verification and next

VERIFY_SIDE_RECT.py runs the existing exact certificate VERIFY_SIDE.py and checks the diagonal increment bounds, then verifies 25 rational parameter pairs (u,w) and 125 triples (u,w,t), including both zero and maximum flows. Every test checks source/target legality, seedless equation, both stop times, full calibrated Q transport and several declarations via Python Fraction; captured stdout is EXACT_SIDE_RECT_OUTPUT.txt. The all-real claim follows from the displayed algebraic kernel formulas.

Next: enlarge the box by changing the seedless target or redistributing rows of the Blackwell kernel, or seek another face with a != b, u,w>0 and additional free variables. Globally, the full pointwise image-equivalence mother problem remains open; role Owner/CLAIM and independent mathematical review are unconfirmed.
