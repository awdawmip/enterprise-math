# R5 — Exact nine-edge Blackwell lift of the opposite (negative-residual) saturated corner

Date: 2026-11-08. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Frozen statistical seven-LR-node P/Q-BRC inputs unchanged (Global a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e). Observer-level result, not native X6 dynamics, and P000 remains locked.

## Theorem and exact witnesses

Consider the lawful FULL_HIST flow for all real 0<=t<=1:

    x_minus(t)=(1,t,1,13t/40+1/80,9/40,0,0).

The original history residual is 9*b*z-4*a*(v-z)=-9t/10 (strictly negative for t>0). It is the physically saturated-u, zero-w, theta=0,kappa=1 corner, complementary to the positive-residual x_plus(t) in sibling BRIDGE.md.

**Theorem:** for every real t in [0,1], x_minus(t) admits a lawful seedless LR target, a nonnegative declaration-independent 7x7 calibrated Blackwell transport Q, and thus precisely the same four observables (e_P,e_Q,T_P,T_Q) for every terminal declaration. Any convex source-target interpolation preserves the statement. This covers the entire one-parameter negative-residual saturated source corner, not all low-ratio four-capacity inputs.

For 0<=t<=1/5, an explicit **nine-edge** kernel exists on the saturated seedless affine face F={z'=a'/10, v'-z'=9b'/40}, with target coordinates y=(g',a',b',u',v',w',z'):

    g'=1-15744t/274955
    a'=287406t/274955
    b'=1-60856t/274955
    u'=1/80+74117t/219964
    v'=9/40+15048t/274955
    w'=172901t/2199640
    z'=143703t/1374775

Its only nonzero entries Q_(target i, source j) are

    Q00=(13234t+7209)/72000
    Q02=28195t/1979676
    Q22=(54991-60630t)/109982
    Q32=73307t/1979676
    Q33=(8566t+1591)/36000
    Q45=22556t/274955
    Q55=(1154811-256510t)/4399280
    Q65=5639t/109982
    Q66=(234t+6709)/72000

Every other Q entry equals zero. The probability and likelihood-ratio data are exactly those in sibling VERIFY.py and predecessor PR #1800, with r=(1/10,1/2,3/4,1,5/4,3/2,19/10), seven terminal masses M_i and stopping times T_P,T_Q.

For all 0<=t<=1/5, the following exact identities and inequalities hold:

    sum_j Q_ij=M_i(y),  sum_i Q_ij=M_j(x_minus),
    sum_i r_i Q_ij=r_j*M_j(x_minus),
    T_P(y)=T_P(x_minus), T_Q(y)=T_Q(x_minus),
    y is lawful: 0<=a',b'<=g'<=1, 0<=u'<=13a'/40+b'/80,
       0<=w'<=3a'/40+21b'/80, 0<=z'<=a'/10,
       0<=v'-z'<=9b'/40.

In particular, z'=a'/10 and v'-z'=9b'/40 imply 9b'z'=4a'(v'-z'), so y is exactly seedless LR even though x_minus(t) is not for t>0. For arbitrary terminal declaration d_j in [0,1], define d'_i=(sum_j Q_ij*d_j)/M_i(y) for positive target row masses, zero otherwise, giving exactly matching P/Q error probabilities.

## All-real proof (two endpoints suffice)

**Every coordinate of x_minus(t), y(t) and every entry Q_ij(t) is affine in t**. The Q-terminal mass map M and both stop-time maps T_P,T_Q are affine in the flow. Therefore all calibration, mass, stopping-time equalities above are affine identities in t. Their exact verification at the **two distinct endpoints t=0 and t=1/5**, where the standard-library Fraction checker verifies every equation, suffices to prove each equality identically for every REAL t. Every physical capacity inequality and every Q_ij nonnegativity constraint is likewise affine in t, so endpoint validity implies the entire real interval via convexity. Both endpoint targets lie in the same affine F face, and every interpolated target does too. This is an exact constructive universal proof, not extrapolation from a finite random sample.

On 1/5<=t<=1 the independent prior author-side full F-face wedge theorem PR #1800 applies to all lawful b/5<=a<=b, including x_minus(t) with b=1,a=t. Combining this nine-edge explicit theorem with that previously published result covers the complete x_minus(t) one-parameter family **0<=t<=1**. As a complementary result, sibling BRIDGE.md establishes the entire positive-residual saturated corner x_plus(t), also 0<=t<=1. Both residual signs now have fully certified author-side one-dimensional corner constructions.

For any 0<=h<=1, the source-target interpolation x_h=(1-h)x+h*y is accompanied by Q_h=(1-h)Q+h*diag(M(y)), retaining the equalities and target legality.

## Exact validation, status and next question

NEGATIVE_VERIFY.py implements all seven mass/likelihood equations, the two stops, seedless and physical legalities, the two endpoint checks and 101 exact rational regression checks with Fraction. NEGATIVE_OUTPUT.txt captures actual local execution. Both 0 and 1/5 endpoint exact checks passed; 101 rational regression checks also passed. The all-real conclusion is supported by the affine endpoint proof.

**Limit:** This proves an important special family with p=1,q=0,theta=0,kappa=1, plus the opposite positive-residual corner, but leaves mixed low-ratio four-parameter physical prism and global FULL_HIST vs seedless LR mother question open. Neither these files nor draft PR #1801 imply canonical mathematical admission; active Native Owner/CLAIM could not be confirmed due to BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE / operation_sent=false and Site research_authority_granted=false.

**Next:** For small t, interpolate the two proven opposite corners and inspect whether source capacity parameters theta,kappa,p,q can be covered by a common seedless face. Their two target faces differ: the positive corner used C_1/10, while the negative corner uses F. A constructive multi-chart triangulation of a mixed-capacity simplex, or an exact fixed-face obstruction with alternative face search, is the next discriminating unit.
