# Stage356-B — Exact central r0=0 Pareto arc exclusion

Research date: 2026-11-01 Asia/Shanghai. Author: continued research2 portable author. Classification: PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is a theorem in an **external** source-labeled Bernoulli observer, not a native P000/X6 or Heartbeat/BRC–Shor computation.

## Frozen sources, authority and provenance

GLOBAL_KNOWLEDGE_V1 canonical main: 301e34842658e23e49724e5dd846a9952258ba50, with both normative entrypoints, task researcher routing, active worldview and mathematical/BRC/journal policies read. Enterprise Math canonical main: 96dbd541e2c8f4f873aaf4ee37a42cf6af0f3278, including actual P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488, native X6/time, joint-observer preservation, current portable and autonomous research protocols. Prior research2 author frontier: Stage355-B at fc0bc5ab283798e3fb520e276b5c66c154eb9550. Its 67/73/37-leaf certificates are not premises of this proof. Native em_status v0.6.11: research_authority_granted=false; bounded owner query: CONTROL_QUOTA. Git provenance confers neither a formal CLAIM nor mathematical acceptance.

## Exact model

For 0<=x,y<=1, let weights w=(1,3,3,1), masses m=(61,21,9,9), cubic Bernstein components B_k(z)=z^k(1-z)^(3-k). All four labeled residuals are retained:

r_k(x,y)=(4 B_k(x)+B_k(y))/5 - m_k/160.

b(x,y)=(5/32) sum_{k=0}^3 w_k |r_k(x,y)|.

D_3(a,z)=(1/2) sum_{k=0}^3 w_k |B_k(a)-B_k(z)|.

c(x,y)=[63 D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)]/256.

For two sources, T(q1,q2)=33/1024+c(q1)+c(q2) with budget b(q1)+b(q2)<=2 beta_*+E. The 16 subset comparisons in the total-variation dual preserve the original source labels; our sign-chamber formulas use that exact identity.

Define q_*=(x_*,y_*) to be the unique selected algebraic intersection r0=r1=0 inside the rational isolating box given below, beta_*=b(q_*). There is no assumption that q_* is globally optimal.

## Theorem (strict domination except at q_*)

For **every real** q=(x,y) with r0(q)=0 and 229/1000<=x<=233/1000, if q != q_*, another q' inside [0,1]^2 strictly reduces BOTH b and c.

More explicitly: if x<x_*, then q'=q_* strictly dominates. If x>x_*, all sufficiently small **positive rational** delta yield the strict dominator q'=(x+delta,y+37 delta).

Hence for **any upper two-source budget limit** (no E restriction), a global optimum cannot contain a source in this closed central r0=0 arc except possibly q_*. The argument does not use Stage355's global b floor or the unreviewed Stage336/342/346/352 lemmas.

## Exact algebraic geometry and signs

Let s=1-x, t=1-y. The r0 equation reads

4s^3+t^3=61/32. (1)

For x in [229/1000,233/1000] there is exactly one y(x), and 533/1000<y(x)<590/1000, because F(x,y)=4(1-x)^3+(1-y)^3-61/32 is strictly decreasing in each coordinate, F(229/1000,590/1000)<0 and F(233/1000,533/1000)>0, with the complementary sign checks also strictly valid. Thus 767/1000<=s<=771/1000 and 410/1000<t<467/1000, with

dt/dx=4s^2/t^2>0, dy/dx=-4s^2/t^2<0. (2)

On the full enclosing rational rectangle the following hold (each corner inequality is checked exactly by the accompanying Fraction code):

r2>=r2(229/1000,533/1000)=13147607/5000000000>0,
r3<=r3(233/1000,590/1000)=-6318413/1250000000<0,
s>t,
4st-(s+t)>=4(767/1000)(410/1000)-(771/1000+467/1000)=497/25000>0. (3)

The r2 monotonic corner inequality uses monotonic increase of z^2(1-z) for z<2/3; the r3 bound is from monotonicity of z^3.

Write A=4s^2+t^2 and L=4s+t. On r0=0, exact Bernstein polynomial expansion gives

r1=(A-41/16)/5, r2=(L-2A+13/8)/5. (4)

Differentiating along (1), with t'=4s^2/t^2, gives

