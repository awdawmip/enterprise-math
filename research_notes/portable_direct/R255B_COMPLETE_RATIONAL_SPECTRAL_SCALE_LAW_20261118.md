# R255B — Complete rational-parameter formula for the 63-mask integral spectral scale

Research date: 2026-11-18 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_COMPUTATION / NOT_REVIEWED.
Frozen science: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Parent R255: e58fda11e2258cc7c896c628dbb3cfc918629921; R254/R254A: d97f5cb6d3cae6fc35107b605da809a2eb12e5dc.

## Theorem

Fix the positive scalar auxiliary observer with all 63 **labelled** source masks. For any rational 39/100 < s < 41/100 let

\[
t(s)=\frac{1691s-2615}{2615s-3539},\quad
a=(1/5,1/4,3/10,9/20,s,2/3,t),\quad b_0=13/60,\quad
b_i=(5/18)|1/2-a_i|\quad (i\ge1).
\]

For D_m={0} union {i+1: bit i of m is 1} define

\[
c_m(x)=\prod_{i\in D_m}(x-a_i)-\sum_{i\in D_m}b_i\prod_{j\in D_m\setminus\{i\}}(x-a_j)
\]

of degree d_m. Let T_min(s) be the least positive integer T for which every T^{d_m} c_m(y/T) belongs to Z[y], and let E(s) be the lcm of the reduced denominators of all fourteen a_i,b_i.

Using normalized p-adic valuations v_p and indicator 1_P, the **exact global rational formula** is

\[
\boxed{T_{\min}(s)=\frac{E(s)}
 {13^{\mathbf1_{v_{13}(s)\le-2}}\,
  23^{\mathbf1_{v_{23}(t(s))\le-2}}}.}
\]

Thus E/T_min belongs to {1,13,23,299}; both exceptions can coexist. R254A's finite grid is a special case.

## Proof — complete prime-adic classification

Set u_i=a_i+b_i. The singleton mask {0} has characteristic polynomial x-u_0, while each two-state mask {0,i} has first nonleading coefficient -(u_0+u_i). Thus integrality of all scaled characteristic polynomials implies T u_0 and every T(u_0+u_i) are integers, hence

\[
U=\operatorname{lcm}_{i=0}^6\operatorname{den}(u_i)\mid T_{\min}(s).
\]

Also T_min(s) divides E(s): each codimension-j coefficient is a sum of products of j entries from a_i,b_i, so multiplying by E^j clears all its denominators. Consequently v_p(U) <= v_p(T_min) <= v_p(E) for every prime.

Three fixed traces are u_1=23/72, u_5=77/108, and u_2=16/45. They force fixed denominators 2^3*3^3*5 inside U; no fixed a_i or b_i has any other denominator prime. For the variable z=s (z<1/2), respectively z=t (z>1/2), the trace formulas are

\[
u_s=(13/18)s+5/36,\qquad u_t=(23/18)t-5/36,
\]

and b_z is affine in z.

**Primes outside {2,3,5,13,23}.** Both slopes are p-units and offsets are p-integral. If s or t has a p-adic pole, the corresponding u has the same pole order as a=z, while b has no larger order; otherwise there is no p-denominator. Therefore v_p(U)=v_p(E).

**p=2,3,5.** Fixed U has baseline exponents (3,3,1). For either z:
- If v_2(z)=-r with r>=2, both u_z and b_z have pole order r+1; when r<=1, variable pole orders are <=2, below baseline 3.
- If v_3(z)=-r with r>=1, both have pole order r+2; otherwise variable pole orders are <=2, below baseline 3.
- If v_5(z)=-r with r>=1, u_z and a_z have pole order r while b_z has at most max(0,r-1); otherwise baseline 1 suffices.

These follow immediately from the affine coefficients and their valuations. Hence v_p(U)=v_p(E) at p=2,3,5.

**p=13.** If v_13(s)=-r<0, the fractional-linear formula gives v_13(t)=0 because 1691 and 2615 are 13-units. R255 proved by the trace and mask-9 coefficients that v_13(E)=r and v_13(T_min)=max(1,r-1). If s is 13-integral but t has a 13-adic pole, slope 23/18 is a 13-unit, so u_t witnesses the full E exponent. If neither has a pole, both are integral. Thus a single factor 13 is saved precisely when v_13(s)<=-2.

**p=23.** If v_23(t)=-r<0, the inverse Mobius relation s=(3539t-2615)/(2615t-1691) gives v_23(s)=0, since 3539 and 2615 are 23-units. R255 proved by the trace and mask-32 coefficients that v_23(E)=r and v_23(T_min)=max(1,r-1). If t is 23-integral but s has a 23-adic pole, slope 13/18 is a 23-unit, and u_s witnesses E; if neither has a pole, both are integral. Thus a single factor 23 is saved precisely when v_23(t)<=-2.

Every prime exponent of T_min is determined, proving the formula. QED.

## Exact simultaneous witness and finite verification

For s=866/2197, t=389159/500963,

\[
E=1,188,664,967,880,\quad T_{\min}=3,975,468,120,\quad E/T_{\min}=299.
\]

The companion R255B_global_spectral_scale.py, importing the unchanged exact R255 model, independently reconstructs all 63 characteristic polynomials and tests minimal spectral scaling via integer coefficients. It checked all 1,522 reduced rationals s=p/q in the open interval with q<=500: ratio 1 occurs 1,515 times and ratio 13 seven times, with no 23 or 299 occurrence in this bounded sample. It also tested 21 anchor parameters (all ratio 1) and eight special examples covering {1,13,23,299}. Exact code returned PASS and produced verification JSON SHA-256 4c9ace917860f8a1db3219d4048972e50dfa2809a9afb65f59cc5f951409ed4b. The all-rational theorem follows from the proof above rather than the finite data.

## Scope and next question

This is the minimum integral *characteristic scaling*; determining the sharp least common denominator of the **reduced scalar outputs** is a distinct modular-witness problem. R254 settled the latter at s=2/5. All 63 labelled source contributions and future scalar observations are retained, without claiming native signed/port BRC equivalence. P000 and ACTIVE worldview stay fixed. No formal CLAIM, mathematical independent review or canonical acceptance has been established.

Next derive general-s initial moment valuations and modular nonvanishing witnesses for the exact labelled-output denominator; retain the independent continuous-real-parameter two-mode thresholds 270/403 research problem.
