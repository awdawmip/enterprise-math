# R005-B — Horizon Window Opening and Saturation Law

Status: `PROVED WIP / DRAFT OWNER SUPPLEMENT / NOT CANONICAL`  
Date: `2026-08-10`  
Track: `R005-B — Prime–Collapse Field Geometry`  
Depends on: Supplements 02–04

## 1. Result

The pure-cap prime slice has two competing lower walls:

\[
\frac AF
\qquad\text{and}\qquad
\frac UR,
\]

where

\[
R=\operatorname{nextprime}(F),
\qquad
g=R-F.
\]

There are therefore two exact gap thresholds.

The first opens any raw non-forcing q-window:

\[
\boxed{
g_0=\frac US-F.}
\]

The second switches which wall controls the q-slice:

\[
\boxed{
g_1=\frac{F(U-A)}{A}.}
\]

Whenever a horizon q-band can exist (`FS>A`),

\[
\boxed{g_1>g_0.}
\]

For fixed `p>=3`,

\[
g_0\sim\frac p2 k^{p/2-1},
\qquad
g_1\sim p k^{p/2-1},
\]

so

\[
\boxed{g_1/g_0\to2.}
\]

Thus the upper factor-horizon obstruction has three phases:

`closed -> gap-controlled expanding window -> horizon-controlled saturated window`.

---

## 2. B22 — window-opening threshold

Let

\[
S=\lfloor\sqrt A\rfloor.
\]

The raw non-forcing condition can hold for some integer `q<=S` only when

\[
qR>U.
\]

The largest available q is S, so the raw q-window is nonempty exactly when

\[
RS>U.
\]

Since `R=F+g`, this is equivalent to

\[
(F+g)S>U,
\]

hence

\[
\boxed{g>g_0:=\frac US-F.}
\]

This is exactly the horizon-gap threshold already identified in Supplement 02.

---

## 3. B23 — wall-crossover threshold

The rational non-forcing wall dominates the horizon-entry wall exactly when

\[
\frac UR\ge\frac AF.
\]

All quantities are positive, so this is equivalent to

\[
UF\ge AR.
\]

Writing `R=F+g` gives

\[
F(U-A)\ge Ag.
\]

Therefore

\[
\boxed{
\frac UR\ge\frac AF
\iff
g\le g_1:=\frac{F(U-A)}A.
}
\]

Likewise

\[
\boxed{
\frac AF\ge\frac UR
\iff
g\ge g_1.
}
\]

Since order is preserved by the floor function, the same regime selects which
of

\[
\left\lfloor\frac AF\right\rfloor,
\qquad
\left\lfloor\frac UR\right\rfloor
\]

controls the exact integer lower endpoint, apart from the equality case where
both walls coincide at the rational level.

---

## 4. B24 — the crossover always comes after opening

Compute

\[
\begin{aligned}
g_1-g_0
&=\frac{F(U-A)}A-\left(\frac US-F\right)\\
&=\frac{U(FS-A)}{AS}.
\end{aligned}
\]

Hence

\[
\boxed{
FS>A
\Longrightarrow
g_1>g_0.
}
\]

But `FS>A` is exactly the real-valued condition that the horizon-entry band

\[
A/F<q\le S
\]

has positive width.

Therefore any nontrivial upper horizon cap necessarily possesses a genuine
intermediate regime between the first opening of the non-forcing window and
full saturation against the fixed horizon-entry wall.

---

## 5. Three phases

### Phase 0 — closed

If

\[
g\le g_0,
\]

then

\[
RS\le U,
\]

so even the largest possible q cannot make qR overshoot the basin.  The raw
pure-cap non-forcing window is empty.

### Phase I — gap-controlled expansion

If

\[
g_0<g\le g_1,
\]

then the q-window is open and

\[
\frac UR\ge\frac AF.
\]

Thus the active lower wall is the moving non-forcing wall `U/R`.

As g increases, R increases, `U/R` moves left, and the q-window expands.

The raw integer window width is exactly

\[
W=S-\left\lfloor\frac UR\right\rfloor
=\left\lceil\frac{RS-U}{R}\right\rceil.
\]

### Phase II — horizon-controlled saturation

If

\[
g\ge g_1,
\]

then

\[
\frac AF\ge\frac UR.
\]

The non-forcing wall has moved left of the fixed horizon-entry wall.  Further
increasing the post-horizon prime gap cannot enlarge the pure horizon band.

The q-slice saturates at the fixed interval

\[
\boxed{
A/F<q\le S
}
\]

subject only to the other pure-cap cutoffs in the general p case.

In the cubic case those other cutoffs are already absent by B21, so this is the
complete saturated interval.

---

## 6. Asymptotic ratio two

For fixed p>=3,

\[
U-A
=p k^{p-1}+O(k^{p-2}),
\]

and

\[
F=k^{p/2}+O(k^{p/2-1}).
\]

Therefore

\[
\boxed{
g_1
=p k^{p/2-1}+O(k^{p/2-2}+1).}
\]

Supplement 02 gives

\[
\boxed{
g_0
=\frac p2 k^{p/2-1}+O(k^{p/2-2}+1).}
\]

Hence

\[
\boxed{g_1/g_0\to2.}
\]

The factor-horizon system therefore has a universal leading-order geometry:

- roughly one unit of horizon drift is needed to open a non-forcing window;
- roughly two units are needed before that window saturates against the
  horizon-entry boundary.

---

## 7. Exact cubic specialization

For p=3,

\[
A=k^3,
\qquad
U-A=3k^2+3k.
\]

Thus

\[
\boxed{
g_1
=\frac{3F(k+1)}{k^2}.}
\]

The opening threshold is

\[
\boxed{
g_0=\frac US-F.}
\]

and the exact non-forced prime slice from B21 is

\[
\max\left(
\left\lfloor\frac AF\right\rfloor,
\left\lfloor\frac UR\right\rfloor
\right)<q\le S.
\]

Therefore:

- if `g0<g<=g1`, the lower endpoint is `floor(U/R)+1`;
- if `g>=g1`, it saturates at `floor(A/F)+1`.

All five explicit cubic failures recorded so far lie in the intermediate
`g0<g<g1` regime.  This is finite evidence only, not a theorem that every cubic
failure has that form.

---

## 8. Interpretation

The cubic full-forcing upper frontier is no longer best described as
"we need a prime gap theorem of exponent 1/3".

The exact structure is richer:

1. the post-horizon prime gap must first exceed the opening threshold;
2. that excess creates a q-window near the lower root S;
3. the q-window must contain a prime;
4. once the post-horizon gap is about twice the opening scale, the q-window
   stops expanding and saturates at the horizon-entry band.

This gives a concrete two-scale correlation problem:

\[
\boxed{
\text{prime-free interval to the right of F}
\quad\leftrightarrow\quad
\text{prime occupancy to the left of S}.
}
\]

No probabilistic independence between the two sides is assumed.

---

## 9. Status boundary

The identities B22–B24 are elementary exact algebra over the existing R005-B
objects.  The phase interpretation is project-side packaging; historical
novelty is unverified.

No claim is made that current prime-gap technology decides whether the cubic
Phase-I/Phase-II event occurs infinitely often.
