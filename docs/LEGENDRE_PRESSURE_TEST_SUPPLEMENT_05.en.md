# Legendre Pressure Test — Supplement 05

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact first-factor cofactor windows and positive rough-window reduction  
Depends on: P017 L001–L019 and the canonical P018 precision/factor tools  
Discipline: **this note does not prove Legendre's conjecture.**

## 1. Why this supplement survives the audit

Let

\[
B_k=\{n\in\mathbb N:k^2<n<(k+1)^2\}.
\]

For each prime \(p\le k\), let \(L_p(k)\) be the states in \(B_k\) whose least prime factor is exactly \(p\).

The useful reduction is not a new primality criterion. It is an exact finite coordinate system for every least-factor shell:

\[
\boxed{\text{square-basin geometry}\longrightarrow\text{short cofactor interval}\longrightarrow\text{p-rough survivors}.}
\]

Rough numbers, least-prime-factor partitions, smooth parts, integer division, and trial-division logic are established number theory. The project-specific question is whether their exact organization inside the consecutive-square basin creates usable proof leverage.

---

## 2. L020 — Square-basin smooth-tail dichotomy

Status: `PROVED`.

For \(n\in B_k\), define the full \(k\)-smooth core

\[
S_k(n)=\prod_{p\le k}p^{v_p(n)}
\]

and the residual tail

\[
Q_k(n)=n/S_k(n).
\]

Then

\[
\boxed{Q_k(n)=1\quad\text{or}\quad Q_k(n)\text{ is a prime }>k.}
\]

### Proof

Every prime divisor of \(Q_k(n)\) is greater than \(k\). If \(Q_k(n)>1\) were composite, it would contain at least two prime factors counted with multiplicity, so

\[
Q_k(n)\ge(k+1)^2.
\]

But \(Q_k(n)\le n<(k+1)^2\), contradiction. ∎

Hence

\[
\boxed{n\text{ is prime}\iff S_k(n)=1.}
\]

---

## 3. L021 — Exact cofactor window

Status: `PROVED`.

Fix a prime \(p\le k\), set

\[
c=k+1,\qquad r=c-p,
\]

and write a shell candidate as \(n=pq\).

The inequalities

\[
(c-1)^2<pq<c^2
\]

are equivalent to

\[
\boxed{
q_{\min}=c+r-1+\left\lfloor\frac{(r-1)^2}{p}\right\rfloor
}
\]

and

\[
\boxed{
q_{\max}=c+r+\left\lfloor\frac{r^2-1}{p}\right\rfloor.
}
\]

### Proof

For the lower endpoint,

\[
(c-1)^2=(p+r-1)^2=p(p+2r-2)+(r-1)^2,
\]

so

\[
q\ge\left\lfloor\frac{(c-1)^2}{p}\right\rfloor+1
=c+r-1+\left\lfloor\frac{(r-1)^2}{p}\right\rfloor.
\]

For the upper endpoint,

\[
c^2-1=p(p+2r)+(r^2-1),
\]

so

\[
q\le\left\lfloor\frac{c^2-1}{p}\right\rfloor
=c+r+\left\lfloor\frac{r^2-1}{p}\right\rfloor.
\]

Both bounds are exact integer bounds. ∎

---

## 4. L022 — First-factor shell equals the p-rough window

Status: `PROVED`.

Call \(q\) **p-rough** when no prime strictly smaller than \(p\) divides \(q\). Then

\[
\boxed{
L_p(k)=
\left\{
pq:q_{\min}\le q\le q_{\max},\ q\text{ is p-rough}
\right\}.
}
\]

### Proof

If \(pq\in L_p(k)\), L021 puts \(q\) in the exact interval. Any prime divisor of \(q\) below \(p\) would also divide \(pq\), contradicting that \(p\) is the least prime factor.

Conversely, an interval candidate \(pq\) lies in \(B_k\) by L021. If \(q\) is p-rough, no prime smaller than \(p\) divides either factor, so the least prime factor of \(pq\) is exactly \(p\). ∎

Thus the remaining arithmetic obstruction after the square geometry is compressed is exactly roughness on a finite explicit interval.

---

## 5. L023 — Centered correction and exact square offsets

Status: `PROVED`.

Write

\[
q=c+r+j.
\]

Then

\[
-1+\left\lfloor\frac{(r-1)^2}{p}\right\rfloor
\le j\le
\left\lfloor\frac{r^2-1}{p}\right\rfloor.
\]

Since \(p=c-r\),

\[
pq=(c-r)(c+r+j)=c^2-r^2+jp.
\]

Therefore the exact distances from the two square boundaries are

\[
\boxed{c^2-pq=r^2-jp}
\]

and

\[
\boxed{pq-(c-1)^2=p(j+2)-(r-1)^2.}
\]

The symmetric product \(c^2-r^2\) is only the special coordinate \(j=0\), not the general shell.

---

## 6. L024 — Window growth is bulk plus one carry

Status: `PROVED`.

The number of raw integer cofactors is

\[
N_{\mathrm{raw}}=q_{\max}-q_{\min}+1,
\]

hence

\[
\boxed{
N_{\mathrm{raw}}
=2+
\left\lfloor\frac{r^2-1}{p}\right\rfloor
-
\left\lfloor\frac{(r-1)^2}{p}\right\rfloor.
}
\]

Set

\[
a=(r-1)^2,\qquad h=2r-2.
\]

