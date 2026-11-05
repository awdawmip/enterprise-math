# Exact BRC N=4 S23 K=17 auxiliary observation-design theorem: 6/7 <= s <= 7/8

Date: 2026-11-05. Source model frozen at enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Author analytic proof; exact rational implementation executed; independent review and native Result admission pending. Continues author proof commit 293d3d4cee964975f1c020fdacb80138e235d1ed.

## Model

Let a=11/21, b=10/21 and 6/7<=s<=7/8. Source observation T compares (as,1-s,bs) with (bs,1-s,as); its distinct Bernoulli projection B compares (as,1-as) with (bs,1-bs). Keep branch/provenance types separate and optimize one shared Chernoff tilt t between 0 and 1:

fT(t,s)=-ln[1-s+s(a^t b^(1-t)+b^t a^(1-t))];
fB(t,s)=-ln[(as)^t(bs)^(1-t)+(1-as)^t(1-bs)^(1-t)];
F(m,n;s)=max_t(m fT(t,s)+n fB(t,s)),
CT=F(1,0;s), CB=F(0,1;s), H=fB(1/2,s).
Feasible integers m,n>=0 obey (2-s)m+n<=17.

## Result: full optimizer set

There are unique continuous crossings alpha in (8573/10000,8574/10000) and beta in (8668/10000,8669/10000).
- 6/7<=s<alpha: (14,1) unique.
- s=alpha: (14,1) and (0,17), precisely.
- alpha<s<13/15: (0,17) unique.
- 13/15<=s<beta: (15,0) unique.
- s=beta: (15,0) and (0,17), precisely.
- beta<s<7/8: (0,17) unique.
- s=7/8: (8,8) unique.

## Exact finite-interval proof

For each m the best allowed n is n_m(s)=17-2m+floor(ms), because any strictly smaller n lowers F. Exact rational enumeration of k/m for 1<=m<=17 finds only three breakpoints 6/7,13/15,7/8. Exact upper convex hull vertices of all feasible count pairs are respectively [(0,17),(14,1)] on [6/7,13/15), [(0,17),(15,0)] on [13/15,7/8), and [(0,17),(8,8),(15,0)] at 7/8. The code checks each left endpoint and an interior representative, and breakpoint exhaustiveness carries this to all real s in the cells. F is convex in the count variables and strictly improves with additional B, reducing maximization to hull vertices.

For each fixed t, fT is convex in s: its logarithm argument is positive affine. For fixed t, fB is convex: its second logarithm summand is the weighted geometric mean of two positive affine functions, hence concave in s, while the first summand is affine; minus logarithm of their positive concave sum is convex. Supremum over t preserves convexity, so both F(m,n;s) and CB(s) are convex in real s.

Symmetry of T gives its unique maximizing tilt t_T=1/2, hence m CT(s)+n H(s) <= F(m,n;s) <= m CT(s)+n CB(s). Write L=m CT+n H and U=m CT+n CB. To establish strict decrease of G(s)=F(m,n;s)-17 CB(s) on each active cell, subdivide it into twelve rational pieces [x,y] and set delta=1/10000. Convex secants imply for a.e. z in [x,y]:

F'(z) <= [U(y+delta)-L(y)]/delta;
CB'(z) >= [CB(x)-CB(x-delta)]/delta.

VERIFY.py certifies at each piece the strict rational inequality 17[CB(x)-CB(x-delta)] > U(y+delta)-L(y), giving G'(z)<0 a.e. and therefore strict decrease throughout each complete real interval. There are 24 such certificates. Four exact lower signs L-17CB>0 at s=6/7,8573/10000,13/15,8668/10000 and two upper signs 17CB-U>0 at 8574/10000,8669/10000 give exactly one crossing in each bracket. At 7/8 two strict inequalities 8CT+8H>17CB and 8H>7CT establish that (8,8) beats both remaining hull vertices.

At the tie points, the B and T experiments have different unique maximizing tilts. The T optimum is 1/2; for Bernoulli p=as,q=bs with p>q, the B optimum at t=1/2 would require r(p/q)=r((1-q)/(1-p)), where r(u)=ln(u)/(sqrt(u)-1/sqrt(u)) is strictly decreasing on u>1. This would force p+q=1, contradicting p+q=s<1. Thus no interior point on the segment joining tied vertices can attain their F value: equality in the convexity bound would require one tilt simultaneously maximizing both endpoints. Lower-count designs are strictly inferior. Every optimizer is therefore listed.

## Executed rational verifier

The self-contained Python stdlib script VERIFY.py encloses square roots between neighboring multiples of 10^-35 and uses a 32-term log-atanh series with rigorously bounded remainder 2|v|^65/[65(1-v^2)], requiring |v|<1/3. CB uses a rigorous Bernoulli KL expression at the Chernoff-optimal tilted Bernoulli rho=J/(L+J), L=ln(a/b), J=ln[(1-bs)/(1-as)]. Rational-interval operations preserve enclosure. Actual check: 24 monotonicity signs, 6 bracket signs, 2 boundary signs, plus all floor breakpoints and hulls. The complete captured stdout is RUN_EVIDENCE.txt; expected terminal marker PASS_BRC_S23_K17_PHASE_S6_7_TO_S7_8_EXACT_20261105.

Scope: complete two-observer shared-tilt auxiliary integer design for every real s in [6/7,7/8]; this result is not a bound on the original ten-label S23 minimax, which retains its separately tracked [1/2,2/3] enclosure. Bridge and independent review remain the next units.
