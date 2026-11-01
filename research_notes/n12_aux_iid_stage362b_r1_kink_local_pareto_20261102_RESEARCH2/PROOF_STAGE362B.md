# Stage362-B — Central r1=0 kink: exact Pareto dichotomy

Research date: 2026-11-02 Asia/Shanghai. Author-side portable research2 result, Draft PR #1736; exact analytic proof with rational-symbolic checker. Scientific pins remain GLOBAL_KNOWLEDGE_V1 bf84bd7c61a2444b59b1da96be57df0e9ae47e53, Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419 and previously frozen auxiliary P000 V4. Current rules separately read from global main 7ed24544f46a91148bf1dffae22abb981488904d, EM main c32183948b0894d26a715ab8a4f7358bfb5b9ec0 (current P000 V5 ACTIVE_LOCKED). The auxiliary 16-outcome Bernoulli/BRC object remains external to native X6.

## 1. Exact observer and theorem

Let B_k(z)=z^k(1-z)^(3-k), k=0,1,2,3; w=(1,3,3,1) and m=(61,21,9,9). Preserve all four source-labeled residuals, four independent audit ports and the original 16 provenance comparisons:

r_k(x,y)=(4 B_k(x)+B_k(y))/5-m_k/160;
b(x,y)=(5/32) sum_{k=0}^3 w_k |r_k(x,y)|;
D_3(a,z)=(1/2) sum_{k=0}^3 w_k |B_k(a)-B_k(z)|;
c(x,y)=(63 D_3(1/4,x)+D_3(3/4,x)+9 D_3(1/4,y)+7 D_3(3/4,y))/256.

For real (x,y) in R=[229/1000,233/1000] × [27/50,14/25] satisfying r_1=0:

**(A) Positive r0:** If r0>0, an explicit rational Q in [0,1]^2 has b(Q)<b(x,y) and c(Q)<c(x,y), with strict improvements greater than 7 delta/200 and 39 delta/100.

**(B) Negative r0:** If r0<0, the point is *strictly locally Pareto efficient*: there exists epsilon>0 such that each distinct real p in the epsilon-neighborhood increases at least one of b and c. In fact every nonzero tangent vector v satisfies b'(q;v)>0 or c'(q;v)>0. This local result leaves finite-distance and two-source global competition open.

**(C) Algebraic junction:** r0=r1=0 is separately preserved as q*, rather than being removed by this theorem.

Both strict-sign sides are nonempty. Exact bisection at x=23/100 gives a unique r1=0 ordinate with r0>0, while x=29/125 gives one with r0<0.

## 2. Shared strict signs, label preservation and derivatives

Identity sum_k w_k r_k=0 follows from the cubic Bernstein partition of unity and sum_k w_k m_k=160. Cubic Bernstein monotonicity yields r2>=3653511/1250000000>0 and r3<=-13759163/1250000000<0 throughout R.

The four comparison-sign vectors for the 63,1,9,7 weighted audit ports, in that order, are (-,+,+,+), (-,-,+,+), (+,+,-,-), (-,-,+,+). They stay fixed on I=[229/1000,234/1000] × J=[27/50,561/1000] (exact anchor-endpoint checks and B_k monotonicity). Therefore
c_x=-3(1-x)(63-61x)/256 < -2/5,
c_y=3y(1-y)/64 > 0.
All reductions retain the source-labeled total-variation identity; no branch or port collapse is assumed.

## 3. Constructive rational Pareto domination at r1=0, r0>0

Take any integer N>max(1000,24/(5r0(q))) and delta=1/N. Because r1_x=4(1-x)(1-3x)/5>0 on I, moving from q=(x,y) to p'=(x+delta,y) enters the (+++-) open cell. Because |r0_x|<=12/5, the selected delta preserves r0>0 throughout the path; r2>0, r3<0 and all audit signs persist.

Within (+++-), b=-(5/16)r3 by exact signed-mass conservation. Hence db/dx=-3x^2/4<-39/1000; dc/dx<-2/5. The real intermediate point p' improves both b,c by at least the corresponding strict derivative margin times delta.

Choose an integer M>1000/delta and define rational
Q=( floor[M(x+delta)]/M, floor[My]/M ).
Throughout [0,1]^2 both objectives have coordinatewise Lipschitz constants L_x<=3, L_y<=3/4, using |B'_k|<=3, weight sum 8 and all four port coefficients. Rounding therefore changes either objective by <(15/4)/M <3 delta/800. Consequently

