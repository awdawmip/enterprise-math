# P017 — P2/Chen Carry Bridge, Supplement 03

Status: `PROVED_WIP EXACT SWITCHING GEOMETRY + PRIME-GAP REDUCTION / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-24`

Researcher-ID: `EM-PRIMEBRC-7F3A21`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Scope: expose the exact ordered-window and gap structure after Chen switching of the super-root binary carry family.

---

## 1. Switched prime windows

Put

\[
U=K^2+2K=(K+1)^2-1.
\]

Fix an odd positive integer `d`. For an odd positive quotient `q`, define the switched prime window

\[
\boxed{
J_{d,q}(K)
=
\left[
\left\lfloor\frac{K^2}{dq}\right\rfloor+1,
\left\lfloor\frac{U}{dq}\right\rfloor
\right]\cap\mathbb N.
}
\]

Thus

\[
p\in J_{d,q}(K)
\iff
K^2<pdq<(K+1)^2.
\]

The binary incidence has the exact switched representation

\[
\boxed{
O_{pd}(K)
=
\#\{q\text{ odd}:p\in J_{d,q}(K)\}.
}
\]

When `pd>K`, the quotient satisfies `q<=K`, and only one odd `q` can occur.

---

## 2. P2-R14 — Consecutive odd switched windows are strictly separated

Let `q` be odd and `q+2<=K`. Then

\[
\boxed{
\max J_{d,q+2}(K)
<
\min J_{d,q}(K).
}
\]

### Proof

It is enough to prove

\[
\frac{U}{d(q+2)}
\le
\frac{K^2}{dq}.
\]

After cancelling `dK>0`, this is

\[
q(K+2)\le K(q+2),
\]

or simply

\[
q\le K.
\]

The assumed `q+2<=K` is stronger. Taking floors and adding one to the lower endpoint gives strict separation. ∎

This extends the cofactor-window separation mechanism from prime labels to every odd quotient channel. Primality of `q` is irrelevant.

---

## 3. Exact jitter-gap count

Write

\[
A_{d,q}
=
\left\lfloor\frac{K^2}{dq}\right\rfloor,
\qquad
B_{d,q}
=
\left\lfloor\frac{U}{dq}\right\rfloor.
\]

For consecutive odd channels define the number of uncovered integer prime coordinates between them by

\[
\boxed{
G_{d,q}(K)
=
A_{d,q}-B_{d,q+2}.
}
\]

P2-R14 gives `G_(d,q)>=0`. The actual missing coordinates are

\[
B_{d,q+2}<p\le A_{d,q}.
\]

The real, pre-floor gap is

\[
\begin{aligned}
\Delta_{d,q}(K)
&=
\frac{K^2}{dq}
-
\frac{U}{d(q+2)}\\
&=
\boxed{
\frac{2K(K-q)}{dq(q+2)}.
}
\end{aligned}
\]

Consequently,

\[
\boxed{
0\le G_{d,q}(K)
\le
\left\lceil
\frac{2K(K-q)}{dq(q+2)}
\right\rceil.
}
\]

In particular,

\[
dq(q+2)>2K(K-q)
\Longrightarrow
G_{d,q}(K)\le1.
\]

Thus high quotient channels and/or large smooth labels `d` leave at most singleton jitter holes.

---

## 4. P2-R15 — Exact telescoping of all switched gaps

Let

\[
q_j=Q+2j
\qquad(0\le j\le N)
\]

be consecutive odd integers with `q_N<=K`. Then

\[
\boxed{
\sum_{j=0}^{N-1}G_{d,q_j}(K)
=
A_{d,q_0}
-B_{d,q_N}
-
\sum_{j=1}^{N-1}H_{dq_j}(K).
}
\]

### Proof

By definition,

\[
\sum_{j=0}^{N-1}G_{d,q_j}
=
\sum_{j=0}^{N-1}
\bigl(A_{d,q_j}-B_{d,q_{j+1}}\bigr).
\]

Separate the two boundary terms and pair the interior terms:

\[
=
A_{d,q_0}-B_{d,q_N}
+
\sum_{j=1}^{N-1}
\bigl(A_{d,q_j}-B_{d,q_j}\bigr).
\]

Since

\[
H_{dq_j}(K)=B_{d,q_j}-A_{d,q_j},
\]

the stated identity follows. ∎

The total hole count is therefore not an independent sum of floor errors. It is an exact boundary span minus the total occupied switched-window mass.

---

## 5. P2-R16 — Long interval minus jitter-gap primes

Because the windows are ordered and disjoint, their union lies in the single outer interval

\[
[A_{d,q_N}+1,B_{d,q_0}].
\]

Let `pi([a,b])` denote the number of primes in the integer interval `[a,b]`. Then

\[
\boxed{
\begin{aligned}
\sum_{j=0}^{N}
\pi\bigl(J_{d,q_j}(K)\bigr)
={}&
\pi\bigl([A_{d,q_N}+1,B_{d,q_0}]\bigr)\\
&-
\sum_{j=0}^{N-1}
\pi\bigl([B_{d,q_{j+1}}+1,A_{d,q_j}]\bigr).
\end{aligned}
}
\]

This is an exact prime-count identity: the switched family is one long prime interval with the explicit floor-jitter gaps deleted.

A sufficient condition for at least one switched prime incidence is therefore

\[
\pi\bigl([A_{d,q_N}+1,B_{d,q_0}]\bigr)
>
\sum_{j=0}^{N-1}G_{d,q_j}(K),
\]

or any sharper estimate replacing the right-hand side by the actual number of primes in the gaps.

---

## 6. Gap states are exactly multiplicative basin skips

A missing integer `p` in the gap between channels `q` and `q+2` satisfies

\[
pdq\le K^2,
\qquad
pd(q+2)>U.
\]

Thus increasing the odd quotient by its primitive parity step `2` jumps completely across the square basin. The jump size is

\[
2pd>2K.
\]

Hence the gap set is not arbitrary deletion noise. It consists exactly of multiplicative step states whose next odd quotient overshoots the entire width-`2K` basin.

This gives a native P017 interpretation:

\[
\boxed{
\text{switched-window gap}
=
\text{odd-quotient carry skip across the square basin}.
}
\]

---

## 7. Consequence for the two-dimensional remainder

For fixed `d`, the switched high-prime sum is no longer a collection of unrelated short intervals. It decomposes into

\[
\boxed{
\text{long interval prime mass}
-
\text{prime mass on an explicit Beatty/floor-jitter gap set}.
}
\]

The long interval term is classical. The square-specific unresolved object is the prime occupancy of

\[
\bigcup_q
(B_{d,q+2},A_{d,q}],
\]

whose sizes and total cardinality obey P2-R14 and P2-R15.

This is a genuine structural compression, but it does not yet prove the required upper bound: singleton or short jitter gaps can still contain primes with ordinary prime density. A positive next step must exploit cancellation/averaging across `d`, a prime-gap theorem strong enough for the declared range, or further arithmetic restrictions on the gap coordinates.

---

## 8. Updated frontier

`SWITCHED_ODD_WINDOWS = STRICTLY_ORDERED_AND_DISJOINT`.

`TOTAL_SWITCHED_GAP_MASS = EXACTLY_TELESCOPING`.

`SWITCHED_PRIME_SUM = LONG_INTERVAL_MINUS_JITTER_GAP_PRIMES`.

`PRIME_OCCUPANCY_OF_MULTI-d JITTER_GAPS = OPEN`.

No Legendre theorem and no all-`K` P2 theorem is claimed.