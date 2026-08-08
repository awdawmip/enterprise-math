# Legendre Pressure Test — Supplement 06

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact least-factor recursion inside the square-basin cofactor windows, high least-factor contraction, and a sieve-density no-shortcut result  
Depends on: P017 L020–L027  
Prior art: rough-number counting and Buchstab least-prime-factor recursion are established sieve theory. [SRC-FAN-2023-ROUGH-NUMBERS] [SRC-LI-2025-BUCHSTAB]  
Discipline: **this note does not prove Legendre's conjecture.** It asks whether the special moving windows forced by consecutive squares give stronger finite constraints than generic rough-number density.

## 1. Why the next step is not a new kind of sieve

L022 reduces each first-factor shell to

\[
L_p(k)=\{pq:q\in W_p(k),\ q\text{ is p-rough}\}.
\]

If a surviving cofactor `q` is composite, the mathematically canonical next operation is to expose its least prime factor. That is standard Buchstab/least-factor recursion, not a new Enterprise Math invention.

The project-specific question is narrower:

> because `W_p(k)` has exact square-derived endpoints and an exact bulk-plus-carry width law, does standard least-factor recursion contract unusually strongly on these windows?

The answer is yes in one explicit high least-factor band.

---

## 2. L028 — Exact finite-interval least-factor recursion

Status: `PROVED SPECIALIZATION OF ESTABLISHED BUCHSTAB-TYPE RECURSION`.

For integers

\[
1\le A\le B
\]

and threshold `z>=2`, let

\[
\mathcal R_z[A,B]
=
\{q\in[A,B]:q\text{ has no prime divisor }<z\}.
\]

Partition this set into prime values and composite values.

If `q` is composite, let

\[
\ell=\operatorname{spf}(q).
\]

Because `q` is `z`-rough,

\[
\ell\ge z.
\]

Write

\[
q=\ell s.
\]

Since `ell` is the least prime factor,

\[
s\ge\ell,
\]

and `s` is `ell`-rough. The interval condition gives

\[
\left\lceil\frac A\ell\right\rceil
\le s\le
\left\lfloor\frac B\ell\right\rfloor.
\]

Hence the composite part of the rough interval is the disjoint union

\[
\boxed{
\mathcal R_z[A,B]_{\rm comp}
=
\coprod_{\substack{\ell\text{ prime}\\
\ell\ge z}}
\left\{
\ell s:
\max\!\left(\ell,\left\lceil\frac A\ell\right\rceil\right)
\le s\le
\left\lfloor\frac B\ell\right\rfloor,
\ s\text{ ell-rough}
\right\}.
}
\]

Only

\[
\ell\le\sqrt B
\]

can contribute.

### Proof

Every composite positive integer has a unique least prime factor. The conditions above follow immediately from unique factorization, the definition of roughness, and division of the interval inequalities by positive `ell`. Conversely every displayed pair `ell,s` has least prime factor `ell`, lies in `[A,B]`, and is therefore a unique composite member of the rough interval. ∎

This is the exact finite-interval form of the standard least-prime-factor/Buchstab decomposition. [SRC-LI-2025-BUCHSTAB]

Applied to P017, take

\[
A=q_{\min}(k,p),
\qquad
B=q_{\max}(k,p),
\qquad
z=p.
\]

---

## 3. L029 — Every child-window length is another quotient response

Status: `PROVED`.

Let the parent interval be `[A,B]`, with length

\[
N=B-A+1.
\]

For a fixed prime `ell`, the number of multiples of `ell` in the parent interval is

\[
M_\ell
=
\left\lfloor\frac B\ell\right\rfloor
-
\left\lfloor\frac{A-1}\ell\right\rfloor.
\]

Since

\[
B=(A-1)+N,
\]

this is exactly

\[
\boxed{
M_\ell
=
Q_\ell((A-1)+N)-Q_\ell(A-1).
}
\]

Thus P018's quotient-response identity applies again:

\[
\boxed{
M_\ell
=
\left\lfloor\frac N\ell\right\rfloor
+
\kappa_\ell((A-1)\bmod\ell,\ N\bmod\ell).
}
\]

In particular,

\[
\boxed{
M_\ell\le\left\lceil\frac N\ell\right\rceil.
}
\]

The actual least-factor child additionally imposes

\[
s\ge\ell,
\]

so its raw length is no larger than `M_ell`.

This gives an exact recursive contraction mechanism:

> extracting the next least prime factor divides the current raw window length by at least that prime, up to one boundary carry.

---

## 4. L030 — High-band parent window bound

Status: `PROVED`.

Return to a P017 cofactor window `W_p(k)`. Let

\[
N_p=|W_p(k)|_{\rm raw}.
\]

L024 gives, with

\[
r=k+1-p,
\qquad
h=2r-2=2k-2p,
\]

that

\[
N_p
=2+\Delta Q_p,
\]

where

\[
\Delta Q_p
=
\left\lfloor\frac{a+h}{p}\right\rfloor
-
\left\lfloor\frac a p\right\rfloor
\le
\left\lceil\frac hp\right\rceil.
\]

Assume

\[
\boxed{p^2\ge2k.}
\]

Then

\[
h=2k-2p
\le p^2-2p
=p(p-2).
\]

Therefore

\[
\left\lceil\frac hp\right\rceil\le p-2,
\]

and hence

\[
\boxed{N_p\le p.}
\]

This is a genuinely square-basin-specific contraction threshold: it uses the exact relation `r=k+1-p` in the P017 window.

---

## 5. L031 — One raw child per second least prime in the high band

Status: `PROVED`.

Under

\[
p^2\ge2k,
\]

