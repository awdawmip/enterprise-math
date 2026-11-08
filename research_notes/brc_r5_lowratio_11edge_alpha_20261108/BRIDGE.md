# R5 — Complete all-real positive-residual corner by a two-chart fixed-face bridge

Date: 2026-11-08. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. The result is for the frozen seven-node P/Q-BRC observer, not for native X6 dynamics. Frozen scientific pins remain Global a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. No P000 or ACTIVE worldview change.

## Precise all-real theorem and scope

Consider the previously defined legal source x(t)=(1,t,1,0,t/10,3t/40+21/80,t/10) for 0<=t<=1. Its historical residual is exactly 9t/10 (strictly positive when t>0). The seven Q-terminal masses M(x) and stopping times T_P(x), T_Q(x), with likelihood ratios r=(1/10,1/2,3/4,1,5/4,3/2,19/10), are exactly those in the sibling VERIFY.py and [prior PR #1800](https://github.com/awdawmip/enterprise-math/pull/1800).

**Theorem:** for every real t in [0,1], there exists a lawful seedless LR target y(t) and a nonnegative, declaration-independent 7x7 Blackwell transport Q(t) satisfying

    sum_j Q_ij = M_i(y),
    sum_i Q_ij = M_j(x),
    sum_i r_i Q_ij = r_j M_j(x),
    T_P(y)=T_P(x), T_Q(y)=T_Q(x).

The terminal declaration transfer d'_i=(sum_j Q_ij*d_j)/M_i(y) on positive target-mass rows (otherwise zero) preserves both errors and both stopping times for every real declaration d in [0,1]^7. Source-to-target interpolation x_h=(1-h)x+h*y, 0<=h<=1, inherits the result with Q_h=(1-h)Q+h*diag(M(y)). This theorem covers **one specific saturated-u=0, saturated-w, positive-residual source corner**, not the entire four-parameter low-ratio physical prism nor unrestricted FULL_HIST sources.

## Two new exact rational anchor certificates on one common seedless affine face

Let tau=1/10, and the common target face be C_tau={ z'=a'/100, v'-z'=9b'/400 }. Every legal target in C_tau is seedless because 9b'z'=4a'(v'-z'). Let t0=1/50 and t1=1/5. Here are the two complete exact rational targets, in the original order (g',a',b',u',v',w',z'):

    y(t0)=(914/919,0,914/919,327/459500,4113/183800,9597/36760,0)
    y(t1)=(16304/16325,6407/32650,16304/16325,0,3191/130600,72321/261200,6407/3265000)

For t=t0 the complete sparse transport has precisely the following nonzero entries (target row i, source column j, Q_ij):

    (0,0,1423/450000)
    (0,1,7531487/827100000)
    (1,1,1199013/459500000)
    (1,2,4186487/459500000)
    (2,2,1265335841/2642125000)
    (2,3,48539159/2642125000)
    (3,1,7531487/1033875000)
    (3,3,216792907/689250000)
    (6,2,4186487/2113700000)
    (6,3,48539159/9511650000)
    (6,6,67423/450000)

For t=t1:

    (0,0,2879/360000)
    (0,1,63/65300)
    (0,2,265403/73462500)
    (1,1,19919/261200)
    (2,2,7897097/20406250)
    (2,3,581431/40812500)
    (3,2,3450239/367312500)
    (3,3,327285391/979500000)
    (6,1,9/32650)
    (6,3,581431/146925000)
    (6,6,58379/360000)

All unlisted matrix entries are zero. Each rational anchor is checked in BRIDGE_VERIFY.py using Python Fraction against every mass, weighted mass, stop, legality, seedless and face equation.

## Rigorous all-real interpolation and coverage

For any real t in [1/50,1/5], put lambda=(t-1/50)/(1/5-1/50). Set x_t=(1-lambda)x(t0)+lambda*x(t1), y_t=(1-lambda)y(t0)+lambda*y(t1), and Q_t=(1-lambda)Q(t0)+lambda*Q(t1). The original source x(t) is affine in t, hence x_t=x(t). Nonnegative convex weights keep the two anchors' 7x7 transport entries nonnegative and targets physically lawful. The target face C_tau is affine and seedless for all of its legal elements. All 7 row-mass, 7 column-mass, 7 LR-weighted-column and both stop identities are linear in the triple, so they hold for EVERY REAL t in this interval, including all irrational parameters. The terminal declaration stochastic transfer then follows by row normalization.

Sibling RESEARCH.md proves an independent exact eleven-edge formula on [0,alpha], with alpha=(sqrt(3385758529)-55477)/68458 and 1/26<alpha<1/25; therefore [0,alpha] overlaps [1/50,1/5]. The two charts prove this difficult corner for the **whole [0,1/5]**.

The predecessor PR #1800 separately constructs a lawful Blackwell lift for all legal b/5<=a<=b (and arbitrary physical capacities). Our normalized corner has b=1, a=t and belongs to that previously author-proved region for 1/5<=t<=1. Taken together, **the entire normalized saturated corner is author-proved on 0<=t<=1**.

This is an exact two-chart positive-residual local result, not an admission that the whole R5 mother question is solved. Independent review of both this bridge and the predecessor proof remains outstanding.

## Exact verification

BRIDGE_VERIFY.py contains both exact targets and all 22 sparse rational nonzero coefficients, imports sibling VERIFY.py, and uses Fraction for the two full seven-node anchor checks and 201 interpolation regression points (endpoints included). Output of actual local execution is in BRIDGE_OUTPUT.txt. Universal truth follows from exact rational anchor identities plus the affine convex proof, not by extrapolating 201 finite checks.

## Next discriminating unit

For 0<=a/b<1/5 choose a **different full-capacity source corner**, e.g. u=u_max,w=0 and theta=0,kappa=1 (negative residual), or a mixed p,q,theta,kappa point. Seek an exact low-ratio seedless target and 7x7 calibrated kernel. Use the new C_(1/10) face and earlier F/G faces as candidate constructions but change representation if needed. A failed fixed-face LP only restricts that face.

No native Researcher-ID, active Owner or formal CLAIM was obtained: Source backend control_tasks and session_start returned BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE, operation_sent=false; Site research_authority_granted=false. This is immutable author-side evidence, not Result/Review/Foundation admission.
