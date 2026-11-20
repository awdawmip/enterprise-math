# Stage321-B — strengthened exterior gap and 62/11-fold Pareto-germ extension

**Classification:** Research2 portable author-side exact rational certificate and mathematical proof; UNREVIEWED / NOT_ADMITTED. No native Source CLAIM, Result, independent review, Foundation promotion or native P000-X6 transfer is claimed. Research date 2026-10-31 Asia/Shanghai.

**Frozen sources:** GLOBAL_KNOWLEDGE_V1 main@d49f63961b75785da65daf58e60f6a926e461e2c; Enterprise Math main@4a473edd23a609d2614c9a5e4318175945cf9ca2; predecessor PR #1736 head fe647ffd831e6e73f18c75b68a53e401d88790fc. Dependencies: Stage307-B.2 exact unique public minimizer and algebraic-root brackets, Stage315-B central-rate MAP uniqueness, Stage316-B exact infimal convolution, Stage320-B global cusp sharpness and the fixed all-F observer reduction. These earlier arguments remain at their author-side evidence status and were not all independently rerun here.

## Precisely typed model

Two hidden positive-mass sources S=0,1; private history h=(J,W,Y); public G=(W,Y); tagged observer (S,J,G); eight locked rates t_h in [0,1], shared across three future Bernoulli F accesses. Future H emits independent fair bits, so public/tagged all-F three-word total variations dominate all history-adaptive H/F readouts by postprocessing. The eight source mass pairs (in lexicographic h order) are (63,1),(21,3),(21,3),(7,9),(9,7),(3,21),(3,21),(1,63), divided by 256. The model does not represent native X6 dynamics.

Stage315 proves all tagged minimizers reset central four rates to t001=t010=1/4, t101=t110=3/4. Stage316 gives the exact reduction with (x,y)=(t000,t100), (x',y')=(1-t111,1-t011):

P3=b(x,y)+b(x',y'), T3=33/1024+c(x,y)+c(x',y').

Define B_k(z)=z^k(1-z)^(3-k), r_k=4B_k(x)/5+B_k(y)/5-p_k where p=(61,21,9,9)/160,
d(x,y)=1/2 sum_{k=0}^3 binom(3,k)|r_k|, b=5d/16,
c=[63D3(1/4,x)+D3(3/4,x)+9D3(1/4,y)+7D3(3/4,y)]/256.
Here D3 denotes TV of three-fold Bernoulli product laws.

Let (x*,y*) be Stage307-B.2's unique global d minimizer, where r0=r1=0,r2>0,r3<0. It lies strictly inside the exact rational intervals:
231083940855521/10^15 < x* < 231083940855522/10^15,
555508857277/10^12 < y* < 555508857278/10^12.
Put beta*=b(x*,y*), Pmin=2beta*, C3(s)=min_{b<=s} c, and F3(z)=min_{P3<=z} T3.

## Lemma 321B.1 — strict exterior gap over full real square

Let B=[23/100,24/100]×[55/100,56/100]. For every real (x,y) in [0,1]^2 outside B:

d(x,y)-d(x*,y*) > 1/50000 and b(x,y)-beta* > 1/160000.

**Exact proof.** Set rational witness w=(231083940855/10^12,555508857277/10^12) and U=d(w)>=d(x*,y*). Cover the exterior by four closed rectangles [0,.23]×[0,1], [.24,1]×[0,1], [.23,.24]×[0,.55], [.23,.24]×[.56,1]. For a subrectangle A, bound each B_k at its two endpoints and the critical point k/3 when present; obtain rational enclosure r_k(A) in [l_k,u_k]. Define the valid lower bound

L(A)=1/2 sum_k binom(3,k) max(0,l_k,-u_k) <= inf_A d.

Bisect the longer side until L(A)-U>1/50000 on every leaf. The supplied executed pure-Fraction checker exhausts the four rectangles in respectively (335,168),(55,28),(29,15),(141,71) (nodes,accepted leaves), total 282 verified leaves; no finite sample substitutes for coverage. The minimum among all 282 exact certified gaps equals
26560643884574661353947893618433/1250000000000000000000000000000000000 > 1/50000.
The leaf rectangles cover the entire exterior (including relevant shared boundaries). Thus d>U+1/50000>=d*+1/50000. Multiply by 5/16. The former certified b exterior gap >1/640000 improves fourfold.

## Lemma 321B.2 — exact rational chamber certificate on expanded rectangle

Take R'=[23055/100000,23157/100000]×[555/1000,556/1000], a subset of B. Stage320's signs r2>0,r3<0 on B imply the local exact identity
d=3r2+max(0,r0)+3max(0,r1).

