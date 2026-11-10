# PREFIX-671-R6 — Exact fixed-z BRC variance nonconcavity and two internal critical points

**Date:** 2026-11-10 (Asia/Shanghai). **Role:** independent TASK_RESEARCH (no shared claim). **Status:** AUTHOR_DERIVED / EXACT_RATIONAL_REPLAY_CHECKED / UNREVIEWED / NOT_ADMITTED. **Frozen science pin:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`. **Mother objective:** global variance maximum of the unchanged 189-layer two-direction BRC first-stop statistical observer over `[0,1]^2`. This note concerns one auxiliary probability slice, not native X6 physical dynamics.

## Research question and theorem

PREFIX-668–670 proved strictly negative normal curvature only on `0<=p<=1/64` and `607/4096<=z<=609/4096`. Could that concavity strategy extend across the whole ordered triangle? Here is an exact counterexample to **global convexity and concavity of the variance objective along a fixed-z slice**, with a positive scientific consequence: two guaranteed, distinct internal stationary points.

Let `mu(p,z)=E[Y]`, `H(p,z)=E[Y^2]/2`, `W=2H-mu^2`, and `V_q(p,z)=q^2 W(p,z)-q mu(p,z)`. Fix `z=19/128`; let

`e=3/32, a=1/8, b=5/32, c=7/32, d=9/32`.

**Theorem 671.1.** For every real `12<=q<=24`, the polynomial `f_q(p)=V_q(p,19/128)` satisfies

```
f_q(a)>f_q(b),    f_q(c)>f_q(b),    f_q(c)>f_q(d),
f_q(e)-2*f_q(b)+f_q(c)>0,
f_q(b)-2*f_q(c)+f_q(d)<0.
```

It follows that `f_q` has at least one interior local minimum in `(a,c)` and one **distinct** interior local maximum in `(b,d)`. Accordingly `f_q'(p)=0` for at least two distinct `p` in `(1/8,9/32)`. The function is neither convex nor concave there; `f_q''` takes both positive and negative values on the slightly wider interval `(3/32,9/32)`. These are lower bounds on the number of critical points, not a count of all roots nor an assertion about global maxima.

## Exact frozen observer reconstruction

The frozen 189-layer survivor predicate is identical to `PREFIX665_R6_SIGNED_CURVATURE_CERTIFICATE.py` (Git blob `019ba810ea8ed60301f0304521fbc01117ba9aba`). Take `DEN=2^18`. At integer `t`, define

`inside(n,k,t) : 40(n+1) binom(n,k) t^k (DEN-t)^(n-k) > DEN^n`.

For each `n,k`, binary search the left/right integer thresholds around `floor(k*DEN/n)`; the frozen path survival predicate is `4*(right_low-left_high)>DEN`, and the exclusion inequality is `4*(right_high-left_low)<DEN`. All ambiguous branches are asserted absent. The recurrent path count is `A_n(k)=(A_(n-1)(k-1)+A_(n-1)(k)) * 1_{wide(n,k)}`. The exact replay confirms **189 survival rows, 9529 nonzero coefficient entries, full survival in layers 0–24, and empty layer 189**.

The finite survival polynomials and Gamma kernel are

```
s_n(u) = sum_k A_n(k)*u^k*(1-u)^(n-k),
w_nm   = binom(n+m,n) / 2^(n+m+1),
a_n(z) = 1-sum_m w_nm*s_m(z),
b_n(z) = n+1-sum_m ((n+m+1)/2)*w_nm*s_m(z).
```

The frozen independent-clock first-stop moment representation, from PREFIX-668, is

```
mu(p,z) = sum_n a_n(z)*s_n(p) + sum_m s_m(z),
H(p,z)  = sum_n b_n(z)*s_n(p) + sum_m (m+1)*s_m(z),
W(p,z)  = 2*H(p,z)-mu(p,z)^2,
V_q(p,z)= q*q*W(p,z)-q*mu(p,z).
```

The self-contained checker reconstructs the entire recurrence, then evaluates `s_n` and these moments using Python `Fraction` at **all five dyadic points**. There is no floating-point decision and no fitted interpolation.

## Exact executed certificate

Each entry in the table is a verified open integer interval `(N,N+1)` for the corresponding gap, **with the displayed integer being the strict lower bound**.

| Exact gap (write `V_x=V_q(x,19/128)`) | `q=12` lower | `q=24` lower |
|---|---:|---:|
| `V_a-V_b` | 4193 | 16591 |
| `V_c-V_b` | 2060 | 8773 |
| `V_c-V_d` | 5911 | 23090 |
| `V_e-2V_b+V_c` | 16707 | 67066 |
| `V_b-2V_c+V_d` | -7972 | -31865 |

For any fixed abscissas `x,y`,

```
(V_q(x,z)-V_q(y,z))/q
  = q*(W(x,z)-W(y,z))-(mu(x,z)-mu(y,z)).
```

This is **affine** in `q`; each Jensen combination normalized by `q` is affine as well. Each endpoint pair at `q=12,24` has the same strict sign, hence its sign holds at every real intermediate `q`. The exact intervals also imply the uniform strict margins `V_a-V_b>4193`, `V_c-V_b>2060`, `V_c-V_d>5911`, `V_e-2V_b+V_c>16707`, and `V_b-2V_c+V_d<-7971` for every `q in [12,24]`; the normalized signed gaps strictly increase in magnitude between the endpoints.

To obtain stationary points, the minimum of `f_q` on `[a,c]` is not at either endpoint since `f_q(b)` lies below both. Likewise the maximum on `[b,d]` is not at an endpoint because `f_q(c)` exceeds both. Both extrema are interior, so Fermat's theorem gives two zeros of `f_q'`. They cannot coincide: a common point would satisfy `f_q(c)<=f_q(r)<=f_q(b)`, contradicting `f_q(c)>f_q(b)`.

Finally `b=(e+c)/2`, but `f_q(b)<(f_q(e)+f_q(c))/2`, disproving concavity; `c=(b+d)/2`, but `f_q(c)>(f_q(b)+f_q(d))/2`, disproving convexity. Smoothness (finite polynomial moments) gives both signs of `f_q''` somewhere in the respective intervals.

**Replay:** `python PREFIX671_R6_NONCONCAVE_VARIANCE_WITNESS.py` (Python 3 standard library). Local execution returned `ALL_CHECKS_PASS 37`. `PREFIX671_R6_RESULTS.json` records every exact integer gap bracket, the scope, and the state count; the code is the full arithmetic evidence.

## Implications and next discriminating unit

The strong-concavity certificate of PREFIX-670 remains valid on its own rectangle. The current counterexample makes a **single global negative-curvature extension** inappropriate: the full-triangle maximum search needs piecewise treatment.

Concrete next unit: partition the ordered triangle `0<=p<=z<=1/2` into rational rectangles (respecting the triangle edge); retain the proven boundary strip, split the wider `p` domain at the witnessed curvature changes, and derive rational Bernstein upper bounds for each region. Use fixed edge witness `(0,19/128)` as a baseline. For each box, certify the strict normalized difference at `q=12` and `24`; only if both endpoint tests pass does the affine-in-`q` formula exclude that box for **all real `12<=q<=24`**. Unresolved boxes remain candidates for refinement.

**Sources:** PREFIX-665 (frozen predicate, Git blob above); PREFIX-668 `f6288695a77bd13ee55752fd73cf177083e7c8db` (Gamma moment formula); PREFIX-670 `24c22a1496db5cb5da05ffef104b55b8d52f520e` (previous strip). No P000 or ACTIVE worldview changes, native task CLAIM, Result, or review are asserted. Independent mathematical review is pending.
