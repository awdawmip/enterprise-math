# Legendre Pressure Test — Supplement 09

Status: `ACTIVE RESEARCH NOTE`  
Scope: multiplicative prime-resource capacity in the high least-factor band  
Depends on: P017 L021, L030–L036, and L037–L039  
Discipline: this supplement does not prove Legendre's conjecture. It strengthens one finite high-band counting bound by using the sizes of the already-separated prime resources, not only their number.

## 1. Why L036 is not the end of the resource argument

In the high least-factor band

\[
p^2\ge 2k,
\]

P017 already proves two decisive facts:

1. the cofactor window `W_p(k)=[A,B]` has length at most `p`;
2. distinct `p`-rough cofactor survivors in that window are pairwise coprime.

For a three-prime shell state

\[
n=p\ell s,
\qquad
p\le \ell\le s,
\]

L036 uses only the number of available prime resources. If

\[
K_p=\left\lfloor\frac{(k+1)^2-1}{p^2}\right\rfloor
\]

and

\[
R_p=\#\{r\text{ prime}:p\le r\le K_p\},
\]

then

\[
T_p\le\left\lfloor\frac{R_p+1}{2}\right\rfloor,
\]

where `T_p` counts three-prime states in the least-factor-`p` shell.

This additive resource count ignores the magnitudes of the primes. The present supplement keeps exactly the same resource separation but multiplies the resources instead of only counting them.

---

## 2. Setup

Let

\[
U=(k+1)^2-1
\]

be the upper endpoint of the open square basin, and let

\[
A=\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\qquad
B=\left\lfloor\frac{U}{p}\right\rfloor.
\]

Thus

\[
W_p(k)=[A,B].
\]

In the high band `p^2>=2k`, every three-prime state has the form

\[
n_i=pq_i,
\qquad
q_i=\ell_i s_i,
\]

with primes

\[
p\le\ell_i\le s_i\le K_p.
\]

Let

\[
\mathcal R_{p,k}
=
\{r\text{ prime}:p\le r\le K_p\}
\]

and define its product

\[
P_{p,k}=\prod_{r\in\mathcal R_{p,k}}r.
\]

The empty product is `1`.

### Prime-square allowance

Because `|W_p(k)|<=p`, its span is at most `p-1`. Two distinct squares with roots at least `p` differ by at least

\[
(p+1)^2-p^2=2p+1>p-1.
\]

Hence `W_p(k)` contains at most one square whose root is a prime at least `p`.

Define

\[
\xi_{p,k}
=
\begin{cases}
r,&\text{if a prime }r\in\mathcal R_{p,k}\text{ satisfies }r^2\in[A,B],\\
1,&\text{otherwise.}
\end{cases}
\]

This quantity is determined from the window and the finite resource interval before enumerating the three-prime states.

---

## 3. L040 — Multiplicative high-band resource capacity

Status: `PROVED`.

Let the three-prime cofactors in the least-factor-`p` shell be

\[
q_1,\ldots,q_{T_p}.
\]

Then

\[
\boxed{
\prod_{i=1}^{T_p}q_i\mid \xi_{p,k}P_{p,k}.
}
\]

Consequently,

\[
\boxed{
A^{T_p}
\le
\prod_{i=1}^{T_p}q_i
\le
\xi_{p,k}P_{p,k}.
}
\]

Define the integer multiplicative capacity

\[
C_\times(k,p)
=
\max\{t\in\mathbb N_0:A^t\le \xi_{p,k}P_{p,k}\}.
\]

Then

\[
\boxed{T_p\le C_\times(k,p).}
\]

Combining this with L036 gives

\[
\boxed{
T_p
\le
\min\left(
C_\times(k,p),
\left\lfloor\frac{R_p+1}{2}\right\rfloor
\right).
}
\]

No logarithm is required: `C_x` is computed by repeated exact integer multiplication until the next power of `A` would exceed the finite resource product.

### Proof

By L035, distinct high-band `p`-rough cofactor survivors are pairwise coprime. Therefore distinct three-prime cofactors have disjoint prime supports.

