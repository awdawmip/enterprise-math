# Legendre Pressure Test — Supplement 10

Status: `ACTIVE RESEARCH NOTE`  
Scope: anchor-surviving support closure after the canonical large-modulus hit theorem  
Depends on: P017 L016 and L039; numbered after canonical L040  
Discipline: **this note does not prove Legendre's conjecture.** It removes a support-language ambiguity left by earlier WIP and keeps only the part not already absorbed by L039.

## 1. What L039 already solved

Let

\[
I_k=\{n\in\mathbb N:k^2<n<(k+1)^2\},
\qquad M=k(k+1).
\]

L039 already proves that every modulus \(d\ge 2k\) has at most one hit in \(I_k\), and gives its exact common-center residue criterion. Therefore a separate "large support incidence" theorem would only rename L039.

The remaining useful question is different:

> after a square-free product of transverse primes hits the basin, when does that hit have **exactly** the proposed transverse support rather than silently acquiring another small transverse prime through its cofactor?

This supplement answers that question and fixes the missing anchor-survival qualifier in the older WIP route.

---

## 2. Setup

Let \(A_k\) be the product of all primes \(a\le k\) dividing the center \(M=k(k+1)\). Call a prime \(p\le k\) **transverse** when

\[
p\nmid M.
\]

Let \(P\) be a finite nonempty set of transverse primes and put

\[
G_P=\prod_{p\in P}p.
\]

Assume

\[
\boxed{G_P>2k.}
\]

If L039 gives a hit, write it uniquely as

\[
\boxed{n=G_Ph.}
\]

Because \(G_P>2k\) and \(n<(k+1)^2\), L016 gives

\[
\boxed{h\le\left\lfloor\frac{k+1}{2}\right\rfloor\le k.}
\]

Thus every prime divisor of \(h\) is itself a small prime at most \(k\).

We call the hit **anchor-surviving** when

\[
\boxed{\gcd(n,A_k)=1.}
\]

Since every prime in \(P\) is transverse, this is equivalent to saying that the cofactor \(h\) contains no anchor prime.

---

## 3. L041 — Anchor-surviving smooth-closure criterion

Status: `PROVED`.

Under the setup above, suppose the unique hit \(n=G_Ph\) is anchor-surviving. Then

\[
\boxed{
\operatorname{Supp}_{\mathrm{tr}}(n)=P
\iff
\operatorname{PrimeSupp}(h)\subseteq P.
}
\]

Equivalently: among anchor-surviving large-support hits, the proposed transverse support is exact if and only if the half-scale cofactor is \(P\)-smooth.

### Proof

Every prime divisor \(q\mid h\) satisfies \(q\le h\le k\). Anchor survival implies \(q\nmid A_k\), hence \(q\nmid M\). Therefore every prime divisor of \(h\) is a transverse small prime.

If the full transverse support of \(n\) is exactly \(P\), any such \(q\mid h\) must already belong to \(P\). Hence

\[
\operatorname{PrimeSupp}(h)\subseteq P.
\]

Conversely, if every prime divisor of \(h\) belongs to \(P\), then all prime divisors contributed by the cofactor are already present in \(G_P\). Since each member of \(P\) divides \(G_P\), the full transverse support is exactly \(P\). ∎

The multiplicity of a prime inside \(h\) is irrelevant: closure is a support condition, not a square-free condition.

---

## 4. Positive example

Take

\[
k=16,
\qquad P=\{5,11\},
\qquad G_P=55>32.
\]

The center is

\[
M=16\cdot17=272.
\]

L039 gives the unique hit

\[
n=275=55\cdot5.
\]

The hit is anchor-surviving. Its cofactor is \(h=5\), which is \(P\)-smooth. Hence

\[
\operatorname{Supp}_{\mathrm{tr}}(275)=\{5,11\}.
\]

---

## 5. Why anchor survival is necessary

Take

\[
k=10,
\qquad P=\{3,7\},
\qquad G_P=21>20.
\]

The center is \(M=110\), and L039 gives

\[
n=105=21\cdot5.
\]

Here \(5\mid M\), so \(5\) is an anchor prime and the hit is **not** anchor-surviving.

Nevertheless

\[
\operatorname{Supp}_{\mathrm{tr}}(105)=\{3,7\}=P,
\]

while \(h=5\) is not \(P\)-smooth.

Therefore the unqualified statement

\[
\operatorname{Supp}_{\mathrm{tr}}(n)=P
\iff
\operatorname{PrimeSupp}(h)\subseteq P
\]

is false. The anchor-survival qualifier in L041 is logically necessary, not stylistic.

---

## 6. Relation to the active P017 route

L041 does not create a second large-modulus route. Its role is only to sharpen what happens **after** the canonical L039 hit bit fires:

\[
\boxed{
\text{L039 unique hit}
\longrightarrow
\text{half-scale cofactor }h
\longrightarrow
\text{L041 support-closure test}.
}
\]

This can be reused when a later argument groups states by proposed transverse support. In particular, a support product may hit the basin but still fail to represent an exact support class because its cofactor introduces an additional transverse prime.

The former WIP four-support graph-tail aggregation is not promoted here: its historical implementation depended on a missing module, so it remains noncanonical until independently reconstructed and audited.

---

## 7. Executable validation

`src/enterprise_math/p017_support_closure.py` and `tests/test_p017_support_closure.py` check that:

- the reused common-center hit agrees with direct basin enumeration for bounded transverse support products;
- every hit with \(G_P>2k\) has the L016 half-scale cofactor bound;
- L041 holds over bounded anchor-surviving hits;
- \((k,P)=(16,\{5,11\})\) is a positive smooth-closure example;
- \((k,P)=(10,\{3,7\})\) is the explicit counterexample to the unqualified statement.

Finite tests audit the implementation; the proof of L041 is the elementary integer argument above.
