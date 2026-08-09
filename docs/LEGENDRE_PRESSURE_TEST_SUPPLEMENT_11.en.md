# Legendre Pressure Test — Supplement 11

Status: `ACTIVE RESEARCH NOTE`  
Scope: basin-level aggregation of high-band three-prime resources by exact large-modulus hit-state unions  
Depends on: P017 L035, L039–L041  
Discipline: **this note does not prove Legendre's conjecture.** It adds no sieve formalism. Canonical L041 handles anchor-surviving support closure; the present L042 instead aggregates already-known large-modulus hits across least-factor shells.

## 1. Position after canonical L041

Canonical L041 answers an exact-support question after a transverse support product has hit the square basin. The present question is different.

L036 and L040 bound three-prime states separately inside each least-factor shell. If those shellwise bounds are simply added, the same cofactor resource prime may be counted again in another shell.

L039 already gives more information than a shell-counting argument uses: whenever a modulus `d>=2k` hits the basin, the hit state is unique and explicit. Therefore cross-shell aggregation should deduplicate **realized hit states**, not merely count eligible moduli.

---

## 2. Triple-eligible least primes

Let

\[
U=(k+1)^2-1.
\]

A high-band three-prime state has the form

\[
n=p\ell s,
\qquad
p\le \ell\le s,
\qquad
p^2\ge2k.
\]

Necessarily

\[
p^3\le n\le U.
\]

Define the finite least-prime set

\[
\mathcal P_H(k)
=
\{p\le k:p\text{ prime},\ p^2\ge2k,\ p^3\le U\}.
\]

Only primes in this set can support a high-band three-prime state.

---

## 3. Exact hit-state capacity of one resource prime

Fix a prime `r` used as one of the two cofactor primes of a triple state.

If a state

\[
n=p\ell s
\]

uses `r`, then

\[
p\le r.
\]

The other cofactor prime is at least `p`, so

\[
n\ge p^2r.
\]

Thus define the eligible least-prime set

\[
\mathcal E_r(k)
=
\{p\in\mathcal P_H(k):p\le r,\ p^2r\le U\}.
\]

For every `p` in this set,

\[
pr\ge p^2\ge2k.
\]

Hence L039 implies that `pr` has at most one hit in the open square basin. When the hit exists, denote its unique state by

\[
x_{p,r}(k).
\]

Define the realized hit-state union

\[
X_r(k)
=
\{x_{p,r}(k):p\in\mathcal E_r(k),\ H_{pr}(k)=1\},
\]

where equal states produced by different moduli are counted once, and define

\[
c_r(k)=|X_r(k)|.
\]

This is an exact finite integer capacity.

It automatically satisfies

\[
c_r(k)
\le
\sum_{p\in\mathcal E_r(k)}H_{pr}(k)
\]

and

\[
c_r(k)\le H_r(k),
\]

because every realized state is itself a basin multiple of `r`. The union can be strictly smaller than both cruder counts because different moduli `pr` can realize the same state.

---

## 4. Exact square-cofactor correction

Let `E_H(k)` denote the number of high-band three-prime states whose cofactor is a prime square `r^2`.

For one least prime `p`, the high-band cofactor window has length at most `p`, hence span at most `p-1`. Two distinct squares with roots at least `p` differ by more than this span, so at most one prime square can occur in that window.

Moreover, if a prime `r>=p` satisfies

\[
r^2\in W_p(k),
\]

then `r^2` is automatically `p`-rough. Therefore

\[
p r^2
\]

is genuinely a three-prime state in the least-factor-`p` shell.

Consequently `E_H(k)` is exactly the finite number of pairs `(p,r)` satisfying

\[
p\in\mathcal P_H(k),
\qquad
r\text{ prime},
\qquad
p\le r,
\qquad
r^2\in W_p(k).
\]

It is not an unknown error term.

---

## 5. L042 — Global hit-union resource bound

