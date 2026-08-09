# Legendre Pressure Test — Supplement 17

Status: `ACTIVE RESEARCH NOTE`  
Scope: full multiplicity-preserving `k`-smooth core and the unique possible large-prime tail of a square-basin state  
Depends on: P017 L001 root-factor horizon and the canonical square basin  
Discipline: smooth numbers, prime factorization, and valuations are established arithmetic. The project-specific content is the exact square-basin consequence that after *all* prime powers at or below the root cutoff are removed, at most one prime factor can remain above the cutoff.

## 1. Why squarefree support is no longer enough

The existing P017 mirror route often records only the squarefree support of small transverse primes. That is the right object for Möbius cancellation and sign-pattern CRT encoding, but it deliberately forgets multiplicity.

For later bounded-capacity arguments, multiplicity can matter. For example, in the `k=16` basin,

\[
279=3^2\cdot31.
\]

The squarefree small support is only `{3}`, while the complete small-prime contribution is `3^2=9`.

The larger modulus can reduce the number of bounded CRT lifts. We therefore isolate the multiplicity-preserving object before using it in the mirror route.

---

## 2. Definition — full k-smooth core and large tail

Let

\[
I_k=\{n\in\mathbb N:k^2<n<(k+1)^2\}.
\]

For `n in I_k`, define the **full `k`-smooth core**

\[
\boxed{
S_k(n)
=\prod_{p\le k}p^{v_p(n)}.
}
\]

All multiplicities are retained.

Define the residual tail

\[
\boxed{
Q_k(n)=\frac{n}{S_k(n)}.
}
\]

By construction, every prime factor of `Q_k(n)` is strictly larger than `k`.

---

## 3. L053 — Single-large-tail classification

Status: `PROVED`.

For every `n in I_k`,

\[
\boxed{
Q_k(n)=1
\quad\text{or}\quad
Q_k(n)\text{ is a prime }>k.
}
\]

There is no third possibility.

### Proof

Assume `Q_k(n)>1`.

Every prime factor of `Q_k(n)` is at least `k+1`. If the tail were composite, it would contain at least two prime factors counted with multiplicity, so

\[
Q_k(n)\ge(k+1)^2.
\]

But

\[
Q_k(n)\le n<(k+1)^2,
\]

a contradiction.

Hence `Q_k(n)` is prime. Its prime factors were all removed up to `k`, so this prime is strictly larger than `k`. ∎

This is an exact finite consequence of the root cutoff, not a density statement.

---

## 4. Exact primality criterion in smooth-core coordinates

Status: `PROVED`.

For every `n in I_k`,

\[
\boxed{
n\text{ is prime}
\iff
S_k(n)=1.
}
\]

### Proof

If `n` is prime then `n>k^2>=k`, so it contributes no prime factor at or below `k`; therefore `S_k(n)=1`.

Conversely, if `S_k(n)=1`, then `n` has no prime divisor at or below `k`. L001 / the square-basin root-factor horizon says every composite state in `I_k` has such a divisor. Therefore `n` is prime. ∎

Thus the prime-count question can be stated as existence of a basin state with trivial full smooth core.

---

## 5. Bounded core when a large tail exists

Status: `PROVED`.

If

\[
Q_k(n)>1,
\]

then

\[
\boxed{S_k(n)\le k.}
\]

Indeed L053 gives `Q_k(n)>=k+1`, while

\[
n<(k+1)^2.
\]

Hence

\[
S_k(n)
=\frac{n}{Q_k(n)}
<k+1,
\]

and `S_k(n)` is an integer.

For a composite state in this branch,

\[
\boxed{
2\le S_k(n)\le k,
\qquad
n=S_k(n)\,Q_k(n),
\qquad
Q_k(n)>k\text{ prime}.
}
\]

This is the precise form of the parity-sensitive prime-tail branch.

---

## 6. The other branch is fully k-smooth

If

\[
Q_k(n)=1,
\]

then

\[
\boxed{n=S_k(n)}
\]

and every prime factor of `n` lies at or below `k`.

Thus every composite square-basin state belongs to exactly one of two classes:

### Fully smooth branch

\[
\boxed{n=S_k(n),\qquad Q_k(n)=1.}
\]

### Single-large-prime-tail branch

\[
\boxed{
2\le S_k(n)\le k,
\qquad
n=S_k(n)Q_k(n),
\qquad
Q_k(n)>k\text{ prime}.
}
\]

No composite state can carry two residual prime factors above `k`.

---

## 7. Why multiplicity matters for the mirror route

Take the surviving `k=16`, `r=7` mirror pair around

\[
M=16\cdot17=272:
\]

\[
M-r=265=5\cdot53,
\]

\[
M+r=279=3^2\cdot31.
\]

The squarefree small-support products are

\[
D_-=5,
\qquad
D_+=3,
\qquad
D=15<k.
\]

The full smooth cores are instead

\[
S_-=5,
\qquad
S_+=9,
\qquad
S=S_-S_+=45\ge k.
\]

So a CRT modulus that retains multiplicity can be strictly larger than the old squarefree support modulus.

This does not by itself prove a new bounded-lift theorem; it identifies the exact information needed for the next step.

---

## 8. Mirror corollary in the prime-tail branch

Let `r` be an anchor-surviving mirror radius and suppose both mirror states are composite and both lie in the single-large-prime-tail branch:

\[
M-r=S_-P_-,
\qquad
M+r=S_+P_+,
\]

where

\[
2\le S_-,S_+\le k
\]

and `P_-,P_+>k` are prime.

The surviving mirror pair is pairwise coprime by the canonical mirror theorem. Therefore

\[
\boxed{\gcd(S_-,S_+)=1.}
\]

Moreover the complete state factorization is already exhausted by one bounded full smooth core and one large prime tail on each side.

The hardest subcase is now explicit:

- if a smooth core contains multiple small primes or a repeated prime power, its full modulus is larger than its squarefree support product;
- the smallest-capacity gain occurs when the core is just one small prime to exponent one.

That exponent-one singleton-core branch is the genuine parity hard core isolated by this classification.

---

## 9. What this theorem does not do

L053 does **not** prove that the prime-tail branch is rare.

It does not bound how often two affine large tails are simultaneously prime in a mirror CRT cell.

It does not break the sieve parity barrier.

Its role is classification and information preservation: later capacity arguments may no longer discard prime-power multiplicity and then hope to recover it after the fact.

---

## 10. Executable validation

`src/enterprise_math/p017_smooth_core.py` provides:

- `square_basin_smooth_core`;
- `square_basin_smooth_core_profile`.

`tests/test_p017_smooth_core.py` checks that:

- every residual tail is `1` or one prime `>k`;
- `n` is prime exactly when `S_k(n)=1`;
- a nontrivial large tail leaves `S_k(n)<=k`;
- prime-power multiplicity is preserved, including the `279=3^2*31` witness;
- complete basin profiles partition all `2k` interior states.

Finite computation audits the implementation; L053 is proved by the elementary square-basin argument above.

---

## 11. Next target

The next justified step is a **full-core mirror CRT upgrade**.

For a prime-tail mirror pair, use

\[
S=S_-S_+
\]

rather than only the squarefree product of distinct small primes. Because `S_-` and `S_+` are coprime, the same sign/idempotent encoding should recover the complete prime-power cores.

The key capacity question is whether the larger full-core modulus gives a strict bounded-radius improvement while remaining only a refinement of the already-classical CRT machinery.
