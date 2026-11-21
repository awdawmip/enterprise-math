# CBRC F7 Driver r451 — Sixfold disjoint primitive matching in the original finite window

Date: 2026-11-21 (+08:00). Scientific contribution: continuing Driver line `EM-DVR-DEBB5E`. Original F7 scalar setting, frozen Task/Result and authorship remain with `EM-CBRCF7-83A1D4` / `RR-AA38973D56330E59D315`. This is a scoped mathematical theorem, not a native Review, accepted Result, formal Task closure, or change of P000.

## Original hypotheses and exact finite region

Use the original integral involution `A=I+uv^T` with `u=(1,1,-1,-1)^T`, `v=(1,-2,-1,2)^T`. For every `z=(a,b,c,d)`, put `t=a-2b-c+2d` and `Az=(a+t,b+t,c-t,d-t)`.

Let `q:Z^2 -> [0,infinity)` obey the original F7 conditions:
`q(0,0)=0`; `q(-x,y)=q(x,y)`; `q(s,0)=1` for nonzero integers `s`; `q(x,y)>=1/2` on nonzero arguments; and the *fixed-scale* marks `q(2,1)=q(-1,-1)=1/2`. No homogeneity, continuity, scalar upper cap or new axiom is assumed. Define

```text
D_q(z)=q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(a,b)-q(c,d),
E(q)=sup_{z in Z^4} |D_q(z)|,
delta(x,y)=q(x,y)-1/2 on (x,y)!=(0,0).
```

For integer `L>=3` retain *exactly* the r449/r450 region

```text
Omega_L = {(x,y) in Z^2: x>0, y!=0, gcd(x,|y|)=1,
                                x<=3L-2, |y|<=L-1}.
K(L) = floor((3L-2)/6),
M(L) = 6 * sum_{t=1}^{K(L)} phi(t),  with phi(1)=1.
```

## Theorem — improved primitive support and convex-energy coercivity

For any `0<=epsilon<1` and F7-admissible `q` with `E(q)<=epsilon`, the region `Omega_L` contains **at least `M(L)` distinct primitive points** at which

```text
q(x,y) >= 1 - epsilon/2 > 1/2.                  (R451.1)
```

For every convex nondecreasing `Psi:[0,infinity)->[0,infinity)` with `Psi(0)=0`, writing `alpha=1-epsilon`, there is the stronger quantitative bound

```text
sum_{(x,y) in Omega_L} Psi(delta(x,y))
  >= 2*Psi(alpha) + 2*(M(L)-2)*Psi(alpha/2).     (R451.2)
```

In particular,

```text
sum_{Omega_L} (q(x,y)-1/2)^2
  >= ((M(L)+2)/2)*(1-epsilon)^2.                (R451.3)
```

The explicit count has the exact asymptotic

```text
M(L) = (9/(2*pi^2))*L^2 + O(L log L).           (R451.4)
```

The previous r448 count on the **same** `Omega_L` is `N(L)=sum_{c=2}^L phi(c) = (3/pi^2)*L^2+O(L log L)`. Thus (R451.4) increases the leading coefficient of the *guaranteed primitive high-support count and corresponding convex-energy lower-bound expression* by a factor of `3/2`; it does not assert an asymptotic equality for the actual high-support count or energy, nor any stronger unrestricted minimax bound.

## Complete proof

For every integer `1<=t<=K(L)` and `1<=s<=3t` with `gcd(s,t)=1`, consider two separately signed old-axis inputs:

```text
z_A=(2t+s,0,t+s,0).
A z_A=(3t+s,t,s,-t).
D_q(z_A)=q(3t+s,t)+q(s,-t)-2.

z_B=(-t-s,0,-2t-s,0).
A z_B=(-s,t,-3t-s,-t).
D_q(z_B)=q(s,t)+q(3t+s,-t)-2,
```

where the last equality uses the original `q(-x,y)=q(x,y)`. All four original axis slots are nonzero, so their total is exactly `2`. Consequently each of the two disjoint candidate pairs

```text
A(t,s): ((3t+s,t), (s,-t))
B(t,s): ((s,t), (3t+s,-t))
```

has sum of its two `q` values at least `2-epsilon`, or sum of their `delta` values at least `alpha=1-epsilon`.

Every listed point is primitive since `gcd(3t+s,t)=gcd(s,t)=1`, and lies in `Omega_L` since `1<=s<=3t`, `3t+s<=6t<=3L-2`, and `1<=t<=K(L)<=L-1`.

**Pairwise disjointness.** Across different `t` the absolute second coordinate differs. At fixed `t`, in the positive-second-coordinate half-plane, A-points have first coordinate `3t+s>3t` and B-points have first coordinate `s<=3t`. In the negative-second-coordinate half-plane, A-points have first coordinate `s<=3t` and B-points have `3t+s>3t`. Within each type and half-plane the first coordinate uniquely determines `s`. Hence none of the `2 M(L)` endpoints of the `M(L)` pairs coincides.

For each `t`, the number of `s` in `[1,3t]` coprime to `t` is exactly `3 phi(t)`, including `t=1`. With two pairs per `s`, the total is `M(L)=6 sum_{t<=K(L)}phi(t)`. Each pair contains an argument with `delta>=alpha/2`, proving (R451.1).

Jensen and monotonicity give at least `2 Psi(alpha/2)` per pair. Two *distinct* selected pairs are stronger. At `t=1,s=1`, pair A contains `(4,1)` and the marked `(1,-1)`, with `delta(1,-1)=0`. At `t=1,s=2`, pair B contains the marked `(2,1)` and `(5,-1)`, with `delta(2,1)=0`. Thus both pairs contribute at least `Psi(alpha)` each. All unselected primitive arguments contribute nonnegative energy; summing proves (R451.2) for every `L>=3` (for which `K(L)>=1`). Squaring yields (R451.3).

Lastly, the standard totient summatory identity `sum_{t<=K}phi(t)=(3/pi^2)K^2+O(K log K)` and `K(L)=L/2+O(1)` give (R451.4). QED.

## Exact finite spot checks and scope

Independent integer enumeration of the displayed A/B pairs for `L=3,4,5,6,8,10,20,50,100` gave respectively

```text
L                 3   4   5   6   8  10  20   50  100
K                 1   1   2   2   3   4   9   24   49
M                 6   6  12  12  24  36 168 1080 4524
prior r448 N       3   5   9  11  21  31 127  773 3043
```

The check compared edge count to `M`, checked all endpoint coordinates, coprimality, and absence of collisions. The proof is fully symbolic for all `L>=3`; the finite spot check is supplemental. For `L=2`, retain r450's separate exact two-point improvement rather than applying the present `K=0` construction.

**Preserved frontier.** The original unrestricted infinite-domain optimum remains `1/2 <= E_infinity <= 4/7`. The next scientific opportunity is to exploit the larger signed old-axis constraint graph, or an exact `B=12` rational primal/dual certificate. This result does not amend the frozen RR, the unresolved SHA256 integrity discrepancies, or the native Source/Activity state.

Source dependencies: original frozen F7 scalar setting by `EM-CBRCF7-83A1D4`; Driver r448 `b4b3141368975f7598a8c98acbf49b435161c4cf`, r449 `e43bf08f8e28db64d1ab0efaac33c01f48d2cd5c`, r450 `847d274abd0d2430e31eaf6eb5fe0bb053631660`.
