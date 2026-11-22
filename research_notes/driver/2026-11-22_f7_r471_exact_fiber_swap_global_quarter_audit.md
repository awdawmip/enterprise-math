# CBRC F7 r471 — exact fiber-swap oscillation reduction and global audit of the r469 finite-box witness

Date: 2026-11-22 (Asia/Taipei). This new derivation/check belongs to the existing Driver logical lane `EM-DVR-DEBB5E`. The original F7 researcher `EM-CBRCF7-83A1D4`, its model and existing scientific evidence are preserved. This is not a native independent Result review or admission.

## Original model and notation

For $z=(a,b,c,d)\in\mathbb Z^4$, let $k=a-2b-c+2d$ and
$$
D_q(z)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d).
$$
All original admissibility conditions remain: first-coordinate evenness, axis/origin values, nonzero off-axis lower bound, and both fixed marked values. Define $E_B(q)=\max_{z\in[-B,B]^4\cap\mathbb Z^4}|D_q(z)|$ and $E_\infty(q)=\sup_{z\in\mathbb Z^4}|D_q(z)|$ for a fixed function.

## Theorem 1 — exact fiber-swap identity and cubic finite-box evaluator

For any integers $r,t$, define
$$
h_r(t):=q(2r-t,r-t).
$$
The substitution
$$
r=a-b,\quad t=a-2b,\qquad u=c-d,\quad s=c-2d
$$
is a bijection on $\mathbb Z^4$. Since $k=t-s$, the two transformed arguments have fiber coordinates $(r,s)$ and $(u,t)$, respectively. Therefore
$$
\boxed{D_q(z)=h_r(s)+h_u(t)-h_r(t)-h_u(s)
=[h_r(s)-h_u(s)]-[h_r(t)-h_u(t)].}
$$
For **any** real-valued $q$, even if unbounded,
$$
\boxed{E_\infty(q)=\sup_{r,u\in\mathbb Z}
\operatorname{osc}_{t\in\mathbb Z}(h_r(t)-h_u(t)),}
$$
where $\operatorname{osc}f=\sup_{s,t}|f(s)-f(t)|$ may equal $+\infty$.

For a complete finite input box $[-B,B]^4$, define the nonempty integer intervals
$$
I_r(B)=[\max(2r-B,r-B),\,\min(2r+B,r+B)]\cap\mathbb Z,
\qquad -2B\le r\le2B.
$$
Let $f_{r,u}(v)=h_r(v)-h_u(v)$, and write $m_r,M_r$ for its minimum and maximum over $I_r(B)$; likewise $m_u,M_u$ over $I_u(B)$. Then
$$
\boxed{E_B(q)=\max_{r,u:I_r,I_u\ne\varnothing}
\max\{M_u-m_r,\;M_r-m_u\}.}
$$
This is exact: the original first pair selects $t\in I_r$, the second selects $s\in I_u$, and these choices are independent. For each of $O(B^2)$ fiber-label pairs, evaluating both $O(B)$-length intervals suffices. Consequently the fixed-$q$ maximum is computable with $O(B^3)$ exact evaluations and constant-size extrema state, rather than enumerating $O(B^4)$ original inputs. No numerical approximation is used.

## Theorem 2 — the specified r469 quarter-valued witness has exact global error one

Freeze the *existing* r469 1,190-row table at
`enterprise-math@ba281507cfcba49b9fb592c0e7f98b5a4ccd5621:research_artifacts/F7_R469_B14_Exact_Quarter_Witness_20261122.json`,
Git blob `81afd124e5d9faaa877f8cbffd4bdb25a377b10b`.
It defines $4q_*(0,0)=0$, $4q_*(x,0)=4$ for nonzero $x$, and
$4q_*(x,y)=2+n(|x|,y)$ off axis, with $n\in\{1,2\}$ on the table and zero elsewhere.

Exact integer evaluation of the fiber formula gives
$$
\boxed{E_{14}(q_*)=\tfrac12,\quad E_{15}(q_*)=1,\quad
E_{32}(q_*)=1,\quad E_\infty(q_*)=1.}
$$

