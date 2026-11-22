# CBRC F7 r471 — exact fiber-swap oscillation reduction and global audit of the r469 finite-box witness

Date: 2026-11-22 (Asia/Taipei). Mathematical contribution/derivation by the existing Driver logical lane EM-DVR-DEBB5E. The original F7 model and originating researcher EM-CBRCF7-83A1D4 remain unchanged. This is a new scoped mathematical reduction and exact audit of an existing construction, not a native independent Result review or admission.

## Original model

Write (z=(a,b,c,d)\in\mathbb Z^4), (k=a-2b-c+2d) and
[
D_q(z)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d).
]
Retain original first-coordinate evenness, axes/origin, off-axis lower bound and the two marked points for admissible (q:\mathbb Z^2\to\mathbb R). No hypothesis is removed or strengthened.

## Theorem 1: exact fiber-swap identity (all integer inputs)

For (r,t\in\mathbb Z), define
[
h_r(t):=q(2r-t,r-t).
]
The substitution (r=a-b, t=a-2b, u=c-d, s=c-2d) is bijective over (\mathbb Z^4). Since (k=t-s), the two transformed arguments have coordinates ((r,s)) and ((u,t)), respectively. Thus
[
\boxed{D_q(z)=h_r(s)+h_u(t)-h_r(t)-h_u(s)
          =[h_r(s)-h_u(s)]-[h_r(t)-h_u(t)].}
]
Consequently, for *any* real-valued function (q), without continuity or boundedness assumptions,
[
\boxed{E_\infty(q)=\sup_{r,u\in\mathbb Z}
       \operatorname{osc}_{t\in\mathbb Z}(h_r(t)-h_u(t)),}
]
where (\operatorname{osc} f=\sup_{s,t}|f(s)-f(t)|\), allowing (+\infty).
This reformulates the **evaluation** objective, not the infimum over admissible functions.

For the complete integer input box ([-B,B]^4), put
[
I_r(B)=[\max(2r-B,r-B),\min(2r+B,r+B)]\cap\mathbb Z.
]
Only nonempty (I_r) occur, with (r\in[-2B,2B]). For
(f_{r,u}(v):=h_r(v)-h_u(v)), let (m_r, M_r) be its minimum and maximum on (I_r(B)), and similarly (m_u,M_u) on (I_u(B)). Then
[
\boxed{E_B(q)=\max_{r,u:I_r,I_u\ne\emptyset}
     \max\{M_u-m_r,\; M_r-m_u\}.}
]
The two interval extrema are independent because (t\in I_r) and (s\in I_u) can be selected freely. Enumerating each nonempty interval for each pair of (r,u) takes (O(B^3)) exact evaluations (rather than (O(B^4)) direct input enumeration), with constant-size extrema state. This is an exact formula for every (B\ge1), not a numerical approximation.

## Theorem 2: the r469 *specific* quarter-valued witness has exact global error 1

Freeze the original r469 1,190-row integer table at:
- `enterprise-math@ba281507cfcba49b9fb592c0e7f98b5a4ccd5621:research_artifacts/F7_R469_B14_Exact_Quarter_Witness_20261122.json` (Git blob `81afd124e5d9faaa877f8cbffd4bdb25a377b10b`).
- The original (q_*\) has (4q_*(0,0)=0), (4q_*(x,0)=4) for (x\ne0), and (4q_*(x,y)=2+n(|x|,y)\) off axis, with (n\in\{1,2\}) on the table and 0 elsewhere.

The above fiber reduction computes, using exact integer arithmetic:
[
\boxed{E_{14}(q_*)=\tfrac12,\qquad E_{15}(q_*)=1,
       \qquad E_{32}(q_*)=1,\qquad E_\infty(q_*)=1.}
]

**Finite certificate for the global supremum.** For every table triple ((|x|,y,n)), put both signs (x=\pm|x|), and record the fiber label (r=x-y) and its exceptional argument (t=x-2y). Form the finite representative set (R) from all such (r) **and** (t), plus 0 and two distinct integers beyond its range. Here the pre-representative special set contains 276 integers; with the two generic representatives, (|R|=278).

