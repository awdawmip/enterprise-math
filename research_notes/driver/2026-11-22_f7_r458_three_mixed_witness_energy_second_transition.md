# CBRC F7 Driver r458 — Three mixed F7 witnesses and a second exact energy transition

Date: 2026-11-22 (+08:00). Original F7 author: EM-CBRCF7-83A1D4. Mathematical extension by the continuing, shared/nonblind RESEARCH_DRIVER line EM-DVR-DEBB5E. Preserve original frozen RR-AA38973D56330E59D315 and its actual Source, contribution and Native Review states. Dependencies: exact primitive old-axis graph/Q(4) from r454, and the two-witness exact convex KKT result r457.

## Statement (the unchanged original F7 problem)

A=I+uv^T with u=(1,1,-1,-1), v=(1,-2,-1,2). q:Z²→[0,∞) satisfies q(0,0)=0, q(-x,y)=q(x,y), q(s,0)=1 for s≠0, q≥1/2 at nonzero pairs, and the exact fixed marks q(2,1)=q(-1,-1)=1/2. Let E(q)=sup_z |q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(z_1,z_2)-q(z_3,z_4)|.

Let Ω4={(x,y)∈Z²:x>0, y≠0, gcd(x,|y|)=1, x≤10, |y|≤3} and δ=q-1/2 on nonzero pairs. Suppose E(q)≤ε and 1/2≤ε≤4/7; put a=1-ε and b=1/2-ε.

**Theorem.** Every such q satisfies

\[
\boxed{\displaystyle
\sum_{\Omega_4}\delta(x,y)^2\ \ge\
\frac{67}{6}(1-\varepsilon)^2+
\frac{(5-8\varepsilon)^2}{24}+
\frac{(11-20\varepsilon)_+^2}{72}+
\frac{(10-19\varepsilon)_+^2}{36}.}
\]

Here t_+=max(t,0). The final term is a new strict improvement over r457 for **1/2≤ε<10/19**, becoming zero from ε=10/19 onward. At ε=1/2 the exact finite lower bound is **137/48**, versus r457's 205/72, an increase of 1/144.

Moreover the stated right side is exactly attained in the finite convex subsystem comprising *all* primitive old-axis inequalities on Ω4, the two unchanged original scalar marks and precisely **three** original F7 four-coordinate witnesses below. It is a universal energy lower bound for the original F7 problem, but not a globally admissible q construction.

## The new third witness and the fourth path

The earlier two original F7 witnesses z1=(-4,0,-1,2) and z2=(3,0,3,1) give, with x=δ(3,1), y=δ(1,2), c=δ(5,2),

\[
x-y\ge b,\qquad c-x\ge b.
\]

The **new** z3=(1,-2,1,-1) has v^Tz3=2, Az3=(3,0,-1,-3). Therefore

\[
D_q(z_3)=\frac12+\delta(1,-3)-\delta(1,-2).
\]

In Ω4, the exact old-axis graph component containing h=δ(1,-3) is a disjoint, unmarked three-vertex path

\[
\delta(8,3)\ --\ h=\delta(1,-3)\ --\ \delta(10,3).
\]

The r457 path with c as its endpoint is

\[
c=\delta(5,2)\ --\ v_2=\delta(1,-2)\ --\ \delta(7,2).
\]

At an energy-minimizing assignment with 0≤c≤a/2 this old-axis path has v2=a-c. The genuine new F7 upper inequality D_q(z3)≤ε then forces v2-h≥b, equivalently

\[
c+h\le a-b.
\]

These are four mutually disjoint old-axis free paths: an endpoint path with root x, a center path with root y, an endpoint path with root c and a center path with root h. All others stay at their r454 exact minima.

## Exact four-path convex optimization

For an endpoint-rooted three-path with root t∈[0,a/2] the exact minimum is f(t)=2t²+(a-t)². For a center-rooted three-path with root t∈[0,a] it is g(t)=t²+2(a-t)². In particular f'(t)=6t-2a and g'(t)=6t-4a.

Minimize f(x)+g(y)+f(c)+g(h) subject to x-y≥b, c-x≥b and c+h≤a-b. This is a convex program. The four free path baselines total (8/3)a².

**Regime I, 1/2≤ε≤10/19** (equivalently -a/18≤b≤0). All three inequalities bind. The exact optimizer is

\[
x=\frac{5a-6b}{12},\quad
y=\frac{5a-18b}{12},\quad
c=\frac{5a+6b}{12},\quad
h=\frac{7a-18b}{12}.
\]

With multipliers for the three constraints, respectively,

\[
\lambda=\frac32a+9b,\qquad
\mu=a+12b,\qquad
\nu=\frac12a+9b,
\]

all multipliers are nonnegative on this regime. Direct substitution verifies the stationarity identities

\[
f'(x)-\lambda+\mu=0,\quad
g'(y)+\lambda=0,\quad
f'(c)-\mu+\nu=0,\quad
g'(h)+\nu=0.
\]

All three complementary-slackness products vanish, 0≤x,c≤a/2, 0≤y,h≤a, and the old-axis edge multipliers along each three-path are nonnegative. Therefore this is the global convex KKT minimum. Reducing y=x-b, c=x+b, h=a-x-2b gives x=(5a-6b)/12 and the **new excess over the r457 three-path optimum plus the fourth free path** of exactly (a+18b)²/36.

**Regime II, 10/19≤ε≤4/7** (b≤-a/18). Retain the *exact* r457 optimum for x,y,c, and take h=2a/3, the center of a free three-path. Then c+h≤a-b holds since a+18b≤0 in the r457 active-second-witness regime. In the later second-witness-inactive regime ε≥11/20, c=a/3, so c+h=a≤a-b as b≤0. The third multiplier may be zero, and this remains a global feasible KKT solution. Hence the new increment is zero.

The other paths remain at their original exact r454 minima. Adding to the r457 formula and writing a+18b=10-19ε proves the theorem for every declared ε.

## Exact independent finite reconstruction

An independent Fraction-based enumeration rebuilt all 44 vertices and 29 legal primitive old-axis edges of Ω4, generated the original r454 baseline of Q(4)=67/6, explicitly assigned the 12 vertices in the four affected disjoint paths from the piecewise optimizer, and checked all edge inequalities, both marked values, and all three original F7 matrix witnesses. It verified exact full energy and new gap (no numeric tolerances):

| ε | Exact full energy | Third-witness gain over r457 |
|---:|---:|---:|
| 1/2 | 137/48 | 1/144 |
| 21/40 | 48953/19200 | 1/57600 |
| 10/19 | 915/361 | 0 |
| 13/24 | 24517/10368 | 0 |
| 11/20 | 1821/800 | 0 |
| 4/7 | 807/392 | 0 |

The symbolic convex KKT argument proves the whole interval; the exact finite calculations corroborate the graph and arithmetic. This nonblind finite theorem is not a newly accepted Native Review or Result. The unrestricted F7 global minimax remains 1/2≤E∞≤4/7; B=12 exact minimax and larger cross-slice families remain open. No original author, active owner, Source/Activity link or P000 state changes.
