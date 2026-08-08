# P019 Supplement 01 — Finite Dimension-Lift Kernel and Graph/Radial Distance Bounds

Status: `RESEARCH WIP`  
Scope: finite integer recursion only; no infinite series, calculus, or continuum limit

## 1. Why another dimension-lift tool is needed

The main P019 note defines the primitive `A_p` graph shells, integer quadratic separation `q_p`, and collapsed radial distance

\[
D_p=R_2(q_p).
\]

But if “higher dimensions are generated from lower dimensions by simple operations” is a core Enterprise Math method, separate closed forms for each dimension are not enough. We need a **single local rule whose repeated application raises dimension**.

This supplement constructs a completely finite integer kernel.

## 2. P019-T10 — Finite charge-energy convolution kernel

For `m>=0`, define

\[
K_m(s,E)
=
\#\left\{(a_1,\ldots,a_m)\in\mathbb Z^m:
\sum_i a_i=s,
\sum_i a_i^2=E
\right\}.
\]

The initial state is

\[
K_0(0,0)=1,
\]

with all other values zero.

After adding one integer slot `a`, the exact recursion is

\[
\boxed{
K_{m+1}(s,E)
=
\sum_{a^2\le E}K_m(s-a,E-a^2).
}
\]

For fixed `E`, the sum only needs

\[
-R_2(E)\le a\le R_2(E),
\]

so this is a **finite integer convolution**, not an infinite formal series and not a continuum construction.

`A_p` uses `p+1` integer slots with total charge zero. Define the fixed-`q` shell count

\[
N_p(q)=\#\{x\in A_p:q_p(0,x)=q\}.
\]

Since

\[
2q=\sum_i x_i^2,
\]

we get directly

\[
\boxed{
N_p(q)=K_{p+1}(0,2q).
}
\]

Thus raising intrinsic dimension from `p` to `p+1` does not require solving a new high-dimensional geometry problem. Apply the same one-coordinate kernel once more and read the `charge=0` slice again.

This matches the LEGO intuition: the old units do not change; one new structural slot is added together with the integer allocations it can carry.

## 3. The unit `1` is strictly invariant under this lift

At `q=0`, zero square sum forces every coordinate to be zero. Hence

\[
N_p(0)=1
\]

for every `p>=1`.

The kernel says the same thing: at `E=0`, the newly added coordinate must be `a=0`, so

\[
K_{m+1}(0,0)=K_m(0,0)=1.
\]

Therefore “1 remains 1 in every finite dimension” is not an exception added by hand; it is a fixed state of the dimension-lift kernel itself.

## 4. P019-T11 — Every precision-distance shell comes from the same kernel

The square-root collapse basin for distance `k` is

\[
k^2\le q<(k+1)^2.
\]

Define

\[
U_{p,k}
=
\#\{x\in A_p:D_p(0,x)=k\}.
\]

Then

\[
\boxed{
U_{p,k}
=
\sum_{q=k^2}^{(k+1)^2-1}K_{p+1}(0,2q).
}
\]

Define also the collapsed-radial closed ball

\[
W_{p,k}
=
\#\{x\in A_p:D_p(0,x)\le k\}.
\]

Then

\[
\boxed{
W_{p,k}
=
\sum_{q=0}^{(k+1)^2-1}K_{p+1}(0,2q).
}
\]

All sums are finite integer sums.

The first low-dimensional values are:

| `p` | `U_(p,0)` | `U_(p,1)` | `U_(p,2)` | `U_(p,3)` | `U_(p,4)` |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 2 | 2 | 2 | 2 |
| 2 | 1 | 12 | 18 | 24 | 30 |
| 3 | 1 | 42 | 98 | 228 | 314 |
| 4 | 1 | 110 | 550 | 1430 | 3130 |

These values were cross-checked by independent finite enumeration.

In particular, `U_(p,0)=1` stays invariant in every dimension, while all higher shells are generated slot-by-slot by the same `K` kernel.

