# Legendre Pressure Test — Supplement 05

Status: `ACTIVE RESEARCH NOTE`  
Scope: full square-basin smooth-tail reduction, exact first-factor cofactor windows, quotient-transport window growth, and a positive rough-window prime-count identity  
Depends on: P017 L001–L019 and P018 factor-precision results  
Discipline: **this note does not prove Legendre's conjecture.** Rough numbers, least-prime-factor partitions, smooth parts, and trial-division logic are established number theory. The project question is whether their exact square-basin organization produces new proof leverage.

## 1. Audit: which recent ideas survive as proof tools?

The recent pressure tests introduced several mathematically valid structures, but they do not all deserve equal foundational weight.

This supplement keeps the pieces that directly reduce the P017 proof problem:

1. the exact finite factor horizon and least-factor partition;
2. the full `k`-smooth core of a square-basin state;
3. an exact cofactor interval for every first-factor shell;
4. an exact quotient-transport / carry description of how that interval widens;
5. integer-root depth bounds on the remaining factor multiplicity.

It demotes the following to special cases or proof languages:

- centered symmetric prime pairs — useful only when the general cofactor window has collapsed to two raw candidates;
- carry cocycles / cohomology — established algebraic language; useful only insofar as the quotient-defect transport reappears in the square-basin window width;
- threshold topology / Alexander duality — retained as independent prior-art reductions, not promoted to the base ontology;
- CRT/idempotent or other coordinate encodings — retain only when they produce a new bound.

The guiding rule is now:

> **Keep a new structure only if it shortens the exact finite obstruction or transports useful information between already-existing P017/P018 layers.**

---

## 2. L020 — Square-basin smooth-tail dichotomy

Status: `PROVED`.

For

\[
k^2<n<(k+1)^2,
\]

define the full `k`-smooth core

\[
S_k(n)=\prod_{p\le k}p^{v_p(n)}
\]

and residual tail

\[
Q_k(n)=\frac{n}{S_k(n)}.
\]

Then

\[
\boxed{
Q_k(n)=1
\quad\text{or}\quad
Q_k(n)\text{ is a prime }>k.
}
\]

### Proof

By construction, every prime divisor of `Q_k(n)` is strictly greater than `k`.

If `Q_k(n)>1` were composite, it would contain at least two prime factors counted with multiplicity, each at least `k+1`. Hence

\[
Q_k(n)\ge(k+1)^2.
\]

But

\[
Q_k(n)\le n<(k+1)^2,
\]

a contradiction. ∎

### Primality corollary

For a square-basin state,

\[
\boxed{
n\text{ is prime}
\iff
S_k(n)=1.
}
\]

Thus every composite basin state consists of:

- a nontrivial `k`-smooth core; and
- either no large tail, or exactly one prime tail greater than `k`.

This is stronger bookkeeping than recording only the square-free small-prime support, because all small-prime multiplicities are retained.

---

## 3. L021 — Exact centered cofactor window for a first-factor shell

Status: `PROVED`.

Let `p<=k` be prime and let `L_p(k)` denote the square-basin states whose least prime factor is exactly `p`.

Set

\[
c=k+1,
\qquad
r=c-p,
\qquad
p=c-r.
\]

Every state in `L_p(k)` has the form

\[
n=pq.
\]

Then the square-basin inequalities

\[
(c-1)^2<pq<c^2
\]

are equivalent to the exact finite cofactor window

\[
\boxed{
q_{\min}
=
c+r-1+\left\lfloor\frac{(r-1)^2}{p}\right\rfloor
}
\]

and

\[
\boxed{
q_{\max}
=
c+r+\left\lfloor\frac{r^2-1}{p}\right\rfloor.
}
\]

### Lower endpoint

Since `pq>(c-1)^2`,

\[
q
\ge
\left\lfloor\frac{(c-1)^2}{p}\right\rfloor+1.
\]

Using `c=p+r`,

\[
(c-1)^2
=(p+r-1)^2
=p(p+2r-2)+(r-1)^2,
\]

so

\[
\left\lfloor\frac{(c-1)^2}{p}\right\rfloor+1
=
p+2r-1+\left\lfloor\frac{(r-1)^2}{p}\right\rfloor
=
c+r-1+\left\lfloor\frac{(r-1)^2}{p}\right\rfloor.
\]

### Upper endpoint

Since `pq<c^2`, in integers

\[
q\le\left\lfloor\frac{c^2-1}{p}\right\rfloor.
\]

Again using `c=p+r`,

\[
c^2-1
=p(p+2r)+(r^2-1),
\]

hence

\[
\left\lfloor\frac{c^2-1}{p}\right\rfloor
=
p+2r+\left\lfloor\frac{r^2-1}{p}\right\rfloor
=
c+r+\left\lfloor\frac{r^2-1}{p}\right\rfloor.
\]

This window is exact for every prime shell `p<=k`; no near-diagonal assumption is used.