r1'=8s(s-t)/(5t)>0,
r2'=4(s-t)(s+t-4st)/(5t^2)<0. (5)

Selected root isolator:

P(s)=(41/16-4s^2)^3-(61/32-4s^3)^2,

P(0.768916059144)<0<P(0.768916059145).

In this box 41/16-4s^2>0 and 61/32-4s^3>0, so the squared relation is reversible with positive t. The function f(s)=4s^3+(41/16-4s^2)^(3/2) has derivative 12s(s-t)>0 on the isolator. Therefore exactly one selected r0=r1 intersection exists. Exact square-rational bounds yield

0.231083940855<x_*<0.231083940856,
0.555508857273<y_*<0.555508857281. (6)

Since r1' is positive, r1<0 for x<x_*, r1>0 for x>x_*. r0=0, r2>0, r3<0 throughout.

## Left arc: q_* strictly dominates

On x<x_* the weighted residual signs are (0,-,+,-). Since sum w_k r_k=0, the sourcewise TV positive-mass formula gives

b=(15/16)r2,

which strictly decreases as x increases to x_* by (5).

For c, the four original independently weighted D_3 channels are retained. Their sign chambers for 229/1000<=x<=233/1000 give

c_x=-[189(1-x)^2+6x(1-x)]/256<0. (7)

For y in (533/1000,590/1000), D_3(1/4,y) has positive labels 0,1; D_3(3/4,y) always has positive label 3 and may also have positive label 2. Consequently the two possible one-sided derivatives in y are

c_y=12y(1-y)/256 > 0, or
c_y=(54y-75y^2)/256 > 0 (as y<590/1000<18/25). (8)

At the one possible label switch both one-sided derivatives remain positive. Together with y'(x)<0, (7)-(8) show c(x,y(x)) strictly decreases along the full continuous arc. Thus q_* has strictly smaller b and c than every x<x_* point.

## Right arc: exact rational tangent strict domination

If x>x_*, signs on r0=0 are (0,+,+,-), while 533/1000<y<560/1000 by (6) and y'(x)<0. Under perturbation (x,y)->(x+delta,y+37delta), for sufficiently small delta>0: r0 becomes negative, r1,r2 stay positive, r3 stays negative, and every D_3 source channel retains its right-arc sign pattern. On this chamber the **exact** loss is

b=(15/16)(r1+r2)=(3/16)[4x(1-x)+y(1-y)-15/16]. (9)

Hence at delta=0+

db/d(delta)=(3/16)[4(1-2x)+37(1-2y)]
 <=-411/8000<0. (10)

In the right-arc audit chamber c_y=12y(1-y)/256 and c_x is (7), so

dc/d(delta)= [-189(1-x)^2-6x(1-x)+12*37*y(1-y)]/256
 <= -186621/256000000 < 0, (11)

using x<=233/1000 and y(1-y)<=1/4. Both inequalities are **uniform strict rational margins**. The functions are analytic in this open chamber; by continuity every point in the real right subarc admits sufficiently small rational delta satisfying both strict improvements, with perturbation remaining inside [0,1]^2. This proves the theorem and all-budget corollary.

## Exact validation, limits, next

Run python REPRO_STAGE356B.py; it uses only fractions.Fraction and assertions, no floating point in proof tests. It verifies rational arc corners, exact algebraic sign isolator, all sign chambers, strict derivative margins, and one raw source-labeled TV sign-chamber identity; the universal real quantifier follows from the analytic monotonicity argument above, not from finite sampling. Actual two identical successful runs are in REPRO_STAGE356B_EXECUTED_STDOUT.txt. The author-side checker does not confer formal proof admission.

Only the central r0=0 section is excluded, except q_*. Outer r0=0 components, all off-boundary residual chambers, and true post-cusp global minimizers remain unresolved. Native P000 X6, third slice coordinate, triadic closure, separately typed time, registered Cell codec and observer/future-operation preserving transfer remain separate proof obligations.

Stage357-B: isolate outer feasible r0=0 components with b<=299/50000 by exact algebraic/Bernstein bounds and determine precise dominance maps, or construct a strict rational/algebraic competitor. Preserve the 16 source comparisons; reuse prior stages without replacing the provenance or claiming official CLAIM/Result.