# EC49FRG — Six native BRC Bellman seams, 116-node certificate, midpoint and rectangle theorems

Research date: **2026-11-17**. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.
Parent: [EC49FRF PR #2610](https://github.com/awdawmip/enterprise-math/pull/2610) @ `e3633f0d819888a13e430d66828a5f94d2310bf2`. Frozen original scientific source commit `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` remains unchanged. Source master SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`, profile CSV SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

## Problem and exact finite certificates

Native BRC class 16943: 310 original configurations, 141 **complete named** profile states, 228 physical observations (144 terminal and 84 root; physically labeled actions retained in tie reporting). Prior on profile i is `p_i(l)=(1-l)/141+l*m_i/310` for `0<=l<=1`. Root observation price `r=x*t` with `x>=1,t>0`; terminal price `t`. Let `V(x,l)` be the unrestricted minimum expected cost among all finite separating adaptive trees. Three feasible *fixed* trees from the parent have normalized costs:

```
A(x,l)=(1-l)*(6*x+290)/141+l*(6*x+751)/310
B(x,l)=(1-l)*(5*x+293)/141+l*(5*x+704)/310
C(x,l)=(1-l)*(5*x+295)/141+l*(5*x+685)/310
K(x)=7557-169*x
G(x)=310*(3-x)/K(x)
beta=620/3299.
```

Six new critical-price/prior pairs `(x,G(x))` were independently solved with unrestricted integer Bellman and a separately written weighted-subset dynamic program. Each computation checks all 228 physical first actions and all complete tied first-action decision trees. The two implementations return the same four minimizing named first actions `{32,34,140,142}` and exact integer optimum.

| Price x | G(x) | Integer Bellman optimum | SHA256 of full native certificate |
|---|---|---:|---|
| 105/64 | 8990/155301 | 932113535360 | `55822a25acdd11e3fa79f1f59c42280b8f3482ce979b51a6dc1efc9c1beb6173` |
| 103/64 | 27590/466241 | 2797241381760 | `4775ab99e39816c1078f5f20223549b5a604290cbb5d6070e052dc9668c7b0c3` |
| 101/64 | 28210/466579 | 2798142157440 | `cac3cb35d549d247879f6fe242f493e7e7031014a0a0fb7f4c01f16f06fb232e` |
| 99/64 | 9610/155639 | 933014311040 | `f3f11f7c2287a00d48e2fa586163f7538a863541057edf070b9df14aaeea8282` |
| 97/64 | 5890/93451 | 559988741760 | `b5506fb8f45dbdc0cde73ecaf2326d002d21282b48dc3eda273ec21888b9d6dc` |
| 275/96 | 4030/678997 | 6212385506880 | `fa6e116005a8bcaeeb6d3e936542a62f1fd18c15be7446052cfa6ae4dd801443` |

Each integer optimum uses scale `x.denominator*310*141*G(x).denominator` relative to `t`. At each of these six points `V(x,G(x))=t*A(x,G(x))=t*B(x,G(x))`. **Using the inherited EC49FQZ–FRF endpoint and exact named-first-action exclusion lemma**, fixed-tree costs' affine dependence on prior and concavity of the Bellman minimum extend the values and optimal first labels to *all real* `l in [0,1]` for each price: `V=t*min(A,B,C)`; `{32,34}` for `l<G(x)`; `{140,142}` for `G(x)<l<beta`; `{16,23}` for `l>beta`. At either seam, include the adjacent tied label sets. The new critical calculations and tree replays were performed afresh; inherited lemmas remain author-proved and have not been independently project-reviewed.

## New theorem: exact arithmetic-midpoint strip-area halving

For `1<=a<b<=3`, define `D=2185500` and the **enclosing, not observed**, potentially uncertified parameter-strip area

`U(a,b)=(b-a)*(G(a)-G(b))=D*(b-a)^2/[K(a)*K(b)]`.

**Theorem.** For `m=(a+b)/2`, one has the exact identity

`U(a,m)+U(m,b)=U(a,b)/2`.

**Proof.** Set `u=K(a)`, `v=K(b)`, `h=b-a`. Since K is affine, `K(m)=(u+v)/2`. Therefore

```
U(a,m)+U(m,b)
 = D*h^2/(4*K(m))*(1/u+1/v)
 = D*h^2/(4*((u+v)/2))*((u+v)/(u*v))
 = D*h^2/(2*u*v)
 = U(a,b)/2.
```

The six additional certified rational prices were the arithmetic midpoints of the currently largest `K(a)/K(b)` interval, repeated six times, in exact order:

```
[13/8,53/32]  -> 105/64
[51/32,13/8]  -> 103/64
[25/16,51/32] -> 101/64
[49/32,25/16] -> 99/64
[3/2,49/32]   -> 97/64
[137/48,23/8] -> 275/96.
```

This scheme is a rational dyadic construction; the exact continuous-grid optimizer in EC49FRD/FRF uses generally irrational equal-log-K positions.

## Certified 116-node enclosure

Under the inherited endpoint-to-interval bound, the 110 old plus six new certified nodes leave **115 parameter strips**. Set `S(P)=sum U(a,b)` over adjacent nodes. Exact rational verification gives

```
S110 = 259924479610030238135/162277343928838082317536
S116 = 353039202146480393615/236644210143071463572064
S110-S116 = 19144978000085375/174245733138392004168
1-S116/2 = 472935381083996446750513/473288420286142927144128
            = 99.92540717519920764...% of [1,3] x [0,1].
```

The inherited price-interval gap enclosure is
`R(a,b)/t=50*(b-a)/(sqrt(K(a))+sqrt(K(b)))^2`.
All 115 interval bounds have been rigorously compared by `10^-40` outward rational square-root enclosures using integer `isqrt`. The **unique largest** is now `[17/6,137/48]`, and its value is

`Rmax/t = 0.00003680069536649680020154...`

(previous bound `0.0000536592398468369543033...`, an improvement of approximately **31.4178%**). Under the inherited outside-[1,3] certificate, this yields for `x>=1`, `0<=l<=1`:

`0<=t*min(A,B,C)-V(x,l) < 0.000036800695366496801*t`.

This is a rigorous upper bound, **not** an equality statement about actual strategy regret. The area identities are exact; the decimal regret bound is rounded upward.

## New lemma: four-corner bilinear Bellman inheritance

For any *fixed* fully separating adaptive tree T, let `n_i^r(T)`, `n_i^t(T)` be its two observation counts on each named profile i. Its normalized cost is

`F_T(x,l)=sum_i p_i(l)*(x*n_i^r(T)+n_i^t(T))`.

For any competitor Q, the difference `F_Q-F_T` is bilinear in `(x,l)`. If T is independently verified Bellman-optimal at all four corners of a rectangle `[a,b] x [c,d]`, then it is Bellman-optimal at every point in that rectangle: any competitor's nonnegative corner gaps bilinearly interpolate with the four nonnegative weights `(1-s)(1-u),s(1-u),(1-s)u,su`, where `s=(x-a)/(b-a)` and `u=(l-c)/(d-c)`.

For the policy seam `l=G(x)`, each fixed competitor Q gives a bilinear gap `F_Q-F_A=(p+q*x)+(s+h*x)*l`. Multiplication by positive `K(x)` gives a quadratic polynomial

`N_Q(x)=K(x)*(p+q*x)+310*(3-x)*(s+h*x)`.

For a **specified** tree Q, its exact nonnegativity over a price interval is decided by endpoints and an interior vertex when the quadratic opens upwards. This provides a target for a future parameterized Bellman certificate; the full set of competing adaptive trees has not yet been discharged by this lemma.

## Reproduction and continuation

The full self-contained EC49FRG evidence bundle contains six original native JSON certificates; `EC49FRG_INDEPENDENT_VERIFY.py` plus its separate BRC loader and two exact pass logs; `EC49FRG_GEOMETRY.py`, nodes JSON, geometry results and full source; inherited EC49FRF evidence; and a per-file SHA256+size manifest. The prior native solver `EC49FQL_ALL_FIRST_BELLMAN.py` is included. Use exact rational/integer operations throughout. See the repository companion checker and certificate index; full raw machine evidence is in the linked evidence archive.

**Next unresolved scientific question:** For the 115 remaining parameter strips, either prove `V=t*min(A,B,C)` by a parameterized full Bellman lower bound, or find a strict action-labeled counterexample tree. Four-corner inheritance covers same-tree rectangles; quadratic seam checks and a compact Bellman policy certificate may handle the variable-switch boundary.

**Control/authority:** GitHub research preservation only; the exact `research_task_records/RS-EC49AS` canonical directory was 404 on `main` during the run. No formal CLAIM/Result/Review or current owner identity is asserted.