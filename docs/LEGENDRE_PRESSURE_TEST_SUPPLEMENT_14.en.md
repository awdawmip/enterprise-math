# Legendre Pressure Test — Supplement 14

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact centered-mirror incidence formulas and a factorized two-slack prime certificate  
Depends on: P017 L042–L045 and canonical L049  
Discipline: **this note does not prove Legendre's conjecture.** Möbius inclusion-exclusion and the Chinese remainder theorem are classical. The project-specific result is the finite obstruction obtained by combining them with the centered-mirror separation theorem.

## 1. Mirror support counts

Let

\[
M=k(k+1),
\]

and let \(A_k\) be the square-free product of the primes \(a\le k\) dividing \(M\). Recall

\[
S_k=\{1\le r<k:\gcd(r,A_k)=1\}.
\]

For \(r\in S_k\), define

\[
P_-(r)=\operatorname{Supp}_{\mathrm{tr}}(M-r),
\qquad
P_+(r)=\operatorname{Supp}_{\mathrm{tr}}(M+r),
\]

and their cardinalities

\[
a_r=|P_-(r)|,
\qquad
b_r=|P_+(r)|.
\]

L043 proves the two support sets are disjoint. If the square basin were prime-free, L044 would force

\[
a_r\ge1,
\qquad
b_r\ge1
\]

for every surviving radius.

Define the first and cross-side moments

\[
J_k=\sum_{r\in S_k}(a_r+b_r),
\qquad
E_k=\sum_{r\in S_k}a_rb_r.
\]

We will evaluate both exactly from small-prime residue data and then extract the **primitive nonnegative slacks** forced by hypothetical prime-free behavior.

---

## 2. Residue-class counter

For \(K\ge0\), \(m\ge1\), and \(1\le\rho<m\), define

\[
\mathcal C(K;m,\rho)
=
\#\{1\le r\le K:r\equiv\rho\pmod m\}.
\]

Then

\[
\boxed{
\mathcal C(K;m,\rho)
=
\begin{cases}
0,&\rho>K,\\
1+\left\lfloor\dfrac{K-\rho}{m}\right\rfloor,&\rho\le K.
\end{cases}
}
\]

---

## 3. L050 — Exact first-moment CRT/Möbius formula

Status: `PROVED / CLASSICAL INCLUSION-EXCLUSION SPECIALIZATION`.

Put \(K=k-1\).

### Surviving radii

Möbius inclusion-exclusion gives

\[
\boxed{
|S_k|
=
\sum_{a\mid A_k}
\mu(a)
\left\lfloor\frac{K}{a}\right\rfloor.
}
\]

### Incidence of one transverse prime

Fix a transverse prime \(p\le k\), so \(p\nmid M\). Let \(N_p(k)\) count surviving radii for which \(p\) divides one mirror state.

For each square-free \(a\mid A_k\), impose \(a\mid r\) together with either

\[
r\equiv M\pmod p
\]

or

\[
r\equiv-M\pmod p.
\]

Since \(\gcd(a,p)=1\), define

\[
 t^+_{a,p}=(Ma^{-1})\bmod p,
\qquad
 t^-_{a,p}=(-Ma^{-1})\bmod p.
\]

Both are nonzero modulo \(p\). The canonical positive representatives modulo \(ap\) are

\[
\rho^+_{a,p}=a t^+_{a,p},
\qquad
\rho^-_{a,p}=a t^-_{a,p}.
\]

Therefore

\[
\boxed{
N_p(k)
=
\sum_{a\mid A_k}
\mu(a)
\left[
\mathcal C(K;ap,\rho^+_{a,p})
+
\mathcal C(K;ap,\rho^-_{a,p})
\right].
}
\]

L043 guarantees that the plus and minus channels never describe the same radius for a transverse prime. Hence

\[
\boxed{
J_k
=
\sum_{\substack{p\le k\\p\nmid M}}N_p(k).
}
\]

### Proof

The formula for \(|S_k|\) is the standard Möbius indicator for \(\gcd(r,A_k)=1\), summed over \(1\le r\le K\). For \(N_p(k)\), apply the same indicator while imposing one mirror congruence; writing \(r=at\) gives the displayed representatives. The last equality is the L045 prime-indexed reindexing. ∎

No state in the square basin is factored by this formula.

---

## 4. L051 — Exact ordered cross-side prime-pair formula

Status: `PROVED / CLASSICAL CRT SPECIALIZATION`.

Fix distinct transverse primes \(p,q\le k\). Let \(N_{p\to q}(k)\) count surviving radii satisfying

\[
p\mid M-r,
\qquad
q\mid M+r.
\]

For each square-free \(a\mid A_k\), write \(r=at\) and set

\[
c_p=(Ma^{-1})\bmod p,
\qquad
c_q=(-Ma^{-1})\bmod q.
\]

The unique canonical solution modulo \(pq\) is

\[
\boxed{
 t_{a;p,q}
=
c_p
+p\left((c_q-c_p)p^{-1}\bmod q\right),
}
\]

with \(1\le t_{a;p,q}<pq\). Put

\[
\rho_{a;p,q}=a t_{a;p,q}.
\]

Then

\[
\boxed{
N_{p\to q}(k)
=
\sum_{a\mid A_k}
\mu(a)
\mathcal C(K;apq,\rho_{a;p,q}).
}
\]

At a fixed radius, the number of ordered choices \((p,q)\) with

\[
p\in P_-(r),
\qquad
q\in P_+(r)
\]

is exactly \(a_rb_r\). Therefore double counting gives

\[
\boxed{
E_k
=
\sum_{\substack{p,q\le k\\p,q\nmid M\\p\ne q}}
N_{p\to q}(k).
}
\]

L043 is exactly what removes the diagonal \(p=q\). ∎