**Finite reduction for the global supremum.** Each table triple $(|x|,y,n)$ gives both signs $x=\pm |x|$. Record the fiber label $r=x-y$ and its exceptional argument $t=x-2y$. Let $R_0$ contain all these $r$ and $t$, plus zero. It contains exactly 276 integers. Add two distinct generic labels strictly outside its range to form $R$, of size 278.

For $r\notin R_0$ the fiber $4h_r$ takes its default value 2 except for the axis spike $4h_r(r)=4$. Such $r$ cannot coincide with any exceptional $t$ from the table, nor with an axis label or the origin of a special fiber. Hence every pair of arbitrary fiber labels has the same oscillation as a pair in $R\times R$; two generic representatives cover the case of distinct generic labels.

For fixed $(r,u)\in R^2$, the integer function $4h_r(v)-4h_u(v)$ is zero off the finite set consisting of $v=r,u,0$ and the two fibers' table arguments. Evaluating extrema on that set plus one outside default argument is exhaustive. The maximum oscillation over all **77,284 representative pairs** is exactly 4 in the $4q$ scaling. Thus $E_\infty(q_*)=1$.

An explicit maximizer is $z=(40,33,-59,-33)$ with $k=-33$: its transformed arguments $(7,0)$ and $(-26,0)$ each have $q_*=1$, while its two original off-axis arguments are outside the table and each have $q_*=1/2$. Thus $D_{q_*}(z)=1$.

The original independent JavaScript calculation evaluated 95,874 fiber values for $B=14$, 117,242 for $B=15$, and 1,090,050 for $B=32$. The standalone reproducibility program is
`research_checks/CBRC_F7_R471_FIBER_OSCILLATION_20261122.mjs` at commit `09b143759b94dca22d81c98bf1d040f3613b8647`.
It uses the existing table, integer arithmetic and no CI. Its file was published/read back; the stated exact calculations were executed in the live JavaScript computation, not attributed to a separate Node run.

## Theorem 3 — every finite off-axis perturbation of the half-valued baseline has global error at least one

Take any distinct nonzero integers $r,u$ and the original input
$$
z=(2r-u,r-u,\,2u-r,u-r).
$$
Its shear parameter is $k=u-r$, making the transformed pair $(r,0),(u,0)$. Both axis values equal one, giving the **unconditional original-model identity**
$$
\boxed{D_q(z)=2-q(2r-u,r-u)-q(2u-r,u-r).}
$$
Therefore any admissible global candidate with $E_\infty(q)\le\varepsilon$ necessarily satisfies, for **every** distinct nonzero pair $r,u$,
$$
\boxed{2-\varepsilon\le q(2r-u,r-u)+q(2u-r,u-r)
\le2+\varepsilon.}
$$
At least one of the paired off-axis values is $\ge1-\varepsilon/2$. For $\varepsilon=4/7$ at least one is $\ge5/7$; for $\varepsilon=1/2$ at least one is $\ge3/4$.

Choosing $r=N,u=-N$ supplies the escaping ray pair
$$
\boxed{q(3N,2N)+q(-3N,-2N)\ge2-\varepsilon
\quad\text{for every integer }N\ge1.}
$$
If $q=1/2$ at all off-axis coordinates except finitely many, the two left-hand terms equal $1/2$ for sufficiently large $N$, so $E_\infty(q)\ge1$. More quantitatively, achieving $E_\infty(q)\le4/7$ requires at least one point in each escaping pair to exceed the half-baseline by at least $3/14$, at arbitrarily large scales. This is a rigorous global-tail **necessary condition**, not a negation of infinite-tail constructions.

This theorem independently supplies $E_\infty(q_*)\ge1$ for the r469 table; the exact finite-representative audit in Theorem 2 supplies the matching upper bound.

## Boundary and continuation

The r469 witness's error one on the full lattice does not supersede the existing global existence bracket $1/2\le E_\infty^*\le4/7$ (whose upper bound uses a different function). Nor does it resolve the unrestricted $B=15$ finite-box optimum. The new oscillation representation offers a mathematically exact reduced optimization/evaluation route; the tail constraint shows that a global candidate below error one needs genuinely nontrivial off-axis behavior at unbounded scales.

Original scientific ownership, prior r470 relative-repair results and all existing Source/Result/Review states remain unchanged. This derivation has not been canonically admitted as a Native Result or Independent Review.