## 5. P019-T12 — Sharp integer bounds between graph distance and quadratic separation

Let

\[
r=d_G(x,y),
\qquad
u=x-y.
\]

The positive coordinates of `u` sum to `r`, and the absolute values of its negative coordinates also sum to `r`.

For every positive integer `a`,

\[
a^2\ge a.
\]

Therefore the positive and negative square sums are each at least `r`, so

\[
\sum_i u_i^2\ge2r,
\]

which gives

\[
\boxed{q_p(x,y)\ge r}.
\]

Conversely, for nonnegative integers summing to `r`,

\[
\sum_i a_i^2\le\left(\sum_i a_i\right)^2=r^2.
\]

Apply this separately to the positive and negative coordinates to get

\[
\sum_i u_i^2\le2r^2,
\]

hence

\[
\boxed{q_p(x,y)\le r^2}.
\]

Together,

\[
\boxed{
r\le q_p(x,y)\le r^2.
}
\]

This is a purely integer inequality.

## 6. P019-T13 — Collapsed radial distance lies between `R_2(d_G)` and `d_G`

By monotonicity of `R_2`,

\[
R_2(r)\le R_2(q_p(x,y))\le R_2(r^2).
\]

Since

\[
R_2(r^2)=r,
\]

we obtain

\[
\boxed{
R_2(d_G(x,y))
\le
D_p(x,y)
\le d_G(x,y).
}
\]

Thus `D_p` is not an arbitrary second distance. It is a radial finite-resolution observation constrained by strict integer bounds under the primitive graph metric.

## 7. Structural meaning of the equality cases

### Upper endpoint `q=r^2`

For nonnegative integers with fixed sum `r`, the square sum reaches `r^2` exactly when all nonzero mass is concentrated in one slot.

Hence

\[
q=r^2
\]

exactly when all positive mass is concentrated in one coordinate and all negative mass in one coordinate: the displacement repeats one root direction `r` times.

Then

\[
D=r.
\]

### Lower endpoint `q=r`

The integer equality `a^2=a` is possible only for `a=0,1`.

Therefore

\[
q=r
\]

exactly when every nonzero coordinate is `+1` or `-1`; there must be `r` positive ones and `r` negative ones.

This requires at least `2r` coordinate slots, i.e.

\[
2r\le p+1.
\]

For this maximally distributed displacement,

\[
D=R_2(r).
\]

So at one fixed primitive graph radius `r`, the direction/allocation structure moves the radial precision distance through

\[
R_2(r),\ldots,r.
\]

**No angle variable is introduced; directional information is represented by how integer units are distributed among structural slots.**

## 8. Relation to high-dimensional directional richness

As dimension rises, more slots are available for distributing positive and negative units. Therefore the same graph radius contains more possible `q` states, while square-root collapse merges consecutive `q` shells into one integer distance basin.

This yields the current strongest working interpretation:

> High-dimensional directional richness need not come from a continuous angle space. It can arise from combinatorial allocation of finite units across more relation slots, followed by distance collapse from fine integer separation states to finite-resolution distance states.

The same mechanism explains:

1. why primitive contacts do not exhaust the `distance = 1` class;
2. why higher-dimensional results can be generated from the same lower-dimensional integer kernel;
3. why `1` itself does not change with dimension;
4. why distance can retain fine structure while its observed value remains an integer precision state.

## 9. Next work

The next priorities are:

1. search for a shorter recursion for `U_(p,k)` that does not retain the full charge-energy table;
2. compare `A_p`, SC, `A_p^*`, and HCP-type structures under collapsed `U_(p,k)`, higher directional moments, and distance-carry distributions;
3. test whether P009 typed scale can represent the precision levels of `D_p` with explicit scale tags and no type erasure;
4. determine whether the `{0,1}` distance carry can be unified with P018 carry/borrow calculus as one abstract finite-precision carry object.
