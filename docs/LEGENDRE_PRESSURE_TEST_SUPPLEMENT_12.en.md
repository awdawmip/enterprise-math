# Legendre Pressure Test — Supplement 12

Status: `ACTIVE RESEARCH NOTE`  
Scope: basin-level aggregation of high-band three-prime resources by exact large-modulus hit-state unions  
Depends on: P017 L035, L039–L045  
Discipline: **this note does not prove Legendre's conjecture.** It adds no sieve formalism. L041 handles support closure and L042–L045 handle centered mirror separation; L046 instead aggregates the canonical large-modulus hits across least-factor shells.

## 1. Why another cross-state inequality is still useful

L042–L045 relate the two states of one centered mirror pair. L036 and L040, by contrast, control three-prime states inside one least-factor shell. Neither prevents the same cofactor resource prime from being counted again in a different least-factor shell.

L039 supplies the missing exact object: every modulus `d>=2k` has at most one hit in the open square basin, and the hit state is explicitly determined by the common center. Cross-shell aggregation should therefore deduplicate the **realized hit states**, not merely count eligible moduli.

---

## 2. High-band triple-eligible least primes

Let

\[
U=(k+1)^2-1.
\]

A high-band three-prime state has the form

\[
n=p\ell s,
\qquad p\le\ell\le s,
\qquad p^2\ge2k.
\]

Necessarily `p^3<=n<=U`. Define

\[
\mathcal P_H(k)
=
\{p\le k:p\text{ prime},\ p^2\ge2k,\ p^3\le U\}.
\]

Only primes in this finite set can be the least factor of a high-band three-prime state.

---

## 3. Exact state capacity of one cofactor resource

Fix a prime `r` that occurs as one of the two cofactor primes of a high-band triple state.

If `n=p\ell s` uses `r`, then `p<=r`. The other cofactor prime is at least `p`, so

\[
n\ge p^2r.
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

Hence L039 gives at most one basin hit for the modulus `pr`. When it exists, call the unique state `x_(p,r)(k)`.

Define the realized hit-state union

\[
X_r(k)
=
\{x_{p,r}(k):p\in\mathcal E_r(k),\ H_{pr}(k)=1\}
\]

and its exact capacity

\[
c_r(k)=|X_r(k)|.
\]

Equal states arising from different moduli are counted once.

Automatically,

\[
c_r(k)
\le
\sum_{p\in\mathcal E_r(k)}H_{pr}(k)
\]

and

\[
c_r(k)\le H_r(k),
\]

because every state in the union is itself divisible by `r`.

---

## 4. Exact square-cofactor correction

Let `E_H(k)` be the number of high-band three-prime states whose cofactor is a prime square `r^2`.

For one least prime `p`, the high-band cofactor window has length at most `p`, hence span at most `p-1`; two distinct squares with roots at least `p` are farther apart than this. Thus at most one prime square occurs in that window.

If a prime `r>=p` satisfies

\[
r^2\in W_p(k),
\]

then `r^2` is automatically `p`-rough, so `p r^2` is genuinely a three-prime state in the least-factor-`p` shell.

Therefore `E_H(k)` is exactly the finite number of pairs `(p,r)` satisfying

\[
p\in\mathcal P_H(k),
\qquad r\text{ prime},
\qquad p\le r,
\qquad r^2\in W_p(k).
\]

---

## 5. L046 — Global hit-union resource bound

Status: `PROVED`.

Let `T_H(k)` be the total number of high-band three-prime states across all least-factor shells. Then

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

Only finitely many resource primes occur: in a least-factor-`p` triple,

\[
r\le\left\lfloor\frac{U}{p^2}\right\rfloor.
\]

### Proof

For each high-band triple state `n=p\ell s`, let

\[
S(n)=\{\ell,s\}
\]

be its cofactor-prime resource set. A nonsquare cofactor contributes two resources, while a square cofactor contributes one. Therefore

\[
\sum_n |S(n)|=2T_H(k)-E_H(k).
\]

Fix a resource prime `r`, and let `u_r(k)` count actual high-band triple states whose cofactor support contains `r`.

Take any such state. Its least prime `p` lies in `P_H(k)`. Since the other cofactor prime is at least `p`,

\[
p\le r,
\qquad p^2r\le n\le U,
\]

so `p` lies in `E_r(k)`. The state is divisible by `pr`, and `pr>=2k`; by L039 the modulus has at most one basin hit. Hence the actual state must be exactly `x_(p,r)(k)` and belongs to `X_r(k)`.

Thus

\[
u_r(k)\le c_r(k).
\]

Summing over all resource primes gives

\[
2T_H(k)-E_H(k)
=
\sum_r u_r(k)
\le
\sum_r c_r(k),
\]

which proves L046. ∎

---

## 6. Exact cross-shell collision witness

At

\[
k=110,
\qquad r=19,
\]

the eligible moduli

\[
17\cdot19
\qquad\text{and}\qquad
19^2
\]

both hit the same basin state

\[
12274.
\]

Hence

\[
X_{19}(110)=\{12274\},
\qquad c_{19}(110)=1.
\]

Two binary modulus hits occupy only one realized resource-19 state slot. This is the common-center phenomenon that survived the earlier falsification work: L046 makes no claim of statistical sparsity; it only uses exact collisions among realized hit states.

---

## 7. Regression checkpoints

The executable tests compare L046 directly with the actual high-band triple states for bounded `k`.

At `k=110`,

\[
\sum_r c_r(110)=7,
\qquad E_H(110)=1,
\]

so

\[
T_H(110)\le4.
\]

The sum of the already-combined shellwise L036/L040 bounds is `5`, so L046 is strictly stronger at this checkpoint.

At `k=500`,

\[
\sum_r c_r(500)=33,
\qquad E_H(500)=1,
\]

hence

\[
T_H(500)\le17.
\]

These are implementation regressions, not asymptotic claims.

---

## 8. Relation to L041–L045 and next target

The current cross-state results now have distinct jobs:

- L041: after a large transverse-support hit, decide anchor-surviving exact-support closure;
- L042–L045: relate opposite centered mirror states and obtain a mirror-incidence necessary condition;
- L046: aggregate high-band cofactor-resource occupancy across least-factor shells by exact large-modulus hit-state unions.

Thus no one result is a renaming of another.

The unresolved pieces are now sharply separated:

1. semiprime states `p q` with prime cofactor `q`;
2. lower least-factor shells satisfying `p^2<2k`;
3. a useful uniform analytic upper envelope for the exact finite quantity
   \[
   \sum_r c_r(k).
   \]

The next step should attack one of these three pieces or connect L046 with the mirror-incidence constraint. Another equivalent encoding of the same binary hits should not be introduced.