For chamber indices e0,e1 in {0,1}, b=(5/16)(3r2+e0r0+3e1r1). Differentiating the displayed B_k and polynomial c, exact closed rational interval substitution over all R' proves:
- all 4 determinants det(grad b,grad c) are nonzero: positive only for (e0,e1)=(0,0), negative for the other three; c_x<0 and c_y>0;
- each curve r0=0, r1=0 has nonzero y derivative throughout R' and |dy/dx|<13. Along r0=0 the derivative of r1 w.r.t. x is positive; along r1=0 the derivative of r0 w.r.t. x is negative;
- each of the four oriented kink arms has |db/dx|>18/100 (positive on the right, negative on the left), and their disjoint exact rational interval enclosures of dc/db are:
r1/right in (-122/100,-118/100);
r0/right in (-91/100,-86/100);
r1/left in (17/10,19/10);
r0/left in (29/10,33/10).
- along r1=0/right, with v=dy/dx=-r1_x/r1_y, w=d²y/dx²=-(r1_xx+r1_yy v²)/r1_y, and with B'=b_x+b_y v, B''=b_xx+b_yy v²+b_yw, E'=c_x+c_yv, E''=c_xx+c_yy v²+c_yw, the exact C3 curvature (E''B'-E'B'')/(B')³ is strictly between -42 and -37 on R'.

All these statements follow from explicitly programmed rational interval operations over full real rectangles, not pointwise float searches; the checker prints its exact bound enclosures.

## Theorem 321B.3 — global Pareto germ to epsilon=31/5,000,000

Let delta=31/5,000,000=0.0000062. For every real 0<=epsilon<=delta the full eight-rate Pareto value is

F3(Pmin+epsilon)=33/1024+c(x*,y*)+c(x_epsilon,y_epsilon),

where (x_epsilon,y_epsilon) is the unique rightward r1=0 curve point with b=beta*+epsilon. For epsilon>0 exactly two global tagged-cost minimizers exist: place the entire public slack epsilon in either one of the two outer groups, leaving the other at (x*,y*), and perform the unique central MAP reset. At epsilon=0 the tagged minimizer is unique. For any 0<theta<epsilon, the excess tagged cost of an interior split obeys
37 theta(epsilon-theta) < Delta_epsilon(theta) < 42 theta(epsilon-theta).

**Proof.** By Lemma321B.1, because delta<1/160000, any single-block feasible b<=beta*+delta lies inside B. Stage320's certified cusp sharpness on B gives
d-d* >= (2109/50000)(|x-x*|+|y-y*|).
Thus |x-x*|+|y-y*| <= delta/[(5/16)(2109/50000)] = 124/263625. The minimum exact root-to-R' boundary margin is its right x margin 243029572239/500000000000000; the checker verifies radius < margin, hence every feasible block lies strictly in R'.

The two zero curves extend to x=x*±L, L=1/27000, inside R'. Indeed the exact root margins dominate L in x and 13L in y, while derivative signs keep both curves regular. The outward b increase on each of the four kink arms exceeds (18/100)L=1/150000>delta, so all arms reach every requested epsilon in [0,delta]. No constrained minimizer can occur at a smooth chamber point: c has nonzero gradient and all four det(grad b,grad c) are nonzero; no unconstrained minimizer is possible. Every positive-budget candidate lies on a kink. The four strictly separated cost-vs-budget slopes force the unique rightward r1=0 kink to have lowest cost; its negative derivative ensures the budget binds. This establishes unique C3 minimizer and its strict curvature -42<C3''<-37 across [beta*,beta*+delta].

Using Stage316's exact two-block infimal convolution, minimize C3(beta*+theta)+C3(beta*+epsilon-theta) over theta in [0,epsilon]. Strict concavity places the minima exactly at theta=0 or theta=epsilon. Integrating -42<C3''<-37 yields the asserted strict gap for any interior theta. Finally Stage315's central MAP uniqueness and symmetry yield exactly two full tagged optimizers for epsilon>0, the two endpoints coalescing at epsilon=0. QED.

## Verification and limits

Actual separately executed Python Fraction program: REPRO_STAGE321B.py. Full actual stdout: REPRO_STAGE321B_EXECUTED_STDOUT.txt; terminal certificate STAGE321B_EXPANDED_RECTANGLE_EXTERIOR_PARETO_EXACT_PASS. It certifies 282 leaves, all 4 determinants, 4 kink slope intervals, right-arm curvature, root-to-rectangle localization and branch reach. The continuum theorem combines this rational certificate with the written calculus and the explicitly cited Stage307/315/316/320 source premises. No independent mathematical review, formal checker admission or native X6 observation-preservation mapping is asserted.

This expands Stage320's delta=11/10,000,000 by the exact factor 62/11. The new curvature interval (-42,-37) and corresponding allocation penalty (37,42) supersede the narrower constants on the widened domain.

Next Stage322-B: improve exterior floor beyond 1/50000 and/or expand the y margin and rationally subdivide R' to reduce interval dependency, so the proof can be extended until a genuine optimizer-switch witness or verified algebraic crossover is found. Preserve P000 native six-axis path, three-dimensional slice/third coordinate, triadic closure, time ordering and registered six-field Cell-address bridge as separate proof duties.