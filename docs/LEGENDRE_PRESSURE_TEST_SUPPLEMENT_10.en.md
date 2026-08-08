# Legendre Pressure Test — Supplement 10

Status: `ACTIVE RESEARCH NOTE`  
Scope: basin-level aggregation of high-band three-prime resources by exact large-modulus hit unions  
Depends on: P017 L034–L041, especially L039–L040  
Discipline: this supplement does not prove Legendre's conjecture. It introduces no new sieve formalism. Its purpose is to turn the already-canonical binary hit events into a genuinely cross-shell inequality.

## 1. Why the next step must be global

L036 and L040 bound three-prime states separately inside each least-factor shell. That is useful, but summing shellwise bounds still allows the same cofactor resource prime to be counted again in another shell.

A first attempted correction was to bound the number of uses of a resource prime `r` by both:

- the number of least-factor shells in which `r` is eligible; and
- the total square-basin hit count `H_r(k)`.

That is valid but still loses information. The stronger fact is already available from L039: for every eligible least prime `p`, the modulus `p r` itself is at least `2k`, so its basin hit is binary and its hit state is explicit.

The correct next object is therefore not an average density. It is the **set union of exact hit states**.

---

## 2. High-band triple-eligible least primes

Let

\[
U=(k+1)^2-1.
\]

A high-band three-prime state has the form

\[
n=p\ell s,
\qquad
p\le\ell\le s,
\]

with

\[
p^2\ge2k.
\]

Necessarily

\[
p^3\le n\le U.
\]

Hence define

\[
\mathcal P_H(k)
=
\{p\le k:p\text{ prime},\ p^2\ge2k,\ p^3\le U\}.
\]

Primes outside this finite set cannot be the least factor of a high-band three-prime state.

---

## 3. Eligible uses of one resource prime

Fix a prime `r` that occurs as one of the two cofactor primes of a triple state.

If

\[
n=p\ell s
\]

uses resource `r`, then

\[
p\le r.
\]

The other cofactor prime is at least `p`, so

\[
n\ge p^2r.
\]

Therefore a necessary eligibility condition is

\[
p^2r\le U.
\]

Define

\[
\mathcal E_r(k)
=
\{p\in\mathcal P_H(k):p\le r,\ p^2r\le U\}.
\]

For every `p` in this set,

\[
pr\ge p^2\ge2k.
\]

Thus the open square basin, which has `2k` consecutive states and span `2k-1`, contains at most one multiple of `pr`.

Let

\[
x_{p,r}(k)
\]

be that unique hit state when it exists, and leave it undefined when

\[
H_{pr}(k)=0.
\]

By L039 the existence test is exactly the common-center residue event for

\[
k(k+1)\bmod(pr).
\]

---

## 4. Resource hit union

Define

\[
X_r(k)
=
\{x_{p,r}(k):p\in\mathcal E_r(k),\ H_{pr}(k)=1\},
\]

where the braces denote a set of **states**, so equal hit states arising from different moduli are counted once.

Let

\[
c_r(k)=|X_r(k)|.
\]

This is an exact finite integer capacity.

It automatically satisfies the weaker bounds

\[
c_r(k)
\le
\sum_{p\in\mathcal E_r(k)}H_{pr}(k)
\]

and

\[
c_r(k)\le H_r(k),
\]

because every state in `X_r(k)` is a basin multiple of `r`.

The point of the union is that both inequalities can be strict: different eligible moduli `pr` can hit the same basin state.

---

## 5. Exact square-cofactor correction

Let `E_H(k)` be the number of high-band three-prime states whose cofactor is a square:

\[
q=r^2.
\]

For a fixed least prime `p`, the cofactor window has span at most `p-1`, so it contains at most one prime square with root at least `p`.

Moreover, if a prime `r>=p` satisfies

\[
r^2\in W_p(k),
\]

then `r^2` is automatically `p`-rough. Hence

\[
p r^2
\]

is genuinely a three-prime state in that shell.

Therefore `E_H(k)` is not an unknown error term. It is exactly the finite number of pairs `(p,r)` with

\[
p\in\mathcal P_H(k),
\quad
r\text{ prime},
\quad
p\le r,
\quad
r^2\in W_p(k).
\]

---

## 6. L041 — Global hit-union resource bound

Status: `PROVED`.