---

## 4. L022 — First-factor shell equals the p-rough cofactor window

Status: `PROVED`.

Call an integer `q` **p-rough** when it has no prime divisor strictly less than `p`.

Then

\[
\boxed{
L_p(k)
=
\left\{
pq:
q_{\min}\le q\le q_{\max},
\ q\text{ is p-rough}
\right\}.
}
\]

### Proof

If `n=pq` lies in `L_p(k)`, L021 puts `q` in the displayed window. If `q` had a prime divisor `<p`, that divisor would also divide `n`, contradicting that `p` is the least prime factor. Hence `q` is `p`-rough.

Conversely, suppose `q` lies in the exact window and is `p`-rough. L021 gives

\[
k^2<pq<(k+1)^2.
\]

The state is divisible by `p`, and no smaller prime divides `q`; no smaller prime divides the factor `p` either. Therefore the least prime factor of `pq` is exactly `p`, so `pq in L_p(k)`. ∎

This theorem is the principal reduction of this supplement:

> the geometry of the shell is now a short explicit integer interval; the remaining arithmetic obstruction is exactly roughness inside that interval.

---

## 5. L023 — Centered correction coordinate and square-boundary offsets

Status: `PROVED`.

Write a candidate cofactor as

\[
q=c+r+j.
\]

By L021 the correction coordinate lies in

\[
\boxed{
j_{\min}
=-1+\left\lfloor\frac{(r-1)^2}{p}\right\rfloor}
\]

through

\[
\boxed{
j_{\max}
=\left\lfloor\frac{r^2-1}{p}\right\rfloor.}
\]

Since `p=c-r`,

\[
pq=(c-r)(c+r+j)=c^2-r^2+jp.
\]

Therefore the two square-boundary margins are exactly

\[
\boxed{
c^2-pq=r^2-jp}
\]

and

\[
\boxed{
pq-(c-1)^2=p(j+2)-(r-1)^2.}
\]

So the deviation from the symmetric product `c^2-r^2` is not an unspecified error. It is the integer correction `jp`.

The centered-prime formula corresponds only to the special correction `j=0`.

---

## 6. L024 — Raw window width is an exact quotient-transport event

Status: `PROVED`.

The number of raw integer cofactors before the `p`-rough filter is

\[
N_{\mathrm{raw}}
=q_{\max}-q_{\min}+1.
\]

Using L021,

\[
\boxed{
N_{\mathrm{raw}}
=
2
+
\left\lfloor\frac{r^2-1}{p}\right\rfloor
-
\left\lfloor\frac{(r-1)^2}{p}\right\rfloor.
}
\]

Now put

\[
a=(r-1)^2,
\qquad
h=2r-2.
\]

Then

\[
a+h=r^2-1,
\]

so

\[
\boxed{
N_{\mathrm{raw}}
=
2+\left(\left\lfloor\frac{a+h}{p}\right\rfloor-\left\lfloor\frac a p\right\rfloor\right).
}
\]

The parenthesized quantity is exactly a quotient-state transport across an increment `h`.

Writing

\[
a=pA+u,
\qquad
h=pH+v,
\qquad
0\le u,v<p,
\]

gives the direct integer decomposition

\[
\boxed{
N_{\mathrm{raw}}
=
2
+
\left\lfloor\frac{2r-2}{p}\right\rfloor
+
\kappa_p
\left(
(r-1)^2\bmod p,
(2r-2)\bmod p
\right),
}
\]

where

\[
\kappa_p(u,v)=\left\lfloor\frac{u+v}{p}\right\rfloor\in\{0,1\}.
\]

Thus cofactor-window growth has only two pieces:

\[
\boxed{
\text{deterministic full-block growth}
+
\text{one residual boundary carry}.
}
\]

This is exactly the kind of reusable finite defect-transport pattern that survived the P018 audit. The formula above is proved directly here and does not depend on any terminology from that branch.

---

## 7. L025 — Two/three-candidate regime and symmetric-prime degeneration

Status: `PROVED`.

### Two or three raw candidates

If

\[
p>2(r-1),
\]

then

\[
\left\lfloor\frac{2r-2}{p}\right\rfloor=0.
\]

By L024,

\[
\boxed{N_{\mathrm{raw}}\in\{2,3\}.}
\]

Which of the two values occurs is exactly the residual boundary carry.

### Strong near-diagonal case

If the stronger condition

\[
\boxed{p>r^2}
\]

holds, then both floor terms in L021 vanish. Hence

\[
\boxed{
q\in\{c+r-1,c+r\}.
}
\]

For `p>=3`, the prime `p=c-r` is odd. Therefore `c+r=p+2r` is odd and `c+r-1` is even. Since every shell cofactor is `p`-rough and is greater than `p`, the even candidate cannot survive.

Moreover `p>r^2` implies

\[
c+r=p+2r<p^2,
\]

