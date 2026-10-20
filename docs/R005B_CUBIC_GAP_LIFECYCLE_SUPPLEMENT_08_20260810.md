# R005-B — Cubic Cofactor-Gap Lifecycle and Critical Constant 3

Status: `PROVED WIP / EXACT INTERNAL ARITHMETIC / NOT CANONICAL`  
Date: `2026-08-10`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: R005-A T-A16; R005-B Supplements 02–07

## 1. Result

The cubic lower cofactor-gap band and upper horizon-gap band are not two
independent failure mechanisms.

A fixed consecutive prime gap

\[
a<b,\qquad g=b-a
\]

passes through three exact states as the cubic factor horizon moves right:

\[
\boxed{
\text{PRE\_HORIZON}
\to
\text{HORIZON\_INSIDE}
\to
\text{RETIRED}.
}
\]

Before the horizon reaches `a`, the gap can generate R005-A reciprocal
e=1 failures.  Once the horizon enters `(a,b)`, the same gap becomes the
post-horizon gap used by the upper-cap mechanism.  After the horizon reaches
`b`, that gap can no longer act as the first excluded cofactor gap.

For the PRE_HORIZON stage there is an exact activation threshold.  The least
integer gap length that can open any real reciprocal q-window is

\[
\boxed{
g_{\rm crit}(a)
=
1+
\left\lfloor
\frac{3a(K_-+1)}{K_-^2}
\right\rfloor,
\qquad
K_-=\left\lfloor\sqrt[3]{a^2}\right\rfloor-1.
}
\]

Hence

\[
\boxed{
g_{\rm crit}(a)=3a^{1/3}+O(1).}
\]

The constant `3` is not a fitted parameter.  It is the cubic relative basin
width transported to the cofactor-prime scale.

At horizon entry this is exactly the same leading scale as Supplement 05's
upper **saturation** threshold:

\[
g_1\sim3\sqrt{k}\sim3a^{1/3},
\]

while the upper **opening** threshold is only

\[
g_0\sim\frac32\sqrt{k}\sim\frac32a^{1/3}.
\]

Thus the same fixed gap has one coherent lifecycle:

\[
\boxed{
\text{lower PRE amplifier}
\to
\text{horizon handoff at the saturation scale}
\to
\text{upper post-horizon pulse}
\to
\text{retirement}.
}
\]

No theorem about the existence of infinitely many cube-root-size prime gaps is
claimed.

---

## 2. Setup

Fix a cubic basin

\[
A=k^3,\qquad U=(k+1)^3-1
=A+3k^2+3k
\]

and its universal factor horizon

\[
F_3(k)=\left\lfloor\sqrt{U}\right\rfloor.
\]

Fix consecutive primes

\[
a<b,\qquad g=b-a.
\]

R005-A T-A16 studies the e=1 cofactor route using the point

\[
x=\frac{A}{q}.
\]

When

\[
a<x<b,
\]

the gap blocks the e=1 exclusive cofactor exactly for prime q in the
reciprocal interval

\[
\boxed{
\frac{U}{b}<q\le\frac{A}{a}.
}
\]

This supplement asks how one fixed `(a,b)` behaves as `k` changes.

---

## 3. B34 — exact inverse of the cubic factor horizon

For every positive integer `t`,

\[
F_3(k)\ge t
\]

is equivalent to

\[
(k+1)^3-1\ge t^2,
\]

hence to

\[
(k+1)^3\ge t^2+1.
\]

Therefore the first cubic basin whose horizon reaches `t` is

\[
\boxed{
K_{\ge}(t)
=
\left\lceil\sqrt[3]{t^2+1}\right\rceil-1.
}
\]

Likewise

\[
F_3(k)<a
\iff
(k+1)^3\le a^2,
\]

so the last PRE_HORIZON basin for the left prime `a` is

\[
\boxed{
K_-(a)
=
\left\lfloor\sqrt[3]{a^2}\right\rfloor-1.
}
\]

Thus one fixed gap has the exact phase decomposition

\[
\begin{cases}
k\le K_-(a), & F_3(k)<a,\\[3pt]
K_{\ge}(a)\le k<K_{\ge}(b), & a\le F_3(k)<b,\\[3pt]
k\ge K_{\ge}(b), & F_3(k)\ge b.
\end{cases}
\]

The middle phase may be empty if one discrete horizon jump skips the whole
gap.

---

## 4. B35 — exact PRE_HORIZON activation threshold

Assume

\[
F_3(k)<a.
\]

The real reciprocal interval has positive width exactly when

\[
\frac{U}{b}<\frac{A}{a}.
\]

Cross-multiplication gives

\[
aU<bA=(a+g)A,
\]

