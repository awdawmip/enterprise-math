# Legendre Pressure Test — Supplement 21

Status: `PROVED + OPEN FRONTIER RESEARCH NOTE`  
Scope: high-band root-shell repair through dual factor windows  
Depends on: P007 dual factor-window Supplement 02, P017 high-band rough windows, P023-S9 minimal repair counting  
Discipline: the prime number theorem is classical prior art. The statements about realized high-band multiplicity are separated strictly into proved finite witnesses and an open unboundedness question.

## 1. Why lower-band one-bit repair cannot simply be reused

P017 Supplement 20 completely localizes lower-band realized cross-shell root ambiguity: a binary repair is needed only at `k=5,8`.

The same claim is false in the high least-factor band

\[
p^2\ge2k.
\]

There can be many distinct least-prime shells inside one retained root fiber. The correct object is therefore the **local shell split multiplicity**, not a fixed shell bit.

## 2. Raw and realized root-label sets

Fix the square basin

\[
(k^2,k(k+2)]
\]

and a retained cofactor root index `s`, whose quotient bucket is

\[
J_s=[s^2,s(s+2)].
\]

Define the raw high-band prime-label envelope

\[
P^{\rm win}_{k,s}
=
\{p\le k:\ p\text{ prime},\ p^2\ge2k,\ W_p(k)\cap J_s\ne\varnothing\}.
\]

Define the realized label set

\[
P^{\rm sh}_{k,s}
=
\{p\in P^{\rm win}_{k,s}:\exists q\in W_p(k)\cap J_s\text{ that is }p\text{-rough}\}.
\]

Then

\[
\boxed{P^{\rm sh}_{k,s}\subseteq P^{\rm win}_{k,s}.}
\]

The corresponding local repair burdens are

\[
R^{\rm win}_{k,s}=|P^{\rm win}_{k,s}|,
\qquad
R^{\rm sh}_{k,s}=|P^{\rm sh}_{k,s}|.
\]

Only the second is the task-minimal shell repair burden for actual P017 states.

## 3. L058 — Exact high-band raw factor window

Status: `PROVED`.

By P007-S2-T03, every raw factor label capable of reaching root `s` lies exactly in

\[
\boxed{
D_{k,s}
=
\left[
\left\lfloor\frac{k^2}{s(s+2)}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{s^2}\right\rfloor
\right].
}
\]

Therefore

\[
\boxed{
P^{\rm win}_{k,s}
=
D_{k,s}
\cap\{p\le k:p\text{ prime},\ p^2\ge2k\}.
}
\]

### Proof

`W_p(k)` hits the root bucket exactly when

\[
k^2<p\,s(s+2)
\]

and

\[
p\,s^2\le k(k+2).
\]

These are precisely the two integer endpoint inequalities defining `D_{k,s}`. Prime, least-factor-range, and high-band conditions are then explicit filters. ∎

This converts a root-shell collision question into one integer interval plus admissibility predicates.

## 4. L059 — Elementary local upper bound for realized repair

Status: `PROVED`.

For any realized least-prime shell state `n=pq` with retained root `s=R_2(q)`, one has `p<=q` and `n>k^2`. Hence

\[
q>k.
\]

Therefore

\[
s\ge\lfloor\sqrt{k}\rfloor.
\]

Writing

\[
r=\lfloor\sqrt{k}\rfloor,
\]

and using the exact dual window gives the crude uniform bound

\[
\boxed{
R^{\rm sh}_{k,s}
\le
R^{\rm win}_{k,s}
\le
2r+8
\qquad(k\ge4).
}
\]

### Proof

Ignoring the prime/high-band filters can only increase the count, so the raw multiplicity is at most the integer cardinality

\[
C_{k,s}
=
\left\lfloor\frac{k(k+2)}{s^2}\right\rfloor
-
\left\lfloor\frac{k^2}{s(s+2)}\right\rfloor.
\]

The real endpoint difference is

\[
\Delta_{k,s}
=
\frac{2k(s+k+2)}{s^2(s+2)},
\]

which decreases with positive `s`. Since `s>=r` and `k<(r+1)^2`, hence `k<=r(r+2)`,

\[
\Delta_{k,s}
\le
\Delta_{k,r}
\le
2r+8.
\]

Finally `floor(x)-floor(y)<=ceil(x-y)`, giving `C_{k,s}<=2r+8`. ∎

The bound is intentionally elementary and loose. Its role is to show that the required shell repair is finite and sublinear in `k` even though it is not constant.

## 5. L060 — Square-of-square diagonal factor window

Status: `PROVED`.

Set

\[
k=t^2,
\qquad
s=t,
\qquad
t\ge6.
\]

Then the dual factor window is

\[
D_{t^2,t}
=
\left[
\left\lfloor\frac{t^4}{t(t+2)}\right\rfloor+1,
\left\lfloor\frac{t^2(t^2+2)}{t^2}\right\rfloor
\right].
\]

Because

\[
\frac{t^3}{t+2}
=t^2-2t+4-\frac8{t+2},
\]

we obtain, after the least-factor bound `p<=k=t^2`,

\[
\boxed{
D_{t^2,t}\cap[1,t^2]
=[(t-1)^2+3,t^2].
}
\]

Every prime in this interval is automatically high-band.

## 6. L061 — Raw high-band root repair multiplicity is unbounded

Status: `PROVED`, using the classical prime number theorem only for the final growth contradiction.

Let

