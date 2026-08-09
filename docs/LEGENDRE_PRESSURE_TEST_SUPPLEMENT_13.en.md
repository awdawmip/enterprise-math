# Legendre Pressure Test — Supplement 13

Status: `ACTIVE RESEARCH NOTE`  
Scope: basin-level aggregation of high-band three-prime resources by exact large-modulus hit-state unions  
Depends on: P017 L035, L039–L048  
Discipline: **this note does not prove Legendre's conjecture.** It adds no sieve formalism. L041 handles support closure, L042–L045 centered mirror separation, and L046–L048 bounded CRT sign-pattern capacity; L049 instead aggregates canonical large-modulus hits across least-factor shells.

## 1. Why another cross-state inequality is still useful

L042–L045 relate the two states of one centered mirror pair. L046–L048 encode the mirror-side sign pattern and bound its finite lifts. L036 and L040, by contrast, control three-prime states inside one least-factor shell. None of these prevents the same cofactor resource prime from being counted again in a different least-factor shell.

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

Fix a prime `r` that occurs as one of the two cofactor primes of a high-band triple state. If `n=p\ell s` uses `r`, then `p<=r`; the other cofactor prime is at least `p`, so

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

Hence L039 gives at most one basin hit for the modulus `pr`. When it exists, call the unique state `x_{p,r}(k)`.

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

Equal states arising from different moduli are counted once. Automatically,

\[
c_r(k)\le\sum_{p\in\mathcal E_r(k)}H_{pr}(k)
\qquad\text{and}\qquad
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

then `r^2` is automatically `p`-rough, so `p r^2` is genuinely a three-prime state in the least-factor-`p` shell. Therefore `E_H(k)` is exactly the finite number of pairs `(p,r)` satisfying

\[
p\in\mathcal P_H(k),\qquad r\text{ prime},\qquad p\le r,\qquad r^2\in W_p(k).
\]

---

## 5. L049 — Global hit-union resource bound

Status: `PROVED`.

Let `T_H(k)` be the total number of high-band three-prime states across all least-factor shells. Then

\[
\boxed{2T_H(k)-E_H(k)\le\sum_r c_r(k).}
\]

Consequently,

\[
\boxed{
T_H(k)
\le
\left\lfloor\frac{E_H(k)+\sum_r c_r(k)}{2}\right\rfloor.
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
\sum_n|S(n)|=2T_H(k)-E_H(k).
\]

Fix a resource prime `r`, and let `u_r(k)` count actual high-band triple states whose cofactor support contains `r`. For any such state, its least prime `p` belongs to `P_H(k)`. Since the other cofactor prime is at least `p`,

\[
p\le r,\qquad p^2r\le n\le U,
\]

so `p` belongs to `E_r(k)`. The state is divisible by `pr`; because `pr>=2k`, L039 says that this modulus has at most one basin hit. Hence the actual state must be exactly `x_{p,r}(k)` and belongs to `X_r(k)`.

Thus

\[
u_r(k)\le c_r(k).
\]

Summing over all resource primes gives

\[
2T_H(k)-E_H(k)=\sum_r u_r(k)\le\sum_r c_r(k),
\]

which proves L049. ∎

---

## 6. Exact cross-shell collision witness

At

\[
k=110,\qquad r=19,
\]

the eligible moduli

\[
17\cdot19\qquad\text{and}\qquad19^2
\]

both hit the same basin state

\[
12274.
\]

Hence

\[
X_{19}(110)=\{12274\},\qquad c_{19}(110)=1.
\]

Two binary modulus hits occupy only one realized resource-19 state slot. L049 makes no statistical sparsity claim; it only uses exact collisions among realized hit states.

---

## 7. Regression checkpoints

The executable tests compare L049 directly with the actual high-band triple states for bounded `k`.

At `k=110`,

\[
\sum_r c_r(110)=7,\qquad E_H(110)=1,
\]

so

\[
T_H(110)\le4.
\]

The sum of the already-combined shellwise L036/L040 bounds is `5`, so L049 is strictly stronger at this checkpoint.

At `k=500`,

\[
\sum_r c_r(500)=33,\qquad E_H(500)=1,
\]

hence

\[
T_H(500)\le17.
\]

These are implementation regressions, not asymptotic claims.

---

## 8. Relation to L041–L048 and next target

The current cross-state tools have distinct jobs:

- L041: anchor-surviving exact-support closure after a large transverse-support hit;
- L042–L045: centered mirror support separation and the basin incidence necessary condition;
- L046–L048: CRT/idempotent sign-pattern encoding and bounded lift capacity;
- L049: exact cross-shell occupancy capacity of high-band cofactor resources via large-modulus hit-state unions.

The unresolved pieces are now sharply separated:

1. semiprime states `p q` with prime cofactor `q`;
2. lower least-factor shells satisfying `p^2<2k`;
3. a useful uniform analytic upper envelope for the exact finite quantity
   \[
   \sum_r c_r(k).
   \]

The next step should attack one of these pieces or genuinely connect L049 to the mirror-incidence inequality. Another equivalent encoding of the same binary hits should not be introduced.