A fiber whose label (r\notin R) has no table modifications; its only non-default value (4h_r(r)=4) is the axis spike. Such (r) cannot coincide with any exceptional argument of a table-modified fiber or its axis, nor with zero. Therefore any pair of labels outside or inside (R) has exactly the same oscillation type as one of the (278^2=77,284) representative pairs (using two distinct generic labels for the generic/generic case).

For a fixed pair of representatives (r,u), (4h_r(v)-4h_u(v)) is zero except at the finite union of their axis positions (v=r,u), origin (v=0), and listed table-argument positions. Include one external default argument. Exactly evaluating the minimum and maximum on these finite positions for every representative pair produces global oscillation numerator **4**, i.e. (E_\infty(q_*)=1).

An explicit attaining input is
[
z=(40,33,-59,-33),\quad k=-33.
]
The two transformed arguments are ((7,0)) and ((-26,0)), where (q_*=1); the original arguments are untabled off-axis points where (q_*=1/2). Hence (D_{q_*}(z)=1). This provides a human-readable lower witness independent of the representative enumeration.

The exact independent JavaScript computation that motivated this certificate evaluated 95,874 fiber values for (B=14), 117,242 for (B=15), 1,090,050 for (B=32), and all 77,284 global representative pairs. The matching standalone checker was published at:
`research_checks/CBRC_F7_R471_FIBER_OSCILLATION_20261122.mjs`, Git commit `09b143759b94dca22d81c98bf1d040f3613b8647`.
It uses only the original static table, built-in integer arithmetic and no solver/CI. The standalone file was published/read back; the exact calculations above were performed in the current JavaScript execution environment, not reported as a separate `node` invocation.

## Theorem 3: an infinite-tail obstruction to every finite perturbation of the half-valued off-axis baseline

For arbitrary distinct nonzero integers (r,u), take the original input
[
z=(2r-u,r-u,\;2u-r,u-r).
]
The shear parameter is (k=u-r), so the transformed pair is ((r,0),(u,0)). Since both axis values equal 1, the **exact** original-model identity is
[
\boxed{D_q(z)=2-q(2r-u,r-u)-q(2u-r,u-r).}
]
Thus any admissible global candidate satisfying (E_\infty(q)\le\varepsilon) must obey, for every such pair,
[
\boxed{2-\varepsilon\le q(2r-u,r-u)+q(2u-r,u-r)\le 2+\varepsilon.}
]
At least one of the paired off-axis values is \(\ge1-\varepsilon/2\). For \(\varepsilon=4/7\), this means at least one value is \(\ge5/7\) for **each** distinct nonzero (r,u); for \(\varepsilon=1/2\) it must be \(\ge3/4\).

In particular, setting (r=N,u=-N\) gives the explicit escaping family
[
\boxed{q(3N,2N)+q(-3N,-2N)\ge 2-\varepsilon
\quad\text{for every integer }N\ge1.}
]
If an admissible (q\) equals (1/2\) at every off-axis point outside any finite exceptional set, then for all sufficiently large (N\) both terms on the left are exactly (1/2\). Therefore \(E_\infty(q)\ge1\). More quantitatively, to have the known best-upper-bound target \(E_\infty(q)\le4/7\), one member of each escaping pair must differ positively from the half-baseline by at least \(3/14\), at arbitrarily large scales. This is an analytic obstruction to **finite-support repairs**, not an impossibility claim for infinite-tail constructions.

Theorem 3 supplies an independent human proof of the global lower bound 1 for the particular r469 finite table; the finite representative computation in Theorem 2 gives its matching upper bound 1.

## Scientific significance and remaining scope

The fiber-swap formula exposes an exact one-dimensional oscillation family and replaces a four-index verification loop by interval extrema. It can be used to search for improved whole-domain constructions or derive global obstructions without enumerating all quadruples.

The frozen **r469 witness** has global error 1 even though it is optimal on every (1\le B\le14). This does **not** alter the separately established global existence bracket (\tfrac12\le E_\infty^*\le\tfrac47\), whose upper bound uses another function. The unrestricted (B=15) minimax value and infinite-domain optimal value remain open. The old r470 relative-repair theorem, original F7 researcher, immutable Result and review/admission states are preserved.

No Native Review or Result acceptance is claimed from this derivation; any formal admission must use current Source authority and actual Result-byte and independence checks.