let `ell>=p` be a possible second least prime factor of a composite cofactor `q`.

By L029,

\[
M_\ell
\le
\left\lceil\frac{N_p}{\ell}\right\rceil.
\]

Since

\[
N_p\le p\le\ell,
\]

we obtain

\[
\boxed{M_\ell\le1.}
\]

Therefore:

\[
\boxed{
\text{for each possible second least prime }\ell,
\text{ the parent cofactor window contains at most one raw multiple of }\ell.
}
\]

After the additional `s>=ell` and `ell`-rough conditions, a branch may disappear, but it can never split into two candidates.

This turns the second level of Buchstab recursion into a **binary presence/absence branch**.

---

## 6. L032 — High-band factor-depth classification

Status: `PROVED`.

Still assume

\[
p^2\ge2k.
\]

Let

\[
U=(k+1)^2-1.
\]

Then

\[
p^4\ge4k^2.
\]

For every `k>=1`,

\[
4k^2>k^2+2k=U.
\]

Thus

\[
p^4>U.
\]

Applying L026 with `m=3` gives

\[
\boxed{\Omega(n)\le3}
\]

for every state in `L_p(k)`.

Since every shell state is composite and has least prime factor `p`, exactly two possibilities remain:

### Type A — semiprime

\[
\boxed{n=pq,\qquad q\text{ prime},\quad q\ge p.}
\]

### Type B — three-prime state

\[
\boxed{n=p\ell s,\qquad p\le\ell\le s,\quad \ell,s\text{ prime}.}
\]

By L031, for each fixed second prime `ell` there is at most one raw child candidate, hence at most one Type-B state.

Therefore the high least-factor band satisfies the exact count decomposition

\[
\boxed{
|L_p(k)|
=
\#\{q\in W_p(k):q\text{ prime}\}
+
\sum_{\substack{\ell\text{ prime}\\
\ell\ge p}} I_{p,\ell}(k),
}
\]

where

\[
I_{p,\ell}(k)\in\{0,1\}
\]

records whether the unique possible second-factor branch actually produces a prime tail `s>=ell`.

This is more concrete than a generic rough-number count: the nonprime cofactors in this band have been reduced to binary three-prime branches.

---

## 7. Stronger upper band: semiprimes only

L026 already gives the stronger condition

\[
p^3>U
\]

under which

\[
\Omega(n)\le2.
\]

Since shell states are composite, every such state is exactly semiprime:

\[
\boxed{n=pq,\qquad p\le q\text{ prime}.}
\]

Thus the high least-factor region has two exact layers:

1. `p^3>U`: semiprime only;
2. `p^2>=2k` but `p^3<=U`: semiprimes plus binary three-prime branches.

Below `p^2<2k`, child windows may contain multiple candidates and deeper Buchstab recursion is genuinely needed.

---

## 8. L033 — First-order sieve-density weights telescope

Status: `PROVED FINITE ALGEBRAIC IDENTITY`; interpretation is diagnostic, not a rigorous short-interval estimate.

Let

\[
p_1<p_2<\cdots<p_m
\]

be the first `m` primes, and define the independent-sieve survival factor before `p_i` by

\[
V_i
=
\prod_{j<i}\left(1-\frac1{p_j}\right).
\]

Then

\[
V_{i+1}
=V_i\left(1-\frac1{p_i}\right),
\]

so exactly

\[
\boxed{
\frac{V_i}{p_i}
=V_i-V_{i+1}.
}
\]

Summing gives the finite telescope

\[
\boxed{
\sum_{i=1}^m\frac{V_i}{p_i}
=1-V_{m+1}.
}
\]

### Why this matters

The naive independent-density model for “least prime factor exactly `p_i`” therefore uses weights that nearly exhaust total density as more primes are included. It does **not** contain a fixed positive density margin that could trivially force one prime survivor in every square basin.

This blocks a tempting but invalid research shortcut:

> one cannot prove P017 merely by observing that each individual p-rough window has low average density and then summing those densities as if a uniform constant slack must remain.

The remaining leverage, if any, must come from the **structured discrepancy of the special moving square-basin windows**, not from first-order average sieve density alone.

---

## 9. What the audit has achieved

The active P017 route is now substantially smaller.

### Geometry

Solved exactly by L021–L025:

\[
\text{least prime }p
\to
\text{finite cofactor window }W_p(k).
\]

### Arithmetic recursion

Use established Buchstab least-factor decomposition, but with exact child-window transport from L029.

### High-band simplification

For

\[
p^2\ge2k,
\]

recursion is at most one candidate per second prime and `Omega<=3`.

### Forbidden shortcut

Average independent sieve density has no fixed margin by L033.

Therefore the next genuinely new target is very specific:

\[
\boxed{
\text{bound the discrepancy of p-rough survivors in the square-derived moving windows}
}
\]

or show that no such extra discrepancy bound exists.

## 10. Next attacks

1. **Binary three-prime branch geometry.** Derive the exact formula for the unique possible child `s` in each `(p,ell)` high-band branch and look for common-center restrictions across different `ell`.
2. **Short-window sieve bounds.** Compare known upper-bound sieve results with the exact P017 window lengths; record whether current constants are genuinely too weak.
3. **Recursive transport.** Track the boundary-carry bit through two least-factor levels and test whether the nested square-derived endpoints create non-generic correlations.
4. **Counterexample-first discrepancy tests.** Any proposed sign or upper bound for the rough-window discrepancy must be tested over large finite ranges before theorem promotion.
5. **Do not reintroduce Möbius parity under a new name.** If the recursion simply reproduces classical parity obstruction, record that as a negative result and move on.