so a `p`-rough composite at `c+r` is impossible: any composite `p`-rough integer greater than `p` is at least `p^2`.

Therefore

\[
\boxed{
L_p(k)\ne\varnothing
\iff
c+r\text{ is prime},
}
\]

and then

\[
\boxed{
L_p(k)=\{(c-r)(c+r)\}
=\{c^2-r^2\}.
}
\]

The previously studied centered-prime radius is therefore not a separate foundational object. It is the **two-candidate degeneration of the general cofactor window**.

### Boundary example: k=10

For

\[
k=10,
\quad c=11,
\quad p=7,
\quad r=4,
\]

L021 gives

\[
q\in\{15,16,17\}.
\]

Only `17` is `7`-rough, hence

\[
L_7(10)=\{7\cdot17\}=\{119\}.
\]

The centered-prime special formula fails here because `7>4^2` is false, but the general cofactor-window theorem remains exact.

---

## 8. L026 — Integer-root depth bounds the remaining factor count

Status: `PROVED`.

Let

\[
U=(k+1)^2-1.
\]

Suppose `p` is the least prime factor of a shell state and

\[
\boxed{p^{m+1}>U.}
\]

Equivalently,

\[
p>R_{m+1}(U).
\]

Then every state `n in L_p(k)` satisfies

\[
\boxed{\Omega(n)\le m,}
\]

where `Omega` counts prime factors with multiplicity.

### Proof

If `Omega(n)>=m+1`, every prime factor of `n` is at least the least one `p`, so

\[
n\ge p^{m+1}>U.
\]

But every basin state satisfies `n<=U`. Contradiction. ∎

Since `n=pq`, the cofactor obeys

\[
\boxed{\Omega(q)\le m-1.}
\]

Thus increasing least-factor precision produces an exact finite hierarchy:

\[
\text{general p-rough cofactor}
\to
\text{bounded factor depth}
\to
\text{prime cofactor}
\to
\text{symmetric-prime degeneration}.
\]

---

## 9. L027 — Positive rough-window prime-count identity

Status: `PROVED REINDEXING`.

The open square basin contains exactly `2k` states.

Every composite state belongs to exactly one first-factor shell `L_p(k)` with prime `p<=k`. Therefore

\[
\Pi(k)
=
2k-
\sum_{p\le k}|L_p(k)|.
\]

Applying L022 gives

\[
\boxed{
\Pi(k)
=
2k-
\sum_{p\le k}
\#\left\{
q\in[q_{\min}(k,p),q_{\max}(k,p)]
:
q\text{ is p-rough}
\right\}.
}
\]

Hence Legendre's conjecture is equivalent to the positive inequality

\[
\boxed{
\sum_{p\le k}
\#\{q\in W_p(k):q\text{ p-rough}\}
\le2k-1.
}
\]

No Möbius signs occur in this representation because composites are partitioned by their unique least prime factor.

This is a reformulation, not a proof. Its value is diagnostic: it isolates the remaining obstruction after the square geometry has been compressed into exact finite windows.

---

## 10. What is now solved geometrically, and what remains hard

The square-basin geometry of a first-factor shell is no longer open:

- exact cofactor endpoints are known;
- exact square offsets are known;
- exact raw candidate count is known;
- window widening has an exact bulk-plus-carry law;
- high least-factor shells have bounded `Omega` depth;
- the centered-prime formula is understood as a limiting degeneration.

The hard part is now sharply located:

\[
\boxed{
\text{control the total number of p-rough survivors inside all exact windows }W_p(k).
}
\]

A proof of Legendre through this route would need a genuinely new upper bound on that total survivor count. Merely renaming roughness, applying inclusion-exclusion termwise, or reintroducing the same parity barrier under new notation does not count as progress.

## 11. Next attacks

Priority directions are now deliberately narrow.

1. **Recursive rough-window factorization.** For a composite `p`-rough cofactor `q`, expose its least factor `p_2>=p` and derive the next exact finite factor/cofactor window instead of returning immediately to global inclusion-exclusion.
2. **Root-depth aggregation.** Sum high-`p` shells by their allowed `Omega` depth, starting with the semiprime layer.
3. **Smooth-core coupling.** Use L020 to determine whether the optional single prime tail `>k` can be separated from the fully `k`-smooth core without losing the common square-center constraint.
4. **Defect-transport reuse.** Use the P018 transport calculus only where it produces an actual shell-count or boundary-crossing identity such as L024; do not import its entire vocabulary into P017.
5. **Counterexample-first gate.** Any proposed upper bound on the total rough-window count must be stress-tested against finite basins before being promoted.

The research line therefore continues with fewer objects than before:

\[
\boxed{
\text{square basin}
\to
\text{least-factor shell}
\to
\text{exact cofactor window}
\to
\text{p-rough survivors}
\to
\text{root-depth recursion}.
}
\]
