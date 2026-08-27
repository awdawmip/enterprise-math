# P017 — c=103/20 T1–T2 High-LPF Pointwise Collapse

Status: `PROVED_WIP EXACT POINTWISE COLLAPSE / LOW-LPF T1-T2 SECTOR REMAINS / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_C515_T1_T3_SOURCE_MAP_AND_T3_BUCHSTAB_COLLAPSE_20260827.md`;
- source equation (3) of Iwaniec–Laborde (1981).

Purpose: use the exact pointwise meaning of T1, T2 and the already-collapsed base-minus-T3 term to prove that T1–T2 cannot create negative mass once the least prime factor reaches the natural T2 endpoint.

---

## 1. Frozen parameters

Keep

\[
a=6,
\qquad
b=\frac{93}{20},
\qquad
c=\frac{103}{20},
\qquad
\Delta=2c-b-1=\frac{93}{20},
\]

and

\[
U=\frac{b+1}{2a}=\frac{113}{240}.
\]

The T2 external-prime endpoint is

\[
U-\frac1a
=\frac{73}{240}.
\]

The full square basin lies below

\[
W^2=D^{9/5}
\]

because `D=W^(10/9)`.

---

## 2. Exact pointwise T1 and T2 weights

Let `n` be a state counted by `S(A,z)`, so every prime factor of `n` is at least `z=D^(1/6)`.

For each distinct prime divisor `p|n`, put

\[
\tau(p)=\frac{\log p}{\log D}.
\]

Then T1 contributes exactly

\[
\boxed{
T_1(n)
=\frac12
\#\left\{p\mid n:\ \frac16\le\tau(p)<\frac{31}{40}\right\}.
}
\tag{H1}
\]

For T2, let `q_p` be the least prime factor of `n/p`, with `q_p=+infinity` if `n=p`, and write

\[
\sigma_p=\frac{\log q_p}{\log D}.
\]

A fixed divisor prime `p` occurs in the T2 integrand precisely for

\[
\frac16\le s\le
\min\bigl(\tau(p),\ U-\tau(p),\ \sigma_p\bigr).
\]

Therefore the exact pointwise T2 contribution is

\[
\boxed{
T_2(n)
=6\sum_{p\mid n}
\left[
\min\bigl(\tau(p),U-\tau(p),\sigma_p\bigr)
-\frac16
\right]_+.
}
\tag{H2}
\]

The sum is over distinct divisor primes `p`; repeated powers are handled through `q_p`, since `n/p` may still be divisible by `p`.

---

## 3. T2 vanishes above the natural low-LPF frontier

Let

\[
\tau_1=rac{\log p_{\min}(n)}{\log D}.
\]

Assume

\[
\boxed{
\tau_1\ge\frac{73}{240}.
}
\tag{H3}
\]

Then every divisor prime `p|n` has `tau(p)>=73/240`, and hence

\[
U-\tau(p)
\le
\frac{113}{240}-\frac{73}{240}
=\frac16.
\]

Thus every bracket in (H2) is zero and

\[
\boxed{T_2(n)=0.}
\tag{H4}
\]

This is exact, not an asymptotic estimate.

---

## 4. At most five T1 primes in the transition band

Still assume (H3). If `n` had six distinct prime factors, then

\[
n\ge D^{6(73/240)}=D^{73/40}.
\]

But

\[
\frac{73}{40}>\frac95,
\]

whereas every basin state satisfies

\[
n<W^2=D^{9/5}.
\]

Contradiction. Therefore `n` has at most five distinct prime factors, so from (H1)

\[
\boxed{T_1(n)\le\frac52.}
\tag{H5}
\]

---

## 5. Base-minus-T3 already dominates T1 in the transition band

Suppose first that

\[
\frac{73}{240}\le\tau_1<U=\frac{113}{240}.
\]

The least-prime T3 shell is present. Its source coefficient is

\[
\psi(p_{\min})
=b+1-12\tau_1.
\]

Thus the exact base-minus-T3 point weight is

\[
1-\frac{\psi(p_{\min})}{\Delta}
=
\frac{12\tau_1-1}{\Delta}.
\]

At the lower endpoint,

\[
12\frac{73}{240}-1
=\frac{53}{20}.
\]

Using (H4) and (H5),

\[
\begin{aligned}
\left(1-\frac{T_3(n)}{\Delta}\right)
-\frac{T_1(n)+T_2(n)}{\Delta}
&\ge
\frac{53/20-5/2}{93/20}\\
&=
\boxed{\frac1{31}}.
\end{aligned}
\tag{H6}
\]

Here the notation `T3(n)` means the pointwise T3 shell coefficient; the displayed expression is the pointwise contribution of `S-T3/Delta-(T1+T2)/Delta`.

---

## 6. Above the T3 endpoint the margin is even larger

If

\[
\tau_1\ge U=\frac{113}{240},
\]

then T3 is absent and the base contribution is `1`. Also T2 remains zero.

Four distinct prime factors would force

\[
n\ge D^{4U}=D^{113/60}>D^{9/5},
\]

so there are at most three distinct prime factors. Hence

\[
T_1(n)\le\frac32,
\]

and

\[
\boxed{
1-\frac{T_1(n)+T_2(n)}{\Delta}
\ge
1-\frac{3/2}{93/20}
=\frac{21}{31}.
}
\tag{H7}
\]

---

## 7. Hard-sector reduction

Combining (H6) and (H7):

\[
\boxed{
 p_{\min}(n)\ge D^{73/240}
 \Longrightarrow
 \left[S-\frac{T_1+T_2+T_3}{\Delta}\right](n)
 \ge\frac1{31}.
}
\tag{H8}

Therefore every state on which T1–T2 can contribute net negative mass must satisfy

\[
\boxed{
 z\le p_{\min}(n)<D^{73/240}.
}
\tag{H9}
\]

At the Tier-A scale this is

\[
D^{73/240}=W^{73/216}\approx5.85\times10^5.
\]

This is the new T1–T2 hard frontier. The enormous T1 external-prime range up to `D^(31/40)` does not mean that all those states require independent analytic treatment: any genuinely dangerous T1/T2 state carries a least-prime anchor below roughly 585,000.

T4 is not included in (H8); it remains governed by the separately frozen terminal T4 certificate.

---

## 8. Next

Condition on the least prime

\[
r=p_{\min}(n)<D^{73/240}
\]

and apply a second Buchstab decomposition to the fixed-cutoff T1 term. The remaining hard object is an ordered two-prime shell `(r,p)` with a small first anchor `r`, rather than an unrestricted prime-lift family.

No finite P2 theorem or all-K claim is made here.
