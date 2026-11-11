# PREFIX-702-R6 — Parameter-adaptive maximal envelope for excluded BRC corner neighborhoods

Date: 2026-11-11 (Asia/Shanghai).
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Provenance: PREFIX-621/625 first-stop model, PREFIX-630 global derivative bounds, PREFIX-700 exact rational corner witness, PREFIX-701 positive-area corner exclusions.
Evidence: AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.
Researcher session: native session requested (control receipt pending at publication); this unshared mathematical note does not claim another live owner.

## Research question and fixed observer

For the two labelled, independently Poissonized signed-information BRC first-stop streams in the frozen X6 observer context, let `D=[0,1/2]^2` be the sign-symmetric **auxiliary probability-parameter square**, not a native spatial plane. For real `q>=2`, define

```text
mu(x)=E[Y(x)], W(x)=Var(Y(x)),
V_q(x)=q^2 W(x)-q mu(x),
G_q(x)=V_q(x)/q^2=W(x)-mu(x)/q.
```

Retain the actual signed branch/history model and finite count normalization from PREFIX-621/700. Fix the same rational witness `e=(0,1/8)`, all four square corners `C`, and `T_c(r)={x in D: ||x-c||_1<=r}`. The question is: how far can the previous explicit corner exclusion extend **without recomputing the 189-row kernel**?

## Theorem 702.1 — Explicit q-adaptive exclusion radius

Set the exact rationals

```text
a = 386820427/1000000,
b = 111509700/1000000,
M0 = 17931816, M1 = 17766,
R(q) = (a*q+b)/(M0*q+M1)     (q>=2 real).
```

**For every real q>=2, every corner c in C, and every x in T_c(R(q)):**

```text
G_q(e) > G_q(x),   hence V_q(e)>V_q(x).
```

Thus no global maximum of `V_q` lies in the four closed L1 corner triangles of radius `R(q)`. The four triangles remain disjoint since `R(q)<1/2`.

**Proof, exact inherited numerical inputs.** PREFIX-700 computed with integer/Fraction arithmetic the following certified (strict) lower bounds for `delta W=W(e)-W(c)` and upper bounds for `delta mu=mu(e)-mu(c)`, in units of `10^-6`:

| corner class | delta W strictly above | delta mu strictly below |
|---|---:|---:|
| (0,0) | 557257209 | 48811612 |
| (0,1/2), (1/2,0) | 386820427 | -111509700 |
| (1/2,1/2) | 439711044 | -119288767 |

By symmetry the second class contains two corners. Subtracting the second class's lower bound from the first gives `170.436782-160.321312/q>0` for all `q>=2`. For the last class the difference is `52.890617+7.779067/q>0`. Consequently, at *every* corner,

```text
G_q(e)-G_q(c) > a+b/q .
```

PREFIX-701's global moment envelope gives `|partial_i W|<=17931816` and `|partial_i mu|<=17766` for each coordinate on D, so

```text
|partial_i G_q| <= M(q)=M0+M1/q.
```

Integrate on the straight segment from c to x (D is convex):

```text
G_q(e)-G_q(x) > a+b/q - (M0+M1/q)*||x-c||_1.
```

For `||x-c||_1<=R(q)`, the right-hand expression is nonnegative by the definition of `R(q)`. The inequality is strict because the inherited corner bounds are strict. QED.

## Theorem 702.2 — Nearly doubled q-uniform excluded area

The radius function is strictly decreasing:

```text
sign R'(q) = sign(386820427*17766 - 111509700*17931816)
           = sign(-1992699170909118) < 0.
```

Thus its infimum over finite real `q>=2` is

```text
R_inf = 386820427/(1000000*17931816)
      = 55260061/2561688000000.
```

Theorem 702.1 already excludes all `T_c(R_inf)` for every finite real `q>=2`. For a **q-independent positive numerical gap**, choose the slightly smaller convenient rational radius

```text
r0=1/46357.
```

For all `q>=2`, all corners and all `x in T_c(r0)`,

```text
V_q(e)-V_q(x)
  > q^2 * (a-M0*r0)
  = q^2 * 18534439/46357000000 > 0.
```

Indeed the omitted term `(b-M1*r0)/q` is positive. The new four-triangle union has area `2/46357^2` in D, versus `2/65536^2` for PREFIX-701. Its exact area multiplier is

```text
(65536/46357)^2 = 4294967296/2148971449 > 1998/1000.
```

Hence the inherited certificate now rigorously excludes over 1.998 times the previous corner area, uniformly for all real `q>=2`. This is an enlargement of the certified excluded **auxiliary square region**, not of the X6 native spatial dimension or world model.

## Theorem 702.3 — Stronger parameter-local certificate for 12<=q<=24

Since `R(q)` decreases, its minimum on the closed real interval `[12,24]` is `R(24)`. The convenient exact radius `r_12_24=1/45809` is strictly less than `R(24)`, and for all `q in [12,24]`,

```text
V_q(e)-V_q(x)
 > q^2 * 14756219/4822000000
```

for every `x in T_c(1/45809)`. Here the lower margin is attained by our affine lower *certificate* at the parameter endpoint 24; it does not assert the true minimum of the model itself.

## What is verified and what remains

The companion `PREFIX702_R6_ADAPTIVE_CORNER_RADIUS.py` checks the exact rational comparisons, derivative-of-radius sign, two quantitative radii, margins, and area ratio using Python standard-library `Fraction`. Local run: `ALL_CHECKS_PASS PREFIX702-R6`. It does not re-run the frozen 189-row recurrence or re-derive the predecessor first-stop moment envelopes; the proof explicitly depends on their pinned certificates.

This `R(q)` is the maximal radius supported by the **specific displayed lower-corner-gap and global Lipschitz inequalities**, in the limit `q->infinity`. A larger true exclusion set may exist with a better local gradient envelope or more effective witness; this is a concrete next research route.

Next discriminating unit: partition the corner neighborhoods into small rational Bernstein cells and certify local bounds on `partial_i G_q` at q=12 and 24; since `G_q=W-mu/q` is affine in t=1/q, endpoint interval certificates extend across the continuum. Then compare how far the corner exclusion mesh can be enlarged toward the narrow active edge band of PREFIX-675, while preserving model and source pins.