Status: `PROVED`.

Let `T_H(k)` be the total number of high-band three-prime states across all least-factor shells. Then

\[
\boxed{
2T_H(k)-E_H(k)
\le
\sum_r c_r(k).
}
\]

Therefore

\[
\boxed{
T_H(k)
\le
\left\lfloor
\frac{E_H(k)+\sum_r c_r(k)}{2}
\right\rfloor.
}
\]

Only finitely many resource primes occur, because every resource in a least-factor-`p` triple satisfies

\[
r\le\left\lfloor\frac{U}{p^2}\right\rfloor.
\]

### Proof

For each high-band triple state

\[
n=p\ell s,
\]

let

\[
S(n)=\{\ell,s\}
\]

be the set of its cofactor prime resources. A nonsquare cofactor has `|S(n)|=2`, while a square cofactor has `|S(n)|=1`. Hence

\[
\sum_n |S(n)|=2T_H(k)-E_H(k).
\]

Fix a resource prime `r`, and let `u_r(k)` be the number of actual high-band triple states whose cofactor support contains `r`.

Take any such state. Its least prime `p` belongs to `P_H(k)`. Since `r` is a cofactor prime, the other cofactor prime is at least `p`, so

\[
p\le r,
\qquad
p^2r\le n\le U.
\]

Thus `p` belongs to `E_r(k)`. The state is divisible by `pr`; because `pr>=2k`, L039 says that the modulus has at most one basin hit. The actual state must therefore be exactly `x_(p,r)(k)` and hence belongs to `X_r(k)`.

Therefore

\[
u_r(k)\le c_r(k).
\]

Summing over resource primes gives

\[
2T_H(k)-E_H(k)
=
\sum_r u_r(k)
\le
\sum_r c_r(k),
\]

which proves the theorem. ∎

---

## 6. Exact cross-shell collision witness

At

\[
k=110,
\qquad
r=19,
\]

the two eligible moduli

\[
17\cdot19
\qquad\text{and}\qquad
19^2
\]

both hit the same basin state

\[
12274.
\]

Thus two binary modulus hits occupy only one realized resource-19 state slot:

\[
X_{19}(110)=\{12274\},
\qquad
c_{19}(110)=1.
\]

This is the common-center phenomenon that survives the earlier falsification work. L042 does **not** claim that hit bits are statistically sparse. It only uses exact collisions among the states they realize.

---

## 7. Regression checkpoints

The executable tests compare L042 with the actual high-band triple states over a bounded range of `k`.

At `k=110`,

\[
\sum_r c_r(110)=7,
\qquad
E_H(110)=1,
\]

so

\[
T_H(110)\le4.
\]

The sum of the already-combined shellwise L036/L040 bounds is `5`, so the cross-shell union is strictly stronger at this checkpoint.

At `k=500`,

\[
\sum_r c_r(500)=33,
\qquad
E_H(500)=1,
\]

and hence

\[
T_H(500)\le17.
\]

These values are retained as implementation regressions, not as asymptotic claims.

---

## 8. Research consequence

L042 is the first result on this route that aggregates high-band three-prime resources across different least-factor shells without assuming an average sieve density.

It also further compresses the P017 vocabulary:

\[
H_d(k)
\longrightarrow
\text{L039 unique hit state}
\longrightarrow
\text{L042 cross-shell state union}.
\]

Canonical L041 remains orthogonal: it decides exact transverse-support closure after a large-support hit; L042 counts how many state slots a cofactor resource can occupy across least-factor shells.

The unresolved pieces are now sharply separated:

1. semiprime states `p q` with prime cofactor `q`;
2. lower least-factor shells satisfying `p^2<2k`;
3. a uniform analytic upper envelope for the exact finite quantity
   \[
   \sum_r c_r(k).
   \]

The next step should attack one of these three pieces or connect them. Another equivalent encoding of the same binary hits should not be introduced.
