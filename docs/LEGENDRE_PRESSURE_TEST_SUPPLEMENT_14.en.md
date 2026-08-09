# Legendre Pressure Test — Supplement 14

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact centered-mirror incidence formulas and factorized aggregate prime certificates  
Depends on: P017 L042–L045 and canonical L049  
Discipline: **this note does not prove Legendre's conjecture.** Möbius inclusion-exclusion and the Chinese remainder theorem are classical. The project-specific results are the finite obstructions obtained by combining them with centered-mirror separation.

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

and

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

Define

\[
J_k=\sum_{r\in S_k}(a_r+b_r),
\qquad
E_k=\sum_{r\in S_k}a_rb_r.
\]

We first evaluate both moments exactly from small-prime residue data, then extract the primitive nonnegative slacks and their sharp aggregate quadratic bound.

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

Put \(K=k-1\). Möbius inclusion-exclusion gives

\[
\boxed{
|S_k|
=
\sum_{a\mid A_k}
\mu(a)
\left\lfloor\frac{K}{a}\right\rfloor.
}
\]

Fix a transverse prime \(p\le k\). Let \(N_p(k)\) count surviving radii for which \(p\) divides one mirror state. For every square-free \(a\mid A_k\), define

\[
 t^+_{a,p}=(Ma^{-1})\bmod p,
\qquad
 t^-_{a,p}=(-Ma^{-1})\bmod p,
\]

and

\[
\rho^+_{a,p}=a t^+_{a,p},
\qquad
\rho^-_{a,p}=a t^-_{a,p}.
\]

Since \(p\nmid M\), both residues are nonzero modulo \(p\). Then

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

L043 guarantees the two mirror channels are disjoint, hence

\[
\boxed{
J_k
=
\sum_{\substack{p\le k\\p\nmid M}}N_p(k).
}
\]

### Proof

Use the standard Möbius indicator

\[
\mathbf1_{\gcd(r,A_k)=1}
=
\sum_{a\mid\gcd(r,A_k)}\mu(a)
\]

and impose one mirror congruence. Writing \(r=at\) produces the displayed residue classes. The last equality is exactly the L045 prime-indexed incidence reindexing. ∎

No square-basin state is factored in these formulas.

---

## 4. L051 — Exact ordered cross-side prime-pair formula

Status: `PROVED / CLASSICAL CRT SPECIALIZATION`.

Fix distinct transverse primes \(p,q\le k\). Let \(N_{p\to q}(k)\) count surviving radii satisfying

\[
p\mid M-r,
\qquad
q\mid M+r.
\]

For every square-free \(a\mid A_k\), write \(r=at\) and set

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

with \(1\le t_{a;p,q}<pq\). Put \(\rho_{a;p,q}=a t_{a;p,q}\). Then

\[
\boxed{
N_{p\to q}(k)
=
\sum_{a\mid A_k}
\mu(a)
\mathcal C(K;apq,\rho_{a;p,q}).
}
\]

At a fixed radius, the number of ordered choices \(p\in P_-(r)\), \(q\in P_+(r)\) is \(a_rb_r\). Therefore

\[
\boxed{
E_k
=
\sum_{\substack{p,q\le k\\p,q\nmid M\\p\ne q}}
N_{p\to q}(k).
}
\]

L043 removes the diagonal \(p=q\). ∎

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

Under prime-free behavior, L044 gives \(a_r,b_r\ge1\). Put

\[
x_r=a_r-1,
\qquad
y_r=b_r-1.
\]

Then \(x_r,y_r\ge0\) and

\[
U_k
=
\sum_{r\in S_k}(x_r+y_r)
\ge0,
\]

while

\[
V_k
=
\sum_{r\in S_k}x_ry_r
\ge0.
\]

Both are sums of explicit nonnegative integers. ∎

Also

\[
\boxed{E_k-|S_k|=U_k+V_k.}
\]

Thus the raw condition \(E_k<|S_k|\) is only a weaker consequence of the primitive slack picture.

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

then there exists a prime \(q\) with

\[
k^2<q<(k+1)^2.
\]

This is the contrapositive of L052. Equivalently,

\[
\boxed{
J_k<2|S_k|
\quad\text{or}\quad
E_k<J_k-|S_k|
\Longrightarrow
\text{prime existence}.
}
\]

The two channels are independent:

- \(k=37\): \(|S|=17,J=33,E=18\), hence \(U=-1<0\) and \(V=2\ge0\);
- \(k=46\): \(|S|=22,J=47,E=18\), hence \(U=3\ge0\) and \(V=-7<0\). Here \(2129\) is a basin prime.

