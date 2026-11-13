# R5 — Exact improved two-certificate tube along the lawful 7→3 Blackwell bridge

Date: 2026-11-10 (Asia/Shanghai). Evidence class: **author-side exact rational derivation**. Source-lift/polygon and original dual validity are inherited from immutable author-side evidence, pending independent mathematical review and any formal Source Result admission.

## Object and frozen science

This is the seven-likelihood-ratio **auxiliary statistical** P/Q–BRC Blackwell observer (30 allowed nonnegative arcs, original 21 marginal/martingale equations, 5 affine physical equalities and 26 affine capacity inequalities). Neither P000's native six-dimensional spatial geometry nor its time/physical semantics is changed.

Frozen scientific source commits: Global Knowledge `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`.

Exact predecessor dependencies:
- [PR #1976](https://github.com/awdawmip/enterprise-math/pull/1976), immutable `b9d0da58b74a18fe45f4b29bb238b70df79b96bc`: the lawful closed five-vertex seven-edge polygon `P7`, its six forcing duals, the seventh linear annihilator, and their uniform positive margins.
- [PR #1986](https://github.com/awdawmip/enterprise-math/pull/1986), immutable `590b50e71a58632b02c5fb930f9a5c8b1c1219f5`: the exact `15×8` physical right-hand-side Jacobian `T` and seven dual norm values.
- [PR #1990](https://github.com/awdawmip/enterprise-math/pull/1990), immutable `08ae691eaa7406c0f17a963294565e4f0f32f6f2`: the lawful convex bridge between any `p7∈P7` and `p3(v)=(x3(v),x3(v))`, where `x3(v)=(1,1,1,27/80,v,27/80,1/10)` and `1/10≤v≤13/40`.

For any `p7,v` and `0≤t≤1`, set `p_t=(1-t)p7+t p3(v)`; let `q(p_t)` be the exact 15-row rescaled Blackwell RHS. Physical perturbations are defined *only* along the **same frozen eight directions** as PR #1986: `q'=q(p_t)+Tδ`.

## New theorem: stronger nonmonotone uniform exclusion radius

Define the following exact positive constants:

```text
A = 254087337130964128905 / 142439520168704998753514
B = 71397 / 1017037
C = 550609460307500 / 116839042577461087
```

**Theorem.** For every `p7∈P7`, `v∈[1/10,13/40]`, `0≤t<1` and real `δ∈R^8` such that

```text
||δ||_∞ < R_new(t) := min{ A+(B−A)t, C(1−t) },
```

every nonnegative coupling on the original 30 allowed edges solving `Ce=q(p_t)+Tδ`, *if such a coupling exists*, has at least seven strictly positive edges.

The predecessor sufficient radius was `R_old(t)=A(1−t)`. The new bound is **strictly greater** for all `0<t<1`. The new certified radius first increases and then decreases, with its unique peak at the exact switch

```text
t* = 27506071400619459894935030258545
     / 686822379881831688569552660816119
   ≈ 0.04004830390843103

R_new(t*) = 3107058982823291144749787115000
            / 686822379881831688569552660816119
          ≈ 0.004523817327207455.
```

This peak is **2.53601921565×** the old radius `A` at the polygon. For `t*≤t<1` the radius is `C(1−t)`, making its end-taper coefficient **2.64181961028×** the old coefficient `A`. These are exact bounds for the *fixed seven-functional positivity test*, not claims of the true closest six-edge physical point.

## Proof (seven exact rational linear inequalities)

In the 15-row exact rescaling of the original 21 equations, write `Ce=q`. The six predecessor forcing functionals `y_f` correspond to `F6={(0,0),(3,3),(4,3),(4,5),(6,5),(6,6)}` and satisfy, on **all 30 columns**, `y_f^T C_e≤1_{e=f}`. Hence every nonnegative coupling obeys `e_f≥y_f^T q`. A seventh functional `ell` annihilates those six columns and is positive on the seventh old support edge `(0,3)`. Therefore when all six `y_f^T q` and `ell^T q` are positive, a feasible coupling contains the six forced arcs and at least one further positive arc.

For each of the seven functionals `h`, let `β_h>0` be its proven uniform minimum `h^Tq(p7)` on the **whole closed five-vertex polygon** and `η_h=||T^Th||_1>0` its physical sensitivity. The exact seven pairs `(β_h,η_h)` are copied from the table in PR #1986 and are present literally in `VERIFY_SHARP_BRIDGE_TUBE.py`.

At the terminal 3-edge point, in the order `(0,0),(3,3),(4,3),(4,5),(6,5),(6,6),ell`, the dual values are `(s(v),1−2s(v),0,0,0,s(v),0)`, with

```text
s(v) = 7933/36000 + (67/162)(v−1/10)
s_min = s(1/10)  = 7933/36000
s_max = s(13/40) = 3761/12000
1−2s_max         = 2239/6000 > 0.
```

Thus every `h` has a uniform terminal lower margin `γ_h`, respectively `(s_min,1−2s_max,0,0,0,s_min,0)`. For every bridge point,

```text
h^T q(p_t) ≥ (1−t)β_h+tγ_h.
```

For `q'=q(p_t)+Tδ`, Hölder's inequality yields

```text
h^T q' ≥ (1−t)β_h+tγ_h−η_h||δ||_∞.
```

Consequently positivity of all seven functionals, and hence the seven-edge lower bound, holds whenever `||δ||∞` is less than

```text
R_all(t) = min_h [((1−t)β_h+tγ_h)/η_h].
```

The seven rational expressions are *affine* in `t`. A complete exact rational comparison at `t=0,t=t*,t=1` shows the minimum is attained by the `(6,6)` line before `t*` and the `(4,3)` line afterwards. Checking these three breakpoints suffices: on each interval the proposed active line and all competing lines are affine, so endpoint dominance extends throughout. The two active lines reduce exactly to

```text
r_66(t) = A+(B−A)t,       B = (7933/36000)/(1017037/324000)
r_43(t) = C(1−t),          C = β_43/(281443/43200).
```

Therefore `R_all(t)=R_new(t)` for the full interval. Both individual values strictly exceed `A(1−t)` whenever `0<t<1`: the former because `B>0), the latter because `C>A`. The first is strictly increasing and the second strictly decreasing, proving the unique peak at their exact crossing.

The seven-column bound concerns **every permitted nonnegative coupling** (not just the exhibited bridge support) and includes all lawful physical perturbations in the stated fixed eight-parameter subspace. Outside that subspace or for changed LR/edge definitions, the theorem makes no claim.

## Actual validation and continuation

Execute `python VERIFY_SHARP_BRIDGE_TUBE.py` using standard-library `fractions.Fraction`. The script performs full exact comparison of all seven affine candidate radii at the three necessary breakpoints, checks constants/terminal bounds, and verifies strict improvement at representative rational parameters. `EXACT_OUTPUT.txt` records an independently executed local Fraction check of these same equations; no floating-point tolerance enters any acceptance condition. Historical 30-column dual checks, 21-equation verification and five-vertex polygon enumeration are **reused with immutable provenance**, not represented as newly re-executed.

BRC reuse: `COMPOSE_APPLIED` to typed positive rational labeled transport, its exact linear observer and dual positivity certificates. This is a statistical minimum-support result, not native-X6 geometric or physical identification.

Next discriminating unit: optimize duals jointly against the `t`-dependent margins rather than only these seven old fixed functionals; test exact 4/5/6-edge non-diagonal feasibility on transverse departures from the terminal three-edge family, retaining all original physical capacities. Formal mathematical review must re-audit inherited margin minima and column inequalities.