\[
A_t
=
\#\{p\text{ prime}:(t-1)^2<p\le t^2\}.
\]

By L060,

\[
R^{\rm win}_{t^2,t}
=
\#\{p\text{ prime}:(t-1)^2+3\le p\le t^2\}.
\]

The two counts differ by at most one because only the two integers immediately after `(t-1)^2` were removed, and for `t>=6` at most one of those two consecutive integers can be prime. Thus

\[
\boxed{
A_t-1
\le
R^{\rm win}_{t^2,t}
\le
A_t.
}
\]

### Proof of unboundedness

If `A_t` were bounded by a constant `C`, then telescoping consecutive-square intervals would give

\[
\pi(T^2)
=
\sum_{t=2}^{T}A_t+O(1)
=O(T).
\]

But the prime number theorem gives

\[
\pi(T^2)
\sim
\frac{T^2}{2\log T},
\]

which is not `O(T)`. Hence `A_t` is unbounded, and so is

\[
\boxed{R^{\rm win}_{t^2,t}.}
\]

By P023-S9, a representation that treats every raw exact-window label as a possible task state cannot have a globally fixed finite repair alphabet over root alone.

This is an exact number-theoretic reason that **envelope precision can carry unbounded label burden**.

## 7. L062 — A fixed one-bit repair already fails for realized high-band shells

Status: `PROVED BY EXPLICIT FINITE WITNESS`.

At

\[
k=1737,
\qquad
s=45,
\]

the same realized root fiber contains the eight distinct least-prime shells

\[
\boxed{
1429,1439,1447,1451,1459,1471,1481,1489.
}
\]

Each label has an actual `p`-rough cofactor in the root-45 bucket. Therefore

\[
\boxed{R^{\rm sh}_{1737,45}=8.}
\]

P023-S9-T03 now implies that any repair coordinate which retains root 45 and must recover the least-prime shell requires an alphabet of at least eight symbols on that fiber.

Consequently a universal one-bit or two-bit high-band shell repair is false.

## 8. Bounded growth evidence for the realized burden

The exact executable scan finds the following first witnessed multiplicities:

- `2` at `k=8`, root `3`, shells `(5,7)`;
- `3` at `k=56`, root `8`, shells `(41,43,47)`;
- `4` at `k=127`, root `12`, shells `(97,103,107,109)`;
- `5` at `k=317`, root `20`, shells `(229,233,239,241,251)`;
- `6` at `k=629`, root `25`;
- `7` at `k=1242`, root `39`;
- `8` at `k=1737`, root `45`.

On the square-of-square diagonal, exact finite audits include

\[
(t,R^{\rm win},R^{\rm sh})
=(100,20,3),
(200,39,6).
\]

These values are **computational observations**, not a proof that the realized multiplicity is unbounded.

## 9. Diagonal realizability becomes a prime-pair problem

For `k=t^2,s=t,t>=6`, every raw candidate prime `p` is much larger than `sqrt(q)` for every `q` in the root bucket. Therefore a `p`-rough quotient in that bucket must itself be prime.

Hence the realized diagonal burden counts prime pairs `p,q` satisfying

\[
(t-1)^2+3\le p\le t^2,
\qquad
t^2\le q\le t^2+2t,
\]

and

\[
t^4<pq\le t^4+2t^2.
\]

This is a thin near-diagonal semiprime incidence problem rather than a raw interval-counting problem.

### Centered Goldbach subfamily

Let `K=t^2` and put

\[
p=K-a,
\qquad
q=K+a+2.
\]

Then

\[
p+q=2K+2
\]

and

\[
\boxed{pq=K(K+2)-a(a+2).}
\]

Whenever both `p,q` are prime and

\[
a(a+2)<2K,
\]

the product lies in the square basin, `p` is its least prime factor, and `q` remains in root bucket `t`. Thus each such near-central Goldbach representation contributes one realized high-band shell to root `t`.

This gives a concrete bridge from actual repair multiplicity to local prime-pair structure without claiming that the bridge solves the prime-pair problem.

## 10. Open frontier — Is realized high-band repair multiplicity unbounded?

Define

\[
H(k)
=
\max_s R^{\rm sh}_{k,s}.
\]

We now know

\[
H(1737)\ge8,
\]

while the raw envelope analogue is provably unbounded.

The current open question is

\[
\boxed{\sup_k H(k)=\infty\ ?}
\]

The diagonal reformulation in Section 9 shows why this is materially harder than raw-window unboundedness: admissibility has converted a one-dimensional prime-counting problem into a thin prime-pair incidence problem.

This question should be attacked as a genuine number-theoretic frontier, not assumed from bounded growth data.

## 11. Tool feedback

This stage adds two durable research lessons.

First,

\[
\boxed{
\text{candidate interval count}
\to
\text{prime-label envelope}
\to
\text{p-rough realized labels}
}
\]

are three different precision layers.

Second, the P023 local split multiplicity is not merely an engineering state-cost measure. In P017 it becomes a number-theoretic observable whose growth is governed first by prime density and then by prime-pair realizability.

## 12. Executable specification

- `src/enterprise_math/quotient_window.py`
- `src/enterprise_math/p017_high_band_root_precision.py`
- `tests/test_p007_dual_factor_window.py`
- `tests/test_p017_high_band_root_precision.py`

Finite computation supplies exact witnesses and regression. L058–L061 are ordinary proofs; L062 is an explicit finite witness theorem; the unboundedness of realized-shell multiplicity remains open.