Each non-square cofactor

\[
q_i=\ell_i s_i,
\qquad \ell_i<s_i,
\]

uses two different primes from `R_(p,k)`, each exactly once in the total cofactor product.

A square cofactor has the form

\[
q_i=r^2.
\]

There can be at most one such cofactor in the window. Its root `r` is already one of the primes occurring once in `P_(p,k)`, so exactly one additional copy of `r` is required. That additional copy is precisely `xi_(p,k)`.

Hence the product of all three-prime cofactors divides

\[
\xi_{p,k}P_{p,k}.
\]

Every `q_i` lies in `[A,B]`, so `q_i>=A`, and therefore

\[
A^{T_p}\le\prod_i q_i.
\]

The definition of `C_x(k,p)` now gives `T_p<=C_x(k,p)`. The final combined bound is the minimum of this inequality and L036. ∎

---

## 4. Why the square allowance is canonical

Suppose a prime `r>=p` satisfies

\[
r^2\in W_p(k).
\]

Then `r^2` has no prime divisor below `p`, so it is automatically `p`-rough. Therefore

\[
p r^2
\]

is genuinely a three-prime state in the least-factor-`p` shell.

Thus the exceptional repeated resource is not a guessed safety factor. If it exists, the square branch is forced by the exact cofactor window itself.

---

## 5. Exact checked examples

### Example A — multiplicative capacity rules out a triple

Take

\[
k=12,
\qquad p=5.
\]

Then

\[
W_5(12)=[29,33],
\qquad
K_5=6.
\]

The only prime resource in `[5,6]` is `5`, so

\[
P_{5,12}=5,
\qquad
\xi_{5,12}=1.
\]

Since

\[
29>5,
\]

we get

\[
C_\times(12,5)=0.
\]

The additive L036 bound still allows one three-prime state, while L040 proves there are none.

### Example B — the new bound is sharp and strictly stronger

Take

\[
k=45,
\qquad p=11.
\]

Then

\[
W_{11}(45)=[185,192]
\]

and the resource primes are

\[
11,13,17.
\]

Hence L036 gives

\[
T_{11}\le2.
\]

But

\[
185^2>11\cdot13\cdot17,
\]

so

\[
C_\times(45,11)=1.
\]

The unique actual three-prime cofactor is

\[
187=11\cdot17,
\]

so the multiplicative bound is attained.

### Example C — the unique square branch

Take

\[
k=11,
\qquad p=5.
\]

Then

\[
W_5(11)=[25,28].
\]

The unique prime square is

\[
25=5^2,
\]

so

\[
\xi_{5,11}=5.
\]

The resource product is also `5`, hence the resource limit is `25`, exactly matching the square cofactor.

---

## 6. What L040 does and does not solve

L040 is a genuine strengthening of L036 because it can use the sizes of the finite prime resources, not only their count. Finite regression scans contain many cases where

\[
C_\times(k,p)
<
\left\lfloor\frac{R_p+1}{2}\right\rfloor.
\]

It is nevertheless only a high-band three-prime bound.

It does **not**:

- bound the semiprime states `p*q` with prime cofactor `q`;
- prove that every high-band shell is small enough to force a prime in the whole square basin;
- improve every value of `(k,p)`—sometimes the additive L036 bound is stronger;
- bypass classical rough-number or Jacobsthal difficulties in arbitrary short intervals.

The correct object is therefore the combined bound, not L040 alone.

---

## 7. Audit consequence and next target

The recent common-center correlation search produced no universal sparsity law for raw hit bits or for successful prime-tail branches. That route should not be promoted further without a new deterministic inequality.

L040 survives the audit because it extracts a new inequality from a structure already proved in L035: **prime resources are not reusable across high-band cofactor survivors.**

The next useful question is correspondingly narrower:

> Can the multiplicative capacity be aggregated across least-factor shells, or coupled to the semiprime part, strongly enough to bound the total number of composite states in a square basin?

If the answer remains negative, the high-band rough-window route should stop at the exact finite reductions already obtained rather than accumulate more equivalent descriptions.