---

## 7. L054 — Aggregate discriminant bound

Status: `PROVED`.

Under prime-free behavior,

\[
\boxed{4V_k\le U_k^2.}
\]

### Proof

Using the nonnegative integers \(x_r,y_r\) from L052,

\[
4x_ry_r\le(x_r+y_r)^2
\]

for every radius. Therefore

\[
4V_k
\le
\sum_{r\in S_k}(x_r+y_r)^2.
\]

Since all \(x_r+y_r\ge0\),

\[
\sum_{r\in S_k}(x_r+y_r)^2
\le
\left(\sum_{r\in S_k}(x_r+y_r)\right)^2
=U_k^2.
\]

Hence the claimed inequality. ∎

Consequently, even when \(U_k,V_k\ge0\), the strict violation

\[
\boxed{4V_k>U_k^2}
\]

is another sufficient certificate of a basin prime.

The bound is the sharp aggregate quadratic envelope available from \(U_k,V_k\) alone: for fixed total \(U\), the product contribution is maximized by concentrating excess on one radius and balancing its two sides as evenly as possible.

---

## 8. L055 — Final three-channel certificate and boundary

Status: `PROVED`.

Combining L052–L054:

\[
\boxed{
U_k<0
\quad\text{or}\quad
V_k<0
\quad\text{or}\quad
4V_k>U_k^2
\Longrightarrow
\exists q\text{ prime with }k^2<q<(k+1)^2.
}
\]

The older raw cross-product test \(E_k<|S_k|\) is redundant because

\[
E_k-|S_k|=U_k+V_k.
\]

At \(k=31\),

\[
|S_{31}|=15,
\qquad
J_{31}=30,
\qquad
E_{31}=15,
\]

so \(U_{31}=V_{31}=0\) and none of the three channels fires. Nevertheless \(967\) is prime in \((31^2,32^2)\). Therefore L055 remains a sufficient certificate, not a characterization.

---

## 9. Computational pressure test

Status: `COMPUTATIONAL`, not a theorem.

For

\[
3\le k\le1000,
\]

the reference implementation gives:

- \(U_k<0\): 273 roots;
- \(V_k<0\): 594 roots;
- both negative: 140 roots;
- union of the two negative-slack channels: 727 roots;
- additional roots certified only by \(4V_k>U_k^2\): 6;
- full L055 three-channel union: **733 roots**;
- weaker raw condition \(E_k<|S_k|\): 323 roots.

The six additional quadratic-envelope examples in this range begin at \(k=128\). The finite statistic is diagnostic only.

This closes the simple information available from the aggregate pair \((U_k,V_k)\): any further progress should use structure discarded by these aggregates, not another arbitrary moment. The 265 roots not certified through \(k=1000\) are the next pressure-test population.

---

## 10. Relation to the current P017 routes

The cross-state layers now have distinct roles:

- L041: exact-support closure after a large support hit;
- L042–L045: centered mirror separation and the basic resource obstruction;
- L046–L048: bounded CRT capacity of a whole side-sign pattern;
- canonical L049: high-band resource occupancy by realized hit-state unions;
- L050–L051: exact additive formulas for first and cross-side mirror incidence;
- L052–L055: primitive nonnegative slacks, their sharp aggregate quadratic envelope, and the finite prime certificate.

The next useful object must explain the residual roots satisfying

\[
U_k\ge0,
\qquad
V_k\ge0,
\qquad
4V_k\le U_k^2.
\]

Candidates should be judged by whether they reduce this residual set through exact-support closure, least-factor depth, or correlations among distinct radii.

---

## 11. Executable validation

`src/enterprise_math/p017_mirror_certificate.py`, `src/enterprise_math/p017_mirror_cross.py`, and their tests check that:

- L050 formulas for \(|S_k|\), every \(N_p(k)\), and \(J_k\) agree with direct mirror-support counts;
- L051 ordered-prime-pair CRT counts agree with direct surviving-radius enumeration;
- the ordered-pair sum equals \(E_k\);
- the identities for \(U_k\), \(V_k\), and \(E_k-|S_k|=U_k+V_k\) hold exactly;
- whenever any L055 channel fires on bounded domains, direct inspection confirms a basin prime;
- \(k=31\), \(37\), and \(46\) lock the stated boundaries;
- the `3<=k<=1000` counts equal 273, 594, 140, 727, 6, 733, and 323.

Finite computation audits implementation and coverage statistics; L050–L055 are proved by exact inclusion-exclusion, CRT, double counting, and the displayed integer inequalities.