Let `T_H(k)` be the total number of high-band three-prime states across **all** least-factor shells.

Then

\[
\boxed{
2T_H(k)-E_H(k)
\le
\sum_r c_r(k).
}
\]

Consequently,

\[
\boxed{
T_H(k)
\le
\left\lfloor
\frac{E_H(k)+\sum_r c_r(k)}{2}
\right\rfloor.
}
\]

Only finitely many resource primes occur: for every eligible least prime `p`, any cofactor resource satisfies

\[
r\le\left\lfloor\frac{U}{p^2}\right\rfloor.
\]

### Proof

For each high-band three-prime state

\[
n=p\ell s,
\]

write its cofactor prime support as

\[
S(n)=\{\ell,s\}.
\]

If `ell<s`, then `|S(n)|=2`. If `ell=s`, then `|S(n)|=1`. Therefore

\[
\sum_n |S(n)|
=
2T_H(k)-E_H(k).
\]

Now fix a resource prime `r`, and let `u_r(k)` be the number of actual high-band three-prime states whose cofactor support contains `r`.

Take any such state. Its least prime `p` belongs to `P_H(k)`. Because `r` is a cofactor prime,

\[
p\le r,
\qquad
p^2r\le n\le U,
\]

so `p` belongs to `E_r(k)`.

The state is divisible by `pr`. Since `pr>=2k`, the modulus `pr` has at most one basin hit, and the actual state must be exactly that unique hit `x_(p,r)(k)`. Hence every actual state counted by `u_r(k)` belongs to the set `X_r(k)`.

Thus

\[
u_r(k)\le c_r(k).
\]

Summing over resource primes gives

\[
2T_H(k)-E_H(k)
=
\sum_r u_r(k)
\le
\sum_r c_r(k).
\]

The stated bound follows. ∎

---

## 7. Why this is stronger than merely summing binary moduli

One could use the weaker capacity

\[
\sum_{p\in\mathcal E_r(k)}H_{pr}(k).
\]

L041 instead takes a union of the **hit states themselves**.

For example, at

\[
k=110,
\qquad
r=19,
\]

the moduli

\[
17\cdot19
\qquad\text{and}\qquad
19^2
\]

both hit the same basin state

\[
12274.
\]

Thus two binary modulus hits consume only one resource-19 state slot:

\[
X_{19}(110)=\{12274\},
\qquad
c_{19}(110)=1.
\]

This is exactly the kind of shared-center correlation that survived falsification: not a claim that hit bits are statistically sparse, but an exact collision between their realized states.

---

## 8. Checked finite capacities

The executable regression layer checks the theorem against the actual high-band triple states for a finite range of `k`.

Two fixed checkpoints are retained:

### `k=110`

\[
\sum_r c_r(110)=7,
\qquad
E_H(110)=1.
\]

Therefore

\[
T_H(110)\le4.
\]

The sum of the already-combined shellwise L036/L040 bounds is `5`, so L041 is strictly stronger at this checkpoint.

### `k=500`

\[
\sum_r c_r(500)=33,
\qquad
E_H(500)=1,
\]

hence

\[
T_H(500)\le17.
\]

These are regression witnesses, not asymptotic claims.

---

## 9. What changed in the research diagnosis

Earlier finite experiments rejected the statement

> the common square center makes the binary hit bits uniformly sparse.

L041 does **not** restore that statement.

It uses a different fact:

> even when many eligible moduli hit, their unique hit states can collide, and actual resource usage is bounded by the cardinality of the realized hit-state union.

This is deterministic, exact, and basin-level.

It also merges more of the earlier P017 work:

\[
H_d(k)
\longrightarrow
\text{large-modulus unique state}
\longrightarrow
\text{cross-shell resource union}.
\]

No new modular invariant is required.

---

## 10. Remaining obstruction

L041 controls only the high-band **three-prime** portion.

The dominant unresolved pieces are now more sharply separated:

1. semiprime states `p q` with prime cofactor `q`;
2. lower least-factor shells with `p^2<2k`;
3. conversion of the exact finite hit-union sum into a uniform analytic bound strong enough to interact with the other two pieces.

The next research step should therefore not add another representation of the same hits. It should test whether

\[
\sum_r c_r(k)
\]

admits a useful uniform upper envelope, or whether the high-band gain can couple to the semiprime/lower-band counts. If neither produces a new inequality, this line should stop at L041.