b(q)-b(Q)>(39/1000-3/800)delta>7delta/200;
c(q)-c(Q)>(2/5-3/800)delta>39delta/100.

Thus this kink side is strictly replaceable in any two-source additive upper-budget feasible pair.

## 4. Strict local Pareto obstruction at r1=0, r0<0

Here r0<0, r2>0, r3<0 in a neighborhood; preserving all masses yields the exact local identity

b=(15/16)[r2+max(r1,0)].

Its directional derivative is b'(q;v)=max(G_minus·v,G_plus·v), with

G_minus=(3x(2-3x)/4, 3y(2-3y)/16),
G_plus=(3(1-2x)/4, 3(1-2y)/16).
Let H=-grad c=(-c_x,-c_y). Throughout R, G_minus has two positive components; G_plus has positive x and negative y; H_x>2/5 and H_y<0. Therefore D1=det(G_minus,H)<0 and D3=det(G_minus,G_plus)<0.

The remaining determinant has the **global rational strict upper bound**

D2=det(H,G_plus)=(-c_x)(G_plus,y)+c_y(G_plus,x)
< -(2/5)(3/200)+(3/256)(813/2000)
= -633/512000 <0,

using -G_plus,y>=3/200, G_plus,x<=813/2000 and c_y<=3/256. Consequently Cramer's rule gives positive a=D2/D3>0 and d=D1/D3>0 such that

H=a G_minus+d G_plus.

If some nonzero vector v made b'(q;v)<=0 and c'(q;v)<=0, then both G vectors dotted with v are <=0 but H·v=-c'(q;v)>=0. Their strictly positive combination forces both dot products to be zero; the nonzero D3 would then force v=0, contradiction. Hence every nonzero v has b'(q;v)>0 or c'(q;v)>0.

The positively homogeneous continuous function v -> max(b'(q;v),c'(q;v)) has positive minimum eta on the unit circle. The underlying expressions are smooth polynomials except for max(r1,0), which has a uniform piecewise-linear expansion plus O(||h||^2). Thus near q,

max(b(q+h)-b(q),c(q+h)-c(q)) >= eta||h||-C||h||^2 >0

for all sufficiently small nonzero h. This proves the stated **strict local** Pareto efficiency; it does not claim global Pareto optimality.

## 5. Independent algebraic audit of Stage356-B r0=0 central arc

Using s=1-x, t=1-y and the exact r0 equation 4s^3+t^3=61/32, derive
r1=(4s^2+t^2-41/16)/5;
r2=(4s+t-2(4s^2+t^2)+13/8)/5;
dt/dx=4s^2/t^2;
dr1/dx=8s(s-t)/(5t)>0;
dr2/dx=4(s-t)(s+t-4st)/(5t^2)<0
on the Stage356-B enclosing arc.

The selected algebraic root isolator
P(s)=(41/16-4s^2)^3-(61/32-4s^3)^2
changes sign between 0.768916059144 and 0.768916059145 (with the positive unsquared branch retained). The right-arc direction (1,37) has exact error derivative <= -411/8000 and audit derivative <= -186621/256000000. These formulas and inequalities were recomputed, not imported as assumptions. This is an author-side independent *algebra check*; canonical mathematical review/admission has not occurred.

## 6. Evidence, model scope and next frontier

The companion SymPy/standard Fraction checker proves rational polynomial identities, exact endpoint inequalities and rational root sign isolations. It was executed twice with byte-identical stdout. The analytic proof in sections 2–4 supplies the universal real quantifiers and the local compactness argument; finite sample checks alone would not.

Sources: Stage361-B parent at Git commit d7bd6def07514b8537a707db2207a0d8c7f36f41; Stage356-B parent at f9fb3fb816998c5d7d00ca8af355b8a69417e639. Status: PORTABLE_AUTHOR_THEOREM / EXACT_SYMBOLIC_EXECUTED / UNREVIEWED / NOT_ADMITTED / NATIVE_OWNER_UNCONFIRMED.

Next Stage363-B: parameterize the surviving r1=0,r0<0 arc, prove exact second-order trade-off or produce a strict rational two-source finite-distance counterexample to the Stage353-B post-cusp restricted split. Keep a separate bridge obligation to P000 native X6, genuine 3D slice, independent time, triadic closure, observer/future-operation scope and registered Cell address.