Since \(a+h=r^2-1\), the width correction is the exact quotient transport

\[
\left\lfloor\frac{a+h}{p}\right\rfloor-\left\lfloor\frac a p\right\rfloor.
\]

Writing \(a=pA+u\), \(h=pH+v\) with \(0\le u,v<p\) gives

\[
\boxed{
N_{\mathrm{raw}}
=2+
\left\lfloor\frac{2r-2}{p}\right\rfloor
+
\left\lfloor\frac{u+v}{p}\right\rfloor,
}
\]

where the last term is in \(\{0,1\}\).

So the finite window has an exact decomposition

\[
\boxed{\text{two base candidates}+\text{full-block growth}+\text{one boundary carry}.}
\]

This is an arithmetic instance of the exact quotient-defect transport retained in canonical P018; it is not evidence for any new physical interpretation.

---

## 7. L025 — Two/three-candidate regime and the corrected near-diagonal degeneration

Status: `PROVED`.

### Two or three raw candidates

If

\[
p>2(r-1),
\]

then the full-block term in L024 vanishes, so

\[
\boxed{N_{\mathrm{raw}}\in\{2,3\}.}
\]

The choice between two and three is exactly the residual boundary carry.

### Strong near-diagonal theorem

For the symmetric-prime degeneration, the correct sufficient hypotheses are

\[
\boxed{p\ge3\qquad\text{and}\qquad p>r^2.}
\]

The inequality \(p>r^2\) makes both floor terms in L021 vanish, hence

\[
q\in\{c+r-1,c+r\}.
\]

Because \(p\ge3\) is an odd prime and \(c+r=p+2r\) is odd, the first candidate \(c+r-1\) is even, greater than \(p\), and therefore not p-rough.

The second candidate satisfies \(p<c+r<p^2\). A p-rough composite greater than \(p\) would be at least \(p^2\), so within this interval p-roughness is equivalent to primality. Consequently

\[
\boxed{
L_p(k)\ne\varnothing
\iff
c+r\text{ is prime},
}
\]

and when nonempty

\[
\boxed{L_p(k)=\{(c-r)(c+r)\}=\{c^2-r^2\}.}
\]

### Why \(p\ge3\) is necessary

The condition cannot be weakened to \(p>r^2\) alone. At

\[
k=2,\quad c=3,\quad p=2,\quad r=1,
\]

we have \(p>r^2\), but the raw cofactor window is

\[
\{3,4\}.
\]

For \(p=2\), p-roughness excludes no smaller prime at all, so both candidates survive:

\[
L_2(2)=\{6,8\},
\]

while \(c+r=4\) is composite. This is the explicit boundary counterexample that fixes the historical overstatement.

### Three-candidate boundary example

At \(k=10\), \(c=11\), \(p=7\), \(r=4\), L021 gives

\[
q\in\{15,16,17\}.
\]

Only \(17\) is 7-rough, hence

\[
L_7(10)=\{119\}.
\]

The general window remains exact even though the strong near-diagonal hypotheses fail.

---

## 8. L026 — Integer-root depth bounds factor multiplicity

Status: `PROVED`.

Let

\[
U=(k+1)^2-1.
\]

If

\[
\boxed{p^{m+1}>U,}
\]

then every \(n\in L_p(k)\) satisfies

\[
\boxed{\Omega(n)\le m,}
\]

where \(\Omega\) counts prime factors with multiplicity.

### Proof

If \(\Omega(n)\ge m+1\), every prime factor of \(n\) is at least the least one \(p\), so

\[
n\ge p^{m+1}>U,
\]

contradicting \(n\le U\). ∎

Equivalently, the threshold can be stated with the integer root \(p>R_{m+1}(U)\). For \(n=pq\), the same argument gives \(\Omega(q)\le m-1\).

---

## 9. L027 — Positive rough-window prime-count identity

Status: `PROVED REINDEXING`.

The open square basin contains exactly \(2k\) states. Every composite state belongs to one and only one shell \(L_p(k)\) for a prime \(p\le k\). Therefore

\[
\Pi(k)=2k-\sum_{p\le k}|L_p(k)|.
\]

Using L022,

\[
\boxed{
\Pi(k)
=
2k-
\sum_{p\le k}
\#\{q\in[q_{\min}(k,p),q_{\max}(k,p)]:q\text{ is p-rough}\}.
}
\]

Thus Legendre's conjecture is equivalent to

\[
\boxed{
\sum_{p\le k}
\#\{q\in W_p(k):q\text{ is p-rough}\}
\le2k-1.
}
\]

This identity is a positive least-factor reindexing, not a proof of the inequality.

---

## 10. What remains genuinely open

The square geometry and shell coordinates are now explicit. The unresolved proof content is concentrated in one place:

> **Control the total number of p-rough survivors across the correlated family of short windows \(W_p(k)\).**

The exact window formulas may help because they couple the least-factor threshold \(p\), the square center \(c=k+1\), and the offset \(r=c-p\). But no currently proved estimate in this note implies

\[
\Pi(k)>0
\]

for every \(k\).

So the current status remains:

- L020–L026: `PROVED` structural reductions;
- L027: `PROVED REINDEXING`;
- Legendre's conjecture: still open;
- historical novelty of this exact packaging: `NOVELTY_UNVERIFIED`.

The implementation `src/enterprise_math/p017_cofactor_window.py` and its regression suite audit the exact identities, including the \(p=2\) boundary counterexample.
