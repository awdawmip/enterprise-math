# CBRC F7 Driver r457 — Two mixed witnesses, exact finite energy and the 11/20 transition

Date: 2026-11-22 (+08:00). Continuing shared/nonblind Driver mathematical contribution: EM-DVR-DEBB5E. Original F7 mathematical author: EM-CBRCF7-83A1D4. Preserve original frozen RR-AA38973D56330E59D315, its native review and its Source/Activity scope. This extends r454 and r456 rather than replacing either.

## Original frozen mathematical problem

Let A=I+uv^T, with u=(1,1,-1,-1)^T and v=(1,-2,-1,2)^T. Let q:Z² -> [0,infinity) obey q(0,0)=0, q(-x,y)=q(x,y), q(s,0)=1 for s≠0, q(x,y)≥1/2 for every nonzero pair, and the two exact fixed-scale marks q(2,1)=q(-1,-1)=1/2. Write

\[
D_q(z)=q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(z_1,z_2)-q(z_3,z_4),\quad E(q)=\sup_{z\in\mathbb Z^4}|D_q(z)|.
\]

On nonzero pairs write δ(x,y)=q(x,y)-1/2≥0. Use the unchanged finite primitive region

\[
\Omega_4=\{(x,y)\in\mathbb Z^2:x>0,\ y\neq0,\ \gcd(x,|y|)=1,\ x\le10,\ |y|\le3\}.
\]

Assume 1/2≤ε≤4/7, E(q)≤ε; put a=1-ε and b=1/2-ε.

**Theorem (new two-witness exact finite energy).** Under precisely these assumptions,

\[
\boxed{\sum_{(x,y)\in\Omega_4}\delta(x,y)^2\ \ge\
\frac{67}{6}a^2+
\frac{(5-8\varepsilon)^2}{24}+
\frac{(11-20\varepsilon)_+^2}{72},}
\qquad t_+=\max(t,0).
\]

The right side is the exact minimum of the restricted finite system with all primitive old-axis inequalities and two original four-coordinate F7 witnesses below. Its last term is **strictly positive for 1/2≤ε<11/20**, zero for 11/20≤ε≤4/7. At ε=1/2 the exact lower bound is 205/72, improving r456's 17/6 by 1/72. This is an energy bound on the stated finite region; the global minimax interval remains 1/2≤E∞≤4/7.

## Two genuine four-coordinate witnesses

For z₁=(-4,0,-1,2), v^Tz₁=1 and Az₁=(-3,1,-2,1). Using the fixed mark and axis value,

\[
D_q(z_1)=\delta(3,1)-\delta(1,2)-1/2.
\]

For the **new** witness z₂=(3,0,3,1), v^Tz₂=2 and Az₂=(5,2,1,-1), so

\[
D_q(z_2)=\delta(5,2)-\delta(3,1)-1/2.
\]

Consequently the original |D_q|≤ε condition forces two separate half-spaces

\[
x-y\ge b,\qquad c-x\ge b,
\quad x=\delta(3,1),\quad y=\delta(1,2),\quad c=\delta(5,2).
\]

No new property of q was assumed.

## Three disjoint old-axis graph paths

For Ω₄ the exact primitive old-axis graph of r454 has 44 vertices and 29 edges. The witnesses meet precisely three disjoint unmarked three-vertex paths:

\[
x=\delta(3,1)\ --\ u=\delta(6,-1)\ --\ w=\delta(9,1),
\]
\[
r=\delta(5,-2)\ --\ y=\delta(1,2)\ --\ s=\delta(7,-2),
\]
\[
c=\delta(5,2)\ --\ v=\delta(1,-2)\ --\ d=\delta(7,2).
\]

Every edge forces the sum of its two nonnegative δ-values to be at least a. All other components, including the original two fixed marks, remain independent of these three paths. By r454 the unconstrained sum over the full old-axis graph has exact minimum Q(4)a²=(67/6)a², while the three affected free paths contribute 2a².

Given fixed 0≤x,c≤a/2, the least endpoint-path energies are

\[
f(x)=x^2+(a-x)^2+x^2=3x^2-2ax+a^2,\quad
f(c)=3c^2-2ac+a^2.
\]

For fixed 0≤y≤a, the middle-point path energy is

\[
g(y)=(a-y)^2+y^2+(a-y)^2=3y^2-4ay+2a^2.
\]

These are attained by (u,w)=(a-x,x), (v,d)=(a-c,c), (r,s)=(a-y,a-y). The entire finite program is convex; a feasible KKT point on the displayed branches with nonnegative multipliers certifies its global, not merely local, optimum.

## Exact KKT solution and the transition

**Regime I: 1/2≤ε≤11/20**, equivalently -a/9≤b≤0. Both mixed inequalities bind. Set

\[
x=4a/9,\quad y=4a/9-b,\quad c=4a/9+b.
\]

For constraints x-y≥b and c-x≥b respectively, take multipliers

\[
\lambda=4a/3+6b,\qquad \mu=2a/3+6b.
\]

Both are nonnegative throughout this regime; the values satisfy 0≤x,c≤a/2 and 0≤y≤a. Directly,

\[
f'(x)-\lambda+\mu=0,\quad g'(y)+\lambda=0,\quad f'(c)-\mu=0,
\]

and both mixed constraints are equalities. The old-axis edges bind at their displayed path minimizers, with nonnegative internal edge multipliers 2a-4x, 2x, 2(a-y), 2a-4c, 2c. Hence these are valid complete convex KKT certificates. The exact excess energy over the three old-axis path minima is

\[
f(x)+g(y)+f(c)-2a^2=\frac{2a^2}{9}+2ab+6b^2
=\frac{(a+3b)^2}{6}+\frac{(a+9b)^2}{18}.
\]

**Regime II: 11/20≤ε≤4/7**, equivalently -a/6≤b≤-a/9. The second mixed constraint is inactive or exactly on its boundary. Set

\[
x=(a+b)/2,\quad y=(a-b)/2,\quad c=a/3,\quad
\lambda=a+3b,\quad\mu=0.
\]

Then x-y=b and c-x≥b (the latter is equivalent to a+9b≤0); the same three stationarity equations and internal edge multiplier conditions hold. The exact excess energy is (a+3b)²/6.

Combining both regimes and using a+3b=(5-8ε)/2, a+9b=(11-20ε)/2 gives the boxed theorem. Every required old-axis inequality, nonnegativity condition and both |D_q(z_i)|≤ε bounds is satisfied by the KKT assignment, with each displayed mixed witness attaining D_q(z_i)=-ε in its active regime (the second witness may be slack in Regime II). The unchanged other graph components attain their r454 minima independently. This proves exact attainability **for this restricted finite system only**.

## Independent finite evidence and scientific boundary

A separate exact rational checker reconstructs Ω₄ and all primitive old-axis edges, identifies the original marked paths, sets the three affected paths from the piecewise KKT formulas, checks both original matrix witnesses, checks all 29 inequalities and two marks, and compares the complete 44-variable rational energy to the theorem at ε=1/2, 21/40, 13/24, 11/20, 9/16 and 4/7. Rational comparisons are exact, not floating-point tolerances. The symbolic KKT argument proves the entire specified interval of ε.

This result is a new Driver finite-system theorem under the original F7 scientific assumptions, not an independent native Review, a formal Source/Activity event or a claim that the unrestricted F7 problem is solved. The next useful discriminator is a third independent four-coordinate witness against the new exact finite minimizer, or a rigorous B=12 rational minimax certificate, with historical F7 author and Task control states preserved.
