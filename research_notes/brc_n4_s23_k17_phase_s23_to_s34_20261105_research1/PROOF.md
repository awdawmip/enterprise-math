# BRC S23 N=4, K=17: exact phase 2/3 <= s <= 3/4

Date: 2026-11-05 Asia/Shanghai. Independent author-side analytic proof with exact-rational executable evidence. Source model: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Continuation: PR #1765 prior artifact commit a32d626ebacbd28f4fba7fe5ca7da877ae4b2556. Review: UNREVIEWED / NOT_ADMITTED. Activity RA-E8214A2B9646E03D3EC300CC (no claim authority).

## Setup

Let a=11/21, b=10/21. The complete T observation retains the three labels, P_T=(as,1-s,bs) and Q_T=(bs,1-s,as); the typed Bernoulli projection B is P_B=(as,1-as), Q_B=(bs,1-bs). For 0<=t<=1 define

- f_T(t,s)=-ln[1-s+s(a^t b^(1-t)+b^t a^(1-t))].
- f_B(t,s)=-ln[(as)^t(bs)^(1-t)+(1-as)^t(1-bs)^(1-t)].
- F(m,n;s)=max_{0<=t<=1}(m f_T(t,s)+n f_B(t,s)).
- C_T(s)=F(1,0;s); C_B(s)=F(0,1;s); H(s)=f_B(1/2,s).

The t of mixed observations is shared; the integer counts m,n>=0 obey (2-s)m+n<=17. This is a two-observer restricted sampling model; its comparison retains the original separate T/B provenance and does not identify the B projection with the complete observation.

## Theorem (five unique phase crossings, plus the right boundary)

Let (l_i,r_i,m_i,n_i) for i=1,...,5 be

1. (2/3, 9/13, 12, 1)
2. (9/13, 7/10, 13, 0)
3. (7/10, 5/7, 10, 4)
4. (5/7, 8/11, 7, 8)
5. (8/11, 3/4, 11, 3).

For each i there exists exactly one real s_i in (l_i,l_i+1/1000) such that F(m_i,n_i;s_i)=17C_B(s_i). The global maximizing integer design is uniquely (m_i,n_i) on [l_i,s_i), exactly (m_i,n_i) and (0,17) at s_i, and uniquely (0,17) on (s_i,r_i). At s=3/4 the unique global maximizing design is (12,2).

## Proof 1: exact integer feasibility and hull

For 2/3<=s<=3/4, 14(2-s)>=17.5>17, so 0<=m<=13. Given m, strict information gain from adding a B observation selects n_m=17-2m+floor(ms), whenever this is >=0. All rationals k/m in [2/3,3/4] for 1<=m<=13 are exactly

{2/3, 9/13, 7/10, 5/7, 8/11, 3/4}.

The upper convex hull vertices of all (m,n_m), in order of the five half-open cells, are respectively

- [(0,17),(12,1)];
- [(0,17),(13,0)];
- [(0,17),(10,4),(13,0)];
- [(0,17),(7,8),(13,0)];
- [(0,17),(11,3),(13,0)].

At s=3/4 the vertices are [(0,17),(12,2),(13,0)]. VERIFY.py performs exact complete rational enumeration at each left endpoint and each cell interior. The function F is a maximum of linear functions of counts, hence convex in counts, so a maximum occurs on a hull vertex. Any non-vertex ties are excluded strictly: the optimal t for T alone is 1/2, while f_B'(1/2,s)>0 throughout the specified regime (the Bernoulli tilt is on the other side). Two noncollinear count vectors cannot have the same stationary maximizer unless f_T' and f_B' both vanish, which cannot occur. Upper-hull strict interpolation therefore cannot attain a tied vertex maximum.

The first two cells already have two vertices. On the last three cells the possible extra vertex (13,0) is excluded by the strictly positive inequality 17C_B(s)-13C_T(s)>0 on [7/10,3/4]. The latter is certified by four left-value and four convex-slope certificates in VERIFY.py. Thus the only global candidates in each open cell are (0,17) and the corresponding (m_i,n_i).

## Proof 2: strict monotonicity on continuous real cells

For each fixed t, f_T(t,s) is convex in s because its logarithm argument is affine and -ln is convex decreasing. For f_B(t,s), the Bernoulli Chernoff coefficient is a sum of a linear term and a weighted geometric mean of two affine positive terms, hence concave; composing with -ln yields convexity. Consequently F(m,n;s), C_T(s), C_B(s) are convex in s.

Put G_i(s)=F(m_i,n_i;s)-17C_B(s). For each of 12 rational subcells [x,y] of a cell [l_i,r_i], let delta=1/10000 and define

L=[C_B(x)-C_B(x-delta)]/delta,
U=[m_i C_T(y+delta)+n_i C_B(y+delta)-m_i C_T(y)-n_i H(y)]/delta.

Since m C_T+n H <= F(m,n) <= m C_T+n C_B, convex secants give, for any x<=u<v<=y,

(G_i(v)-G_i(u))/(v-u) <= U-17L.

All 60 rational interval checks prove 17L-U>0. Therefore each G_i is strictly decreasing throughout its cell. For every left endpoint l_i, a strict rational lower bound verifies
m_i C_T(l_i)+n_i H(l_i)>17C_B(l_i),
while at l_i+1/1000 a strict upper bound verifies
m_i C_T(l_i+1/1000)+n_i C_B(l_i+1/1000)<17C_B(l_i+1/1000).
This yields exactly one zero in each stated open rational interval and the full piecewise strategy classification.

At s=3/4, the strict rational inequalities
12C_T+2H>17C_B and 12C_T+2H>13C_T
select the (12,2) hull vertex over the other two vertices. The same strict hull argument excludes other maximizing designs.

## Computer-assisted exactness and status

VERIFY.py uses Fraction, isqrt, outward 10^-48 square-root enclosures, a 34-term artanh logarithm series with proved geometric remainder, and a rigorous Bernoulli tilt interval rho=J/(H0+J) where H0=ln(a/b) and J=ln((1-bs)/(1-as)). The 60 strict monotonicity, 10 endpoint, 8 extra-vertex elimination, and two boundary comparisons yield 80 strictly positive rational certificates, plus exact hull enumeration. RUN_EVIDENCE.txt records the actual local execution output of an arithmetically equivalent checker for the same model, test cases and 80 inequalities. The published VERIFY.py shares the exact certificate routines with the previous pinned artifact; formatting varies from the local runner.

This theorem solves the declared K=17 auxiliary sampling phase. The separate ten-label S23 minimax target remains on the previously recorded [1/2,2/3] bracket. Native claim, Result and independent mathematics review remain pending.