so

\[
a(U-A)<gA.
\]

Since

\[
U-A=3k^2+3k
\]

and `A=k^3`, this is exactly

\[
\boxed{
gk^2>3a(k+1).
}
\]

Equivalently,

\[
\boxed{
g>a\left(\frac3k+\frac3{k^2}\right).
}
\]

The function

\[
\frac{k^2}{k+1}
\]

is strictly increasing for positive k.  Therefore, among all PRE_HORIZON
basins, the inequality is easiest to satisfy at the last one,

\[
k=K_-(a).
\]

Hence a fixed gap can activate at least one PRE_HORIZON real reciprocal
window if and only if

\[
gK_-^2>3a(K_-+1).
\]

The exact least integer gap length is therefore

\[
\boxed{
g_{\rm crit}(a)
=
1+
\left\lfloor
\frac{3a(K_-+1)}{K_-^2}
\right\rfloor.
}
\]

If activation occurs, monotonicity shows that the active PRE_HORIZON k-values
form one terminal interval

\[
[k_{\rm first},K_-(a)].
\]

---

## 5. B36 — cube-root critical constant

Because

\[
K_-(a)=a^{2/3}+O(1),
\]

we have

\[
\frac{3a(K_-+1)}{K_-^2}
=
3a^{1/3}+O(1).
\]

Thus

\[
\boxed{
g_{\rm crit}(a)=3a^{1/3}+O(1).}
\]

This gives the lower cubic band an exact critical exponent and leading
constant:

\[
\boxed{
\text{PRE activation scale}
=
3a^{1/3}.
}
\]

The exponent `1/3` agrees with R005-A T-A22's full-forcing exponent for
`p=3,m=2`.  R005-B now supplies the sharper local meaning of the constant:
it is the amount by which one consecutive cofactor-prime gap must beat the
cubic basin's relative width before the factor horizon reaches that gap.

---

## 6. B37 — exact reciprocal prime slice and boundary-prime compression

In PRE_HORIZON phase, the captured integer q-values are exactly

\[
\boxed{
L_q
=
\left\lfloor\frac{U}{b}\right\rfloor+1,
\qquad
H_q
=
\left\lfloor\frac{A}{a}\right\rfloor.
}
\]

So the e=1 failing candidates generated by this fixed gap are precisely the
primes in

\[
[L_q,H_q].
\]

Let

\[
Q_{a,b}(k)
=
\max\{q\le H_q:q\text{ prime}\},
\]

when such a prime exists.

Then

\[
\boxed{
[a,b]\text{ captures a prime q}
\iff
Q_{a,b}(k)\ge L_q.
}
\]

Equivalently,

\[
\boxed{
Q_{a,b}(k)b>U.
}
\]

When nonempty, `Q_{a,b}(k)` is the canonical maximal e=1 failure generated by
this one cofactor gap.

This is the lower-band analogue of Supplement 06's upper boundary-prime
compression.  The semantic question “does this fixed gap generate any q?”
does not require the whole reciprocal prime slice; it requires only its right
boundary prime.

---

## 7. B38 — when e=1 failure is already full non-forcing

Still assume PRE_HORIZON and let q be a captured prime satisfying

\[
q>k.
\]

Then q is fully non-forced in the singleton-support sense, not merely an e=1
failure.

First, PRE_HORIZON gives

\[
a>F_3(k)>\sqrt{A},
\]

while

\[
q\le \frac{A}{a}.
\]

Hence

\[
q<\sqrt A,
\qquad
q^2<A.
\]

Thus the pure square route lies below the basin.

Second, q is an integer and `q>k`, so

\[
q\ge k+1,
\]

and therefore

\[
q^3\ge(k+1)^3>U.
\]

Every higher pure power also lies above U.

Third,

\[
q^2(F+1)
\ge
(k+1)^2(F+1)
\ge
(k+1)^3
>
U,
\]

so every `q^e r` route with `e>=2` and prime `r>F` overshoots the basin.

Finally the e=1 route is blocked by the gap `(a,b)` itself.

By the one-large-prime horizon normal form, these exhaust the possible
singleton candidate-support shapes.  Therefore

\[
\boxed{
q>k
\quad+\quad
q\in[L_q,H_q]\text{ prime}
\quad\Longrightarrow\quad
q\text{ fully non-forced}.
}
\]

For the asymptotic critical regime below, the reciprocal q-window lies at
scale `a`, while `k` lies at scale `a^{2/3}`, so `q>k` is automatic for all
sufficiently large states.

---

## 8. B39 — lower/upper critical constants match at horizon handoff

Supplement 05 gave two upper post-horizon gap thresholds:

\[
g_0(k)\sim\frac32\sqrt{k},
\qquad
g_1(k)\sim3\sqrt{k}.
\]

When one fixed cofactor gap reaches the cubic horizon,

\[
a\asymp F_3(k)\asymp k^{3/2},
\]

so

\[
\sqrt{k}\asymp a^{1/3}.
\]

The lower PRE activation threshold from B36 is

\[
g_{\rm crit}(a)
=
3a^{1/3}+O(1).
\]

Therefore at the handoff scale,

\[
\boxed{
g_{\rm PRE,crit}
\sim
g_1
\sim
3a^{1/3},
}
\]

whereas

\[
\boxed{
g_0
\sim
\frac32a^{1/3}.
}
\]

So the leading constant `3` is shared by:

1. the last chance for a gap to generate a lower reciprocal obstruction before
   horizon entry;
2. the upper window's saturation/crossover scale at horizon entry.

This is the arithmetic continuity between the two bands.

For a fixed gap, the remaining post-horizon distance `b-F_3(k)` then decreases
as the horizon moves through the gap, so the upper obstruction is a short
handoff pulse before the gap retires.

---

## 9. Exact prototype — the gap 1327 < 1361

Take

\[
a=1327,\qquad b=1361,\qquad g=34.
\]

Exact integer inversion gives

\[
K_-(1327)=119.
\]

The exact critical gap is

\[
\boxed{
g_{\rm crit}(1327)=34.
}
\]

Thus this real prime gap lands exactly on the integer PRE activation
threshold.

The active PRE interval is only

\[
\boxed{k=119.}
\]

At k=119,

\[
F_3(119)=1314<1327,
\]

but the exact reciprocal integer interval is

\[
\boxed{
[1270,1269],
}
\]

which is empty.  So the real reciprocal window opens, but it does not yet
capture even an integer q.

The same gap then enters the factor horizon:

\[
F_3(120)=1330,
\qquad
F_3(121)=1347,
\qquad
F_3(122)=1364.
\]

Hence

\[
\boxed{
120\le k\le121
}
\]

is its HORIZON_INSIDE phase.

At k=120 this same gap is exactly the upper post-horizon gap already seen in
R005-B and produces the non-forced upper candidates

\[
1303,\ 1307.
\]

By k=122 the factor horizon has passed 1361 and the gap is retired.

So one concrete prime gap realizes the full lifecycle

\[
\boxed{
\text{PRE real activation with no q}
\to
\text{upper non-forcing event}
\to
\text{retirement}.
}
\]

---

## 10. Comparator — the gap 113 < 127

For

\[
a=113,\qquad b=127,\qquad g=14,
\]

the exact PRE critical length is

\[
g_{\rm crit}(113)=17.
\]

Therefore the gap never opens a PRE reciprocal window.

Its horizon phase is nevertheless

\[
23\le k\le24.
\]

At k=23 this is exactly the earlier upper scope fixture:

\[
F_3(23)=117,
\]

so the next prime after `A/q` may still lie below the horizon, and the first
eligible exclusive cofactor is the same right endpoint 127.

Thus the earlier `(k,q)=(23,109)` example is also one ordinary lifecycle event.

---

## 11. Finite exact evidence

The owner regression locks:

- exact cubic horizon inverse;
- exact PRE/HORIZON/RETIRED phase classification;
- the 1327–1361 critical fixture;
- the 113–127 non-PRE comparator;
- exact reciprocal q-slice compilation against literal inequalities on a
  bounded cubic grid.

A finite sieve through prime left endpoints below 5000 finds only

\[
\boxed{1327<1361}
\]

meeting

\[
b-a\ge g_{\rm crit}(a).
\]

A wider local discovery scan through 5,000,000 found the same unique event.
This is finite evidence only and is **not** used as a theorem about all prime
gaps.

---

## 12. Status boundary

Internal exact mathematics:

- horizon inverse and lifecycle;
- PRE activation inequality;
- exact critical gap length;
- cube-root leading constant 3;
- reciprocal boundary-prime compression;
- q>k full-nonforcing closure;
- lower/upper leading-scale handoff.

External/classical ingredients consumed:

- primality and consecutive prime gaps;
- R005-A T-A16's reciprocal e=1 characterization.

Nonclaims:

- no proof that only finitely many gaps satisfy
  `g>=3a^(1/3)+O(1)`;
- no proof that infinitely many do;
- no complete cubic full-forcing theorem;
- no claim that the finite scan is exhaustive beyond its stated cutoff.

The next supplement asks what happens **conditionally on a genuinely
supercritical sequence**

\[
g\ge(3+\eta)a^{1/3}.
\]