---

## 5. L052 — The two primitive prime-free slacks

Status: `PROVED`.

Define

\[
\boxed{U_k=J_k-2|S_k|}
\]

and

\[
\boxed{V_k=E_k-J_k+|S_k|.}
\]

If the square basin is prime-free, then

\[
\boxed{U_k\ge0,
\qquad
V_k\ge0.}
\]

### Proof

Under prime-free behavior, L044 gives \(a_r,b_r\ge1\) for every \(r\in S_k\). Hence

\[
U_k
=
\sum_{r\in S_k}
\bigl[(a_r-1)+(b_r-1)\bigr]
\ge0.
\]

Also

\[
V_k
=
\sum_{r\in S_k}
(a_r-1)(b_r-1)
\ge0.
\]

Both are sums of explicit nonnegative integers. ∎

This factorization is stronger and conceptually cleaner than treating \(E_k\ge|S_k|\) as an independent primitive inequality. Indeed

\[
\boxed{
E_k-|S_k|=U_k+V_k.
}
\]

Thus the older cross-product certificate \(E_k<|S_k|\) is automatically implied by the failure of at least one primitive slack.

---

## 6. L053 — Factorized two-slack prime certificate

Status: `PROVED`.

If

\[
\boxed{
U_k<0
\quad\text{or}\quad
V_k<0,
}
\]

then

\[
\boxed{
\exists q\text{ prime with }k^2<q<(k+1)^2.
}
\]

### Proof

Contrapositive of L052. ∎

Written directly in terms of the exact moments:

\[
\boxed{
J_k<2|S_k|
\quad\text{or}\quad
E_k<J_k-|S_k|
\Longrightarrow
\exists q\text{ prime in the square basin.}
}
\]

The two channels are genuinely independent.

### `U`-channel example

For \(k=37\),

\[
|S_{37}|=17,
\qquad
J_{37}=33,
\qquad
E_{37}=18.
\]

Hence

\[
U_{37}=-1<0,
\qquad
V_{37}=2\ge0.
\]

The first channel certifies a prime.

### `V`-channel example

For \(k=46\),

\[
|S_{46}|=22,
\qquad
J_{46}=47,
\qquad
E_{46}=18.
\]

Therefore

\[
U_{46}=3\ge0,
\qquad
V_{46}=18-47+22=-7<0.
\]

The second channel certifies a prime even though the first channel fails. Indeed \(2129\) lies in \((46^2,47^2)\).

---

## 7. L054 — Boundary and relation to the raw cross-product certificate

Status: `PROVED`.

The factorization

\[
E_k-|S_k|=U_k+V_k
\]

shows:

1. the raw condition \(E_k<|S_k|\) is sufficient but not fundamental;
2. whenever it fires, at least one of \(U_k<0\) or \(V_k<0\) already fires;
3. the converse fails, so the factorized certificate is strictly stronger.

At \(k=31\),

\[
|S_{31}|=15,
\qquad
J_{31}=30,
\qquad
E_{31}=15,
\]

so

\[
U_{31}=V_{31}=0.
\]

The factorized certificate does not fire, yet \(967\) is prime and lies in \((31^2,32^2)\). Therefore L053 remains a sufficient certificate, not a characterization of prime existence.

---

## 8. Computational pressure test

Status: `COMPUTATIONAL`, not a theorem.

For

\[
3\le k\le1000,
\]

the reference implementation gives:

- \(U_k<0\): 273 roots;
- \(V_k<0\): 594 roots;
- both negative: 140 roots;
- factorized union \(U_k<0\) or \(V_k<0\): **727 roots**;
- the weaker raw cross-product condition \(E_k<|S_k|\): 323 roots.

So the algebraic factorization more than doubles the coverage of the raw two-moment union previously considered. More importantly, it identifies the actual missing structure:

- \(U_k\) measures total excess support beyond one transverse resource per side;
- \(V_k\) measures **simultaneous excess on both sides of the same surviving radius**.

The 271 roots not certified in this bounded range satisfy both nonnegative slack conditions. Any next step should target those residual roots directly rather than adding another arbitrary moment.

---

## 9. Relation to the current P017 routes

The cross-state layers now have distinct jobs:

- L041: exact-support closure after a large support hit;
- L042–L045: centered mirror separation and the basic resource obstruction;
- L046–L048: bounded CRT capacity of a whole side-sign pattern;
- canonical L049: high-band resource occupancy by realized hit-state unions;
- L050–L051: exact additive formulas for first and cross-side mirror incidence;
- L052–L054: factorized nonnegative slacks and the stronger finite prime certificate.

The most promising next object is no longer “another moment.” It is a structural upper bound on one of the two primitive slacks for the roots that survive L053, using exact-support closure, least-factor depth, or correlations among different radii.

---

## 10. Executable validation

`src/enterprise_math/p017_mirror_certificate.py`, `src/enterprise_math/p017_mirror_cross.py`, and their tests check that:

- the L050 formulas for \(|S_k|\), every \(N_p(k)\), and \(J_k\) agree with direct mirror-support counts;
- the L051 ordered-prime-pair CRT formula agrees with direct surviving-radius enumeration;
- the ordered-pair sum equals \(E_k=\sum_r a_rb_r\);
- the identities for \(U_k\), \(V_k\), and \(E_k-|S_k|=U_k+V_k\) hold exactly;
- whenever L053 fires on bounded domains, direct inspection confirms a basin prime;
- \(k=31\), \(37\), and \(46\) lock the stated boundaries;
- the `3<=k<=1000` counts equal 273, 594, 140, 727, and 323.

Finite computation audits implementation and coverage statistics; L050–L054 are proved by exact inclusion-exclusion, CRT, double counting, and the displayed integer factorization.
